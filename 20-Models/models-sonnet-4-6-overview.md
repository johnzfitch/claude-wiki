---
title: "Claude Sonnet 4.6 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/sonnet-4-6/overview"
category: "20-Models"
fetched_at: "2026-11-13T06:34:15Z"
tags: ["models"]
---

Although Claude Sonnet 4.6 is still available, you should consider migrating to Claude Sonnet 5.5.

[See Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

[Models & pricing](about-claude-models-overview.md)Legacy models

# Claude Sonnet 4.6Legacy

Copy page



claude-sonnet-4-6

[Migrate to Claude Sonnet 5.5](models-sonnet-5-5-migration-guide.md#migrating-from-claude-sonnet-4-6)

Copy page



[Announcement(opens in new tab)](../19-Reference/claude-sonnet-4-6.md)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$3/ MTok

Output pricing  
\$15/ MTok

## How it compares to the current lineup

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-sonnet-4-6

[Amazon Bedrock (bedrock-runtime)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)  
global.anthropic.claude-sonnet-4-6

[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)  
claude-sonnet-4-6

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-sonnet-4-6

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-sonnet-4-6

[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)  
claude-sonnet-4-6

### Pricing

Input  
\$3 / MTok

Output  
\$15 / MTok

[5m cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$3.75 / MTok

[1h cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$6 / MTok

[Cache read](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$0.30 / MTok

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
Adaptive (extended deprecated)

[Default effort](../04-API-Reference/Guides/build-with-claude-effort.md)  
`high`

Input → output  
Text and images → text

Reliable knowledge cutoff  
Aug 2025

Training data cutoff  
Jan 2026

### Availability

[Status](about-claude-model-deprecations.md)  
Active (legacy)

Released  
February 17, 2026

Retirement  
Not sooner than February 17, 2027

Platforms  
Claude API[Amazon Bedrock (bedrock-runtime)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

## Resources

[Migrate to Claude Sonnet 5.5](models-sonnet-5-5-migration-guide.md#migrating-from-claude-sonnet-4-6)

What changes when moving from Claude Sonnet 4.6 to Claude Sonnet 5.5.



[Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

The current Sonnet model: overview, specs, and resources.

## Reference



[System prompt](release-notes-system-prompts-overview.md#claude-sonnet-4-6)

The system prompt Claude Sonnet 4.6 uses on claude.ai and the Claude apps.



[System card](../15-Claude-AI-Features/claude-sonnet-4-6-system-card.md)

Safety evaluations and deployment decisions for Claude Sonnet 4.6.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.



[Amazon Bedrock (bedrock-runtime)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)

Claude Sonnet 4.6 is on the `bedrock-runtime` endpoint (the InvokeModel and Converse APIs), with Bedrock-style model IDs.
