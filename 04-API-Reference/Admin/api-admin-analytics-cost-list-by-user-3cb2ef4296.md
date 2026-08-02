---
title: "Get Per-User Cost - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:18Z"
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


Get Cost Over Time


Get Per-User Cost

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

# Get Per-User Cost

GET/v1/organizations/analytics/user_cost_report

Get per-user cost in USD across a date range.

Returns one row per user, ranked by spend. Use this to see which users account for the most cost. Only cost attributable to a seat user is included; for organization-wide totals including direct API-key and automation traffic, use the bucketed `/v1/organizations/analytics/cost_report` endpoint. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.

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

group_by: optional array of "context_window" or "cost_type" or "inference_geo" or 5 more



Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/cost_report` endpoint. The `product`, `model`, `context_window`, `inference_geo`, and `speed` dimensions — and the time bucket, when `bucket_width` is set — count toward `limit`. `cost_type` and `token_type` do not: `cost_type` returns one row per cost component (tokens, web search, code execution); `token_type` returns one row per token type, each with `cost_type: "tokens"`; combining both returns the per-token-type rows plus the web-search and code-execution rows. A page can therefore contain more rows than `limit` when `cost_type` or `token_type` is requested.

One of the following:

"context_window"



[](#list_by_user.group_by.items%5B0%5D)

"cost_type"



[](#list_by_user.group_by.items%5B1%5D)

"inference_geo"



[](#list_by_user.group_by.items%5B2%5D)

"model"



[](#list_by_user.group_by.items%5B3%5D)

"product"



[](#list_by_user.group_by.items%5B4%5D)

"rbac_group_id"



[](#list_by_user.group_by.items%5B5%5D)

"speed"



[](#list_by_user.group_by.items%5B6%5D)

"token_type"



[](#list_by_user.group_by.items%5B7%5D)

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

order_by: optional "amount" or "list_amount"



Metric to rank actors by. Defaults to `amount`.

One of the following:

"amount"



[](#list_by_user.order_by%5B0%5D)

"list_amount"



[](#list_by_user.order_by%5B1%5D)

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

UserCost object { data, data_refreshed_at, has_more, 2 more }





data: array of object { actor, amount, context_window, 12 more }





actor: [AnalyticsUserActor](/docs/en/api/admin/analytics#analytics_user_actor) { user_id, deleted, email, 2 more }



user_id: string



Tagged user ID.

[](#user_cost.data.items.actor%20%2B%20(resource)%20admin.analytics.user_id)

deleted: optional boolean



True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

[](#user_cost.data.items.actor%20%2B%20(resource)%20admin.analytics.deleted)

email: optional string



The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

[](#user_cost.data.items.actor%20%2B%20(resource)%20admin.analytics.email)

name: optional string



The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

[](#user_cost.data.items.actor%20%2B%20(resource)%20admin.analytics.name)

type: optional "user_actor"



[](#user_cost.data.items.actor%20%2B%20(resource)%20admin.analytics.type)

[](#user_cost.data.items.actor)

amount: string



Amount (post-discount, pre-credit) in fractional cents (minor units).

[](#user_cost.data.items.amount)



context_window: "0-200k" or "200k-1M"



One of the following:

"0-200k"



[](#user_cost.data.items.context_window%5B0%5D)

"200k-1M"



[](#user_cost.data.items.context_window%5B1%5D)

[](#user_cost.data.items.context_window)



cost_type: "code_execution" or "tokens" or "web_search"



Cost component breakdown; null when returning the combined total.

One of the following:

"code_execution"



[](#user_cost.data.items.cost_type%5B0%5D)

"tokens"



[](#user_cost.data.items.cost_type%5B1%5D)

"web_search"



[](#user_cost.data.items.cost_type%5B2%5D)

[](#user_cost.data.items.cost_type)

currency: "USD"



[](#user_cost.data.items.currency)

ending_at: string



[](#user_cost.data.items.ending_at)



inference_geo: "global" or "us"



One of the following:

"global"



[](#user_cost.data.items.inference_geo%5B0%5D)

"us"



[](#user_cost.data.items.inference_geo%5B1%5D)

[](#user_cost.data.items.inference_geo)

list_amount: string



List-price amount (pre-discount) in fractional cents.

[](#user_cost.data.items.list_amount)

model: string



[](#user_cost.data.items.model)

product: string



Product surface that produced the usage or cost. Null unless product is in group_by\[\]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

[](#user_cost.data.items.product)

rbac_group_id: string



RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

[](#user_cost.data.items.rbac_group_id)

requests: number



Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

[](#user_cost.data.items.requests)



speed: "fast" or "standard"



One of the following:

"fast"



[](#user_cost.data.items.speed%5B0%5D)

"standard"



[](#user_cost.data.items.speed%5B1%5D)

[](#user_cost.data.items.speed)

starting_at: string



[](#user_cost.data.items.starting_at)



token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more



Token type when cost_type=tokens; null otherwise.

One of the following:

"cache_creation.ephemeral_1h_input_tokens"



[](#user_cost.data.items.token_type%5B0%5D)

"cache_creation.ephemeral_5m_input_tokens"



[](#user_cost.data.items.token_type%5B1%5D)

"cache_read_input_tokens"



[](#user_cost.data.items.token_type%5B2%5D)

"output_tokens"



[](#user_cost.data.items.token_type%5B3%5D)

"uncached_input_tokens"



[](#user_cost.data.items.token_type%5B4%5D)

[](#user_cost.data.items.token_type)

[](#user_cost.data)

data_refreshed_at: string



RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

[](#user_cost.data_refreshed_at)

has_more: boolean



[](#user_cost.has_more)

next_page: string



[](#user_cost.next_page)

organization_id: string



ID of the Organization.

[](#user_cost.organization_id)

[](#user_cost)

Get Per-User Cost



```python
curl https://api.anthropic.com/v1/organizations/analytics/user_cost_report \
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
      "amount": "41280.000000",
      "context_window": "0-200k",
      "cost_type": "code_execution",
      "currency": "USD",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "list_amount": "51600.000000",
      "model": "model",
      "product": "product",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "token_type": "cache_creation.ephemeral_1h_input_tokens"
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
      "amount": "41280.000000",
      "context_window": "0-200k",
      "cost_type": "code_execution",
      "currency": "USD",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "list_amount": "51600.000000",
      "model": "model",
      "product": "product",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "token_type": "cache_creation.ephemeral_1h_input_tokens"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
