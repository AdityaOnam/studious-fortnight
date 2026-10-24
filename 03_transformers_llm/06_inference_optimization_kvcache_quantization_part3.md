---
domain: llm
topic: inference_optimization_kvcache_quantization
title: Inference optimization, KV cache, quantization
tags: [inference, kv-cache, quantization, vllm]
count: 113
part: 3/3
---
# Inference optimization, KV cache, quantization (part 3)

## Quantization fundamentals
- [LLM06-206] What is quantization in LLMs, and why do we quantize models for deployment?
- [LLM06-207] How does quantization reduce model size, and how much memory does INT8 or INT4 save for a given parameter count?
- [LLM06-208] What are the main types of quantization (PTQ vs QAT, weight-only vs weight-and-activation, static vs dynamic, symmetric vs asymmetric)?
- [LLM06-209] What is weight-only quantization, what is activation quantization, and how do they differ?
- [LLM06-210] What is calibration in quantization, and how does your choice of calibration data matter?
- [LLM06-211] What is mixed precision (for example FP16), and why is it used during inference?
- [LLM06-212] Why do many serving stacks prefer BF16 over FP16 for inference, and when does FP16 still win?
- [LLM06-213] What is the trade-off between accuracy and performance in quantization, and how does it affect latency and memory?
- [LLM06-214] Compare FP16, BF16, INT8, and INT4 for LLM inference in memory, speed, and quality. Why is INT8 not always faster in practice?
- [LLM06-215] Why does moderate quantization cause only a small accuracy loss in LLMs, and when does that stop being true?
- [LLM06-216] Why does weight-only quantization speed up decode but barely help prefill?
- [LLM06-217] Why does W4A16 quantization barely help a high-batch serving deployment?
- [LLM06-218] What do quantization granularity choices (per-tensor, per-channel, group-wise) change in accuracy and kernel cost?
- [LLM06-219] What is the difference between static and dynamic activation quantization, and what does each cost at runtime?
- [LLM06-220] Where does dequantization happen at runtime for weight-only schemes, and why are fused dequant-GEMM kernels needed?
- [LLM06-221] Why is quantizing activations harder than quantizing weights, and how does that shape architecture choices?
- [LLM06-222] What are activation outliers, and why do they make W8A8 quantization harder than W4A16? How do SmoothQuant and LLM.int8() address them?

## Quantization schemes and formats
- [LLM06-223] What is GPTQ, and why is it important for LLM quantization?
- [LLM06-224] How does AWQ differ from GPTQ in how it chooses what to protect and how it quantizes?
- [LLM06-225] GPTQ vs AWQ vs GGUF vs bitsandbytes NF4 vs INT8 vs FP8: when would you use each, and how do you pick a scheme for a deployment?
- [LLM06-226] Why does QLoRA use NF4 rather than a standard 4-bit format?
- [LLM06-227] Compare FP16, BF16, FP8, INT8, INT4, and FP4 for serving. What breaks at each step down?
- [LLM06-228] How does FP8 improve inference throughput on H100 GPUs?
- [LLM06-229] On H100s you want lower memory and higher matmul throughput for a Llama-class model with minimal accuracy work. What is the best quantization choice?
- [LLM06-230] Blackwell GPUs run NVFP4 natively. How does it differ from INT4 weight-only quantization, and when would you serve a model in it?
- [LLM06-231] Why does a non-uniform floating-point grid such as NVFP4 suit weight distributions better than INT4's uniform grid?
- [LLM06-232] How does serving a 70B model change on a Blackwell-class GPU with FP4 support?
- [LLM06-233] The team wants to move serving from FP8 to NVFP4 to cut cost. What do you check, and what would you measure for a latency-sensitive chat product?
- [LLM06-234] How does serving a large MoE model change if the customer only has 8x A100 80 GB, which has no FP8 tensor cores?
- [LLM06-235] Why might you still choose 2 GPUs with FP8 over 1 GPU with INT4 for serving a large model?
- [LLM06-236] You must deploy a 70B model on 8x A100 40GB GPUs. Walk through the precision choice and the strongest plan.
- [LLM06-237] Where would you spend a 2x quantization win when serving an LLM: fewer chips per instance, or longer context?
- [LLM06-238] How would you decide the quantization bit-width per layer under a fixed 1 GB model budget?
- [LLM06-239] What is post-training quantization versus quantization-aware training, and what breaks when you push weights to 2-4 bits?
- [LLM06-240] When would you accept the cost of quantization-aware training over post-training quantization?
- [LLM06-241] What is KV cache quantization, when is it the right lever, and why is it usually quantized separately from the weights?
- [LLM06-242] Why are keys more sensitive to quantization than values in the KV cache, and how can the error be compensated?
- [LLM06-243] How does grouped-query attention interact with KV cache quantization?

