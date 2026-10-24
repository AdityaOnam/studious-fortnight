---
domain: genai
topic: agents_planning_memory_multiagent
title: Agents: planning, memory, multi-agent
tags: [agents, multi-agent, memory, langgraph]
count: 120
part: 3/4
---
# Agents: planning, memory, multi-agent (part 3)

## Multi-agent fundamentals and patterns
- [GA03-187] What is the difference between single-agent and multi-agent systems?
- [GA03-188] What are AI SubAgents?
- [GA03-189] When would you choose a multi-agent system over a single agent, and when do multi-agent systems break down?
- [GA03-190] How would you design a multi-agent system, and when is multi-agent actually warranted?
- [GA03-191] You are building a coding agent where several agents would edit the same repository in parallel. Should it be single-agent or multi-agent?
- [GA03-192] What is agent orchestration, and how do you implement it?
- [GA03-193] Orchestration versus choreography for multi-agent systems: what are the tradeoffs?
- [GA03-194] How do agents communicate in a multi-agent system, and how do you handle conflicts?
- [GA03-195] Compare commander, peer-to-peer and hybrid multi-agent collaboration modes.
- [GA03-196] When do you define a multi-agent workflow in code, and when do you let a coordinator model delegate?
- [GA03-197] How do you choose between a sequence of chains and a multi-agent graph?
- [GA03-198] What are the main failure modes of a supervisor multi-agent architecture?
- [GA03-199] How do you prevent agents from talking to each other in an infinite loop without solving the task?
- [GA03-200] When would you use multi-agent debate versus a mixture of agents?
- [GA03-201] How do you decide whether a published multi-agent research result is worth building on?
- [GA03-202] How do you divide responsibilities and decompose tasks hierarchically among agents?
- [GA03-203] What would make you collapse a multi-agent system back into a single loop?
- [GA03-204] What are common multi-agent anti-patterns in production, and how would you split a customer-ticket workflow?

## Orchestrator-worker, handoffs and multi-agent operations
- [GA03-205] Explain the orchestrator-worker (subagent) pattern. What is the real benefit?
- [GA03-206] When should you split an agent into sub-agents, and what do you pass between them?
- [GA03-207] You are splitting a research agent into an orchestrator and subagents. What exactly crosses the boundary in each direction?
- [GA03-208] What should a subagent's result schema contain for a research task?
- [GA03-209] A subagent returns a summary containing a subtle hallucination and the orchestrator cannot tell. How do you defend against this?
- [GA03-210] When would you let a subagent spawn its own subagents?
- [GA03-211] When would you give a worker agent write access versus keeping all writes in the orchestrator?
- [GA03-212] How would you parallelize a large refactor safely, if not with concurrent write-agents?
- [GA03-213] How would you decide at runtime whether a subtask is safe to parallelise?
- [GA03-214] What are the benefits and bottlenecks of massively parallel agents?
- [GA03-215] What signal tells the primary model in a multi-agent setup that it should escalate rather than guess?
- [GA03-216] What are handoffs in multi-agent systems, and how do they differ from orchestration?
- [GA03-217] How do you evaluate routing quality in a handoff system?
- [GA03-218] What happens to in-flight tool approvals or permissions across an agent handoff?
- [GA03-219] How do you control quality, latency and cost when orchestrating agents dynamically at runtime?
- [GA03-220] What coordination failures would you expect to see in multi-agent traces?
- [GA03-221] How do you debug failures across interacting agents?
- [GA03-222] How would you detect that two sub-agents made conflicting implicit decisions?
- [GA03-223] How do you pass trace IDs across agents for distributed tracing?
- [GA03-224] How do you design a policy engine, permissions and an audit trail for a multi-agent system?

