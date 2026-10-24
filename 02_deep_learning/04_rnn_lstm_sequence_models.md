---
domain: dl
topic: rnn_lstm_sequence_models
title: RNN, LSTM, GRU and sequence models
tags: [rnn, lstm, gru, seq2seq]
count: 102
---
# RNN, LSTM, GRU and sequence models

## RNN fundamentals
- [DL04-001] What is a recurrent neural network, and what kinds of sequential tasks is it well suited for?
- [DL04-002] How does a recurrent neural network differ from a feedforward network?
- [DL04-003] What is a time step in an RNN, and how does the hidden state carry information from one step to the next?
- [DL04-004] Describe the common input-output configurations of RNNs (one-to-many, many-to-one, many-to-many) and give a task for each.
- [DL04-005] Why do RNNs share the same weights across all time steps, and what does that buy you?
- [DL04-006] Write the equations of a vanilla RNN with hidden-to-hidden recurrence. How do you define the loss over a sequence, and what training problems would you expect?
- [DL04-007] What does it mean to unfold an RNN as a computational graph, and how does that relate to a dynamical system? What determines the size of the unfolded graph?
- [DL04-008] What are the advantages of viewing an RNN as an unrolled computational graph?
- [DL04-009] Why is the choice of activation function important in an RNN, and why is tanh the usual default rather than ReLU?
- [DL04-010] Is the RNN hidden state a lossless summary of the past inputs? If not, why not?
- [DL04-011] Compare an RNN with only output-to-hidden recurrence to one with hidden-to-hidden recurrence. What are the trade-offs?
- [DL04-012] How do you batch variable-length sequences for an RNN? Explain padding, masking and packed sequences.
- [DL04-013] How many trainable parameters does a vanilla RNN layer have with input size 128 and hidden size 256, including biases?
- [DL04-014] What is the difference between stateful and stateless RNN training, and when would you carry the hidden state across batches?
- [DL04-015] How would you initialize the hidden state at the start of a sequence: zeros, learned, or from another network? What are the trade-offs?
- [DL04-016] What are the main limitations of RNNs, and how have they been addressed?
- [DL04-017] Why can't an RNN be parallelised across time steps during training, and what does that mean for throughput on GPUs?

## Training RNNs: BPTT and teacher forcing
- [DL04-018] What is backpropagation through time (BPTT) and how does it work?
- [DL04-019] In BPTT, how are gradients for the shared recurrent weights accumulated over time steps?
- [DL04-020] What are the main challenges of training vanilla RNNs, and why is it hard to train them with plain SGD?
- [DL04-021] What are the limitations of full BPTT, and how does truncated BPTT mitigate them?
- [DL04-022] How do you choose the truncation length in truncated BPTT, and what dependencies can you no longer learn?
- [DL04-023] What is teacher forcing, and how does it compare with training by BPTT on the model's own outputs?
- [DL04-024] What is the disadvantage of strict teacher forcing, and how can it be addressed?
- [DL04-025] What is exposure bias in autoregressive RNN decoders, and how do scheduled sampling or sequence-level training help?
- [DL04-026] Why is batch normalization awkward for RNNs, and how does layer normalization help?
- [DL04-027] Which optimizer and learning rate schedule would you use for an LSTM language model, and why do many people prefer Adam or RMSProp for RNNs?
- [DL04-028] How do you preprocess time-series data (scaling, windowing, missing values) before feeding it to an RNN without leaking information?
- [DL04-029] Your LSTM training loss suddenly becomes NaN after a few epochs. What do you check and how do you fix it?
- [DL04-030] Estimate the memory needed for BPTT over a sequence of length T with batch B and hidden size H. How does gradient checkpointing reduce it?
- [DL04-031] Orthogonal and identity initialization of recurrent weights: why do they help, and what does an IRNN do?

## Vanishing and exploding gradients
- [DL04-032] Explain the vanishing gradient problem in RNNs and why it matters for learning long-range dependencies.
- [DL04-033] What is the exploding gradient problem, and how does it show up in RNN training?
- [DL04-034] Explain mathematically why gradients vanish or explode in an RNN, in terms of the product of Jacobians across time steps and the spectral radius of the recurrent matrix.
- [DL04-035] Why don't we see the vanishing/exploding gradient problem in the same way in feedforward networks?
- [DL04-036] How do you tackle exploding gradients in RNNs?
- [DL04-037] What is gradient clipping? Compare clipping by value with clipping by global norm, and explain how you would pick the threshold.
- [DL04-038] How do you tackle vanishing gradients in RNNs?
- [DL04-039] Does gradient clipping fix the vanishing gradient problem? Why or why not?
- [DL04-040] How does the choice of activation (sigmoid, tanh, ReLU) affect vanishing and exploding gradients in a recurrent network?
- [DL04-041] How would you empirically diagnose vanishing gradients in a trained RNN, for example by inspecting gradient norms per time step?
- [DL04-042] Your RNN only learns dependencies up to about 10-20 steps back. How would you investigate and fix this?
- [DL04-043] Why is there a fundamental tension between storing information robustly over long durations and being able to learn it by gradient descent?

