---
title: "Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/members"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:38:02Z"
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


Create Workspace


Get Workspace


List Workspaces


Update Workspace


Archive Workspace

Members


Create Workspace Member


Get Workspace Member


List Workspace Members


Update Workspace Member


Delete Workspace Member

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


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Members




# Members

##### [Create Workspace Member](/docs/en/api/admin/workspaces/members/create)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](/docs/en/api/admin/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [List Workspace Members](/docs/en/api/admin/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Update Workspace Member](/docs/en/api/admin/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](/docs/en/api/admin/workspaces/members/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### ModelsExpand Collapse 



WorkspaceMember object { type, user_id, workspace_id, workspace_role }





type: "workspace_member"



Object type.

For Workspace Members, this is always `"workspace_member"`.

[](#workspaceMember.type)

user_id: string



ID of the User.

[](#workspaceMember.user_id)

workspace_id: string



ID of the Workspace.

[](#workspaceMember.workspace_id)



workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more



Role of the Workspace Member.

One of the following:

"workspace_admin"



[](#workspaceMember.workspace_role%5B0%5D)

"workspace_billing"



[](#workspaceMember.workspace_role%5B1%5D)

"workspace_developer"



[](#workspaceMember.workspace_role%5B2%5D)

"workspace_restricted_developer"



[](#workspaceMember.workspace_role%5B3%5D)

"workspace_user"



[](#workspaceMember.workspace_role%5B4%5D)

[](#workspaceMember.workspace_role)

[](#workspaceMember)



MemberDeleteResponse object { type, user_id, workspace_id }





type: "workspace_member_deleted"



Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

[](#member_delete_response.type)

user_id: string



ID of the User.

[](#member_delete_response.user_id)

workspace_id: string



ID of the Workspace.

[](#member_delete_response.workspace_id)
