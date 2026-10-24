---
domain: dl
topic: neural_net_basics_backprop
title: Neural network basics and backpropagation
tags: [dl, backprop, activation, mlp]
count: 93
---
# Neural network basics and backpropagation

## Deep learning vs classical machine learning
- [DL01-001] What is deep learning, and how does it differ from traditional machine learning approaches?
- [DL01-002] What kinds of problems can neural networks solve?
- [DL01-003] What does the 'depth' of a neural network mean, and how do shallow and deep networks differ?
- [DL01-004] What is representation learning, and why is it useful?
- [DL01-005] When would you prefer classical ML such as gradient-boosted trees over a neural network, and when the reverse?
- [DL01-006] Why did deep learning only take off around 2012 although the core ideas date back decades?
- [DL01-007] What is the mathematical motivation for deep learning over standard ML techniques?
- [DL01-008] How does the number of training samples relate to the number of regions in function space that standard ML versus deep learning can distinguish?
- [DL01-009] How does deep learning tackle the curse of dimensionality?
- [DL01-010] Why do hierarchical, compositional features make deep networks more parameter-efficient than very wide shallow ones?

## Neurons, perceptrons and MLPs
- [DL01-011] What is an artificial neural network, and how does it loosely relate to biological neurons?
- [DL01-012] Describe the structure of a basic artificial neuron.
- [DL01-013] What is a perceptron, and what kind of functions can a single perceptron represent?
- [DL01-014] What roles do weights and biases play in a neural network?
- [DL01-015] Describe the architecture of a multi-layer perceptron (MLP) and explain a feedforward neural network.
- [DL01-016] Why can a single perceptron not learn XOR, and how does adding a hidden layer fix this?
- [DL01-017] Why is the bias term needed? What geometric effect does it have on the decision boundary?
- [DL01-018] How does matrix multiplication implement a layer of a neural network, and why is it GPU-friendly?
- [DL01-019] How does a neural network with one layer, one input and one output compare to logistic regression?
- [DL01-020] What happens in a neural network if you remove all the hidden layers?
- [DL01-021] How do you count the number of parameters in an MLP with given layer sizes?
- [DL01-022] How do the width and depth of an MLP each affect capacity, trainability and compute cost?

## Forward propagation
- [DL01-023] Walk through a forward pass of a neural network from input to output.
- [DL01-024] What intermediate values must be stored during the forward pass, and why does this dominate training memory?
- [DL01-025] Why do we process inputs in mini-batches, and how does batching change the shapes in the forward pass?

## Activation functions
- [DL01-026] What are activation functions, and why are they necessary?
- [DL01-027] Why do neural networks need non-linear activation functions? What does a deep network without them collapse into?
- [DL01-028] List the common activation functions and give the formula and output range of each.
- [DL01-029] What is the sigmoid function, and what does it do?
- [DL01-030] Compare sigmoid, tanh, ReLU, Leaky ReLU and softmax, with their pros and cons.
- [DL01-031] Why are sigmoid and tanh not preferred in the hidden layers of a deep network?
- [DL01-032] Why is ReLU better and more widely used than sigmoid in hidden layers?
- [DL01-033] Between sigmoid and tanh, why is tanh generally the better choice for a hidden layer?
- [DL01-034] What is the dying ReLU problem, and how would you detect dead units in a trained network?
- [DL01-035] Compare ReLU, Leaky ReLU, PReLU and ELU. When would you choose each?
- [DL01-036] What is GELU, why is it preferred in Transformers, and how is it commonly approximated?
- [DL01-037] Define Swish/SiLU and explain why it is smooth and non-monotonic.
- [DL01-038] What is a Gated Linear Unit, and how does it differ from a plain activation in a feed-forward block?
- [DL01-039] Compare ReLU, GELU and SwiGLU in their gradient behaviour near zero. Why does it matter for deep Transformers?
- [DL01-040] Is ReLU differentiable at zero? How do frameworks handle the gradient there?
- [DL01-041] Why are ReLU networks piecewise linear, and what does that imply for the function they represent?
- [DL01-042] What does it mean for an activation function to be zero-centered, and why does it affect optimisation?
- [DL01-043] Why is the GELU or SiLU gradient not monotonic, and could that hurt or help training?

