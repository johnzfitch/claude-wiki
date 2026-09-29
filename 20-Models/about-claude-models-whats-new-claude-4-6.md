---
title: "What's new in Claude 4.6"
source_url: "https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6"
category: "20-Models"
fetched_at: "2026-04-08"
tags: ["models"]
---

# What's new in Claude 4.6

Overview of new features and capabilities in Claude Opus 4.6 and Sonnet 4.6.

---

Claude 4.6 represents the next generation of Claude models, bringing significant new capabilities and API improvements. This page summarizes all new features available at launch.

## New models

| Model | API model ID | Description |
|:------|:-------------|:------------|
| Claude Opus 4.6 | `claude-opus-4-6` | The most intelligent model for building agents and coding |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | The best combination of speed and intelligence |

Claude Opus 4.6 and Sonnet 4.6 both support a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md), extended thinking, and all existing Claude API features. Opus 4.6 offers 128k max output tokens; Sonnet 4.6 offers 64k max output tokens.

For complete pricing and specs, see the [models overview](about-claude-models-overview.md).

## New features

### Adaptive thinking mode

[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking-steering-and-cost.md) (`thinking: {type: "adaptive"}`) is the recommended thinking mode for Opus 4.6 and Sonnet 4.6. Claude dynamically decides when and how much to think. At the default effort level (`high`), Claude almost always thinks. At lower effort levels, it may skip thinking for simpler problems.

`thinking: {type: "enabled"}` and `budget_tokens` are **deprecated** on Opus 4.6 and Sonnet 4.6. They remain functional but will be removed in a future model release. Use adaptive thinking and the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) to control thinking depth instead. Adaptive thinking also automatically enables interleaved thinking.

```python
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=[{"role": "user", "content": "Solve this complex problem..."}],
)
```

### Effort parameter GA

The [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) is now generally available (no beta header required). A new `max` effort level provides the absolute highest capability on Opus 4.6. Combine effort with adaptive thinking for optimal cost-quality tradeoffs.

Sonnet 4.6 introduces the effort parameter to the Sonnet family. Consider setting effort to `medium` for most Sonnet 4.6 use cases to balance speed, cost, and performance.

### Code execution is now free with web tools

[Code execution](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) is now free when used with [web search](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-search-tool.md) or [web fetch](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md). When either tool is included in your API request, there are no additional charges for code execution beyond standard input and output token costs. Code execution enables dynamic filtering in web search and web fetch tools, improving accuracy while reducing token consumption. See the [code execution pricing](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md#usage-and-pricing) for details on standalone usage.

### Improved web search and web fetch with dynamic filtering

[Web search](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-search-tool.md) and [web fetch](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md) tools now support dynamic filtering with Opus 4.6 and Sonnet 4.6. Claude can write and execute code to filter results before they reach the context window, keeping only relevant information and improving accuracy while reducing token consumption. To enable dynamic filtering, use the `web_search_20260209` or `web_fetch_20260209` tool versions.

### Tools graduating to general availability

The following tools are now generally available:
- [Code execution](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) (free with web tools)
- [Web fetch](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)
- [Programmatic tool calling](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)
- [Tool search tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)
- [Tool use examples](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md#providing-tool-use-examples)
- [Memory tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-memory-tool.md)

### Compaction API (beta)

[Compaction](../04-API-Reference/Guides/build-with-claude-compaction.md) provides automatic, server-side context summarization, enabling effectively infinite conversations. When context approaches the window limit, the API automatically summarizes earlier parts of the conversation.

### Fast mode (beta: research preview)

[Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) (`speed: "fast"`) delivers significantly faster output token generation for Opus models. Fast mode is up to 2.5x as fast at premium pricing ($30/$150 per MTok). This is the same model running with faster inference (no change to intelligence or capabilities).

```python
response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[{"role": "user", "content": "Refactor this module..."}],
)
```

### Fine-grained tool streaming (GA)

[Fine-grained tool streaming](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md) is now generally available on all models and platforms. No beta header is required.

### Higher output token limits

Opus 4.6 supports up to 128k output tokens. This enables longer thinking budgets and more comprehensive responses. The SDKs require streaming for requests with large `max_tokens` values to avoid HTTP timeouts. If you don't need to process events incrementally, use `.stream()` with `.get_final_message()` to get the complete response. See [Streaming Messages](../04-API-Reference/Guides/build-with-claude-streaming.md#get-the-final-message-without-handling-events) for details.

On the Message Batches API, Opus 4.6 and Sonnet 4.6 can generate up to 300k output tokens by using the `output-300k-2026-03-24` beta header. See [Batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md#extended-output-beta) for details.

### Data residency controls

[Data residency controls](../04-API-Reference/Guides/build-with-claude-data-residency.md) allow you to specify where model inference runs using the `inference_geo` parameter. You can choose `"global"` (default) or `"us"` routing per request. US-only inference is priced at 1.1x on Claude Opus 4.6 and newer models.

## Deprecations

### `type: "enabled"` and `budget_tokens`

`thinking: {type: "enabled", budget_tokens: N}` is **deprecated** on Opus 4.6 and Sonnet 4.6. It is still functional but no longer recommended and will be removed in a future model release. Migrate to `thinking: {type: "adaptive"}` with the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md).

### `interleaved-thinking-2025-05-14` beta header

The `interleaved-thinking-2025-05-14` beta header is **deprecated** on Opus 4.6. It is safely ignored if included, but is no longer required. [Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking-steering-and-cost.md) automatically enables [interleaved thinking](../04-API-Reference/Guides/build-with-claude-extended-thinking.md#interleaved-thinking). Remove `betas=["interleaved-thinking-2025-05-14"]` from your requests when using Opus 4.6.

On **Sonnet 4.6**, the `interleaved-thinking-2025-05-14` beta header is still functional for use with manual extended thinking (`thinking: {type: "enabled"}`), but manual mode is deprecated. Adaptive thinking is the recommended path and automatically enables interleaved thinking.

### `output_format`

The `output_format` parameter for [structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md) has been moved to `output_config.format`. The old parameter remains functional but is deprecated and will be removed in a future model release.

```python
# Before
response = client.messages.create(
    output_format={"type": "json_schema", "schema": {...}},
    # ...
)

# After
response = client.messages.create(
    output_config={"format": {"type": "json_schema", "schema": {...}}},
    # ...
)
```

## Breaking changes

### Prefill removal

Prefilling assistant messages (last-assistant-turn prefills) is **not supported** on Opus 4.6. Requests with prefilled assistant messages return a 400 error.

**Alternatives:**
- [Structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md) for controlling response format
- System prompt instructions for guiding response style
- [`output_config.format`](../04-API-Reference/Guides/build-with-claude-structured-outputs.md#json-outputs) for JSON output

### Tool parameter quoting

Opus 4.6 may produce slightly different JSON string escaping in tool call arguments (e.g., different handling of Unicode escapes or forward slash escaping). Standard JSON parsers handle these differences automatically. If you parse tool call `input` as a raw string rather than using `json.loads()` or `JSON.parse()`, verify your parsing logic still works.

## Migration guide

For step-by-step migration instructions, see [Migrating to Claude 4.6](about-claude-models-migration-guide.md).

## Next steps

- [Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking-steering-and-cost.md): Learn how to use adaptive thinking mode.
- [Models overview](about-claude-models-overview.md): Compare all Claude models.
- [Compaction](../04-API-Reference/Guides/build-with-claude-compaction.md): Explore server-side context compaction.
- [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md): Faster output token generation for Opus models.
- [Migration guide](about-claude-models-migration-guide.md): Step-by-step migration instructions.
