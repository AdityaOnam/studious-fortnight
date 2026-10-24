---
domain: llm
topic: attention_transformer_architecture
title: Attention and Transformer architecture
tags: [transformer, attention, bert, gpt]
count: 156
---
# Attention and Transformer architecture

## Transformer fundamentals and motivation
- [LLM01-001] Give a high-level explanation of how the Transformer architecture works and what it is typically used for.
- [LLM01-002] What are the key components of a Transformer, and what role does each play (including Add and Norm)?
- [LLM01-003] Why did Transformers replace RNNs and LSTMs for language modelling?
- [LLM01-004] How does the Transformer achieve parallelism in training, and where is computation still sequential?
- [LLM01-005] How does attention help a Transformer capture long-range dependencies compared with an RNN or CNN?
- [LLM01-006] How do Transformers mitigate the vanishing gradient problem that affects deep recurrent networks?
- [LLM01-007] What inference-time cost do Transformers pay that RNNs do not?
- [LLM01-008] Why is the Transformer's lack of recurrence both a strength and a weakness for modelling very long sequences?
- [LLM01-009] If the KV cache makes autoregressive decoding recurrent anyway, where does the Transformer's advantage over RNNs actually show up?
- [LLM01-010] What are the fundamental limitations of the Transformer, and how can they be addressed?
- [LLM01-011] Walk through a single Transformer block and explain how data flows through it.
- [LLM01-012] Walk through one forward pass of a decoder-only Transformer from token IDs to next-token probabilities, naming tensor shapes.
- [LLM01-013] What does each Transformer block or layer learn as you go deeper?
- [LLM01-014] What changed architecturally between GPT-2 and Llama-style models?
- [LLM01-015] Where does the non-linearity in a Transformer block come from?
- [LLM01-016] How do you implement multi-head self-attention efficiently with batched matrix multiplies and reshapes?
- [LLM01-017] The original Transformer multiplies token embeddings by sqrt(d_model). Why?
- [LLM01-018] How is attention fundamentally different from a fully connected layer or a convolution?

## Self-attention and scaled dot-product
- [LLM01-019] What is the attention mechanism in deep learning, and why is it significant?
- [LLM01-020] Explain self-attention step by step, including the shapes of Q, K, V and the output.
- [LLM01-021] Why is it called "self-attention", and what role does it play in a Transformer?
- [LLM01-022] What are queries, keys and values, and why use separate learned projections for each rather than comparing raw embeddings?
- [LLM01-023] Why do we divide the query-key dot product by sqrt(d_k) in scaled dot-product attention?
- [LLM01-024] What happens to the softmax distribution and its gradients if you remove the 1/sqrt(d_k) scaling?
- [LLM01-025] Give the variance argument for why dot products grow with dimension, and how that leads to softmax saturation.
- [LLM01-026] What happens to gradients when softmax saturates? Walk through the softmax Jacobian.
- [LLM01-027] Would you expect attention scaling problems to be worse with larger or smaller head dimensions?
- [LLM01-028] Why does attention use softmax, and where else is softmax applied in the Transformer?
- [LLM01-029] A teammate removes the 1/sqrt(d_k) scaling from a custom attention layer and training loss plateaus with tiny gradients. What is the diagnosis?
- [LLM01-030] Your from-scratch Transformer runs but never learns; attention weights look nearly uniform and loss is flat. What bugs would you suspect?
- [LLM01-031] If you shuffle the tokens in a prompt and there is no positional encoding, attention outputs are just permuted. What property is this?
- [LLM01-032] Why is permutation equivariance a problem for attention but not for convolution?
- [LLM01-033] How would you verify and encourage an attention layer to focus on the right parts of the input?
- [LLM01-034] Are attention weights a faithful explanation of a model's predictions?
- [LLM01-035] How do you compute softmax in attention in a numerically stable way, especially in fp16 or bf16?

