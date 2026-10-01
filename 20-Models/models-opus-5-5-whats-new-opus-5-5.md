---
title: "What's new in Claude Opus 5.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5"
category: "20-Models"
fetched_at: "2026-09-30T06:31:07Z"
tags: ["models"]
---

- [Managed Agents](../04-API-Reference/Other/managed-agents-overview.md)

- [Admin](../04-API-Reference/Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../04-API-Reference/About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../04-API-Reference/Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](release-notes-overview.md)

[API reference](../04-API-Reference/Endpoints/overview.md)




[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fopus-5-5%2Fwhats-new-opus-5-5)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Overview](models-opus-5-5-overview.md)[What's new](models-opus-5-5-whats-new-opus-5-5.md)[Migration guide](models-opus-5-5-migration-guide.md)

[Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

[Claude Haiku 4.5](models-haiku-4-5-overview.md)

Specialized models

Legacy models

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)

[Models & pricing](about-claude-models-overview.md)Claude Opus 5.5

# What's new in Claude Opus 5.5

Copy page



Overview of breaking changes, feature support, and behavior differences in Claude Opus 5.5.

Copy page



Claude Opus 5.5 is built for long-running agentic coding and knowledge work, priced at \$4 / \$20 USD per million input / output tokens. Four breaking changes affect code already running on Claude Opus 5: [thinking can't be disabled](#thinking-cant-be-disabled), [forced tool use returns an error](#forced-tool-use-is-not-supported), [thinking blocks are tied to the model and the conversation](#thinking-blocks-are-tied-to-the-model-that-produced-them), and, on the Claude API and Google Cloud, [the earlier `computer_20251124` computer use tool is not accepted](#computer-20251124-is-not-supported). The first three also apply on Claude Fable 5.1. A further change alters the response shape without failing any request: [text between tool calls comes back in `thinking` blocks](#text-between-tool-calls) whose text is empty at the default `display` setting. An application that streams that text to its users as progress updates goes quiet between tool calls until it sets a `display` value that returns the text.

## New model

| Model           | Claude API ID   | Description                                        |
|:----------------|:----------------|:---------------------------------------------------|
| Claude Opus 5.5 | claude-opus-5-5 | For long-running agentic coding and knowledge work |

[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is always on, and the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) controls thinking depth; its default on this model is `medium`. For the context window, output limits, knowledge cutoff, and prices, see the [Claude Opus 5.5 model page](models-opus-5-5-overview.md); for all current models, see the [models overview](about-claude-models-overview.md).

## Breaking changes

### Thinking can't be disabled

On Claude Opus 5, thinking is on by default and `thinking: {"type": "disabled"}` is accepted at effort `high` or below. On Claude Opus 5.5, thinking is always on: a request that sets `thinking: {"type": "disabled"}`, or a manual budget with `thinking: {"type": "enabled", "budget_tokens": N}`, returns a 400 `invalid_request_error`. Omit the `thinking` field, or send `thinking: {"type": "adaptive"}`, which is equivalent. No beta header is involved.

The error messages are:

``` block
"thinking.type.disabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```



``` block
"thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```



The [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) is the control for thinking depth, latency, and cost: lower it where you previously disabled thinking; [Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md#tune-effort) has measured results for choosing a level. Because every response can begin with one or more `thinking` blocks (returned with an empty `thinking` field at the default `display: "omitted"`), select content blocks by their `type` field rather than by position, and pass `thinking` blocks back unmodified in tool-use loops. Code that already runs on Claude Opus 5 with thinking on needs no change. See [Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) and the migration guide's [before and after](models-opus-5-5-migration-guide.md#thinking-cant-be-disabled).

### Forced tool use is not supported

Claude Opus 5.5 doesn't support forced tool use. `tool_choice` set to `{"type": "any"}` or `{"type": "tool", "name": "..."}` returns a 400 `invalid_request_error`:

``` block
tool_choice: type "tool" and "any" are not supported for this model.
```



`tool_choice: {"type": "auto"}` (the default) and `{"type": "none"}` are supported, and the same validation applies to the [token counting](../04-API-Reference/Guides/build-with-claude-token-counting.md) endpoint. For schema-valid JSON, keep `tool_choice: {"type": "auto"}` and set `strict: true` with [strict tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md), or move the schema to [structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md). To make the model call a tool rather than reply in text, say in the prompt when the tool applies. The migration guide shows the [before and after](models-opus-5-5-migration-guide.md#forced-tool-use).

### Thinking blocks are tied to the model and the conversation

Every thinking block records which model produced it, and each model reads its own blocks and only some other models'. Claude Opus 5.5 reads thinking blocks from Claude Opus 5 and earlier Opus, Sonnet, and Haiku models, but not from Claude Fable or Claude Mythos models. On the Claude API, Claude Fable 5.1 and Claude Mythos 5.1 read thinking blocks from Claude Opus 5.5; no other model does. A conversation that moves from Claude Opus 5 onto Claude Opus 5.5, or from Claude Opus 5.5 up to Claude Fable 5.1 or Claude Mythos 5.1 on the Claude API, keeps its reasoning. One that moves from Claude Opus 5.5 to any model other than those two, or onto it from a Claude Fable or Claude Mythos model, runs the turns after the switch without the previous model's reasoning. When a request carries a block the target model can't read, the API drops it before the model sees it: the request succeeds, and dropped blocks aren't billed. With the `thinking-binding-controls-2026-08-01` beta header the drop is reported in a top-level `input_transformations` array. See [Switching models mid-conversation](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md#switching-models).

The API also checks whether anything before a Claude Opus 5.5 thinking block (the `system` prompt, the `tools`, or an earlier message) has changed since the block was produced. As on Claude Fable 5.1, it enforces that check by default for accounts created on or after August 31, 2026, 00:00 UTC, on the Claude API and on cloud platforms. On those accounts, a request that replays a block after such a change returns a 400 error. To drop the affected blocks instead, send the `thinking-binding-controls-2026-08-01` beta header and set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`. On older accounts, setting that field to either value opts the request in. Keep the conversation append-only so the question never arises: change instructions or tools with [mid-conversation system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md) rather than edits. See [Preserved thinking](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md) and the migration guide's [note on this change](models-opus-5-5-migration-guide.md#thinking-blocks).

### The `computer_20251124` computer use tool is not supported on the Claude API and Google Cloud

Claude Opus 5 accepts [computer use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) both as the `computer_toolset_20260801` toolset and, with the `computer-use-2025-11-24` beta header, as the earlier `computer_20251124` tool. On the Claude API and Google Cloud, Claude Opus 5.5 supports only the toolset: a request that declares a `computer_20251124` tool returns a 400 `invalid_request_error`. The message names the rejected type, then lists the tool types the model does accept (`computer_toolset_20260801` among them) after `Did you mean one of`; it begins:

```python
'claude-opus-5-5' does not support tool types: computer_20251124.
```



To move an existing integration on the Claude API or Google Cloud, follow [Migrate from `computer_20251124`](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#migrate-from-computer-20251124): drop the beta header, replace the `tools` entry with `{"type": "computer_toolset_20260801"}`, and update your agent loop for member `tool_use` blocks, batch actions, and `toolset_name` on results. On Amazon Bedrock, the earlier `computer_20251124` tool continues to work on Claude Opus 5.5 as it does on Claude Opus 5, so no change is needed there. For other platforms, see the computer use tool's [Compatibility](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#compatibility) section. Integrations that already use the toolset, and the [browser use tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md), need no change. The migration guide shows the request [before and after](models-opus-5-5-migration-guide.md#computer-use-toolset).

## Feature support

Claude Opus 5.5 supports [per-message effort](../04-API-Reference/Guides/build-with-claude-effort.md#change-effort-mid-conversation-beta) (beta), [mid-conversation system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md), [task budgets](../04-API-Reference/Guides/build-with-claude-task-budgets.md), [prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) with a 512-token minimum cacheable prompt, [batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md), the [Files API](../04-API-Reference/Guides/build-with-claude-files.md), [PDF support](../04-API-Reference/Guides/build-with-claude-pdf-support.md), [vision](../04-API-Reference/Guides/build-with-claude-vision.md), and server-side and client-side [tools](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md). On the Claude API and Google Cloud, computer use requires the `computer_toolset_20260801` toolset (see the [breaking change](#computer-20251124-is-not-supported)). See each feature's page for model availability.

### Fast mode

[Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) (research preview) is available for Claude Opus 5.5 on the Claude API only; it is not available on Amazon Bedrock, Claude Platform on AWS, Google Cloud, or Microsoft Foundry. Set `speed: "fast"` with the `fast-mode-2026-02-01` beta header. See [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) for access, supported models, and pricing.

### Define tools in a message (beta)

With the `inline-tools-2026-09-15` beta header, a `tool_addition` block in a mid-conversation system message can carry a full tool definition instead of a reference, so you can add a tool, change its schema, or move a server tool to a newer version mid-conversation without editing `tools` and without losing the prompt cache. This works on every model that supports mid-conversation tool changes, including Claude Opus 5.5. See [Define tools in a message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#define-tools-in-a-message-beta).

### Compact on demand (beta)

With the `compact-2026-09-04` beta header, a request that sends the top-level `compaction` parameter returns a signed `compaction` block summarizing the whole conversation, which you then send first in place of the summarized messages. It is available on the models that support compaction, Claude Opus 5.5 included. You choose when to compact, the request can run in the background, and the thinking blocks in the turns you keep can stay valid after the swap (under the conditions in [Compaction and preserved thinking](../04-API-Reference/Guides/build-with-claude-compaction-thinking-blocks.md#conditions-for-kept-thinking-to-stay-valid)), which matters on Claude Opus 5.5 because its [thinking blocks are tied to the conversation](#thinking-blocks-are-tied-to-the-model-that-produced-them). See [Compaction on demand](../04-API-Reference/Guides/build-with-claude-compaction-on-demand.md) for platform availability and the full request flow.

## Behavior differences

Claude Opus 5.5 differs from Claude Opus 5 in several ways that show up without any code change. Each has guidance in [Prompting Claude Opus 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md):

- **The default effort is `medium`.** A request that omits `effort` runs at `medium`; on Claude Opus 5 it ran at `high`. Set `effort` explicitly and re-run your sweep; see [Calibrate effort](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#calibrate-effort).
- **More thinking per turn at a given effort level.** At the same [effort](../04-API-Reference/Guides/build-with-claude-effort.md) setting the model tends to think more per turn than Claude Opus 5, most of all at `xhigh` and `max`. Re-run your effort sweep rather than carrying a setting over, and leave room in `max_tokens` for the thinking. See [Calibrate effort](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#calibrate-effort).
- **Text between tool calls comes back in thinking blocks.** The short notes the model writes between tool calls arrive as [progress-update `thinking` blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#progress-updates) rather than `text` blocks, so at the default `display: "omitted"` an application that streams them to its users goes quiet between tool calls, with no error. The [migration guide](models-opus-5-5-migration-guide.md#text-between-tool-calls) has the fix for receiving them, and [User-facing progress updates](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#user-facing-progress-updates) covers how to ask for more of them.
- **More safeguard categories.** The model runs a biology safety classifier in addition to the cybersecurity one, and requests that push it to reproduce its internal reasoning in the response text can be declined with the `reasoning_extraction` category. See [Refusals and fallback](#refusals-and-fallback) and [Safeguard refusals](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#safeguard-refusals).
- **Sharper reading of charts, diagrams, and screenshots.** The model reads values off dense charts and layout-dependent visuals much more precisely without tools, so prompt-side vision workarounds built for earlier models may no longer be needed; image tools still add accuracy on the densest inputs. See [Tools for complex visual inputs](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#tools-for-complex-visual-inputs).

If your Claude Opus 5 integration ran with thinking disabled, see [Prompts written for thinking disabled](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#prompts-written-for-thinking-disabled) alongside the [breaking change](#thinking-cant-be-disabled). For the capability gains in agentic coding and code review, knowledge work, communication, visual inputs, and computer use, see [Capabilities relevant to prompting](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#capability-improvements).

## Refusals and fallback

Claude Opus 5.5 ships with safety classifiers, and everything in [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md) applies. A declined request returns HTTP 200 with `stop_reason: "refusal"` and a [`stop_details`](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response) object naming the policy area, so handle refusals and configure fallback: retry on another model with [server-side fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#server-side-fallback) (`fallbacks: "default"`, in beta, retries on the model Anthropic recommends for that category), the [SDK middleware](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#client-side-fallback), or your own retry. Whether a refusal that arrives before any output is billed depends on its refusal category, and it counts against your rate limits either way; see [How refusals are billed](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#how-refusals-are-billed).

## Pricing

Claude Opus 5.5 costs \$4 USD per million input tokens and \$20 USD per million output tokens, below Claude Opus 5's \$5 and \$25, with 5-minute cache writes at \$5, 1-hour cache writes at \$8, and cache reads at \$0.20 per million tokens (0.05x the base input price). [Batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md) is half price: \$2 and \$10. See [Pricing](../17-Billing-Plans/about-claude-pricing.md) for data residency and tool pricing.

## Availability

Claude Opus 5.5 is available on:

- **Claude API:** all customers, as `claude-opus-5-5`.
- **AWS:** [Claude in Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), as `anthropic.claude-opus-5-5`, and [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md), as `claude-opus-5-5`.
- **Google Cloud:** [Claude on Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md), as `claude-opus-5-5`.
- **Microsoft Foundry:** [Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md), as `claude-opus-5-5`.

## Migrate from Claude Opus 5

Update your model ID:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
model = "claude-opus-5"  # Before
model = "claude-opus-5-5"  # After
```

Then remove any `thinking: {"type": "disabled"}` or `thinking: {"type": "enabled", ...}` settings and choose an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level instead. Replace `tool_choice` types `any` and `tool` with `auto` plus [strict tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md). If you use computer use through `computer_20251124` on the Claude API or Google Cloud, [move to the toolset](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#migrate-from-computer-20251124). If your interface shows the text between tool calls, also set `thinking.display`; see [Text between tool calls is returned in thinking blocks](models-opus-5-5-migration-guide.md#text-between-tool-calls). See the [migration guide](models-opus-5-5-migration-guide.md) for step-by-step instructions from Claude Opus 5 and earlier models, and the full checklist.

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
