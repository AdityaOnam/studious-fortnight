---
domain: llm
topic: decoding_sampling_context_length
title: Decoding, sampling and context length
tags: [decoding, sampling, temperature, context-window]
count: 143
---
# Decoding, sampling and context length

## Autoregressive generation and stopping
- [LLM05-001] What is autoregressive generation in an LLM, and how is text produced one token at a time?
- [LLM05-002] What are logits, and how does an LLM turn them into the next token, step by step?
- [LLM05-003] In autoregressive generation, what is fed back as the next input: the sampled token id or the probability distribution?
- [LLM05-004] Why is the decode phase of generation typically memory-bandwidth-bound rather than compute-bound?
- [LLM05-005] What are the main decoding strategies for choosing the next token?
- [LLM05-006] Compare greedy decoding, beam search and sampling for text generation.
- [LLM05-007] Compare greedy, beam search, top-k, top-p and temperature sampling. When does each one fail?
- [LLM05-008] How do greedy, beam, temperature, top-k and top-p decoding differ, and when would you use each?
- [LLM05-009] Which inference-time parameters can you tune to control generation, and what does each one do?
- [LLM05-010] How do tokens, the context window, temperature and top-p each affect an LLM's behavior?
- [LLM05-011] How can you control text generation via prompts, modifying probabilities, or architectural changes?
- [LLM05-012] How do autoregressive and non-autoregressive generation differ in speed and quality?
- [LLM05-013] What are stop tokens (EOS), and how does an LLM know when to stop generating?
- [LLM05-014] What is the difference between a stop token and a stop sequence?
- [LLM05-015] What stopping criteria can you define for generation (EOS, max tokens, stop sequences), and how do they interact?
- [LLM05-016] How do logit bias and stop sequences give precise control over generation, and what are the pitfalls?
- [LLM05-017] What are logprobs, and what are they useful for in production systems?
- [LLM05-018] Why is the probability of an answer not the same as the probability of the sequence that produces it?
- [LLM05-019] What happens to the visible output when a reasoning model hits its max-token cap?
- [LLM05-020] How would you safely continue a generation that was truncated in the middle of a JSON object?
- [LLM05-021] A response ends mid-sentence in production. How do you tell whether it hit the token limit or a stop sequence, and what do you do?

## Temperature
- [LLM05-022] What is temperature in LLM inference, and how does it affect the output?
- [LLM05-023] What does temperature do mathematically to the logits, and what happens near zero and at very high values?
- [LLM05-024] Given logits [2.0, 1.0, 0.0], roughly what are the softmax probabilities at T=1, and how do they change at T=0.5 and T=2?
- [LLM05-025] When you set temperature to 0, which decoding strategy are you effectively using?
- [LLM05-026] What is greedy decoding, and what are its weaknesses compared with beam search?
- [LLM05-027] What do temperature and top_p actually do, and how do you choose them per task?
- [LLM05-028] How would you choose generation parameters for a code assistant versus a creative writing assistant?
- [LLM05-029] Why can high temperature increase hallucination while very low temperature lowers diversity? How would you choose in a QA product?
- [LLM05-030] If you had to raise output diversity without raising the error rate, what would you change instead of temperature?
- [LLM05-031] Why is low temperature not the same thing as top-k truncation?
- [LLM05-032] Why is text sampled at temperature 1 often worse than the model's "true" distribution would suggest?
- [LLM05-033] A product team wants the model to be "more creative but still factually safe." Which decoding settings would you vary and how would you evaluate the result?

## Top-k, top-p and min-p sampling
- [LLM05-034] Compare greedy decoding, top-k sampling and top-p (nucleus) sampling.
- [LLM05-035] Explain top-k and top-p sampling. How do they differ, and when is top-p preferable?
- [LLM05-036] How do top-k, top-p and temperature each reshape the next-token distribution?
- [LLM05-037] What failure mode of top-k sampling does top-p (nucleus) sampling fix?
- [LLM05-038] In what order are top-k, top-p and temperature applied when combined, and does the order change the result?
- [LLM05-039] What happens if you set top-k to 1, or top-p to a very small value like 0.05?
- [LLM05-040] Explain min-p sampling. When do standard top-k and top-p settings fail?
- [LLM05-041] What does min-p or typical sampling try to improve over top-p?
- [LLM05-042] If you increase temperature, why do you usually also want min-p or top-p?
- [LLM05-043] Why does top-p specifically break down at high temperature?
- [LLM05-044] Truncation sampling renormalizes the remaining probabilities. What bias does this introduce, and when does it matter?
- [LLM05-045] How would you tune top-p and temperature empirically for a new task, and what metrics would you use?

