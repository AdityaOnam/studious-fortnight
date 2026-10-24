---
domain: finetune
topic: peft_lora_qlora_adapters
title: PEFT: LoRA, QLoRA, adapters
tags: [peft, lora, qlora, adapters]
count: 121
---
# PEFT: LoRA, QLoRA, adapters

## PEFT landscape and when to use it
- [FT02-001] What is the difference between full fine-tuning and parameter-efficient fine-tuning (PEFT), and why is PEFT needed?
- [FT02-002] What is the difference between LoRA and full fine-tuning?
- [FT02-003] What are the advantages of PEFT in terms of memory, per-task storage, catastrophic forgetting and deployment?
- [FT02-004] What are the pros and cons of full fine-tuning compared with PEFT methods?
- [FT02-005] What are the main categories of PEFT methods (additive, selective, reparameterization), and what is an example of each?
- [FT02-006] What are re-parameterized methods for fine-tuning, and how do they differ from additive methods such as adapters?
- [FT02-007] When would you choose fine-tuning with PEFT over prompt engineering or RAG?
- [FT02-008] A team wants a model for a narrow classification task with 2,000 labeled examples. Do you pick full fine-tuning or PEFT, and why?
- [FT02-009] How do you choose between LoRA and full fine-tuning for a domain-specific assistant, given data, budget and quality bar?
- [FT02-010] When is full or near-full fine-tuning genuinely worth its cost over LoRA?
- [FT02-011] Your LoRA model matches full fine-tuning on the target task. Is there any reason to still prefer full fine-tuning?
- [FT02-012] What quality gap, if any, does LoRA show versus full fine-tuning on reasoning-heavy or knowledge-heavy tasks?
- [FT02-013] Can PEFT inject genuinely new knowledge into a model, or does it mainly adapt style, format and behaviour?
- [FT02-014] What are known limitations of current PEFT methods, such as a lower ceiling on knowledge injection or hyperparameter sensitivity?
- [FT02-015] What best practices would you follow when choosing and configuring a PEFT method for a new task?
- [FT02-016] What common view unifies adapters, prefix tuning and LoRA, and which design choices differ between them?

## LoRA fundamentals
- [FT02-017] What is LoRA, and how does it work at a high level?
- [FT02-018] Does LoRA change the base model weights during training, and what exactly gets saved in an adapter checkpoint?
- [FT02-019] Explain the LoRA decomposition mathematically: which matrices are trained, how are they initialized, and what do r and alpha mean?
- [FT02-020] Why is B initialized to zero and A randomly, instead of initializing both matrices randomly?
- [FT02-021] If B starts at zero, the gradient to A is zero at step one. Why does training still get going?
- [FT02-022] Calculate the trainable parameters when adding LoRA with rank 8 to the q and v projections of a 32-layer model with hidden size 4096.
- [FT02-023] Walk through a forward and backward pass through a LoRA layer. Which tensors need gradients and which do not?
- [FT02-024] What is the low intrinsic dimensionality hypothesis behind LoRA, and when does it break down?
- [FT02-025] Why can a rank-8 B·A update approximate a full fine-tune of a 12,288-dimensional attention weight?
- [FT02-026] Why do LoRA runs tolerate roughly 10x higher learning rate than full fine-tuning?
- [FT02-027] Does LoRA reduce training compute (FLOPs) as much as it reduces memory? Where does the time still go?
- [FT02-028] What changes when you add LoRA to a setup that uses gradient accumulation and gradient checkpointing?
- [FT02-029] Why is LoRA often less prone to catastrophic forgetting than full fine-tuning, and what does "LoRA Learns Less and Forgets Less" suggest?

## LoRA hyperparameters, targets and debugging
- [FT02-030] How do rank r and alpha affect capacity and training dynamics, and how would you tune them?
- [FT02-031] Why is LoRA alpha often set to twice the rank?
- [FT02-032] What breaks if LoRA alpha is far too large relative to r?
- [FT02-033] Do you need to retune the learning rate when you change the LoRA rank while keeping alpha fixed? Why?
- [FT02-034] If doubling the LoRA rank does not improve quality, what does that tell you?
- [FT02-035] How would you decide the LoRA rank for a task of known complexity and dataset size?
- [FT02-036] How would you pick the LoRA rank, learning rate, epochs and batch size for a new task?
- [FT02-037] Which modules should LoRA target, and what is the effect of targeting only attention versus all linear layers?
- [FT02-038] Why does low-rank-many-modules tend to beat high-rank-few-modules at equal parameter count in LoRA?
- [FT02-039] When would you also train the embedding layer or LM head alongside LoRA?
- [FT02-040] What is the role of LoRA dropout, and when would you turn it on or off?
- [FT02-041] When fine-tuning an 8B model on a single 24 GB GPU, which modules do you target, and why does rank matter less than people expect?
- [FT02-042] Your LoRA fine-tune (q_proj and v_proj, r=16) lands about 3 points below a full fine-tune on a clean held-out set. What do you try first?
- [FT02-043] How would you detect that LoRA is underfitting versus the data being the problem?
- [FT02-044] How would you test whether an SFT stage is capacity-limited by its LoRA rank rather than by data?
- [FT02-045] Training loss looks fine, but your LoRA model degrades on general benchmarks after fine-tuning. How do you diagnose and mitigate it?
- [FT02-046] LoRA training diverges or shows loss spikes at the start. What hyperparameters and settings do you check?

