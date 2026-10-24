## Autoregressive generation and stopping
- [E] What is autoregressive generation in an LLM, and how is text produced one token at a time? {Q003374,Q005302,Q012565}
- [E] What are logits, and how does an LLM turn them into the next token, step by step? {Q004674,Q005921,D00106}
- [M] In autoregressive generation, what is fed back as the next input: the sampled token id or the probability distribution? {Q003485}
- [M] Why is the decode phase of generation typically memory-bandwidth-bound rather than compute-bound? {GEN}
- [E] What are the main decoding strategies for choosing the next token? {Q003368,Q004266,Q007114}
- [E] Compare greedy decoding, beam search and sampling for text generation. {D00099}
- [M] Compare greedy, beam search, top-k, top-p and temperature sampling. When does each one fail? {Q004673,Q011795}
- [M] How do greedy, beam, temperature, top-k and top-p decoding differ, and when would you use each? {D03762}
- [M] Which inference-time parameters can you tune to control generation, and what does each one do? {Q004264}
- [M] How do tokens, the context window, temperature and top-p each affect an LLM's behavior? {Q003521}
- [M] How can you control text generation via prompts, modifying probabilities, or architectural changes? {D04879}
- [M] How do autoregressive and non-autoregressive generation differ in speed and quality? {D04878}
- [E] What are stop tokens (EOS), and how does an LLM know when to stop generating? {Q004675,Q005338,Q005922}
- [E] What is the difference between a stop token and a stop sequence? {Q004676}
- [M] What stopping criteria can you define for generation (EOS, max tokens, stop sequences), and how do they interact? {Q004267,Q007115,D00107}
- [M] How do logit bias and stop sequences give precise control over generation, and what are the pitfalls? {D00105}
- [M] What are logprobs, and what are they useful for in production systems? {Q007522}
- [H] Why is the probability of an answer not the same as the probability of the sequence that produces it? {Q007525}
- [M] What happens to the visible output when a reasoning model hits its max-token cap? {Q007677}
- [M] How would you safely continue a generation that was truncated in the middle of a JSON object? {Q008588}
- [M] A response ends mid-sentence in production. How do you tell whether it hit the token limit or a stop sequence, and what do you do? {GEN}

## Temperature
- [E] What is temperature in LLM inference, and how does it affect the output? {Q003373,Q004670,Q005336,Q007113}
- [E] What does temperature do mathematically to the logits, and what happens near zero and at very high values? {Q007445,D00100,D04570}
- [M] Given logits [2.0, 1.0, 0.0], roughly what are the softmax probabilities at T=1, and how do they change at T=0.5 and T=2? {GEN}
- [E] When you set temperature to 0, which decoding strategy are you effectively using? {Q003370}
- [E] What is greedy decoding, and what are its weaknesses compared with beam search? {D04572}
- [E] What do temperature and top_p actually do, and how do you choose them per task? {Q007659,Q011232}
- [M] How would you choose generation parameters for a code assistant versus a creative writing assistant? {D04575}
- [M] Why can high temperature increase hallucination while very low temperature lowers diversity? How would you choose in a QA product? {D04956}
- [M] If you had to raise output diversity without raising the error rate, what would you change instead of temperature? {Q007661}
- [H] Why is low temperature not the same thing as top-k truncation? {Q007320}
- [H] Why is text sampled at temperature 1 often worse than the model's "true" distribution would suggest? {Q007452}
- [M] A product team wants the model to be "more creative but still factually safe." Which decoding settings would you vary and how would you evaluate the result? {GEN}