## Validating and debugging quantized models
- [LLM06-244] You quantized your LLM but accuracy dropped significantly. How do you minimize the quantization loss?
- [LLM06-245] A BF16 fine-tune passed your quality gates and you quantize it to INT4 for serving. What is the disciplined final step?
- [LLM06-246] What would make you reject a 4-bit quantized model that passes perplexity and aggregate benchmark checks?
- [LLM06-247] Your 4-bit model matches on aggregate benchmarks, but users complain. How do you find what broke?
- [LLM06-248] A customer says the FP8 endpoint "feels dumber" but your evals show parity. What do you do?
- [LLM06-249] You must quantize a model for a customer's hardware. How do you choose a scheme, and how do you prove quality has not regressed?
- [LLM06-250] Why does quantization hurt long generations more than short ones?
- [LLM06-251] What accuracy and speed trade-offs do you expect from 4-bit weight-only quantization of a 7B model, and how would you validate it?
- [LLM06-252] How would you detect that quantization has damaged a few rarely routed experts more than the rest of an MoE model?
- [LLM06-253] What does INT4 KV cache quantization do to long-context retrieval quality, and how would you measure it?
- [LLM06-254] When would you serve two precisions of the same model behind a router?
- [LLM06-255] How can poorly chosen calibration data cause a quantized model to fail on production traffic?

## Pruning, distillation, and on-device inference
- [LLM06-256] What are structured versus unstructured sparsity in LLMs, and why is unstructured sparsity hard to accelerate?
- [LLM06-257] What is 2:4 structured sparsity, what hardware does it need, and what speedup is realistic?
- [LLM06-258] How does knowledge distillation produce a smaller serving model, and when is distillation preferred over quantization?
- [LLM06-259] Your model meets quality targets but runs at 4s p95 latency, and you need 400ms with 10x the throughput. Design the compression plan.
- [LLM06-260] How does LLM inference speed compare on CPU versus GPU, and when is CPU inference acceptable?
- [LLM06-261] How do you optimize LLM inference for edge and mobile deployment?
- [LLM06-262] How do you deploy a capable assistant on cost-sensitive or on-device hardware without a datacentre GPU? Walk through the efficiency toolkit.
- [LLM06-263] You need to run a roughly 3B-parameter model on a phone with tight memory and power budgets. Do the maths and say what changes versus datacenter serving.
- [LLM06-264] Estimate the KV cache memory for a 3B on-device model at 4k context and name the levers that shrink it.
- [LLM06-265] Which KV cache memory lever would you try first if you needed 2x headroom for a new on-device feature?
- [LLM06-266] When would you give up on on-device inference and route the request to a server model, and what do you give up by going on-device?
- [LLM06-267] A new on-device model is a 20B sparse model whose weights live in flash, with only 1-4B parameters active at a time. How do you serve it on a phone?
- [LLM06-268] What do Ray Serve or MLC LLM add for deployment, and when would you use them for edge devices?

## Dense model parallelism for inference
- [LLM06-269] What is model sharding, and when would you use it for inference?
- [LLM06-270] What are the challenges of performing distributed inference across multiple GPUs?
- [LLM06-271] How are tensor, pipeline, and sequence parallelism used at inference time, and when is each preferred?
- [LLM06-272] How is tensor parallelism sharded, how costly is the AllReduce communication per layer, and when should you use DP, PP, or EP instead?
- [LLM06-273] Why is tensor parallelism preferred over pipeline parallelism for low-latency serving?
- [LLM06-274] Why does TP=8 spread across two 4-GPU nodes over Ethernet perform terribly?
- [LLM06-275] How do pipeline bubbles show up in inference, and how does micro-batching help?
- [LLM06-276] Design the parallelism strategy for serving a 405B-parameter dense model. What goes where among TP, PP, and EP, and why?
- [LLM06-277] How does the serving layout change when the NVLink domain grows from 8 GPUs to a 72-GPU rack, as with GB200 NVL72-class systems?
- [LLM06-278] What are context parallelism and ring attention, and why does context parallelism help prefill far more than decode?
- [LLM06-279] Why can DeepSeek-style MLA models not use standard tensor-parallel layouts without KV duplication, and how does MLA compare with GQA under TP?
- [LLM06-280] How do you decide how many GPUs of 80 GB you need to serve a 70B model in FP16, and which parallelism do you use?

