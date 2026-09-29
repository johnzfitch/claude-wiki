---
title: "Claude Opus 4.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-4-5/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:39:44Z"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fopus-4-5%2Foverview)

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

[Claude Fable 5](models-fable-5-overview.md)[Claude Opus 5](models-opus-5-overview.md)[Claude Opus 4.8](models-opus-4-8-overview.md)[Claude Opus 4.7](models-opus-4-7-overview.md)[Claude Opus 4.6](models-opus-4-6-overview.md)[Claude Sonnet 4.6](models-sonnet-4-6-overview.md)[Claude Opus 4.5](models-opus-4-5-overview.md)[Claude Sonnet 4.5](models-sonnet-4-5-overview.md)

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)



Although Claude Opus 4.5 is still available, you should consider migrating to Claude Opus 5.5 for improved performance.

[See Claude Opus 5.5](models-opus-5-5-overview.md)

[Models & pricing](about-claude-models-overview.md)Legacy models

# Claude Opus 4.5Legacy

Copy page



claude-opus-4-5-20251101

[Migrate to Claude Opus 5.5](models-opus-5-5-migration-guide.md#migrating-from-claude-opus-45)

Copy page



[Announcement(opens in new tab)](../19-Reference/claude-opus-4-5.md)

Context window  
200Ktokens

Max output  
64Ktokens

Input pricing  
\$5/ MTok

Output pricing  
\$25/ MTok

## How it compares to the current lineup

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-opus-4-5-20251101

Claude API alias  
claude-opus-4-5

[Amazon Bedrock (InvokeModel)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)  
anthropic.claude-opus-4-5-20251101-v1:0

[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)  
claude-opus-4-5@20251101

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-opus-4-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-opus-4-5

### Pricing

Input  
\$5 / MTok

Output  
\$25 / MTok

[5m cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$6.25 / MTok

[1h cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$10 / MTok

[Cache read](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$0.50 / MTok

[Batch API](../04-API-Reference/Guides/build-with-claude-batch-processing.md)  
50% discount on input and output

[Full price list](../17-Billing-Plans/about-claude-pricing.md)

### Capabilities

[Context window](../04-API-Reference/Guides/build-with-claude-context-windows.md)  
200K tokens

Max output  
64K tokens

[Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)  
Extended

[Default effort](../04-API-Reference/Guides/build-with-claude-effort.md)  
`high`

Input → output  
Text and images → text

Reliable knowledge cutoff  
May 2025

Training data cutoff  
Aug 2025

### Availability

[Status](about-claude-model-deprecations.md)  
Active (legacy)

Released  
November 24, 2025

Retirement  
Not sooner than November 24, 2026

Platforms  
Claude API[Amazon Bedrock (InvokeModel)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)

## Resources

[Migrate to Claude Opus 5.5](models-opus-5-5-migration-guide.md#migrating-from-claude-opus-45)

What changes when moving from Claude Opus 4.5 to Claude Opus 5.5.



[Claude Opus 5.5](models-opus-5-5-overview.md)

The current Opus model: overview, specs, and resources.

## Reference



[System prompt](release-notes-system-prompts-overview.md#claude-opus-4-5)

The system prompt Claude Opus 4.5 uses on claude.ai and the Claude apps.



[System card](../15-Claude-AI-Features/claude-opus-4-5-system-card.md)

Safety evaluations and deployment decisions for Claude Opus 4.5.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.



[Amazon Bedrock (Opus 4.6 and earlier)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)

Claude Opus 4.5 uses the InvokeModel Bedrock integration and Bedrock-style model IDs.
