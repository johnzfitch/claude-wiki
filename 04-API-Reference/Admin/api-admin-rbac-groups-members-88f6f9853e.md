---
title: "Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/rbac_groups/members"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:32Z"
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


List RBAC Groups


Get RBAC Group


Create RBAC Group


Update RBAC Group


Delete RBAC Group

Members


List RBAC Group Members


Add RBAC Group Member


Remove RBAC Group Member

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

##### [List RBAC Group Members](/docs/en/api/admin/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{group_id}/members

##### [Add RBAC Group Member](/docs/en/api/admin/rbac_groups/members/create)

POST/v1/organizations/rbac_groups/{group_id}/members

##### [Remove RBAC Group Member](/docs/en/api/admin/rbac_groups/members/delete)

DELETE/v1/organizations/rbac_groups/{group_id}/members/{user_id}

##### ModelsExpand Collapse 



RbacGroupMember object { created_at, email, group_id, 2 more }



created_at: string



RFC 3339 timestamp of when the User was added to the RBAC Group.

[](#rbac_group_member.created_at)

email: string



Email of the User.

[](#rbac_group_member.email)

group_id: string



ID of the RBAC Group.

[](#rbac_group_member.group_id)



type: "rbac_group_member"



Object type.

For RBAC Group Members, this is always `"rbac_group_member"`.

[](#rbac_group_member.type)

user_id: string



ID of the User.

[](#rbac_group_member.user_id)

[](#rbac_group_member)



RbacGroupMemberDeleted object { group_id, type, user_id }



group_id: string



ID of the RBAC Group.

[](#rbac_group_member_deleted.group_id)

type: "rbac_group_member_deleted"



Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

[](#rbac_group_member_deleted.type)

user_id: string



ID of the User.

[](#rbac_group_member_deleted.user_id)

[](#rbac_group_member_deleted)
