---
title: "Usage Report - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/usage_report"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:37:59Z"
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


Get Messages Usage Report


Get Claude Code Usage Report

Cost Report

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

Usage report




# Usage Report

##### [Get Messages Usage Report](/docs/en/api/admin/usage_report/retrieve_messages)

GET/v1/organizations/usage_report/messages

##### [Get Claude Code Usage Report](/docs/en/api/admin/usage_report/retrieve_claude_code)

GET/v1/organizations/usage_report/claude_code

##### ModelsExpand Collapse 



ClaudeCodeUsageReport object { data, has_more, next_page }





data: array of object { actor, core_metrics, customer_type, 6 more }



List of Claude Code usage records for the requested date.



actor: object { email_address, type } or object { api_key_name, type }



The user or API key that performed the Claude Code actions.

One of the following:



ClaudeCodeUserActor object { email_address, type }



email_address: string



Email address of the user who performed Claude Code actions.

[](#claude_code_usage_report.data.items.actor%5B0%5D.email_address)

type: "user_actor"



[](#claude_code_usage_report.data.items.actor%5B0%5D.type)

[](#claude_code_usage_report.data.items.actor%5B0%5D)



ClaudeCodeAPIActor object { api_key_name, type }



api_key_name: string



Name of the API key used to perform Claude Code actions.

[](#claude_code_usage_report.data.items.actor%5B1%5D.api_key_name)

type: "api_actor"



[](#claude_code_usage_report.data.items.actor%5B1%5D.type)

[](#claude_code_usage_report.data.items.actor%5B1%5D)

[](#claude_code_usage_report.data.items.actor)



core_metrics: object { commits_by_claude_code, lines_of_code, num_sessions, pull_requests_by_claude_code }



Core productivity metrics measuring Claude Code usage and impact.

commits_by_claude_code: number



Number of git commits created through Claude Code's commit functionality.

[](#claude_code_usage_report.data.items.core_metrics.commits_by_claude_code)



lines_of_code: object { added, removed }



Statistics on code changes made through Claude Code.

added: number



Total number of lines of code added across all files by Claude Code.

[](#claude_code_usage_report.data.items.core_metrics.lines_of_code.added)

removed: number



Total number of lines of code removed across all files by Claude Code.

[](#claude_code_usage_report.data.items.core_metrics.lines_of_code.removed)

[](#claude_code_usage_report.data.items.core_metrics.lines_of_code)

num_sessions: number



Number of distinct Claude Code sessions initiated by this actor.

[](#claude_code_usage_report.data.items.core_metrics.num_sessions)

pull_requests_by_claude_code: number



Number of pull requests created through Claude Code's PR functionality.

[](#claude_code_usage_report.data.items.core_metrics.pull_requests_by_claude_code)

[](#claude_code_usage_report.data.items.core_metrics)



customer_type: "api" or "subscription"



Type of customer account (api for API customers, subscription for Pro/Team customers).

One of the following:

"api"



[](#claude_code_usage_report.data.items.customer_type%5B0%5D)

"subscription"



[](#claude_code_usage_report.data.items.customer_type%5B1%5D)

[](#claude_code_usage_report.data.items.customer_type)

date: string



UTC date for the usage metrics in YYYY-MM-DD format.

[](#claude_code_usage_report.data.items.date)



model_breakdown: array of object { estimated_cost, model, tokens }



Token usage and cost breakdown by AI model used.



estimated_cost: object { amount, currency }



Estimated cost for using this model

amount: number



Estimated cost amount in minor currency units (e.g., cents for USD).

[](#claude_code_usage_report.data.items.model_breakdown.items.estimated_cost.amount)

currency: string



Currency code for the estimated cost (e.g., 'USD').

[](#claude_code_usage_report.data.items.model_breakdown.items.estimated_cost.currency)

[](#claude_code_usage_report.data.items.model_breakdown.items.estimated_cost)

model: string



Name of the AI model used for Claude Code interactions.

[](#claude_code_usage_report.data.items.model_breakdown.items.model)



tokens: object { cache_creation, cache_read, input, output }



Token usage breakdown for this model

cache_creation: number



Number of cache creation tokens consumed by this model.

[](#claude_code_usage_report.data.items.model_breakdown.items.tokens.cache_creation)

cache_read: number



Number of cache read tokens consumed by this model.

[](#claude_code_usage_report.data.items.model_breakdown.items.tokens.cache_read)

input: number



Number of input tokens consumed by this model.

[](#claude_code_usage_report.data.items.model_breakdown.items.tokens.input)

output: number



Number of output tokens generated by this model.

[](#claude_code_usage_report.data.items.model_breakdown.items.tokens.output)

[](#claude_code_usage_report.data.items.model_breakdown.items.tokens)

[](#claude_code_usage_report.data.items.model_breakdown)

organization_id: string



ID of the organization that owns the Claude Code usage.

[](#claude_code_usage_report.data.items.organization_id)

terminal_type: string



Type of terminal or environment where Claude Code was used.

[](#claude_code_usage_report.data.items.terminal_type)



tool_actions: map\[object { accepted, rejected } \]



Breakdown of tool action acceptance and rejection rates by tool type.

accepted: number



Number of tool action proposals that the user accepted.

[](#claude_code_usage_report.data.items.tool_actions.items.accepted)

rejected: number



Number of tool action proposals that the user rejected.

[](#claude_code_usage_report.data.items.tool_actions.items.rejected)

[](#claude_code_usage_report.data.items.tool_actions)



subscription_type: optional "enterprise" or "team"



Subscription tier for subscription customers. `null` for API customers.

One of the following:

"enterprise"



[](#claude_code_usage_report.data.items.subscription_type%5B0%5D)

"team"



[](#claude_code_usage_report.data.items.subscription_type%5B1%5D)

[](#claude_code_usage_report.data.items.subscription_type)

[](#claude_code_usage_report.data)

has_more: boolean



True if there are more records available beyond the current page.

[](#claude_code_usage_report.has_more)

next_page: string



Opaque cursor token for fetching the next page of results, or null if no more pages are available.

[](#claude_code_usage_report.next_page)

[](#claude_code_usage_report)



MessagesUsageReport object { data, has_more, next_page }





data: array of object { ending_at, results, starting_at }



ending_at: string



End of the time bucket (exclusive) in RFC 3339 format.

[](#messages_usage_report.data.items.ending_at)



results: array of object { account_id, api_key_id, cache_creation, 10 more }



List of usage items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

account_id: string



ID of the user account that made the request. `null` if not grouping by account or for non-OAuth requests.

[](#messages_usage_report.data.items.results.items.account_id)

api_key_id: string



ID of the API key used. `null` if not grouping by API key or for usage in the Anthropic Console.

[](#messages_usage_report.data.items.results.items.api_key_id)



cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }



The number of input tokens for cache creation.

ephemeral_1h_input_tokens: number



The number of input tokens used to create the 1 hour cache entry.

[](#messages_usage_report.data.items.results.items.cache_creation.ephemeral_1h_input_tokens)

ephemeral_5m_input_tokens: number



The number of input tokens used to create the 5 minute cache entry.

[](#messages_usage_report.data.items.results.items.cache_creation.ephemeral_5m_input_tokens)

[](#messages_usage_report.data.items.results.items.cache_creation)

cache_read_input_tokens: number



The number of input tokens read from the cache.

[](#messages_usage_report.data.items.results.items.cache_read_input_tokens)



context_window: "0-200k" or "200k-1M"



Context window used. `null` if not grouping by context window.

One of the following:

"0-200k"



[](#messages_usage_report.data.items.results.items.context_window%5B0%5D)

"200k-1M"



[](#messages_usage_report.data.items.results.items.context_window%5B1%5D)

[](#messages_usage_report.data.items.results.items.context_window)

inference_geo: string



Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`. For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

[](#messages_usage_report.data.items.results.items.inference_geo)

model: string



Model used. `null` if not grouping by model.

[](#messages_usage_report.data.items.results.items.model)

output_tokens: number



The number of output tokens generated.

[](#messages_usage_report.data.items.results.items.output_tokens)



server_tool_use: object { web_search_requests }



Server-side tool usage metrics.

web_search_requests: number



The number of web search requests made.

[](#messages_usage_report.data.items.results.items.server_tool_use.web_search_requests)

[](#messages_usage_report.data.items.results.items.server_tool_use)

service_account_id: string



ID of the service account that made the request. `null` if not grouping by service account or for non-OIDC-federation requests.

[](#messages_usage_report.data.items.results.items.service_account_id)



service_tier: "batch" or "flex" or "flex_discount" or 3 more



Service tier used. `null` if not grouping by service tier.

One of the following:

"batch"



[](#messages_usage_report.data.items.results.items.service_tier%5B0%5D)

"flex"



[](#messages_usage_report.data.items.results.items.service_tier%5B1%5D)

"flex_discount"



[](#messages_usage_report.data.items.results.items.service_tier%5B2%5D)

"priority"



[](#messages_usage_report.data.items.results.items.service_tier%5B3%5D)

"priority_on_demand"



[](#messages_usage_report.data.items.results.items.service_tier%5B4%5D)

"standard"



[](#messages_usage_report.data.items.results.items.service_tier%5B5%5D)

[](#messages_usage_report.data.items.results.items.service_tier)

uncached_input_tokens: number



The number of uncached input tokens processed.

[](#messages_usage_report.data.items.results.items.uncached_input_tokens)

workspace_id: string



ID of the Workspace used. `null` if not grouping by workspace or for the default workspace.

[](#messages_usage_report.data.items.results.items.workspace_id)

[](#messages_usage_report.data.items.results)

starting_at: string



Start of the time bucket (inclusive) in RFC 3339 format.

[](#messages_usage_report.data.items.starting_at)

[](#messages_usage_report.data)

has_more: boolean



Indicates if there are more results.

[](#messages_usage_report.has_more)

next_page: string



Token to provide in as `page` in the subsequent request to retrieve the next page of data.

[](#messages_usage_report.next_page)
