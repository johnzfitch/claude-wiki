---
title: "Get Spend Limit - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/spend_limits/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:40:18Z"
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

External Keys

Usage Report

Cost Report

Analytics

Spend Limits


Set Spend Limit


Get Spend Limit


Delete Spend Limit


List Effective Spend Limits

Increase Requests

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

# Get Spend Limit

GET/v1/organizations/spend_limits/{spend_limit_id}

Retrieve a spend limit by ID.

##### Path ParametersExpand Collapse 

spend_limit_id: string



ID of the Spend Limit.

[](#retrieve.spend_limit_id)

##### ReturnsExpand Collapse 



SpendLimit object { id, amount, created_at, 5 more }



id: string



[](#spend_limit.id)

amount: string



[](#spend_limit.amount)

created_at: string



[](#spend_limit.created_at)

currency: string



[](#spend_limit.currency)



period: "daily" or "monthly" or "weekly"



One of the following:

"daily"



[](#spend_limit.period%5B0%5D)

"monthly"



[](#spend_limit.period%5B1%5D)

"weekly"



[](#spend_limit.period%5B2%5D)

[](#spend_limit.period)



scope: object { type, user_id } or object { seat_tier, type } or object { rbac_group_id, type } or 2 more



One of the following:



User object { type, user_id }



type: "user"



[](#spend_limit.scope%5B0%5D.type)

user_id: string



[](#spend_limit.scope%5B0%5D.user_id)

[](#spend_limit.scope%5B0%5D)



SeatTier object { seat_tier, type }



seat_tier: string



[](#spend_limit.scope%5B1%5D.seat_tier)

type: "seat_tier"



[](#spend_limit.scope%5B1%5D.type)

[](#spend_limit.scope%5B1%5D)



RbacGroup object { rbac_group_id, type }



rbac_group_id: string



[](#spend_limit.scope%5B2%5D.rbac_group_id)

type: "rbac_group"



[](#spend_limit.scope%5B2%5D.type)

[](#spend_limit.scope%5B2%5D)



OrganizationService object { service, type }



service: string



[](#spend_limit.scope%5B3%5D.service)

type: "organization_service"



[](#spend_limit.scope%5B3%5D.type)

[](#spend_limit.scope%5B3%5D)



Organization object { type }



type: "organization"



[](#spend_limit.scope%5B4%5D.type)

[](#spend_limit.scope%5B4%5D)

[](#spend_limit.scope)

type: "spend_limit"



[](#spend_limit.type)

updated_at: string



[](#spend_limit.updated_at)

[](#spend_limit)

Get Spend Limit



```python
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "period": "monthly",
  "scope": {
    "type": "user",
    "user_id": "user_id"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "period": "monthly",
  "scope": {
    "type": "user",
    "user_id": "user_id"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
