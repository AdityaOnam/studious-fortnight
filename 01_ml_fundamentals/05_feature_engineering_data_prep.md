---
domain: ml
topic: feature_engineering_data_prep
title: Feature engineering and data preparation
tags: [ml, features, data-prep, leakage]
count: 158
---
# Feature engineering and data preparation

## Preprocessing fundamentals and data quality
- [ML05-001] What is data preprocessing in machine learning, and why is it a necessary step before model training?
- [ML05-002] What is data cleaning, and why is it essential before training a model?
- [ML05-003] What are the most common data preprocessing techniques?
- [ML05-004] What data quality issues do you commonly encounter, and how would you detect them?
- [ML05-005] What types of features are commonly used in machine learning, and how does each type affect preprocessing?
- [ML05-006] What are the advantages of plotting and exploring your data before running any analysis?
- [ML05-007] How does data transformation differ from data normalization?
- [ML05-008] What preprocessing steps would you apply before feeding data into a machine learning algorithm?
- [ML05-009] Describe the steps you would take to preprocess data for a linear regression model.
- [ML05-010] How would you design a reusable preprocessing component that behaves identically in training and in serving?
- [ML05-011] Domain experts tell you the sensor data is too noisy to trust. What do you do in the first week of the project?
- [ML05-012] How would you do a first-pass audit of a brand-new tabular dataset before modelling?
- [ML05-013] What is training-serving skew in preprocessing, and how do you prevent it?
- [ML05-014] Why should preprocessing be wrapped in a pipeline object such as scikit-learn Pipeline or ColumnTransformer rather than done ad hoc in a notebook?
- [ML05-015] How do you decide which preprocessing steps are needed for a given model family, such as linear models, trees and neural networks?

## Missing values
- [ML05-016] How do you handle missing values in a dataset (for example with Pandas or scikit-learn)?
- [ML05-017] Name three ways to handle missing or corrupted data in a dataset.
- [ML05-018] What is the difference between imputation and deletion of missing values, and when do you prefer each?
- [ML05-019] How do missing values affect machine learning models, and which models can handle them natively?
- [ML05-020] How do you inspect missing data, and when does the pattern of missingness matter?
- [ML05-021] Describe the pros and cons of mean, median and mode imputation.
- [ML05-022] How does the choice of missing-data strategy depend on why the values are missing (MCAR, MAR, MNAR)?
- [ML05-023] How does K-Nearest Neighbors imputation work, and what are its drawbacks?
- [ML05-024] When would you recommend regression imputation?
- [ML05-025] How does the scikit-learn imputer work, and why must it be fit on training data only?
- [ML05-026] Some predictors are missing for part of your data at both training and prediction time. How do you deal with that?
- [ML05-027] Why can adding a missing-value indicator column improve a model, and when can it hurt?
- [ML05-028] What is the difference between single and multiple imputation, and why does single imputation understate uncertainty?
- [ML05-029] How do tree-based models such as XGBoost handle missing values internally, and how does that compare to imputing beforehand?
- [ML05-030] A feature is 70% missing. How do you decide whether to drop it, impute it or keep the missingness as signal?

## Outliers and noisy data
- [ML05-031] What are outliers, and what impact can they have on a dataset and on a model?
- [ML05-032] How do you handle outliers in your data?
- [ML05-033] Name three ways to make your model robust to outliers.
- [ML05-034] What methods can you use to detect outliers during data preprocessing?
- [ML05-035] How do outliers affect different model families, such as linear models, trees and k-NN?
- [ML05-036] How do you deal with noisy data in machine learning models?
- [ML05-037] You are predicting the probability of a flight delay, but delays of up to 12 hours distort your regression. How do you address this?
- [ML05-038] How do you tell whether an extreme value is a data error, a legitimate rare event or the signal you actually care about?
- [ML05-039] Why can the z-score method fail for outlier detection on skewed data, and what would you use instead?
- [ML05-040] Outlier removal improved your validation score. Why might that be misleading, and what should you check before shipping the change?

## Categorical encoding and scaling
- [ML05-041] How do you handle categorical variables in a dataset (for example in scikit-learn or logistic regression)?
- [ML05-042] What is one-hot encoding, and when should you use it?
- [ML05-043] When should you use label encoding versus one-hot encoding?
- [ML05-044] What is the dummy variable trap, and when does it matter?
- [ML05-045] How do you encode ordinal features, and why is one-hot encoding not always the right choice for them?
- [ML05-046] How would you encode a categorical feature with thousands of distinct values?
- [ML05-047] How does target encoding work, and how can it leak the label if implemented naively?
- [ML05-048] How do you handle categories that appear at inference time but never appeared in training?
- [ML05-049] What is feature scaling, and when do you need it?
- [ML05-050] What is the purpose of normalization and standardization, and how do you apply them (for example with scikit-learn)?
- [ML05-051] How is feature scaling relevant to linear regression?
- [ML05-052] Compare normalization and standardization, and say which models actually need scaled inputs.
- [ML05-053] What is the difference between feature scaling and normalization?
- [ML05-054] Describe the different types of data normalization techniques.
- [ML05-055] How does feature scaling affect the convergence of gradient descent?
- [ML05-056] Why do tree-based models not need feature scaling while k-NN and SVMs do?
- [ML05-057] When would you prefer robust scaling or a log transform over min-max scaling or z-scoring?
- [ML05-058] How do outliers affect min-max scaling versus standardization?

