---
title: "List Organization Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/rate_limits/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:41:36Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Frate_limits%2Flist)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


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

Cost Report

Analytics

Spend Limits

Rate Limits


List Organization Rate Limits

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

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Admin](http-admin.md)
3.  [Rate Limits](https://platform.claude.com/docs/en/api/http/admin/rate_limits)

# List Organization Rate Limits

GET/v1/organizations/rate_limits

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family or an API-surface category such as the Files API or Message Batches) and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single page; when `limit` truncates the result, follow `next_page` to fetch the remaining entries.

##### Query parameters



group_type: optional "batch" or "files" or "model_group" or 3 more



Filter by group type.

One of the following:

"batch"



"files"



"model_group"



"skills"



"token_count"



"web_search"





limit: optional number



Maximum number of items to return per page. Ranges from `1` to `1000`.

When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

maximum1000

minimum1

model: optional string



Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

page: optional string



Opaque cursor from a previous response's `next_page`.

##### Returns



data: array of object{ id, group_type, limits, 2 more }



Rate-limit entries for the organization, one per group.

id: string



Stable identifier for this rate-limit group within the organization.



group_type: "batch" or "files" or "model_group" or 3 more



The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

One of the following:

"batch"



"files"



"model_group"



"skills"



"token_count"



"web_search"





limits: array of object{ type, value }



The limiter values that apply to this group.

type: string



The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number



The configured limit value for this limiter type.

models: array of string or null



Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.



type: "rate_limit"



Object type. Always `rate_limit` for organization rate-limit entries.

defaultrate_limit

next_page: string or null



Opaque cursor for the next page of results, or `null` when no entries remain beyond this response.

List Organization Rate Limits

cURL



```python
curl https://api.anthropic.com/v1/organizations/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
