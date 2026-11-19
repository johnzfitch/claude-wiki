---
title: "Claude Sonnet 4.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/sonnet-4-5/overview"
category: "20-Models"
fetched_at: "2026-11-13T06:36:59Z"
tags: ["models"]
---

Claude Sonnet 4.5 is deprecated: it is still functional but no longer recommended, and retires on November 30, 2026. Recommended replacement: Claude Sonnet 5.5.

[See Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

[Models & pricing](about-claude-models-overview.md)Legacy models

# Claude Sonnet 4.5Deprecated

Copy page



claude-sonnet-4-5-20250929

[Migrate to Claude Sonnet 5.5](models-sonnet-5-5-migration-guide.md#migrating-from-sonnet-45)

Copy page



[Announcement(opens in new tab)](../19-Reference/claude-sonnet-4-5.md)

Context window  
200Ktokens

Max output  
64Ktokens

Input pricing  
\$3/ MTok

Output pricing  
\$15/ MTok

## How it compares to the current lineup

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-sonnet-4-5-20250929

Claude API alias  
claude-sonnet-4-5

[Amazon Bedrock (bedrock-runtime)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)  
global.anthropic.claude-sonnet-4-5-20250929-v1:0

[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)  
claude-sonnet-4-5@20250929

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-sonnet-4-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-sonnet-4-5

[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)  
claude-sonnet-4-5-20250929

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
Jan 2025

Training data cutoff  
Jul 2025

### Availability

[Status](about-claude-model-deprecations.md)  
Deprecated

Released  
September 29, 2025

Deprecated  
September 30, 2026

Retires  
November 30, 2026

Platforms  
Claude API[Amazon Bedrock (bedrock-runtime)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

## Resources

[Migrate to Claude Sonnet 5.5](models-sonnet-5-5-migration-guide.md#migrating-from-claude-sonnet-4-6)

What changes when moving from Claude Sonnet 4.5 and earlier Sonnet models to Claude Sonnet 5.5.



[Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

The current Sonnet model: overview, specs, and resources.

## Reference



[System prompt](release-notes-system-prompts-overview.md#claude-sonnet-4-5)

The system prompt Claude Sonnet 4.5 uses on claude.ai and the Claude apps.



[System card](../19-Reference/updated-footnote-24-stress-testing-deliberative-alignment-to-correct.md)

Safety evaluations and deployment decisions for Claude Sonnet 4.5.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.



[Amazon Bedrock (bedrock-runtime)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)

Claude Sonnet 4.5 is on the `bedrock-runtime` endpoint (the InvokeModel and Converse APIs), with Bedrock-style model IDs.
