---
domain: dl
topic: training_tricks_optimizers_norm
title: Training deep nets: optimizers, normalization, regularization
tags: [dl, optimizers, batchnorm, dropout, training]
count: 111
---
# Training deep nets: optimizers, normalization, regularization

## Training basics and hyperparameters
- [DL02-001] Explain the terms epoch, batch, batch size, and iteration.
- [DL02-002] What is the learning rate in neural network training?
- [DL02-003] What happens when the learning rate is too large? What happens when it is too small?
- [DL02-004] What is the difference between parameters and hyperparameters in a neural network?
- [DL02-005] Can you name and explain a few hyperparameters used for training a neural network?
- [DL02-006] Why do we initialize weights with schemes like Xavier or He instead of zeros or large random values?
- [DL02-007] What causes vanishing and exploding gradients in deep networks, and which training-time techniques mitigate them?
- [DL02-008] How do you choose the number of layers and neurons in a network, and when should you start from a pre-trained model instead?
- [DL02-009] How do you decide when to stop training a neural network?
- [DL02-010] What is early stopping, how do you choose its patience, and what are its pitfalls?
- [DL02-011] Describe the checkpointing pattern in ML training. What state must you save to resume a run exactly?
- [DL02-012] What strategies would you use to reduce the training time of a deep learning model?
- [DL02-013] Which sources of randomness make two training runs of the same model differ, and how do you make a run reproducible?
- [DL02-014] What does the training loss curve tell you about whether the bottleneck is optimization, data, or model capacity?

## SGD, momentum and adaptive optimizers
- [DL02-015] What is the difference between batch, mini-batch, and stochastic gradient descent?
- [DL02-016] Why do we use mini-batch SGD instead of full-batch gradient descent when training deep networks?
- [DL02-017] What is momentum in neural network optimization, and what problem does it solve over vanilla SGD?
- [DL02-018] What is Nesterov momentum and how does it differ from classical momentum?
- [DL02-019] What might happen if you set the SGD momentum coefficient too close to 1, for example 0.9999?
- [DL02-020] What is the Adagrad optimizer, and why does its learning rate decay too aggressively?
- [DL02-021] Explain the RMSprop optimizer and how it fixes the problem with Adagrad.
- [DL02-022] Compare SGD, momentum, RMSprop, Adagrad, and Adam update rules and say when each is appropriate.
- [DL02-023] Why can plain SGD struggle in ravines and saddle points, and how do momentum and adaptive methods help?
- [DL02-024] Why does SGD with momentum often generalize better than Adam on convolutional networks?
- [DL02-025] Why do adaptive optimizers need more optimizer-state memory, and how much extra memory does Adam need per parameter?
- [DL02-026] Adaptive optimizers like Adam and RMSprop scale gradients by past gradient magnitudes. Do they inherently perform gradient clipping? If not, why?
- [DL02-027] What is the Muon optimizer, how does it differ from AdamW, and why have some frontier pretraining runs adopted it?
- [DL02-028] Why might switching to Muon to fine-tune a model pretrained with AdamW go badly?

## Adam, AdamW and weight decay
- [DL02-029] Describe Adam's update rule and its key features.
- [DL02-030] Why does Adam need bias correction, and what happens without it?
- [DL02-031] What do the Adam hyperparameters beta1, beta2, and epsilon control, and when would you change them?
- [DL02-032] Adam vs AdamW: what is decoupled weight decay, and why did AdamW become the default for transformers?
- [DL02-033] Why is weight decay equivalent to L2 regularization under SGD but not under Adam?
- [DL02-034] Why do we exclude biases and LayerNorm parameters from weight decay?
- [DL02-035] What happens to the effective weight decay as the learning rate is cosine-annealed to near zero?
- [DL02-036] Why do large-model training runs often use beta2 around 0.95 instead of 0.999?
- [DL02-037] How can a very small epsilon or rare-token gradients cause Adam instability in large-model training?
- [DL02-038] Why do Adam-style optimizers behave differently from SGD when gradients are sparse, such as for embedding rows?

## Learning-rate schedules and warmup
- [DL02-039] How do you implement learning-rate scheduling, and which schedules (step, exponential, cosine, one-cycle) are common?
- [DL02-040] When should a learning-rate scheduler step: per batch or per epoch?
- [DL02-041] Why do transformer training recipes use learning-rate warmup, and what does the rest of the schedule typically look like?
- [DL02-042] How do cosine decay with warmup help LLM training compared with a constant learning rate?
- [DL02-043] Why does a transformer need warmup, and what happens to Adam's second-moment estimate early in training?
- [DL02-044] What goes wrong if you skip learning-rate warmup? Describe the failure signature in the loss and gradient-norm curves.
- [DL02-045] Why does a cosine-to-zero schedule interact badly with wanting to resume or extend training?
- [DL02-046] What is ReduceLROnPlateau, and when would you prefer it over a fixed schedule?
- [DL02-047] How would you run a learning-rate range test to pick a good maximum learning rate?
- [DL02-048] What are warmup-stable-decay (WSD) schedules, and why are they attractive for open-ended pretraining?
- [DL02-049] Your loss spikes right after the learning rate reaches its peak. What do you check and what do you change?
- [DL02-050] How do learning rate, warmup length, gradient clipping, and effective batch size interact?

