---
title: "Service Accounts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/service_accounts"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:41:38Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fservice_accounts)

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

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts


Create Service Account


Get Service Account


List Service Accounts


Update Service Account


Archive Service Account

Workspaces

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

# Service Accounts

##### [Create Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/create)

POST/v1/organizations/service_accounts

##### [Get Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/retrieve)

GET/v1/organizations/service_accounts/{service_account_id}

##### [List Service Accounts](https://platform.claude.com/docs/en/api/http/admin/service_accounts/list)

GET/v1/organizations/service_accounts

##### [Update Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/update)

POST/v1/organizations/service_accounts/{service_account_id}

##### [Archive Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/archive)

POST/v1/organizations/service_accounts/{service_account_id}/archive

##### Models



ServiceAccount object{ id, archived_at, archived_by_actor_id, 8 more }



Named non-human identity within the caller's organization.

A service account is a pure identity: name + org. Authorization lives on whatever references it (federation rules).

#### Service Accounts[Workspaces](https://platform.claude.com/docs/en/api/http/admin/service_accounts/workspaces)

##### [Add Workspace To Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/workspaces/create)

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

##### [List Workspaces For Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/workspaces/list)

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

##### [Remove Workspace From Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/workspaces/delete)

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}
