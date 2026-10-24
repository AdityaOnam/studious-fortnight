---
domain: coding
topic: ml_llm_coding_problems
title: ML / LLM coding problems (titles only)
tags: [coding, from-scratch, pytorch, implementation]
count: 91
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
