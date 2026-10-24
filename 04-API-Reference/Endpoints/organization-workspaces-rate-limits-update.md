---
title: "Set Workspace Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/workspaces/rate_limits/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-21T06:29:05Z"
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

[API reference](overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fworkspaces%2Frate_limits%2Fupdate)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


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

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits/update).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces)
4.  [Rate Limits](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits)

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

Read more about versioning and our version history [here](versioning.md).

##### Body



limits: array of [WorkspaceRateLimitUpdateValue](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits#workspace_rate_limit_update_value) { type, value }



Limits to set or clear. Unspecified limit types are unchanged.

minItems1

maxItems16



type: [WorkspaceRateLimitType](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits#workspace_rate_limit_type)

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

WorkspaceRateLimit object{ type: "workspace_rate_limit", group, group_type, 4 more }

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
