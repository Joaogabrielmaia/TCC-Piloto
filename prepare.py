"""Prepara as 30 tarefas: enunciado (formato EvalPlus), referência, suíte oficial e EvalPlus.

- Enunciado: o `prompt` do HumanEval+ / MBPP+ (o do MBPP+ traz um assert de exemplo).
- Referência: a `canonical_solution` do EvalPlus (corrige erros das originais).
- Suíte oficial: asserts originais do HumanEval (check) e do MBPP sanitizado (test_list).
- EvalPlus: base_input + plus_input, saídas esperadas calculadas pela referência.
"""
import ast, copy, gzip, json, pickle
from pathlib import Path
from testes_fronteira import TASKS

D = Path(__file__).parent / "data"
he = {t["task_id"]: t for t in (json.loads(l) for l in gzip.open(D / "HumanEval.jsonl.gz"))}
hep = {t["task_id"]: t for t in (json.loads(l) for l in gzip.open(D / "HumanEvalPlus.jsonl.gz"))}
mbpp = {t["task_id"]: t for t in json.load(open(D / "sanitized-mbpp.json"))}
mbp = {t["task_id"]: t for t in (json.loads(l) for l in gzip.open(D / "MbppPlus.jsonl.gz"))}


def he_official(test_src, entry):
    mod = ast.parse(test_src)
    check = next(n for n in mod.body if isinstance(n, ast.FunctionDef) and n.name == "check")
    return [ast.unparse(s) for s in check.body if isinstance(s, ast.Assert)]


out = []
(D / "evalplus").mkdir(exist_ok=True)
for t in TASKS:
    tid = t["id"]
    bench = "HumanEval" if tid.startswith("HumanEval") else "MBPP"
    if bench == "HumanEval":
        plus = hep[tid]
        official = he_official(he[tid]["test"], t["entry"])
        reference = plus["prompt"] + plus["canonical_solution"]
    else:
        plus = mbp[tid]
        official = [a.replace(t["entry"] + "(", "candidate(", 1) for a in mbpp[int(tid.split("/")[1])]["test_list"]]
        reference = plus["canonical_solution"]
    inputs = plus["base_input"] + plus["plus_input"]
    ns = {}; exec(reference, ns); f = ns[t["entry"]]
    expected = [f(*copy.deepcopy(i)) for i in inputs]
    pickle.dump({"inputs": inputs, "expected": expected, "atol": plus.get("atol", 0)},
                open(D / "evalplus" / f"{tid.replace('/', '_')}.pkl", "wb"))
    tests = [{**b, "expected_repr": repr(b["expected"])} for b in t["tests"]]  # preserva tuplas
    out.append({**t, "tests": tests, "bench": bench, "prompt": plus["prompt"], "reference": reference,
                "official": official, "n_evalplus": len(inputs)})
    print(f"{tid:14s} oficiais={len(official):3d} fronteira={len(t['tests'])} evalplus={len(inputs)}")
json.dump(out, open(D / "tasks.json", "w"), indent=2, ensure_ascii=False)
