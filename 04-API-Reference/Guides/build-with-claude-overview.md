---
title: "Features overview - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/overview"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-13T06:33:56Z"
tags: ["agents", "api"]
---

# Features overview

Copy page



Explore Claude’s advanced features and capabilities.

Copy page



For each feature’s eligibility under zero data retention (ZDR) and HIPAA readiness, see [API and data retention](../Other/manage-claude-api-and-data-retention.md#feature-eligibility).

For administration and governance, see the [Admin API](../Other/manage-claude-admin-api.md), the [Usage and Cost Analytics API](../Other/manage-claude-usage-cost-analytics-api.md), and the [Compliance API](../Other/manage-claude-compliance-api.md).

## Platform features

Features of the Claude Platform that work across its APIs. Each feature’s page says where you can use it.



You can discover which capabilities a model supports programmatically. The [Models API](../Endpoints/models-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. returns `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.

| Feature | Description |
|----|----|
| [Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md) | Lets a faster executor model consult a more capable advisor model mid-generation for a plan or a course correction. |
| [Agent Skills](../Agents-Tools/agents-and-tools-agent-skills-overview.md) | Reusable packages of instructions, metadata and optional scripts that Claude uses automatically when they are relevant to a task. |
| Part of Agent Skills: [Custom Skills](build-with-claude-skills-guide.md#managing-custom-skills) | Skills you write and upload to your workspace. |
| Part of Agent Skills: [Pre-built Agent Skills](../Agents-Tools/agents-and-tools-agent-skills-overview.md#pre-built-agent-skills) | Anthropic’s pre-built skills for PowerPoint, Excel, Word and PDF files. |
| [Batch processing](build-with-claude-batch-processing.md) | Processes many Messages API requests asynchronously in one batch, at half the standard price. |
| [Browser and computer use SDK toolsets](../Agents-Tools/agents-and-tools-tool-use-browser-use-sdk.md) | Classes in the Python and TypeScript SDKs that connect the browser use or computer use tool to a browser or desktop that you supply. |
| [Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md) | Lets Claude navigate, read, and interact with webpages in your own browser environment. |
| [Citations](build-with-claude-citations.md) | Claude’s answers about your documents cite the exact passages that support each claim. |
| [Classifier refusals](build-with-claude-refusals-and-fallback.md) | Safety classifiers on some models can decline a request; the decline comes back as a normal response, not an error. |
| Part of Classifier refusals: [Client-side fallback](build-with-claude-refusals-and-fallback.md#client-side-fallback) | A middleware in the Anthropic SDKs that retries a refused request on the fallback models you list. |
| Part of Classifier refusals: [Fallback credit](build-with-claude-fallback-credit.md) | Bills a retry of a refused request on another model as if the conversation had been on that model from the start, so you do not pay the prompt-cache write twice. |
| Part of Classifier refusals: [Server-side fallback](build-with-claude-refusals-and-fallback.md#server-side-fallback) | The API retries a refused request on a fallback model within the same call and returns one response. |
| [Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) | Gives Claude screenshot, mouse, and keyboard control of a desktop environment. |
| [Custom tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md) | Tools you define with a name, description and input schema. Claude asks to call them; your code runs them and returns the result. |
| [Data residency](../Other/manage-claude-data-residency.md) | Controls for where model inference runs (inference geo) and where data is stored at rest (workspace geo). |
| [Effort](build-with-claude-effort.md) | A setting that controls how many tokens Claude spends on a response, trading thoroughness for token efficiency. |
| Part of Effort: [Per-message effort](build-with-claude-effort-per-message.md) | Changing the effort level for later turns of a conversation with a per-message `output_config`, which keeps the prompt cache. |
| [Fast mode](build-with-claude-fast-mode.md) | Up to 2.5 times more output tokens per second from supported models, at premium pricing. |
| [Files API](build-with-claude-files.md) | Upload a file once and refer to it by `file_id` in later requests, and download files that skills or the code execution tool create. |
| [MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md) | Connect Claude to remote MCP servers so it can call their tools, without running your own MCP client. |
| Part of MCP connector: [Client-side MCP helpers](../Agents-Tools/agents-and-tools-mcp-connector.md#client-side-mcp-helpers) | SDK helpers that convert between MCP types and Claude API types, for when you run your own MCP client, for example for local servers, prompts or resources. |
| [MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md) | Connect Claude to MCP servers inside your private network over an outbound-only connection, with no inbound ports open. |
| [Mid-conversation system messages](build-with-claude-mid-conversation-system-messages.md) | A system instruction added partway through a conversation, without changing the top-level system prompt or the cached prefix before it. |
| Part of Mid-conversation system messages: [Mid-conversation tool changes](build-with-claude-mid-conversation-system-messages.md#mid-conversation-tool-changes) | Offer or withdraw tools partway through a conversation without changing the tools array, so the cached prefix stays valid. |
| Part of Mid-conversation system messages: [Turn-scoped system messages](build-with-claude-mid-conversation-system-messages.md#turn-scoped-system-messages) | A mid-conversation system message that applies only until the next user message, then stays in the history but renders nothing and costs no input tokens. |
| [Multilingual support](build-with-claude-multilingual-support.md) | Claude works in many languages, with strong performance relative to English. |
| [OpenTelemetry](../Other/manage-claude-opentelemetry.md) | Traces your Messages API requests, tool uses, and Managed Agents sessions with OpenTelemetry spans from the Anthropic SDK and the Claude API. |
| Part of OpenTelemetry: [API tracing](../Other/manage-claude-opentelemetry-api.md) | OpenTelemetry spans that the Claude API sends to your observability platform for each model request and tool use that it runs. |
| Part of OpenTelemetry: [SDK tracing](../Other/manage-claude-opentelemetry-sdk.md) | OpenTelemetry spans that the Anthropic SDK emits in your application for each request it sends and each tool that its tool runner runs. |
| [Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md) | Claude can call several tools in one response. |
| [PDF support](build-with-claude-pdf-support.md) | Send PDFs to Claude so it can read the text, pictures, charts and tables in them. |
| [Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md) | Lets Claude call your tools from code in the code execution container, instead of one model round trip for each call. |
| [Prompt caching](build-with-claude-prompt-caching.md) | Reuses a cached prompt prefix from a recent request to reduce processing time and cost. |
| Part of Prompt caching: [1-hour duration](build-with-claude-prompt-caching.md#1-hour-cache-duration) | A 1-hour prompt cache lifetime, for a higher cache write price than the 5-minute default. |
| Part of Prompt caching: [5-minute duration (default)](build-with-claude-prompt-caching.md#how-prompt-caching-works) | The default prompt cache lifetime. Each use of the cached content refreshes it at no extra cost. |
| Part of Prompt caching: [Automatic caching](build-with-claude-prompt-caching.md#automatic-caching) | Prompt caching with one top-level `cache_control` field: the cache breakpoint goes on the last cacheable block and moves forward as the conversation grows. |
| Part of Prompt caching: [Cache diagnostics](build-with-claude-cache-diagnostics.md) | Compares a request with your previous one and reports where the prompt prefix changed, to explain cache misses. |
| Part of Prompt caching: [Explicit cache breakpoints](build-with-claude-prompt-caching.md#explicit-cache-breakpoints) | Prompt caching with `cache_control` on individual content blocks, to choose exactly what is cached. |
| [SDK middleware](../Other/cli-sdks-libraries-middleware.md) | A hook in the Anthropic SDKs that runs your code before each request is sent and after its response is received. |
| [Search results](build-with-claude-search-results.md) | Content blocks that hold your own search results, with a source and title, so Claude can cite them the same way it cites web search results. |
| [Service tiers](../Endpoints/service-tiers.md) | Lets a request use your organization’s Priority Tier capacity. |
| [Session budgets](../Other/managed-agents-budgets.md) | A hard spending limit in US dollars on one session, measured at public list prices. |
| [Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md) | A streamed response ends with `stop_reason` `"refusal"` when streaming classifiers stop it for a possible policy violation. |
| [Structured outputs](build-with-claude-structured-outputs.md) | Constrains Claude’s response to a JSON schema that you give, so the output is valid and parseable. |
| [Task budgets](build-with-claude-task-budgets.md) | Tells Claude how many tokens it has for a full agentic loop, so it can plan its work and finish before the budget runs out. |
| [Thinking](build-with-claude-thinking.md) | Claude works through a problem in thinking blocks before it writes its answer. |
| Part of Thinking: [Adaptive thinking](build-with-claude-thinking-steering-and-cost.md) | Thinking mode in which Claude decides, for each request, whether to think and how much. |
| Part of Thinking: [Extended thinking](build-with-claude-extended-thinking.md) | Manual thinking mode in which you set a fixed thinking token budget (`budget_tokens`) on each request. |
| Part of Thinking: [Preserved thinking](build-with-claude-preserved-thinking.md) | Claude uses thinking blocks from earlier turns only if the current model can read them and nothing before them (system prompt, tools, earlier messages) has changed. |
| [Threshold compaction](build-with-claude-compaction-threshold.md) | Automatic compaction: when a conversation reaches a token threshold, the API summarizes older context inside the request. |
| [Token counting](build-with-claude-token-counting.md) | Counts the tokens in a message before you send it to Claude. |
| [Tool runner](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md) | An SDK helper that runs the tool-use loop for you: it runs your tools when Claude calls them and sends the results back. |
| [Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md) | Lets Claude search your tool catalog and load only the tool definitions it needs. |
| [Vision (images)](build-with-claude-vision.md) | Claude can read and analyze images that you send to it. |
| [Web domain restrictions](../Other/managed-agents-tools-web-restrictions.md) | Lists of allowed or blocked domains that control which sites the web search and web fetch tools can reach. |
| [Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md) | A server tool that lets Claude get the full content of web pages and PDF documents at given URLs. |
| [Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md) | A server tool that lets Claude search the web for current information. |

## Messages API features

| Feature | Description |
|----|----|
| [Apple Foundation Models](../Other/cli-sdks-libraries-libraries-apple-foundation-models.md) | A Swift package that makes Claude available as a language model in Apple’s Foundation Models framework. |
| [Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md) | Lets Claude request shell commands, which run in a bash session that keeps its state between commands. |
| [Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) | Lets Claude run Python and Bash code in a sandboxed container. |
| [Context editing](build-with-claude-context-editing.md) | Clears selected content, such as old tool results or old thinking blocks, from the conversation history as it grows. |
| [Forced tool use](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md#forcing-tool-use) | Makes Claude call a tool, or one specific tool, instead of answering directly. |
| [Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md) | Lets Claude store and read information across conversations in a directory of memory files. |
| Part of Memory tool: [Memory tool helpers](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md#implement-the-memory-handler) | SDK helpers that handle the memory tool’s interface and tool-use loop, so your code supplies only the storage. |
| [Message streaming](build-with-claude-streaming.md) | Receiving a Messages API response incrementally, as server-sent events, while it is generated. |
| Part of Message streaming: [Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md) | Streams a tool’s input to your client as Claude writes it, without the server first buffering and checking the JSON. |
| [Message threads](build-with-claude-message-threads.md) | Give long-running agents a faster time to first token, especially in long conversations, by sending only the new messages on each request. |
| [On-demand compaction](build-with-claude-compaction-on-demand.md) | Replaces the earlier messages of a conversation with a summary that Claude writes when your application asks for it. |
| Part of On-demand compaction: [Background compaction](build-with-claude-compaction-background.md) | Runs the on-demand compaction request while the conversation continues on its full history, then swaps in the summary when it arrives. |
| Part of On-demand compaction: [Compaction and preserved thinking](build-with-claude-compaction-thinking-blocks.md) | Thinking blocks in the turns you keep after on-demand compaction can stay valid, under stated conditions, on models with preserved thinking. |
| Part of On-demand compaction: [Keep-tail compaction](build-with-claude-compaction-keep-recent-turns.md) | On-demand compaction that summarizes the older turns and keeps the last few turns word for word after the summary. |
| Part of On-demand compaction: [Tool runner compaction helper](build-with-claude-compaction-on-demand.md#compact-in-a-loop) | A method on the SDK tool runner that sends the compaction request for you once the current turn and its tool calls finish. |
| [OpenAI SDK compatibility](../Other/cli-sdks-libraries-libraries-openai-sdk.md) | A compatibility layer that lets you call the Claude API with the OpenAI SDK, meant for testing and comparing models. |
| [Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md) | Makes Claude’s tool inputs always match the tool’s JSON Schema. |
| [Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md) | Lets Claude view, create, and edit text files with an Anthropic-defined tool. |
| [Typed structured output helpers](build-with-claude-structured-outputs.md#usage) | SDK helpers that build the JSON schema from a type in your code and parse Claude’s response into that type. |

## Managed Agents features

| Feature | Description |
|----|----|
| [Agent configurations](../Other/managed-agents-agent-setup.md) | A reusable, versioned configuration of the model, system prompt, tools, MCP servers and skills that a session runs. |
| [Agent toolset](../Other/managed-agents-tools.md) | A set of built-in tools (bash, read, write, edit, glob, grep, web fetch and web search) that the agent uses in its sandbox. |
| [Cloud sandboxes](../Other/managed-agents-environments.md) | Isolated Linux containers on Anthropic-managed infrastructure where a session’s tools and code run. |
| [Console agent builder](../Other/managed-agents-onboarding.md) | A visual interface in the Claude Console to create, configure and test agents. |
| [Dreams](../Other/managed-agents-dreams.md) | A job that reads a memory store and past session transcripts and writes a new, reorganized memory store. |
| [Event deltas](../Other/managed-agents-event-deltas.md) | Live previews of the agent’s response text on the session event stream while the model is still generating it. |
| [GitHub access](../Other/managed-agents-github.md) | Access to GitHub from a session: repositories mounted in the sandbox, and the GitHub MCP server for pull requests. |
| [Memory stores](../Other/managed-agents-memory.md) | Collections of text documents that an agent reads and writes, so that information persists across sessions. |
| [Multiagent orchestration](../Other/managed-agents-multiagent-orchestration.md) | Lets the agent of a session hand work to other agents, as subagents or in workflows, and consult an advisor model. |
| Part of Multiagent orchestration: [Dynamic workflows](../Other/managed-agents-workflow-runs.md) | Programs that an agent writes to run many agents in the background and combine their results. |
| Part of Multiagent orchestration: [Session threads](../Other/managed-agents-session-threads.md) | The thread in which each agent of a multiagent session works, which you can list, stream, interrupt and archive. |
| [Outcomes](../Other/managed-agents-define-outcomes.md) | A target result for a session, with a rubric that a separate grader uses to check the agent’s work until the target is met. |
| [Permission policies](../Other/managed-agents-permission-policies.md) | Settings that control whether the agent’s built-in tools and MCP tools run automatically, wait for your approval, or are checked by the server on each call. |
| [Scheduled deployments](../Other/managed-agents-scheduled-deployments.md) | Runs an agent on a cron schedule, so that the agent starts sessions by itself. |
| [Self-hosted Claude Managed Agents](../Other/managed-agents-self-hosted.md) | The whole Managed Agents service on your own infrastructure: you host the API, the agent loop, the storage, and the sandboxes. |
| [Self-hosted sandboxes](../Other/managed-agents-self-hosted-sandboxes.md) | Sandboxes on your own infrastructure that run the agent’s tool calls, while Claude still runs on Anthropic’s side. |
| Part of Self-hosted sandboxes: [Self-hosted workers](../Other/managed-agents-self-hosted-sandboxes-workers.md) | A process that you run on your own infrastructure to claim sessions from a self-hosted environment’s queue and run their tool calls. |
| [Session viewer](../Other/managed-agents-session-observability.md) | A session viewer in the Claude Console and per-session usage totals, to see what an agent did and what it used. |
| [Vaults](../Other/managed-agents-vaults.md) | Stores of per-user credentials for third-party services that you register once and reference by ID when you create a session. |
| [Webhooks](../Other/managed-agents-webhooks.md) | Notifications to your HTTPS endpoint when events happen in your Managed Agents resources, such as a change in a session’s status. |