## Agent protocols: A2A and MCP
- [GA03-225] How does the A2A protocol work for agent discovery, task delegation and status queries?
- [GA03-226] What is the difference between A2A and ordinary agent invocation?
- [GA03-227] What does A2A solve that MCP does not, and how do the two compose in a production multi-agent system?
- [GA03-228] What are the responsibility boundaries between RAG, agents, MCP and A2A?
- [GA03-229] How would you design a hybrid A2A + MCP architecture?
- [GA03-230] When would you use A2A for multi-agent orchestration versus keeping all agents in a single framework?
- [GA03-231] Would you ever put A2A between two agents inside your own company, and what would justify the overhead?
- [GA03-232] What are ACP and UCP, and how do MCP, A2A, ACP and UCP together form an agent technology stack?
- [GA03-233] When one agent connects to multiple MCP servers at once, how do you orchestrate their collaboration and resolve conflicts?
- [GA03-234] A peer agent's Agent Card advertises a skill it turns out to do badly. How would you find out, and what do you do?
- [GA03-235] You are exposing one of your agents to another company's agent. What crosses the boundary, and what do you refuse to expose?
- [GA03-236] A peer agent returns a subtly wrong artifact and your agent acts on it. Who is accountable, and what would have caught it?
- [GA03-237] How would you rate-limit a peer agent whose legitimate traffic is genuinely spiky?
- [GA03-238] Your agent buys things on behalf of users. Design the authorisation trail so a disputed transaction is resolvable.
- [GA03-239] A user's constraint said "under 200" and the purchasing agent found an item at 195 plus an 18 delivery fee. Whose reading binds, and where in your design is that decided?
- [GA03-240] What changes in an agent purchasing system when the counterparty is also an agent and no human is present on either side?

## Agent skills and instruction files
- [GA03-241] What are Agent Skills?
- [GA03-242] When do you package knowledge as a skill rather than a tool, an MCP server, or retrieval?
- [GA03-243] How does skill routing work, and why is it similar to RAG but with a different goal?
- [GA03-244] A skill's instructions conflict with your system prompt. Which should win, and how do you make that predictable?
- [GA03-245] How would you evaluate whether an Agent Skill improves outcomes rather than just being loaded?
- [GA03-246] Design a skill system for a fleet of internal agents. How do skills differ from MCP tools and fine-tuning?
- [GA03-247] What risks come from skill or plugin ecosystems for agents, given that static detection has a ceiling?
- [GA03-248] How do you keep an internal registry of agent plugins from becoming a bottleneck?
- [GA03-249] How would you decide whether a rule belongs in the repository instruction file, a linter config, or a skill loaded on demand?
- [GA03-250] What is a CLAUDE.md-style project manifest, and how would you detect that it has gone stale?

## LangChain and LangGraph
- [GA03-251] How does LangChain work, and what are its core modules (models, prompts, chains, memory, agents, retrievers)?
- [GA03-252] What is a LangChain agent, and how does it choose and execute tools?
- [GA03-253] How would you build a knowledge Q&A application with LangChain, from loaders and splitters to retriever and chain?
- [GA03-254] What is the main benefit of LCEL over plain chains of function calls, and how do you keep a LangChain system lean?
- [GA03-255] When should you use LangChain, and when build from scratch? What are the production tradeoffs of an orchestration framework?
- [GA03-256] How does LangGraph work?
- [GA03-257] What are the core differences between LangGraph and LangChain, and when do you use each?
- [GA03-258] Why use a graph-based state machine like LangGraph instead of a simple while loop for agents?
- [GA03-259] Why use LangGraph instead of a managed agent runtime, and when would you hand the loop to a managed runtime instead?
- [GA03-260] How do you handle state overload in a graph with 20+ nodes?
- [GA03-261] How do you design LangGraph State, checkpoints and thread_id, and how do you resume accurately after an interruption?
- [GA03-262] How do you write a reducer when two parallel nodes update 'messages' at the same time in LangGraph?
- [GA03-263] What production problems do node caching and deferred nodes in LangGraph solve?
- [GA03-264] How do you combine retry, timeout and error handlers for fault tolerance in LangGraph?
- [GA03-265] How do you use LangGraph's native features to debug an agent, and what role does a checkpoint play?
- [GA03-266] How do you monitor LangGraph in production, how do time-travel debugging, checkpointing and interrupts work, and how does LangSmith complement them?
- [GA03-267] Your team edits a bad turn in LangGraph and replays from that checkpoint. After switching models, replays start failing with 400 errors. What happened?

