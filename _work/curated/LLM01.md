## Transformer fundamentals and motivation
- [E] Give a high-level explanation of how the Transformer architecture works and what it is typically used for. {Q001005,Q001268,Q001650,Q004653,Q007172,Q012559}
- [E] What are the key components of a Transformer, and what role does each play (including Add and Norm)? {Q004654,Q011901,Q012560,D04500}
- [E] Why did Transformers replace RNNs and LSTMs for language modelling? {Q007405,Q009190a,Q005293,Q007173,Q005297,Q005331,Q005291,Q003357,D04505}
- [M] How does the Transformer achieve parallelism in training, and where is computation still sequential? {Q001657,D04504}
- [M] How does attention help a Transformer capture long-range dependencies compared with an RNN or CNN? {Q005332,Q012561,D04506}
- [M] How do Transformers mitigate the vanishing gradient problem that affects deep recurrent networks? {Q003328,Q003358,Q003357}
- [M] What inference-time cost do Transformers pay that RNNs do not? {Q007406}
- [M] Why is the Transformer's lack of recurrence both a strength and a weakness for modelling very long sequences? {D04600}
- [H] If the KV cache makes autoregressive decoding recurrent anyway, where does the Transformer's advantage over RNNs actually show up? {Q007267}
- [M] What are the fundamental limitations of the Transformer, and how can they be addressed? {Q003356,Q005298,Q012562}
- [M] Walk through a single Transformer block and explain how data flows through it. {Q004422a,Q007409,D03749}
- [M] Walk through one forward pass of a decoder-only Transformer from token IDs to next-token probabilities, naming tensor shapes. {Q004655,Q011799,Q011211,D00025}
- [M] What does each Transformer block or layer learn as you go deeper? {Q005325}
- [M] What changed architecturally between GPT-2 and Llama-style models? {D00026}
- [E] Where does the non-linearity in a Transformer block come from? {D04513}
- [M] How do you implement multi-head self-attention efficiently with batched matrix multiplies and reshapes? {GEN}
- [M] The original Transformer multiplies token embeddings by sqrt(d_model). Why? {GEN}
- [M] How is attention fundamentally different from a fully connected layer or a convolution? {GEN}

## Self-attention and scaled dot-product
- [E] What is the attention mechanism in deep learning, and why is it significant? {Q005292,Q012022a,Q001652,Q001011,Q004318}
- [E] Explain self-attention step by step, including the shapes of Q, K, V and the output. {Q004661,Q007169,Q007413,D04493}
- [E] Why is it called "self-attention", and what role does it play in a Transformer? {Q003342}
- [E] What are queries, keys and values, and why use separate learned projections for each rather than comparing raw embeddings? {Q004660,D00005,D04496}
- [E] Why do we divide the query-key dot product by sqrt(d_k) in scaled dot-product attention? {Q004663,Q007319,Q011204,Q011784,Q012515,D00003,Q009931,Q003346}
- [M] What happens to the softmax distribution and its gradients if you remove the 1/sqrt(d_k) scaling? {D00004,D04602,D04494}
- [H] Give the variance argument for why dot products grow with dimension, and how that leads to softmax saturation. {Q006809,D04495}
- [H] What happens to gradients when softmax saturates? Walk through the softmax Jacobian. {Q007419}
- [H] Would you expect attention scaling problems to be worse with larger or smaller head dimensions? {Q007420}
- [M] Why does attention use softmax, and where else is softmax applied in the Transformer? {Q005341,Q003352}
- [M] A teammate removes the 1/sqrt(d_k) scaling from a custom attention layer and training loss plateaus with tiny gradients. What is the diagnosis? {Q006962}
- [M] Your from-scratch Transformer runs but never learns; attention weights look nearly uniform and loss is flat. What bugs would you suspect? {Q006964}
- [M] If you shuffle the tokens in a prompt and there is no positional encoding, attention outputs are just permuted. What property is this? {Q006972}
- [M] Why is permutation equivariance a problem for attention but not for convolution? {Q007383}
- [H] How would you verify and encourage an attention layer to focus on the right parts of the input? {Q007220}
- [M] Are attention weights a faithful explanation of a model's predictions? {GEN}
- [M] How do you compute softmax in attention in a numerically stable way, especially in fp16 or bf16? {GEN}

