---
title: "Analytics - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:37:36Z"
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

API Keys

External Keys

Usage Report

Cost Report

Analytics


Get Activity Summaries

Usage

Cost

Users

Skills

Connectors

Chat Projects

Plugins

Artifacts

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

Analytics




# Analytics

##### [Get Activity Summaries](/docs/en/api/admin/analytics/retrieve_summaries)

GET/v1/organizations/analytics/summaries

##### ModelsExpand Collapse 



ActivitySummary object { summaries }



Response for GET /v1/organizations/analytics/summaries.



summaries: array of object { assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 26 more }



assigned_seat_count: number



Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

[](#activity_summary.summaries.items.assigned_seat_count)

cowork_daily_active_user_count: number



Number of users with Cowork activity on the requested day

[](#activity_summary.summaries.items.cowork_daily_active_user_count)

cowork_monthly_active_user_count: number



Number of users with Cowork activity in the 30-day rolling window

[](#activity_summary.summaries.items.cowork_monthly_active_user_count)

cowork_weekly_active_user_count: number



Number of users with Cowork activity in the 7-day rolling window

[](#activity_summary.summaries.items.cowork_weekly_active_user_count)

daily_active_user_count: number



Number of users with token consumption on the requested day

[](#activity_summary.summaries.items.daily_active_user_count)

daily_adoption_rate: number



Percentage of assigned seats with activity on the requested day (DAU / assigned_seat_count \* 100). Null when the response is scoped to an RBAC group.

[](#activity_summary.summaries.items.daily_adoption_rate)

ending_at: string



End time in UTC of aggregation period (e.g. 2026-01-16T00:00

)

[](#activity_summary.summaries.items.ending_at)

monthly_active_user_count: number



Number of users with token consumption in the 30-day rolling window

[](#activity_summary.summaries.items.monthly_active_user_count)

monthly_adoption_rate: number



Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned_seat_count \* 100). Null when the response is scoped to an RBAC group.

[](#activity_summary.summaries.items.monthly_adoption_rate)

pending_invite_count: number



Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

[](#activity_summary.summaries.items.pending_invite_count)

starting_at: string



Start time in UTC of aggregation period (e.g. 2026-01-15T00:00

)

[](#activity_summary.summaries.items.starting_at)

weekly_active_user_count: number



Number of users with token consumption in the 7-day rolling window

[](#activity_summary.summaries.items.weekly_active_user_count)

weekly_adoption_rate: number



Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned_seat_count \* 100). Null when the response is scoped to an RBAC group.

[](#activity_summary.summaries.items.weekly_adoption_rate)

chat_daily_active_user_count: optional number



Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.chat_daily_active_user_count)

chat_monthly_active_user_count: optional number



Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.chat_monthly_active_user_count)

chat_weekly_active_user_count: optional number



Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.chat_weekly_active_user_count)

claude_code_daily_active_user_count: optional number



Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.claude_code_daily_active_user_count)

claude_code_monthly_active_user_count: optional number



Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.claude_code_monthly_active_user_count)

claude_code_weekly_active_user_count: optional number



Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.claude_code_weekly_active_user_count)

claude_design_daily_active_user_count: optional number



Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.claude_design_daily_active_user_count)

claude_design_monthly_active_user_count: optional number



Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.claude_design_monthly_active_user_count)

claude_design_weekly_active_user_count: optional number



Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.claude_design_weekly_active_user_count)

office_agent_daily_active_user_count: optional number



Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.office_agent_daily_active_user_count)

office_agent_monthly_active_user_count: optional number



Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.office_agent_monthly_active_user_count)

office_agent_weekly_active_user_count: optional number



Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.office_agent_weekly_active_user_count)

science_daily_active_user_count: optional number



Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.science_daily_active_user_count)

science_entitled_user_count: optional number



Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.science_entitled_user_count)

science_monthly_active_user_count: optional number



Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.science_monthly_active_user_count)

science_weekly_active_user_count: optional number



Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

