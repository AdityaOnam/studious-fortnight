## Language model and architecture basics
- [E] What is a large language model, and how does it differ from a traditional statistical (n-gram) language model? {Q004258,Q001649,Q004651,Q001651,Q001004,Q007110}
- [E] What are autoregressive models, and how is the probability of a sequence factorized in an autoregressive language model? {Q004713,D04456}
- [E] What is a foundation model, and how has the foundation-model paradigm changed how AI systems are built? {Q004650}
- [E] What is the difference between dense and sparse models? {Q004684}
- [E] Why can an encoder-only model such as BERT not be used directly for open-ended text generation? {GEN}
- [M] How does ChatGPT work end to end, from the pretrained model to what happens after you press Enter? {Q001002,Q000639,Q004652}
- [M] How does GPT-4 differ from GPT-3 in capabilities and architecture, as far as is publicly known? {Q001659}
- [M] Describe the GPT architecture and explain how a decoder-only design supports language generation. {Q001009,Q001012}
- [M] What is the difference between encoder-only, decoder-only and encoder-decoder Transformers? {Q004679,Q007179,D04450}
- [M] Explain the different LLM architecture families and which kind of task each is best suited to. {Q012401}
- [M] What is the difference between a prefix LM and a causal LM in terms of attention masks and which tokens can attend to which? {Q012505,D04441}
- [M] What are the trade-offs between causal, prefix and encoder-decoder language models for generation versus understanding tasks? {D04442}
- [M] How do T5-style span-corruption pretraining and GPT-style next-token pretraining differ as objectives? {GEN}
- [M] What is cross-attention, and where does it appear in an encoder-decoder model but not in a decoder-only one? {GEN}
- [M] Why have most mainstream LLMs converged on causal decoder-only architectures instead of encoder-decoder? {Q005923,Q005969,D04446}
- [M] Why is decoder-only pretraining often said to give better zero-shot performance than encoder-decoder pretraining? {D04448}
- [M] If you were building a translation system today, would you choose an encoder-decoder or a decoder-only LLM, and on what criteria? {Q007432}
- [M] Roughly estimate the parameter count of a decoder-only Transformer from its number of layers and hidden size. Where do most of the parameters live? {GEN}
- [M] How does the scale of the model and the dataset size affect pretraining and the resulting model? {Q012406,D04599}
- [H] At a fixed parameter budget, how would you trade depth against width, and what do on-device constraints change? {Q009251,GEN}

## Model families and design choices
- [M] What changed architecturally between GPT-2 and Llama 2? {Q011217}
- [M] What architectural changes distinguish LLaMA from the original Transformer (RMSNorm pre-norm, SwiGLU, RoPE)? {D04539}
- [M] What changed between LLaMA 1, 2 and 3 in data size, context length, tokenizer vocabulary and attention? {D04541}
- [M] How do the ChatGLM, LLaMA and GPT families differ in position encoding, masking and normalization? {D04538}
- [M] What is the GLM autoregressive blank-infilling objective, and how does it unify understanding and generation? {D04536}
- [M] Why do modern LLMs use RMSNorm with pre-normalization instead of LayerNorm with post-normalization? {GEN}
- [M] Why use grouped-query attention rather than multi-head or multi-query attention in models like Llama and Mistral? {GEN}
- [M] What is sliding-window attention in Mistral, and how does stacking layers let information travel beyond the window? {GEN}
- [M] Why did LLaMA 3 invest so heavily in data quality and filtering, and how does that interact with scaling-law predictions? {D04542}
- [M] Compare the architectural choices of Llama, Mistral, Gemma and DeepSeek models. What does each family optimize for? {GEN}
- [H] Explain why a Llama-class model uses grouped-query attention, RoPE and SwiGLU instead of the vanilla 2017 Transformer. {Q009749}
- [H] What is Multi-head Latent Attention (MLA) in DeepSeek models, and how does it shrink the KV cache compared with GQA? {GEN}
- [H] Which architectural innovations does DeepSeek-V3 combine (MLA, DeepSeekMoE, multi-token prediction, load balancing), and what does each buy? {Q004685}
- [H] What is Multi-Token Prediction (MTP), why add an MTP layer, and how can it help at inference time? {Q011992}
- [H] Walk through a LLaMA-2 forward pass for one generated token, naming each module from embedding to logits. {D04546}

