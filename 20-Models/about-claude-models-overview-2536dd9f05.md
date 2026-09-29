---
title: "Models overview - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/about-claude/models/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:38:13Z"
tags: ["api", "prompting"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Foverview)





SearchCtrlK

Models

[Models overview](/docs/en/models/overview)

[Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

[Claude Opus 5.5](/docs/en/models/opus-5-5/overview)

[Claude Sonnet 5](/docs/en/models/sonnet-5/overview)

[Claude Haiku 4.5](/docs/en/models/haiku-4-5/overview)

Specialized models

Legacy models

Guides

[Choosing a model](/docs/en/about-claude/models/choosing-a-model)[Optimizing for cost and intelligence](/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)[Upgrade between model versions](/docs/en/about-claude/models/migration-guide)

Lifecycle and reference

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)[Model deprecations](/docs/en/about-claude/model-deprecations)[Model cards](/docs/en/resources/overview)[Pricing](/docs/en/about-claude/pricing)

[System prompts](/docs/en/release-notes/system-prompts/overview)

[Console](/)

Models & pricingModels

# Models overview

Claude is a family of state-of-the-art large language models developed by Anthropic. Compare the current lineup, find the model ID for every platform, and open each model's page for its full specs and resources.

Copy page



[Choosing a model](/docs/en/about-claude/models/choosing-a-model)[Pricing](/docs/en/about-claude/pricing)[Migration guide](/docs/en/about-claude/models/migration-guide)

Copy page



## Compare models

If you're unsure which model to use, start with [Claude Opus 5.5](/docs/en/models/opus-5-5/overview) for most workloads. Use [Claude Fable 5.1](/docs/en/models/fable-5-1/overview) for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short. All current models support text and image input, text output, multilingual capabilities, vision, and tool use. Each model's page lists the platforms it's available on.

[TABLE]

Once you've picked a model, [learn how to make your first API call](/docs/en/get-started). To understand how model IDs, aliases, and snapshots work, see [Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions); for the reliable-knowledge and training-data cutoffs behind each model, see [Anthropic's Transparency Hub](https://www.anthropic.com/transparency).

## Using the Models API

You can query model capabilities and token limits programmatically with the [Models API](/docs/en/api/models/list). The response includes `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.

## Prompt and output performance

Current Claude models excel in:

- **Performance:** Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) for general and model-specific prompting guidance.
- **Engaging responses:** Claude models are ideal for applications that require rich, human-like interactions. If you prefer more concise responses, adjust your prompts to guide the model toward the desired output length. Refer to the [prompt engineering guides](/docs/en/build-with-claude/prompt-engineering) for details.
- **Output quality:** When migrating from a previous model generation, you may notice larger improvements in overall performance. If you're on Claude Opus 5 or earlier, see [Migrating to Claude Opus 5.5](/docs/en/models/opus-5-5/migration-guide).

## Get started with Claude

If you're ready to start exploring what Claude can do for you, dive in! Whether you're a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, the following resources can help.



[Intro to Claude](/docs/en/intro)

Explore Claude's capabilities and development flow.



[Quickstart](/docs/en/get-started)

Learn how to make your first API call in minutes.

[Choosing a model](/docs/en/about-claude/models/choosing-a-model)

Establish criteria and pick the right model for your use case.

[Pricing](/docs/en/about-claude/pricing)

Complete pricing, including batch discounts and prompt caching rates.



[Model deprecations](/docs/en/about-claude/model-deprecations)

Lifecycle status and retirement commitments for every model.



[Claude Console](/)

Craft and test prompts directly in your browser.

Looking to chat with Claude? Visit [claude.ai](https://claude.ai). If you have questions, reach out to the [support team](https://support.claude.com/) or the [Discord community](https://www.anthropic.com/discord).
