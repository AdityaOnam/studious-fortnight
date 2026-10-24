---
domain: llm
topic: inference_optimization_kvcache_quantization
title: Inference optimization, KV cache, quantization
tags: [inference, kv-cache, quantization, vllm]
count: 98
part: 2/3
---
# Inference optimization, KV cache, quantization (part 2)

## Batching and scheduling
- [LLM06-108] What is batch inference, and how does it differ from single-query inference?
- [LLM06-109] How does batching improve GPU efficiency for LLM inference?
- [LLM06-110] What is static batching, and why is it inefficient for variable-length LLM requests?
- [LLM06-111] What is continuous (in-flight) batching, how does it differ from static batching, and why did it become standard?
- [LLM06-112] Compare static, dynamic, and continuous batching strategies for LLM serving.
- [LLM06-113] What new scheduling problems does continuous batching create?
- [LLM06-114] Your serving GPU has plenty of free KV cache memory, yet throughput is poor and requests sit idle waiting for a batch to finish. Which lever helps most?
- [LLM06-115] Why does increasing batch size improve decode throughput only up to a point, and what limits it?
- [LLM06-116] Design the scheduler for a continuous-batching inference engine.
- [LLM06-117] Design a batched inference system where 100 concurrent requests take roughly the same time as one.
- [LLM06-118] What is chunked prefill, and what scheduling problem does it fix?
- [LLM06-119] What is a prefill "stall" in LLM serving, and how does chunked prefill improve tail latency under mixed traffic?
- [LLM06-120] Why does mixing a prefill chunk into a decode batch improve hardware utilization rather than just sharing the pain?
- [LLM06-121] How would you choose the chunk size for chunked prefill?
- [LLM06-122] How do chunked prefill and layered prefill differ, and what scenarios suit each?
- [LLM06-123] What metrics would tell you decode steps are being starved, or that the scheduler is misbehaving, and what would a rising preemption rate indicate?
- [LLM06-124] How would you handle head-of-line blocking from very long requests, for example with priority or SLO-aware scheduling?
- [LLM06-125] Could predicting output length help a batch scheduler, and what could go wrong?
- [LLM06-126] How do you apply admission control and backpressure to an LLM server under overload?

## Speculative decoding and latency tuning
- [LLM06-127] How does speculative decoding work, why does it preserve the target model's output distribution, and what speedup should you expect?
- [LLM06-128] What determines the speedup from speculative decoding, and when does it fail to help or even hurt throughput?
- [LLM06-129] You enabled speculative decoding and saw a latency win at low traffic, but at peak concurrency it got slightly slower. Why?
- [LLM06-130] Which latency metric does speculative decoding improve, and which can it hurt?
- [LLM06-131] How would you measure whether speculative decoding is actually helping in a live deployment?
- [LLM06-132] How does speculative decoding interact with a continuous-batching scheduler when sequences accept different numbers of tokens per step?
- [LLM06-133] Compare draft-model speculative decoding with Medusa or EAGLE-style heads and prompt-lookup (n-gram) speculation.
- [LLM06-134] What are the main options for accelerating LLM inference?
- [LLM06-135] How do you improve inference speed and throughput in production LLM deployments?
- [LLM06-136] How can you accelerate a model's response time without attention approximations such as grouped-query attention?
- [LLM06-137] Why does the decoder generate tokens sequentially, and what techniques reduce its latency?
- [LLM06-138] How would you cut TTFT for a generated answer by half without changing models?
- [LLM06-139] At low batch sizes decode is slower than the bandwidth math predicts and the GPU timeline shows gaps between kernels. What is CPU overhead, and how do CUDA graphs and overlapped scheduling fix it?
- [LLM06-140] Why do CUDA graphs need batch-size buckets, and what does padding to a bucket cost?
- [LLM06-141] How would you confirm from a profile that a latency problem is host overhead rather than memory bandwidth?
- [LLM06-142] What role do custom CUDA kernels and operator fusion play in LLM inference engines?
- [LLM06-143] How much overhead does grammar-constrained (structured output) decoding add, and how do engines reduce it?
- [LLM06-144] How do you make sampling reproducible across different batch sizes on a GPU?

