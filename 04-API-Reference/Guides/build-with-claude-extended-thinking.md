---
title: "Extended thinking - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/extended-thinking"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:21Z"
tags: ["api", "prompting"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fextended-thinking)

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

# Extended thinking

Copy page



Configure manual extended thinking with a fixed budget_tokens budget on Claude models that support it, and migrate to adaptive thinking.

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).



Extended thinking (`thinking.type: "enabled"` with `budget_tokens`) is deprecated on the Claude 4.6 models (requests using it still succeed). Claude 4.7 and later models do not support it and reject requests that use it, returning a 400 error. On Claude 4.5 and earlier models that support thinking, extended thinking is the only available thinking mode. Claude Mythos Preview supports both modes. Where both modes are available, use [adaptive thinking](build-with-claude-thinking.md) instead.

See [Migrating to adaptive thinking](#migrating-to-adaptive-thinking) to move to adaptive thinking. If your model supports only extended thinking, this page describes the supported configuration; no change is needed until you move to a newer model.



If a request fails with a 400 error whose message starts with `"thinking.type.enabled" is not supported`, your model uses adaptive thinking instead. See [Troubleshooting thinking](build-with-claude-thinking-troubleshooting.md#error-thinking-type-enabled), or jump to [Migrating to adaptive thinking](#migrating-to-adaptive-thinking).

Extended thinking in manual mode gives you direct control over how much Claude thinks. You set a thinking token budget on each request with `thinking: {type: "enabled", budget_tokens: N}`, and Claude thinks against that budget before it starts its final answer. Manual mode remains useful when your workload requires predictable latency or precise control over thinking costs. This page covers how to set and tune the budget, how manual mode interacts with interleaved thinking and prompt caching, and how to migrate to adaptive thinking.

To learn how thinking itself works, including thinking blocks and the response shape, the `display` parameter, streaming, thinking with tool use, and encryption, see the [thinking overview](build-with-claude-thinking.md).

## Supported models

Extended thinking availability per model, including the models where extended thinking is the only mode, is listed in the [per-model configuration table](build-with-claude-thinking-troubleshooting.md#supported-models).

## How to use extended thinking

Here is an example of using extended thinking in the Messages API:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[
        {
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
        }
    ],
)

# The response contains summarized thinking blocks and text blocks
for block in response.content:
    match block.type:
        case "thinking":
            print(f"\nThinking summary: {block.thinking}")
        case "text":
            print(f"\nResponse: {block.text}")
```

To turn on manual extended thinking, add a `thinking` object with `type` set to `enabled` and a `budget_tokens` value.

The `budget_tokens` parameter sets a target for how many tokens Claude can use for its internal reasoning process. Larger budgets can improve response quality by enabling more thorough analysis for complex problems.

## Budget rules and tuning

`budget_tokens` must satisfy these constraints:

- **Minimum of 1,024 tokens.** The API rejects smaller values.
- **Less than `max_tokens`.** Thinking tokens count toward the `max_tokens` limit for the turn, so the budget must leave room for the final response. The one exception is [interleaved thinking](#interleaved-thinking), where `budget_tokens` can exceed `max_tokens` because the budget spans all thinking blocks within one assistant turn.
- **No cache pre-warming.** Because `budget_tokens` must be less than `max_tokens`, extended thinking cannot be combined with `max_tokens: 0` ([cache pre-warming](build-with-claude-prompt-caching.md#pre-warming-the-cache)).

The budget is a target rather than a strict cap. Actual token usage varies with the task, and Claude may stop reasoning well before the budget is exhausted; `max_tokens` remains the hard ceiling on total output.

On Claude Opus 4.5, the only extended-thinking-only model that supports [effort](build-with-claude-effort.md), effort shapes the overall response while `budget_tokens` sets thinking depth; set both.

To tune the budget:

- Match the starting point to the task. For simple tasks, start near the 1,024-token minimum and increase incrementally to find the optimal range for your use case. For complex tasks, start with a larger budget of 16,000 tokens or more and adjust to your latency and quality needs. Higher budgets enable more comprehensive reasoning, with diminishing returns that depend on the task, and at the cost of increased latency. For critical tasks, test different settings to find the right balance.
- For thinking budgets above 32k, use [batch processing](build-with-claude-batch-processing.md) to avoid networking issues. Pushing the model to think beyond 32k tokens produces long-running requests that can hit system timeouts and open-connection limits.

To track what a budget actually costs you, monitor the `usage.output_tokens_details.thinking_tokens` field in the response, which reports how many of the billed output tokens were internal reasoning. When streaming, this breakdown appears only on the final `message_delta` event.

When you are ready to move off manual budgets, see [Migrating to adaptive thinking](#migrating-to-adaptive-thinking).

## Interleaved thinking in manual mode

Interleaved thinking lets Claude think between tool calls within a single assistant turn, reasoning about each tool result before deciding what to do next. For the concept, the turn structure, and how it behaves on adaptive-thinking models, see [interleaved thinking](build-with-claude-thinking.md#interleaved-thinking) in the thinking overview. This section covers how to enable it when you use manual `type: "enabled"` thinking.

On Claude Opus 4.5, Claude Sonnet 4.5, and earlier Claude 4 models, add the `interleaved-thinking-2025-05-14` [beta header](../Endpoints/beta-headers.md) to your API request.

The 4.6 generation splits in manual mode:

- **Claude Sonnet 4.6**: the beta header with manual `type: "enabled"` is still functional but deprecated. Prefer [adaptive thinking](build-with-claude-thinking.md), which interleaves automatically with no header.
- **Claude Opus 4.6**: manual mode has no interleaved thinking at all. Only its adaptive mode interleaves, so switch to `thinking: {type: "adaptive"}` if you need reasoning between tool calls on this model.

Claude Haiku 4.5 does not support interleaved thinking. On the Claude API, the beta header is accepted but ignored.

Two more considerations for interleaved thinking in manual mode:

- `budget_tokens` can exceed `max_tokens` here; the [budget rules](#budget-rules-and-tuning) explain this exception.
- Interleaved thinking is only supported for [tools used through the Messages API](../Agents-Tools/agents-and-tools-tool-use-overview.md).

How platforms treat the beta header differs. The Claude API and [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md) accept `interleaved-thinking-2025-05-14` on any model and ignore it where unsupported. Acceptance is not the same as effect: on models that reject `type: "enabled"` (4.7 and later) or lack manual-mode interleaving (Claude Opus 4.6), the header has no manual-mode effect; adaptive thinking interleaves automatically there.

Partner-operated platforms ([Amazon Bedrock](build-with-claude-claude-in-amazon-bedrock.md) and [Google Cloud](build-with-claude-claude-on-vertex-ai.md)) likewise accept the header on any model without returning an error, and ignore it on models that don't support interleaved thinking.

## Turn structure in manual mode

The general turn-structure rules, including the single-turn tool-use loop, mid-turn conflict handling, and toggling thinking between turns, are on [Thinking with tool use](build-with-claude-thinking.md#thinking-with-tool-use).

Manual mode adds one requirement: the final assistant turn of a thinking-enabled request must begin with a thinking block ([adaptive thinking](build-with-claude-thinking.md) drops that requirement). Changing the thinking configuration between turns also invalidates prompt caching; see the following section.

## Prompt caching in manual mode

Manual mode adds one rule on top of the mode-neutral caching behavior described in [thinking and prompt caching](build-with-claude-thinking.md#thinking-and-prompt-caching): changing `budget_tokens` between requests invalidates cache breakpoints, just as switching thinking modes does, because the budget value is rendered into the prompt. Message-level breakpoints always miss after a budget change; whether tool and system-prompt breakpoints miss too depends on where the model renders the configuration.

In practice, pick a budget and hold it stable for the life of a cached conversation. Running a multi-turn conversation with message-level caching on Claude Sonnet 4.6 and changing the budget on the third request from 4,000 to 8,000 tokens shows the invalidation directly:

Output



``` block
First request - establishing cache
First response usage: { cache_creation_input_tokens: 1370, cache_read_input_tokens: 0, input_tokens: 17, output_tokens: 700 }

Second request - same thinking parameters (cache hit expected)
Second response usage: { cache_creation_input_tokens: 0, cache_read_input_tokens: 1370, input_tokens: 303, output_tokens: 874 }

Third request - different thinking budget (cache miss expected)
Third response usage: { cache_creation_input_tokens: 1370, cache_read_input_tokens: 0, input_tokens: 747, output_tokens: 619 }
```

The third request re-creates the cache (`cache_creation_input_tokens=1370`, `cache_read_input_tokens=0`) because the budget changed between requests. For a runnable version of the same experiment in adaptive mode, where the effort level plays the cache role that `budget_tokens` plays here, see [Prompt caching](build-with-claude-thinking-steering-and-cost.md#prompt-caching) on the steering page.

## Shared mechanics

Most thinking behavior is mode neutral and documented once on the [Thinking](build-with-claude-thinking.md) page. Everything there applies in manual mode too:

- [Controlling thinking display](build-with-claude-thinking.md#controlling-thinking-display)
- [Streaming thinking](build-with-claude-thinking.md#streaming-thinking)
- [Thinking with tool use](build-with-claude-thinking.md#thinking-with-tool-use), including [preserving thinking blocks](build-with-claude-thinking.md#preserving-thinking-blocks)
- [Thinking and prompt caching](build-with-claude-thinking.md#thinking-and-prompt-caching)
- [Thinking and the context window](build-with-claude-thinking.md#thinking-and-the-context-window)
- [Thinking encryption](build-with-claude-thinking.md#thinking-encryption)
- [Pricing](build-with-claude-thinking-steering-and-cost.md#pricing) (on the [Steering thinking](build-with-claude-thinking-steering-and-cost.md) page)

## Migrating to adaptive thinking

If your model supports only extended thinking (Claude Sonnet 4.5, Claude Opus 4.5, Claude Haiku 4.5, and earlier Claude 4 models), no action is needed now: adaptive thinking is not available there, and `type: "adaptive"` [returns a 400 error](build-with-claude-thinking-troubleshooting.md#error-thinking-type-adaptive). Keep `budget_tokens` until you move to a model that supports adaptive thinking, then apply the mapping that follows.

You need to migrate off `type: "enabled"` if:

- You use Claude Opus 4.6 or Claude Sonnet 4.6, where `budget_tokens` is deprecated.
- You use Claude 4.7 or a later model, such as Claude Opus 5.5, Claude Sonnet 5, or Claude Fable 5.1, where `type: "enabled"` returns a 400 error.

The mapping is small: remove `budget_tokens`, set `thinking: {type: "adaptive"}`, and control reasoning depth with `output_config: {effort: ...}` instead of a token budget.

```python
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 16000,
  "thinking": {
    "type": "enabled",
    "budget_tokens": 10000
  }
}
```



becomes:

```python
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 16000,
  "thinking": {
    "type": "adaptive"
  },
  "output_config": {
    "effort": "high"
  }
}
```



`effort: "high"` matches the API default; it appears here only to show where the depth control now lives, and omitting it produces identical behavior.

Expect a behavioral difference, not just a syntax change. With a fixed budget, Claude thinks on every request. With adaptive thinking, Claude decides whether and how much to think on each request, and at lower [effort](build-with-claude-effort.md) settings it may skip thinking entirely on easy inputs. You can also remove the `interleaved-thinking-2025-05-14` beta header after migrating: adaptive thinking interleaves automatically, and the Claude API ignores the header on these models. Thinking block preservation changes too: Claude Opus 4.5 and models numbered 4.6 and higher keep prior turns' thinking blocks in context and bill them as input, where Claude Sonnet 4.5, Claude Haiku 4.5, and earlier models stripped them; see [thinking block preservation by model](build-with-claude-thinking.md#thinking-block-preservation-by-model).

Switching modes is a thinking-configuration change, so the first request after the switch invalidates cache breakpoints, as described in [Prompt caching in manual mode](#extended-thinking-with-prompt-caching).

For full guidance, see [adaptive thinking](build-with-claude-thinking.md), [effort](build-with-claude-effort.md), and the [model migration guide](../../20-Models/about-claude-models-migration-guide.md).

## Next steps



[Thinking](build-with-claude-thinking.md)

Learn how thinking works: blocks, display, streaming, and tool use.

[Steering thinking](build-with-claude-thinking-steering-and-cost.md)

Let Claude decide when and how much to think on each request.



[Thinking in tool and multi-turn workflows](build-with-claude-thinking-tool-workflows.md)

Preserve thinking blocks and manage thinking across tool calls and turns.