## Beam search, best-of-N and repetition
- [LLM05-046] What is beam search, and how does it improve on greedy search? What does the beam width control?
- [LLM05-047] How is beam search fundamentally different from breadth-first or depth-first search?
- [LLM05-048] Why do beam scores need length normalization, and how is it done?
- [LLM05-049] Why does raw beam search favour short sequences?
- [LLM05-050] Beam search is standard in machine translation. Why is it rarely used for open-ended LLM generation?
- [LLM05-051] For which tasks (translation, summarization, code, chat) would you still choose beam search, and why?
- [LLM05-052] Why does likelihood diverge from quality for open-ended tasks? What is the entropy argument?
- [LLM05-053] You enable beam search (width 4 to 8) and hit OOM at a context that was fine with greedy decoding. Why, and what happens to TTFT?
- [LLM05-054] How does beam search interact with batching and prefix sharing in an LLM serving system?
- [LLM05-055] What is self-consistency decoding, and how does best-of-N differ from it?
- [LLM05-056] Why does best-of-n with a reward model succeed where beam search fails?
- [LLM05-057] Why do LLMs fall into repetitive loops, and what decoding-time and training-time remedies would you apply?
- [LLM05-058] Your text generation repeats phrases in long outputs. How do you fix it?
- [LLM05-059] Mechanistically, why does greedy decoding loop?
- [LLM05-060] Why can top-p=1.0, temperature=1.0 still produce degenerate repetition, and what mitigations exist?
- [LLM05-061] What is the difference between repetition, frequency and presence penalties?
- [LLM05-062] How does a repetition penalty modify logits, and what side effects can it have on code or structured text?
- [LLM05-063] Why do repetition penalties operate on tokens rather than words, and what artifacts does that cause?

## Determinism and reproducibility
- [LLM05-064] Why does temperature 0 not guarantee identical outputs across identical API calls?
- [LLM05-065] Why does a busier LLM server make output divergence more likely at temperature 0?
- [LLM05-066] How do floating-point non-associativity and batch-size-dependent kernels cause nondeterministic LLM outputs?
- [LLM05-067] How do you get reproducible outputs when the API no longer accepts a temperature parameter?
- [LLM05-068] How do sampling controls on hosted frontier models differ from open-weight models, and what does that imply for determinism?
- [LLM05-069] What does a seed parameter guarantee, and what does it not?
- [LLM05-070] How would you make nucleus (top-p) sampling deterministic for reproducible on-device tests?
- [LLM05-071] How would you design a regression test suite for an LLM feature, given nondeterministic generation?

## Constrained and structured decoding
- [LLM05-072] What is constrained decoding, and how does it differ from JSON mode, structured outputs and function calling?
- [LLM05-073] How does constrained decoding guarantee valid JSON or grammar-conforming output?
- [LLM05-074] How does constrained decoding work at the logit level, and what does it do to output quality?
- [LLM05-075] How do you make an LLM output comply with a required format (JSON, regex, schema), and what are the trade-offs of constrained decoding?
- [LLM05-076] How would you generate guaranteed-valid JSON: sampling settings or constrained decoding?
- [LLM05-077] When would you prefer parse-and-retry over constrained decoding?
- [LLM05-078] Why must the grammar be compiled against the tokenizer vocabulary in constrained decoding?
- [LLM05-079] How is structured output enforced at the serving layer, and what are the throughput and quality costs? How would you mitigate them at scale?
- [LLM05-080] What is a logits processor, and how would you implement one that bans a set of tokens?
- [LLM05-081] Why can schema-constrained decoding hurt answer quality when the schema forces the model to emit an answer field before its reasoning?
- [LLM05-082] How do tokenization boundaries (e.g., token healing, multi-character tokens) complicate grammar-constrained decoding?
- [LLM05-083] Your on-device model must emit valid, schema-conforming tool calls. How do you guarantee validity rather than hope for it?
- [LLM05-084] How do constrained decoding and speculative decoding interact?

## Speculative decoding
- [LLM05-085] What is speculative decoding, how does it speed up generation, and when would you use it?
- [LLM05-086] Why can the target model verify k draft tokens in one forward pass at roughly the cost of a single decoding step?
- [LLM05-087] Why does speculative decoding preserve the output distribution of the target model?
- [LLM05-088] Why does speculative decoding preserve the output distribution even when the draft model is terrible?
- [LLM05-089] Derive why the speculative decoding acceptance rule preserves the target distribution.
- [LLM05-090] Explain speculative decoding: why is quality preserved, when does it help, and when does it not?
- [LLM05-091] How do you choose the draft length k in speculative decoding, and what happens to acceptance as k grows?
- [LLM05-092] With draft length k=4 and a per-token acceptance rate of 0.8, what is the expected number of tokens produced per target forward pass?
- [LLM05-093] What acceptance rate do you need for speculative decoding to be a net win?
- [LLM05-094] How would you choose a draft model (size, tokenizer, training data) for speculative decoding?
- [LLM05-095] How does batch size change the economics of speculative decoding? A colleague says it should be disabled at high load; do you agree?
- [LLM05-096] Why does speculative decoding give little benefit for high-temperature creative generation?
- [LLM05-097] What is n-gram or lookahead speculation, and when does it beat a trained draft model?
- [LLM05-098] How does Medusa (multi-head speculative decoding) work?
- [LLM05-099] How does EAGLE (feature-level speculative decoding) work, and how does it differ from traditional draft-model speculation?
- [LLM05-100] How do draft heads (Medusa, EAGLE, native MTP) differ from a separate small draft model?
- [LLM05-101] What is Multi-Token Prediction (MTP), why do models add an MTP layer, and how does it help at inference time?
- [LLM05-102] Why can an MTP draft head achieve higher acceptance than a separately trained small draft model?
- [LLM05-103] When does Multi-Token Prediction give little speed-up (low acceptance)?
- [LLM05-104] Where does speculative decoding fit in a serving stack that separates prefill and decode?

