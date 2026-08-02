---
title: "List User Activity - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/users/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:40:01Z"
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


List User Activity

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

List




# List User Activity

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

Returns activity metrics for each user in the organization, sorted by email address. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse 

date: optional string



UTC date in YYYY-MM-DD format. The day to get user activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

[](#list.date)

ending_date: optional string



UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

[](#list.ending_date)

filter: optional array of string



Filters as 'dimension

', e.g. filter\[\]=rbac_group_id:\<id\>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group\_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

[](#list.filter)

group_by: optional array of string



Dimensions to break results out by, e.g. group_by\[\]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

[](#list.group_by)

limit: optional number



Number of results per page (1-1000, default 100).

[](#list.limit)



order: optional "asc" or "desc"



Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

One of the following:

"asc"



[](#list.order%5B0%5D)

"desc"



[](#list.order%5B1%5D)

[](#list.order)

order_by: optional string



Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

[](#list.order_by)

page: optional string



Opaque cursor from a previous response's next_page field.

[](#list.page)

starting_date: optional string



UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

[](#list.starting_date)

##### ReturnsExpand Collapse 



UserActivity object { data, next_page }



Response for GET /v1/organizations/analytics/users.



data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 9 more }





chat_metrics: object { connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }



Claude.ai activity metrics for a single user on a given day.

connectors_used_count: number



Number of MCP connector invocations.

[](#user_activity.data.items.chat_metrics.connectors_used_count)

distinct_artifacts_created_count: number



Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

[](#user_activity.data.items.chat_metrics.distinct_artifacts_created_count)

distinct_connectors_used_count: number



Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.chat_metrics.distinct_connectors_used_count)

distinct_conversation_count: number



Number of distinct conversations the user participated in. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.chat_metrics.distinct_conversation_count)

distinct_files_uploaded_count: number



Number of distinct files uploaded. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.chat_metrics.distinct_files_uploaded_count)

distinct_projects_created_count: number



Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

[](#user_activity.data.items.chat_metrics.distinct_projects_created_count)

distinct_projects_used_count: number



Number of distinct projects used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.chat_metrics.distinct_projects_used_count)

distinct_shared_artifacts_viewed_count: number



Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.chat_metrics.distinct_shared_artifacts_viewed_count)

distinct_skills_used_count: number



Number of distinct skills used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.chat_metrics.distinct_skills_used_count)

message_count: number



Number of messages sent

[](#user_activity.data.items.chat_metrics.message_count)

shared_conversations_viewed_count: number



Number of times the user opened a shared conversation in a project

[](#user_activity.data.items.chat_metrics.shared_conversations_viewed_count)

thinking_message_count: number



Number of messages that used extended thinking

[](#user_activity.data.items.chat_metrics.thinking_message_count)

[](#user_activity.data.items.chat_metrics)



claude_code_metrics: object { core_metrics, tool_actions }



Claude Code activity metrics for a single user on a given day.



core_metrics: object { commit_count, distinct_session_count, lines_of_code, pull_request_count }



Core Claude Code activity metrics for a single user on a given day.

commit_count: number



Number of commits made via Claude Code

[](#user_activity.data.items.claude_code_metrics.core_metrics.commit_count)

distinct_session_count: number



Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

[](#user_activity.data.items.claude_code_metrics.core_metrics.distinct_session_count)



lines_of_code: object { added_count, removed_count }



Lines of code added and removed via Claude Code.

added_count: number



Lines of code added

[](#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code.added_count)

removed_count: number



Lines of code removed

[](#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code.removed_count)

[](#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code)

pull_request_count: number



Number of pull requests created via Claude Code

[](#user_activity.data.items.claude_code_metrics.core_metrics.pull_request_count)

[](#user_activity.data.items.claude_code_metrics.core_metrics)



tool_actions: object { edit_tool, multi_edit_tool, notebook_edit_tool, write_tool }



Per-tool accepted/rejected counts for Claude Code file modification tools.



edit_tool: [ToolActionCounts](/docs/en/api/admin/analytics#tool_action_counts) { accepted_count, rejected_count }



Accepted/rejected counts for a single Claude Code tool type.

accepted_count: number



Number of tool proposals accepted

[](#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool%20%2B%20(resource)%20admin.analytics.accepted_count)

rejected_count: number



Number of tool proposals rejected

[](#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool%20%2B%20(resource)%20admin.analytics.rejected_count)

[](#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool)



multi_edit_tool: [ToolActionCounts](/docs/en/api/admin/analytics#tool_action_counts) { accepted_count, rejected_count }



Accepted/rejected counts for a single Claude Code tool type.

accepted_count: number



Number of tool proposals accepted

[](#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool%20%2B%20(resource)%20admin.analytics.accepted_count)

rejected_count: number



Number of tool proposals rejected

[](#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool%20%2B%20(resource)%20admin.analytics.rejected_count)

[](#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool)



notebook_edit_tool: [ToolActionCounts](/docs/en/api/admin/analytics#tool_action_counts) { accepted_count, rejected_count }



Accepted/rejected counts for a single Claude Code tool type.

accepted_count: number



Number of tool proposals accepted

[](#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool%20%2B%20(resource)%20admin.analytics.accepted_count)

rejected_count: number



Number of tool proposals rejected

[](#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool%20%2B%20(resource)%20admin.analytics.rejected_count)

[](#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool)



write_tool: [ToolActionCounts](/docs/en/api/admin/analytics#tool_action_counts) { accepted_count, rejected_count }



Accepted/rejected counts for a single Claude Code tool type.

accepted_count: number



Number of tool proposals accepted

[](#user_activity.data.items.claude_code_metrics.tool_actions.write_tool%20%2B%20(resource)%20admin.analytics.accepted_count)

rejected_count: number



Number of tool proposals rejected

[](#user_activity.data.items.claude_code_metrics.tool_actions.write_tool%20%2B%20(resource)%20admin.analytics.rejected_count)

[](#user_activity.data.items.claude_code_metrics.tool_actions.write_tool)

[](#user_activity.data.items.claude_code_metrics.tool_actions)

[](#user_activity.data.items.claude_code_metrics)



cowork_metrics: object { action_count, connectors_used_count, dispatch_turn_count, 13 more }



Cowork activity metrics for a single user on a given day.

action_count: number



Number of tool actions completed in Cowork sessions

[](#user_activity.data.items.cowork_metrics.action_count)

connectors_used_count: number



Total number of connector invocations in Cowork sessions

[](#user_activity.data.items.cowork_metrics.connectors_used_count)

dispatch_turn_count: number



Number of Dispatch (background agent) turns completed

[](#user_activity.data.items.cowork_metrics.dispatch_turn_count)

distinct_connectors_used_count: number



Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.cowork_metrics.distinct_connectors_used_count)

distinct_session_count: number



Number of distinct Cowork sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.cowork_metrics.distinct_session_count)

distinct_skills_used_count: number



Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.cowork_metrics.distinct_skills_used_count)

message_count: number



Number of messages sent in Cowork sessions

[](#user_activity.data.items.cowork_metrics.message_count)

skills_used_count: number



Total number of skill invocations in Cowork sessions

[](#user_activity.data.items.cowork_metrics.skills_used_count)

distinct_plugins_used_count: optional number



Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.cowork_metrics.distinct_plugins_used_count)

edit_tool_count: optional number



Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

[](#user_activity.data.items.cowork_metrics.edit_tool_count)

file_edit_count: optional number



Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

[](#user_activity.data.items.cowork_metrics.file_edit_count)

multi_edit_tool_count: optional number



Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

[](#user_activity.data.items.cowork_metrics.multi_edit_tool_count)

notebook_edit_tool_count: optional number



Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

[](#user_activity.data.items.cowork_metrics.notebook_edit_tool_count)

plugins_used_count: optional number



Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

[](#user_activity.data.items.cowork_metrics.plugins_used_count)

sessions_with_file_edits_count: optional number



Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.cowork_metrics.sessions_with_file_edits_count)

write_tool_count: optional number



Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

[](#user_activity.data.items.cowork_metrics.write_tool_count)

[](#user_activity.data.items.cowork_metrics)



design_metrics: object { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count }



Claude Design activity metrics for a single user on a given day.

distinct_projects_created_count: number



Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

[](#user_activity.data.items.design_metrics.distinct_projects_created_count)

distinct_projects_used_count: number



Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.design_metrics.distinct_projects_used_count)

distinct_session_count: number



Number of distinct Claude Design sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.design_metrics.distinct_session_count)

message_count: number



Number of messages sent in Claude Design sessions

[](#user_activity.data.items.design_metrics.message_count)

[](#user_activity.data.items.design_metrics)



office_metrics: object { excel, outlook, powerpoint, word }



Office Agent activity metrics for a single user on a given day, broken out by Office product.



excel: [OfficeProductMetrics](/docs/en/api/admin/analytics#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }



Office Agent activity metrics for a single user on a given day within one Office product.

connectors_used_count: number



Number of MCP connector invocations

[](#user_activity.data.items.office_metrics.excel%20%2B%20(resource)%20admin.analytics.connectors_used_count)

distinct_connectors_used_count: number



Number of distinct MCP connectors used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.excel%20%2B%20(resource)%20admin.analytics.distinct_connectors_used_count)

distinct_session_count: number



Number of distinct Office Agent sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.excel%20%2B%20(resource)%20admin.analytics.distinct_session_count)

distinct_skills_used_count: number



Number of distinct skills used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.excel%20%2B%20(resource)%20admin.analytics.distinct_skills_used_count)

message_count: number



Number of messages sent

[](#user_activity.data.items.office_metrics.excel%20%2B%20(resource)%20admin.analytics.message_count)

skills_used_count: number



Number of skill invocations

[](#user_activity.data.items.office_metrics.excel%20%2B%20(resource)%20admin.analytics.skills_used_count)

[](#user_activity.data.items.office_metrics.excel)



outlook: [OfficeProductMetrics](/docs/en/api/admin/analytics#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }



Office Agent activity metrics for a single user on a given day within one Office product.

connectors_used_count: number



Number of MCP connector invocations

[](#user_activity.data.items.office_metrics.outlook%20%2B%20(resource)%20admin.analytics.connectors_used_count)

distinct_connectors_used_count: number



Number of distinct MCP connectors used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.outlook%20%2B%20(resource)%20admin.analytics.distinct_connectors_used_count)

distinct_session_count: number



Number of distinct Office Agent sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.outlook%20%2B%20(resource)%20admin.analytics.distinct_session_count)

distinct_skills_used_count: number



Number of distinct skills used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.outlook%20%2B%20(resource)%20admin.analytics.distinct_skills_used_count)

message_count: number



Number of messages sent

[](#user_activity.data.items.office_metrics.outlook%20%2B%20(resource)%20admin.analytics.message_count)

skills_used_count: number



Number of skill invocations

[](#user_activity.data.items.office_metrics.outlook%20%2B%20(resource)%20admin.analytics.skills_used_count)

[](#user_activity.data.items.office_metrics.outlook)



powerpoint: [OfficeProductMetrics](/docs/en/api/admin/analytics#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }



Office Agent activity metrics for a single user on a given day within one Office product.

connectors_used_count: number



Number of MCP connector invocations

[](#user_activity.data.items.office_metrics.powerpoint%20%2B%20(resource)%20admin.analytics.connectors_used_count)

distinct_connectors_used_count: number



Number of distinct MCP connectors used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.powerpoint%20%2B%20(resource)%20admin.analytics.distinct_connectors_used_count)

distinct_session_count: number



Number of distinct Office Agent sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.powerpoint%20%2B%20(resource)%20admin.analytics.distinct_session_count)

distinct_skills_used_count: number



Number of distinct skills used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.powerpoint%20%2B%20(resource)%20admin.analytics.distinct_skills_used_count)

message_count: number



Number of messages sent

[](#user_activity.data.items.office_metrics.powerpoint%20%2B%20(resource)%20admin.analytics.message_count)

skills_used_count: number



Number of skill invocations

[](#user_activity.data.items.office_metrics.powerpoint%20%2B%20(resource)%20admin.analytics.skills_used_count)

[](#user_activity.data.items.office_metrics.powerpoint)



word: [OfficeProductMetrics](/docs/en/api/admin/analytics#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }



Office Agent activity metrics for a single user on a given day within one Office product.

connectors_used_count: number



Number of MCP connector invocations

[](#user_activity.data.items.office_metrics.word%20%2B%20(resource)%20admin.analytics.connectors_used_count)

distinct_connectors_used_count: number



Number of distinct MCP connectors used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.word%20%2B%20(resource)%20admin.analytics.distinct_connectors_used_count)

distinct_session_count: number



Number of distinct Office Agent sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.word%20%2B%20(resource)%20admin.analytics.distinct_session_count)

distinct_skills_used_count: number



Number of distinct skills used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.office_metrics.word%20%2B%20(resource)%20admin.analytics.distinct_skills_used_count)

message_count: number



Number of messages sent

[](#user_activity.data.items.office_metrics.word%20%2B%20(resource)%20admin.analytics.message_count)

skills_used_count: number



Number of skill invocations

[](#user_activity.data.items.office_metrics.word%20%2B%20(resource)%20admin.analytics.skills_used_count)

[](#user_activity.data.items.office_metrics.word)

[](#user_activity.data.items.office_metrics)



science_metrics: object { delegation_count, distinct_session_count, message_count, 2 more }



Claude Science activity metrics for a single user on a given day.

delegation_count: number



Number of delegations (handoffs to a specialized agent) in Claude Science sessions

[](#user_activity.data.items.science_metrics.delegation_count)

distinct_session_count: number



Number of distinct Claude Science sessions. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#user_activity.data.items.science_metrics.distinct_session_count)

message_count: number



Number of messages sent in Claude Science sessions

[](#user_activity.data.items.science_metrics.message_count)

remote_compute_job_count: number



Number of remote compute jobs launched from Claude Science sessions

[](#user_activity.data.items.science_metrics.remote_compute_job_count)

skills_used_count: number



Total number of skill invocations in Claude Science sessions

[](#user_activity.data.items.science_metrics.skills_used_count)

[](#user_activity.data.items.science_metrics)

web_search_count: number



Number of web searches performed

[](#user_activity.data.items.web_search_count)

distinct_user_count: optional number



Number of distinct active users represented by this row. Only set for grouped rollups (group_by\[\]); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

[](#user_activity.data.items.distinct_user_count)

last_activity_date: optional string



Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested date in single-day mode, and to the latest active day in \[starting_date, ending_date) in date-range rollup mode — never a day earlier than the window start. On filtered requests (filter\[\]) only days matching the filter count: with filter\[\]=rbac_group_id it is the last day the user was active while a member of that group, consistent with the row's other metrics. Null on grouped (group_by\[\]) rows. Omitted from the response while last-activity reporting is not enabled for this organization.

[](#user_activity.data.items.last_activity_date)

rbac_group_id: optional string



Tagged RBAC group identifier (rbac_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

[](#user_activity.data.items.rbac_group_id)

rbac_group_name: optional string



Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

[](#user_activity.data.items.rbac_group_name)



user: optional [AnalyticsUser](/docs/en/api/admin/analytics#analytics_user) { id, email_address }



User identifier.

id: string



Tagged user identifier (e.g. user\_...)

[](#user_activity.data.items.user%20%2B%20(resource)%20admin.analytics.id)

email_address: string



Email address of the user

[](#user_activity.data.items.user%20%2B%20(resource)%20admin.analytics.email_address)

[](#user_activity.data.items.user)

[](#user_activity.data)

next_page: string



Opaque cursor for the next page, or null if no more results

[](#user_activity.next_page)

[](#user_activity)

List User Activity



```python
curl https://api.anthropic.com/v1/organizations/analytics/users \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
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
      "last_activity_date": "last_activity_date",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user": {
        "id": "id",
        "email_address": "email_address"
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
      "last_activity_date": "last_activity_date",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user": {
        "id": "id",
        "email_address": "email_address"
