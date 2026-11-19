---
title: "Claude Haiku 5.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/haiku-5-5/overview"
category: "20-Models"
fetched_at: "2026-11-14T06:25:36Z"
tags: ["models"]
---

# Claude Haiku 5.5Latest

For high-volume, latency-sensitive tasks such as classification, extraction, and routing

Copy page



claude-haiku-5-5

[Try in playground](../04-API-Reference/Other/playground.md)

Copy page



[Announcement(opens in new tab)](../15-Claude-AI-Features/claude-haiku-5-5.md)[What’s new](models-haiku-5-5-whats-new-haiku-5-5.md)[Migration guide](models-haiku-5-5-migration-guide.md)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
From \$0.10/ MTok

Output pricing  
From \$0.50/ MTok

## Overview

Claude Haiku 5.5 is built for high-volume, latency-sensitive work such as classification, routing, extraction, and subagent tasks. It supports adaptive thinking with the effort parameter, a 1M token context window, and up to 128k output tokens. It uses the same newer tokenizer as Claude 4.7 and later models, so the same text counts as approximately 30 percent more tokens than on Claude Haiku 4.5. Its thinking blocks work only in the account that produced them, or in an account linked to it.

For code changes, see the [migration guide](models-haiku-5-5-migration-guide.md). For model IDs, pricing, and limits, see the [Claude Haiku 5.5 overview](models-haiku-5-5-overview.md). For prompting guidance, see [Prompting Claude Haiku 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-haiku-5-5.md).

[What’s new in Claude Haiku 5.5](models-haiku-5-5-whats-new-haiku-5-5.md)

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-haiku-5-5

[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)  
anthropic.claude-haiku-5-5

[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)  
claude-haiku-5-5

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-haiku-5-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-haiku-5-5

[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)  
claude-haiku-5-5

### Pricing

Input  
\$0.10 / MTok for prompts up to 100,000 tokens\$0.50 / MTok for prompts over 100,000 tokens

Output  
\$0.50 / MTok for prompts up to 100,000 tokens\$2.50 / MTok for prompts over 100,000 tokens

[5m cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$0.125 / MTok for prompts up to 100,000 tokens\$0.625 / MTok for prompts over 100,000 tokens

[1h cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$0.20 / MTok for prompts up to 100,000 tokens\$1 / MTok for prompts over 100,000 tokens

[Cache read](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$0.01 / MTok for prompts up to 100,000 tokens\$0.05 / MTok for prompts over 100,000 tokens

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
`medium`

Comparative latency  
Fastest

Input → output  
Text and images → text

Reliable knowledge cutoff  
Jun 2026

Training data cutoff  
Jun 2026

### Availability

[Status](about-claude-model-deprecations.md)  
Active (latest)

Released  
October 7, 2026

Retirement  
Not sooner than October 7, 2027

Platforms  
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

## Good to know

- Adaptive thinking is on by default. Control thinking depth with the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md).
- Omit `temperature`, `top_p`, and `top_k`.
- On the [Message Batches API](../04-API-Reference/Guides/build-with-claude-batch-processing.md#extended-output-beta), Claude Haiku 5.5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- The minimum cacheable prompt length is 512 tokens. See [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#cache-limitations).
- Query limits and capabilities programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return..

## Resources



[Prompting Claude Haiku 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-haiku-5-5.md)

Behavioral differences and prompting patterns specific to Claude Haiku 5.5.



[Reduce latency](../04-API-Reference/Test-Evaluate/test-and-evaluate-strengthen-guardrails-reduce-latency.md)

Choose a model and effort level, shape prompts, and stream output for faster responses.



[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)

Claude Haiku 5.5 determines when and how much to think. Steer depth with `effort`.



[Context windows](../04-API-Reference/Guides/build-with-claude-context-windows.md)

How the context window is counted and managed.

## Reference



[System prompt](release-notes-system-prompts-claude-haiku-5-5.md)

The system prompt Claude Haiku 5.5 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/document/claude-haiku-5-5-system-card)

Safety evaluations and deployment decisions for Claude Haiku 5.5.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.
