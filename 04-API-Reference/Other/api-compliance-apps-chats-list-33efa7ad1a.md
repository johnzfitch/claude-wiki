---
title: "List chats - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/list"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:02Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fchats%2Flist)

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


List chats


Delete chat

Messages

Files

Generated Files

Projects

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
4.  [Chats](/docs/en/api/http/compliance/apps/chats)

# List chats

GET/v1/compliance/apps/chats

Lists chat metadata with filtering capabilities for targeted compliance review. Results are sorted chronologically (time ascending) by the `order_by` key, with ties broken by id.

Incremental polling with `order_by=updated_at` returns a chat again after it receives a new message, is moved into or out of a project, or is deleted in claude.ai. A chat is not guaranteed to be returned again after other edits, such as a rename.

**Deprecation notice:** Combining `user_ids[]` with any `updated_at.*` filter is deprecated and will be rejected with HTTP 400 after 2026-09-22. For incremental polling by update time, omit `user_ids[]` and set `order_by=updated_at` with `after_id` cursor pagination — this returns the same chats across the whole organization in a single request stream. For per-user listing, use `created_at.*` filters (or no time filter) with the default `order_by`. `user_ids[]` with `order_by=updated_at` is already rejected.

##### Query parameters

after_id: optional string



Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

before_id: optional string



Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



created_at: optional object{ gt, gte, lt, lte }





gt: optional string



Filter chats created after this time (RFC 3339 format)

formatdate-time



gte: optional string



Filter chats created at or after this time (RFC 3339 format)

formatdate-time



lt: optional string



Filter chats created before this time (RFC 3339 format)

formatdate-time



lte: optional string



Filter chats created at or before this time (RFC 3339 format)

formatdate-time



limit: optional number



Maximum results (default: 100, max: 1000)

default100

minimum1

maximum1000



order_by: optional "created_at" or "updated_at"



Sort key for results. `created_at` (default) sorts by chat creation time. `updated_at` sorts by last update time and is only supported for org-wide queries (omit user_ids\[\]). For org-wide queries, any time filter must match the sort key: `created_at.*` filters require `order_by=created_at`, and `updated_at.*` filters require `order_by=updated_at`.

defaultcreated_at

One of the following:

"created_at"



"updated_at"



organization_ids: optional array of string



Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

project_ids: optional array of string



Filter by project IDs (accepts `claude_proj_...`). Enumerate IDs via `GET /v1/compliance/apps/projects`. Requires user_ids\[\]; not supported for org-wide queries.



updated_at: optional object{ gt, gte, lt, lte }





gt: optional string



Filter chats updated after this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

formatdate-time



gte: optional string



Filter chats updated at or after this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

formatdate-time



lt: optional string



Filter chats updated before this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

formatdate-time



lte: optional string



Filter chats updated at or before this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

formatdate-time



user_ids: optional array of string



Filter to chats created by specific users (max 10 per request). Omit for an org-wide query. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`. Deprecated combination: passing `user_ids[]` together with any `updated_at.*` filter is deprecated and will be rejected after 2026-09-22. For `updated_at`-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

maxItems10

##### Headers

"x-api-key": optional string



##### Returns



data: array of object{ id, created_at, deleted_at, 8 more }



List of chat metadata sorted chronologically by the request's `order_by` key (default `created_at`), tie break by id

id: string



Chat ID



created_at: string



Creation timestamp

formatdate-time



deleted_at: string or null



Deletion timestamp if deleted

formatdate-time

href: string



URL to view this chat in claude.ai

model: string or null



Model selected for this chat (e.g. 'claude-opus-5'). May be null for legacy chats that never had a model recorded.

name: string



Chat name/title

organization_uuid: string



Organization UUID this chat belongs to

project_id: string or null



Project ID this chat belongs to



updated_at: string



Last update timestamp. Updated when the chat receives a new message, is moved into or out of a project, or is deleted in claude.ai. Other edits, such as renaming the chat, are not guaranteed to change it.

formatdate-time



user: object{ id, email_address } or null



The user who created the chat. Null when the API key is restricted to one organization and the creator is no longer a member of it.

id: string



User identifier

email_address: string



User's email address

organization_id: string⁠Deprecated



Organization ID this chat belongs to

first_id: string or null



Opaque pagination cursor for the first chat in the current result set. Pass as `before_id` on the next request to page backwards. Backward pagination is only supported for per-user queries (`user_ids[]` set); org-wide queries do not accept `before_id`. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

has_more: boolean



Whether more records exist beyond the current result set

last_id: string or null



Opaque pagination cursor for the last chat in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

List chats

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/chats \
    -H 'anthropic-version: 2023-06-01' \
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
      "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
      "project_id": "claude_proj_xyz789",
      "model": "claude-opus-5",
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
      "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
      "project_id": "claude_proj_xyz789",
      "model": "claude-opus-5",
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
