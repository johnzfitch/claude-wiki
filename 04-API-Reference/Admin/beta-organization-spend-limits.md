---
title: "Spend Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/spend_limits"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-20T06:37:17Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fspend_limits)

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

# Spend Limits

Copy page



cURL

##### [Set Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/set)

POST/v1/organizations/spend_limits

Set a spend limit.

##### [Get Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/retrieve)

GET/v1/organizations/spend_limits/{spend_limit_id}

Retrieve a spend limit by ID.

##### [Delete Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/delete)

DELETE/v1/organizations/spend_limits/{spend_limit_id}

Delete a spend limit.

##### [List Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/list)

GET/v1/organizations/spend_limits

List the organization's spend limits.

##### Models



BetaSpendLimit object{ type: "spend_limit", id, amount, 6 more }



A configured spend limit: a cap on metered spend for one scope and period.



BetaSpendLimitOrganizationScope object{ type: "organization" }





type: "organization"



defaultorganization

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

BetaSpendLimitPeriod = "daily" or "monthly" or "weekly"



One of the following:

"daily"



"monthly"



"weekly"

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

BetaSpendLimitScopedAPIKeyActor object{ type: "scoped_api_key_actor", scoped_api_key_id }



A scoped Admin API key acting on behalf of the organization.



type: "scoped_api_key_actor"



defaultscoped_api_key_actor

scoped_api_key_id: string



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

BetaSpendLimitUsageTierScope object{ type: "usage_tier" }



Scope of the monthly spend cap Anthropic sets for a Claude Console organization from its usage tier, or a higher cap Anthropic granted the organization. Read-only; its `created_at` and `updated_at` are the organization's creation time, so `amount` can change while `updated_at` stays the same.



type: "usage_tier"



Scope type. Always `usage_tier` for this scope.

defaultusage_tier



BetaSpendLimitUserActor object{ type: "user_actor", deleted, email_address, 2 more }



A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.



type: "user_actor"



Actor type. Always `user_actor`.

defaultuser_actor



deleted: boolean



True only when the underlying account has been deleted.

defaultfalse

email_address: string or null



The user's email address. Null when the account is unavailable or has been deleted.

name: string or null



The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

user_id: string



Tagged ID of the user.

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

BetaSpendSummary object{ actor, amount, currency, 5 more }



Per-member effective-limit report row (`GET /spend_limits/effective`).



SpendLimitDeleteResponse object{ type: "spend_limit_deleted", id }





type: "spend_limit_deleted"



defaultspend_limit_deleted

id: string



#### Spend Limits[Effective](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/effective)

##### [List Effective Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/effective/list)

GET/v1/organizations/spend_limits/effective

List each member's effective spend limit and period-to-date spend.

#### Spend Limits[Increase Requests](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests)

##### [List Spend Limit Increase Requests](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

List spend limit increase requests, most recent first.

##### [Get Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

Retrieve a spend limit increase request.

##### [Approve Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

Approve a pending spend limit increase request.

##### [Deny Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny

Deny a pending spend limit increase request.
