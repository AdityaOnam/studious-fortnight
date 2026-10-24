---
domain: genai
topic: tool_use_function_calling_mcp
title: Tool use, function calling and MCP
tags: [function-calling, mcp, tool-use]
count: 97
part: 1/2
---
# Tool use, function calling and MCP (part 1)

## Function calling basics
- [GA02-001] What is function calling in LLMs, and how does it let an agent act on the outside world?
- [GA02-002] How does function calling work end to end, from tool schema to feeding the result back to the model?
- [GA02-003] What fields does a tool call contain, and why does each call carry an ID that must be echoed back with its result?
- [GA02-004] A teammate says "the model executes the tool." What is wrong with that, and why does the distinction matter?
- [GA02-005] How does an agent decide when to call a tool versus answering from its own knowledge?
- [GA02-006] When should the model ask a clarifying question instead of calling a tool with guessed arguments?
- [GA02-007] What is the difference between structured output and function calling, and when would you use each?
- [GA02-008] What do function calling, MCP, and agents each handle, and what problem does each solve?
- [GA02-009] How does function calling map onto an HTTP API, and how does an MCP tool relate to an ordinary HTTP API?
- [GA02-010] What are Agent Skills, and how do they differ from prompts, tools or function calling, and MCP?
- [GA02-011] Explain parallel tool calls and tool-choice forcing. When would you use each?
- [GA02-012] Why might you force a required tool call on the first iteration of an agent loop but use "auto" afterwards?
- [GA02-013] What happens if you return tool results in a different order than the calls were issued?
- [GA02-014] You are building a production agent that calls tools. What makes the loop reliable enough to ship?
- [GA02-015] How do open-weight models implement tool calling (chat templates, special tokens, fine-tuning), and how does that differ from hosted APIs?
- [GA02-016] What are the pitfalls of putting tool-call schemas inside chat templates?
- [GA02-017] Why do providers use constrained decoding for tool arguments but not for choosing which tool to call?
- [GA02-018] How would you fine-tune a model to improve its tool-calling ability, and what training data would you need?

## Tool definition, design and selection
- [GA02-019] How do you design and define tools for an AI agent?
- [GA02-020] Why is the tool description so important when registering tools for an agent?
- [GA02-021] What makes a good tool definition? Give concrete design rules for names, descriptions and parameters.
- [GA02-022] Consolidated versus granular tools: how do you decide?
- [GA02-023] How does per-call latency change the decision between consolidated and granular tools?
- [GA02-024] When would you split one consolidated agent tool into two?
- [GA02-025] How many tools is too many, and how do you design tool schemas an LLM can use correctly?
- [GA02-026] You are exposing retrieval as a tool to an agent. How does designing the tool interface differ from designing a retrieval API, and what changes if it is exposed over MCP?
- [GA02-027] Design the tool set for an agent that manages a Postgres database. Where do you consolidate?
- [GA02-028] Design the tool surface for a coding agent: which tools exist, what their schemas look like, how results come back, and how errors are handled.
- [GA02-029] Your agent keeps picking the wrong tool. How do you improve tool selection?
- [GA02-030] An agent keeps picking the wrong one of two similar tools. What are your first three fixes?
- [GA02-031] How would you detect in production that two tools are being confused by the model?
- [GA02-032] Your LLM selects the right tool but extracts the wrong parameters. How do you fix parameter extraction?
- [GA02-033] Your AI agent hallucinates tool capabilities and passes wrong inputs. How do you fix it?
- [GA02-034] What is tool-call hallucination, and how do you defend against it?
- [GA02-035] Why is a fabricated-but-valid ID worse than a call to a nonexistent tool?
- [GA02-036] Does strict or constrained decoding eliminate tool-call hallucination?
- [GA02-037] You need to give an agent access to 200 internal tools. How do you handle schema overload?
- [GA02-038] An agent has grown to 90 strict tool definitions; the model increasingly calls the wrong tool with perfectly valid arguments and latency is up. What is the strongest fix?
- [GA02-039] How would you build a search_tools capability for dynamic tool discovery without adding a round trip to every task, and how do you change the tool set mid-session without losing the prompt cache?
- [GA02-040] A model call must pick among tools that overlap in purpose. How would you use few-shot examples, descriptions, and tool_choice constraints to disambiguate?

