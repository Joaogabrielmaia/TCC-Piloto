"""Extrai e congela o código de cada resposta (sem correção manual)."""
import ast, hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).parent
tasks = {t["id"]: t for t in json.load(open(ROOT / "data/tasks.json"))}
(ROOT / "solutions").mkdir(exist_ok=True)
rows = []
for f in sorted((ROOT / "raw").glob("*/*.json")):
    r = json.loads(f.read_text())
    text = r["text"] or ""
    m = re.findall(r"```(?:python|py)?\s*\n(.*?)```", text, re.S)
    code = m[0] if m else text
    entry = tasks[r["task"]]["entry"]
    status = "ok"
    try:
        tree = ast.parse(code)
        if not any(isinstance(n, ast.FunctionDef) and n.name == entry for n in tree.body):
            status = "assinatura_ausente"
    except SyntaxError:
        status = "erro_sintaxe"
    sid = f"{r['provider']}_{r['task'].replace('/', '_')}_g{r['generation']}"
    (ROOT / "solutions" / f"{sid}.py").write_text(code)
    rows.append({"sid": sid, "provider": r["provider"], "model": r["model_returned"] or r["model_requested"],
                 "task": r["task"], "generation": r["generation"], "status": status,
                 "sha256": hashlib.sha256(code.encode()).hexdigest(), "code_block_found": bool(m),
                 "seconds": r["seconds"], "usage": r["usage"]})
json.dump(rows, open(ROOT / "results/solutions.json", "w"), indent=2)
from collections import Counter
print(len(rows), "soluções", Counter((x["provider"], x["status"]) for x in rows))
