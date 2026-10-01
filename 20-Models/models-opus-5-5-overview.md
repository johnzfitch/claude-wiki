---
title: "Claude Opus 5.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5-5/overview"
category: "20-Models"
fetched_at: "2026-09-30T06:32:06Z"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fopus-5-5%2Foverview)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Overview](models-opus-5-5-overview.md)[What's new](models-opus-5-5-whats-new-opus-5-5.md)[Migration guide](models-opus-5-5-migration-guide.md)

[Claude Sonnet 5.5](models-sonnet-5-5-overview.md)

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

# Claude Opus 5.5Latest

For long-running agentic coding and knowledge work

Copy page



claude-opus-5-5

[Try in playground](../04-API-Reference/Other/usage-limits.md)

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

Claude Opus 5.5 is built for long-running agentic coding and knowledge work, priced at \$4 / \$20 USD per million input / output tokens. Four breaking changes affect code already running on Claude Opus 5: [thinking can't be disabled](models-opus-5-5-whats-new-opus-5-5.md#thinking-cant-be-disabled), [forced tool use returns an error](models-opus-5-5-whats-new-opus-5-5.md#forced-tool-use-is-not-supported), [thinking blocks are tied to the model and the conversation](models-opus-5-5-whats-new-opus-5-5.md#thinking-blocks-are-tied-to-the-model-that-produced-them), and, on the Claude API and Google Cloud, [the earlier `computer_20251124` computer use tool is not accepted](models-opus-5-5-whats-new-opus-5-5.md#computer-20251124-is-not-supported). The first three also apply on Claude Fable 5.1. A further change alters the response shape without failing any request: [text between tool calls comes back in `thinking` blocks](models-opus-5-5-whats-new-opus-5-5.md#text-between-tool-calls) whose text is empty at the default `display` setting. An application that streams that text to its users as progress updates goes quiet between tool calls until it sets a `display` value that returns the text.

[What's new in Claude Opus 5.5](models-opus-5-5-whats-new-opus-5-5.md)

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-opus-5-5

[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)  
anthropic.claude-opus-5-5

[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)  
claude-opus-5-5

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-opus-5-5

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
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
Claude API[Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md)[Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)

## Good to know

- Adaptive thinking is always on and can't be turned off. Control thinking depth with the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md).
- On the [Message Batches API](../04-API-Reference/Guides/build-with-claude-batch-processing.md#extended-output-beta), Claude Opus 5.5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- The minimum cacheable prompt length is 512 tokens. See [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#cache-limitations).
- Query limits and capabilities programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md).

## Resources



[Prompting Claude Opus 5.5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md)

Behavioral differences and prompting patterns specific to Claude Opus 5.5.



[Effort](../04-API-Reference/Guides/build-with-claude-effort.md)

The control for thinking depth, latency, and cost. Choose a level per workload.



[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)

How adaptive thinking works and how thinking blocks are preserved.



[Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md)

Lower-latency Claude Opus 5.5 on the Claude API (research preview), priced separately.

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
