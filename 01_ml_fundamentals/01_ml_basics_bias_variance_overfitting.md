---
domain: ml
topic: ml_basics_bias_variance_overfitting
title: ML basics, bias-variance, overfitting
tags: [ml, basics, bias-variance, overfitting]
count: 105
---
# ML basics, bias-variance, overfitting

## What machine learning is and the types of learning
- [ML01-001] What is machine learning, and how does it differ from traditional programming?
- [ML01-002] State Tom Mitchell's definition of learning and explain the roles of the task T, performance measure P and experience E using a concrete example.
- [ML01-003] What are the main types of machine learning, and how do supervised, unsupervised, semi-supervised, self-supervised, weakly supervised and reinforcement learning differ?
- [ML01-004] What is supervised learning, and what kinds of problems does it solve?
- [ML01-005] How does supervised learning differ from unsupervised learning? Give examples, including where K-Means clustering fits.
- [ML01-006] What is semi-supervised learning, and when is it worth using?
- [ML01-007] What is the difference between classification and regression problems?
- [ML01-008] What are the different kinds of tasks (classification, regression, clustering, ranking, density estimation and so on) that machine learning is applied to?
- [ML01-009] At a high level, how does a classification algorithm learn from labelled data?
- [ML01-010] How does reinforcement learning differ from supervised learning in terms of the feedback the learner receives?
- [ML01-011] Loosely, how can a supervised learning problem be converted into an unsupervised one and vice versa?
- [ML01-012] Define supervised, unsupervised and self-supervised learning. Where does each stage of modern LLM training fit?
- [ML01-013] What is active learning, and what is one strategy for choosing which examples to label?
- [ML01-014] What is the difference between online learning and batch (offline) learning, and when would you pick each?
- [ML01-015] What are the stages of building a machine learning model, from problem definition to deployment and monitoring?

## Training, generalization and model capacity
- [ML01-016] What is the difference between training error, test error and generalization error?
- [ML01-017] Write the formulae for training error and generalization error and point out how they differ.
- [ML01-018] Why do we care about performance on unseen data rather than on the training data?
- [ML01-019] Compare the representational capacity of a model with its effective capacity.
- [ML01-020] What is an inductive bias, and why is one necessary for a learner to generalize at all?
- [ML01-021] How does regularization differ from validation, and when is each the right tool?
- [ML01-022] What is empirical risk minimization, and why is minimizing training loss not the same as minimizing true risk?
- [ML01-023] What is the difference between a model's parameters and its hyperparameters, and how are each set?
- [ML01-024] Considering that directly minimizing 0-1 empirical risk is NP-hard, why do logistic regression and SVM use surrogate losses?
- [ML01-025] What is the local constancy or smoothness prior, and how does it limit what a learner can generalize to?

## Overfitting and underfitting
- [ML01-026] What are overfitting and underfitting in machine learning models?
- [ML01-027] How would you recognise overfitting versus underfitting from training and validation metrics?
- [ML01-028] What methods can be used to prevent or reduce overfitting?
- [ML01-029] How do you combat underfitting, and how does that differ from the fixes for overfitting?
- [ML01-030] Your validation loss is much lower than your training loss. What could cause that?
- [ML01-031] Your training accuracy is 99% but validation accuracy is 70%. What steps do you take, in what order?
- [ML01-032] Why can adding more features make a model overfit even when each feature looks informative?
- [ML01-033] Can a model overfit to the validation set? How does that happen and how do you guard against it?
- [ML01-034] When would you accept some overfitting deliberately?
- [ML01-035] A model overfits badly on a small dataset, but you cannot collect more data. What are your options and tradeoffs?

## Bias and variance
- [ML01-036] What do bias and variance mean in machine learning? Describe them with examples.
- [ML01-037] What is the difference between a high-bias model and a high-variance model?
- [ML01-038] How do bias and variance contribute to a model's expected test error? Write the decomposition for squared error.
- [ML01-039] What are the potential causes of high bias in a model?
- [ML01-040] What are the potential causes of high variance in a model?
- [ML01-041] How does model complexity relate to bias and variance?
- [ML01-042] Why is irreducible error part of the decomposition, and what are its sources?
- [ML01-043] What are learning curves?
- [ML01-044] How would you diagnose high bias versus high variance using learning curves, and what would you do about each?
- [ML01-045] What techniques reduce bias in machine learning models?
- [ML01-046] Which methods lower variance without increasing bias much?
- [ML01-047] How do bagging and boosting each affect bias and variance?
- [ML01-048] How can you estimate bias and variance empirically, for example using cross-validation or bootstrap resampling?
- [ML01-049] How does the amount of training data affect bias and variance?
- [ML01-050] Explain how regularization strength moves a model along the bias-variance curve.
- [ML01-051] Why can't bias and variance always be minimized simultaneously?

