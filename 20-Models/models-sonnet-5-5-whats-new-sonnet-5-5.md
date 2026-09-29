---
title: "What's new in Claude Sonnet 5.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5"
category: "20-Models"
fetched_at: "2026-09-29T06:30:57Z"
tags: ["billing", "models"]
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fsonnet-5-5%2Fwhats-new-sonnet-5-5)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

[Overview](models-sonnet-5-5-overview.md)[What's new](models-sonnet-5-5-whats-new-sonnet-5-5.md)[Migration guide](models-sonnet-5-5-migration-guide.md)

[Claude Haiku 4.5](models-haiku-4-5-overview.md)

Specialized models

Legacy models

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)

[Models & pricing](about-claude-models-overview.md)Claude Sonnet 5.5

# What's new in Claude Sonnet 5.5

Copy page



What changes when you move from Claude Sonnet 5 to Claude Sonnet 5.5: breaking changes, feature support, behavior differences, pricing, and availability.

Copy page



Claude Sonnet 5.5 offers the best combination of speed and intelligence. Five breaking changes affect code already running on Claude Sonnet 5:

- [Turn off up-front thinking with `between_tools`](#turn-off-up-front-thinking).
- [Forced tool use returns an error](#forced-tool-use-is-not-supported).
- [Thinking blocks are tied to the model and the conversation](#thinking-blocks-are-tied-to-the-model-that-produced-them).
- [On the Claude API and Google Cloud, the earlier `computer_20251124` computer use tool is not accepted](#computer-20251124-is-not-supported).
- [The advisor tool rejects Claude Opus 4.8, Claude Opus 4.7, and Claude Sonnet 5 as advisors](#advisor-tool-pairings).

One more change alters the response shape without failing any request: [text between tool calls comes back in `thinking` blocks](#text-between-tool-calls). An application that streams that text to its users goes quiet between tool calls until it sets a `display` value that returns the text, or turns off up-front thinking with `between_tools`.

## New model

| Model             | Claude API ID     | Description                                    |
|:------------------|:------------------|:-----------------------------------------------|
| Claude Sonnet 5.5 | claude-sonnet-5-5 | The best combination of speed and intelligence |

[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is on by default, and the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) controls thinking depth. Its default on the Claude API is `high`. The tokenizer is the same as Claude Sonnet 5's, so the same text produces the same token counts. For the context window, output limits, knowledge cutoff, and prices, see the [Claude Sonnet 5.5 model page](models-sonnet-5-5-overview.md).

For all current models, see the [models overview](about-claude-models-overview.md).

## Breaking changes

### Turn off up-front thinking with `between_tools`

To turn off up-front thinking on Claude Sonnet 5.5, send `thinking: {"type": "between_tools"}` instead of `"disabled"`. It's the lowest thinking setting on this model. It's available on every platform that offers Claude Sonnet 5.5. It needs no beta header. The short [progress updates](../04-API-Reference/Guides/build-with-claude-thinking.md#progress-updates) the model writes between tool calls still come back as `thinking` blocks with their summary text. Pass those blocks back unchanged with the rest of the assistant turn. A progress-update block you send back gives the model the full note it wrote, not the summary. If your requests don't use tools, the response contains only text, as with `disabled` on Claude Sonnet 5.

On Claude Sonnet 5.5, a request that sends `thinking: {"type": "disabled"}` returns a 400 `invalid_request_error` whose message points to `between_tools`.

`between_tools` is accepted at `low`, `medium`, and `high` effort. At `xhigh` or `max` effort, a request with `between_tools` returns a 400 error. To run at `xhigh` or `max`, use adaptive thinking: omit the `thinking` field or send `thinking: {"type": "adaptive"}`, which is equivalent. With `between_tools`, effort can't change mid-conversation: a [per-message](../04-API-Reference/Guides/build-with-claude-effort.md#change-effort-mid-conversation-beta) `output_config.effort` that differs from the level in effect returns a 400 error. To vary effort per turn, use adaptive thinking.

`between_tools` takes no other field: `display`, `budget_tokens`, or `block_binding` sent with it returns a 400 error. Manual thinking budgets (`thinking: {"type": "enabled", "budget_tokens": N}`) return a 400 error. See [Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) and the migration guide's [before and after](models-sonnet-5-5-migration-guide.md#turn-off-up-front-thinking).

### Forced tool use is not supported

Claude Sonnet 5.5 doesn't support forced tool use. `tool_choice` set to `{"type": "any"}` or `{"type": "tool", "name": "..."}` returns a 400 `invalid_request_error`:

``` block
tool_choice: type "tool" and "any" are not supported for this model.
```



`tool_choice: {"type": "auto"}` (the default) and `{"type": "none"}` are supported. The same check applies to the [token counting](../04-API-Reference/Guides/build-with-claude-token-counting.md) endpoint. For schema-valid tool input, keep `tool_choice: {"type": "auto"}` and set `strict: true` with [strict tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md), or move the schema to [structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md). To make the model call a tool rather than reply in text, say in the prompt when the tool applies. The migration guide shows the [before and after](models-sonnet-5-5-migration-guide.md#forced-tool-use).

### Thinking blocks are tied to the model and the conversation

Every thinking block records which model produced it. Each model reads its own blocks and only some other models' blocks. Claude Sonnet 5.5 reads thinking blocks from Claude Sonnet 5, Claude Opus 4.8, Claude Haiku 4.5, and earlier models, but not from Claude Opus 5, Claude Opus 5.5, or any Claude Fable or Claude Mythos model. No other model reads Claude Sonnet 5.5 thinking blocks.

So a conversation that moves from Claude Sonnet 5 onto Claude Sonnet 5.5 keeps its reasoning, and one that moves from Claude Sonnet 5.5 to any other model runs the turns after the switch without it. When a request carries a block the target model can't read, the API drops it before the model sees it: the request succeeds, and dropped blocks aren't billed. With the `thinking-binding-controls-2026-08-01` beta header, the drop is reported in a top-level `input_transformations` array. See [Switching models mid-conversation](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md#switching-models).

The API also checks whether anything before a Claude Sonnet 5.5 thinking block has changed since the block was produced: the `system` prompt, the `tools`, or an earlier message. It enforces that check by default for accounts created on or after August 31, 2026, 00:00 UTC, on the Claude API, Amazon Bedrock, and Google Cloud. On those accounts, a request that replays a block after such a change returns a 400 error. To drop the affected blocks instead, send the `thinking-binding-controls-2026-08-01` beta header and set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`. On older accounts, setting that field to either value opts the request in. `block_binding` works only with `thinking: {"type": "adaptive"}`. With `between_tools`, keep the history append-only, or strip the thinking blocks from the edited turn on.

Keep the conversation append-only so the check never fails: change instructions or tools with [mid-conversation system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md) rather than edits. See [Preserved thinking](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md) and the migration guide's [note on this change](models-sonnet-5-5-migration-guide.md#thinking-blocks).

### The `computer_20251124` computer use tool is not supported on the Claude API and Google Cloud

On the Claude API and Google Cloud, Claude Sonnet 5.5 supports [computer use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) only through the `computer_toolset_20260801` toolset. A request that declares the earlier `computer_20251124` tool returns a 400 `invalid_request_error`. On the Claude API, the message names the rejected type, then lists the tool types the model does accept. It begins:

```python
'claude-sonnet-5-5' does not support tool types: computer_20251124.
```



On Amazon Bedrock, Claude Sonnet 5.5 accepts the earlier `computer_20251124` tool.

To move an existing integration on the Claude API or Google Cloud, follow [Migrate from `computer_20251124`](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#migrate-from-computer-20251124), which shows the request before and after. Drop the beta header, replace the `tools` entry with `{"type": "computer_toolset_20260801"}`, and update your agent loop for member `tool_use` blocks, batch actions, and `toolset_name` on results. The toolset is available on the Claude API and Google Cloud. For other platforms, see the computer use tool's [Compatibility](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#compatibility) section. Integrations that already use the toolset, and the [browser use tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md), need no change.

### Some advisor tool pairings are not supported

With the [advisor tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-advisor-tool.md) (beta), a Claude Sonnet 5.5 executor needs Claude Mythos 5.1, Claude Fable 5.1, Claude Mythos 5, Claude Fable 5, Claude Opus 5.5, or Claude Opus 5 as its advisor, or Claude Sonnet 5.5 itself. Claude Opus 4.8, Claude Opus 4.7, and Claude Sonnet 5 advisors work with a Claude Sonnet 5 executor, but with a Claude Sonnet 5.5 executor they return a 400 `invalid_request_error`. Every advisor that Claude Sonnet 5.5 accepts returns its advice encrypted, as an `advisor_redacted_result` block, so your client can't read the advice text. See the advisor tool's [Model compatibility](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-advisor-tool.md#model-compatibility) and [Result variants](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-advisor-tool.md#result-variants).

## Feature support

Claude Sonnet 5.5 supports [per-message effort](../04-API-Reference/Guides/build-with-claude-effort.md#change-effort-mid-conversation-beta) (beta), [mid-conversation system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md), [mid-conversation tool changes](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#mid-conversation-tool-changes) (beta), [prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) with a 512-token minimum cacheable prompt, [batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md), the [Files API](../04-API-Reference/Guides/build-with-claude-files.md), [PDF support](../04-API-Reference/Guides/build-with-claude-pdf-support.md), [vision](../04-API-Reference/Guides/build-with-claude-vision.md), and server-side and client-side [tools](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md). Per-message effort, mid-conversation system messages, and mid-conversation tool changes aren't available on Claude Sonnet 5, whose minimum cacheable prompt is 1,024 tokens. On the Claude API and Google Cloud, computer use requires the `computer_toolset_20260801` toolset (see the [breaking change](#computer-20251124-is-not-supported)). See each feature's page for model availability.

### Compact on demand (beta)

With the `compact-2026-09-04` beta header, a request that sends the top-level `compaction` parameter returns a signed `compaction` block that summarizes the whole conversation. You then send that block first, in place of the summarized messages. You choose when to compact, and the thinking blocks in the turns you keep can stay valid after the swap, under the conditions in [Compaction and preserved thinking](../04-API-Reference/Guides/build-with-claude-compaction-thinking-blocks.md#conditions-for-kept-thinking-to-stay-valid). That matters on Claude Sonnet 5.5 because its [thinking blocks are tied to the conversation](#thinking-blocks-are-tied-to-the-model-that-produced-them). See [Compaction on demand](../04-API-Reference/Guides/build-with-claude-compaction-on-demand.md) for platform availability and the full request flow.

### Define tools in a message (beta)

With the `inline-tools-2026-09-15` beta header, a `tool_addition` block in a mid-conversation system message can carry a full tool definition instead of a reference. You can add a tool, change its schema, or move a server tool to a newer version mid-conversation without editing `tools` and without losing the prompt cache. See [Define tools in a message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#define-tools-in-a-message-beta).

### Thinking blocks stay with the account that produced them

Thinking blocks that Claude Sonnet 5.5 produces work only in the account that produced them, or in an account linked to it. When another account sends one of these blocks, the API drops the block before the model sees it, and the request succeeds. On the Claude API and Google Cloud, with the `thinking-binding-controls-2026-08-01` beta header, the response lists each dropped block in `input_transformations` with `reason: "organization_binding_mismatch"`. Blocks from earlier models aren't affected. See [Preserved thinking](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md#account-bound-thinking).

## Behavior differences

Claude Sonnet 5.5 differs from Claude Sonnet 5 in several ways that show up without any code change. [Prompting Claude Sonnet 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-sonnet-5-5.md) has guidance for each:

- **Effort levels are recalibrated.** An [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level doesn't produce the same amount of thinking as it did on Claude Sonnet 5. Re-run your effort sweep rather than carrying a setting over. Start at `high` unless your workload is agentic or latency-sensitive. For agentic coding and multistep tool use, start at `medium` for well-specified tasks and move to `high` for harder or longer ones. For chat and other latency-sensitive work, start at `medium` or `low`.
- **Text between tool calls comes back in thinking blocks.** Between tool calls, notes longer than a sentence or two come back as [progress-update `thinking` blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#progress-updates). Shorter remarks stay `text`. At the default `display: "omitted"`, the progress-update blocks' text is empty, so an application that streams those notes to its users goes quiet between tool calls, with no error. If you [turn off up-front thinking with `between_tools`](#turn-off-up-front-thinking), the text comes back. The [migration guide](models-sonnet-5-5-migration-guide.md#text-between-tool-calls) shows how to receive it.
- **Safeguard categories.** The model's safeguards can decline a request in five [`stop_details` categories](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response). `"cyber"` means the request could enable cyber harm. `"bio"` means it could enable biological harm. `"frontier_llm"` means it could assist the development of competing AI models. `"reasoning_extraction"` means it asks the model to reproduce its internal reasoning in the response text. `"general_harms"` means it falls under another usage-policy area. See [Refusals, fallback, and billing](#refusals-fallback-and-billing).

## Refusals, fallback, and billing

Everything in [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md) applies to Claude Sonnet 5.5. A declined request returns HTTP 200 with `stop_reason: "refusal"` and a [`stop_details`](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response) object naming the policy area. Handle refusals and configure fallback. [Server-side fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#server-side-fallback) (`fallbacks: "default"`, in beta, on the Claude API) retries `"cyber"` and `"frontier_llm"` declines on Claude Sonnet 5. It doesn't retry `"bio"`, `"reasoning_extraction"`, or `"general_harms"` declines. You can also use the [SDK middleware](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#client-side-fallback) or your own retry. Whether a refusal that arrives before any output is billed depends on its refusal category, and it counts against your rate limits either way. See [How refusals are billed](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#how-refusals-are-billed).

## Pricing

Claude Sonnet 5.5 has the same prices as Claude Sonnet 5, including prompt caching and batch processing rates. See [Pricing](../17-Billing-Plans/about-claude-pricing.md) for the full list, data residency, and tool pricing.

## Availability

Claude Sonnet 5.5 is available on:

- **Claude API:** all customers, as `claude-sonnet-5-5`.
- **AWS:** [Claude in Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), as `anthropic.claude-sonnet-5-5`, and [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md), as `claude-sonnet-5-5`.
- **Google Cloud:** [Claude on Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md), as `claude-sonnet-5-5`.
- **Microsoft Foundry:** [Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md), as `claude-sonnet-5-5`.

## Migrate from Claude Sonnet 5

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
model = "claude-sonnet-5"  # Before
model = "claude-sonnet-5-5"  # After
```

Then check six things:

1.  If your code turns thinking off with `disabled`, send `between_tools` instead, at `high` effort or below.
2.  Replace `tool_choice` types `any` and `tool` with `auto` plus [strict tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md).
3.  Keep conversations append-only. A request that replays a Claude Sonnet 5.5 thinking block after an edit to earlier history can return a 400 error. See [Thinking blocks are tied to the model and the conversation](#thinking-blocks-are-tied-to-the-model-that-produced-them).
4.  If you use computer use through `computer_20251124` on the Claude API or Google Cloud, [move to the toolset](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#migrate-from-computer-20251124).
5.  If you use the advisor tool with a Claude Opus 4.8, Claude Opus 4.7, or Claude Sonnet 5 advisor, [switch to an advisor that Claude Sonnet 5.5 accepts](#advisor-tool-pairings).
6.  If your interface shows the text between tool calls, set `thinking.display` when you use adaptive thinking. With `between_tools`, the text comes back without it. See [Text between tool calls is returned in thinking blocks](models-sonnet-5-5-migration-guide.md#text-between-tool-calls).

The [migration guide](models-sonnet-5-5-migration-guide.md) has step-by-step instructions from Claude Sonnet 5 and earlier models, and the full checklist.

## Next steps



[Models overview](about-claude-models-overview.md)

Complete specs and pricing for all current Claude models.



[Migration guide](models-sonnet-5-5-migration-guide.md)

Move code from Claude Sonnet 5 and earlier models to Claude Sonnet 5.5.



[Prompting Claude Sonnet 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-sonnet-5-5.md)

Behavioral differences and prompting patterns specific to Claude Sonnet 5.5.



[Effort](../04-API-Reference/Guides/build-with-claude-effort.md)

Control how many tokens Claude uses when responding, from low to max.



[Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)

How adaptive thinking works and how thinking blocks are preserved.



[Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md)

Handle `stop_reason: "refusal"` and retry on another model.
