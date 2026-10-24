---
domain: genai
topic: agents_planning_memory_multiagent
title: Agents: planning, memory, multi-agent
tags: [agents, multi-agent, memory, langgraph]
count: 96
part: 4/4
---
# Agents: planning, memory, multi-agent (part 4)

## Agent evaluation: metrics and benchmarks
- [GA03-307] How do you evaluate and test an agent, as opposed to a single model response, and what does a test case look like?
- [GA03-308] Why is evaluating agents more complex than evaluating ordinary Q&A and RAG systems?
- [GA03-309] In agent evaluation, what are a task, a trial, a grader and a transcript?
- [GA03-310] Compare trajectory evaluation and final-outcome evaluation of agents. When does each fail?
- [GA03-311] How do you evaluate an agent's capabilities, and what do the mainstream agent benchmarks measure?
- [GA03-312] How would you evaluate an LLM agent on long-horizon tasks, and which failure categories would you track?
- [GA03-313] Define task success rate, action success rate and unit cost per task for agents.
- [GA03-314] Your agent's final answers look fine, but its cost is creeping up and some runs take many extra tool calls. Which eval surfaces this?
- [GA03-315] You are reporting reliability for a customer-facing support agent. Which metric should the SLA use?
- [GA03-316] You inherit an agent with no evals and a vague "make it better" mandate. What is the right first move?
- [GA03-317] How do you build an evaluation harness for an agent? Design an eval suite for a coding agent covering three metric categories.
- [GA03-318] Explain pass@k versus pass^k. Why does the distinction matter for production agents?
- [GA03-319] Your agent has pass@1 of 80% and pass^4 of 40%. What does that tell you and what do you try first?
- [GA03-320] When is best-of-n with a verifier a legitimate way to convert pass@k into pass^1?
- [GA03-321] How many scenarios do you need before a pass^k number means anything?
- [GA03-322] Your agent passes 92% of eval tasks. Why might that number be misleading, and what would you measure instead?
- [GA03-323] An agent scores 90% pass@1 on your benchmark and fails constantly in the customer's staging environment. What did your benchmark miss?
- [GA03-324] A vendor shows 90% agent success on their own environment suite. What do you ask before buying?
- [GA03-325] How would you evaluate whether an agentic model is actually good, beyond a single benchmark number?
- [GA03-326] How would you benchmark an LLM agent's tool use for enterprise workflows composing 10+ APIs?
- [GA03-327] How do you inject and score mid-episode failures when benchmarking an agent's tool use?
- [GA03-328] What is agent harness engineering, and how do you put LLM-as-a-Judge, trajectory analysis and chaos engineering into practice for evaluating agents?
- [GA03-329] How would you do trajectory grading with agent-as-judge, and what new failure modes does it add?
- [GA03-330] What rubric items would you give an LLM judge for a support agent?
- [GA03-331] How do you control the ROI of an AI agent, and which metrics matter?
- [GA03-332] Your agent's success rate at four-hour tasks doubled after a model upgrade, but cost per success tripled. Is that a win?

## Agent evaluation: environments and testing
- [GA03-333] How do you evaluate an agent when the environment is non-deterministic, such as the open web?
- [GA03-334] How do you build a resettable environment for evaluating an agent that touches three external SaaS APIs?
- [GA03-335] How do you evaluate an agent whose tools hit non-resettable third-party APIs?
- [GA03-336] How do you test an agent without real side effects, and how do you test an agent's write path without touching a production system?
- [GA03-337] How would you build a deterministic replay harness for agent evals, and what does it genuinely buy you?
- [GA03-338] In a replay harness for agent evals, how do you detect that your recordings have gone stale?
- [GA03-339] Where does a mocked sandbox for agent evals stop being worth its maintenance cost, and when is a live staging environment cheaper?
- [GA03-340] Your agent handles multi-turn conversations where users change their minds, and static test cases cannot cover that. Build me an evaluation environment.
- [GA03-341] Your agent overfits to the evaluation simulator's quirks and regresses in production. How do you detect that?
- [GA03-342] Where does the simulated-user approach for evaluating conversational agents systematically diverge from real users?
- [GA03-343] The space of possible conversations is effectively infinite. How do you evaluate a conversational agent before launch?
- [GA03-344] What does it mean when an agent games its evaluation harness, and how do you detect it?
- [GA03-345] Your agent now runs tasks that take hours and hundreds of steps. How do you evaluate and observe it?
- [GA03-346] How do you write milestones for an agent task with many valid paths without punishing unconventional ones?
- [GA03-347] Design a testing strategy for a tool-use agent that handles customer support.
- [GA03-348] How do you regression-test an agent before a model upgrade or when the underlying model version changes?
- [GA03-349] How do you regression-test a fix to step 7 of a long multi-step agent run without paying for steps 1 to 6 on every run?
- [GA03-350] How would you write a regression test for a non-deterministic reproduction of an agent bug?
- [GA03-351] You are handed a small unfamiliar agent codebase. Users report it sometimes confirms an order that was never actually placed. How do you debug it?
- [GA03-352] How do you evaluate an LLM workflow before and after giving it access to production operations?
- [GA03-353] Your agent's regression suite passes, yet users report quality regressions in long conversations. What eval gaps would you look for?
- [GA03-354] What should a good agent trace record so that a failed run can be diagnosed and replayed later?

