---
title: "Migrating to Claude Opus 5.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5-5/migration-guide"
category: "20-Models"
fetched_at: "2026-09-23T06:27:10Z"
tags: ["models"]
---

- [Managed Agents](../04-API-Reference/Other/managed-agents-overview.md)

- [Admin](../04-API-Reference/Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../04-API-Reference/About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../04-API-Reference/Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](release-notes-overview.md)

[API reference](../04-API-Reference/Endpoints/overview.md)




[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fopus-5-5%2Fmigration-guide)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Overview](models-opus-5-5-overview.md)[What's new](models-opus-5-5-whats-new-opus-5-5.md)[Migration guide](models-opus-5-5-migration-guide.md)

[Claude Opus 5](models-opus-5-overview.md)

[Claude Sonnet 5](models-sonnet-5-overview.md)

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

# Migrating to Claude Opus 5.5

Copy page



Migrate to Claude Opus 5.5 from earlier Claude models: model IDs, breaking changes, recommended changes, and migration checklists.

Copy page





This guide covers migrating [Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md) code. If you use [Claude Managed Agents](../04-API-Reference/Other/managed-agents-overview.md), no changes beyond updating the model name are required.



**Automate your migration with the Claude API skill.** In Claude Code, run `/claude-api migrate` to invoke the bundled [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md#migrating-to-a-newer-claude-model). It works for any current Claude model as the target:

```python
/claude-api migrate this project to claude-opus-5-5
```



The skill applies the model ID swap and, as needed, breaking parameter changes, prefill replacement, and effort calibration for your target model across your code base, then produces a checklist of items to verify manually. It asks you to confirm the migration scope (entire working directory, a subdirectory, or a specific file list) before editing any files. The skill also detects Amazon Bedrock and Claude Platform on AWS clients and adjusts model ID formats and feature changes for those platforms.

For behavioral differences and model-specific prompting patterns, see [Prompting Claude Opus 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md).

Claude Opus 5.5 costs less than Claude Opus 5 (\$4 / \$20 USD per million input / output tokens, compared with \$5 / \$25; see [Claude pricing](../17-Billing-Plans/about-claude-pricing.md)), and keeps Claude Opus 5's [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) and 128k max output tokens. There are four breaking changes for code already running on Claude Opus 5, covered under [Breaking changes](#breaking-changes). For feature support, see [What's new in Claude Opus 5.5](models-opus-5-5-whats-new-opus-5-5.md#feature-support).

## Migrating to Claude Opus 5.5 from Claude Opus 5

### Update your model name

```python
model = "claude-opus-5"  # Before
model = "claude-opus-5-5"  # After
```



`claude-opus-5-5` is a fixed model ID with no date suffix, the same scheme as `claude-opus-5`. On Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry, use that platform's model ID; see [Availability](models-opus-5-5-whats-new-opus-5-5.md#availability).

### Breaking changes

Each change is explained in [What's new in Claude Opus 5.5](models-opus-5-5-whats-new-opus-5-5.md#breaking-changes); this section gives the code change for each.

#### Thinking can't be disabled

`thinking: {"type": "disabled"}` and `thinking: {"type": "enabled", "budget_tokens": N}` both return a 400 error (`"thinking.type.disabled" is not supported for this model.` or `"thinking.type.enabled" is not supported for this model.`). Remove the `thinking` field and pick an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level; where you disabled thinking to save tokens, use a lower one. Responses then begin with `thinking` blocks, so select content blocks by `type` and pass `thinking` blocks back unmodified with tool results. See [Thinking can't be disabled](models-opus-5-5-whats-new-opus-5-5.md#thinking-cant-be-disabled).

Before (accepted on Claude Opus 5, rejected on Claude Opus 5.5):

```python
client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    thinking={"type": "disabled"},
    messages=[{"role": "user", "content": "..."}],
)
```



After:

```python
client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    output_config={"effort": "low"},  # thinking is always on; effort is the control
    messages=[{"role": "user", "content": "..."}],
)
```



#### Forced tool use is not supported

`tool_choice` types `any` and `tool` return a 400 error (`tool_choice: type "tool" and "any" are not supported for this model.`), including on the token counting endpoint. Use `auto` with [strict tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md) or [structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md), and say in the prompt when the tool applies. See [Forced tool use is not supported](models-opus-5-5-whats-new-opus-5-5.md#forced-tool-use-is-not-supported).

Before:

```python
client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "tool", "name": "get_weather"},
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
)
```



After:

```python
client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    # strict tool use: every call matches the tool's input_schema
    tools=[{**tool, "strict": True} for tool in tools],
    tool_choice={"type": "auto"},
    messages=[
        {
            "role": "user",
            "content": "What's the weather in Paris? Use the get_weather tool.",
        }
    ],
)
```



#### Thinking blocks are tied to the model and the conversation

On the Claude API, Claude Fable 5.1 and Claude Mythos 5.1 read Claude Opus 5.5 thinking blocks; no other model does. A router or fallback that moves a conversation from Claude Opus 5.5 to any other model runs those turns without them. In the other direction, Claude Opus 5.5 reads thinking blocks from Claude Opus 5 and earlier Opus, Sonnet, and Haiku models, but not from Claude Fable or Claude Mythos models. Keep the conversation append-only (no edits to the `system` prompt, `tools`, or earlier messages mid-conversation) so the blocks stay valid; Claude Code, claude.ai, Claude Managed Agents, and the Claude Agent SDK already do. Enforcement matches Claude Fable 5.1 on every platform: for accounts created on or after August 31, 2026, 00:00 UTC, replaying a thinking block after such an edit returns a 400 error by default. There is no code change for append-only integrations. See [Thinking blocks are tied to the model and the conversation](models-opus-5-5-whats-new-opus-5-5.md#thinking-blocks-are-tied-to-the-model-that-produced-them) and [Preserved thinking](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md).

#### The `computer_20251124` computer use tool is not supported on the Claude API and Google Cloud

On the Claude API and Google Cloud, a `tools` entry of type `computer_20251124` returns a 400 error (`'claude-opus-5-5' does not support tool types: computer_20251124.`, followed by the tool types the model accepts). Declare the `computer_toolset_20260801` toolset instead: drop the beta header and send the entry with no `name` or display dimensions. In your agent loop, handle member `tool_use` blocks (the action is the block's `name`, not `input.action`), several of them per turn, and echo `toolset_name` on every result. The request change is shown below; the agent-loop changes are listed in [Migrate from `computer_20251124`](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#migrate-from-computer-20251124). On Amazon Bedrock, the earlier `computer_20251124` tool continues to work on Claude Opus 5.5 as it does on Claude Opus 5, so no change is needed there; for other platforms, see the computer use tool's [Compatibility](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#compatibility) section. See [The `computer_20251124` computer use tool is not supported on the Claude API and Google Cloud](models-opus-5-5-whats-new-opus-5-5.md#computer-20251124-is-not-supported).

Before:

```python
client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["computer-use-2025-11-24"],
    tools=[
        {
            "type": "computer_20251124",
            "name": "computer",
            "display_width_px": 1024,
            "display_height_px": 768,
        }
    ],
    messages=[{"role": "user", "content": "Open the display settings."}],
)
```



After:

```python
client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    # no beta header; the toolset entry takes no name or display size
    tools=[{"type": "computer_toolset_20260801"}],
    messages=[{"role": "user", "content": "Open the display settings."}],
)
```



### Text between tool calls is returned in thinking blocks

On Claude Opus 5, text the model writes between tool calls comes back as `text` blocks. On Claude Opus 5.5, as on Claude Fable 5.1, that narration comes back as [progress-update `thinking` blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#progress-updates), at most one before each tool call. At the default `thinking.display` of `"omitted"`, their `thinking` field is empty. No request fails, but an application that streams that text to its users as progress updates goes quiet between tool calls. To restore the updates, read them from `thinking` blocks and set a `display` value that returns their text: `"updates"` (beta, `thinking-display-updates-2026-08-18` header) returns the progress updates while reasoning stays hidden, and `"summarized"` returns both, mixed together. Then render each non-empty `thinking` block ahead of the `tool_use` block it precedes, and pass the blocks back unchanged with the rest of the assistant turn. See [User-facing progress updates](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#user-facing-progress-updates).

### Safety classifiers and fallback

Claude Opus 5.5 can return `stop_reason: "refusal"` with a `stop_details` category. Its classifiers cover a broader set of categories than Claude Opus 5's, so expect `stop_details.category` values such as `"bio"` and `"reasoning_extraction"` in addition to `"cyber"`; see the [refusal category table](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response). Handle refusals and configure [server-side fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#server-side-fallback) or your own retry (server-side fallback doesn't retry requests declined with `"reasoning_extraction"`; that refusal is returned to you); see [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md) and [Safeguard refusals](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#safeguard-refusals).

### Recommended changes

1.  **Re-run your effort sweep.** Effort is the only thinking control on Claude Opus 5.5, and its default is `medium` where Claude Opus 5's is `high`, so a request that omits `effort` now runs at `medium`. Step down where quality holds, and step up for the most demanding work. See [Effort](../04-API-Reference/Guides/build-with-claude-effort.md).
2.  **Re-evaluate model-specific prompt instructions.** Instructions tuned for Claude Opus 5's behavior may no longer be needed; see [Prompting Claude Opus 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md). If you ran with thinking disabled, also see [Prompts written for thinking disabled](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md#prompts-written-for-thinking-disabled).
3.  **Test in a development environment** before switching production traffic.

### Migration checklist

- Update the model ID to `claude-opus-5-5`.
- Remove `thinking: {"type": "disabled"}` and `thinking: {"type": "enabled", ...}`; choose an effort level instead.
- Set `effort` explicitly: the default is `medium`, where Claude Opus 5's is `high`.
- Replace `tool_choice` types `any` and `tool` with `auto` plus strict tool use or structured outputs.
- If you use computer use on the Claude API or Google Cloud, declare `computer_toolset_20260801` (no beta header) instead of `computer_20251124` and update your agent loop for the toolset. On Amazon Bedrock, keep `computer_20251124`; check the computer use tool's [Compatibility](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#compatibility) section for other platforms.
- If a router or fallback can move a conversation from Claude Opus 5.5 to another model, expect that model to run without Claude Opus 5.5's thinking blocks (Claude Fable 5.1 and Claude Mythos 5.1 on the Claude API are the exception and keep them). Claude Opus 5.5 itself reads thinking from Claude Opus 5 and earlier Opus, Sonnet, and Haiku models, but not from Claude Fable or Claude Mythos models.
- Read content blocks by `type`, and pass `thinking` blocks back unmodified in tool-use loops.
- If your interface renders text between tool calls, set `display: "updates"` (beta) or `"summarized"` and render the non-empty `thinking` blocks.
- If your code edits earlier turns, the `system` prompt, or `tools` mid-conversation, follow [Preserved thinking](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md).
- Handle `stop_reason: "refusal"` and configure fallback.
- Re-baseline cost and latency at your chosen effort level.

## Migrating to Claude Opus 5.5 from Claude Opus 4.8

Work through [Migrating to Claude Opus 5 from Claude Opus 4.8](models-opus-5-migration-guide.md#migrating-from-claude-opus-4-8-to-claude-opus-5) first: it covers thinking on by default and the response-shape changes that come with it. Then apply [Migrating from Claude Opus 5](#migrating-from-claude-opus-5). The second Claude Opus 5 breaking change there (thinking can be disabled only at `high` effort or below) doesn't carry over: on Claude Opus 5.5 thinking can't be disabled at all.

### Migration checklist

- Everything in the [Claude Opus 4.8 → Claude Opus 5 checklist](models-opus-5-migration-guide.md#migrating-from-claude-opus-4-8-to-claude-opus-5), except that `thinking: {"type": "disabled"}` is not an option.
- Everything in the [Claude Opus 5 → Claude Opus 5.5 checklist](#migration-checklist-from-claude-opus-5).

## Migrating to Claude Opus 5.5 from Claude Opus 4.7 and earlier Opus models

The [Claude Opus 5 migration guide](models-opus-5-migration-guide.md#migrating-from-claude-opus-47) covers the breaking changes between your current model and Claude Opus 5: sampling parameters rejected, manual extended thinking rejected, prefill removed, and the newer tokenizer. Work through the section for your model there, targeting `claude-opus-5-5` instead of `claude-opus-5`, then apply [Migrating from Claude Opus 5](#migrating-from-claude-opus-5). Where that guide tells you thinking can be disabled at `high` effort or below, it can't on Claude Opus 5.5; and where it says existing `computer_20251124` integrations keep working, on the Claude API and Google Cloud they don't on Claude Opus 5.5, which there accepts computer use only as the `computer_toolset_20260801` toolset (see [the breaking change](#computer-use-toolset)); on Amazon Bedrock they keep working.

## Migrating to Claude Opus 5.5 from Claude Sonnet 5

See [Migrating to Claude Opus 5 from Claude Sonnet 5](models-opus-5-migration-guide.md#migrating-to-claude-opus-5-from-claude-sonnet-5) for what changes when moving up a model class, then apply [Migrating from Claude Opus 5](#migrating-from-claude-opus-5).
