---
title: "Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members"
category: "04-API-Reference/Other"
fetched_at: "2026-09-27T06:27:02Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Frbac_groups%2Fmembers)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

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

cURL

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)
3.  [Organization](/docs/en/api/http/beta/organization)
4.  [RBAC Groups](/docs/en/api/http/beta/organization/rbac_groups)

# Members

##### [List RBAC Group Members](/docs/en/api/http/beta/organization/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{rbac_group_id}/members

List members of an RBAC Group.

##### [Add RBAC Group Member](/docs/en/api/http/beta/organization/rbac_groups/members/create)

POST/v1/organizations/rbac_groups/{rbac_group_id}/members

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Remove RBAC Group Member](/docs/en/api/http/beta/organization/rbac_groups/members/delete)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### Models



BetaRBACGroupMember object{ type: "rbac_group_member", created_at, email, 3 more }





type: "rbac_group_member"



Object type.

For RBAC Group Members, this is always `"rbac_group_member"`.

defaultrbac_group_member



created_at: string



RFC 3339 timestamp of when the User was added to the RBAC Group.

formatdate-time

email: string



Email of the User.

rbac_group_id: string



ID of the RBAC Group.

user_id: string



ID of the User.



group_id: string⁠Deprecated



Deprecated: use `rbac_group_id` instead. ID of the RBAC Group; always the same value as `rbac_group_id`.

Use \`rbac_group_id\` instead; \`group_id\` always has the same value.



BetaRBACGroupMemberDeleted object{ type: "rbac_group_member_deleted", group_id, rbac_group_id, user_id }





type: "rbac_group_member_deleted"



Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

defaultrbac_group_member_deleted

rbac_group_id: string



ID of the RBAC Group.

user_id: string



ID of the User.



group_id: string⁠Deprecated



Deprecated: use `rbac_group_id` instead. ID of the RBAC Group; always the same value as `rbac_group_id`.

Use \`rbac_group_id\` instead; \`group_id\` always has the same value.
