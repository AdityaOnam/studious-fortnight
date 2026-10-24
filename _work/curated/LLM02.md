## Tokens and tokenization basics
- [E] What is tokenization in LLMs, and why is it necessary? {Q001008,Q003329,Q004656,Q012403,Q004261}
- [E] What is a token, and how does it differ from a word? {Q004260,Q007111}
- [E] Why do LLMs use subword tokenization instead of whole words or raw characters? {Q007437,Q005333,D04558}
- [E] After tokenization, how are token IDs converted into embeddings, and what is the embedding table? {Q003366,D00048}
- [E] What is the difference between a tokenizer's encode and decode steps, and is the round trip always lossless? {GEN}
- [M] How do LLMs handle out-of-vocabulary words? {Q003338}
- [M] Walk through the pipeline from raw text to model input: normalization, pre-tokenization, subword tokenization, special tokens and embedding lookup. {Q001017}
- [M] Why are Unicode normalization and pre-tokenization (whitespace, digit splitting) important in tokenizer design? {D04910}
- [M] Why does pre-tokenization matter in BPE, and what would go wrong without word-boundary constraints? {Q007477}
- [M] Why do "the" and " the" (with a leading space) need to be separate tokens? {Q007478}
- [M] What is a token, and why do Chinese, English and code consume different numbers of tokens? {Q003583}
- [M] What are special tokens and chat templates, and what breaks when the wrong template is used at inference? {D00043}
- [M] What are BOS, EOS and padding tokens used for, and why can a missing EOS or wrong pad token break fine-tuning? {GEN}
- [M] Why is an embedding lookup used instead of multiplying a one-hot vector by a weight matrix? {GEN}
- [M] Are token embeddings contextual? How does the input embedding of a token differ from its hidden state at a deep layer? {GEN}
- [H] How would you check whether the learned token embeddings place semantically related tokens close together, and what are the limits of that analysis? {GEN}

## BPE, WordPiece and Unigram
- [E] What is Byte Pair Encoding, and how does it build its vocabulary? {Q004657,Q005334}
- [M] Walk through the BPE training algorithm step by step, and explain how a new string is encoded afterwards. {Q007476,D04559,D00036}
- [M] When encoding with BPE, why must merges be applied in the order they were learned rather than by longest match? {GEN}
- [M] How does WordPiece differ from BPE in how it selects merges? {D04560}
- [M] How does unigram-LM tokenization differ conceptually from BPE? {Q007479}
- [M] Compare BPE, WordPiece and unigram tokenization in how vocabularies are learned and how text is segmented. {D00037}
- [H] Given the same vocabulary size, why might unigram-LM produce more linguistically natural segmentations than BPE? {Q007483}
- [M] What is subword regularization (e.g. BPE-dropout or unigram sampling), and why can it improve robustness? {GEN}
- [H] BPE segments greedily and deterministically. What suboptimality does this introduce compared with a segmentation that minimizes token count or maximizes likelihood? {GEN}
- [M] How does the composition of the tokenizer training corpus shape the vocabulary, and what goes wrong if it differs from the pretraining mix? {GEN}
- [M] Why do a tokenizer's merge rules or vocabulary file need to be versioned together with the model weights? {GEN}

## Byte-level BPE and SentencePiece
- [M] What is SentencePiece, and what does it add compared with running BPE over pre-tokenized words? {Q004658,D04562}
- [M] Why does SentencePiece encode whitespace explicitly, and what property does that buy? {Q007481}
- [M] How does SentencePiece handle languages without whitespace, such as Japanese or Chinese? {GEN}
- [E] What is byte-fallback in tokenization? {Q007482}
- [M] How does byte-level BPE guarantee that there are no out-of-vocabulary strings? {Q007438,D04561}
- [M] Why is byte-level BPE attractive for robustness, and what is its downside for non-Latin scripts? {D00039}
- [M] Compare BPE, WordPiece, SentencePiece and byte-level BPE. {Q007480,D03756}
- [M] Byte-level tokens can split a multi-byte UTF-8 character across tokens. How does that affect streaming output, and how do serving stacks handle it? {GEN}
- [M] Why do GPT-2 style byte-level tokenizers map raw bytes to printable Unicode characters before applying merges? {GEN}

