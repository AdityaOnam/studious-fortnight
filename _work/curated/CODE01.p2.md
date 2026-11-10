## Tokenization and decoding
- [H] Implement BPE tokenizer training and encoding from scratch. {Q005164,Q011887,D03844,D04891}
- [M] Implement the byte-level fallback and decoding path of a BPE tokenizer so that any string round-trips. {GEN}
- [M] Write code to measure a tokenizer's fertility across languages, and say what you would do with the result. {Q010077}
- [E] Implement temperature sampling over a logits vector. {Q002359}
- [E] Implement top-k sampling. {Q002360}
- [M] Implement top-p (nucleus) sampling. {Q002361,Q009618a}
- [M] Implement temperature, top-k and top-p sampling together over a logits tensor. {Q005165,D03847,D04885}
- [M] Implement min-p sampling and compare its behaviour with top-p on a flat versus a peaked distribution. {GEN}
- [M] Implement a repetition penalty and a frequency penalty applied to logits during generation. {GEN}
- [M] Implement an autoregressive generate loop with greedy decoding, EOS handling, stop sequences and batched sequences that finish at different times. {GEN}
- [M] Implement beam search with length normalization for a causal language model, and say when a production system would use it. {Q002364,Q010018,D04886}
- [H] Implement constrained decoding that masks logits so the output always follows a given JSON schema or regular expression. {GEN}

## Efficient inference, kernels and distributed training
- [M] Implement an append-only KV cache for autoregressive decoding of a small Transformer and show it matches full recomputation. {Q002352,Q005163,Q011886,D03848,D04884}
- [H] Add a KV cache to causal multi-head attention and write the single-token decode path. Where is RoPE applied, and why only to q and k? {Q009820}
- [H] Implement single-step decode with a KV cache in PyTorch, then describe what changes for a long-context serving system. {Q009875}
- [H] Modify scaled dot-product attention for grouped-query attention. How does the causal mask interact with a KV cache at inference? {Q009206}
- [M] Estimate the KV cache memory for a given model configuration, batch size and context length, then write a function that computes it. {GEN}
- [M] Implement the online softmax algorithm in pure PyTorch. {Q002500}
- [H] Implement the tiled FlashAttention algorithm with online softmax in pure PyTorch, processing keys in blocks. {Q002489,D04898}
- [H] Write a fused softmax kernel in Triton. {Q002373}
- [H] Implement FlashAttention-2 in Triton. {Q002375}
- [H] Implement Ring Attention for long contexts. {Q002355}
- [H] Implement the block manager for a paged KV cache: allocate, append, free, and copy-on-write prefix sharing. {Q012034}
- [H] Implement prefix caching so that requests sharing a prompt prefix reuse KV blocks. {GEN}
- [H] Implement speculative decoding with a draft model and the accept/reject correction step. {Q002358}
- [H] Implement continuous batching for LLM inference. {Q002363}
- [H] Build a complete LLM inference engine. {Q002362}
- [M] Implement per-channel symmetric int8 weight quantization and dequantization for a linear layer. {GEN}
- [H] Implement gradient checkpointing. {Q002371}
- [H] Implement a tensor-parallel linear layer that splits a weight matrix across devices (column then row parallel). {GEN}
- [H] Implement Fully Sharded Data Parallel (FSDP) from scratch. {Q002350}

## Alignment, RL, generative and vision models
- [M] Implement a LoRA linear layer that wraps a frozen linear layer and supports merging. {Q002353,D03850,D04887}
- [H] Implement a QLoRA-style layer with a frozen 4-bit quantized base weight and a trainable low-rank adapter. {GEN}
- [M] Implement the supervised fine-tuning loss with prompt tokens masked out so only response tokens contribute. {GEN}
- [M] Implement a reward model with the Bradley-Terry pairwise preference loss. {GEN}
- [M] Implement the DPO loss given policy and reference log-probabilities for chosen and rejected responses. {Q002349,D03853,D04888}
- [M] Implement REINFORCE with a baseline on a simple environment. {D04890}
- [M] Implement the PPO clipped objective and a GAE advantage computation for a batch of trajectories. {D04889}
- [H] Implement PPO for RLHF, including a per-token KL penalty against a reference model. {Q002354}
- [H] Implement GRPO (Group Relative Policy Optimization). {Q002458}
- [M] Implement a symmetric contrastive (InfoNCE) loss for paired embeddings. {D03851}
- [H] Implement a CLIP training step with a contrastive loss over image and text batches. {Q002348}
- [H] Implement DDPM (denoising diffusion) training and sampling from scratch. {Q002343}
- [E] Implement the classifier-free guidance combination of conditional and unconditional predictions. {D03854}
- [H] Implement DDIM sampling with classifier-free guidance. {Q002342}
- [H] Implement a variational autoencoder with the reparameterization trick and the ELBO loss. {GEN}
- [H] Implement a Vision Transformer with masked autoencoder (MAE) pretraining. {Q002366}
- [H] Implement a Swin Transformer block with shifted window attention. {Q002367}
- [H] Implement a selective state space model (Mamba block). {Q002356}
- [M] Implement non-maximum suppression, then vectorise it. {Q005485,Q012044}
- [M] Implement intersection-over-union for batches of bounding boxes. {GEN}

