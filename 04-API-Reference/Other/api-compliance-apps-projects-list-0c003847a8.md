---
title: "List projects - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/list"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:41:38Z"
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

Groups

Apps

Chats

Projects


List projects


Get project details


Delete project

Attachments

Collaborators

Documents

Artifacts

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

# List projects

GET/v1/compliance/apps/projects

Lists project metadata with filtering capabilities. Results are sorted chronologically (time ascending) by created_at.

##### Query ParametersExpand Collapse 



created_at: optional object { gt, gte, lt, lte }



gt: optional string



Filter projects created after this time (RFC 3339 format)

[](#list.created_at.gt)

gte: optional string



Filter projects created at or after this time (RFC 3339 format)

[](#list.created_at.gte)

lt: optional string



Filter projects created before this time (RFC 3339 format)

[](#list.created_at.lt)

lte: optional string



Filter projects created at or before this time (RFC 3339 format)

[](#list.created_at.lte)

[](#list.created_at)

limit: optional number



Maximum results (default: 20, max: 100)

[](#list.limit)

organization_ids: optional array of string



Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

[](#list.organization_ids)

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list.page)



updated_at: optional object { gt, gte, lt, lte }



gt: optional string



Filter projects updated after this time (RFC 3339 format)

[](#list.updated_at.gt)

gte: optional string



Filter projects updated at or after this time (RFC 3339 format)

[](#list.updated_at.gte)

lt: optional string



Filter projects updated before this time (RFC 3339 format)

[](#list.updated_at.lt)

lte: optional string



Filter projects updated at or before this time (RFC 3339 format)

[](#list.updated_at.lte)

[](#list.updated_at)

user_ids: optional array of string



Filter by user IDs. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

[](#list.user_ids)

##### Header ParametersExpand Collapse 

"x-api-key": optional string



[](#list.x-api-key)

##### ReturnsExpand Collapse 



data: array of object { id, created_at, deleted_at, 6 more }



List of projects sorted by creation date ascending

id: string



Project identifier (tagged ID)

[](#project_list_response.id)

created_at: string



Project creation timestamp

[](#project_list_response.created_at)

deleted_at: string



Timestamp when the project was deleted by an end user, or null otherwise

[](#project_list_response.deleted_at)

is_private: boolean



If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

[](#project_list_response.is_private)

name: string



Project name

[](#project_list_response.name)

organization_uuid: string



Organization UUID this project belongs to

[](#project_list_response.organization_uuid)

updated_at: string



Project last update timestamp

[](#project_list_response.updated_at)



user: object { id, email_address }



The user who created a project or project document.

Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.

id: string



User identifier (tagged ID)

[](#project_list_response.user.id)

email_address: string



User's email address

[](#project_list_response.user.email_address)

[](#project_list_response.user)

organization_id: string⁠Deprecated



Organization identifier (tagged ID)

[](#project_list_response.organization_id)

[](#list)

has_more: boolean



Whether more records exist beyond the current result set

[](#list)

next_page: string



Token to retrieve the next page. Use this as the 'page' parameter in your next request

[](#list)

List projects



```python
curl https://api.anthropic.com/v1/compliance/apps/projects \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "claude_proj_abc123",
      "name": "Q4 Product Planning",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z",
      "is_private": true,
      "organization_id": "org_abc123",
      "organization_uuid": "abc12345-6789-0abc-def0-123456789abc",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "page_eyJjcmVhdGVkX2F0IjoiMjAyNS0wNi0wMVQxMDowMDowMFoiLCJ1dWlkIjoiYWJjMTIzIn0="
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "claude_proj_abc123",
      "name": "Q4 Product Planning",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z",
      "is_private": true,
      "organization_id": "org_abc123",
      "organization_uuid": "abc12345-6789-0abc-def0-123456789abc",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "page_eyJjcmVhdGVkX2F0IjoiMjAyNS0wNi0wMVQxMDowMDowMFoiLCJ1dWlkIjoiYWJjMTIzIn0="