## Vocabulary size and embedding tables
- [M] What are the tradeoffs in choosing vocabulary size, in terms of embedding parameters, sequence length, softmax cost and multilingual quality? {Q007484,D00038,D04564}
- [M] How would you size the embedding table for a 50k-vocabulary model with d_model=4096, and what does it cost? {Q006960}
- [M] Compute the embedding and LM-head parameters for a 128K vocabulary with d_model=4096, tied versus untied, and compare to an 8B-parameter model. {GEN}
- [M] How does vocabulary size affect bytes per token, and through that the effective context window and inference cost per document? {GEN}
- [H] A large vocabulary causes computation issues and a small one causes OOV or long sequences. How would you find the best balance? {Q007178}
- [H] With a 100K-token vocabulary, which parts of the transformer become expensive, and how would you reduce that cost? {Q007177}
- [M] Why do many models pad their vocabulary size to a multiple of 64 or 128? {GEN}
- [M] What is weight tying, and why do some models tie the embedding and output matrices while others do not? {Q007460}
- [H] How does the vocabulary size decision interact with the weight-tying decision? {Q007461}
- [H] Why does weight-tying the embedding and LM head matter more for small models? {Q007486}
- [H] What happens to a weight-tied model if you want to extend the vocabulary after training? {Q007462}
- [M] When is extending the vocabulary of a pretrained model for a new domain or language worthwhile, and what are the risks? {D04565}
- [H] Describe the steps to extend a LLaMA tokenizer with new tokens and initialize their embeddings so continued pretraining converges. {D04566}
- [H] How would you initialize embeddings for newly added tokens (random, mean of existing, subword average), and what are the tradeoffs? {GEN}
- [H] What breaks if you simply bolt 20k new Indic tokens onto an existing English tokenizer's vocabulary? {Q010062}
- [H] Why does adding a new language after pretraining rarely mean just retraining the tokenizer? {Q010031}
- [H] Qwen uses byte-level BPE with a ~151K vocabulary, extra multilingual coverage and digits split into single characters. Why those choices, and what are the trade-offs? {Q011996,Q010029}
- [H] What problems do very large vocabularies (250K+) create for training undertrained rare tokens, softmax cost and memory, and how are they mitigated? {GEN}
- [H] Why is comparing perplexity across models with different tokenizers misleading, and what metric would you use instead? {GEN}

## Tokenizer failure modes and debugging
- [M] Why do LLMs struggle with simple character counting or reversing strings? {Q011200,D00040,D04567}
- [M] Why do LLMs famously miscount the number of r's in "strawberry"? {Q007441}
- [M] Why does asking the model to spell the word out first fix the letter-counting error? {Q007442}
- [M] What other task categories fail for the same root cause as letter counting? {Q007443}
- [M] How would a byte-level model differ on letter-counting tasks? {Q007444}
- [M] Your model counts the letters in "ELEPHANT" correctly when it can write Python but fails when asked directly, and a teammate wants to fine-tune on letter-counting examples. What is the best read? {Q006955}
- [M] Why does single-digit number tokenization improve arithmetic in LLMs? {Q007488}
- [M] Why do digit and whitespace handling in the tokenizer affect arithmetic and code benchmarks? {Q009713}
- [M] Why does the whitespace and formatting of code or JSON change token counts and model behavior? {D00045}
- [M] What are glitch tokens, and what causes them? {Q007485}
- [H] A model emits bizarre, unsteerable text whenever a specific rare username-like string appears in the prompt, even across temperatures and rephrasings. What is the best explanation? {Q006961}
- [M] Your tokenizer splits important domain terms into meaningless subword pieces. How do you fix it? {Q004701}
- [M] What happens when you swap the tokenizer between a model and its fine-tuned variant or serving stack? {Q011202,D00041}
- [M] How would you detect a train/inference tokenization mismatch after the fact? {Q009714}
- [M] Why is a production tokenizer library often written in Rust, and what tokenizer bugs bite people in practice? {Q012078,Q009712}
- [M] How would tokenization affect a code-diff-generation feature? {Q007490}
- [M] You build a code assistant on a model whose tokenizer was trained on web prose, and long files blow the context window sooner than expected. What is the strongest lever? {Q006957}
- [H] A prompt ends with a trailing space and completions become strange. Why does this happen at the token level? {GEN}
- [M] What is token healing, and when is it needed for prefix-completion prompts? {GEN}
- [M] Why can the same text tokenize differently depending on leading whitespace or casing, and how does that make prompts brittle? {GEN}
- [H] Why do token boundaries make grammar-constrained or JSON-schema-constrained decoding tricky? {GEN}

