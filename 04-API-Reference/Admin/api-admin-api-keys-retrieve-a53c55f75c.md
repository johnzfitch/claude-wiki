---
title: "Retrieve API Key (Admin API) - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/api_keys/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:38:56Z"
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


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys


Retrieve API Key (Admin API)


List API Keys


Update API Key

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Retrieve






Looking for your API keys? You can view and create them in [Settings → API keys](/settings/keys) in the Claude Console.

# Retrieve API Key (Admin API)

GET/v1/organizations/api_keys/{api_key_id}

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](https://platform.claude.com/settings/keys) in the Claude Console.

##### Path ParametersExpand Collapse 

api_key_id: string



ID of the API key.

[](#retrieve.api_key_id)

##### ReturnsExpand Collapse 



APIKey object { id, created_at, created_by, 7 more }



id: string



ID of the API key.

[](#api_key.id)

created_at: string



RFC 3339 datetime string indicating when the API Key was created.

[](#api_key.created_at)



created_by: object { id, type }



The ID and type of the actor that created the API key.

id: string



ID of the actor that created the object.

[](#api_key.created_by.id)

type: string



Type of the actor that created the object.

[](#api_key.created_by.type)

[](#api_key.created_by)

expires_at: string



RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

[](#api_key.expires_at)

name: string



Name of the API key.

[](#api_key.name)

partial_key_hint: string



Partially redacted hint for the API key.

[](#api_key.partial_key_hint)



principal: object { id, type }



The ID and type of the principal the API key acts as, or `null` if the key is not bound to a principal.

id: string



ID of the principal the API key acts as: a User ID (`user_...`) when the type is `user`, or a Service Account ID (`svac_...`) when the type is `service_account`.

[](#api_key.principal.id)



type: "service_account" or "user"



Type of the principal the API key acts as.

One of the following:

"service_account"



[](#api_key.principal.type%5B0%5D)

"user"



[](#api_key.principal.type%5B1%5D)

[](#api_key.principal.type)

[](#api_key.principal)



status: "active" or "archived" or "expired" or "inactive"



Status of the API key.

One of the following:

"active"



[](#api_key.status%5B0%5D)

"archived"



[](#api_key.status%5B1%5D)

"expired"



[](#api_key.status%5B2%5D)

"inactive"



[](#api_key.status%5B3%5D)

[](#api_key.status)



type: "api_key"



Object type.

For API Keys, this is always `"api_key"`.

[](#api_key.type)

workspace_id: string



ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.

[](#api_key.workspace_id)

[](#api_key)

Retrieve API Key (Admin API)



```python
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
