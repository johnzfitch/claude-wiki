---
title: "Get Activity Summaries - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:37:39Z"
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

Retrieve summaries




# Get Activity Summaries

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

Returns one entry per day in \[starting_date, ending_date). Data is typically available with a 1-day lag and may be revised by a few percent over the following days: when ending_date is omitted it defaults to the most recent available day + 1, so the last entry covers the most recent available day. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse 

starting_date: string



UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

[](#retrieve_summaries.starting_date)

ending_date: optional string



UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is typically available with a 1-day lag, so this can be at most today — which is also the default when omitted, making the last entry cover the most recent available day. Data may be revised by a few percent over the following days. The range may span at most 366 days.

[](#retrieve_summaries.ending_date)

filter: optional array of string



Filters as 'dimension

'. Only rbac_group_id is supported (e.g. filter\[\]=rbac_group_id:\<id\>); repeat the param to OR across groups. Scopes the whole day series to members of the matching group(s), re-aggregated from member-level activity — org-wide seat/invite fields and the adoption rates derived from them are null on scoped rows. rbac_group_id accepts the tagged id (rbac_group\_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each UTC day (time-of-usage attribution). At most 100 entries.

[](#retrieve_summaries.filter)

##### ReturnsExpand Collapse 

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

Get Activity Summaries



```python
curl https://api.anthropic.com/v1/organizations/analytics/summaries \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "summaries": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "ending_at",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "starting_at",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
    }
  ]
}
```

##### Returns Examples

Response 200



```python
{
  "summaries": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "ending_at",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "starting_at",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
