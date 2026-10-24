---
domain: mlsd
topic: ml_system_design_framework_and_case_studies
title: ML system design: framework and case studies
tags: [ml-system-design, recommendation, ranking, ads, fraud]
count: 169
---
# ML system design: framework and case studies

## Interview framework and problem framing
- [MS03-001] What are the typical steps you follow when approaching an ML system design interview question?
- [MS03-002] Walk me through a structured framework for designing a production ML system from problem formulation to monitoring.
- [MS03-003] Why is it important to ask clarifying questions at the start of an ML system design interview, and which ones do you usually ask?
- [MS03-004] An interviewer says "design a system to recommend products" and you have 45 minutes. What is the strongest first move?
- [MS03-005] How do you scope an open-ended ML design prompt in the first five minutes, and what do you explicitly declare out of scope?
- [MS03-006] How do you translate an abstract business problem into a concrete ML problem with defined inputs, outputs and learning category?
- [MS03-007] How do you decide whether a problem needs machine learning at all, or whether a rule or heuristic would win?
- [MS03-008] The prompt is "detect spam in comments", volume is low and a keyword blocklist already catches most of it. What is the strongest senior response?
- [MS03-009] What business, latency, scale and privacy requirements would you pin down before designing any ML system?
- [MS03-010] How do you weigh the cost of data collection, annotation and compute against expected impact when deciding to build an ML solution?
- [MS03-011] Why is it usually right to start an ML project with a heuristic or simple baseline before moving to a complex model?
- [MS03-012] What are the main components of a production ML system beyond the model itself?
- [MS03-013] How would you do a back-of-envelope estimate of QPS, storage and serving cost for a ranking system with 100M daily active users?
- [MS03-014] What are the main differences between ML in research and ML in production regarding objectives, stakeholders, latency and fairness?
- [MS03-015] In a Staff+ ML system design interview with 45 minutes, how should you allocate depth versus breadth compared to a mid-level candidate?
- [MS03-016] Halfway through a 45-minute ML design interview you have spent 20 minutes on feature engineering and not touched serving or monitoring. How do you recover?

## Metrics, evaluation and experimentation
- [MS03-017] How do you choose between offline and online metrics, and how do you reconcile them when they disagree?
- [MS03-018] What are counter (guardrail) metrics, and why do you track them alongside the primary success metric of an ML product?
- [MS03-019] How do you handle trade-offs between competing metrics such as engagement, revenue and user satisfaction in a recommendation system?
- [MS03-020] When would you use NDCG, MAP, AUC or log loss as the offline metric for a ranking or classification system?
- [MS03-021] Your ranker lifts offline NDCG@10 by 4 points and the interviewer asks how you know this helps the business. How do you answer?
- [MS03-022] How do you evaluate user satisfaction in a content recommender when click-through rate alone is misleading?
- [MS03-023] How do you define relevance for a recommender when completed views, watch time, likes and clicks each give different incentives?
- [MS03-024] How do you avoid optimizing for clickbait when the training signal is clicks?
- [MS03-025] Engagement metrics and wellbeing metrics disagree. How do you build a system that resolves that?
- [MS03-026] Your recommendation model is trained on engagement labels. How would you change the training objective, not just the launch gate?
- [MS03-027] A wellbeing guardrail metric regresses, but only for a small, highly engaged cohort. What do you do?
- [MS03-028] How do you design an online A/B test for a new recommendation model, including user allocation, duration and guardrails?
- [MS03-029] When would you use a bandit approach instead of a fixed A/B test for deploying model variants?
- [MS03-030] When would you use interleaving instead of an A/B test to compare two rankers, and what are its limits?
- [MS03-031] Why are standard user-level A/B tests biased in a two-sided marketplace such as ride-hailing, and how would you design the experiment instead?

