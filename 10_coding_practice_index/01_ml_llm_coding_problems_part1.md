---
domain: coding
topic: ml_llm_coding_problems
title: ML / LLM coding problems (titles only)
tags: [coding, from-scratch, pytorch, implementation]
count: 104
part: 1/2
---
# ML / LLM coding problems (titles only) (part 1)

## Activations, losses and optimizers
- [CODE01-001] Implement softmax from scratch and make it numerically stable.
- [CODE01-002] Implement the sigmoid, tanh, ReLU, LeakyReLU and softmax activation functions from scratch.
- [CODE01-003] Write functions that compute MSE, MAE and RMSE from predictions and targets.
- [CODE01-004] Implement a custom activation as an nn.Module with a learnable parameter, such as a learned SiLU.
- [CODE01-005] Implement the Huber loss as a torch.nn.Module.
- [CODE01-006] Implement one-hot encoding without using F.one_hot.
- [CODE01-007] Implement label-smoothed targets and the corresponding cross-entropy loss.
- [CODE01-008] Implement a numerically stable softmax and cross-entropy loss in NumPy.
- [CODE01-009] Implement binary cross-entropy directly from logits in a numerically stable way.
- [CODE01-010] Implement token-level cross-entropy for a language model that ignores padding positions, and compute perplexity from it.
- [CODE01-011] Implement the KL divergence between two categorical distributions given their logits.
- [CODE01-012] Implement Dice loss for segmentation.
- [CODE01-013] Implement focal loss for an imbalanced classification problem.
- [CODE01-014] Write a finite-difference gradient check that verifies a hand-written backward pass.
- [CODE01-015] Implement SGD with momentum and weight decay as a custom optimizer.
- [CODE01-016] Implement Adam from scratch.
- [CODE01-017] Implement AdamW from scratch.
- [CODE01-018] Implement global-norm gradient clipping.
- [CODE01-019] Implement a learning-rate scheduler with linear warmup followed by cosine decay.
- [CODE01-020] Implement the Muon optimizer from scratch.

## Classical ML from scratch
- [CODE01-021] Implement the perceptron learning rule.
- [CODE01-022] Implement linear regression with gradient descent using vectorized NumPy.
- [CODE01-023] Implement a linear regression model class in PyTorch.
- [CODE01-024] Implement ridge regression using both the closed-form solution and gradient descent.
- [CODE01-025] Implement logistic regression with gradient descent and handle numerical stability.
- [CODE01-026] Implement multiclass softmax regression with vectorized gradients.
- [CODE01-027] Implement k-nearest neighbors classification with vectorized distance computation.
- [CODE01-028] Implement k-means clustering from scratch and discuss its convergence.
- [CODE01-029] Implement k-means++ initialization.
- [CODE01-030] Implement a Gaussian mixture model fitted with the EM algorithm.
- [CODE01-031] Implement principal component analysis using the SVD.
- [CODE01-032] Implement the best-split search of a decision tree using Gini impurity.
- [CODE01-033] Implement a random forest using bootstrap sampling and feature subsampling on top of your decision tree.
- [CODE01-034] Implement one gradient boosting step that fits a regression tree to the residuals.
- [CODE01-035] Implement a linear SVM trained with hinge loss.
- [CODE01-036] Implement a multinomial Naive Bayes text classifier with smoothing.
- [CODE01-037] Implement TF-IDF from scratch.
- [CODE01-038] Implement matrix factorization for recommendations trained with SGD.
- [CODE01-039] Implement word2vec skip-gram with negative sampling.
- [CODE01-040] Implement a feedforward neural network with backpropagation using only NumPy.

## Metrics, data splitting and preprocessing
- [CODE01-041] Implement precision, recall and F1 from scratch with vectorized operations and no loops.
- [CODE01-042] Implement binary accuracy from logits.
- [CODE01-043] Implement multiclass top-k accuracy.
- [CODE01-044] Compute a batched confusion matrix without per-example loops.
- [CODE01-045] Implement macro and micro averaged multiclass metrics from a confusion matrix.
- [CODE01-046] Implement binary classification metrics and ROC AUC from predicted scores.
- [CODE01-047] Implement average precision (area under the precision-recall curve) from scores and labels.
- [CODE01-048] Implement expected calibration error for a binary or multiclass classifier.
- [CODE01-049] Implement a bootstrap confidence interval for an arbitrary evaluation metric.
- [CODE01-050] Implement a streaming metric that accumulates results across batches.
- [CODE01-051] Implement sample-weighted losses and streaming metrics that aggregate correctly across distributed workers.
- [CODE01-052] Write code to perform k-fold cross-validation.
- [CODE01-053] Implement a reproducible train, validation and test split without scikit-learn that avoids leakage and supports stratification.
- [CODE01-054] Implement a time-ordered train/validation split for time-series data that avoids look-ahead leakage.
- [CODE01-055] Implement feature standardization with fit, transform and inverse_transform using only training statistics.
- [CODE01-056] Implement missing value imputation and handling of unseen categories at inference.
- [CODE01-057] Implement uniform, weighted and stratified sampling with reproducible seeds.
- [CODE01-058] Implement reservoir sampling for a stream of unknown length.
- [CODE01-059] Write a Python generator that lazily reads and transforms records from a dataset too large for memory.
- [CODE01-060] Implement a custom PyTorch Dataset for numerical and categorical features.
- [CODE01-061] Implement a Dataset and DataLoader for a CSV file.
- [CODE01-062] Write a custom Dataset and collate_fn for variable-length sequences.

