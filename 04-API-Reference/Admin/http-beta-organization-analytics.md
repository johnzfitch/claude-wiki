---
title: "Analytics - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/organization/analytics"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-27T06:27:14Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Forganization%2Fanalytics)

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

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics


Get Activity Summaries

Usage

Cost

Users

Skills

Connectors

Chat Projects

Plugins

Artifacts

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

# Analytics

##### [Get Activity Summaries](http-beta-organization-analytics-retrieve-summaries.md)

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

##### Models



BetaActivitySummary object{ summaries }



Response for GET /v1/organizations/analytics/summaries.



BetaAnalyticsUser object{ type: "user", id, email_address }



A user in the organization, identified by tagged id and email address.



type: "user"



Object type. Always `user`.

defaultuser

id: string



Tagged user identifier (e.g. `user_...`)

email_address: string



Email address of the user



BetaAnalyticsUserActor object{ type: "user_actor", deleted, email, 2 more }



type: "user_actor"



Actor type. Always `"user_actor"`.

deleted: boolean



True when the account has been deleted, or when the user is no longer a member of the organization or its associated organizations (for example, their membership was removed or they were deprovisioned via your identity provider). `email` stays populated for removed users and is null when the account has been deleted. `name` follows the rules described on that field. The `user_id` is still populated for reconciliation.

email: string or null



The user's email address, including for users who are no longer members of the organization or its associated organizations. Null when the account has been deleted (check `deleted`) and for system-minted service accounts, which have no person's mailbox behind them (check `name`).

name: string or null



The user's full name. Null when the user has not set a name. Returns `"Deleted User"` when the account itself has been deleted, or when the user is no longer a member of the organization or its associated organizations and the organization has chosen to hide the names of removed users. Otherwise, the name stays populated for removed users. Rows for system-minted service accounts render the service name (for example, `"Claude Security"` for usage by Anthropic's security-patching service) or null.

user_id: string



Tagged user ID.



BetaConnectorOfficeProductMetrics object{ distinct_session_connector_used_count }



Office Agent activity metrics for a single connector on a given day within one Office product.

distinct_session_connector_used_count: number or null



Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaOfficeProductMetrics object{ connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }



Office Agent activity metrics for a single user on a given day within one Office product.

connectors_used_count: number



Number of MCP connector invocations

distinct_connectors_used_count: number or null



Number of distinct MCP connectors used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct_session_count: number or null



Number of distinct Office Agent sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct_skills_used_count: number or null



Number of distinct skills used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message_count: number



Number of messages sent

skills_used_count: number



Number of skill invocations



BetaSkillOfficeProductMetrics object{ distinct_session_skill_used_count }



Office Agent activity metrics for a single skill on a given day within one Office product.

distinct_session_skill_used_count: number or null



Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaToolActionCounts object{ accepted_count, rejected_count }



Accepted/rejected counts for a single Claude Code tool type.

accepted_count: number



Number of tool proposals accepted

rejected_count: number



Number of tool proposals rejected

#### Analytics[Usage](http-beta-organization-analytics-usage.md)

##### [Get Token Usage Over Time](http-beta-organization-analytics-usage-list.md)

GET/v1/organizations/analytics/usage_report

Get token usage over time across a date range.

##### [Get Per-User Token Usage](beta-organization-analytics-usage-list-by-user.md)

GET/v1/organizations/analytics/user_usage_report

Get per-user token usage across a date range.

#### Analytics[Cost](http-beta-organization-analytics-cost.md)

##### [Get Cost Over Time](http-beta-organization-analytics-cost-list.md)

GET/v1/organizations/analytics/cost_report

Get cost in USD over time across a date range.

##### [Get Per-User Cost](beta-organization-analytics-cost-list-by-user.md)

GET/v1/organizations/analytics/user_cost_report

Get per-user cost in USD across a date range.

#### Analytics[Users](http-beta-organization-analytics-users.md)

##### [List User Activity](http-beta-organization-analytics-users-list.md)

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

#### Analytics[Skills](beta-organization-analytics-skills.md)

##### [Get Skill Usage](http-beta-organization-analytics-skills-list.md)

GET/v1/organizations/analytics/skills

Get per-skill usage for a given day, with cursor-based pagination.

#### Analytics[Connectors](beta-organization-analytics-connectors.md)

##### [Get Connector Usage](http-beta-organization-analytics-connectors-list.md)

GET/v1/organizations/analytics/connectors

Get per-connector usage for a given day, with cursor-based pagination.

#### Analytics[Chat Projects](http-beta-organization-analytics-chat-projects.md)

##### [Get Chat Project Usage](http-beta-organization-analytics-chat-projects-list.md)

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

#### Analytics[Plugins](http-beta-organization-analytics-plugins.md)

##### [Get Plugin Usage](http-beta-organization-analytics-plugins-list.md)

GET/v1/organizations/analytics/plugins

Get per-plugin install + invocation usage for a given day, with pagination.

#### Analytics[Artifacts](beta-organization-analytics-artifacts.md)

##### [Get Artifact Activity](http-beta-organization-analytics-artifacts-list.md)

GET/v1/organizations/analytics/artifacts

Get artifact-creation activity for a given day, broken out by MIME type.
