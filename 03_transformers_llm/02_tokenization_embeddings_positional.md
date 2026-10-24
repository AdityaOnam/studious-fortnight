---
domain: llm
topic: tokenization_embeddings_positional
title: Tokenization, embeddings and positional encoding
tags: [tokenization, bpe, rope, positional-encoding]
count: 154
---
# Tokenization, embeddings and positional encoding

## Tokens and tokenization basics
- [LLM02-001] What is tokenization in LLMs, and why is it necessary?
- [LLM02-002] What is a token, and how does it differ from a word?
- [LLM02-003] Why do LLMs use subword tokenization instead of whole words or raw characters?
- [LLM02-004] After tokenization, how are token IDs converted into embeddings, and what is the embedding table?
- [LLM02-005] What is the difference between a tokenizer's encode and decode steps, and is the round trip always lossless?
- [LLM02-006] How do LLMs handle out-of-vocabulary words?
- [LLM02-007] Walk through the pipeline from raw text to model input: normalization, pre-tokenization, subword tokenization, special tokens and embedding lookup.
- [LLM02-008] Why are Unicode normalization and pre-tokenization (whitespace, digit splitting) important in tokenizer design?
- [LLM02-009] Why does pre-tokenization matter in BPE, and what would go wrong without word-boundary constraints?
- [LLM02-010] Why do "the" and " the" (with a leading space) need to be separate tokens?
- [LLM02-011] What is a token, and why do Chinese, English and code consume different numbers of tokens?
- [LLM02-012] What are special tokens and chat templates, and what breaks when the wrong template is used at inference?
- [LLM02-013] What are BOS, EOS and padding tokens used for, and why can a missing EOS or wrong pad token break fine-tuning?
- [LLM02-014] Why is an embedding lookup used instead of multiplying a one-hot vector by a weight matrix?
- [LLM02-015] Are token embeddings contextual? How does the input embedding of a token differ from its hidden state at a deep layer?
- [LLM02-016] How would you check whether the learned token embeddings place semantically related tokens close together, and what are the limits of that analysis?

## BPE, WordPiece and Unigram
- [LLM02-017] What is Byte Pair Encoding, and how does it build its vocabulary?
- [LLM02-018] Walk through the BPE training algorithm step by step, and explain how a new string is encoded afterwards.
- [LLM02-019] When encoding with BPE, why must merges be applied in the order they were learned rather than by longest match?
- [LLM02-020] How does WordPiece differ from BPE in how it selects merges?
- [LLM02-021] How does unigram-LM tokenization differ conceptually from BPE?
- [LLM02-022] Compare BPE, WordPiece and unigram tokenization in how vocabularies are learned and how text is segmented.
- [LLM02-023] Given the same vocabulary size, why might unigram-LM produce more linguistically natural segmentations than BPE?
- [LLM02-024] What is subword regularization (e.g. BPE-dropout or unigram sampling), and why can it improve robustness?
- [LLM02-025] BPE segments greedily and deterministically. What suboptimality does this introduce compared with a segmentation that minimizes token count or maximizes likelihood?
- [LLM02-026] How does the composition of the tokenizer training corpus shape the vocabulary, and what goes wrong if it differs from the pretraining mix?
- [LLM02-027] Why do a tokenizer's merge rules or vocabulary file need to be versioned together with the model weights?

## Byte-level BPE and SentencePiece
- [LLM02-028] What is SentencePiece, and what does it add compared with running BPE over pre-tokenized words?
- [LLM02-029] Why does SentencePiece encode whitespace explicitly, and what property does that buy?
- [LLM02-030] How does SentencePiece handle languages without whitespace, such as Japanese or Chinese?
- [LLM02-031] What is byte-fallback in tokenization?
- [LLM02-032] How does byte-level BPE guarantee that there are no out-of-vocabulary strings?
- [LLM02-033] Why is byte-level BPE attractive for robustness, and what is its downside for non-Latin scripts?
- [LLM02-034] Compare BPE, WordPiece, SentencePiece and byte-level BPE.
- [LLM02-035] Byte-level tokens can split a multi-byte UTF-8 character across tokens. How does that affect streaming output, and how do serving stacks handle it?
- [LLM02-036] Why do GPT-2 style byte-level tokenizers map raw bytes to printable Unicode characters before applying merges?

