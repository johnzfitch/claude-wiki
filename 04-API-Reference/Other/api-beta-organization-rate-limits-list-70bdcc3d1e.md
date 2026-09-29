---
title: "List Organization Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/rate_limits/list"
category: "04-API-Reference/Other"
fetched_at: "2026-09-28T06:33:21Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Frate_limits%2Flist)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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


List Organization Rate Limits

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

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)
3.  [Organization](/docs/en/api/http/beta/organization)
4.  [Rate Limits](/docs/en/api/http/beta/organization/rate_limits)

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

minimum1

maximum1000

model: optional string



Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

page: optional string



Opaque cursor from a previous response's `next_page`.

##### Returns



data: array of [BetaOrganizationRateLimit](/docs/en/api/http/beta/organization/rate_limits#beta_organization_rate_limit) { type: "rate_limit", id, group, 3 more }



Rate-limit entries for the organization, one per group.



type: "rate_limit"



Object type. Always `rate_limit` for organization rate-limit entries.

defaultrate_limit

id: string



Identifier of this rate-limit entry. It is stable within the organization and differs between organizations; the group's own identifier is `group.id`.



group: [BetaOrganizationRateLimitModelGroup](/docs/en/api/http/beta/organization/rate_limits#beta_organization_rate_limit_model_group) or [BetaOrganizationRateLimitBatchGroup](/docs/en/api/http/beta/organization/rate_limits#beta_organization_rate_limit_batch_group) or [BetaOrganizationRateLimitTokenCountGroup](/docs/en/api/http/beta/organization/rate_limits#beta_organization_rate_limit_token_count_group) or 3 more

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

limits: array of [BetaOrganizationRateLimitValue](/docs/en/api/http/beta/organization/rate_limits#beta_organization_rate_limit_value) { type, value }

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

List Organization Rate Limits

cURL



```python
curl https://api.anthropic.com/v1/organizations/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "group": {
        "id": "id",
        "display_name": "display_name",
        "type": "model_group"
      },
      "group_type": "batch",
      "limits": [
        {
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "rate_limit"
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
      "id": "id",
      "group": {
        "id": "id",
        "display_name": "display_name",