## Feature engineering
- [ML05-059] What is feature engineering, and why is it significant for model performance?
- [ML05-060] What common challenges do you face when engineering features?
- [ML05-061] Why is domain knowledge important when engineering features?
- [ML05-062] How would you create new features from existing ones?
- [ML05-063] How can you extract time-based features from a SQL datetime field for a machine learning model?
- [ML05-064] How can SQL window functions be used for feature engineering?
- [ML05-065] How do you encode cyclical features such as hour of day or day of week, and why is plain integer encoding a poor choice?
- [ML05-066] When are interaction or polynomial features useful, and what are the risks of adding many of them?
- [ML05-067] How would you build aggregate features such as user-level counts or averages for a prediction problem, and how do you keep them point-in-time correct?
- [ML05-068] What is the difference between feature engineering and representation learning? Where does hand-engineering still pay off today?
- [ML05-069] Give an example of a hand-engineered feature that a model could never have learned on its own, and explain why.
- [ML05-070] A newly engineered feature gives a large offline lift but is expensive to compute in production. How do you decide whether to ship it?

## Feature selection and dimensionality
- [ML05-071] Why is feature selection required, and why might it be preferable to use fewer predictors?
- [ML05-072] What is feature selection, and what are the main techniques?
- [ML05-073] How does feature selection differ from feature extraction?
- [ML05-074] What are filter methods in feature selection, and when are they used? Describe two of them.
- [ML05-075] What are wrapper methods in feature selection?
- [ML05-076] What are embedded methods for feature selection, and what are their benefits?
- [ML05-077] What is Recursive Feature Elimination (RFE), and what is it used for?
- [ML05-078] What is forward feature selection, and what are its advantages and disadvantages?
- [ML05-079] What is backward feature selection, and what are its advantages and disadvantages?
- [ML05-080] How does a feature's correlation with the target influence whether you select it?
- [ML05-081] How can you determine which features are the most important in your model?
- [ML05-082] Which feature selection methods can you apply before building a regression model?
- [ML05-083] How do feature selection and feature extraction differ in the context of high-dimensional data?
- [ML05-084] What role does feature selection play in mitigating the curse of dimensionality?
- [ML05-085] You are given an unfeasibly large number of predictors. How do you make the prediction task tractable?
- [ML05-086] How do you deal with sparse, very high-dimensional data?
- [ML05-087] How does multicollinearity affect feature selection and interpretation, and how do you handle it?
- [ML05-088] Why can impurity-based feature importance from random forests be misleading, and what would you use instead?
- [ML05-089] How does L1 regularization act as feature selection, and when does it behave unstably with correlated features?
- [ML05-090] Why must feature selection be performed inside the cross-validation loop?
- [ML05-091] When would you choose PCA over feature selection, and what do you lose in interpretability?
- [ML05-092] How would you check that a selected feature subset is stable across different samples of the data?

## Data splitting, sampling and leakage
- [ML05-093] Explain the concept of splitting data into training and test sets, and how you do it in scikit-learn.
- [ML05-094] What is the difference between training, validation and test datasets?
- [ML05-095] Why do we need three splits of the data, and how do you split into train, validation and test sets?
- [ML05-096] When would you use a stratified split, and what problem does it solve?
- [ML05-097] How do you split data for time series or any data where the future must not inform the past?
- [ML05-098] When must you split by group (for example by user or patient) rather than by row?
- [ML05-099] What sampling methods exist, such as random, stratified, reservoir and importance sampling, and when is each used?
- [ML05-100] What is the difference between probability and non-probability sampling, and what biases does each introduce?
- [ML05-101] What is selection bias in training data collection, and how can it silently ruin a model?
- [ML05-102] You have been tuning against the same test set for months. What has happened to your estimate, and how do you recover a trustworthy one?
- [ML05-103] What is data leakage, and how do you prevent it during preprocessing?
- [ML05-104] Why must scaling statistics and imputation values be computed on the training split only?
- [ML05-105] What is data leakage? Give three subtle examples and explain how you would detect them.
- [ML05-106] How does k-fold cross-validation make preprocessing leakage worse when done naively?
- [ML05-107] When the same user appears in both the training and validation splits, how does that failure show up in the metrics?
- [ML05-108] What is target leakage, and how do you decide whether a feature will actually be available at prediction time?
- [ML05-109] How does leakage appear in time series problems, and how do you avoid it?
- [ML05-110] A teammate wants to ship a new feature purely because it lifts held-out AUC by six points. What do you check first?
- [ML05-111] An assistant's fix lifted validation accuracy from 81% to 96%. What do you check before believing it?
- [ML05-112] Your model gets 0.99 AUC on a fraud problem. Walk me through your audit.
- [ML05-113] What problems arise if the test data distribution differs significantly from the training distribution, and how does distribution shift affect a deployed model?
- [ML05-114] How would you detect covariate shift between your training data and live data?
- [ML05-115] A feature has suspiciously high importance and your model is nearly perfect offline but mediocre online. How do you find the leak?

