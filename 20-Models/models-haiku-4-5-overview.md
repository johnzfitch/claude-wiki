---
title: "Claude Haiku 4.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/haiku-4-5/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:39:53Z"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fhaiku-4-5%2Foverview)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Claude Sonnet 5](models-sonnet-5-overview.md)

[Claude Haiku 4.5](models-haiku-4-5-overview.md)

[Overview](models-haiku-4-5-overview.md)[Migration guide](models-haiku-4-5-migration-guide.md)

Specialized models

Legacy models

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)

[Models & pricing](about-claude-models-overview.md)Models

# Claude Haiku 4.5Latest

The fastest model with near-frontier intelligence

Copy page



claude-haiku-4-5-20251001

[Try in playground](../04-API-Reference/Other/usage-limits.md)

Copy page



[Announcement(opens in new tab)](../19-Reference/claude-haiku-4-5.md)[Migration guide](models-haiku-4-5-migration-guide.md)

Context window  
200Ktokens

Max output  
64Ktokens

Input pricing  
\$1/ MTok

Output pricing  
\$5/ MTok

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-haiku-4-5-20251001

Claude API alias  
claude-haiku-4-5

[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)  
anthropic.claude-haiku-4-5

[Amazon Bedrock (InvokeModel)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)  
anthropic.claude-haiku-4-5-20251001-v1:0

[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)  
claude-haiku-4-5@20251001

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-haiku-4-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-haiku-4-5

### Pricing

Input  
\$1 / MTok

Output  
\$5 / MTok

[5m cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$1.25 / MTok

[1h cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$2 / MTok

[Cache read](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$0.10 / MTok

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
Not supported

Comparative latency  
Fastest

Input → output  
Text and images → text

Reliable knowledge cutoff  
Feb 2025

Training data cutoff  
Jul 2025

### Availability

[Status](about-claude-model-deprecations.md)  
Active (latest)

Released  
October 15, 2025

Retirement  
Not sooner than October 15, 2026

Platforms  
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (InvokeModel)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)

## Good to know

- `claude-haiku-4-5` is a convenience alias that resolves to the pinned snapshot `claude-haiku-4-5-20251001`. See [Model IDs and versioning](about-claude-models-model-ids-and-versions.md).
- Claude Haiku 4.5 uses manual extended thinking (`thinking.type: "enabled"`), not adaptive thinking.
- Query limits and capabilities programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md).

## Resources



[Extended thinking](../04-API-Reference/Guides/build-with-claude-extended-thinking.md)

Claude Haiku 4.5 supports manual extended thinking with `budget_tokens`.



[Choosing a model](about-claude-models-choosing-a-model.md)

When to start efficiency-first with Haiku and when to reach for a larger model.



[Reduce latency](../04-API-Reference/Test-Evaluate/test-and-evaluate-strengthen-guardrails-reduce-latency.md)

Techniques that pair well with the fastest model in the lineup.

## Reference



[System prompt](release-notes-system-prompts-overview.md#claude-haiku-4-5)

The system prompt Claude Haiku 4.5 uses on claude.ai and the Claude apps.



[System card](../15-Claude-AI-Features/claude-haiku-4-5-system-card.md)

Safety evaluations and deployment decisions for Claude Haiku 4.5.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.



[Amazon Bedrock (Opus 4.6 and earlier)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)

Claude Haiku 4.5 is also available through the InvokeModel Bedrock integration and Bedrock-style model IDs.