## Multi-head attention and masking
- [M] Why use multiple attention heads instead of one large head of the same total dimension? {Q003347,Q004665,Q007425,D00006,D04497,Q006963}
- [M] Does multi-head attention cost more FLOPs than single-head attention at the same d_model? {Q007428,D04498}
- [M] How are the outputs of multiple heads combined and projected back to d_model, and what does the output projection do? {Q003348}
- [H] Explain the dimensions of each weight matrix and activation in a multi-head attention block. {Q007219}
- [M] How is the hidden dimension split across heads, and what happens to representational capacity if head dimension is too small? {D04904}
- [M] Where does dropout conventionally go in a multi-head attention implementation, and why? {Q009616}
- [H] What is an induction head and why does it matter for in-context learning? {Q007426}
- [H] If many attention heads are redundant, what architectural optimisations does that motivate? {Q007427}
- [E] What is causal masking, and how does masked self-attention differ from regular self-attention? {Q004664,Q003349}
- [M] How is the causal mask implemented numerically, and why must it be applied before the softmax rather than after? {Q007421,Q007422,D00007,D04502}
- [M] What lets a decoder be trained on all positions in parallel while generating left to right at inference? {Q006966,Q007407}
- [M] What is the difference between a padding mask and a causal mask, and when do you need each? {GEN}
- [M] What is a prefix LM, and when is bidirectional attention over the prompt useful? {Q007423}

## Encoder, decoder and architecture families
- [E] What is the purpose of the encoder in a Transformer? {Q003343}
- [E] What is the purpose of the decoder in a Transformer? {Q003344}
- [E] What is the functional difference between the encoder and the decoder? {Q003484}
- [M] How does the encoder-decoder structure work at a high level? {Q003345}
- [M] What is fed into the decoder during training versus inference, and what is teacher forcing? {D04501}
- [M] What is cross-attention, how does it differ from self-attention, and where do Q, K and V come from? {Q003351,Q004662,Q005972,D00028,D04503}
- [M] What is the compute cost of cross-attention in terms of source and target lengths? {GEN}
- [M] Why do cross-attention layers typically read from the encoder's final layer output, and what are the alternatives? {GEN}
- [M] Compare encoder-only, decoder-only and encoder-decoder architectures. What is each used for? {Q004321,Q007429}
- [M] Contrast BERT, GPT and T5 in architecture, pretraining objective and typical downstream use. {D00029,D04601}
- [M] Why did decoder-only models win for general-purpose LLMs, and where do encoder-decoder models still make sense? {D00030}
- [M] Why do embedding models still use bidirectional attention? {Q007430}
- [H] Explain the low-rank argument for why bidirectional attention may limit the expressiveness of an encoder-style model compared with causal attention. {D04447}
- [M] Compare autoregressive and autoencoding pretraining. How does XLNet's permutation language model try to combine them? {D04535}

## BERT and encoder-only models
- [E] What is BERT and how does it improve language understanding? {Q005299,Q012564}
- [E] What are BERT's two pretraining tasks, and what does each teach the model? {D04522}
- [M] BERT replaces 15% of tokens for masked language modelling. Why the 80/10/10 mask/random/keep split? {GEN}
- [M] What is the purpose of the [CLS] token, and how is its output used for classification? {D04525}
- [M] How does BERT distinguish different senses of a polysemous word? {D04527}
- [M] Why is ELMo called shallowly bidirectional while BERT is deeply bidirectional? {D04528}
- [M] What are the differences between BERT and the original Transformer encoder? {D04529}
- [M] How do you process documents longer than BERT's 512-token limit in fine-tuning and inference? {D04530}
- [M] What are BERT's strengths and limitations, such as the pretrain-finetune mismatch and independence between masked tokens? {D04531}
- [M] What did RoBERTa change relative to BERT (dynamic masking, no NSP, more data), and why does it matter? {D04532}
- [M] How does ALBERT reduce parameters, and why replace NSP with sentence-order prediction? {D04533}
- [M] What does SpanBERT change in masking and the training objective, and which tasks benefit? {D04534}

