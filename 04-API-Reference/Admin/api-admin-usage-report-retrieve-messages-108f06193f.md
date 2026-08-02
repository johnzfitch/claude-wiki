---
title: "Get Messages Usage Report - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:14Z"
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

Retrieve messages




# Get Messages Usage Report

GET/v1/organizations/usage_report/messages

Get Messages Usage Report

##### Query ParametersExpand Collapse 

starting_at: string



Time buckets that start on or after this RFC 3339 timestamp will be returned. Each time bucket will be snapped to the start of the minute/hour/day in UTC.

[](#retrieve_messages.starting_at)

account_ids: optional array of string



Restrict usage returned to the specified user account ID(s).

[](#retrieve_messages.account_ids)

api_key_ids: optional array of string



Restrict usage returned to the specified API key ID(s).

[](#retrieve_messages.api_key_ids)



bucket_width: optional "1d" or "1h" or "1m"



Time granularity of the response data.

One of the following:

"1d"



[](#retrieve_messages.bucket_width%5B0%5D)

"1h"



[](#retrieve_messages.bucket_width%5B1%5D)

"1m"



[](#retrieve_messages.bucket_width%5B2%5D)

[](#retrieve_messages.bucket_width)



context_window: optional array of "0-200k" or "200k-1M"



Restrict usage returned to the specified context window(s).

One of the following:

"0-200k"



[](#retrieve_messages.context_window.items%5B0%5D)

"200k-1M"



[](#retrieve_messages.context_window.items%5B1%5D)

[](#retrieve_messages.context_window)

ending_at: optional string



Time buckets that end before this RFC 3339 timestamp will be returned.

[](#retrieve_messages.ending_at)



group_by: optional array of "account_id" or "api_key_id" or "context_window" or 6 more



Group by any subset of the available options. Grouping by `speed` requires the `fast-mode-2026-02-01` beta header.

One of the following:

"account_id"



[](#retrieve_messages.group_by.items%5B0%5D)

"api_key_id"



[](#retrieve_messages.group_by.items%5B1%5D)

"context_window"



[](#retrieve_messages.group_by.items%5B2%5D)

"inference_geo"



[](#retrieve_messages.group_by.items%5B3%5D)

"model"



[](#retrieve_messages.group_by.items%5B4%5D)

"service_account_id"



[](#retrieve_messages.group_by.items%5B5%5D)

"service_tier"



[](#retrieve_messages.group_by.items%5B6%5D)

"speed"



[](#retrieve_messages.group_by.items%5B7%5D)

"workspace_id"



[](#retrieve_messages.group_by.items%5B8%5D)

[](#retrieve_messages.group_by)



inference_geos: optional array of "global" or "not_available" or "us"



Restrict usage returned to the specified inference geo(s). Use `not_available` for models that do not support specifying `inference_geo`.

One of the following:

"global"



[](#retrieve_messages.inference_geos.items%5B0%5D)

"not_available"



[](#retrieve_messages.inference_geos.items%5B1%5D)

"us"



[](#retrieve_messages.inference_geos.items%5B2%5D)

[](#retrieve_messages.inference_geos)



limit: optional number



Maximum number of time buckets to return in the response.

The default and max limits depend on `bucket_width`: • `"1d"`: Default of 7 days, maximum of 31 days • `"1h"`: Default of 24 hours, maximum of 168 hours • `"1m"`: Default of 60 minutes, maximum of 1440 minutes

[](#retrieve_messages.limit)

models: optional array of string



Restrict usage returned to the specified model(s).

[](#retrieve_messages.models)

page: optional string



Optionally set to the `next_page` token from the previous response.

[](#retrieve_messages.page)

service_account_ids: optional array of string



Restrict usage returned to the specified service account ID(s).

[](#retrieve_messages.service_account_ids)



service_tiers: optional array of "batch" or "flex" or "flex_discount" or 3 more



Restrict usage returned to the specified service tier(s).

One of the following:

"batch"



[](#retrieve_messages.service_tiers.items%5B0%5D)

"flex"



[](#retrieve_messages.service_tiers.items%5B1%5D)

"flex_discount"



[](#retrieve_messages.service_tiers.items%5B2%5D)

"priority"



[](#retrieve_messages.service_tiers.items%5B3%5D)

"priority_on_demand"



[](#retrieve_messages.service_tiers.items%5B4%5D)

"standard"



[](#retrieve_messages.service_tiers.items%5B5%5D)

[](#retrieve_messages.service_tiers)



speeds: optional array of "fast" or "standard"



Restrict usage returned to the specified speed(s) (Claude Code research preview). Requires the `fast-mode-2026-02-01` beta header.

One of the following:

"fast"



[](#retrieve_messages.speeds.items%5B0%5D)

"standard"



[](#retrieve_messages.speeds.items%5B1%5D)

[](#retrieve_messages.speeds)

workspace_ids: optional array of string



Restrict usage returned to the specified workspace ID(s).

[](#retrieve_messages.workspace_ids)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

[](#retrieve_messages.anthropic-beta)

##### ReturnsExpand Collapse 

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

[](#messages_usage_report)

Get Messages Usage Report



```python
curl https://api.anthropic.com/v1/organizations/usage_report/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "account_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "service_account_id": "svac_01Hk3R9TWxq7CfQak00OiVw4",
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "account_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "service_account_id": "svac_01Hk3R9TWxq7CfQak00OiVw4",
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"
