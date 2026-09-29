---
title: "Cache diagnostics - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:28Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcache-diagnostics)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](build-with-claude-overview.md)[Using the Messages API](build-with-claude-working-with-messages.md)[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)[Refusals and fallback](build-with-claude-refusals-and-fallback.md)[Fallback credit](build-with-claude-fallback-credit.md)

Model capabilities

[Effort](build-with-claude-effort.md)[Task budgets (beta)](build-with-claude-task-budgets.md)[Fast mode (research preview)](build-with-claude-fast-mode.md)[Structured outputs](build-with-claude-structured-outputs.md)[Citations](build-with-claude-citations.md)[Streaming Messages](build-with-claude-streaming.md)[Batch processing](build-with-claude-batch-processing.md)[Search results](build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](build-with-claude-multilingual-support.md)[Embeddings](build-with-claude-embeddings.md)

[Thinking](build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

[Compaction](build-with-claude-compaction.md)

Working with files

[Files API](build-with-claude-files.md)[PDF support](build-with-claude-pdf-support.md)

[Images and vision](build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)[Google Cloud](build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Context management

# Cache diagnostics

Copy page



Diagnose unexpected prompt cache misses by comparing consecutive requests and identifying exactly where the prompt prefix diverged.

Copy page



Cache diagnostics

[ZDR](../Other/manage-claude-api-and-data-retention.md)

Eligible

excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

[Prompt caching](build-with-claude-prompt-caching.md) cuts latency and cost significantly, but only when the beginning of your prompt is byte-for-byte identical to a recent request. A reordered tool, a timestamp interpolated into your system prompt, or an edit to an earlier message can silently invalidate the cache. Without cache diagnostics, the only signal is `usage.cache_read_input_tokens` dropping to zero, with no indication of what changed.

Cache diagnostics closes that gap. Pass the `id` of your previous response, and the API compares the two requests and tells you where they diverged (the model, the system prompt, the tools, or the message history) so you can fix the root cause instead of guessing.

## How cache diagnostics works

For each request that includes the `diagnostics` object, the API stores a lightweight fingerprint keyed by the response `id`. It stores nothing for requests that omit the object. On your next request, include the previous response's `id` as `diagnostics.previous_message_id`. The API rebuilds the fingerprint for the new request, compares it against the stored one, and attaches a `diagnostics` object to the response describing the first point of divergence.

The comparison is about request structure, independent of whether the cache actually hit. See [Reading diagnostics alongside usage](#reading-diagnostics-alongside-usage) for how to combine the `diagnostics` result with `usage.cache_read_input_tokens`.

Fingerprints contain only hashes and token-count estimates (never raw prompt content), are retained for a limited time, are scoped to your organization and workspace, and are not used for any other purpose.

## Basic usage

Include the `diagnostics` object on every turn. The object is the opt-in: the API stores a fingerprint only for requests that include it. On the first turn, pass `"previous_message_id": null` to opt in without a prior message to compare against. On subsequent turns, pass the `id` from the previous response. The `cache-diagnosis-2026-04-07` beta header is no longer required, and requests that still send it work as before.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

SYSTEM = "You are an AI assistant analyzing a large document. <document>...</document>"

# Turn 1: opt in with previous_message_id=None
r1 = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},
    system=SYSTEM,
    messages=[{"role": "user", "content": "Summarize section 1."}],
    diagnostics={"previous_message_id": None},
)

# Turn 2: reference the previous response id
r2 = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},
    system=SYSTEM,
    messages=[
        {"role": "user", "content": "Summarize section 1."},
        {"role": "assistant", "content": r1.content},
        {"role": "user", "content": "Now summarize section 2."},
    ],
    diagnostics={"previous_message_id": r1.id},
)

diagnostics = r2.diagnostics
if diagnostics is None:
    print("No divergence detected.")
elif diagnostics.cache_miss_reason is None:
    print("Comparison still pending.")
else:
    print(f"cache_miss_reason: {diagnostics.cache_miss_reason.type}")
