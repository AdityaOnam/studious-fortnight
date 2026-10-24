---
domain: llm
topic: pretraining_data_distributed_training
title: Pretraining, data and distributed training
tags: [pretraining, distributed-training, zero, fsdp]
count: 107
part: 1/2
---
# Pretraining, data and distributed training (part 1)

## Pretraining objectives and pipeline
- [LLM04-001] What is the primary objective of the pretraining phase for a large language model?
- [LLM04-002] What is the significance of self-supervised learning in LLM pretraining?
- [LLM04-003] What is the difference between causal language modeling and masked language modeling as pretraining objectives?
- [LLM04-004] What are the main phases of LLM development, from pretraining through post-training?
- [LLM04-005] How are large language models trained? Walk through the training process of a GPT-style model.
- [LLM04-006] Why do we pretrain and then fine-tune, and what does each stage contribute to a transformer's capabilities?
- [LLM04-007] Describe the three-stage pipeline of pretraining, SFT and alignment (RLHF/DPO). What does each stage change about the model?
- [LLM04-008] Which loss is used for pretraining, how is cross-entropy applied to next-token targets, and how does it relate to perplexity?
- [LLM04-009] How do causal LM, masked LM and span-corruption objectives differ, and which architectures suit each?
- [LLM04-010] BERT selects 15% of tokens, then replaces 80% of them with [MASK], 10% with random tokens and leaves 10% unchanged. Why?
- [LLM04-011] How does BERT's masked language modelling differ from CBOW in word2vec?
- [LLM04-012] Why is next-token prediction such a powerful pretext task compared with autoencoding or denoising objectives?
- [LLM04-013] What is exposure bias, and how much does it matter in practice?
- [LLM04-014] When would you still pretrain or fine-tune with a masked language modeling objective today?
- [LLM04-015] What are the main challenges in LLM pretraining, such as compute cost, data quality, long run times and instability?
- [LLM04-016] What is the difference between pretraining from scratch and a mid-training or continued-pretraining stage, and why do labs add one?
- [LLM04-017] Why do many labs anneal the learning rate at the end of pretraining while upsampling high-quality data?
- [LLM04-018] What is multi-token prediction as a training objective, and what does it buy you?
- [LLM04-019] Why does in-context learning emerge from next-token prediction on web-scale text?
- [LLM04-020] How would you weight the auxiliary losses for the t+2 and t+3 heads in multi-token prediction?
- [LLM04-021] GLM uses autoregressive blank infilling. How does it differ from BERT and GPT, and why was it argued to unify understanding and generation?
- [LLM04-022] In autoregressive blank infilling, why does the order in which spans are predicted matter?
- [LLM04-023] How would you adapt the span-length distribution of a blank-infilling objective if you cared mostly about long-form generation?
- [LLM04-024] Why can naive fill-in-the-middle (FIM) masking leak the middle into the suffix, and how do you prevent it?
- [LLM04-025] In repository-level FIM training for a code model, how would you order context files so the most relevant ones survive truncation?