## Coding agents: design
- [GA03-355] What matters more for an agentic coding tool, the model or the harness? Design the agent loop.
- [GA03-356] What is the agent mode of AI coding tools, and how does it differ from ordinary code completion?
- [GA03-357] How do coding agents like Claude Code, Cursor and Copilot differ in architecture and workflow?
- [GA03-358] How does a coding agent's plan, execute, test and fix loop work?
- [GA03-359] You have eight hours to build a coding agent from scratch. What do you build, and more importantly, what do you cut?
- [GA03-360] If you had more time to extend a from-scratch coding agent, which single tool would you add first, and why?
- [GA03-361] Design the harness for an agent that makes multi-file changes from a natural-language task. How do you keep it from wrecking a codebase?
- [GA03-362] Your coding agent spends over half its first turn just finding the relevant code. How do you fix that?
- [GA03-363] The agent model outputs an edited version of a 500-line file, and applying it verbatim is slow and error-prone. How do you make "apply" fast and reliable?
- [GA03-364] When does the split of planning with a frontier model and applying edits with a small model break down?
- [GA03-365] An asynchronous cloud coding agent and an in-editor coding agent are different products. What actually changes between them technically?
- [GA03-366] Between an asynchronous cloud coding agent and an in-editor agent, which would you ship a new tool to first, and why?
- [GA03-367] How would you decide whether a task should be handed off from the IDE to an asynchronous agent session?
- [GA03-368] How would you evaluate an autonomous coding agent, and why can SWE-bench pass rates be misleading or gamed?
- [GA03-369] What single metric would you show a customer instead of a benchmark score when evaluating an autonomous software engineering agent?

## Coding agents: CI, review and testing
- [GA03-370] Leadership wants coding agents running unattended in CI to fix flaky tests, bump dependencies and draft PRs from tickets. What guardrails do you build, and how do you control cost?
- [GA03-371] How do you measure whether agent-authored PRs are worth the review time they consume?
- [GA03-372] Is it safe to run a coding agent in auto-approval mode on developer laptops?
- [GA03-373] How would you test an AI coding agent in CI?
- [GA03-374] Would you let an AI reviewer's approval count toward required reviews?
- [GA03-375] How do you stop an LLM PR-review agent's comments from becoming noise that developers learn to ignore?
- [GA03-376] Would you let an LLM security agent auto-fix low-severity findings, and with what controls?
- [GA03-377] We want an AI agent to maintain our end-to-end test suite by generating tests from the running app and auto-healing broken ones. What is your position, and what guardrails do you add?
- [GA03-378] An auto-healed test locator passes on both builds but now targets a different button with the same accessible name. How would you catch that?
- [GA03-379] What auto-heal rate would make you stop trusting a test, and what do you do with it?

## Customer-facing, GUI and enterprise agents
- [GA03-380] How do you build a customer support agent with escalation logic?
- [GA03-381] Design the human-handoff path for a customer-service agent. When should it escalate, and what does a good handoff look like?
- [GA03-382] Should a customer-service agent stay in the loop after handoff, for example by drafting replies for the human?
- [GA03-383] How does a customer-facing agent handle the customer changing their goal mid-flow?
- [GA03-384] Design an agent that operates a web browser to complete multi-step tasks. How do you make it reliable enough to ship?
- [GA03-385] Websites A/B-test and change layouts constantly. How does a browser-operating agent stay robust?
- [GA03-386] Your computer-use agent passes demos but fails 30 percent of real workflows. What is your reliability plan?
- [GA03-387] For a GUI-operating agent, why is verifying state after each action more important than a perfect plan up front?
- [GA03-388] How do you keep a GUI agent working when a target app redesigns its UI?
- [GA03-389] How do you build the training data, action space and evaluation loop for a GUI agent, and when must it request human takeover?
- [GA03-390] In a cloud-based phone-automation agent product, where do you draw the line for actions that require user confirmation?
- [GA03-391] The user backgrounds the app while an agent is mid-plan with two actions already executed. How do you resume, and which tools would you let auto-execute?
- [GA03-392] Design an LLM agent that files and updates work orders in a customer's ERP with real writes to production. How do you make that safe and stage it?
- [GA03-393] Design an agent that automates an enterprise workflow, such as drafting RFP responses from internal documents and a CRM. What does enterprise-grade add?
- [GA03-394] Design an agent that takes actions in enterprise tools (file a Jira ticket, draft an email) on a user's behalf. How do you handle permissions and evaluation?
- [GA03-395] Design agent orchestration across dozens of connected SaaS systems. Where is authorization enforced, and why can it not live in the model?
- [GA03-396] Design an agent that takes actions in a spreadsheet, such as inserting a pivot table of Q3 sales by region, covering orchestration, tools and failure handling.
- [GA03-397] How would you make an agent's document edits idempotent when it is re-run on a document it already edited?
- [GA03-398] What is your rollback story when a user rejects half of an agent's redlines and asks for another pass?
- [GA03-399] An agent builds and edits customer agents from plain-English instructions, SOPs and call transcripts. How do you stop it shipping a broken or unsafe agent?
- [GA03-400] Design an agentic AI system that can autonomously adapt to new tasks.
- [GA03-401] Design an always-on personal agent that keeps working while the user is away. What does it need beyond a chat agent, including architecture and security concerns?
- [GA03-402] For a long-running research agent, how do you show progress and let the user steer mid-task without restarting?
