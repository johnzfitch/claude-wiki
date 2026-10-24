---
title: "Get Chat Project Usage - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/analytics/apps/chat/projects/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-18T06:27:04Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fanalytics%2Fapps%2Fchat%2Fprojects%2Flist)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


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


Organization


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

MCP Tunnels

Analytics

Summaries

Users

Apps

Chat

Projects


Get Chat Project Usage

Connectors

Plugins

Skills

Artifacts

Usage Report

User Usage Report

Cost Report

User Cost Report

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


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


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](../Endpoints/opentelemetry-spans.md)

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Analytics](platform-claude-com-http-beta-organization-analytics.md)
5.  [Apps](https://platform.claude.com/docs/en/api/http/beta/organization/analytics/apps)
6.  [Chat](https://platform.claude.com/docs/en/api/http/beta/organization/analytics/apps/chat)
7.  [Projects](http-beta-organization-analytics-apps-chat-projects.md)

# Get Chat Project Usage

Copy page



cURL

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

Returns activity metrics for each project in the organization, sorted by project ID. Use `group_by[]` to break projects out per member or per RBAC group, and `filter[]` to scope results; the parameter descriptions list the supported dimensions. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.

##### Query parameters



date: optional string



UTC date in YYYY-MM-DD format. The day to get project activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

formatdate



ending_date: optional string



UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

formatdate



filter: optional array of string



Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `project_id`, `rbac_group_id`, `user_id`. Value forms: `project_id` takes a tagged project id (`claude_proj_...`); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

maxItems100



group_by: optional array of "rbac_group_id" or "user_id"



Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

maxItems100

One of the following:

"rbac_group_id"



"user_id"





limit: optional number



Number of results per page (1-1000, default 100).

minimum1

maximum1000



order: optional "asc" or "desc"



Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

One of the following:

"asc"



"desc"



order_by: optional string



Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

page: optional string



Opaque cursor from a previous response's `next_page` field.



starting_date: optional string



UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

formatdate

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns



data: array of [BetaAnalyticsProjectActivity](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_project_activity) { distinct_user_count, message_count, project_id, 8 more }



distinct_user_count: number



Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

message_count: number



Number of messages sent in the project on the requested day

project_id: string



Tagged project identifier (e.g. `claude_proj_...`)

project_name: string



Name of the project



created_at: optional string or null



Project creation timestamp in RFC 3339 format. Null if the project was deleted before attribution was recorded.

formatdate-time



created_by: optional [BetaAnalyticsUser](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_user) { type: "user", id, email_address } or null



User who created the project. Null if the project was deleted before attribution was recorded, or if the creator's account no longer exists.



type: "user"



Object type. Always `user`.

defaultuser

id: string



Tagged user identifier (e.g. `user_...`)

email_address: string



Email address of the user

distinct_conversation_count: optional number or null



Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

product: optional string or null



Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

rbac_group_id: optional string or null



Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

rbac_group_name: optional string or null



Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

user_id: optional string or null



Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

next_page: string or null



Opaque cursor for the next page, or null if no more results

Get Chat Project Usage

cURL



```python
curl https://api.anthropic.com/v1/organizations/analytics/apps/chat/projects \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
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
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      },
      "distinct_conversation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
