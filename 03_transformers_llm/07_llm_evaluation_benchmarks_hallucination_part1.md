---
domain: llm
topic: llm_evaluation_benchmarks_hallucination
title: LLM evaluation, benchmarks and hallucination
tags: [llm-eval, benchmarks, hallucination, llm-as-judge]
count: 136
part: 1/2
---
# LLM evaluation, benchmarks and hallucination (part 1)

## Evaluation fundamentals and metrics
- [LLM07-001] What are the main ways to evaluate an LLM, and how do you choose metrics for a given application?
- [LLM07-002] What is the difference between intrinsic evaluation (such as perplexity) and extrinsic evaluation on downstream tasks for a language model?
- [LLM07-003] How does evaluating an LLM application differ from evaluating a traditional ML model?
- [LLM07-004] Give a taxonomy of LLM evaluation methods and say when you would use each one.
- [LLM07-005] What is evaluation-driven development for AI applications, and why do people say evals are the moat?
- [LLM07-006] What is the difference between reference-based and reference-free evaluation?
- [LLM07-007] Why do BLEU, ROUGE and exact match fail on open-ended LLM output, and what do teams use instead?
- [LLM07-008] Explain BLEU, ROUGE and BERTScore. When would you use each?
- [LLM07-009] When is BLEU still the right tool for evaluating LLM output?
- [LLM07-010] How do you evaluate open-ended generation when there is no single right answer and no ground truth?
- [LLM07-011] How is an LLM typically evaluated during and after the pretraining phase?
- [LLM07-012] How do you evaluate answers to questions on which even domain experts have no consensus ground truth?
- [LLM07-013] What is perplexity, and what are its limits as a measure of LLM quality?
- [LLM07-014] Why is perplexity the exponential of cross-entropy, and what does a perplexity of 8 mean in terms of average branching factor?
- [LLM07-015] Convert a loss of 2.0 nats per token into perplexity.
- [LLM07-016] What does perplexity measure, and why can't you compare it across models with different tokenizers?
- [LLM07-017] Why is perplexity not a reliable measure of instruction-following or chat quality?
- [LLM07-018] How would you use perplexity on a held-out corpus to spot low-quality documents or a domain shift in your data?
- [LLM07-019] Tokenizer A averages 3.5 bytes per token and tokenizer B averages 4.5. How do you compare the losses of models that use them?
- [LLM07-020] Why might a better model show a higher perplexity on your eval set?

## Public benchmarks, leaderboards and vendor claims
- [LLM07-021] What is the difference between a public capability benchmark and a task-specific eval, and when is each the right tool?
- [LLM07-022] What do MMLU, GSM8K, HumanEval, MT-Bench, GPQA and SWE-bench each measure, and how should you interpret their scores?
- [LLM07-023] Why is a general benchmark like MMLU a poor basis for choosing a model for your own product?
- [LLM07-024] Why have MMLU and HumanEval stopped being useful for ranking frontier models, and what has replaced them?
- [LLM07-025] If public benchmarks are this compromised, why do labs keep reporting them?
- [LLM07-026] How do you detect that a benchmark has saturated or leaked, and what do you do next?
- [LLM07-027] What is SWE-bench, and how is it used to evaluate AI coding ability?
- [LLM07-028] How do SWE-bench Pro, SWE-bench Multimodal and Terminal-Bench differ from the original SWE-bench?
- [LLM07-029] How do SWE-bench Verified and LiveCodeBench differ, and which matters more for evaluating a coding agent?
- [LLM07-030] Why do two labs report very different scores for the same model on the same benchmark when scaffolds or harnesses differ?
- [LLM07-031] Why does AlpacaEval 2.0 use a length-controlled win rate?
- [LLM07-032] How would you construct a length-controlled evaluation of a DPO-tuned model that a reviewer would trust?
- [LLM07-033] How does Chatbot Arena-style evaluation work, and what are its strengths and limits?
- [LLM07-034] How would you use a crowd-voted Elo leaderboard such as Arena responsibly when choosing a model for a chat product?
- [LLM07-035] Why is Bradley-Terry preferable to a naive win rate in Arena-style evaluation when comparison counts are uneven across model pairs?
- [LLM07-036] Design an internal arena for your company's use case. What breaks first?
- [LLM07-037] A vendor says its model scores 90% on a coding benchmark. What do you ask before believing it predicts your own quality?
- [LLM07-038] A vendor says its new model beats your current one by 10 points. What do you check before switching?
- [LLM07-039] A vendor reports 99.9% on a benchmark, but the organizer's own harness gives 62.7% for the same model. Which number do you use, and is a vendor number ever admissible?
- [LLM07-040] A launch post claims near-perfect scores on a new reasoning benchmark and a computer-use benchmark. How do you read those numbers?
- [LLM07-041] A candidate claims their AI system achieves 95% accuracy. What questions do you ask to decide whether that is meaningful?
- [LLM07-042] How do you evaluate which LLM is best for your use case, for example a customer support chatbot?
- [LLM07-043] What do you do when model-comparison eval results are ambiguous?

