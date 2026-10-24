"""Lint the final corpus. usage: python -I lint.py <root>"""
import glob, os, re, sys, collections, json
ROOT = sys.argv[1]
dirs = [d for d in sorted(os.listdir(ROOT)) if re.match(r"\d\d_", d) and d != "00_START_HERE"]
errs, warns = [], []
ids = set(); total = 0; files = 0
allq = collections.defaultdict(list)
LEAK = re.compile(r"(^|\s)(answer\s*:|hint\s*:|solution\s*:|ans\s*:|\(answer)", re.I)
tok = []
for d in dirs:
    for f in sorted(glob.glob(os.path.join(ROOT, d, "*.md"))):
        files += 1
        txt = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, ROOT)
        m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
        if not m: errs.append(f"{rel}: no front-matter"); continue
        fm = dict(l.split(": ", 1) for l in m.group(1).splitlines() if ": " in l)
        for k in ("domain", "topic", "title", "tags", "count"):
            if k not in fm: errs.append(f"{rel}: missing {k}")
        qs = 0; sec = None; seccount = collections.Counter()
        for ln in txt.splitlines():
            if ln.startswith("## "): sec = ln; continue
            mm = re.match(r"^- \[([A-Z]+\d*-\d{3})\] (.+)$", ln)
            if ln.startswith("- "):
                if not mm: errs.append(f"{rel}: bad line {ln[:70]}"); continue
                qid, q = mm.groups()
                qs += 1; total += 1
                seccount[sec] += 1
                if qid in ids: errs.append(f"dup id {qid}")
                ids.add(qid)
                if len(q) > 260: warns.append(f"{rel}: long ({len(q)}) {qid}")
                if len(q) < 15: errs.append(f"{rel}: too short {qid}: {q}")
                if LEAK.search(q): errs.append(f"{rel}: answer-leak? {qid}: {q[:80]}")
                if "{" in q and "}" in q: warns.append(f"{rel}: braces {qid}")
                allq[re.sub(r"[^a-z0-9]+", " ", q.lower()).strip()].append(qid)
        if str(qs) != fm.get("count"): errs.append(f"{rel}: count {fm.get('count')} != {qs}")
        for s, c in seccount.items():
            if c > 30: warns.append(f"{rel}: section '{s}' has {c}")
        if qs > 175: warns.append(f"{rel}: {qs} questions")
        tok.append((len(txt) // 4, rel, qs))
dups = {k: v for k, v in allq.items() if len(v) > 1}
print("files", files, "questions", total, "unique ids", len(ids))
print("exact duplicate texts across corpus:", len(dups))
for k, v in list(dups.items())[:10]: print("   ", v, k[:70])
tok.sort()
print("tokens/file min %d median %d max %d" % (tok[0][0], tok[len(tok)//2][0], tok[-1][0]))
print("smallest:", tok[:3]); print("largest:", tok[-3:])
print("ERRORS", len(errs)); [print("  E", e) for e in errs[:30]]
print("WARNINGS", len(warns)); [print("  W", w) for w in warns[:20]]