## Multi-head attention and masking
- [LLM01-036] Why use multiple attention heads instead of one large head of the same total dimension?
- [LLM01-037] Does multi-head attention cost more FLOPs than single-head attention at the same d_model?
- [LLM01-038] How are the outputs of multiple heads combined and projected back to d_model, and what does the output projection do?
- [LLM01-039] Explain the dimensions of each weight matrix and activation in a multi-head attention block.
- [LLM01-040] How is the hidden dimension split across heads, and what happens to representational capacity if head dimension is too small?
- [LLM01-041] Where does dropout conventionally go in a multi-head attention implementation, and why?
- [LLM01-042] What is an induction head and why does it matter for in-context learning?
- [LLM01-043] If many attention heads are redundant, what architectural optimisations does that motivate?
- [LLM01-044] What is causal masking, and how does masked self-attention differ from regular self-attention?
- [LLM01-045] How is the causal mask implemented numerically, and why must it be applied before the softmax rather than after?
- [LLM01-046] What lets a decoder be trained on all positions in parallel while generating left to right at inference?
- [LLM01-047] What is the difference between a padding mask and a causal mask, and when do you need each?
- [LLM01-048] What is a prefix LM, and when is bidirectional attention over the prompt useful?

## Encoder, decoder and architecture families
- [LLM01-049] What is the purpose of the encoder in a Transformer?
- [LLM01-050] What is the purpose of the decoder in a Transformer?
- [LLM01-051] What is the functional difference between the encoder and the decoder?
- [LLM01-052] How does the encoder-decoder structure work at a high level?
- [LLM01-053] What is fed into the decoder during training versus inference, and what is teacher forcing?
- [LLM01-054] What is cross-attention, how does it differ from self-attention, and where do Q, K and V come from?
- [LLM01-055] What is the compute cost of cross-attention in terms of source and target lengths?
- [LLM01-056] Why do cross-attention layers typically read from the encoder's final layer output, and what are the alternatives?
- [LLM01-057] Compare encoder-only, decoder-only and encoder-decoder architectures. What is each used for?
- [LLM01-058] Contrast BERT, GPT and T5 in architecture, pretraining objective and typical downstream use.
- [LLM01-059] Why did decoder-only models win for general-purpose LLMs, and where do encoder-decoder models still make sense?
- [LLM01-060] Why do embedding models still use bidirectional attention?
- [LLM01-061] Explain the low-rank argument for why bidirectional attention may limit the expressiveness of an encoder-style model compared with causal attention.
- [LLM01-062] Compare autoregressive and autoencoding pretraining. How does XLNet's permutation language model try to combine them?

## BERT and encoder-only models
- [LLM01-063] What is BERT and how does it improve language understanding?
- [LLM01-064] What are BERT's two pretraining tasks, and what does each teach the model?
- [LLM01-065] BERT replaces 15% of tokens for masked language modelling. Why the 80/10/10 mask/random/keep split?
- [LLM01-066] What is the purpose of the [CLS] token, and how is its output used for classification?
- [LLM01-067] How does BERT distinguish different senses of a polysemous word?
- [LLM01-068] Why is ELMo called shallowly bidirectional while BERT is deeply bidirectional?
- [LLM01-069] What are the differences between BERT and the original Transformer encoder?
- [LLM01-070] How do you process documents longer than BERT's 512-token limit in fine-tuning and inference?
- [LLM01-071] What are BERT's strengths and limitations, such as the pretrain-finetune mismatch and independence between masked tokens?
- [LLM01-072] What did RoBERTa change relative to BERT (dynamic masking, no NSP, more data), and why does it matter?
- [LLM01-073] How does ALBERT reduce parameters, and why replace NSP with sentence-order prediction?
- [LLM01-074] What does SpanBERT change in masking and the training objective, and which tasks benefit?

