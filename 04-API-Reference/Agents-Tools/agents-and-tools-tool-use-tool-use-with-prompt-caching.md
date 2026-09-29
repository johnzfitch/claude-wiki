---
title: "Tool use with prompt caching - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:27Z"
tags: ["api", "prompting"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Ftool-use-with-prompt-caching)

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

# Tool use with prompt caching

Copy page



Cache tool definitions across turns and understand what invalidates your cache.

Copy page



This page covers prompt caching for tool definitions: where to place `cache_control` breakpoints, how `defer_loading` preserves your cache, and what invalidates it. For general prompt caching, see [Prompt caching](../Guides/build-with-claude-prompt-caching.md).

## cache_control on tool definitions

Place `cache_control: {"type": "ephemeral"}` on the last tool in your `tools` array. This caches the entire tool-definitions prefix, from the first tool through the marked breakpoint:

```python
{
  "tools": [
    {
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": { "type": "string" }
        },
        "required": ["location"]
      }
    },
    {
      "name": "get_time",
      "description": "Get the current time in a given time zone",
      "input_schema": {
        "type": "object",
        "properties": {
          "timezone": { "type": "string" }
        },
        "required": ["timezone"]
      },
      "cache_control": { "type": "ephemeral" }
    }
  ]
}
```



For `mcp_toolset`, the `cache_control` breakpoint lands on the last tool in the set. You don't control tool order within an MCP toolset, so place the breakpoint on the `mcp_toolset` entry itself and the API applies it to the final expanded tool.

The [computer use](agents-and-tools-tool-use-computer-use-tool.md) and [browser use](agents-and-tools-tool-use-browser-use-tool.md) toolset entries follow the same rule: place `cache_control` on the toolset entry itself, and the breakpoint lands after the toolset's definition. It isn't accepted inside a member's `configs` entry, because the toolset's members load as one definition. Within a [batch action](agents-and-tools-tool-use-computer-use-tool.md#batch-actions), a `cache_control` marker on any of the turn's member `tool_use` or `tool_result` blocks is accepted and takes effect at the end of that batch, so several markers in one batch act as a single breakpoint. Each marker still counts toward the request's limit of [four breakpoints](../Guides/build-with-claude-prompt-caching.md#when-to-use-multiple-breakpoints), so use one per turn.

## defer_loading and cache preservation

Deferred tools are not included in the system-prompt prefix. When the model discovers a deferred tool through [tool search](agents-and-tools-tool-use-tool-search-tool.md), the definition is appended inline as a `tool_reference` block in the conversation history. The prefix is untouched, so prompt caching is preserved.

This means adding tools dynamically through tool search does not break your cache. You can start a conversation with a small set of always-loaded tools (cached), let the model discover additional tools as needed, and keep the same cache hit across every turn.

`defer_loading` also acts independently of grammar construction for [strict mode](agents-and-tools-tool-use-strict-tool-use.md). The grammar builds from the full toolset regardless of which tools are deferred, so prompt caching and grammar caching are both preserved when tools load dynamically.

## What invalidates your cache

The cache follows a prefix hierarchy (`tools` → `system` → `messages`), so a change at one level invalidates that level and everything after it:

| Change                               | Invalidates                                                                                                                                                                                   |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Modifying tool definitions           | Entire cache (tools, system, messages)                                                                                                                                                        |
| Toggling web search or citations     | System and messages caches                                                                                                                                                                    |
| Changing `tool_choice`               | Messages cache                                                                                                                                                                                |
| Changing `disable_parallel_tool_use` | Messages cache                                                                                                                                                                                |
| Toggling images present/absent       | Messages cache                                                                                                                                                                                |
| Changing thinking parameters         | Messages cache always; tool and system caches too on models that render the thinking configuration ahead of them ([details](../Guides/build-with-claude-thinking.md#thinking-and-prompt-caching)) |
| Changing `output_config.effort`      | Same as thinking parameters; setting the model's default explicitly is equivalent to omitting it                                                                                              |



If you need to vary `tool_choice` mid-conversation, consider placing cache breakpoints before the variation point.

## Server tool results are cached automatically

When your request has prompt caching enabled and Claude uses a [server tool](agents-and-tools-tool-use-server-tools.md) such as web search, web fetch, or code execution, the API automatically places a cache breakpoint on the server tool result before running the next iteration of the agentic loop. This lets later iterations within the same request read the growing prefix from cache instead of reprocessing it.

This automatic breakpoint always uses the default 5-minute TTL, independent of any TTL you set on your own `cache_control` markers. In the response `usage`, these writes appear under `cache_creation.ephemeral_5m_input_tokens`, so you may see 5-minute cache writes even when every `cache_control` you set uses a 1-hour TTL.

This behavior only applies when your request already has at least one `cache_control` marker. Requests without prompt caching do not receive the automatic breakpoint.

## Per-tool interaction table

| Tool                                                                     | Caching considerations                                                                                                                                              |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Web search](agents-and-tools-tool-use-web-search-tool.md)         | Enabling or disabling invalidates the system and messages caches                                                                                                    |
| [Web fetch](agents-and-tools-tool-use-web-fetch-tool.md)           | Enabling or disabling invalidates the system and messages caches                                                                                                    |
| [Code execution](agents-and-tools-tool-use-code-execution-tool.md) | Container state is independent of prompt cache                                                                                                                      |
| [Tool search](agents-and-tools-tool-use-tool-search-tool.md)       | Discovered tools load as `tool_reference` blocks, preserving prefix cache                                                                                           |
| [Computer use](agents-and-tools-tool-use-computer-use-tool.md)     | Screenshot presence affects messages cache; `cache_control` goes on the toolset entry (see [cache_control on tool definitions](#cache-control-on-tool-definitions)) |
| [Browser use](agents-and-tools-tool-use-browser-use-tool.md)       | Screenshot presence affects messages cache; `cache_control` goes on the toolset entry (see [cache_control on tool definitions](#cache-control-on-tool-definitions)) |
| [Text editor](agents-and-tools-tool-use-text-editor-tool.md)       | Standard client tool, no special caching interaction                                                                                                                |
| [Bash](agents-and-tools-tool-use-bash-tool.md)                     | Standard client tool, no special caching interaction                                                                                                                |
| [Memory](agents-and-tools-tool-use-memory-tool.md)                 | Standard client tool, no special caching interaction                                                                                                                |

## Next steps



[Prompt caching](../Guides/build-with-claude-prompt-caching.md)

Learn the full prompt caching model, including TTLs and pricing.



[Tool search](agents-and-tools-tool-use-tool-search-tool.md)

Load tools on demand without breaking your cache.



[Tool reference](agents-and-tools-tool-use-tool-reference.md)

Browse all available tools and their parameters.