## Top-k, top-p and min-p sampling
- [E] Compare greedy decoding, top-k sampling and top-p (nucleus) sampling. {Q007449}
- [M] Explain top-k and top-p sampling. How do they differ, and when is top-p preferable? {Q004672,D04569,D00101}
- [M] How do top-k, top-p and temperature each reshape the next-token distribution? {D04568}
- [M] What failure mode of top-k sampling does top-p (nucleus) sampling fix? {Q009618b}
- [M] In what order are top-k, top-p and temperature applied when combined, and does the order change the result? {D04571}
- [M] What happens if you set top-k to 1, or top-p to a very small value like 0.05? {GEN}
- [M] Explain min-p sampling. When do standard top-k and top-p settings fail? {Q007451,Q007518}
- [M] What does min-p or typical sampling try to improve over top-p? {D04955}
- [M] If you increase temperature, why do you usually also want min-p or top-p? {Q007447}
- [H] Why does top-p specifically break down at high temperature? {Q007519}
- [H] Truncation sampling renormalizes the remaining probabilities. What bias does this introduce, and when does it matter? {GEN}
- [M] How would you tune top-p and temperature empirically for a new task, and what metrics would you use? {GEN}

## Beam search, best-of-N and repetition
- [M] What is beam search, and how does it improve on greedy search? What does the beam width control? {Q004132,Q003369}
- [M] How is beam search fundamentally different from breadth-first or depth-first search? {Q003371}
- [M] Why do beam scores need length normalization, and how is it done? {D04576}
- [M] Why does raw beam search favour short sequences? {Q007596,Q010019}
- [M] Beam search is standard in machine translation. Why is it rarely used for open-ended LLM generation? {Q007593,D04573}
- [M] For which tasks (translation, summarization, code, chat) would you still choose beam search, and why? {GEN}
- [H] Why does likelihood diverge from quality for open-ended tasks? What is the entropy argument? {Q007594}
- [M] You enable beam search (width 4 to 8) and hit OOM at a context that was fine with greedy decoding. Why, and what happens to TTFT? {Q006982,Q010020}
- [H] How does beam search interact with batching and prefix sharing in an LLM serving system? {GEN}
- [M] What is self-consistency decoding, and how does best-of-N differ from it? {D00126}
- [H] Why does best-of-n with a reward model succeed where beam search fails? {Q007595}
- [M] Why do LLMs fall into repetitive loops, and what decoding-time and training-time remedies would you apply? {Q012506,D04451}
- [M] Your text generation repeats phrases in long outputs. How do you fix it? {Q004711}
- [H] Mechanistically, why does greedy decoding loop? {Q007450}
- [H] Why can top-p=1.0, temperature=1.0 still produce degenerate repetition, and what mitigations exist? {Q009619}
- [E] What is the difference between repetition, frequency and presence penalties? {GEN}
- [M] How does a repetition penalty modify logits, and what side effects can it have on code or structured text? {D00104,D04574}
- [H] Why do repetition penalties operate on tokens rather than words, and what artifacts does that cause? {Q007521}

## Determinism and reproducibility
- [M] Why does temperature 0 not guarantee identical outputs across identical API calls? {Q003585,Q007446,Q007660,Q008578,Q010633,D00102}
- [H] Why does a busier LLM server make output divergence more likely at temperature 0? {Q008579}
- [H] How do floating-point non-associativity and batch-size-dependent kernels cause nondeterministic LLM outputs? {GEN}
- [M] How do you get reproducible outputs when the API no longer accepts a temperature parameter? {Q011233,Q011326,D00103}
- [M] How do sampling controls on hosted frontier models differ from open-weight models, and what does that imply for determinism? {D00125}
- [M] What does a seed parameter guarantee, and what does it not? {GEN}
- [M] How would you make nucleus (top-p) sampling deterministic for reproducible on-device tests? {Q009268}
- [M] How would you design a regression test suite for an LLM feature, given nondeterministic generation? {GEN}

