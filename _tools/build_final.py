"""Render curated topic files into the final RAG corpus + provenance metadata.

usage: python -I build_final.py <root>
Reads  <root>/_work/curated/<KEY>[.pN].md, <root>/_work/prov.json, <root>/_work/pools/*.tsv
Writes <root>/<dir>/<file>.md (or _partN), <root>/_meta/questions.jsonl, <root>/_meta/unplaced_refs.jsonl
"""
import json, os, re, sys, glob, collections

ROOT = sys.argv[1]
W = os.path.join(ROOT, "_work")
T = json.load(open(os.path.join(os.path.dirname(__file__), "taxonomy.json"), encoding="utf-8"))
prov = json.load(open(os.path.join(W, "prov.json"), encoding="utf-8"))
LINE = re.compile(r"^-\s*\[([EMH])\]\s*(.+?)\s*\{([^}]*)\}\s*$")

os.makedirs(os.path.join(ROOT, "_meta"), exist_ok=True)
meta_out = open(os.path.join(ROOT, "_meta", "questions.jsonl"), "w", encoding="utf-8")
placed_refs = set()
summary = []
problems = []

for t in T:
    key = t["key"]
    files = sorted(glob.glob(os.path.join(W, "curated", key + ".md"))) + sorted(
        glob.glob(os.path.join(W, "curated", key + ".p[0-9]*.md")), key=lambda p: int(re.search(r"\.p(\d+)\.md$", p).group(1)))
    if not files:
        problems.append(f"{key}: no curated file")
        continue
    multi = len(files) > 1
    counter = 0
    seen_q = set()
    for pi, fp in enumerate(files, 1):
        sections = []  # (title, [(d, q, refs)])
        for ln in open(fp, encoding="utf-8"):
            ln = ln.rstrip("\n")
            if not ln.strip():
                continue
            if ln.startswith("## "):
                sections.append((ln[3:].strip(), []))
                continue
            m = LINE.match(ln)
            if not m or not sections:
                problems.append(f"{os.path.basename(fp)}: bad line: {ln[:80]}")
                continue
            d, q, refs = m.group(1), re.sub(r"\s+", " ", m.group(2)).strip(), [r.strip() for r in m.group(3).split(",") if r.strip()]
            nk = re.sub(r"[^a-z0-9]+", " ", q.lower()).strip()
            if nk in seen_q:
                continue
            seen_q.add(nk)
            sections[-1][1].append((d, q, refs))
        sections = [(s, qs) for s, qs in sections if qs]
        n = sum(len(qs) for _, qs in sections)
        fname = t["file"] if not multi else t["file"].replace(".md", f"_part{pi}.md")
        out = [
            "---",
            f"domain: {t['domain']}",
            f"topic: {t['file'][3:-3]}",
            f"title: {t['title']}",
            f"tags: [{', '.join(t['tags'])}]",
            f"count: {n}",
        ]
        if multi:
            out.append(f"part: {pi}/{len(files)}")
        out += ["---", f"# {t['title']}" + (f" (part {pi})" if multi else ""), ""]
        for title, qs in sections:
            out.append(f"## {title}")
            for d, q, refs in qs:
                counter += 1
                qid = f"{key}-{counter:03d}"
                out.append(f"- [{qid}] {q}")
                srcs = []
                for r in refs:
                    placed_refs.add(r)
                    if r in prov:
                        srcs += prov[r]["srcs"][:2]
                meta_out.write(json.dumps({
                    "id": qid, "file": f"{t['dir']}/{fname}", "section": title, "difficulty": d, "q": q,
                    "generated": refs == ["GEN"] or all(r == "GEN" for r in refs),
                    "refs": refs, "sources": sorted(set(srcs))[:6]}, ensure_ascii=False) + "\n")
            out.append("")
        fp_out = os.path.join(ROOT, t["dir"], fname)
        open(fp_out, "w", encoding="utf-8", newline="\n").write("\n".join(out).rstrip() + "\n")
        summary.append((t["dir"] + "/" + fname, t["title"], n))

meta_out.close()

# audit: pool refs that never appear in any curated file
unplaced = []
for fp in glob.glob(os.path.join(W, "pools", "*.tsv")):
    for l in open(fp, encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if len(p) >= 3 and p[0] not in placed_refs:
            unplaced.append({"ref": p[0], "q": p[2], "pool": os.path.basename(fp)[:-4], "sources": prov.get(p[0], {}).get("srcs", [])[:2]})
with open(os.path.join(ROOT, "_meta", "unplaced_refs.jsonl"), "w", encoding="utf-8") as f:
    for u in unplaced:
        f.write(json.dumps(u, ensure_ascii=False) + "\n")

json.dump(summary, open(os.path.join(W, "final_summary.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("files", len(summary), "questions", sum(n for _, _, n in summary), "unplaced refs", len(unplaced))
for p in problems[:40]:
    print("PROBLEM", p)
print("problems", len(problems))
