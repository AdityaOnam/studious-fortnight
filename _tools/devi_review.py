"""Curation aid: for each new item of KEY, show its closest existing corpus question (TF-IDF cosine).

usage: python -I devi_review.py <root> <KEY> [threshold]
Prints `ref  score  new question  ||  closest existing (id)`; score >= threshold marked with '*'.
Existing = every question already in the corpus (_meta/questions.jsonl), so cross-file duplicates show too.
"""
import json, os, sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT, KEY = sys.argv[1], sys.argv[2]
TH = float(sys.argv[3]) if len(sys.argv) > 3 else 0.6
meta = [json.loads(l) for l in open(os.path.join(ROOT, "_meta", "questions.jsonl"), encoding="utf-8")]
new = [l.rstrip("\n").split("\t") for l in open(os.path.join(ROOT, "_work", "pools_new", KEY + ".tsv"), encoding="utf-8") if l.strip()]
vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, stop_words="english").fit([m["q"] for m in meta] + [n[2] for n in new])
S = cosine_similarity(vec.transform([n[2] for n in new]), vec.transform([m["q"] for m in meta]))
for i, (ref, page, q) in enumerate(new):
    j = S[i].argmax()
    s = S[i, j]
    print(f"{ref} {'*' if s >= TH else ' '}{s:.2f} [{page}] {q}  ||  {meta[j]['id']}: {meta[j]['q']}")
