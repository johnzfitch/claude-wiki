---
title: "List API Keys - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/api_keys/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:21Z"
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

List






Looking for your API keys? You can view and create them in [Settings → API keys](/settings/keys) in the Claude Console.

# List API Keys

GET/v1/organizations/api_keys

List API Keys

##### Query ParametersExpand Collapse 

after_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

[](#list.after_id)

before_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

[](#list.before_id)

created_by_user_id: optional string



Filter by the ID of the User who created the object.

[](#list.created_by_user_id)



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

[](#list.limit)



status: optional "active" or "archived" or "expired" or "inactive"



Filter by API key status.

One of the following:

"active"



[](#list.status%5B0%5D)

"archived"



[](#list.status%5B1%5D)

"expired"



[](#list.status%5B2%5D)

"inactive"



[](#list.status%5B3%5D)

[](#list.status)

workspace_id: optional string



Filter by Workspace ID.

[](#list.workspace_id)

##### ReturnsExpand Collapse 



data: array of [APIKey](/docs/en/api/$shared#api_key) { id, created_at, created_by, 7 more }

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

[](#list)

first_id: string



First ID in the `data` list. Can be used as the `before_id` for the previous page.

[](#list)

has_more: boolean



Indicates if there are more results in the requested page direction.

[](#list)

last_id: string



Last ID in the `data` list. Can be used as the `after_id` for the next page.

[](#list)

List API Keys



```python
curl https://api.anthropic.com/v1/organizations/api_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
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
