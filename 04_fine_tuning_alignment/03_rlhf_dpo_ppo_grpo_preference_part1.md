---
domain: finetune
topic: rlhf_dpo_ppo_grpo_preference
title: RLHF, DPO, PPO, GRPO and preference tuning
tags: [rlhf, dpo, ppo, grpo, alignment]
count: 111
part: 1/2
---
# RLHF, DPO, PPO, GRPO and preference tuning (part 1)

## Alignment and post-training landscape
- [FT03-001] What is AI alignment, and why does alignment tuning matter for making an LLM usable?
- [FT03-002] Why is a pretrained next-token predictor not a good assistant out of the box, even after instruction tuning?
- [FT03-003] What do "helpful, honest and harmless" mean as alignment goals, and how can they conflict?
- [FT03-004] Explain the difference between pre-training, supervised fine-tuning (SFT), and preference optimization (RLHF/DPO).
- [FT03-005] At which stage would you move from SFT to a preference-alignment method, and what does preference data give you that demonstrations do not?
- [FT03-006] Why do modern post-training stacks layer SFT, preference optimization and RL instead of relying on a single method?
- [FT03-007] What are the mainstream post-training pipelines, and how do you choose between SFT then DPO and SFT then GRPO?
- [FT03-008] Compare SFT, RLHF with PPO, DPO, KTO, ORPO, SimPO, GRPO and RLVR in terms of data requirements, extra models needed, cost and when to use each.
- [FT03-009] What do RLHF, DPO and Constitutional AI actually do for safety, and why can't a system prompt replace them?
- [FT03-010] Why is no single alignment technique a safety guarantee, and how would you layer defenses?
- [FT03-011] What is the alignment tax, and how do you measure it?
- [FT03-012] After RLHF your model became safer but lost capability on hard tasks. How do you manage the alignment tax?
- [FT03-013] How does preference tuning cause over-refusal, and how do you manage it?
- [FT03-014] You are aligning a customer-support chat model to a preferred tone and refusal style with a small team and limited GPU budget. Which approach fits best and why?
- [FT03-015] Walk me through a post-training recipe to turn a pretrained base model into a personalized assistant.

## Reward models and the RLHF pipeline
- [FT03-016] What is RLHF, and why is it used to fine-tune large language models?
- [FT03-017] Walk me through RLHF end to end: its three stages (SFT, reward modelling, RL optimisation), the policy optimisation step and the KL penalty.
- [FT03-018] What was the core idea of the original deep RL from human preferences work, and how did it lead to RLHF for language models?
- [FT03-019] Why use pairwise preference comparisons instead of absolute ratings when collecting data for RLHF?
- [FT03-020] What breaks if you skip SFT and run PPO directly on the base model?
- [FT03-021] How does a reward model differ architecturally from the base language model it is initialised from?
- [FT03-022] How do you train a reward model from pairwise preferences? Explain the data format and the Bradley-Terry loss.
- [FT03-023] What is the Bradley-Terry model and what assumptions does it make about human preferences?
- [FT03-024] What data format does a reward model need, and how does it differ from SFT data?
- [FT03-025] Is a reward model trained with supervised learning or with RL?
- [FT03-026] Why is the absolute value of a Bradley-Terry reward meaningless, and what does that imply for normalising rewards before PPO?
- [FT03-027] Why sample reward-model training responses from the SFT model rather than another model?
- [FT03-028] Does the reward model need to be the same size or family as the policy? What are the trade-offs?
- [FT03-029] Reward models typically reach only about 70 to 75 percent held-out pairwise accuracy. Why is the ceiling so low, and does it matter?
- [FT03-030] How would you detect and correct length bias in a reward model?
- [FT03-031] How do you evaluate a reward model before using it for RL? Why is held-out pairwise accuracy not enough?
- [FT03-032] How would you decide when to retrain the reward model during a long RLHF run?
- [FT03-033] What would a best-of-N curve that is flat from N=1 tell you about a reward model?
- [FT03-034] How would a reward-model ensemble or uncertainty estimate help during policy optimisation?
- [FT03-035] Why does RLHF hurt calibration of model confidence?
- [FT03-036] Why can RLHF increase confident hallucination?
- [FT03-037] What are the main challenges and limitations of RLHF?
- [FT03-038] The SFT, reward-model, PPO pipeline is long and slow to iterate. How would you shorten it?
- [FT03-039] What are some alternatives and recent advances beyond the standard RLHF process?

