"""Extract all question titles (free + premium, titles only) from saved devinterview.io topic pages.

usage: python -I devi_titles.py <html_dir> <urls_ml.txt> <out.jsonl>
Output rows use the raw_candidates.jsonl schema so they can flow through the normal pipeline.
"""
import html, json, os, re, sys

HDIR, URLS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
ART = re.compile(r'<article id="([A-Za-z]+)(\d+)" class="Question".*?<h3>(.*?)</h3>', re.S)

rows = []
for line in open(URLS, encoding="utf-8"):
    repo, n, url = line.split()
    slug = repo[len("Devinterview-io__"):]
    page = open(os.path.join(HDIR, slug + ".html"), encoding="utf-8").read()
    seen = set()
    for _, num, h3 in ART.findall(page):
        if num in seen:
            continue
        seen.add(num)
        q = html.unescape(re.sub(r"<[^>]+>", "", h3)).strip()
        rows.append({"src": repo, "path": "devinterview.io", "line": int(num), "h": slug, "q": q, "kind": "devi_full"})
    print(f"{slug}: {len(seen)}/{n}", file=sys.stderr)

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(rows), "titles", file=sys.stderr)
