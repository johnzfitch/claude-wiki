---
title: "Manage tool context - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:25Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Fmanage-tool-context)





SearchCtrlK

First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)[Authentication](/docs/en/manage-claude/authentication)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

[Thinking](/docs/en/build-with-claude/thinking)

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[Console](/)

[Messages](/docs/en/intro)Tool infrastructure

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
| Tool search               | Tool definitions loaded upfront         | Large toolsets (20+ tools) where most tools aren't needed every turn | [Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)                         |
| Programmatic tool calling | `tool_result` roundtrips                | Chains of tool calls that can execute as a single script             | [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)       |
| Prompt caching            | Token cost of repeated tool definitions | Stable toolsets across many requests                                 | [Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching) |
| Context editing           | Old `tool_result` blocks in history     | Long conversations where early results are no longer relevant        | [Context editing](/docs/en/build-with-claude/context-editing)                                   |

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

[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)

Load tool definitions on demand instead of upfront.



[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)

Collapse tool-call chains into a single executable script.



[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)

Cache tool definitions across requests to cut token costs.

[Context editing](/docs/en/build-with-claude/context-editing)

Trim stale tool results from long-running conversations.
