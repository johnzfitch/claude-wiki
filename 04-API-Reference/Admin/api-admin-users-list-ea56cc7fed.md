---
title: "List Users - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/users/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:40Z"
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


Get User


List Users


Update User


Remove User

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

# List Users

GET/v1/organizations/users

For Claude Enterprise organizations, this endpoint's availability is in beta.

##### Query ParametersExpand Collapse 

after_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

[](#list.after_id)

before_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

[](#list.before_id)

email: optional string



Filter by user email.

[](#list.email)



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

[](#list.limit)

##### ReturnsExpand Collapse 



data: array of [User](/docs/en/api/admin/users#user) { id, added_at, email, 3 more }



id: string



ID of the User.

[](#user.id)

added_at: string



RFC 3339 datetime string indicating when the User joined the Organization.

[](#user.added_at)

email: string



Email of the User.

[](#user.email)

name: string



Name of the User.

[](#user.name)



role: "admin" or "billing" or "claude_code_user" or 6 more



Organization role of the User.

One of the following:

"admin"



[](#user.role%5B0%5D)

"billing"



[](#user.role%5B1%5D)

"claude_code_user"



[](#user.role%5B2%5D)

"developer"



[](#user.role%5B3%5D)

"managed"



[](#user.role%5B4%5D)

"membership_admin"



[](#user.role%5B5%5D)

"owner"



[](#user.role%5B6%5D)

"primary_owner"



[](#user.role%5B7%5D)

"user"



[](#user.role%5B8%5D)

[](#user.role)



type: "user"



Object type.

For Users, this is always `"user"`.

[](#user.type)

[](#list)

first_id: string



First ID in the `data` list. Can be used as the `before_id` for the previous page.

[](#list)

has_more: boolean



Indicates if there are more results in the requested page direction.

[](#list)

last_id: string



Last ID in the `data` list. Can be used as the `after_id` for the next page.

[](#list)

List Users



```python
curl https://api.anthropic.com/v1/organizations/users \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "name": "Jane Doe",
      "role": "user",
      "type": "user"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
