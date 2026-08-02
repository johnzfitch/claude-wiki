---
title: "List chats - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/list"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:10Z"
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


List chats


Delete chat

Messages

Files

Generated Files

Projects

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

# List chats

GET/v1/compliance/apps/chats

Lists chat metadata with filtering capabilities for targeted compliance review. Results are sorted chronologically (time ascending) by the `order_by` key, with ties broken by id.

##### Query ParametersExpand Collapse 

after_id: optional string



Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list.after_id)

before_id: optional string



Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list.before_id)



created_at: optional object { gt, gte, lt, lte }



gt: optional string



Filter chats created after this time (RFC 3339 format)

[](#list.created_at.gt)

gte: optional string



Filter chats created at or after this time (RFC 3339 format)

[](#list.created_at.gte)

lt: optional string



Filter chats created before this time (RFC 3339 format)

[](#list.created_at.lt)

lte: optional string



Filter chats created at or before this time (RFC 3339 format)

[](#list.created_at.lte)

[](#list.created_at)

limit: optional number



Maximum results (default: 100, max: 1000)

[](#list.limit)



order_by: optional "created_at" or "updated_at"



Sort key for results. `created_at` (default) sorts by chat creation time. `updated_at` sorts by last update time and is only supported for org-wide queries (omit user_ids\[\]). For org-wide queries, any time filter must match the sort key: `created_at.*` filters require `order_by=created_at`, and `updated_at.*` filters require `order_by=updated_at`.

One of the following:

"created_at"



[](#list.order_by%5B0%5D)

"updated_at"



[](#list.order_by%5B1%5D)

[](#list.order_by)

organization_ids: optional array of string



Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

[](#list.organization_ids)

project_ids: optional array of string



Filter by project IDs (accepts `claude_proj_...`). Enumerate IDs via `GET /v1/compliance/apps/projects`. Requires user_ids\[\]; not supported for org-wide queries.

[](#list.project_ids)



updated_at: optional object { gt, gte, lt, lte }



gt: optional string



Filter chats updated after this time (RFC 3339 format)

[](#list.updated_at.gt)

gte: optional string



Filter chats updated at or after this time (RFC 3339 format)

[](#list.updated_at.gte)

lt: optional string



Filter chats updated before this time (RFC 3339 format)

[](#list.updated_at.lt)

lte: optional string



Filter chats updated at or before this time (RFC 3339 format)

[](#list.updated_at.lte)

[](#list.updated_at)

user_ids: optional array of string



Filter to chats created by specific users (max 10 per request). Omit for an org-wide query. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

[](#list.user_ids)

##### Header ParametersExpand Collapse 

"x-api-key": optional string



[](#list.x-api-key)

##### ReturnsExpand Collapse 



data: array of object { id, created_at, deleted_at, 8 more }



List of chat metadata sorted chronologically by the request's `order_by` key (default `created_at`), tie break by id

id: string



Chat ID

[](#chat_list_response.id)

created_at: string



Creation timestamp

[](#chat_list_response.created_at)

deleted_at: string



Deletion timestamp if deleted

[](#chat_list_response.deleted_at)

href: string



URL to view this chat in claude.ai

[](#chat_list_response.href)

model: string



Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

[](#chat_list_response.model)

name: string



Chat name/title

[](#chat_list_response.name)

organization_uuid: string



Organization UUID this chat belongs to

[](#chat_list_response.organization_uuid)

project_id: string



Project ID this chat belongs to

[](#chat_list_response.project_id)

updated_at: string



Last update timestamp

[](#chat_list_response.updated_at)



user: object { id, email_address }



User information for compliance responses.

id: string



User identifier

[](#chat_list_response.user.id)

email_address: string



User's email address

[](#chat_list_response.user.email_address)

[](#chat_list_response.user)

organization_id: string⁠Deprecated



Organization ID this chat belongs to

[](#chat_list_response.organization_id)

[](#list)

first_id: string



Opaque pagination cursor for the first chat in the current result set. Pass as `before_id` on the next request to page backwards. Backward pagination is only supported for per-user queries (`user_ids[]` set); org-wide queries do not accept `before_id`. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list)

has_more: boolean



Whether more records exist beyond the current result set

[](#list)

last_id: string



Opaque pagination cursor for the last chat in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list)

List chats



```python
curl https://api.anthropic.com/v1/compliance/apps/chats \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "claude_chat_abc123",
      "name": "Product Requirements Discussion",
      "created_at": "2025-06-07T08:09:10Z",
      "updated_at": "2025-06-07T09:10:11Z",
      "organization_id": "org_abc123",
      "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
      "project_id": "claude_proj_xyz789",
      "model": "claude-opus-4-7",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      },
      "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789"
    }
  ],
  "has_more": false,
  "first_id": "eyJrIjogImNyZWF0ZWRfYXQiLCAidCI6ICIyMDI1LTA2LTA3VDA4OjA5OjEwKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLTIzNDUtNjc4OS1hYmNkLWVmMDEyMzQ1Njc4OSJ9",
  "last_id": "eyJrIjogImNyZWF0ZWRfYXQiLCAidCI6ICIyMDI1LTA2LTA3VDA4OjA5OjEwKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLTIzNDUtNjc4OS1hYmNkLWVmMDEyMzQ1Njc4OSJ9"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "claude_chat_abc123",
      "name": "Product Requirements Discussion",
      "created_at": "2025-06-07T08:09:10Z",
      "updated_at": "2025-06-07T09:10:11Z",
      "organization_id": "org_abc123",
      "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
      "project_id": "claude_proj_xyz789",
      "model": "claude-opus-4-7",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      },
      "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789"
    }
  ],
  "has_more": false,
  "first_id": "eyJrIjogImNyZWF0ZWRfYXQiLCAidCI6ICIyMDI1LTA2LTA3VDA4OjA5OjEwKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLTIzNDUtNjc4OS1hYmNkLWVmMDEyMzQ1Njc4OSJ9",
  "last_id": "eyJrIjogImNyZWF0ZWRfYXQiLCAidCI6ICIyMDI1LTA2LTA3VDA4OjA5OjEwKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLTIzNDUtNjc4OS1hYmNkLWVmMDEyMzQ1Njc4OSJ9"
