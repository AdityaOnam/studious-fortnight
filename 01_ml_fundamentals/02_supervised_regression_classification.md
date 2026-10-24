---
domain: ml
topic: supervised_regression_classification
title: Supervised learning: regression and classification models
tags: [ml, regression, classification, svm, knn]
count: 152
---
# Supervised learning: regression and classification models

## Regression vs classification basics
- [ML02-001] What is the difference between regression and classification, and which models would you use for each?
- [ML02-002] What is the difference between binary, multiclass and multilabel classification?
- [ML02-003] What is a decision boundary, and how does its shape differ for logistic regression, kNN and a kernel SVM?
- [ML02-004] What is the difference between generative and discriminative classifiers? Give examples of each.
- [ML02-005] What is the difference between parametric and non-parametric models? Where do linear regression, kNN and SVMs fall?
- [ML02-006] Which of linear regression, logistic regression, kNN, Naive Bayes and SVM require feature scaling, and why?
- [ML02-007] How does the bias-variance tradeoff show up in simple linear models versus kNN with small k or an RBF SVM?
- [ML02-008] You have 10k labelled rows and 50 tabular features. How would you decide between logistic regression, SVM, kNN and Naive Bayes?

## Linear regression fundamentals
- [ML02-009] What is linear regression and when do you use it?
- [ML02-010] What is the difference between simple and multiple linear regression?
- [ML02-011] Explain ordinary least squares, residuals, and how the model extends to multivariate inputs.
- [ML02-012] How do you interpret the coefficients of a linear regression model?
- [ML02-013] What is the role of the intercept term in a linear regression model?
- [ML02-014] Why do we minimise squared error? Under what assumption is OLS the maximum likelihood estimator?
- [ML02-015] Derive the closed-form normal equation solution for OLS. When does it fail or become impractical?
- [ML02-016] Compare the normal equation with gradient descent for fitting linear regression in terms of cost and scalability.
- [ML02-017] What are the p-value, coefficient and R-squared in a linear regression output, and what does each tell you?
- [ML02-018] How is hypothesis testing used on linear regression coefficients?
- [ML02-019] What is the difference between R-squared and adjusted R-squared, and can R-squared be negative?
- [ML02-020] What is the difference between a confidence interval and a prediction interval in linear regression?
- [ML02-021] How do you handle categorical predictors in linear regression, and what is the dummy variable trap?
- [ML02-022] How can you model a non-linear relationship using linear regression?
- [ML02-023] Your target is strictly positive and right-skewed, and linear regression predicts negative values. What would you do?
- [ML02-024] Compare MSE, MAE and Huber loss for regression. When would you prefer each?

