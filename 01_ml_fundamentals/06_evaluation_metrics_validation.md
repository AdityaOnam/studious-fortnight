---
domain: ml
topic: evaluation_metrics_validation
title: Evaluation metrics and validation
tags: [ml, metrics, auc, cross-validation, interpretability]
count: 160
---
# Evaluation metrics and validation

## Validation fundamentals and data leakage
- [ML06-001] What is model evaluation, and why must a model be evaluated on data it was not trained on?
- [ML06-002] Why do you need a separate validation set in addition to a test set?
- [ML06-003] How do you decide the sizes of the train, validation and test splits, and how does the choice change with dataset size?
- [ML06-004] What is data leakage? Give three examples of how it silently inflates offline evaluation scores.
- [ML06-005] Why must scaling, imputation and feature selection be fit only on the training split? What goes wrong otherwise?
- [ML06-006] How can learning curves help in model evaluation?
- [ML06-007] If you tune against the same validation set many times, what happens to its reliability, and how do you guard against that?
- [ML06-008] How would you put a confidence interval on a test-set metric such as accuracy or F1?
- [ML06-009] How big does a golden evaluation set need to be to trust per-class metrics across 40 classes?

## Cross-validation and validation strategies
- [ML06-010] What is cross-validation, and why is it used?
- [ML06-011] How does k-fold cross-validation work, step by step?
- [ML06-012] What are the advantages and disadvantages of hold-out validation?
- [ML06-013] What are the advantages and disadvantages of k-fold cross-validation?
- [ML06-014] What is leave-one-out cross-validation, and what are its advantages and disadvantages?
- [ML06-015] What are the different types of cross-validation, and when do you use which one?
- [ML06-016] How do you choose K in k-fold cross-validation? What is your favorite K and why?
- [ML06-017] How does the choice of K affect the bias and variance of the cross-validation estimate?
- [ML06-018] What is stratified cross-validation and when should you use it?
- [ML06-019] When do you need group-aware cross-validation, for example with many rows per user, and what happens if you use plain k-fold?
- [ML06-020] Where in a cross-validation pipeline should you apply oversampling such as SMOTE, and why?
- [ML06-021] Walk me through train/validation/test splits. When do you use cross-validation, and when is it a bad idea?
- [ML06-022] What is nested cross-validation for?
- [ML06-023] After choosing a model with cross-validation, should the final model be retrained on all the data? Why or why not?
- [ML06-024] Two models have cross-validated scores of 0.81 and 0.82. How do you decide whether the difference is real?
- [ML06-025] What goes wrong when you validate a model on time-ordered data, and how do you do it properly?
- [ML06-026] Your walk-forward validation folds show wildly different scores. What does that tell you and what do you report to stakeholders?
- [ML06-027] How do delayed fraud labels, for example chargebacks arriving 60 days later, change your evaluation?
- [ML06-028] How do you evaluate a model change when labels are policy-dependent and reviewers disagree about 15% of the time?

## Classification metrics
- [ML06-029] What is a confusion matrix, and how do you derive accuracy, precision, recall, specificity and F-score from it?
- [ML06-030] Define precision, recall, F1-score and accuracy.
- [ML06-031] What are sensitivity and specificity, and how do they relate to recall and the false positive rate?
- [ML06-032] What metrics would you use to evaluate a classifier?
- [ML06-033] Why is accuracy not always the best metric, and when would you use other metrics instead?
- [ML06-034] Give a concrete case where 99% accuracy means the model is useless.
- [ML06-035] Discuss the precision/recall trade-off. When would you prioritise one over the other?
- [ML06-036] Is it better to have too many false positives or too many false negatives?
- [ML06-037] Why is F1 the harmonic mean rather than the arithmetic mean of precision and recall?
- [ML06-038] What is the F-beta score, and how do you choose beta?
- [ML06-039] Your model's precision is 0.95 but the product team is unhappy. What would you check?
- [ML06-040] You have two models with 85% and 82% accuracy. Which do you pick?
- [ML06-041] How do you choose among accuracy, precision, recall and F1 on an imbalanced dataset?
- [ML06-042] What error metric would you use for a binary classifier? What changes if the classes are imbalanced, or if there are more than two classes?
- [ML06-043] What metrics would you use for a multi-class problem, and how do you extend precision, recall and ROC to it?
- [ML06-044] How do micro- and macro-averaged metrics differ, especially on an imbalanced multiclass problem?
- [ML06-045] What evaluation metrics can be used for multi-label classification?
- [ML06-046] Why is averaging per-batch F1 scores wrong, and how should F1 be computed over a dataset?
- [ML06-047] When are Matthews correlation coefficient or balanced accuracy better than F1 or accuracy?
- [ML06-048] How do you evaluate a classifier when false positives and false negatives have very different business costs?

