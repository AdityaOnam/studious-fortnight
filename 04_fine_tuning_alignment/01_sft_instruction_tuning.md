---
domain: finetune
topic: sft_instruction_tuning
title: Supervised fine-tuning and instruction tuning
tags: [sft, instruction-tuning, fine-tuning]
count: 166
---
# Supervised fine-tuning and instruction tuning

## Fine-tuning fundamentals and when to fine-tune
- [FT01-001] What is fine-tuning of an LLM, and why is it done instead of just prompting the base pre-trained model?
- [FT01-002] How do pre-training and fine-tuning differ in objective, data, scale and learning-rate regime?
- [FT01-003] What are the different types of LLM fine-tuning?
- [FT01-004] Walk me through how you would fine-tune a pre-trained model for a specific task.
- [FT01-005] Explain transfer learning in the context of Transformers and how it underpins fine-tuning.
- [FT01-006] What is the difference between pre-training, supervised fine-tuning and preference optimisation in terms of data, loss and what each changes?
- [FT01-007] What can fine-tuning do that in-context learning fundamentally cannot?
- [FT01-008] When should you fine-tune instead of improving the prompt, and what signs suggest you are fine-tuning prematurely?
- [FT01-009] What are the strengths and limitations of full fine-tuning?
- [FT01-010] Compare full-parameter fine-tuning with parameter-efficient fine-tuning in cost, quality and risk.
- [FT01-011] When is full fine-tuning preferable to parameter-efficient methods, considering compute, storage and forgetting?
- [FT01-012] You are adapting a pretrained model to a new task. What do you freeze, what do you train, and how do you decide?
- [FT01-013] What are the typical failure modes of a team that fine-tunes a model before trying prompting and evaluation baselines?
- [FT01-014] What are common challenges encountered when fine-tuning LLMs in practice?
- [FT01-015] You have a fixed budget. How do you decide between fine-tuning a small model and prompting a large one for a narrow task?
- [FT01-016] How do you future-proof a fine-tuning investment against base-model churn?

## Instruction tuning and chat templates
- [FT01-017] What is instruction tuning, and why is it important for making a base model usable as a chat assistant?
- [FT01-018] What actually happens during supervised fine-tuning? What role do chat templates and special tokens play?
- [FT01-019] What are the benefits of instruction tuning for zero-shot generalization to unseen tasks?
- [FT01-020] What does a single SFT record look like, and how do single-turn and multi-turn formats differ?
- [FT01-021] What is the difference between an instruction-tuned model and a chat-tuned model?
- [FT01-022] What problem do chat templates solve, and what goes wrong when they are ignored?
- [FT01-023] What is a chat template mismatch between training and inference, and how does it silently ruin results?
- [FT01-024] How do you keep the system prompt and chat template consistent between training and inference when fine-tuning a chat model for a narrow task?
- [FT01-025] How would you catch a chat template mismatch before deploy, both in CI and across a serving fleet?
- [FT01-026] What requirements does an instruction format impose when fine-tuning a domain model (templates, special tokens, loss masking)?
- [FT01-027] Why must the end-of-sequence token appear in the training targets, and what happens if it is missing or masked out?
- [FT01-028] Your fine-tuned model never stops generating or echoes the prompt back, although data and loss curve looked fine. What are the top suspects?
- [FT01-029] Would you fine-tune a base model or an instruct model? How does that choice change your data and recipe?
- [FT01-030] Why can training a base versus an instruct checkpoint on the same data give different results?
- [FT01-031] How would you teach a model to follow a system prompt reliably through SFT?
- [FT01-032] You want the same fine-tuned model to follow several output formats depending on the system prompt. How do you design the data?

## Loss masking, packing and multi-turn formats
- [FT01-033] What is loss masking in SFT, and why is the loss typically computed only on assistant tokens? What goes wrong if you also train on the prompt?
- [FT01-034] How would you verify loss masking is correct before launching an SFT run?
- [FT01-035] In a multi-turn SFT dataset, would you train on all assistant turns or only the final one? What is the tradeoff?
- [FT01-036] How would you fine-tune a model for multi-turn dialogue, and how do you construct training samples from conversations?
- [FT01-037] When a conversation includes tool calls or function outputs, which tokens should receive loss and which should be masked?
- [FT01-038] Why does padding side matter in training versus batched generation, and how do attention masks interact with padding?
- [FT01-039] Explain sequence packing in SFT. What is the cross-sequence attention contamination problem and how is it solved?
- [FT01-040] What bugs arise from packing when attention masks or loss masks are handled incorrectly?
- [FT01-041] What breaks if you pack sequences in SFT but forget to reset position IDs?
- [FT01-042] Why is cross-sequence attention contamination from packing worse on templated datasets than on diverse ones?
- [FT01-043] How can you optimize SFT batches and samples for throughput and quality, for example packing, length bucketing, or dropping contradictory examples?
- [FT01-044] A few very long examples dominate your SFT token count. How do the loss normalization choices (per-token versus per-sample) change what the model learns?

