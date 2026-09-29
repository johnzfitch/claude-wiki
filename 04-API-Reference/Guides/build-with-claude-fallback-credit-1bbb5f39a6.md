---
title: "Fallback credit - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/fallback-credit"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:30Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Ffallback-credit)





SearchCtrlK

First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)[Authentication](/docs/en/manage-claude/authentication)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

[Thinking](/docs/en/build-with-claude/thinking)

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[Console](/)

[Messages](/docs/en/intro)Building with Claude

# Fallback credit

Copy page



Avoid paying the prompt-cache cost twice when you retry a refused request on another model.

Copy page



Prompt caches are per-model. When a model declines a request and you retry on another model, the conversation prefix already cached for the first model must be written into the new model's cache from scratch. Cache writes cost more than cache reads. Fallback credit removes that extra cost. The refusal carries a credit token, you echo the token on the retry, and the retry is billed as though the conversation had been on the new model all along.

You need this page only when you build the retry yourself: over raw HTTP or with custom retry logic. [Server-side fallback](/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback) and the [SDK middleware](/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback) apply fallback credit automatically. If you use either, skip this page.

[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback) covers detecting refusals and choosing a fallback approach. [Prompt caching](/docs/en/build-with-claude/prompt-caching) explains cache reads and cache writes if those terms are new.

## The basic flow

1.  1

    ### Opt in with the beta header

    Send the request that may be refused with the `anthropic-beta: fallback-credit-2026-07-01` header. The `server-side-fallback-2026-07-01` header also grants the same fields, and the earlier `fallback-credit-2026-06-01` header remains accepted and grants the same fields.

2.  2

    ### Read two fields from the refusal

    On a refusal, `stop_details` includes two fields:

    - **`fallback_credit_token`:** an opaque string that represents the credit.
    - **`fallback_has_prefill_claim`:** a Boolean that tells you which retry body shape to use.

    Both are `null` when no credit is available for the refusal.

3.  3

    ### Build the retry

    Start from the refused request body. Set `model` to the fallback model and add the token as the top-level `fallback_credit_token` parameter. Pick the body shape from the following table.

4.  4

    ### Send the retry with the same header

    Send the retry with the same `fallback-credit-2026-07-01` beta header. The retry needs the header to redeem the token.

The `fallback_has_prefill_claim` field tells you whether the retry can continue the refused model's partial output instead of starting over:

| `fallback_has_prefill_claim` | Retry body                                                                                                                                                                                                                                                          |
|:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `true`                       | The refused request body, unchanged, plus one appended assistant message whose `content` echoes the refused response's `content`. The retry model continues the response from where the refused model stopped, and completed server tool calls are not re-executed. |
| `false`                      | The refused request body, unchanged.                                                                                                                                                                                                                                |

## Example

