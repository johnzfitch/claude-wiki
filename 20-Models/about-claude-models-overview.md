---
title: "Models overview - Claude Platform Docs"
source_url: "https://platform.claude.com/en/docs/about-claude/models/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:39:52Z"
tags: ["api", "models", "prompting"]
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Foverview)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

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

Models & pricingModels

# Models overview

Claude is a family of state-of-the-art large language models developed by Anthropic. Compare the current lineup, find the model ID for every platform, and open each model's page for its full specs and resources.

Copy page



[Choosing a model](about-claude-models-choosing-a-model.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)[Migration guide](about-claude-models-migration-guide.md)

Copy page



## Compare models

If you're unsure which model to use, start with [Claude Opus 5.5](models-opus-5-5-overview.md) for most workloads. Use [Claude Fable 5.1](models-fable-5-1-overview.md) for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short. All current models support text and image input, text output, multilingual capabilities, vision, and tool use. Each model's page lists the platforms it's available on.

[TABLE]

Once you've picked a model, [learn how to make your first API call](../01-Getting-Started/get-started.md). To understand how model IDs, aliases, and snapshots work, see [Model IDs and versioning](about-claude-models-model-ids-and-versions.md); for the reliable-knowledge and training-data cutoffs behind each model, see [Anthropic's Transparency Hub](https://www.anthropic.com/transparency).

## Using the Models API

You can query model capabilities and token limits programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md). The response includes `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.

## Prompt and output performance

Current Claude models excel in:

- **Performance:** Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See [Prompting best practices](../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md) for general and model-specific prompting guidance.
- **Engaging responses:** Claude models are ideal for applications that require rich, human-like interactions. If you prefer more concise responses, adjust your prompts to guide the model toward the desired output length. Refer to the [prompt engineering guides](../10-Prompting-Guides/build-with-claude-prompt-engineering-overview.md) for details.
- **Output quality:** When migrating from a previous model generation, you may notice larger improvements in overall performance. If you're on Claude Opus 5 or earlier, see [Migrating to Claude Opus 5.5](models-opus-5-5-migration-guide.md).

## Get started with Claude

If you're ready to start exploring what Claude can do for you, dive in! Whether you're a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, the following resources can help.



[Intro to Claude](../01-Getting-Started/intro.md)

Explore Claude's capabilities and development flow.

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

[Claude Console](../04-API-Reference/Other/usage-limits.md)

Craft and test prompts directly in your browser.

Looking to chat with Claude? Visit [claude.ai](https://claude.ai). If you have questions, reach out to the [support team](https://support.claude.com/) or the [Discord community](https://www.anthropic.com/discord).
