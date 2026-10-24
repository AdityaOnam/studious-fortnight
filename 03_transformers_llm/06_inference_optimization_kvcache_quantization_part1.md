---
domain: llm
topic: inference_optimization_kvcache_quantization
title: Inference optimization, KV cache, quantization
tags: [inference, kv-cache, quantization, vllm]
count: 107
part: 1/3
---
# Inference optimization, KV cache, quantization (part 1)

## Inference fundamentals and metrics
- [LLM06-001] How does LLM inference differ from LLM training in compute pattern, memory use, and optimization goals?
- [LLM06-002] Walk me through what happens inside an LLM server from the moment a request arrives until the last token is streamed back.
- [LLM06-003] How does token streaming work, and why does it change how users perceive latency?
- [LLM06-004] What are TTFT, TPOT (inter-token latency), end-to-end latency, and throughput in LLM serving, and what drives each one?
- [LLM06-005] How do TTFT, TPOT, and throughput trade off against each other when you tune batch size?
- [LLM06-006] What are reasonable TTFT and per-token latency targets for an interactive chat product, and how would you turn them into SLOs?
- [LLM06-007] How do you measure LLM inference performance, and what would you report beyond average tokens per second?
- [LLM06-008] Describe the throughput-versus-latency trade-off curve of an LLM server and explain what goodput is.
- [LLM06-009] Why does queueing delay explode as an LLM server approaches saturation?
- [LLM06-010] Besides model compute, what are the main sources of latency in an LLM serving stack?
- [LLM06-011] What are the main challenges in LLM inference?
- [LLM06-012] What are MFU and MBU, and which one is the more meaningful efficiency metric for decode?
- [LLM06-013] How would you compare tokens-per-second fairly across models that use different tokenizers?
- [LLM06-014] Why do API providers usually charge more for output tokens than for input tokens?
- [LLM06-015] Your chat product has acceptable TTFT, but users complain that text "types out" too slowly. Which bottleneck do you target?
- [LLM06-016] How do you optimize TTFT versus TPOT, and why do the two goals often conflict?

## Prefill, decode, and the roofline
- [LLM06-017] What is autoregressive generation, and how do the prefill and decode phases differ in compute and memory behavior?
- [LLM06-018] Why is LLM generation so much slower per token than a classifier's single forward pass?
- [LLM06-019] Why is the first token slower to appear than the tokens after it?
- [LLM06-020] Explain arithmetic intensity and the roofline model as applied to LLM inference.
- [LLM06-021] Why is prefill compute-bound while decode is memory-bandwidth-bound?
- [LLM06-022] Why is decode memory-bandwidth-bound? Walk through the numbers on an H100.
- [LLM06-023] Why is decode throughput bounded by memory bandwidth, and how does GQA change the arithmetic?
- [LLM06-024] Do the roofline math: how many tokens per second can one H100 produce for a 70B model at batch size 1?
- [LLM06-025] Why doesn't a faster GPU with the same memory bandwidth speed up batch-1 decode?
- [LLM06-026] During decode your GPU shows low compute utilization yet is clearly the bottleneck. What is the most accurate explanation?
- [LLM06-027] Why does batching raise decode throughput so dramatically, and why doesn't the KV cache read amortise across the batch the way weight reads do?
- [LLM06-028] At roughly what batch size does LLM decode become compute-bound?
- [LLM06-029] At what batch size does KV cache traffic overtake weight traffic in decode, and how does GQA shift that crossover?
- [LLM06-030] Why does KV cache bandwidth, rather than FLOPs, dominate decode latency?
- [LLM06-031] Where does attention sit on the roofline, compared with the MLP GEMMs, as context length grows?
- [LLM06-032] How does moving to FP8 shift the roofline ridge point?
- [LLM06-033] Why does decode need a differently shaped attention kernel than prefill, and what does a kernel like FlashDecoding parallelize over?
- [LLM06-034] How does FlashAttention reduce memory traffic, and why does it matter more for prefill than for decode?
- [LLM06-035] Why does per-token decode latency still grow with context length even when a KV cache is used?
- [LLM06-036] Request A has a 4,000-token prompt and a 50-token answer; request B has a 400-token prompt and a 2,000-token answer. Which feels slower end-to-end, and which costs more?
- [LLM06-037] In LLM serving, what does a long-context request cost you that a long-generation request does not?
- [LLM06-038] What are the main bottlenecks in a typical LLM inference pipeline on a modern GPU?