## Building SFT datasets
- [FT01-045] How do you prepare a dataset for fine-tuning an LLM?
- [FT01-046] What does SFT need as data, and how do you build a high-quality, diverse instruction dataset (sources, formatting, deduplication, quality filtering)?
- [FT01-047] How do you create fine-tuning datasets for question answering?
- [FT01-048] How would you prepare and quality-check a fine-tuning dataset from raw support transcripts?
- [FT01-049] You have 50k support tickets. What is the strongest data move before fine-tuning a 7B model?
- [FT01-050] How much data do you need to fine-tune a model? How do you find the point of diminishing returns, and why does quality often beat quantity?
- [FT01-051] What is the quality hierarchy of SFT data, and why does a small high-quality set often beat a large noisy one?
- [FT01-052] What is the LIMA hypothesis, and how does it influence how much SFT data you collect?
- [FT01-053] You have 2M scraped instruction pairs, while a competitor shipped a strong model trained on about 8k curated ones. Where do you start?
- [FT01-054] You have 100k scraped examples of mixed quality. What is your pipeline before training?
- [FT01-055] Where would you source data for domain-specific continued pretraining and instruction tuning, and how would you vet its quality?
- [FT01-056] Two expert annotators persistently disagree on about 12% of your legal SFT labels. What is the senior move?
- [FT01-057] Your fine-tuned LLM produces factually wrong outputs because of training data quality problems. How do you fix it?
- [FT01-058] How do you improve a model so that it answers only when there is sufficient context to do so?
- [FT01-059] How would you build a fine-tuning dataset from production traffic without licensing or privacy problems?
- [FT01-060] How do you prevent feedback-loop bias when training on the model's own accepted drafts?
- [FT01-061] How do you split an SFT dataset into train, validation and test sets so that multi-turn conversations or the same user never leak across splits?
- [FT01-062] How do you decide how many refusal or "I don't know" examples to include, and what happens if there are too many?
- [FT01-063] What style and formatting inconsistencies in SFT data cause erratic output formats, and how do you detect them?
- [FT01-064] How would you set up an annotation process and guidelines for writing SFT responses by humans, and how do you measure annotator quality?

## Data selection, deduplication and synthetic data
- [FT01-065] Why do you deduplicate fine-tuning data, and how would you actually do it?
- [FT01-066] Why is MinHash preferred over pairwise cosine similarity for deduplication at scale?
- [FT01-067] How would you pick the Jaccard threshold for near-duplicate removal rather than just taking 0.8 on faith?
- [FT01-068] How would you detect that near-duplicates in the fine-tuning data are hurting you?
- [FT01-069] How do duplicated training examples masquerade as extra epochs?
- [FT01-070] You have 500k instruction examples of mixed quality and budget to train on 20k. How do you choose the 20k?
- [FT01-071] When selecting instruction data with an LLM judge, how do you handle a judge that shares a base with your target model and prefers its own style?
- [FT01-072] What changes in instruction data selection if the 500k examples come from 4 sources with very different quality profiles?
- [FT01-073] How was Alpaca built from self-instruct data, and what risks come with training on model-generated instructions?
- [FT01-074] Describe the self-instruct data generation pipeline: seed tasks, instruction generation, filtering and deduplication.
- [FT01-075] What are the benefits and risks of fine-tuning with synthetic data generated by a stronger model?
- [FT01-076] Your synthetic SFT set scores great on your in-distribution eval but the model is brittle on slightly unusual real queries. What is the most likely cause?
- [FT01-077] How do you keep synthetic instruction data diverse and avoid mode collapse in style and topics?
- [FT01-078] How would you use rejection sampling or best-of-n filtering to turn model generations into an SFT dataset?
- [FT01-079] What are the licensing and terms-of-service concerns when distilling SFT data from a proprietary model's outputs?
- [FT01-080] How would you decontaminate your SFT data against evaluation benchmarks, and why can paraphrased leakage evade exact-match filters?

