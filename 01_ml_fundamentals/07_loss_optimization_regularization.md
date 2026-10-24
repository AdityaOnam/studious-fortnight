---
domain: ml
topic: loss_optimization_regularization
title: Loss functions, optimization, regularization
tags: [ml, loss, optimization, regularization]
count: 142
---
# Loss functions, optimization, regularization

## Loss, cost and objective functions
- [ML07-001] What is the role of a loss function in supervised learning, and what is a cost function used for during training?
- [ML07-002] What is the difference between a loss function, a cost function and an objective function?
- [ML07-003] What does optimization mean in the context of machine learning?
- [ML07-004] What are the characteristics of a good loss function for training a model?
- [ML07-005] How does the choice of loss function affect how well a model generalizes?
- [ML07-006] How can a learning problem be turned into an optimization problem, and how do the two differ?
- [ML07-007] What is empirical risk minimization, and why is the risk called empirical?
- [ML07-008] Why is pure empirical risk minimization rarely the whole story in deep learning?
- [ML07-009] What is the 0-1 loss, and why is it impractical to optimize directly?
- [ML07-010] What is a surrogate loss, and what properties should it have relative to the true metric you care about?
- [ML07-011] If a classifier has 100% accuracy, what are the lower and upper bounds on the loss of a single training example?
- [ML07-012] Can the training loss go down while accuracy stays flat or even drops? Explain why this happens.
- [ML07-013] When would you train on one loss but select and report models using a different metric?

## Regression losses
- [ML07-014] Describe the mean squared error loss and when it is appropriate.
- [ML07-015] Compare L2 loss, L1 loss and Huber loss for regression.
- [ML07-016] How does a model that minimizes squared error differ from one that minimizes absolute error, and when is each appropriate?
- [ML07-017] When is the Huber loss preferable to MSE, and what does its threshold parameter control?
- [ML07-018] What noise distribution corresponds to the L1 loss, and when would you prefer it?
- [ML07-019] Which statistic of the target distribution does MSE estimate, and which does MAE estimate?
- [ML07-020] How do the gradients of MSE and MAE behave near zero error, and what does that mean for optimization?
- [ML07-021] What is quantile (pinball) loss, and how do you use it to predict intervals?
- [ML07-022] Your regression data has heavy-tailed outliers. How would you adapt the loss function?
- [ML07-023] Why might you minimize MSE on log-transformed targets, and what does this do to the loss on the original scale?
- [ML07-024] What do you change in the loss if the noise variance depends on the input (heteroscedastic regression)?

## Classification losses and cross-entropy
- [ML07-025] What is cross-entropy loss?
- [ML07-026] Explain the cross-entropy loss and its applications.
- [ML07-027] How is log loss used in logistic regression, and why is cross-entropy appropriate for classification?
- [ML07-028] Derive cross-entropy loss from first principles. Why is it the right loss for classification and language modeling?
- [ML07-029] Why is MSE a poor loss for classification, even though it can work? Connect it to the probabilistic view of losses.
- [ML07-030] What is the difference between binary cross-entropy and categorical cross-entropy?
- [ML07-031] How does cross-entropy relate to KL divergence and to the entropy of the label distribution?
- [ML07-032] What is hinge loss, and when is it applied?
- [ML07-033] How does the hinge loss lead to margin maximization in SVMs?
- [ML07-034] Compare hinge loss, logistic loss and exponential loss as surrogates for the 0-1 loss.
- [ML07-035] Write the loss function for logistic regression. Why does it have a global minimum?
- [ML07-036] Show that softmax followed by cross-entropy gives a gradient of p minus y with respect to the logits.
- [ML07-037] Derive the p minus y gradient for logistic loss and show where the cancellation happens.
- [ML07-038] What does label smoothing change in the softmax cross-entropy gradient?
- [ML07-039] What happens to the logistic regression weights if the data is perfectly linearly separable and there is no regularization?
- [ML07-040] How does cross-entropy penalize confident wrong predictions, and why can that hurt with noisy labels?
- [ML07-041] Why do implementations combine softmax and cross-entropy into one numerically stable operation?
- [ML07-042] How does focal loss modify cross-entropy, and when does it help?
- [ML07-043] How would you modify the loss for a heavily imbalanced classification problem?

