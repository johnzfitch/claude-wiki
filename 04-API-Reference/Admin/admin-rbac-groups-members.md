---
title: "Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/rbac_groups/members"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:42:06Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Frbac_groups%2Fmembers)

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


List RBAC Groups


Get RBAC Group


Create RBAC Group


Update RBAC Group


Delete RBAC Group

Members


List RBAC Group Members


Add RBAC Group Member


Remove RBAC Group Member

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

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Admin](http-admin.md)
3.  [RBAC Groups](https://platform.claude.com/docs/en/api/http/admin/rbac_groups)

# Members

##### [List RBAC Group Members](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{group_id}/members

##### [Add RBAC Group Member](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/members/create)

POST/v1/organizations/rbac_groups/{group_id}/members

##### [Remove RBAC Group Member](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/members/delete)

DELETE/v1/organizations/rbac_groups/{group_id}/members/{user_id}

##### Models



RbacGroupMember object{ created_at, email, group_id, 2 more }





created_at: string



RFC 3339 timestamp of when the User was added to the RBAC Group.

formatdate-time

email: string



Email of the User.

group_id: string



ID of the RBAC Group.



type: "rbac_group_member"



Object type.

For RBAC Group Members, this is always `"rbac_group_member"`.

defaultrbac_group_member

user_id: string



ID of the User.



RbacGroupMemberDeleted object{ group_id, type, user_id }



group_id: string



ID of the RBAC Group.



type: "rbac_group_member_deleted"



Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

defaultrbac_group_member_deleted

user_id: string



ID of the User.
