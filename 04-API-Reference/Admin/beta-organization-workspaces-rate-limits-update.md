---
title: "Set Workspace Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/workspaces/rate_limits/update"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-21T06:29:13Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fworkspaces%2Frate_limits%2Fupdate)

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


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces


List Workspaces


Create Workspace


Get Workspace


Update Workspace


Archive Workspace

Rate Limits


List Workspace Rate Limits


Set Workspace Rate Limits

Members

Service Accounts

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations

Webhooks


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Delete User Profile


Create Enrollment URL

Action URLs


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


Compliance API

Activities

Organizations

Groups

Apps


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](../Endpoints/opentelemetry-spans.md)

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)
5.  [Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits)

# Set Workspace Rate Limits

Copy page



cURL

POST/v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}

Set or clear rate-limit overrides for one rate-limit group in a workspace.

Only the limiter types named in `limits` change: an integer `value` sets that type's override and `null` clears it. Types not named keep their current value. A value above the organization's own limit is stored, but the organization limit still applies, so the lower of the two is enforced.

Returns the targeted group's entry with this request applied, in the shape `GET /v1/organizations/workspaces/{workspace_id}/rate_limits` returns. Changes take effect within about an hour.

##### Path parameters

workspace_id: string



The ID of the workspace.

rate_limit_id: string



The `id` of the organization's rate-limit entry to set overrides for.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Body



limits: array of [BetaWorkspaceRateLimitUpdateValue](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits#beta_workspace_rate_limit_update_value) { type, value }



Limits to set or clear. Unspecified limit types are unchanged.

minItems1

maxItems16



type: [BetaWorkspaceRateLimitType](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits#beta_workspace_rate_limit_type)



Rate limiter type.

One of the following:

"fast_itpmca"



"fast_otpm"



"input_tokens_per_minute"



"input_tokens_per_minute_cache_aware"



"output_tokens_per_minute"



"requests_per_minute"



"tokens_per_day"



"tokens_per_minute"



"tool_uses_per_second"





value: number or null



New limit value. Set to null to clear the workspace override and fall back to the organization limit.

minimum0

maximum9007199254740991

##### Returns



BetaWorkspaceRateLimit object{ type: "workspace_rate_limit", group, group_type, 4 more }



Set Workspace Rate Limits

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits/$RATE_LIMIT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "limits": [
            {
              "type": "fast_itpmca",
              "value": 0
            }
          ]
        }'
```

Response 200



```python
{
  "group": {
    "id": "id",
    "display_name": "display_name",
    "type": "model_group"
  },
  "group_type": "batch",
  "limits": [
    {
      "org_limit": 0,
      "source": {
        "type": "workspace"
      },
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
```

##### Returns Examples

Response 200



```python
{
  "group": {
    "id": "id",
    "display_name": "display_name",
    "type": "model_group"
  },
  "group_type": "batch",
  "limits": [
    {
      "org_limit": 0,
      "source": {
        "type": "workspace"
      },
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
