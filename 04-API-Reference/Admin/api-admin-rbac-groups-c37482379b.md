---
title: "RBAC Groups - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/rbac_groups"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:42:05Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Frbac_groups)

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


List RBAC Groups


Get RBAC Group


Create RBAC Group


Update RBAC Group


Delete RBAC Group

Members

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

# RBAC Groups

##### [List RBAC Groups](/docs/en/api/http/admin/rbac_groups/list)

GET/v1/organizations/rbac_groups

##### [Get RBAC Group](/docs/en/api/http/admin/rbac_groups/retrieve)

GET/v1/organizations/rbac_groups/{group_id}

##### [Create RBAC Group](/docs/en/api/http/admin/rbac_groups/create)

POST/v1/organizations/rbac_groups

##### [Update RBAC Group](/docs/en/api/http/admin/rbac_groups/update)

POST/v1/organizations/rbac_groups/{group_id}

##### [Delete RBAC Group](/docs/en/api/http/admin/rbac_groups/delete)

DELETE/v1/organizations/rbac_groups/{group_id}

##### Models



RbacGroup object{ id, created_at, name, 4 more }



id: string



ID of the RBAC Group.



created_at: string



RFC 3339 timestamp of when the RBAC Group was created.

formatdate-time

name: string



Name of the RBAC Group. Not uniqueness-enforced.

roles: array of string or null



RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.



source_type: "direct" or "scim"



How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

One of the following:

"direct"



"scim"





type: "rbac_group"



Object type.

For RBAC Groups, this is always `"rbac_group"`.

defaultrbac_group



updated_at: string



RFC 3339 timestamp of when the RBAC Group was last updated.

formatdate-time



RbacGroupDeleted object{ id, type }



id: string



ID of the RBAC Group.



type: "rbac_group_deleted"



Deleted object type.

For RBAC Groups, this is always `"rbac_group_deleted"`.

defaultrbac_group_deleted

#### RBAC Groups[Members](/docs/en/api/http/admin/rbac_groups/members)

##### [List RBAC Group Members](/docs/en/api/http/admin/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{group_id}/members

##### [Add RBAC Group Member](/docs/en/api/http/admin/rbac_groups/members/create)

POST/v1/organizations/rbac_groups/{group_id}/members

##### [Remove RBAC Group Member](/docs/en/api/http/admin/rbac_groups/members/delete)

DELETE/v1/organizations/rbac_groups/{group_id}/members/{user_id}
