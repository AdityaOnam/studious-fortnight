---
domain: genai
topic: agents_planning_memory_multiagent
title: Agents: planning, memory, multi-agent
tags: [agents, multi-agent, memory, langgraph]
count: 89
part: 1/4
---
# Agents: planning, memory, multi-agent (part 1)

## Agent fundamentals
- [GA03-001] What is an AI agent, and how does it differ from a simple LLM call or a chatbot?
- [GA03-002] What are the core components of an LLM agent, and how do you interpret Agent = LLM + Planning + Memory + Tools?
- [GA03-003] Why do we need agents, and what layers of technique (prompting, tools, decomposition, feedback loops, multi-agent) are used to build them?
- [GA03-004] What are the main design components of a goal-oriented agent architecture (central executive, memory, perception, action, learning, world model)?
- [GA03-005] What is the difference between reactive and proactive agents?
- [GA03-006] What is the core difference between a copilot and an agent, and why are planning and reflection needed?
- [GA03-007] What makes a system truly agentic, and what does not?
- [GA03-008] What does Agent = Model + Harness + Tools + Environment mean, and why is it said the model sets the ceiling while the harness sets the floor?
- [GA03-009] What is harness engineering, and how does it relate to prompt engineering and context engineering?
- [GA03-010] What types of LLM agents exist (reactive, plan-and-execute, goal-driven, multi-agent), and when is each suitable?
- [GA03-011] What are agency levels, and how do you decide how much autonomy to grant an agent?
- [GA03-012] What is the difference between code-generating agents and tool-calling agents?
- [GA03-013] How would you construct an agent on top of an LLM, covering prompting, tool schemas, loop control and stop conditions?
- [GA03-014] How does an agent decide when to call a tool versus answer from its own knowledge?
- [GA03-015] Why is building agents a systems problem rather than only a modeling problem?
- [GA03-016] Why is a reasoning model better suited to agentic work than a standard LLM?
- [GA03-017] When is a reasoning model worth using inside an agent loop, and when is it a waste of money?
- [GA03-018] How would you measure whether a reasoning model is earning its cost at a given step of an agent?
- [GA03-019] If reasoning models think internally anyway, is an explicit scratchpad or "think" tool still useful in an agent?
- [GA03-020] You add a "think" tool to a policy-heavy refund agent but see almost no improvement. What is the most likely reason?
- [GA03-021] What changes in agent design when the agent must respond in real time?
- [GA03-022] How does an AI research agent work end to end, from planning to synthesis?
- [GA03-023] How does AutoGPT work, and how does it differ from an ordinary agent?
- [GA03-024] What is Voyager-style lifelong learning, and how does a skill library accumulate over time?
- [GA03-025] An experiment let an LLM run a shop autonomously for an extended period. What does it teach about the limits of LLM agency?
- [GA03-026] How do the agent, tool, data and harness layers of an AI application architecture work together?

## Workflows versus agents
- [GA03-027] What is the difference between an agent and a workflow, and how do workflows, agents and tools relate?
- [GA03-028] What is an agentic workflow, and how does it differ from a traditional AI application?
- [GA03-029] How is a multi-agent system different from a multi-stage prompt chain?
- [GA03-030] What is flow engineering?
- [GA03-031] How do workflows, graphs and loops relate, and how does a graph loop differ from an agent loop?
- [GA03-032] When should you use a pure agent, a deterministic workflow, or an agentic workflow, and how has agent engineering evolved?
- [GA03-033] When is an agentic approach the wrong solution?
- [GA03-034] A PM wants an "agent" for invoice processing with fixed extraction fields. What do you build?
- [GA03-035] Where on the workflow-to-agent spectrum would you place a RAG chatbot that can optionally issue a search query?
- [GA03-036] Can a system be a workflow at the top level with agents inside it?
- [GA03-037] How would you retrofit an over-agentic system into a workflow?
- [GA03-038] A PM asks you to spec an agent that reads a support email and either answers, issues a refund, or escalates to a human. What is the right first architecture?
- [GA03-039] Why use an agent rather than a RAG Q&A system or a workflow, and how would you make that case to the business?
- [GA03-040] A complex agentic system scores 15% better on benchmarks than a simpler RAG pipeline that is easier to maintain. How do you decide?
- [GA03-041] How do you distinguish RAG, memory, context and state in an agent system?
- [GA03-042] What are the boundaries between the model, tools, memory, RAG and state, and why should they be governed separately?

