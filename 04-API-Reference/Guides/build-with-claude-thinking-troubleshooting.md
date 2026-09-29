---
title: "Troubleshooting thinking - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:28Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fthinking-troubleshooting)

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

[Overview](build-with-claude-thinking.md)[Steering and cost control](build-with-claude-thinking-steering-and-cost.md)[Tool and multi-turn workflows](build-with-claude-thinking-tool-workflows.md)[Preserved thinking](build-with-claude-preserved-thinking.md)[Troubleshooting](build-with-claude-thinking-troubleshooting.md)[Extended thinking (legacy)](build-with-claude-extended-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

[Compaction](build-with-claude-compaction.md)

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

[Messages](../../01-Getting-Started/intro.md)Thinking

# Troubleshooting thinking

Copy page



Diagnose and fix the most common thinking failures: configuration 400 errors, empty or missing thinking blocks, max_tokens stops, and cache misses.

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

This page covers the most common failures when configuring thinking or round-tripping thinking blocks (sending returned thinking blocks back in later requests). The first section maps each model to its supported thinking configurations and the ones it rejects; the sections after it each start from a symptom you observe, so you can match an error message or unexpected response directly to its cause and fix. To learn how thinking works, see the [Thinking](build-with-claude-thinking.md) overview.

## Thinking support, defaults, and rejected configurations by model

Most thinking configuration errors are a mismatch between the `thinking.type` value in the request and what the model supports. On most models, thinking runs as `thinking: {type: "adaptive"}`, and many have it on by default. Some earlier models instead use [extended thinking](build-with-claude-extended-thinking.md), a legacy manual mode configured as `thinking: {type: "enabled", budget_tokens: N}`.

Extended thinking (`thinking.type: "enabled"` with `budget_tokens`) is deprecated on the Claude 4.6 models (requests using it still succeed). Claude 4.7 and later models do not support it and reject requests that use it, returning a 400 error. On Claude 4.5 and earlier models that support thinking, extended thinking is the only available thinking mode. Claude Mythos Preview supports both modes. Where both modes are available, use [adaptive thinking](build-with-claude-thinking.md) instead.

The table lists what each model supports, what it defaults to, and which `thinking.type` values it rejects with a 400 error; any value not listed as rejected is accepted.

| Model                 | Thinking types                   | Default   | Rejected with 400          |
|:----------------------|:---------------------------------|:----------|:---------------------------|
| Claude Fable 5.1      | Adaptive only                    | Always on | `"enabled"`, `"disabled"`  |
| Claude Mythos 5.1     | Adaptive only                    | Always on | `"enabled"`, `"disabled"`  |
| Claude Fable 5        | Adaptive only                    | Always on | `"enabled"`, `"disabled"`  |
| Claude Mythos 5       | Adaptive only                    | Always on | `"enabled"`, `"disabled"`  |
| Claude Mythos Preview | Adaptive, extended               | Always on | `"disabled"`               |
| Claude Opus 5.5       | Adaptive only                    | Always on | `"enabled"`, `"disabled"`  |
| Claude Opus 5         | Adaptive only                    | On        | `"enabled"`, `"disabled"`² |
| Claude Opus 4.8       | Adaptive only                    | Off       | `"enabled"`                |
| Claude Opus 4.7       | Adaptive only                    | Off       | `"enabled"`                |
| Claude Sonnet 5       | Adaptive only                    | On        | `"enabled"`                |
| Claude Opus 4.6       | Adaptive, extended (deprecated)¹ | Off       | None                       |
| Claude Sonnet 4.6     | Adaptive, extended (deprecated)¹ | Off       | None                       |
| Claude Opus 4.5       | Extended only                    | Off       | `"adaptive"`               |
| Claude Haiku 4.5      | Extended only                    | Off       | `"adaptive"`               |
| Claude Sonnet 4.5     | Extended only                    | Off       | `"adaptive"`               |

*¹ `enabled` and `budget_tokens` still work on these models but are deprecated; use adaptive thinking instead.*  
*² Claude Opus 5 accepts `"disabled"` at [effort](build-with-claude-effort.md) `high` or below; combining it with effort `xhigh` or `max` returns a 400 error. This restriction is enforced on each request.*

Models marked `Always on` cannot turn thinking off. Models marked `On` default to thinking but accept `thinking: {type: "disabled"}`.

Earlier Claude 4 models (Claude Opus 4.1, Claude Sonnet 4, and Claude Opus 4) support extended thinking only. See [Model deprecations](../../20-Models/about-claude-model-deprecations.md) for their availability. Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, and Claude Mythos 5 are not available under [zero data retention](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements) unless expressly authorized by Anthropic.

## A 400 error says `"thinking.type.enabled"` is not supported

The request fails with a 400 error whose message reads:

``` block
"thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```



This happens because the model you requested has removed extended thinking (see the [per-model configuration table](#rejected-configurations)).

Switch the request to `thinking: {type: "adaptive"}` and steer thinking depth with `effort` instead of `budget_tokens`. [Migrating to adaptive thinking](build-with-claude-extended-thinking.md#migrating-to-adaptive-thinking) walks through the conversion.

## A 400 error says `"thinking.type.disabled"` is not supported

The request fails with a 400 error. On Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, Claude Opus 5.5, and Claude Mythos 5, the message reads:

``` block
"thinking.type.disabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```



On Claude Mythos Preview, the only one of these models that accepts extended thinking, the message reads:

``` block
"thinking.type.disabled" is not supported for this model. Thinking defaults to adaptive mode when not specified; use "thinking.type.enabled" with "budget_tokens" for extended thinking.
```



This happens because thinking is always on for all of these models (see the [per-model configuration table](#rejected-configurations)).

Omit the `thinking` parameter; these models think without any configuration. If your goal was to keep thinking text out of responses, use `display: "omitted"` instead of disabling thinking; see [Controlling thinking display](build-with-claude-thinking.md#controlling-thinking-display).

A 400 error on `"disabled"` can also occur on Claude Opus 5, which accepts `thinking: {type: "disabled"}` only at [effort](build-with-claude-effort.md) `high` or below: combining it with effort `xhigh` or `max` is rejected. Lower the effort level, or leave thinking on.

## A 400 error says adaptive thinking is not supported

The request fails with a 400 error whose message reads:

``` block
adaptive thinking is not supported on this model
```



This happens because the model supports only extended thinking (see the [per-model configuration table](#rejected-configurations)).

Use `thinking: {type: "enabled", budget_tokens: N}` instead; see [Extended thinking](build-with-claude-extended-thinking.md) for the configuration.

## A 400 error says thinking blocks cannot be modified

A request that returns tool results fails with a 400 `invalid_request_error` whose message contains:

``` block
`thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified
```



In multi-turn and tool-use conversations you send previous assistant messages, including their `thinking` and `redacted_thinking` blocks, back to the API, and the API verifies they arrive unmodified. This error happens when the assistant message you send back differs from the one the API returned, most often because your code filters content blocks by type and drops `redacted_thinking` blocks, or rebuilds the assistant message instead of echoing it.

Echo the assistant turn back verbatim, thinking blocks included. See [Preserving thinking blocks](build-with-claude-thinking.md#preserving-thinking-blocks) for the rules, and the worked round trip in [Thinking in tool and multi-turn workflows](build-with-claude-thinking-tool-workflows.md#two-turn-tool-use-round-trip) for correct code in every SDK.

## A 400 error says a thinking block signature is invalid

A request to Claude Fable 5.1 or Claude Opus 5.5 that replays earlier thinking blocks fails with a 400 `invalid_request_error` whose message reads:

``` block
messages.{i}.content.{j}: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.prefix_mismatch_behavior` to "drop_block".
```



If the request didn't send the `thinking-binding-controls-2026-08-01` beta header, the message adds `` That setting requires the `thinking-binding-controls-2026-08-01` value in the `anthropic-beta` header. ``

The message usually ends with a sentence naming what changed: the `system` prompt, the `tools` list, the first message or block that differs, content that is missing or new, or an earlier thinking block that is missing or out of order. That sentence is for people and logs. Its wording can change, so don't match on it in code.

If the message stops after `` Invalid `signature` in `thinking` block ``, the signature itself didn't verify: it was truncated, altered, or sent back empty, and `prefix_mismatch_behavior` doesn't apply. Edited thinking text returns a different error. See [A 400 error says thinking blocks cannot be modified](#error-thinking-blocks-modified).

On Claude Fable 5.1 and Claude Opus 5.5, the API accepts a replayed thinking block only while the `system` prompt, `tools`, and messages that preceded it are unchanged. See [Keeping the prefix unchanged](build-with-claude-preserved-thinking.md#prefix-check). The error means something earlier in the conversation changed between requests: an edited, reordered, or removed turn, a per-turn reminder that was injected and later removed, a rebuilt `system` prompt or `tools` array, or client-side compaction that kept recent turns and their thinking verbatim. The check is enforced for new accounts created on or after August 31, 2026, and for any request that sets `thinking.block_binding.prefix_mismatch_behavior`. Server-side [compaction](build-with-claude-compaction.md) and [context editing](build-with-claude-context-editing.md) never trigger it.

To fix it, keep the history append-only: pass earlier turns back exactly as sent and received, add instructions with a [mid-conversation system message](build-with-claude-mid-conversation-system-messages.md) instead of editing `system` or `tools`, and let server-side [context editing](build-with-claude-context-editing.md) or [compaction](build-with-claude-compaction.md) do any trimming. Retrying the same request body doesn't clear the error. To continue this request without the invalidated reasoning, send the `thinking-binding-controls-2026-08-01` beta header and set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`. Alternatively, strip every `thinking` and `redacted_thinking` block from the history (at minimum the named block and every one after it, in that turn and all later turns), leave each turn's other blocks in place, and retry once.

A block from a model the target model can't read never produces this error: the API drops it and, under the beta header, reports it in `input_transformations`.

## The thinking field is empty in the response

The response contains `thinking` blocks, but their `thinking` field is an empty string and only the `signature` field is populated.

This happens because `display` defaults to `"omitted"` on newer models, which returns thinking blocks without their text.

Set `display: "summarized"` in your thinking configuration to receive the summarized thinking text. See [Controlling thinking display](build-with-claude-thinking.md#controlling-thinking-display) for the defaults per model. If you only want the short status lines some models write between tool calls, and not the reasoning, set `display: "updates"` (beta) instead. See [Progress updates between tool calls](build-with-claude-thinking.md#progress-updates).

A block whose `thinking` field is empty is still complete: the `signature` holds the reasoning. Send it back with the turn like any other. See [Send assistant turns back exactly as returned](build-with-claude-preserved-thinking.md#append-assistant-turns-exactly-as-returned).

## No thinking block appears on some turns

Some responses contain no `thinking` block at all, even though thinking is configured.

This is normal in adaptive mode: Claude skips thinking on requests it judges simple enough to answer directly.

If you want thinking more often or more deeply, raise `effort` or steer with prompting; see [Steering how often Claude thinks](build-with-claude-thinking-steering-and-cost.md#tuning-thinking-behavior).

## Tool calls or XML tags appear in the text output

A response occasionally writes a tool call into its text instead of emitting a `tool_use` block, or includes `<thinking>` or other internal XML tags in its visible text. A leaked tool call never runs, and in agentic loops the leaked text stays in the conversation history, so later turns are affected as well.

This happens on Claude Opus 5 when thinking is disabled, most commonly on tool-heavy workloads such as search. System-prompt rules instructing the model not to think or not to reason increase the tag leakage.

Re-enable thinking (the default) and use lower `effort` levels to control token cost instead. If your integration must keep thinking disabled, apply the prompting mitigations in [Running with thinking disabled](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#running-with-thinking-disabled).

## The response stops with `stop_reason: "max_tokens"`

The response ends with `stop_reason: "max_tokens"`, often with a truncated or missing text block.

This happens because thinking tokens count toward `max_tokens`, so a long thinking pass can consume the budget before the text response completes.

Raise `max_tokens` to leave room for both thinking and text, or lower `effort` so Claude spends less on thinking; see [Cost control](build-with-claude-thinking-steering-and-cost.md#cost-control) and [Thinking and the context window](build-with-claude-thinking.md#thinking-and-the-context-window).

## Cache hits drop after changing thinking settings

`cache_read_input_tokens` falls to zero on requests that previously hit the cache.

This happens because the thinking configuration and the effort level (or its default) are part of the cached prompt prefix, so changing any of them starts a new prefix: switching thinking modes, changing the effort value, and changing `budget_tokens` all invalidate message cache breakpoints, and can invalidate tool and system-prompt breakpoints too, depending on where the model renders the configuration.

Keep the thinking configuration and effort level constant across requests that share a conversation; setting a parameter explicitly to its default is equivalent to omitting it and does not invalidate. See [Thinking and prompt caching](build-with-claude-thinking.md#thinking-and-prompt-caching).

## Setting effort does not change thinking

You change `effort` but thinking frequency or depth stays the same.

This happens because effort is the primary thinking lever only in adaptive mode. On extended-thinking-only models, thinking depth is set by `budget_tokens` instead.

Adjust `budget_tokens` on those models, or check which mode your model runs in; see [Thinking and effort](build-with-claude-thinking.md#thinking-and-effort). On Claude Opus 4.5, the one extended-thinking-only model that supports effort, effort composes with the budget; see [Budget rules and tuning](build-with-claude-extended-thinking.md#budget-rules-and-tuning).

## Next steps



[Thinking](build-with-claude-thinking.md)

The overview: what thinking is, how to configure it, and how it interacts with tools, caching, and streaming.



[Errors](../Endpoints/errors.md)

The full error reference, including the thinking configuration 400s with their exact server messages.



[Migrating to adaptive thinking](build-with-claude-extended-thinking.md#migrating-to-adaptive-thinking)

Convert `budget_tokens` requests to adaptive thinking with effort.
