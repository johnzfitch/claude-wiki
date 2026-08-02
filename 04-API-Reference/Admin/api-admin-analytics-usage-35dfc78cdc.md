---
title: "Usage - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/usage"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:40:00Z"
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

Usage




# Usage

##### [Get Token Usage Over Time](/docs/en/api/admin/analytics/usage/list)

GET/v1/organizations/analytics/usage_report

##### [Get Per-User Token Usage](/docs/en/api/admin/analytics/usage/list_by_user)

GET/v1/organizations/analytics/user_usage_report

##### ModelsExpand Collapse 



UsageBucket object { data, data_refreshed_at, has_more, 2 more }





data: array of object { ending_at, results, starting_at }



ending_at: string



[](#usage_bucket.data.items.ending_at)



results: array of object { cache_creation, cache_read_input_tokens, context_window, 9 more }





cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }



ephemeral_1h_input_tokens: number



The number of input tokens used to create the 1 hour cache entry.

[](#usage_bucket.data.items.results.items.cache_creation.ephemeral_1h_input_tokens)

ephemeral_5m_input_tokens: number



The number of input tokens used to create the 5 minute cache entry.

[](#usage_bucket.data.items.results.items.cache_creation.ephemeral_5m_input_tokens)

[](#usage_bucket.data.items.results.items.cache_creation)

cache_read_input_tokens: number



The number of input tokens read from the cache.

[](#usage_bucket.data.items.results.items.cache_read_input_tokens)



context_window: "0-200k" or "200k-1M"



One of the following:

"0-200k"



[](#usage_bucket.data.items.results.items.context_window%5B0%5D)

"200k-1M"



[](#usage_bucket.data.items.results.items.context_window%5B1%5D)

[](#usage_bucket.data.items.results.items.context_window)



inference_geo: "global" or "us"



One of the following:

"global"



[](#usage_bucket.data.items.results.items.inference_geo%5B0%5D)

"us"



[](#usage_bucket.data.items.results.items.inference_geo%5B1%5D)

[](#usage_bucket.data.items.results.items.inference_geo)

model: string



[](#usage_bucket.data.items.results.items.model)

output_tokens: number



The number of output tokens generated.

[](#usage_bucket.data.items.results.items.output_tokens)

product: string



Product surface that produced the usage or cost. Null unless product is in group_by\[\]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

[](#usage_bucket.data.items.results.items.product)

rbac_group_id: string



RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

[](#usage_bucket.data.items.results.items.rbac_group_id)

requests: number



Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

[](#usage_bucket.data.items.results.items.requests)



server_tool_use: object { web_search_requests }



web_search_requests: number



The number of web search requests made.

[](#usage_bucket.data.items.results.items.server_tool_use.web_search_requests)

[](#usage_bucket.data.items.results.items.server_tool_use)



speed: "fast" or "standard"



One of the following:

"fast"



[](#usage_bucket.data.items.results.items.speed%5B0%5D)

"standard"



[](#usage_bucket.data.items.results.items.speed%5B1%5D)

[](#usage_bucket.data.items.results.items.speed)

uncached_input_tokens: number



The number of uncached input tokens processed.

[](#usage_bucket.data.items.results.items.uncached_input_tokens)

[](#usage_bucket.data.items.results)

starting_at: string



[](#usage_bucket.data.items.starting_at)

[](#usage_bucket.data)

data_refreshed_at: string



RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

[](#usage_bucket.data_refreshed_at)

has_more: boolean



[](#usage_bucket.has_more)

next_page: string



[](#usage_bucket.next_page)

organization_id: string



ID of the Organization.

[](#usage_bucket.organization_id)

[](#usage_bucket)

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
