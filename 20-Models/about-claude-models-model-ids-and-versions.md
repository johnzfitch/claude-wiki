---
title: "Model IDs and versioning - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions"
category: "20-Models"
fetched_at: "2026-09-26T06:38:09Z"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fabout-claude%2Fmodels%2Fmodel-ids-and-versions)

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

[Models & pricing](about-claude-models-overview.md)Lifecycle and reference

# Model IDs and versioning

Copy page



How Claude model IDs are structured and versioned, including the dateless format introduced with the Claude 4.6 generation and what it means for stability.

Copy page



Each Claude model ID identifies a pinned version of the model. When you use a model ID in an API request, the underlying model remains constant for the lifetime of that ID. This guarantee covers model IDs, not the convenience aliases that the Claude API accepts for some earlier models (see [Before the 4.6 generation](#before-the-4-6-generation)).

## Model ID format

Claude model IDs follow a versioned naming scheme.

### The 4.6 generation and later

Starting with the Claude 4.6 generation, model IDs use a dateless format:

``` block
claude-{name}-{major}[-{minor}]
```



Major-version releases such as Claude Sonnet 5 and Claude Opus 5 omit the minor segment.

For example: `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-opus-4-6`, `claude-opus-4-7`, `claude-opus-4-8`, and `claude-opus-5`

On Amazon Bedrock, the corresponding format is:

``` block
anthropic.claude-{name}-{major}[-{minor}]
```



For example: `anthropic.claude-sonnet-4-6`, `anthropic.claude-sonnet-5`, `anthropic.claude-opus-4-7`, `anthropic.claude-opus-4-8`, `anthropic.claude-opus-5`

Claude Opus 4.6 is the last Bedrock model ID to include the `-v1` suffix (`anthropic.claude-opus-4-6-v1`). Anthropic dropped the suffix starting with Claude Sonnet 4.6.

On Google Cloud, the format matches the Claude API.

### Before the 4.6 generation

Models before the 4.6 generation include a snapshot date in the ID:

``` block
claude-{name}-{major}-{minor}-{YYYYMMDD}
```



For example: `claude-sonnet-4-5-20250929`, `claude-haiku-4-5-20251001`

On Amazon Bedrock, these use the format:

``` block
anthropic.claude-{name}-{major}-{minor}-{YYYYMMDD}-v1:0
```



For example: `anthropic.claude-sonnet-4-5-20250929-v1:0`

On Google Cloud, the date is separated with `@`:

``` block
claude-{name}-{major}-{minor}@{YYYYMMDD}
```



For example: `claude-haiku-4-5@20251001`

On the Claude API, these models also have shorter aliases (for example, `claude-sonnet-4-5`) that point to the most recent dated snapshot for that minor version.

## Dateless IDs are pinned snapshots

A common misconception is that dateless model IDs such as `claude-sonnet-4-6` behave as evergreen pointers that route to the latest or best-performing version. That is not the case.

For the 4.6 generation and later, the dateless ID is the canonical model ID for that release. It maps to a single, fixed model snapshot. Anthropic does not update the weights or configuration of an existing model ID. When an updated version is available, it ships under a new model ID.

This differs from the dateless aliases that exist on the Claude API for earlier models. An alias such as `claude-sonnet-4-5` is a convenience pointer that resolves to the most recent dated snapshot for that minor version. A 4.6-generation ID such as `claude-sonnet-4-6` is not an alias. It is the snapshot.

Every model ID, whether dated or dateless, has its own distinct deprecation and retirement schedule.

## Model weights versus serving infrastructure

Model weights are fixed for a given ID, but the serving infrastructure around the model can change over time. This infrastructure includes components such as the request router, safety classifiers, and sampling logic.

Occasionally, infrastructure updates produce minor differences in observable behavior even when the model ID and weights have not changed. If you notice unexpected behavioral differences on a previously stable model ID, an infrastructure update is the most likely cause.

## Current model IDs

For the full list of current model IDs and their Amazon Bedrock and Google Cloud equivalents, see [Models overview](about-claude-models-overview.md).