## Vocabulary size and embedding tables
- [LLM02-037] What are the tradeoffs in choosing vocabulary size, in terms of embedding parameters, sequence length, softmax cost and multilingual quality?
- [LLM02-038] How would you size the embedding table for a 50k-vocabulary model with d_model=4096, and what does it cost?
- [LLM02-039] Compute the embedding and LM-head parameters for a 128K vocabulary with d_model=4096, tied versus untied, and compare to an 8B-parameter model.
- [LLM02-040] How does vocabulary size affect bytes per token, and through that the effective context window and inference cost per document?
- [LLM02-041] A large vocabulary causes computation issues and a small one causes OOV or long sequences. How would you find the best balance?
- [LLM02-042] With a 100K-token vocabulary, which parts of the transformer become expensive, and how would you reduce that cost?
- [LLM02-043] Why do many models pad their vocabulary size to a multiple of 64 or 128?
- [LLM02-044] What is weight tying, and why do some models tie the embedding and output matrices while others do not?
- [LLM02-045] How does the vocabulary size decision interact with the weight-tying decision?
- [LLM02-046] Why does weight-tying the embedding and LM head matter more for small models?
- [LLM02-047] What happens to a weight-tied model if you want to extend the vocabulary after training?
- [LLM02-048] When is extending the vocabulary of a pretrained model for a new domain or language worthwhile, and what are the risks?
- [LLM02-049] Describe the steps to extend a LLaMA tokenizer with new tokens and initialize their embeddings so continued pretraining converges.
- [LLM02-050] How would you initialize embeddings for newly added tokens (random, mean of existing, subword average), and what are the tradeoffs?
- [LLM02-051] What breaks if you simply bolt 20k new Indic tokens onto an existing English tokenizer's vocabulary?
- [LLM02-052] Why does adding a new language after pretraining rarely mean just retraining the tokenizer?
- [LLM02-053] Qwen uses byte-level BPE with a ~151K vocabulary, extra multilingual coverage and digits split into single characters. Why those choices, and what are the trade-offs?
- [LLM02-054] What problems do very large vocabularies (250K+) create for training undertrained rare tokens, softmax cost and memory, and how are they mitigated?
- [LLM02-055] Why is comparing perplexity across models with different tokenizers misleading, and what metric would you use instead?

## Tokenizer failure modes and debugging
- [LLM02-056] Why do LLMs struggle with simple character counting or reversing strings?
- [LLM02-057] Why do LLMs famously miscount the number of r's in "strawberry"?
- [LLM02-058] Why does asking the model to spell the word out first fix the letter-counting error?
- [LLM02-059] What other task categories fail for the same root cause as letter counting?
- [LLM02-060] How would a byte-level model differ on letter-counting tasks?
- [LLM02-061] Your model counts the letters in "ELEPHANT" correctly when it can write Python but fails when asked directly, and a teammate wants to fine-tune on letter-counting examples. What is the best read?
- [LLM02-062] Why does single-digit number tokenization improve arithmetic in LLMs?
- [LLM02-063] Why do digit and whitespace handling in the tokenizer affect arithmetic and code benchmarks?
- [LLM02-064] Why does the whitespace and formatting of code or JSON change token counts and model behavior?
- [LLM02-065] What are glitch tokens, and what causes them?
- [LLM02-066] A model emits bizarre, unsteerable text whenever a specific rare username-like string appears in the prompt, even across temperatures and rephrasings. What is the best explanation?
- [LLM02-067] Your tokenizer splits important domain terms into meaningless subword pieces. How do you fix it?
- [LLM02-068] What happens when you swap the tokenizer between a model and its fine-tuned variant or serving stack?
- [LLM02-069] How would you detect a train/inference tokenization mismatch after the fact?
- [LLM02-070] Why is a production tokenizer library often written in Rust, and what tokenizer bugs bite people in practice?
- [LLM02-071] How would tokenization affect a code-diff-generation feature?
- [LLM02-072] You build a code assistant on a model whose tokenizer was trained on web prose, and long files blow the context window sooner than expected. What is the strongest lever?
- [LLM02-073] A prompt ends with a trailing space and completions become strange. Why does this happen at the token level?
- [LLM02-074] What is token healing, and when is it needed for prefix-completion prompts?
- [LLM02-075] Why can the same text tokenize differently depending on leading whitespace or casing, and how does that make prompts brittle?
- [LLM02-076] Why do token boundaries make grammar-constrained or JSON-schema-constrained decoding tricky?

