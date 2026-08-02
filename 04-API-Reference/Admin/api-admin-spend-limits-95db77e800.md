---
title: "Spend Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/spend_limits"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:11Z"
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

Spend limits




# Spend Limits

##### [Set Spend Limit](/docs/en/api/admin/spend_limits/create)

POST/v1/organizations/spend_limits

##### [Get Spend Limit](/docs/en/api/admin/spend_limits/retrieve)

GET/v1/organizations/spend_limits/{spend_limit_id}

##### [Delete Spend Limit](/docs/en/api/admin/spend_limits/delete)

DELETE/v1/organizations/spend_limits/{spend_limit_id}

##### [List Effective Spend Limits](/docs/en/api/admin/spend_limits/list_effective)

GET/v1/organizations/spend_limits/effective

##### ModelsExpand Collapse 

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



SpendSummary object { actor, amount, currency, 5 more }



Per-member effective-limit report row (GET /spend_limits/effective).



actor: object { deleted, email_address, name, 2 more }



A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.

deleted: boolean



[](#spend_summary.actor.deleted)

email_address: string



[](#spend_summary.actor.email_address)

name: string



[](#spend_summary.actor.name)

type: "user_actor"



[](#spend_summary.actor.type)

user_id: string



[](#spend_summary.actor.user_id)

[](#spend_summary.actor)

amount: string



[](#spend_summary.amount)

currency: string



[](#spend_summary.currency)



period: "daily" or "monthly" or "weekly"



One of the following:

"daily"



[](#spend_summary.period%5B0%5D)

"monthly"



[](#spend_summary.period%5B1%5D)

"weekly"



[](#spend_summary.period%5B2%5D)

[](#spend_summary.period)

period_to_date_spend: string



[](#spend_summary.period_to_date_spend)



scope: object { type, user_id }



type: "user"



[](#spend_summary.scope.type)

user_id: string



[](#spend_summary.scope.user_id)

[](#spend_summary.scope)



source: object { type, user_id } or object { seat_tier, type } or object { rbac_group_id, type } or 2 more



One of the following:



User object { type, user_id }



type: "user"



[](#spend_summary.source%5B0%5D.type)

user_id: string



[](#spend_summary.source%5B0%5D.user_id)

[](#spend_summary.source%5B0%5D)



SeatTier object { seat_tier, type }



seat_tier: string



[](#spend_summary.source%5B1%5D.seat_tier)

type: "seat_tier"



[](#spend_summary.source%5B1%5D.type)

[](#spend_summary.source%5B1%5D)



RbacGroup object { rbac_group_id, type }



rbac_group_id: string



[](#spend_summary.source%5B2%5D.rbac_group_id)

type: "rbac_group"



[](#spend_summary.source%5B2%5D.type)

[](#spend_summary.source%5B2%5D)



OrganizationService object { service, type }



service: string



[](#spend_summary.source%5B3%5D.service)

type: "organization_service"



[](#spend_summary.source%5B3%5D.type)

[](#spend_summary.source%5B3%5D)



Organization object { type }



type: "organization"



[](#spend_summary.source%5B4%5D.type)

[](#spend_summary.source%5B4%5D)

[](#spend_summary.source)

spend_limit_id: string



[](#spend_summary.spend_limit_id)

[](#spend_summary)



SpendLimitDeleteResponse object { id, type }



id: string



[](#spend_limit_delete_response.id)

type: "spend_limit_deleted"



[](#spend_limit_delete_response.type)

[](#spend_limit_delete_response)

#### Spend LimitsIncrease Requests

##### [List Spend Limit Increase Requests](/docs/en/api/admin/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

##### [Get Spend Limit Increase Request](/docs/en/api/admin/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

##### [Approve Spend Limit Increase Request](/docs/en/api/admin/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

##### [Deny Spend Limit Increase Request](/docs/en/api/admin/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny
