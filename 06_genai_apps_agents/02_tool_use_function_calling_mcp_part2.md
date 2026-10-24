---
domain: genai
topic: tool_use_function_calling_mcp
title: Tool use, function calling and MCP
tags: [function-calling, mcp, tool-use]
count: 113
part: 2/2
---
# Tool use, function calling and MCP (part 2)

## MCP fundamentals and architecture
- [GA02-098] What is the Model Context Protocol (MCP), what integration problem does it solve, and why is it often compared to USB-C for AI?
- [GA02-099] What are an MCP client, an MCP server, and a host?
- [GA02-100] Does MCP expose only Tools as capabilities?
- [GA02-101] What are MCP's core primitives (Tools, Resources, Prompts), and what problem does each solve?
- [GA02-102] Describe MCP's client, server and transport layers and how a request flows through them.
- [GA02-103] Which MCP primitives are model-controlled, application-controlled, and user-controlled, and why does that split matter?
- [GA02-104] How does MCP differ from traditional function calling, and how do the two relate?
- [GA02-105] When would you use MCP over a custom tool bus or plain function calling, and when should you not use MCP?
- [GA02-106] You are building one embedded agent with a single latency-sensitive tool surface and sensitive local credentials. Should you use MCP or in-process tools?
- [GA02-107] What are the similarities and differences between MCP and the OpenAI tools API or GPT Actions?
- [GA02-108] How does MCP relate to A2A, and how do the two work together in a production multi-agent system?
- [GA02-109] Why do we need MCP at all? Why not just hand the model an OpenAPI spec and let it call REST endpoints?
- [GA02-110] Your company already has 200 internal REST services. Would you write 200 MCP servers?
- [GA02-111] How would you decide the granularity of MCP servers relative to underlying endpoints?
- [GA02-112] Why is it important to separate tool logic from the agent application using MCP servers?
- [GA02-113] You are designing an MCP server. How do you decide whether something should be a tool, a resource, or a prompt?
- [GA02-114] When would you expose data as an MCP resource instead of a "search" tool?
- [GA02-115] Your MCP server exposes a 500 MB log file as a resource. What goes wrong, and how do you restructure it?
- [GA02-116] When would you use MCP resource templates rather than fixed URIs?
- [GA02-117] What should you watch out for when writing an MCP server?
- [GA02-118] How can MCP serve as a cross-language tool bus, for example wrapping Go business tools and calling them uniformly from Python?
- [GA02-119] After connecting several MCP servers, your agent has over a hundred tool definitions and tens of thousands of schema tokens in context, and tool selection has gotten worse. What do you do?
- [GA02-120] How does an agent or MCP host handle two servers exposing identically named tools, and what name does the model actually see?
- [GA02-121] Walk me through an MCP handshake between a client and a Postgres MCP server.

## MCP transports and protocol operations
- [GA02-122] How do you choose an MCP transport, and which production scenarios suit stdio, SSE and Streamable HTTP?
- [GA02-123] A stdio MCP server randomly breaks the client session after you add debug logging. What is the likely cause?
- [GA02-124] MCP communicates over JSON-RPC 2.0. What error codes exist, and how should a server surface errors and diagnostics?
- [GA02-125] How does capability negotiation work during MCP initialization, and why does it matter when clients and servers evolve independently?
- [GA02-126] How do you monitor an MCP server in production?
- [GA02-127] Why was mandatory long-lived SSE a problem for serverless MCP deployments?
- [GA02-128] What changed with the stateless revision of MCP, and what is the migration impact for servers running behind sticky sessions?
- [GA02-129] How does session state work over the Streamable HTTP transport if the server is stateless?
- [GA02-130] You maintain an MCP server with clients on three different protocol revisions. How do you handle negotiation and deprecation?
- [GA02-131] How do you migrate an existing stateful MCP server fleet to a stateless core without breaking old clients?
- [GA02-132] What breaks if a client retries an MCP call against a server that already applied the side effect?