## Contamination and benchmark integrity
- [LLM07-044] What is benchmark contamination, and why does it inflate scores?
- [LLM07-045] What are canary strings, and how do they help keep benchmark data out of training corpora?
- [LLM07-046] How would you concretely detect that a model has memorized a benchmark or that it leaked into a vendor's training data?
- [LLM07-047] How would you decontaminate an eval set or a pretraining corpus, and keep eval results honest?
- [LLM07-048] How do you stop eval tasks from leaking into later fine-tuning data, including synthetic training data?
- [LLM07-049] Can benchmark contamination ever make a model look worse?
- [LLM07-050] What properties make a benchmark resistant to saturation and contamination?
- [LLM07-051] Your vendor claims decontamination via 13-gram overlap. What does that miss?
- [LLM07-052] How do you detect that a model was trained on paraphrases of your benchmark set?
- [LLM07-053] Why is benchmark contamination especially insidious for a multilingual model?
- [LLM07-054] Your fine-tune gained 8 points on your benchmark. How do you know the gain is real and not contamination?
- [LLM07-055] After a fine-tune gained 8 points, you find 3% n-gram overlap with training data, and removing it costs 2 of the 8 points. Do you ship?
- [LLM07-056] Your coding agent's benchmark score jumped 15 points after a model upgrade. How do you know the gain is real?
- [LLM07-057] How would you detect that a high SWE-bench score is inflated by contamination?
- [LLM07-058] As release engineer for an open-weights model that tops leaderboards, how do you make sure the benchmark numbers are trustworthy?
- [LLM07-059] Design a private LLM benchmark and leaderboard. How do you keep it trustworthy as labs optimise against it?
- [LLM07-060] A lab disputes its score on your private benchmark and demands the failing items. What do you give them?
- [LLM07-061] How would you design an eval that stays meaningful six months after a model's release?
- [LLM07-062] What is eval awareness, and how might it distort safety or capability evaluations?

## LLM-as-a-judge
- [LLM07-063] What is LLM-as-a-judge, when is it the right tool, and when is it unacceptable as the primary evaluation gate?
- [LLM07-064] What are the main limitations of LLM-as-a-judge evaluation?
- [LLM07-065] What biases does an LLM judge have (position, verbosity, self-preference), and how do you mitigate each?
- [LLM07-066] Design a quick experiment to measure position bias in your own LLM judge, and say how you would debias it.
- [LLM07-067] What is G-Eval, and how does it use LLMs for evaluation?
- [LLM07-068] Pointwise scoring versus pairwise comparison for LLM judges: which is more reliable, and why?
- [LLM07-069] Your pairwise judge says B beats A 60/40 but binary criteria show identical pass rates. What do you conclude?
- [LLM07-070] How do you aggregate pairwise judge results across five candidate prompts efficiently?
- [LLM07-071] Why do binary pass/fail judge criteria often work better than numeric rating scales?
- [LLM07-072] How do you design a good rubric for model-graded evals, how many criteria are too many, and where does chain-of-thought fit?
- [LLM07-073] How does rubric-based evaluation differ from a generic LLM-as-a-judge prompt, and why is it often recommended?
- [LLM07-074] Your faithfulness judge passes an answer that hedges so much it says nothing. What rubric change fixes that?
- [LLM07-075] What temperature would you use for an LLM-as-a-judge evaluation, and why?
- [LLM07-076] Would you use the same model as generator and judge? What if the judge disagrees with your spot-checks?
- [LLM07-077] Your LLM judge is from the same family as your production model, and switching families drops agreement with humans. What now?
- [LLM07-078] What is a panel of LLM judges, and when is it worth the cost?
- [LLM07-079] Your three LLM judges agree on 95% of verdicts. Is that good news?
- [LLM07-080] Your eval pipeline runs a cheap judge on all traffic and escalates low-confidence cases to a frontier judge. How do you validate that the escalation buys accuracy?
- [LLM07-081] Your distilled evaluator agrees with the frontier judge 92% of the time but with humans only 78%. Which number do you trust?
- [LLM07-082] How would you decide whether a small evaluator model is good enough to block responses inline?
- [LLM07-083] Agent-as-judge versus LLM-as-judge: when does the upgrade pay off, and what new failure modes does it introduce?
- [LLM07-084] Design a production LLM-as-a-judge pipeline. What are its biases and failure modes, and how do you correct for them?
- [LLM07-085] Walk through building and validating an LLM judge: labeling, data splits, prompt iteration and the metrics you track.
- [LLM07-086] How would you use an LLM judge for Hindi without importing the judge's English bias?
- [LLM07-087] How would you evaluate a candidate judge model on human-labelled preference data before adopting it?