## Disaggregation and KV-aware routing
- [LLM06-145] What is prefill-decode disaggregation, why do large deployments separate the two phases, and what does it cost?
- [LLM06-146] When does disaggregated prefill/decode beat chunked prefill on a single pool?
- [LLM06-147] When is disaggregated prefill/decode serving not worth the operational cost?
- [LLM06-148] Estimate the KV bytes transferred for an 8K-token prompt on a 70B GQA model under disaggregation. Is the transfer a problem on NVLink versus Ethernet?
- [LLM06-149] How does prefill/decode disaggregation interact with prefix caching?
- [LLM06-150] In a disaggregated setup, how would you decide the ratio of prefill to decode capacity?
- [LLM06-151] How would you deploy prefill-decode disaggregation in vLLM, with KV transfer across nodes through something like Mooncake or LMCache?
- [LLM06-152] Why is load balancing LLM inference different from load balancing stateless HTTP, and what does a good routing layer do?
- [LLM06-153] Session affinity versus prefix-hash routing for LLM inference: when does each fail?
- [LLM06-154] How does prefix caching change your load-balancer design for LLM serving?
- [LLM06-155] Would you replicate a prefix cache across serving nodes or shard requests by prefix hash? What hit rate justifies a shared KV tier over sticky sessions?
- [LLM06-156] How does prefix-aware routing interact with autoscaling, and what does that do to your scale-up policy?

## Deployment, autoscaling, and multi-tenancy
- [LLM06-157] How do you serve LLMs in production?
- [LLM06-158] How would you design a scalable LLM inference system for real-time applications?
- [LLM06-159] You must serve a Llama-class 70B+ model to hundreds of millions of assistant users. What does the serving stack look like and where does the money go?
- [LLM06-160] Walk me through deploying a 70B open-weight model to production on Kubernetes. What breaks?
- [LLM06-161] How do you autoscale a vLLM deployment? Why does CPU-based HPA not work, and why is GPU utilization a poor scaling signal for decode-heavy workloads?
- [LLM06-162] Your queue-depth autoscaler for an LLM deployment flaps every 5 minutes. How do you stabilise it without eating the spike?
- [LLM06-163] GPU cold starts take minutes. How do you autoscale an inference fleet anyway, for example cutting replica startup from 12 minutes to under 3?
- [LLM06-164] Peak LLM traffic is 3x the daily average. How do you split reserved versus autoscaled capacity?
- [LLM06-165] Which graceful-degradation options relieve KV memory pressure versus compute pressure in LLM serving?
- [LLM06-166] In a serverless model-inference platform, when does it become cheaper to give a model dedicated capacity?
- [LLM06-167] What is multi-LoRA serving, and how does it let one base model serve many tenants?
- [LLM06-168] How do you serve fine-tuned models at scale: merged checkpoints versus adapters, versioning, and rollback?
- [LLM06-169] Design routing for 500 tenant LoRA adapters where 10 tenants account for 80% of traffic. What changes if variants also need different system prompts?
- [LLM06-170] How do you handle noisy neighbors in a multi-tenant LLM serving cluster?
- [LLM06-171] One malformed request crashed an inference replica and every tenant on it lost service. What is the design lesson and fix?
- [LLM06-172] Design a premium low-latency tier for an agent product that needs very high tokens per second per user.
- [LLM06-173] Your traffic is shifting from single-turn chat to agents: 20 to 50 model calls per task, tool calls in between, long sessions. What does that do to your serving design?
- [LLM06-174] In a low-latency serving system, how do you cheaply cancel in-flight GPU work when the client disconnects or the user keeps typing?
- [LLM06-175] How do you ship a major vLLM version upgrade without changing model behavior?
- [LLM06-176] How do you handle a replica failing mid-stream, and what are the options for retrying or resuming a partially generated response?