## LoRA variants and advanced settings
- [FT02-047] What is DoRA, and why would you use it over standard LoRA?
- [FT02-048] Why does DoRA still merge cleanly into the base weights at inference?
- [FT02-049] If DoRA beats LoRA on your eval by 0.4 points but costs 30% more training time, how do you decide?
- [FT02-050] DoRA, rsLoRA and LoRA+ all claim to improve on vanilla LoRA. What does each actually change, and when would you reach for them?
- [FT02-051] What are VeRA and rank-stabilized LoRA, and what problems do they address?
- [FT02-052] Why does the alpha/r scaling in standard LoRA hurt learning at high ranks, and how does alpha/sqrt(r) fix it?
- [FT02-053] What is LoRA+, and why would using different learning rates for the A and B matrices help?
- [FT02-054] How does AdaLoRA allocate rank adaptively across layers, and what importance score does it use?
- [FT02-055] How do initialization-based variants such as PiSSA or LoftQ differ from standard LoRA initialization?
- [FT02-056] How does GaLore differ from LoRA in how it saves optimizer memory, and what tradeoffs does it make?
- [FT02-057] Why does LoRA hold up so well for RL fine-tuning, even at very low rank, when the same rank can underfit a large SFT run?
- [FT02-058] If RL needs so little capacity, why do labs still run full-parameter RL?
- [FT02-059] How would you pick which experts to put LoRA on when fine-tuning a mixture-of-experts model?

## Adapters, prefix tuning, prompt tuning and other PEFT
- [FT02-060] What is adapter-based fine-tuning, and how does an adapter module work (down-projection, nonlinearity, up-projection, residual) inside a Transformer layer?
- [FT02-061] What latency penalty do adapters add at inference compared with LoRA, and why?
- [FT02-062] What do AdapterFusion and AdapterDrop add, and why would you drop adapters in lower layers?
- [FT02-063] What do MAM Adapter and UniPELT propose in terms of unifying PEFT designs?
- [FT02-064] Explain prefix tuning and prompt tuning. How are they different from LoRA?
- [FT02-065] How does prefix tuning prepend trainable vectors to each layer's keys and values, and why use a reparameterization MLP during training?
- [FT02-066] Compare prompt tuning, prefix tuning, P-tuning and P-tuning v2. What scale effects do they show?
- [FT02-067] Why does prompt tuning approach full fine-tuning only for very large models, and how does P-tuning v2 address smaller models?
- [FT02-068] What are the inference-time costs of prompt-based PEFT, and how do they reduce usable context length?
- [FT02-069] What is a verbalizer and a template in prompt learning, and why does prompt learning with masked LMs work well in few-shot settings?
- [FT02-070] What is BitFit, how few parameters does it train, and when might it be enough?
- [FT02-071] What is IA3, and how does learning rescaling vectors for keys, values and FFN activations compare with LoRA in parameter count?
- [FT02-072] Why are soft prompts often harder to optimize and less stable than LoRA, and how sensitive are they to initialization?
- [FT02-073] Compare LoRA, adapters, prefix tuning, prompt tuning and full fine-tuning. When would you choose each?
- [FT02-074] Which PEFT method would you choose to serve many tasks in a single batch with minimal latency overhead, and why?

