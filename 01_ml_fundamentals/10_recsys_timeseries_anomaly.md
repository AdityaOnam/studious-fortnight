---
domain: ml
topic: recsys_timeseries_anomaly
title: Recommender systems, time series, anomaly detection
tags: [recsys, time-series, anomaly-detection]
count: 151
---
# Recommender systems, time series, anomaly detection

## Recommender system fundamentals
- [ML10-001] What is a recommender system, and what business problems does it solve?
- [ML10-002] Explain the difference between collaborative filtering and content-based recommendation.
- [ML10-003] What is the difference between implicit and explicit feedback in recommender systems, and how does each change your modelling choices?
- [ML10-004] What roles do user profiles and item profiles play in a recommender system?
- [ML10-005] Why is a most-popular baseline hard to beat, and why should you build one before any complex recommender?
- [ML10-006] What are the different approaches to implementing recommendation systems?
- [ML10-007] What are the pros and cons of content-based recommendation compared with collaborative filtering?
- [ML10-008] What is a hybrid recommendation system, and when would you use one?
- [ML10-009] What are the main challenges in building recommendation systems?
- [ML10-010] Why are serendipity, novelty and diversity important in recommender systems, and how would you measure them?
- [ML10-011] How can association rule mining be used for recommendations, and where does it fall short compared with collaborative filtering?
- [ML10-012] Clicks and watch time are noisy proxies for preference. How would you convert implicit signals into training labels?
- [ML10-013] A feed recommender optimises engagement but you also care about long-term retention and creator health. How would you define the objective?

## Collaborative filtering and matrix factorization
- [ML10-014] Explain user-based and item-based collaborative filtering.
- [ML10-015] How does the sparsity of the user-item matrix affect collaborative filtering, and how do you cope with it?
- [ML10-016] Compare user-based collaborative filtering, item-based collaborative filtering and matrix factorization.
- [ML10-017] How would you implement a recommendation system using the k-NN algorithm?
- [ML10-018] Which similarity measures (cosine, Pearson, Jaccard) can you use for neighbourhood methods, and when does each break down?
- [ML10-019] Why is item-based collaborative filtering often preferred over user-based when there are far more users than items?
- [ML10-020] How do matrix factorization techniques work in recommendation engines?
- [ML10-021] Describe Singular Value Decomposition (SVD) and its role in recommendations.
- [ML10-022] Why does plain SVD fail on a rating matrix with missing entries, and how do FunkSVD-style methods address this?
- [ML10-023] What is the purpose of Alternating Least Squares (ALS) in recommendation systems?
- [ML10-024] Why do matrix factorization models include user and item bias terms and regularization?
- [ML10-025] How does matrix factorization for implicit feedback (confidence-weighted ALS) differ from factorizing explicit ratings?
- [ML10-026] In implicit feedback data, unobserved items are not true negatives. How do you sample or weight negatives?
- [ML10-027] Compare BPR (pairwise) loss with pointwise squared error for training matrix factorization on implicit feedback.
- [ML10-028] How would you produce embeddings for a new user without retraining the whole factorization model (fold-in)?
- [ML10-029] You have 100 mathletes and 100 math problems, and each mathlete attempts 10 problems. Given who answered which correctly, how would you rank problems by difficulty?
- [ML10-030] Given data on bills and which representatives co-sponsored them, how would you find the representatives most similar to yours and rank who is most bipartisan?

## Retrieval, ranking and deep recommenders
- [ML10-031] Why do large recommenders use a multi-stage pipeline of retrieval, ranking and re-ranking?
- [ML10-032] What are the main approaches to candidate generation in a recommender system, and what are the trade-offs of each?
- [ML10-033] Explain how a two-tower retrieval model is trained and served, and what limits its expressiveness.
- [ML10-034] How does approximate nearest neighbour search (HNSW, IVF-PQ) fit into serving a two-tower model, and what recall versus latency trade-offs does it introduce?
- [ML10-035] Describe the use of deep learning in recommendation systems.
- [ML10-036] How do wide-and-deep or DLRM-style models handle sparse categorical features using embeddings?
- [ML10-037] Compare pointwise, pairwise and listwise learning to rank and when you would use each.
- [ML10-038] How can you use click data as training data for ranking algorithms?
- [ML10-039] How do you use gradient boosted trees for ranking?
- [ML10-040] Explain LambdaRank and LambdaMART, and why optimising NDCG directly is difficult.
- [ML10-041] How would you re-rank a candidate list to improve diversity (for example MMR or DPP) without a large drop in relevance?
- [ML10-042] How would you handle huge ID embedding tables with long-tailed frequency, for example with the hashing trick?
- [ML10-043] How do you choose negatives for two-tower training (in-batch, hard negatives), and what bias does in-batch sampling add?
- [ML10-044] How do sequence models such as GRU4Rec or SASRec differ from matrix factorization, and when are they worth the cost?
- [ML10-045] How would you combine predicted click, like, watch time and purchase probabilities into a single ranking score?
- [ML10-046] When would a graph-based model such as PinSage or LightGCN improve over matrix factorization?

