---
title: "Claude Haiku 5.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/haiku-5-5/overview"
category: "20-Models"
fetched_at: "2026-10-08T06:24:44Z"
tags: ["models"]
---

- [Managed Agents](../04-API-Reference/Other/managed-agents-overview.md)

- [Admin](../04-API-Reference/Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../04-API-Reference/About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../04-API-Reference/Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](release-notes-overview.md)

[API reference](../04-API-Reference/Endpoints/overview.md)




[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fhaiku-5-5%2Foverview)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

[Claude Haiku 5.5](models-haiku-5-5-overview.md)

[Overview](models-haiku-5-5-overview.md)[What's new](models-haiku-5-5-whats-new-haiku-5-5.md)[Migration guide](models-haiku-5-5-migration-guide.md)

Specialized models

Legacy models

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)[API credits for subscribers](../04-API-Reference/About/about-claude-api-credits-for-subscribers.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)

[Models & pricing](about-claude-models-overview.md)Models

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

Claude Haiku 5.5 is built for high-volume, latency-sensitive work such as classification, routing, extraction, and subagent tasks. It supports adaptive thinking with the effort parameter, a 1M token context window, and up to 128k output tokens. It uses the same newer tokenizer as Claude 4.7 and later models, so the same text counts as approximately 30% more tokens than on Claude Haiku 4.5. Its thinking blocks work only in the account that produced them, or in an account linked to it.

For code changes, see the [migration guide](models-haiku-5-5-migration-guide.md). For model IDs, pricing, and limits, see the [Claude Haiku 5.5 overview](models-haiku-5-5-overview.md). For prompting guidance, see [Prompting Claude Haiku 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-haiku-5-5.md).

[What's new in Claude Haiku 5.5](models-haiku-5-5-whats-new-haiku-5-5.md)

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-haiku-5-5

[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)  
anthropic.claude-haiku-5-5

[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)  
claude-haiku-5-5

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-haiku-5-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
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
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)

## Good to know

- Adaptive thinking is on by default. Control thinking depth with the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md).
- Omit `temperature`, `top_p`, and `top_k`, since a non-default value for any of them returns a 400 error.
- On the [Message Batches API](../04-API-Reference/Guides/build-with-claude-batch-processing.md#extended-output-beta), Claude Haiku 5.5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- Query limits and capabilities programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md).

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

1M tokens. How the window is counted and managed.

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
