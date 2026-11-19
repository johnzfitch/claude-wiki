---
title: "What's new in Claude Opus 5.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5"
category: "20-Models"
fetched_at: "2026-11-16T06:26:18Z"
tags: ["models"]
---

# What’s new in Claude Opus 5.5

Copy page



Overview of breaking changes, feature support, and behavior differences in Claude Opus 5.5.

Copy page



Claude Opus 5.5 is built for long-running agentic coding and knowledge work, priced at \$4 / \$20 USD per million input / output tokens. Four breaking changes can affect code already running on Claude Opus 5:

- [Thinking can’t be disabled](#thinking-cant-be-disabled).
- [Forced tool use returns an error](#forced-tool-use-is-not-supported).
- [Thinking blocks are tied to the model and the conversation](#thinking-blocks-are-tied-to-the-model-that-produced-them).
- [Some computer use tool versions are not supported](#computer-20251124-is-not-supported).

The first three also apply on Claude Fable 5.1. A further change alters the response shape without failing any request: [text between tool calls comes back in `thinking` blocks](#text-between-tool-calls) whose text is empty at the default `display` setting. An application that streams that text to its users as progress updates goes quiet between tool calls until it sets a `display` value that returns the text.

## New model

| Model | Claude API ID | Description |
|:---|:---|:---|
| Claude Opus 5.5 | claude-opus-5-5 | For long-running agentic coding and knowledge work |

[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is always on, and the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) controls thinking depth; its default on this model is `medium`. For the context window, output limits, knowledge cutoff, and prices, see the [Claude Opus 5.5](models-opus-5-5-overview.md) model page; for all current models, see [Models overview](about-claude-models-overview.md).

## Breaking changes

### Thinking can’t be disabled

On Claude Opus 5, thinking is on by default and `thinking: {"type": "disabled"}` is accepted at effort `high` or below. On Claude Opus 5.5, thinking is always on: a request that sets `thinking: {"type": "disabled"}`, or one that sets a manual budget with `thinking: {"type": "enabled", "budget_tokens": N}`, returns a 400 `invalid_request_error`. Omit the `thinking` field, or send `thinking: {"type": "adaptive"}`, which is equivalent.

The error messages are:

```
"thinking.type.disabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```



```
"thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```



The [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) is the control for thinking depth, latency, and cost: lower it where you previously disabled thinking; [Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md#tune-effort) has measured results for choosing a level. Because every response can start with one or more `thinking` blocks (returned with an empty `thinking` field at the default `display: "omitted"`), select content blocks by their `type` field rather than by position, and pass `thinking` blocks back unmodified in tool-use loops. Code that already runs on Claude Opus 5 with thinking on needs no change. See [Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) and the migration guide’s [before and after for thinking](models-opus-5-5-migration-guide.md#thinking-cant-be-disabled).

### Forced tool use is not supported

Claude Opus 5.5 doesn’t support forced tool use. `tool_choice` set to `{"type": "any"}` or `{"type": "tool", "name": "..."}` returns a 400 `invalid_request_error`:

```
tool_choice: type "tool" and "any" are not supported for this model.
```



`tool_choice: {"type": "auto"}` (the default) and `{"type": "none"}` are supported, and the same validation applies to the [token counting](../04-API-Reference/Guides/build-with-claude-token-counting.md) endpoint. For schema-valid JSON, keep `tool_choice: {"type": "auto"}` and set `strict: true` with [strict tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md), or move the schema to [structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md). To make the model call a tool rather than reply in text, say in the prompt when the tool applies. The migration guide shows the [before and after for tool choice](models-opus-5-5-migration-guide.md#forced-tool-use).

### Thinking blocks are tied to the model and the conversation

Every thinking block records which model produced it. A conversation that switches models keeps its earlier reasoning only if the model that it switches to can read the earlier model’s thinking blocks:

| Switch | Keeps its reasoning |
|----|----|
| To Claude Opus 5.5, from Claude Opus 5 or earlier, Claude Sonnet 5 or earlier, or Claude Haiku 4.5 or earlier | Yes |
| To Claude Opus 5.5, from Claude Sonnet 5.5 or Claude Haiku 5.5 | Yes, on the Claude API and Claude Models on Google Cloud (Google managed) only |
| To Claude Opus 5.5, from a Claude Fable or Claude Mythos model | No |
| From Claude Opus 5.5, to Claude Fable 5.2 or Claude Mythos 5.2 | Yes, on the Claude API and Claude Models on Google Cloud (Google managed) only |
| From Claude Opus 5.5, to Claude Fable 5.1 or Claude Mythos 5.1 | Yes, on the Claude API only |
| From Claude Opus 5.5, to any other model | No |

When a request carries a block the target model can’t read, the API drops it before the model receives it. The request succeeds, and dropped blocks aren’t billed. With the `thinking-binding-controls-2026-08-01` beta header, the API reports the drop in a top-level `input_transformations` array. See [Switch models and back](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md#switching-models). For switches that don’t involve Claude Opus 5.5, see [Which model switches keep the reasoning on the Claude API](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md#which-model-switches-keep-reasoning).

The API also checks whether anything before a Claude Opus 5.5 thinking block has changed since the model produced the block. This prefix check covers the `system` prompt, the `tools`, and every earlier message. Keep the conversation append-only: change instructions or tools with [mid-conversation system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md) rather than edits.

Failing the [prefix check](../04-API-Reference/Guides/build-with-claude-preserved-thinking-prefix-checks.md#prefix-check) might or might not result in a [400 error](../04-API-Reference/Endpoints/errors.md#thinking-block-conversation-mismatch). To identify and handle both cases, see [Prefix checks on thinking blocks](../04-API-Reference/Guides/build-with-claude-preserved-thinking-prefix-checks.md).

The prefix check runs on the Claude API and on [some cloud platforms](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md#feature-availability).

See [Preserved thinking](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md) and the migration guide’s [note on thinking blocks](models-opus-5-5-migration-guide.md#thinking-blocks).

### Some computer use tool versions are not supported

Claude Opus 5.5 supports [computer use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) through the `computer_toolset_20260801` toolset. On Amazon Bedrock, Claude Opus 5.5 also accepts the `computer_20251124` tool with the `computer-use-2025-11-24` beta header. Claude Opus 5.5 returns a 400 error for any computer use tool version it doesn’t accept, such as `computer_20251124` on the Claude API. The Claude API’s `invalid_request_error` message names the rejected type and, after `Did you mean one of`, lists the tool types the model accepts. The message begins:

```python
'claude-opus-5-5' does not support tool types: computer_20251124.
```



Integrations that use the toolset need no change. To move a `computer_20251124` integration to the toolset, follow [Migrate from `computer_20251124`](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#migrate-from-computer-20251124). Drop the beta header and replace the `tools` entry with `{"type": "computer_toolset_20260801"}`. Then update your agent loop for member `tool_use` blocks, batch actions, and `toolset_name` on results. The migration guide shows the [before and after for computer use](models-opus-5-5-migration-guide.md#computer-use-toolset).

## Feature support

Claude Opus 5.5 supports [per-message effort](../04-API-Reference/Guides/build-with-claude-effort-per-message.md), [mid-conversation system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md), [task budgets](../04-API-Reference/Guides/build-with-claude-task-budgets.md), [prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) with a 512-token minimum cacheable prompt, [batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md), the [Files API](../04-API-Reference/Guides/build-with-claude-files.md), [PDF support](../04-API-Reference/Guides/build-with-claude-pdf-support.md), [vision](../04-API-Reference/Guides/build-with-claude-vision.md), and server-side and client-side tools (see [Tool use with Claude](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md)). Task budgets and per-message effort are in beta. See each feature’s page for model availability.

### Fast mode

[Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) is available for Claude Opus 5.5 on the Claude API, on [Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md), and on [Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md) for deployments hosted on Azure. On the Claude API and on Claude Models on Google Cloud (Anthropic managed), set `speed: "fast"` on your request. See [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) for supported models, rate limits, and pricing.

### Define tools in a message (beta)

With the `inline-tools-2026-09-15` beta header, a `tool_addition` block in a mid-conversation system message can carry a full tool definition instead of a reference, so you can add a tool, change its schema, or move a server tool to a newer version mid-conversation without editing `tools` and without losing the prompt cache. This works on every model that supports mid-conversation tool changes, including Claude Opus 5.5. See [Define tools in a message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#define-tools-in-a-message-beta).

### Compact on demand (beta)

With the `compact-2026-09-04` beta header, a request that sends the top-level `compaction` parameter returns a signed `compaction` block summarizing the whole conversation, which you then send first in place of the summarized messages. It is available on the models that support compaction, Claude Opus 5.5 included. You choose when to compact, and the request can run in the background. Under the conditions in [Compaction and preserved thinking](../04-API-Reference/Guides/build-with-claude-compaction-thinking-blocks.md#conditions-for-kept-thinking-to-stay-valid), the thinking blocks in the turns you keep can stay valid after the swap. This matters on Claude Opus 5.5 because its [thinking blocks are tied to the conversation](#thinking-blocks-are-tied-to-the-model-that-produced-them). See [Compaction on demand](../04-API-Reference/Guides/build-with-claude-compaction-on-demand.md) for platform availability and the full request flow.

## Behavior differences

Claude Opus 5.5 differs from Claude Opus 5 in several ways that show up without any code change. Each has guidance in [Prompting Claude Opus 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md):

- **The default effort is `medium`.** A request that omits `effort` runs at `medium`; on Claude Opus 5 it ran at `high`. Set `effort` explicitly and re-run your sweep; see [Calibrate effort](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#calibrate-effort).
- **More thinking per turn at a given effort level.** At the same [effort](../04-API-Reference/Guides/build-with-claude-effort.md) setting the model tends to think more per turn than Claude Opus 5, most of all at `xhigh` and `max`. Re-run your effort sweep rather than carrying a setting over, and leave room in `max_tokens` for the thinking. See [Calibrate effort](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#calibrate-effort).
- **Text between tool calls comes back in thinking blocks.** The short notes the model writes between tool calls arrive as [progress-update `thinking` blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#progress-updates) rather than `text` blocks. At the default `display: "omitted"`, an application that streams them to its users goes quiet between tool calls, with no error. The migration guide explains [how to receive text between tool calls](models-opus-5-5-migration-guide.md#text-between-tool-calls). For how to ask for more of them, see [User-facing progress updates](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#user-facing-progress-updates).
- **More safeguard categories.** The model runs a biology safety classifier in addition to the cybersecurity one. As on Claude Opus 5, requests that push it to reproduce its internal reasoning in the response text might be declined with the `reasoning_extraction` category. See [Refusals and fallback in Claude Opus 5.5](#refusals-and-fallback) and [Safeguard refusals](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#safeguard-refusals).
- **Sharper reading of charts, diagrams, and screenshots.** The model reads values off dense charts and layout-dependent visuals much more precisely without tools, so prompt-side vision workarounds built for earlier models might no longer be needed; image tools still add accuracy on the densest inputs. See [Tools for complex visual inputs](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#tools-for-complex-visual-inputs).

If your Claude Opus 5 integration ran with thinking disabled, see [Prompts written for thinking disabled](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#prompts-written-for-thinking-disabled) alongside the breaking change [Thinking can’t be disabled](#thinking-cant-be-disabled). For the capability gains in agentic coding and code review, knowledge work, communication, visual inputs, and computer use, see [Capabilities relevant to prompting](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#capability-improvements).

## Refusals and fallback

Claude Opus 5.5 ships with safety classifiers, and everything in [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md) applies. A declined request returns HTTP 200 with `stop_reason: "refusal"` and a [`stop_details`](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response) object naming the policy area, so handle refusals and configure fallback: retry on another model with [server-side fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#server-side-fallback) (`fallbacks: "default"`, in beta, retries on the model Anthropic recommends for that category), the [SDK middleware](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#client-side-fallback), or your own retry. Whether a refusal that arrives before any output is billed depends on its refusal category, and it counts against your rate limits either way; see [How refusals are billed](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#how-refusals-are-billed).

## Pricing

Claude Opus 5.5 costs \$4 USD per million input tokens and \$20 USD per million output tokens, below Claude Opus 5’s \$5 and \$25 USD, with 5-minute cache writes at \$5 USD, 1-hour cache writes at \$8 USD, and cache reads at \$0.20 USD per million tokens (0.05x the base input price). [Batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md) is half price: \$2 and \$10 USD. See [Pricing](../17-Billing-Plans/about-claude-pricing.md) for data residency and tool pricing.

## Availability

Claude Opus 5.5 is available on:

- **Claude API:** all customers, as `claude-opus-5-5`
- **AWS:** [Claude in Amazon Bedrock (`bedrock-mantle`)](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), as `anthropic.claude-opus-5-5`, and [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md), as `claude-opus-5-5`
- **Google Cloud:** [Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md), as `claude-opus-5-5`, and [Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md), as `claude-opus-5-5`
- **Microsoft Foundry:** [Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md), as `claude-opus-5-5`

## Migrate from Claude Opus 5

Update your model ID:

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
model = "claude-opus-5"  # Before
model = "claude-opus-5-5"  # After
```

Then remove any `thinking: {"type": "disabled"}` or `thinking: {"type": "enabled", ...}` settings and choose an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level instead. Replace `tool_choice` types `any` and `tool` with `auto` plus [strict tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md). If you use computer use through `computer_20251124`, [move to the toolset](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#migrate-from-computer-20251124). On Amazon Bedrock, `computer_20251124` also works. If your interface shows the text between tool calls, also set `thinking.display`; see [Text between tool calls is returned in thinking blocks](models-opus-5-5-migration-guide.md#text-between-tool-calls). See the [Claude Opus 5.5 migration guide](models-opus-5-5-migration-guide.md) for step-by-step instructions from Claude Opus 5 and earlier models, and the full checklist.

## Next steps



[Models overview](about-claude-models-overview.md)

Complete specs and pricing for all current Claude models.



[Migration guide](models-opus-5-5-migration-guide.md)

Move code from Claude Opus 5 and earlier models to Claude Opus 5.5.



[Prompting Claude Opus 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md)

Behavioral differences and prompting patterns specific to Claude Opus 5.5.



[Effort](../04-API-Reference/Guides/build-with-claude-effort.md)

Control how many tokens Claude uses when responding, from low to max.



[Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)

How adaptive thinking works and how thinking blocks are preserved.



[Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md)

Handle `stop_reason: "refusal"` and retry on another model.