## Mixture of experts fundamentals
- [E] What is a mixture-of-experts model, and how does it differ from a dense model? {Q007214}
- [M] Explain mixture of experts: the router, top-k expert selection, and why it saves compute per token. {Q004324,Q007573,D00056,D03757,Q004683}
- [M] What is the difference between active and total parameters in an MoE model, and which one governs memory versus FLOPs? {Q004437,D04914}
- [M] How does an MoE architecture scale model capacity without scaling per-token FLOPs? {Q011793,D04582}
- [M] What problem does the sparsely-gated mixture-of-experts layer solve, and how does the gating network select experts? {D04577}
- [M] What changes inside a Transformer decoder block when you convert it to a mixture-of-experts model? {Q007412}
- [M] Why does MoE replace the feed-forward network rather than the attention layer? {Q007459}
- [M] Why route per token rather than per sequence in a mixture-of-experts model? {Q007574}
- [M] Explain how a Mixtral-style sparse MoE works. Why does a roughly 47B-parameter model run at about the cost of a 13B one? {Q011975,Q009821}
- [M] How does a shared (always-on) expert change the routing dynamics in an MoE? {Q009868}
- [M] What do experts in an MoE model actually specialize in, empirically? {Q007575,D04588}
- [M] Why is MoE another response to the same economic pressure that pushes training far beyond Chinchilla-optimal? {Q007568}
- [M] How do GShard, Switch Transformer and GLaM differ in routing (top-2 vs top-1), capacity factor and expert placement? {D04583}
- [M] How can MoE be used to make a dense model lighter, as in MoEBERT's conversion of FFNs into experts? {D04592}
- [M] What is upcycling, i.e. initializing an MoE from a dense checkpoint, and what are its pros and cons? {GEN}
- [H] Is a 47B-total, 13B-active MoE comparable to a 13B dense model or a 47B dense model, and on which axis? {Q007576}
- [H] Walk through DeepSeekMoE. How do fine-grained experts and shared experts differ from a standard top-2 MoE like Mixtral? {Q009462,D04912}

## MoE routing and load balancing
- [M] What is noisy top-k gating, and why is noise added to the gate logits? {D04578}
- [M] Why does an MoE layer need an auxiliary load-balancing loss, and what happens to expert utilization without it? {D04580,D00058}
- [M] Describe the importance loss and load loss used to balance experts in sparsely-gated MoE. {D04581}
- [M] Write down the Switch Transformer load-balancing auxiliary loss and explain what it penalizes. {D04586}
- [M] What is the router z-loss in ST-MoE, and what instability does it address? {D04587}
- [M] Why did Switch Transformer route each token to a single expert, and what stability tricks did it use? {D04585,D04911}
- [M] What is the capacity factor in Switch Transformers, and what happens to tokens that overflow an expert? {D04584}
- [M] What is the shrinking batch problem in MoE training, and how is it mitigated? {D04579}
- [M] What is expert-choice routing, and how does it change the load-balancing story compared with token-choice routing? {D04913,Q010036}
- [M] In MoE training, what happens to experts that receive no tokens for many steps, and how do you recover them? {Q010275}
- [H] Why does the MoE load-balancing loss trade quality for stability? {Q007578}
- [H] What makes MoE training harder to load-balance than dense training, and why do fine-grained experts make it harder still? {Q009766,Q009463}
- [H] DeepSeek-V3 uses auxiliary-loss-free balancing. What was wrong with the auxiliary loss, and how does the bias trick work? {Q009465,Q010274b}
- [H] In auxiliary-loss-free load balancing, how would you set the bias update step size, and what happens if it is too aggressive? {Q009466}
- [H] Does auxiliary-loss-free balancing remove the need for any balancing signal at inference time? {Q009467}
- [H] How does capacity factor and token dropping interact with load balancing, including the auxiliary-loss-free bias? {Q010276,Q009483b}
- [H] Design the router for an MoE LLM that must avoid expert collapse, token dropping and communication hot-spots. What would you monitor? {D04915}
- [H] How would you detect that tokens from one language or domain are piling onto a few overloaded experts? {Q010096}