## Convexity and the loss landscape
- [ML07-044] What is the difference between convex and non-convex cost functions?
- [ML07-045] Why is convexity important in optimization problems?
- [ML07-046] Distinguish between local minima and global minima, and say why the global minimum matters.
- [ML07-047] Is the linear regression MSE loss convex? How can you show it using the Hessian?
- [ML07-048] Is logistic regression's loss convex in the weights? Is the same true for a neural network?
- [ML07-049] What challenges arise when using gradient descent on non-convex functions?
- [ML07-050] What are saddle points, and why are they a bigger concern than local minima in high dimensions?
- [ML07-051] Neural network losses are non-convex. Why does gradient-based training still work well in practice?
- [ML07-052] What does a contour plot of the cost function in linear regression tell you about gradient descent?
- [ML07-053] What is the effect of the condition number of the Hessian on gradient descent convergence?

## Gradient descent and its variants
- [ML07-054] What is gradient descent and how does it work?
- [ML07-055] What does the gradient or derivative of the cost function tell us in gradient descent?
- [ML07-056] Why use gradient descent to minimize a function, and how does it find a local minimum?
- [ML07-057] How does an optimization algorithm work to minimize the cost function?
- [ML07-058] Explain gradient descent and its main variants.
- [ML07-059] What is batch gradient descent, and when would you use it?
- [ML07-060] What is stochastic gradient descent, and what are its advantages and disadvantages over batch gradient descent?
- [ML07-061] What is mini-batch gradient descent, and how does it differ from batch and stochastic variants?
- [ML07-062] Compare batch, stochastic and mini-batch gradient descent, with pros and cons of each.
- [ML07-063] How does batch size affect training speed, gradient noise and generalization?
- [ML07-064] Why does the gradient noise in SGD sometimes help rather than hurt?
- [ML07-065] Why should you shuffle training data between epochs when using SGD?
- [ML07-066] If you increase the batch size by a factor of k, how would you adjust the learning rate, and why?
- [ML07-067] What are exploding gradients, and how does gradient clipping help?
- [ML07-068] How would you verify that your hand-derived gradient is correct?
- [ML07-069] Your training loss becomes NaN or oscillates wildly. How would you debug it?
- [ML07-070] What convergence rates does gradient descent have for convex smooth, strongly convex, and non-convex objectives?
- [ML07-071] Why does SGD with a constant learning rate fail to converge exactly, and how do decaying step sizes fix it?

## Learning rate, momentum and adaptive optimizers
- [ML07-072] What is a hyperparameter, and how does it relate to the optimization process?
- [ML07-073] What is a learning rate, and why is it important in gradient descent?
- [ML07-074] How do you choose a good learning rate?
- [ML07-075] What symptoms indicate that your learning rate is too high or too low?
- [ML07-076] What are common learning rate schedules, and why does warmup help?
- [ML07-077] Explain how momentum accelerates gradient descent.
- [ML07-078] How does Nesterov momentum differ from classical momentum?
- [ML07-079] How does AdaGrad work, and what problem does it address?
- [ML07-080] Explain RMSprop and how it fixes AdaGrad's shrinking learning rate.
- [ML07-081] Compare momentum, RMSprop and Adam as extensions of gradient descent.
- [ML07-082] Why do features on very different scales slow down gradient descent, and how does normalization help?
- [ML07-083] Why is Adam sometimes reported to generalize worse than SGD with momentum?
- [ML07-084] What is the difference between L2 regularization and weight decay in Adam, and why does AdamW exist?
- [ML07-085] What are second-order methods, and how do they differ from first-order methods?
- [ML07-086] Explain Newton's method for optimization. Why is it rarely used directly for deep networks?
- [ML07-087] What is L-BFGS, and when is it preferable to SGD?
- [ML07-088] What is line search, and how is it used in gradient-based optimization?

