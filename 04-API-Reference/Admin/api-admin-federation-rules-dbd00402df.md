---
title: "Federation Rules - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/federation_rules"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:43:00Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Ffederation_rules)

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

Rate Limits

Service Accounts

Federation Issuers

Federation Rules


Create Federation Rule


Get Federation Rule


List Federation Rules


Update Federation Rule


Archive Federation Rule

Workspaces

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

# Federation Rules

##### [Create Federation Rule](/docs/en/api/http/admin/federation_rules/create)

POST/v1/organizations/federation_rules

##### [Get Federation Rule](/docs/en/api/http/admin/federation_rules/retrieve)

GET/v1/organizations/federation_rules/{federation_rule_id}

##### [List Federation Rules](/docs/en/api/http/admin/federation_rules/list)

GET/v1/organizations/federation_rules

##### [Update Federation Rule](/docs/en/api/http/admin/federation_rules/update)

POST/v1/organizations/federation_rules/{federation_rule_id}

##### [Archive Federation Rule](/docs/en/api/http/admin/federation_rules/archive)

POST/v1/organizations/federation_rules/{federation_rule_id}/archive

##### Models



FederationRule object{ id, applies_to_all_workspaces, archived_at, 17 more }



Authorization rule binding an external OIDC identity to Anthropic.

Evaluates the match conditions and mints an OAuth access token for the resolved target, scoped to a single workspace where the rule is enabled (chosen by the caller at exchange time when the rule is enabled for more than one). For rules enabled via `workspace_ids` or `applies_to_all_workspaces`, the target service account must be a member of that workspace (it is implicitly a member of the default workspace); rules carrying only the legacy `workspace_id` binding do not enforce this.

#### Federation Rules[Workspaces](/docs/en/api/http/admin/federation_rules/workspaces)

##### [List Federation Rule Workspaces](/docs/en/api/http/admin/federation_rules/workspaces/list)

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

##### [Add Federation Rule Workspace](/docs/en/api/http/admin/federation_rules/workspaces/create)

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

##### [Remove Federation Rule Workspace](/docs/en/api/http/admin/federation_rules/workspaces/delete)

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}