## Data, labels and features
- [MS03-032] What data needs do you identify at the start of an ML design, and how do you decide which signals are the big actors?
- [MS03-033] How do you obtain labels when natural labels such as clicks exist only for positives, and how do natural labels, explicit feedback and human annotation compare on cost, noise and bias?
- [MS03-034] You propose training a feed model with "click = positive, no-click = negative", and the interviewer pushes back. What is the strongest revision?
- [MS03-035] How do weak supervision and programmatic labeling work, and what are their risks?
- [MS03-036] How do you build a data generation pipeline that joins features and labels for training, and what can go wrong?
- [MS03-037] What are the challenges of building the joiner between impression logs and later user actions such as purchases?
- [MS03-038] How do you handle delayed feedback when conversions arrive hours or days after the impression?
- [MS03-039] How do you mine hard negatives from click logs without poisoning training with position bias?
- [MS03-040] How do you decide which features to build for a problem with users, items, queries and context as actors?
- [MS03-041] How do you represent high-cardinality ID features and text features in a ranking model?
- [MS03-042] What is the difference between static features from a feature store and dynamic features computed at request time, and when do you use each?
- [MS03-043] Why is point-in-time correctness important when building training features from a feature store, and how do you enforce it?
- [MS03-044] How do you split time-correlated data into train, validation and test sets, and what leakage pitfalls do you watch for?
- [MS03-045] Your ranking model shows suspiciously high offline accuracy. How do you hunt for label leakage?
- [MS03-046] How do you handle class imbalance in a production classification system at the data level and the loss level?
- [MS03-047] How can bias in training data and human labeling affect an ML product, and how would you reduce it by design?
- [MS03-048] How do you structure the pipeline between research training and production serving to avoid training-serving skew?

## Models, serving and monitoring
- [MS03-049] How would you structure a funnel of candidate generation, ranking, re-ranking and filtering, and why is it needed?
- [MS03-050] For a 100M-DAU video feed over a 10M-item catalog with a 120 ms p99 latency, why use a two-stage funnel rather than one big ranking model?
- [MS03-051] What factors drive your choice between logistic regression, gradient boosted trees and a deep neural network for a new ranking problem?
- [MS03-052] What are the pros and cons of separate models versus one multi-task model with shared layers and task-specific heads?
- [MS03-053] How would you combine predicted probabilities such as click, like, share and hide into one ranking score?
- [MS03-054] How do you compare batch prediction, online prediction and a hybrid of both for serving an ML model?
- [MS03-055] When would you choose on-device inference over server-side inference, and what constraints does that impose on the model?
- [MS03-056] How do you scale an ML system for both training and serving when traffic grows tenfold?
- [MS03-057] How do you split a latency budget across retrieval, ranking and re-ranking stages in a real-time system?
- [MS03-058] You have a 200 ms latency budget for a personalized ranking service. How would you design the system to meet it?
- [MS03-059] How do you roll out a new ranking model safely using shadow deployment, canary release and A/B testing?
- [MS03-060] What would you log and monitor in a production ML system to detect problems early?
- [MS03-061] How do you detect and respond to covariate shift, label shift and concept drift in production?
- [MS03-062] How often should a production model be retrained, and how do you decide between training from scratch and fine-tuning the previous model?
- [MS03-063] How do you debug an ML model that performs well offline but poorly after launch?
- [MS03-064] How do feedback loops arise in deployed recommendation or ranking models, and how would you mitigate them?
- [MS03-065] How do you balance freshness and diversity against relevance in a ranking system?

## Recommender system fundamentals
- [MS03-066] Why not just use an LLM for everything in a recommendation system?
- [MS03-067] Describe the candidate generation, ranking and re-ranking stages of a recommender and the goal of each.
- [MS03-068] How do you combine content-based and collaborative filtering in a hybrid recommender, in parallel or sequentially?
- [MS03-069] Which algorithms would you combine in a recommender, such as collaborative filtering, logistic regression, GBDT, factorization machines and DNNs?
- [MS03-070] How do recall (candidate generation) strategies reduce latency in a recommender, and how do they interact with ranking?
- [MS03-071] How would you train a two-tower retrieval model for recommendations, and when would it beat matrix factorization?
- [MS03-072] How do you handle position and selection bias in implicit-feedback training data for a recommender?
- [MS03-073] How would you solve the cold start problem for new users and new items in a recommender, for example with trending signals and content features?
- [MS03-074] How do you balance exploration and exploitation in a recommender while measuring the cost of exploring?
- [MS03-075] What business rules and re-ranking constraints do you apply after a ranker, such as freshness, fairness and diversity?
- [MS03-076] Your feed maximizes CTR and engagement climbs, but the catalog collapses into the same popular items for everyone. What is the right fix and where do you apply it?
- [MS03-077] How would you train a recommendation model continuously on real-time feedback at large scale?

