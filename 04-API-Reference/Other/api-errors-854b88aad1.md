---
title: "Claude API errors - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/errors"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:16Z"
tags: ["api", "sdk"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Ferrors)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

[API reference](/docs/en/api/overview)Using the API

# Claude API errors

Copy page



Understand the HTTP status codes, error response shape, and request IDs the Claude API returns, and handle errors with the SDKs' typed exceptions.

Copy page



## HTTP errors

The API follows a predictable HTTP error code format:

- 400 - `invalid_request_error`: There was an issue with the format or content of your request. This error type may also be used for other 4XX status codes not listed in this section. The API also returns a 400 when usage reaches an organization or workspace [spend limit you set](/docs/en/api/rate-limits#setting-your-own-spend-limit), except limits on the [Claude Code workspace](/docs/en/manage-claude/workspaces#claude-code-workspace), which can return a 429 instead.

- 401 - `authentication_error`: There's an issue with your [API key](/docs/en/get-api-key) (for example, it's malformed, revoked, or expired; see [Key expiration](/docs/en/manage-claude/authentication#key-expiration)). On Claude Platform on AWS, this can also indicate a problem with your AWS credentials or SigV4 signature.

- 402 - `billing_error`: There's an issue with your billing or payment information. Check your payment details in the [Claude Console](https://platform.claude.com), or in AWS Marketplace if you're using Claude Platform on AWS.

- 403 - `permission_error`: Your API key does not have permission to use the specified resource. Check your organization's access and workspace settings in the [Claude Console](https://platform.claude.com).

- 404 - `not_found_error`: The requested resource was not found. Check the endpoint path and any resource IDs in the request URL.

- 409 - `conflict_error`: The request conflicts with the current state of a resource. For example, the resource was modified concurrently, or a value that must be unique is already in use. Resolve the conflict, then retry the request.

- 413 - `request_too_large`: Request exceeds the maximum allowed number of bytes. See [Request size limits](#request-size-limits) for per-endpoint maximums.

- 429 - `rate_limit_error`: Your organization has hit a [rate limit](/docs/en/api/rate-limits), reached its usage tier's monthly spend cap, or reached a spend limit on the Claude Code workspace. A tier spend-cap 429 has no `retry-after` header and keeps failing until access resumes; see [Reaching your spend cap](/docs/en/api/rate-limits#reaching-your-spend-cap) for how to recognize it.

- 500 - `api_error`: An unexpected error has occurred internal to Anthropic's systems. Retry the request with exponential backoff; if the error persists, contact support with the [request ID](#request-id).

- 504 - `timeout_error`: The request timed out while processing. Consider using the [streaming Messages API](/docs/en/build-with-claude/streaming) for long-running requests. See [Long requests](#long-requests) for more options.

- 529 - `overloaded_error`: The API is temporarily overloaded.

  

  529 errors can occur when the API experiences high traffic across all users.

  In rare cases, if your organization has a sharp increase in usage, you might see 429 errors because of acceleration limits on the API. To avoid hitting acceleration limits, ramp up your traffic gradually and maintain consistent usage patterns.

The official SDKs automatically retry transient failures (such as connection errors, rate limits, and 5xx server errors) with exponential backoff, twice by default, honoring the `retry-after` header when present. The SDK client accepts `max_retries` to configure or disable this behavior.

When receiving a [streaming](/docs/en/build-with-claude/streaming) response over server-sent events (SSE), an error can occur after the API returns a 200 response. In that case, error handling doesn't follow these standard mechanisms. See [Error events](/docs/en/build-with-claude/streaming#error-events) for the shape of mid-stream errors.

## Request size limits

The API enforces request size limits:

| Endpoint type                                            | Maximum request size |
|:---------------------------------------------------------|:---------------------|
| Messages API                                             | 32 MB                |
| Token Counting API                                       | 32 MB                |
| [Batch API](/docs/en/build-with-claude/batch-processing) | 256 MB               |
| [Files API](/docs/en/build-with-claude/files)            | 500 MB               |

If you exceed these limits, you'll receive a 413 `request_too_large` error. On the direct Claude API, Cloudflare returns this error before the request reaches the API servers.

## Error shapes

The API always returns errors as JSON, with a top-level `error` object that always includes a `type` and `message` value. The response also includes a `request_id` field for easier tracking and debugging. For example:

JSON



```python
{
  "type": "error",
  "error": {
    "type": "not_found_error",
    "message": "The requested resource could not be found."
  },
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"
}
```

In accordance with the [versioning](/docs/en/api/versioning) policy, the values within these objects may expand, and it is possible that the `type` values will grow over time.

## SDK error types

The official SDKs raise typed exceptions for these errors instead of returning raw JSON, and the class names and namespaces differ by language. For example, a 404 surfaces as `anthropic.NotFoundError`. The Go SDK has one error type for every status, `*anthropic.Error`: branch on `StatusCode`. Catch the SDK's typed classes rather than string-matching error messages, handling the most specific classes first. Each SDK page documents its full exception hierarchy:

- [Python](/docs/en/cli-sdks-libraries/sdks/python#handling-errors) · [TypeScript](/docs/en/cli-sdks-libraries/sdks/typescript#handling-errors) · [C#](/docs/en/cli-sdks-libraries/sdks/csharp#error-handling) · [Go](/docs/en/cli-sdks-libraries/sdks/go#error-handling) · [Java](/docs/en/cli-sdks-libraries/sdks/java#error-handling) · [PHP](/docs/en/cli-sdks-libraries/sdks/php#error-handling) · [Ruby](/docs/en/cli-sdks-libraries/sdks/ruby#handling-errors)

## Request ID

Every API response includes a unique `request-id` header. This header contains a value such as `req_018EeWyXxfu5pfWkrYcMdjWG`. The same identifier appears as the `request_id` field in [error response bodies](#error-shapes). When contacting support about a specific request, include this ID to help quickly resolve your issue.

On [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), responses include two request IDs: the AWS request ID (`x-amzn-requestid`, primary, indexed in CloudTrail) and the Anthropic request ID (`request-id`, secondary). Use the AWS request ID for CloudTrail lookups and the Anthropic request ID for Anthropic support tickets.

The Python and TypeScript SDKs expose the request ID as a `_request_id` property on top-level response objects. The C#, Go, Java, and PHP SDKs expose it through their raw-response accessors, and the Ruby SDK through [middleware](/docs/en/cli-sdks-libraries/middleware). In every SDK except Ruby, use `with_raw_response` to read any other [response header](/docs/en/api/overview#response-headers), such as `anthropic-organization-id` and [`anthropic-workspace-id`](/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response). In Ruby, use the same middleware. On Claude Platform on AWS, use the raw-response accessor to read the AWS request ID (`x-amzn-requestid`) as well:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python (Claude Platform on AWS)

TypeScript (Claude Platform on AWS)



```python
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(f"Request ID: {message._request_id}")
```

For Claude Platform on AWS request-ID examples in other languages, see [Request IDs](/docs/en/build-with-claude/claude-platform-on-aws#request-ids).

## Long requests



Consider using the [streaming Messages API](/docs/en/build-with-claude/streaming) or [Message Batches API](/docs/en/api/messages/batches/create) for long-running requests, especially those over 10 minutes.

Avoid setting a large `max_tokens` value without using the [streaming Messages API](/docs/en/build-with-claude/streaming) or [Message Batches API](/docs/en/api/messages/batches/create):

- Some networks may drop idle connections after a variable period of time, which can cause the request to fail or time out without receiving a response from Anthropic.
- Networks differ in reliability. The [Message Batches API](/docs/en/api/messages/batches/create) can help you manage the risk of network issues by allowing you to poll for results rather than requiring an uninterrupted network connection.

If you are building a direct API integration, setting a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/programming.html) can reduce the impact of idle connection timeouts on some networks.

The [SDKs](/docs/en/cli-sdks-libraries/overview) validate that your non-streaming Messages API requests are not expected to exceed a 10-minute timeout. They also set a socket option for TCP keep-alive.

If you don't need to process events incrementally, the SDKs can consume the stream for you and return the complete `Message` object, identical to what a non-streaming call returns:

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

with client.messages.stream(
    max_tokens=128000,
    messages=[{"role": "user", "content": "Write a detailed analysis..."}],
    model="claude-sonnet-5",
) as stream:
    message = stream.get_final_message()

print(next(block.text for block in message.content if block.type == "text"))
```

See [Streaming Messages](/docs/en/build-with-claude/streaming#get-the-final-message-without-handling-events) for more details.

## Common validation errors

### Prefill not supported

Claude 4.6 and later models and [Claude Mythos Preview](https://anthropic.com/glasswing) do not support prefilling assistant messages. Sending a request with a prefilled last assistant message to any of these models returns a 400 `invalid_request_error`:

```python
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "This model does not support assistant message prefill. The conversation must end with a user message."
  }
}
```



Use [structured outputs](/docs/en/build-with-claude/structured-outputs) on models that support it, system prompt instructions, or [`output_config.format`](/docs/en/build-with-claude/structured-outputs#json-outputs) instead.

### Thinking blocks cannot be modified

If the most recent assistant message contains `thinking` or `redacted_thinking` blocks that were edited, reordered, filtered out, or reconstructed before being sent back to the API, the request returns a 400 `invalid_request_error`. The error message starts with the position of the offending block (for example, `messages.1.content.0`) and contains:

``` block
`thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified. These blocks must remain as they were in the original response.
```



With tool use, every `thinking` and `redacted_thinking` block from the assistant turn must be passed back exactly as received, including blocks whose `thinking` field is empty. Pass thinking blocks back unchanged, and if your application filters content blocks by type before resending, include both `thinking` and `redacted_thinking`. See [Troubleshooting thinking](/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-blocks-modified), [Preserving thinking blocks](/docs/en/build-with-claude/thinking#preserving-thinking-blocks), and [Preserved thinking](/docs/en/build-with-claude/thinking#preserved-thinking).

### Extended thinking not supported

Claude 4.7 and later models have removed extended thinking. Sending `thinking: {"type": "enabled"}` to any of these models returns a 400 `invalid_request_error`:

``` block
"thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```



Use [adaptive thinking](/docs/en/build-with-claude/thinking) instead. [Migrating to adaptive thinking](/docs/en/build-with-claude/extended-thinking#migrating-to-adaptive-thinking) shows the parameter mapping, and [Troubleshooting thinking](/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-type-enabled) covers the symptom-first fix.

### Adaptive thinking not supported

Models that support only extended thinking (Claude 4.5 and earlier models) reject `thinking: {"type": "adaptive"}` with a 400 `invalid_request_error`:

``` block
adaptive thinking is not supported on this model
```



Use `thinking: {"type": "enabled", "budget_tokens": N}` on these models; see [Extended thinking](/docs/en/build-with-claude/extended-thinking) for the configuration and [Troubleshooting thinking](/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-type-adaptive) for the symptom-first fix.

### Thinking cannot be disabled

On Claude Fable 5.1, [Claude Mythos 5.1](https://anthropic.com/glasswing), Claude Fable 5, [Claude Mythos 5](https://anthropic.com/glasswing), Claude Opus 5.5, and [Claude Mythos Preview](https://anthropic.com/glasswing), thinking is always on. Sending `thinking: {"type": "disabled"}` to any of these models returns a 400 `invalid_request_error`. On all of these models except Claude Mythos Preview, the message reads:

``` block
"thinking.type.disabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```



On Claude Mythos Preview, the only one of these models that accepts extended thinking, the message reads:

``` block
"thinking.type.disabled" is not supported for this model. Thinking defaults to adaptive mode when not specified; use "thinking.type.enabled" with "budget_tokens" for extended thinking.
```



Omit the `thinking` parameter and the request runs with adaptive thinking. To keep thinking content out of responses without turning thinking off, set `display: "omitted"` on the thinking configuration. See [Troubleshooting thinking](/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-type-disabled).

### Forced tool use not supported

Claude Opus 5.5, Claude Fable 5.1, and [Claude Mythos 5.1](https://anthropic.com/glasswing) don't support forced tool use. Sending `tool_choice: {"type": "any"}` or `tool_choice: {"type": "tool", "name": "..."}` to any of these models, including on the [token counting endpoint](/docs/en/build-with-claude/token-counting), returns a 400 `invalid_request_error`:

``` block
tool_choice: type "tool" and "any" are not supported for this model.
```



`tool_choice: {"type": "auto"}` (the default) and `{"type": "none"}` are accepted. Use `auto` with [strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use) to keep tool inputs schema-valid, or [structured outputs](/docs/en/build-with-claude/structured-outputs) when you need the response itself in a fixed JSON shape. See [Forcing tool use](/docs/en/agents-and-tools/tool-use/define-tools#forcing-tool-use).

### Computer use tool version not supported

On the Claude API and Google Cloud, Claude Opus 5.5 supports [computer use](/docs/en/agents-and-tools/tool-use/computer-use-tool) only as the `computer_toolset_20260801` toolset. On those platforms, sending it a `tools` entry of the earlier `computer_20251124` type (with that tool's beta header) returns a 400 `invalid_request_error`. The message names the rejected type, then lists the tool types the model does accept after `Did you mean one of`; it begins:

```python
'claude-opus-5-5' does not support tool types: computer_20251124.
```



The API returns the same message for any Anthropic-defined tool type that the requested model doesn't support. Declare `{"type": "computer_toolset_20260801"}` without the beta header and update your agent loop as described in [Migrate from `computer_20251124`](/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer-20251124). Earlier models that support the toolset keep accepting `computer_20251124`, as does Claude Opus 5.5 on Amazon Bedrock.

### Thinking block no longer matches the conversation

On Claude Fable 5.1 and Claude Opus 5.5, the API accepts a replayed thinking block only while the `system` prompt, `tools`, and messages that preceded it are unchanged. For new accounts created on or after August 31, 2026, and for any request that sets `thinking.block_binding.prefix_mismatch_behavior` to `"error"`, a replayed block whose earlier history changed is rejected with a 400 `invalid_request_error` (with `"drop_block"`, the API drops the block and the request succeeds). The message starts with the position of the first failing block:

``` block
messages.{i}.content.{j}: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.prefix_mismatch_behavior` to "drop_block".
```



Without the `thinking-binding-controls-2026-08-01` beta header the message also names that header. Keep the conversation history append-only, or send the beta header with `prefix_mismatch_behavior: "drop_block"` to drop the block and continue. A block from a model the target model can't read is dropped rather than rejected. See [Keeping the prefix unchanged](/docs/en/build-with-claude/preserved-thinking#prefix-check) and [Troubleshooting thinking](/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-block-signature).

Sending `thinking.block_binding` without the `thinking-binding-controls-2026-08-01` [beta header](/docs/en/api/beta-headers) returns a 400 `invalid_request_error` whose message ends in:

``` block
block_binding: Extra inputs are not permitted
```



Add the header, or remove the field.

### Outbound web identity federation disabled (Claude Platform on AWS)

If every request to [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws) returns `"Outbound web identity federation is disabled for your account"`, run `aws iam enable-outbound-web-identity-federation` once per AWS account. See [Enable outbound web identity federation](/docs/en/build-with-claude/claude-platform-on-aws#enable-outbound-web-identity-federation) for details.

## Next steps



[Troubleshooting thinking](/docs/en/build-with-claude/thinking-troubleshooting)

Symptom-first fixes for thinking configuration 400 errors, empty thinking blocks, and `max_tokens` stops.



[Rate limits](/docs/en/api/rate-limits)

To mitigate misuse and manage capacity on the API, limits are in place on how much an organization can use the Claude API.



[Streaming messages](/docs/en/build-with-claude/streaming)

Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.
