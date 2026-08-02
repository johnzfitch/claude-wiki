---
title: "Get Per-User Token Usage - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/usage/list_by_user"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:20Z"
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


Get Token Usage Over Time


Get Per-User Token Usage

Cost

Users

Skills

Connectors

Chat Projects

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

List by user




# Get Per-User Token Usage

GET/v1/organizations/analytics/user_usage_report

Get per-user token usage across a date range.

Returns one row per user, ranked by the chosen token metric. Use this to see which users consume the most tokens. Only usage attributable to a seat user is included; for organization-wide totals including direct API-key and automation traffic, use the bucketed `/v1/organizations/analytics/usage_report` endpoint. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse 

starting_at: string



Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00

.

[](#list_by_user.starting_at)



bucket_width: optional "1d" or "1h" or "1m"



Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

One of the following:

"1d"



[](#list_by_user.bucket_width%5B0%5D)

"1h"



[](#list_by_user.bucket_width%5B1%5D)

"1m"



[](#list_by_user.bucket_width%5B2%5D)

[](#list_by_user.bucket_width)



context_windows: optional array of "0-200k" or "200k-1M"



Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

One of the following:

"0-200k"



[](#list_by_user.context_windows.items%5B0%5D)

"200k-1M"



[](#list_by_user.context_windows.items%5B1%5D)

[](#list_by_user.context_windows)

ending_at: optional string



End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

[](#list_by_user.ending_at)

exclude_deleted_users: optional boolean



If true, omit rows for deleted accounts. Pages may return fewer than `limit` rows when deleted users were filtered.

[](#list_by_user.exclude_deleted_users)



group_by: optional array of "context_window" or "inference_geo" or "model" or 3 more



Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/usage_report` endpoint. `limit` bounds (actor × time bucket × dimension) rows — with dimensions or `bucket_width` present, one actor may span several rows.

One of the following:

"context_window"



[](#list_by_user.group_by.items%5B0%5D)

"inference_geo"



[](#list_by_user.group_by.items%5B1%5D)

"model"



[](#list_by_user.group_by.items%5B2%5D)

"product"



[](#list_by_user.group_by.items%5B3%5D)

"rbac_group_id"



[](#list_by_user.group_by.items%5B4%5D)

"speed"



[](#list_by_user.group_by.items%5B5%5D)

[](#list_by_user.group_by)



inference_geos: optional array of "global" or "not_available" or "us"



Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

One of the following:

"global"



[](#list_by_user.inference_geos.items%5B0%5D)

"not_available"



[](#list_by_user.inference_geos.items%5B1%5D)

"us"



[](#list_by_user.inference_geos.items%5B2%5D)

[](#list_by_user.inference_geos)

limit: optional number



Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

[](#list_by_user.limit)

models: optional array of string



Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

[](#list_by_user.models)



order: optional "asc" or "desc"



Sort direction. Defaults to `desc`.

One of the following:

"asc"



[](#list_by_user.order%5B0%5D)

"desc"



[](#list_by_user.order%5B1%5D)

[](#list_by_user.order)



order_by: optional "output_tokens" or "requests" or "total_tokens" or "uncached_input_tokens"



Metric to rank actors by. Defaults to `total_tokens`.

One of the following:

"output_tokens"



[](#list_by_user.order_by%5B0%5D)

"requests"



[](#list_by_user.order_by%5B1%5D)

"total_tokens"



[](#list_by_user.order_by%5B2%5D)

"uncached_input_tokens"



[](#list_by_user.order_by%5B3%5D)

[](#list_by_user.order_by)

page: optional string



Opaque cursor from a previous response's `next_page` field.

[](#list_by_user.page)

products: optional array of string



Product surfaces to include. Defaults to all products. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it.

[](#list_by_user.products)

rbac_group_ids: optional array of string



Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

[](#list_by_user.rbac_group_ids)



speeds: optional array of "fast" or "standard"



Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

One of the following:

"fast"



[](#list_by_user.speeds.items%5B0%5D)

"standard"



[](#list_by_user.speeds.items%5B1%5D)

[](#list_by_user.speeds)

user_ids: optional array of string



Filter to specific users by tagged user ID.

[](#list_by_user.user_ids)

##### ReturnsExpand Collapse 



UserUsage object { data, data_refreshed_at, has_more, 2 more }





data: array of object { actor, cache_creation, cache_read_input_tokens, 13 more }





actor: [AnalyticsUserActor](/docs/en/api/admin/analytics#analytics_user_actor) { user_id, deleted, email, 2 more }



user_id: string



Tagged user ID.

[](#user_usage.data.items.actor%20%2B%20(resource)%20admin.analytics.user_id)

deleted: optional boolean



True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

[](#user_usage.data.items.actor%20%2B%20(resource)%20admin.analytics.deleted)

email: optional string



The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

[](#user_usage.data.items.actor%20%2B%20(resource)%20admin.analytics.email)

name: optional string



The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

[](#user_usage.data.items.actor%20%2B%20(resource)%20admin.analytics.name)

type: optional "user_actor"



[](#user_usage.data.items.actor%20%2B%20(resource)%20admin.analytics.type)

[](#user_usage.data.items.actor)



cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }



ephemeral_1h_input_tokens: number



The number of input tokens used to create the 1 hour cache entry.

[](#user_usage.data.items.cache_creation.ephemeral_1h_input_tokens)

ephemeral_5m_input_tokens: number



The number of input tokens used to create the 5 minute cache entry.

[](#user_usage.data.items.cache_creation.ephemeral_5m_input_tokens)

[](#user_usage.data.items.cache_creation)

cache_read_input_tokens: number



The number of input tokens read from the cache.

[](#user_usage.data.items.cache_read_input_tokens)



context_window: "0-200k" or "200k-1M"



One of the following:

"0-200k"



[](#user_usage.data.items.context_window%5B0%5D)

"200k-1M"



[](#user_usage.data.items.context_window%5B1%5D)

[](#user_usage.data.items.context_window)

ending_at: string



[](#user_usage.data.items.ending_at)



inference_geo: "global" or "us"



One of the following:

"global"



[](#user_usage.data.items.inference_geo%5B0%5D)

"us"



[](#user_usage.data.items.inference_geo%5B1%5D)

[](#user_usage.data.items.inference_geo)

model: string



[](#user_usage.data.items.model)

output_tokens: number



The number of output tokens generated.

[](#user_usage.data.items.output_tokens)

product: string



Product surface that produced the usage or cost. Null unless product is in group_by\[\]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

[](#user_usage.data.items.product)

rbac_group_id: string



RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

[](#user_usage.data.items.rbac_group_id)

requests: number



Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

[](#user_usage.data.items.requests)



server_tool_use: object { web_search_requests }



web_search_requests: number



The number of web search requests made.

[](#user_usage.data.items.server_tool_use.web_search_requests)

[](#user_usage.data.items.server_tool_use)



speed: "fast" or "standard"



One of the following:

"fast"



[](#user_usage.data.items.speed%5B0%5D)

"standard"



[](#user_usage.data.items.speed%5B1%5D)

[](#user_usage.data.items.speed)

starting_at: string



[](#user_usage.data.items.starting_at)

total_tokens: number



Total token count across all token types. This is the value the default order_by='total_tokens' sorts on.

[](#user_usage.data.items.total_tokens)

uncached_input_tokens: number



The number of uncached input tokens processed.

[](#user_usage.data.items.uncached_input_tokens)

[](#user_usage.data)

data_refreshed_at: string



RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

[](#user_usage.data_refreshed_at)

has_more: boolean



[](#user_usage.has_more)

next_page: string



[](#user_usage.next_page)

organization_id: string



ID of the Organization.

[](#user_usage.organization_id)

[](#user_usage)

Get Per-User Token Usage



```python
curl https://api.anthropic.com/v1/organizations/analytics/user_usage_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "data": [
    {
      "actor": {
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor"
      },
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1000,
        "ephemeral_5m_input_tokens": 500
      },
      "cache_read_input_tokens": 3200000,
      "context_window": "0-200k",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "model": "model",
      "output_tokens": 891000,
      "product": "product",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "server_tool_use": {
        "web_search_requests": 10
      },
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "total_tokens": 5377000,
      "uncached_input_tokens": 1284500
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "actor": {
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor"
      },
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1000,
        "ephemeral_5m_input_tokens": 500
      },
      "cache_read_input_tokens": 3200000,
      "context_window": "0-200k",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "model": "model",
      "output_tokens": 891000,
      "product": "product",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "server_tool_use": {
        "web_search_requests": 10
      },
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "total_tokens": 5377000,
      "uncached_input_tokens": 1284500
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
