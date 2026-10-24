---
domain: ml
topic: unsupervised_clustering_dim_reduction
title: Unsupervised learning: clustering and dimensionality reduction
tags: [ml, clustering, pca, unsupervised]
count: 121
---
# Unsupervised learning: clustering and dimensionality reduction

## Unsupervised learning and clustering basics
- [ML04-001] What is unsupervised learning, and what are the main types of problems it addresses?
- [ML04-002] What is clustering, when do you need it, and what are some common use cases such as data segmentation?
- [ML04-003] How does clustering differ from classification, and why is it considered an unsupervised task?
- [ML04-004] Explain the difference between hard and soft clustering, and give an algorithm for each.
- [ML04-005] Why is clustering considered an ill-defined problem, and what makes one clustering "better" than another?
- [ML04-006] What is the role of the distance metric in clustering, and how do different metrics change the result?
- [ML04-007] When would you prefer cosine distance over Euclidean distance for clustering, for example with text embeddings?
- [ML04-008] Discuss the importance of scaling and normalization in cluster analysis.
- [ML04-009] How would you cluster a dataset with a mix of numerical and categorical features?
- [ML04-010] What are the main challenges associated with clustering high-dimensional data?
- [ML04-011] Why do high-dimensional Euclidean distances concentrate, and what does that do to k-means specifically?
- [ML04-012] You have data on all purchases of customers at a grocery store. How would you cluster the customers into groups, and how would you determine the appropriate number of clusters?

## K-means
- [ML04-013] Describe the k-means algorithm step by step and explain why it is used.
- [ML04-014] What are centroids in k-means, and how are they updated?
- [ML04-015] What objective does k-means optimize, and what is cluster inertia (within-cluster sum of squares)?
- [ML04-016] What is the distortion function in k-means? Is it convex or non-convex?
- [ML04-017] Why does k-means always converge, and why does it not necessarily converge to the global optimum?
- [ML04-018] Why is k-means considered a greedy algorithm?
- [ML04-019] What are some methods for initializing centroids, and how does k-means++ improve on random initialization?
- [ML04-020] What distance metrics can be used in k-means, and why is Euclidean distance tied to the mean as the centroid?
- [ML04-021] What are the main limitations and failure modes of k-means?
- [ML04-022] How does k-means behave with non-spherical clusters or clusters of very different sizes and densities?
- [ML04-023] How do you handle outliers in k-means?
- [ML04-024] Why is feature scaling important for k-means, and what happens if you skip it?
- [ML04-025] Can k-means be used for categorical data? What are the alternatives, such as k-modes or k-prototypes?
- [ML04-026] What is the difference between k-means and k-medoids, and when would you prefer k-medoids?
- [ML04-027] Discuss clustering algorithms that scale to very large datasets, such as mini-batch k-means.

## Choosing k and evaluating clusters
- [ML04-028] How do you decide on the number of clusters k in k-means?
- [ML04-029] What does the elbow method do, and why is it often ambiguous in practice?
- [ML04-030] If the ground truth of a dataset is unknown, how can you determine the most useful number of clusters?
- [ML04-031] What is the silhouette coefficient, and how is it used to assess clustering quality?
- [ML04-032] When does the silhouette score give misleading results, for example on density-based or non-convex clusters?
- [ML04-033] How do you evaluate a clustering model's effectiveness without pre-labelled groups?
- [ML04-034] What evaluation metrics can you use for a clustering problem, and how do you choose between them?
- [ML04-035] What are external clustering metrics such as adjusted Rand index and normalized mutual information, and when can you use them?
- [ML04-036] The silhouette score says k=2, but the product team needs about 10 actionable segments. What do you do?