## Maximum likelihood and MAP estimation
- [ML07-089] What is maximum likelihood estimation?
- [ML07-090] What is the maximum likelihood estimate of a parameter vector, and where does the log come from?
- [ML07-091] Is there any case where the maximum likelihood estimate does not exist?
- [ML07-092] Show how maximum likelihood generates the standard loss functions, and where MAP connects to regularization.
- [ML07-093] Describe maximum likelihood estimation as it applies to logistic regression.
- [ML07-094] Derive MSE from the Gaussian likelihood explicitly.
- [ML07-095] Prove that MSE for linear regression can be derived from maximum likelihood under the right assumptions.
- [ML07-096] What is the difference between MLE and MAP estimation?
- [ML07-097] What is the difference between MAP, method of moments and MLE estimators, and when would you use each?
- [ML07-098] What do you mean by Bayesian regularization?
- [ML07-099] Which prior on the weights makes MAP equivalent to L2 regularization, and which gives L1?
- [ML07-100] Why does minimizing cross-entropy equal maximizing likelihood, and equal minimizing KL divergence to the data distribution?
- [ML07-101] Is the MLE of the variance of a Gaussian biased? What does this say about MLE in general?
- [ML07-102] How does the influence of the prior on the MAP estimate change as the amount of data grows?
- [ML07-103] What are the consistency and asymptotic efficiency properties of the MLE, and when do they fail?

## Regularization fundamentals
- [ML07-104] What is regularization and why do we need it?
- [ML07-105] Intuitively, what does regularization do during the optimization procedure?
- [ML07-106] How does regularization help with bias and variance?
- [ML07-107] Explain the concept of regularization in cost functions.
- [ML07-108] How does regularization help when the number of features is large compared to the data, as with the curse of dimensionality?
- [ML07-109] How does regularization help prevent overfitting in practice, and what are the main design choices?
- [ML07-110] How do we select the right regularization strength?
- [ML07-111] What happens to bias, variance and training error as the regularization strength increases?
- [ML07-112] Why do we usually not regularize the bias term?
- [ML07-113] Beyond L1 and L2, how do early stopping, data augmentation and label smoothing act as regularizers?
- [ML07-114] How does dropout act as a regularizer, and how does it relate to L2 regularization?
- [ML07-115] Can too much regularization hurt, and how would you recognize underfitting caused by it?

## L1, L2 and elastic net
- [ML07-116] What is L2 regularization?
- [ML07-117] What is L1 regularization?
- [ML07-118] What is weight decay, and why is it added?
- [ML07-119] Explain L1 (Lasso) and L2 (Ridge) regularization and their effect on weights and sparsity.
- [ML07-120] What are the differences between L1 and L2 regularization?
- [ML07-121] Compare L1 and L2 regularization. Why does L1 produce sparse weights?
- [ML07-122] Why does L1 regularization result in sparse models?
- [ML07-123] Compare and contrast L1 loss versus L2 loss, and L1 regularization versus L2 regularization.
- [ML07-124] How does Ridge regression prevent overfitting?
- [ML07-125] Describe Lasso regression and its unique property.
- [ML07-126] What is elastic net, and when would you use it?
- [ML07-127] What are the differences between L1 and L2 regularization in logistic regression?
- [ML07-128] How does L1 or L2 regularization affect a neural network?
- [ML07-129] Explain the geometry of the L1 and L2 constraint regions and why the L1 solution lands on the axes.
- [ML07-130] If features are highly correlated, how do Lasso and Ridge behave differently?
- [ML07-131] Why is the Lasso objective not differentiable, and how do solvers handle that?
- [ML07-132] If you have more features than samples, how many features can the Lasso select at most?
- [ML07-133] Why does an unscaled feature interfere with L2 regularization differently from L1's sparsity property?
- [ML07-134] Why should features be standardized before applying L1 or L2 regularization?

## Closed-form solutions and implicit regularization
- [ML07-135] Derive the normal equation for linear regression.
- [ML07-136] What is the closed-form solution of linear regression, and when do you use gradient descent instead?
- [ML07-137] What is the computational complexity of the normal equation compared to gradient descent as features grow?
- [ML07-138] What happens to the normal equation when X transpose X is not invertible, and how does Ridge fix it?
- [ML07-139] What is the closed-form solution of Ridge regression, and why does it shrink coefficients?
- [ML07-140] Why is early stopping approximately equivalent to L2 regularization for quadratic losses?
- [ML07-141] What is implicit regularization of SGD, and why does it matter in overparameterized models?
- [ML07-142] Why does the Lasso have no closed-form solution in general, and what algorithms are used instead?
