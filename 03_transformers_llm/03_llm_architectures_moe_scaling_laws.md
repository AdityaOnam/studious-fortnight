---
domain: llm
topic: llm_architectures_moe_scaling_laws
title: LLM architectures, MoE and scaling laws
tags: [llm, moe, scaling-laws, architecture]
count: 136
---
# LLM architectures, MoE and scaling laws

## Language model and architecture basics
- [LLM03-001] What is a large language model, and how does it differ from a traditional statistical (n-gram) language model?
- [LLM03-002] What are autoregressive models, and how is the probability of a sequence factorized in an autoregressive language model?
- [LLM03-003] What is a foundation model, and how has the foundation-model paradigm changed how AI systems are built?
- [LLM03-004] What is the difference between dense and sparse models?
- [LLM03-005] Why can an encoder-only model such as BERT not be used directly for open-ended text generation?
- [LLM03-006] How does ChatGPT work end to end, from the pretrained model to what happens after you press Enter?
- [LLM03-007] How does GPT-4 differ from GPT-3 in capabilities and architecture, as far as is publicly known?
- [LLM03-008] Describe the GPT architecture and explain how a decoder-only design supports language generation.
- [LLM03-009] What is the difference between encoder-only, decoder-only and encoder-decoder Transformers?
- [LLM03-010] Explain the different LLM architecture families and which kind of task each is best suited to.
- [LLM03-011] What is the difference between a prefix LM and a causal LM in terms of attention masks and which tokens can attend to which?
- [LLM03-012] What are the trade-offs between causal, prefix and encoder-decoder language models for generation versus understanding tasks?
- [LLM03-013] How do T5-style span-corruption pretraining and GPT-style next-token pretraining differ as objectives?
- [LLM03-014] What is cross-attention, and where does it appear in an encoder-decoder model but not in a decoder-only one?
- [LLM03-015] Why have most mainstream LLMs converged on causal decoder-only architectures instead of encoder-decoder?
- [LLM03-016] Why is decoder-only pretraining often said to give better zero-shot performance than encoder-decoder pretraining?
- [LLM03-017] If you were building a translation system today, would you choose an encoder-decoder or a decoder-only LLM, and on what criteria?
- [LLM03-018] Roughly estimate the parameter count of a decoder-only Transformer from its number of layers and hidden size. Where do most of the parameters live?
- [LLM03-019] How does the scale of the model and the dataset size affect pretraining and the resulting model?
- [LLM03-020] At a fixed parameter budget, how would you trade depth against width, and what do on-device constraints change?

## Model families and design choices
- [LLM03-021] What changed architecturally between GPT-2 and Llama 2?
- [LLM03-022] What architectural changes distinguish LLaMA from the original Transformer (RMSNorm pre-norm, SwiGLU, RoPE)?
- [LLM03-023] What changed between LLaMA 1, 2 and 3 in data size, context length, tokenizer vocabulary and attention?
- [LLM03-024] How do the ChatGLM, LLaMA and GPT families differ in position encoding, masking and normalization?
- [LLM03-025] What is the GLM autoregressive blank-infilling objective, and how does it unify understanding and generation?
- [LLM03-026] Why do modern LLMs use RMSNorm with pre-normalization instead of LayerNorm with post-normalization?
- [LLM03-027] Why use grouped-query attention rather than multi-head or multi-query attention in models like Llama and Mistral?
- [LLM03-028] What is sliding-window attention in Mistral, and how does stacking layers let information travel beyond the window?
- [LLM03-029] Why did LLaMA 3 invest so heavily in data quality and filtering, and how does that interact with scaling-law predictions?
- [LLM03-030] Compare the architectural choices of Llama, Mistral, Gemma and DeepSeek models. What does each family optimize for?
- [LLM03-031] Explain why a Llama-class model uses grouped-query attention, RoPE and SwiGLU instead of the vanilla 2017 Transformer.
- [LLM03-032] What is Multi-head Latent Attention (MLA) in DeepSeek models, and how does it shrink the KV cache compared with GQA?
- [LLM03-033] Which architectural innovations does DeepSeek-V3 combine (MLA, DeepSeekMoE, multi-token prediction, load balancing), and what does each buy?
- [LLM03-034] What is Multi-Token Prediction (MTP), why add an MTP layer, and how can it help at inference time?
- [LLM03-035] Walk through a LLaMA-2 forward pass for one generated token, naming each module from embedding to logits.