## Hierarchical, density-based and other clustering
- [ML04-037] How does hierarchical clustering work, how does it differ from k-means, and when would you use it?
- [ML04-038] What is the difference between agglomerative and divisive hierarchical clustering?
- [ML04-039] What are single, complete, average and Ward linkage, and how do they affect the shape of clusters?
- [ML04-040] Explain the basic idea behind DBSCAN. What advantages does it offer over k-means?
- [ML04-041] Compare centroid-based, hierarchical and density-based clustering, and say when DBSCAN is preferable.
- [ML04-042] What do the eps and minPts parameters of DBSCAN mean, and how would you choose them?
- [ML04-043] When does DBSCAN fail, for example with varying density or high dimensions, and how does HDBSCAN address this?
- [ML04-044] How does the Mean Shift algorithm work, and in what situations would you use it?
- [ML04-045] How does spectral clustering work, and when does it outperform k-means?

## Gaussian mixture models and EM
- [ML04-046] What is a Gaussian Mixture Model?
- [ML04-047] What is the difference between a Gaussian Mixture Model and k-means?
- [ML04-048] What are the two steps of the EM algorithm?
- [ML04-049] Describe the EM algorithm intuitively, and explain how it is used to fit a GMM.
- [ML04-050] Discuss the Expectation-Maximization algorithm in general and its application in clustering.
- [ML04-051] What are responsibilities in a GMM, and how are they computed in the E-step?
- [ML04-052] Derive the M-step updates for the means, covariances and mixing weights of a GMM.
- [ML04-053] Why does EM never decrease the likelihood, and why can it still get stuck in a local optimum?
- [ML04-054] When using a Gaussian mixture model, how do you know it is applicable to your data?
- [ML04-055] How do you choose the number of components in a GMM, for example with BIC or AIC?
- [ML04-056] What is the singularity problem in GMM likelihood maximization, and how do you avoid it?

## Dimensionality reduction fundamentals
- [ML04-057] What is dimensionality reduction, and why is it important in machine learning?
- [ML04-058] Explain the curse of dimensionality and how dimensionality reduction helps to overcome it.
- [ML04-059] How can dimensionality reduction help prevent overfitting?
- [ML04-060] When would you use dimensionality reduction in a machine learning pipeline?
- [ML04-061] What is the difference between feature selection and feature extraction?
- [ML04-062] Discuss the difference between linear and nonlinear dimensionality reduction techniques.
- [ML04-063] Can dimensionality reduction be reversed? Why or why not?
- [ML04-064] What is manifold learning, and how does it relate to high-dimensional data analysis?
- [ML04-065] How can you evaluate the performance of a dimensionality reduction algorithm on your dataset?
- [ML04-066] Why must a dimensionality reduction step be fit on the training data only, and what goes wrong if it is not?

## Principal Component Analysis
- [ML04-067] What is PCA, what does it do, and what is its objective?
- [ML04-068] Explain how PCA works step by step and when you would use it.
- [ML04-069] What is the physical or geometric intuition behind PCA?
- [ML04-070] Why is PCA considered an unsupervised technique?
- [ML04-071] What are the pre-processing steps that should be applied before doing PCA?
- [ML04-072] How does the scaling of features affect PCA?
- [ML04-073] Describe the role of the covariance matrix in PCA.
- [ML04-074] What is the role of eigenvectors and eigenvalues in PCA, and how does eigenvalue decomposition yield the components?
- [ML04-075] What is the variance explained by a principal component?
- [ML04-076] How do you determine the number of principal components to keep?
- [ML04-077] What is meant by "loading" in PCA, and how do you interpret it?
- [ML04-078] Why are principal components orthogonal, and does orthogonality always make them interpretable?
- [ML04-079] Derive PCA from the optimization perspective, i.e., as minimization of reconstruction error.
- [ML04-080] Show that maximizing projected variance and minimizing reconstruction error lead to the same principal components.
- [ML04-081] How can PCA be used for noise reduction in data?
- [ML04-082] What are the limitations of PCA when handling nonlinear relationships?
- [ML04-083] Why is PCA sensitive to outliers, and what robust alternatives exist?
- [ML04-084] Does PCA preserve class separability? Give an example where the top component hurts classification.
- [ML04-085] What is the difference between logistic regression and PCA?
- [ML04-086] What is the difference between PCA and Factor Analysis?
- [ML04-087] In what cases would you use vanilla PCA, Incremental PCA, Randomized PCA, or Kernel PCA?
- [ML04-088] How do you run PCA when the number of features is much larger than the number of samples?

