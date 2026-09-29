---
title: "Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:41:42Z"
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

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fworkspaces)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


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

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Admin](http-admin.md)

# Workspaces

##### [Create Workspace](https://platform.claude.com/docs/en/api/http/admin/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](https://platform.claude.com/docs/en/api/http/admin/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [List Workspaces](https://platform.claude.com/docs/en/api/http/admin/workspaces/list)

GET/v1/organizations/workspaces

##### [Update Workspace](https://platform.claude.com/docs/en/api/http/admin/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](https://platform.claude.com/docs/en/api/http/admin/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

#### Workspaces[Members](https://platform.claude.com/docs/en/api/http/admin/workspaces/members)

##### [Create Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/members/create)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [List Workspace Members](https://platform.claude.com/docs/en/api/http/admin/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Update Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/members/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

#### Workspaces[Rate Limits](https://platform.claude.com/docs/en/api/http/admin/workspaces/rate_limits)

##### [List Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/admin/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

#### Workspaces[Service Accounts](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts)

##### [Create Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/create)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

##### [Get Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### [List Service Account Workspace Members](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

##### [Update Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### [Delete Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}