## KV cache basics and sizing
- [LLM06-039] What is the KV cache, and why does it make autoregressive generation faster?
- [LLM06-040] In token-by-token decoding, which of Q, K, and V are cached, and why is there no point in caching queries?
- [LLM06-041] How does KV cache memory scale with context length, batch size, and model dimensions, and what happens if the context window grows 4x?
- [LLM06-042] Derive the per-token KV cache memory formula and compute it for a concrete model.
- [LLM06-043] Why does context length become a memory problem before it becomes a compute problem during decode?
- [LLM06-044] A Llama-7B FP16 service at 4k context runs at batch 1 on a 24 GB GPU but OOMs at batch 8. What changed, and what is the cheapest fix?
- [LLM06-045] How much memory does the KV cache add for 32 concurrent 8K-context sequences on a 70B model?
- [LLM06-046] Serve Llama-2-70B (GQA, 8 KV heads, 80 layers, head dim 128, FP16) at 32k context with batch 4. Roughly how much GPU memory does the KV cache alone need?
- [LLM06-047] Ballpark the KV cache size of a 70B-class model at 128K context.
- [LLM06-048] A 70B-class model at 128k context does not fit in memory because of the KV cache. What do you do?
- [LLM06-049] Redo the 128k-context KV estimate for a 70B-class model with FP8 KV cache and MQA. What is the new maximum batch size?
- [LLM06-050] Estimate the KV cache needed to serve a large model, and explain how it constrains batch size and context length.
- [LLM06-051] Estimate the KV cache footprint of a Llama-3-70B-class model and explain what PagedAttention fixes.
- [LLM06-052] How would you size the KV cache for a new open-weight model you have not served before?
- [LLM06-053] Your capacity plan used "2 x layers x kv_heads x head_dim x bytes" per token for every model in the fleet. What breaks for MLA, sliding-window, or hybrid models?
- [LLM06-054] In LLaMA-2 style inference code, how are the KV cache tensors laid out and updated at each decoding step?
- [LLM06-055] Product wants a 1M-token context window on a self-hosted model. What breaks in serving, and how do you make it work?
- [LLM06-056] Why does KV cache memory, not FLOPs, often become the real bottleneck at 1M-token contexts?

## Architectural levers on KV cache size
- [LLM06-057] Why does grouped-query attention shrink the KV cache but barely change the weight count, and what does it trade off?
- [LLM06-058] How does Multi-head Latent Attention (MLA) compress the KV cache, and what does it cost at inference time?
- [LLM06-059] Would you expect MLA or KV cache quantization to be the better first move on an existing GQA model?
- [LLM06-060] A 70B MHA model is too KV-heavy for your target context and concurrency, and you have about 5% of the original pre-training compute. What is the best move?
- [LLM06-061] With an open-source base model that already uses GQA-8, which KV reduction techniques can you still apply after training, and which need pretraining?
- [LLM06-062] How does sliding-window attention change the KV cache memory formula, and how would you design the rolling-buffer cache it enables?
- [LLM06-063] Does an MoE model such as Mixtral have different KV cache math from a dense model with the same attention setup, and why do people assume otherwise?
- [LLM06-064] What is an attention sink, why does it exist, and what breaks if you evict it from the KV cache?
- [LLM06-065] What approaches exist for compressing the KV cache itself (eviction, merging, low-rank, quantization), and what are the newer directions?
- [LLM06-066] How do LRU or LFU cache eviction policies relate to KV cache eviction policies in long-context serving?
- [LLM06-067] What memory-saving methods exist specifically for LLM inference?