## Cold start, bias and evaluation of recommenders
- [ML10-047] Which offline metrics (precision@k, recall@k, MAP, NDCG) would you use for a recommender, and how do you choose among them?
- [ML10-048] How do cold-start problems affect recommendation systems, and how can they be mitigated?
- [ML10-049] In a short-video recommendation system, how do you handle cold start for brand-new videos with zero engagement?
- [ML10-050] How would you onboard a brand-new user with no history so that the first recommendations are useful?
- [ML10-051] What should you do if a user's taste changes rapidly in a recommender system?
- [ML10-052] Explain position bias in ranking data and how you would debias training from click logs.
- [ML10-053] How do you A/B test recommendation algorithms?
- [ML10-054] Why should you split recommender data by time rather than randomly when evaluating offline?
- [ML10-055] How would you use multi-armed bandits to balance exploration and exploitation in recommendations?
- [ML10-056] What is interleaving, and when is it preferable to a standard A/B test for comparing rankers?
- [ML10-057] Offline NDCG improved by 5% but the online A/B test shows no lift. What could explain this?
- [ML10-058] How do popularity bias and feedback loops arise in recommender systems, and how would you detect and reduce them?
- [ML10-059] How would you use inverse propensity scoring for off-policy evaluation of a new recommendation policy from logged data?
- [ML10-060] How does interference between users or between buyers and sellers in a marketplace threaten the validity of recommender A/B tests?

## Time series fundamentals and ARIMA models
- [ML10-061] What is a time series?
- [ML10-062] How do time series differ from cross-sectional data?
- [ML10-063] Explain the concept of trend in time series analysis.
- [ML10-064] What is an AR (autoregressive) model in time series?
- [ML10-065] Describe an MA (moving average) model and its use in time series.
- [ML10-066] How is time series modelling different from the usual regression problem?
- [ML10-067] What is seasonality in time series analysis, and how do you detect it?
- [ML10-068] What is stationarity, and why is it important in time series analysis?
- [ML10-069] How do you test for stationarity (ADF, KPSS), and what does the null hypothesis of each test imply?
- [ML10-070] Describe the difference between white noise and a random walk.
- [ML10-071] What is autocorrelation, and how is it quantified in time series?
- [ML10-072] Explain the purpose of differencing in time series analysis.
- [ML10-073] What is the role of the ACF and PACF in identifying model orders?
- [ML10-074] Explain the ARMA model.
- [ML10-075] Explain the ARIMA model and its components, and how it extends ARMA.
- [ML10-076] What assumptions does the ARIMA model make?
- [ML10-077] Why does lag selection matter in ARMA/ARIMA models, and how do you choose p and q (AIC, BIC, ACF/PACF)?
- [ML10-078] How does the SARIMA model address seasonality?
- [ML10-079] How do you decompose a series into trend, seasonal and residual parts, and when do you choose additive versus multiplicative?
- [ML10-080] How do you check that a fitted ARIMA model is adequate (residual diagnostics, Ljung-Box test)?
- [ML10-081] How would you handle multiple seasonalities, such as daily and weekly patterns, in a time series model?
- [ML10-082] When would exponential smoothing (Holt-Winters) be preferable to ARIMA?
- [ML10-083] What is spurious regression between two non-stationary series, and how does cointegration relate to it?
- [ML10-084] When does ARIMA fail in practice, and what would you use instead (state-space models, GARCH, VAR, gradient boosting)?

## Forecasting in practice
- [ML10-085] How would you approach a time series forecasting problem from scratch?
- [ML10-086] Why can't you use random k-fold cross-validation on time series, and how would you backtest a forecasting model?
- [ML10-087] Compare MAPE, sMAPE, WAPE and MASE as forecasting metrics. When does each one mislead?
- [ML10-088] When would you choose a global model (gradient boosting or deep learning across many series) over one statistical model per series?
- [ML10-089] How do you build lag, rolling-window and calendar features without leaking future information?
- [ML10-090] Compare recursive and direct strategies for multi-step forecasting.
- [ML10-091] How would you forecast the sales potential of a newly launched product with no history?
- [ML10-092] How would you build a deep learning forecasting model for fashion demand with many new products and short histories?
- [ML10-093] How would you forecast intermittent demand with many zero-sales periods (Croston, zero-inflated models)?
- [ML10-094] How do you decide how often to retrain a forecasting model, and how do you detect concept drift in a time series?
- [ML10-095] How do you produce and evaluate probabilistic forecasts (quantile loss, prediction intervals, calibration) instead of point forecasts?
- [ML10-096] How do you reconcile forecasts across a hierarchy such as SKU, category and region so they add up?
- [ML10-097] Given training data on tweets and their retweets, how would you predict the number of retweets 7 days after posting after seeing only 2 days of data?

