---
domain: ml
topic: reinforcement_learning
title: Reinforcement learning
tags: [rl, q-learning, policy-gradient, bandits]
count: 107
---
# Reinforcement learning

## RL fundamentals and MDPs
- [ML11-001] What is reinforcement learning, and how does it differ from supervised and unsupervised learning?
- [ML11-002] Define agent, environment, state, action, reward, policy, and return in a reinforcement learning problem.
- [ML11-003] What is an episode, and how do episodic tasks differ from continuing tasks?
- [ML11-004] How do discrete and continuous state and action spaces differ, and how does that affect your choice of RL algorithm?
- [ML11-005] What is a Markov Decision Process, and what is the role of each element in the tuple (S, A, P, R, gamma)?
- [ML11-006] What is the role of a policy in RL, and how do deterministic and stochastic policies differ?
- [ML11-007] What does the discount factor gamma control, and what happens when it is 0, close to 1, or equal to 1 in an infinite-horizon task?
- [ML11-008] Why can't you simply treat RL as supervised learning on the best action at each state?
- [ML11-009] Why is the data in RL not i.i.d., and what problems does that cause for training?
- [ML11-010] What is the credit assignment problem in RL, and which techniques help with delayed rewards?
- [ML11-011] What is a partially observable MDP, and how do practitioners deal with partial observability in deep RL?
- [ML11-012] Give an example of reward hacking (specification gaming) and explain how it arises from a mis-specified reward.
- [ML11-013] When would you prefer an average-reward objective over a discounted-return objective?

## Value functions and Bellman equations
- [ML11-014] What are state-value and action-value functions, and how do they relate to a policy?
- [ML11-015] What is the difference between a value function V, an action-value function Q, and an advantage function?
- [ML11-016] Explain the Bellman expectation and Bellman optimality equations and how the Markov property makes them possible.
- [ML11-017] How does the Bellman optimality equation relate to the Q-learning update?
- [ML11-018] Why are the optimal value function V* and the optimal policy pi* equivalent?
- [ML11-019] What is the difference between policy evaluation and policy improvement, and how do they combine in policy iteration?
- [ML11-020] Compare policy iteration and value iteration. When would you pick one over the other?
- [ML11-021] Why does the Bellman optimality operator converge to a unique fixed point? Explain the contraction argument.

## Monte Carlo and temporal-difference learning
- [ML11-022] Describe the Monte Carlo method for RL. What are first-visit and every-visit MC, and what are its requirements?
- [ML11-023] Compare Monte Carlo and temporal-difference learning in terms of bias, variance, and the need for complete episodes.
- [ML11-024] What does bootstrapping mean in RL, and which methods use it?
- [ML11-025] What is n-step TD and TD(lambda), and how do they interpolate between TD(0) and Monte Carlo?
- [ML11-026] What does dynamic programming need that Monte Carlo and TD methods do not, and why does that limit its use?
- [ML11-027] A TD learner is stable on a tabular problem but diverges after you add a function approximator. Why does this happen?

## Q-learning and SARSA
- [ML11-028] What is Q-learning, and where does it fit in the field of reinforcement learning?
- [ML11-029] What is a Q-table, and when does it stop being practical?
- [ML11-030] What does the action-value function Q(s,a) represent?
- [ML11-031] Write the Q-learning update rule and explain each term. Why is it off-policy?
- [ML11-032] Why is Q-learning considered a model-free method?
- [ML11-033] What roles do the learning rate alpha and the discount factor gamma play in Q-learning?
- [ML11-034] Explain SARSA and its update rule. Is it on-policy or off-policy, and why?
- [ML11-035] What is the difference between SARSA and Q-learning, and what does on-policy versus off-policy mean?
- [ML11-036] Compare the behaviour of SARSA and Q-learning on the cliff-walking problem. Why do they learn different paths?
- [ML11-037] What is Expected SARSA and how does it relate to the other two algorithms?
- [ML11-038] How does Q-learning differ from policy gradient methods, and when would you choose one over the other?
- [ML11-039] Under what conditions does tabular Q-learning converge to the optimal policy?
- [ML11-040] What are common strategies for initializing the Q-table, and what does optimistic initialization do?
- [ML11-041] How do you decide when a Q-learning agent has learned enough to stop training?
- [ML11-042] How would you apply Q-learning to a continuous action space?
- [ML11-043] Your Q-learning agent's average return plateaus at a poor level. What would you check first?

## Exploration, exploitation and bandits
- [ML11-044] What is the exploration versus exploitation trade-off in reinforcement learning?
- [ML11-045] How is exploration typically handled in Q-learning? Explain epsilon-greedy, epsilon decay, and softmax (Boltzmann) exploration.
- [ML11-046] What is a multi-armed bandit problem, and how does it differ from a full RL problem?
- [ML11-047] Explain epsilon-greedy, UCB, and Thompson sampling for bandits. What are their trade-offs?
- [ML11-048] What is regret in a bandit setting, and how does it grow for a good algorithm?
- [ML11-049] What is a contextual bandit, and when is it a better model than full RL, for example in recommendation?
- [ML11-050] What is the sparse-reward problem in RL, and what remedies exist such as reward shaping, curiosity, and curriculum learning?
- [ML11-051] What is potential-based reward shaping, and why does it preserve the optimal policy?
- [ML11-052] How do count-based and prediction-error (curiosity) intrinsic rewards work, and what failure modes do they have, such as the noisy-TV problem?
- [ML11-053] How does exploration appear in policy-gradient training, and what is the role of entropy regularization?