[](#activity_summary.summaries.items.science_weekly_active_user_count)

[](#activity_summary.summaries)

[](#activity_summary)



AnalyticsUser object { id, email_address }



User identifier.

id: string



Tagged user identifier (e.g. user\_...)

[](#analytics_user.id)

email_address: string



Email address of the user

[](#analytics_user.email_address)

[](#analytics_user)



AnalyticsUserActor object { user_id, deleted, email, 2 more }



user_id: string



Tagged user ID.

[](#analytics_user_actor.user_id)

deleted: optional boolean



True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

[](#analytics_user_actor.deleted)

email: optional string



The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

[](#analytics_user_actor.email)

name: optional string



The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

[](#analytics_user_actor.name)

type: optional "user_actor"



[](#analytics_user_actor.type)

[](#analytics_user_actor)



ConnectorOfficeProductMetrics object { distinct_session_connector_used_count }



Office Agent activity metrics for a single connector on a given day within one Office product.

distinct_session_connector_used_count: number



Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#connector_office_product_metrics.distinct_session_connector_used_count)

[](#connector_office_product_metrics)



OfficeProductMetrics object { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }



Office Agent activity metrics for a single user on a given day within one Office product.

connectors_used_count: number



Number of MCP connector invocations

[](#office_product_metrics.connectors_used_count)

distinct_connectors_used_count: number



Number of distinct MCP connectors used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#office_product_metrics.distinct_connectors_used_count)

distinct_session_count: number



Number of distinct Office Agent sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#office_product_metrics.distinct_session_count)

distinct_skills_used_count: number



Number of distinct skills used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#office_product_metrics.distinct_skills_used_count)

message_count: number



Number of messages sent

[](#office_product_metrics.message_count)

skills_used_count: number



Number of skill invocations

[](#office_product_metrics.skills_used_count)

[](#office_product_metrics)



SkillOfficeProductMetrics object { distinct_session_skill_used_count }



Office Agent activity metrics for a single skill on a given day within one Office product.

distinct_session_skill_used_count: number



Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#skill_office_product_metrics.distinct_session_skill_used_count)

[](#skill_office_product_metrics)



ToolActionCounts object { accepted_count, rejected_count }



Accepted/rejected counts for a single Claude Code tool type.

accepted_count: number



Number of tool proposals accepted

[](#tool_action_counts.accepted_count)

rejected_count: number



Number of tool proposals rejected

[](#tool_action_counts.rejected_count)

[](#tool_action_counts)

#### AnalyticsUsage

##### [Get Token Usage Over Time](/docs/en/api/admin/analytics/usage/list)

GET/v1/organizations/analytics/usage_report

##### [Get Per-User Token Usage](/docs/en/api/admin/analytics/usage/list_by_user)

GET/v1/organizations/analytics/user_usage_report

#### AnalyticsCost

##### [Get Cost Over Time](/docs/en/api/admin/analytics/cost/list)

GET/v1/organizations/analytics/cost_report

##### [Get Per-User Cost](/docs/en/api/admin/analytics/cost/list_by_user)

GET/v1/organizations/analytics/user_cost_report

#### AnalyticsUsers

##### [List User Activity](/docs/en/api/admin/analytics/users/list)

GET/v1/organizations/analytics/users

#### AnalyticsSkills

##### [Get Skill Usage](/docs/en/api/admin/analytics/skills/list)

GET/v1/organizations/analytics/skills

#### AnalyticsConnectors

##### [Get Connector Usage](/docs/en/api/admin/analytics/connectors/list)

GET/v1/organizations/analytics/connectors

#### AnalyticsChat Projects

##### [Get Chat Project Usage](/docs/en/api/admin/analytics/chat_projects/list)

GET/v1/organizations/analytics/apps/chat/projects

#### AnalyticsPlugins

##### [Get Plugin Usage](/docs/en/api/admin/analytics/plugins/list)

GET/v1/organizations/analytics/plugins

#### AnalyticsArtifacts

##### [Get Artifact Activity](/docs/en/api/admin/analytics/artifacts/list)

GET/v1/organizations/analytics/artifacts
