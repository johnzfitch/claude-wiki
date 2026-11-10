---
title: "Models overview - Claude Platform Docs"
source_url: "https://support.claude.com/en/articles/8606395-how-large-is-the-claude-api-s-context-window"
category: "04-API-Reference/Other"
fetched_at: "2026-11-09T06:26:41Z"
tags: ["api", "prompting"]
---

# Models overview

Copy page



Claude is a family of state-of-the-art large language models developed by Anthropic. Compare the current lineup, find the model ID for every platform, and open each model’s page for its full specs and resources.

[Choosing a model](https://support.claude.com/docs/en/about-claude/models/choosing-a-model)[Pricing](https://support.claude.com/docs/en/about-claude/pricing)[Migration guide](https://support.claude.com/docs/en/about-claude/models/migration-guide)

Copy page



## Compare models

If you’re unsure which model to use, start with [Claude Opus 5.5](https://support.claude.com/docs/en/models/opus-5-5/overview) for most workloads. Use [Claude Fable 5.1](https://support.claude.com/docs/en/models/fable-5-1/overview) for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short. All current models support text and image input, text output, multilingual capabilities, vision, and tool use. Each model’s page lists the platforms it’s available on.

[TABLE]

Once you’ve picked a model, [learn how to make your first API call](https://support.claude.com/docs/en/get-started). To understand how model IDs, aliases, and snapshots work, see [Model IDs and versioning](https://support.claude.com/docs/en/about-claude/models/model-ids-and-versions); for the reliable-knowledge and training-data cutoffs behind each model, see Anthropic’s [Transparency Hub](https://www.anthropic.com/transparency).

## Using the Models API

You can query model capabilities and token limits programmatically with the [Models API](https://support.claude.com/docs/en/api/models/list)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.. The response includes [`max_input_tokens`](https://support.claude.com/docs/en/api/models#model_info.max_input_tokens)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., [`max_tokens`](https://support.claude.com/docs/en/api/models#model_info.max_tokens)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., and a [`capabilities`](https://support.claude.com/docs/en/api/models#model_info.capabilities)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. object for every available model.

Each model in the response also has a [`line`](https://support.claude.com/docs/en/api/models#model_info.line)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. field, which names the model line it belongs to. Claude Opus 4.5 and Claude Opus 4.6 both report `opus`. Use `line` to group models, for example, in a model picker. `line` is `null` when a model belongs to no line. Read `line` instead of inferring it from the model’s `id`. Anthropic might add more lines, so don’t treat the set of values as fixed.

Each model’s `capabilities` object includes [`thinking.types.disabled`](https://support.claude.com/docs/en/api/models#thinking_types.disabled)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., which reports whether the model accepts `thinking: {type: "disabled"}`, the setting that [turns thinking off](https://support.claude.com/docs/en/build-with-claude/thinking#turning-thinking-off). `supported` is `false` when the model rejects `"disabled"` with a 400 error, and `true` on a model that doesn’t support thinking. Even when `supported` is `true`, the API can still reject a `"disabled"` request for another reason. One such reason is an [effort](https://support.claude.com/docs/en/build-with-claude/effort) level that the model doesn’t allow with thinking off.

Each model’s `capabilities` object also includes [`thinking.types.between_tools`](https://support.claude.com/docs/en/api/models#thinking_types.between_tools)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., which reports whether the model accepts `thinking: {type: "between_tools"}`, the setting that [turns off up-front thinking](https://support.claude.com/docs/en/build-with-claude/thinking#turning-thinking-off). `supported` is `false` when the model rejects `"between_tools"` with a 400 error. Even when `supported` is `true`, the API can still reject a `"between_tools"` request for another reason, such as an [effort](https://support.claude.com/docs/en/build-with-claude/effort) level that the model doesn’t allow with `"between_tools"`. For Claude Sonnet 5.5, for example, the Models API reports `thinking.types.between_tools.supported` as `true` and `thinking.types.disabled.supported` as `false`.

Each model’s `capabilities` object also includes [`server_tools`](https://support.claude.com/docs/en/api/models#model_capabilities.server_tools)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., which reports whether the model accepts the [web search](https://support.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) and [code execution](https://support.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) tools. It doesn’t cover other server tools, such as web fetch. `server_tools.web_search.supported` and `server_tools.code_execution.supported` are `true` when the model accepts at least one version of that tool, not necessarily every version. `server_tools.supported` is `true` when the model accepts at least one of the two tools. Even when a tool is supported, your organization’s settings can still cause a request that uses it to fail. For example, an administrator can [disable web search](https://support.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#how-to-use-web-search).

The top-level [`code_execution`](https://support.claude.com/docs/en/api/models#model_capabilities.code_execution)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. capability is a different check. It reports whether code that Claude runs in the code execution tool can call the request’s other tools, as in [programmatic tool calling](https://support.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling). For Claude Haiku 4.5, for example, the Models API reports `server_tools.code_execution.supported` as `true` and `code_execution.supported` as `false`.

The API reference lists the List Models endpoint’s parameters and full response.

#### [List Models](https://support.claude.com/docs/en/api/models/list)

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

Read more about versioning and our version history [here](../Endpoints/versioning.md).



"anthropic-workspace-id": optional string

Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns `data` `first_id` `has_more` `last_id`



data: array of [ModelInfo](https://support.claude.com/docs/en/api/http/models#model_info) { type: "model", id, capabilities, 8 more }



type: "model"

Object type.

For Models, this is always `"model"`.

defaultmodel

id: string

Unique model identifier.



capabilities: [ModelCapabilities](https://support.claude.com/docs/en/api/http/models#model_capabilities) { batch, citations, code_execution, 7 more } or null

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

line: [ModelLine](https://support.claude.com/docs/en/api/http/models#model_line) or null

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

- **Performance:** Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See [Prompting best practices](https://support.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) for general and model-specific prompting guidance.
- **Engaging responses:** Claude models are ideal for applications that require rich, human-like interactions. If you prefer more concise responses, adjust your prompts to guide the model toward the output length you want. Refer to the [prompt engineering guides](https://support.claude.com/docs/en/build-with-claude/prompt-engineering) for details.
- **Output quality:** When migrating from a previous model generation, you might notice larger improvements in overall performance. If you’re on Claude Opus 5 or earlier, see the [Claude Opus 5.5 migration guide](https://support.claude.com/docs/en/models/opus-5-5/migration-guide).

## Get started with Claude

Whether you’re a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, the following resources can help.



[Intro to Claude](https://support.claude.com/docs/en/intro)

Explore Claude’s capabilities and development flow.



[Quickstart](https://support.claude.com/docs/en/get-started)

Learn how to make your first API call in minutes.

[Choosing a model](https://support.claude.com/docs/en/about-claude/models/choosing-a-model)

Establish criteria and pick the right model for your use case.

[Pricing](https://support.claude.com/docs/en/about-claude/pricing)

Complete pricing, including batch discounts and prompt caching rates.



[Model deprecations](https://support.claude.com/docs/en/about-claude/model-deprecations)

Lifecycle status and retirement commitments for every model.



[Claude Console](https://support.claude.com/)

Craft and test prompts directly in your browser.

Looking to chat with Claude? Visit [claude.ai](https://claude.ai). If you have questions, contact the [support team](https://support.claude.com/) or the [Discord community](https://www.anthropic.com/discord).