## Data curation, mixing and synthetic data
- [LLM04-026] What kinds of data are used to pretrain LLMs, and what are the trade-offs between data quality and scale?
- [LLM04-027] Why is data quality often said to matter more than raw quantity for pretraining, and how would you measure it?
- [LLM04-028] What heuristic filters, such as length, symbol ratio, repetition and small-LM perplexity, are commonly applied to web text, and why?
- [LLM04-029] What open pretraining corpora exist, and what filtering and quality steps do web-scale corpora go through?
- [LLM04-030] Describe a pretraining data pipeline: sources, filtering, deduplication, quality scoring and mixing.
- [LLM04-031] Why do many pipelines use a model-based quality classifier, and what biases can it introduce into the corpus?
- [LLM04-032] How do you handle PII, copyrighted and toxic content in pretraining data, and what does aggressive filtering cost you?
- [LLM04-033] How should multilingual data be balanced so low-resource languages are not drowned out without hurting English performance?
- [LLM04-034] What is sequence packing, and why must attention masks and loss masks be handled correctly with it?
- [LLM04-035] What is a data curriculum in pretraining, and why might ordering or mixing proportions matter?
- [LLM04-036] How do you choose mixture weights across domains such as web, code, books and math, and how can small proxy runs help?
- [LLM04-037] Why does upsampling code and math data tend to help general reasoning, and what are the costs?
- [LLM04-038] How would you mix general, code and domain data when continuing to pretrain a base model on a vertical domain?
- [LLM04-039] How do you decide whether to train a domain LLM from scratch, continue pretraining, or only fine-tune?
- [LLM04-040] When building a web-scale pretraining corpus, why can a benchmark suite mislead you at small scale?
- [LLM04-041] What is the data wall, and how does synthetic data change the pretraining picture?
- [LLM04-042] What are the risks of training on model-generated data, and what is model collapse?
- [LLM04-043] What is evol-instruct style data generation, and what diversity problems can it introduce?
- [LLM04-044] How do you ensure the quality of a ten-million-row synthetic dataset before using it for training?
- [LLM04-045] If you had one frontier multimodal pretraining run, what data-mixture questions would you have to answer?
- [LLM04-046] How would you design a data curation pipeline for pretraining a new LLM, covering language ID, quality classifiers, PII removal and decontamination?

## Deduplication, decontamination and repeated data
- [LLM04-047] Why is deduplication one of the most important stages of a pretraining data pipeline, and what harm do duplicates cause?
- [LLM04-048] What is the difference between exact, near-duplicate and semantic deduplication, and what does each cost?
- [LLM04-049] How do MinHash and SimHash work for near-duplicate detection?
- [LLM04-050] In near-duplicate detection with shingling, how do you pick the shingle size, and what breaks with unigrams?
- [LLM04-051] In MinHash LSH, how do the number of bands and rows trade off precision and recall around a Jaccard threshold?
- [LLM04-052] Does repeating tokens in pretraining data hurt performance? What does empirical evidence say about how many epochs are useful?
- [LLM04-053] Why might a team consider multi-epoch training on the same corpus, and what degradation mechanisms such as memorization and overfitting arise?
- [LLM04-054] Can dropout or other regularization reduce the harm of repeated data in pretraining?
- [LLM04-055] How does duplication frequency in the training corpus relate to verbatim memorization and privacy risk?
- [LLM04-056] How does benchmark contamination in a pretraining corpus show up in benchmark scores?
- [LLM04-057] How would you detect benchmark contamination in a model whose training data you cannot inspect?
- [LLM04-058] Two outlets rewrite the same story with different shingles but the same facts. Is that a duplicate, and whose problem is it?
- [LLM04-059] How do you dedup eval sets against the training corpus (decontamination), and why is that a different problem from corpus deduplication?
- [LLM04-060] Design a deduplication pipeline for a web-scale pretraining corpus that has to run as a streaming process.
- [LLM04-061] In a MinHash-based deduplication pipeline, what breaks if you parallelize by document rather than by band?