## LSTM networks
- [DL04-044] What are the key components of an LSTM cell, and what is it used for?
- [DL04-045] What is the key architectural difference between LSTMs/GRUs and a traditional RNN, and what problem was it designed to fix?
- [DL04-046] Describe the gating mechanism of an LSTM. What do the forget, input and output gates each do?
- [DL04-047] Explain the memory (cell state) of an LSTM and how it is updated at each step.
- [DL04-048] Write out the LSTM update equations and explain the role of each term.
- [DL04-049] Why do gates use sigmoid while the candidate cell value uses tanh?
- [DL04-050] What is the difference between the hidden state h and the cell state c in an LSTM, and why are both needed?
- [DL04-051] How does the LSTM cell state mitigate the vanishing gradient problem?
- [DL04-052] The LSTM's cell state update is additive, but the gates are multiplicative. Why does the additive path still help gradients?
- [DL04-053] Derive the gradient of c_t with respect to c_{t-1} in an LSTM. Under what conditions can it still vanish or explode?
- [DL04-054] Why is it common to initialize the forget gate bias to 1 (or a positive value)?
- [DL04-055] How many parameters does an LSTM layer have with input size d and hidden size h?
- [DL04-056] What do peephole connections add to an LSTM, and are they worth it?
- [DL04-057] What would it mean if the forget gate of a trained LSTM is almost always near 1, or almost always near 0?
- [DL04-058] Do LSTMs completely solve the vanishing and exploding gradient problems? What failure modes remain?

## GRU and RNN variants
- [DL04-059] How does a Gated Recurrent Unit work, and how does it address the vanishing gradient problem?
- [DL04-060] What are the update and reset gates in a GRU, and what does each control?
- [DL04-061] Explain the differences between LSTM and GRU.
- [DL04-062] Compare GRU and LSTM in number of parameters and training speed, and say when you would choose each.
- [DL04-063] Compare vanilla RNNs, LSTMs and GRUs in trainability, computational cost and capacity.
- [DL04-064] How many parameters does a GRU layer have for input size d and hidden size h, and how does that compare with an LSTM?
- [DL04-065] How do recurrent variants such as QRNN, SRU or IndRNN trade expressiveness for speed or stability?

## Bidirectional and deep recurrent models, regularization
- [DL04-066] What is a bidirectional RNN, when would you use it, and when can it not be used?
- [DL04-067] How does a BiLSTM work, and how do you combine the forward and backward states for classification versus tagging?
- [DL04-068] When do stacked (deep) recurrent layers help, and why are residual connections often needed between layers?
- [DL04-069] What kinds of regularization do you use for an LSTM?
- [DL04-070] How do you apply dropout to an LSTM, and why is naive dropout on the recurrent connections problematic?
- [DL04-071] What are variational (locked) dropout, zoneout and weight dropout for recurrent networks, and what is each trying to preserve?
- [DL04-072] Which hyperparameters matter most for an LSTM model (hidden size, depth, sequence length, clipping), and how do you tune them?
- [DL04-073] How does padding side and masking interact with bidirectional RNNs, and what bug can arise if you get it wrong?

## Sequence-to-sequence models and attention
- [DL04-074] What are sequence-to-sequence models?
- [DL04-075] How does an encoder-decoder RNN work, and what limitation motivated attention?
- [DL04-076] Why is a single fixed-length context vector a bottleneck in an encoder-decoder, and why did reversing the source sentence help?
- [DL04-077] How do attention mechanisms work in conjunction with RNNs?
- [DL04-078] Compare Bahdanau (additive) and Luong (multiplicative) attention in an RNN decoder.
- [DL04-079] Compare greedy decoding with beam search for an RNN decoder. How does beam size affect quality, latency and length bias?
- [DL04-080] How do you handle out-of-vocabulary words in a seq2seq model, for example with subwords or a copy/pointer mechanism?
- [DL04-081] How would you evaluate a seq2seq model, and what are the weaknesses of perplexity and BLEU?
- [DL04-082] An LSTM encoder-decoder performs well on short sentences but degrades on long ones even with attention. What could be going wrong?

## CTC and sequence modelling tasks
- [DL04-083] What problem does Connectionist Temporal Classification (CTC) solve, and when is it used?
- [DL04-084] How does CTC handle alignment between inputs and outputs? Explain the blank token and the collapsing of repeated labels.
- [DL04-085] How is the CTC loss computed efficiently, and why does it sum over all valid alignments?
- [DL04-086] What conditional independence assumption does CTC make, and how do attention-based and RNN-Transducer models relax it?
- [DL04-087] Compare greedy CTC decoding with prefix beam search combined with a language model.
- [DL04-088] For sentiment classification with an LSTM, would you use the last hidden state, mean pooling or max pooling over time? Why?
- [DL04-089] Why is a CRF layer often added on top of a BiLSTM for sequence labelling such as NER?
- [DL04-090] How do you train an LSTM language model, and what are perplexity, weight tying and the softmax cost issue?
- [DL04-091] Compare character-level and word-level RNN language models.
- [DL04-092] When would you choose an LSTM over classical methods such as ARIMA for time-series forecasting, and what are the pitfalls?

## RNNs versus Transformers and state-space models
- [DL04-093] How do RNNs and Transformers differ?
- [DL04-094] Walk me from RNNs to LSTMs to Transformers. Why did attention win?
- [DL04-095] Compare RNNs and Transformers in inference memory: why does an RNN use constant state per token while a Transformer's KV cache grows with length?
- [DL04-096] In what situations would you still prefer an LSTM or GRU over a Transformer (streaming, small data, edge devices)?
- [DL04-097] What are state-space models trying to recover from RNNs?
- [DL04-098] What is a linear state-space model such as S4, and how can the same model be computed as a recurrence or as a convolution?
- [DL04-099] Why can a linear recurrence be parallelised with an associative scan while an LSTM cannot?
- [DL04-100] What does "selective" mean in Mamba, why does input-dependent state dynamics break the convolutional view, and how is it made efficient?
- [DL04-101] Compare Mamba, a Transformer and an LSTM on training parallelism, inference cost, long-context handling and recall of specific earlier tokens.
- [DL04-102] How do linear attention and models like RWKV connect Transformers to recurrent networks?
