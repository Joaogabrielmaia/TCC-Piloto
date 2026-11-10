"""Métricas das soluções geradas: FND por suíte, instabilidade, custo, bootstrap por tarefa."""
import csv, json, math, random
from collections import defaultdict
from pathlib import Path
from scipy.stats import binomtest

ROOT = Path(__file__).parent
sols = {s["sid"]: s for s in json.load(open(ROOT / "results/solutions.json"))}
tasks = {t["id"]: t for t in json.load(open(ROOT / "data/tasks.json"))}
res = defaultdict(lambda: defaultdict(list))
for r in csv.DictReader(open(ROOT / "results/execucoes_solucao.csv")):
    res[r["subject"]][r["test"]].append(r["result"])
suite = lambda name: name.split("_")[1]

per = []
for sid, tests in res.items():
    st = {t: ("falha" if set(v) == {"falha"} else "passa" if set(v) == {"passa"} else "instavel") for t, v in tests.items()}
    s = sols[sid]
    def passes(x): return all(v == "passa" for t, v in st.items() if suite(t) == x)
    fr_fail = sorted(t for t, v in st.items() if suite(t) == "fronteira" and v == "falha")
    per.append({"sid": sid, "modelo": s["provider"], "tarefa": s["task"], "bench": tasks[s["task"]]["bench"],
                "sha": s["sha256"][:10], "passa_oficial": passes("oficial"), "passa_evalplus": passes("evalplus"),
                "passa_fronteira": passes("fronteira"), "falhas_fronteira": " ".join(fr_fail),
                "instavel": any(v == "instavel" for v in st.values()),
                "n_execucoes": sum(len(v) for v in tests.values())})

def fnd(rows, S):
    den = [p for p in rows if p[f"passa_{S}"] and not p["instavel"]]
    num = [p for p in den if not p["passa_fronteira"]]
    return len(num), len(den)

def boot(rows, S, B=10000, seed=20261109):
    by = defaultdict(list)
    for p in rows: by[p["tarefa"]].append(p)
    ts = sorted(by); rng = random.Random(seed); vals = []
    for _ in range(B):
        samp = [p for t in (rng.choice(ts) for _ in ts) for p in by[t]]
        k, n = fnd(samp, S)
        if n: vals.append(k / n)
    vals.sort()
    return round(100 * vals[int(.025 * len(vals))], 1), round(100 * vals[int(.975 * len(vals)) - 1], 1)

def wilson_up(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n
    return round(100 * ((p + z * z / (2 * n)) / d + z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d), 1)

out = {"solucoes": len(per), "instaveis": [p["sid"] for p in per if p["instavel"]], "fnd": {}}
groups = [("todos", per)] + [(m, [p for p in per if p["modelo"] == m]) for m in ("claude", "openai", "deepseek")] \
       + [(b, [p for p in per if p["bench"] == b]) for b in ("HumanEval", "MBPP")]
for g, rows in groups:
    d = {"n": len(rows), "passa_oficial": sum(p["passa_oficial"] for p in rows),
         "passa_evalplus": sum(p["passa_evalplus"] for p in rows),
         "passa_fronteira": sum(p["passa_fronteira"] for p in rows)}
    for S in ("oficial", "evalplus"):
        k, n = fnd(rows, S)
        tarefas = len({p["tarefa"] for p in rows if p[f"passa_{S}"] and not p["passa_fronteira"] and not p["instavel"]})
        d[f"fnd_{S}"] = {"k": k, "n": n, "pct": round(100 * k / n, 1) if n else None,
                         "ic95_bootstrap_tarefa": boot(rows, S) if k else None,
                         "tarefas_afetadas": tarefas,
                         "wilson_sup_por_tarefa": wilson_up(0, len({p['tarefa'] for p in rows})) if k == 0 else None}
    out["fnd"][g] = d
# McNemar entre suítes: passa oficial e falha fronteira vs passa evalplus e falha fronteira (por solução)
b = sum(p["passa_oficial"] and not p["passa_evalplus"] for p in per)
c = sum(p["passa_evalplus"] and not p["passa_oficial"] for p in per)
out["mcnemar_oficial_vs_evalplus_aprovacao"] = {"so_oficial": b, "so_evalplus": c,
                                                 "p": round(binomtest(b, b + c).pvalue, 4) if b + c else None}
out["execucoes_totais"] = sum(p["n_execucoes"] for p in per)
json.dump(out, open(ROOT / "results/metricas.json", "w"), indent=2, ensure_ascii=False)
with open(ROOT / "results/por_solucao.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(per[0])); w.writeheader(); w.writerows(per)
print(json.dumps(out, indent=1, ensure_ascii=False))