## Residual connections and normalization
- [E] What is the purpose of residual connections in a Transformer, and what happens to training without them? {Q003353,Q004677,D04507}
- [M] Why do residual connections matter more as depth grows? Give the gradient-flow argument. {Q007411,D00024}
- [E] In a pre-norm Transformer block, which tensor is carried forward on the residual stream between sublayers? {Q006978}
- [E] Why is layer normalization used in Transformers and where is it applied? {Q003354}
- [M] Why do LLMs use LayerNorm or RMSNorm rather than BatchNorm, given BatchNorm's success in CNNs? Compare batch, layer, instance and group norm. {Q006974,Q009932,D04508}
- [H] Why does batch norm underperform layer norm even in encoder-only Transformers where autoregressive decoding is not an issue? {Q007313}
- [M] Compare Pre-LN and Post-LN in gradient flow, warmup requirements and final performance. Why do modern LLMs use pre-norm (as Llama does on each sublayer input)? {D04509,D00020,Q004693,Q011195,Q011797,Q007472,Q005962,D03753,D04540}
- [M] Post-norm sometimes reaches a lower final loss, so why does almost everyone ship pre-norm? {Q006977}
- [H] Why does Post-LN need learning-rate warmup while Pre-LN tolerates little or none? Explain via gradient scale near the output layer. {D04511,Q007473,Q007307}
- [H] You scale a post-norm decoder from 12 to 48 layers without warmup and loss spikes and diverges early. What is the fastest principled fix? {Q006973}
- [M] What is DeepNorm, and why might very deep Transformers need modified residual scaling? {D04512}
- [M] What is RMSNorm, what does it remove compared with LayerNorm, and why is that acceptable? {Q004692,Q005970,D04510,D00021,Q007314}
- [M] Beyond pre-norm and post-norm placement, where else do norms appear in modern Transformers (QK-norm, final norm)? What does QK-norm fix? {Q007418,Q007475}
- [M] Write the LayerNorm formula. What do the learned gain and bias do, and why do some LLMs drop bias terms? {GEN}

## Feed-forward networks, embeddings and parameter budgets
- [E] What does the position-wise feed-forward network do in a Transformer block, and why is it needed beyond attention? {Q004666,Q003359,D04490}
- [M] Roughly what fraction of a Transformer block's parameters sit in the MLP versus attention? {Q007410,D00022}
- [M] Why is the FFN intermediate size typically 4x d_model, and why do SwiGLU/GeGLU blocks use three matrices and about 8/3x? {D04902,Q007273,D04491}
- [M] How does a gated FFN such as GLU or SwiGLU differ from a standard FFN with ReLU or GELU, and why is SwiGLU the default now? {Q005961,Q007457,Q011798,D00023,Q005965}
- [M] Write the computation formula of an FFN block using a GLU with a GELU or Swish gate. {Q012512,Q012513,Q012514}
- [M] What empirical evidence supports gated FFN variants over ReLU FFNs in LLMs? {D04492}
- [M] How do the compute shares of attention and the FFN change as sequence length grows, and where does attention overtake the FFN? {D00031,Q007458,Q006976}
- [M] What are the benefits and risks of tying input embeddings to the output projection? {D00027,D04903}
- [M] Why does the token embedding layer often need special treatment in training and fine-tuning? {D00035}
- [M] Count the parameters of a decoder-only Transformer given vocabulary size, hidden size, layers and FFN expansion. {D04901}
- [M] Using the approximation of 12 d_model^2 parameters per layer, estimate the size of a model with d_model=12288 and 96 layers. {GEN}
- [H] How would you estimate FLOPs and activation memory for one Transformer layer given batch size, sequence length and hidden size? {D00032}
- [M] What is a parallel attention-and-FFN block (as in GPT-J or PaLM), and what does it trade off against the sequential design? {GEN}

## Attention cost and efficient variants
- [E] What is the time and memory complexity of self-attention in sequence length, and which operation causes the quadratic term? {Q003327,D00001,D04499,Q007415,Q011206}
- [M] What alternatives to full attention exist for long sequences, and what does each give up? {Q011190,Q011930,Q009930,D00002}
- [M] Attention is O(n^2). Where does that actually bite in practice: prefill or decode? {Q007491}
- [M] Moving from 2k to 16k context, single-GPU prefill latency and memory grow far more than 8x. What explains this? {Q006965}
- [M] What does the (B, n_head, T, T) attention tensor imply at scale? {Q006988}
- [M] What are the disadvantages of self-attention, and how can they be overcome? {Q004320,Q007170}
- [H] What makes Transformers heavy in computation and memory, and how can we address it? {Q007175}
- [M] If you double sequence length, how do attention FLOPs and activation memory change in standard attention versus FlashAttention? {D04899}
- [M] Why does decoding with a KV cache cost O(n) per step in attention while recomputation costs O(n^2)? {D04900}
- [M] What is the difference between local and global attention? {Q007174}
- [M] How does sliding-window attention reduce cost, and how can information still propagate beyond the window across layers? {Q004689,D00017,D04906}
- [M] What does sliding-window attention give up? A single-layer windowed model answers about recent text but fails on facts far earlier; why? {Q007493,Q006985}
- [H] Does sliding-window attention make quality strictly worse than full attention, and how would you measure it? {Q007382}
- [M] Explain hybrid local/global attention stacks. What do you gain and what do you give up? {Q007533}
- [H] How would you choose the local-to-global attention ratio for a code model versus a chat model? {Q007534}
- [M] Compare sparse and linear attention approximations. Why have they not replaced softmax attention? {D00018,D04521}
- [M] What is linear attention and how does it fundamentally differ from standard softmax attention? {Q005974}
- [H] With top-k sparse attention, how would you choose the top-k budget, and what symptom shows it is too small? {Q010301}
- [H] In a hybrid sparse/dense attention stack, where would you place the sparse layers and how would you test that choice? {Q010302}
- [H] What is an attention sink, and why do streaming-inference methods keep the first few tokens in the cache? {Q004690,D00019,D04905}
- [H] What is attention sink, and why does gated attention mitigate it? {Q005973}
- [H] How do attention sinks connect to the lost-in-the-middle problem? {Q007561}
- [H] Would you expect attention sinks in an encoder-only model? {Q007532}
- [M] What is a state-space model such as Mamba, and why are hybrid SSM-Transformer models appealing? {D00034}

