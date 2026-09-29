---
title: "Claude Haiku 4.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/haiku-4-5/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:39:53Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fhaiku-4-5%2Foverview)





SearchCtrlK

Models

[Models overview](/docs/en/models/overview)

[Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

[Claude Opus 5.5](/docs/en/models/opus-5-5/overview)

[Claude Sonnet 5](/docs/en/models/sonnet-5/overview)

[Claude Haiku 4.5](/docs/en/models/haiku-4-5/overview)

[Overview](/docs/en/models/haiku-4-5/overview)[Migration guide](/docs/en/models/haiku-4-5/migration-guide)

Specialized models

Legacy models

Guides

[Choosing a model](/docs/en/about-claude/models/choosing-a-model)[Optimizing for cost and intelligence](/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)[Upgrade between model versions](/docs/en/about-claude/models/migration-guide)

Lifecycle and reference

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)[Model deprecations](/docs/en/about-claude/model-deprecations)[Model cards](/docs/en/resources/overview)[Pricing](/docs/en/about-claude/pricing)

[System prompts](/docs/en/release-notes/system-prompts/overview)

[Console](/)

[Models & pricing](/docs/en/models/overview)Models

# Claude Haiku 4.5Latest

The fastest model with near-frontier intelligence

Copy page



claude-haiku-4-5-20251001

[Try in playground](/playground?model=claude-haiku-4-5-20251001)

Copy page



[Announcement(opens in new tab)](https://www.anthropic.com/news/claude-haiku-4-5)[Migration guide](/docs/en/models/haiku-4-5/migration-guide)

Context window  
200Ktokens

Max output  
64Ktokens

Input pricing  
\$1/ MTok

Output pricing  
\$5/ MTok

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-haiku-4-5-20251001

Claude API alias  
claude-haiku-4-5

[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)  
anthropic.claude-haiku-4-5

[Amazon Bedrock (InvokeModel)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)  
anthropic.claude-haiku-4-5-20251001-v1:0

[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)  
claude-haiku-4-5@20251001

[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)  
claude-haiku-4-5

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)  
claude-haiku-4-5

### Pricing

Input  
\$1 / MTok

Output  
\$5 / MTok

[5m cache write](/docs/en/build-with-claude/prompt-caching)  
\$1.25 / MTok

[1h cache write](/docs/en/build-with-claude/prompt-caching)  
\$2 / MTok

[Cache read](/docs/en/build-with-claude/prompt-caching)  
\$0.10 / MTok

[Batch API](/docs/en/build-with-claude/batch-processing)  
50% discount on input and output

[Full price list](/docs/en/about-claude/pricing)

### Capabilities

[Context window](/docs/en/build-with-claude/context-windows)  
200K tokens

Max output  
64K tokens

[Thinking](/docs/en/build-with-claude/thinking)  
Extended

[Default effort](/docs/en/build-with-claude/effort)  
Not supported

Comparative latency  
Fastest

Input → output  
Text and images → text

Reliable knowledge cutoff  
Feb 2025

Training data cutoff  
Jul 2025

### Availability

[Status](/docs/en/about-claude/model-deprecations)  
Active (latest)

Released  
October 15, 2025

Retirement  
Not sooner than October 15, 2026

Platforms  
Claude API[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (InvokeModel)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

## Good to know

- `claude-haiku-4-5` is a convenience alias that resolves to the pinned snapshot `claude-haiku-4-5-20251001`. See [Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions).
- Claude Haiku 4.5 uses manual extended thinking (`thinking.type: "enabled"`), not adaptive thinking.
- Query limits and capabilities programmatically with the [Models API](/docs/en/api/models/list).

## Resources



[Extended thinking](/docs/en/build-with-claude/extended-thinking)

Claude Haiku 4.5 supports manual extended thinking with `budget_tokens`.



[Choosing a model](/docs/en/about-claude/models/choosing-a-model)

When to start efficiency-first with Haiku and when to reach for a larger model.



[Reduce latency](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)

Techniques that pair well with the fastest model in the lineup.

## Reference



[System prompt](/docs/en/release-notes/system-prompts/overview#claude-haiku-4-5)

The system prompt Claude Haiku 4.5 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-haiku-4-5-system-card)

Safety evaluations and deployment decisions for Claude Haiku 4.5.

[Pricing](/docs/en/about-claude/pricing)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](/docs/en/about-claude/model-deprecations)

Lifecycle status and retirement commitments for every Claude model.



[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)

Claude Haiku 4.5 is also available through the InvokeModel Bedrock integration and Bedrock-style model IDs.