## Recommendation case studies
- [MS03-078] Design a video recommendation system for a streaming platform with hundreds of millions of users.
- [MS03-079] Design a real-time recommendation system that reacts to what a user did in the last few minutes.
- [MS03-080] Design the recommendation system for Instagram Reels.
- [MS03-081] What breaks in a short-video recommendation design at 100k QPS, and where do you spend your latency budget?
- [MS03-082] Design a recommendation system for e-commerce products.
- [MS03-083] Design a system that suggests replacement items when an item in an online grocery order is out of stock.
- [MS03-084] Design a system that recommends complementary products, such as completing an outfit or a room.
- [MS03-085] Design a recommendation system for books.
- [MS03-086] Design a music recommendation engine that recommends tracks and playlists from listening history.
- [MS03-087] Design a game recommendation engine for a gaming platform.
- [MS03-088] Design an event recommendation system for a ticketing platform.
- [MS03-089] Why is event recommendation harder than movie recommendation, and how does that change your feature and model choices?
- [MS03-090] Design similar-listing recommendations for a rental marketplace.
- [MS03-091] Design a personalised recommendation system for rental listings using demographics, property metadata, amenities, price, reviews and location.
- [MS03-092] Design a news recommendation system, including content analysis, semantic tags and article features.
- [MS03-093] Predict when a streaming user stops watching a show, and whether they are tired of it or only taking a break.
- [MS03-094] Design a recommender for a second-hand marketplace where each item can be sold only once.

## Feeds and social graph
- [MS03-095] Design a personalised feed ranking system for a social network with billions of users, including the "next post" logic.
- [MS03-096] How would you design the "For You" timeline recommendation of a microblogging platform to respond within about 1.5 seconds?
- [MS03-097] What signals would you use for a feed model: post features, author-user affinity, user history and context?
- [MS03-098] How would you handle new posts with no engagement history in a feed ranking system?
- [MS03-099] How would you incorporate user-author relationship strength into feed ranking?
- [MS03-100] How would you add diversity and ads into a ranked feed without hurting engagement?
- [MS03-101] How would you design a feed ranking service that mixes learned relevance with business constraints such as frequency caps?
- [MS03-102] You work on a social news feed. What are the important metrics, and how would you make the content each person gets more relevant?
- [MS03-103] Design the "People You May Know" friend recommendation system, including job recommendations at professional-network scale.
- [MS03-104] How would you generate friend candidates at a scale of one billion users using friends of friends?
- [MS03-105] How do you avoid recommending popular hub users to everyone in a social graph recommender?
- [MS03-106] Suggest who a user should follow on a microblogging service, handle brand-new users, and name the limits of data-driven recommenders.
- [MS03-107] How would you predict who a user is likely to want to message next in a chat or email app?

## Search ranking and visual search
- [MS03-108] How does Google Search work end to end, from query to ranked results?
- [MS03-109] Design a search system for an e-commerce marketplace.
- [MS03-110] How would you design the system that returns the top ten rental listings for a location search?
- [MS03-111] Describe the stages of a multi-layer search pipeline from query understanding to blending and filtering.
- [MS03-112] What does query understanding include, such as spell checking, expansion, relaxation and intent classification?
- [MS03-113] How do you scale candidate retrieval from billions of documents to thousands using an inverted index and semantic retrieval?
- [MS03-114] Why use a multi-stage ranker with a lightweight first stage and a heavier second stage?
- [MS03-115] What is a blender in search result page construction, and why is it needed?
- [MS03-116] How do you evaluate a search ranker online when clicks are affected by position bias and clickbait?
- [MS03-117] How would you evaluate the relevance of search results at scale without relying only on clicks?
- [MS03-118] You have dozens of ranking signals and a brand-new tenant with zero interaction data. How do you rank, and how do you improve?
- [MS03-119] Design a typeahead query suggestion system for a search box.
- [MS03-120] How would you generate the related searches shown under a search engine query?
- [MS03-121] Build a system that returns images for a text query, as in an image search engine.
- [MS03-122] Design a visual search system that returns visually similar in-catalogue items for an uploaded image.
- [MS03-123] How would you train an image embedding model with contrastive learning, and how do you choose positive and negative pairs?
- [MS03-124] How would you build an approximate nearest neighbor service for billions of image embeddings?
- [MS03-125] Design a text-to-video search system for a video sharing platform.
- [MS03-126] Build text-to-image search over 100M product images. Walk me through the design.
- [MS03-127] A merchandiser complains that "red dress" surfaces orange dresses in text-to-image product search. What is your debug path?