## Hyperparameters, training dynamics and compute
- [FT01-081] What are the key hyperparameters for fine-tuning (learning rate, epochs, batch size, LoRA rank), and what are sensible starting values?
- [FT01-082] How do you pick the learning rate for fine-tuning, and why is it usually much lower than for pretraining?
- [FT01-083] What is the effect of a fine-tuning learning rate that is too high, and how would you recognize it from training curves?
- [FT01-084] What learning-rate schedule, warmup and weight decay would you use for SFT, and why?
- [FT01-085] How do you decide the number of epochs for SFT and detect over-training of an instruction-tuned model?
- [FT01-086] How would you run hyperparameter experiments for fine-tuning with limited compute?
- [FT01-087] How do you prevent overfitting during fine-tuning?
- [FT01-088] How do you tell that a fine-tune is overfitting? What are the signals?
- [FT01-089] Your fine-tuned model memorized training data verbatim instead of learning patterns. How do you fix it?
- [FT01-090] How do you tell whether a fine-tuned model is overfitting, leaking test data, or simply showing evaluation noise?
- [FT01-091] Your fine-tuning loss curve has a spike at step 50 and never recovers. What do you check?
- [FT01-092] Your eval loss rises after epoch 1 but human raters prefer the epoch-3 checkpoint. Which do you ship and why?
- [FT01-093] Why does a larger effective batch size often call for a different learning rate in fine-tuning, and how do you choose it?
- [FT01-094] What is gradient accumulation, and how does it help with fine-tuning large models?
- [FT01-095] What are the possible options to speed up LLM fine-tuning?
- [FT01-096] How much GPU memory does full-parameter fine-tuning of a 7B model need with Adam in mixed precision, and what drives the estimate?
- [FT01-097] How do you handle out-of-memory errors during fine-tuning without changing the model, and why does memory scale the way it does?
- [FT01-098] How do DDP, FSDP and ZeRO differ in what they replicate or shard during fine-tuning?
- [FT01-099] What are the trade-offs between bf16 and fp16 for fine-tuning, and what does gradient checkpointing cost and save?
- [FT01-100] Estimate the GPU-hours needed to fully fine-tune a 7B model on 1B tokens. What assumptions do you make?

## Continued pretraining, domain adaptation and knowledge injection
- [FT01-101] What is continued pre-training, and when would you use it?
- [FT01-102] Why use continued pretraining rather than just mixing domain data into the SFT set?
- [FT01-103] What is the difference between continued pretraining and SFT, and when do you need domain knowledge injection?
- [FT01-104] What is domain adaptation, and how does it differ from task adaptation?
- [FT01-105] How do you fine-tune a model for a specific domain such as legal, medical or finance?
- [FT01-106] What preparation is needed for continued pretraining: data collection, cleaning, tokenization, mixing ratio and learning rate?
- [FT01-107] What learning-rate and warmup strategy do you use when continuing pretraining of a converged model so you do not destabilize it?
- [FT01-108] How is an incremental-pretraining pipeline organized end to end, from raw domain documents to a checkpoint ready for SFT?
- [FT01-109] How can continued pretraining be made to inject more domain knowledge, for example via data mixing, repeated exposure and curriculum?
- [FT01-110] Design the data mixture for adapting an 8B model to clinical notes. What fractions and why?
- [FT01-111] How would you check that continued pretraining actually added knowledge rather than style?
- [FT01-112] Why does SFT inject knowledge so poorly compared with continued pretraining, and what does the evidence say about SFT teaching knowledge versus style?
- [FT01-113] Why does SFT on new facts encourage hallucination?
- [FT01-114] Why is fine-tuning unreliable for knowledge injection, mechanistically?
- [FT01-115] How would you structure fine-tuning data so a set of product facts is retrievable from any direction, not just the order seen in training?
- [FT01-116] What is knowledge editing, and how does it differ from fine-tuning, RAG and machine unlearning?
- [FT01-117] You are fine-tuning on a domain full of jargon and someone suggests adding new tokens to the tokenizer. What can go wrong, and how do you handle vocabulary changes correctly?
- [FT01-118] How would you verify after training that newly added tokens actually learned anything?
- [FT01-119] A regional government wants an assistant in a low-resource language with only a few thousand sentences of clean text. How do you adapt a model to it?

