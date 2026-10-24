---
domain: finetune
topic: distillation_merging_continual_learning
title: Distillation, model merging, continual learning
tags: [distillation, merging, continual-learning, synthetic-data]
count: 107
---
# Distillation, model merging, continual learning

## Distillation fundamentals
- [FT04-001] What is knowledge distillation, and how is it used in the LLM ecosystem?
- [FT04-002] Why can a distilled small model beat a same-size model trained from scratch on the same number of tokens?
- [FT04-003] When would you distill an LLM into a smaller model, and what does that pipeline look like end to end?
- [FT04-004] What is strong-to-weak distillation, where smaller models are bootstrapped from flagship ones, and why is it cheaper than running full post-training on every size?
- [FT04-005] Why do soft targets carry more information than hard labels or sampled text, and how would you formalise that?
- [FT04-006] Compare hard-label, soft-label and on-policy distillation.
- [FT04-007] What is the difference between logit (token-level) distillation and sequence-level distillation?
- [FT04-008] What is temperature scaling in soft-label distillation, and how does it change the soft targets the student sees?
- [FT04-009] Compare pruning, quantization, low-rank approximation, weight sharing and distillation as model compression methods.
- [FT04-010] How does knowledge distillation compress language models such as TinyBERT or patient KD, and which layers or signals are matched?
- [FT04-011] When does distillation not make sense?
- [FT04-012] Why does label smoothing conflict with knowledge distillation?
- [FT04-013] Why is combining quantization-aware training with distillation attractive for deploying small models?
- [FT04-014] In knowledge distillation, what is the typical loss, and how do you balance the distillation term against the ground-truth term?

## Distillation methods for LLMs
- [FT04-015] Explain black-box versus logit distillation for LLMs. What do you need access to in each case?
- [FT04-016] When does logit distillation beat plain SFT on teacher outputs, and when is it not worth the extra plumbing?
- [FT04-017] When does on-policy distillation, where the student generates and the teacher corrects or scores, beat plain imitation of teacher outputs?
- [FT04-018] Your student and teacher have different tokenizers. What breaks in logit distillation, and what are the workarounds?
- [FT04-019] What changes if the teacher and student have different tokenizers and you only have the teacher's text outputs?
- [FT04-020] How would you distill reasoning ability into a small model, and why is collecting long chain-of-thought traces for SFT not enough?
- [FT04-021] Your distilled student fails on the complex reasoning that the teacher handled. How do you close the gap?
- [FT04-022] What is self-distillation via rejection sampling, and when is it useful?
- [FT04-023] How does self-instruct style bootstrapping relate to distillation from a stronger model, and what are the legal and quality caveats?
- [FT04-024] In post-training that distills from per-domain expert models, how do you decide the mixing ratio across domains?
- [FT04-025] When distilling from per-domain expert models, what goes wrong if the agent specialist's traces dominate the distillation set?
- [FT04-026] How would you distill a VLM's labels into a small classifier without inheriting its systematic errors?
- [FT04-027] What are the tradeoffs between matching intermediate hidden states or attention maps versus matching only the output distribution?
- [FT04-028] How do you choose the student architecture and size for a distillation project, and what is the capacity gap problem when the teacher is far larger?
- [FT04-029] What is multi-teacher distillation, and how would you combine disagreeing teachers?

## Distillation in practice and risks
- [FT04-030] Design a pipeline to distill a frontier model's performance on your task into an 8B model you can serve yourself. Walk me through the whole thing.
- [FT04-031] How would you build a distillation data pipeline with quality filtering?
- [FT04-032] Design a customer-specific distillation pipeline from production traces to a canary-deployed student model.
- [FT04-033] Why should distillation data come from real production traces rather than purely synthetic prompts?
- [FT04-034] When serving a distilled student behind a cascade with its teacher, how do you pick the confidence or routing threshold?
- [FT04-035] What are the legal and technical risks of distilling a closed API model into an open-weight student?
- [FT04-036] What is a model distillation (extraction) attack through an API, and how would you defend against it?
- [FT04-037] How do teacher hallucinations get baked into the student, and how do you filter them?
- [FT04-038] The teacher model is wrong in a systematic way on one class. What do you do before and during distillation?
- [FT04-039] How would you detect that a distilled student has simply memorised teacher traces?
- [FT04-040] What would you distill first from a large teacher, and how would you know the student lost something that only matters in the tail?
- [FT04-041] What happens to a student when the teacher is upgraded, and how often should you re-distill?
- [FT04-042] A customer spends fifty thousand dollars per month on a frontier model. How would you quote a distillation project, including payback?
- [FT04-043] How would you detect that the teacher you use for distillation or synthetic data was contaminated on your benchmark, given you cannot inspect its training set?
- [FT04-044] How do you evaluate whether a distilled student is good enough to replace the teacher, and which metrics beyond average accuracy matter?

## Synthetic data generation
- [FT04-045] How do you generate synthetic training data with an LLM for fine-tuning, and what are the pitfalls?
- [FT04-046] What are the main use cases of synthetic data for LLMs, and where is it a poor substitute for real data?
- [FT04-047] How do you ensure the quality of a synthetic dataset of 10 million rows?
- [FT04-048] How do you evaluate the quality of synthetic instruction data and prevent a loss of diversity?
- [FT04-049] How would you measure whether a synthetic dataset is diverse enough?
- [FT04-050] Why does rejection sampling change the quality economics of synthetic data for math and code but not for creative writing?
- [FT04-051] How would you seed and prompt a generator to avoid mode collapse and repetitive synthetic examples?
- [FT04-052] What role do verifiers (unit tests, proof checkers, reward models) play in filtering synthetic data?
- [FT04-053] How do you decide the mix of real and synthetic data in a fine-tuning set?
- [FT04-054] How do you prevent benchmark contamination and leakage when generating synthetic data with an LLM?
- [FT04-055] When would you use an LLM as a judge to filter synthetic data, and what biases does that introduce?
- [FT04-056] You need to fine-tune a model for a low-resource language or niche domain with almost no labelled data. How would you bootstrap synthetic data?

