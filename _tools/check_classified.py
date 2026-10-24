"""Validate classified batch outputs: coverage of ids, valid keys, format.

usage: python -I check_classified.py <batches_dir> <classified_dir> [batch_name ...]
"""
import json, os, re, sys, collections

B, C = sys.argv[1], sys.argv[2]
names = sys.argv[3:] or sorted(f[:-4] for f in os.listdir(B) if f.endswith(".tsv"))
keys = {x["key"] for x in json.load(open(os.path.join(os.path.dirname(__file__), "taxonomy.json"), encoding="utf-8"))}
ok_all = True
for n in names:
    bp, cp = os.path.join(B, n + ".tsv"), os.path.join(C, n + ".tsv")
    if not os.path.exists(cp):
        print(n, "MISSING")
        ok_all = False
        continue
    want = [l.split("\t", 1)[0] for l in open(bp, encoding="utf-8") if l.strip()]
    got, bad, kept, drop, badkey = set(), 0, 0, 0, 0
    reasons = collections.Counter()
    for l in open(cp, encoding="utf-8"):
        l = l.rstrip("\n")
        if not l.strip():
            continue
        p = l.split("\t")
        if len(p) < 4:
            bad += 1
            continue
        got.add(re.sub(r"[a-z]$", "", p[0]))
        if p[1] == "DROP":
            drop += 1
            reasons[p[3]] += 1
        elif p[1] in keys:
            kept += 1
        else:
            badkey += 1
    miss = [w for w in want if w not in got]
    flag = bad or badkey or len(miss) > 0
    ok_all &= not flag
    print(f"{n}: in={len(want)} kept={kept} drop={drop} missing={len(miss)} badfmt={bad} badkey={badkey} {dict(reasons)}")
    if miss:
        print("   missing sample:", miss[:8])
print("ALL OK" if ok_all else "ISSUES FOUND")
