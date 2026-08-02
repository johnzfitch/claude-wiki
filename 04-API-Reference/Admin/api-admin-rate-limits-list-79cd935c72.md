---
title: "List Organization Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/rate_limits/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:37:51Z"
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

Spend Limits

Rate Limits


List Organization Rate Limits

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

# List Organization Rate Limits

GET/v1/organizations/rate_limits

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family or an API-surface category such as the Files API or Message Batches) and contains the set of limiter values that apply to it.

##### Query ParametersExpand Collapse 



group_type: optional "batch" or "files" or "model_group" or 3 more



Filter by group type.

One of the following:

"batch"



[](#list.group_type%5B0%5D)

"files"



[](#list.group_type%5B1%5D)

"model_group"



[](#list.group_type%5B2%5D)

"skills"



[](#list.group_type%5B3%5D)

"token_count"



[](#list.group_type%5B4%5D)

"web_search"



[](#list.group_type%5B5%5D)

[](#list.group_type)

model: optional string



Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

[](#list.model)

page: optional string



Opaque cursor from a previous response's `next_page`.

[](#list.page)

##### ReturnsExpand Collapse 



data: array of object { group_type, limits, models, type }



Rate-limit entries for the organization, one per group.



group_type: "batch" or "files" or "model_group" or 3 more



The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

One of the following:

"batch"



[](#rate_limit_list_response.data.items.group_type%5B0%5D)

"files"



[](#rate_limit_list_response.data.items.group_type%5B1%5D)

"model_group"



[](#rate_limit_list_response.data.items.group_type%5B2%5D)

"skills"



[](#rate_limit_list_response.data.items.group_type%5B3%5D)

"token_count"



[](#rate_limit_list_response.data.items.group_type%5B4%5D)

"web_search"



[](#rate_limit_list_response.data.items.group_type%5B5%5D)

[](#rate_limit_list_response.data.items.group_type)



limits: array of object { type, value }



The limiter values that apply to this group.

type: string



The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

[](#rate_limit_list_response.data.items.limits.items.type)

value: number



The configured limit value for this limiter type.

[](#rate_limit_list_response.data.items.limits.items.value)

[](#rate_limit_list_response.data.items.limits)

models: array of string



Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

[](#rate_limit_list_response.data.items.models)

type: "rate_limit"



Object type. Always `rate_limit` for organization rate-limit entries.

[](#rate_limit_list_response.data.items.type)

[](#rate_limit_list_response.data)

next_page: string



Token to provide in as `page` in the subsequent request to retrieve the next page of data.

[](#rate_limit_list_response.next_page)

List Organization Rate Limits



```python
curl https://api.anthropic.com/v1/organizations/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
