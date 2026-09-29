---
title: "List projects - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/list"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:59Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fprojects%2Flist)

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

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

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

Chats

Projects


List projects


Get project details


Delete project

Attachments

Collaborators

Documents

Artifacts

Sessions

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)

Copy page



1.  [API reference](/docs/en/api/http)
2.  [Compliance API](/docs/en/api/http/compliance)
3.  [Apps](/docs/en/api/http/compliance/apps)
4.  [Projects](/docs/en/api/http/compliance/apps/projects)

# List projects

GET/v1/compliance/apps/projects

Lists project metadata with filtering capabilities. Results are sorted chronologically (time ascending) by created_at.

##### Query parameters



created_at: optional object{ gt, gte, lt, lte }





gt: optional string



Filter projects created after this time (RFC 3339 format)

formatdate-time



gte: optional string



Filter projects created at or after this time (RFC 3339 format)

formatdate-time



lt: optional string



Filter projects created before this time (RFC 3339 format)

formatdate-time



lte: optional string



Filter projects created at or before this time (RFC 3339 format)

formatdate-time



limit: optional number



Maximum results (default: 20, max: 100)

default20

minimum1

maximum100

organization_ids: optional array of string



Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



updated_at: optional object{ gt, gte, lt, lte }





gt: optional string



Filter projects updated after this time (RFC 3339 format)

formatdate-time



gte: optional string



Filter projects updated at or after this time (RFC 3339 format)

formatdate-time



lt: optional string



Filter projects updated before this time (RFC 3339 format)

formatdate-time



lte: optional string



Filter projects updated at or before this time (RFC 3339 format)

formatdate-time

user_ids: optional array of string



Filter by user IDs. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

##### Headers

"x-api-key": optional string



##### Returns



data: array of object{ id, created_at, deleted_at, 6 more }



List of projects sorted by creation date ascending

id: string



Project identifier (tagged ID)



created_at: string



Project creation timestamp

formatdate-time



deleted_at: string or null



Timestamp when the project was deleted by an end user, or null otherwise

formatdate-time

is_private: boolean



If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

name: string



Project name

organization_uuid: string



Organization UUID this project belongs to



updated_at: string



Project last update timestamp

formatdate-time



user: object{ id, email_address } or null



Project creator information, or null if the creator's account has been deleted or the creator is no longer a member of an organization the key may read

id: string



User identifier (tagged ID)

email_address: string



User's email address

organization_id: string⁠Deprecated



Organization identifier (tagged ID)

has_more: boolean



Whether more records exist beyond the current result set

next_page: string or null



Token to retrieve the next page. Use this as the 'page' parameter in your next request

List projects

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/projects \
    -H 'anthropic-version: 2023-06-01' \
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