## MoE training, serving and trade-offs
- [M] What goes wrong when training MoE models, and what is the inference memory caveat? {Q007577}
- [M] Why are MoE models harder to fine-tune than dense models, and what remedies exist? {D04589}
- [M] Compare MoE and dense models at equal active parameters or equal FLOPs in terms of quality, memory footprint and serving cost. {D04590}
- [M] How can techniques like mixture-of-experts improve inference efficiency? {Q003367}
- [M] Why did later frontier models move toward MoE layers, and what does that do to serving? {Q009751}
- [M] What are the system-design consequences of MoE for memory, batching and expert load balancing at serving time? {D00057}
- [M] Why is the KV cache of an MoE model not smaller than that of a dense model with the same attention configuration? {D00059}
- [M] Estimate the memory needed to host an 8x7B MoE in fp16 versus the compute per token. Which is the bottleneck? {GEN}
- [M] GLM-4.5 is an MoE with 355B total and 32B active parameters. What does that split buy you, and what does it cost? {Q011991,Q010271}
- [M] When would you pick a 30B MoE with ~3B active parameters over a 32B dense model? {Q011998}
- [M] When would you recommend a dense model over an MoE to a customer self-hosting on limited VRAM? {Q009823}
- [H] Why is batched inference harder for MoE than for dense models? {Q009822}
- [H] Why does expert imbalance hurt more during training than during single-request inference? {Q009867}
- [H] What does expert parallelism do to inference latency tails, and what all-to-all communication does it require? {Q007579,GEN}
- [H] How would you serve a large MoE efficiently when every expert's weights must be resident even though only a few activate per token? {D04591}
- [H] A flagship model is a sparse MoE with ~10x more total than active parameters. Why does that suit private enterprise deployment, and where does it hurt? {Q011977,Q009373}
- [H] A model pairs MLA attention with a 128-expert MoE (top-8 plus a shared expert, loss-free balancing). What does each choice buy when serving many languages? {Q010095}
- [H] When would you recommend a dense model over MoE despite MoE's training-compute advantage? {Q007580}

## Scaling laws and compute-optimal training
- [E] What is a scaling law in LLM pretraining? {Q003339,Q005926}
- [M] What does the training compute estimate C ≈ 6ND assume, and where does it break down? {Q007564}
- [M] What does the Chinchilla law say about the optimal ratio of parameters to training tokens, and what does "compute-optimal" mean? {D00060,Q004694,Q005967,D03758,Q011792}
- [M] Compare the Kaplan and Chinchilla scaling laws. What did Chinchilla change? {Q007562,D04916,Q005926}
- [M] According to compute-optimal scaling, how should model size and training tokens grow together for a fixed compute budget? {D04596}
- [M] Given a compute budget of 1e23 FLOPs, use C ≈ 6ND and roughly 20 tokens per parameter to estimate the compute-optimal model size and token count. {GEN}
- [M] In the parametric loss form L(N,D) = E + A/N^a + B/D^b, what do the terms represent, and what does the irreducible term E mean? {GEN}
- [M] Why train an 8B model on 15T tokens when Chinchilla says about 160B tokens is optimal? {Q011266,Q007566,D00061}
- [M] Distinguish training-compute-optimal from inference-optimal scaling, and explain when each matters. {D00062}
- [M] How do scaling laws guide the choice of model size versus training data in practice? {Q004694}
- [M] How would you use small-scale experiments to predict the loss of a much larger model, and what could break the extrapolation? {D04917}
- [M] Does lower pretraining loss translate smoothly into better downstream task performance? Where does that relationship break? {GEN}
- [H] Why did Kaplan's learning-rate schedule choice bias its conclusion about model size versus data? {Q007563}
- [H] If high-quality data becomes the binding constraint, how does the optimal compute allocation shift? What happens when you must repeat data? {Q007565}
- [H] Sketch the total-cost-of-ownership optimization that replaces Chinchilla's objective. How does distillation change the overtraining calculus? {Q007567,Q007566,D04597}
- [H] What is hyperparameter transfer across scale (for example muP), and why does it matter for scaling-law experiments? {GEN}

