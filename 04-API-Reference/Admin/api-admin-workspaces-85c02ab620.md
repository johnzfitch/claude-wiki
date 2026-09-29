---
title: "Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:41:42Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fworkspaces)

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


Create Workspace


Get Workspace


List Workspaces


Update Workspace


Archive Workspace

Members

Rate Limits

Service Accounts

API Keys

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

# Workspaces

##### [Create Workspace](/docs/en/api/http/admin/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](/docs/en/api/http/admin/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [List Workspaces](/docs/en/api/http/admin/workspaces/list)

GET/v1/organizations/workspaces

##### [Update Workspace](/docs/en/api/http/admin/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](/docs/en/api/http/admin/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

#### Workspaces[Members](/docs/en/api/http/admin/workspaces/members)

##### [Create Workspace Member](/docs/en/api/http/admin/workspaces/members/create)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](/docs/en/api/http/admin/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [List Workspace Members](/docs/en/api/http/admin/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Update Workspace Member](/docs/en/api/http/admin/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](/docs/en/api/http/admin/workspaces/members/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

#### Workspaces[Rate Limits](/docs/en/api/http/admin/workspaces/rate_limits)

##### [List Workspace Rate Limits](/docs/en/api/http/admin/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

#### Workspaces[Service Accounts](/docs/en/api/http/admin/workspaces/service_accounts)

##### [Create Service Account Workspace Member](/docs/en/api/http/admin/workspaces/service_accounts/create)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

##### [Get Service Account Workspace Member](/docs/en/api/http/admin/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### [List Service Account Workspace Members](/docs/en/api/http/admin/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

##### [Update Service Account Workspace Member](/docs/en/api/http/admin/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### [Delete Service Account Workspace Member](/docs/en/api/http/admin/workspaces/service_accounts/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}