## Forecasting system design
- [ML10-098] Design the demand forecasting system for an e-commerce retailer covering millions of items with intermittent sales.
- [ML10-099] Design the forecasting system for grocery demand that handles holidays and promotions.
- [ML10-100] Design the forecasting system for ride demand at airports that accounts for flight arrivals.
- [ML10-101] Design the forecasting system for order volume and courier supply in a delivery marketplace.
- [ML10-102] Design the ML system for making causally valid forecasts when business actions such as pricing change demand.
- [ML10-103] Design the ML system for predicting stock-outs and spotting lost demand when items are unavailable.
- [ML10-104] Design the system to forecast user activity metrics and detect anomalies in them.
- [ML10-105] Design the ML system for forecasting flight prices and recommending when to buy.

## Anomaly and fraud detection
- [ML10-106] What is anomaly detection?
- [ML10-107] What are the main types of anomalies in data (point, contextual, collective)?
- [ML10-108] What are some real-world applications of anomaly detection?
- [ML10-109] Explain the Z-score and how it is used in anomaly detection.
- [ML10-110] How does anomaly detection differ from noise removal?
- [ML10-111] What is the difference between supervised, semi-supervised and unsupervised anomaly detection?
- [ML10-112] What are some common statistical methods for anomaly detection?
- [ML10-113] Why is the robust z-score (median and MAD) often preferred over the mean and standard deviation for flagging outliers?
- [ML10-114] Explain how k-NN is used for anomaly detection.
- [ML10-115] Describe how cluster analysis can be used to detect anomalies.
- [ML10-116] Explain how the Isolation Forest algorithm works.
- [ML10-117] Describe the autoencoder approach to anomaly detection.
- [ML10-118] How does PCA help identify anomalies?
- [ML10-119] How do you handle high-dimensional data in anomaly detection?
- [ML10-120] Compare Local Outlier Factor, one-class SVM and Isolation Forest. When would you pick each?
- [ML10-121] How do you detect anomalies in a seasonal time series without raising false alarms on regular peaks?
- [ML10-122] How do you find an anomaly in a distribution, and how do you investigate whether a trend in it is due to an anomaly?
- [ML10-123] With no labels, how do you choose an alert threshold, and how do you evaluate an anomaly detector?
- [ML10-124] Why is PR-AUC usually more informative than ROC-AUC for rare anomalies and fraud?
- [ML10-125] Your fraud model has 0.99 offline AUC but performs poorly in production. What is the most likely root cause given fraud's label dynamics?
- [ML10-126] How exactly does the selective-labels problem bias naive retraining of a fraud model?
- [ML10-127] How would you build a system to detect anomalies in network traffic?
- [ML10-128] Design the anomaly detection system for equipment such as refrigeration units using sensor data.
- [ML10-129] How would you detect coordinated fraud rings, and how does adversarial adaptation by fraudsters change your modelling and retraining strategy?

## Causal inference and churn targeting
- [ML10-130] Why does correlation not imply causation, and what role do confounders play in observational data?
- [ML10-131] How would you use causal inference to estimate the impact of a product change when a randomized test is not possible?
- [ML10-132] Explain difference-in-differences and the parallel-trends assumption.
- [ML10-133] How does propensity score matching or weighting work, and what are its limitations?
- [ML10-134] When would you use an instrumental variable or a regression discontinuity design?
- [ML10-135] Explain the synthetic control method and when it is appropriate.
- [ML10-136] What is uplift modelling, and how does it differ from predicting an outcome such as churn?
- [ML10-137] Compare the S-learner, T-learner and X-learner for estimating heterogeneous treatment effects.
- [ML10-138] How can interference between users (violating SUTVA) invalidate an A/B test, and what designs mitigate it?
- [ML10-139] Why does an S-learner tend to underestimate treatment effects?
- [ML10-140] Design the ML system for predicting user churn and which customers are likely to upsell.
- [ML10-141] Your churn model has 0.9 AUC and product wants to send retention discounts to the top 5% of predicted churners. Why might that be a bad plan?
- [ML10-142] How would you have caught the mistake of predicting churn instead of persuadability before launch?
- [ML10-143] You have no budget for a randomized holdout when evaluating a retention-discount targeting model. What is your next best option, and what assumption are you buying?
- [ML10-144] How would you design an experiment to measure the incremental effect of a marketing campaign when a holdout group is costly?

## Survival analysis
- [ML10-145] What is survival analysis, and what is censoring?
- [ML10-146] Why is a plain classifier or regression on time-to-event data biased when some subjects are censored?
- [ML10-147] Explain the Kaplan-Meier estimator and how to interpret a survival curve.
- [ML10-148] Explain the Cox proportional hazards model and the proportional hazards assumption.
- [ML10-149] When is survival analysis better than logistic regression for modelling customer churn?
- [ML10-150] How do you evaluate a survival model (concordance index, time-dependent AUC, calibration)?
- [ML10-151] How would you handle time-varying covariates and competing risks in a survival model?
