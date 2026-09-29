---
title: "Claude Fable 5.1 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/fable-5-1/overview"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Ffable-5-1%2Foverview)





SearchCtrlK

Models

[Models overview](/docs/en/models/overview)

[Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

[Overview](/docs/en/models/fable-5-1/overview)[What's new](/docs/en/models/fable-5-1/whats-new-fable-5-1)[Migration guide](/docs/en/models/fable-5-1/migration-guide)

[Claude Opus 5.5](/docs/en/models/opus-5-5/overview)

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

# Claude Fable 5.1Latest

For demanding reasoning and long-horizon agentic work

Copy page



claude-fable-5-1

[Try in playground](/playground?model=claude-fable-5-1)

Copy page



[Announcement(opens in new tab)](https://www.anthropic.com/claude-fable-and-mythos-5-1)[What’s new](/docs/en/models/fable-5-1/whats-new-fable-5-1)[Migration guide](/docs/en/models/fable-5-1/migration-guide)

Context window  
1Mtokens

Max output  
128Ktokens

Input pricing  
\$10/ MTok

Output pricing  
\$50/ MTok

## Overview

Claude Fable 5.1 extends Claude Fable 5 at the same input and output prices, with cache reads at a quarter of the cost, and brings stronger long-running agentic coding, multistep research, and document, spreadsheet, and slide work. For most workloads, start with Claude Opus 5 (see [Choosing a model](/docs/en/about-claude/models/choosing-a-model)). Use Claude Fable 5.1 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5 at higher effort still fall short. Claude Mythos 5.1 offers the same capabilities to [Project Glasswing](https://anthropic.com/glasswing) participants only.

If you already call Claude Fable 5, three changes are breaking: [forced tool use returns an error](/docs/en/models/fable-5-1/whats-new-fable-5-1#forced-tool-use-is-not-supported), [earlier models can't read its thinking blocks](/docs/en/models/fable-5-1/whats-new-fable-5-1#thinking-blocks-are-tied-to-the-model-that-produced-them), and [editing earlier turns invalidates thinking blocks](/docs/en/models/fable-5-1/whats-new-fable-5-1#editing-earlier-turns-invalidates-thinking-blocks). Five are additive: [per-message effort](/docs/en/models/fable-5-1/whats-new-fable-5-1#change-effort-mid-conversation-beta) (beta), [turn-scoped system messages](/docs/en/models/fable-5-1/whats-new-fable-5-1#turn-scoped-system-messages-beta) (beta), [readable progress updates between tool calls](/docs/en/models/fable-5-1/whats-new-fable-5-1#progress-updates-between-tool-calls-beta) (`display: "updates"`, beta), a [lower cache read price](/docs/en/models/fable-5-1/whats-new-fable-5-1#pricing), and [content provenance](/docs/en/models/fable-5-1/whats-new-fable-5-1#content-provenance).

[What's new in Claude Fable 5.1](/docs/en/models/fable-5-1/whats-new-fable-5-1)

## Claude Fable 5.1 and Claude Mythos 5.1

[Claude Mythos 5.1](/docs/en/models/mythos-5-1/overview) offers the same capabilities by invitation only, as part of [Project Glasswing](https://anthropic.com/glasswing). It shares Claude Fable 5.1's specifications and pricing. For access, contact your Anthropic, AWS, or Google Cloud account team.

## How it compares

[TABLE]

## Specifications

### Model IDs

Claude API  
claude-fable-5-1

[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)  
anthropic.claude-fable-5-1

[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)  
claude-fable-5-1

[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)  
claude-fable-5-1

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)  
claude-fable-5-1

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
\$0.25 / MTok

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

Comparative latency  
Slower

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
September 1, 2026

Retirement  
Not sooner than September 1, 2027

Platforms  
Claude API[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

## Resources



[Prompting Claude Fable 5.1](/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)

Model-specific prompting guidance for long-horizon and agentic work.



[Migrating to Claude Fable 5.1](/docs/en/models/fable-5-1/migration-guide)

What changes when you move from Claude Fable 5, Claude Opus 5, or Claude Opus 4.8.



[Preserved thinking](/docs/en/build-with-claude/thinking#preserved-thinking)

When this model's thinking blocks stay usable: across model switches and across changes to the conversation.



[Per-message effort](/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta)

Change the effort level partway through a conversation without invalidating the prompt cache.



[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)

Handle classifier refusals and retry on another Claude model.



[Adaptive thinking](/docs/en/build-with-claude/thinking)

The only thinking mode on Claude Fable 5.1. Steer depth with `effort`.

## Reference



[System prompt](/docs/en/release-notes/system-prompts/claude-fable-5-1)

The system prompt Claude Fable 5.1 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card)

Safety evaluations and deployment decisions for Claude Fable 5.1 and Claude Mythos 5.1.

[Pricing](/docs/en/about-claude/pricing)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](/docs/en/about-claude/model-deprecations)

Lifecycle status and retirement commitments for every Claude model.