## Retrieval and RAG
- [M] Create sentence embeddings from an LLM's hidden states and choose a pooling strategy. {Q002378}
- [E] Implement cosine similarity, dot product and Euclidean distance functions from scratch. {Q005153}
- [E] Compute pairwise cosine similarity between tensors of shape [N, D] and [M, D]. {Q004466}
- [M] Compute the masked mean of a [B, T, D] tensor using a [B, T] mask. {Q004465}
- [M] Implement exact cosine top-k semantic search over embeddings from scratch for a RAG system. {Q005141,Q005146,D03852}
- [M] Implement cosine similarity search over embeddings, then explain why you would not ship it. {Q011893}
- [M] Implement a BM25 scorer and a simple retriever over a small corpus. {D04896}
- [M] Implement hybrid retrieval that combines BM25 and dense scores with reciprocal rank fusion. {GEN}
- [M] Write code for different text chunking strategies (fixed-size, recursive, semantic). {Q005142}
- [M] Implement a text chunker with overlap that never splits a semantic unit. {Q011892}
- [M] Build a document parser that extracts text from PDFs and splits it into chunks. {Q005152}
- [M] Implement a basic RAG pipeline: chunking, embedding, vector search, and prompt assembly with a vector database. {Q005139,D04897}
- [M] Implement a simple re-ranker for search results. {Q005151}
- [M] Implement maximal marginal relevance to diversify retrieved passages. {GEN}
- [M] Implement recall@k, MRR and NDCG@k for evaluating a retriever. {GEN}
- [H] Implement a locality-sensitive hashing index for approximate nearest neighbor search and measure its recall against exact search. {GEN}
- [M] Implement metadata-filtered vector search and explain the pre-filter versus post-filter trade-off in code. {GEN}
- [H] Implement a groundedness check that flags answer sentences not supported by the retrieved context. {Q005148}

## LLM application plumbing and agents
- [E] Implement a prompt template system with variable substitution. {Q005143}
- [M] Build a simple prompt versioning system. {Q005155}
- [M] Implement token counting and context window management that truncates or drops history to fit a budget. {Q005154}
- [M] Implement conversation memory for a chatbot using a sliding window with a token budget, summary memory and a full buffer. {Q005147,D03859}
- [M] Implement streaming responses for an LLM API. {Q005145}
- [M] Write a parser for server-sent-event LLM token streams that handles arbitrary chunk boundaries and yields complete JSON events. {Q005169,Q009357}
- [H] Make a streamed-response parser async with a per-event timeout, and describe how to test chunk-boundary edge cases deterministically. {Q009358}
- [E] Implement a retry mechanism with exponential backoff and jitter for LLM API calls. {Q005149}
- [H] Write an async batch processor that runs an LLM call over 50,000 documents with a concurrency limit, retries with jitter and error isolation. {Q005168}
- [M] Implement a caching layer for LLM responses. {Q005156}
- [M] Implement semantic caching for LLM queries that reuses responses for similar queries. {Q005157,Q007016b}
- [M] Build an evaluation pipeline for LLM outputs using LLM-as-a-judge. {Q005144}
- [M] Write code to detect prompt injection attempts in user inputs. {Q005158}
- [M] Implement an LLM output guardrails system that checks for off-topic responses and PII leakage. {Q005159}
- [M] Write a function-calling (tool use) handler for an LLM API. {Q005150}
- [E] Implement validation of JSON tool arguments against a schema. {D03855}
- [M] Implement a permission-aware tool registry for an LLM agent. {D03856}
- [M] Implement a bounded agent loop with tool dispatch, error handling, a step budget and safety checks. {Q005140,Q005170,D03860}
- [M] Implement a ReAct agent that calls two tools and recovers from a tool error. {Q006866}
- [M] Implement a planner and executor for an agent with a clean boundary and tracing. {D03857}
- [M] Implement retry logic with idempotency keys for tool calls that have side effects. {D03858}
- [H] Build a multi-agent system where agents have different roles and collaborate on a task. {Q005160}