## Other frameworks and build-versus-buy
- [GA03-268] How do you choose among production agent frameworks such as LangGraph, Claude Agent SDK, CrewAI, AutoGen, Semantic Kernel, LlamaIndex Agents and Pydantic AI?
- [GA03-269] How do LangGraph and Semantic Kernel compare, and why might a senior engineer choose Semantic Kernel over LangChain?
- [GA03-270] LangChain and LlamaIndex now both have graph and workflow features. How do you choose between them?
- [GA03-271] How does AutoGen implement conversational multi-agent collaboration?
- [GA03-272] How does CrewAI implement role-driven agent collaboration?
- [GA03-273] How do AutoGen and CrewAI differ, and what is the commander pattern for multi-agent collaboration?
- [GA03-274] When would you use CrewAI instead of LangGraph?
- [GA03-275] Microsoft moved AutoGen to maintenance mode in favor of its Agent Framework. How does this affect existing AutoGen deployments?
- [GA03-276] When would you choose Pydantic AI over LangGraph, and what does a typed agent framework buy you in production?
- [GA03-277] Should you build your agent on a framework or roll the loop yourself? Defend a position.
- [GA03-278] Which single piece of agent framework infrastructure would you pay for first, and why?
- [GA03-279] How would you structure agent code so you can swap frameworks later and avoid lock-in across vendor SDKs?
- [GA03-280] How do you pin, lock and isolate dependencies to survive fast-moving AI frameworks?
- [GA03-281] What stays in-house no matter which agent harness you rent?
- [GA03-282] How do Dify, Coze, n8n and similar low-code agent platforms compare with code-first frameworks?
- [GA03-283] How would you design an enterprise AI agent platform similar to a low-code agent builder?

## Human-in-the-loop, approvals and control
- [GA03-284] What is the human-in-the-loop pattern for agents, when is it needed, and which actions should need approval?
- [GA03-285] When should an agent pause for human confirmation, and how would you implement interrupts in LangGraph?
- [GA03-286] Design human-in-the-loop approval for an agent that takes consequential actions.
- [GA03-287] How do you design a human-in-the-loop system that does not fatigue the human operator?
- [GA03-288] What is the over-reliance risk in human-in-the-loop designs, and how do you mitigate approval laundering?
- [GA03-289] You gate agent actions with a classifier that can run, deny or defer to a human. How do you set and monitor the defer threshold?
- [GA03-290] How would you decide the auto-approve threshold for a refund agent?
- [GA03-291] What do you show a user who is approving something they cannot realistically evaluate, like a generated SQL migration?
- [GA03-292] How do you keep human approval gates from destroying UX on a 50-step agent task?
- [GA03-293] Who approves when an agent runs unattended overnight, and what happens when the approver is unavailable?
- [GA03-294] Design the human approval flow for an agent that files expense reports. Where do the gates go, and how do you stop people clicking through them?
- [GA03-295] How do you audit that a human approval of an agent action was meaningful rather than reflexive?
- [GA03-296] How do you evaluate the approval-gate UX of an enterprise agent? What metric says the human is a real check, not a rubber stamp?
- [GA03-297] What does a human approval prompt look like when the unit of action is a script?
- [GA03-298] Where does an agent permission model put the boundary between agent autonomy and approval fatigue?
- [GA03-299] What would you do if an agent kept asking the human too often after you added escalation rules?
- [GA03-300] How do you decide when a coding agent should ask a clarifying question versus proceed?
- [GA03-301] What is your escalation design when an agent stalls mid-task?
- [GA03-302] How do you make an agent's actions reversible, or at least auditable, in a production system?
- [GA03-303] Compare sandboxed and unsandboxed execution for AI agents.
- [GA03-304] The user hits Stop while your agent is mid tool call. What should happen, and how do you design streaming and cancellation for an agent UI?
- [GA03-305] The user hits Stop on an agent, then types "actually, carry on". What does the agent do with the half-finished work?
- [GA03-306] A customer says approval queues defeat the purpose of an agent and wants full autonomy now. What data would change your position?