## Compute, memory and cost estimation
- [LLM04-062] Where do the parameters and FLOPs actually live in a transformer? Walk me through the budget.
- [LLM04-063] Where does the 6ND estimate of training FLOPs come from, and how do you use it to estimate training time on a cluster?
- [LLM04-064] Why is training memory so much larger than inference memory?
- [LLM04-065] Why does mixed-precision Adam need about 12 bytes of optimizer state per parameter (FP32 weights, momentum, variance)?
- [LLM04-066] What is the memory footprint of Adam for a 7B-parameter model, and how do you reduce it?
- [LLM04-067] How do you estimate GPU memory for an N-billion-parameter model for inference and for full training?
- [LLM04-068] Which batch-size and sequence-length terms drive activation memory, and which parts dominate in long-context training?
- [LLM04-069] How do you measure model FLOPs utilization (MFU) during training, and what is a healthy value?
- [LLM04-070] What is the difference between MFU and hardware FLOPs utilization when activation recomputation is used?
- [LLM04-071] Discuss the cost and resource implications of training models in the GPT-3 class.
- [LLM04-072] Why does the Chinchilla compute-optimal recipe not tell you the right model size for a product that will serve billions of requests?
- [LLM04-073] What is missing from a single "training cost" number for an LLM?
- [LLM04-074] Your AI training produces massive carbon emissions. How do you reduce the environmental impact?
- [LLM04-075] How reliably can scaling laws fitted on small runs predict the loss of a large run, and where do they break down?
- [LLM04-076] Derive the 6ND training-FLOP estimate. At what context length does attention compute overtake MLP compute for this architecture?
- [LLM04-077] Estimate the compute to pretrain a 70B dense model on 15T tokens, and explain the formula you use.
- [LLM04-078] How much GPU memory does a 7B model need for training with Adam in mixed precision? Break down weights, gradients, optimizer states and activations.
- [LLM04-079] Can you train a 65B-parameter model such as Vicuna on four 32GB GPUs? Reason through weights, gradients, optimizer states and activations.
- [LLM04-080] You have 2048 GPUs at 40% MFU. Roughly how long does it take to train a 7B model on 2T tokens? Show your arithmetic.
- [LLM04-081] Why can loss computation for a large-vocabulary LM dominate memory, and what do fused kernels such as chunked cross-entropy do about it?
- [LLM04-082] A lab claims frontier-class results at a fraction of the usual training cost. How is that possible? Give a structured answer.
- [LLM04-083] Of the levers behind low-cost frontier training, which generalise to a lab with different hardware and which are specific to one GPU setup?

## Data parallelism, ZeRO and FSDP
- [LLM04-084] What are the main parallelism strategies for training LLMs, and what problem does each solve?
- [LLM04-085] Explain data parallelism. What gets replicated, what gets split, and what is communicated each step?
- [LLM04-086] Why is PyTorch DataParallel (DP) inferior to DistributedDataParallel (DDP)?
- [LLM04-087] What are the collective primitives (broadcast, scatter, reduce, all-reduce, all-gather, reduce-scatter) and where is each used in training?
- [LLM04-088] What is the difference between point-to-point and collective communication, and which does pipeline parallelism rely on?
- [LLM04-089] How does DDP use bucketed ring all-reduce to overlap gradient communication with backward computation?
- [LLM04-090] How is all-reduce implemented as reduce-scatter plus all-gather, and what is the per-GPU communication volume of ring all-reduce?
- [LLM04-091] What is synchronous versus asynchronous gradient updating in data parallelism, and why do LLM trainings use synchronous?
- [LLM04-092] Where does communication become the bottleneck as you scale data parallelism, and what does gradient accumulation change?
- [LLM04-093] How do you speed up data-parallel training when communication starts to dominate step time?
- [LLM04-094] Estimate the all-reduce time for BF16 gradients of a 7B model across 8 GPUs with 300 GB/s links.
- [LLM04-095] What problems do DDP, FSDP and ZeRO each solve?
- [LLM04-096] What do ZeRO stages 1, 2 and 3 partition (optimizer states, gradients, parameters), and how does FSDP relate?
- [LLM04-097] How does PyTorch FSDP differ from DDP, and what are its memory and communication trade-offs?
- [LLM04-098] Why does ZeRO-1 add almost no communication overhead while ZeRO-3 raises it to roughly 1.5x that of DDP?
- [LLM04-099] What do ZeRO-Offload and ZeRO-Infinity do, and when do they make sense?
- [LLM04-100] What does a DeepSpeed config typically control (stage, offload, bucket size, accumulation, micro-batch), and how would you tune it for throughput?
- [LLM04-101] What is hybrid sharded data parallelism (HSDP), and when would you use it instead of full sharding?
- [LLM04-102] How do FSDP wrapping granularity and prefetching affect peak memory and communication overlap?
- [LLM04-103] What is overlapping of communication and computation, and what prevents perfect overlap in ZeRO-3?
- [LLM04-104] Why is ZeRO-3 over slow commodity Ethernet impractical for large models?
- [LLM04-105] How does FSDP differ from DeepSpeed ZeRO?
- [LLM04-106] For a model with Psi parameters trained with Adam in mixed precision, derive the per-GPU memory for ZeRO-0, 1, 2 and 3 with N GPUs.
- [LLM04-107] What does an optimizer like Muon, which needs the full weight matrix, do to ZeRO or FSDP sharding?