## Output layers, softmax and losses
- [DL01-044] What is the softmax function, and when do you use it?
- [DL01-045] Explain softmax and the temperature parameter. How do you compute softmax stably, and where does temperature show up in ML?
- [DL01-046] What breaks numerically if you compute log(softmax(z)) naively, and how is it fixed?
- [DL01-047] Which output activation would you use for classes that are not mutually exclusive, and why?
- [DL01-048] Why is cross-entropy preferred over mean squared error for classification with a softmax or sigmoid output?
- [DL01-049] Which output activation and loss would you pick for regression, binary classification, multiclass and multi-label problems?
- [DL01-050] Show that the gradient of softmax cross-entropy with respect to the logits is simply (p - y).
- [DL01-051] What does it mean that softmax is invariant to adding a constant to all logits, and why does this matter?

## Backpropagation
- [DL01-052] What is backpropagation, and why is it important for training neural networks?
- [DL01-053] Explain backpropagation to a strong software engineer who has never done ML. Why is it efficient?
- [DL01-054] Walk through backpropagation on a small computational graph and state the chain rule at one node.
- [DL01-055] How does backpropagation differ from gradient descent? What does each compute and what does each do?
- [DL01-056] Why is reverse-mode automatic differentiation used for training rather than forward mode or numerical differentiation?
- [DL01-057] What is the computational cost of a backward pass relative to the forward pass, and why?
- [DL01-058] Derive the gradient of the loss with respect to the weights of a single linear layer followed by an activation.
- [DL01-059] How would you verify a hand-written backward pass using gradient checking?
- [DL01-060] Why must backpropagation store forward activations, and how does gradient checkpointing trade compute for memory?
- [DL01-061] How does a framework such as PyTorch build the autograd graph and compute gradients during backward()?
- [DL01-062] What problem does the sigmoid cause during backpropagation?
- [DL01-063] Why is backpropagation not considered biologically plausible?

## Vanishing and exploding gradients
- [DL01-064] What is the vanishing gradient problem, and how does it affect training?
- [DL01-065] Explain vanishing and exploding gradients, their causes in deep networks, and practical mitigations.
- [DL01-066] How does the exploding gradient problem occur, and what are the potential solutions?
- [DL01-067] How do you identify whether your model is suffering from exploding gradients?
- [DL01-068] How would you diagnose vanishing gradients from per-layer gradient norms during training?
- [DL01-069] What are skip (residual) connections, and how do they help training?
- [DL01-070] Why does the residual connection's Jacobian I + ∂f/∂x fix gradient flow?
- [DL01-071] How does gradient clipping work, and when would you use norm clipping versus value clipping?
- [DL01-072] How do batch normalization and layer normalization help gradient flow?
- [DL01-073] Why are vanishing gradients especially severe in vanilla RNNs, and how do LSTMs mitigate them?
- [DL01-074] Show how the product of per-layer Jacobians leads to exponentially shrinking or growing gradients as depth grows.
- [DL01-075] Your deep network's loss becomes NaN after a few iterations. What would you check first?
- [DL01-076] Name the common fixes for vanishing gradients (activation choice, initialization, normalization, residuals) and say which you would try first.

## Weight initialization
- [DL01-077] Why can't you initialize all weights to zero?
- [DL01-078] What do Xavier/Glorot and He initialization do, and when should each be used?
- [DL01-079] Why is random initialization needed to break symmetry between neurons?
- [DL01-080] Derive why fan_in (and fan_out) appears in the variance formula for the weight initialization of a linear layer.
- [DL01-081] How do default weight initializations in frameworks such as PyTorch work for linear and convolutional layers?
- [DL01-082] Why do residual networks need an extra 1/√N scaling in their initialization?
- [DL01-083] What breaks if you initialize a Transformer with std 0.2 instead of 0.02?
- [DL01-084] How does initialization interact with the choice of activation function (ReLU vs tanh)?
- [DL01-085] What would happen if you initialize all weights with very large values versus very small values?
- [DL01-086] Is it fine to initialize biases to zero? Are there cases where you would not?

## Universal approximation and expressiveness
- [DL01-087] What is the universal approximation theorem?
- [DL01-088] State the universal approximation theorem. What technique is used to prove it?
- [DL01-089] Given the universal approximation theorem, why can't an MLP still reach an arbitrarily small error in practice?
- [DL01-090] The theorem says one hidden layer suffices, so why do we use deep networks instead?
- [DL01-091] What are depth-separation results, and what do they say about the efficiency of deep versus shallow networks?
- [DL01-092] Does the universal approximation theorem tell us anything about whether gradient descent will find the approximating function?
- [DL01-093] How many linear regions can a ReLU network with L layers and n units per layer have, and why does it grow with depth?
