---
category: "20-Models"
fetched_at: "2026-02-07T10:04:03Z"
source_url: "https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6"
title: "What's new in Claude 4.6 - Claude API Docs"
---

Models & pricing

# What's new in Claude 4.6

Copy page

Overview of new features and capabilities in Claude Opus 4.6.

Copy page

Claude 4.6 represents the next generation of Claude models, bringing significant new capabilities and API improvements. This page summarizes all new features available at launch.

## 

New models

| Model | API model ID | Description |
|----|----|----|
| Claude Opus 4.6 | `claude-opus-4-6` | Our most intelligent model for building agents and coding |

Claude Opus 4.6 supports a 200K context window (with [1M token context window](/docs/en/build-with-claude/context-windows#1m-token-context-window) available in beta), 128K max output tokens, extended thinking, and all existing Claude API features.

For complete pricing and specs, see the [models overview](/docs/en/about-claude/models/overview).

## 

New features

### 

Adaptive thinking mode

[Adaptive thinking](/docs/en/build-with-claude/adaptive-thinking) (`thinking: {type: "adaptive"}`) is the recommended thinking mode for Opus 4.6. Claude dynamically decides when and how much to think. At the default effort level (`high`), Claude will almost always think. At lower effort levels, it may skip thinking for simpler problems.

`thinking: {type: "enabled"}` and `budget_tokens` are **deprecated** on Opus 4.6. They remain functional but will be removed in a future model release. Use adaptive thinking and the [effort parameter](/docs/en/build-with-claude/effort) to control thinking depth instead. Adaptive thinking also automatically enables interleaved thinking.

``` shiki
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=[{"role": "user", "content": "Solve this complex problem..."}]
)
```

### 

Effort parameter GA

The [effort parameter](/docs/en/build-with-claude/effort) is now generally available (no beta header required). A new `max` effort level provides the absolute highest capability on Opus 4.6. Combine effort with adaptive thinking for optimal cost-quality tradeoffs.

### 

Compaction API (beta)

[Compaction](/docs/en/build-with-claude/compaction) provides automatic, server-side context summarization, enabling effectively infinite conversations. When context approaches the window limit, the API automatically summarizes earlier parts of the conversation.

### 

Fine-grained tool streaming (GA)

[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming) is now generally available on all models and platforms. No beta header is required.

### 

128K output tokens

Opus 4.6 supports up to 128K output tokens, doubling the previous 64K limit. This enables longer thinking budgets and more comprehensive responses. The SDKs require streaming for requests with large `max_tokens` values to avoid HTTP timeouts. If you don't need to process events incrementally, use `.stream()` with `.get_final_message()` to get the complete response — see [Streaming Messages](/docs/en/build-with-claude/streaming#get-the-final-message-without-handling-events) for details.

### 

Data residency controls

[Data residency controls](/docs/en/build-with-claude/data-residency) allow you to specify where model inference runs using the `inference_geo` parameter. You can choose `"global"` (default) or `"us"` routing per request. US-only inference is priced at 1.1x on Claude Opus 4.6 and newer models.

## 

Deprecations

### 

`type: "enabled"` and `budget_tokens`

`thinking: {type: "enabled", budget_tokens: N}` is **deprecated** on Opus 4.6. It remains functional but will be removed in a future model release. Migrate to `thinking: {type: "adaptive"}` with the [effort parameter](/docs/en/build-with-claude/effort).

### 

`interleaved-thinking-2025-05-14` beta header

The `interleaved-thinking-2025-05-14` beta header is **deprecated** on Opus 4.6. It is safely ignored if included, but is no longer required. [Adaptive thinking](/docs/en/build-with-claude/adaptive-thinking) automatically enables [interleaved thinking](/docs/en/build-with-claude/extended-thinking#interleaved-thinking). Remove `betas=["interleaved-thinking-2025-05-14"]` from your requests when using Opus 4.6.

### 

`output_format`

The `output_format` parameter for [structured outputs](/docs/en/build-with-claude/structured-outputs) has been moved to `output_config.format`. The old parameter remains functional but is deprecated and will be removed in a future model release.

``` shiki
# Before
response = client.messages.create(
    output_format={"type": "json_schema", "schema": {...}},
    ...
)

# After
response = client.messages.create(
    output_config={"format": {"type": "json_schema", "schema": {...}}},
    ...
)
```

## 

Breaking changes

### 

Prefill removal

Prefilling assistant messages (last-assistant-turn prefills) is **not supported** on Opus 4.6. Requests with prefilled assistant messages return a 400 error.

**Alternatives:**

- [Structured outputs](/docs/en/build-with-claude/structured-outputs) for controlling response format
- System prompt instructions for guiding response style
- [`output_config.format`](/docs/en/build-with-claude/structured-outputs#json-outputs) for JSON output

### 

Tool parameter quoting

Opus 4.6 may produce slightly different JSON string escaping in tool call arguments (e.g., different handling of Unicode escapes or forward slash escaping). Standard JSON parsers handle these differences automatically. If you parse tool call `input` as a raw string rather than using `json.loads()` or `JSON.parse()`, verify your parsing logic still works.

## 

Migration guide

For step-by-step migration instructions, see [Migrating to Claude 4.6](/docs/en/about-claude/models/migration-guide).

## 

Next steps

[](/docs/en/build-with-claude/adaptive-thinking)

Adaptive thinking

Learn how to use adaptive thinking mode.

[](/docs/en/about-claude/models/overview)

Models overview

Compare all Claude models.

[](/docs/en/build-with-claude/compaction)

Compaction

Explore server-side context compaction.

[](/docs/en/about-claude/models/migration-guide)

Migration guide

Step-by-step migration instructions.

Was this page helpful?

- 

- [New models](#new-models)

- [New features](#new-features)

- [Adaptive thinking mode](#adaptive-thinking-mode)

- [Effort parameter GA](#effort-parameter-ga)

- [Compaction API (beta)](#compaction-api-beta)

- [Fine-grained tool streaming (GA)](#fine-grained-tool-streaming-ga)

- [128K output tokens](#128-k-output-tokens)

- [Data residency controls](#data-residency-controls)

- [Deprecations](#deprecations)

- [type: "enabled" and budget_tokens](#type-enabled-and-budget-tokens)

- [interleaved-thinking-2025-05-14 beta header](#interleaved-thinking-2025-05-14-beta-header)

- [output_format](#output-format)

- [Breaking changes](#breaking-changes)

- [Prefill removal](#prefill-removal)

- [Tool parameter quoting](#tool-parameter-quoting)

- [Migration guide](#migration-guide)

- [Next steps](#next-steps)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
