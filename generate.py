"""Gera N soluções por tarefa e por modelo, via API, com a temperatura padrão.

Uso:  python3 generate.py claude|openai|deepseek [N]
As chaves vêm de variáveis de ambiente (ANTHROPIC_API_KEY, OPENAI_API_KEY,
DEEPSEEK_API_KEY) ou, se ausentes, são injetadas pelo proxy do ambiente
(segredos de rede); nada é gravado em arquivo. O identificador exato do modelo
de cada provedor vem de CLAUDE_MODEL / OPENAI_MODEL / DEEPSEEK_MODEL.
Cada chamada é independente (sem histórico), com o mesmo prompt de sistema e o
mesmo template. A resposta bruta fica em raw/<modelo>/ e não é sobrescrita.
"""
import json, os, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).parent
SYSTEM = "You write Python code. Answer only with the requested code block."
TEMPLATE = (ROOT / "prompt_template.txt").read_text()
TASKS = json.load(open(ROOT / "data/tasks.json"))
MAX_TOKENS = int(os.environ.get("MAX_TOKENS", 16384))

PROVIDERS = {
    "claude":   {"key": "ANTHROPIC_API_KEY", "model_env": "CLAUDE_MODEL", "default": "claude-opus-5-5",
                 "url": "https://api.anthropic.com/v1/messages"},
    "openai":   {"key": "OPENAI_API_KEY", "model_env": "OPENAI_MODEL", "default": None,
                 "url": "https://api.openai.com/v1/chat/completions"},
    "deepseek": {"key": "DEEPSEEK_API_KEY", "model_env": "DEEPSEEK_MODEL", "default": None,
                 "url": "https://api.deepseek.com/chat/completions"},
}


def call(prov, model, key, prompt):
    if prov == "claude":
        body = {"model": model, "max_tokens": MAX_TOKENS, "system": SYSTEM,
                "messages": [{"role": "user", "content": prompt}]}
        headers = {"anthropic-version": "2023-06-01", **({"x-api-key": key} if key else {})}
    else:
        body = {"model": model, "messages": [{"role": "system", "content": SYSTEM},
                                             {"role": "user", "content": prompt}]}
        if prov == "openai":
            body["max_completion_tokens"] = MAX_TOKENS
        else:
            body["max_tokens"] = MAX_TOKENS
        headers = {"Authorization": f"Bearer {key}"} if key else {}
    req = urllib.request.Request(PROVIDERS[prov]["url"], data=json.dumps(body).encode(),
                                 headers={**headers, "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read())


def text_of(prov, resp):
    if prov == "claude":
        return "".join(b.get("text", "") for b in resp.get("content", []) if b.get("type") == "text")
    return resp["choices"][0]["message"].get("content") or ""


def main():
    prov = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    cfg = PROVIDERS[prov]
    key = os.environ.get(cfg["key"]); model = os.environ.get(cfg["model_env"], cfg["default"])
    if not model:
        sys.exit(f"falta {cfg['model_env']} no ambiente")
    outdir = ROOT / "raw" / prov; outdir.mkdir(parents=True, exist_ok=True)

    def run(task, g):
        out = outdir / f"{task['id'].replace('/', '_')}_g{g}.json"
        if out.exists():
            return
        prompt = TEMPLATE.replace("{task}", task["prompt"].strip("\n"))
        for attempt in range(1, 6):
            t0 = time.time()
            try:
                resp = call(prov, model, key, prompt); err = None; break
            except urllib.error.HTTPError as e:
                resp, err = None, f"HTTP {e.code}: {e.read()[:500]!r}"
                if e.code not in (429, 500, 502, 503, 529):
                    break
            except Exception as e:  # rede
                resp, err = None, repr(e)
            time.sleep(2 ** attempt)
        rec = {"task": task["id"], "generation": g, "provider": prov, "model_requested": model,
               "model_returned": (resp or {}).get("model"), "system": SYSTEM, "prompt": prompt,
               "temperature": "padrão (não enviada)", "max_tokens": MAX_TOKENS,
               "seconds": round(time.time() - t0, 1), "attempts": attempt, "error": err,
               "text": text_of(prov, resp) if resp else None,
               "finish": ((resp or {}).get("stop_reason") or ((resp or {}).get("choices") or [{}])[0].get("finish_reason")), "usage": (resp or {}).get("usage"),
               "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        if err is None:  # só congela respostas bem-sucedidas; erros podem ser refeitos
            out.write_text(json.dumps(rec, indent=2, ensure_ascii=False))
        print(prov, task["id"], g, "ok" if err is None else err, flush=True)

    only = os.environ.get("ONLY")  # ex.: ONLY=3 gera só as 3 primeiras tarefas (teste de custo)
    tasks = TASKS[:int(only)] if only else TASKS
    jobs = [(t, g) for t in tasks for g in range(1, n + 1)]
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(lambda a: run(*a), jobs))


if __name__ == "__main__":
    main()