## Mixture of experts fundamentals
- [LLM03-036] What is a mixture-of-experts model, and how does it differ from a dense model?
- [LLM03-037] Explain mixture of experts: the router, top-k expert selection, and why it saves compute per token.
- [LLM03-038] What is the difference between active and total parameters in an MoE model, and which one governs memory versus FLOPs?
- [LLM03-039] How does an MoE architecture scale model capacity without scaling per-token FLOPs?
- [LLM03-040] What problem does the sparsely-gated mixture-of-experts layer solve, and how does the gating network select experts?
- [LLM03-041] What changes inside a Transformer decoder block when you convert it to a mixture-of-experts model?
- [LLM03-042] Why does MoE replace the feed-forward network rather than the attention layer?
- [LLM03-043] Why route per token rather than per sequence in a mixture-of-experts model?
- [LLM03-044] Explain how a Mixtral-style sparse MoE works. Why does a roughly 47B-parameter model run at about the cost of a 13B one?
- [LLM03-045] How does a shared (always-on) expert change the routing dynamics in an MoE?
- [LLM03-046] What do experts in an MoE model actually specialize in, empirically?
- [LLM03-047] Why is MoE another response to the same economic pressure that pushes training far beyond Chinchilla-optimal?
- [LLM03-048] How do GShard, Switch Transformer and GLaM differ in routing (top-2 vs top-1), capacity factor and expert placement?
- [LLM03-049] How can MoE be used to make a dense model lighter, as in MoEBERT's conversion of FFNs into experts?
- [LLM03-050] What is upcycling, i.e. initializing an MoE from a dense checkpoint, and what are its pros and cons?
- [LLM03-051] Is a 47B-total, 13B-active MoE comparable to a 13B dense model or a 47B dense model, and on which axis?
- [LLM03-052] Walk through DeepSeekMoE. How do fine-grained experts and shared experts differ from a standard top-2 MoE like Mixtral?

## MoE routing and load balancing
- [LLM03-053] What is noisy top-k gating, and why is noise added to the gate logits?
- [LLM03-054] Why does an MoE layer need an auxiliary load-balancing loss, and what happens to expert utilization without it?
- [LLM03-055] Describe the importance loss and load loss used to balance experts in sparsely-gated MoE.
- [LLM03-056] Write down the Switch Transformer load-balancing auxiliary loss and explain what it penalizes.
- [LLM03-057] What is the router z-loss in ST-MoE, and what instability does it address?
- [LLM03-058] Why did Switch Transformer route each token to a single expert, and what stability tricks did it use?
- [LLM03-059] What is the capacity factor in Switch Transformers, and what happens to tokens that overflow an expert?
- [LLM03-060] What is the shrinking batch problem in MoE training, and how is it mitigated?
- [LLM03-061] What is expert-choice routing, and how does it change the load-balancing story compared with token-choice routing?
- [LLM03-062] In MoE training, what happens to experts that receive no tokens for many steps, and how do you recover them?
- [LLM03-063] Why does the MoE load-balancing loss trade quality for stability?
- [LLM03-064] What makes MoE training harder to load-balance than dense training, and why do fine-grained experts make it harder still?
- [LLM03-065] DeepSeek-V3 uses auxiliary-loss-free balancing. What was wrong with the auxiliary loss, and how does the bias trick work?
- [LLM03-066] In auxiliary-loss-free load balancing, how would you set the bias update step size, and what happens if it is too aggressive?
- [LLM03-067] Does auxiliary-loss-free balancing remove the need for any balancing signal at inference time?
- [LLM03-068] How does capacity factor and token dropping interact with load balancing, including the auxiliary-loss-free bias?
- [LLM03-069] Design the router for an MoE LLM that must avoid expert collapse, token dropping and communication hot-spots. What would you monitor?
- [LLM03-070] How would you detect that tokens from one language or domain are piling onto a few overloaded experts?

