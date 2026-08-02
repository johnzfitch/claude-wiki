---
title: "List Workspace Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:40:22Z"
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


Create Workspace


Get Workspace


List Workspaces


Update Workspace


Archive Workspace

Members

Rate Limits


List Workspace Rate Limits

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

# List Workspace Rate Limits

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level override. Groups without overrides inherit the organization limits and are not listed; use `GET /v1/organizations/rate_limits` to see those.

##### Path ParametersExpand Collapse 

workspace_id: string



The ID of the workspace.

[](#list.workspace_id)

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

page: optional string



Opaque cursor from a previous response's `next_page`.

[](#list.page)

##### ReturnsExpand Collapse 



data: array of object { group_type, limits, models, type }



Rate-limit entries for the workspace, one per group that has at least one override.

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

limits: array of object { org_limit, type, value }



The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

org_limit: number



The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

[](#rate_limit_list_response.data.items.limits.items.org_limit)

type: string



The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

[](#rate_limit_list_response.data.items.limits.items.type)

value: number



The workspace-level override value for this limiter type.

[](#rate_limit_list_response.data.items.limits.items.value)

[](#rate_limit_list_response.data.items.limits)

models: array of string



Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

[](#rate_limit_list_response.data.items.models)

type: "workspace_rate_limit"



Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

[](#rate_limit_list_response.data.items.type)

[](#rate_limit_list_response.data)

next_page: string



Token to provide in as `page` in the subsequent request to retrieve the next page of data.

[](#rate_limit_list_response.next_page)

List Workspace Rate Limits



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
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
      "type": "workspace_rate_limit"
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
      "type": "workspace_rate_limit"
