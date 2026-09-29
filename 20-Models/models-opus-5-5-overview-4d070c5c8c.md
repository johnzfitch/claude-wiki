---
title: "Claude Opus 5.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5-5/overview"
category: "20-Models"
fetched_at: "2026-09-23T06:27:34Z"
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fopus-5-5%2Foverview)





SearchCtrlK

Models

[Models overview](/docs/en/models/overview)

[Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

[Claude Opus 5.5](/docs/en/models/opus-5-5/overview)

[Overview](/docs/en/models/opus-5-5/overview)[What's new](/docs/en/models/opus-5-5/whats-new-opus-5-5)[Migration guide](/docs/en/models/opus-5-5/migration-guide)

[Claude Opus 5](/docs/en/models/opus-5/overview)

[Claude Sonnet 5](/docs/en/models/sonnet-5/overview)

[Claude Haiku 4.5](/docs/en/models/haiku-4-5/overview)

Specialized models

Legacy models

Guides

[Choosing a model](/docs/en/about-claude/models/choosing-a-model)[Optimizing for cost and intelligence](/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)[Upgrade between model versions](/docs/en/about-claude/models/migration-guide)

Lifecycle and reference

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)[Model deprecations](/docs/en/about-claude/model-deprecations)[Model cards](/docs/en/resources/overview)[Pricing](/docs/en/about-claude/pricing)

[System prompts](/docs/en/release-notes/system-prompts/overview)

[Console](/)

[Models & pricing](/docs/en/models/overview)Models

# Claude Opus 5.5Latest

For long-running agentic coding and knowledge work

Copy page



claude-opus-5-5

[Try in playground](/playground?model=claude-opus-5-5)

Copy page



[Announcement](https://www.anthropic.com/news/claude-opus-5-5)·[What’s new](/docs/en/models/opus-5-5/whats-new-opus-5-5)·[Migration guide](/docs/en/models/opus-5-5/migration-guide)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$4/ MTok

Output pricing  
\$20/ MTok

## Overview

Claude Opus 5.5 is built for long-running agentic coding and knowledge work, priced at \$4 / \$20 USD per million input / output tokens. Four breaking changes affect code already running on Claude Opus 5: [thinking can't be disabled](/docs/en/models/opus-5-5/whats-new-opus-5-5#thinking-cant-be-disabled), [forced tool use returns an error](/docs/en/models/opus-5-5/whats-new-opus-5-5#forced-tool-use-is-not-supported), [thinking blocks are tied to the model and the conversation](/docs/en/models/opus-5-5/whats-new-opus-5-5#thinking-blocks-are-tied-to-the-model-that-produced-them), and, on the Claude API and Google Cloud, [the earlier `computer_20251124` computer use tool is not accepted](/docs/en/models/opus-5-5/whats-new-opus-5-5#computer-20251124-is-not-supported). The first three also apply on Claude Fable 5.1. A further change alters the response shape without failing any request: [text between tool calls comes back in `thinking` blocks](/docs/en/models/opus-5-5/whats-new-opus-5-5#text-between-tool-calls) whose text is empty at the default `display` setting. An application that streams that text to its users as progress updates goes quiet between tool calls until it sets a `display` value that returns the text.

[What's new in Claude Opus 5.5](/docs/en/models/opus-5-5/whats-new-opus-5-5)

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-opus-5-5

[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)  
anthropic.claude-opus-5-5

[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)  
claude-opus-5-5

[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)  
claude-opus-5-5

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)  
claude-opus-5-5

### Pricing

Input  
\$4 / MTok

Output  
\$20 / MTok

[5m cache write](/docs/en/build-with-claude/prompt-caching)  
\$5 / MTok

[1h cache write](/docs/en/build-with-claude/prompt-caching)  
\$8 / MTok

[Cache read](/docs/en/build-with-claude/prompt-caching)  
\$0.20 / MTok

[Batch API](/docs/en/build-with-claude/batch-processing)  
50% discount on input and output

Full price list  
[Pricing](/docs/en/about-claude/pricing)

### Capabilities

[Context window](/docs/en/build-with-claude/context-windows)  
1M tokens

Max output  
128K tokens

[Max output (Batch API, beta)](/docs/en/build-with-claude/batch-processing#extended-output-beta)  
300K tokens

[Thinking](/docs/en/build-with-claude/thinking)  
Adaptive (always on)

[Default effort](/docs/en/build-with-claude/effort)  
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

[Status](/docs/en/about-claude/model-deprecations)  
Active (latest)

Released  
September 22, 2026

Retirement  
Not sooner than September 22, 2027

Platforms  
Claude API[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

## Good to know

- Adaptive thinking is always on and can't be turned off. Control thinking depth with the [effort parameter](/docs/en/build-with-claude/effort).
- On the [Message Batches API](/docs/en/build-with-claude/batch-processing#extended-output-beta), Claude Opus 5.5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- The minimum cacheable prompt length is 512 tokens. See [Prompt caching](/docs/en/build-with-claude/prompt-caching#cache-limitations).
- Query limits and capabilities programmatically with the [Models API](/docs/en/api/models/list).

## Resources



[Prompting Claude Opus 5.5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)

Behavioral differences and prompting patterns specific to Claude Opus 5.5.



[Effort](/docs/en/build-with-claude/effort)

The control for thinking depth, latency, and cost. Choose a level per workload.



[Adaptive thinking](/docs/en/build-with-claude/thinking)

How adaptive thinking works and how thinking blocks are preserved.



[Fast mode](/docs/en/build-with-claude/fast-mode)

Lower-latency Claude Opus 5.5 on the Claude API (research preview), priced separately.

## Reference



[System prompt](/docs/en/release-notes/system-prompts/claude-opus-5-5)

The system prompt Claude Opus 5.5 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-opus-5-5-system-card)

Safety evaluations and deployment decisions for Claude Opus 5.5.

[Pricing](/docs/en/about-claude/pricing)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](/docs/en/about-claude/model-deprecations)

Lifecycle status and retirement commitments for every Claude model.