## Model collapse and data feedback loops
- [FT04-057] What is the risk of model collapse when training on synthetic data?
- [FT04-058] When is self-generated data safe to train on, and when is it poison?
- [FT04-059] How do you build a training dataset without triggering model collapse when much of your data is synthetic?
- [FT04-060] How would you quantitatively measure diversity loss in a model trained on synthetic data before it shows up in benchmarks, and how do you detect and prevent quality collapse?
- [FT04-061] Why do the tails of the distribution disappear first when a model is trained recursively on its own outputs?
- [FT04-062] The web is increasingly filled with LLM-generated text. How does that affect future pretraining data curation?

## Model merging
- [FT04-063] Explain model merging: task arithmetic, TIES, DARE and SLERP. When does merging actually work?
- [FT04-064] When does model merging work, and what is actually going on underneath in weight space?
- [FT04-065] Why does model merging fail across independently pretrained models but work across fine-tunes of one base?
- [FT04-066] What is a task vector, and what does adding, negating or scaling it do?
- [FT04-067] What interference problem does TIES-Merging address, and how do trimming, sign election and disjoint merge work?
- [FT04-068] How does DARE reduce redundancy in delta weights before merging, and why does random dropping work?
- [FT04-069] When is SLERP preferable to linear averaging of weights?
- [FT04-070] How does model soup or averaging of checkpoints from different fine-tuning runs improve robustness?
- [FT04-071] How would you merge three LoRAs of different ranks trained on the same base model?
- [FT04-072] How would you decide merge coefficients without a huge eval budget?
- [FT04-073] Why does model merging inflate leaderboard scores more than real capability?
- [FT04-074] What are the advantages and drawbacks of model merging compared with multi-task training on the union of the datasets?
- [FT04-075] How would you use merging to add a new capability, such as code or a new language, without degrading the base model's general behaviour?

## Continual learning and data flywheels
- [FT04-076] What is catastrophic forgetting, and why does it happen when fine-tuning a pretrained LLM on a new task?
- [FT04-077] Why does continual learning in a deployed agent risk catastrophic forgetting, and what mitigations exist?
- [FT04-078] Compare regularization-based (EWC), replay-based and architecture-based (adapters, LoRA) approaches to continual learning.
- [FT04-079] How do you choose the replay mix when continually pretraining a model on a new domain without losing general ability?
- [FT04-080] What is continued pretraining, and how do you pick the learning rate schedule and warmup when resuming training on new data?
- [FT04-081] You fine-tuned a model on a new domain and its general benchmarks dropped sharply. How do you diagnose and fix it?
- [FT04-082] How does an online training loop let a product model keep improving from user feedback, and what are its risks?
- [FT04-083] What is a data flywheel for an AI product, and how do you build one safely?
- [FT04-084] How do you evaluate a continually updated model so you detect regressions on old capabilities before each release?
- [FT04-085] How do you handle knowledge that becomes stale over time: continual learning, retrieval, or knowledge editing?

## Multi-task learning and curriculum
- [FT04-086] How do multi-task learning and transfer learning compare?
- [FT04-087] What is negative transfer in multi-task training, and how do you detect and reduce it?
- [FT04-088] How do you set task sampling proportions and loss weights when fine-tuning one model on many tasks of very different dataset sizes?
- [FT04-089] What are gradient conflicts between tasks, and how do methods like PCGrad address them?
- [FT04-090] What is curriculum learning, and how would you apply it to LLM pretraining or fine-tuning?
- [FT04-091] Why is data ordering and annealing on high-quality data at the end of pretraining useful?
- [FT04-092] What is the difference between ensemble learning and model merging, and when would you use each?

## Test-time compute and scaling
- [FT04-093] What is test-time (inference-time) scaling, and how does it trade inference compute for accuracy?
- [FT04-094] What is test-time compute, and how does a thinking budget control how much a model thinks?
- [FT04-095] How does inference-time scaling relate to agentic loops, and what does it cost in latency and money?
- [FT04-096] When would you use Self-Consistency versus Best-of-N sampling?
- [FT04-097] Compare majority voting, best-of-N with a reward model, and tree search as test-time strategies.
- [FT04-098] What is the difference between outcome reward models and process reward models, and how do they guide test-time search?
- [FT04-099] Under a fixed inference budget, when is it better to use a larger model with less thinking versus a smaller model with more samples?
- [FT04-100] Why does best-of-N with an imperfect verifier eventually plateau or degrade as N grows?
- [FT04-101] How would you train a model to reason for longer, for example with reinforcement learning on verifiable rewards?
- [FT04-102] A model unifies a thinking mode and a non-thinking mode with a caller-settable thinking budget. How would you train it, and how would you serve it?
- [FT04-103] How would you stop a hybrid thinking model from thinking on trivial prompts?
- [FT04-104] Does test-time compute help on visual tasks? Where does it help, where does it not, and how would you actually use it?
- [FT04-105] Given a fixed budget, would you spend it on more image tokens or more reasoning tokens, and how do you decide empirically?
- [FT04-106] Why can overthinking hurt, and how do you detect and mitigate excessively long reasoning traces?
- [FT04-107] How would you estimate the serving cost impact of test-time scaling on throughput and tail latency?
