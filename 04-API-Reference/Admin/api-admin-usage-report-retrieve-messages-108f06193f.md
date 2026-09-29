---
title: "Get Messages Usage Report - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:42:49Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fusage_report%2Fretrieve_messages)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


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


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


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


Webhooks


Unwrap


Parse Unverified


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report


Get Messages Usage Report


Get Claude Code Usage Report

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


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



1.  [API reference](/docs/en/api/http)
2.  [Admin](/docs/en/api/http/admin)
3.  [Usage Report](/docs/en/api/http/admin/usage_report)

# Get Messages Usage Report

GET/v1/organizations/usage_report/messages

Get Messages Usage Report

##### Query parameters



starting_at: string



Time buckets that start on or after this RFC 3339 timestamp will be returned. Each time bucket will be snapped to the start of the minute/hour/day in UTC.

formatdate-time

account_ids: optional array of string



Restrict usage returned to the specified user account ID(s).

api_key_ids: optional array of string



Restrict usage returned to the specified API key ID(s).



bucket_width: optional "1d" or "1h" or "1m"



Time granularity of the response data.

default1d

One of the following:

"1d"



"1h"



"1m"





context_window: optional array of "0-200k" or "200k-1M"



Restrict usage returned to the specified context window(s).

One of the following:

"0-200k"



"200k-1M"





ending_at: optional string



Time buckets that end before this RFC 3339 timestamp will be returned.

formatdate-time



group_by: optional array of "account_id" or "api_key_id" or "context_window" or 6 more



Group by any subset of the available options. Grouping by `speed` requires the `fast-mode-2026-02-01` beta header.

One of the following:

"account_id"



"api_key_id"



"context_window"



"inference_geo"



"model"



"service_account_id"



"service_tier"



"speed"



"workspace_id"





inference_geos: optional array of "global" or "not_available" or "us"



Restrict usage returned to the specified inference geo(s). Use `not_available` for models that do not support specifying `inference_geo`.

One of the following:

"global"



"not_available"



"us"





limit: optional number



Maximum number of time buckets to return in the response.

The default and max limits depend on `bucket_width`: • `"1d"`: Default of 7 days, maximum of 31 days • `"1h"`: Default of 24 hours, maximum of 168 hours • `"1m"`: Default of 60 minutes, maximum of 1440 minutes

models: optional array of string



Restrict usage returned to the specified model(s).

page: optional string



Optionally set to the `next_page` token from the previous response.

service_account_ids: optional array of string



Restrict usage returned to the specified service account ID(s).



service_tiers: optional array of "batch" or "flex" or "flex_discount" or 3 more



Restrict usage returned to the specified service tier(s).

One of the following:

"batch"



"flex"



"flex_discount"



"priority"



"priority_on_demand"



"standard"





speeds: optional array of "fast" or "standard"



Restrict usage returned to the specified speed(s) (Claude Code research preview). Requires the `fast-mode-2026-02-01` beta header.

One of the following:

"fast"



"standard"



workspace_ids: optional array of string



Restrict usage returned to the specified workspace ID(s).

##### Headers



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### Returns



MessagesUsageReport object{ data, has_more, next_page }



Get Messages Usage Report

cURL



```python
curl https://api.anthropic.com/v1/organizations/usage_report/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
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
          "model": "claude-opus-5",
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
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
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
          "model": "claude-opus-5",
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
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
