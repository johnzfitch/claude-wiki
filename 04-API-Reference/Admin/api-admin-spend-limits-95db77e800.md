---
title: "Spend Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/spend_limits"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:42:47Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fspend_limits)

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


Webhooks


Unwrap


Parse Unverified


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits


Set Spend Limit


Get Spend Limit


Delete Spend Limit


List Effective Spend Limits

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


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



1.  [API reference](/docs/en/api/http)
2.  [Admin](/docs/en/api/http/admin)

# Spend Limits

##### [Set Spend Limit](/docs/en/api/http/admin/spend_limits/create)

POST/v1/organizations/spend_limits

##### [Get Spend Limit](/docs/en/api/http/admin/spend_limits/retrieve)

GET/v1/organizations/spend_limits/{spend_limit_id}

##### [Delete Spend Limit](/docs/en/api/http/admin/spend_limits/delete)

DELETE/v1/organizations/spend_limits/{spend_limit_id}

##### [List Effective Spend Limits](/docs/en/api/http/admin/spend_limits/list_effective)

GET/v1/organizations/spend_limits/effective

##### Models



SpendLimit object{ id, amount, created_at, 5 more }



A configured spend limit: a cap on metered spend for one scope and period.



SpendSummary object{ actor, amount, currency, 5 more }



Per-member effective-limit report row (`GET /spend_limits/effective`).



SpendLimitDeleteResponse object{ id, type }



id: string





type: "spend_limit_deleted"



defaultspend_limit_deleted

#### Spend Limits[Increase Requests](/docs/en/api/http/admin/spend_limits/increase_requests)

##### [List Spend Limit Increase Requests](/docs/en/api/http/admin/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

##### [Get Spend Limit Increase Request](/docs/en/api/http/admin/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

##### [Approve Spend Limit Increase Request](/docs/en/api/http/admin/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

##### [Deny Spend Limit Increase Request](/docs/en/api/http/admin/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny
