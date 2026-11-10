"""Show the closest existing corpus questions for each candidate line (TF-IDF cosine).

usage: python -I near_dups.py <root> <candidates.tsv> [threshold]
candidates.tsv lines: KEY<TAB>D<TAB>question<TAB>refs
"""
import json, os, sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

root, cand = sys.argv[1], sys.argv[2]
th = float(sys.argv[3]) if len(sys.argv) > 3 else 0.35
meta = [json.loads(l) for l in open(os.path.join(root, "_meta", "questions.jsonl"), encoding="utf-8")]
c = [l.rstrip("\n").split("\t") for l in open(cand, encoding="utf-8") if l.strip()]
v = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, stop_words="english").fit([m["q"] for m in meta] + [x[2] for x in c])
S = cosine_similarity(v.transform([x[2] for x in c]), v.transform([m["q"] for m in meta]))
for i, x in enumerate(c):
    j = S[i].argmax()
    if S[i, j] >= th:
        print(f"{S[i, j]:.2f} {x[0]} {x[2][:80]}\n      || {meta[j]['id']}: {meta[j]['q'][:120]}")
print(len(c), "candidates")
