---
title: "Claude Fable 5.1 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/fable-5-1/overview"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Ffable-5-1%2Foverview)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Overview](models-fable-5-1-overview.md)[What's new](models-fable-5-1-whats-new-fable-5-1.md)[Migration guide](models-fable-5-1-migration-guide.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Claude Sonnet 5](models-sonnet-5-overview.md)

[Claude Haiku 4.5](models-haiku-4-5-overview.md)

Specialized models

Legacy models

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)

[Models & pricing](about-claude-models-overview.md)Models

# Claude Fable 5.1Latest

For demanding reasoning and long-horizon agentic work

Copy page



claude-fable-5-1

[Try in playground](../04-API-Reference/Other/usage-limits.md)

Copy page



[Announcement(opens in new tab)](../15-Claude-AI-Features/claude-fable-and-mythos-5-1.md)[What’s new](models-fable-5-1-whats-new-fable-5-1.md)[Migration guide](models-fable-5-1-migration-guide.md)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$10/ MTok

Output pricing  
\$50/ MTok

## Overview

Claude Fable 5.1 extends Claude Fable 5 at the same input and output prices, with cache reads at a quarter of the cost, and brings stronger long-running agentic coding, multistep research, and document, spreadsheet, and slide work. For most workloads, start with Claude Opus 5 (see [Choosing a model](about-claude-models-choosing-a-model.md)). Use Claude Fable 5.1 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5 at higher effort still fall short. Claude Mythos 5.1 offers the same capabilities to [Project Glasswing](../22-Safety-Policy/glasswing.md) participants only.

If you already call Claude Fable 5, three changes are breaking: [forced tool use returns an error](models-fable-5-1-whats-new-fable-5-1.md#forced-tool-use-is-not-supported), [earlier models can't read its thinking blocks](models-fable-5-1-whats-new-fable-5-1.md#thinking-blocks-are-tied-to-the-model-that-produced-them), and [editing earlier turns invalidates thinking blocks](models-fable-5-1-whats-new-fable-5-1.md#editing-earlier-turns-invalidates-thinking-blocks). Five are additive: [per-message effort](models-fable-5-1-whats-new-fable-5-1.md#change-effort-mid-conversation-beta) (beta), [turn-scoped system messages](models-fable-5-1-whats-new-fable-5-1.md#turn-scoped-system-messages-beta) (beta), [readable progress updates between tool calls](models-fable-5-1-whats-new-fable-5-1.md#progress-updates-between-tool-calls-beta) (`display: "updates"`, beta), a [lower cache read price](models-fable-5-1-whats-new-fable-5-1.md#pricing), and [content provenance](models-fable-5-1-whats-new-fable-5-1.md#content-provenance).

[What's new in Claude Fable 5.1](models-fable-5-1-whats-new-fable-5-1.md)

## Claude Fable 5.1 and Claude Mythos 5.1

[Claude Mythos 5.1](models-mythos-5-1-overview.md) offers the same capabilities by invitation only, as part of [Project Glasswing](../22-Safety-Policy/glasswing.md). It shares Claude Fable 5.1's specifications and pricing. For access, contact your Anthropic, AWS, or Google Cloud account team.

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-fable-5-1

[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)  
anthropic.claude-fable-5-1

[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)  
claude-fable-5-1

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-fable-5-1

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-fable-5-1

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
\$0.25 / MTok

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

Comparative latency  
Slower

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
September 1, 2026

Retirement  
Not sooner than September 1, 2027

Platforms  
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)

## Resources



[Prompting Claude Fable 5.1](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md)

Model-specific prompting guidance for long-horizon and agentic work.



[Migrating to Claude Fable 5.1](models-fable-5-1-migration-guide.md)

What changes when you move from Claude Fable 5, Claude Opus 5, or Claude Opus 4.8.



[Preserved thinking](../04-API-Reference/Guides/build-with-claude-thinking.md#preserved-thinking)

When this model's thinking blocks stay usable: across model switches and across changes to the conversation.



[Per-message effort](../04-API-Reference/Guides/build-with-claude-effort.md#change-effort-mid-conversation-beta)

Change the effort level partway through a conversation without invalidating the prompt cache.



[Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md)

Handle classifier refusals and retry on another Claude model.



[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)

The only thinking mode on Claude Fable 5.1. Steer depth with `effort`.

## Reference



[System prompt](release-notes-system-prompts-claude-fable-5-1.md)

The system prompt Claude Fable 5.1 uses on claude.ai and the Claude apps.



[System card](../15-Claude-AI-Features/claude-fable-5-1-mythos-5-1-system-card.md)

Safety evaluations and deployment decisions for Claude Fable 5.1 and Claude Mythos 5.1.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.
