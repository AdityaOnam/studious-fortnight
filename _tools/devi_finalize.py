"""Merge curated devinterview additions into the curated topic files without renumbering existing IDs.

usage: python -I devi_finalize.py <root>
- <KEY>.add.md   -> appended to the end of the KEY's last curated file (existing IDs keep their numbers).
- <KEY>.pN.md    -> new part files are picked up by build_final.py as they are.
- Adds provenance (prov.json) for every new ref, and writes _meta/devi_unused.jsonl listing harvested
  devinterview items that were not placed (duplicates of existing questions, off-scope or trivial).
Idempotent: an .add.md whose lines are already present in the target file is skipped.
"""
import glob, json, os, re, sys

ROOT = sys.argv[1]
W = os.path.join(ROOT, "_work")
C = os.path.join(W, "curated")
REF = re.compile(r"\{([^}]*)\}\s*$")


def parts(key):
    fs = glob.glob(os.path.join(C, key + ".md")) + glob.glob(os.path.join(C, key + ".p[0-9]*.md"))
    return sorted(fs, key=lambda p: 0 if p.endswith(key + ".md") else int(re.search(r"\.p(\d+)\.md$", p).group(1)))


for add in sorted(glob.glob(os.path.join(C, "*.add.md"))):
    key = os.path.basename(add)[:-len(".add.md")]
    target = parts(key)[-1]
    body = open(add, encoding="utf-8").read().strip("\n")
    cur = open(target, encoding="utf-8").read()
    first_q = next(l for l in body.splitlines() if l.startswith("- "))
    if first_q in cur:
        print(f"{key}: already merged into {os.path.basename(target)}")
        continue
    open(target, "w", encoding="utf-8").write(cur.rstrip("\n") + "\n\n" + body + "\n")
    print(f"{key}: +{sum(1 for l in body.splitlines() if l.startswith('- '))} -> {os.path.basename(target)}")

# provenance for new refs
items = {}
for l in open(os.path.join(W, "batches", "all_items.jsonl"), encoding="utf-8"):
    r = json.loads(l)
    if r.get("kind") == "devi_full":
        items[r["id"]] = r
prov_p = os.path.join(W, "prov.json")
prov = json.load(open(prov_p, encoding="utf-8"))
used = set()
for f in glob.glob(os.path.join(C, "*.md")):
    for ln in open(f, encoding="utf-8"):
        m = REF.search(ln)
        if m:
            used.update(r.strip() for r in m.group(1).split(","))
added = 0
for rid in used & items.keys():
    if rid not in prov:
        prov[rid] = {"srcs": items[rid]["srcs"], "derived": False}
        added += 1
# problems from the Deep Learning Interviews book (refs Bnnnn, extracted by dli_extract.py)
BOOK = "BoltzmannEntropy__interviews.ai:Deep Learning Interviews (arXiv 2201.00650)"
book_used = {r for r in used if re.fullmatch(r"B\d{4}", r)}
for rid in book_used:
    if rid not in prov:
        prov[rid] = {"srcs": [BOOK], "derived": True}
        added += 1
json.dump(prov, open(prov_p, "w", encoding="utf-8"), ensure_ascii=False)

unused = [items[r] for r in sorted(items) if r not in used]
with open(os.path.join(ROOT, "_meta", "devi_unused.jsonl"), "w", encoding="utf-8") as f:
    for it in unused:
        f.write(json.dumps({"ref": it["id"], "q": it["q"], "source": it["src"],
                            "reason": "duplicate of an existing question, off-scope, or trivial library usage"},
                           ensure_ascii=False) + "\n")
print(f"devi items: {len(items)} placed {len(used & items.keys())} unused {len(unused)}; "
      f"book problems referenced {len(book_used)}; prov added {added}")