## Capacity planning and cost
- [LLM06-177] How do you estimate whether a model fits on a given GPU? Will a 70B model fit on one 80 GB card?
- [LLM06-178] Build the full GPU memory budget for a serving deployment (weights, KV cache, activations, fragmentation) and show how it determines maximum batch size, including FP8 weights on 2 GPUs.
- [LLM06-179] How would you estimate the number of GPUs needed to serve a given model at a target QPS and latency?
- [LLM06-180] Mistral Large 3 is an open-weight sparse MoE with about 675B total and 41B active parameters. A customer wants to self-host it on one 8-GPU node. Does it fit, and how would you serve it?
- [LLM06-181] Your product wants to raise the context limit from 8K to 128K. What does that do to cost per request and to capacity?
- [LLM06-182] How does a 30% prompt-cache hit rate change an LLM serving capacity plan?
- [LLM06-183] When sizing a self-hosted 13B deployment where 80% of traffic shares one system prompt, how does prefix caching change the math?
- [LLM06-184] How do prefill-heavy workloads (long prompts, short answers) change the cost-per-million-tokens math of a dedicated endpoint?
- [LLM06-185] What changes in the cost-per-million-tokens estimate for a dedicated endpoint when moving it to B200 GPUs?
- [LLM06-186] Given a GPU hourly price and a measured tokens-per-second at a given batch size, how do you compute cost per million tokens?
- [LLM06-187] Estimate what one chat message costs to serve, and say which lever moves that cost most as dialogue length grows.
- [LLM06-188] How do you estimate the cost of running SaaS-based versus open-source LLMs, and when is self-hosting cheaper than an API?
- [LLM06-189] How would you cut LLM serving cost by 10x? Enumerate every lever and rank them.
- [LLM06-190] What would you try next to cut LLM inference costs by another 50% once the obvious levers are used?
- [LLM06-191] When would you use cheaper tiers such as offline batch processing, a model cascade, or a semantic cache to cut serving cost, and what are the risks?
- [LLM06-192] Your product moves from a standard chat model to a reasoning model with extended thinking. What changes for capacity, SLOs, and design?
- [LLM06-193] Which is worse for your fleet: one 30K-token reasoning request or thirty 1K-token chat requests, and why?
- [LLM06-194] A customer sends a different 900K-token document with every request. How does that change your pricing and capacity plan?

## Debugging and design scenarios
- [LLM06-195] A customer's LLM chatbot on 8 GPUs is "too slow and too expensive." You have one week with them. What do you do?
- [LLM06-196] Production LLM serving suddenly slows down. What metrics and diagnostic steps do you follow?
- [LLM06-197] Your p99 TTFT for an LLM service doubles at peak traffic while p50 stays flat. What are your top suspects?
- [LLM06-198] Your p99 TTFT breaches its SLO but GPU utilization shows 60%. What do you investigate?
- [LLM06-199] KV cache utilization is 95%, preemptions are climbing, but GPU utilization looks fine. What is happening and what do you do?
- [LLM06-200] A custom code-completion model serving millions of users shows 35% GPU utilization with fine p99 latency. Do you chase the utilization?
- [LLM06-201] When diagnosing a jump in an endpoint's p99 latency, how does continuous batching change the analysis versus static batching?
- [LLM06-202] To control p99 latency on an LLM endpoint, what would you cap first, input tokens or output tokens, and why?
- [LLM06-203] Your LLM service must meet a p95 TTFT target while maximizing tokens per second. How do you configure batching, chunked prefill, and replicas?
- [LLM06-204] You self-host a VLM for a document pipeline and throughput is a third of what you projected from the LLM's specs. Why, and what do you do?
- [LLM06-205] In a serving system for a multimodal LLM assistant, what breaks first as median context length grows 10x?