## MoE training, serving and trade-offs
- [LLM03-071] What goes wrong when training MoE models, and what is the inference memory caveat?
- [LLM03-072] Why are MoE models harder to fine-tune than dense models, and what remedies exist?
- [LLM03-073] Compare MoE and dense models at equal active parameters or equal FLOPs in terms of quality, memory footprint and serving cost.
- [LLM03-074] How can techniques like mixture-of-experts improve inference efficiency?
- [LLM03-075] Why did later frontier models move toward MoE layers, and what does that do to serving?
- [LLM03-076] What are the system-design consequences of MoE for memory, batching and expert load balancing at serving time?
- [LLM03-077] Why is the KV cache of an MoE model not smaller than that of a dense model with the same attention configuration?
- [LLM03-078] Estimate the memory needed to host an 8x7B MoE in fp16 versus the compute per token. Which is the bottleneck?
- [LLM03-079] GLM-4.5 is an MoE with 355B total and 32B active parameters. What does that split buy you, and what does it cost?
- [LLM03-080] When would you pick a 30B MoE with ~3B active parameters over a 32B dense model?
- [LLM03-081] When would you recommend a dense model over an MoE to a customer self-hosting on limited VRAM?
- [LLM03-082] Why is batched inference harder for MoE than for dense models?
- [LLM03-083] Why does expert imbalance hurt more during training than during single-request inference?
- [LLM03-084] What does expert parallelism do to inference latency tails, and what all-to-all communication does it require?
- [LLM03-085] How would you serve a large MoE efficiently when every expert's weights must be resident even though only a few activate per token?
- [LLM03-086] A flagship model is a sparse MoE with ~10x more total than active parameters. Why does that suit private enterprise deployment, and where does it hurt?
- [LLM03-087] A model pairs MLA attention with a 128-expert MoE (top-8 plus a shared expert, loss-free balancing). What does each choice buy when serving many languages?
- [LLM03-088] When would you recommend a dense model over MoE despite MoE's training-compute advantage?

## Scaling laws and compute-optimal training
- [LLM03-089] What is a scaling law in LLM pretraining?
- [LLM03-090] What does the training compute estimate C ≈ 6ND assume, and where does it break down?
- [LLM03-091] What does the Chinchilla law say about the optimal ratio of parameters to training tokens, and what does "compute-optimal" mean?
- [LLM03-092] Compare the Kaplan and Chinchilla scaling laws. What did Chinchilla change?
- [LLM03-093] According to compute-optimal scaling, how should model size and training tokens grow together for a fixed compute budget?
- [LLM03-094] Given a compute budget of 1e23 FLOPs, use C ≈ 6ND and roughly 20 tokens per parameter to estimate the compute-optimal model size and token count.
- [LLM03-095] In the parametric loss form L(N,D) = E + A/N^a + B/D^b, what do the terms represent, and what does the irreducible term E mean?
- [LLM03-096] Why train an 8B model on 15T tokens when Chinchilla says about 160B tokens is optimal?
- [LLM03-097] Distinguish training-compute-optimal from inference-optimal scaling, and explain when each matters.
- [LLM03-098] How do scaling laws guide the choice of model size versus training data in practice?
- [LLM03-099] How would you use small-scale experiments to predict the loss of a much larger model, and what could break the extrapolation?
- [LLM03-100] Does lower pretraining loss translate smoothly into better downstream task performance? Where does that relationship break?
- [LLM03-101] Why did Kaplan's learning-rate schedule choice bias its conclusion about model size versus data?
- [LLM03-102] If high-quality data becomes the binding constraint, how does the optimal compute allocation shift? What happens when you must repeat data?
- [LLM03-103] Sketch the total-cost-of-ownership optimization that replaces Chinchilla's objective. How does distillation change the overtraining calculus?
- [LLM03-104] What is hyperparameter transfer across scale (for example muP), and why does it matter for scaling-law experiments?

