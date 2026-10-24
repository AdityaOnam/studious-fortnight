"""Build heading outlines of note-style repos so questions can be derived from them.

usage: python -I outline.py <raw_dir> <out_dir>
"""
import os, re, sys

RAW, OUTD = sys.argv[1], sys.argv[2]
os.makedirs(OUTD, exist_ok=True)

# repo -> (include path regex, max heading level)
CFG = {
    "Snailclimb__JavaGuide": (r"^docs/(cs-basics|database|distributed-system|high-performance|high-availability|system-design|java/concurrent|java/jvm|java/collection)/", 3),
    "CyC2018__CS-Notes": (r"^notes/", 3),
    "wolverinn__Waking-Up": (r"\.md$", 3),
    "gyoogle__tech-interview-for-developer": (r"^(Computer Science|Database|Design Pattern|Algorithm|Web|Language|Development_common_sense|Interview|Linux)", 3),
    "huihut__interview": (r"\.md$", 3),
    "wdndev__llm_interview_note": (r"^\d\d\.", 3),
    "ByteByteGoHq__system-design-101": (r"^(README|data/guides|[^/]+\.md)", 2),
    "karanpratapsingh__system-design": (r"\.md$", 3),
    "puncsky__system-design-and-architecture": (r"^(README|\w+/)?.*\.md$", 2),
    "donnemartin__system-design-primer": (r"^(README|solutions)", 3),
    "ombharatiya__ai-system-design-guide": (r"\.md$", 3),
    "alirezadir__AIMLInterviews": (r"^src/.*\.md$", 3),
    "guocong-bincai__ai-interview-guide": (r"\.md$", 2),
    "chiphuyen__ml-interviews-book": (r"^contents/.*\.md$", 3),
    "chiphuyen__machine-learning-systems-design": (r"\.md$", 2),
    "ashishps1__awesome-low-level-design": (r"README\.md$|problems", 2),
}

for repo, (inc, maxlvl) in CFG.items():
    root = os.path.join(RAW, repo)
    lines = [f"# OUTLINE of {repo}\n"]
    nfiles = 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d != ".git"]
        for f in sorted(fn):
            if not f.lower().endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dp, f), root).replace("\\", "/")
            if not re.search(inc, rel):
                continue
            try:
                txt = open(os.path.join(dp, f), encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            heads = []
            fence = False
            for line in txt.splitlines():
                if line.strip().startswith("```"):
                    fence = not fence
                    continue
                if fence:
                    continue
                m = re.match(r"^(#{1,6})\s+(.*)", line)
                if m and len(m.group(1)) <= maxlvl:
                    t = re.sub(r"\s+", " ", re.sub(r"\[([^\]]*)\]\([^)]*\)", lambda mm: mm.group(1), m.group(2))).strip()
                    heads.append("  " * (len(m.group(1)) - 1) + "- " + t[:110])
            if not heads:
                continue
            nfiles += 1
            lines.append(f"\n## FILE {rel}  ({len(txt)//1024} KB)")
            lines.extend(heads[:80])
    open(os.path.join(OUTD, repo + ".md"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"{repo}: {nfiles} files, outline {sum(len(l) for l in lines)//1024} KB")
