---
title: "Manage tool context - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:25Z"
tags: ["api"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Fmanage-tool-context)

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

[Messages](../../01-Getting-Started/intro.md)Tool infrastructure

# Manage tool context

Copy page



Choose between tool search, programmatic tool calling, prompt caching, and context editing to manage context bloat.

Copy page



Tool definitions and accumulated `tool_result` blocks consume your context window. Long-running agents with many tools or many turns can exhaust available context before the task is finished. Four approaches address this at different points in the pipeline.

## The four approaches

Each approach targets a different source of context pressure. Pick the one that matches where your tokens are going.

| Approach                  | What it reduces                         | When it fits                                                         | Learn more                                                                                      |
|---------------------------|-----------------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Tool search               | Tool definitions loaded upfront         | Large toolsets (20+ tools) where most tools aren't needed every turn | [Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)                         |
| Programmatic tool calling | `tool_result` roundtrips                | Chains of tool calls that can execute as a single script             | [Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md)       |
| Prompt caching            | Token cost of repeated tool definitions | Stable toolsets across many requests                                 | [Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md) |
| Context editing           | Old `tool_result` blocks in history     | Long conversations where early results are no longer relevant        | [Context editing](../Guides/build-with-claude-context-editing.md)                                   |

### Tool search

Tool search keeps tool definitions out of the context window until Claude asks for them. Instead of sending 50 tool schemas upfront, you send a single `tool_search` tool and let Claude discover the rest on demand. This trades a small amount of latency (one extra turn to look up a tool) for a large reduction in baseline context usage.

### Programmatic tool calling

Programmatic tool calling collapses a sequence of tool calls into a single code block that Claude writes and Anthropic's code execution sandbox runs. Rather than five roundtrips of `tool_use` and `tool_result`, Claude emits one script that calls all five functions from within the sandbox. The intermediate results never enter the conversation history.

### Prompt caching

Prompt caching doesn't reduce the number of tokens in context, but it reduces what you pay for them on subsequent requests. If your tool definitions are stable, cache them once and reuse the cached prefix across thousands of requests. This is the right choice when the toolset is large but fixed.

### Context editing

Context editing removes old `tool_result` blocks from the conversation history once they've served their purpose. A long agent loop might produce hundreds of intermediate results that were useful at the time but are now dead weight. Context editing lets you trim them without restarting the conversation.

## Combining approaches

These approaches compose. A long-running agent might use tool search to keep the toolset lean, prompt caching to amortize the cost of the remaining definitions, and context editing to trim stale results as the conversation grows. Each solves a different part of the problem, so there's no conflict in using them together.

A reasonable starting point for a high-volume agent:

1.  Enable prompt caching on your tool definitions from day one. Cache writes carry a 25% markup over base input pricing, which pays back on the second request that hits the cache.
2.  Add tool search once your toolset grows past roughly 20 tools or your baseline context usage becomes noticeable.
3.  Add context editing once individual conversations start running long enough that early results become irrelevant.
4.  Consider programmatic tool calling if you notice repetitive chains of small tool calls that could run as a single batch.

## Next steps



[Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)

Load tool definitions on demand instead of upfront.



[Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md)

Collapse tool-call chains into a single executable script.



[Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md)

Cache tool definitions across requests to cut token costs.

[Context editing](../Guides/build-with-claude-context-editing.md)

Trim stale tool results from long-running conversations.