## FlashAttention
- [M] Why is standard attention memory-bound rather than compute-bound on modern GPUs? {D00012}
- [M] What does IO-awareness mean for GPU kernels, and how do the HBM and SRAM hierarchy shape an attention implementation? {D04520}
- [M] What is FlashAttention, and why is it faster than standard attention even though FLOPs are unchanged? {Q004686,Q005963,Q011788,Q007495,Q010174,D00013,D04518,D03752}
- [M] How does FlashAttention reduce memory usage, and in what sense is its memory linear in sequence length? {Q006938c,Q011209}
- [H] Why doesn't FlashAttention change the asymptotic FLOP complexity of attention? {Q007494}
- [H] Explain tiling and the online softmax rescaling in FlashAttention. Why is tiling possible at all? {D00014,Q007496,D04519}
- [H] Why does the FlashAttention backward pass recompute attention instead of caching it, and why is recomputation faster? {Q010175}
- [M] What does FlashAttention-2 change in work partitioning compared with the first version, and why does it help? {D00015}
- [H] Why do newer FlashAttention versions depend on specific GPU generations, and how does FP8 attention affect accuracy? {D00016}
- [M] How does FlashAttention exploit causal masking for speed? {Q007497,Q007424}
- [H] How do FlashAttention varlen kernels avoid materializing the block-diagonal mask for packed sequences? {Q008157}
- [M] What does FlashAttention do, and how is it different from PagedAttention? {Q008581}
- [M] Is FlashAttention compatible with ALiBi-style attention biases? {Q005928}
- [H] At 8k+ context, attention latency dominates on an A100 and you run a hand-written three-loop attention kernel. What is the highest-impact change and why is it safe? {Q006984}
- [M] Does FlashAttention produce exactly the same outputs as standard attention, or only approximately? {GEN}
- [H] Does FlashAttention help single-token decoding with a long KV cache? What do split-KV approaches such as Flash-Decoding add? {GEN}

## MQA, GQA and MLA
- [E] What are Multi-Query Attention and Grouped-Query Attention, and how do they differ from multi-head attention? {D04514,Q007510,Q011196}
- [M] Compare MHA, MQA and GQA in quality, KV-cache size, memory bandwidth and decode speed. {D00008,Q011786,Q005960,D04515}
- [M] Why have most large models moved from MHA to GQA, and why does it matter for serving? {D00009,Q004424,Q011216,D03751}
- [M] How do you modify multi-head attention code to implement GQA? What changes, and what does it buy at inference? {Q009617}
- [H] How would you convert an existing MHA checkpoint into a GQA model with minimal retraining (uptraining, mean-pooling KV heads)? {D00010,D04516,Q007512}
- [H] Given n_heads=32 and n_kv_heads=8, compute the KV cache per token per layer and explain how query heads share K/V. {D04517}
- [H] How does GQA change the parameter budget and the memory-bandwidth budget differently? {Q007599}
- [H] Why do open-weight models almost always ship GQA while a frontier lab might train MHA at the same size? {Q006991}
- [M] How would you choose the number of KV groups in GQA, and how does it interact with tensor-parallel degree? {GEN}
- [M] Compare MHA, MQA, GQA and multi-head latent attention in memory and throughput. {D03750}
- [M] What problem does multi-head latent attention (MLA) solve, and how does it differ from GQA? {Q005966,Q011787,D00011,Q007513,Q007536,Q009459}
- [H] In MLA, why does RoPE complicate the low-rank factorisation, and how is it usually resolved? {Q009856}
- [H] How does MLA interact with tensor parallelism across the head dimension? {Q009461}
- [M] In what regime would plain GQA still be the pragmatic choice over MLA? {Q009857}
- [H] Mistral 7B combines GQA and sliding-window attention. What does each buy you and what does each cost? {Q009816}