## Reasoning and planning patterns
- [GA03-043] Explain the ReAct pattern, what it adds over chain-of-thought alone, and its main failure modes.
- [GA03-044] How does ReAct relate to modern native tool calling, and how relevant is it today?
- [GA03-045] Why does interleaving reasoning and acting often beat plan-everything-then-execute, and when does plan-first win?
- [GA03-046] What is the Plan-and-Execute agent pattern?
- [GA03-047] Compare ReAct with Plan-and-Execute. When does each win, and how do you choose?
- [GA03-048] What are Plan-and-Solve and ReWOO, and how do they differ from ReAct?
- [GA03-049] How does ReAct's myopia show up concretely in a coding agent?
- [GA03-050] How would you implement a code review agent using ReAct?
- [GA03-051] How can task decomposition be approached in LLM agents, and what do decomposition and recomposition buy you?
- [GA03-052] Why should an agent clarify requirements before decomposing a task?
- [GA03-053] How do you prevent an agent from infinite recursion during task decomposition?
- [GA03-054] Should an agent's plan be represented as prose in context or as a structured todo tool, and why?
- [GA03-055] What is dynamic replanning, and what triggers should make a plan-then-execute agent replan?
- [GA03-056] Why is plan revision often more expensive than plan generation?
- [GA03-057] What is LATS (Language Agent Tree Search), and how does it differ from Reflexion?
- [GA03-058] How does inference-time scaling relate to agentic loops?
- [GA03-059] You run a reasoning model in a multi-turn tool-use loop. What do you do with its reasoning between calls, and what breaks if you drop it?
- [GA03-060] How do zero-data-retention requirements change how you carry reasoning between calls in an agent?

## Reflection and verification
- [GA03-061] What is agent reflection, and how does it improve agent performance?
- [GA03-062] What is a generator-evaluator architecture, and why does reflection help?
- [GA03-063] What is the Reflexion mechanism, and how does it differ from ReAct and from plain self-reflection?
- [GA03-064] When does Reflexion-style self-critique actually improve an agent, and what does it cost?
- [GA03-065] Should the critic in a reflection loop be a different model than the generator?
- [GA03-066] Where would you insert reflection in a coding agent's loop: every step, or at commit boundaries?
- [GA03-067] How does CRITIC-style grounded verification differ from self-reflection?
- [GA03-068] Why must the verifier be separate from the producer in an agent loop, and where should budget enforcement live?
- [GA03-069] Should the verifier tell the agent why it rejected its work?
- [GA03-070] Why can a critic or verifier agent improve quality but also cause new problems?

## Agent loop and termination
- [GA03-071] What is an agent loop, what are its components, and how does it decide when to stop?
- [GA03-072] How do observation, planning, action and reflection work together in an agent loop?
- [GA03-073] Define the agent loop, and explain when a loop is actively harmful.
- [GA03-074] What is loopmaxxing, and how do you convert a non-converging agent loop into a useful one?
- [GA03-075] How do you set exit boundaries for an agent loop and bound its cost and step count?
- [GA03-076] How would you write a stop condition for an open-ended research task for an agent?
- [GA03-077] Where would you put permission checks in the agent loop?
- [GA03-078] What triggers the next round of an outer loop: a CI event, a scheduled task, a goal check, or manual approval?
- [GA03-079] What is the difference between an outer loop and the agent loop inside a single task, and how are state and verification results handed over?
- [GA03-080] How is a system prompt for a long-running agent different from one for a single-shot feature?
- [GA03-081] How does an agent decide between waiting on a long-running task and continuing with other work?
- [GA03-082] Your AI agent is stuck in an infinite loop. How do you detect and break the cycle?
- [GA03-083] An agent called a broken tool 400 times in five minutes. Diagnose it and design the fix.
- [GA03-084] Your agent re-issues slightly reworded versions of the same failing search for many steps even though a max-steps cap exists. What is missing?
- [GA03-085] How do you stop a ReAct-style agent that keeps retrying a failing tool?
- [GA03-086] How would you stop a coding agent from looping on the same failing edit or failing test?
- [GA03-087] How do you detect an unproductive loop programmatically, and tell a productive retry from a loop?
- [GA03-088] Your agent gets stuck in loops or gives up too early. Diagnose and fix both.
- [GA03-089] What is the right behaviour when the agent correctly determines a task is impossible?
