---
title: "Claude Haiku 4.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/haiku-4-5/overview"
category: "20-Models"
fetched_at: "2026-11-05T06:37:14Z"
tags: ["models"]
---

Although Claude Haiku 4.5 is still available, you should consider migrating to Claude Haiku 5.5.

[See Claude Haiku 5.5](models-haiku-5-5-overview.md)

[Models & pricing](about-claude-models-overview.md)Legacy models

# Claude Haiku 4.5Legacy

Copy page



claude-haiku-4-5-20251001

[Migrate to Claude Haiku 5.5](models-haiku-5-5-migration-guide.md)

Copy page



[Announcement(opens in new tab)](../19-Reference/claude-haiku-4-5.md)

Context window  
200Ktokens

Max output  
64Ktokens

Input pricing  
\$1/ MTok

Output pricing  
\$5/ MTok

## How it compares to the current lineup

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

[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)  
claude-haiku-4-5@20251001

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-haiku-4-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-haiku-4-5

[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)  
claude-haiku-4-5-20251001

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

Input → output  
Text and images → text

Reliable knowledge cutoff  
Feb 2025

Training data cutoff  
Jul 2025

### Availability

[Status](about-claude-model-deprecations.md)  
Active (legacy)

Released  
October 15, 2025

Retirement  
Not sooner than October 15, 2026

Platforms  
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (InvokeModel)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

## Good to know

- `claude-haiku-4-5` is a convenience alias that resolves to the pinned snapshot `claude-haiku-4-5-20251001`. See [Model IDs and versioning](about-claude-models-model-ids-and-versions.md).
- Claude Haiku 4.5 uses manual extended thinking (`thinking.type: "enabled"`), not adaptive thinking.
- Query limits and capabilities programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md).

## Resources

[Migrate to Claude Haiku 5.5](models-haiku-5-5-migration-guide.md)

What changes when moving from Claude Haiku 4.5 to Claude Haiku 5.5.



[Claude Haiku 5.5](models-haiku-5-5-overview.md)

The current Haiku model: overview, specs, and resources.



[Extended thinking](../04-API-Reference/Guides/build-with-claude-extended-thinking.md)

Claude Haiku 4.5 supports manual extended thinking with `budget_tokens`.

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