## Batch size and gradient accumulation
- [DL02-051] What does batch size actually change about training dynamics: noise, speed, and memory?
- [DL02-052] You double the batch size. What do you do to the learning rate and why?
- [DL02-053] How do batch size and learning rate interact, and how would you scale them together?
- [DL02-054] Why might a very large batch size hurt generalization?
- [DL02-055] What is gradient accumulation and when would you use it?
- [DL02-056] What is gradient accumulation actually equivalent to, and where does the equivalence break, for example with BatchNorm?
- [DL02-057] What is the critical batch size, and why do returns diminish beyond it?
- [DL02-058] Why do linear learning-rate scaling and warmup matter for large-batch training, and when do they fail?
- [DL02-059] Your GPU runs out of memory at your target batch size. List the options to fit it and their tradeoffs.

## Normalization
- [DL02-060] How do batch normalization layers work, and what problem do they solve?
- [DL02-061] Why does batch normalization help training?
- [DL02-062] Does batch norm really work by reducing internal covariate shift? What does normalization do to the loss landscape?
- [DL02-063] How does batch normalization behave differently at training and inference time?
- [DL02-064] What are the hyperparameters of a batch normalization layer that can be tuned?
- [DL02-065] Batch norm vs layer norm: how does each work, and why do transformers use layer norm?
- [DL02-066] Can we apply batch normalization in RNNs? If not, what is the alternative?
- [DL02-067] When would you prefer group norm or instance norm over batch norm?
- [DL02-068] What is RMSNorm and why do many recent LLMs use it instead of LayerNorm?
- [DL02-069] Pre-LN versus post-LN transformers: how does the normalization placement affect training stability and the need for warmup?
- [DL02-070] Batch norm breaks with very small per-device batches or with distribution shift between train and test. How do you diagnose and fix it?
- [DL02-071] Why does batch norm interact badly with dropout, and with fine-tuning when batch statistics differ?

## Dropout and other regularization
- [DL02-072] What is regularization in neural networks, and why is it used?
- [DL02-073] How does dropout work, and what changes between training and inference?
- [DL02-074] How would you implement dropout in the forward and backward pass, and why do we rescale activations?
- [DL02-075] What is the effect of dropout on training and inference speed?
- [DL02-076] What are L1 and L2 regularization, and how do they affect a neural network's weights?
- [DL02-077] How do you apply dropout in an LSTM, and why can naive dropout hurt recurrent connections?
- [DL02-078] How is dropout used in LLMs and transformers, and why is it often turned off in large-scale pretraining?
- [DL02-079] When does label smoothing help, and when can it hurt?
- [DL02-080] What is data augmentation and how does it act as a regularizer?
- [DL02-081] How do you choose a dropout rate, and how does it depend on layer type and model size?
- [DL02-082] How would you use MC dropout to get uncertainty estimates?
- [DL02-083] Why can dropout and batch norm interact badly when used in the same block?
- [DL02-084] Your deep network strongly overfits the training set. What would you try, in what order?
- [DL02-085] How do you monitor overfitting during training and reduce it?

## Gradient clipping and numerical stability
- [DL02-086] What is gradient clipping and why is it useful for training deep models?
- [DL02-087] What is clipping by global norm, and why is it standard in LLM training?
- [DL02-088] How does clipping by value differ from clipping by norm, and how do you choose a threshold?
- [DL02-089] How would you use gradient-norm logging to detect an impending loss spike or divergence?
- [DL02-090] Loss becomes NaN after several thousand steps. Walk through how you would find the cause.
- [DL02-091] What are common mitigations for loss spikes in large-model training (skipping batches, restarts, lower beta2, QK-norm, z-loss)?

## Mixed precision and training efficiency
- [DL02-092] What is mixed precision training, and what numerical issue does loss scaling address?
- [DL02-093] Why do mixed-precision setups keep fp32 master weights?
- [DL02-094] Why did BF16 largely replace FP16 with loss scaling for training?
- [DL02-095] Which operations should stay in fp32 under mixed precision, and why?
- [DL02-096] What is activation (gradient) checkpointing and what is the compute-memory tradeoff?
- [DL02-097] A model runs fine in FP32 but produces garbage after conversion to lower precision. If it only fails on some inputs, what does that suggest?
- [DL02-098] Estimate the memory needed to train a 7B-parameter model with Adam in mixed precision, excluding activations.
- [DL02-099] What does FP8 training require beyond BF16 to remain stable?

## Debugging training and hyperparameter tuning
- [DL02-100] Why is overfitting a single small batch the first step when debugging a training pipeline?
- [DL02-101] Training loss or test loss stays constant. What do you check?
- [DL02-102] What common training problems occur in deep learning, and how do you debug them?
- [DL02-103] A network overfits a small batch but fails to generalize. How do you debug it?
- [DL02-104] Training loss goes down but validation loss goes up from the start. What are the likely causes?
- [DL02-105] Validation loss is lower than training loss. Is that a bug, and what could explain it?
- [DL02-106] Why is random search often preferred over grid search for tuning deep learning hyperparameters?
- [DL02-107] Which hyperparameters would you tune first for a new network, and which would you leave at defaults?
- [DL02-108] How would you tune hyperparameters cheaply for a model too expensive to train many times (small proxies, muP, scaling-law extrapolation)?
- [DL02-109] Two training runs with identical configs reach different final losses. How do you tell noise from a real regression?
- [DL02-110] Training diverges only when you scale to more GPUs. What differs in the setup and what would you check?
- [DL02-111] Which per-layer statistics (activation, gradient and update-to-weight ratios) would you monitor to catch silent training bugs?