## Multilingual tokenization and cost
- [LLM02-077] What is tokenizer fertility (tokens per word), and why does it matter?
- [LLM02-078] What is the effect of tokenizer choice on multilingual pricing and quality?
- [LLM02-079] How does tokenization affect cost and latency for non-English languages, and what can be done about it?
- [LLM02-080] What happens to multilingual and low-resource languages when a tokenizer is trained mostly on English text?
- [LLM02-081] Why is tokenization the first bottleneck for Indian-language LLMs, and how does a low-fertility tokenizer change the economics?
- [LLM02-082] How would you measure tokenizer fertility empirically across a multilingual corpus?
- [LLM02-083] Why can two tokenizers with the same vocabulary size have very different fertility on Tamil?
- [LLM02-084] How would fertility measured on a parallel corpus differ from fertility measured on independent monolingual corpora?
- [LLM02-085] How would you evaluate whether a tokenizer serves your target languages well?
- [LLM02-086] How would you measure whether a tokenizer is fair across languages, and detect that it unfairly penalises Chinese?
- [LLM02-087] When a model must serve both Chinese and English well, what changes in tokenization, data and evaluation?
- [LLM02-088] If your product targets Southeast Asian languages, what tokenizer-related things would you check before choosing a model?
- [LLM02-089] When does tokenizer inefficiency justify choosing a different model for specific language markets?
- [LLM02-090] A multilingual support feature is 3x over budget and frequently truncates context, but only for Japanese and Arabic tickets; English is fine. What is the most likely cause?
- [LLM02-091] Explain token counting and why it matters for cost, latency and context limits.
- [LLM02-092] How would you estimate token counts for cost planning before you have production traffic?
- [LLM02-093] Why does chars/4 break as a token estimate, and where does it break worst?
- [LLM02-094] You migrate to a new provider at the same price per token and your bill rises 30%. What tokenizer-related causes would you investigate?
- [LLM02-095] Estimate the monthly token cost of a chatbot with a 2K-token system prompt, 1K tokens of retrieved context, 300-token outputs and 1M requests.

## Positional encoding fundamentals
- [LLM02-096] What is positional encoding, and why is it needed in transformers?
- [LLM02-097] Why does a transformer need positional information, and what happens without it?
- [LLM02-098] CNNs and RNNs do not use positional embeddings. Why do transformers need them?
- [LLM02-099] Why is self-attention without positional information permutation-equivariant, and what does that imply for word-order-sensitive tasks?
- [LLM02-100] What are the main ways to inject position information into a transformer?
- [LLM02-101] Compare sinusoidal, learned absolute, relative and rotary position encodings, and how has the field evolved.
- [LLM02-102] How do sinusoidal positional encodings work, and how do they compare to learned positional embeddings?
- [LLM02-103] Why does the original transformer use sinusoids of different frequencies across dimensions, and what property does that give for relative offsets?
- [LLM02-104] What does the base of 10000 in sinusoidal encoding control, and what wavelengths does it cover?
- [LLM02-105] Show why a fixed offset is a linear transform of a sinusoidal positional encoding.
- [LLM02-106] Why does adding position to token embeddings entangle content and position, and why does that matter?
- [LLM02-107] BERT sums token, segment and position embeddings. Why does adding rather than concatenating not destroy semantic information?
- [LLM02-108] Why can adding position embeddings once at the input lose information compared with injecting position in every attention layer?
- [LLM02-109] Why is relative position more useful than absolute position for language?
- [LLM02-110] What limits the maximum sequence length of a learned absolute position table, and what happens at positions never seen in training?
- [LLM02-111] How do T5-style relative position biases differ from RoPE and ALiBi?
- [LLM02-112] How does NoPE (no positional encoding) work in decoder-only models, and why can causal masking leak positional information?

