---
title: "Claude Fable 5.2 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/fable-5-2/overview"
category: "20-Models"
fetched_at: "2026-11-18T06:27:42Z"
tags: ["models"]
---

# Claude Fable 5.2Latest

For demanding reasoning and long-horizon agentic work

Copy page



claude-fable-5-2

[Try in playground](../04-API-Reference/Other/playground.md)

Copy page



[Announcement(opens in new tab)](../15-Claude-AI-Features/claude-fable-and-mythos-5-2.md)[What’s new](models-fable-5-2-whats-new-fable-5-2.md)[Migration guide](models-fable-5-2-migration-guide.md)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$8/ MTok

Output pricing  
\$40/ MTok

## Overview

Claude Fable 5.2 is built for demanding reasoning and long-horizon agentic work. Typical uses include agent sessions that run for hours, multistep deep research, and analysis carried through to a finished document, spreadsheet, or deck.

## Claude Fable 5.2 and Claude Mythos 5.2

[Claude Mythos 5.2](models-mythos-5-2-overview.md) offers the same capabilities only to organizations verified through Anthropic’s verification programs, such as the [Cyber Verification Program](https://support.claude.com/en/articles/14604842). It shares Claude Fable 5.2’s specifications and pricing. To request access, apply to the program that covers your use case, or contact your account team.

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-fable-5-2

[Amazon Bedrock (bedrock-runtime)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)  
global.anthropic.claude-fable-5-2

[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)  
claude-fable-5-2

[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)  
claude-fable-5-2

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)  
claude-fable-5-2

[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)  
claude-fable-5-2

### Pricing

Input  
\$8 / MTok

Output  
\$40 / MTok

[5m cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$10 / MTok

[1h cache write](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)  
\$16 / MTok

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

[Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)  
Adaptive (always on)

[Default effort](../04-API-Reference/Guides/build-with-claude-effort.md)  
`high`

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
November 9, 2026

Retirement  
Not sooner than November 9, 2027

Platforms  
Claude API[Amazon Bedrock (bedrock-runtime)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)[Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md)[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md)[Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

## Good to know

- Adaptive thinking is always on and can’t be turned off. Control thinking depth with the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md).
- Forced tool use (`tool_choice` types `any` and `tool`) returns a 400 error. See [Thinking and tool choice](models-fable-5-2-whats-new-fable-5-2.md#thinking-and-tool-choice).
- Omit `temperature`, `top_p`, and `top_k`. See [Sampling parameters](../04-API-Reference/Guides/build-with-claude-thinking.md#sampling-parameters) for the values that return a 400 error.
- Claude Fable 5.2 requires 30-day data retention and isn’t available under zero data retention unless expressly authorized by Anthropic. See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements).
- Query limits and capabilities programmatically with the [Models API](../04-API-Reference/Endpoints/models-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return..

## Resources



[Prompting Claude Fable 5.2](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-2.md)

Behavioral differences and prompting patterns specific to Claude Fable 5.2.



[Claude Fable 5.2 migration guide](models-fable-5-2-migration-guide.md)

What changes when you move from Claude Fable 5.1 or from a Claude Opus model.



[Preserved thinking](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md)

Editing earlier turns invalidates thinking blocks.



[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)

How adaptive thinking works. It’s the only thinking mode on Claude Fable 5.2.



[Effort](../04-API-Reference/Guides/build-with-claude-effort.md)

The control for thinking depth, latency, and cost. Choose a level for each workload.



[Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md)

Handle classifier refusals and retry on another Claude model.



[Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md)

Faster output from Claude Fable 5.2 in Messages API requests, at premium pricing.

## Reference



[System prompt](release-notes-system-prompts-claude-fable-5-2.md)

The system prompt Claude Fable 5.2 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card)

Safety evaluations and deployment decisions for Claude Fable 5.2 and Claude Mythos 5.2.

[Pricing](../17-Billing-Plans/about-claude-pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude-model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.
