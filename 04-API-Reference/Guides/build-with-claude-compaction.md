---
title: "Compaction overview - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:29Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcompaction)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](build-with-claude-overview.md)[Using the Messages API](build-with-claude-working-with-messages.md)[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)[Refusals and fallback](build-with-claude-refusals-and-fallback.md)[Fallback credit](build-with-claude-fallback-credit.md)

Model capabilities

[Effort](build-with-claude-effort.md)[Task budgets (beta)](build-with-claude-task-budgets.md)[Fast mode (research preview)](build-with-claude-fast-mode.md)[Structured outputs](build-with-claude-structured-outputs.md)[Citations](build-with-claude-citations.md)[Streaming Messages](build-with-claude-streaming.md)[Batch processing](build-with-claude-batch-processing.md)[Search results](build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](build-with-claude-multilingual-support.md)[Embeddings](build-with-claude-embeddings.md)

[Thinking](build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

[Compaction](build-with-claude-compaction.md)

[Overview](build-with-claude-compaction.md)[Compact on demand](build-with-claude-compaction-on-demand.md)[Keep recent turns](build-with-claude-compaction-keep-recent-turns.md)[Compact in the background](build-with-claude-compaction-background.md)[Keep thinking blocks valid](build-with-claude-compaction-thinking-blocks.md)[Threshold compaction](build-with-claude-compaction-threshold.md)

Working with files

[Files API](build-with-claude-files.md)[PDF support](build-with-claude-pdf-support.md)

[Images and vision](build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)[Google Cloud](build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Context management

# Compaction overview

Copy page



Learn what compaction does, how compaction on demand and compaction at a token threshold differ, and which page covers your task.

Copy page



Compaction replaces the older turns of a conversation with a summary that Claude writes on the server, so you need no summarization code of your own. It keeps a long conversation or agent task inside the context window, and it keeps the active context small, because response quality degrades as a conversation grows.

If you want to skip this overview, start with [Compaction on demand](build-with-claude-compaction-on-demand.md) to add compaction to your application. While both it and [Compaction at a token threshold](build-with-claude-compaction-threshold.md) are in beta, Compaction on demand covers more common use cases. To clear old tool results or old thinking blocks by rule instead of summarizing them, see [Context editing](build-with-claude-context-editing.md).

## Choose how to compact

Use on-demand compaction wherever it is available.

|                                                                                                                        | [Compaction on demand](build-with-claude-compaction-on-demand.md)                                                                                                         | [Compaction at a token threshold](build-with-claude-compaction-threshold.md)                                                                                                                  | Your own summarizer ([Compact on the client](build-with-claude-preserved-thinking.md#custom-compaction-on-the-client)) |
|:-----------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| **Who decides when**                                                                                                   | You, by sending a request                                                                                                                                                       | The API, when input tokens reach the trigger you set                                                                                                                                                | You                                                                                                                          |
| **Code you write**                                                                                                     | A [compaction loop](build-with-claude-compaction-on-demand.md#compact-in-a-loop) that requests the summary and swaps it in                                                | One parameter on your ordinary requests                                                                                                                                                             | The summarization call, its prompt, and the history rewrite                                                                  |
| **What you send back afterward**                                                                                       | The returned block first in `messages`, in place of the messages it summarizes                                                                                                  | The response, appended as usual. The API drops what came before the block                                                                                                                           | Your summary, as a message of your own                                                                                       |
| **Recent turns stay word for word**                                                                                    | Yes: [Compaction that keeps recent turns](build-with-claude-compaction-keep-recent-turns.md)                                                                              | Yes, by [pausing after compaction](build-with-claude-compaction-threshold.md#pausing-after-compaction) and re-inserting them                                                                  | Yes                                                                                                                          |
| **Runs in the background**                                                                                             | Yes: [Compaction in the background](build-with-claude-compaction-background.md)                                                                                           | No: it runs inside the request that reaches the threshold                                                                                                                                           | Yes, in your own code                                                                                                        |
| **Kept turns keep their thinking**, on models with [preserved thinking](build-with-claude-preserved-thinking.md) | Yes, under the conditions in [Compaction and preserved thinking](build-with-claude-compaction-thinking-blocks.md)                                                         | No: on Claude Fable 5.1 and Claude Opus 5.5, remove or drop the thinking in turns you re-insert (see the [threshold compaction examples](build-with-claude-compaction-threshold.md#examples)) | No: that thinking [fails the check](build-with-claude-preserved-thinking.md#keep-tail-compaction)                      |
| **Beta header, parameter, and platforms**                                                                              | `compact-2026-09-04` and the top-level `compaction` parameter. Platforms: see the [on-demand Compatibility list](build-with-claude-compaction-on-demand.md#compatibility) | See the [threshold Compatibility list](build-with-claude-compaction-threshold.md#compatibility) and [Basic usage](build-with-claude-compaction-threshold.md#basic-usage)                | None. It runs in your code                                                                                                   |
| **Choose it when**                                                                                                     | Your application needs to control when compaction happens, can't pause while a summary is written, or must keep recent turns and their thinking                                 | You want the API to manage context inside ordinary requests                                                                                                                                         | You already run your own summarizer and it replaces the whole history with the summary                                       |

## On-demand compaction options

[Compaction on demand](build-with-claude-compaction-on-demand.md) shows a loop that summarizes the whole conversation while your application waits. The first two pages in this list change how that loop runs, and you can combine them. The third applies if you send thinking blocks back and do either.

- [Compaction that keeps recent turns](build-with-claude-compaction-keep-recent-turns.md): when the last few turns must reach Claude word for word. The summary covers only the older turns.
- [Compaction in the background](build-with-claude-compaction-background.md): when the conversation can't pause for the summary. The request runs while work continues, and you swap the block in when it arrives.
- [Compaction and preserved thinking](build-with-claude-compaction-thinking-blocks.md): if you send thinking blocks back on a model with preserved thinking and you keep recent turns or compact in the background. Otherwise skip it.
- [Write your own summarization prompt](build-with-claude-compaction-on-demand.md#write-your-own-summarization-prompt): when the default summary drops something a later turn needs. Your prompt replaces the default one.
- [Compact again](build-with-claude-compaction-on-demand.md#compact-again): when a conversation that already starts with a compaction block grows long again.

Find these topics on other pages:

- [Request a summary](build-with-claude-compaction-on-demand.md#request-a-summary) is on Compaction on demand.
- [Continue from the summary](build-with-claude-compaction-on-demand.md#continue-from-the-summary) is on Compaction on demand. The conditions that keep thinking valid in the turns you keep are on [Compaction and preserved thinking](build-with-claude-compaction-thinking-blocks.md).
- When no summary comes back: see [Handle a missing summary or an error](build-with-claude-compaction-on-demand.md#when-no-summary-comes-back) on Compaction on demand.
- How it fits with the rest of the API: see [Limits and interactions with other features](build-with-claude-compaction-on-demand.md#how-it-fits-with-the-rest-of-the-api) on Compaction on demand.
- Understanding usage: see [Count compaction usage](build-with-claude-compaction-on-demand.md#understanding-usage) for on-demand compaction, or [Understanding usage](build-with-claude-compaction-threshold.md#understanding-usage) for threshold compaction.
- Compatibility: each kind has its own beta header, so each page has its own list. See the [on-demand Compatibility list](build-with-claude-compaction-on-demand.md#compatibility) or the [threshold Compatibility list](build-with-claude-compaction-threshold.md#compatibility).

Threshold compaction has its own page: [Compaction at a token threshold](build-with-claude-compaction-threshold.md).