## SVD, topic modelling and other linear methods
- [ML04-089] Explain Singular Value Decomposition (SVD) and its relationship with PCA.
- [ML04-090] Why is truncated SVD preferred over PCA for sparse high-dimensional data such as TF-IDF matrices?
- [ML04-091] What does the Eckart-Young theorem say about low-rank approximation, and why does it matter for dimensionality reduction?
- [ML04-092] What is latent semantic analysis, and how does it relate to the SVD?
- [ML04-093] What are the limitations of LSA for topic discovery compared with probabilistic topic models?
- [ML04-094] How does Latent Dirichlet Allocation (topic model) work at a high level, and how is it different from LDA for dimensionality reduction?
- [ML04-095] How would you choose the number of topics and evaluate a topic model, for example with coherence?
- [ML04-096] How does non-negative matrix factorization differ from PCA, and why are its components often more interpretable?
- [ML04-097] How does Linear Discriminant Analysis (LDA) differ from PCA, and when would you use each?
- [ML04-098] What assumptions does LDA make, and how many discriminant components can it produce for C classes?
- [ML04-099] Explain PCA and when you would use it, and compare it with ICA.

## Nonlinear methods and autoencoders
- [ML04-100] Explain the kernel trick in Kernel PCA and when you might use it.
- [ML04-101] Describe t-Distributed Stochastic Neighbor Embedding (t-SNE) and its use cases.
- [ML04-102] What is the difference between t-SNE and PCA, and why do we often run PCA before t-SNE?
- [ML04-103] What is the crowding problem, and why does t-SNE use a Student-t distribution in the low-dimensional space?
- [ML04-104] What does the perplexity parameter in t-SNE control, and how sensitive are results to it?
- [ML04-105] Can you trust distances between clusters or cluster sizes in a t-SNE plot? Why or why not?
- [ML04-106] What is the difference between t-SNE and UMAP for dimensionality reduction?
- [ML04-107] Why can UMAP transform new points while t-SNE cannot?
- [ML04-108] Compare PCA, t-SNE and UMAP. When would you use each, and how do people misread these plots?
- [ML04-109] How is t-SNE used for NLP, for example to visualize word or document embeddings, and what are the pitfalls?
- [ML04-110] Why should you not feed t-SNE output into a downstream clustering or classification model as if it were a faithful embedding?
- [ML04-111] How do autoencoders perform dimensionality reduction?
- [ML04-112] What is a linear autoencoder? Discuss its equivalence with PCA. Which one is better in reconstruction?
- [ML04-113] What is the difference between undercomplete and overcomplete autoencoders, and what regularization is needed for the latter?
- [ML04-114] When would you prefer an autoencoder over PCA for dimensionality reduction, and what do you lose?

## Applied scenarios
- [ML04-115] Why might you apply PCA before k-means, and what can go wrong?
- [ML04-116] How would you use PCA reconstruction error for anomaly detection?
- [ML04-117] You have gene expression data with 20,000 features and 200 samples. How would you explore its structure and find subgroups?
- [ML04-118] You cluster user embeddings weekly and the cluster assignments keep changing. How do you debug and stabilize this?
- [ML04-119] Your k-means clusters are dominated by one feature with a large scale. How do you diagnose and fix it?

## Additional questions
- [ML04-120] Can you describe the K-means clustering algorithm and its limitations?
- [ML04-121] What is Principal Component Analysis (PCA) and how does it address high dimensionality?