## The bias-variance tradeoff
- [ML01-052] Explain the bias-variance tradeoff.
- [ML01-053] How do you tell which of bias or variance is hurting your model, and how do you make the tradeoff in practice?
- [ML01-054] Is a k-nearest-neighbours model with small k or large k higher in variance? Explain in bias-variance terms.
- [ML01-055] Compare the bias and variance of a single deep decision tree, a random forest and a linear model.

## Double descent and modern generalization
- [ML01-056] What is double descent, and how does it change the classical story about model size and overfitting?
- [ML01-057] Where does the implicit bias of SGD enter the double descent story?
- [ML01-058] How can adding training data hurt model performance? Walk through the mechanism.
- [ML01-059] Does double descent contradict the bias-variance decomposition, or only the classical capacity narrative?
- [ML01-060] What is grokking, and does it have any bearing on how you actually train models?
- [ML01-061] Heavily over-parameterized neural networks can interpolate noisy training data and still generalize. Why is this puzzling from a classical viewpoint?

## Data splits and cross-validation
- [ML01-062] Why and how do you split data into training, validation and test sets, and what is each set used for?
- [ML01-063] What is cross-validation, how do you choose k in k-fold, and what are its limitations?
- [ML01-064] Compare k-fold, leave-one-out and stratified cross-validation. When would you use each?
- [ML01-065] How do you cross-validate on time-series data, and why does a random k-fold split give misleading results there?
- [ML01-066] What is data leakage? Give examples of how it creeps into a train/validation split.
- [ML01-067] What is nested cross-validation, and what problem does it solve compared with using a single CV loop for tuning and evaluation?
- [ML01-068] Why must the test set be touched only once, and what goes wrong if it guides model selection?
- [ML01-069] If your dataset has groups (for example several rows per patient), how should you split it?

## Learning theory and no free lunch
- [ML01-070] What is the no free lunch theorem, and what does it mean for choosing a learning algorithm in practice?
- [ML01-071] What is an ideal model? What is Bayes error and what are its sources?
- [ML01-072] What is the VC dimension?
- [ML01-073] What is the VC dimension of a linear classifier in n dimensions?
- [ML01-074] What is PAC learning, and what does it guarantee?
- [ML01-075] What is structural risk minimization, and how does it relate to regularization?
- [ML01-076] State the uniform convergence theorem and sketch how it is derived.
- [ML01-077] What is the sample complexity bound that follows from uniform convergence?
- [ML01-078] What is the error bound given by the uniform convergence theorem?
- [ML01-079] How does the required training set size depend on the hypothesis class for finite versus infinite hypothesis sets?
- [ML01-080] Why are VC bounds usually too loose to be useful for deep networks?

## Parametric vs non-parametric, and discriminative vs generative
- [ML01-081] What is the difference between parametric and non-parametric models? Give examples of each.
- [ML01-082] What are the practical tradeoffs of parametric versus non-parametric methods regarding data size, speed and flexibility?
- [ML01-083] What is the difference between linear and nonlinear algorithms in practice, and how do you choose between them?
- [ML01-084] What is the difference between generative and discriminative models?
- [ML01-085] Give examples of generative and discriminative classifiers, and say when you would prefer one over the other.
- [ML01-086] Why can Naive Bayes outperform logistic regression on very small training sets, but lose as data grows?
- [ML01-087] How does the split between predictive (discriminative) AI and generative AI differ in what the model outputs?

## Curse of dimensionality
- [ML01-088] What is the curse of dimensionality in machine learning? Illustrate with an example.
- [ML01-089] What problems commonly arise when analysing high-dimensional data?
- [ML01-090] How does the curse of dimensionality affect distance measures in high-dimensional spaces?
- [ML01-091] Explain sparsity in relation to the curse of dimensionality.
- [ML01-092] How does the curse of dimensionality affect the training of machine learning models?
- [ML01-093] Use the volume of a hypercube and its inscribed hypersphere to illustrate the curse of dimensionality.
- [ML01-094] How does the curse of dimensionality affect k-NN, and how can you mitigate it?
- [ML01-095] How do you combat the curse of dimensionality?
- [ML01-096] How many samples do you need to cover a feature space at fixed resolution as the dimension grows?
- [ML01-097] When is feature selection preferable to dimensionality reduction such as PCA for dealing with high dimensions?
- [ML01-098] Why can high-dimensional data still be learnable in practice despite the curse, for example because of the manifold hypothesis?

## Practical modelling judgement
- [ML01-099] How do you choose the right machine learning algorithm for a problem?
- [ML01-100] Is more data always better?
- [ML01-101] How would you justify using a neural network for a given problem? What do you need to know about the dataset, timeline and business context?
- [ML01-102] Would 1 million ride trips be enough to build an accurate ETA prediction model? How would you decide?
- [ML01-103] Given a black-box ML algorithm that you cannot modify, how could you improve its error?
- [ML01-104] You have a tight deadline and a small labelled dataset. How do you pick a simple baseline, and why start with one?
- [ML01-105] Model performance dropped in production although offline validation looked fine. What generalization issues might explain it?
