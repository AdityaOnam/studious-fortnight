"""Remove cross-file exact-duplicate questions from curated files; export dropped questions for audit.
usage: python -I final_cleanup.py <root>"""
import glob, json, os, re, sys
ROOT = sys.argv[1]; W = os.path.join(ROOT, "_work")
T = json.load(open(os.path.join(os.path.dirname(__file__), "taxonomy.json"), encoding="utf-8"))
prov = json.load(open(os.path.join(W, "prov.json"), encoding="utf-8"))
seen = {}; removed = 0
for t in T:
    k = t["key"]
    files = sorted(glob.glob(os.path.join(W, "curated", k + ".md")) + glob.glob(os.path.join(W, "curated", k + ".p[0-9]*.md")))
    for f in files:
        out = []
        for ln in open(f, encoding="utf-8").read().split("\n"):
            m = re.match(r"^-\s*\[[EMH]\]\s*(.+?)\s*\{", ln)
            if m:
                n = re.sub(r"[^a-z0-9]+", " ", m.group(1).lower()).strip()
                if n in seen and seen[n] != k:
                    removed += 1; continue
                seen.setdefault(n, k)
            out.append(ln)
        open(f, "w", encoding="utf-8").write("\n".join(out))
print("cross-file exact duplicates removed:", removed)
# dropped audit
n = 0
with open(os.path.join(ROOT, "_meta", "dropped_questions.jsonl"), "w", encoding="utf-8") as o:
    for f in glob.glob(os.path.join(W, "curated", "*.dropped.txt")):
        k = os.path.basename(f).replace(".dropped.txt", "")
        pool = {}
        for l in open(os.path.join(W, "pools", k + ".tsv"), encoding="utf-8"):
            p = l.rstrip("\n").split("\t")
            if len(p) >= 3: pool[p[0]] = p[2]
        for l in open(f, encoding="utf-8"):
            p = l.rstrip("\n").split("\t")
            if p[0].strip() in pool:
                n += 1
                o.write(json.dumps({"ref": p[0].strip(), "pool": k, "reason": p[1] if len(p) > 1 else "", "q": pool[p[0].strip()], "sources": prov.get(p[0].strip(), {}).get("srcs", [])[:2]}, ensure_ascii=False) + "\n")
print("dropped questions exported:", n)
