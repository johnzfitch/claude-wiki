---
title: "How tool use works - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:25Z"
tags: ["agents", "api", "cli"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Fhow-tool-use-works)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](../Guides/build-with-claude-overview.md)[Using the Messages API](../Guides/build-with-claude-working-with-messages.md)[Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md)[Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md)[Fallback credit](../Guides/build-with-claude-fallback-credit.md)

Model capabilities

[Effort](../Guides/build-with-claude-effort.md)[Task budgets (beta)](../Guides/build-with-claude-task-budgets.md)[Fast mode (research preview)](../Guides/build-with-claude-fast-mode.md)[Structured outputs](../Guides/build-with-claude-structured-outputs.md)[Citations](../Guides/build-with-claude-citations.md)[Streaming Messages](../Guides/build-with-claude-streaming.md)[Batch processing](../Guides/build-with-claude-batch-processing.md)[Search results](../Guides/build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](../Guides/build-with-claude-multilingual-support.md)[Embeddings](../Guides/build-with-claude-embeddings.md)

[Thinking](../Guides/build-with-claude-thinking.md)

Tools

[Overview](agents-and-tools-tool-use-overview.md)[How tool use works](agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](agents-and-tools-tool-use-tool-runner.md)[Strict tool use](agents-and-tools-tool-use-strict-tool-use.md)[Server tools](agents-and-tools-tool-use-server-tools.md)[Web search tool](agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](agents-and-tools-tool-use-memory-tool.md)[Bash tool](agents-and-tools-tool-use-bash-tool.md)[Text editor tool](agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](agents-and-tools-tool-use-tool-reference.md)[Manage tool context](agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](../Guides/build-with-claude-context-windows.md)[Context editing](../Guides/build-with-claude-context-editing.md)[Prompt caching](../Guides/build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](../Guides/build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](../Guides/build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md)[Token counting](../Guides/build-with-claude-token-counting.md)

[Compaction](../Guides/build-with-claude-compaction.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](agents-and-tools-agent-skills-overview.md)[Quickstart](agents-and-tools-agent-skills-quickstart.md)[Best practices](agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](agents-and-tools-agent-skills-enterprise.md)[Skills in the API](../Guides/build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](agents-and-tools-remote-mcp-servers.md)[MCP connector](agents-and-tools-mcp-connector.md)