## PyTorch layers, models and training loops
- [CODE01-063] Implement a feedforward neural network with fully connected layers in PyTorch, for example for MNIST.
- [CODE01-064] Implement a CNN for image classification in PyTorch.
- [CODE01-065] Implement an RNN model in PyTorch.
- [CODE01-066] Implement an LSTM model using the built-in LSTM layer.
- [CODE01-067] Implement an LSTM model using a hand-written LSTM cell and layer.
- [CODE01-068] Implement inverted dropout as a layer with different train and eval behaviour.
- [CODE01-069] Implement a BatchNorm1d layer with running statistics for training and evaluation modes.
- [CODE01-070] Implement a custom Conv2d class that mimics nn.Conv2d, and derive its output shape.
- [CODE01-071] Implement a custom MaxPool2d class that mimics nn.MaxPool2d.
- [CODE01-072] Implement a ResNet basic block with a skip connection and a projection shortcut.
- [CODE01-073] Implement the AlexNet architecture.
- [CODE01-074] Implement a 3D CNN with Conv3d and ConvTranspose3d layers for downsampling and upsampling volumetric data.
- [CODE01-075] Implement a convolutional autoencoder in PyTorch.
- [CODE01-076] Implement the generator and discriminator of a GAN and its training step in PyTorch.
- [CODE01-077] Implement Xavier and He weight initialization and compare activation variance across layers.
- [CODE01-078] Write a PyTorch training and evaluation loop with gradient clipping and checkpointing.
- [CODE01-079] Extend a training loop with gradient accumulation and mixed-precision training.
- [CODE01-080] Implement early stopping.
- [CODE01-081] Implement knowledge distillation with a temperature-scaled soft-target loss.

## Attention and Transformer components
- [CODE01-082] Implement scaled dot-product attention with a causal mask from scratch, in NumPy or PyTorch, with batch and head dimensions.
- [CODE01-083] Build a causal attention mask for autoregressive decoding.
- [CODE01-084] Implement padding and attention masks for a batch of variable-length token sequences.
- [CODE01-085] Implement multi-head self-attention from scratch, without nn.MultiheadAttention, and make it causal.
- [CODE01-086] Implement cross-attention between decoder states and encoder outputs.
- [CODE01-087] Implement an attention mechanism that scores encoder outputs against the current decoder hidden state in a seq2seq model.
- [CODE01-088] Implement multi-head attention, then convert it into grouped-query attention.
- [CODE01-089] Implement grouped-query attention in PyTorch and quantify where the KV-cache savings come from.
- [CODE01-090] Implement sliding window attention.
- [CODE01-091] Implement the sinusoidal positional embedding as an nn.Module.
- [CODE01-092] Implement ALiBi attention biases.
- [CODE01-093] Implement 2D positional embeddings for image patches.
- [CODE01-094] Implement rotary position embeddings (RoPE) from scratch.
- [CODE01-095] Implement rotary position embeddings and verify numerically that the attention score depends only on relative position.
- [CODE01-096] Implement RMSNorm and compare it numerically with LayerNorm.
- [CODE01-097] Implement LayerNorm from scratch with learnable scale and shift.
- [CODE01-098] Implement the position-wise feed-forward layer used inside Transformer blocks.
- [CODE01-099] Implement a SwiGLU feed-forward block.
- [CODE01-100] Implement a pre-norm Transformer decoder block with residual connections.
- [CODE01-101] Implement a small GPT-style decoder-only language model and train it on a toy corpus.
- [CODE01-102] Implement a top-k mixture-of-experts layer with an auxiliary load-balancing loss.
- [CODE01-103] Implement top-k MoE routing with a shared expert in PyTorch, and point out the efficiency and correctness traps.
- [CODE01-104] Rewrite the per-expert inner loop of a top-k MoE layer as a grouped matmul.