## Preference data collection
- [FT03-040] What kind of data is needed to train the reward model in RLHF, and how is it typically collected?
- [FT03-041] How is preference data collected, what does it cost, and what quality problems arise in annotation?
- [FT03-042] Walk through actually collecting preference data. What are the logistics, and where does it go wrong?
- [FT03-043] Your RLHF preference data has low annotator agreement. How do you ensure data quality?
- [FT03-044] Your vendor delivers 50k preference pairs with a Krippendorff's alpha of 0.45. What do you do?
- [FT03-045] How would you address potential biases in human preference data, such as verbosity or style preferences?
- [FT03-046] Human preference data is expensive. What strategies reduce annotation cost, such as AI feedback and active selection?
- [FT03-047] Where would you still insist on human labels in preference-data collection?
- [FT03-048] How would you design preference data collection differently if the task is code review rather than open-ended chat?
- [FT03-049] Design an end-to-end pipeline producing RLHF preference data for a frontier lab: 100k prompt-response comparisons a week, with quality guarantees.
- [FT03-050] How does an RLHF preference-data pipeline design change when the customer requires that their data never train other customers' models?
- [FT03-051] Which prompts and which response pairs are most informative to label, and how would you select them?
- [FT03-052] What are the pitfalls of using LLM-as-judge for preference labels, such as position, verbosity and self-preference bias?

## PPO and the KL penalty
- [FT03-053] Explain PPO in the RLHF context. Why is PPO used for the RL stage and what is the role of the KL penalty?
- [FT03-054] Why does PPO-based RLHF need a KL penalty against the reference model, and what happens if the coefficient is too small or too large?
- [FT03-055] What does the KL constraint in RLHF actually prevent?
- [FT03-056] From the maximum likelihood or MAP viewpoint, what role does the KL penalty play in RLHF?
- [FT03-057] What are the common estimators of KL used in LLM RL (k1, k2, k3), and how would you choose between them and between reward-level and loss-level KL?
- [FT03-058] How would you pick the KL coefficient, and what does an adaptive KL controller do?
- [FT03-059] Why is the reference model kept frozen during RLHF and DPO, and what would happen if it were updated every step?
- [FT03-060] Why does PPO clip probability ratios instead of just taking a bigger learning rate?
- [FT03-061] What is the advantage function, and why does LLM PPO use GAE with a value head?
- [FT03-062] How is the reward assigned per token in RLHF (terminal reward plus per-token KL shaping), and why does the critic matter for credit assignment?
- [FT03-063] Walk through the PPO actor loss for RLHF: ratio, clipping, advantage and KL term. How is the critic loss defined?
- [FT03-064] What data does PPO training consume in an RLHF pipeline (prompts, rollouts, rewards), and how are prompts sampled?
- [FT03-065] PPO for LLMs keeps four models in memory (actor, critic, reference, reward). What does each do, and how would you reduce the compute and memory burden?
- [FT03-066] Estimate the GPU memory needed for PPO RLHF on a 70B policy, covering weights, optimizer states and rollouts, and say how you would shard it.
- [FT03-067] Why can the critic or value head in LLM PPO be unstable, and what options such as GRPO remove it?
- [FT03-068] What do you monitor during a PPO run to catch failure early?
- [FT03-069] What stability problems appear in RL training of LLMs, and how would you diagnose them?