## Catastrophic forgetting and data mixtures
- [FT01-120] What is catastrophic forgetting in LLM fine-tuning, and why is it a concern?
- [FT01-121] How do you prevent a model from losing general capabilities during fine-tuning?
- [FT01-122] Which techniques (replay, regularization, EWC, parameter-efficient methods, lower learning rates) limit forgetting in fine-tuned LLMs, and what are their costs?
- [FT01-123] After fine-tuning on a customer's task, target accuracy is up but the model got worse at everything else. What happened and what do you do?
- [FT01-124] Your fine-tuned model regressed on general instruction-following. What happened and what do you do?
- [FT01-125] Your fine-tune lifted task accuracy on support tickets but MMLU dropped 6 points. What does a senior engineer do?
- [FT01-126] Your fine-tune improves the task metric by 15% but drops an internal instruction-following eval by 5%. Do you ship it?
- [FT01-127] How do you mix replay data from the general distribution with task data, and how do you pick the ratio?
- [FT01-128] How do you construct the data mixture for a fine-tune to prevent capability regressions, and how do you validate it?
- [FT01-129] Why can interleaving data mixtures beat sequential training phases in fine-tuning?
- [FT01-130] Your general-data slice fixes MMLU but the task metric drops 3 points. What are your options?
- [FT01-131] How does the right data mixture ratio differ between SFT and continued pretraining?
- [FT01-132] What does your held-out set need to contain to detect catastrophic forgetting on a document-extraction LoRA?
- [FT01-133] If you do not have access to the original instruct model's training data, how can you build replay data to protect its existing behaviour?
- [FT01-134] Why do lower learning rates and fewer epochs reduce forgetting, and what do you give up?

## Evaluating and debugging fine-tuned models
- [FT01-135] How do you evaluate the performance of a fine-tuned LLM?
- [FT01-136] How do you evaluate a model before and after fine-tuning?
- [FT01-137] How would you evaluate a fine-tuned model against both the base model and a strong prompted baseline?
- [FT01-138] How do you prove the fine-tune got better, not just different?
- [FT01-139] A team fine-tuned a model on 300 noisy examples and says "it feels better". What do you ask for?
- [FT01-140] How would you build an evaluation set for a domain-tuned model, and how do you keep it from leaking into the training data?
- [FT01-141] How do you use an LLM judge to compare a fine-tuned model with a baseline, and how do you control for position and verbosity bias?
- [FT01-142] How many evaluation examples do you need to claim a fine-tuned model is better, and how do you quantify the uncertainty?
- [FT01-143] How do you evaluate that a fine-tuned model has not regressed on safety and general capabilities?
- [FT01-144] If you fine-tune an instruct model and its multi-turn behaviour degrades, how would you detect that before shipping?
- [FT01-145] Your SFT loss is decreasing nicely but users say the model got worse. What happened?
- [FT01-146] After SFT a model seems worse or "dumber" even though the task metric improved. What are the likely causes and what is your diagnostic plan?
- [FT01-147] Your fine-tuned model's training loss looked great, but outputs in production are worse than the base model. Walk me through your debugging process.
- [FT01-148] What single artefact would you log at training time to make debugging a fine-tuned model's production regressions easy later?
- [FT01-149] How would you set up a regression suite and golden set so that every new fine-tuning iteration is compared against the previous one?
- [FT01-150] How would you roll out a fine-tuned model safely to production, for example with shadow traffic, A/B testing and rollback criteria?

## Special cases and end-to-end design
- [FT01-151] Design an end-to-end fine-tuning pipeline for a customer-support model at a mid-size company. Walk me through data, training, evaluation, deployment and iteration.
- [FT01-152] Walk me through a post-training recipe to turn a pretrained base model into a personalised assistant.
- [FT01-153] How would you fine-tune a model to emit reliable structured output such as JSON that conforms to a schema?
- [FT01-154] How would you fine-tune a model for tool use or function calling, and how do you build and validate the training data?
- [FT01-155] You fine-tune a reasoning model that writes a thinking block before its final answer. How do you build the SFT data, and what breaks if you train on final answers only?
- [FT01-156] Your domain experts gave you answer-only labels. How do you get reasoning traces without inventing reasoning the experts never used?
- [FT01-157] How would you shorten a reasoning model's thinking without losing accuracy?
- [FT01-158] How would you train a single model to support both a thinking mode and a non-thinking mode with a caller-settable thinking budget?
- [FT01-159] What changes when you fine-tune a mixture-of-experts model instead of a dense one?
- [FT01-160] Would you freeze or train the router for a 5k-example SFT run of an MoE model, and what evidence would change your mind?
- [FT01-161] What would you do differently if the base model and instruct model have different tokenizers?
- [FT01-162] What breaks if you add tokens to a model whose embeddings are tied and quantized to 4-bit?
- [FT01-163] When do you fine-tune a vision-language model instead of prompting it, and what exactly do you unfreeze?
- [FT01-164] You fine-tuned a model on narrow, harmless-looking domain data and it now complies with requests it used to refuse. Why, and how do you ship fine-tunes safely?
- [FT01-165] A customer wants to fine-tune your hosted model on their own data. Which safety checks do you run, and which do you require them to run?
- [FT01-166] How do you handle fine-tuning on customer data that contains regulated or personal information?