## Multilingual tokenization and cost
- [E] What is tokenizer fertility (tokens per word), and why does it matter? {GEN}
- [M] What is the effect of tokenizer choice on multilingual pricing and quality? {Q007439}
- [M] How does tokenization affect cost and latency for non-English languages, and what can be done about it? {D00042}
- [M] What happens to multilingual and low-resource languages when a tokenizer is trained mostly on English text? {D04563}
- [M] Why is tokenization the first bottleneck for Indian-language LLMs, and how does a low-fertility tokenizer change the economics? {Q012003,Q010060}
- [M] How would you measure tokenizer fertility empirically across a multilingual corpus? {Q010061}
- [M] Why can two tokenizers with the same vocabulary size have very different fertility on Tamil? {Q010078}
- [H] How would fertility measured on a parallel corpus differ from fertility measured on independent monolingual corpora? {Q010079}
- [H] How would you evaluate whether a tokenizer serves your target languages well? {Q007487}
- [M] How would you measure whether a tokenizer is fair across languages, and detect that it unfairly penalises Chinese? {Q010030,Q010288}
- [H] When a model must serve both Chinese and English well, what changes in tokenization, data and evaluation? {Q010287}
- [M] If your product targets Southeast Asian languages, what tokenizer-related things would you check before choosing a model? {Q007489}
- [M] When does tokenizer inefficiency justify choosing a different model for specific language markets? {Q007720}
- [M] A multilingual support feature is 3x over budget and frequently truncates context, but only for Japanese and Arabic tickets; English is fine. What is the most likely cause? {Q006956}
- [M] Explain token counting and why it matters for cost, latency and context limits. {Q010868}
- [M] How would you estimate token counts for cost planning before you have production traffic? {Q011201,D00044}
- [M] Why does chars/4 break as a token estimate, and where does it break worst? {Q007784}
- [M] You migrate to a new provider at the same price per token and your bill rises 30%. What tokenizer-related causes would you investigate? {GEN}
- [M] Estimate the monthly token cost of a chatbot with a 2K-token system prompt, 1K tokens of retrieved context, 300-token outputs and 1M requests. {GEN}

## Positional encoding fundamentals
- [E] What is positional encoding, and why is it needed in transformers? {Q001010,Q001653,Q004322,Q004659,Q005335,Q007171}
- [E] Why does a transformer need positional information, and what happens without it? {D00049}
- [M] CNNs and RNNs do not use positional embeddings. Why do transformers need them? {Q003326}
- [M] Why is self-attention without positional information permutation-equivariant, and what does that imply for word-order-sensitive tasks? {GEN}
- [E] What are the main ways to inject position information into a transformer? {D04549}
- [M] Compare sinusoidal, learned absolute, relative and rotary position encodings, and how has the field evolved. {D04550,Q011790}
- [M] How do sinusoidal positional encodings work, and how do they compare to learned positional embeddings? {Q007498}
- [M] Why does the original transformer use sinusoids of different frequencies across dimensions, and what property does that give for relative offsets? {D00050,D04557}
- [M] What does the base of 10000 in sinusoidal encoding control, and what wavelengths does it cover? {GEN}
- [H] Show why a fixed offset is a linear transform of a sinusoidal positional encoding. {Q007500a}
- [H] Why does adding position to token embeddings entangle content and position, and why does that matter? {Q007500b}
- [M] BERT sums token, segment and position embeddings. Why does adding rather than concatenating not destroy semantic information? {D04526}
- [M] Why can adding position embeddings once at the input lose information compared with injecting position in every attention layer? {D04907}
- [M] Why is relative position more useful than absolute position for language? {Q007499}
- [M] What limits the maximum sequence length of a learned absolute position table, and what happens at positions never seen in training? {GEN}
- [M] How do T5-style relative position biases differ from RoPE and ALiBi? {GEN}
- [M] How does NoPE (no positional encoding) work in decoder-only models, and why can causal masking leak positional information? {D04909}