## DPO and offline preference optimisation
- [FT03-070] What is Direct Preference Optimization (DPO), and how does it differ from RLHF?
- [FT03-071] In an interview you are asked to explain DPO. What is the one-sentence core that signals real understanding?
- [FT03-072] What is the key insight that lets DPO skip the reward model and the RL loop? How does it turn preference learning into a supervised loss?
- [FT03-073] Derive the DPO loss from the KL-regularised reward-maximisation objective and show how the optimal policy yields an implicit reward.
- [FT03-074] In the DPO derivation, why does the partition function term cancel, and why does that matter?
- [FT03-075] In DPO, what does beta trade off, and what happens at very small or very large values?
- [FT03-076] Why do you usually run SFT on the chosen responses before DPO, and what goes wrong if the reference model does not match the preference data distribution?
- [FT03-077] Why has DPO displaced PPO-based RLHF at many labs?
- [FT03-078] Compare DPO and PPO-based RLHF in stability, compute, data requirements and final quality. When is PPO still better?
- [FT03-079] Explain DPO to someone who knows PPO-based RLHF. When would you still choose an online RL method?
- [FT03-080] What is lost by never sampling from the policy during DPO training, and why does off-policy data limit DPO's ceiling?
- [FT03-081] What is online alignment, and how does it differ from offline preference optimisation?
- [FT03-082] Design an iterative or online DPO loop. Where does its extra signal come from?
- [FT03-083] Give one-liners on IPO, KTO, ORPO and SimPO: what problem does each solve, and when would you pick it?
- [FT03-084] How does DPO behave with noisy preference labels, and what do conservative DPO or label smoothing change?
- [FT03-085] Why does DPO's implicit reward margin grow without bound, and why is that bad?
- [FT03-086] Why do both chosen and rejected log-probabilities decrease during DPO, and when is that actually fine?
- [FT03-087] Your DPO run improves win rate against the SFT model, but outputs are longer, waffly and hedge constantly. Debug it.
- [FT03-088] After heavy DPO the model is more on-tone but its answers feel repetitive and slightly shallower factually. What is happening and what do you do?
- [FT03-089] Your DPO run improved chat evals but regressed math. What are your hypotheses?
- [FT03-090] You have 500k thumbs-up and thumbs-down events from production. Which preference-tuning method would you use and why?
- [FT03-091] What are the failure modes of RLHF compared with the failure modes of DPO?

## Reward hacking and over-optimisation
- [FT03-092] What is reward hacking in RLHF? Give concrete examples, the impact on preference tuning, and mitigations.
- [FT03-093] Your RLHF-trained LLM is gaming the reward model instead of being genuinely helpful. How do you fix reward hacking?
- [FT03-094] What is sycophancy, why does RLHF tend to produce it, and how would you reduce it?
- [FT03-095] Reward is climbing steadily during your RLHF run, but human evaluation shows quality getting worse. What evidence distinguishes genuine improvement from reward hacking?
- [FT03-096] Training reward rises steadily but the held-out benchmark or human-rated quality is flat. What do you check first?
- [FT03-097] What does the gold-versus-proxy reward-model over-optimisation curve look like as KL from the reference grows, and how does it guide early stopping?
- [FT03-098] How is RLHF reward hacking formally the same problem as Goodhart's law in evaluation, and what do the mitigations share?
- [FT03-099] How do you prevent reward hacking when using Best-of-N sampling?
- [FT03-100] When would best-of-n sampling with a reward model beat both DPO and PPO?
- [FT03-101] When does a learned reward model still earn its keep despite the reward-hacking risk?
- [FT03-102] How would you detect reward hacking in aggregate during an online RL run, before a human notices it in production?
- [FT03-103] What reward-hacking failure modes would you watch for with rule-based rewards?
- [FT03-104] What reward-hacking behaviours occur against unit-test rewards, such as hard-coding expected outputs, and how do you defend against them?
- [FT03-105] How would you design a verifier for a code task that is genuinely hard to hack?
- [FT03-106] When training an agent with RL on code tasks, what do you do about flaky tests polluting the reward signal?
- [FT03-107] Why does a single scalar reward tend to over-weight harmlessness, and what is the alternative?
- [FT03-108] You plan to run RL on a domain with no programmatic verifier, using a rubric-scored judge as the reward. What goes wrong, and how do you guard against it?
- [FT03-109] How would you tell whether a policy is exploiting the judge rather than genuinely improving?
- [FT03-110] Your grader agrees with humans 90 percent of the time on natural outputs. Is that enough to use it as a reward?
- [FT03-111] Your team wants to reuse the eval suite's graders as the reward signal for reinforcement fine-tuning. What changes?