## Imbalanced data
- [ML05-116] What is an imbalanced dataset, and what are some ways to deal with it?
- [ML05-117] Why is accuracy a misleading metric on imbalanced data?
- [ML05-118] How do you handle imbalanced classes in a classification problem?
- [ML05-119] What strategies does scikit-learn (or imbalanced-learn) provide for handling imbalanced datasets?
- [ML05-120] How do you deal with imbalanced data in practice, and which evaluation metrics do you switch to?
- [ML05-121] How do you choose among the techniques for handling imbalanced datasets?
- [ML05-122] How does SMOTE generate synthetic samples, and what are its limitations?
- [ML05-123] Why must resampling be applied only to the training folds and never before the train/test split?
- [ML05-124] Compare class weights, oversampling and undersampling. When would you choose each?
- [ML05-125] When is undersampling actually preferable?
- [ML05-126] Your fraud dataset is 0.5% positive. Walk me through your strategy for handling the imbalance.
- [ML05-127] Can SMOTE be applied directly to categorical features, and what would you do instead?
- [ML05-128] How do you tune the decision threshold for an imbalanced problem, and why is this often better than resampling?
- [ML05-129] How do you handle extreme class imbalance in rare-event detection, such as a child running into the road?
- [ML05-130] How would you compare ROC-AUC with PR-AUC on a heavily imbalanced dataset?
- [ML05-131] You oversampled the minority class and now the predicted probabilities are inflated. Why, and how do you correct them?
- [ML05-132] When would you reframe an extremely imbalanced problem as anomaly detection instead of classification?

## Data augmentation and limited labels
- [ML05-133] What is data augmentation, and what techniques are commonly used?
- [ML05-134] What is the difference between augmentation for images, text and tabular data?
- [ML05-135] Why must augmentation be applied only to the training set, and how can augmenting before the split cause leakage?
- [ML05-136] When does data augmentation hurt?
- [ML05-137] How would you approach building an AI feature when you have very limited labeled data?
- [ML05-138] How do transfer learning, semi-supervised learning and weak supervision help when labels are scarce?
- [ML05-139] What are the risks of training on synthetic data generated by a model?
- [ML05-140] You have 10M unlabelled examples and a budget for 20k labels. How do you spend it?
- [ML05-141] Your uncertainty sampling in active learning keeps surfacing the same ambiguous case. What does that tell you about the task rather than the model?

## Labeling and annotation quality
- [ML05-142] How would you measure inter-annotator agreement before committing to an ML project?
- [ML05-143] When is a noisy label set still good enough to build on?
- [ML05-144] About 10% of your training labels are wrong. What happens to the model, and what do you do about it?
- [ML05-145] A network confuses pugs and pit bulls and some training labels are wrong. How do you modify the model and the data?
- [ML05-146] Inter-annotator agreement (Cohen's kappa) on your labeling task is 0.55. What does that tell you, and what do you do next?
- [ML05-147] Experts disagree with each other on 20% of the golden set. What do you do?
- [ML05-148] What makes good labeling guidelines, and how do you iterate on them with annotators?
- [ML05-149] What happens in an annotation pipeline when a new task type launches and there are no gold tasks yet?
- [ML05-150] How would you auto-label a large fleet dataset, and what quality controls would you put on it?
- [ML05-151] How do you decide between expert annotators and crowd workers for a labeling task, considering cost and quality?
- [ML05-152] How can you automatically find likely mislabeled examples in a training set?
- [ML05-153] How would you distinguish a genuinely hard example from a mislabelled one in your high-loss bucket?
- [ML05-154] Annotators have no ground truth because the tasks are subjective preference judgments. How do you measure and improve label quality?
- [ML05-155] Inter-annotator kappa is 0.45 on a task the customer insists is objective. Walk through your diagnosis. When would you fire an annotator versus retrain them?
- [ML05-156] How do you estimate the true error rate of 10M model-generated labels from an audit sample, and how big does the sample need to be?
- [ML05-157] Some annotators are pasting your tasks into an LLM and submitting the output. How do you detect and handle it?
- [ML05-158] How do you estimate what fraction of already-delivered annotation data is contaminated by LLM-generated content?
