"""Extract problem statements (PRB-n blocks, no solutions) from the Deep Learning Interviews book text.

usage: python -I dli_extract.py <book.txt> <out.tsv>
Each block runs from 'PRB-n' to the next PRB/SOL marker or chapter heading; whitespace is collapsed.
"""
import re, sys

lines = open(sys.argv[1], encoding="utf-8", errors="replace").read().splitlines()
START = re.compile(r"^\s*PRB-(\d+)\s+CH\.PRB-\s*([\d.]+)")
STOP = re.compile(r"^\s*(PRB-\d+|SOL-\d+|\d+\.\d+\s+Solutions|Chapter\s+\d+|CHAPTER\s+\d+|\d+\.\d+(\.\d+)?\s+[A-Z][A-Za-z ,\-]+$)")
out, cur = [], None
for ln in lines:
    m = START.match(ln)
    if m:
        if cur: out.append(cur)
        cur = [m.group(1), m.group(2), []]
        continue
    if cur is not None:
        if STOP.match(ln) or "\f" in ln:
            if STOP.match(ln):
                out.append(cur); cur = None; continue
        cur[2].append(ln.strip())
if cur: out.append(cur)
seen = set()
with open(sys.argv[2], "w", encoding="utf-8") as f:
    for n, ch, body in out:
        if n in seen: continue
        seen.add(n)
        t = re.sub(r"\s+", " ", " ".join(body)).strip()
        f.write(f"B{int(n):04d}\t{ch}\t{t}\n")
print(len(seen), "problems")