## Constrained and structured decoding
- [M] What is constrained decoding, and how does it differ from JSON mode, structured outputs and function calling? {Q005937,D00114}
- [M] How does constrained decoding guarantee valid JSON or grammar-conforming output? {D00113,D03764}
- [M] How does constrained decoding work at the logit level, and what does it do to output quality? {Q006833}
- [M] How do you make an LLM output comply with a required format (JSON, regex, schema), and what are the trade-offs of constrained decoding? {D04768}
- [M] How would you generate guaranteed-valid JSON: sampling settings or constrained decoding? {Q007520}
- [M] When would you prefer parse-and-retry over constrained decoding? {Q008672}
- [H] Why must the grammar be compiled against the tokenizer vocabulary in constrained decoding? {Q008671}
- [H] How is structured output enforced at the serving layer, and what are the throughput and quality costs? How would you mitigate them at scale? {Q008670,D00115}
- [M] What is a logits processor, and how would you implement one that bans a set of tokens? {GEN}
- [H] Why can schema-constrained decoding hurt answer quality when the schema forces the model to emit an answer field before its reasoning? {GEN}
- [H] How do tokenization boundaries (e.g., token healing, multi-character tokens) complicate grammar-constrained decoding? {GEN}
- [H] Your on-device model must emit valid, schema-conforming tool calls. How do you guarantee validity rather than hope for it? {Q009270}
- [H] How do constrained decoding and speculative decoding interact? {Q009272}

## Speculative decoding
- [M] What is speculative decoding, how does it speed up generation, and when would you use it? {Q003376,Q004431,Q005118,Q010847,Q011176,D03763}
- [M] Why can the target model verify k draft tokens in one forward pass at roughly the cost of a single decoding step? {GEN}
- [M] Why does speculative decoding preserve the output distribution of the target model? {Q007463,Q009400,Q010291,D00108}
- [H] Why does speculative decoding preserve the output distribution even when the draft model is terrible? {Q010178}
- [H] Derive why the speculative decoding acceptance rule preserves the target distribution. {Q008603a}
- [H] Explain speculative decoding: why is quality preserved, when does it help, and when does it not? {Q011803,Q008602,Q009918,Q010177}
- [M] How do you choose the draft length k in speculative decoding, and what happens to acceptance as k grows? {Q009919}
- [M] With draft length k=4 and a per-token acceptance rate of 0.8, what is the expected number of tokens produced per target forward pass? {GEN}
- [H] What acceptance rate do you need for speculative decoding to be a net win? {Q007465,Q009470}
- [M] How would you choose a draft model (size, tokenizer, training data) for speculative decoding? {GEN}
- [H] How does batch size change the economics of speculative decoding? A colleague says it should be disabled at high load; do you agree? {Q008603b,D00111}
- [M] Why does speculative decoding give little benefit for high-temperature creative generation? {Q011300,D00109,Q008676}
- [M] What is n-gram or lookahead speculation, and when does it beat a trained draft model? {Q005121,Q008604,D00112}
- [H] How does Medusa (multi-head speculative decoding) work? {Q005119}
- [H] How does EAGLE (feature-level speculative decoding) work, and how does it differ from traditional draft-model speculation? {Q005120,Q006174}
- [H] How do draft heads (Medusa, EAGLE, native MTP) differ from a separate small draft model? {Q011301,D00110}
- [M] What is Multi-Token Prediction (MTP), why do models add an MTP layer, and how does it help at inference time? {Q010290}
- [H] Why can an MTP draft head achieve higher acceptance than a separately trained small draft model? {Q007546,Q009469}
- [M] When does Multi-Token Prediction give little speed-up (low acceptance)? {Q010292}
- [M] Where does speculative decoding fit in a serving stack that separates prefill and decode? {Q009937}

