---
title: "Claude Opus 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:39:46Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fopus-5%2Foverview)

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

Although Claude Opus 5 is still available, you should consider migrating to Claude Opus 5.5 for improved performance.

[See Claude Opus 5.5](/docs/en/models/opus-5-5/overview)

[Models & pricing](/docs/en/models/overview)Legacy models

# Claude Opus 5Legacy

Copy page



claude-opus-5

[Migrate to Claude Opus 5.5](/docs/en/models/opus-5-5/migration-guide#migrating-from-claude-opus-5)

Copy page



[Announcement(opens in new tab)](https://www.anthropic.com/news/claude-opus-5)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$5/ MTok

Output pricing  
\$25/ MTok

## How it compares to the current lineup

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-opus-5

[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)  
anthropic.claude-opus-5

[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)  
claude-opus-5

[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)  
claude-opus-5

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)  
claude-opus-5

### Pricing

Input  
\$5 / MTok

Output  
\$25 / MTok

[5m cache write](/docs/en/build-with-claude/prompt-caching)  
\$6.25 / MTok

[1h cache write](/docs/en/build-with-claude/prompt-caching)  
\$10 / MTok

[Cache read](/docs/en/build-with-claude/prompt-caching)  
\$0.50 / MTok

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

Input → output  
Text and images → text

Reliable knowledge cutoff  
May 2026

Training data cutoff  
May 2026

### Availability

[Status](/docs/en/about-claude/model-deprecations)  
Active (legacy)

Released  
July 24, 2026

Retirement  
Not sooner than July 24, 2027

Platforms  
Claude API[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

## Good to know

- On the [Message Batches API](/docs/en/build-with-claude/batch-processing#extended-output-beta), Claude Opus 5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- The minimum cacheable prompt length is 512 tokens. See [Prompt caching](/docs/en/build-with-claude/prompt-caching#cache-limitations).
- Query limits and capabilities programmatically with the [Models API](/docs/en/api/models/list).

## Resources

[Migrate to Claude Opus 5.5](/docs/en/models/opus-5-5/migration-guide#migrating-from-claude-opus-5)

What changes when moving from Claude Opus 5 to Claude Opus 5.5.



[Claude Opus 5.5](/docs/en/models/opus-5-5/overview)

The current Opus model: overview, specs, and resources.



[Prompting Claude Opus 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)

Model-specific prompting guidance.

## Reference



[System prompt](/docs/en/release-notes/system-prompts/overview#claude-opus-5)

The system prompt Claude Opus 5 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-opus-5-system-card)

Safety evaluations and deployment decisions for Claude Opus 5.

[Pricing](/docs/en/about-claude/pricing)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](/docs/en/about-claude/model-deprecations)

Lifecycle status and retirement commitments for every Claude model.
