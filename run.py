"""Executa as suítes (oficial, fronteira, EvalPlus) K vezes sobre cada sujeito (solução, referência ou mutante).

Cada execução: processo novo, PYTHONHASHSEED aleatório, ordem dos testes
embaralhada pelo pytest-randomly (semente registrada) e timeout de 10 s por teste.
"""
import csv, json, os, random, shutil, subprocess, sys, xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).parent
K = int(os.environ.get("K", 10))
tasks = {t["id"]: t for t in json.load(open(ROOT / "data/tasks.json"))}
WORK = ROOT / "work"


def test_file(task, pkl):
    lines = ["import copy, math, pickle", "from subject import " + task["entry"] + " as candidate", ""]
    for i, a in enumerate(task["official"], 1):
        lines += [f"def test_oficial_{i:02d}():", f"    {a}", ""]
    for b in task["tests"]:
        args = ", ".join(repr(x) for x in b["args"])
        lines += [f"def test_fronteira_{b['tid']}():",
                  f"    assert candidate({args}) == {b.get('expected_repr', repr(b['expected']))}", ""]
    # comparação no estilo do EvalPlus: floats com tolerância, inclusive dentro de listas/tuplas
    lines += ["def _eq(a, b, atol):",
              "    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):",
              "        return type(a) is type(b) and len(a) == len(b) and all(_eq(x, y, atol) for x, y in zip(a, b))",
              "    if isinstance(b, float) or isinstance(a, float):",
              "        try:",
              "            return math.isclose(a, b, rel_tol=1e-6, abs_tol=max(atol, 1e-6))",
              "        except TypeError:",
              "            return False",
              "    return a == b", "",
              "def test_evalplus():",
              f"    d = pickle.load(open({str(pkl)!r}, 'rb'))",
              "    for inp, exp in zip(d['inputs'], d['expected']):",
              "        assert _eq(candidate(*copy.deepcopy(inp)), exp, d['atol']), inp", ""]
    return "\n".join(lines)


def subjects():
    sol = ROOT / "results/solutions.json"
    for s in (json.load(open(sol)) if sol.exists() else []):
        yield s["sid"], "solucao", s["task"], ROOT / "solutions" / f"{s['sid']}.py"
    for tid, t in tasks.items():
        p = WORK / "refs" / f"{tid.replace('/', '_')}_ref.py"
        p.parent.mkdir(parents=True, exist_ok=True); p.write_text(t["reference"])
        yield f"{tid.replace('/', '_')}_ref", "referencia", tid, p
    for m in json.load(open(ROOT / "results/mutants.json")):
        yield m["mid"], "mutante", m["task"], ROOT / "mutants" / f"{m['mid']}.py"


def run_subject(sub):
    sid, kind, tid, src = sub
    d = WORK / sid
    shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
    shutil.copy(src, d / "subject.py")
    pkl = ROOT / "data" / "evalplus" / f"{tid.replace('/', '_')}.pkl"
    (d / "test_suite.py").write_text(test_file(tasks[tid], pkl))
    rows = []
    rng = random.Random(f"{sid}")
    for k in range(1, K + 1):
        hseed, rseed = rng.randrange(1, 2**32 - 1), rng.randrange(1, 2**31)
        xml = d / f"k{k}.xml"
        env = {**os.environ, "PYTHONHASHSEED": str(hseed), "PYTHONDONTWRITEBYTECODE": "1"}
        subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
                        "-p", "randomly", f"--randomly-seed={rseed}", "--timeout=10",
                        f"--junitxml={xml}", "test_suite.py"],
                       cwd=d, env=env, capture_output=True, text=True, timeout=900)
        root = ET.parse(xml).getroot()
        for tc in root.iter("testcase"):
            failed = any(c.tag in ("failure", "error") for c in tc)
            name = tc.get("name")
            suite = name.split("_")[1]
            rows.append({"subject": sid, "kind": kind, "task": tid, "k": k, "hashseed": hseed,
                         "order_seed": rseed, "test": name, "suite": suite,
                         "result": "falha" if failed else "passa"})
    return rows


if __name__ == "__main__":
    only = set(sys.argv[1:])  # opcional: solucao / referencia / mutante
    subs = [s for s in subjects() if not only or s[1] in only]
    with ThreadPoolExecutor(int(os.environ.get("JOBS", 4))) as ex:
        allrows = [r for rs in ex.map(run_subject, subs) for r in rs]
    with open(ROOT / f"results/execucoes{'_' + '_'.join(sorted(only)) if only else ''}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(allrows[0])); w.writeheader(); w.writerows(allrows)
    print(len(subs), "sujeitos,", len(allrows), "resultados de teste")
