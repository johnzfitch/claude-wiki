---
title: "Usage and Cost Analytics API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api"
category: "04-API-Reference/Other"
fetched_at: "2026-11-07T06:23:55Z"
tags: ["api", "enterprise"]
---

# Usage and Cost Analytics API

Copy page



Query token usage and cost for your Claude Console or Claude Enterprise organization by model, workspace, API key, actor, and more.

Copy page





**The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization on the [Organization](playground.md) page (`platform.claude.com/settings/organization`) in the Claude Console.

The Usage and Cost Analytics API reports historical token usage and cost for your organization, broken down by the dimensions you choose, such as model, workspace, API key, or the user or service account behind each request. For Claude Console organizations, this data is similar to what the [Usage](playground.md) and [Cost](playground.md) pages of the Claude Console show.

The API has two endpoints:

- `GET /v1/organizations/analytics/usage` reports token counts and request counts.
- `GET /v1/organizations/analytics/cost` reports cost in USD.

The Usage and Cost Analytics API is in beta. Send the `anthropic-beta: analytics-usage-cost-2026-08-24` header and an [`anthropic-version`](../Endpoints/versioning.md) header on every request. The SDK and the `ant` CLI send both headers for you and fetch the remaining pages as you read the results, so `limit` sets only the page size.

Use this API to:

- **Attribute spend:** Break down cost and token usage by workspace, API key, model, service tier, or the identity that made each request.
- **Find top consumers:** Rank results by tokens, requests, or cost to answer questions such as “which API keys spend the most this month?”
- **Build time series:** Split results into daily, hourly, or per-minute buckets for dashboards and finance reports.
- **Integrate once:** The same endpoints, parameters, and response fields serve Claude Console and Claude Enterprise organizations.



**Authentication**

