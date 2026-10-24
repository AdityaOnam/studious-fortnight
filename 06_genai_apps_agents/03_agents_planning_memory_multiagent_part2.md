---
domain: genai
topic: agents_planning_memory_multiagent
title: Agents: planning, memory, multi-agent
tags: [agents, multi-agent, memory, langgraph]
count: 97
part: 2/4
---
# Agents: planning, memory, multi-agent (part 2)

## Failure modes and reliability
- [GA03-090] What failure modes do agents have, such as loops, hallucinated tools and unrecoverable errors, and how do you handle agent failures and recover?
- [GA03-091] Why do seemingly simple problems (arithmetic, long-horizon planning) stay hard for LLM agents, and how do you mitigate compounding errors?
- [GA03-092] Each step of your ReAct agent is about 95% reliable, yet success on 15-step tasks is poor. What is going on, and what is the structural fix?
- [GA03-093] Walk me through the compounding-error math for agents and what it implies for design.
- [GA03-094] How does verification-before-done interact with the compounding-error math?
- [GA03-095] Given a fixed budget, when do you spend it on a better model versus recovery machinery?
- [GA03-096] Your agent takes 47 LLM calls to finish a task that should take 5. How do you debug it?
- [GA03-097] Your AI agent takes too long to complete a task. How do you speed it up?
- [GA03-098] Why is meandering (taking too many steps) a critical failure in agent design, and what metrics expose it?
- [GA03-099] How do you avoid agent runaway costs?
- [GA03-100] Why is traditional try/catch exception handling insufficient for agentic systems?
- [GA03-101] How do you handle silent failures where a tool returns 200 OK but the data is wrong or the downstream effect never happened?
- [GA03-102] Your AI agent gets conflicting answers from different tools. How does it reconcile them?
- [GA03-103] How would you tell tool-selection failures apart from planning failures in production agent traces?
- [GA03-104] An agent's cost per task rose 40% and its tone changed overnight with no code change. What happened?
- [GA03-105] What is the difference between a kill switch and a circuit breaker for an agent, and why do you need both?
- [GA03-106] What would you alert on to catch a runaway agent before the circuit breaker trips?
- [GA03-107] How do you make sure an agent's kill switch actually works when it is never exercised in normal operation?

## Memory fundamentals and storage
- [GA03-108] What is short-term (working) memory in an AI agent, and how does it differ from persistent memory?
- [GA03-109] What are the types of agent memory (short-term, long-term, episodic), and how do short-term and long-term memory differ and get realized?
- [GA03-110] Explain the agent memory hierarchy of working, episodic, semantic and procedural memory.
- [GA03-111] How do you design short-term versus long-term memory for an agent, and what technology choices exist for each?
- [GA03-112] What is an agent memory architecture, and when do flat vector, episodic, graph and hybrid designs suit? What do Mem0, Zep, Letta and LOCOMO represent?
- [GA03-113] When does an agent need a memory layer beyond a long context window, and why not just use a 1M-token window for everything?
- [GA03-114] Design memory for a long-running agent whose users expect it to remember decisions from weeks ago. What do you store, where, and how do you retrieve it?
- [GA03-115] How do you choose between a vector database and a knowledge graph for long-term memory?
- [GA03-116] How does a knowledge graph help an AI agent?
- [GA03-117] Would you implement agent memory as vector search or as files the agent greps, and when is file-based memory the better choice?
- [GA03-118] Would you use a vector store or rolling summarisation for cross-session memory? Defend the choice.
- [GA03-119] How would you add a vector database for an agent's long-term memory?
- [GA03-120] How can Markdown files store an agent's memory, and why does that work?
- [GA03-121] Which team-shared agent memories suit Git and code review, and which are better kept in a database?
- [GA03-122] Why use a dedicated memory service like Mem0 instead of a custom script that writes to Postgres?
- [GA03-123] In a multi-user shared agent with memory, how do you decide whose memories are whose?
- [GA03-124] How do you handle session continuity across multiple messaging channels in a personal AI agent?
- [GA03-125] Your memory store holds 50M memories across 10K tenants. How do you guarantee cross-tenant isolation, and what is the blast radius if it fails?

