---
title: "Claude Fable 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/fable-5/overview"
category: "20-Models"
fetched_at: "2026-11-13T06:35:13Z"
tags: ["models"]
---

Although Claude Fable 5 is still available, you should consider migrating to Claude Fable 5.2.

[See Claude Fable 5.2](models-fable-5-2-overview.md)

[Models & pricing](about-claude-models-overview.md)Legacy models

# Claude Fable 5Legacy

Copy page



claude-fable-5

[Migrate to Claude Fable 5.2](models-fable-5-2-migration-guide.md#migrating-from-claude-fable-5-to-claude-fable-5-2)

Copy page



[Announcement(opens in new tab)](../19-Reference/claude-fable-5-mythos-5.md)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$10/ MTok

Output pricing  
\$50/ MTok

## Fable versus Mythos

[Claude Mythos 5](models-mythos-5-overview.md) is offered separately for defensive cybersecurity workflows and is available only to organizations verified through Anthropic’s verification programs, such as the [Cyber Verification Program](https://support.claude.com/en/articles/14604842). It shares Claude Fable 5’s specifications and pricing.

## How it compares to the current lineup

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-fable-5

[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)  
anthropic.claude-fable-5

[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)  
claude-fable-5

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-fable-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-fable-5

[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)  
claude-fable-5

### Pricing

Input  
\$10 / MTok

Output  
\$50 / MTok

[5m cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$12.50 / MTok

[1h cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$20 / MTok

[Cache read](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$1 / MTok

[Batch API](../04-API-Reference/Guides/build-with-claude-batch-processing.md)  
50% discount on input and output

[Full price list](../17-Billing-Plans/about-claude-pricing.md)

### Capabilities

[Context window](../04-API-Reference/Guides/build-with-claude-context-windows.md)  
1M tokens

Max output  
128K tokens

[Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)  
Adaptive (always on)

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
June 9, 2026

Retirement  
Not sooner than June 9, 2027

Platforms  
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

## Resources

[Migrate to Claude Fable 5.2](models-fable-5-2-migration-guide.md#migrating-from-claude-fable-5-to-claude-fable-5-2)

What changes when moving from Claude Fable 5 to Claude Fable 5.2.



[Claude Fable 5.2](models-fable-5-2-overview.md)

The current Fable model: overview, specs, and resources.



[Prompting Claude Fable 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5.md)

Model-specific prompting guidance for long-horizon and agentic work.



[Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md)

Handle classifier refusals and retry on another Claude model with the `fallbacks` parameter.

## Reference



[System prompt](release-notes-system-prompts-overview.md#claude-fable-5)

The system prompt Claude Fable 5 uses on claude.ai and the Claude apps.



[System card](../15-Claude-AI-Features/claude-fable-5-mythos-5-system-card.md)

Safety evaluations and deployment decisions for Claude Fable 5 and Claude Mythos 5.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.
