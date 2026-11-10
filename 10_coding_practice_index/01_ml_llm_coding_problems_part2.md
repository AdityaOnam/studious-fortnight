---
domain: coding
topic: ml_llm_coding_problems
title: ML / LLM coding problems (titles only)
tags: [coding, from-scratch, pytorch, implementation]
count: 140
part: 2/2
---
# ML / LLM coding problems (titles only) (part 2)

## Tokenization and decoding
- [CODE01-105] Implement BPE tokenizer training and encoding from scratch.
- [CODE01-106] Implement the byte-level fallback and decoding path of a BPE tokenizer so that any string round-trips.
- [CODE01-107] Write code to measure a tokenizer's fertility across languages, and say what you would do with the result.
- [CODE01-108] Implement temperature sampling over a logits vector.
- [CODE01-109] Implement top-k sampling.
- [CODE01-110] Implement top-p (nucleus) sampling.
- [CODE01-111] Implement temperature, top-k and top-p sampling together over a logits tensor.
- [CODE01-112] Implement min-p sampling and compare its behaviour with top-p on a flat versus a peaked distribution.
- [CODE01-113] Implement a repetition penalty and a frequency penalty applied to logits during generation.
- [CODE01-114] Implement an autoregressive generate loop with greedy decoding, EOS handling, stop sequences and batched sequences that finish at different times.
- [CODE01-115] Implement beam search with length normalization for a causal language model, and say when a production system would use it.
- [CODE01-116] Implement constrained decoding that masks logits so the output always follows a given JSON schema or regular expression.

## Efficient inference, kernels and distributed training
- [CODE01-117] Implement an append-only KV cache for autoregressive decoding of a small Transformer and show it matches full recomputation.
- [CODE01-118] Add a KV cache to causal multi-head attention and write the single-token decode path. Where is RoPE applied, and why only to q and k?
- [CODE01-119] Implement single-step decode with a KV cache in PyTorch, then describe what changes for a long-context serving system.
- [CODE01-120] Modify scaled dot-product attention for grouped-query attention. How does the causal mask interact with a KV cache at inference?
- [CODE01-121] Estimate the KV cache memory for a given model configuration, batch size and context length, then write a function that computes it.
- [CODE01-122] Implement the online softmax algorithm in pure PyTorch.
- [CODE01-123] Implement the tiled FlashAttention algorithm with online softmax in pure PyTorch, processing keys in blocks.
- [CODE01-124] Write a fused softmax kernel in Triton.
- [CODE01-125] Implement FlashAttention-2 in Triton.
- [CODE01-126] Implement Ring Attention for long contexts.
- [CODE01-127] Implement the block manager for a paged KV cache: allocate, append, free, and copy-on-write prefix sharing.
- [CODE01-128] Implement prefix caching so that requests sharing a prompt prefix reuse KV blocks.
- [CODE01-129] Implement speculative decoding with a draft model and the accept/reject correction step.
- [CODE01-130] Implement continuous batching for LLM inference.
- [CODE01-131] Build a complete LLM inference engine.
- [CODE01-132] Implement per-channel symmetric int8 weight quantization and dequantization for a linear layer.
- [CODE01-133] Implement gradient checkpointing.
- [CODE01-134] Implement a tensor-parallel linear layer that splits a weight matrix across devices (column then row parallel).
- [CODE01-135] Implement Fully Sharded Data Parallel (FSDP) from scratch.

## Alignment, RL, generative and vision models
- [CODE01-136] Implement a LoRA linear layer that wraps a frozen linear layer and supports merging.
- [CODE01-137] Implement a QLoRA-style layer with a frozen 4-bit quantized base weight and a trainable low-rank adapter.
- [CODE01-138] Implement the supervised fine-tuning loss with prompt tokens masked out so only response tokens contribute.
- [CODE01-139] Implement a reward model with the Bradley-Terry pairwise preference loss.
- [CODE01-140] Implement the DPO loss given policy and reference log-probabilities for chosen and rejected responses.
- [CODE01-141] Implement REINFORCE with a baseline on a simple environment.
- [CODE01-142] Implement the PPO clipped objective and a GAE advantage computation for a batch of trajectories.
- [CODE01-143] Implement PPO for RLHF, including a per-token KL penalty against a reference model.
- [CODE01-144] Implement GRPO (Group Relative Policy Optimization).
- [CODE01-145] Implement a symmetric contrastive (InfoNCE) loss for paired embeddings.
- [CODE01-146] Implement a CLIP training step with a contrastive loss over image and text batches.
- [CODE01-147] Implement DDPM (denoising diffusion) training and sampling from scratch.
- [CODE01-148] Implement the classifier-free guidance combination of conditional and unconditional predictions.
- [CODE01-149] Implement DDIM sampling with classifier-free guidance.
- [CODE01-150] Implement a variational autoencoder with the reparameterization trick and the ELBO loss.
- [CODE01-151] Implement a Vision Transformer with masked autoencoder (MAE) pretraining.
- [CODE01-152] Implement a Swin Transformer block with shifted window attention.
- [CODE01-153] Implement a selective state space model (Mamba block).
- [CODE01-154] Implement non-maximum suppression, then vectorise it.
- [CODE01-155] Implement intersection-over-union for batches of bounding boxes.