## QLoRA and quantization
- [FT02-075] What is QLoRA, and how does it differ from LoRA?
- [FT02-076] When would you use QLoRA instead of standard LoRA?
- [FT02-077] What are the three key ideas of QLoRA (NF4, double quantization, paged optimizers), and what do you give up for the memory savings?
- [FT02-078] Why does QLoRA use NF4 instead of standard Float4, and why is NF4 suited to normally distributed pretrained weights?
- [FT02-079] Why are normal-distribution quantiles the right levels for weight quantization in NF4?
- [FT02-080] What does double quantization quantize, and roughly how much memory does it save per parameter?
- [FT02-081] What problem do paged optimizers solve, and when do they actually trigger?
- [FT02-082] In QLoRA, which tensors stay in 4-bit, which are in bf16, and how does backprop work through frozen quantized weights?
- [FT02-083] What memory does QLoRA save relative to LoRA, and where does de-quantization add compute cost?
- [FT02-084] Is QLoRA training slower than LoRA at the same rank? Why, and when is the trade acceptable?
- [FT02-085] Your QLoRA adapter evaluates worse when served on the fp16 base model. Why, and what would you do?
- [FT02-086] Why is merging a LoRA adapter into a 4-bit quantized base model problematic?
- [FT02-087] How would you choose between QLoRA on a 4-bit base and LoRA on an 8-bit or GPTQ/AWQ-quantized base?
- [FT02-088] What does very low-bit (2-bit) base-model quantization change about fine-tuning options for downstream teams?

## Memory math and hardware planning
- [FT02-089] Why can't you full-fine-tune a 7B model on a single 24 GB GPU with Adam? Do the memory math.
- [FT02-090] Do the GPU memory math for fine-tuning a 7B model in bf16 with Adam: full fine-tuning, LoRA and QLoRA.
- [FT02-091] Redo the fine-tuning memory math for LoRA at r=16. What is now the dominant memory term?
- [FT02-092] Walk through the memory math of fine-tuning a 65B or 70B model with QLoRA versus full fine-tuning, and where the savings come from.
- [FT02-093] Why keep fp32 master weights at all in bf16 training?
- [FT02-094] Where does 8-bit Adam save memory, and what is the risk?
- [FT02-095] How do activations, sequence length and batch size affect memory in LoRA fine-tuning, and what does gradient checkpointing trade?
- [FT02-096] How would you handle LLM fine-tuning on consumer hardware with limited GPU memory?
- [FT02-097] You need to fine-tune a 33B model on a single 48 GB GPU. What is the defensible approach, and what cost should you flag?
- [FT02-098] How do you estimate infrastructure requirements (GPUs, memory, time) for fine-tuning an LLM?
- [FT02-099] You need to QLoRA-fine-tune a 70B model on 1 million tokens of data. Estimate the GPUs, memory and wall-clock time you need.
- [FT02-100] When would you combine QLoRA with FSDP or DeepSpeed across multiple GPUs, and what does sharding a quantized base model require?

## Merging adapters
- [FT02-101] Can LoRA adapters be merged into the base weights, and what are the implications for serving and quantization?
- [FT02-102] What is the practical difference between merging a LoRA into the base weights and keeping it as a runtime adapter?
- [FT02-103] When would you merge an adapter into the base weights and serve it as its own model?
- [FT02-104] How do you merge multiple LoRA adapters into one model?
- [FT02-105] Why does naively summing two LoRA deltas often degrade quality, and how do methods such as TIES or DARE address interference?
- [FT02-106] What happens to numerical precision when you merge a bf16 LoRA delta into an fp16 or int8 base model, and how do you check for it?
- [FT02-107] How do adapter merging, multi-LoRA serving and hot-swapping work in production?

## Serving many adapters
- [FT02-108] How do you serve hundreds of LoRA adapters on a shared base model efficiently?
- [FT02-109] Why might LoRA at a moderate rank be a better default than full fine-tuning for a multi-tenant platform?
- [FT02-110] What changes when one LLM deployment serves LoRA adapters for ten teams?
- [FT02-111] You need to serve 200 customer-specific fine-tunes of the same 8B base model on a handful of GPUs. How, and what breaks first?
- [FT02-112] Design a platform that serves hundreds of tenant-specific LoRA adapters on shared GPUs, including adapter swapping, scheduling and isolation.
- [FT02-113] How would you design serving for 500 tenant-specific fine-tunes with skewed traffic?
- [FT02-114] Why can't a shared system prompt's KV cache be reused across two different LoRA adapters?
- [FT02-115] How do batched multi-LoRA kernels (as in S-LoRA or Punica) let one batch mix requests for different adapters, and what limits throughput?
- [FT02-116] How do adapter cold starts and eviction affect tail latency, and how would you mitigate them?
- [FT02-117] How do you handle a base-model upgrade that breaks existing tenant adapters?
- [FT02-118] What integrity controls, such as signing and checksums, would you put on adapter artifacts?
- [FT02-119] You have one on-device base model but a dozen features (summarization, rewriting, reply suggestions, tone adjustment). How do you specialize without shipping a dozen models?
- [FT02-120] How do you update one feature's adapter on an on-device model without a full OS release?
- [FT02-121] What breaks in per-feature adapters if the base model is re-quantized between releases?