## Residual connections and normalization
- [LLM01-075] What is the purpose of residual connections in a Transformer, and what happens to training without them?
- [LLM01-076] Why do residual connections matter more as depth grows? Give the gradient-flow argument.
- [LLM01-077] In a pre-norm Transformer block, which tensor is carried forward on the residual stream between sublayers?
- [LLM01-078] Why is layer normalization used in Transformers and where is it applied?
- [LLM01-079] Why do LLMs use LayerNorm or RMSNorm rather than BatchNorm, given BatchNorm's success in CNNs? Compare batch, layer, instance and group norm.
- [LLM01-080] Why does batch norm underperform layer norm even in encoder-only Transformers where autoregressive decoding is not an issue?
- [LLM01-081] Compare Pre-LN and Post-LN in gradient flow, warmup requirements and final performance. Why do modern LLMs use pre-norm (as Llama does on each sublayer input)?
- [LLM01-082] Post-norm sometimes reaches a lower final loss, so why does almost everyone ship pre-norm?
- [LLM01-083] Why does Post-LN need learning-rate warmup while Pre-LN tolerates little or none? Explain via gradient scale near the output layer.
- [LLM01-084] You scale a post-norm decoder from 12 to 48 layers without warmup and loss spikes and diverges early. What is the fastest principled fix?
- [LLM01-085] What is DeepNorm, and why might very deep Transformers need modified residual scaling?
- [LLM01-086] What is RMSNorm, what does it remove compared with LayerNorm, and why is that acceptable?
- [LLM01-087] Beyond pre-norm and post-norm placement, where else do norms appear in modern Transformers (QK-norm, final norm)? What does QK-norm fix?
- [LLM01-088] Write the LayerNorm formula. What do the learned gain and bias do, and why do some LLMs drop bias terms?

## Feed-forward networks, embeddings and parameter budgets
- [LLM01-089] What does the position-wise feed-forward network do in a Transformer block, and why is it needed beyond attention?
- [LLM01-090] Roughly what fraction of a Transformer block's parameters sit in the MLP versus attention?
- [LLM01-091] Why is the FFN intermediate size typically 4x d_model, and why do SwiGLU/GeGLU blocks use three matrices and about 8/3x?
- [LLM01-092] How does a gated FFN such as GLU or SwiGLU differ from a standard FFN with ReLU or GELU, and why is SwiGLU the default now?
- [LLM01-093] Write the computation formula of an FFN block using a GLU with a GELU or Swish gate.
- [LLM01-094] What empirical evidence supports gated FFN variants over ReLU FFNs in LLMs?
- [LLM01-095] How do the compute shares of attention and the FFN change as sequence length grows, and where does attention overtake the FFN?
- [LLM01-096] What are the benefits and risks of tying input embeddings to the output projection?
- [LLM01-097] Why does the token embedding layer often need special treatment in training and fine-tuning?
- [LLM01-098] Count the parameters of a decoder-only Transformer given vocabulary size, hidden size, layers and FFN expansion.
- [LLM01-099] Using the approximation of 12 d_model^2 parameters per layer, estimate the size of a model with d_model=12288 and 96 layers.
- [LLM01-100] How would you estimate FLOPs and activation memory for one Transformer layer given batch size, sequence length and hidden size?
- [LLM01-101] What is a parallel attention-and-FFN block (as in GPT-J or PaLM), and what does it trade off against the sequential design?

## Attention cost and efficient variants
- [LLM01-102] What is the time and memory complexity of self-attention in sequence length, and which operation causes the quadratic term?
- [LLM01-103] What alternatives to full attention exist for long sequences, and what does each give up?
- [LLM01-104] Attention is O(n^2). Where does that actually bite in practice: prefill or decode?
- [LLM01-105] Moving from 2k to 16k context, single-GPU prefill latency and memory grow far more than 8x. What explains this?
- [LLM01-106] What does the (B, n_head, T, T) attention tensor imply at scale?
- [LLM01-107] What are the disadvantages of self-attention, and how can they be overcome?
- [LLM01-108] What makes Transformers heavy in computation and memory, and how can we address it?
- [LLM01-109] If you double sequence length, how do attention FLOPs and activation memory change in standard attention versus FlashAttention?
- [LLM01-110] Why does decoding with a KV cache cost O(n) per step in attention while recomputation costs O(n^2)?
- [LLM01-111] What is the difference between local and global attention?
- [LLM01-112] How does sliding-window attention reduce cost, and how can information still propagate beyond the window across layers?
- [LLM01-113] What does sliding-window attention give up? A single-layer windowed model answers about recent text but fails on facts far earlier; why?
- [LLM01-114] Does sliding-window attention make quality strictly worse than full attention, and how would you measure it?
- [LLM01-115] Explain hybrid local/global attention stacks. What do you gain and what do you give up?
- [LLM01-116] How would you choose the local-to-global attention ratio for a code model versus a chat model?
- [LLM01-117] Compare sparse and linear attention approximations. Why have they not replaced softmax attention?
- [LLM01-118] What is linear attention and how does it fundamentally differ from standard softmax attention?
- [LLM01-119] With top-k sparse attention, how would you choose the top-k budget, and what symptom shows it is too small?
- [LLM01-120] In a hybrid sparse/dense attention stack, where would you place the sparse layers and how would you test that choice?
- [LLM01-121] What is an attention sink, and why do streaming-inference methods keep the first few tokens in the cache?
- [LLM01-122] What is attention sink, and why does gated attention mitigate it?
- [LLM01-123] How do attention sinks connect to the lost-in-the-middle problem?
- [LLM01-124] Would you expect attention sinks in an encoder-only model?
- [LLM01-125] What is a state-space model such as Mamba, and why are hybrid SSM-Transformer models appealing?

