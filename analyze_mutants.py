"""Mutation score de cada suíte por grupo de operador (fronteira vs genérico)."""
import csv, json, math
from collections import defaultdict
from pathlib import Path
from scipy.stats import binomtest

ROOT = Path(__file__).parent
meta = {m["mid"]: m for m in json.load(open(ROOT / "results/mutants.json"))}
tasks = {t["id"]: t for t in json.load(open(ROOT / "data/tasks.json"))}
res = defaultdict(lambda: defaultdict(list))  # mid -> test -> [resultados]
for r in csv.DictReader(open(ROOT / "results/execucoes_mutante_referencia.csv")):
    if r["kind"] == "mutante":
        res[r["subject"]][r["test"]].append(r["result"])


def wilson(k, n, z=1.96):
    if n == 0: return (None, None)
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return round(100 * (c - h), 1), round(100 * (c + h), 1)


EQUIV = json.load(open(ROOT / "data/mutantes_equivalentes.json"))  # inspeção manual
rows, instaveis = [], []
for mid, tests in res.items():
    st = {t: ("falha" if set(v) == {"falha"} else "passa" if set(v) == {"passa"} else "instavel") for t, v in tests.items()}
    if "instavel" in st.values(): instaveis.append(mid)
    suite = lambda name: name.split("_")[1]
    k = {s: any(v == "falha" for t, v in st.items() if suite(t) == s) for s in ("oficial", "fronteira", "evalplus")}
    rows.append({**meta[mid], "mata_oficial": k["oficial"], "mata_fronteira": k["fronteira"],
                 "mata_evalplus": k["evalplus"], "mata_ofi_front": k["oficial"] or k["fronteira"],
                 "sobrevive_todas": not any(k.values())})

out = {"mutantes": len(rows), "instaveis": instaveis, "por_grupo": {}}
out["equivalentes"] = len(EQUIV)
rows = [r for r in rows if r["mid"] not in EQUIV]  # scores sobre mutantes não equivalentes
for g in ("fronteira", "generico", "todos"):
    sel = [r for r in rows if g == "todos" or r["grupo"] == g]
    d = {"n": len(sel)}
    for s in ("mata_oficial", "mata_fronteira", "mata_ofi_front", "mata_evalplus"):
        k = sum(r[s] for r in sel); d[s] = {"mortos": k, "score": round(100 * k / len(sel), 1), "ic95": wilson(k, len(sel))}
    b = sum(r["mata_ofi_front"] and not r["mata_oficial"] for r in sel)
    d["so_fronteira_mata_alem_oficial"] = b
    b2 = sum(r["mata_ofi_front"] and not r["mata_evalplus"] for r in sel)
    c2 = sum(r["mata_evalplus"] and not r["mata_ofi_front"] for r in sel)
    d["mcnemar_ofifront_vs_evalplus"] = {"so_ofifront": b2, "so_evalplus": c2,
                                         "p": round(binomtest(b2, b2 + c2).pvalue, 4) if b2 + c2 else None}
    d["sobrevivem_todas"] = sum(r["sobrevive_todas"] for r in sel)
    out["por_grupo"][g] = d
# custo: testes executados por mutante morto
n_tests = {tid: {"oficial": len(t["official"]), "fronteira": len(t["tests"]), "evalplus": t["n_evalplus"]} for tid, t in tasks.items()}
for s, col in (("oficial", "mata_oficial"), ("fronteira", "mata_fronteira"), ("evalplus", "mata_evalplus")):
    tot = sum(n_tests[r["task"]][s] for r in rows); k = sum(r[col] for r in rows)
    out.setdefault("custo_testes_por_morto", {})[s] = round(tot / k, 1) if k else None
out["testes_por_tarefa_medios"] = {s: round(sum(v[s] for v in n_tests.values()) / len(n_tests), 1) for s in ("oficial", "fronteira", "evalplus")}
json.dump(out, open(ROOT / "results/metricas_mutantes.json", "w"), indent=2, ensure_ascii=False)
with open(ROOT / "results/mutantes_resultado.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(json.dumps(out, indent=1, ensure_ascii=False))
