"""Extract candidate interview questions (questions only) from cloned repos.

usage: python -I extract.py <raw_dir> <out_jsonl> [repo_substring ...]
Each output record: {src, path, line, h (heading breadcrumb), q}
"""
import json, os, re, sys

RAW, OUT = sys.argv[1], sys.argv[2]
ONLY = sys.argv[3:]
HEADS_ONLY = ("ombharatiya__AI-Engineer", "Devinterview-io__")
FOLLOW = re.compile(r"^\s*(?:[-*+]\s+)?(?:\*\*)?follow-?ups?(?:\*\*)?\s*:?(?:\*\*)?\s*(.*)$", re.I)

SKIP_FILES = re.compile(r"(^|/)(LICENSE|CONTRIBUTING|CODE_OF_CONDUCT|CHANGELOG|SUMMARY|_sidebar|_navbar)[^/]*$", re.I)
SKIP_DIRS = re.compile(r"(^|/)(\.git|node_modules|_book|Translation|translations?|cn|fa|zh|ko|assets|images?)(/|$)", re.I)

IMPER = re.compile(
    r"^(explain|describe|discuss|compare|contrast|design|implement|write|derive|define|differentiate|distinguish|"
    r"what|why|how|when|which|where|who|can|could|does|do|did|is|are|was|should|would|will|walk me|tell me|"
    r"give|name|prove|show|list|outline|suggest|calculate|compute|find|estimate|propose|devise|build|create|"
    r"state|justify|elaborate|enumerate|identify|illustrate|summari[sz]e|mention|argue|criticize|evaluate|"
    r"if |suppose|imagine|consider|given|assume|you have|you are|your )\b", re.I)

LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
LEAD = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+|\(?\d+\)\s*|[#]+\s*|>\s*)+")
QPREF = re.compile(r"^(?:\*\*)?\s*(?:Q(?:uestion)?\s*\.?\s*\d*\s*[:.)\-–]|\d+\s*[.)]\s*|Q\d+\s*[-–:.]?)\s*(?:\*\*)?\s*", re.I)
EMOJI = re.compile(r"[\U0001F300-\U0001FAFF☀-➿]+")


def clean(s):
    s = LINK.sub(r"\1", s)
    s = LEAD.sub("", s)
    s = QPREF.sub("", s)
    s = s.replace("**", "").replace("__", "").replace("`", "'")
    s = EMOJI.sub("", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\s+", " ", s).strip(" \t-–:*_")
    return s


def iter_lines(path):
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            txt = f.read()
    except OSError:
        return
    if path.endswith(".ipynb"):
        try:
            nb = json.loads(txt)
            txt = "\n\n".join("".join(c.get("source", [])) for c in nb.get("cells", []) if c.get("cell_type") == "markdown")
        except Exception:
            return
    fence = False
    for i, line in enumerate(txt.splitlines(), 1):
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        yield i, line


def main():
    out = open(OUT, "w", encoding="utf-8")
    total = {}
    for repo in sorted(os.listdir(RAW)):
        if ONLY and not any(o in repo for o in ONLY):
            continue
        rroot = os.path.join(RAW, repo)
        for dp, dn, fn in os.walk(rroot):
            dn[:] = [d for d in dn if d != ".git"]
            for f in fn:
                if not f.lower().endswith((".md", ".ipynb", ".markdown")):
                    continue
                rel = os.path.relpath(os.path.join(dp, f), rroot).replace("\\", "/")
                if SKIP_FILES.search(rel) or SKIP_DIRS.search(rel):
                    continue
                stack = []
                seen = set()
                for ln, line in iter_lines(os.path.join(dp, f)):
                    raw = line.rstrip()
                    if not raw.strip():
                        continue
                    hm = re.match(r"^(#{1,6})\s+(.*)", raw)
                    is_head = bool(hm)
                    if hm:
                        lvl = len(hm.group(1))
                        stack = stack[: lvl - 1] + [clean(hm.group(2))[:80]]
                    is_item = bool(re.match(r"^\s*(?:[-*+]|\d+[.)])\s+", raw))
                    fm = FOLLOW.match(raw)
                    if fm and fm.group(1):
                        for part in re.findall(r"[^?]+[?]", re.sub(r"\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1), fm.group(1)).replace("*", "")):
                            part = clean(part)
                            if 15 <= len(part) <= 260 and part.lower() not in seen:
                                seen.add(part.lower())
                                out.write(json.dumps({"src": repo, "path": rel, "line": ln, "h": " > ".join(x for x in stack if x)[:140], "q": part, "kind": "followup"}, ensure_ascii=False) + "\n")
                                total[repo] = total.get(repo, 0) + 1
                        continue
                    if any(repo.startswith(h) for h in HEADS_ONLY) and not is_head:
                        continue
                    c = clean(raw)
                    if not (20 <= len(c) <= 320) or len(c.split()) < 4:
                        continue
                    if c.lower().startswith(("http", "see ", "for more", "note:", "tip:", "answer", "image", "source")):
                        continue
                    ok = False
                    if c.endswith(("?", "？")):
                        ok = True
                    if not ok and (is_head or is_item) and len(c) <= 200 and IMPER.match(c) and not c.endswith(":"):
                        ok = True
                    if ok and not (is_head or is_item) and not (len(c) <= 200 and IMPER.match(c)):
                        ok = False
                    if not ok:
                        continue
                    key = c.lower()
                    if key in seen:
                        continue
                    seen.add(key)
                    rec = {"src": repo, "path": rel, "line": ln, "h": " > ".join(x for x in stack[:-1] if x)[:140] if is_head else " > ".join(x for x in stack if x)[:140], "q": c, "kind": "head" if is_head else ("item" if is_item else "text")}
                    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    total[repo] = total.get(repo, 0) + 1
    out.close()
    for k, v in sorted(total.items(), key=lambda x: -x[1]):
        print(f"{v:6d}  {k}")
    print("TOTAL", sum(total.values()))


main()
