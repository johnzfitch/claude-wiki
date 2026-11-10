---
title: "Claude Opus 4.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-4-5/overview"
category: "20-Models"
fetched_at: "2026-11-05T06:36:51Z"
tags: ["models"]
---

Although Claude Opus 4.5 is still available, you should consider migrating to Claude Opus 5.5.

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

[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)  
claude-opus-4-5@20251101

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-opus-4-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-opus-4-5

[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)  
claude-opus-4-5-20251101

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
Claude API[Amazon Bedrock (InvokeModel)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

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
