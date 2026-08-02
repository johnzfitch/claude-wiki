---
title: "Cost Report - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/cost_report"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:37:41Z"
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


Get Cost Report

Analytics

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

Cost report




# Cost Report

##### [Get Cost Report](/docs/en/api/admin/cost_report/retrieve)

GET/v1/organizations/cost_report

##### ModelsExpand Collapse 



CostReport object { data, has_more, next_page }





data: array of object { ending_at, results, starting_at }



ending_at: string



End of the time bucket (exclusive) in RFC 3339 format.

[](#cost_report.data.items.ending_at)



results: array of object { amount, context_window, cost_type, 7 more }



List of cost items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

amount: string



Cost amount in lowest currency units (e.g. cents) as a decimal string. For example, `"123.45"` in `"USD"` represents `$1.23`.

[](#cost_report.data.items.results.items.amount)



context_window: "0-200k" or "200k-1M"



Input context window used. `null` if not grouping by description or for non-token costs.

One of the following:

"0-200k"



[](#cost_report.data.items.results.items.context_window%5B0%5D)

"200k-1M"



[](#cost_report.data.items.results.items.context_window%5B1%5D)

[](#cost_report.data.items.results.items.context_window)



cost_type: "code_execution" or "session_usage" or "tokens" or "web_search"



Type of cost. `null` if not grouping by description.

One of the following:

"code_execution"



[](#cost_report.data.items.results.items.cost_type%5B0%5D)

"session_usage"



[](#cost_report.data.items.results.items.cost_type%5B1%5D)

"tokens"



[](#cost_report.data.items.results.items.cost_type%5B2%5D)

"web_search"



[](#cost_report.data.items.results.items.cost_type%5B3%5D)

[](#cost_report.data.items.results.items.cost_type)

currency: string



Currency code for the cost amount. Currently always `"USD"`.

[](#cost_report.data.items.results.items.currency)

description: string



Description of the cost item. `null` if not grouping by description.

[](#cost_report.data.items.results.items.description)

inference_geo: string



Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`. For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

[](#cost_report.data.items.results.items.inference_geo)

model: string



Model name used. `null` if not grouping by description or for non-token costs.

[](#cost_report.data.items.results.items.model)



service_tier: "batch" or "standard"



Service tier used. `null` if not grouping by description or for non-token costs.

One of the following:

"batch"



[](#cost_report.data.items.results.items.service_tier%5B0%5D)

"standard"



[](#cost_report.data.items.results.items.service_tier%5B1%5D)

[](#cost_report.data.items.results.items.service_tier)



token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more



Type of token. `null` if not grouping by description or for non-token costs.

One of the following:

"cache_creation.ephemeral_1h_input_tokens"



[](#cost_report.data.items.results.items.token_type%5B0%5D)

"cache_creation.ephemeral_5m_input_tokens"



[](#cost_report.data.items.results.items.token_type%5B1%5D)

"cache_read_input_tokens"



[](#cost_report.data.items.results.items.token_type%5B2%5D)

"output_tokens"



[](#cost_report.data.items.results.items.token_type%5B3%5D)

"uncached_input_tokens"



[](#cost_report.data.items.results.items.token_type%5B4%5D)

[](#cost_report.data.items.results.items.token_type)

workspace_id: string



ID of the Workspace this cost is associated with. `null` if not grouping by workspace or for the default workspace.

[](#cost_report.data.items.results.items.workspace_id)

[](#cost_report.data.items.results)

starting_at: string



Start of the time bucket (inclusive) in RFC 3339 format.

[](#cost_report.data.items.starting_at)

[](#cost_report.data)

has_more: boolean



Indicates if there are more results.

[](#cost_report.has_more)

next_page: string



Token to provide in as `page` in the subsequent request to retrieve the next page of data.

[](#cost_report.next_page)
