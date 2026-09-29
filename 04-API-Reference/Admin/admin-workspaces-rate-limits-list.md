---
title: "List Workspace Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:43:14Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fworkspaces%2Frate_limits%2Flist)

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


Create Workspace


Get Workspace


List Workspaces


Update Workspace


Archive Workspace

Members

Rate Limits


List Workspace Rate Limits

Service Accounts

API Keys

External Keys

Usage Report

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

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Admin](http-admin.md)
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/admin/workspaces)
4.  [Rate Limits](https://platform.claude.com/docs/en/api/http/admin/workspaces/rate_limits)

# List Workspace Rate Limits

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level override. Groups without overrides inherit the organization limits and are not listed; use `GET /v1/organizations/rate_limits` to see those.

When `limit` is omitted, every matching entry is returned in a single page; when `limit` truncates the result, follow `next_page` to fetch the remaining entries.

##### Path parameters

workspace_id: string



The ID of the workspace.

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

page: optional string



Opaque cursor from a previous response's `next_page`.

##### Returns



data: array of object{ group_type, limits, models, 3 more }



Rate-limit entries for the workspace, one per group that has at least one override.

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

limits: array of object{ org_limit, type, value }



The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

org_limit: number or null



The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

type: string



The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number



The workspace-level override value for this limiter type.

models: array of string or null



Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

rate_limit_id: string



The `id` of the RateLimit group this override applies to.



type: "workspace_rate_limit"



Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

defaultworkspace_rate_limit

workspace_id: string



ID of the Workspace this override applies to.

next_page: string or null



Opaque cursor for the next page of results, or `null` when no entries remain beyond this response.

List Workspace Rate Limits

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
```

Response 200



```python
{
  "data": [
    {
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "rate_limit_id": "rate_limit_id",
      "type": "workspace_rate_limit",
      "workspace_id": "workspace_id"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "rate_limit_id": "rate_limit_id",
      "type": "workspace_rate_limit",
      "workspace_id": "workspace_id"
