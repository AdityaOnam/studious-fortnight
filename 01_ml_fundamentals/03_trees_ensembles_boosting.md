---
domain: ml
topic: trees_ensembles_boosting
title: Decision trees, ensembles, boosting
tags: [ml, trees, ensemble, boosting, xgboost]
count: 138
---
# Decision trees, ensembles, boosting

## Decision tree basics
- [ML03-001] What is a decision tree, and how does it make predictions for classification tasks?
- [ML03-002] What is the difference between classification trees and regression trees?
- [ML03-003] What are the main advantages of decision trees?
- [ML03-004] What are the main limitations of decision trees?
- [ML03-005] Do decision trees require feature scaling or normalization? Why or why not?
- [ML03-006] Walk me through how a decision tree is constructed from a training set using recursive partitioning.
- [ML03-007] Name and describe the common algorithms used to build decision trees, such as ID3, C4.5 and CART.
- [ML03-008] How do decision trees handle both categorical and numerical features when making splits?
- [ML03-009] How are missing values handled by decision trees?
- [ML03-010] Can decision trees be used for multi-output tasks? How?
- [ML03-011] Why are decision trees considered high-variance and unstable learners?
- [ML03-012] Why can a regression tree not extrapolate beyond the range of its training targets, and when does that hurt?
- [ML03-013] Why do decision trees struggle with a linear decision boundary that is not axis-aligned, and how would you mitigate it?
- [ML03-014] How do you explain an individual decision tree prediction to a non-technical stakeholder?
- [ML03-015] What is the time complexity of training and predicting with a decision tree?

## Splitting criteria and impurity
- [ML03-016] Explain the concept of impurity in a decision tree and how it is used to choose splits.
- [ML03-017] Define Gini impurity and explain its role in decision trees.
- [ML03-018] What are entropy and information gain in the context of decision trees?
- [ML03-019] How do Gini impurity and entropy compare in practice, and does the choice matter much?
- [ML03-020] A node has 40 positive and 10 negative samples. Compute its Gini impurity and entropy.
- [ML03-021] How does a regression tree choose its splits, for example using variance reduction or MSE?
- [ML03-022] How does a tree find the best split point for a continuous feature efficiently?
- [ML03-023] What are the different methods for splitting a node, and how does a tree decide when to stop growing?
- [ML03-024] Why does information gain favour features with many distinct values, and how do gain ratio or other methods correct for it?
- [ML03-025] Why is greedy top-down tree building not guaranteed to produce an optimal tree?
- [ML03-026] If instead of searching for the best split we sample a few random splits and pick the best among them, would the tree still work?

## Overfitting, pruning and tree hyperparameters
- [ML03-027] What is the significance of the depth of a decision tree?
- [ML03-028] What are the main hyperparameters of a decision tree model?
- [ML03-029] What is tree pruning and why is it important?
- [ML03-030] How does a decision tree avoid overfitting?
- [ML03-031] What strategies would you use to combat overfitting in tree-based classification models?
- [ML03-032] What is the difference between pre-pruning and post-pruning, and how does cost-complexity pruning work?
- [ML03-033] What would the training accuracy of a fully grown, unpruned decision tree typically be, and what does that tell you?
- [ML03-034] How would you choose min_samples_leaf and max_depth for a decision tree in practice?
- [ML03-035] How would you handle severe class imbalance when training a decision tree?

## Ensemble learning fundamentals
- [ML03-036] What is ensemble learning, and why are ensemble methods powerful?
- [ML03-037] What is a weak learner and how is it used in ensemble methods?
- [ML03-038] What are the advantages of ensemble methods over single models?
- [ML03-039] What is the difference between hard and soft voting classifiers?
- [ML03-040] Why do ensembles typically score higher than their individual models? What if you had many different models predicting the same target?
- [ML03-041] Can you explain the difference between bagging, boosting and stacking?
- [ML03-042] Compare bagging and boosting. Which one mainly reduces variance and which mainly reduces bias?
- [ML03-043] How does ensemble learning help with the bias-variance trade-off?
- [ML03-044] What is a bootstrap sample and how is it used in bagging?
- [ML03-045] How can ensemble learning be used for both classification and regression tasks?
- [ML03-046] What is model stacking, and how do you select the base learners and the meta-learner?
- [ML03-047] Why do ensembles work, and when are they worth the added cost in latency and complexity?
- [ML03-048] Explain the Model Ensemble design pattern and when you would use it.
- [ML03-049] Why must the base models in an ensemble be diverse, and how do you create diversity?
- [ML03-050] In stacking, why must the meta-learner be trained on out-of-fold predictions? What goes wrong otherwise?
- [ML03-051] What is the difference between stacking and blending?
- [ML03-052] Averaging n models, each with variance sigma squared and pairwise correlation rho: what is the variance of the average, and what does it imply for bagging?
- [ML03-053] Can an ensemble ever perform worse than its best single member? When?