## Advanced MCP primitives and agent skills
- [GA02-133] What is a Root in MCP, and what is its role in file access control and multi-workspace scenarios?
- [GA02-134] What is the MCP sampling primitive, and why does it let a server exhibit agentic behavior?
- [GA02-135] What types of MCP clients exist, how do internal and external clients differ, and how is the sampling callback implemented?
- [GA02-136] Why does MCP sampling route through the host instead of the server calling a model API directly?
- [GA02-137] What are MCP's sampling and elicitation primitives for, and why does hardly anyone use them?
- [GA02-138] You are writing an MCP host. Would you enable sampling for third-party servers, and what controls would you put on it?
- [GA02-139] A tool call takes twenty minutes, or needs the user's answer halfway through. How do you model that over MCP now that the protocol is stateless?
- [GA02-140] The user answers an MCP elicitation an hour later and the signed state has expired. What should the server do?
- [GA02-141] What is an MCP Server Card, and how does it let AI applications discover and evaluate server capabilities automatically?
- [GA02-142] What are MCP tasks, triggers and events, and why do they let an agent move from passive response to proactive awareness?
- [GA02-143] What is the MCP Registry, and how do you publish and distribute enterprise MCP servers?
- [GA02-144] What are MCP Apps, and what do they change about an MCP server's security model?
- [GA02-145] When a user filters a chart in an MCP App's UI and then asks the model about "these results", how does the model know what they are?
- [GA02-146] What is "Skills over MCP", and why does it let an agent compose multiple tool capabilities dynamically?
- [GA02-147] What is a Skill in an AI application, how do you design its structure (input definition, processing and tool calls, structured output), and how do you handle versioning and regression evaluation?
- [GA02-148] Design a skill system for a fleet of internal agents using Agent Skills. How do skills differ from MCP tools and from fine-tuning?

## MCP authorization, security and enterprise readiness
- [GA02-149] What are the key MCP attack vectors: tool poisoning, confused deputy, token passthrough and SSRF?
- [GA02-150] A third-party MCP server changes a tool description after the user approved it. How do you detect and defend against this kind of rug-pull?
- [GA02-151] How can a stdio-based MCP launch lead to command injection, and how do you migrate away safely?
- [GA02-152] What do the OWASP MCP and agentic top-10 lists add beyond the traditional web top-10?
- [GA02-153] Which actions would you refuse to expose over MCP at all, and why?
- [GA02-154] A vendor's MCP server exposes sixty tools and you need four. How do you constrain it?
- [GA02-155] How does the MCP authorization flow work, and how do protected resource metadata, OAuth 2.1, audience binding and DPoP fit together?
- [GA02-156] How does authorization work for a remote MCP server, and what do teams get wrong when they implement it?
- [GA02-157] Explain MCP's remote transport and authorization model, and the security risks of running MCP servers in production.
- [GA02-158] An agent calls tools on five MCP servers on a user's behalf. How do you authorize it?
- [GA02-159] Your agent connects to a dozen third-party MCP servers over OAuth. How do you stop one malicious server from abusing credentials intended for another?
- [GA02-160] Your MCP server needs to call three upstream SaaS APIs on behalf of the user. How do you obtain and store those tokens?
- [GA02-161] An agent runs unattended overnight and an access token expires mid-run. What happens, and how should it be handled?
- [GA02-162] How would you propagate and verify end-user identity through an MCP tool call down to the retrieval filter?
- [GA02-163] What enterprise-readiness issues must MCP address, including audit trails, enterprise authentication and gateway patterns?
- [GA02-164] How would you build an enterprise MCP gateway for audit, authorization and routing?
- [GA02-165] Design a secure multi-tenant MCP server on the stateless protocol, covering state handles, authorization and rate limiting.

## Code interpreters and sandboxed execution
- [GA02-166] What is a code interpreter tool, and where does it sit in the trade-off between sandboxing and privilege?
- [GA02-167] When is a sandboxed environment mandatory for tool-using agents, and what are the isolation options?
- [GA02-168] Compare Docker, gVisor, WebAssembly and Firecracker for agent sandboxing.
- [GA02-169] How do you build a code execution agent safely using sandboxed environments, including one that runs arbitrary Python?
- [GA02-170] What resource limits and network egress policies would you put on a sandbox that runs model-generated code?
- [GA02-171] An agent's generated code needs installed packages and files that persist across turns. How do you design the sandbox lifecycle (per call, per session, or snapshot) and its security trade-offs?