## PagedAttention and KV memory management
- [LLM06-068] How do you handle the large memory footprint of the KV cache when serving many concurrent requests?
- [LLM06-069] What KV cache memory management problems (fragmentation, over-reservation) do naive serving systems have, and how does PagedAttention solve them?
- [LLM06-070] What is PagedAttention and how does it work?
- [LLM06-071] What is the block table in vLLM, and how does it map logical to physical KV blocks?
- [LLM06-072] How does copy-on-write work in PagedAttention for beam search, parallel sampling, or n-best sampling?
- [LLM06-073] Why does PagedAttention raise throughput rather than single-request latency?
- [LLM06-074] Why does vLLM report such a large throughput gain over naive batching? What is the mechanism-level answer?
- [LLM06-075] What is the trade-off in choosing the block size for a paged KV cache? Why not 1-token blocks, and why not 128?
- [LLM06-076] What does the block-table indirection in paged attention cost inside the attention kernel?
- [LLM06-077] Why does paged allocation of the KV cache help with fragmentation and with admission control?
- [LLM06-078] Why does GPU memory keep growing during LLM serving and stay occupied after requests finish?
- [LLM06-079] Your self-hosted LLM cluster rejects requests with OOM errors under load, yet nvidia-smi shows several GB free per GPU. What is the likely cause and fix?
- [LLM06-080] What happens in vLLM when the KV cache fills up mid-generation, and how does the engine decide which sequence to preempt?
- [LLM06-081] When GPU memory runs out, how do you choose between preempt-and-recompute and swapping KV blocks to CPU?
- [LLM06-082] When would you evict KV cache blocks versus offload them to host memory?
- [LLM06-083] What metric would you alert on to detect KV cache thrashing in an LLM serving system?
- [LLM06-084] How does paged attention interact with a ring-buffer (rolling) KV cache?
- [LLM06-085] What breaks in a paged-attention cache manager when three quarters of the layers keep no per-token KV state?
- [LLM06-086] Why is prefix caching harder with a recurrent (Mamba-style) state than with a KV cache?
- [LLM06-087] Why can't you roll back a Mamba state by 30 tokens the way you drop KV blocks, and what does that cost an agent that edits its own history?
- [LLM06-088] You are moving from a dense transformer to a Mamba-attention hybrid. What changes in your serving stack?

## Prefix caching and KV reuse
- [LLM06-089] How does prefix (prompt) caching relate to the KV cache, and what exactly gets reused?
- [LLM06-090] What is prefix caching (for example RadixAttention), when does it save money, and what invalidates a cached prefix?
- [LLM06-091] Your chatbot shares a long system prompt across most requests and TTFT is high under load. Which lever gives the biggest direct win?
- [LLM06-092] How does a shared multi-thousand-token system prompt change the economics in favour of a cache-centric serving design?
- [LLM06-093] When does RadixAttention outperform plain PagedAttention, and for what workloads?
- [LLM06-094] How does a decoder-only model make KV cache reuse across multi-turn conversations simpler than an encoder-decoder model does?
- [LLM06-095] A chat assistant re-sends a long conversation history every turn. How do you avoid recomputing it, and what are the pitfalls?
- [LLM06-096] What happens to the prefix cache hit rate when a user edits a message at turn 40 or in the middle of a file, and how do you keep the rest usable?
- [LLM06-097] When building the next-turn prompt under a prefix cache, where do you insert retrieved older turns without breaking the cache boundary?
- [LLM06-098] What exactly must go into the cache key for cross-request KV cache reuse?
- [LLM06-099] How would you add hash-based block reuse (prefix caching) to a paged KV cache block manager?
- [LLM06-100] How would you unit-test that a refactor did not silently drop the prefix cache hit rate?
- [LLM06-101] Prefix cache hit rate fell from 80% to 30% after an app release with no infrastructure change. What do you look for first?
- [LLM06-102] What does sliding-window attention do to prefix caching in a multi-turn agent?
- [LLM06-103] How does sequence-axis KV compression interact with prefix caching for agent sessions that keep appending tool output?
- [LLM06-104] Why is context caching sometimes a better choice than RAG for a single 50K-token document queried repeatedly?
- [LLM06-105] What is tiered KV cache offloading across GPU, CPU, and NVMe, and when does loading a cached prefix beat recomputing the prefill?
- [LLM06-106] At what hit rate does an NVMe tier for the KV cache stop paying for itself?
- [LLM06-107] How do distributed KV cache layers such as LMCache and Mooncake Store differ in architecture and role, and how do they share KV across engines?