## Random forest
- [ML03-054] What is a random forest and how does it work?
- [ML03-055] Why is a random forest often more effective than a single decision tree?
- [ML03-056] What are the main advantages of random forests?
- [ML03-057] What is bagging, and how is it implemented in a random forest?
- [ML03-058] How does a random forest achieve feature randomness, and why does it decorrelate the trees?
- [ML03-059] How does a random forest reduce variance, and why does it overfit less than a single decision tree?
- [ML03-060] How does a random forest make predictions for regression versus classification?
- [ML03-061] What is out-of-bag (OOB) error in a random forest, and how does it compare with cross-validation?
- [ML03-062] What are the key hyperparameters of a random forest, and how do they affect the model?
- [ML03-063] How do you handle missing values in a random forest model?
- [ML03-064] Are random forests biased towards attributes with more levels? Explain.
- [ML03-065] Can random forests handle high-dimensional data without overfitting?
- [ML03-066] Does adding more trees to a random forest cause overfitting? Why or why not?
- [ML03-067] What are the default values of max_features for classification and regression, and why are they chosen?
- [ML03-068] How do highly correlated features affect a random forest's accuracy and its feature importances?
- [ML03-069] How would you train a random forest on a heavily imbalanced dataset?
- [ML03-070] What is the difference between random forest and Extra Trees?
- [ML03-071] How does a random forest differ from AdaBoost?
- [ML03-072] Compare random forest and gradient boosting: how does each work, and what are the advantages and disadvantages of each?
- [ML03-073] A random forest with 500 deep trees is too slow and too large to serve. How would you reduce latency and memory?

## Boosting, AdaBoost and gradient boosting
- [ML03-074] How does boosting improve weak learners, and what are two well-known boosting methods?
- [ML03-075] How does boosting help to reduce bias?
- [ML03-076] Describe the AdaBoost algorithm step by step, including how sample weights and learner weights are updated.
- [ML03-077] Why is AdaBoost sensitive to noisy labels and outliers?
- [ML03-078] Explain what gradient boosting is and how it works.
- [ML03-079] How does gradient boosting differ from AdaBoost, and how do AdaBoost, gradient boosting and XGBoost relate?
- [ML03-080] Why is fitting residuals in gradient boosting equivalent to gradient descent in function space for squared loss? How does this generalize to other losses?
- [ML03-081] In gradient boosting for classification, what does each new tree actually fit?
- [ML03-082] Why are shallow trees or stumps typically used as base learners in boosting?
- [ML03-083] Explain the learning rate (shrinkage) in gradient boosting and its trade-off with the number of trees.
- [ML03-084] What is stochastic gradient boosting, and how do row and column subsampling help?
- [ML03-085] Can boosting overfit? How do you detect and control it compared with bagging?
- [ML03-086] Why is boosting harder to parallelize than bagging, and how do modern libraries work around this?

