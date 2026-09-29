---
title: "Claude Fable 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/fable-5/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:39:44Z"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Ffable-5%2Foverview)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Claude Sonnet 5](models-sonnet-5-overview.md)

[Claude Haiku 4.5](models-haiku-4-5-overview.md)

Specialized models

Legacy models

[Claude Fable 5](models-fable-5-overview.md)[Claude Opus 5](models-opus-5-overview.md)[Claude Opus 4.8](models-opus-4-8-overview.md)[Claude Opus 4.7](models-opus-4-7-overview.md)[Claude Opus 4.6](models-opus-4-6-overview.md)[Claude Sonnet 4.6](models-sonnet-4-6-overview.md)[Claude Opus 4.5](models-opus-4-5-overview.md)[Claude Sonnet 4.5](models-sonnet-4-5-overview.md)

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)



Although Claude Fable 5 is still available, you should consider migrating to Claude Fable 5.1 for improved performance.

[See Claude Fable 5.1](models-fable-5-1-overview.md)

[Models & pricing](about-claude-models-overview.md)Legacy models

# Claude Fable 5Legacy

Copy page



claude-fable-5

[Migrate to Claude Fable 5.1](models-fable-5-1-migration-guide.md#migrating-from-claude-fable-5-to-claude-fable-5-1)

Copy page



[Announcement(opens in new tab)](../19-Reference/claude-fable-5-mythos-5.md)[What’s new](models-fable-5-introducing-claude-fable-5-and-claude-mythos-5.md)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$10/ MTok

Output pricing  
\$50/ MTok

## Fable vs. Mythos

[Claude Mythos 5](models-mythos-5-overview.md) is offered separately, by invitation only, for defensive cybersecurity workflows as part of [Project Glasswing](../22-Safety-Policy/glasswing.md). It shares Claude Fable 5's specifications and pricing; Claude Fable 5 includes safety classifiers that can decline requests, and Claude Mythos 5 does not. For access, contact your Anthropic, AWS, or Google Cloud account team.

## How it compares to the current lineup

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-fable-5

[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)  
anthropic.claude-fable-5

[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)  
claude-fable-5

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-fable-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
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
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)

## Resources

[Migrate to Claude Fable 5.1](models-fable-5-1-migration-guide.md#migrating-from-claude-fable-5-to-claude-fable-5-1)

What changes when moving from Claude Fable 5 to Claude Fable 5.1.



[Claude Fable 5.1](models-fable-5-1-overview.md)

The current Fable model: overview, specs, and resources.



[Introducing Claude Fable 5 and Claude Mythos 5](models-fable-5-introducing-claude-fable-5-and-claude-mythos-5.md)

Capabilities, API changes, and availability for Claude Fable 5.

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
