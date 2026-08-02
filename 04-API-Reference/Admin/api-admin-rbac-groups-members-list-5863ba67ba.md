---
title: "List RBAC Group Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/rbac_groups/members/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:37:53Z"
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

List




# List RBAC Group Members

GET/v1/organizations/rbac_groups/{group_id}/members

List members of an RBAC Group.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

##### Path ParametersExpand Collapse 

group_id: string



ID of the RBAC Group.

[](#list.group_id)

##### Query ParametersExpand Collapse 



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

[](#list.limit)

page: optional string



Optionally set to the `next_page` token from the previous response.

[](#list.page)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

[](#list.anthropic-beta)

##### ReturnsExpand Collapse 



data: array of [RbacGroupMember](/docs/en/api/admin/rbac_groups/members#rbac_group_member) { created_at, email, group_id, 2 more }

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

[](#list)

has_more: boolean



Indicates if there are more results in the requested page direction.

[](#list)

next_page: string



Token to provide in as `page` in the subsequent request to retrieve the next page of data.

[](#list)

List RBAC Group Members



```python
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID/members \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
