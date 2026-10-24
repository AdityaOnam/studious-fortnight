---
domain: finetune
topic: rlhf_dpo_ppo_grpo_preference
title: RLHF, DPO, PPO, GRPO and preference tuning
tags: [rlhf, dpo, ppo, grpo, alignment]
count: 78
part: 2/2
---
# RLHF, DPO, PPO, GRPO and preference tuning (part 2)

## GRPO and its variants
- [FT03-112] What are the differences in principle between PPO, GRPO and DPO?
- [FT03-113] Why does GRPO drop the critic network, and how does it estimate advantages from a group of samples?
- [FT03-114] In GRPO you sample four completions for a prompt and get rewards [1, 0, 0, 1]. Compute the advantages and say what the gradient does.
- [FT03-115] How does GRPO differ from PPO, and why has it displaced PPO for reasoning RL? Why did DeepSeek-R1 use it?
- [FT03-116] Explain GRPO and one of its known failure modes.
- [FT03-117] In GRPO, how does group size trade off against variance and cost?
- [FT03-118] What happens to GRPO's gradient on prompts the model always or never solves, and what does that imply for data curation?
- [FT03-119] How would you construct the prompt curriculum for RLVR training to avoid degenerate groups?
- [FT03-120] What biases do standard-deviation normalisation and per-sequence length normalisation introduce in GRPO, and how do variants such as Dr. GRPO address them?
- [FT03-121] What are DAPO and GSPO, and how do they differ from GRPO? What instabilities do they target?
- [FT03-122] Why does entropy collapse specifically hurt GRPO more than it hurts PPO?
- [FT03-123] What is RLOO, and why does a leave-one-out baseline work as a critic-free alternative to PPO?
- [FT03-124] Why is the KL-to-reference term still needed with verifiable rewards, and what breaks if you drop it?
- [FT03-125] In GRPO, should the KL term go into the reward or the loss, and does it change the gradient?
- [FT03-126] You are running GRPO with a verifier reward on a code task. Reward climbs, but outputs get shorter and more repetitive and the held-out pass rate drops. What is happening?
- [FT03-127] Response length often grows during RLVR training. Is that desirable, and how do you handle truncated or overlong samples?

## RLVR and reasoning RL
- [FT03-128] What is RLVR (reinforcement learning with verifiable rewards), and for which tasks does it work well?
- [FT03-129] Why is RLVR more stable and scalable than reward-model RLHF for reasoning? What goes wrong when RL-training reasoning against a learned preference reward?
- [FT03-130] Why are math and code so RL-friendly? Explain verifiable rewards and the R1-style training recipe.
- [FT03-131] For a reasoning model, how would you design the reward for RLVR, and how does it differ from classic RLHF?
- [FT03-132] Walk me through training a reasoning model with RLVR. Why GRPO instead of PPO, and what breaks in practice?
- [FT03-133] What is the difference between accuracy rewards and format rewards in RLVR, and what risks does each carry?
- [FT03-134] DeepSeek R1-Zero was trained with RL and essentially no SFT first. What did that show, and why did full R1 add SFT back?
- [FT03-135] Why did pure-RL R1-Zero produce messy outputs, and what does the cold-start SFT fix?
- [FT03-136] In R1-Zero-style RL training, why does language mixing emerge, and how would you penalise it without hurting reasoning?
- [FT03-137] How do you handle sparse reward on long reasoning chains in RLVR?
- [FT03-138] Does RL add new capability, or only sharpen sampling from the base model? What evidence would distinguish the two?
- [FT03-139] If RLVR mostly elicits existing capability, what does that imply for where to spend your next dollar?
- [FT03-140] How would you measure pass@k on the base model before committing GPU budget to reinforcement fine-tuning?
- [FT03-141] Kimi K1.5 scaled RL for reasoning without a process reward model or tree search. Why deliberately keep the RL recipe that simple?
- [FT03-142] What can go wrong with reward design when you skip a process reward model and reward only final correctness?
- [FT03-143] Why does long context reduce the need for explicit search at training time in RL for reasoning models?
- [FT03-144] A model ships hybrid think and non-think modes, post-trained with SFT then RLVR. How would you build that, and why RLVR over vanilla RLHF?
- [FT03-145] You want one model that runs at several effort levels, trading capability for cost. How do you design the RL reward and set the cost penalty?
- [FT03-146] What is the equivalent of a verifiable reward for a domain like legal drafting?
- [FT03-147] How would you design a verifier for an Indic-language instruction-following task where there is no single correct string?
- [FT03-148] How does rejection sampling fine-tuning work, and how does it differ from DPO and GRPO? When is best-of-n distillation enough?