## Computer-use and browser agents
- [GA02-172] How do computer-use agents work, including the screenshot, reason, act loop?
- [GA02-173] How do browser agents work?
- [GA02-174] When do you choose a computer-use agent over an API integration?
- [GA02-175] Explain the trade-offs between vision-based computer use and API-based tool calling.
- [GA02-176] Compare computer-use agents with Selenium-style scripted automation. When would you choose each?
- [GA02-177] Why are computer-use and browser agents so much harder to make reliable than API-based agents?
- [GA02-178] Given a choice of DOM access versus screenshots for a browser agent, what does DOM access fix and what does it not fix?
- [GA02-179] What errors are specific to computer-use agents, such as misclicks, stale screenshots, scaling mismatches and unexpected dialogs?
- [GA02-180] What do latency and cost per action look like for computer-use agents, and how do you optimize them?
- [GA02-181] What unique challenges do mobile GUI agents face compared with desktop agents?
- [GA02-182] How do you design the action space and the data loop for a GUI agent?
- [GA02-183] Design the perception layer of a computer-use agent: screenshots, coordinates, and the accessibility tree.
- [GA02-184] How would you handle an app with no accessibility tree and a canvas-rendered UI in a computer-use agent?
- [GA02-185] Your computer-use agent passes demos but fails 30% of real workflows in production. Walk through your reliability engineering plan.
- [GA02-186] How would you evaluate a computer-use agent beyond task success rate?
- [GA02-187] A vendor says its computer-use model scores about 82% on a desktop benchmark. How do you turn that into a production capacity plan?
- [GA02-188] A client has 500 insurance claim PDFs per day to enter into a legacy portal with no API. Design the automation.

## Testing, evaluation and versioning of tools
- [GA02-189] What are the three testing layers for a tool-using agent?
- [GA02-190] Design a testing strategy for a customer-support tool-using agent.
- [GA02-191] How do you systematically evaluate function-calling quality, for example with BFCL-style benchmarks, and how do you trace tool-call quality in production?
- [GA02-192] What metrics would you track for tool use: tool-selection accuracy, argument accuracy, redundant calls, and task success? How would you build the eval set?
- [GA02-193] How do you evaluate a change to a tool description in a function-calling agent?
- [GA02-194] How would you measure whether a tool-surface change actually improved an agent, and on what eval set?
- [GA02-195] How do you evaluate semantic (not just syntactic) tool-call accuracy without logging user requests?
- [GA02-196] How do you regression-test 100+ agent tools without 100 live sandboxes?
- [GA02-197] How do you safely test new tools against a live agent?
- [GA02-198] How would you evaluate the reliability of an MCP wrapper around an internal API?
- [GA02-199] How do you evaluate a retrieval tool when the metric is now "did the agent's task succeed" rather than recall@k?
- [GA02-200] Your agent depends on MCP servers owned by three other teams. How do you test so a change on their side does not silently break your agent?
- [GA02-201] A provider adds an optional parameter to a tool and tool-selection accuracy drops 6%. Whose bug is it, and who fixes it?
- [GA02-202] How do you test tool description changes without paying for full agent evals on every provider commit?
- [GA02-203] How would you version tools and keep backwards compatibility?
- [GA02-204] How do you change a tool's schema when customer agents already depend on the old one?
- [GA02-205] How would you version tool schemas without invalidating every saved agent trajectory?

## End-to-end design scenarios
- [GA02-206] How would you design a tool-using agent that automates invoice processing for thousands of invoices per day?
- [GA02-207] Design the tool layer for a customer-support agent that can look up orders, issue refunds and escalate to humans. Cover schemas, permissions, idempotency and failure handling.
- [GA02-208] The PM says: "Users should be able to use our product from inside ChatGPT and Claude." What do you build, and what changes about how you design the product?
- [GA02-209] A customer wants agents on other vendors' platforms to read and act on their ontology over MCP. How do you expose it without losing the governance that made the ontology worth building?
- [GA02-210] You are asked to give an LLM safe read-write access to an internal data warehouse. Which tools, permissions, and guardrails do you design?
