---
title: "Beta headers - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/beta-headers"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:35:35Z"
tags: ["api"]
---

# Beta headers

Copy page



Access experimental features before they become part of the standard API with the `anthropic-beta` header or the SDK’s `betas` parameter.

Copy page



Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.



The [client SDK](../Other/cli-sdks-libraries-overview.md) exposes a `client.beta` namespace for calling the API with beta features enabled.

## How to use beta headers

To access beta features, include the `anthropic-beta` header in your API requests:

```python
POST /v1/messages
Authorization: Bearer YOUR_API_KEY
anthropic-version: 2026-10-21
anthropic-beta: BETA_FEATURE_NAME
content-type: application/json
```



Each feature’s documentation states the exact beta name to send. The [API overview](overview.md) lists the APIs in beta.

The following example sends a request with the [context editing](../Guides/build-with-claude-context-editing.md) beta. The SDK takes beta names through `betas` and sends the `anthropic-beta` header for you:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = Anthropic()

response = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    betas=["context-management-2025-06-27"],
)

print(response.content)
```



Beta features are experimental and may:

- Have breaking changes with notice
- Be deprecated or removed
- Have different rate limits or pricing
- Not be available in all regions

### Multiple beta features

To use multiple beta features in a single request, include all feature names in the header separated by commas:

```python
anthropic-beta: feature1,feature2,feature3
```



You can also send the `anthropic-beta` header more than once in the same request. The Claude API reads every `anthropic-beta` header, so the following is equivalent to the previous example:

```python
anthropic-beta: feature1
anthropic-beta: feature2
anthropic-beta: feature3
```



With the SDK, list each feature (for example, `betas=["feature1", "feature2"]`). With the CLI, pass a single `--beta` flag with the feature names separated by commas (for example, `--beta feature1,feature2`). You can also repeat the flag (for example, `--beta feature1 --beta feature2`).

### Beta features on other platforms

Beta names are the same on every platform that accepts them, but not every platform accepts every beta. [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), [Claude Models on Google Cloud (Anthropic managed)](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md), [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md), and [Claude Models on Google Cloud (Google managed)](../Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md) take beta names in the `anthropic-beta` header, as the Claude API does. To send several betas, put their names in one header, separated by commas: Claude Models on Google Cloud (Google managed) reads only one `anthropic-beta` header and ignores the rest, so betas in the others don’t take effect.

On Amazon Bedrock, where beta names go depends on the API you call:

- [Claude in Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md) (`bedrock-mantle` endpoints) takes them in the `anthropic-beta` header.
- The [InvokeModel API](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md) reads them from the request body, not from a header. List them in the body’s `anthropic_beta` array, one name for each element, for example `"anthropic_beta": ["feature1", "feature2"]`.

### Endpoint-specific headers

Some beta APIs are scoped to specific endpoints and require a feature-specific beta header on every request:

| Endpoints | Beta header |
|----|----|
| `/v1/agents`, `/v1/sessions`, `/v1/environments` | `managed-agents-2026-04-01` |
| `/v1/tunnels` | `mcp-tunnels-2026-06-22` |
| `/v1/memory_stores` and sub-resources | `agent-memory-2026-07-22` |

The SDK’s `client.beta` namespace adds these headers automatically. Add them yourself only when making raw HTTP requests. See the [Managed Agents overview](../Other/managed-agents-overview.md), [Using agent memory](../Other/managed-agents-memory.md), and the [MCP tunnels reference](../Agents-Tools/agents-and-tools-mcp-tunnels-reference.md#tunnels-api) for details.

Endpoint-specific headers that apply to the same endpoint aren’t always combinable. On memory store endpoints, `agent-memory-2026-07-22` replaces `managed-agents-2026-04-01`: sending both on the same request returns a `400` error. The SDK sends the correct header for each endpoint automatically.

### Version naming conventions

Beta feature names typically follow the pattern `feature-name-YYYY-MM-DD`, where the date indicates when the beta was released. Always use the exact beta feature name as documented.

## Error handling

If you use an invalid beta name, or a beta your organization doesn’t have access to, you’ll receive a `400` error response:

Output



```python
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Unexpected value(s) `invalid-beta-name` for the `anthropic-beta` header. Please consult our documentation at platform.claude.com/docs or try again without the header."
  },
  "request_id": "req_011CcnGfC9fELffo2EALu4Wd"
}
```

## Getting help

For updates to beta features, see the [release notes](../../20-Models/release-notes-overview.md). For help with production issues, contact [support](https://support.claude.com/).

## Next steps



[Errors](errors.md)

Understand the HTTP status codes, error response shape, and request IDs the Claude API returns, and handle errors with the SDK’s typed exceptions.

[API overview](overview.md)

Explore the Claude API’s features, including the APIs in beta.