## Retrieval and RAG
- [CODE01-156] Create sentence embeddings from an LLM's hidden states and choose a pooling strategy.
- [CODE01-157] Implement cosine similarity, dot product and Euclidean distance functions from scratch.
- [CODE01-158] Compute pairwise cosine similarity between tensors of shape [N, D] and [M, D].
- [CODE01-159] Compute the masked mean of a [B, T, D] tensor using a [B, T] mask.
- [CODE01-160] Implement exact cosine top-k semantic search over embeddings from scratch for a RAG system.
- [CODE01-161] Implement cosine similarity search over embeddings, then explain why you would not ship it.
- [CODE01-162] Implement a BM25 scorer and a simple retriever over a small corpus.
- [CODE01-163] Implement hybrid retrieval that combines BM25 and dense scores with reciprocal rank fusion.
- [CODE01-164] Write code for different text chunking strategies (fixed-size, recursive, semantic).
- [CODE01-165] Implement a text chunker with overlap that never splits a semantic unit.
- [CODE01-166] Build a document parser that extracts text from PDFs and splits it into chunks.
- [CODE01-167] Implement a basic RAG pipeline: chunking, embedding, vector search, and prompt assembly with a vector database.
- [CODE01-168] Implement a simple re-ranker for search results.
- [CODE01-169] Implement maximal marginal relevance to diversify retrieved passages.
- [CODE01-170] Implement recall@k, MRR and NDCG@k for evaluating a retriever.
- [CODE01-171] Implement a locality-sensitive hashing index for approximate nearest neighbor search and measure its recall against exact search.
- [CODE01-172] Implement metadata-filtered vector search and explain the pre-filter versus post-filter trade-off in code.
- [CODE01-173] Implement a groundedness check that flags answer sentences not supported by the retrieved context.

## LLM application plumbing and agents
- [CODE01-174] Implement a prompt template system with variable substitution.
- [CODE01-175] Build a simple prompt versioning system.
- [CODE01-176] Implement token counting and context window management that truncates or drops history to fit a budget.
- [CODE01-177] Implement conversation memory for a chatbot using a sliding window with a token budget, summary memory and a full buffer.
- [CODE01-178] Implement streaming responses for an LLM API.
- [CODE01-179] Write a parser for server-sent-event LLM token streams that handles arbitrary chunk boundaries and yields complete JSON events.
- [CODE01-180] Make a streamed-response parser async with a per-event timeout, and describe how to test chunk-boundary edge cases deterministically.
- [CODE01-181] Implement a retry mechanism with exponential backoff and jitter for LLM API calls.
- [CODE01-182] Write an async batch processor that runs an LLM call over 50,000 documents with a concurrency limit, retries with jitter and error isolation.
- [CODE01-183] Implement a caching layer for LLM responses.
- [CODE01-184] Implement semantic caching for LLM queries that reuses responses for similar queries.
- [CODE01-185] Build an evaluation pipeline for LLM outputs using LLM-as-a-judge.
- [CODE01-186] Write code to detect prompt injection attempts in user inputs.
- [CODE01-187] Implement an LLM output guardrails system that checks for off-topic responses and PII leakage.
- [CODE01-188] Write a function-calling (tool use) handler for an LLM API.
- [CODE01-189] Implement validation of JSON tool arguments against a schema.
- [CODE01-190] Implement a permission-aware tool registry for an LLM agent.
- [CODE01-191] Implement a bounded agent loop with tool dispatch, error handling, a step budget and safety checks.
- [CODE01-192] Implement a ReAct agent that calls two tools and recovers from a tool error.
- [CODE01-193] Implement a planner and executor for an agent with a clean boundary and tracing.
- [CODE01-194] Implement retry logic with idempotency keys for tool calls that have side effects.
- [CODE01-195] Build a multi-agent system where agents have different roles and collaborate on a task.

