---
title: "Models overview - Claude Platform Docs"
source_url: "https://platform.claude.com/en/docs/about-claude/models/overview"
category: "20-Models"
fetched_at: "2026-11-13T06:35:19Z"
tags: ["api", "models", "prompting"]
---

# Models overview

Copy page



Claude is a family of state-of-the-art large language models developed by Anthropic. Compare the current lineup, find the model ID for every platform, and open each model’s page for its full specs and resources.

[Choosing a model](about-claude-models-choosing-a-model.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)[Migration guide](about-claude-models-migration-guide.md)

Copy page



## Latest models

If you’re unsure which model to use, start with [Claude Opus 5.5](models-opus-5-5-overview.md) for most workloads. Use [Claude Fable 5.2](models-fable-5-2-overview.md) for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short. All current models support text and image input, text output, multilingual capabilities, vision, and tool use.

[TABLE]

Once you’ve picked a model, [learn how to make your first API call](../01-Getting-Started/get-started.md). To understand how model IDs, aliases, and snapshots work, see [Model IDs and versioning](about-claude-models-model-ids-and-versions.md). For the reliable-knowledge and training-data cutoffs behind each model, see Anthropic’s [Transparency Hub](https://www.anthropic.com/transparency).

## All models

Older models might still be available, but where possible, you should default to the [latest models](#latest-models-comparison). To move to a newer model, see the [migration guides](about-claude-models-migration-guide.md). For retirement dates, see [model deprecations](about-claude-model-deprecations.md).

[TABLE]

## Using the Models API

You can query model capabilities and token limits programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.. The response includes [`max_input_tokens`](../04-API-Reference/Endpoints/models.md#model_info.max_input_tokens)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., [`max_tokens`](../04-API-Reference/Endpoints/models.md#model_info.max_tokens)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., and a [`capabilities`](../04-API-Reference/Endpoints/models.md#model_info.capabilities)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. object for every available model.

Each model in the response also has a [`line`](../04-API-Reference/Endpoints/models.md#model_info.line)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. field, which names the model line it belongs to. Claude Opus 4.5 and Claude Opus 4.6 both report `opus`. Use `line` to group models, for example, in a model picker. `line` is `null` when a model belongs to no line. Read `line` instead of inferring it from the model’s `id`. Anthropic might add more lines, so don’t treat the set of values as fixed.

Each model’s `capabilities` object includes [`thinking.types.disabled`](../04-API-Reference/Endpoints/models.md#thinking_types.disabled)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., which reports whether the model accepts `thinking: {type: "disabled"}`, the setting that [turns thinking off](../04-API-Reference/Guides/build-with-claude-thinking.md#turning-thinking-off). `supported` is `false` when the model rejects `"disabled"` with a 400 error, and `true` on a model that doesn’t support thinking. Even when `supported` is `true`, the API can still reject a `"disabled"` request for another reason. One such reason is an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level that the model doesn’t allow with thinking off.

Each model’s `capabilities` object also includes [`thinking.types.between_tools`](../04-API-Reference/Endpoints/models.md#thinking_types.between_tools)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., which reports whether the model accepts `thinking: {type: "between_tools"}`, the setting that [turns off up-front thinking](../04-API-Reference/Guides/build-with-claude-thinking.md#turning-thinking-off). `supported` is `false` when the model rejects `"between_tools"` with a 400 error. Even when `supported` is `true`, the API can still reject a `"between_tools"` request for another reason, such as an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level that the model doesn’t allow with `"between_tools"`. For Claude Sonnet 5.5, for example, the Models API reports `thinking.types.between_tools.supported` as `true` and `thinking.types.disabled.supported` as `false`.

Each model’s `capabilities` object also includes [`server_tools`](../04-API-Reference/Endpoints/models.md#model_capabilities.server_tools)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., which reports whether the model accepts the [web search](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-search-tool.md) and [code execution](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) tools. It doesn’t cover other server tools, such as web fetch. `server_tools.web_search.supported` and `server_tools.code_execution.supported` are `true` when the model accepts at least one version of that tool, not necessarily every version. `server_tools.supported` is `true` when the model accepts at least one of the two tools. Even when a tool is supported, your organization’s settings can still cause a request that uses it to fail. For example, an administrator can [disable web search](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-search-tool.md#how-to-use-web-search).

The top-level [`code_execution`](../04-API-Reference/Endpoints/models.md#model_capabilities.code_execution)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. capability is a different check. It reports whether code that Claude runs in the code execution tool can call the request’s other tools, as in [programmatic tool calling](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md). For Claude Haiku 4.5, for example, the Models API reports `server_tools.code_execution.supported` as `true` and `code_execution.supported` as `false`.

The API reference lists the List Models endpoint’s parameters and full response.

#### [List Models](../04-API-Reference/Endpoints/models-list.md)

GET/v1/models

List available models.

##### Query parameters `after_id` `before_id` `lifecycle` `limit`

after_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.



lifecycle: optional array of "active" or "deprecated" or "retired"

Filter the list to models in any of the given lifecycle stages (`active`, `deprecated`, or `retired`). Up to 3 values. When omitted, the list contains the `active` and `deprecated` models; `retired` models appear only when `retired` is requested explicitly.

maxItems3

One of the following:

"active"

"deprecated"

"retired"



limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

minimum1

maximum1000

##### Headers `anthropic-version` `anthropic-workspace-id`



"anthropic-version": optional string

The version of the Claude API you want to use.

Read more about versioning and our version history [here](../04-API-Reference/Endpoints/versioning.md).



"anthropic-workspace-id": optional string

Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns `data` `first_id` `has_more` `last_id`



data: array of [ModelInfo](../04-API-Reference/Endpoints/models.md#model_info) { type: "model", id, capabilities, 8 more }



type: "model"

Object type.

For Models, this is always `"model"`.

defaultmodel

id: string

Unique model identifier.



capabilities: [ModelCapabilities](../04-API-Reference/Endpoints/models.md#model_capabilities) { batch, citations, code_execution, 7 more } or null

Object mapping capability names to their support details. Keys are always present for all known capabilities.



created_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time



deprecated_at: string or null

RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

formatdate-time

display_name: string

A human-readable name for the model.



lifecycle: "active" or "deprecated" or "retired"

The model's current lifecycle stage.

- `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
- `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
- `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

defaultactive

One of the following:

"active"

"deprecated"

"retired"



line: [ModelLine](../04-API-Reference/Endpoints/models.md#model_line) or null

The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

One of the following:

"haiku"

"sonnet"

"opus"

"fable"

"mythos"

max_input_tokens: number or null

Maximum input context window size in tokens for this model.

max_tokens: number or null

Maximum value for the `max_tokens` parameter when using this model.



retires_at: string or null

RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

formatdate-time

first_id: string or null

First ID in the `data` list. Can be used as the `before_id` for the previous page.

has_more: boolean

Indicates if there are more results in the requested page direction.

last_id: string or null

Last ID in the `data` list. Can be used as the `after_id` for the next page.

## Prompt and output performance

Current Claude models excel in:

- **Performance:** Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See [Prompting best practices](../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md) for general and model-specific prompting guidance.
- **Engaging responses:** Claude models are ideal for applications that require rich, human-like interactions. If you prefer more concise responses, adjust your prompts to guide the model toward the output length you want. Refer to the [prompt engineering guides](../10-Prompting-Guides/build-with-claude-prompt-engineering-overview.md) for details.
- **Output quality:** When migrating from a previous model generation, you might notice larger improvements in overall performance. If you’re on Claude Opus 5 or earlier, see the [Claude Opus 5.5 migration guide](models-opus-5-5-migration-guide.md).

## Get started with Claude

Whether you’re a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, the following resources can help.



[Intro to Claude](../01-Getting-Started/intro.md)

Explore Claude’s capabilities and development flow.



[Quickstart](../01-Getting-Started/get-started.md)

Learn how to make your first API call in minutes.

[Choosing a model](about-claude-models-choosing-a-model.md)

Establish criteria and pick the right model for your use case.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Complete pricing, including batch discounts and prompt caching rates.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every model.



[Claude Console](../04-API-Reference/Other/playground.md)

Craft and test prompts directly in your browser.

Looking to chat with Claude? Visit [claude.ai](https://claude.ai). If you have questions, contact the [support team](https://support.claude.com/) or the [Discord community](https://www.anthropic.com/discord).
