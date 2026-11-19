---
title: "Models overview - Claude Platform Docs"
source_url: "https://support.claude.com/en/articles/8606395-how-large-is-the-claude-api-s-context-window"
category: "04-API-Reference/Other"
fetched_at: "2026-11-18T06:28:40Z"
tags: ["api", "prompting"]
---

# Models overview

Copy page



Claude is a family of state-of-the-art large language models developed by Anthropic. Compare the current lineup, find the model ID for every platform, and open each model’s page for its full specs and resources.

[Choosing a model](https://support.claude.com/docs/en/about-claude/models/choosing-a-model)[Pricing](https://support.claude.com/docs/en/about-claude/pricing)[Migration guide](https://support.claude.com/docs/en/about-claude/models/migration-guide)

Copy page



## Latest models

If you’re unsure which model to use, start with [Claude Opus 5.5](https://support.claude.com/docs/en/models/opus-5-5/overview) for most workloads. Use [Claude Fable 5.2](https://support.claude.com/docs/en/models/fable-5-2/overview) for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short. All current models support text and image input, text output, multilingual capabilities, vision, and tool use.

[TABLE]

Once you’ve picked a model, [learn how to make your first API call](https://support.claude.com/docs/en/get-started). To understand how model IDs, aliases, and snapshots work, see [Model IDs and versioning](https://support.claude.com/docs/en/about-claude/models/model-ids-and-versions). For the reliable-knowledge and training-data cutoffs behind each model, see Anthropic’s [Transparency Hub](https://www.anthropic.com/transparency).

## All models

Older models might still be available, but where possible, you should default to the [latest models](#latest-models-comparison). To move to a newer model, see the [migration guides](https://support.claude.com/docs/en/about-claude/models/migration-guide). For retirement dates, see [model deprecations](https://support.claude.com/docs/en/about-claude/model-deprecations).

[TABLE]

## Using the Models API

You can query model capabilities and token limits programmatically with the [Models API](https://support.claude.com/docs/en/api/models/list)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.. The response includes [`max_input_tokens`](https://support.claude.com/docs/en/api/models#model_info.max_input_tokens)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., [`max_tokens`](https://support.claude.com/docs/en/api/models#model_info.max_tokens)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., and a [`capabilities`](https://support.claude.com/docs/en/api/models#model_info.capabilities)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. object for every available model.

Each model in the response also has a [`line`](https://support.claude.com/docs/en/api/models#model_info.line)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. field, which names the model line it belongs to. Claude Opus 4.5 and Claude Opus 4.6 both report `opus`. Use `line` to group models, for example, in a model picker. `line` is `null` when a model belongs to no line. Read `line` instead of inferring it from the model’s `id`. Anthropic might add more lines, so don’t treat the set of values as fixed.

Each model’s `capabilities` object includes [`thinking.types.disabled`](https://support.claude.com/docs/en/api/models#thinking_types.disabled)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., which reports whether the model accepts `thinking: {type: "disabled"}`, the setting that [turns thinking off](https://support.claude.com/docs/en/build-with-claude/thinking#turning-thinking-off). `supported` is `false` when the model rejects `"disabled"` with a 400 error, and `true` on a model that doesn’t support thinking. Even when `supported` is `true`, the API can still reject a `"disabled"` request for another reason. One such reason is an [effort](https://support.claude.com/docs/en/build-with-claude/effort) level that the model doesn’t allow with thinking off.

Each model’s `capabilities` object also includes [`thinking.types.between_tools`](https://support.claude.com/docs/en/api/models#thinking_types.between_tools)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., which reports whether the model accepts `thinking: {type: "between_tools"}`, the setting that [turns off up-front thinking](https://support.claude.com/docs/en/build-with-claude/thinking#turning-thinking-off). `supported` is `false` when the model rejects `"between_tools"` with a 400 error. Even when `supported` is `true`, the API can still reject a `"between_tools"` request for another reason, such as an [effort](https://support.claude.com/docs/en/build-with-claude/effort) level that the model doesn’t allow with `"between_tools"`. For Claude Sonnet 5.5, for example, the Models API reports `thinking.types.between_tools.supported` as `true` and `thinking.types.disabled.supported` as `false`.

Each model’s `capabilities` object also includes [`server_tools`](https://support.claude.com/docs/en/api/models#model_capabilities.server_tools)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., which reports whether the model accepts the [web search](https://support.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) and [code execution](https://support.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) tools. It doesn’t cover other server tools, such as web fetch. `server_tools.web_search.supported` and `server_tools.code_execution.supported` are `true` when the model accepts at least one version of that tool, not necessarily every version. `server_tools.supported` is `true` when the model accepts at least one of the two tools. Even when a tool is supported, your organization’s settings can still cause a request that uses it to fail. For example, an administrator can [disable web search](https://support.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#how-to-use-web-search).

The top-level [`code_execution`](https://support.claude.com/docs/en/api/models#model_capabilities.code_execution)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. capability is a different check. It reports whether code that Claude runs in the code execution tool can call the request’s other tools, as in [programmatic tool calling](https://support.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling). For Claude Haiku 4.5, for example, the Models API reports `server_tools.code_execution.supported` as `true` and `code_execution.supported` as `false`.

The API reference lists the List Models endpoint’s parameters and full response.

## Prompt and output performance

Current Claude models excel in:

- **Performance:** Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See [Prompting best practices](https://support.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) for general and model-specific prompting guidance.
- **Engaging responses:** Claude models are ideal for applications that require rich, human-like interactions. If you prefer more concise responses, adjust your prompts to guide the model toward the output length you want. Refer to the [prompt engineering guides](https://support.claude.com/docs/en/build-with-claude/prompt-engineering) for details.
- **Output quality:** When migrating from a previous model generation, you might notice larger improvements in overall performance. If you’re on Claude Opus 5 or earlier, see the [Claude Opus 5.5 migration guide](https://support.claude.com/docs/en/models/opus-5-5/migration-guide).

## Get started with Claude

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
