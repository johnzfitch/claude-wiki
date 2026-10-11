---
title: "Claude Sonnet 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/sonnet-5/overview"
category: "20-Models"
fetched_at: "2026-10-04T08:34:18Z"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fsonnet-5%2Foverview)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

[Claude Haiku 4.5](models-haiku-4-5-overview.md)

Specialized models

Legacy models

[Claude Fable 5](models-fable-5-overview.md)[Claude Opus 5](models-opus-5-overview.md)[Claude Sonnet 5](models-sonnet-5-overview.md)[Claude Opus 4.8](models-opus-4-8-overview.md)[Claude Opus 4.7](models-opus-4-7-overview.md)[Claude Opus 4.6](models-opus-4-6-overview.md)[Claude Sonnet 4.6](models-sonnet-4-6-overview.md)[Claude Opus 4.5](models-opus-4-5-overview.md)[Claude Sonnet 4.5](models-sonnet-4-5-overview.md)

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)



Although Claude Sonnet 5 is still available, you should consider migrating to Claude Sonnet 5.5 for improved performance.

[See Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

[Models & pricing](about-claude-models-overview.md)Legacy models

# Claude Sonnet 5Legacy

Copy page



claude-sonnet-5

[Migrate to Claude Sonnet 5.5](models-sonnet-5-5-migration-guide.md#migrating-from-claude-sonnet-5)

Copy page



[Announcement(opens in new tab)](../19-Reference/claude-sonnet-5.md)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$2/ MTok

Output pricing  
\$10/ MTok

## How it compares to the current lineup

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-sonnet-5

[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)  
anthropic.claude-sonnet-5

[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)  
claude-sonnet-5

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-sonnet-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-sonnet-5

### Pricing

Input  
\$2 / MTok

Output  
\$10 / MTok

[5m cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$2.50 / MTok

[1h cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$4 / MTok

[Cache read](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$0.20 / MTok

[Batch API](../04-API-Reference/Guides/build-with-claude-batch-processing.md)  
50% discount on input and output

[Full price list](../17-Billing-Plans/about-claude-pricing.md)

### Capabilities

[Context window](../04-API-Reference/Guides/build-with-claude-context-windows.md)  
1M tokens

Max output  
128K tokens

[Max output (Batch API, beta)](../04-API-Reference/Guides/build-with-claude-batch-processing.md#extended-output-beta)  
300K tokens

[Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)  
Adaptive

[Default effort](../04-API-Reference/Guides/build-with-claude-effort.md)  
`high`

Input → output  
Text and images → text

Reliable knowledge cutoff  
Jan 2026

Training data cutoff  
Jan 2026

### Availability

[Status](about-claude-model-deprecations.md)  
Active (legacy)

Released  
June 30, 2026

Retirement  
Not sooner than June 30, 2027

Platforms  
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)

## Good to know

- On the [Message Batches API](../04-API-Reference/Guides/build-with-claude-batch-processing.md#extended-output-beta), Claude Sonnet 5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- Setting `temperature`, `top_p`, or `top_k` to non-default values returns a 400 error.
- Query limits and capabilities programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md).

## Resources

[Migrate to Claude Sonnet 5.5](models-sonnet-5-5-migration-guide.md#migrating-from-claude-sonnet-5)

What changes when moving from Claude Sonnet 5 to Claude Sonnet 5.5.



[Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

The current Sonnet model: overview, specs, and resources.



[Prompting Claude Sonnet 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-sonnet-5.md)

Model-specific prompting guidance.



[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)

On by default on Claude Sonnet 5. Steer depth with `effort`.



[Effort](../04-API-Reference/Guides/build-with-claude-effort.md)

Effort defaults to `high` on the Claude API and Claude Code. Choose a level per workload.



[Context windows](../04-API-Reference/Guides/build-with-claude-context-windows.md)

1M tokens by default. How the window is counted and managed.

## Reference



[System prompt](release-notes-system-prompts-claude-sonnet-5.md)

The system prompt Claude Sonnet 5 uses on claude.ai and the Claude apps.



[System card](../19-Reference/added-a-footnote-in-8-9-2-browsecomp-with-a-reproduction-recipe-via-public.md)

Safety evaluations and deployment decisions for Claude Sonnet 5.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.
