---
title: "Claude Opus 5.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5-5/overview"
category: "20-Models"
fetched_at: "2026-11-07T06:23:56Z"
tags: ["models"]
---

# Claude Opus 5.5Latest

For long-running agentic coding and knowledge work

Copy page



claude-opus-5-5

[Try in playground](../04-API-Reference/Other/playground.md)

Copy page



[Announcement(opens in new tab)](../15-Claude-AI-Features/claude-opus-5-5.md)[What’s new](models-opus-5-5-whats-new-opus-5-5.md)[Migration guide](models-opus-5-5-migration-guide.md)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$4/ MTok

Output pricing  
\$20/ MTok

## Overview

Claude Opus 5.5 is built for long-running agentic coding and knowledge work. Typical uses include multihour autonomous coding agents, large-scale refactoring, complex systems engineering, vision-heavy workflows, and computer use.

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-opus-5-5

[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)  
anthropic.claude-opus-5-5

[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)  
claude-opus-5-5

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-opus-5-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-opus-5-5

[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)  
claude-opus-5-5

### Pricing

Input  
\$4 / MTok

Output  
\$20 / MTok

[5m cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$5 / MTok

[1h cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$8 / MTok

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
Adaptive (always on)

[Default effort](../04-API-Reference/Guides/build-with-claude-effort.md)  
`medium`

Comparative latency  
Moderate

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
September 22, 2026

Retirement  
Not sooner than September 22, 2027

Platforms  
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

## Good to know

- Adaptive thinking is always on and can’t be turned off. Control thinking depth with the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md).
- On the [Message Batches API](../04-API-Reference/Guides/build-with-claude-batch-processing.md#extended-output-beta), Claude Opus 5.5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- The minimum cacheable prompt length is 512 tokens. See [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#cache-limitations).
- Query limits and capabilities programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return..

## Resources



[Prompting Claude Opus 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md)

Behavioral differences and prompting patterns specific to Claude Opus 5.5.



[Effort](../04-API-Reference/Guides/build-with-claude-effort.md)

The control for thinking depth, latency, and cost. Choose a level for each workload.



[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)

How adaptive thinking works and how thinking blocks are preserved.



[Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md)

Lower-latency Claude Opus 5.5 on the Claude API, priced separately.

## Reference



[System prompt](release-notes-system-prompts-claude-opus-5-5.md)

The system prompt Claude Opus 5.5 uses on claude.ai and the Claude apps.



[System card](../15-Claude-AI-Features/claude-opus-5-5-system-card.md)

Safety evaluations and deployment decisions for Claude Opus 5.5.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.