## ROC, precision-recall curves and thresholds
- [ML06-049] What is the ROC curve, what is AUC, and how is it interpreted?
- [ML06-050] What is the probabilistic interpretation of AUC?
- [ML06-051] Explain precision and recall. How do they relate to the ROC curve?
- [ML06-052] What does the area under the precision-recall curve capture, and what is its baseline for a random classifier?
- [ML06-053] ROC-AUC vs PR-AUC: what does each measure, and why does ROC-AUC look deceptively good on imbalanced data?
- [ML06-054] Why is linear interpolation between points on a precision-recall curve invalid?
- [ML06-055] Your ROC-AUC improved but your PR-AUC dropped. What happened?
- [ML06-056] Two models have ROC curves that cross. How do you decide which is better for your use case?
- [ML06-057] How do you extend ROC curves and AUC to a multi-class problem?
- [ML06-058] How do you choose the final operating threshold for production?
- [ML06-059] If a false negative costs 20 times a false positive, how would you choose the decision threshold?
- [ML06-060] In a fraud-detection system, the ops team's review capacity halves. What changes in your metric and threshold?
- [ML06-061] Class prevalence in production shifts from 1% to 3%. Which metrics and thresholds are affected, and which are not?

## Regression metrics
- [ML06-062] What are the common metrics for evaluating a regression model?
- [ML06-063] What are MSE and RMSE, and how are they used in regression?
- [ML06-064] What is the difference between MAE, MSE and RMSE?
- [ML06-065] When would you prefer MAE over RMSE, especially when the data has outliers?
- [ML06-066] Why does minimizing squared error target the conditional mean while minimizing absolute error targets the median?
- [ML06-067] Explain R-squared and adjusted R-squared.
- [ML06-068] What is the difference between explained variance and R-squared?
- [ML06-069] What is R2? What other metrics could be better than R2, and why?
- [ML06-070] How can R-squared be negative on a held-out set, and what does that tell you?
- [ML06-071] What problems does MAPE have, and what alternatives would you use for targets near zero?
- [ML06-072] How do you compare two regression models?
- [ML06-073] How would you validate a predictive model of a quantitative outcome that you built with multiple regression?
- [ML06-074] What do residual plots tell you about a regression model that a single summary metric hides?

## Calibration and probabilistic metrics
- [ML06-075] What is log loss, and why does it punish confident wrong predictions so heavily?
- [ML06-076] When would you use log loss instead of accuracy?
- [ML06-077] When would you use the Brier score deliberately?
- [ML06-078] What does it mean for a classifier to be calibrated? How do you measure and fix miscalibration?
- [ML06-079] How do you read a reliability diagram, and what does expected calibration error measure?
- [ML06-080] Compare Platt scaling and isotonic regression for calibration. When would you use each?
- [ML06-081] Why is isotonic regression risky with sparse segments?
- [ML06-082] How would you get calibrated probabilities out of a boosted tree model?
- [ML06-083] Why does temperature scaling leave accuracy and AUC unchanged?
- [ML06-084] How does class imbalance interact with calibration under resampling?
- [ML06-085] Can a model have a high AUC and still be badly calibrated? When does that matter?
- [ML06-086] How would you assess the goodness-of-fit of a logistic regression model?
- [ML06-087] What is normalized cross entropy and why is it used to evaluate ads click prediction models?

## Ranking, recommendation and clustering metrics
- [ML06-088] Which metrics would you use to evaluate a recommendation system?
- [ML06-089] When would you prefer Precision@k and Recall@k, and why do they fail to capture ranking quality?
- [ML06-090] Explain Mean Reciprocal Rank and describe a situation where it is the right metric.
- [ML06-091] Explain mean average precision for ranked retrieval and when binary relevance makes it appropriate.
- [ML06-092] Explain DCG and nDCG, why the log discount is used, and when graded relevance calls for nDCG.
- [ML06-093] Why is raw DCG not comparable across queries, and how does normalization fix this?
- [ML06-094] How would you choose between offline ranking metrics for a system with binary versus graded relevance?
- [ML06-095] Why is AUC a poor proxy for the quality of the top of a ranked list?
- [ML06-096] How does position bias distort click-based relevance labels, and how does it affect offline ranking metrics?
- [ML06-097] Beyond relevance, what metrics such as coverage, diversity or novelty would you track for a recommender, and why?
- [ML06-098] How do you evaluate an unsupervised learning model?
- [ML06-099] How do you evaluate a clustering algorithm?
- [ML06-100] What does the silhouette score measure, and when can it mislead?
- [ML06-101] What is the difference between internal and external clustering validation, for example silhouette versus adjusted Rand index?

