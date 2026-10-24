---
domain: ml
topic: probability_statistics_ab_testing
title: Probability, statistics and A/B testing
tags: [statistics, probability, ab-testing, bayes]
count: 124
part: 1/2
---
# Probability, statistics and A/B testing (part 1)

## Probability fundamentals
- [ML08-001] What is probability, and how is it used in machine learning?
- [ML08-002] Define sample space and event, and give a simple example of each.
- [ML08-003] What is a random variable, and how do discrete and continuous random variables differ?
- [ML08-004] What does it mean for two events to be independent, and how is that different from being mutually exclusive?
- [ML08-005] Let A and B be events with P(A) = 0.6 and P(B) = 0.7. Can these two events be disjoint?
- [ML08-006] What are joint, marginal and conditional probabilities, and how do you compute the marginal and conditional from a joint distribution?
- [ML08-007] State the chain rule of conditional probabilities and say where it is used in ML.
- [ML08-008] What is the law of total probability, and when would you use it?
- [ML08-009] What are the conditions for independence and for conditional independence of two random variables, and can variables be conditionally independent but not independent?
- [ML08-010] State Bayes' theorem and walk through an example of using it.
- [ML08-011] How is Bayes' theorem used in the Naive Bayes classifier, and why is the "naive" assumption needed?
- [ML08-012] A disease affects 1 in 1000 people and a test has 99% sensitivity and 95% specificity. If a person tests positive, what is the probability they have the disease, and why is it surprisingly low?
- [ML08-013] What is the base-rate fallacy, and how does it show up when evaluating a rare-event classifier?
- [ML08-014] What is the difference between probability and likelihood?
- [ML08-015] Alice has two children and at least one is a girl. What is the probability that both are girls?
- [ML08-016] In the Monty Hall problem, should you switch doors, and why?
- [ML08-017] If P(A|B) is high, what can you say about P(B|A)? Give an example where the two differ greatly.

## Random variables and probability distributions
- [ML08-018] What is the difference between discrete and continuous probability distributions?
- [ML08-019] What is the difference between a probability mass function and a probability density function? Can a PDF value exceed 1?
- [ML08-020] What conditions must a function satisfy to be a valid PMF or PDF?
- [ML08-021] What is the role of the cumulative distribution function, and how does it relate to the PDF?
- [ML08-022] Name the common probability distributions (Normal, Binomial, Poisson, Uniform) and give a use case for each.
- [ML08-023] What are the key characteristics of a normal distribution, and why do we care about it so much?
- [ML08-024] Why is the normal distribution a default choice for a prior or noise model over real numbers?
- [ML08-025] What is the Bernoulli distribution? Derive its expectation and variance.
- [ML08-026] What is the Binomial distribution, and where is it used in ML and statistics?
- [ML08-027] What is the difference between the Bernoulli and Binomial distributions?
- [ML08-028] How does the Poisson distribution differ from the Binomial, and when would you use one over the other?
- [ML08-029] What are the multinoulli (categorical) and multinomial distributions?
- [ML08-030] What is the exponential distribution, and what is its memoryless property?
- [ML08-031] What is the Laplace distribution, and how does it differ from the Gaussian?
- [ML08-032] What is the lognormal distribution, and what kinds of data does it model well?
- [ML08-033] What is the gamma distribution, and how does it relate to the exponential and Poisson distributions?
- [ML08-034] What is the logistic distribution, and how does it relate to logistic regression?
- [ML08-035] What is the beta distribution, and why is it a natural prior for a conversion rate or click-through rate?
- [ML08-036] Which distribution would you use to model the number of support tickets per hour, the time between ticket arrivals, and the share of users who convert?
- [ML08-037] What are the Dirac distribution and the empirical distribution?
- [ML08-038] What is a mixture of distributions, and what are two common examples?
- [ML08-039] Is a Gaussian mixture model a universal approximator of densities?
- [ML08-040] If two random variables are related in a deterministic way, how are their PDFs related?
- [ML08-041] What is a long-tailed distribution? Give examples and explain why they matter for classification and regression.
- [ML08-042] Give an example of a real-world dataset that does not follow a Gaussian distribution.

## Expectation, variance and descriptive statistics
- [ML08-043] What is the difference between descriptive and inferential statistics?
- [ML08-044] What is the difference between a population and a sample?
- [ML08-045] Explain the difference between mean, median and mode, and when you would prefer each.
- [ML08-046] Define expectation, variance and covariance.
- [ML08-047] Is the expectation of a product of random variables the product of their expectations? What is Var(X+Y) in general?
- [ML08-048] What is the difference between correlation and covariance?
- [ML08-049] What do correlation coefficients of +1, 0 and -1 indicate?
- [ML08-050] How do covariance and independence relate? Can two uncorrelated variables be dependent?
- [ML08-051] What is the covariance for a vector of random variables, and what properties does the covariance matrix have?
- [ML08-052] What is the difference between Pearson and Spearman correlation, and when would you use each?
- [ML08-053] Explain correlation versus causation, and give an example of how a spurious correlation can arise.
- [ML08-054] What is Simpson's paradox, and how can it lead to a wrong conclusion from aggregated data?
- [ML08-055] What is a confounder, and how can you control for one in observational data?
- [ML08-056] What are the population mean and the sample mean?
- [ML08-057] What are the population standard deviation and the sample standard deviation?
- [ML08-058] Why does the sample standard deviation divide by N-1 while the population standard deviation divides by N?
- [ML08-059] What is standard error, and how does it differ from standard deviation?
- [ML08-060] What is the formula for the standard deviation of the sample mean, and how does it change as the sample grows?
- [ML08-061] What is skewness? Discuss two ways to measure it.
- [ML08-062] A left-skewed distribution has a median of 60. What can you say about the mean and the mode?
- [ML08-063] How do box plots and histograms differ, and when would you use each?
- [ML08-064] Given the means and standard deviations of two subsets, how do you compute the mean and standard deviation of the combined dataset? Can you extend it to K subsets?
- [ML08-065] If a very tall father has a son, would you expect the son to be taller than, equal to, or shorter than the father on average? What about a very short father?
- [ML08-066] Why is the median more robust than the mean, and how would you detect and handle outliers before computing statistics?

