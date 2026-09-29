---
title: "Beta headers - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/beta-headers"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:25Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta-headers)

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

# Beta headers

Copy page



Access experimental features before they become part of the standard API with the `anthropic-beta` header or the SDKs' `betas` parameter.

Copy page



Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.



Each [client SDK](/docs/en/cli-sdks-libraries/overview) exposes a `beta` namespace for calling the API with beta features enabled.

## How to use beta headers

To access beta features, include the `anthropic-beta` header in your API requests:

```python
POST /v1/messages
x-api-key: YOUR_API_KEY
anthropic-version: 2023-06-01
anthropic-beta: BETA_FEATURE_NAME
content-type: application/json
```



Each feature's documentation states the exact beta name to send. The [API overview](/docs/en/api/overview) lists the APIs currently in beta.

The following examples show the same request with cURL, the `ant` CLI, and the SDKs, using the [context editing](/docs/en/build-with-claude/context-editing) beta as the example. The SDKs take beta names in the `betas` parameter and send the `anthropic-beta` header for you:

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

When using an SDK, list each feature in the `betas` parameter (for example, `betas=["feature1", "feature2"]`). With the CLI, pass a single `--beta` flag with the feature names separated by commas (for example, `--beta feature1,feature2`). You can also repeat the flag (for example, `--beta feature1 --beta feature2`).

### Endpoint-specific headers

Some beta APIs are scoped to specific endpoints and require a feature-specific beta header on every request:

| Endpoints                                        | Beta header                 |
|--------------------------------------------------|-----------------------------|
| `/v1/agents`, `/v1/sessions`, `/v1/environments` | `managed-agents-2026-04-01` |
| `/v1/tunnels`                                    | `mcp-tunnels-2026-06-22`    |
| `/v1/memory_stores` and sub-resources            | `agent-memory-2026-07-22`   |

The SDKs' `beta` namespaces add these headers automatically. Add them yourself only when making raw HTTP requests. See the [Managed Agents overview](/docs/en/managed-agents/overview), [Using agent memory](/docs/en/managed-agents/memory), and the [MCP tunnels reference](/docs/en/agents-and-tools/mcp-tunnels/reference#tunnels-api) for details.

Endpoint-specific headers that apply to the same endpoint aren't always combinable. On memory store endpoints, `agent-memory-2026-07-22` replaces `managed-agents-2026-04-01`: sending both on the same request returns a `400` error. The client SDKs send the correct header for each endpoint automatically.

### Version naming conventions

Beta feature names typically follow the pattern `feature-name-YYYY-MM-DD`, where the date indicates when the beta was released. Always use the exact beta feature name as documented.

## Error handling

If you use an invalid beta name, or a beta your organization doesn't have access to, you'll receive a `400` error response:

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

For updates to beta features, see the [release notes](/docs/en/release-notes/overview). For help with production issues, contact [support](https://support.claude.com/).

## Next steps



[Errors](/docs/en/api/errors)

Understand the HTTP status codes, error response shape, and request IDs the Claude API returns, and handle errors with the SDKs' typed exceptions.

[API overview](/docs/en/api/overview)

Explore the Claude API's features, including the APIs currently in beta.
