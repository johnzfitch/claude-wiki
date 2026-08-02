---
title: "Get Chat Project Usage - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:37:37Z"
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


Get Activity Summaries

Usage

Cost

Users

Skills

Connectors

Chat Projects


Get Chat Project Usage

Plugins

Artifacts

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

# Get Chat Project Usage

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

Returns activity metrics for each project in the organization, sorted by project ID. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse 

date: optional string



UTC date in YYYY-MM-DD format. The day to get project activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

[](#list.date)

ending_date: optional string



UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

[](#list.ending_date)

filter: optional array of string



Filters as 'dimension

', e.g. filter\[\]=rbac_group_id:\<id\>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group\_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

[](#list.filter)

group_by: optional array of string



Dimensions to break results out by, e.g. group_by\[\]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

[](#list.group_by)

limit: optional number



Number of results per page (1-1000, default 100).

[](#list.limit)



order: optional "asc" or "desc"



Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

One of the following:

"asc"



[](#list.order%5B0%5D)

"desc"



[](#list.order%5B1%5D)

[](#list.order)

order_by: optional string



Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

[](#list.order_by)

page: optional string



Opaque cursor from a previous response's next_page field.

[](#list.page)

starting_date: optional string



UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

[](#list.starting_date)

##### ReturnsExpand Collapse 



ChatProjectUsage object { data, next_page }



Response for GET /v1/organizations/analytics/apps/chat/projects.



data: array of object { distinct_user_count, message_count, project_id, 8 more }



distinct_user_count: number



Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

[](#chat_project_usage.data.items.distinct_user_count)

message_count: number



Number of messages sent in the project on the requested day

[](#chat_project_usage.data.items.message_count)

project_id: string



Tagged project identifier (e.g. claude_proj\_...)

[](#chat_project_usage.data.items.project_id)

project_name: string



Name of the project

[](#chat_project_usage.data.items.project_name)

created_at: optional string



Project creation timestamp, RFC 3339. Null if the project was deleted before attribution was recorded.

[](#chat_project_usage.data.items.created_at)



created_by: optional [AnalyticsUser](/docs/en/api/admin/analytics#analytics_user) { id, email_address }



User identifier.

id: string



Tagged user identifier (e.g. user\_...)

[](#chat_project_usage.data.items.created_by%20%2B%20(resource)%20admin.analytics.id)

email_address: string



Email address of the user

[](#chat_project_usage.data.items.created_by%20%2B%20(resource)%20admin.analytics.email_address)

[](#chat_project_usage.data.items.created_by)

distinct_conversation_count: optional number



Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

[](#chat_project_usage.data.items.distinct_conversation_count)

product: optional string



Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by\[\] or filter\[\] there is rejected). Present only when the request grouped by product.

[](#chat_project_usage.data.items.product)

rbac_group_id: optional string



Tagged RBAC group identifier (rbac_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

[](#chat_project_usage.data.items.rbac_group_id)

rbac_group_name: optional string



Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

[](#chat_project_usage.data.items.rbac_group_name)

user_id: optional string



Tagged user identifier (e.g. user\_...). Present only when the request grouped by user_id.

[](#chat_project_usage.data.items.user_id)

[](#chat_project_usage.data)

next_page: string



Opaque cursor for the next page, or null if no more results

[](#chat_project_usage.next_page)

[](#chat_project_usage)

Get Chat Project Usage



```python
curl https://api.anthropic.com/v1/organizations/analytics/apps/chat/projects \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "data": [
    {
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address"
      },
      "distinct_conversation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address"
      },
      "distinct_conversation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