## XGBoost
- [ML03-087] What is XGBoost and why is it considered an effective machine learning algorithm?
- [ML03-088] How does XGBoost differ from a standard gradient boosting machine (GBM), and what are its advantages over other boosting methods?
- [ML03-089] How does XGBoost differ from random forests, including the computational difference?
- [ML03-090] How does XGBoost handle missing or null values in the dataset?
- [ML03-091] What does regularization mean in XGBoost, and how does it help prevent overfitting?
- [ML03-092] Why does XGBoost use a second-order Taylor expansion of the loss, and what role do the gradient and Hessian play?
- [ML03-093] Explain the XGBoost split gain formula and the roles of the lambda and gamma parameters.
- [ML03-094] What loss functions and objectives does XGBoost support for regression and classification, and how does the objective affect performance?
- [ML03-095] How does XGBoost use tree pruning, and why is it important?
- [ML03-096] Describe the role of shrinkage (learning rate) in XGBoost.
- [ML03-097] What are the core XGBoost parameters you typically tune?
- [ML03-098] Explain the importance of the max_depth parameter in XGBoost.
- [ML03-099] How do you manage the trade-off between learning rate and n_estimators in XGBoost?
- [ML03-100] What is early stopping in XGBoost and how do you implement it correctly?
- [ML03-101] How can XGBoost handle highly imbalanced datasets?
- [ML03-102] How does XGBoost handle the bias-variance tradeoff?
- [ML03-103] What are exact, approximate and histogram-based split finding in XGBoost, and what is sparsity-aware split finding?
- [ML03-104] XGBoost training is too slow on a large dataset. What would you change to speed it up?

## LightGBM and CatBoost
- [ML03-105] What is LightGBM, and how does it differ from other gradient boosting frameworks?
- [ML03-106] What are the advantages of LightGBM over XGBoost or CatBoost?
- [ML03-107] How does LightGBM achieve faster training and lower memory usage?
- [ML03-108] Explain the histogram-based approach used by LightGBM.
- [ML03-109] What is leaf-wise tree growth in LightGBM, and how does it differ from depth-wise growth?
- [ML03-110] What types of boosting or tree learners are available in LightGBM?
- [ML03-111] How does LightGBM deal with overfitting?
- [ML03-112] How do Gradient-based One-Side Sampling (GOSS) and Exclusive Feature Bundling (EFB) contribute to LightGBM's performance?
- [ML03-113] What are feature parallelism and data parallelism in LightGBM?
- [ML03-114] How would you tune the number of leaves and maximum depth of trees in LightGBM, and how are they related?
- [ML03-115] What is the significance of the min_data_in_leaf parameter in LightGBM?
- [ML03-116] Explain the role of the learning rate in LightGBM.
- [ML03-117] Discuss the impact of a large versus small bagging_fraction in LightGBM.
- [ML03-118] How does LightGBM handle categorical features differently from other tree-based algorithms?
- [ML03-119] How does CatBoost handle categorical features differently from other boosting algorithms?
- [ML03-120] Why does CatBoost use ordered target encoding, and what leakage does it prevent?
- [ML03-121] What are CatBoost's ordered boosting and symmetric (oblivious) trees, and what problems do they solve?
- [ML03-122] How would you choose between XGBoost, LightGBM and CatBoost for a new tabular problem?
- [ML03-123] What is DART in gradient boosting, and when would you use it?

## Feature importance, tuning and practice
- [ML03-124] How do you approach tuning hyperparameters in XGBoost or LightGBM?
- [ML03-125] How do impurity-based (gain) importance, split count, permutation importance and SHAP differ for tree models?
- [ML03-126] Why is impurity-based feature importance biased in random forests, and how do you correct for it?
- [ML03-127] Are there differences between continuous and discrete variables when it comes to feature importance in gradient boosting models?
- [ML03-128] How do correlated features distort feature importance in tree ensembles?
- [ML03-129] Why do tree ensembles often beat neural networks on tabular data, and when does that stop being true?
- [ML03-130] How would you encode a high-cardinality categorical feature for a tree-based model?
- [ML03-131] What are monotonic constraints in gradient boosting, and when are they useful?
- [ML03-132] Your gradient boosting model has train AUC 0.99 but validation AUC 0.80. How do you debug it?
- [ML03-133] A feature has suspiciously dominant importance in your boosted model. What could be wrong and how do you check?
- [ML03-134] Are probabilities from random forests and boosted trees well calibrated? How would you fix this?
- [ML03-135] A boosted-tree model trained on past data degrades on future data with shifted feature ranges. Why, and what would you do?
- [ML03-136] How would you train and serve gradient boosted trees on billions of rows?

## Additional questions
- [ML03-137] Is random forest bagging or boosting?
- [ML03-138] Why is boosting a more stable algorithm compared to other ensemble algorithms?