## Mixture-of-experts inference
- [LLM06-281] How does MoE inference change batching, communication, and memory planning compared with a dense model?
- [LLM06-282] How does serving a large sparse MoE model differ from serving a dense one, and what does expert parallelism change?
- [LLM06-283] For MoE inference, how do you choose between expert parallelism and tensor parallelism?
- [LLM06-284] Where does an MoE model sit on the roofline compared with a dense model of the same active-parameter count?
- [LLM06-285] Why does low traffic hurt an MoE deployment more than a dense one of similar quality?
- [LLM06-286] Why is batched MoE inference trickier than dense inference, given expert imbalance within a batch?
- [LLM06-287] How would you detect and quantify expert imbalance in production, and what happens to p99 latency when the routing histogram shifts?
- [LLM06-288] How would you pick an MoE capacity factor from production traffic rather than from the training config?
- [LLM06-289] How would you serve a large MoE model when expert selection is data-dependent?
- [LLM06-290] Why does wide expert parallelism free HBM for KV cache, and how does that change achievable batch size?
- [LLM06-291] Serve a DeepSeek-V3-class MoE (671B total, about 37B active) on Blackwell GPUs. How do you lay it out, and why does expert parallelism change the economics?
- [LLM06-292] How does the parallelism strategy change for a 400B MoE with about 30B active parameters?
- [LLM06-293] Serving a 70B dense model with 8-bit weights versus a sparse MoE of the same total parameter count: how does the analysis change?
- [LLM06-294] Dense 30B versus an MoE with 25B active parameters on a single 80 GB GPU: how do you decide for a specific customer?
- [LLM06-295] What optimization problems are specific to MoE models in inference frameworks, and how do speculative decoding and PD separation work with MoE?

## Serving frameworks, hardware, and benchmarking
- [LLM06-296] What are the main LLM inference engines available, and what does each aim to optimize?
- [LLM06-297] How does SGLang work, and what is the difference between vLLM and SGLang?
- [LLM06-298] How does TensorRT-LLM make a model faster, and when will it not help?
- [LLM06-299] How does llama.cpp run LLMs on everyday hardware, and how does Ollama build on it?
- [LLM06-300] Why is Ollama not a production inference server, and why are GGUF-style formats unsuited to datacenter serving?
- [LLM06-301] How are HuggingFace TGI and vLLM related, and what are their strengths and weaknesses?
- [LLM06-302] Besides vLLM, SGLang, and TensorRT-LLM, what other inference frameworks exist, and how do you choose by hardware?
- [LLM06-303] When would you choose vLLM vs SGLang vs TensorRT-LLM vs a custom stack?
- [LLM06-304] Your workload is mostly shared-system-prompt or multi-call agentic programs emitting strict JSON. Which serving stack fits best, and why?
- [LLM06-305] What does a vendor-tuned stack like TensorRT-LLM buy over a portable engine, and what does it cost when you want to add AMD capacity?
- [LLM06-306] What does changing the attention backend actually change for you operationally?
- [LLM06-307] A new LLM architecture ships with an attention variant no inference-engine kernel supports. What happens on day zero, and what is the fallback?
- [LLM06-308] How would you verify that a fused or compiled inference engine is numerically equivalent enough to the source model?
- [LLM06-309] What is your process when a TensorRT engine turns out slower than the PyTorch baseline?
- [LLM06-310] How would you design a reproducible benchmark to choose between inference frameworks for a customer?
- [LLM06-311] A vendor pitches an accelerator at "3,000 tokens per second." How do you evaluate that claim, and how would you evaluate a new serving platform for your fleet?
- [LLM06-312] How do you select GPUs for LLM inference?
- [LLM06-313] How do you choose inference hardware among NVIDIA GPUs, AMD, TPUs, and cloud silicon like Inferentia and Trainium?
- [LLM06-314] Compare A100, H100, H200, and B200 for LLM inference. Which specification matters most for decode?
- [LLM06-315] How does an LPU or other SRAM-based accelerator work, and at what model size does an SRAM-only design start to win?
- [LLM06-316] On a GPU you batch to amortise weight reads. What is the batching calculus on an SRAM-only accelerator?
- [LLM06-317] Why might one GPU with more HBM beat two smaller GPUs with the same total memory for LLM inference?
- [LLM06-318] How do you share a GPU or manage GPU memory when serving multiple models (MIG, MPS, time slicing)?