## RoPE and ALiBi
- [LLM02-113] What is RoPE, and why are rotary embeddings preferred over learned absolute position embeddings?
- [LLM02-114] Explain how RoPE rotates query and key vectors, and why its attention score depends only on relative offset.
- [LLM02-115] Why is RoPE described as "relative" even though each token is rotated by its absolute index?
- [LLM02-116] Prove that the RoPE attention score depends only on m-n for a single 2D pair.
- [LLM02-117] Why is RoPE applied to queries and keys but not values, and which tensors does it touch inside the attention layer?
- [LLM02-118] In single-token decoding with a growing KV cache, where is RoPE applied, and what is cached?
- [LLM02-119] What is the long-range decay property of RoPE, and how does the base frequency affect it?
- [LLM02-120] What is the difference between interleaved and half-split RoPE pairing, and what breaks when a checkpoint is loaded with the wrong convention?
- [LLM02-121] What does partial rotary embedding (rotating only a fraction of each head dimension) do, and why would a model use it?
- [LLM02-122] How does ALiBi (Attention with Linear Biases) work, and why can it extrapolate to longer sequences zero-shot?
- [LLM02-123] How are ALiBi's per-head slopes chosen, and why do heads use different slopes?
- [LLM02-124] Why does ALiBi extrapolate where RoPE does not?
- [LLM02-125] What is the cost of ALiBi's recency prior for retrieval-heavy tasks?
- [LLM02-126] Compare RoPE and ALiBi in extrapolation behavior and typical use cases.
- [LLM02-127] Why have most recent open-weight LLMs converged on RoPE rather than ALiBi or learned embeddings?

## Context length extension
- [LLM02-128] Why do models fail at lengths beyond their training window, and what are the common length-extrapolation approaches?
- [LLM02-129] Why does RoPE degrade beyond the trained context length, and how do position interpolation and NTK-aware scaling address it?
- [LLM02-130] How do position interpolation and YaRN manipulate RoPE's frequencies to extend a pretrained model's context?
- [LLM02-131] Compare position interpolation, NTK-aware scaling and YaRN for extending RoPE context. What do they trade off?
- [LLM02-132] Why do high-frequency RoPE dimensions need little or no interpolation, while low-frequency ones need gentler scaling?
- [LLM02-133] What is the effect of the RoPE base (theta) on long-context behavior, and why do long-context models raise it?
- [LLM02-134] How does dynamic NTK scaling at inference differ from static scaling, and what is its downside for short prompts?
- [LLM02-135] What is YaRN's attention temperature scaling, and why is it needed when frequencies are interpolated?
- [LLM02-136] Why is some fine-tuning at the longer length still needed after interpolating positions, and roughly how much is typical?
- [LLM02-137] How would you extend a model trained at 8K context to 128K, and how would you verify quality did not regress at short lengths?
- [LLM02-138] You set a 4k-trained model's max position to 32k with no other change. Perplexity barely moves, but users say it forgets facts pasted near the top of long inputs. What is the best read?
- [LLM02-139] Two candidates: A uses a learned absolute position table trained to 2k; B uses RoPE. A product needs occasional 16k inputs with a light fine-tuning budget. Which is the safer base and why?
- [LLM02-140] Beyond perplexity, how would you evaluate whether a model really uses its extended context (needle-in-a-haystack, position-wise loss, multi-hop retrieval)?
- [LLM02-141] What is the "lost in the middle" effect, and is it a positional-encoding problem or a training-data problem?
- [LLM02-142] With sliding-window attention, what breaks if you use a rolling buffer but fail to keep RoPE positions consistent across the wrap-around?

## Multimodal inputs and tokenizer-free models
- [LLM02-143] How are images converted into tokens for a vision transformer, and how does that affect the context budget?
- [LLM02-144] How do audio and video get tokenized for multimodal models, and what are the cost implications?
- [LLM02-145] How are positions encoded for image patches in a ViT, and how does this differ from text positions?
- [LLM02-146] In M-RoPE, why does giving text tokens identical t, h and w indices matter when grafting it onto an already-trained LLM?
- [LLM02-147] How would you extend the M-RoPE position scheme to a 50-page document where page identity matters?
- [LLM02-148] Why hasn't character- or byte-level modeling replaced BPE yet?
- [LLM02-149] What is the case for tokenizer-free models, and why hasn't the tokenizer died yet?
- [LLM02-150] How would pricing and context accounting work for a model with no fixed token unit?
- [LLM02-151] Does dynamic patching in tokenizer-free models interact well or badly with prefix caching?
- [LLM02-152] How does a byte-patch model such as the Byte Latent Transformer decide patch boundaries, and what compute is saved?

## Additional questions
- [LLM02-153] How does Byte Pair Encoding work, and what are its failure modes (numbers, code, non-Latin scripts)?
- [LLM02-154] How does rotary position embedding encode relative position, and why is it popular in modern LLMs?
