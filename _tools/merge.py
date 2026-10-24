"""Merge classified + derived questions into per-topic pools.

usage: python -I merge.py <work_dir>
Reads  _work/all_items (batches/all_items.jsonl), _work/classified/*.tsv, _work/derived/*.tsv
Writes _work/pools/<KEY>.tsv  (ref \t D \t question) and _work/pools/_summary.txt
"""
import json, os, re, sys, collections

W = sys.argv[1]
T = json.load(open(os.path.join(os.path.dirname(__file__), "taxonomy.json"), encoding="utf-8"))
KEYS = [t["key"] for t in T]
items = {}
for l in open(os.path.join(W, "batches", "all_items.jsonl"), encoding="utf-8"):
    r = json.loads(l)
    items[r["id"]] = r

pools = collections.defaultdict(list)
prov = {}
cdir = os.path.join(W, "classified")
for f in sorted(os.listdir(cdir)):
    if not f.endswith(".tsv"):
        continue
    for l in open(os.path.join(cdir, f), encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if len(p) < 4 or p[1] == "DROP" or p[1] not in KEYS:
            continue
        rid, key, d, q = p[0], p[1], p[2], p[3].strip()
        base = re.sub(r"[a-z]$", "", rid)
        if base not in items or len(q) < 12:
            continue
        pools[key].append((rid, d, q))
        prov[rid] = {"srcs": items[base]["srcs"][:4], "derived": False}

ddir = os.path.join(W, "derived")
n = 0
for f in sorted(os.listdir(ddir)):
    if not f.endswith(".tsv"):
        continue
    for l in open(os.path.join(ddir, f), encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if len(p) < 3 or p[0] not in KEYS or len(p[2].strip()) < 12:
            continue
        n += 1
        rid = f"D{n:05d}"
        pools[p[0]].append((rid, p[1] if p[1] in "EMH" else "M", p[2].strip()))
        prov[rid] = {"srcs": [p[3] if len(p) > 3 else f], "derived": True}

pd = os.path.join(W, "pools")
os.makedirs(pd, exist_ok=True)
with open(os.path.join(W, "prov.json"), "w", encoding="utf-8") as f:
    json.dump(prov, f, ensure_ascii=False)
lines = []
for k in KEYS:
    lst = pools.get(k, [])
    with open(os.path.join(pd, k + ".tsv"), "w", encoding="utf-8") as f:
        for rid, d, q in lst:
            f.write(f"{rid}\t{d}\t{q}\n")
    lines.append(f"{k}\t{len(lst)}")
open(os.path.join(pd, "_summary.txt"), "w").write("\n".join(lines))
print("\n".join(lines))
print("TOTAL", sum(len(v) for v in pools.values()))