## Human evaluation and trusting your judge
- [LLM07-088] How do you conduct human evaluation for AI systems?
- [LLM07-089] When would you pay for human evaluation even though your LLM judge agrees with humans 85% of the time?
- [LLM07-090] How do you measure inter-annotator agreement, and what do you do when annotators disagree a lot?
- [LLM07-091] Your annotators reach a Krippendorff's alpha of 0.4 and a rubric rewrite does not help. What now?
- [LLM07-092] How would you detect one annotator drifting over a month?
- [LLM07-093] Subject-matter experts disagree on 20% of golden labels, or the customer's own experts disagree. Who defines correct, and what do you do?
- [LLM07-094] How do you decide whether to trust your LLM judge? Walk me through calibration against human labels.
- [LLM07-095] How do you calibrate an LLM judge against human labels and correct estimated metrics for judge error?
- [LLM07-096] Your LLM judge's Cohen's kappa with humans is 0.45. What specifically do you do next?
- [LLM07-097] How would you calibrate an LLM judge that outputs a 1-10 score?
- [LLM07-098] How do you detect judge-human disagreement systematically?
- [LLM07-099] Your LLM judge and human labels disagree 15-30% of the time. What do you do?
- [LLM07-100] Your judge agrees with humans 70-80% of the time (including a VLM judge). Is that usable, and for what?
- [LLM07-101] Your automated judge and your clinicians disagree on a slice of notes. How do you work out which one is wrong?
- [LLM07-102] Your LLM judge prefers the new model 60/40 but human raters are 50/50, or the customer disagrees with the judge. Which do you trust?
- [LLM07-103] Your LLM judge scores rose but the user follow-up rate worsened. What happened?
- [LLM07-104] Your LLM judge passes 90-95% of outputs but users are unhappy. How do you debug the judge itself?
- [LLM07-105] How do you make judge scores trustworthy enough to gate releases, and what is the senior objection to a judge-only deploy gate?
- [LLM07-106] You use an LLM judge to gate deploys. A month later it is passing changes that users dislike. What is the likely cause and fix?
- [LLM07-107] How do you keep LLM judge calibration current without a standing labelling team?
- [LLM07-108] Your judge model is deprecated or updated and every score shifts. How do you keep scores comparable?
- [LLM07-109] How would you detect judge drift if the model version is genuinely pinned?
- [LLM07-110] The new LLM judge agrees with humans slightly less but is 5x cheaper. Do you take it?
- [LLM07-111] How do you version the judge itself so a judge-prompt change does not masquerade as a product regression?

## Hallucination
- [LLM07-112] What is hallucination in LLMs, and how do factuality errors differ from faithfulness errors?
- [LLM07-113] What are the different forms of hallucination, and how would you detect each in production?
- [LLM07-114] Why do LLMs hallucinate? Discuss data, training and inference-level causes.
- [LLM07-115] Why might maximum-likelihood training and exposure bias encourage hallucination?
- [LLM07-116] Why might SFT on knowledge the base model never saw encourage hallucination?
- [LLM07-117] On what types of queries are LLMs most likely to hallucinate?
- [LLM07-118] Is hallucination always harmful? When is a hallucination-shaped answer acceptable or desirable, and how do you switch regimes?
- [LLM07-119] How does RLHF or preference tuning affect hallucination, for example through sycophancy and rewarding confident answers?
- [LLM07-120] How does retrieval-augmented generation reduce hallucination, and how can a RAG system still produce unfaithful answers?
- [LLM07-121] How do you detect and measure hallucinations in LLM outputs?
- [LLM07-122] How do you measure factual consistency or groundedness, and how do you enforce it as well as measure it?
- [LLM07-123] How do SelfCheckGPT-style sampling consistency, semantic entropy and citation verification detect hallucinations?
- [LLM07-124] What is Chain-of-Verification (CoVe), and how does it reduce hallucination?
- [LLM07-125] Why does verifying citations require checking the source text, not just that a citation exists?
- [LLM07-126] How do you mitigate hallucination at the data, training and inference levels?
- [LLM07-127] Your summarization system hallucinated facts that are not in the original article. How do you fix it?
- [LLM07-128] Your LLM does not admit when it does not know. How do you make it say "I don't know"?
- [LLM07-129] How would you design an abstention strategy, by training or prompting, so a model abstains instead of fabricating?
- [LLM07-130] How would you measure the knowledge boundary of a model to enable honest refusal?
- [LLM07-131] Which is safer for a medical FAQ: a fluent guess or an "I can't answer that" response?
- [LLM07-132] How do you treat hallucination as a safety and product risk, and design the product around it rather than only the prompt?
- [LLM07-133] When is showing confidence scores to users a bad idea?
- [LLM07-134] How would you measure your hallucination rate in production?
- [LLM07-135] How do you handle hallucinations when they occur in a production AI system?
- [LLM07-136] Your hallucination rate jumped 30% after a provider silently updated the model. How do you detect and respond?
