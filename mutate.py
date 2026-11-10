"""Mutador baseado no módulo ast, aplicado às soluções de referência.

Operadores de FRONTEIRA:
  ROR  troca estrito <-> inclusivo (<  <->  <=,  >  <->  >=)
  CON  constante inteira usada em comparação deslocada em +1 e -1
  RNG  início/fim de range() deslocado em +1 e -1
Operadores GENÉRICOS (grupo de controle):
  AOR  troca + <-> -
  LCR  troca and <-> or
  NEG  remove um `not`
"""
import ast, json
from pathlib import Path

ROOT = Path(__file__).parent
SWAP = {ast.Lt: ast.LtE, ast.LtE: ast.Lt, ast.Gt: ast.GtE, ast.GtE: ast.Gt}
SYM = {ast.Lt: "<", ast.LtE: "<=", ast.Gt: ">", ast.GtE: ">="}
GROUP = {"ROR": "fronteira", "CON": "fronteira", "RNG": "fronteira",
         "AOR": "generico", "LCR": "generico", "NEG": "generico"}


def sites(tree):
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare):
            for i, op in enumerate(node.ops):
                if type(op) in SWAP:
                    out.append(("ROR", node, i, None))
            for j, c in enumerate([node.left] + node.comparators):
                if isinstance(c, ast.Constant) and type(c.value) is int:
                    out += [("CON", node, j, +1), ("CON", node, j, -1)]
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "range":
            for j in range(min(2, len(node.args))):
                out += [("RNG", node, j, +1), ("RNG", node, j, -1)]
        if isinstance(node, (ast.BinOp, ast.AugAssign)) and isinstance(node.op, (ast.Add, ast.Sub)):
            out.append(("AOR", node, 0, None))
        if isinstance(node, ast.BoolOp):
            out.append(("LCR", node, 0, None))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            out.append(("NEG", node, 0, None))
    return out


class _Unnot(ast.NodeTransformer):
    def __init__(self, target): self.target = target
    def visit_UnaryOp(self, node):
        self.generic_visit(node)
        return node.operand if node is self.target else node


def apply(src, k):
    tree = ast.parse(src)
    op, node, i, d = sites(tree)[k]
    line = node.lineno
    if op == "ROR":
        old = type(node.ops[i]); node.ops[i] = SWAP[old]()
        desc = f"{SYM[old]} -> {SYM[SWAP[old]]}"
    elif op == "CON":
        c = ([node.left] + node.comparators)[i]
        desc = f"constante {c.value} -> {c.value + d}"; c.value += d
    elif op == "RNG":
        a = node.args[i]
        node.args[i] = ast.BinOp(a, ast.Add() if d > 0 else ast.Sub(), ast.Constant(1))
        desc = f"range arg{i} {'+' if d > 0 else '-'}1"
    elif op == "AOR":
        add = isinstance(node.op, ast.Add)
        node.op = ast.Sub() if add else ast.Add(); desc = "+ -> -" if add else "- -> +"
    elif op == "LCR":
        a = isinstance(node.op, ast.And)
        node.op = ast.Or() if a else ast.And(); desc = "and -> or" if a else "or -> and"
    else:
        tree = _Unnot(node).visit(tree); desc = "remove not"
    return ast.unparse(tree), f"{op}: {desc} (linha {line})"


if __name__ == "__main__":
    tasks = json.load(open(ROOT / "data/tasks.json"))
    mdir = ROOT / "mutants"; mdir.mkdir(exist_ok=True)
    (ROOT / "results").mkdir(exist_ok=True)
    meta, seen = [], set()
    for t in tasks:
        ref_norm = ast.unparse(ast.parse(t["reference"]))
        for k in range(len(sites(ast.parse(t["reference"])))):
            code, desc = apply(t["reference"], k)
            if code == ref_norm or (t["id"], code) in seen:
                continue  # mutante idêntico à referência ou duplicado
            seen.add((t["id"], code))
            mid = f"{t['id'].replace('/', '_')}_m{len([m for m in meta if m['task'] == t['id']]) + 1}"
            (mdir / f"{mid}.py").write_text(code)
            op = desc.split(":")[0]
            meta.append({"mid": mid, "task": t["id"], "op": op, "grupo": GROUP[op], "desc": desc})
    json.dump(meta, open(ROOT / "results/mutants.json", "w"), indent=2, ensure_ascii=False)
    from collections import Counter
    print(len(meta), "mutantes", Counter(m["grupo"] for m in meta), Counter(m["op"] for m in meta))
