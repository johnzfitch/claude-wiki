---
title: "Refusals and fallback - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback"
category: "04-API-Reference/Guides"
fetched_at: "2026-08-02T05:40:21Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

Thinking

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Compaction](/docs/en/build-with-claude/compaction)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics (beta)](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

Images and vision

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

MCP tunnels

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[](/login)




Messages

Refusals and fallback

Messages/Building with Claude

# Refusals and fallback




How Claude Fable 5 and Claude Opus 5 return classifier refusals and how to retry refused requests on a fallback model.




Claude Fable 5 and Claude Opus 5 include safety classifiers that can decline a request. When that happens, you receive a normal response, not an error, with `stop_reason: "refusal"`. You can usually still get an answer by sending the same request to another Claude model. This page shows you how to recognize a refusal and how to set up that retry.

Read this page when you build on Claude Fable 5 or Claude Opus 5 and want declined requests to fall through to another model automatically. It also applies when you have just seen `"refusal"` in a response and want to know what to do next.

Related pages:

- [Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons): the full list of `stop_reason` values.
- [Fallback credit](/docs/en/build-with-claude/fallback-credit): how refused requests are billed, and how to avoid paying twice for prompt caching on a retry.
- [SDK middleware](/docs/en/cli-sdks-libraries/middleware): the SDK helper that wraps all of this.
- [Fallback and billing cookbook](https://platform.claude.com/cookbook/fable-5-fallback-billing-guide): a worked end-to-end example.

The simplest setup, in beta on the Claude API: set `fallbacks` to `"default"`, and the API retries a declined request on the fallback model Anthropic recommends for its refusal category. For categories with no recommended fallback, the refusal stands.

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
client = Anthropic()

response = client.beta.messages.create(
    model="claude-fable-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    fallbacks="default",
    betas=["server-side-fallback-2026-07-01"],
)
print(response.model)
```

The following sections cover what a refusal response contains, when to use server-side or client-side fallback, and how each is billed.




What a refusal looks like

A refusal is a successful HTTP 200 response with `stop_reason: "refusal"`:

```python
{
  "id": "msg_01XFUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "model": "claude-fable-5",
  "content": [],
  "stop_reason": "refusal",
  "stop_details": {
    "type": "refusal",
    "category": "cyber",
    "explanation": "This request was declined because it could enable cyber harm."
  },
  "usage": {
    "input_tokens": 412,
    "output_tokens": 0
  }
}
```



The `stop_details` object explains the decline:

- **`category`:** names the policy area that triggered the classifier.
- **`explanation`:** a human-readable description. The text is not stable, so display it rather than parse it.
- Both fields are `null` when the refusal does not map to a named category. That `null` is a normal, permanent value, not a placeholder.
- `stop_details` itself is `null` for every stop reason other than `refusal`.

| `category`               | What it means                                                                                                                                                                                                                             |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `"cyber"`                | The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.                                                                                                    |
| `"bio"`                  | The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.                                                                                                    |
| `"frontier_llm"`         | The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category. |
| `"reasoning_extraction"` | The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](/docs/en/build-with-claude/thinking).                                         |
| `"general_harms"`        | The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.                                                                                                                |

A refusal can arrive before any output, or mid-stream after partial output. In either case, treat any partial output as incomplete and discard it.



**How refusals are billed:** You are not billed for a refusal that arrives before any output. `content` is empty, and token counts appear in `usage` but are not charged. The request still counts against your rate limits. A mid-stream refusal bills the input tokens and the output already streamed at normal rates.




Picking a fallback approach

There are three ways to retry a refused request on another model. The right one depends on where you are running and how much control you need.

| Your situation                       | Use                                                                             | Why                                                         |
|--------------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------|
| Claude API, simplest setup           | [Server-side fallback](#server-side-fallback)                                   | One request, one response. The API handles the retry.       |
| Any platform, using an Anthropic SDK | [The SDK middleware](#client-side-fallback)                                     | Configure once on the client. Retries happen automatically. |
| Raw HTTP or custom retry logic       | Manual retry with [fallback credit](/docs/en/build-with-claude/fallback-credit) | Full control. Fallback credit keeps the cost down.          |

Server-side fallback and the SDK middleware apply fallback credit for you. You only need the [Fallback credit](/docs/en/build-with-claude/fallback-credit) page when you build the retry yourself.




Server-side fallback

Server-side fallback retries a refused request inside a single API call. In the default mode, when the primary model declines and the refusal category has a recommended fallback, the API runs the same request on the model Anthropic recommends for that category. You can instead name up to three fallback models of your own (below). Either way, you get back one response that names the model that answered, so your user gets an answer in one round trip.



Server-side fallback is in beta on the Claude API. The `fallbacks` parameter is not supported on the [Message Batches API](/docs/en/build-with-claude/batch-processing) (a batch item that includes it comes back as an errored result) and is not available on Amazon Bedrock, Google Cloud, or Microsoft Foundry. On those platforms, use [client-side fallback with the SDK middleware](#client-side-fallback) instead.




Making the request

Set the `fallbacks` parameter to the string `"default"` and send the `server-side-fallback-2026-07-01` beta header. The API then applies the requested model's server-defined default routing, which selects a recommended fallback model based on the refusal category the classifier reports, so refused requests are served without you maintaining a model list as recommendations change.

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
client = Anthropic()

response = client.beta.messages.create(
    model="claude-fable-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    fallbacks="default",
    betas=["server-side-fallback-2026-07-01"],
)

# A fallback_message entry in usage.iterations means a fallback model ran;
# pair it with stop_reason to confirm the fallback served the response.
fallback_ran = any(
    iteration.type == "fallback_message"
    for iteration in response.usage.iterations or []
)
served_by_fallback = fallback_ran and response.stop_reason != "refusal"

print(
    json.dumps(
        {
            "stop_reason": response.stop_reason,
            "model": response.model,
            "served_by_fallback": served_by_fallback,
        }
    )
)
```

Anthropic sets safeguards for each model individually and for each policy category, in line with the model's capability: depending on the category, a flagged request may fall back to a less capable model or be declined. The `"default"` mode encodes these per-model, per-category recommendations for you, so a refused request is retried on the model Anthropic recommends for that category. Fallbacks are visible either way: the response names the model that served it, and the `fallback` content block marks the handoff.

The routing is applied server-side and is not published per model on the [Models API](/docs/en/api/models/list). To see which model served a refused request, check the response's top-level `model` field and look for a `fallback_message` entry in `usage.iterations`, as this page's samples do.

Only a safety classifier decline triggers the fallback. A rate limit, overload, or server error on the requested model is returned to you as-is.



The beta header must carry exactly the date `2026-07-01`, which supports both `"default"` and the explicit-list form below, or `2026-06-01`, which accepts only the explicit-list form. Under any other `server-side-fallback-*` value, the `fallbacks` parameter is rejected with a 400 error. If you built against an earlier preview of this feature, update the beta header and the request and response shapes together to the ones on this page.




Naming your own fallback models

Instead of default routing, you can set `fallbacks` to a list of up to three models. When the requested model declines, the API runs the next model in the chain on the same request. Use this form when you want to control exactly which models serve refused requests, such as pinning a model your application has qualified.

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
client = Anthropic()

response = client.beta.messages.create(
    model="claude-fable-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    fallbacks=[{"model": "claude-opus-4-8"}],
    betas=["server-side-fallback-2026-07-01"],
)
print(response.model)
```

A few rules apply to the `fallbacks` list:

- Entries are tried in order. Each must be distinct from the other entries and from the requested model.
- Each entry must be one of the requested model's permitted targets. With the beta header set, that list is published as `allowed_fallback_models` on the model's entry in the [Models API](/docs/en/api/models/list).
- Each entry names a `model` and can override `max_tokens`, `thinking`, `output_config`, and `speed` for that attempt only.
- The request must be valid as a direct request to every model named. If a fallback model does not support a feature the request uses, the API rejects the request up front.
- As with the default mode, only a safety classifier decline triggers the fallback. A rate limit, overload, or server error on the requested model is returned to you as-is.

The explicit-list form also works under the `server-side-fallback-2026-06-01` beta header; the `"default"` mode does not.

The response has the same shape in both modes: the model that served the turn appears in the top-level `model` field, a `fallback` content block marks the handoff, and `usage.iterations` records each attempt.




What the response contains

The response looks like any other message, with two additions:

- The top-level `model` field reports the model that produced the returned message, whether that is the requested model or a fallback.
- A `fallback` content block marks each point in `content` where one model's output gives way to the next: `{"type": "fallback", "from": {"model": ...}, "to": {"model": ...}}`.
  - `from.model` echoes the model string you sent when the declining hop is the requested model.
  - `to.model` is always the resolved ID of the model that continues.

On a refusal before any output, the `fallback` block is the first content block. For example, when default routing selects Claude Opus 4.8 for the refusal's category:

```python
{
  "id": "msg_01XFUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "model": "claude-opus-4-8",
  "content": [
    {
      "type": "fallback",
      "from": { "model": "claude-fable-5" },
      "to": { "model": "claude-opus-4-8" }
    },
    { "type": "text", "text": "Hi! How can I help you today?" }
  ],
  "stop_reason": "end_turn",
  "stop_details": null,
  "usage": {
    "input_tokens": 412,
    "output_tokens": 264,
    "cache_read_input_tokens": 0,
    "cache_creation_input_tokens": 0,
    "iterations": [
      {
        "type": "message",
        "model": "claude-fable-5",
        "input_tokens": 535,
        "output_tokens": 0,
        "cache_read_input_tokens": 0,
        "cache_creation_input_tokens": 0
      },
      {
        "type": "fallback_message",
        "model": "claude-opus-4-8",
        "input_tokens": 412,
        "output_tokens": 264,
        "cache_read_input_tokens": 0,
        "cache_creation_input_tokens": 0
      }
    ]
  }
}
```



The `usage.iterations` array records every attempt. A model that declined appears as an ordinary `message` entry, and the model that served the turn appears as a `fallback_message` entry. If every model in the chain declines, the response is the last model's refusal, with a `message` entry for each earlier hop and a `fallback_message` entry for the last.




Continuing the conversation

On the next turn, send the assistant content back as you received it. After a mid-output fallback, `content` can include block types the declining model produced before the handoff; the following table covers which to keep and which to drop when you echo the turn.

| Block type                                                                             | On the next turn                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fallback`                                                                             | Keep it exactly where it appeared. The API uses its position to validate the thinking blocks around it, so a request that echoes thinking blocks from both sides of the boundary is rejected if the block is omitted or moved. |
| `text`                                                                                 | Keep.                                                                                                                                                                                                                          |
| Any block after the final `fallback` block                                             | Keep.                                                                                                                                                                                                                          |
| `thinking`, `redacted_thinking`, or `connector_text` before the final `fallback` block | Drop.                                                                                                                                                                                                                          |
| Client-side `tool_use` before the final `fallback` block                               | Drop.                                                                                                                                                                                                                          |
| `server_tool_use` before the final `fallback` block                                    | Keep when paired with its result. Drop when it has no matching result.                                                                                                                                                         |



A `connector_text` block carries narration text that some tool-using responses include between tool calls.




Streaming

On a streaming request, the retry happens on the same stream, and nothing you have already received is invalidated. What you see depends on when the decline happens.

**When the decline happens before any output:**

- `message_start` names the fallback model, and the `fallback` block is the first content block.
- Because `message_start` waits for the fallback attempt to start, time to first byte includes the declined attempt.

**When the decline happens mid-output:**

- The open content block closes, and the `fallback` block (an ordinary `content_block_start` and `content_block_stop` pair with no deltas) marks the boundary.
- The fallback model continues from the partial output. Only the partial output's `text` blocks are passed to the fallback model as context; other block types remain in `content`.
- `message_start` already named the requested model, so read the serving model from the `fallback` block's `to.model` and from the `fallback_message` entry in the final `message_delta`'s `usage.iterations`.




Non-streaming responses

On a non-streaming request, a mid-output decline behaves differently: the response omits the declined model's partial output, and the fallback model answers from scratch. The result looks like a decline before any output, with the `fallback` block first. The declined attempt and its output tokens still appear in `usage.iterations`.



**Declines during tool use:** completed tool work does not block fallback. When a decline fires after server tools (for example, web search or code execution) have finished executing within a request, the fallback attempt proceeds: the completed tool results carry over, and the fallback model can keep invoking server tools. The one case that does not retry is a streaming decline that fires while a tool-use block of any type (a client tool, a server tool, or an MCP tool call) is still open on the stream: that refusal is returned directly, and if the `fallback-credit-2026-07-01` header is set it still carries a credit token redeemable by continuing the partial response. Non-streaming requests are unaffected; the API clears the partial work and retries before responding.

### Sticky routing

### How server-side fallback is billed




Client-side fallback with the SDK middleware

Every Anthropic SDK includes a refusal-fallback middleware. You configure it once on the client with your list of fallback models. Calls through `client.beta.messages` then retry refused requests automatically, on any platform. The middleware also sends the `fallback-credit-2026-07-01` beta header on every request it handles, so retries are repriced without per-request setup.




Setting it up

Pass the middleware to the client constructor, and share one `BetaFallbackState` instance across the requests of a conversation.

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
from anthropic import Anthropic, BetaFallbackState, BetaRefusalFallbackMiddleware

# On a refusal, the middleware retries on the listed fallback model and
# automatically sends the fallback-credit beta header on every request it handles.
client = Anthropic(
    middleware=[BetaRefusalFallbackMiddleware([{"model": "claude-opus-4-8"}])],
)

state = BetaFallbackState()  # pins follow-ups to the model that accepted

# Streaming: on a refusal the middleware retries on the fallback model and
# splices its events onto the open stream.
with (
    state,
    client.beta.messages.stream(
        max_tokens=1024,
        model="claude-fable-5",
        messages=[{"role": "user", "content": "Hello, Claude"}],
    ) as stream,
):
    for text in stream.text_stream:
        print(text, end="", flush=True)
    final_message = stream.get_final_message()
print(f"\nserved by: {final_message.model}")

# Non-streaming: reusing the state keeps the conversation pinned.
with state:
    message = client.beta.messages.create(
        max_tokens=1024,
        model="claude-fable-5",
        messages=[{"role": "user", "content": "Hello, Claude"}],
    )
print(f"served by: {message.model}")
```




How it behaves

- Retries walk your fallback list in order. A fallback model that itself refuses passes the request to the next entry.
- When every model in the list has declined, the middleware returns the final refusal (the last model's refusal response) rather than raising an error.
- [Thinking blocks from Claude Fable 5](/docs/en/build-with-claude/thinking#thinking-output-on-claude-fable-5-and-claude-mythos-5) pass through unchanged: each retry re-sends your original request body, and the only blocks the middleware removes from conversation history on later requests are the `fallback` boundary blocks it added itself.
- Responses served through the middleware include a `fallback` content block at each model boundary, the same as server-side fallback responses. The middleware manages those blocks for you on later requests.
- The model that accepted is recorded in `BetaFallbackState`, so follow-up requests that share the state stay pinned to it rather than re-asking a model that refused.



The middleware and the server-side `fallbacks` parameter do the same job. Configure one or the other, never both on the same request. To send a server-side `fallbacks` request from an application that installs the middleware, use a separate client instance without it.

### Writing the retry yourself




Refusals in Message Batches

A refused request in a [Message Batch](/docs/en/build-with-claude/batch-processing) comes back as `result.type: "succeeded"` with `stop_reason: "refusal"`. Batch results carry the same `stop_details` object as synchronous responses, so you can detect refusals through either `stop_reason` or `stop_details.type`. One difference: batch refusals don't mint fallback credits, so `stop_details` on a batch result never includes a `fallback_credit_token`.

Server-side fallback is not available for batches (a batch request that includes `fallbacks` produces a per-item errored result). To retry refused batch items:

1.  Collect the refused items from the results.
2.  Strip Claude Fable 5's thinking blocks from any multi-turn histories.
3.  Resubmit them on a fallback model as a new batch or as direct requests.




Common pitfalls

- **Retry on a different model.** Re-sending a refused request to the same model usually earns another refusal. Point the retry at the fallback model.
- **Budget retries per request, not per turn or per session.** A single turn can produce several refusals, for example an agent plus its sub-agents.
- **Configure fallback on every request path.** Retry handlers, error-recovery branches, and background workers all need it. A handler that re-issues a request without fallback loses the protection on exactly the requests most likely to need it.
- **Give sub-agent calls their own fallback.** The `fallbacks` parameter does not propagate into model calls made from inside tool execution.
- **Make fallback a property of the request, not of ambient state.** A shared flag, cached config value, or global toggle can drift out of sync and silently leave a request unprotected. When you cannot confirm fallback is active, configure it rather than assume it is on.
- **Instrument refusals as their own signal.** A refusal is an HTTP 200, so monitoring built on error rates or 5xx responses never sees it. Emit one event per refusal and one per fallback-served response (the `fallback_message` entry in `usage.iterations` marks the latter), then alert on the gap between the two counts.
- **Branch on `stop_reason` or `stop_details.type`, not on `content` or the inner `stop_details` fields.** The `stop_details` object is always present on a refusal, but its `category` and `explanation` fields can be `null`. Check for `stop_reason` equal to `"refusal"` directly.




Next steps


Fallback credit

Avoid paying the prompt-cache cost twice when you build the retry yourself.




Stop reasons and fallback

Every `stop_reason` value and how to handle it.




SDK middleware

How SDK middleware works, including the refusal-fallback helper.




Migration guide

Move an existing application to Claude Fable 5.
