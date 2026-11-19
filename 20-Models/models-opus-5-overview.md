---
title: "Claude Opus 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5/overview"
category: "20-Models"
fetched_at: "2026-11-13T06:36:49Z"
tags: ["models"]
---

Although Claude Opus 5 is still available, you should consider migrating to Claude Opus 5.5.

[See Claude Opus 5.5](models-opus-5-5-overview.md)

[Models & pricing](about-claude-models-overview.md)Legacy models

# Claude Opus 5Legacy

Copy page



claude-opus-5

[Migrate to Claude Opus 5.5](models-opus-5-5-migration-guide.md#migrating-from-claude-opus-5)

Copy page



[Announcement(opens in new tab)](../19-Reference/claude-opus-5.md)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$5/ MTok

Output pricing  
\$25/ MTok

## How it compares to the current lineup

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-opus-5

[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)  
anthropic.claude-opus-5

[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)  
claude-opus-5

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-opus-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-opus-5

[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)  
claude-opus-5

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
May 2026

Training data cutoff  
May 2026

### Availability

[Status](about-claude-model-deprecations.md)  
Active (legacy)

Released  
July 24, 2026

Retirement  
Not sooner than July 24, 2027

Platforms  
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

## Good to know

- On the [Message Batches API](../04-API-Reference/Guides/build-with-claude-batch-processing.md#extended-output-beta), Claude Opus 5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- The minimum cacheable prompt length is 512 tokens. See [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#cache-limitations).
- Query limits and capabilities programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return..

## Resources

[Migrate to Claude Opus 5.5](models-opus-5-5-migration-guide.md#migrating-from-claude-opus-5)

What changes when moving from Claude Opus 5 to Claude Opus 5.5.



[Claude Opus 5.5](models-opus-5-5-overview.md)

The current Opus model: overview, specs, and resources.



[Prompting Claude Opus 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md)

Model-specific prompting guidance.

## Reference



[System prompt](release-notes-system-prompts-overview.md#claude-opus-5)

The system prompt Claude Opus 5 uses on claude.ai and the Claude apps.



[System card](../15-Claude-AI-Features/claude-opus-5-system-card.md)

Safety evaluations and deployment decisions for Claude Opus 5.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.