## RoPE and ALiBi
- [M] What is RoPE, and why are rotary embeddings preferred over learned absolute position embeddings? {Q004425,D03754}
- [M] Explain how RoPE rotates query and key vectors, and why its attention score depends only on relative offset. {Q007501,D04551}
- [M] Why is RoPE described as "relative" even though each token is rotated by its absolute index? {Q006969}
- [H] Prove that the RoPE attention score depends only on m-n for a single 2D pair. {Q007502a,D04552}
- [M] Why is RoPE applied to queries and keys but not values, and which tensors does it touch inside the attention layer? {Q007502b,D04548}
- [M] In single-token decoding with a growing KV cache, where is RoPE applied, and what is cached? {Q010043}
- [M] What is the long-range decay property of RoPE, and how does the base frequency affect it? {D04553}
- [M] What is the difference between interleaved and half-split RoPE pairing, and what breaks when a checkpoint is loaded with the wrong convention? {GEN}
- [M] What does partial rotary embedding (rotating only a fraction of each head dimension) do, and why would a model use it? {GEN}
- [M] How does ALiBi (Attention with Linear Biases) work, and why can it extrapolate to longer sequences zero-shot? {Q005968,Q007504,D04554,D00055}
- [M] How are ALiBi's per-head slopes chosen, and why do heads use different slopes? {GEN}
- [H] Why does ALiBi extrapolate where RoPE does not? {Q007505}
- [H] What is the cost of ALiBi's recency prior for retrieval-heavy tasks? {Q007506}
- [M] Compare RoPE and ALiBi in extrapolation behavior and typical use cases. {D00052}
- [H] Why have most recent open-weight LLMs converged on RoPE rather than ALiBi or learned embeddings? {GEN}

## Context length extension
- [M] Why do models fail at lengths beyond their training window, and what are the common length-extrapolation approaches? {D04555}
- [H] Why does RoPE degrade beyond the trained context length, and how do position interpolation and NTK-aware scaling address it? {D00053}
- [M] How do position interpolation and YaRN manipulate RoPE's frequencies to extend a pretrained model's context? {Q011791,Q007503,D03755}
- [H] Compare position interpolation, NTK-aware scaling and YaRN for extending RoPE context. What do they trade off? {D04556}
- [H] Why do high-frequency RoPE dimensions need little or no interpolation, while low-frequency ones need gentler scaling? {Q007507,Q009879}
- [M] What is the effect of the RoPE base (theta) on long-context behavior, and why do long-context models raise it? {D04908}
- [H] How does dynamic NTK scaling at inference differ from static scaling, and what is its downside for short prompts? {GEN}
- [H] What is YaRN's attention temperature scaling, and why is it needed when frequencies are interpolated? {GEN}
- [M] Why is some fine-tuning at the longer length still needed after interpolating positions, and roughly how much is typical? {GEN}
- [H] How would you extend a model trained at 8K context to 128K, and how would you verify quality did not regress at short lengths? {D00054}
- [H] You set a 4k-trained model's max position to 32k with no other change. Perplexity barely moves, but users say it forgets facts pasted near the top of long inputs. What is the best read? {Q006967}
- [M] Two candidates: A uses a learned absolute position table trained to 2k; B uses RoPE. A product needs occasional 16k inputs with a light fine-tuning budget. Which is the safer base and why? {Q006971}
- [M] Beyond perplexity, how would you evaluate whether a model really uses its extended context (needle-in-a-haystack, position-wise loss, multi-hop retrieval)? {GEN}
- [H] What is the "lost in the middle" effect, and is it a positional-encoding problem or a training-data problem? {GEN}
- [H] With sliding-window attention, what breaks if you use a rolling buffer but fail to keep RoPE positions consistent across the wrap-around? {Q009818}

## Multimodal inputs and tokenizer-free models
- [M] How are images converted into tokens for a vision transformer, and how does that affect the context budget? {D00046}
- [M] How do audio and video get tokenized for multimodal models, and what are the cost implications? {D00047}
- [M] How are positions encoded for image patches in a ViT, and how does this differ from text positions? {GEN}
- [H] In M-RoPE, why does giving text tokens identical t, h and w indices matter when grafting it onto an already-trained LLM? {Q008943}
- [H] How would you extend the M-RoPE position scheme to a 50-page document where page identity matters? {Q008944}
- [H] Why hasn't character- or byte-level modeling replaced BPE yet? {Q007440}
- [H] What is the case for tokenizer-free models, and why hasn't the tokenizer died yet? {Q007617}
- [H] How would pricing and context accounting work for a model with no fixed token unit? {Q007618}
- [H] Does dynamic patching in tokenizer-free models interact well or badly with prefix caching? {Q007619}
- [H] How does a byte-patch model such as the Byte Latent Transformer decide patch boundaries, and what compute is saved? {GEN}

## Additional questions
- [M] How does Byte Pair Encoding work, and what are its failure modes (numbers, code, non-Latin scripts)? {Q011789}
- [M] How does rotary position embedding encode relative position, and why is it popular in modern LLMs? {D00051}
