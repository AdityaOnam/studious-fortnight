#!/usr/bin/env bash
# Shallow, text-only sparse clones of source repos into ../_raw/<owner>__<repo>
# usage: bash clone_sources.sh <raw_dir>
RAW="$1"
mkdir -p "$RAW"

REPOS="
alirezadir/AIMLInterviews
khangich/machine-learning-interview
chiphuyen/machine-learning-systems-design
chiphuyen/ml-interviews-book
andrewekhalel/MLQuestions
alexeygrigorev/data-science-interviews
youssefHosni/Data-Science-Interview-Questions-Answers
kojino/120-Data-Science-Interview-Questions
iamtodor/data-science-interview-questions-and-answers
Sroy20/machine-learning-interview-questions
rbhatia46/Data-Science-Interview-Resources
BoltzmannEntropy/interviews.ai
Exorust/TorchLeet
amitshekhariitbhu/machine-learning-interview-questions
amitshekhariitbhu/ai-engineering-interview-questions
pallavi-shekhar/ai-engineering-interview-questions-company-wise
llmgenai/LLMInterviewQuestions
KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub
KalyanKS-NLP/RAG-Interview-Questions-and-Answers-Hub
sreekanth-madisetty/Awesome-LLM-Interview-Questions
a-tabaza/genai_interview_questions
ombharatiya/AI-Engineer-Interview-Questions
ombharatiya/ai-system-design-guide
landedjobs/awesome-ai-engineer-interview
amanailab/Production-level-Generative-AI-Interview-Questions
MisterBooo/llm-interview-questions
DolbyUUU/Awesome-LLM-Interview-Questions-and-Answers
guocong-bincai/ai-interview-guide
bbruceyuan/AI-Interview-Code
wdndev/llm_interview_note
donnemartin/system-design-primer
ByteByteGoHq/system-design-101
karanpratapsingh/system-design
ashishps1/awesome-system-design-resources
ashishps1/awesome-low-level-design
systemdesign42/system-design-academy
checkcheckzz/system-design-interview
arpitbbhayani/system-design-questions
prasadgujar/low-level-design-primer
Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies
puncsky/system-design-and-architecture
CyC2018/CS-Notes
Snailclimb/JavaGuide
wolverinn/Waking-Up
gyoogle/tech-interview-for-developer
WooVictory/Ready-For-Tech-Interview
huihut/interview
Olshansk/interview
kansiris/SQL-interview-questions
JayrajSinh16/CS-Fundamentals-Interview
Amankalyrex007/Cs_fundamentals00
TanmayKJha/CS-Fundamentals-Interview-Questions
Ashiii27/Computer-Fundamentals
"

DEV="
llms-interview-questions llmops-interview-questions chatgpt-interview-questions
deep-learning-interview-questions nlp-interview-questions computer-vision-interview-questions
pytorch-interview-questions tensorflow-interview-questions keras-interview-questions
reinforcement-learning-interview-questions recommendation-systems-interview-questions
time-series-interview-questions statistics-interview-questions probability-interview-questions
linear-algebra-interview-questions optimization-interview-questions
data-scientist-interview-questions python-ml-interview-questions scikit-learn-interview-questions
xgboost-interview-questions light-gbm-interview-questions linear-regression-interview-questions
logistic-regression-interview-questions unsupervised-learning-interview-questions
supervised-learning-interview-questions k-means-clustering-interview-questions
random-forest-interview-questions pca-interview-questions svm-interview-questions
decision-tree-interview-questions naive-bayes-interview-questions k-nearest-neighbors-interview-questions
cnn-interview-questions rnn-interview-questions gans-interview-questions autoencoders-interview-questions
neural-networks-interview-questions gradient-descent-interview-questions feature-engineering-interview-questions
model-evaluation-interview-questions bias-and-variance-interview-questions ensemble-learning-interview-questions
dimensionality-reduction-interview-questions cluster-analysis-interview-questions classification-algorithms-interview-questions
cost-function-interview-questions transfer-learning-interview-questions anomaly-detection-interview-questions
explainable-ai-interview-questions ml-design-patterns-interview-questions mlops-interview-questions
curse-of-dimensionality-interview-questions genetic-algorithms-interview-questions q-learning-interview-questions
data-mining-interview-questions data-processing-interview-questions sql-ml-interview-questions
data-engineer-interview-questions apache-spark-interview-questions hadoop-interview-questions numpy-interview-questions pandas-interview-questions
software-architecture-interview-questions microservices-interview-questions caching-interview-questions
api-design-interview-questions concurrency-interview-questions cap-theorem-interview-questions
load-balancing-interview-questions availability-and-reliability-interview-questions
service-oriented-architecture-interview-questions reactive-systems-interview-questions layering-and-middleware-interview-questions
domain-driven-design-interview-questions dependency-injection-interview-questions websocket-interview-questions graphql-interview-questions
oop-interview-questions sql-interview-questions databases-interview-questions nosql-interview-questions
redis-interview-questions mongodb-interview-questions docker-interview-questions kubernetes-interview-questions
git-interview-questions devops-interview-questions cryptography-interview-questions web-security-interview-questions
big-o-notation-interview-questions testing-interview-questions python-interview-questions java-interview-questions cpp-interview-questions
blockchain-interview-questions
"

clone_one() {
  local url="$1" dest="$2"
  [ -d "$dest/.git" ] && return 0
  git clone -q --depth 1 --filter=blob:none --no-checkout "$url" "$dest" 2>/dev/null || { echo "FAIL $url"; return 1; }
  git -C "$dest" sparse-checkout set --no-cone '*.md' '*.txt' '*.ipynb' '*.markdown' 2>/dev/null
  git -C "$dest" checkout -q 2>/dev/null || echo "CHECKOUT-FAIL $url"
}

for r in $REPOS; do
  clone_one "https://github.com/$r.git" "$RAW/${r/\//__}" &
  while [ "$(jobs -r | wc -l)" -ge 6 ]; do sleep 1; done
done
for d in $DEV; do
  clone_one "https://github.com/Devinterview-io/$d.git" "$RAW/Devinterview-io__$d" &
  while [ "$(jobs -r | wc -l)" -ge 6 ]; do sleep 1; done
done
wait
echo DONE
