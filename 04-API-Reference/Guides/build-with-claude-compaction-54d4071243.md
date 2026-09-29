---
title: "Compaction overview - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:29Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcompaction)

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

[Overview](/docs/en/build-with-claude/compaction)[Compact on demand](/docs/en/build-with-claude/compaction-on-demand)[Keep recent turns](/docs/en/build-with-claude/compaction-keep-recent-turns)[Compact in the background](/docs/en/build-with-claude/compaction-background)[Keep thinking blocks valid](/docs/en/build-with-claude/compaction-thinking-blocks)[Threshold compaction](/docs/en/build-with-claude/compaction-threshold)

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

[Messages](/docs/en/intro)Context management

# Compaction overview

Copy page



Learn what compaction does, how compaction on demand and compaction at a token threshold differ, and which page covers your task.

Copy page



Compaction replaces the older turns of a conversation with a summary that Claude writes on the server, so you need no summarization code of your own. It keeps a long conversation or agent task inside the context window, and it keeps the active context small, because response quality degrades as a conversation grows.

If you want to skip this overview, start with [Compaction on demand](/docs/en/build-with-claude/compaction-on-demand) to add compaction to your application. While both it and [Compaction at a token threshold](/docs/en/build-with-claude/compaction-threshold) are in beta, Compaction on demand covers more common use cases. To clear old tool results or old thinking blocks by rule instead of summarizing them, see [Context editing](/docs/en/build-with-claude/context-editing).

## Choose how to compact

Use on-demand compaction wherever it is available.

|                                                                                                                        | [Compaction on demand](/docs/en/build-with-claude/compaction-on-demand)                                                                                                         | [Compaction at a token threshold](/docs/en/build-with-claude/compaction-threshold)                                                                                                                  | Your own summarizer ([Compact on the client](/docs/en/build-with-claude/preserved-thinking#custom-compaction-on-the-client)) |
|:-----------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| **Who decides when**                                                                                                   | You, by sending a request                                                                                                                                                       | The API, when input tokens reach the trigger you set                                                                                                                                                | You                                                                                                                          |
| **Code you write**                                                                                                     | A [compaction loop](/docs/en/build-with-claude/compaction-on-demand#compact-in-a-loop) that requests the summary and swaps it in                                                | One parameter on your ordinary requests                                                                                                                                                             | The summarization call, its prompt, and the history rewrite                                                                  |
| **What you send back afterward**                                                                                       | The returned block first in `messages`, in place of the messages it summarizes                                                                                                  | The response, appended as usual. The API drops what came before the block                                                                                                                           | Your summary, as a message of your own                                                                                       |
| **Recent turns stay word for word**                                                                                    | Yes: [Compaction that keeps recent turns](/docs/en/build-with-claude/compaction-keep-recent-turns)                                                                              | Yes, by [pausing after compaction](/docs/en/build-with-claude/compaction-threshold#pausing-after-compaction) and re-inserting them                                                                  | Yes                                                                                                                          |
| **Runs in the background**                                                                                             | Yes: [Compaction in the background](/docs/en/build-with-claude/compaction-background)                                                                                           | No: it runs inside the request that reaches the threshold                                                                                                                                           | Yes, in your own code                                                                                                        |
| **Kept turns keep their thinking**, on models with [preserved thinking](/docs/en/build-with-claude/preserved-thinking) | Yes, under the conditions in [Compaction and preserved thinking](/docs/en/build-with-claude/compaction-thinking-blocks)                                                         | No: on Claude Fable 5.1 and Claude Opus 5.5, remove or drop the thinking in turns you re-insert (see the [threshold compaction examples](/docs/en/build-with-claude/compaction-threshold#examples)) | No: that thinking [fails the check](/docs/en/build-with-claude/preserved-thinking#keep-tail-compaction)                      |
| **Beta header, parameter, and platforms**                                                                              | `compact-2026-09-04` and the top-level `compaction` parameter. Platforms: see the [on-demand Compatibility list](/docs/en/build-with-claude/compaction-on-demand#compatibility) | See the [threshold Compatibility list](/docs/en/build-with-claude/compaction-threshold#compatibility) and [Basic usage](/docs/en/build-with-claude/compaction-threshold#basic-usage)                | None. It runs in your code                                                                                                   |
| **Choose it when**                                                                                                     | Your application needs to control when compaction happens, can't pause while a summary is written, or must keep recent turns and their thinking                                 | You want the API to manage context inside ordinary requests                                                                                                                                         | You already run your own summarizer and it replaces the whole history with the summary                                       |

## On-demand compaction options

[Compaction on demand](/docs/en/build-with-claude/compaction-on-demand) shows a loop that summarizes the whole conversation while your application waits. The first two pages in this list change how that loop runs, and you can combine them. The third applies if you send thinking blocks back and do either.

- [Compaction that keeps recent turns](/docs/en/build-with-claude/compaction-keep-recent-turns): when the last few turns must reach Claude word for word. The summary covers only the older turns.
- [Compaction in the background](/docs/en/build-with-claude/compaction-background): when the conversation can't pause for the summary. The request runs while work continues, and you swap the block in when it arrives.
- [Compaction and preserved thinking](/docs/en/build-with-claude/compaction-thinking-blocks): if you send thinking blocks back on a model with preserved thinking and you keep recent turns or compact in the background. Otherwise skip it.
- [Write your own summarization prompt](/docs/en/build-with-claude/compaction-on-demand#write-your-own-summarization-prompt): when the default summary drops something a later turn needs. Your prompt replaces the default one.
- [Compact again](/docs/en/build-with-claude/compaction-on-demand#compact-again): when a conversation that already starts with a compaction block grows long again.

Find these topics on other pages:

- [Request a summary](/docs/en/build-with-claude/compaction-on-demand#request-a-summary) is on Compaction on demand.
- [Continue from the summary](/docs/en/build-with-claude/compaction-on-demand#continue-from-the-summary) is on Compaction on demand. The conditions that keep thinking valid in the turns you keep are on [Compaction and preserved thinking](/docs/en/build-with-claude/compaction-thinking-blocks).
- When no summary comes back: see [Handle a missing summary or an error](/docs/en/build-with-claude/compaction-on-demand#when-no-summary-comes-back) on Compaction on demand.
- How it fits with the rest of the API: see [Limits and interactions with other features](/docs/en/build-with-claude/compaction-on-demand#how-it-fits-with-the-rest-of-the-api) on Compaction on demand.
- Understanding usage: see [Count compaction usage](/docs/en/build-with-claude/compaction-on-demand#understanding-usage) for on-demand compaction, or [Understanding usage](/docs/en/build-with-claude/compaction-threshold#understanding-usage) for threshold compaction.
- Compatibility: each kind has its own beta header, so each page has its own list. See the [on-demand Compatibility list](/docs/en/build-with-claude/compaction-on-demand#compatibility) or the [threshold Compatibility list](/docs/en/build-with-claude/compaction-threshold#compatibility).

Threshold compaction has its own page: [Compaction at a token threshold](/docs/en/build-with-claude/compaction-threshold).
