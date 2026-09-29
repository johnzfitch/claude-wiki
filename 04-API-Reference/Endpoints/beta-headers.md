---
title: "Beta headers - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/beta-headers"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:25Z"
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

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta-headers)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


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

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

[API reference](overview.md)Using the API

# Beta headers

Copy page



Access experimental features before they become part of the standard API with the `anthropic-beta` header or the SDKs' `betas` parameter.

Copy page



Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.



Each [client SDK](../Other/cli-sdks-libraries-overview.md) exposes a `beta` namespace for calling the API with beta features enabled.

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

Each feature's documentation states the exact beta name to send. The [API overview](overview.md) lists the APIs currently in beta.

The following examples show the same request with cURL, the `ant` CLI, and the SDKs, using the [context editing](../Guides/build-with-claude-context-editing.md) beta as the example. The SDKs take beta names in the `betas` parameter and send the `anthropic-beta` header for you:

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

The SDKs' `beta` namespaces add these headers automatically. Add them yourself only when making raw HTTP requests. See the [Managed Agents overview](../Other/managed-agents-overview.md), [Using agent memory](../Other/managed-agents-memory.md), and the [MCP tunnels reference](../Agents-Tools/agents-and-tools-mcp-tunnels-reference.md#tunnels-api) for details.

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

For updates to beta features, see the [release notes](../../20-Models/release-notes-overview.md). For help with production issues, contact [support](https://support.claude.com/).

## Next steps



[Errors](errors.md)

Understand the HTTP status codes, error response shape, and request IDs the Claude API returns, and handle errors with the SDKs' typed exceptions.

[API overview](overview.md)

Explore the Claude API's features, including the APIs currently in beta.