## Context window fundamentals and management
- [E] What is the context window in an LLM, and why does it matter during inference? {Q003372,Q004668,Q005343}
- [E] Does the context window include output tokens? How do input and output budgets interact? {GEN}
- [E] Why does the same text consume different numbers of context tokens under different tokenizers? {GEN}
- [M] Why is the context window limited? Can a model accept arbitrary-length input in theory, and what architectural and hardware limits bound it? {Q004669,D04452}
- [M] What is the effect of increasing or decreasing an LLM's context window size? {Q011932}
- [M] Why is an LLM API stateless, and where does conversational memory actually live? {D00121}
- [H] Your Transformer runs out of memory on long documents due to quadratic self-attention. How do you scale it? {Q004703}
- [H] Estimate the KV cache size for a 70B-class model with grouped-query attention at 128k tokens. What dominates the memory? {GEN}
- [M] Your LLM-powered tool hits the context limit on long documents. What are your options? {Q004696,D00117}
- [M] How do you manage context window limits in long conversations? {Q010884}
- [M] How do you allocate the context window budget across system prompt, history, retrieved data and output? {Q006043}
- [M] What techniques exist to compress long contexts, and when would you use a semantic cache versus a sliding window? {Q006018,D00122}
- [M] How do you handle long contexts efficiently in production (context compression, prefix caching)? {Q004980}
- [M] A user uploads a 400-page contract well over the context window and asks for a one-paragraph summary. What is the best approach? {Q007007}
- [M] When would you choose long context over RAG, and when does RAG still win? {D00118}
- [H] A model claims a 10M-token window but scores poorly on a long-context benchmark at 128K. How would you advise a team that wants to "just dump everything into the context"? {Q010960}
- [H] When you push a model from 8K to hundreds of thousands of tokens of context, what breaks first, and why? {Q011986,Q009853}
- [H] How do you handle the high TTFT of million-token prompts? {Q011339,D00119}
- [H] How do inference frameworks handle ultra-long contexts (1M+ tokens)? What is the idea behind Ring Attention and block-wise attention? {Q006180}

## Lost in the middle and long-context reliability
- [M] What is the "lost in the middle" problem, and why doesn't a long context window equal reliable retrieval? {Q004739,Q007558}
- [H] What causes lost-in-the-middle behaviour (positional bias, attention patterns, training data)? {GEN}
- [M] How can lost-in-the-middle be mitigated in long-context scenarios? {Q003584,Q011796,Q010806}
- [E] What does the lost-in-the-middle effect imply for how you order retrieved context? {D00116,D04957}
- [M] You stuff 60 documents into one prompt; the model nails facts from the first and last few but ignores a crucial one in the middle. What is the best fix? {Q006941}
- [M] What is context rot, and why does response quality degrade as the context fills with irrelevant material? {D00120}
- [M] How would you detect lost-in-the-middle empirically in production? {Q007706}
- [M] How would you verify the usable context length of a model before shipping? {Q007509,Q010041}
- [M] What are the limitations of the needle-in-a-haystack test, and what harder long-context benchmarks would you use? {GEN}
- [M] How do you evaluate whether a long-context extension actually works, beyond perplexity? {D04958}

## Extending context length
- [M] How can you increase the context length of an LLM? {Q007176}
- [M] What are the solutions to the length extrapolation problem? {Q012510}
- [M] How do positional interpolation, NTK-aware scaling and YaRN differ for extending RoPE-based models? {GEN}
- [H] How do you take a model trained at 8K-32K context and make it work at 128K or more? {Q011987,Q009878}
- [H] What techniques let a pretrained model handle inputs much longer than its training context, and what does each sacrifice? {D04453}
- [H] Why does long-context extension usually still require some fine-tuning on long documents? {Q007508}
- [H] How do sliding-window attention and attention sinks (StreamingLLM) support unbounded streaming, and what do they sacrifice? {GEN}
- [H] After extending a model from 32k to 256k context with YaRN, how much short-context replay data would you mix in, and how would you pick that ratio? {Q007620}
- [H] If disabling RoPE scaling restores short-prompt quality in a context-extended model, what is your next move? {Q007621}
- [H] Your team plans to extend a 4k-context 70B model to 128k and quantize the KV cache to fit. What single safeguard belongs in the rollout plan above all? {Q006992}