## FlashAttention
- [LLM01-126] Why is standard attention memory-bound rather than compute-bound on modern GPUs?
- [LLM01-127] What does IO-awareness mean for GPU kernels, and how do the HBM and SRAM hierarchy shape an attention implementation?
- [LLM01-128] What is FlashAttention, and why is it faster than standard attention even though FLOPs are unchanged?
- [LLM01-129] How does FlashAttention reduce memory usage, and in what sense is its memory linear in sequence length?
- [LLM01-130] Why doesn't FlashAttention change the asymptotic FLOP complexity of attention?
- [LLM01-131] Explain tiling and the online softmax rescaling in FlashAttention. Why is tiling possible at all?
- [LLM01-132] Why does the FlashAttention backward pass recompute attention instead of caching it, and why is recomputation faster?
- [LLM01-133] What does FlashAttention-2 change in work partitioning compared with the first version, and why does it help?
- [LLM01-134] Why do newer FlashAttention versions depend on specific GPU generations, and how does FP8 attention affect accuracy?
- [LLM01-135] How does FlashAttention exploit causal masking for speed?
- [LLM01-136] How do FlashAttention varlen kernels avoid materializing the block-diagonal mask for packed sequences?
- [LLM01-137] What does FlashAttention do, and how is it different from PagedAttention?
- [LLM01-138] Is FlashAttention compatible with ALiBi-style attention biases?
- [LLM01-139] At 8k+ context, attention latency dominates on an A100 and you run a hand-written three-loop attention kernel. What is the highest-impact change and why is it safe?
- [LLM01-140] Does FlashAttention produce exactly the same outputs as standard attention, or only approximately?
- [LLM01-141] Does FlashAttention help single-token decoding with a long KV cache? What do split-KV approaches such as Flash-Decoding add?

## MQA, GQA and MLA
- [LLM01-142] What are Multi-Query Attention and Grouped-Query Attention, and how do they differ from multi-head attention?
- [LLM01-143] Compare MHA, MQA and GQA in quality, KV-cache size, memory bandwidth and decode speed.
- [LLM01-144] Why have most large models moved from MHA to GQA, and why does it matter for serving?
- [LLM01-145] How do you modify multi-head attention code to implement GQA? What changes, and what does it buy at inference?
- [LLM01-146] How would you convert an existing MHA checkpoint into a GQA model with minimal retraining (uptraining, mean-pooling KV heads)?
- [LLM01-147] Given n_heads=32 and n_kv_heads=8, compute the KV cache per token per layer and explain how query heads share K/V.
- [LLM01-148] How does GQA change the parameter budget and the memory-bandwidth budget differently?
- [LLM01-149] Why do open-weight models almost always ship GQA while a frontier lab might train MHA at the same size?
- [LLM01-150] How would you choose the number of KV groups in GQA, and how does it interact with tensor-parallel degree?
- [LLM01-151] Compare MHA, MQA, GQA and multi-head latent attention in memory and throughput.
- [LLM01-152] What problem does multi-head latent attention (MLA) solve, and how does it differ from GQA?
- [LLM01-153] In MLA, why does RoPE complicate the low-rank factorisation, and how is it usually resolved?
- [LLM01-154] How does MLA interact with tensor parallelism across the head dimension?
- [LLM01-155] In what regime would plain GQA still be the pragmatic choice over MLA?
- [LLM01-156] Mistral 7B combines GQA and sliding-window attention. What does each buy you and what does each cost?