## Emergent abilities
- [LLM03-105] What are emergent abilities in LLMs, and why is their existence debated?
- [LLM03-106] What is the "mirage" critique of emergent abilities, and where does the debate land practically?
- [LLM03-107] Are emergent abilities real phase transitions or artifacts of the chosen metric? How would you test that?
- [LLM03-108] Does chain-of-thought change which abilities appear emergent?
- [LLM03-109] Does instruction-following ability depend on model scale, and does chain-of-thought emerge only in large models?
- [LLM03-110] How does the emergent-abilities mirage debate affect capability forecasts based on scaling laws?
- [LLM03-111] How does the mirage critique of emergent abilities connect to grokking?

## State-space, linear-attention and hybrid models
- [LLM03-112] What is a state space model (SSM), and what problem does it solve when hybridized with a Transformer?
- [LLM03-113] How does Mamba compare with a Transformer in per-token inference cost and memory as context length grows?
- [LLM03-114] Mamba and state-space models were expected to replace Transformers. What actually happened, and why?
- [LLM03-115] Why is a Transformer-SSM hybrid attractive for long-context inference?
- [LLM03-116] How do dense, MoE and hybrid-attention architectures differ in what they optimize for?
- [LLM03-117] What idea do RWKV and RetNet share: recurrent inference with parallel training? What do they give up compared with attention?
- [LLM03-118] Why do pure SSMs tend to struggle with in-context retrieval and copying, and how do hybrids address it?
- [LLM03-119] What are attention-free Transformer architectures, and what are their trade-offs?
- [LLM03-120] Linear attention was written off for years. What do gated delta-rule layers like Gated DeltaNet change, and why are they showing up in hybrids?
- [LLM03-121] Why hybridize linear and full attention (for example one full-attention layer in four) rather than going all-linear or all-full, and what does it change when serving a 1M-token context?
- [LLM03-122] For an agent doing long tool-use trajectories, would you choose a hybrid or a pure Transformer architecture?
- [LLM03-123] A model advertises a 10M-token context window but scores poorly at 128K on a long-context benchmark. How do you advise a team planning to rely on it?

## Diffusion language models
- [LLM03-124] How does a diffusion language model differ from an autoregressive one, and where is that an advantage?
- [LLM03-125] If diffusion LLMs decode faster in parallel, why hasn't everyone switched?
- [LLM03-126] How do diffusion language models generate text, and why haven't they displaced autoregressive models?
- [LLM03-127] Why do tokens committed in the same denoising step risk being mutually inconsistent in a diffusion language model?
- [LLM03-128] How does block-wise diffusion recover KV caching, and what does it give up?
- [LLM03-129] Would you prefer a diffusion language model or an autoregressive LLM for latency-sensitive applications, and why?
- [LLM03-130] Which product would you pilot a diffusion language model on first, and what would you measure?

## Small language models and model selection
- [LLM03-131] When would you use a small language model rather than a frontier model, and which tasks suit each?
- [LLM03-132] How do small models such as Phi or Gemma get close to larger models' quality (data quality, distillation, longer training)?
- [LLM03-133] How does knowledge distillation produce a small language model from a larger teacher?
- [LLM03-134] What quantization and memory budget would you need to run a 7B-parameter model on a laptop?
- [LLM03-135] How would you choose between a closed frontier model and an open-weight model when quality is close but cost differs widely?
- [LLM03-136] Why do reasoning models differ architecturally and in training from standard chat models?