## More classical ML from scratch
- [M] Implement a regression tree using recursive binary splitting on squared error. {Q013227}
- [M] Implement cost-complexity pruning for a trained decision tree. {Q013228}
- [M] Compute impurity-based feature importances from a trained decision tree. {Q013229}
- [M] Implement AdaBoost with decision stumps from scratch. {Q013232,Q013361}
- [M] Compute the out-of-bag error of a random forest from its bootstrap samples. {Q014508,Q013366}
- [M] Implement a Gaussian Naive Bayes classifier from scratch. {Q014019,Q014327}
- [M] Implement a categorical Naive Bayes classifier with Laplace smoothing. {Q014022}
- [M] Implement distance-weighted k-nearest neighbors and compare it with uniform voting. {Q013632}
- [M] Implement a one-vs-one multiclass classifier on top of a binary SVM. {Q014859}
- [M] Implement mini-batch k-means. {Q013599}
- [M] Implement the silhouette coefficient from scratch for a given clustering. {Q013598,Q015026,Q012839}
- [M] Implement the Apriori algorithm to find frequent itemsets and generate association rules. {Q013005,Q015029}
- [M] Implement the Local Outlier Factor algorithm from scratch. {Q012705}
- [E] Write a function that flags outliers with the interquartile range (IQR) rule. {Q012699}
- [M] Implement user-based collaborative filtering with Pearson correlation from scratch. {Q014541,Q014545}
- [M] Implement item-item collaborative filtering with cosine similarity and produce top-N recommendations. {Q014543,Q014540}

## Feature selection, explainability and evaluation code
- [M] Select the top-k features by mutual information with the target, implementing the estimate for discrete features. {Q012971}
- [M] Implement recursive feature elimination around any estimator that exposes coefficients or importances. {Q012972,Q013325}
- [E] Write a function that drops one feature from every highly correlated pair above a threshold. {Q013445}
- [M] Implement the hashing trick for high-cardinality categorical features. {Q013444}
- [M] Compute a variance inflation factor for each predictor. {Q013807}
- [H] Compute exact Shapley values for a single prediction of a model with a handful of features. {Q013404}
- [M] Implement a simple LIME-style local explanation by fitting a weighted linear surrogate on perturbed samples. {Q013403}
- [M] Compute a partial dependence curve for one feature of a trained model. {Q013407}
- [E] Compute learning curves of training and validation score as the training set grows. {Q012770,Q013990}

## Optimization, statistics and linear algebra code
- [M] Implement AdaGrad and RMSprop optimizers from scratch. {Q012956,Q012954}
- [M] Minimize a non-convex function with simulated annealing. {Q012955}
- [M] Implement a genetic algorithm that evolves a random string toward a target string. {Q013516,Q013515}
- [M] Implement roulette-wheel and rank-based selection, single-point crossover and mutation for a genetic algorithm. {Q013519,Q013520,Q013517,Q013518}
- [M] Implement the Metropolis-Hastings algorithm to sample from an unnormalized posterior. {Q014766}
- [M] Implement Welch's two-sample t-test from scratch. {Q014764}
- [M] Implement a chi-squared test of independence on a contingency table. {Q014768}
- [M] Implement matrix inversion with Gauss-Jordan elimination and partial pivoting. {Q013754,Q013753}
- [M] Implement power iteration to find the dominant eigenvalue and eigenvector of a matrix. {Q013755}
- [M] Compute gradients of linear regression by hand and verify them against autograd. {Q014440}

## Time series, sequence and vision code
- [E] Implement simple exponential smoothing for a time series. {Q014962}
- [M] Compute the autocorrelation function of a time series from scratch. {Q014967}
- [M] Implement an efficient rolling-window mean in NumPy without Python loops. {Q014183,Q014192}
- [M] Implement a character-level RNN in NumPy that generates text from a seed. {Q014077}
- [M] Implement an n-gram language model with smoothing from scratch. {Q014130}
- [M] Implement the forward pass of a 2D convolution in NumPy, including stride and padding. {Q012876,Q014189}
- [M] Implement Sobel edge detection, then outline the remaining Canny steps of non-maximum suppression and hysteresis. {Q012910}
- [M] Implement the gradient penalty term of WGAN-GP. {Q013472}

## Reinforcement learning code
- [E] Compute discounted returns for a sequence of rewards. {Q014579}
- [M] Implement value iteration for a small MDP given its transition matrix. {Q014578}
- [M] Implement a tabular Q-learning agent with decaying epsilon-greedy exploration for a grid world. {Q014465,Q014577,Q014575,Q014583}
- [M] Implement a SARSA agent and compare its learned policy with Q-learning on the same environment. {Q014580}

## Feature extraction and autograd code
- [M] Implement a custom torch.autograd.Function, for example for arctanh, with an analytical backward pass, and verify it with gradcheck. {B0124,B0120,B0123}
- [M] Turn a pretrained torchvision ResNet-34 into a 512-dimensional feature extractor, with the correct ImageNet preprocessing. {B0166,B0167,B0168}
