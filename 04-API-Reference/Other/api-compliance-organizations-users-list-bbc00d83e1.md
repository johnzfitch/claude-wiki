---
title: "List organization users - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/users/list"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:38Z"
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

MCP Tunnels


Compliance API

Activities

Organizations


List organizations

Users


List organization users

Roles

Settings

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



To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# List organization users

GET/v1/compliance/organizations/{org_uuid}/users

List current user members of an organization.

##### Path ParametersExpand Collapse 

org_uuid: string



The organization UUID

[](#list.org_uuid)

##### Query ParametersExpand Collapse 

limit: optional number



Maximum results (default: 500, max: 1000)

[](#list.limit)

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list.page)

##### Header ParametersExpand Collapse 

"x-api-key": optional string



[](#list.x-api-key)

##### ReturnsExpand Collapse 



data: array of object { id, created_at, email, 2 more }



List of current organization members sorted by organization join date ascending

id: string



User identifier (tagged ID)

[](#user_list_response.id)

created_at: string



User account creation timestamp

[](#user_list_response.created_at)

email: string



User's current email address

[](#user_list_response.email)

full_name: string



User's current full name

[](#user_list_response.full_name)



organization_role: "admin" or "billing" or "claude_code_user" or 6 more



User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

One of the following:

"admin"



[](#user_list_response.organization_role%5B0%5D)

"billing"



[](#user_list_response.organization_role%5B1%5D)

"claude_code_user"



[](#user_list_response.organization_role%5B2%5D)

"developer"



[](#user_list_response.organization_role%5B3%5D)

"managed"



[](#user_list_response.organization_role%5B4%5D)

"membership_admin"



[](#user_list_response.organization_role%5B5%5D)

"owner"



[](#user_list_response.organization_role%5B6%5D)

"primary_owner"



[](#user_list_response.organization_role%5B7%5D)

"user"



[](#user_list_response.organization_role%5B8%5D)

[](#user_list_response.organization_role)

[](#list)

has_more: boolean



Whether more records exist beyond the current result set

[](#list)

next_page: string



Token to retrieve the next page. Use this as the 'page' parameter in your next request

[](#list)

List organization users



```python
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "email": "jane.doe@example.com",
      "full_name": "Jane Doe",
      "organization_role": "admin"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
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
      "created_at": "2025-03-12T18:22:41.123456Z",
      "email": "jane.doe@example.com",
      "full_name": "Jane Doe",
      "organization_role": "admin"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
