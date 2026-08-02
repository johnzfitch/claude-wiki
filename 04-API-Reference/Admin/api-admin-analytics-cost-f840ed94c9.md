---
title: "Cost - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/cost"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:58Z"
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

Cost




# Cost

##### [Get Cost Over Time](/docs/en/api/admin/analytics/cost/list)

GET/v1/organizations/analytics/cost_report

##### [Get Per-User Cost](/docs/en/api/admin/analytics/cost/list_by_user)

GET/v1/organizations/analytics/user_cost_report

##### ModelsExpand Collapse 

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
