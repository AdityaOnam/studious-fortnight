"""Route new devinterview items to topic keys by source page; mixed pages go to a manual list.

usage: python -I devi_route.py <work_dir> [manual_routes.tsv]
Writes _work/pools_new/<KEY>.tsv (ref \t page \t question) and _work/pools_new/_MIX.tsv (unrouted).
manual_routes.tsv lines: `ref<TAB>KEY` (KEY may be DROP).
"""
import json, os, re, sys, collections

# "Write/Implement/Code ..." tasks are coding exercises -> CODE01 (titles only)
CODING = re.compile(r"^(write|implement|code|create|develop|construct|build|use|train|perform|simulate|generate|demonstrate|apply|design a (python|function|script|class))\b", re.I)

W = sys.argv[1]
MAN = sys.argv[2] if len(sys.argv) > 2 else None
SLUG = {
    "bias-and-variance": "ML01", "curse-of-dimensionality": "ML01", "supervised-learning": "ML01",
    "classification-algorithms": "ML02", "linear-regression": "ML02", "logistic-regression": "ML02", "svm": "ML02",
    "k-nearest-neighbors": "ML02", "naive-bayes": "ML02",
    "decision-tree": "ML03", "random-forest": "ML03", "ensemble-learning": "ML03", "xgboost": "ML03", "light-gbm": "ML03",
    "cluster-analysis": "ML04", "k-means-clustering": "ML04", "pca": "ML04", "dimensionality-reduction": "ML04",
    "unsupervised-learning": "ML04",
    "feature-engineering": "ML05",
    "model-evaluation": "ML06", "explainable-ai": "ML06",
    "cost-function": "ML07", "gradient-descent": "ML07", "optimization": "ML07", "genetic-algorithms": "ML07",
    "probability": "ML08", "statistics": "ML08",
    "linear-algebra": "ML09",
    "anomaly-detection": "ML10", "recommendation-systems": "ML10", "time-series": "ML10",
    "reinforcement-learning": "ML11", "q-learning": "ML11",
    "cnn": "DL03", "computer-vision": "DL03", "transfer-learning": "DL03",
    "rnn": "DL04", "gans": "DL05", "autoencoders": "DL05", "nlp": "DL06",
    "pytorch": "DL07", "tensorflow": "DL07", "keras": "DL07", "numpy": "DL07", "pandas": "DL07", "scikit-learn": "DL07",
    "mlops": "MS01",
}
items = {}
for l in open(os.path.join(W, "batches", "all_items.jsonl"), encoding="utf-8"):
    r = json.loads(l)
    if r.get("kind") == "devi_full":
        items[r["id"]] = r
man = {}
if MAN and os.path.exists(MAN):
    for l in open(MAN, encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if len(p) >= 2:
            man[p[0].strip()] = p[1].strip()
out = collections.defaultdict(list)
for rid, r in items.items():
    page = r["h"].replace("-interview-questions", "")
    key = man.get(rid)
    if key != "DROP" and CODING.match(r["q"]):
        key = "CODE01"
    key = key or SLUG.get(page, "_MIX")
    if key != "DROP":
        out[key].append((rid, page, r["q"]))
od = os.path.join(W, "pools_new")
os.makedirs(od, exist_ok=True)
for f in os.listdir(od):
    if f.endswith(".tsv"):
        os.remove(os.path.join(od, f))
for k, lst in sorted(out.items()):
    with open(os.path.join(od, k + ".tsv"), "w", encoding="utf-8") as f:
        for rid, page, q in lst:
            f.write(f"{rid}\t{page}\t{q}\n")
    print(k, len(lst))
