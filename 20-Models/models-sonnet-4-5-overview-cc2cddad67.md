---
title: "Claude Sonnet 4.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/sonnet-4-5/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:39:54Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fsonnet-4-5%2Foverview)





SearchCtrlK

Models

[Models overview](/docs/en/models/overview)

[Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

[Claude Opus 5.5](/docs/en/models/opus-5-5/overview)

[Claude Sonnet 5](/docs/en/models/sonnet-5/overview)

[Claude Haiku 4.5](/docs/en/models/haiku-4-5/overview)

Specialized models

Legacy models

[Claude Fable 5](/docs/en/models/fable-5/overview)[Claude Opus 5](/docs/en/models/opus-5/overview)[Claude Opus 4.8](/docs/en/models/opus-4-8/overview)[Claude Opus 4.7](/docs/en/models/opus-4-7/overview)[Claude Opus 4.6](/docs/en/models/opus-4-6/overview)[Claude Sonnet 4.6](/docs/en/models/sonnet-4-6/overview)[Claude Opus 4.5](/docs/en/models/opus-4-5/overview)[Claude Sonnet 4.5](/docs/en/models/sonnet-4-5/overview)

Guides

[Choosing a model](/docs/en/about-claude/models/choosing-a-model)[Optimizing for cost and intelligence](/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)[Upgrade between model versions](/docs/en/about-claude/models/migration-guide)

Lifecycle and reference

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)[Model deprecations](/docs/en/about-claude/model-deprecations)[Model cards](/docs/en/resources/overview)[Pricing](/docs/en/about-claude/pricing)

[System prompts](/docs/en/release-notes/system-prompts/overview)

[Console](/)



Although Claude Sonnet 4.5 is still available, you should consider migrating to Claude Sonnet 5 for improved performance.

[See Claude Sonnet 5](/docs/en/models/sonnet-5/overview)

[Models & pricing](/docs/en/models/overview)Legacy models

# Claude Sonnet 4.5Legacy

Copy page



claude-sonnet-4-5-20250929

[Migrate to Claude Sonnet 5](/docs/en/models/sonnet-5/migration-guide#migrating-from-sonnet-45)

Copy page



[Announcement(opens in new tab)](https://www.anthropic.com/news/claude-sonnet-4-5)

Context window  
200Ktokens

Max output  
64Ktokens

Input pricing  
\$3/ MTok

Output pricing  
\$15/ MTok

## How it compares to the current lineup

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-sonnet-4-5-20250929

Claude API alias  
claude-sonnet-4-5

[Amazon Bedrock (InvokeModel)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)  
anthropic.claude-sonnet-4-5-20250929-v1:0

[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)  
claude-sonnet-4-5@20250929

[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)  
claude-sonnet-4-5

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)  
claude-sonnet-4-5

### Pricing

Input  
\$3 / MTok

Output  
\$15 / MTok

[5m cache write](/docs/en/build-with-claude/prompt-caching)  
\$3.75 / MTok

[1h cache write](/docs/en/build-with-claude/prompt-caching)  
\$6 / MTok

[Cache read](/docs/en/build-with-claude/prompt-caching)  
\$0.30 / MTok

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

Input → output  
Text and images → text

Reliable knowledge cutoff  
Jan 2025

Training data cutoff  
Jul 2025

### Availability

[Status](/docs/en/about-claude/model-deprecations)  
Active (legacy)

Released  
September 29, 2025

Retirement  
Not sooner than September 29, 2026

Platforms  
Claude API[Amazon Bedrock (InvokeModel)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

## Resources

[Migrate to Claude Sonnet 5](/docs/en/models/sonnet-5/migration-guide#migrating-from-sonnet-45)

What changes when moving from Claude Sonnet 4.5 and earlier Sonnet models to Claude Sonnet 5.



[Claude Sonnet 5](/docs/en/models/sonnet-5/overview)

The current Sonnet model: overview, specs, and resources.

## Reference



[System prompt](/docs/en/release-notes/system-prompts/overview#claude-sonnet-4-5)

The system prompt Claude Sonnet 4.5 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-sonnet-4-5-system-card)

Safety evaluations and deployment decisions for Claude Sonnet 4.5.

[Pricing](/docs/en/about-claude/pricing)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](/docs/en/about-claude/model-deprecations)

Lifecycle status and retirement commitments for every Claude model.



[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)

Claude Sonnet 4.5 uses the InvokeModel Bedrock integration and Bedrock-style model IDs.
