---
title: "Get Spend Limit Increase Request - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:38Z"
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


List Spend Limit Increase Requests


Get Spend Limit Increase Request


Approve Spend Limit Increase Request


Deny Spend Limit Increase Request

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

# Get Spend Limit Increase Request

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

Retrieve a spend limit increase request.

While `pending`, the response includes a live `spend_summary` for the requester at the request's period.

##### Path ParametersExpand Collapse 

spend_limit_increase_request_id: string



ID of the spend limit increase request.

[](#retrieve.spend_limit_increase_request_id)

##### ReturnsExpand Collapse 



SpendLimitIncreaseRequest object { id, actor, created_at, 6 more }



id: string



[](#spend_limit_increase_request.id)



actor: object { deleted, email_address, name, 2 more }



A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.

deleted: boolean



[](#spend_limit_increase_request.actor.deleted)

email_address: string



[](#spend_limit_increase_request.actor.email_address)

name: string



[](#spend_limit_increase_request.actor.name)

type: "user_actor"



[](#spend_limit_increase_request.actor.type)

user_id: string



[](#spend_limit_increase_request.actor.user_id)

[](#spend_limit_increase_request.actor)

created_at: string



[](#spend_limit_increase_request.created_at)



period: "daily" or "monthly" or "weekly"



One of the following:

"daily"



[](#spend_limit_increase_request.period%5B0%5D)

"monthly"



[](#spend_limit_increase_request.period%5B1%5D)

"weekly"



[](#spend_limit_increase_request.period%5B2%5D)

[](#spend_limit_increase_request.period)

resolved_at: string



[](#spend_limit_increase_request.resolved_at)



resolved_by: object { deleted, email_address, name, 2 more } or object { scoped_api_key_id, type }



A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.

One of the following:



UserActor object { deleted, email_address, name, 2 more }



A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.

deleted: boolean



[](#spend_limit_increase_request.resolved_by%5B0%5D.deleted)

email_address: string



[](#spend_limit_increase_request.resolved_by%5B0%5D.email_address)

name: string



[](#spend_limit_increase_request.resolved_by%5B0%5D.name)

type: "user_actor"



[](#spend_limit_increase_request.resolved_by%5B0%5D.type)

user_id: string



[](#spend_limit_increase_request.resolved_by%5B0%5D.user_id)

[](#spend_limit_increase_request.resolved_by%5B0%5D)



ScopedAPIKeyActor object { scoped_api_key_id, type }



A scoped Admin API key acting on behalf of the organization.

scoped_api_key_id: string



[](#spend_limit_increase_request.resolved_by%5B1%5D.scoped_api_key_id)

type: "scoped_api_key_actor"



[](#spend_limit_increase_request.resolved_by%5B1%5D.type)

[](#spend_limit_increase_request.resolved_by%5B1%5D)

[](#spend_limit_increase_request.resolved_by)



spend_summary: [SpendSummary](/docs/en/api/admin/spend_limits#spend_summary) { actor, amount, currency, 5 more }



Per-member effective-limit report row (GET /spend_limits/effective).



actor: object { deleted, email_address, name, 2 more }



A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.

deleted: boolean



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.actor.deleted)

email_address: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.actor.email_address)

name: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.actor.name)

type: "user_actor"



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.actor.type)

user_id: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.actor.user_id)

[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.actor)

amount: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.amount)

currency: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.currency)



period: "daily" or "monthly" or "weekly"



One of the following:

"daily"



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.period%5B0%5D)

"monthly"



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.period%5B1%5D)

"weekly"



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.period%5B2%5D)

[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.period)

period_to_date_spend: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.period_to_date_spend)



scope: object { type, user_id }



type: "user"



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.scope.type)

user_id: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.scope.user_id)

[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.scope)



source: object { type, user_id } or object { seat_tier, type } or object { rbac_group_id, type } or 2 more



One of the following:



User object { type, user_id }



type: "user"



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B0%5D.type)

user_id: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B0%5D.user_id)

[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B0%5D)



SeatTier object { seat_tier, type }



seat_tier: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B1%5D.seat_tier)

type: "seat_tier"



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B1%5D.type)

[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B1%5D)



RbacGroup object { rbac_group_id, type }



rbac_group_id: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B2%5D.rbac_group_id)

type: "rbac_group"



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B2%5D.type)

[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B2%5D)



OrganizationService object { service, type }



service: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B3%5D.service)

type: "organization_service"



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B3%5D.type)

[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B3%5D)



Organization object { type }



type: "organization"



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B4%5D.type)

[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source%5B4%5D)

[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.source)

spend_limit_id: string



[](#spend_limit_increase_request.spend_summary%20%2B%20(resource)%20admin.spend_limits.spend_limit_id)

[](#spend_limit_increase_request.spend_summary)



status: "approved" or "denied" or "pending"



One of the following:

"approved"



[](#spend_limit_increase_request.status%5B0%5D)

"denied"



[](#spend_limit_increase_request.status%5B1%5D)

"pending"



[](#spend_limit_increase_request.status%5B2%5D)

[](#spend_limit_increase_request.status)

type: "spend_limit_increase_request"



[](#spend_limit_increase_request.type)

[](#spend_limit_increase_request)

Get Spend Limit Increase Request



```python
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "monthly",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_id"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "monthly",
    "period_to_date_spend": "period_to_date_spend",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    },
    "source": {
      "type": "user",
      "user_id": "user_id"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "monthly",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_id"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "monthly",
    "period_to_date_spend": "period_to_date_spend",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    },
    "source": {
      "type": "user",
      "user_id": "user_id"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