## Memory quality, safety and learning
- [GA03-126] How do you handle an agent memory that becomes false, such as a user changing their address, and how does a user correct a wrong memory?
- [GA03-127] How do you handle conflicting memories, including a retrieved memory that contradicts what the user just said?
- [GA03-128] How do you prevent one bad memory from degrading every future session?
- [GA03-129] Should an agent be allowed to write to its own long-term memory at all, and what changes if the memory is shared across a team?
- [GA03-130] How do you prevent memory poisoning when an agent can write to its own long-term store?
- [GA03-131] Memory hallucinations accumulate at write time and then propagate. How would you instrument production memory to catch this?
- [GA03-132] When does episodic memory become a liability rather than an asset?
- [GA03-133] Design the consolidation policy for the episodic-to-semantic transition. When does an episode become a fact?
- [GA03-134] A benchmark shows your agent does better with memory turned off. What do you do, and how do you evaluate whether memory helps at all?
- [GA03-135] How do memory pruning, decay and privacy rules work in long-term memory design?
- [GA03-136] How do you handle privacy leakage in a global semantic memory tier?
- [GA03-137] How do you handle memory fatigue, where an agent brings up too many irrelevant past details?
- [GA03-138] What is catastrophic forgetting in the context of learned agentic memory?
- [GA03-139] How would you design procedural memory for a production AI agent?
- [GA03-140] Your agent solves the same class of task 500 times a week and never improves. How do you make it learn without fine-tuning?
- [GA03-141] How would you stop two learned procedures in an agent's memory from contradicting each other?
- [GA03-142] What would make you delete a learned procedure that is still being retrieved and still succeeding?
- [GA03-143] What is the eternal intern problem for agents, and how does continual learning address it?
- [GA03-144] TTT-E2E compresses context into weights via test-time training. Where does it fit in an agent memory hierarchy, and what new failure mode does it introduce?

## Context management
- [GA03-145] Your chatbot loses the thread after about ten turns. What are your options for managing conversation history?
- [GA03-146] Your chatbot fails when users switch topics mid-conversation. How do you handle topic switches?
- [GA03-147] A conversation or agent task runs past the context window. What do you keep, and how do you decide?
- [GA03-148] How does conversation memory work in an LLM application, and how do sliding windows, buffers and summarization compare for a thousand-turn conversation?
- [GA03-149] How does context compaction work?
- [GA03-150] What must a compaction summary preserve for a coding agent specifically?
- [GA03-151] How do you evaluate that context compaction is not losing critical state?
- [GA03-152] How would you evaluate a compaction model when its errors only show up hours later?
- [GA03-153] What breaks when you summarise a conversation that contains tool calls and their results?
- [GA03-154] How would you decide between compressing conversation history and offloading it to a file?
- [GA03-155] Your context compaction job runs on a timer and sometimes fires mid tool-use turn. What breaks, and how do you fix it?
- [GA03-156] What is context rot, and what is your full mitigation stack for a multi-hour agent loop?
- [GA03-157] How do you detect context rot with metrics rather than vibes?
- [GA03-158] Your agent retrieves a 50k-token document early in a task and three steps later seems to forget its original goal. Most likely cause and fix?
- [GA03-159] In an agent that reads large files, what specific mechanisms keep the context window clean?
- [GA03-160] Design a token budget for an agent with a 200k context window. How do you allocate and enforce it?
- [GA03-161] How would you find the quality-versus-context-length curve for your agent?
- [GA03-162] Why can keeping failed attempts in context be valuable, and how do you keep them without amplifying self-conditioning?
- [GA03-163] How do you prevent state bloat in long-running agent sessions?
- [GA03-164] Why does input token cost in an agent loop grow roughly quadratically with steps, and what would you change to flatten it?
- [GA03-165] In a tiered conversation-memory design with four tiers, how do you split the context budget and tune it empirically?
- [GA03-166] How do you handle a user deliberately contradicting a stored fact as part of a roleplay?
- [GA03-167] What is the difference between the model's context window and the application's context window?
- [GA03-168] Your agent performs well for 5 minutes but degrades past 30 minutes of autonomous work. How do you fix it with context engineering?

## Long-running agents and durable execution
- [GA03-169] Your long-running agent drifts after hours and confidently works on the wrong thing. How do you diagnose and fix it?
- [GA03-170] How do you prevent agentic drift in long-running tasks?
- [GA03-171] An agent works fine for short tasks but degrades on long-running ones. How do you fix it?
- [GA03-172] Your agent must handle a task spanning far more than one context window. What is the right architecture?
- [GA03-173] How do you build agents that survive long-horizon tasks of hours or days, and how do you handle long-running tasks in general?
- [GA03-174] Your long-running agent occasionally crashes mid-task and loses hours of work. What is the best fix, and how do you make the loop resumable?
- [GA03-175] How would you checkpoint a 20-step agent job so a worker crash or a deploy restart does not restart it from step 1?
- [GA03-176] For a long-running agent, what exactly goes into the checkpoint (full message array or summarised state), and what makes a resumed session equivalent to an uninterrupted one?
- [GA03-177] How do you handle a tool version change in the middle of a long-running agent run?
- [GA03-178] How do you implement state management in complex agent workflows?
- [GA03-179] How do you choose the update strategy for state in a graph-based agent workflow?
- [GA03-180] What are checkpointing, time-travel and fork/join in agent state management?
- [GA03-181] What are stateful rollbacks and checkpoints in an agent workflow?
- [GA03-182] Checkpointing is not durable execution. What core things are still missing for durable agent execution?
- [GA03-183] Why are naive retries and checkpoints insufficient for a production agent with side effects?
- [GA03-184] When is durable execution overkill for an agent, and what would you use instead?
- [GA03-185] Would you build your agent on Temporal or rent a managed agent runtime?
- [GA03-186] Why can't an agent harness replay simply re-call real APIs, and how does replay differ from checkpoint recovery?