```

## Streaming

In streaming responses, `diagnostics` appears on the `message_start` event.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
# Turn 2: stream, referencing the previous response id
with client.beta.messages.stream(
    model="claude-opus-5-5",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},
    system=SYSTEM,
    messages=[
        {"role": "user", "content": "Summarize section 1."},
        {"role": "assistant", "content": r1.content},
        {"role": "user", "content": "Now summarize section 2."},
    ],
    diagnostics={"previous_message_id": r1.id},
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    print()
    r2 = stream.get_final_message()

diagnostics = r2.diagnostics
if diagnostics is None:
    print("No divergence detected.")
elif diagnostics.cache_miss_reason is None:
    print("Comparison still pending.")
else:
    print(f"cache_miss_reason: {diagnostics.cache_miss_reason.type}")
```

The `message_start` event carries the full `diagnostics` field; see [Response format](#response-format) for the possible values.

## Threading diagnostics through a conversation loop

In a multi-turn conversation, carry the latest response `id` forward as `previous_message_id` on every turn. The first iteration passes `null` to opt in; each subsequent iteration passes the `id` from the previous response.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

```python
client = anthropic.Anthropic()

SYSTEM = "You are an AI assistant analyzing a large document. <document>...</document>"

messages = []
prev_id = None

for i, user_message in enumerate(
    ["Summarize section 1.", "Now section 2.", "Now section 3."]
):
    messages.append({"role": "user", "content": user_message})

    r = client.beta.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        cache_control={"type": "ephemeral"},
        system=SYSTEM,
        messages=messages,
        diagnostics={"previous_message_id": prev_id},
    )

    if r.diagnostics is not None and r.diagnostics.cache_miss_reason is not None:
        print(f"Turn {i + 1} cache_miss_reason: {r.diagnostics.cache_miss_reason.type}")

    messages.append({"role": "assistant", "content": r.content})
    prev_id = r.id
```



## Response format

The `diagnostics` field on the response `Message` has three possible values:

| Value                          | Meaning                                                                                                                                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `null`                         | The request did not include the `diagnostics` object, `previous_message_id` was `null` (first turn, nothing to compare), or a comparison ran and found no divergence.                           |
| `{"cache_miss_reason": null}`  | The comparison was still running when the response was serialized. This can happen when the response starts very quickly. Treat it as inconclusive and check the next turn.                     |
| `{"cache_miss_reason": {...}}` | A `cache_miss_reason` is attached. For `*_changed` types this identifies the first divergence point; `previous_message_not_found` and `unavailable` are cases where no comparison was produced. |

When `cache_miss_reason` is non-null, it looks like this:

```python
{
  "id": "msg_01Xyz...",
  "type": "message",
  "role": "assistant",
  "content": [{ "type": "text", "text": "..." }],
  "usage": {
    "input_tokens": 42,
    "cache_read_input_tokens": 0,
    "cache_creation_input_tokens": 41850,
    "output_tokens": 210
  },
  "diagnostics": {
    "cache_miss_reason": {
      "type": "system_changed",
      "cache_missed_input_tokens": 41850
    }
  }
}
```



## Cache miss reason types

`cache_miss_reason` is a discriminated union on `type`. The response reports the earliest divergence only, so fix it first; later ones may be hidden behind it.

| Type                         | What it means                                                                                                                                                                                                                                                                                                                                                                                                                                   | What to change                                                                                                                                                                                                                                                                     |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `model_changed`              | The `model` differs from the previous request (for example, a router, A/B test, or fallback selected a different model). The cache is per-model.                                                                                                                                                                                                                                                                                                | Hold the model constant within a cached conversation.                                                                                                                                                                                                                              |
| `system_changed`             | The `system` parameter differs. Typically a timestamp, request ID, or other per-request value was interpolated into the system prompt.                                                                                                                                                                                                                                                                                                          | Make the system prompt a byte-stable constant and move dynamic data into the first `user` message after your cache breakpoint.                                                                                                                                                     |
| `tools_changed`              | The `tools` array differs: tools were added, removed, or reordered between turns, or tool `input_schema` JSON was serialized non-deterministically.                                                                                                                                                                                                                                                                                             | Send the same tool list on every turn in a fixed order with deterministically serialized schemas (for example, sort keys).                                                                                                                                                         |
| `messages_changed`           | The model, system, and tools all match, but an earlier entry in `messages` was altered, reordered, or removed rather than appended to. Typically conversation history was truncated or edited, or assistant turns and `tool_result` blocks were re-serialized differently on resend.                                                                                                                                                            | Treat the history as append-only; echo assistant `content` and tool results back verbatim.                                                                                                                                                                                         |
| `previous_message_not_found` | No stored fingerprint exists for the supplied `previous_message_id`. This is not evidence that your request changed. Typically the previous request did not include the `diagnostics` object, it came from a different workspace, or too much time has passed since it was sent.                                                                                                                                                                | Include the `diagnostics` object on every turn and keep consecutive turns close together in time.                                                                                                                                                                                  |
| `unavailable`                | Diagnostic information was not available for this request. This includes the case where `model`, `system`, and `tools` match but another prompt-affecting request parameter (`tool_choice`, `thinking`, `context_management`, `output_config`, `output_format`, or the set of active `anthropic-beta` headers) differs, and very long conversations where the divergence is beyond the comparison horizon. Your request was processed normally. | Keep the prompt-affecting request parameters constant for the lifetime of a cached conversation. If persistent, apply the manual checks under [Troubleshooting common issues](build-with-claude-prompt-caching.md#troubleshooting-common-issues) on the prompt caching page. |



The four `*_changed` types also carry a `cache_missed_input_tokens` integer: an estimate of how many input tokens fell after the divergence point, giving you a sense of how much cacheable prefix was lost. It is derived from byte lengths before tokenization, so treat it as a magnitude indicator rather than a billing number. It can differ from (and occasionally exceed) `usage.input_tokens`.

## Reading diagnostics alongside usage

`diagnostics` answers "did my request change?" while `usage.cache_read_input_tokens` answers "did the cache hit?". Combining them tells you where to look.

This matrix applies to turns where you passed a real `previous_message_id`. On the first turn (`previous_message_id: null`), `diagnostics` is always `null` and `cache_read_input_tokens` is normally zero because the cache is being written, not read; no troubleshooting is needed. The matrix also does not apply when `cache_miss_reason` is `null` (the comparison is still pending; check the next turn) or when its `type` is `previous_message_not_found` or `unavailable` (no comparison was produced).

| Diagnostics result                        | Cache read tokens | Interpretation                                                                                                                                                                                            |
|-------------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `null`                                    | high              | Working as expected. Your prefix is stable and the cache hit.                                                                                                                                             |
| `null`                                    | low or zero       | Your requests match but the cache entry was no longer available. Consider shortening gaps between turns or using the [1-hour cache TTL](build-with-claude-prompt-caching.md#1-hour-cache-duration). |
| `cache_miss_reason` is a `*_changed` type | low or zero       | Your bug. The request changed; fix the cause indicated by `type`.                                                                                                                                         |
| `cache_miss_reason` is a `*_changed` type | high              | Rare. A change occurred late in the prompt but an earlier `cache_control` breakpoint still hit. Worth fixing, but low impact.                                                                             |

## Limitations

- **Claude API only:** Not available on Amazon Bedrock or Google Cloud.
- **Limited retention:** Fingerprints for `previous_message_id` lookup expire after a short period. Run diagnostic comparisons between closely spaced requests.
- **Same workspace:** The previous request must have run in the same organization and workspace. To check, compare the `anthropic-workspace-id` [response header](../Endpoints/overview.md#response-headers) on the two responses.
- **Comparison horizon:** For very long conversations where the only change is deep in the message list, the response may be `unavailable` rather than a precise location.
- **Best-effort:** Diagnostics never blocks or fails your request. If diagnostic information is not available, the response returns `unavailable`, or `cache_miss_reason: null` when the comparison was still running.

## Data retention

Cache diagnostics is ZDR eligible (qualified). Anthropic does not store the raw text of your prompts or Claude's outputs for this feature.

The API stores a fingerprint only for requests that include the `diagnostics` object. The fingerprint consists only of cryptographic hashes and token-count estimates, keyed by the response `id` and scoped to your organization and workspace. Fingerprints expire after a short period and are not used for any other purpose.

For ZDR eligibility across all features, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

## See also

- [Prompt caching](build-with-claude-prompt-caching.md)
- [Token counting](build-with-claude-token-counting.md)

## Compatibility

Supported platforms  
- Claude API