## Offline vs online evaluation
- [ML06-102] Your offline metric improved but the online A/B test did not. Enumerate the reasons this happens and how you would tell them apart.
- [ML06-103] Your ads CTR model shows a 2% offline AUC gain, but the online A/B is revenue-neutral with worse calibration. What is going on, and what do you do?
- [ML06-104] Your model hits 0.87 AUC offline, you launch it, and the business metric does not move. Debug it.
- [ML06-105] If online AUC matches offline and the intervention is randomized but the business metric still does not move, what explanation is left, and how do you quantify it?
- [ML06-106] Your offline Recall@10 improves 8 points but the A/B test is flat. What are the likely explanations?
- [ML06-107] Your offline nDCG improved but online engagement did not. What are possible reasons?
- [ML06-108] Why is click-through rate an imperfect online metric for search or recommendation quality?
- [ML06-109] What is the difference between conversion rate, bounce rate, engagement rate and time spent, and when is each appropriate?
- [ML06-110] How would you compute and interpret a revenue lift metric from an online experiment on an ads system?
- [ML06-111] What are prevalence, proactive rate and appeal reversal rate in content moderation, and what does each tell you?
- [ML06-112] Why do PR-AUC and F1 suit harmful content detection better than accuracy?
- [ML06-113] Design the evaluation for a fraud model at 0.1% prevalence, end to end: metrics, thresholding, validation protocol and monitoring.
- [ML06-114] How do guardrail metrics complement a primary metric when deciding whether to ship a model?
- [ML06-115] How would you check that an offline metric actually predicts the online metric you care about?
- [ML06-116] What are shadow deployment and interleaving, and how do they help evaluate a model before a full A/B test?
- [ML06-117] How can you evaluate a new ranking policy offline using logs collected from the old policy?
- [ML06-118] How would you detect that ranking quality regressed for one tenant without being able to read their queries?

## Hyperparameter tuning and model selection
- [ML06-119] What is the difference between parameters and hyperparameters? How do you tune hyperparameters efficiently?
- [ML06-120] What is hyperparameter tuning, and why is it needed?
- [ML06-121] How do you approach hyperparameter tuning, and how do you find the best hyperparameters?
- [ML06-122] Explain grid search vs random search vs Bayesian optimization.
- [ML06-123] Why does random search often beat grid search when only a few hyperparameters matter?
- [ML06-124] Explain TPE (Tree-structured Parzen Estimator) and Bayesian optimization for hyperparameter tuning.
- [ML06-125] In Gaussian-process Bayesian optimization, what do the surrogate model and the acquisition function each do?
- [ML06-126] How do successive halving and Hyperband save compute during hyperparameter search?
- [ML06-127] Why sample the learning rate log-uniformly during hyperparameter search?
- [ML06-128] If you can afford only 20 training runs, how do you allocate them for hyperparameter tuning?
- [ML06-129] Is the number of training epochs a parameter or a hyperparameter, and what about a learned temperature like CLIP's?
- [ML06-130] Why are model selection methods needed?
- [ML06-131] Explain how you select the best model, and describe some criteria for model selection.
- [ML06-132] How do you choose the right evaluation metric for a given problem?
- [ML06-133] How do you compare the performance of different models?
- [ML06-134] How do AIC and BIC support model selection, and how do they differ from cross-validation?
- [ML06-135] How do you weigh a small accuracy gain against latency, cost and maintainability when picking a model?

## Interpretability and explainability
- [ML06-136] What is explainable AI (XAI), and why does it matter?
- [ML06-137] What is the difference between interpretable and explainable models?
- [ML06-138] How does explainability relate to model transparency, and why is it needed in sensitive applications?
- [ML06-139] What challenges arise when implementing explainability in AI systems?
- [ML06-140] What are the trade-offs between model accuracy and explainability?
- [ML06-141] How do model-agnostic methods differ from model-specific methods for explainability? Give an example of each.
- [ML06-142] What techniques would you use to make a model more interpretable?
- [ML06-143] What is feature importance, and how can it help explain model predictions?
- [ML06-144] How does a decision tree support interpretability?
- [ML06-145] How do you interpret the coefficients of a linear model?
- [ML06-146] What role does the Partial Dependence Plot (PDP) play in model interpretation?
- [ML06-147] How do PDP, ICE and ALE plots differ, and why can PDPs mislead with correlated features?
- [ML06-148] What are the advantages and disadvantages of LIME?
- [ML06-149] What is SHAP, and when is it used?
- [ML06-150] What properties make Shapley values a principled attribution method?
- [ML06-151] Compare SHAP and LIME. When would you choose one over the other?
- [ML06-152] Why is TreeSHAP fast while KernelSHAP is expensive?
- [ML06-153] Why can impurity-based feature importance in tree ensembles be misleading, and how does permutation importance differ?
- [ML06-154] Two features are 0.95 correlated and both show near-zero permutation importance. What is going on, and how do you report it?
- [ML06-155] Why might two SHAP tools give different values for the same model?
- [ML06-156] Describe the use of counterfactual explanations in XAI.
- [ML06-157] You have a binary loan-approval classifier and limited access to feature weights. How do you explain a rejection?
- [ML06-158] How can activation maximization be used for neural network interpretability?
- [ML06-159] Do SHAP values or feature importances imply causal effects? How would you caveat them to stakeholders?
- [ML06-160] How would you test whether an explanation method is faithful to the model rather than just plausible to humans?
