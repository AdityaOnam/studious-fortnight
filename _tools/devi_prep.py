"""Add full devinterview.io title lists (devi_titles.py output) to the pipeline.

Drops titles already in the corpus (normalised exact match), appends the rest to
_work/batches/all_items.jsonl with fresh Q ids, and writes classification batches devi_NN.tsv.
Idempotent: items already appended (kind == devi_full) are not added twice.

usage: python -I devi_prep.py <work_dir> <devi_full.jsonl> [batch_size]
"""
import json, os, re, sys

W, SRC = sys.argv[1], sys.argv[2]
BS = int(sys.argv[3]) if len(sys.argv) > 3 else 300
B = os.path.join(W, "batches")
norm = lambda t: re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()

ai_path = os.path.join(B, "all_items.jsonl")
items = [json.loads(l) for l in open(ai_path, encoding="utf-8")]
if any(i.get("kind") == "devi_full" for i in items):
    sys.exit("devi_full items already appended; nothing to do")
have = {norm(i["q"]) for i in items}
have |= {norm(json.loads(l)["q"]) for l in open(os.path.join(W, "..", "_meta", "questions.jsonl"), encoding="utf-8")}

nxt = max(int(i["id"][1:]) for i in items) + 1
new = []
for l in open(SRC, encoding="utf-8"):
    r = json.loads(l)
    k = norm(r["q"])
    if not k or k in have:
        continue
    have.add(k)
    new.append({"q": r["q"], "src": r["src"], "path": r["path"], "h": r["h"], "kind": "devi_full",
                "srcs": [f'{r["src"]}:devinterview.io'], "id": f"Q{nxt:06d}", "group": "devi"})
    nxt += 1

with open(ai_path, "a", encoding="utf-8") as f:
    for it in new:
        f.write(json.dumps(it, ensure_ascii=False) + "\n")
for bi in range(0, len(new), BS):
    with open(os.path.join(B, f"devi_{bi // BS + 1:02d}.tsv"), "w", encoding="utf-8") as f:
        for it in new[bi: bi + BS]:
            tag = it["src"].split("__")[-1].replace("-interview-questions", "")
            f.write(f'{it["id"]}\t{it["q"]}\t[{tag}|devinterview]\n')
print("new", len(new), "batches", (len(new) + BS - 1) // BS, "ids", new[0]["id"], "-", new[-1]["id"])
