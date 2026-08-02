---
title: "Get Cost Over Time - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/cost/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:37:38Z"
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

List




# Get Cost Over Time

GET/v1/organizations/analytics/cost_report

Get cost in USD over time across a date range.

Returns cost bucketed by minute, hour, or day, optionally broken down by product, model, context window, inference region, speed, cost type, or token type. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse 

starting_at: string



Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00

.

[](#list.starting_at)



bucket_width: optional "1d" or "1h" or "1m"



Time bucket granularity.

One of the following:

"1d"



[](#list.bucket_width%5B0%5D)

"1h"



[](#list.bucket_width%5B1%5D)

"1m"



[](#list.bucket_width%5B2%5D)

[](#list.bucket_width)



context_windows: optional array of "0-200k" or "200k-1M"



Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

One of the following:

"0-200k"



[](#list.context_windows.items%5B0%5D)

"200k-1M"



[](#list.context_windows.items%5B1%5D)

[](#list.context_windows)

ending_at: optional string



End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

[](#list.ending_at)



group_by: optional array of "context_window" or "cost_type" or "inference_geo" or 5 more



Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

One of the following:

"context_window"



[](#list.group_by.items%5B0%5D)

"cost_type"



[](#list.group_by.items%5B1%5D)

"inference_geo"



[](#list.group_by.items%5B2%5D)

"model"



[](#list.group_by.items%5B3%5D)

"product"



[](#list.group_by.items%5B4%5D)

"rbac_group_id"



[](#list.group_by.items%5B5%5D)

"speed"



[](#list.group_by.items%5B6%5D)

"token_type"



[](#list.group_by.items%5B7%5D)

[](#list.group_by)



inference_geos: optional array of "global" or "not_available" or "us"



Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

One of the following:

"global"



[](#list.inference_geos.items%5B0%5D)

"not_available"



[](#list.inference_geos.items%5B1%5D)

"us"



[](#list.inference_geos.items%5B2%5D)

[](#list.inference_geos)

limit: optional number



Maximum number of time buckets per page. Defaults and caps vary by bucket_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).

[](#list.limit)

models: optional array of string



Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

[](#list.models)

page: optional string



Opaque cursor from a previous response's `next_page` field.

[](#list.page)

products: optional array of string



Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it.

[](#list.products)

rbac_group_ids: optional array of string



Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

[](#list.rbac_group_ids)



speeds: optional array of "fast" or "standard"



Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

One of the following:

"fast"



[](#list.speeds.items%5B0%5D)

"standard"



[](#list.speeds.items%5B1%5D)

[](#list.speeds)

user_ids: optional array of string



Filter to specific users by tagged user ID.

[](#list.user_ids)

##### ReturnsExpand Collapse 



CostBucket object { data, data_refreshed_at, has_more, 2 more }





data: array of object { ending_at, results, starting_at }



ending_at: string



[](#cost_bucket.data.items.ending_at)



results: array of object { amount, context_window, cost_type, 9 more }



amount: string



Amount (post-discount, pre-credit) in fractional cents.

[](#cost_bucket.data.items.results.items.amount)



context_window: "0-200k" or "200k-1M"



One of the following:

"0-200k"



[](#cost_bucket.data.items.results.items.context_window%5B0%5D)

"200k-1M"



[](#cost_bucket.data.items.results.items.context_window%5B1%5D)

[](#cost_bucket.data.items.results.items.context_window)



cost_type: "code_execution" or "tokens" or "web_search"



Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

One of the following:

"code_execution"



[](#cost_bucket.data.items.results.items.cost_type%5B0%5D)

"tokens"



[](#cost_bucket.data.items.results.items.cost_type%5B1%5D)

"web_search"



[](#cost_bucket.data.items.results.items.cost_type%5B2%5D)

[](#cost_bucket.data.items.results.items.cost_type)

currency: "USD"



[](#cost_bucket.data.items.results.items.currency)



inference_geo: "global" or "us"



One of the following:

"global"



[](#cost_bucket.data.items.results.items.inference_geo%5B0%5D)

"us"



[](#cost_bucket.data.items.results.items.inference_geo%5B1%5D)

[](#cost_bucket.data.items.results.items.inference_geo)

list_amount: string



List-price amount (pre-discount) in fractional cents.

[](#cost_bucket.data.items.results.items.list_amount)

model: string



[](#cost_bucket.data.items.results.items.model)

product: string



Product surface that produced the usage or cost. Null unless product is in group_by\[\]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

[](#cost_bucket.data.items.results.items.product)

rbac_group_id: string



RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

[](#cost_bucket.data.items.results.items.rbac_group_id)

requests: number



Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

[](#cost_bucket.data.items.results.items.requests)



speed: "fast" or "standard"



One of the following:

"fast"



[](#cost_bucket.data.items.results.items.speed%5B0%5D)

"standard"



[](#cost_bucket.data.items.results.items.speed%5B1%5D)

[](#cost_bucket.data.items.results.items.speed)



token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more



Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

One of the following:

"cache_creation.ephemeral_1h_input_tokens"



[](#cost_bucket.data.items.results.items.token_type%5B0%5D)

"cache_creation.ephemeral_5m_input_tokens"



[](#cost_bucket.data.items.results.items.token_type%5B1%5D)

"cache_read_input_tokens"



[](#cost_bucket.data.items.results.items.token_type%5B2%5D)

"output_tokens"



[](#cost_bucket.data.items.results.items.token_type%5B3%5D)

"uncached_input_tokens"



[](#cost_bucket.data.items.results.items.token_type%5B4%5D)

[](#cost_bucket.data.items.results.items.token_type)

[](#cost_bucket.data.items.results)

starting_at: string



[](#cost_bucket.data.items.starting_at)

[](#cost_bucket.data)

data_refreshed_at: string



RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

[](#cost_bucket.data_refreshed_at)

has_more: boolean



[](#cost_bucket.has_more)

next_page: string



[](#cost_bucket.next_page)

organization_id: string



ID of the Organization.

[](#cost_bucket.organization_id)

[](#cost_bucket)

Get Cost Over Time



```python
curl https://api.anthropic.com/v1/organizations/analytics/cost_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "amount": "amount",
          "context_window": "0-200k",
          "cost_type": "code_execution",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "model",
          "product": "product",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "speed": "fast",
          "token_type": "cache_creation.ephemeral_1h_input_tokens"
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
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
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "amount": "amount",
          "context_window": "0-200k",
          "cost_type": "code_execution",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "model",
          "product": "product",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "speed": "fast",
          "token_type": "cache_creation.ephemeral_1h_input_tokens"
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
