"""Generate 00_START_HERE/INDEX.md and SOURCES.md from _meta/questions.jsonl + final_summary.json.

usage: python -I make_docs.py <root>
"""
import json, os, re, subprocess, sys, collections, datetime

ROOT = sys.argv[1]
meta = [json.loads(l) for l in open(os.path.join(ROOT, "_meta", "questions.jsonl"), encoding="utf-8")]
summary = json.load(open(os.path.join(ROOT, "_work", "final_summary.json"), encoding="utf-8"))
T = json.load(open(os.path.join(os.path.dirname(__file__), "taxonomy.json"), encoding="utf-8"))
today = datetime.date.today().isoformat()

# ---------- INDEX ----------
by_file = collections.OrderedDict()
for path, title, n in summary:
    by_file[path] = (title, n)
domain_names = {
    "01_ml_fundamentals": "Classical ML & statistics", "02_deep_learning": "Deep learning",
    "03_transformers_llm": "Transformers & LLM internals", "04_fine_tuning_alignment": "Fine-tuning & alignment",
    "05_rag_retrieval": "RAG & retrieval", "06_genai_apps_agents": "GenAI apps, agents, safety",
    "07_mlops_ml_system_design": "MLOps & ML/GenAI system design", "08_system_design": "System design (HLD/LLD)",
    "09_cs_fundamentals": "CS fundamentals", "10_coding_practice_index": "ML/LLM coding tasks (titles only)",
}
gen_by_file = collections.Counter(m["file"] for m in meta if m["generated"])
dif = collections.Counter(m["difficulty"] for m in meta)
lines = ["# INDEX — every question file", "",
         f"Generated {today}. Total questions: **{len(meta)}** in **{len(by_file)}** files "
         f"(E/M/H = {dif['E']}/{dif['M']}/{dif['H']}; {sum(1 for m in meta if m['generated'])} written by Claude to fill gaps, the rest harvested from GitHub repos — see SOURCES.md).", "",
         "Question IDs look like `RAG03-014` (topic key + running number). Files contain questions only.", ""]
cur = None
tot = collections.Counter()
for path, (title, n) in by_file.items():
    d = path.split("/")[0]
    tot[d] += n
for d in domain_names:
    ps = [p for p in by_file if p.startswith(d + "/")]
    if not ps:
        continue
    lines += [f"## {d} — {domain_names[d]} ({tot[d]} questions)", "", "| File | Topic | Questions |", "|---|---|---|"]
    for p in ps:
        lines.append(f"| `{p}` | {by_file[p][0]} | {by_file[p][1]} |")
    lines.append("")
open(os.path.join(ROOT, "00_START_HERE", "INDEX.md"), "w", encoding="utf-8").write("\n".join(lines))

# ---------- SOURCES ----------
cnt = collections.Counter()
for m in meta:
    seen = set()
    for s in m["sources"]:
        repo = s.split(":", 1)[0]
        repo = repo.replace("__", "/", 1) if "__" in repo else repo
        if repo.startswith("Devinterview-io/"):
            repo = "Devinterview-io/*"
        seen.add(repo)
    for r in seen:
        cnt[r] += 1
    if m["generated"]:
        cnt["(written by Claude, gap-fill)"] += 1

def gh(repo):
    try:
        out = subprocess.run(["gh", "api", f"repos/{repo}", "--jq", "[.stargazers_count,(.license.spdx_id//\"none\")]|@tsv"],
                             capture_output=True, text=True, timeout=30).stdout.strip().split("\t")
        return int(out[0]), out[1]
    except Exception:
        return None, "?"

rows = []
for repo, c in cnt.most_common():
    if repo.startswith("(") or repo == "Devinterview-io/*":
        rows.append((repo, "", "", c))
    elif "/" in repo:
        st, lic = gh(repo)
        rows.append((repo, st if st is not None else "?", lic, c))
    else:
        rows.append((repo, "", "", c))
L = ["# SOURCES", "",
     f"Built {today}. Questions were harvested (questions only, no answers) from the public GitHub repositories below, "
     "cleaned, translated to English where needed, de-duplicated and re-organised by topic. "
     "A question can be traced back to its source repo/path in `_meta/questions.jsonl`.", "",
     "**Licence note.** Many of these repos carry no licence or a restrictive one (GPL etc.). This corpus is for **private study / personal RAG use**. "
     "Do not redistribute it publicly without re-checking each source's licence.", "",
     "Notes-style repos (JavaGuide, CS-Notes, wdndev/llm_interview_note, gyoogle, system-design guides, …) are not question lists; "
     "questions from them were *derived* by Claude from their topic structure. Questions marked generated were written by Claude to fill coverage gaps.", "",
     "| Source | Stars | Licence | Questions touched |", "|---|---|---|---|"]
for repo, st, lic, c in rows:
    link = f"[{repo}](https://github.com/{repo})" if "/" in repo and not repo.startswith("(") and "*" not in repo else (f"[Devinterview-io](https://github.com/Devinterview-io) (≈95 repos)" if repo == "Devinterview-io/*" else repo)
    L.append(f"| {link} | {st} | {lic} | {c} |")
L += ["", "Not harvested: *Deep Learning Interviews* (interviews.ai, arXiv 2201.00650) — the book is PDF-only; add it manually if you want its problems.", ""]
open(os.path.join(ROOT, "00_START_HERE", "SOURCES.md"), "w", encoding="utf-8").write("\n".join(L))
print("INDEX/SOURCES written;", len(meta), "questions;", len(rows), "source rows")
