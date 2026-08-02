---
title: "RBAC Groups - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/rbac_groups"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:31Z"
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

Rbac groups




# RBAC Groups

##### [List RBAC Groups](/docs/en/api/admin/rbac_groups/list)

GET/v1/organizations/rbac_groups

##### [Get RBAC Group](/docs/en/api/admin/rbac_groups/retrieve)

GET/v1/organizations/rbac_groups/{group_id}

##### [Create RBAC Group](/docs/en/api/admin/rbac_groups/create)

POST/v1/organizations/rbac_groups

##### [Update RBAC Group](/docs/en/api/admin/rbac_groups/update)

POST/v1/organizations/rbac_groups/{group_id}

##### [Delete RBAC Group](/docs/en/api/admin/rbac_groups/delete)

DELETE/v1/organizations/rbac_groups/{group_id}

##### ModelsExpand Collapse 



RbacGroup object { id, created_at, name, 4 more }



id: string



ID of the RBAC Group.

[](#rbac_group.id)

created_at: string



RFC 3339 timestamp of when the RBAC Group was created.

[](#rbac_group.created_at)

name: string



Name of the RBAC Group. Not uniqueness-enforced.

[](#rbac_group.name)

roles: array of string



RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

[](#rbac_group.roles)



source_type: "direct" or "scim"



How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

One of the following:

"direct"



[](#rbac_group.source_type%5B0%5D)

"scim"



[](#rbac_group.source_type%5B1%5D)

[](#rbac_group.source_type)



type: "rbac_group"



Object type.

For RBAC Groups, this is always `"rbac_group"`.

[](#rbac_group.type)

updated_at: string



RFC 3339 timestamp of when the RBAC Group was last updated.

[](#rbac_group.updated_at)

[](#rbac_group)



RbacGroupDeleted object { id, type }



id: string



ID of the RBAC Group.

[](#rbac_group_deleted.id)



type: "rbac_group_deleted"



Deleted object type.

For RBAC Groups, this is always `"rbac_group_deleted"`.

[](#rbac_group_deleted.type)

[](#rbac_group_deleted)

#### RBAC GroupsMembers

##### [List RBAC Group Members](/docs/en/api/admin/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{group_id}/members

##### [Add RBAC Group Member](/docs/en/api/admin/rbac_groups/members/create)

POST/v1/organizations/rbac_groups/{group_id}/members

##### [Remove RBAC Group Member](/docs/en/api/admin/rbac_groups/members/delete)

DELETE/v1/organizations/rbac_groups/{group_id}/members/{user_id}