## Emergent abilities
- [M] What are emergent abilities in LLMs, and why is their existence debated? {D03759,D04444}
- [M] What is the "mirage" critique of emergent abilities, and where does the debate land practically? {Q007569}
- [M] Are emergent abilities real phase transitions or artifacts of the chosen metric? How would you test that? {D00063,D04445}
- [M] Does chain-of-thought change which abilities appear emergent? {Q007572}
- [M] Does instruction-following ability depend on model scale, and does chain-of-thought emerge only in large models? {D04603}
- [H] How does the emergent-abilities mirage debate affect capability forecasts based on scaling laws? {Q007571}
- [H] How does the mirage critique of emergent abilities connect to grokking? {Q007611}

## State-space, linear-attention and hybrid models
- [M] What is a state space model (SSM), and what problem does it solve when hybridized with a Transformer? {Q005959}
- [M] How does Mamba compare with a Transformer in per-token inference cost and memory as context length grows? {GEN}
- [M] Mamba and state-space models were expected to replace Transformers. What actually happened, and why? {Q007548}
- [M] Why is a Transformer-SSM hybrid attractive for long-context inference? {D00073}
- [M] How do dense, MoE and hybrid-attention architectures differ in what they optimize for? {D00065}
- [M] What idea do RWKV and RetNet share: recurrent inference with parallel training? What do they give up compared with attention? {GEN}
- [H] Why do pure SSMs tend to struggle with in-context retrieval and copying, and how do hybrids address it? {GEN}
- [H] What are attention-free Transformer architectures, and what are their trade-offs? {Q011902}
- [H] Linear attention was written off for years. What do gated delta-rule layers like Gated DeltaNet change, and why are they showing up in hybrids? {Q007630}
- [H] Why hybridize linear and full attention (for example one full-attention layer in four) rather than going all-linear or all-full, and what does it change when serving a 1M-token context? {Q009887,Q010057}
- [H] For an agent doing long tool-use trajectories, would you choose a hybrid or a pure Transformer architecture? {Q007550}
- [H] A model advertises a 10M-token context window but scores poorly at 128K on a long-context benchmark. How do you advise a team planning to rely on it? {D00074}

## Diffusion language models
- [M] How does a diffusion language model differ from an autoregressive one, and where is that an advantage? {Q011316,D00066}
- [M] If diffusion LLMs decode faster in parallel, why hasn't everyone switched? {Q011317,D00067}
- [H] How do diffusion language models generate text, and why haven't they displaced autoregressive models? {Q007626}
- [H] Why do tokens committed in the same denoising step risk being mutually inconsistent in a diffusion language model? {Q007627}
- [H] How does block-wise diffusion recover KV caching, and what does it give up? {Q007628}
- [H] Would you prefer a diffusion language model or an autoregressive LLM for latency-sensitive applications, and why? {Q003375}
- [H] Which product would you pilot a diffusion language model on first, and what would you measure? {Q007629}

## Small language models and model selection
- [M] When would you use a small language model rather than a frontier model, and which tasks suit each? {Q010839,D00064}
- [M] How do small models such as Phi or Gemma get close to larger models' quality (data quality, distillation, longer training)? {GEN}
- [M] How does knowledge distillation produce a small language model from a larger teacher? {GEN}
- [M] What quantization and memory budget would you need to run a 7B-parameter model on a laptop? {GEN}
- [M] How would you choose between a closed frontier model and an open-weight model when quality is close but cost differs widely? {D00070}
- [M] Why do reasoning models differ architecturally and in training from standard chat models? {D00071}
