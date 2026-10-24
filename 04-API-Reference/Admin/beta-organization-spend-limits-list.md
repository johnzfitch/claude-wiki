---
title: "List Spend Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/spend_limits/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-18T06:26:51Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fspend_limits%2Flist)

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


Organization


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

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits


Set Spend Limit


Get Spend Limit


Delete Spend Limit


List Spend Limits

Effective

Increase Requests

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


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
4.  [Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits)

# List Spend Limits

Copy page



cURL

GET/v1/organizations/spend_limits

List the organization's spend limits.

Limits are grouped by scope type, in the order `organization`, `seat_tier`, `rbac_group`, `organization_service`, `user`; within a type they come in a fixed order that is not creation order. Supported for Claude Enterprise organizations only, not for Claude Console organizations.

##### Query parameters



limit: optional number



Maximum number of limits per page. Defaults to `20`.

default20

minimum1

maximum1000

page: optional string



Opaque cursor from a previous response's `next_page` field.



scope_type: optional array of "organization" or "organization_service" or "rbac_group" or 3 more



Return only limits with these scope types. Omit for all.

maxItems100

One of the following:

"organization"



"organization_service"



"rbac_group"



"seat_tier"



"user"



"workspace"



##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).



"anthropic-beta": optional array of [AnthropicBeta](../Endpoints/platform-claude-com-http-beta.md#anthropic_beta)



This endpoint is in beta: requests must send `spend-limit-reads-2026-09-26` in this header.

One of the following:

string



"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"cache-diagnosis-2026-04-07"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"ce-user-management-2026-07-13"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"



"ce-plugins-2026-09-01"



"spend-limit-reads-2026-09-26"



"telemetry-destinations-2026-08-11"



##### Returns



data: array of [BetaSpendLimit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit) { type: "spend_limit", id, amount, 6 more }





type: "spend_limit"



Object type. Always `spend_limit`.

defaultspend_limit

id: string



Unique tagged ID of the spend limit (`spl_...`).

amount: string or null



Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is \$500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.



created_at: string



RFC 3339 datetime at which the spend limit was created.

formatdate-time

currency: string



ISO 4217 code of the organization's billing currency; the unit for `amount`.

is_enabled: boolean



Read-only. `false` when extra usage is switched off for this organization (`organization` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.



period: [BetaSpendLimitPeriod](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit_period)



Length of the window the limit resets over. `amount` caps spend within each period.

One of the following:

"daily"



"monthly"



"weekly"





scope: [BetaSpendLimitUserScope](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit_user_scope) or [BetaSpendLimitSeatTierScope](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit_seat_tier_scope) or [BetaSpendLimitRBACGroupScope](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit_rbac_group_scope) or 4 more



What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

One of the following:



BetaSpendLimitUserScope object{ type: "user", user_id }



Scope selecting a single member of the organization.



type: "user"



Scope type. Always `user` for this scope.

defaultuser

user_id: string



Tagged ID of the member the spend limit applies to.



BetaSpendLimitSeatTierScope object{ type: "seat_tier", seat_tier }





type: "seat_tier"



defaultseat_tier

seat_tier: string





BetaSpendLimitRBACGroupScope object{ type: "rbac_group", rbac_group_id }





type: "rbac_group"



defaultrbac_group

rbac_group_id: string





BetaSpendLimitOrganizationServiceScope object{ type: "organization_service", service }





type: "organization_service"



defaultorganization_service

service: string





BetaSpendLimitOrganizationScope object{ type: "organization" }





type: "organization"



defaultorganization



BetaSpendLimitWorkspaceScope object{ type: "workspace", workspace_id }



Scope selecting one workspace of a Claude Console organization.



type: "workspace"



Scope type. Always `workspace` for this scope.

defaultworkspace

workspace_id: string



Tagged ID of the workspace the spend limit applies to.



BetaSpendLimitUsageTierScope object{ type: "usage_tier" }



Scope of the monthly spend cap Anthropic sets for a Claude Console organization from its usage tier, or a higher cap Anthropic granted the organization. Read-only; its `created_at` and `updated_at` are the organization's creation time, so `amount` can change while `updated_at` stays the same.



type: "usage_tier"



Scope type. Always `usage_tier` for this scope.

defaultusage_tier



updated_at: string



RFC 3339 datetime at which the spend limit was last modified.

formatdate-time

next_page: string or null



List Spend Limits

cURL



```python
curl https://api.anthropic.com/v1/organizations/spend_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: spend-limit-reads-2026-09-26' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "amount": "50000",
      "created_at": "2019-12-27T18:11:19.117Z",
      "currency": "USD",
      "is_enabled": true,
      "period": "daily",
      "scope": {
        "type": "user",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "type": "spend_limit",
      "updated_at": "2019-12-27T18:11:19.117Z"
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
      "amount": "50000",
      "created_at": "2019-12-27T18:11:19.117Z",
      "currency": "USD",
      "is_enabled": true,
      "period": "daily",
      "scope": {
        "type": "user",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "type": "spend_limit",
      "updated_at": "2019-12-27T18:11:19.117Z"