## Assumptions and diagnostics
- [ML02-025] What are the assumptions of linear regression?
- [ML02-026] What is homoscedasticity, and why is it important? What can you do if it is violated?
- [ML02-027] What does normality of residuals mean, and is it needed for fitting or only for inference?
- [ML02-028] Why does autocorrelation of errors matter in linear regression, and how would you detect it?
- [ML02-029] How do you use residual plots to diagnose a misspecified linear model?
- [ML02-030] What are leverage and influential points? How do outliers affect OLS, and how would you detect them (e.g. Cook's distance)?
- [ML02-031] State the Gauss-Markov theorem. Which assumptions does it need and what does it guarantee?
- [ML02-032] Your linear model has high R-squared on training data but poor performance on new data. What could be going on?

## Multicollinearity
- [ML02-033] What is multicollinearity and how can it affect a regression model?
- [ML02-034] How do you check for multicollinearity in regression models?
- [ML02-035] Does multicollinearity hurt predictive accuracy, or only coefficient interpretation?
- [ML02-036] You run linear regression on different subsets of your data and the beta for one variable varies wildly. What could be the issue?
- [ML02-037] Several predictors correlate positively with the response, yet one gets a negative weight in multiple regression. What could cause this?
- [ML02-038] Your linear regression fails and reports infinitely many best estimates for the coefficients. What could be wrong?
- [ML02-039] Explain collinearity: how is it possible to get a negative coefficient in a generalized linear model for a positively related predictor?
- [ML02-040] What happens to logistic regression coefficients and their confidence intervals when two predictors are highly correlated?
- [ML02-041] What are the options for dealing with multicollinearity (dropping features, PCA, regularization)? What are the tradeoffs?
- [ML02-042] Why does ridge regression fix a singular or ill-conditioned X-transpose-X matrix?

## Regularized linear models and GLMs
- [ML02-043] What are ridge, lasso and elastic net regression, and how do their penalties differ?
- [ML02-044] Why does L1 regularization produce sparse solutions while L2 does not? Explain geometrically.
- [ML02-045] What is the Bayesian interpretation of ridge and lasso regression?
- [ML02-046] Given a group of highly correlated features, how do lasso and ridge behave differently?
- [ML02-047] Why must you standardise features before applying a regularized linear model?
- [ML02-048] How do you choose the regularization strength lambda?
- [ML02-049] What is a generalized linear model? Explain its random component, linear predictor and link function.
- [ML02-050] What is the role of the link function, and what is a canonical link?
- [ML02-051] When would you use Poisson regression, and what do you do when the data is overdispersed?
- [ML02-052] Which GLM would you choose to model positive, right-skewed insurance claim amounts, and why?
- [ML02-053] Why are linear regression, logistic regression and Poisson regression all GLMs?

## Logistic regression
- [ML02-054] What is logistic regression, when is it used, and how does it differ from linear regression?
- [ML02-055] Why shouldn't we use linear regression for a binary classification problem?
- [ML02-056] What is the sigmoid function and why is it important in logistic regression?
- [ML02-057] What is the logit function in logistic regression?
- [ML02-058] How is logistic regression used for classification, and how do you choose the decision threshold?
- [ML02-059] Is logistic regression a linear model? Why or why not?
- [ML02-060] Explain logistic regression, its cost function (log loss) and how it is derived from maximum likelihood.
- [ML02-061] Why can't we use mean squared error as the loss for logistic regression?
- [ML02-062] What are odds and the odds ratio, and how do you interpret logistic regression coefficients through them?
- [ML02-063] How should the probability outputs of logistic regression be interpreted? Are they well calibrated?
- [ML02-064] What are the assumptions of logistic regression?
- [ML02-065] How does logistic regression perform feature selection?
- [ML02-066] Can logistic regression handle more than two classes? Compare one-vs-rest with softmax regression.
- [ML02-067] Derive the gradient of the logistic regression log loss with respect to the weights.
- [ML02-068] What happens to logistic regression if the classes are perfectly separable? How do you fix it?
- [ML02-069] How does Newton's method (IRLS) compare with gradient descent for fitting logistic regression?
- [ML02-070] How does the regularization parameter C in logistic regression implementations relate to L2 penalty strength?
- [ML02-071] How can you get a non-linear decision boundary from logistic regression?
- [ML02-072] Explain linear discriminant analysis and how it relates to logistic regression.
- [ML02-073] What are the assumptions of LDA versus QDA, and when would you prefer each over logistic regression?

## Naive Bayes
- [ML02-074] What is the Naive Bayes classifier and how does it work?
- [ML02-075] Explain Bayes' theorem and how it applies to Naive Bayes.
- [ML02-076] What is the naive assumption in Naive Bayes, and what does class conditional independence mean?
- [ML02-077] Why does Naive Bayes often perform reasonably well even though its independence assumption is violated?
- [ML02-078] What are the types of Naive Bayes classifiers (Gaussian, Multinomial, Bernoulli), and when would you use each?
- [ML02-079] How does Naive Bayes handle categorical and numerical features?
- [ML02-080] Why is Naive Bayes a good choice for text classification, and how would you apply it to spam detection?
- [ML02-081] Why do we use log probabilities in Naive Bayes computation?
- [ML02-082] What role does Laplace smoothing play in Naive Bayes, and what happens without it?
- [ML02-083] How would you deal with missing values in a Naive Bayes classifier?
- [ML02-084] Can Naive Bayes be used for regression? Why or why not?
- [ML02-085] What are the advantages and disadvantages of Naive Bayes?
- [ML02-086] How interpretable is Naive Bayes compared to other classifiers?
- [ML02-087] What happens to Naive Bayes if you duplicate a highly informative feature several times?
- [ML02-088] Why are Naive Bayes probability estimates usually poorly calibrated even when its classifications are accurate?
- [ML02-089] Compare Naive Bayes and logistic regression as generative and discriminative models. How do they behave with small versus large training sets?
- [ML02-090] Continuous features in your data are clearly not Gaussian. How would you adapt Naive Bayes?

## k-Nearest Neighbors
- [ML02-091] How does the k-nearest neighbors algorithm classify a data point?
- [ML02-092] How can kNN be used for regression?
- [ML02-093] How do you choose k and a distance metric for kNN?
- [ML02-094] How does the value of k affect the bias-variance tradeoff in kNN?
- [ML02-095] What are the pros and cons of kNN?
- [ML02-096] In what situations is kNN not an ideal choice?
- [ML02-097] How does the choice of distance metric affect kNN performance?
- [ML02-098] What is the effect of feature scaling on kNN?
- [ML02-099] How does the curse of dimensionality affect kNN?
- [ML02-100] How does kNN handle multiclass problems and tied votes?
- [ML02-101] What is the difference between weighted kNN and standard kNN?
- [ML02-102] How does class imbalance affect kNN, and what can you do about it?
- [ML02-103] Can kNN be used for feature selection? If so, how?
- [ML02-104] How do you apply kNN to data with categorical or mixed-type features?
- [ML02-105] What is the training and prediction cost of kNN? How can you speed up neighbour search (KD-trees, approximate NN)?
- [ML02-106] What is the training error of 1-NN, and why does that make it prone to overfitting?
- [ML02-107] How do k-means and k-nearest neighbors differ?

## Support vector machines: margins and optimisation
- [ML02-108] Explain how a support vector machine finds its decision boundary. What does a kernel SVM add?
- [ML02-109] What is a hyperplane in SVM?
- [ML02-110] What is a large margin classifier, and why is SVM an example of one?
- [ML02-111] What is the maximum margin classifier, and how is the margin width related to the weight vector?
- [ML02-112] What are support vectors and why are they important?
- [ML02-113] What is the difference between linear and non-linear SVM?
- [ML02-114] What is a soft margin in SVM and why is it used?
- [ML02-115] Describe the objective function of the SVM.
- [ML02-116] Explain the hinge loss function and how it differs from log loss.
- [ML02-117] What is the role of Lagrange multipliers in SVM, and what do the KKT conditions tell you about support vectors?
- [ML02-118] Explain how the dual problem is solved in SVM optimization and why the dual form is useful.
- [ML02-119] In SVM, why is the weight vector orthogonal to the decision boundary?
- [ML02-120] How can the SVM optimization objective be derived from the logistic regression objective?
- [ML02-121] What is the difference between logistic regression and a linear SVM?
- [ML02-122] Logistic regression versus SVM: when would you use which?
- [ML02-123] How does SVM handle multiclass classification?
- [ML02-124] What are the limitations of SVMs?
- [ML02-125] How do you get probability estimates out of an SVM?
- [ML02-126] What is the training complexity of kernel SVMs, and what would you do with millions of samples?
- [ML02-127] The VC dimension of an RBF-kernel SVM seems infinite, yet SVMs generalize. How is its capacity bounded?
- [ML02-128] How does support vector regression (SVR) work, and what is the epsilon-insensitive loss?

## Kernels and SVM tuning
- [ML02-129] What is the kernel trick in SVM, and why do we use it?
- [ML02-130] What kinds of kernels can be used in SVM? Give examples of each.
- [ML02-131] How do you choose which kernel to use for a given problem?
- [ML02-132] What is a similarity function in SVM, and why is it called that?
- [ML02-133] How are landmarks chosen in a kernel SVM, and how many are used?
- [ML02-134] Can any similarity function be used as an SVM kernel? What does Mercer's condition require?
- [ML02-135] Can the kernel trick be applied to logistic regression? Why is it not used in practice?
- [ML02-136] What is the role of the parameter C in SVM, and how do you choose it?
- [ML02-137] How does C affect the bias-variance tradeoff in an SVM?
- [ML02-138] How does the RBF kernel parameter (gamma or sigma squared) affect bias and variance?
- [ML02-139] Do you need to scale your data before using an SVM? Why?
- [ML02-140] When would you pick a linear kernel over an RBF kernel, for example when features far outnumber samples?
- [ML02-141] Why does the RBF kernel correspond to an infinite-dimensional feature space, and why is that not a computational problem?
- [ML02-142] How would you tune C and gamma for an RBF SVM, and what do under- and overfitting look like on a grid search?
- [ML02-143] Where else besides SVMs can the kernel trick be used (e.g. kernel ridge regression, kernel PCA)?

## Class imbalance at the model level
- [ML02-144] Why is accuracy misleading for a 99:1 imbalanced classification problem, and how does it affect logistic regression training?
- [ML02-145] How do class weights work in logistic regression and SVM? Is this equivalent to oversampling?
- [ML02-146] How would you set per-class penalties C in an SVM when the minority class is costlier to miss?
- [ML02-147] Compare moving the decision threshold with reweighting the loss for imbalanced classification.
- [ML02-148] After undersampling the majority class, how must you correct logistic regression's probabilities and intercept?
- [ML02-149] How do class priors enter Naive Bayes, and how would you adjust them for imbalanced data?
- [ML02-150] What is the case for and against SMOTE versus cost-sensitive learning for linear models?
- [ML02-151] Which of logistic regression, SVM, kNN and Naive Bayes is most sensitive to imbalance, and why?
- [ML02-152] What is a one-class SVM and when would you use it instead of a binary classifier?