## Process rewards, RLAIF and Constitutional AI
- [FT03-149] What is a process reward model (PRM), and how does it differ from an outcome reward model? When do you need each?
- [FT03-150] How would you generate process reward model labels without human annotators, and what bias does that introduce?
- [FT03-151] Why might a process reward model used as a best-of-N reranker degrade as N grows?
- [FT03-152] Design a process reward model for a customer-support agent. What signals do you score, and how do you avoid degenerate reward?
- [FT03-153] What is the one-line difference between RLHF and RLAIF?
- [FT03-154] What is Constitutional AI, and how does it differ from RLHF? How does AI feedback replace human feedback?
- [FT03-155] Explain Constitutional AI. What does it buy you over vanilla RLHF, and what does it not solve?
- [FT03-156] How does RLAIF preference data differ in failure modes from human preference data?
- [FT03-157] If the AI labeller in RLAIF is the same model family being trained, what failure loops does that risk?
- [FT03-158] A model's guiding constitution moves from a list of principles toward explained reasoning with a priority order. What does that shift change, and how would you test whether it worked?
- [FT03-159] Where does RLAIF or constitutional-style feedback fit in the taxonomy of supervised, unsupervised and self-supervised learning?
- [FT03-160] How would you write and iterate on a constitution so that the resulting model is neither over-refusing nor under-refusing?

## Agentic RL and training systems
- [FT03-161] Why is reward design harder for multi-step agentic tasks than for single-answer maths?
- [FT03-162] What changes in an RL reward for an agent if success is graded, such as partial test passes, rather than binary?
- [FT03-163] You want to RL-train an agent for a multi-turn tool-use task where the only reward is whether the final task succeeded. How do you make that work?
- [FT03-164] Why is trajectory-level advantage tolerable when RL-training a multi-turn agent with only a final-success reward, and at what horizon does it stop working?
- [FT03-165] How do you assign credit across a 300-action trajectory in agent RL training?
- [FT03-166] How would you RL-train an agent on a task where success is only checkable by a human?
- [FT03-167] You train an agentic coding model with RL on long-horizon tasks. Design the environment and reward: what does the agent see, what counts as success, and how do you stop it gaming the reward?
- [FT03-168] What makes a good RL environment for LLM training, concretely?
- [FT03-169] How do you decide a task belongs in an RL environment at all, rather than in an SFT set?
- [FT03-170] A team wants to run reinforcement fine-tuning on an open-weights model to make an extraction agent more reliable. Who owns it, and how do you decide whether to do it at all?
- [FT03-171] How would you sandbox code execution safely and at scale for an RL environment?
- [FT03-172] Why does long-horizon agentic RL need a disaggregated, asynchronous training design rather than a colocated-synchronous one?
- [FT03-173] In asynchronous agentic RL training, how stale can rollouts get before training destabilises, and how would you bound it?
- [FT03-174] What does going fully asynchronous buy you in RL throughput, and what does it cost in correctness?
- [FT03-175] Your RL loop samples rollouts with a fast inference engine and trains with FSDP. Why do the two disagree on token log-probs, and what do you do about it?
- [FT03-176] How would you tell training-inference mismatch apart from a learning rate that is simply too high?
- [FT03-177] Why is training-inference mismatch worse for MoE models in RL, and why is expert routing a source of noise?
- [FT03-178] Why is rollout generation usually the throughput bottleneck in LLM RL, and how do you improve GPU utilisation?

## Choosing and evaluating alignment methods
- [FT03-179] How do you choose between on-policy methods, off-policy methods and DPO?
- [FT03-180] What are the suitable use cases for PPO, GRPO and DPO respectively?
- [FT03-181] You are building a model that must solve multi-step math and verify tool-call success. Why might PPO/RLHF beat DPO here?
- [FT03-182] Explain the different preference alignment methods and how they relate to each other.
- [FT03-183] You have 10k preference pairs, one node of GPUs and a two-week deadline. Which method would you run first and what would you ablate?
- [FT03-184] How would you evaluate the success of preference alignment methods, and of an RLHF-trained model?
- [FT03-185] What metrics or strategies would you use to compare preference-tuned LLMs?
- [FT03-186] How do win rates from an LLM judge get distorted by length and position, and how would you correct for it?
- [FT03-187] How does preference tuning affect generalisation in LLMs?
- [FT03-188] How would you check a preference-tuned model for regressions in sycophancy, factuality and safety, not just helpfulness?
- [FT03-189] How would you present the helpfulness versus safety trade-off of a tuned model to stakeholders, and how would you pick an operating point?