[MCP tunnels](agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](../Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)[Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Tools

# How tool use works

Copy page



Understand the tool use loop, where tools execute, and when to use tools instead of prose.

Copy page



This page explains the concepts behind tool use: where tools run, how the agentic loop works, and when tool use is the right approach. For hands-on guidance, start with the [Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md) tutorial or the [Define tools](agents-and-tools-tool-use-implement-tool-use.md) guide.

## The tool-use contract

Tool use is a contract between your application and the model. You specify what operations are available and what shape their inputs and outputs take; Claude determines when and how to call them. The model never executes anything on its own. It emits a structured request, your code (or Anthropic's servers) runs the operation, and the result flows back into the conversation.

This contract makes the model behave less like a text generator and more like a function you call. Engineers with classical API experience can integrate tool use the same way they would any other typed interface: define the schema, handle the callback, return a result. The difference is that the caller on the other side is a language model choosing which function to call based on the conversation.

## Where tools run

The primary axis along which tools differ is where the code executes. Every tool falls into one of three buckets, and the bucket determines what your application is responsible for.

### User-defined tools (client-executed)

You write the schema, you execute the code, you return the results. This is the most common case: the vast majority of tool-use traffic is [user-defined tools](agents-and-tools-tool-use-implement-tool-use.md) calling into application-specific logic.

When Claude calls one of your tools, the API response contains a `tool_use` block with the tool name and a JSON object of arguments. Your application extracts those arguments, runs the operation (a database query, an HTTP call, a file write, whatever the tool does), and sends the output back in a `tool_result` block on the next request. Claude never sees your implementation; it only sees the schema you provided and the result you returned.

### Anthropic-schema tools (client-executed)

For a handful of common operations (managing scratchpad memory, running shell commands, editing files, controlling a desktop or a browser), Anthropic publishes the tool schema and your application handles execution. The tools in this category are [`memory`](agents-and-tools-tool-use-memory-tool.md), [`bash`](agents-and-tools-tool-use-bash-tool.md), [`text_editor`](agents-and-tools-tool-use-text-editor-tool.md), [`computer`](agents-and-tools-tool-use-computer-use-tool.md), and [`browser`](agents-and-tools-tool-use-browser-use-tool.md).

The execution model is identical to user-defined tools: the response contains a `tool_use` block, your code runs the operation, and you send back a `tool_result`. The reason to use an Anthropic-schema tool instead of defining your own equivalent is that these schemas are trained-in. Claude has been optimized on thousands of successful trajectories that use these exact tool signatures, so it calls them more reliably and recovers from errors more gracefully than it would with a custom tool that does the same thing. The schema is the interface the model already expects.

### Server-executed tools

For [`web_search`](agents-and-tools-tool-use-web-search-tool.md), [`web_fetch`](agents-and-tools-tool-use-web-fetch-tool.md), [`code_execution`](agents-and-tools-tool-use-code-execution-tool.md), and [`tool_search`](agents-and-tools-tool-use-tool-search-tool.md), Anthropic runs the code. You enable the tool in your request and the server handles everything else. You never construct a `tool_result` block for these tools. When a turn calls only [server tools](agents-and-tools-tool-use-server-tools.md), the server-side loop executes the operation and feeds the output back to the model before the response reaches you, unless the loop stops before it finishes, most often because it pauses.

The response you receive contains `server_tool_use` blocks showing what ran and what came back. In the common case, execution is already complete by the time you see them, and your application's job is to enable the tool and read the final answer rather than to participate in the execution loop; the main exceptions are a paused loop ([`pause_turn`](#the-server-side-loop)) and a turn that also calls a client tool.

## The agentic loop (client tools)

Client-executed tools (both user-defined and Anthropic-schema) require your application to drive a loop. The model can't run your code, so every tool call is a round trip: the model asks, you execute, you report back, the model continues.

The canonical shape is a `while` loop keyed on `stop_reason`:

1.  Send a request with your `tools` array and the user message.
2.  Claude responds with `stop_reason: "tool_use"` and one or more `tool_use` blocks.
3.  Execute each tool. Format the outputs as `tool_result` blocks.
4.  Send a new request containing the original messages, the assistant's response, and a user message with the `tool_result` blocks.
5.  Repeat from step 2 while `stop_reason` is `"tool_use"`.

In practice this reads as: while `stop_reason == "tool_use"`, execute the tools and continue the conversation. The loop exits on any other stop reason (`"end_turn"`, `"max_tokens"`, `"stop_sequence"`, or `"refusal"`), which means Claude has either produced a final answer or stopped for another reason that your application should handle.

For the mechanics of building requests, handling parallel tool calls, and formatting results, see [Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md).

## The server-side loop

Server-executed tools run their own loop inside Anthropic's infrastructure. A single request from your application might trigger several web searches or code executions before a response comes back. The model searches, reads results, determines whether to search again, and iterates until it has what it needs, all without your application participating.

This internal loop has an iteration limit. If the model is still iterating when it hits the cap, the response comes back with `stop_reason: "pause_turn"` instead of `"end_turn"`. A paused turn means the work isn't finished; re-send the conversation (including the paused response) to let the model continue where it left off. See [Server tools](agents-and-tools-tool-use-server-tools.md) for the continuation pattern.

The loop also hands control back to you before a server tool runs if Claude calls that server tool and a client tool in the same group of parallel tool calls. The response then comes back with `stop_reason: "tool_use"` and a `server_tool_use` block that has no result block yet; the API runs it after you return the client tool results. See [Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md#tool-use) for the exact contract.

## When to use tools (and when not to)

Tool use fits when the task requires something the model can't do from text alone:

- **Actions with side effects.** Sending an email, writing a file, updating a record. The model can describe these actions, but only a tool can perform them.
- **Fresh or external data.** Current prices, today's weather, the contents of a database. Anything outside the training data or specific to your system needs a tool to fetch it.
- **Structured, guaranteed-shape outputs.** When you need a JSON object with specific fields rather than prose that happens to contain the information, a tool schema enforces the shape.
- **Calling into existing systems.** Databases, internal APIs, filesystems. Tool use is the bridge between natural-language requests and the systems that fulfill them.

A clear sign that you should be using tools: if you're writing a regex to extract a decision from model output, that decision should have been a tool call. Parsing free-form text to recover structured intent is a sign the structure belongs in the schema.

Tool use doesn't fit when:

- The model can answer from training alone. Summarization, translation, and general-knowledge questions don't need a tool round trip.
- The interaction is one-shot Q&A with no side effects. If there's nothing to execute, there's nothing for a tool to do.
- Tool-calling latency would dominate a trivial response. Every tool call is at least one extra round trip; for lightweight tasks the overhead can exceed the work.

## Choosing between approaches

| Approach                      | When to use it                                                            | What to expect                                                                        | Learn more                                                          |
|-------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| User-defined client tools     | Custom business logic, internal APIs, proprietary data                    | You handle execution and the agentic loop                                             | [Define tools](agents-and-tools-tool-use-implement-tool-use.md)     |
| Anthropic-schema client tools | Standard dev operations (bash, file editing, desktop and browser control) | You handle execution; Claude calls the tool reliably because the schema is trained-in | [Tool reference](agents-and-tools-tool-use-tool-reference.md) |
| Server-executed tools         | Web search, code sandbox, web fetch                                       | Anthropic handles execution; you read the results instead of producing them           | [Server tools](agents-and-tools-tool-use-server-tools.md)     |

## Next steps

[Tutorial: Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md)

Build an agent step by step from a single tool call to production.

[Define tools](agents-and-tools-tool-use-implement-tool-use.md)

Schema specification, descriptions, and `tool_choice`.

[Tool reference](agents-and-tools-tool-use-tool-reference.md)

Directory of Anthropic-provided tools.