Claude Console organizations use an [Admin API key](manage-claude-admin-api-keys.md#create-a-key-for-a-claude-console-organization) or another [Admin API credential](manage-claude-admin-api.md#authentication), such as an OAuth token with the `org:admin` scope. Send an OAuth token in an `authorization: Bearer` header instead of the `x-api-key` header; see [Obtain an OAuth bearer token](manage-claude-admin-api.md#oauth-bearer-token).

Claude Enterprise organizations use a key with the `read:analytics` scope, created in claude.ai by the primary owner after the Analytics API is enabled for the organization; see [Get access to the Claude Enterprise Analytics API](manage-claude-analytics-api.md#get-access-to-the-claude-enterprise-analytics-api).

The examples on this page read a key from the `ANTHROPIC_API_KEY` environment variable, so set it to your key before you run them.

If you call these endpoints with an Admin API key, give the service that collects this data its own key, store it in a secrets manager, and rotate it regularly; setting a [key expiration](manage-claude-authentication.md#key-expiration) when you create the key enforces the rotation. Where you can, use a [Workload Identity Federation](manage-claude-workload-identity-federation.md) rule with the [`org:admin` scope](manage-claude-wif-reference.md#oauth-scopes) instead, so the service gets short-lived tokens and there’s no long-lived key to leak.



**Claude Platform on AWS:** Both endpoints are available. Requests use the Claude Platform on AWS base URL and authentication in place of an Admin API key (see [Making requests](../Guides/build-with-claude-claude-platform-on-aws.md#making-requests)), and AWS IAM authorizes them through the [`ListAccountUsage` and `ListAccountCost` actions](../Endpoints/claude-platform-on-aws-iam-actions.md#usage-and-cost). Each request covers only the workspaces in the AWS region of the endpoint you call, so call each region’s endpoint to cover your whole organization. `user_profile_id`, `claude_tag_category`, `claude_tag_user_id`, and the Claude Managed Agents dimensions (`agent_id`, `environment_id`, `deployment_id`, and `session_id`) are `null` on every row.



**Claude Models on Google Cloud (Anthropic managed):** Both endpoints are available. Call them through the [organization-level base URL](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#making-requests) with Google Cloud credentials instead of an Admin API key. The `/usage` endpoint needs the `usageAnalytics.list` [IAM permission](../Endpoints/claude-models-on-google-cloud-anthropic-managed-iam-permissions.md), and the `/cost` endpoint needs `costAnalytics.list`.

## Quick start

Get daily token usage for the first week of September, one row for each model and day:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

rows = client.beta.organization.analytics.usage.list(
    starting_at="2026-09-01T00:00:00Z",
    ending_at="2026-09-08T00:00:00Z",
    time_bucket_width="1d",
    group_by=["model"],
    limit=10,
)

for row in rows:
    print(f"{row.starting_at} {row.group.model}: {row.usage.total_tokens}")
```

The response has one row for each model and day that has usage, largest `total_tokens` first. This example shows a single row:

```python
{
  "data": [
    {
      "starting_at": "2026-09-03T00:00:00Z",
      "ending_at": "2026-09-04T00:00:00Z",
      "group": {
        "product": null,
        "model": "claude-sonnet-5",
        "context_window": null,
        "inference_geo": null,
        "speed": null,
        "slack_channel_id": null,
        "claude_tag_category": null,
        "claude_tag_user_id": null,
        "rbac_group_id": null,
        "workspace_id": null,
        "service_tier": null,
        "user_profile_id": null,
        "agent_id": null,
        "environment_id": null,
        "deployment_id": null,
        "session_id": null,
        "actor": null,
        "actor_type": null,
        "api_key_id": null
      },
      "usage": {
        "uncached_input_tokens": 1284500,
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 215300
        },
        "cache_read_input_tokens": 3200000,
        "output_tokens": 891000,
        "total_tokens": 5590800,
        "server_tool_use": {
          "web_search_requests": 12
        },
        "requests": 4210
      }
    }
  ],
  "has_more": true,
  "next_page": "page_V2mQ4dkt9HcbX3pLr...",
  "data_refreshed_at": "2026-09-18T16:02:11Z"
}
```





**Set a User-Agent header for integrations**

If you’re building an integration, set your User-Agent header to help Anthropic understand usage patterns:

``` block
User-Agent: YourApp/1.0.0 (https://yourapp.com)
```



## How results are shaped

- **Every row has three parts:** `starting_at` and `ending_at` give the period the row covers, `group` holds every dimension, and `usage` (or `cost` on the cost endpoint) holds the metrics.
- **Dimensions are null unless grouped:** A dimension in `group` is `null` unless you list it in `group_by[]`. A grouped dimension is also `null` on rows that have no value for it, such as `model` on code execution usage. `group_by[]` takes up to five dimensions.
- **One row for each combination:** Each row is one combination of the grouped dimensions, and every combination that has usage or cost appears exactly once across the pages of a query. With no `group_by[]` and no `time_bucket_width`, the response is a single row that totals the whole range.
- **Time buckets are optional:** Set `time_bucket_width` to `1m`, `1h`, or `1d` to split each combination by UTC bucket; each row’s `starting_at` and `ending_at` are then its bucket’s bounds. Buckets with no usage or cost produce no rows.
- **Ranked by default:** Rows are ordered by the `order_by` metric across the whole range, largest first by default (`order=asc` reverses it). To build a time series, set `time_bucket_width` and `order_by=time`. Rows then come back one time bucket after another, newest bucket first by default (`order=asc` puts the oldest first), with the largest rows first within each bucket. Fill empty buckets with zeros.
- **Filters work alongside grouping:** Most dimensions you can group by have a matching list filter in bracket notation, such as `models[]=claude-opus-5-5`. Repeat the parameter to pass several values, up to 100. Multiple values for the same filter are combined with OR, and different filters are combined with AND. Filters and `group_by[]` are independent; you can filter by any dimension with or without grouping by it, or the reverse.

Dimensions such as `model` and `actor` apply to every organization. Some, such as `api_key_id`, apply only to Claude Console organizations, and others, such as `slack_channel_id`, apply only to Claude Enterprise organizations. A dimension that doesn’t apply to your organization is `null` on every row and its filter matches nothing; the exception is `rbac_group_id`, which returns an error instead when teams aren’t available to your organization. The [usage](../Admin/http-beta-organization-analytics-usage-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. and [cost](../Admin/http-beta-organization-analytics-cost-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. API reference lists every dimension, filter, and value.

### Actors

The `actor` dimension is who a request is attributed to: a user, a service account, a federated cloud identity (an AWS or Google Cloud principal, for organizations that access Claude through their cloud platform), or, when none of those is behind the request, the API key itself. When you group by `actor`, each row’s `actor` is an object whose `type` says which kind it is. Usage that can’t be attributed to any identity has `actor: null`.

[Personal keys and service account keys](manage-claude-authentication.md#key-types) act as the user or service account they’re linked to, so their requests show that identity as the `actor` and the key in `api_key_id`. Legacy workspace keys aren’t linked to an identity, so the key appears as both the `actor` and the `api_key_id`.

Requests made without an API key, such as from the Claude Console or with a [Workload Identity Federation](manage-claude-workload-identity-federation.md) token, have `api_key_id: null`. With a Workload Identity Federation token, the `actor` is the service account the token acts as.

Whichever way a member signs in to Claude Code with their Claude Console account, the `actor` is that member. If Claude Code creates an API key at sign-in, `api_key_id` is that key, which lives in the [Claude Code workspace](manage-claude-workspaces.md#claude-code-workspace). After a [sign-in without an API key](../../02-Claude-Code-CLI/authentication.md#sign-in-without-an-api-key), `api_key_id` is `null`.

Token usage from some [Claude Managed Agents](managed-agents-overview.md) sessions is attributed to an Anthropic-managed service account (`svac_...`). For this usage, `api_key_id` is `null`. The account isn’t listed with the service accounts that you create. See [Find session usage across your organization](managed-agents-session-observability.md#find-session-usage-across-your-organization).

The `api_key_ids[]` and `actor_ids[]` filters answer different questions. `api_key_ids[]=apikey_...` matches every request the key authenticated, whoever it is attributed to. `actor_ids[]=apikey_...` matches only requests attributed to the key itself. To include usage with no API key in an `api_key_ids[]` filter, add an empty entry: `api_key_ids[]=`.

## Usage endpoint

`GET /v1/organizations/analytics/usage` returns token counts by type. `order_by` accepts `total_tokens` (the default), `output_tokens`, `uncached_input_tokens`, `requests`, or `time`.

For example, to see a week of usage for one workspace and one API key, broken down by service tier (one row for each tier, covering the whole week):

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

rows = client.beta.organization.analytics.usage.list(
    starting_at="2026-09-01T00:00:00Z",
    ending_at="2026-09-08T00:00:00Z",
    workspace_ids=["wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"],
    api_key_ids=["apikey_01Rj2N8SVvo6BePZj99NhmiT"],
    group_by=["service_tier"],
)

for row in rows:
    print(f"{row.group.service_tier}: {row.usage.total_tokens}")
```

To look up API key and workspace IDs, use the [List API Keys](../Endpoints/organization-api-keys-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. and [List Workspaces](../Endpoints/organization-workspaces-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. endpoints or the Claude Console.

To find which users, service accounts, and API keys made the most requests in a month:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

rows = client.beta.organization.analytics.usage.list(
    starting_at="2026-09-01T00:00:00Z",
    ending_at="2026-10-01T00:00:00Z",
    group_by=["actor"],
    order_by="requests",
    limit=25,
)

for row in rows:
    print(f"{row.group.actor}: {row.usage.requests}")
```

## Cost endpoint

`GET /v1/organizations/analytics/cost` accepts the same filters, dimensions, and time buckets as the `/usage` endpoint. Each row’s `cost` object holds `amount` (the cost after discounts and before any credits are applied), `list_amount` (the cost at list prices), `currency` (always `"USD"`), and `requests`. Amounts are decimal strings in cents with six decimal places: `"41280.000000"` is \$412.80 USD. `order_by` accepts `amount` (the default), `list_amount`, or `time`.

Two extra dimensions exist only on this endpoint and don’t count toward the five-dimension limit: `group_by[]=cost_type` splits each row into one row for every cost type, and `group_by[]=token_type` splits token cost into one row for every token type. `limit` doesn’t apply to these two dimensions either, so a page can hold more than `limit` rows. For example, cost by model, cost type, and token type for a month:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

rows = client.beta.organization.analytics.cost.list(
    starting_at="2026-09-01T00:00:00Z",
    ending_at="2026-10-01T00:00:00Z",
    group_by=["model", "cost_type", "token_type"],
)

for row in rows:
    print(
        f"{row.group.model} {row.group.cost_type} {row.group.token_type}: {row.cost.amount}"
    )
```

For each model, the response has five `tokens` rows (one for every token type) plus one row each for `web_search`, `code_execution`, and `session_usage`. One of those rows:

```python
{
  "starting_at": "2026-09-01T00:00:00Z",
  "ending_at": "2026-10-01T00:00:00Z",
  "group": {
    "model": "claude-opus-5",
    ...,
    "cost_type": "tokens",
    "token_type": "cache_read_input_tokens"
  },
  "cost": {
    "currency": "USD",
    "amount": "41280.000000",
    "list_amount": "51600.000000",
    "requests": null
  }
}
```



The `group` object carries every dimension and is abbreviated here. With `group_by[]=cost_type` or `token_type` specified, `requests` is `null` on every row.



Requests served under a Priority Tier commitment appear on the usage endpoint with `service_tier: "priority"` but contribute zero token cost to `amount` and `list_amount`, because your commitment covers them; the commitment fee is billed separately and isn’t in this data. Web search on those requests is billed at the standard rate. Requests beyond your committed capacity are served and priced at the standard tier.

## Date ranges and time buckets

- Timestamps are RFC 3339 with a UTC offset, for example `2026-09-01T00:00:00Z`. `starting_at` is inclusive and `ending_at` is exclusive.
- `starting_at` must be on or after January 1, 2026, and within the last 365 days. A request can span at most 31 days; `ending_at` defaults to 31 days after `starting_at` or the current time, whichever is earlier.
- `ending_at` is required whenever `time_bucket_width` is set, and with `time_bucket_width=1m` a request can span at most 24 hours.
- Both ends of the range are rounded down to a UTC bucket boundary, or to the hour when `time_bucket_width` isn’t set. For example, with `time_bucket_width=1h`, a `starting_at` of `2026-09-01T10:43:00Z` is treated as `2026-09-01T10:00:00Z` and an `ending_at` of `2026-09-01T15:43:00Z` as `2026-09-01T15:00:00Z`, so the response covers 10:00 to 15:00 UTC.

## Data freshness

Every response includes a `data_refreshed_at` timestamp, and usage after that time is missing or partial. When no data is available yet for any part of the requested range, `data_refreshed_at` is `null` and `data` is empty. Data typically refreshes within 4 hours of the underlying usage and can take up to 24 hours. Values can be revised as late events arrive and reconciliation runs, until about 7 days after the end of the calendar month. For example, values for October 1 can change until about November 7. For stable results across repeated calls, set `ending_at` at or before a `data_refreshed_at` you have already seen; for final totals, query only months that ended at least 7 days ago. Every page of a paginated query reads the same data snapshot, so `data_refreshed_at` is identical across pages.

## Migrate from the Usage and Cost API

This section is for Claude Console organizations that call the legacy [Usage and Cost API](manage-claude-usage-cost-api.md) (`/v1/organizations/usage_report/messages` and `/v1/organizations/cost_report`). Your Admin API key, the `anthropic-version` header, `starting_at` and `ending_at`, the bucket width values (`1m`, `1h`, `1d`), bracket notation, the pagination field names, and the token and cost field names carry over. What changes:

| Usage and Cost API | Usage and Cost Analytics API |
|----|----|
| No beta header | `anthropic-beta: analytics-usage-cost-2026-08-24` on every request |
| Data typically appears within 5 minutes | Data typically refreshes within 4 hours and can take up to 24 hours (see [Data freshness](#data-freshness)) |
| `data` is a list of time buckets, oldest first, including empty ones, each with a `results` list whose entries hold dimensions and metrics side by side | `data` is a list of rows ranked by `order_by`, each with its own `starting_at` and `ending_at`, dimensions in `group`, and metrics in `usage` or `cost`. Combinations with no usage or cost have no row. |
| `bucket_width`, default `1d` | `time_bucket_width`, no default. Pass `time_bucket_width=1d` to keep daily rows; omit it for whole-range totals. The cost endpoint also accepts every filter and `1m` and `1h` buckets. |
| `limit` counts time buckets per page | `limit` counts rows per page (1 to 1,000, default 20), so the number of pages depends on how many combinations have data |
| Any date range, paged forward by bucket | `starting_at` on or after January 1, 2026, and within the last 365 days, at most 31 days per request, `ending_at` required with `time_bucket_width`, and at most 24 hours with `1m` buckets (see [Date ranges and time buckets](#date-ranges-and-time-buckets)). Split longer ranges into several requests. |
| `account_ids[]`, `service_account_ids[]`, `group_by[]=account_id`, `group_by[]=service_account_id` | `actor_ids[]` with the same tagged IDs, and `group_by[]=actor` or `actor_type`; read `actor.user_id` or `actor.service_account_id`. See [Actors](#actors). |
| `context_window[]` | `context_windows[]` |
| `group_by[]=description` on the cost report, with a `description` string | No `description`. Group by the structured dimensions instead: any of `model`, `cost_type`, `token_type`, `context_window`, `service_tier`, `inference_geo`, and `speed`, all of which fit in one request. |
| An unknown API key or workspace ID returns an error | It matches nothing, including a misspelled `models[]` name. Each list takes up to 100 values. |
| `workspace_id: null` for the default workspace | The default workspace’s real `workspace_id` (see [How is the default workspace represented?](#how-is-the-default-workspace-represented)) |
| `inference_geo: "not_available"` and `service_tier: "standard"` on usage with no geo or tier | `null` for both. `inference_geos[]=not_available` still matches the rows with no inference geo. |
| Cost `service_tier` is `standard` or `batch`; `amount` such as `"123.45"` | The actual tier; `amount` with six decimal places, such as `"123.450000"`, plus `list_amount`. |
| Code execution not in the usage report; no request counts | Code execution appears as usage rows with `model: null`; adds `requests` on both endpoints and `total_tokens` on usage rows |

To reproduce the legacy daily report, request `time_bucket_width=1d` with the same `group_by[]`, page through with `limit=1000`, then group rows by `starting_at` and fill missing days with zeros. Add `order_by=time&order=asc` to get the days in order. Daily usage by model for 1 week, before:

cURL



```python
curl --globoff "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2026-09-01T00:00:00Z&\
ending_at=2026-09-08T00:00:00Z&\
group_by[]=model&\
bucket_width=1d" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_API_KEY"
```

and after:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

rows = client.beta.organization.analytics.usage.list(
    starting_at="2026-09-01T00:00:00Z",
    ending_at="2026-09-08T00:00:00Z",
    time_bucket_width="1d",
    group_by=["model"],
    limit=1000,
)

for row in rows:
    print(f"{row.starting_at} {row.group.model}: {row.usage.total_tokens}")
```

Daily cost by workspace, model, service tier, context window, and inference geo, split by cost type and token type:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

rows = client.beta.organization.analytics.cost.list(
    starting_at="2026-09-01T00:00:00Z",
    ending_at="2026-09-08T00:00:00Z",
    time_bucket_width="1d",
    group_by=[
        "workspace_id",
        "model",
        "service_tier",
        "context_window",
        "inference_geo",
        "cost_type",
        "token_type",
    ],
    limit=1000,
)

for row in rows:
    group = row.group
    print(
        f"{row.starting_at} {group.workspace_id} {group.model} {group.service_tier} "
        f"{group.context_window} {group.inference_geo} {group.cost_type} {group.token_type}: "
        f"{row.cost.amount}"
    )
```

## Migrate from the Claude Enterprise usage and cost reports

This section is for Claude Enterprise organizations that call the [Claude Enterprise Analytics API](manage-claude-analytics-api.md) report endpoints `usage_report`, `cost_report`, `user_usage_report`, and `user_cost_report` under `/v1/organizations/analytics/`. Those endpoints are legacy and remain supported. Move to `/analytics/usage` and `/analytics/cost` when you want any of the following:

- Every group in every time bucket, rather than the top 100 groups in each bucket
- Grouping by `actor` or `actor_type` together with other dimensions, on both usage and cost
- Rows ranked by a metric of your choice across the whole range, or ordered by time bucket
- One integration that also serves Claude Console organizations

Your key, the earliest date, the 365-day lookback and 31-day span, the filter and dimension names and values (except `user_ids[]` and the Claude Tag product value), the user `actor` fields, the metric and amount fields, `data_refreshed_at`, the cursor rules, and the [organization-level rate limit](manage-claude-analytics-api.md#working-with-the-api) carry over. The only new header is the `analytics-usage-cost-2026-08-24` beta header. What changes:

| Claude Enterprise reports | Usage and Cost Analytics API |
|----|----|
| `usage_report` and `cost_report` return time buckets, oldest first, including empty ones, each holding at most its top 100 groups; `bucket_width` defaults to `1d` and `limit` counts buckets | Rows covering every combination with data, ranked by `order_by`, each with its own `starting_at` and `ending_at`, dimensions in `group`, and metrics in `usage` or `cost`. `time_bucket_width` is optional and `limit` counts rows. |
| The time-bucket parameter is `bucket_width` | It is `time_bucket_width`, with the same values |
| On `usage_report` and `cost_report`, `ending_at` is optional with `bucket_width` and `1m` buckets can span up to 31 days | `ending_at` required with `time_bucket_width`; `1m` buckets span at most 24 hours per request |
| `user_usage_report` and `user_cost_report` return one row per user | `group_by[]=actor&actor_types[]=user_actor`. Without the filter you also get rows for non-user identities and an `actor: null` row for unattributed usage. |
| Claude Tag usage has `product: "claude-tag"` | `product: "claude_tag"`; `products[]` accepts either spelling |
| An unrecognized `models[]` name returns a 400 error | It matches nothing |
| `user_ids[]` | `actor_ids[]` with the same tagged `user_...` IDs |
| `exclude_deleted_users` on the per-user reports | Requires `group_by[]=actor`; without it, the request returns a 400 error. It drops only rows whose `actor` is a user with `deleted: true`; rows for other identities and rows with `actor: null` stay. |

Per-user cost for a month, before:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

rows = client.beta.organization.analytics.user_cost_report.list(
    starting_at="2026-09-01T00:00:00Z",
    ending_at="2026-10-01T00:00:00Z",
    limit=100,
)

for row in rows:
    print(f"{row.actor.user_id}: {row.amount}")
```

and after, adding a breakdown by product:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

rows = client.beta.organization.analytics.cost.list(
    starting_at="2026-09-01T00:00:00Z",
    ending_at="2026-10-01T00:00:00Z",
    actor_types=["user_actor"],
    group_by=["actor", "product"],
    limit=100,
)

for row in rows:
    actor = row.group.actor
    if actor is not None and actor.type == "user_actor":
        print(f"{actor.user_id} {row.group.product}: {row.cost.amount}")
```

## Frequently asked questions

### How is the default workspace represented?

A Claude Console organization’s default workspace has its own `wrkspc_` ID, like every other workspace. Rows for the default workspace have that ID in `workspace_id`, and you can filter on it with `workspace_ids[]`. [List Workspaces](../Endpoints/organization-workspaces-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. leaves out the default workspace unless you pass `include_default=true`. To check whether an unfamiliar `workspace_id` is the default workspace, pass it to [Get Workspace](../Endpoints/organization-workspaces-retrieve.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.: the default workspace returns `"name": "Default"`.

### How do I get per-user cost for Claude Code?

Call the cost endpoint with `products[]=claude_code&group_by[]=actor`. Claude Console organizations can also use the [Claude Code Analytics API](manage-claude-claude-code-analytics-api.md), which reports per-user Claude Code activity and estimated cost.

## See also

- [Usage and Cost API](manage-claude-usage-cost-api.md) (legacy)
- [Analytics APIs](manage-claude-analytics-api.md): which analytics API and key type your organization needs
- [Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)
- [Admin API reference](../Admin/http-beta-organization.md)
- [Pricing](../../17-Billing-Plans/about-claude-pricing.md)
