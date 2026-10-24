"""Pre-filter raw candidates, assign ids, split into classification batches.

usage: python -I prep_batches.py <raw_candidates.jsonl> <out_dir> [batch_size]
"""
import json, os, re, sys, collections, hashlib

SRC, OUTD = sys.argv[1], sys.argv[2]
BS = int(sys.argv[3]) if len(sys.argv) > 3 else 300
os.makedirs(OUTD, exist_ok=True)

NOISE = re.compile(r"(https?://|www\.|\||\{|\}|=>|</|^\W|^\d+(\.\d+)*$|\.(py|md|png|jpg|ipynb)\b|©|star history|buy me|subscribe|follow me|click here)", re.I)
BAD_START = ("table of contents", "contents", "references", "prerequisites", "installation", "getting started", "how to use", "how to contribute", "how to run", "usage", "license", "acknowledg", "you can also find", "stay updated", "answers:", "answer:", "solution")

AI_SRC = ("alirezadir", "chiphuyen", "andrewekhalel", "alexeygrigorev", "youssefHosni", "kojino", "iamtodor", "Sroy20",
          "rbhatia46", "Exorust", "amitshekhariitbhu", "pallavi-shekhar", "llmgenai", "KalyanKS", "sreekanth", "a-tabaza",
          "landedjobs", "MisterBooo", "DolbyUUU", "guocong", "bbruceyuan", "wdndev", "khangich", "Engineer1999",
          "BoltzmannEntropy")
CS_SRC = ("Amankalyrex007", "Ashiii27", "JayrajSinh16", "TanmayKJha", "CyC2018", "Snailclimb", "wolverinn", "gyoogle",
          "huihut", "Olshansk", "kansiris", "ByteByteGoHq", "puncsky", "karanpratapsingh", "donnemartin", "systemdesign42",
          "arpitbbhayani", "prasadgujar", "ashishps1", "checkcheckzz")
DEV_AI = ("llm", "chatgpt", "deep-learning", "nlp", "computer-vision", "pytorch", "tensorflow", "keras", "reinforcement",
          "recommendation", "time-series", "statistics", "probability", "linear-algebra", "optimization", "data-scientist",
          "python-ml", "scikit", "xgboost", "light-gbm", "regression", "unsupervised", "supervised", "k-means", "random-forest",
          "pca", "svm", "decision-tree", "naive-bayes", "k-nearest", "cnn", "rnn", "gans", "autoencoders", "neural", "gradient",
          "feature-eng", "model-eval", "bias-and", "ensemble", "dimensionality", "cluster", "classification", "cost-function",
          "transfer", "anomaly", "explainable", "ml-design", "mlops", "curse", "genetic", "q-learning", "data-mining",
          "data-processing", "sql-ml", "data-engineer", "apache-spark", "hadoop", "numpy", "pandas")


def group_of(src):
    if src.startswith("ombharatiya__AI-Engineer"):
        return "mix"
    if src.startswith("ombharatiya__ai-system"):
        return "ai"
    if src.startswith("Devinterview-io__"):
        n = src[len("Devinterview-io__"):]
        return "ai" if any(k in n for k in DEV_AI) else "cs"
    if any(src.split("__", 1)[0] == s or src.split("__", 1)[0].startswith(s) or s in src for s in AI_SRC):
        return "ai"
    if any(s in src for s in CS_SRC):
        return "cs"
    return "mix"


rows = [json.loads(l) for l in open(SRC, encoding="utf-8")]
kept, dropped = [], 0
for r in rows:
    q = r["q"]
    ql = q.lower()
    if NOISE.search(q) or ql.startswith(BAD_START) or len(re.findall(r"[;=<>]", q)) > 2:
        dropped += 1
        continue
    r["q"] = q
    kept.append(r)

# exact-duplicate collapse (normalised text) keeping every provenance
def norm(t):
    return re.sub(r"[^a-z0-9\u0080-￿ ]+", "", t.lower()).strip()

by = collections.OrderedDict()
for r in kept:
    k = norm(r["q"])
    if not k:
        continue
    if k in by:
        by[k]["srcs"].append(f'{r["src"]}:{r["path"]}')
    else:
        by[k] = {"q": r["q"], "src": r["src"], "path": r["path"], "h": r["h"], "kind": r["kind"], "srcs": [f'{r["src"]}:{r["path"]}']}

items = list(by.values())
for i, it in enumerate(items, 1):
    it["id"] = f"Q{i:06d}"
    it["group"] = group_of(it["src"])

with open(os.path.join(OUTD, "all_items.jsonl"), "w", encoding="utf-8") as f:
    for it in items:
        f.write(json.dumps(it, ensure_ascii=False) + "\n")

groups = collections.defaultdict(list)
for it in items:
    groups[it["group"]].append(it)

nb = 0
for g, lst in groups.items():
    lst.sort(key=lambda x: (x["src"], x["path"], x["id"]))
    for bi in range(0, len(lst), BS):
        chunk = lst[bi: bi + BS]
        nb += 1
        name = f"{g}_{bi // BS + 1:02d}.tsv"
        with open(os.path.join(OUTD, name), "w", encoding="utf-8") as f:
            for it in chunk:
                h = it["h"].split(" > ")[-1][:50] if it["h"] else ""
                tag = it["src"].split("__")[-1][:28]
                f.write(f'{it["id"]}\t{it["q"]}\t[{tag}|{h}]\n')
print("raw", len(rows), "noise-dropped", dropped, "unique", len(items), "batches", nb)
print({g: len(v) for g, v in groups.items()})
