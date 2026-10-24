"""Report curation status per KEY: files present, coverage of pool refs, malformed lines.
usage: python -I check_curated.py <work_dir>"""
import json, os, re, sys, glob
W = sys.argv[1]
T = json.load(open(os.path.join(os.path.dirname(__file__), "taxonomy.json"), encoding="utf-8"))
LINE = re.compile(r"^-\s*\[([EMH])\]\s*(.+?)\s*\{([^}]*)\}\s*$")
todo, done = [], []
for t in T:
    k = t["key"]
    pool = [l.split("\t")[0] for l in open(os.path.join(W, "pools", k + ".tsv"), encoding="utf-8") if l.strip()]
    files = glob.glob(os.path.join(W, "curated", k + ".md")) + glob.glob(os.path.join(W, "curated", k + ".p[0-9]*.md"))
    if not files:
        todo.append((k, "NOFILE")); continue
    refs, nq, bad, gen = set(), 0, 0, 0
    for f in files:
        for ln in open(f, encoding="utf-8"):
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.startswith("## "): continue
            m = LINE.match(ln)
            if not m: bad += 1; continue
            nq += 1
            rs = [r.strip() for r in m.group(3).split(",") if r.strip()]
            if rs == ["GEN"]: gen += 1
            refs.update(rs)
    dp = os.path.join(W, "curated", k + ".dropped.txt")
    dropped = set()
    if os.path.exists(dp):
        dropped = {l.split("\t")[0].strip() for l in open(dp, encoding="utf-8") if l.strip()}
    missing = [r for r in pool if r not in refs and r not in dropped]
    pct = 100 * (len(pool) - len(missing)) / max(1, len(pool))
    status = "OK" if not missing and not bad and nq > 20 else "INCOMPLETE"
    (done if status == "OK" else todo).append((k, f"{status} q={nq} gen={gen} missing={len(missing)}/{len(pool)} bad={bad} files={len(files)}"))
print("DONE", len(done)); print("TODO", len(todo))
for k, s in todo: print("  ", k, s)