The following example makes a request that may be refused and redeems the credit token on a retry against Claude Opus 4.8. When a retry attempt is rejected, the example degrades through the rejection ladder: the sequence of progressively simpler retry shapes covered in [When a retry is rejected](#when-a-retry-is-rejected).

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

request = {
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello, Claude"}],
}


def send(model: str, body: dict[str, object]) -> BetaMessage:
    return client.beta.messages.create(
        model=model, betas=["fallback-credit-2026-07-01"], **body
    )


response = send("claude-fable-5", request)

if (
    response.stop_reason == "refusal"
    and (details := response.stop_details)
    and (token := details.fallback_credit_token)
):
    exact_body = request | {"fallback_credit_token": token}
    # Prefer the continuation shape unless the claim is False
    if details.fallback_has_prefill_claim is not False:
        echoed = [block.model_dump() for block in response.content]
        match echoed:
            case [*_, {"type": "text"} as final_block]:
                final_block["text"] = final_block["text"].rstrip()
        attempt = exact_body | {
            "messages": [
                *request["messages"],
                {"role": "assistant", "content": echoed},
            ]
        }
    else:
        attempt = exact_body

    try:
        response = send("claude-opus-4-8", attempt)
    except BadRequestError as error:
        if "redemption temporarily unavailable" in error.message:
            raise  # Transient: retry with the token within its five-minute window
        try:
            # Fall back to the unchanged body, still with the token
            response = send("claude-opus-4-8", exact_body)
        except BadRequestError as retry_error:
            if "redemption temporarily unavailable" in retry_error.message:
                raise  # Transient: retry with the token within its five-minute window
            # The token itself was rejected: forfeit it and retry without.
            response = send("claude-opus-4-8", request)

print(json.dumps({"stop_reason": response.stop_reason, "model": response.model}))
```

## Where it works

Fallback credit is in beta on the Claude API, Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry. Refusals in [Message Batches](/docs/en/build-with-claude/batch-processing) don't mint credit tokens, and redemption applies only to direct Messages API requests: a token passed on a batch request is accepted but ignored.

The retry model must be one of the refused model's permitted fallback targets. For Claude Fable 5.1 and Claude Fable 5, those are Claude Opus 4.8 (`claude-opus-4-8`) and Claude Opus 5 (`claude-opus-5`).

### Looking up permitted fallback targets programmatically

On the Claude API and Claude Platform on AWS, the target list is published as `allowed_fallback_models` on each model's entry in the [Models API](/docs/en/api/models/list) when the `server-side-fallback-2026-07-01` beta header is set. The list is not yet visible under the `fallback-credit-*` header alone. It is not exposed on Amazon Bedrock, Google Cloud, or Microsoft Foundry.

## Checking that the credit applied

The refund is visible in the retry's `usage`. Compared with what the same request would report without the token, `cache_creation_input_tokens` is lower, and `cache_read_input_tokens` is higher by the same amount. A shift of zero means the token was honored but there was nothing to reprice, for example because the retry model's cache was already warm.

## When a retry is rejected

Most retries redeem on the first attempt. When one does not, the API returns a 400 error that tells you what to try next.

1.  1

    ### Continuation rejected: resend the unchanged body

    If the retry that appends the assistant message is rejected with a 400 error, resend the refused request body unchanged, still with the token.

2.  2

    ### Token rejected: drop the token

    If the unchanged body is also rejected with a 400 error whose message names `fallback_credit_token`, retry without the token. The credit is forfeited, but the retry itself goes through.



If the refused request executed server tools, a tokenless retry re-runs and re-bills those tools. In that case, surface the 400 error to your caller instead of falling through to a tokenless retry.

### If the error says 'redemption temporarily unavailable'

This rejection is transient, not a verdict on your retry shape. Retry the same request, with the same token, within the token's five-minute window. Do not move to the next step of the ladder.

## Reference

The following sections cover edge cases and the complete redemption rules. Most integrations do not need them.

### Fields that must match the refused request

Redemption compares the retry against the refused request. Every field that shapes the prompt must match exactly. Fields that do not shape the prompt may change on the retry.

| Rule                    | Fields                                                                                                                                                                      |
|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Must match exactly      | `system`, `messages`, `tools`, `tool_choice`, `thinking`, and `cache_control`, plus `output_config`, `mcp_servers`, `context_management`, and `container` when you use them |
| May change on the retry | `model`, `max_tokens`, `stop_sequences`, `temperature`, `top_p`, `top_k`, `stream`, `metadata`, and `service_tier`                                                          |

The continuation shape (`fallback_has_prefill_claim: true`) is the one exception to the `messages` match: it adds exactly one assistant message at the end of `messages`.

Do not strip `thinking` or `redacted_thinking` blocks from earlier turns on the retry, even though a plain retry without a token usually strips them. The body must match the refused request, and the server handles those blocks itself.

### Beta headers must match too

Send the same `anthropic-beta` headers on the retry as on the refused request. A beta header present on one of the two requests but not the other can fail the match even when the bodies are identical. The resulting 400 error carries the same `request body ... does not match` message as a body difference, so a header difference is easy to misread as a body problem. In particular, do not add or drop beta headers based on which model the request targets.

Two header families are exempt from the match, for the retry's sake:

- **`server-side-fallback-*`:** a retry must drop the `fallbacks` parameter, and dropping this header along with it does not cause a mismatch.
- **`fallback-credit-*`:** keep this header on both requests. The retry needs it to redeem the token.



On models that include the 1M token context window by default, such as Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, and Claude Opus 4.8, the `context-1m-2025-08-07` beta header has no effect. To keep the two requests identical, omit that header on both rather than sending it on one and not the other.

### When fallback_has_prefill_claim is absent

The field is `null` only when the token is also `null`, so a value you observe while holding a token is never `null`. It can still be absent (`None` in the typed SDKs) on Amazon Bedrock, Google Cloud, and Microsoft Foundry while their support for the field rolls out. In that case, treat the retry shape as unknown rather than as `false`. Try the appended-assistant-message shape first, and rely on the rejection handling in [When a retry is rejected](#when-a-retry-is-rejected), which falls back to the unchanged body.

### Echoing the refused response's content

When a refusal's token supports the continuation shape, the response `content` carries only the model's own output, and the refusal explanation is delivered in `stop_details.explanation`. You can therefore echo `content` into the appended assistant message as-is.

Two adjustments may still be needed before sending:

- If the final block you send is a `text` block, strip its trailing whitespace.
- Omit any client-side `tool_use` block that has no matching `tool_result`.

If the echoed content includes a `fallback` block from an earlier [server-side fallback](/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback), keep the block exactly where it appeared. It is accepted on any request without a beta header. The API uses its position to validate the thinking blocks around it, so a request that echoes thinking blocks from both sides of that boundary is rejected if the block is omitted or moved.

### Token scope and lifetime

The token redeems only from the organization and workspace that received the refusal, including on Microsoft Foundry. On Amazon Bedrock and Google Cloud, which do not have workspaces, the token is bound to the platform's caller identity instead.

The token expires five minutes after the refusal. After that, send the retry without it. The token is also stateless: the server stores nothing about it, and there is no endpoint to inspect or revoke it.

### When a token cannot be redeemed by either shape

When the refusal arrived after server tools had already executed within the request, the token redeems only by continuing the partial response. That restriction is what prevents the completed tool calls from running, and billing, again.

One combination can therefore leave the token unredeemable by either shape, when both of the following are true:

- The request used `output_config.format` or a `tool_choice` that forces tool use. Either one rules out the appended-assistant-message shape.
- The refusal arrived after server tools had executed. That rules out the unchanged body.

If the unchanged-body retry is rejected with a 400 error saying the token must be redeemed by continuing the partial response, discard the token. A retry without it goes through, but it re-runs and re-bills the completed server tools. Surface the cost or the error to your caller rather than retrying silently.

## Next steps



[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)

Detect refusals and choose between server-side fallback, the SDK middleware, and a manual retry.



[Prompt caching](/docs/en/build-with-claude/prompt-caching)

How cache reads and cache writes are billed.



[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)

Every `stop_reason` value and how to handle it.



[SDK middleware](/docs/en/cli-sdks-libraries/middleware)

The SDK helper that applies fallback credit automatically.