## Deep Q-networks
- [ML11-054] What is a Deep Q-Network, and what does it add over tabular Q-learning? What roles do experience replay and target networks play?
- [ML11-055] Why is experience replay important in DQN?
- [ML11-056] Why does DQN use a separate target network, and how do hard and soft (Polyak) updates differ?
- [ML11-057] What is overestimation bias in Q-learning, and how does Double DQN reduce it?
- [ML11-058] What is the deadly triad in reinforcement learning, and which of the three elements is given up in each family of methods?
- [ML11-059] What do dueling networks and prioritized experience replay add to DQN?
- [ML11-060] Why can't vanilla DQN be applied directly to continuous action spaces?
- [ML11-061] Why does DQN on Atari use frame stacking, reward clipping, and an epsilon schedule?
- [ML11-062] Your DQN's Q-values keep growing and the loss oscillates. What are the likely causes and fixes?
- [ML11-063] Name some components of Rainbow DQN and explain which problems each one addresses.

## Policy gradients and actor-critic
- [ML11-064] What is the difference between policy-based and value-based methods? When is each preferable, for example with continuous actions?
- [ML11-065] Derive the REINFORCE policy gradient and explain why subtracting a baseline reduces variance without adding bias.
- [ML11-066] Explain the log-derivative trick and the policy gradient theorem in your own words.
- [ML11-067] Why are policy-gradient methods high variance, and how do reward-to-go, baselines, and advantage estimation help?
- [ML11-068] Explain the actor-critic architecture and the advantage actor-critic (A2C/A3C) algorithm.
- [ML11-069] How do A2C and A3C differ, and why did synchronous variants largely replace asynchronous ones?
- [ML11-070] What kinds of policy distributions are used for discrete versus continuous actions, and how is the log-probability computed?
- [ML11-071] What bias-variance trade-off appears when the critic is used to bootstrap the policy gradient target?
- [ML11-072] Policy entropy collapses early in training and the return stops improving. What do you do?

## Trust regions, PPO and continuous control
- [ML11-073] Why is on-policy training sample-inefficient, and how does importance sampling let you reuse data from an older policy?
- [ML11-074] When does importance sampling become unreliable, and why does TRPO constrain the KL divergence between old and new policy?
- [ML11-075] Explain PPO-Clip and PPO-Penalty. What does the clipping range epsilon do to the policy update?
- [ML11-076] Why does PPO clip the importance ratio instead of using a KL penalty alone?
- [ML11-077] What is generalized advantage estimation, and how do lambda and gamma control the bias-variance trade-off?
- [ML11-078] What implementation details matter most in PPO, such as number of epochs, minibatch size, advantage normalization, and value loss clipping?
- [ML11-079] During PPO training the approximate KL and clip fraction spike and performance collapses. How do you diagnose and fix it?
- [ML11-080] What is DDPG, and how does it extend DQN ideas to continuous action spaces?
- [ML11-081] How does TD3 fix the problems of DDPG?
- [ML11-082] What is Soft Actor-Critic, and why does maximum-entropy RL help with exploration and robustness?
- [ML11-083] Compare PPO and SAC. When would you choose each for a continuous control task?
- [ML11-084] What is the natural policy gradient, and how does it relate to TRPO?

## Model-based RL, offline RL and multi-agent
- [ML11-085] Explain the difference between model-based and model-free reinforcement learning.
- [ML11-086] What are the advantages and disadvantages of model-based reinforcement learning?
- [ML11-087] What is the Dyna architecture, and how does it combine real experience with simulated experience?
- [ML11-088] Why does compounding model error hurt model-based RL, and how do methods such as short rollouts or ensembles mitigate it?
- [ML11-089] How do AlphaZero and MuZero combine search with learned policy and value networks?
- [ML11-090] What is offline (batch) RL, and why does naive off-policy RL fail on a fixed dataset?
- [ML11-091] How does Conservative Q-Learning, or a behaviour-regularized approach, address distribution shift in offline RL?
- [ML11-092] What makes multi-agent RL harder than single-agent RL?

## Imitation learning, reward design and sim-to-real
- [ML11-093] What is imitation learning, how does behavioral cloning suffer from compounding error, and how does inverse RL differ?
- [ML11-094] Behaviour cloning has a well-known failure mode when the policy drifts off the expert's data distribution. What is it, and how do you mitigate it?
- [ML11-095] How does DAgger work, and what does it require from the expert?
- [ML11-096] In behaviour cloning, how do you decide which failure states are worth the cost of collecting correction data?
- [ML11-097] Why can adding more expert-quality demonstrations fail to fix the compounding-error problem of behaviour cloning?
- [ML11-098] What is GAIL, and how does it differ from inverse reinforcement learning?
- [ML11-099] Where does reinforcement learning fit on top of imitation learning for control or manipulation, and why is the reward the hard part?
- [ML11-100] How would you use the failed episodes that imitation learning throws away?
- [ML11-101] What safeguards would let you run online RL on a real physical system?
- [ML11-102] A control policy trained entirely in simulation has to run on real hardware. What transfers, what does not, and how do you close the gap?
- [ML11-103] How would you tell an overfit-to-sim failure from a genuinely under-trained policy?
- [ML11-104] In sim-to-real training, why does randomising actuation or sensing latency matter more than it sounds like it should?
- [ML11-105] What is domain randomization, and what are its limits?
- [ML11-106] How do you evaluate an RL algorithm fairly given high variance across random seeds?
- [ML11-107] Your RL agent maximizes the training reward but behaves badly in deployment. How do you investigate?
