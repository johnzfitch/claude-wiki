---
title: "Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:26Z"
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

Rate Limits

Service Accounts

Federation Issuers

Federation Rules


Create Federation Rule


Get Federation Rule


List Federation Rules


Update Federation Rule


Archive Federation Rule

Workspaces


List Federation Rule Workspaces


Add Federation Rule Workspace


Remove Federation Rule Workspace

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

Workspaces




# Workspaces

##### [List Federation Rule Workspaces](/docs/en/api/admin/federation_rules/workspaces/list)

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

##### [Add Federation Rule Workspace](/docs/en/api/admin/federation_rules/workspaces/create)

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

##### [Remove Federation Rule Workspace](/docs/en/api/admin/federation_rules/workspaces/delete)

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}

##### ModelsExpand Collapse 



WorkspaceListResponse object { created_at, created_by_actor_id, federation_rule_id, 3 more }



created_at: string



When this workspace was enabled for the rule.

[](#workspace_list_response.created_at)

created_by_actor_id: string



Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

[](#workspace_list_response.created_by_actor_id)

federation_rule_id: string



Tagged ID of the federation rule.

[](#workspace_list_response.federation_rule_id)

type: "federation_rule_workspace"



[](#workspace_list_response.type)

workspace_id: string



Tagged ID of the workspace this rule is enabled for.

[](#workspace_list_response.workspace_id)

workspace_name: string



Workspace display name. Populated when listing; null in the enable response.

[](#workspace_list_response.workspace_name)

[](#workspace_list_response)



WorkspaceCreateResponse object { created_at, created_by_actor_id, federation_rule_id, 3 more }



created_at: string



When this workspace was enabled for the rule.

[](#workspace_create_response.created_at)

created_by_actor_id: string



Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

[](#workspace_create_response.created_by_actor_id)

federation_rule_id: string



Tagged ID of the federation rule.

[](#workspace_create_response.federation_rule_id)

type: "federation_rule_workspace"



[](#workspace_create_response.type)

workspace_id: string



Tagged ID of the workspace this rule is enabled for.

[](#workspace_create_response.workspace_id)

workspace_name: string



Workspace display name. Populated when listing; null in the enable response.

[](#workspace_create_response.workspace_name)

[](#workspace_create_response)



WorkspaceDeleteResponse object { federation_rule_id, type, workspace_id }



federation_rule_id: string



Tagged ID of the federation rule.

[](#workspace_delete_response.federation_rule_id)

type: "federation_rule_workspace_deleted"



[](#workspace_delete_response.type)

workspace_id: string



Tagged ID of the workspace named in the delete request. Removal is idempotent.

[](#workspace_delete_response.workspace_id)

[](#workspace_delete_response)