## Ads, notifications and marketplace prediction
- [MS03-128] Design an ad click prediction system.
- [MS03-129] For ad click prediction, how do you collect negative samples and handle the extreme imbalance between clicks and impressions?
- [MS03-130] How would you model user-ad feature interactions in a CTR model, from feature crossing to deep architectures?
- [MS03-131] How do you ensure predicted CTRs are well calibrated when they feed into an ad auction?
- [MS03-132] How does an ad auction combine bids with predicted CTR, and why does a miscalibrated model hurt revenue?
- [MS03-133] How would you handle ad fatigue and negative feedback such as hide or block in ad ranking?
- [MS03-134] How would you continually train a CTR model on a stream of impressions without catastrophic drift?
- [MS03-135] Design a recommendation system for ads on a social platform and an evaluation framework for ads ranking.
- [MS03-136] Design an AI notification system that decides whether and when to send a push notification to each user instead of broadcasting.
- [MS03-137] How would you measure the long-term effect of notifications on retention versus short-term opens and clicks?
- [MS03-138] Every time users unlock their phone, suggest the one app they are most likely to open first with 90% accuracy. How would you do it?
- [MS03-139] An e-commerce company wants to minimize the time customers take to purchase their selected items. What can you do as an ML engineer?
- [MS03-140] Design a customer churn prediction model and choose retention actions.
- [MS03-141] Design uplift modeling to decide which customers should receive a promotion.
- [MS03-142] Design the ETA prediction system for a ride-hailing marketplace. What features, what model, and how do you serve it in under 100 ms?
- [MS03-143] Design a system that estimates food delivery time and shows it to customers at checkout.
- [MS03-144] Design dynamic pricing and surge pricing for a two-sided marketplace and describe the feedback loops that can go wrong.
- [MS03-145] Design a ride matching system for pooled rides in a ride-hailing service.

## Fraud, spam and content moderation
- [MS03-146] Design a fraud detection system for an online platform.
- [MS03-147] Given a dataset of credit card purchases labelled fraudulent or safe, how would you build a fraud detection algorithm end to end?
- [MS03-148] Design the ML system for detecting fraudulent card payments in real time for an online payments processor.
- [MS03-149] Design a fraud-detection system with heavy class imbalance and an adversarial opponent.
- [MS03-150] Design a payment fraud detection system where fraud patterns change quickly and labels arrive weeks late.
- [MS03-151] How do you set the decision threshold for a fraud detection model?
- [MS03-152] Why does a payments fraud system use logistic regression, GBMs and random forests rather than a large transformer?
- [MS03-153] A new merchant joins your payments platform with zero transaction history. How do you score their transactions for fraud on day one?
- [MS03-154] In a fraud detection system, why combine ML with rules instead of using only ML?
- [MS03-155] How do you handle model latency spikes in a real-time fraud detection system?
- [MS03-156] How does a fraud detection system handle coordinated fraud attacks?
- [MS03-157] Design the ML system for detecting fraud using graph relationships between accounts, devices and payment instruments.
- [MS03-158] Design a real-time system that detects account takeover and botnet logins using risk scores and a rule engine.
- [MS03-159] How would you prevent repeat fraudsters who create new accounts after being banned?
- [MS03-160] When your fraud model blocks suspicious transactions you never observe their true label. How do you correct for this selection bias?
- [MS03-161] How would you build a spam detection system for a platform with user accounts and user-generated content?
- [MS03-162] Design a content moderation system.
- [MS03-163] Design a harmful content detection system for a social media platform, for uploads such as text, images and video.
- [MS03-164] Compare early fusion and late fusion for combining text, image and video signals in a content moderation model.
- [MS03-165] How would you support many languages in a harmful content classifier with limited labeled data per language?
- [MS03-166] How do you combine automated detection, user reports and human review in a moderation pipeline?
- [MS03-167] How do you pick thresholds for removing versus demoting content when harm categories have different severity?
- [MS03-168] How do you deal with adversarial users who modify content to evade a deployed moderation model?
- [MS03-169] In a harmful-content detection pipeline, where would you insert an LLM, and for which policy areas is it too slow or expensive?