## Context window fundamentals and management
- [LLM05-105] What is the context window in an LLM, and why does it matter during inference?
- [LLM05-106] Does the context window include output tokens? How do input and output budgets interact?
- [LLM05-107] Why does the same text consume different numbers of context tokens under different tokenizers?
- [LLM05-108] Why is the context window limited? Can a model accept arbitrary-length input in theory, and what architectural and hardware limits bound it?
- [LLM05-109] What is the effect of increasing or decreasing an LLM's context window size?
- [LLM05-110] Why is an LLM API stateless, and where does conversational memory actually live?
- [LLM05-111] Your Transformer runs out of memory on long documents due to quadratic self-attention. How do you scale it?
- [LLM05-112] Estimate the KV cache size for a 70B-class model with grouped-query attention at 128k tokens. What dominates the memory?
- [LLM05-113] Your LLM-powered tool hits the context limit on long documents. What are your options?
- [LLM05-114] How do you manage context window limits in long conversations?
- [LLM05-115] How do you allocate the context window budget across system prompt, history, retrieved data and output?
- [LLM05-116] What techniques exist to compress long contexts, and when would you use a semantic cache versus a sliding window?
- [LLM05-117] How do you handle long contexts efficiently in production (context compression, prefix caching)?
- [LLM05-118] A user uploads a 400-page contract well over the context window and asks for a one-paragraph summary. What is the best approach?
- [LLM05-119] When would you choose long context over RAG, and when does RAG still win?
- [LLM05-120] A model claims a 10M-token window but scores poorly on a long-context benchmark at 128K. How would you advise a team that wants to "just dump everything into the context"?
- [LLM05-121] When you push a model from 8K to hundreds of thousands of tokens of context, what breaks first, and why?
- [LLM05-122] How do you handle the high TTFT of million-token prompts?
- [LLM05-123] How do inference frameworks handle ultra-long contexts (1M+ tokens)? What is the idea behind Ring Attention and block-wise attention?

## Lost in the middle and long-context reliability
- [LLM05-124] What is the "lost in the middle" problem, and why doesn't a long context window equal reliable retrieval?
- [LLM05-125] What causes lost-in-the-middle behaviour (positional bias, attention patterns, training data)?
- [LLM05-126] How can lost-in-the-middle be mitigated in long-context scenarios?
- [LLM05-127] What does the lost-in-the-middle effect imply for how you order retrieved context?
- [LLM05-128] You stuff 60 documents into one prompt; the model nails facts from the first and last few but ignores a crucial one in the middle. What is the best fix?
- [LLM05-129] What is context rot, and why does response quality degrade as the context fills with irrelevant material?
- [LLM05-130] How would you detect lost-in-the-middle empirically in production?
- [LLM05-131] How would you verify the usable context length of a model before shipping?
- [LLM05-132] What are the limitations of the needle-in-a-haystack test, and what harder long-context benchmarks would you use?
- [LLM05-133] How do you evaluate whether a long-context extension actually works, beyond perplexity?

## Extending context length
- [LLM05-134] How can you increase the context length of an LLM?
- [LLM05-135] What are the solutions to the length extrapolation problem?
- [LLM05-136] How do positional interpolation, NTK-aware scaling and YaRN differ for extending RoPE-based models?
- [LLM05-137] How do you take a model trained at 8K-32K context and make it work at 128K or more?
- [LLM05-138] What techniques let a pretrained model handle inputs much longer than its training context, and what does each sacrifice?
- [LLM05-139] Why does long-context extension usually still require some fine-tuning on long documents?
- [LLM05-140] How do sliding-window attention and attention sinks (StreamingLLM) support unbounded streaming, and what do they sacrifice?
- [LLM05-141] After extending a model from 32k to 256k context with YaRN, how much short-context replay data would you mix in, and how would you pick that ratio?
- [LLM05-142] If disabling RoPE scaling restores short-prompt quality in a context-extended model, what is your next move?
- [LLM05-143] Your team plans to extend a 4k-context 70B model to 128k and quantize the KV cache to fit. What single safeguard belongs in the rollout plan above all?