## Tool execution, errors and safety
- [GA02-041] How do you handle tool-call errors, timeouts and retries in an agentic loop?
- [GA02-042] How should tool errors be surfaced to the model so it can self-correct?
- [GA02-043] Should transient infrastructure errors (timeouts, 502s, 503s) reach the model or be retried silently by the executor? What should a tool return so the agent loop behaves well?
- [GA02-044] Design a retry strategy for tool failures, including exponential backoff with jitter and a circuit breaker.
- [GA02-045] How would you measure whether your tool error messages are actually working?
- [GA02-046] How do you stop an agent from getting stuck in an infinite loop of repeated failing tool calls?
- [GA02-047] Parallel tool calls: when do they help and what do they break?
- [GA02-048] How do you handle parallel tool calls with dependencies, timeouts and mixed success, such as one failure among five calls?
- [GA02-049] Your agent charged a customer's card twice, yet the trace shows one tool call. What happened, and how do you prevent it?
- [GA02-050] The model itself decides to call a charge tool twice because it forgot it already did. Does an idempotency key save you?
- [GA02-051] How do you handle a tool that is not idempotent and cannot be made so?
- [GA02-052] How do you prevent a tool from executing twice when a stream retry replays the tool call?
- [GA02-053] How do you handle streaming when the model is emitting tool calls or structured JSON?
- [GA02-054] How would you stream tool calls and partial results to a front end?
- [GA02-055] How do you choose between SSE and WebSocket for streaming LLM or agent output?
- [GA02-056] Where would you implement human approval for a delete_records tool, in the prompt or in the executor, and why?
- [GA02-057] How do you design tool permissions for an agent, and how do you stop human approval gates from becoming rubber-stamping?
- [GA02-058] In an LLM tool-calling system, where does per-user permission enforcement belong: the tool, a decorator, or the downstream service?
- [GA02-059] An agent can call your internal APIs as tools. What are the security and reliability implications for those endpoints?
- [GA02-060] How do you prevent an AI agent from causing damage through tool calls?
- [GA02-061] How would you protect a database tool from agent-driven SQL injection?
- [GA02-062] A customer's agent calls your search tool 50 times per task. Do you throttle it or redesign the tool?

## Tool outputs and context efficiency
- [GA02-063] How should tool results be formatted before they go back into the model's context?
- [GA02-064] What does the Observation step in ReAct imply for how you design tool output formats?
- [GA02-065] How do you make tool outputs token-efficient, and why does it matter so much for agents?
- [GA02-066] How do you handle a tool that returns 100k tokens of JSON?
- [GA02-067] How would you decide the truncation limit for a given tool's output?
- [GA02-068] Why is a paginated tool result better than a truncated one for an agent, given both hide data?
- [GA02-069] When is truncating tool outputs actively dangerous?
- [GA02-070] What is progressive disclosure for agent skills, and why not load every skill into context?
- [GA02-071] What is programmatic tool calling, and when is it better than model-orchestrated chaining? What are the main composition patterns?
- [GA02-072] When an agent writes code against an API instead of calling exposed function definitions, at how many tools or how large a result does the code approach start paying for itself?
- [GA02-073] A tool returns a web page or document that contains instructions aimed at the model. How should tool-result handling reduce the risk of indirect prompt injection?
- [GA02-074] Why should tool results include human-readable names next to opaque IDs?

## Structured outputs and JSON reliability
- [GA02-075] What are output parsers, and why are they needed for production applications?
- [GA02-076] How would you structure a prompt so the LLM outputs a specific, parsable format such as JSON or YAML?
- [GA02-077] Why can't structured output rely on the prompt alone, and why is JSON mode more reliable? What do JSON Schema, function calling and server-side validation each solve?
- [GA02-078] What is the difference between JSON mode and Structured Outputs?
- [GA02-079] How do you get reliable structured output from a model in production, and what happens when it fails anyway?
- [GA02-080] How is Pydantic v2 used to get structured LLM outputs?
- [GA02-081] How do you handle invalid or partial JSON from an LLM in production?
- [GA02-082] You set temperature=0 and parse the reply with json.loads(). It works in dev, then crashes intermittently in production. What is the explanation and the fix?
- [GA02-083] With strict structured outputs on, you still occasionally get JSON that ends mid-object with stop_reason="max_tokens". What is happening and what is the right response?
- [GA02-084] Your extraction schema requires owner: str (non-null). On documents with no owner, the model invents a plausible name. What is the best fix?
- [GA02-085] What is the risk of asking an LLM for too many structured fields at once?
- [GA02-086] The JSON is always valid, yet a field is wrong on a noticeable fraction of responses and schema checks pass. How do you catch and fix valid-but-wrong values?
- [GA02-087] An LLM ticket-classification pipeline using structured outputs misclassifies urgent tickets as low priority. What is your fastest fix within the hour?
- [GA02-088] How do you version the output schema when the prompt and the consuming code deploy separately?
- [GA02-089] What is the difference between a schema validation failure and a semantic validation failure, and how does your retry-with-feedback loop treat each?

## Constrained decoding and strict mode
- [GA02-090] What does strict mode on a tool schema guarantee, and what does it leave to you? Would you ever turn it off?
- [GA02-091] Your extraction schema has 40 fields and uses keywords that strict mode rejects. What do you do?
- [GA02-092] Compare JSON mode with schema-constrained decoding. How does constrained decoding actually enforce the schema?
- [GA02-093] Why can constrained decoding change the output distribution rather than just filter invalid outputs, and why can it hurt answer quality? How do you mitigate that?
- [GA02-094] How would you implement constrained decoding for a non-JSON DSL?
- [GA02-095] How would you make streaming output usable when the format is JSON, for example rendering a 10-item array progressively, and where would you validate?
- [GA02-096] Your extraction service forces a tool call to get JSON back. After switching to a newer model, every request returns HTTP 400. What are the likely causes and how do you keep the schema guarantee?
- [GA02-097] How would you allow reasoning or free-text explanation before the final structured answer without breaking schema guarantees?