## More classical ML from scratch
- [CODE01-196] Implement a regression tree using recursive binary splitting on squared error.
- [CODE01-197] Implement cost-complexity pruning for a trained decision tree.
- [CODE01-198] Compute impurity-based feature importances from a trained decision tree.
- [CODE01-199] Implement AdaBoost with decision stumps from scratch.
- [CODE01-200] Compute the out-of-bag error of a random forest from its bootstrap samples.
- [CODE01-201] Implement a Gaussian Naive Bayes classifier from scratch.
- [CODE01-202] Implement a categorical Naive Bayes classifier with Laplace smoothing.
- [CODE01-203] Implement distance-weighted k-nearest neighbors and compare it with uniform voting.
- [CODE01-204] Implement a one-vs-one multiclass classifier on top of a binary SVM.
- [CODE01-205] Implement mini-batch k-means.
- [CODE01-206] Implement the silhouette coefficient from scratch for a given clustering.
- [CODE01-207] Implement the Apriori algorithm to find frequent itemsets and generate association rules.
- [CODE01-208] Implement the Local Outlier Factor algorithm from scratch.
- [CODE01-209] Write a function that flags outliers with the interquartile range (IQR) rule.
- [CODE01-210] Implement user-based collaborative filtering with Pearson correlation from scratch.
- [CODE01-211] Implement item-item collaborative filtering with cosine similarity and produce top-N recommendations.

## Feature selection, explainability and evaluation code
- [CODE01-212] Select the top-k features by mutual information with the target, implementing the estimate for discrete features.
- [CODE01-213] Implement recursive feature elimination around any estimator that exposes coefficients or importances.
- [CODE01-214] Write a function that drops one feature from every highly correlated pair above a threshold.
- [CODE01-215] Implement the hashing trick for high-cardinality categorical features.
- [CODE01-216] Compute a variance inflation factor for each predictor.
- [CODE01-217] Compute exact Shapley values for a single prediction of a model with a handful of features.
- [CODE01-218] Implement a simple LIME-style local explanation by fitting a weighted linear surrogate on perturbed samples.
- [CODE01-219] Compute a partial dependence curve for one feature of a trained model.
- [CODE01-220] Compute learning curves of training and validation score as the training set grows.

## Optimization, statistics and linear algebra code
- [CODE01-221] Implement AdaGrad and RMSprop optimizers from scratch.
- [CODE01-222] Minimize a non-convex function with simulated annealing.
- [CODE01-223] Implement a genetic algorithm that evolves a random string toward a target string.
- [CODE01-224] Implement roulette-wheel and rank-based selection, single-point crossover and mutation for a genetic algorithm.
- [CODE01-225] Implement the Metropolis-Hastings algorithm to sample from an unnormalized posterior.
- [CODE01-226] Implement Welch's two-sample t-test from scratch.
- [CODE01-227] Implement a chi-squared test of independence on a contingency table.
- [CODE01-228] Implement matrix inversion with Gauss-Jordan elimination and partial pivoting.
- [CODE01-229] Implement power iteration to find the dominant eigenvalue and eigenvector of a matrix.
- [CODE01-230] Compute gradients of linear regression by hand and verify them against autograd.

## Time series, sequence and vision code
- [CODE01-231] Implement simple exponential smoothing for a time series.
- [CODE01-232] Compute the autocorrelation function of a time series from scratch.
- [CODE01-233] Implement an efficient rolling-window mean in NumPy without Python loops.
- [CODE01-234] Implement a character-level RNN in NumPy that generates text from a seed.
- [CODE01-235] Implement an n-gram language model with smoothing from scratch.
- [CODE01-236] Implement the forward pass of a 2D convolution in NumPy, including stride and padding.
- [CODE01-237] Implement Sobel edge detection, then outline the remaining Canny steps of non-maximum suppression and hysteresis.
- [CODE01-238] Implement the gradient penalty term of WGAN-GP.

## Reinforcement learning code
- [CODE01-239] Compute discounted returns for a sequence of rewards.
- [CODE01-240] Implement value iteration for a small MDP given its transition matrix.
- [CODE01-241] Implement a tabular Q-learning agent with decaying epsilon-greedy exploration for a grid world.
- [CODE01-242] Implement a SARSA agent and compare its learned policy with Q-learning on the same environment.

## Feature extraction and autograd code
- [CODE01-243] Implement a custom torch.autograd.Function, for example for arctanh, with an analytical backward pass, and verify it with gradcheck.
- [CODE01-244] Turn a pretrained torchvision ResNet-34 into a 512-dimensional feature extractor, with the correct ImageNet preprocessing.
