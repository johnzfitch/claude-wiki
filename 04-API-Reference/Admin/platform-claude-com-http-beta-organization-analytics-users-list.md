---
title: "List User Activity - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/organization/analytics/users/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-04T08:33:13Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Forganization%2Fanalytics%2Fusers%2Flist)

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

MCP Tunnels

Analytics

Summaries

Users


List User Activity

Apps

Connectors

Plugins

Skills

Artifacts

Usage Report

User Usage Report

Cost Report

User Cost Report

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces


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

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Analytics](platform-claude-com-http-beta-organization-analytics.md)
5.  [Users](platform-claude-com-http-beta-organization-analytics-users.md)

# List User Activity

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

Returns activity metrics for each user in the organization, sorted by email address. Use `group_by[]` for per-RBAC-group aggregates, or `filter[]` to scope results to specific members, groups, or a chat project. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.

##### Query parameters



date: optional string



UTC date in YYYY-MM-DD format. The day to get user activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

formatdate



ending_date: optional string



UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

formatdate



filter: optional array of string



Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `project_id`, `rbac_group_id`, `user_id`. Value forms: `project_id` takes a tagged project id (`claude_proj_...`) and scopes each member's row to their claude.ai chat activity within that project (it cannot be combined with `group_by[]` or an `rbac_group_id` filter); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

maxItems100



group_by: optional array of "rbac_group_id"



Dimensions to break results out by (e.g. `group_by[]=rbac_group_id`). Supported on this endpoint: `rbac_group_id`. Rows are already per-member, so the one supported grouping aggregates them per RBAC group instead. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

maxItems100



limit: optional number



Number of results per page (1-1000, default 100).

minimum1

maximum1000



order: optional "asc" or "desc"



Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

One of the following:

"asc"



"desc"



order_by: optional string



Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

page: optional string



Opaque cursor from a previous response's `next_page` field.



starting_date: optional string



UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

formatdate

##### Returns



data: array of [BetaAnalyticsUserActivity](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_user_activity) { chat_metrics, claude_code_metrics, cowork_metrics, 9 more }





chat_metrics: [BetaAnalyticsChatMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_chat_metrics) { connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }



Claude.ai activity metrics for a single user on a given day.



claude_code_metrics: [BetaAnalyticsClaudeCodeMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_claude_code_metrics) { core_metrics, tool_actions }



Claude Code activity metrics for a single user on a given day.



cowork_metrics: [BetaAnalyticsCoworkMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_cowork_metrics) { action_count, artifacts_created_count, connectors_used_count, 14 more }



Cowork activity metrics for a single user on a given day.



design_metrics: [BetaAnalyticsDesignMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_design_metrics) { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count }



Claude Design activity metrics for a single user on a given day.

distinct_projects_created_count: number



Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

distinct_projects_used_count: number or null



Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct_session_count: number or null



Number of distinct Claude Design sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message_count: number



Number of messages sent in Claude Design sessions



office_metrics: [BetaAnalyticsOfficeMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_office_metrics) { excel, outlook, powerpoint, word }



Office Agent activity metrics for a single user on a given day, broken out by Office product.



science_metrics: [BetaAnalyticsScienceMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_science_metrics) { delegation_count, distinct_session_count, message_count, 2 more }



Claude Science activity metrics for a single user on a given day.

delegation_count: number



Number of delegations (handoffs to a specialized agent) in Claude Science sessions

distinct_session_count: number or null



Number of distinct Claude Science sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message_count: number



Number of messages sent in Claude Science sessions

remote_compute_job_count: number



Number of remote compute jobs launched from Claude Science sessions

skills_used_count: number



Total number of skill invocations in Claude Science sessions

web_search_count: number



Number of web searches performed

distinct_user_count: optional number or null



Number of distinct active users represented by this row. Only set for grouped rollups (`group_by[]`); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.



last_activity_date: optional string or null



Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested `date` in single-day mode, and to the latest active day from `starting_date` (inclusive) to `ending_date` (exclusive) in date-range rollup mode — never a day earlier than the window start. On filtered requests (`filter[]`) only days matching the filter count: with `filter[]=rbac_group_id:{id}` it is the last day the user was active while a member of that group, consistent with the row's other metrics. On grouped (`group_by[]`) rows it is the latest day any member of the group was active (the requested `date` in single-day mode). Omitted from the response while last-activity reporting is not enabled for this organization.

formatdate

rbac_group_id: optional string or null



Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

rbac_group_name: optional string or null



Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.



user: optional [BetaAnalyticsUser](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_user) { type: "user", id, email_address } or null



The user this row describes. Null on rows aggregated across users.

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

next_page: string or null



Opaque cursor for the next page, or null if no more results

List User Activity

cURL



```python
curl https://api.anthropic.com/v1/organizations/analytics/users \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "chat_metrics": {
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      },
      "claude_code_metrics": {
        "core_metrics": {
          "artifacts_created_count": 0,
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          },
          "pull_request_count": 0
        },
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          }
        }
      },
      "cowork_metrics": {
        "action_count": 0,
        "artifacts_created_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "skills_used_count": 0,
        "distinct_plugins_used_count": 0,
        "edit_tool_count": 0,
        "file_edit_count": 0,
        "multi_edit_tool_count": 0,
        "notebook_edit_tool_count": 0,
        "plugins_used_count": 0,
        "sessions_with_file_edits_count": 0,
        "write_tool_count": 0
      },
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      },
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        }
      },
      "science_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
      "web_search_count": 0,
      "distinct_user_count": 0,
      "last_activity_date": "2019-12-27",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      }
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
      "chat_metrics": {
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      },
      "claude_code_metrics": {
        "core_metrics": {
          "artifacts_created_count": 0,
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          },
          "pull_request_count": 0
        },
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          }
        }
      },
      "cowork_metrics": {
        "action_count": 0,
        "artifacts_created_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "skills_used_count": 0,
        "distinct_plugins_used_count": 0,
        "edit_tool_count": 0,
        "file_edit_count": 0,
        "multi_edit_tool_count": 0,
        "notebook_edit_tool_count": 0,
        "plugins_used_count": 0,
        "sessions_with_file_edits_count": 0,
        "write_tool_count": 0
      },
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      },
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        }
      },
      "science_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
      "web_search_count": 0,
      "distinct_user_count": 0,
      "last_activity_date": "2019-12-27",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user": {
        "id": "id",
        "email_address": "email_address",
