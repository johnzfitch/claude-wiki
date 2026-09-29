---
title: "Claude Sonnet 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/sonnet-5/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:39:45Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fsonnet-5%2Foverview)





SearchCtrlK

Models

[Models overview](/docs/en/models/overview)

[Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

[Claude Opus 5.5](/docs/en/models/opus-5-5/overview)

[Claude Sonnet 5](/docs/en/models/sonnet-5/overview)

[Overview](/docs/en/models/sonnet-5/overview)[What's new](/docs/en/models/sonnet-5/whats-new-sonnet-5)[Migration guide](/docs/en/models/sonnet-5/migration-guide)

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

# Claude Sonnet 5Latest

The best combination of speed and intelligence

Copy page



claude-sonnet-5

[Try in playground](/playground?model=claude-sonnet-5)

Copy page



[Announcement(opens in new tab)](https://www.anthropic.com/news/claude-sonnet-5)[What’s new](/docs/en/models/sonnet-5/whats-new-sonnet-5)[Migration guide](/docs/en/models/sonnet-5/migration-guide)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$2/ MTok

Output pricing  
\$10/ MTok

## Overview

Claude Sonnet 5 is the next generation of Anthropic's Sonnet model family. It is a drop-in upgrade for Claude Sonnet 4.6 with three behavior changes: [adaptive thinking](/docs/en/build-with-claude/thinking) is on by default, manual extended thinking now returns a 400 error (it was deprecated on Claude Sonnet 4.6), and setting sampling parameters (`temperature`, `top_p`, `top_k`) to non-default values returns a 400 error. This page summarizes everything new at launch, including a new tokenizer.

[What's new in Claude Sonnet 5](/docs/en/models/sonnet-5/whats-new-sonnet-5)

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-sonnet-5

[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)  
anthropic.claude-sonnet-5

[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)  
claude-sonnet-5

[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)  
claude-sonnet-5

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)  
claude-sonnet-5

### Pricing

Input  
\$2 / MTok

Output  
\$10 / MTok

[5m cache write](/docs/en/build-with-claude/prompt-caching)  
\$2.50 / MTok

[1h cache write](/docs/en/build-with-claude/prompt-caching)  
\$4 / MTok

[Cache read](/docs/en/build-with-claude/prompt-caching)  
\$0.20 / MTok

[Batch API](/docs/en/build-with-claude/batch-processing)  
50% discount on input and output

[Full price list](/docs/en/about-claude/pricing)

### Capabilities

[Context window](/docs/en/build-with-claude/context-windows)  
1M tokens

Max output  
128K tokens

[Max output (Batch API, beta)](/docs/en/build-with-claude/batch-processing#extended-output-beta)  
300K tokens

[Thinking](/docs/en/build-with-claude/thinking)  
Adaptive

[Default effort](/docs/en/build-with-claude/effort)  
`high`

Comparative latency  
Fast

Input → output  
Text and images → text

Reliable knowledge cutoff  
Jan 2026

Training data cutoff  
Jan 2026

### Availability

[Status](/docs/en/about-claude/model-deprecations)  
Active (latest)

Released  
June 30, 2026

Retirement  
Not sooner than June 30, 2027

Platforms  
Claude API[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

## Good to know

- On the [Message Batches API](/docs/en/build-with-claude/batch-processing#extended-output-beta), Claude Sonnet 5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- Setting `temperature`, `top_p`, or `top_k` to non-default values returns a 400 error. See [What's new in Claude Sonnet 5](/docs/en/models/sonnet-5/whats-new-sonnet-5#sampling-parameters-not-accepted).
- Query limits and capabilities programmatically with the [Models API](/docs/en/api/models/list).

## Resources



[Prompting Claude Sonnet 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)

Model-specific prompting guidance.



[Adaptive thinking](/docs/en/build-with-claude/thinking)

On by default on Claude Sonnet 5. Steer depth with `effort`.



[Effort](/docs/en/build-with-claude/effort)

Effort defaults to `high` on the Claude API and Claude Code. Choose a level per workload.



[Context windows](/docs/en/build-with-claude/context-windows)

1M tokens by default. How the window is counted and managed.

## Reference



[System card](https://www.anthropic.com/claude-sonnet-5-system-card)

Safety evaluations and deployment decisions for Claude Sonnet 5.

[Pricing](/docs/en/about-claude/pricing)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](/docs/en/about-claude/model-deprecations)

Lifecycle status and retirement commitments for every Claude model.