## Sampling, CLT, law of large numbers and the bootstrap
- [ML08-067] What is the Law of Large Numbers, and how can it be used in data science?
- [ML08-068] State the Central Limit Theorem and explain why it matters in statistics and ML.
- [ML08-069] What general conditions must hold for the Central Limit Theorem to apply?
- [ML08-070] Give a real-world example where you would rely on the Central Limit Theorem.
- [ML08-071] When does the CLT fail or converge slowly, for instance with heavy-tailed data such as the Cauchy distribution?
- [ML08-072] What is sampling, and what sampling techniques do you know?
- [ML08-073] How do simple random, stratified and cluster sampling differ, and when would you use stratified sampling?
- [ML08-074] What is selection bias, and how can it be avoided?
- [ML08-075] What is survivorship bias, and how can it distort model evaluation or an analysis?
- [ML08-076] What is the bootstrap method, and how is it used to estimate uncertainty?
- [ML08-077] When does the bootstrap fail or give misleading results?
- [ML08-078] What is the difference between a bootstrap confidence interval and a normal-approximation interval?
- [ML08-079] What are Monte Carlo and Las Vegas algorithms, and how do they differ?
- [ML08-080] What are the union bound and Hoeffding's inequality, and how are they used in ML theory?
- [ML08-081] How would you estimate a proportion to within a margin of error of 2% at 95% confidence, and how many samples do you need?

## Estimation and Bayesian inference
- [ML08-082] What are point estimation and function estimation in ML, and how are they related?
- [ML08-083] Discuss methods you would use to estimate the parameters of a probability distribution.
- [ML08-084] What is an unbiased estimator? Is unbiasedness always desirable in inference, data analysis or predictive modeling?
- [ML08-085] Why is maximum likelihood the preferred estimator in ML?
- [ML08-086] Under what conditions does the maximum likelihood estimator guarantee consistency?
- [ML08-087] Derive the maximum likelihood estimates of the mean and variance of a Gaussian. Is the MLE of the variance unbiased?
- [ML08-088] How does maximum likelihood estimation differ from Bayesian inference?
- [ML08-089] Explain MLE versus maximum a posteriori estimation, and how priors act as regularizers.
- [ML08-090] Why does MLE from a single observation of a rare event give pathological probabilities, and what is the fix?
- [ML08-091] What is a conjugate prior? Show how a beta prior updates after observing k successes in n trials.
- [ML08-092] What is the difference between a Bayesian credible interval and a frequentist confidence interval?
- [ML08-093] How does the influence of the prior change as you collect more data?
- [ML08-094] What are the differences between the Bayesian and frequentist interpretations of probability?
- [ML08-095] What are the differences between the Bayesian and frequentist approaches to machine learning?
- [ML08-096] When would you use Bayesian methods instead of frequentist methods, for example with a small dataset or a large feature set?
- [ML08-097] How do Bayesian methods perform automatic feature selection?
- [ML08-098] What is Fisher information, and what does the Cramer-Rao bound say about estimator variance?
- [ML08-099] You have 5000 people who each rank 10 sushis by saltiness. How would you aggregate the rankings to estimate the true saltiness order?

## Hypothesis testing and p-values
- [ML08-100] What is hypothesis testing, and when is it used in ML?
- [ML08-101] What are the null and alternative hypotheses?
- [ML08-102] What is a p-value, how is it calculated, and what does statistical significance mean?
- [ML08-103] Explain hypothesis testing and the p-value in layman's terms and give a practical application.
- [ML08-104] What are the limitations of p-values, and what do p-values and R-squared not tell you?
- [ML08-105] What are common pitfalls when using statistical significance to judge a model or an experiment?
- [ML08-106] Explain Type I and Type II errors with an example.
- [ML08-107] What is the significance level in a hypothesis test, and how do you choose it?
- [ML08-108] What is the relationship between significance level and confidence level?
- [ML08-109] What is statistical power, and what factors affect it?
- [ML08-110] What is the difference between statistical significance and practical significance?
- [ML08-111] Is a non-significant result evidence that there is no effect? Explain.
- [ML08-112] When would you use a one-sided test instead of a two-sided test?
- [ML08-113] You flip a coin 10 times and see only one head. What is the null hypothesis, and what is the p-value for testing fairness?
- [ML08-114] You are running hundreds of hypothesis tests, each with a t-test. What should you consider?
- [ML08-115] Compare the Bonferroni correction with Benjamini-Hochberg false discovery rate control. When would you use each?
- [ML08-116] What is p-hacking, and how can you guard against it in analysis?
- [ML08-117] What is a permutation test, and when is it preferable to a t-test?
- [ML08-118] What are the z-score and t-score, and when do you use each?
- [ML08-119] What are the differences between a z-test and a t-test?
- [ML08-120] Given a dataset, how do you calculate the t-statistic or z-statistic?
- [ML08-121] Where does the t-test show up in machine learning?
- [ML08-122] Explain the chi-square test, ANOVA and the t-test, and when each is appropriate.
- [ML08-123] How do you assess whether a feature is statistically significant?
- [ML08-124] When would you use a non-parametric test such as Mann-Whitney instead of a t-test?
