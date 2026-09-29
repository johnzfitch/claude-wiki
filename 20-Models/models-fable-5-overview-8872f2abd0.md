---
title: "Claude Fable 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/fable-5/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:39:44Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Ffable-5%2Foverview)

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

Although Claude Fable 5 is still available, you should consider migrating to Claude Fable 5.1 for improved performance.

[See Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

[Models & pricing](/docs/en/models/overview)Legacy models

# Claude Fable 5Legacy

Copy page



claude-fable-5

[Migrate to Claude Fable 5.1](/docs/en/models/fable-5-1/migration-guide#migrating-from-claude-fable-5-to-claude-fable-5-1)

Copy page



[Announcement(opens in new tab)](https://www.anthropic.com/news/claude-fable-5-mythos-5)[What’s new](/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$10/ MTok

Output pricing  
\$50/ MTok

## Fable vs. Mythos

[Claude Mythos 5](/docs/en/models/mythos-5/overview) is offered separately, by invitation only, for defensive cybersecurity workflows as part of [Project Glasswing](https://anthropic.com/glasswing). It shares Claude Fable 5's specifications and pricing; Claude Fable 5 includes safety classifiers that can decline requests, and Claude Mythos 5 does not. For access, contact your Anthropic, AWS, or Google Cloud account team.

## How it compares to the current lineup

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-fable-5

[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)  
anthropic.claude-fable-5

[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)  
claude-fable-5

[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)  
claude-fable-5

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)  
claude-fable-5

### Pricing

Input  
\$10 / MTok

Output  
\$50 / MTok

[5m cache write](/docs/en/build-with-claude/prompt-caching)  
\$12.50 / MTok

[1h cache write](/docs/en/build-with-claude/prompt-caching)  
\$20 / MTok

[Cache read](/docs/en/build-with-claude/prompt-caching)  
\$1 / MTok

[Batch API](/docs/en/build-with-claude/batch-processing)  
50% discount on input and output

[Full price list](/docs/en/about-claude/pricing)

### Capabilities

[Context window](/docs/en/build-with-claude/context-windows)  
1M tokens

Max output  
128K tokens

[Thinking](/docs/en/build-with-claude/thinking)  
Adaptive (always on)

[Default effort](/docs/en/build-with-claude/effort)  
`high`

Input → output  
Text and images → text

Reliable knowledge cutoff  
Jan 2026

Training data cutoff  
Jan 2026

### Availability

[Status](/docs/en/about-claude/model-deprecations)  
Active (legacy)

Released  
June 9, 2026

Retirement  
Not sooner than June 9, 2027

Platforms  
Claude API[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

## Resources

[Migrate to Claude Fable 5.1](/docs/en/models/fable-5-1/migration-guide#migrating-from-claude-fable-5-to-claude-fable-5-1)

What changes when moving from Claude Fable 5 to Claude Fable 5.1.



[Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

The current Fable model: overview, specs, and resources.



[Introducing Claude Fable 5 and Claude Mythos 5](/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5)

Capabilities, API changes, and availability for Claude Fable 5.



[Prompting Claude Fable 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)

Model-specific prompting guidance for long-horizon and agentic work.



[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)

Handle classifier refusals and retry on another Claude model with the `fallbacks` parameter.

## Reference



[System prompt](/docs/en/release-notes/system-prompts/overview#claude-fable-5)

The system prompt Claude Fable 5 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-fable-5-mythos-5-system-card)

Safety evaluations and deployment decisions for Claude Fable 5 and Claude Mythos 5.

[Pricing](/docs/en/about-claude/pricing)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](/docs/en/about-claude/model-deprecations)

Lifecycle status and retirement commitments for every Claude model.
