---
domain: ml
topic: probability_statistics_ab_testing
title: Probability, statistics and A/B testing
tags: [statistics, probability, ab-testing, bayes]
count: 91
part: 2/2
---
# Probability, statistics and A/B testing (part 2)

## Confidence intervals and prediction intervals
- [ML08-125] What is a confidence interval, and how is it used?
- [ML08-126] How would you explain a confidence interval to an engineer with no statistics background? What does 95% confidence mean?
- [ML08-127] What is the difference between a confidence interval and a prediction interval, and how do you compute each?
- [ML08-128] How are confidence intervals and hypothesis tests related?
- [ML08-129] How does the width of a confidence interval change with sample size, variance and confidence level?
- [ML08-130] How would you compute a confidence interval for a proportion such as a click-through rate?

## A/B testing fundamentals
- [ML08-131] What is A/B testing, and how does it apply to ML products?
- [ML08-132] How would you explain an A/B test, and a linear regression, to an engineer with no statistics background?
- [ML08-133] Explain how you would design and evaluate an A/B test, and how you interpret the p-value.
- [ML08-134] How would you design an A/B test for a website homepage?
- [ML08-135] How do you choose the primary, secondary and guardrail metrics for an experiment, and how do you decide it was successful?
- [ML08-136] How do you calculate the sample size and run time for an A/B test, and what inputs do you need?
- [ML08-137] What is the minimum detectable effect, and how does it affect sample size?
- [ML08-138] In an A/B test, how can you check that assignment to buckets was truly random?
- [ML08-139] What is sample ratio mismatch, and what would you check if you see one?
- [ML08-140] What are the benefits of running an A/A test?
- [ML08-141] When you split a population for an A/B test, what could explain a significant difference between control and variant that is not caused by the change?
- [ML08-142] Briefly explain A/B testing and its common pitfalls.
- [ML08-143] What is the peeking problem, and how do you stop an experiment early without inflating false positives?
- [ML08-144] What are sequential testing and always-valid p-values, and when would you use them?
- [ML08-145] How do you choose the randomization unit for an experiment, and what goes wrong if the analysis unit differs from it?

## Experiment design scenarios
- [ML08-146] How would you conduct an A/B test on an opt-in feature?
- [ML08-147] How would you run an A/B test with many variants, say 20 or more?
- [ML08-148] How would you run an A/B test when the observations are extremely right-skewed?
- [ML08-149] Two experiments that both change the sign-up button must run at the same time. What should you keep in mind?
- [ML08-150] What hazards arise if users can see or sneak a peek at the other bucket in an A/B test?
- [ML08-151] What issues arise if blogs or the press start covering one of your experimental groups?
- [ML08-152] You are Airbnb and want to test whether more photos in a listing increase the chance that a buyer selects it. How would you test this?
- [ML08-153] How would you design an experiment to determine the impact of latency on user engagement?
- [ML08-154] How would you measure the impact of sponsored stories on Facebook News Feed engagement and find the optimal balance with organic content?
- [ML08-155] How do you power an A/B test when only 5% of sessions touch the feature?
- [ML08-156] How would you measure the impact of an AI feature when a holdout group is not politically possible?
- [ML08-157] How would you design a holdback experiment to measure long-term advertiser value rather than next-day revenue?
- [ML08-158] How do you A/B test a new fraud model when the intervention itself changes the labels you observe?
- [ML08-159] How do you run experiments on a marketplace or social network where treatment spills over to control users?

## Analysing experiments and metrics
- [ML08-160] What do you do when the headline metric of an experiment looks great but a guardrail metric moves the wrong way?
- [ML08-161] In an A/B test of a new model your metric is revenue per user, which is heavy-tailed and mostly zero. How does that affect sample size and what would you do?
- [ML08-162] How would you detect a novelty effect in an A/B test rather than assume one?
- [ML08-163] Why does interleaving reach significance faster than an A/B test on the same traffic?
- [ML08-164] What is CUPED or regression adjustment, and how does it increase experiment sensitivity?
- [ML08-165] How do you compute the variance of a ratio metric such as click-through rate per session in an A/B test?
- [ML08-166] What would be good success metrics for an advertising-driven product, a service-driven consumer product, a productivity tool, a MOOC, and a game with in-app purchases?
- [ML08-167] A key metric is moving up or down more than you expect. How would you identify the cause?
- [ML08-168] Growth in the total number of tweets sent has been slow this month. What data would you look at to find the cause?
- [ML08-169] What kinds of services find churn helpful, and how would you calculate it?

