---
title: "Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:42:02Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Ffederation_rules%2Fworkspaces)

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

Federation Issuers

Federation Rules


Create Federation Rule


Get Federation Rule


List Federation Rules


Update Federation Rule


Archive Federation Rule

Workspaces


List Federation Rule Workspaces


Add Federation Rule Workspace


Remove Federation Rule Workspace

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
3.  [Federation Rules](https://platform.claude.com/docs/en/api/http/admin/federation_rules)

# Workspaces

##### [List Federation Rule Workspaces](https://platform.claude.com/docs/en/api/http/admin/federation_rules/workspaces/list)

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

##### [Add Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/admin/federation_rules/workspaces/create)

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

##### [Remove Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/admin/federation_rules/workspaces/delete)

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}

##### Models



WorkspaceCreateResponse object{ created_at, created_by_actor_id, federation_rule_id, 3 more }





created_at: string



When this workspace was enabled for the rule.

formatdate-time

created_by_actor_id: string or null



Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

federation_rule_id: string



Tagged ID of the federation rule.



type: "federation_rule_workspace"



defaultfederation_rule_workspace

workspace_id: string



Tagged ID of the workspace this rule is enabled for.

workspace_name: string or null



Workspace display name. Populated when listing; null in the enable response.



WorkspaceListResponse object{ created_at, created_by_actor_id, federation_rule_id, 3 more }





created_at: string



When this workspace was enabled for the rule.

formatdate-time

created_by_actor_id: string or null



Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

federation_rule_id: string



Tagged ID of the federation rule.



type: "federation_rule_workspace"



defaultfederation_rule_workspace

workspace_id: string



Tagged ID of the workspace this rule is enabled for.

workspace_name: string or null



Workspace display name. Populated when listing; null in the enable response.



WorkspaceDeleteResponse object{ federation_rule_id, type, workspace_id }



federation_rule_id: string



Tagged ID of the federation rule.



type: "federation_rule_workspace_deleted"



defaultfederation_rule_workspace_deleted

workspace_id: string



Tagged ID of the workspace named in the delete request. Removal is idempotent.
