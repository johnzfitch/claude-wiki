---
title: "Refusals and fallback - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:35Z"
tags: ["api", "cli", "sdk"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Frefusals-and-fallback)

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

[Messages](../../01-Getting-Started/intro.md)Building with Claude

# Refusals and fallback

Copy page



How Claude Fable and Claude Opus models return classifier refusals and how to retry refused requests on a fallback model.

Copy page



Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, and Claude Opus 5 include safety classifiers that can decline a request. When that happens, you receive a normal response, not an error, with `stop_reason: "refusal"`. Its `stop_details.category` names the policy area (see [What a refusal looks like](#refusal-response)). You can usually still get an answer by sending the same request to another Claude model. This page shows you how to recognize a refusal and how to set up that retry.

Read this page when you build on any of these models and want declined requests to fall through to another model automatically. It also applies when you have seen `"refusal"` in a response and want to know what to do next.

Related pages:

- [Stop reasons and fallback](build-with-claude-handling-stop-reasons.md): the full list of `stop_reason` values.
- [Fallback credit](build-with-claude-fallback-credit.md): how to avoid paying the prompt-cache cost twice when you build the retry yourself.
- [SDK middleware](../Other/cli-sdks-libraries-middleware.md): the SDK helper that wraps all of this.
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

## What a refusal looks like

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
- **`recommended_model`:** present only on requests that set `fallbacks` ([server-side fallback](#server-side-fallback), beta). It names a model to retry directly when the API skipped the fallback attempt (for example, the fallback model was rate limited), and is `null` otherwise. It's a hint, not a guarantee.
- `category` and `explanation` are both `null` when the refusal does not map to a named category. That `null` is a normal, permanent value, not a placeholder.
- `stop_details` itself is `null` for every stop reason other than `refusal`.

| `category`               | What it means                                                                                                                                                                                                                             | Billed before any output |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| `"cyber"`                | The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.                                                                                                    | No                       |
| `"bio"`                  | The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.                                                                                                    | Yes                      |
| `"frontier_llm"`         | The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category. | Yes                      |
| `"reasoning_extraction"` | The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](build-with-claude-thinking.md).                                         | Yes                      |
| `"general_harms"`        | The request falls under a usage-policy area outside the four named categories. Benign work can also trigger this category.                                                                                                                | No                       |

A refusal can arrive before any output, or mid-stream after partial output. In either case, treat any partial output as incomplete and discard it.

## How refusals are billed

These billing rules apply on every platform: the Claude API, Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry.

**Refusals before any output:** To disrupt attempts to circumvent Anthropic's safeguards at scale, a refusal that arrives before any output is billed when its `stop_details.category` is `"bio"`, `"frontier_llm"`, or `"reasoning_extraction"`. These are the categories where Anthropic measures low volumes of false positives, as of September 2026. These refusals are billed like any other request, at the rates of the model that ran it. A refusal before any output in any other category, or with a `null` category, is not billed. Either way, `content` is empty and token counts appear in `usage`. The request still counts against your rate limits.

**Mid-stream refusals:** A mid-stream refusal bills the input tokens and the output already streamed at normal rates.

**Fallback:** When you use fallback, the refusal that triggered it is billed, in addition to the fallback request, when it arrived mid-stream or is in one of the billed categories. [Fallback credit](build-with-claude-fallback-credit.md) compensates for the fallback request's prompt-cache miss, so you don't pay to cache the conversation twice. For how server-side fallback reports each attempt, see [Billing and rate limits](#billing-and-rate-limits).

The billed categories may change as Anthropic keeps measuring and refining its safeguards' false positive rates. The **Billed before any output** column in the [refusal category table](#refusal-response) lists the billed categories.

## Picking a fallback approach

There are three ways to retry a refused request on another model. The right one depends on where you are running and how much control you need.

| Your situation                       | Use                                                                                                | Why                                                         |
|:-------------------------------------|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------|
| Claude API, simplest setup           | [Server-side fallback](#server-side-fallback)                                                      | One request, one response. The API handles the retry.       |
| Any platform, using an Anthropic SDK | [The SDK middleware](#client-side-fallback)                                                        | Configure once on the client. Retries happen automatically. |
| Raw HTTP or custom retry logic       | [A manual retry](#manual-retry) with [fallback credit](build-with-claude-fallback-credit.md) | Full control. Fallback credit keeps the cost down.          |

Server-side fallback and the SDK middleware apply fallback credit for you. You only need the [Fallback credit](build-with-claude-fallback-credit.md) page when you build the retry yourself.

## Server-side fallback

Server-side fallback retries a refused request inside a single API call. In the default mode, when the primary model declines and the refusal category has a recommended fallback, the API runs the same request on the model Anthropic recommends for that category. You can instead [name up to three fallback models of your own](#naming-your-own-fallback-models). Either way, you get back one response that names the model that answered, so your user gets an answer in one round trip.



Server-side fallback is in beta on the Claude API. The `fallbacks` parameter is not supported on the [Message Batches API](build-with-claude-batch-processing.md) (a batch item that includes it comes back as an errored result) and is not available on Amazon Bedrock, Google Cloud, or Microsoft Foundry. On those platforms, use [client-side fallback with the SDK middleware](#client-side-fallback) instead.

### Making the request

Set the `fallbacks` parameter to the string `"default"` and send the `server-side-fallback-2026-07-01` beta header. The API then applies the requested model's server-defined default routing, which selects a recommended fallback model based on the refusal category the classifier reports, so refused requests are served without you maintaining a model list as recommendations change.

Default routing never draws the up-front [oversized-image rejection](build-with-claude-vision-coordinates.md#oversized-image-error) for models you did not choose: a routed model that would resize an image marked `"oversized_image": "error"` is dropped from the routing instead, so a marked image is never served resized.

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

The routing is applied server-side and is not published per model on the [Models API](../Endpoints/models-list.md). To see which model served a refused request, check the response's top-level `model` field and look for a `fallback_message` entry in `usage.iterations`, as this page's samples do.

Only a safety classifier decline triggers the fallback. A rate limit, overload, or server error on the requested model is returned to you as-is.



The beta header must carry exactly the date `2026-07-01`, which supports both `"default"` and the explicit-list form, or `2026-06-01`, which accepts only the explicit-list form. Under any other `server-side-fallback-*` value, the `fallbacks` parameter is rejected with a 400 error. If you built against an earlier preview of this feature, update the beta header and the request and response shapes together to the ones on this page.

### Naming your own fallback models

Instead of default routing, you can set `fallbacks` to a list of up to three models. When the requested model declines, the API runs the next model in the chain on the same request. Use this form when you want to control exactly which models serve refused requests, such as pinning a model your application has qualified.

Named fallback models count toward the [oversized-image check](build-with-claude-vision-coordinates.md#oversized-image-error): a request whose image block sets `"oversized_image": "error"` is checked up front against the requested model and every named fallback, is rejected if any of them would resize that image, and the rejection's reported rescale target fits them all.

The highlighted lines are the only difference from the default-routing request.

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
- Each entry must be one of the requested model's permitted targets. With the beta header set, that list is published as `allowed_fallback_models` on the model's entry in the [Models API](../Endpoints/models-list.md).
- Each entry names a `model` and can override `max_tokens`, `thinking`, `output_config`, and `speed` for that attempt only.
- The request must be valid as a direct request to every model named. If a fallback model does not support a feature the request uses, the API rejects the request up front.
- As with the default mode, only a safety classifier decline triggers the fallback. A rate limit, overload, or server error on the requested model is returned to you as-is.
- If a fallback model is rate limited or overloaded, the fallback attempt is not made and the preceding refusal is returned instead. The refusal's `stop_details.recommended_model` then names a model to retry directly. Size the fallback model's rate limits for the refusal volume you expect, or fallbacks degrade to refusals under load.

The response has the same shape in both modes: the model that served the turn appears in the top-level `model` field, a `fallback` content block marks the handoff, and `usage.iterations` records each attempt.

### What the response contains

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

[Sticky routing](#sticky-routing) can send a later turn straight to the fallback model. Such a turn carries no `fallback` content block, because no model declined that turn. Identify it by the `fallback_message` entry in `usage.iterations`, the absence of a `message` entry for the requested model, and the response's `model` field.

### Continuing the conversation

On the next turn, send the assistant content back as you received it. After a mid-output fallback, `content` can include block types the declining model produced before the handoff. The following table covers which to keep and which to drop when you echo the turn.

| Block type                                                                             | On the next turn                                                                                                                                                                                                               |
|:---------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fallback`                                                                             | Keep it exactly where it appeared. The API uses its position to validate the thinking blocks around it, so a request that echoes thinking blocks from both sides of the boundary is rejected if the block is omitted or moved. |
| `text`                                                                                 | Keep.                                                                                                                                                                                                                          |
| Any block after the final `fallback` block                                             | Keep.                                                                                                                                                                                                                          |
| `thinking`, `redacted_thinking`, or `connector_text` before the final `fallback` block | Drop.                                                                                                                                                                                                                          |
| Client-side `tool_use` before the final `fallback` block                               | Drop.                                                                                                                                                                                                                          |
| `server_tool_use` before the final `fallback` block                                    | Keep when paired with its result. Drop when it has no matching result.                                                                                                                                                         |



A `connector_text` block carries narration text that some tool-using responses include between tool calls.

### Streaming

On a streaming request, the retry happens on the same stream, and nothing you have already received is invalidated. What you see depends on when the decline happens.

**When the decline happens before any output:**

- `message_start` names the fallback model, and the `fallback` block is the first content block.
- Because `message_start` waits for the fallback attempt to start, time to first byte includes the declined attempt.

**When the decline happens mid-output:**

- The open content block closes, and the `fallback` block (an ordinary `content_block_start` and `content_block_stop` pair with no deltas) marks the boundary.
- The fallback model continues from the partial output. Only the partial output's `text` blocks are passed to the fallback model as context. Other block types remain in `content`.
- `message_start` already named the requested model, so read the serving model from the `fallback` block's `to.model` and from the `fallback_message` entry in the final `message_delta`'s `usage.iterations`.

### Non-streaming responses

On a non-streaming request, a mid-output decline behaves differently: the response omits the declined model's partial output, and the fallback model answers from scratch. The result looks like a decline before any output, with the `fallback` block first. The declined attempt and its output tokens still appear in `usage.iterations`.



**Declines during tool use:** completed tool work does not block fallback. When a decline fires after server tools (for example, web search or code execution) have finished executing within a request, the fallback attempt proceeds: the completed tool results carry over, and the fallback model can keep invoking server tools. The one case that does not retry is a streaming decline that fires while a tool-use block of any type (a client tool, a server tool, or an MCP tool call) is still open on the stream: that refusal is returned directly, and if the `fallback-credit-2026-07-01` header is set it still carries a credit token redeemable by continuing the partial response. Non-streaming requests are unaffected; the API clears the partial work and retries before responding.

### Billing and rate limits

Each attempt follows the rules in [How refusals are billed](#how-refusals-are-billed), at the rates of the model that ran it. An attempt that declined before producing any output is billed only when its refusal category is billed, and its tokens are reported on its `usage.iterations` entry either way. Every attempt that produced output, including one that declined partway through its response, is billed separately. The `usage.iterations` array is the per-attempt record of what you're billed. The top-level `usage` counts describe only the attempt that produced the returned message. Tokens from different models are never summed into one field.

Every attempt that runs, including one that declined, counts against its own model's rate limits.

### Sticky routing

After a conversation falls back, the API records which model served it. Later requests for that conversation that include `fallbacks` go directly to that fallback model, without running the requested model. This avoids paying for an attempt that would predictably be declined again on every turn.

A few properties of the routing decision:

- It is retained for approximately 1 hour and is scoped to your organization.
- It is stored as a content hash of the conversation prefix plus the model that served it. The message content itself is not stored.
- It is best-effort, so your code must handle the requested model being tried again at any time.

Sticky routing applies to both streaming and non-streaming requests. On a streaming request, the routing decision is made before the stream opens, so the `message_start` event's `model` field already carries the fallback model's ID.

## Client-side fallback with the SDK middleware

Every Anthropic SDK includes a refusal-fallback middleware. You configure it once on the client with your list of fallback models. Calls through `client.beta.messages` then retry refused requests automatically, on any platform. The middleware also sends the `fallback-credit-2026-07-01` beta header on every request it handles, so retries are repriced without per-request setup.

### Setting it up

Pass `BetaRefusalFallbackMiddleware` to the client constructor, and share one `BetaFallbackState` instance across the requests of a conversation.

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

### How it behaves

- Retries walk your fallback list in order. A fallback model that itself refuses passes the request to the next entry.
- When every model in the list has declined, the middleware returns the final refusal (the last model's refusal response) rather than raising an error.
- Thinking blocks from Claude Fable 5.1, Claude Opus 5.5, or Claude Fable 5 pass through unchanged. Each retry re-sends your original request body, and the only blocks the middleware removes from conversation history on later requests are the `fallback` boundary blocks it added itself. The fallback model can't read Claude Fable 5.1 blocks, which are [preserved only for that model or a newer one](build-with-claude-thinking.md#preserved-for-model), so the API drops them. The API also drops Claude Opus 5.5 blocks for every fallback model except Claude Fable 5.1 and Claude Mythos 5.1 (see [Switching models mid-conversation](build-with-claude-preserved-thinking.md#switching-models)).
- Responses served through the middleware include a `fallback` content block at each model boundary, the same as server-side fallback responses. The middleware manages those blocks for you on later requests.
- The model that accepted is recorded in `BetaFallbackState`, so follow-up requests that share the state stay pinned to it rather than re-asking a model that refused.



The middleware and the server-side `fallbacks` parameter do the same job. Configure one or the other, never both on the same request. To send a server-side `fallbacks` request from an application that installs the middleware, use a separate client instance without it.

## Writing the retry yourself

Over raw HTTP or with custom retry logic, implement the pattern the middleware wraps:

1.  1

    ### Detect the refusal

    Check the response for `stop_reason: "refusal"`.

2.  2

    ### Re-send on a fallback model

    Send the same request with `model` set to a fallback model, such as Claude Opus 4.8. Another model can normally serve a request that Claude Fable 5.1 or Claude Fable 5 declines. How you handle the conversation history depends on whether you redeem a [fallback credit](build-with-claude-fallback-credit.md):

    - **Not redeeming a credit:** you can leave the earlier `thinking` and `redacted_thinking` blocks in place or strip them to save input tokens. The fallback model normally can't use them either way: it ignores Claude Fable 5 blocks, and Claude Fable 5.1 blocks are [preserved only for that model or a newer one](build-with-claude-thinking.md#preserved-for-model), so the API drops them. The API also drops Claude Opus 5.5 blocks for every fallback model except Claude Fable 5.1 and Claude Mythos 5.1 (see [Switching models mid-conversation](build-with-claude-preserved-thinking.md#switching-models)).
    - **Redeeming a credit:** send the body unchanged, because redemption requires an exact match. The server handles the earlier model's thinking blocks on a redemption, so do not strip them (see [Fields that must match the refused request](build-with-claude-fallback-credit.md#reference)).

3.  3

    ### Stay on the fallback model

    For multi-turn conversations, keep using the fallback model for subsequent turns rather than switching back.

A manual retry writes the fallback model's prompt cache from scratch, which costs more than reading an existing cache. [Fallback credit](build-with-claude-fallback-credit.md) refunds that cost; redeem it on every retry you build yourself.

## Refusals in Message Batches

A refused request in a [Message Batch](build-with-claude-batch-processing.md) comes back as `result.type: "succeeded"` with `stop_reason: "refusal"`. Batch results carry the same `stop_details` object as synchronous responses, so you can detect refusals through either `stop_reason` or `stop_details.type`. One difference: batch refusals don't mint fallback credits, so `stop_details` on a batch result never includes a `fallback_credit_token`.

Server-side fallback is not available for batches (a batch request that includes `fallbacks` produces a per-item errored result). To retry refused batch items:

1.  Collect the refused items from the results.
2.  Strip the Claude Fable 5.1 or Claude Fable 5 thinking blocks from any multi-turn histories.
3.  Resubmit them on a fallback model as a new batch or as direct requests.

## Common pitfalls

- **Retry on a different model.** Re-sending a refused request to the same model usually earns another refusal. Point the retry at the fallback model.
- **Budget retries per request, not per turn or per session.** A single turn can produce several refusals, for example an agent plus its sub-agents.
- **Configure fallback on every request path.** Retry handlers, error-recovery branches, and background workers all need it. A handler that re-issues a request without fallback loses the protection on exactly the requests most likely to need it.
- **Give sub-agent calls their own fallback.** The `fallbacks` parameter does not propagate into model calls made from inside tool execution.
- **Make fallback a property of the request, not of ambient state.** A shared flag, cached config value, or global toggle can drift out of sync and silently leave a request unprotected. When you cannot confirm fallback is active, configure it rather than assume it is on.
- **Instrument refusals as their own signal.** A refusal is an HTTP 200, so monitoring built on error rates or 5xx responses never sees it. Emit one event per refusal and one per fallback-served response (the `fallback_message` entry in `usage.iterations` marks the latter), then alert on the gap between the two counts.
- **Branch on `stop_reason` or `stop_details.type`, not on `content` or the inner `stop_details` fields.** The `stop_details` object is always present on a refusal, but its `category` and `explanation` fields can be `null`. Check for `stop_reason` equal to `"refusal"` directly.

## Next steps



[Fallback credit](build-with-claude-fallback-credit.md)

Avoid paying the prompt-cache cost twice when you build the retry yourself.



[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)

Every `stop_reason` value and how to handle it.



[SDK middleware](../Other/cli-sdks-libraries-middleware.md)

How SDK middleware works, including the refusal-fallback helper.



[Migration guide](../../20-Models/models-fable-5-1-migration-guide.md)

Move an existing application to Claude Fable 5.1.
