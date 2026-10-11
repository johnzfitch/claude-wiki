---
title: "What's new in Claude Haiku 5.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5"
category: "20-Models"
fetched_at: "2026-10-08T06:24:51Z"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fhaiku-5-5%2Fwhats-new-haiku-5-5)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

[Claude Haiku 5.5](models-haiku-5-5-overview.md)

[Overview](models-haiku-5-5-overview.md)[What's new](models-haiku-5-5-whats-new-haiku-5-5.md)[Migration guide](models-haiku-5-5-migration-guide.md)

Specialized models

Legacy models

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)[API credits for subscribers](../04-API-Reference/About/about-claude-api-credits-for-subscribers.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)

[Models & pricing](about-claude-models-overview.md)Claude Haiku 5.5

# What's new in Claude Haiku 5.5

Copy page



Overview of new capabilities, breaking changes, and behavior changes in Claude Haiku 5.5, with a link to each feature's guide and to the migration guide for code changes.

Copy page



Claude Haiku 5.5 is built for high-volume, latency-sensitive work such as classification, routing, extraction, and subagent tasks. It supports adaptive thinking with the effort parameter, a 1M token context window, and up to 128k output tokens. It uses the same newer tokenizer as Claude 4.7 and later models, so the same text counts as approximately 30% more tokens than on Claude Haiku 4.5. Its thinking blocks work only in the account that produced them, or in an account linked to it.

For code changes, see the [migration guide](models-haiku-5-5-migration-guide.md). For model IDs, pricing, and limits, see the [Claude Haiku 5.5 overview](models-haiku-5-5-overview.md). For prompting guidance, see [Prompting Claude Haiku 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-haiku-5-5.md).

## Summary of changes from Claude Haiku 4.5

Each row names one change, whether it is new, changed, or breaking, and what your code has to do.

| Change                                                                                                                              | Type     | Action needed                                                                                                     |
|:------------------------------------------------------------------------------------------------------------------------------------|:---------|:------------------------------------------------------------------------------------------------------------------|
| [Adaptive thinking and effort](#adaptive-thinking-and-effort)                                                                       | New      | Optional: set `effort` to trade response quality against speed and cost.                                          |
| [Larger context window and output](#larger-context-window-and-output)                                                               | New      | None. Existing `max_tokens` values stay valid, but thinking tokens count toward them.                             |
| [Browser use tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)                                                             | New      | None. Available on the Claude API and Google Cloud.                                                               |
| [Safety classifiers can decline a request](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response)                       | New      | Handle `stop_reason: "refusal"` in your client. Server-side fallback isn't available.                             |
| [Manual extended thinking returns an error](models-haiku-5-5-migration-guide.md#configure-thinking)                           | Breaking | Replace `budget_tokens` with adaptive thinking.                                                                   |
| [Non-default sampling parameters return an error](models-haiku-5-5-migration-guide.md#remove-sampling-parameters)             | Breaking | Omit `temperature`, `top_p`, and `top_k`.                                                                         |
| [Assistant message prefill returns an error](models-haiku-5-5-migration-guide.md#replace-assistant-prefill)                   | Breaking | End `messages` with a user turn.                                                                                  |
| [Computer use needs the toolset on the Claude API and Google Cloud](models-haiku-5-5-migration-guide.md#computer-use-toolset) | Breaking | Replace `computer_20250124` with `computer_toolset_20260801`.                                                     |
| [Changing earlier turns invalidates thinking blocks](models-haiku-5-5-migration-guide.md#keep-earlier-turns-unchanged)        | Breaking | Keep conversations append-only if you send thinking blocks back.                                                  |
| [Responses can begin with thinking blocks](#responses-can-begin-with-thinking-blocks)                                               | Changed  | Select content blocks by `type`, not by position.                                                                 |
| [Thinking text is omitted by default](models-haiku-5-5-migration-guide.md#configure-thinking)                                 | Changed  | To receive summarized thinking, set `thinking.display` to `"summarized"`.                                         |
| [Same text counts as more tokens](#same-text-counts-as-more-tokens)                                                                 | Changed  | Recount prompts and revisit `max_tokens` and cost estimates.                                                      |
| [Replaying thinking blocks across accounts](#replaying-thinking-blocks-across-accounts)                                             | Changed  | If you replay stored conversations through a different account, replay each through the account that produced it. |

## New capabilities

### Adaptive thinking and effort

With [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md), Claude Haiku 5.5 determines when and how much to think. Adaptive thinking is on by default. While you can still turn thinking off with `thinking: {"type": "disabled"}` at `high` effort or below, the better way to trade response quality against speed and cost is to use the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md).

### Larger context window and output

Claude Haiku 5.5 has a 1M token [context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) and returns up to 128k output tokens, up from 200k and 64k on Claude Haiku 4.5. Existing `max_tokens` values stay valid, but thinking tokens count toward `max_tokens`, so a small limit can stop after a `thinking` block and before any text. See [Configure thinking](models-haiku-5-5-migration-guide.md#configure-thinking).

## Behavior changes

### Responses can begin with thinking blocks

Adaptive thinking is on by default, so a response can begin with one or more `thinking` blocks even when the request doesn't mention thinking. Code that reads the first content block as the answer needs to select blocks by their `type` field. See [Configure thinking](models-haiku-5-5-migration-guide.md#configure-thinking) in the migration guide.

### Same text counts as more tokens

Claude Haiku 5.5 uses the same newer tokenizer as Claude 4.7 and later models. As with all models that use this tokenizer, the same input text produces approximately 30% more tokens on Claude Haiku 5.5 than on Claude Haiku 4.5. The exact increase depends on the content. The shape of requests and responses doesn't depend on the tokenizer, but anything you measure or budget in tokens changes. See [Recount tokens](models-haiku-5-5-migration-guide.md#recount-tokens) in the migration guide.

### Replaying thinking blocks across accounts

Thinking blocks from Claude Haiku 5.5 work only in the account that produced them, or in an account linked to it. This matters only if you store conversations and replay them through a different account. See [Replay thinking blocks through the account that produced them](models-haiku-5-5-migration-guide.md#replay-thinking-blocks-through-the-producing-account).
