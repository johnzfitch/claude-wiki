---
title: "List remote sessions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/sessions/remote/list"
category: "04-API-Reference/Other"
fetched_at: "2026-09-29T06:31:15Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [SDKs, CLI, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fsessions%2Fremote%2Flist)

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

Artifacts

Sessions

Local

Remote


List remote sessions

Messages

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
4.  [Sessions](/docs/en/api/http/compliance/apps/sessions)
5.  [Remote](/docs/en/api/http/compliance/apps/sessions/remote)

# List remote sessions

GET/v1/compliance/apps/sessions/remote

List remote sessions (Cowork sessions that run in Anthropic-managed cloud environments) across the organizations the key may read.

Each entry carries session metadata only; retrieve a session's transcript from the messages endpoint. By default the list spans every such organization; pass up to 500 `organization_ids[]` values to narrow it. Pass 1 to 10 `user_ids[]` values to scope the list to specific users: that filter matches the session's owning user, so agent-owned sessions are excluded whenever it is set. Bound results in time with the `created_at` range parameters (`created_at.gte`, `created_at.gt`, `created_at.lt`, `created_at.lte`; RFC 3339). There is no `updated_at` filter.

Results are sorted newest first by `created_at`, with at most `limit` sessions per page (default 100, maximum 500). Pagination is forward-only: pass the response's `next_page` value back as `page` to retrieve the next page, and stop when `next_page` is null.

##### Query parameters



created_at: optional object{ gt, gte, lt, lte }





gt: optional string



Filter remote sessions created after this time (RFC 3339 format)

formatdate-time



gte: optional string



Filter remote sessions created at or after this time (RFC 3339 format)

formatdate-time



lt: optional string



Filter remote sessions created before this time (RFC 3339 format)

formatdate-time



lte: optional string



Filter remote sessions created at or before this time (RFC 3339 format)

formatdate-time



limit: optional number



Maximum results (default: 100, max: 500)

default100

minimum1

maximum500



organization_ids: optional array of string



Filter to specific child organization identifiers. Omit to enumerate every child organization the key may read.

maxItems500

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



user_ids: optional array of string



Filter to sessions owned by specific users (max 10 per request). Agent-owned sessions are excluded when this filter is set.

maxItems10

##### Headers

"x-api-key": optional string



##### Returns



data: array of object{ id, agent_id, claude_project_id, 7 more }



id: string



Remote session identifier

agent_id: string or null



Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

claude_project_id: string or null



ID of the project the session is bound to. Null when the session has no project binding.



created_at: string



When the session was created (RFC 3339, UTC)

formatdate-time

organization_uuid: string



UUID of the organization the session belongs to

product_surface: string or null



The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.



started_by_user: object{ id, email_address } or null



The user who initiated an agent-owned session (for example, by mentioning Claude in Slack or via a scheduled trigger). Null for user-owned sessions — where the session's `user` started it — and for agent sessions with no human initiator. For initiators no longer a member of an organization the key may read, the object is populated with `email_address` null.

id: string



User identifier

email_address: string or null



User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

status: string



Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.



updated_at: string



When the session was last modified (RFC 3339, UTC)

formatdate-time



user: object{ id, email_address } or null



The user who owns the session. Null for sessions owned by an automated agent rather than a user. At most one of `user` and `agent_id` is set. For users no longer a member of an organization the key may read, the object is populated with `email_address` null.

id: string



User identifier

email_address: string or null



User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

next_page: string or null



Opaque page token; pass as `page` to retrieve the next page. Null when no rows exist after this page. Treat this value as opaque; do not parse or store it long-term, as the format may change without notice.

List remote sessions

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/sessions/remote \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "cse_01A0000000000000000000000",
      "organization_uuid": "00000000-0000-0000-0000-000000000000",
      "user": {
        "id": "user_01A0000000000000000000000",
        "email_address": "user@example.com"
      },
      "status": "active",
      "created_at": "2026-01-02T03:04:05.000000Z",
      "updated_at": "2026-01-02T03:04:05.000000Z",
      "product_surface": "cowork_remote",
      "claude_project_id": "claude_proj_01Nm7PqRsTuVwXyZaBcDeFgH"
    }
  ],
  "next_page": "page_AAE..."
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "cse_01A0000000000000000000000",
      "organization_uuid": "00000000-0000-0000-0000-000000000000",
      "user": {
        "id": "user_01A0000000000000000000000",
        "email_address": "user@example.com"
      },
      "status": "active",
      "created_at": "2026-01-02T03:04:05.000000Z",
      "updated_at": "2026-01-02T03:04:05.000000Z",
      "product_surface": "cowork_remote",
      "claude_project_id": "claude_proj_01Nm7PqRsTuVwXyZaBcDeFgH"
    }
  ],
  "next_page": "page_AAE..."
