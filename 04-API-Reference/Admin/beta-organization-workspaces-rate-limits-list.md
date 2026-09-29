---
title: "List Workspace Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/workspaces/rate_limits/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-28T06:33:27Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fworkspaces%2Frate_limits%2Flist)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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


List Workspaces


Create Workspace


Get Workspace


Update Workspace


Archive Workspace

Rate Limits


List Workspace Rate Limits

Members

Service Accounts

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


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

cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/http-beta.md)
3.  [Organization](http-beta-organization.md)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)
5.  [Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits)

# List Workspace Rate Limits

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List a workspace's rate limits.

By default, returns only the groups and limiter types that have a workspace-level override. With `include_inherited=true`, returns every group with organization-level limits the workspace can see, listing for each the values it inherits from the organization as well as its own overrides. Each value's `source` says which it is.

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

include_inherited: optional boolean



Also list the limiter values the workspace inherits from the organization, including groups with no workspace-level override.

defaultfalse



limit: optional number



Maximum number of items to return per page. Ranges from `1` to `1000`.

When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

minimum1

maximum1000

page: optional string



Opaque cursor from a previous response's `next_page`.

##### Returns



data: array of [BetaWorkspaceRateLimit](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits#beta_workspace_rate_limit) { type: "workspace_rate_limit", group, group_type, 4 more }



Rate-limit entries for the workspace: one per group with at least one override, or, with `include_inherited` set to `true`, one per group the workspace can see that has organization-level limits.



type: "workspace_rate_limit"



Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

defaultworkspace_rate_limit



group: [BetaOrganizationRateLimitModelGroup](https://platform.claude.com/docs/en/api/http/beta/organization/rate_limits#beta_organization_rate_limit_model_group) or [BetaOrganizationRateLimitBatchGroup](https://platform.claude.com/docs/en/api/http/beta/organization/rate_limits#beta_organization_rate_limit_batch_group) or [BetaOrganizationRateLimitTokenCountGroup](https://platform.claude.com/docs/en/api/http/beta/organization/rate_limits#beta_organization_rate_limit_token_count_group) or 3 more



The rate-limit group this entry's limits apply to. Its `type` equals `group_type`.

One of the following:



BetaOrganizationRateLimitModelGroup object{ type: "model_group", id, display_name }





type: "model_group"



Always `model_group`: a family of models.

defaultmodel_group

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

display_name: string



Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.



BetaOrganizationRateLimitBatchGroup object{ type: "batch", id }





type: "batch"



Always `batch`: the Message Batches API.

defaultbatch

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



BetaOrganizationRateLimitTokenCountGroup object{ type: "token_count", id }





type: "token_count"



Always `token_count`: the Token Count API.

defaulttoken_count

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



BetaOrganizationRateLimitFilesGroup object{ type: "files", id }





type: "files"



Always `files`: the Files API.

defaultfiles

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



BetaOrganizationRateLimitSkillsGroup object{ type: "skills", id }





type: "skills"



Always `skills`: the Skills API.

defaultskills

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



BetaOrganizationRateLimitWebSearchGroup object{ type: "web_search", id }





type: "web_search"



Always `web_search`: the Messages API web search tool.

defaultweb_search

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



limits: array of [BetaWorkspaceRateLimitValue](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits#beta_workspace_rate_limit_value) { type, org_limit, source, value }



The workspace's limiter values for this group. By default only the limiter types with a workspace-level override are listed. With `include_inherited` set to `true`, the limiter types the workspace inherits from the organization are listed too, each marked by `source`.

type: string



The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

org_limit: number or null



The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.



source: [BetaWorkspaceRateLimitWorkspaceSource](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits#beta_workspace_rate_limit_workspace_source) or [BetaWorkspaceRateLimitOrganizationSource](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits#beta_workspace_rate_limit_organization_source)



Where `value` comes from. `organization` values are listed only when `include_inherited` is `true`, and then `value` equals `org_limit`.

One of the following:



BetaWorkspaceRateLimitWorkspaceSource object{ type: "workspace" }





type: "workspace"



Always `workspace`: a workspace-level override is stored.

defaultworkspace



BetaWorkspaceRateLimitOrganizationSource object{ type: "organization" }





type: "organization"



Always `organization`: no workspace-level override is stored, so the organization's value applies.

defaultorganization

value: number



The workspace's value for this limiter type: the workspace-level override when `source.type` is `workspace`, otherwise the organization's value.

models: array of string or null



Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

rate_limit_id: string



The `id` of the organization's RateLimit entry this entry applies to.

workspace_id: string



ID of the Workspace this entry applies to.



group_type: "batch" or "files" or "model_group" or 3 more⁠Deprecated



Deprecated: use `group.type` instead. The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`. Always equal to `group.type`.

Use \`group.type\` instead. \`group_type\` is still returned and always equals \`group.type\`.

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

next_page: string or null



Opaque cursor for the next page of results, or `null` when no entries remain beyond this response.

List Workspace Rate Limits

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
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