## Statistical comparison of models
- [ML08-170] What statistical tests would you use to compare two models?
- [ML08-171] Your new model scores 87.2% on the test set and the incumbent scores 86.5%. Do you ship it?
- [ML08-172] How would you set up the evaluation so that a 0.7 point difference is detectable, and is that a good use of budget?
- [ML08-173] Your test set has 5 examples per user across 200 users. What breaks in a naive bootstrap?
- [ML08-174] Why is a paired test the right choice for comparing two prompt variants or two models on the same examples?
- [ML08-175] How many examples would you need to detect a 3-point improvement in an eval pass rate?
- [ML08-176] How many samples do you need before calling a 3-point drop in an LLM eval pass rate a regression?
- [ML08-177] What is conformal prediction, and how would you use it to put a statistical guarantee on a classifier's or an LLM pipeline's outputs?
- [ML08-178] Why does conformal prediction use an (n+1) correction in the quantile?
- [ML08-179] How would you get conformal prediction coverage that holds per class rather than on average?
- [ML08-180] Traffic shifts after a product launch. What happens to conformal prediction coverage, and how would you detect it?
- [ML08-181] How do you compare two classifiers with cross-validation, and why are naive t-tests on fold scores problematic?

## Dice, cards and counting puzzles
- [ML08-182] If you draw 2 cards from a shuffled 52-card deck, what is the probability of getting a pair?
- [ML08-183] How many ways can you split 12 people into 3 teams of 4?
- [ML08-184] 60 students are randomly split into 3 equal classes. What is the probability that Jack and Jill end up in the same class?
- [ML08-185] On a dating site users pick 5 of 24 adjectives, and two users match if they share at least 4. If Alice and Bob pick at random, what is the probability they match?
- [ML08-186] n applications are put at random into n envelopes addressed to different colleges. What is the expected number that go to the correct college?
- [ML08-187] If you roll a die three times, what is the probability of getting two consecutive threes?
- [ML08-188] You throw ten fair dice. What is the probability that the sum of the top faces is divisible by six?
- [ML08-189] From a deck of 100 cards numbered 1 to 100, you draw two without replacement. What is the probability that one value is double the other?
- [ML08-190] If there are 30 people in a room, what is the probability that everyone has a different birthday?
- [ML08-191] A deck has 40 cards in four colors, 10 of each, numbered 1 to 10. Drawing two without replacement, what is the probability they differ in both color and number?
- [ML08-192] You call 2 UberX and 3 Lyft cars with IID arrival times. What is the probability that all Lyfts arrive first? That all UberX arrive first?
- [ML08-193] What is the expected number of rolls of a fair die until you see a 6?
- [ML08-194] What is the probability that the sum of two fair dice is 7, and what is the expected value of the maximum of the two?

## Coin-flip puzzles and expected values
- [ML08-195] You have a fair coin and a coin with heads probability 3/4. You pick one at random, flip it twice and get two heads. What is the probability you picked the fair coin?
- [ML08-196] You pick a two-headed coin with probability 0.1% or a fair coin with probability 99.9%, and flip 10 heads in a row. What is the probability it is the fair coin?
- [ML08-197] You pick one of a fair and an unfair coin at random, flip it five times and see five tails. What is the probability it is the unfair coin?
- [ML08-198] You and a friend toss a fair coin until HH or TH appears. If HH comes first you win. What is your winning probability?
- [ML08-199] What is the expected number of flips until two heads in a row? Until two tails in a row?
- [ML08-200] On average, how many fair coin flips until you see HHH?
- [ML08-201] How would you estimate by simulation the expected number of flips until HHH, and how many trials do you need for a standard error under 0.01?
- [ML08-202] You flip a coin until heads, and if the first head is on flip n you pay me 2^(n-1) dollars. How much would you pay to play, and why is this paradoxical?
- [ML08-203] Couples keep having children until their first girl. What is the expected gender ratio of the children, and the expected number of children per couple?
- [ML08-204] How can you get a fair coin toss from a coin weighted to land heads more often than tails with unknown bias?
- [ML08-205] How can you generate a random number between 1 and 7 using only a fair die?
- [ML08-206] In any 15-minute interval there is a 20% chance of seeing at least one shooting star. What is the probability of seeing at least one in an hour, and how would you adapt this to a 5-minute airplane example with 15%?
- [ML08-207] Bobo the amoeba produces 0, 1 or 2 offspring with probabilities 25%, 25% and 50%, and each descendant does the same. What is the probability that the lineage dies out?

## Continuous and simulation puzzles
- [ML08-208] You break a stick of length 1 uniformly at random into three parts. What is the probability that the pieces can form a triangle?
- [ML08-209] You pick two random chords of a circle. What is the probability that they intersect?
- [ML08-210] You draw three values from a uniform distribution on [0, 2]. What is the probability that the median is greater than 1.5?
- [ML08-211] A 50-50 mixture of two normals has equal standard deviations. How far apart must the means be for the mixture to be bimodal?
- [ML08-212] Given draws from a normal distribution with known parameters, how can you simulate draws from a uniform distribution?
- [ML08-213] How would you sample from an arbitrary distribution given only a uniform random number generator?
- [ML08-214] What is the expected value of the minimum of two independent uniform [0, 1] random variables?
- [ML08-215] How would you estimate pi with a Monte Carlo simulation, and how does the error shrink with the number of samples?
