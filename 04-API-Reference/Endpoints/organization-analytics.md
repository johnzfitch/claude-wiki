---
title: "Analytics - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/analytics"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:36:43Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](../Admin/platform-claude-com-http-beta-organization-analytics.md).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# Analytics

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### Models



AnalyticsArtifactActivity object{ artifact_type, artifacts_created_count, distinct_user_count, 6 more }



Artifact-creation activity for one (`artifact_type`, `is_shared`) bucket on a given day.

Artifacts form a small finite cube — the canonical MIME type (8 values incl. `other`) crossed with shared-vs-private — so the response is the full set of non-empty buckets, not a ranked/paginated list. Claude Code and Cowork artifacts report under `text/html` and are counted from 2026-08-17 onward; earlier days contain claude.ai chat artifacts only. With `group_by[]=product` / `user_id` / `rbac_group_id` each row is further split by the flat group keys and counts are scoped to that cut.



AnalyticsArtifactGroupBy = "product" or "rbac_group_id" or "user_id"



A dimension to group artifact activity by.

One of the following:

"product"



"rbac_group_id"



"user_id"





AnalyticsChatCoworkUnifiedChatMetrics object{ connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }



Chat activity recorded while members had Chat and Cowork unified turned on.



AnalyticsChatCoworkUnifiedMetrics object{ chat, sessions }



Activity in Chat and Cowork unified for one user on one day: `chat` holds chat activity and `sessions` holds Cowork session activity.



chat: [AnalyticsChatCoworkUnifiedChatMetrics](https://platform.claude.com/docs/en/api/http/organization/analytics#analytics_chat_cowork_unified_chat_metrics) { connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }



Chat activity recorded while members had Chat and Cowork unified turned on.



sessions: [AnalyticsChatCoworkUnifiedSessionsMetrics](https://platform.claude.com/docs/en/api/http/organization/analytics#analytics_chat_cowork_unified_sessions_metrics) { action_count, artifacts_created_count, connectors_used_count, 14 more }



Cowork session activity recorded while members had Chat and Cowork unified turned on.



AnalyticsChatCoworkUnifiedSessionsMetrics object{ action_count, artifacts_created_count, connectors_used_count, 14 more }



Cowork session activity recorded while members had Chat and Cowork unified turned on.



AnalyticsChatMetrics object{ connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }



Claude.ai activity metrics for a single user on a given day.



AnalyticsClaudeCodeMetrics object{ core_metrics, tool_actions }



Claude Code activity metrics for a single user on a given day.



AnalyticsConnectorActivity object{ chat_metrics, claude_code_metrics, connector_display_name, 14 more }



Per-connector activity data for a given day.



AnalyticsConnectorChatCoworkUnifiedChatMetrics object{ distinct_conversation_connector_used_count }



A connector's use in chat conversations recorded while members had Chat and Cowork unified turned on.

distinct_conversation_connector_used_count: number or null



Same measure as `chat_metrics.distinct_conversation_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsConnectorChatCoworkUnifiedMetrics object{ chat, sessions }



A connector's use in Chat and Cowork unified on one day: `chat` holds its use in chat conversations and `sessions` its use in Cowork sessions.



chat: [AnalyticsConnectorChatCoworkUnifiedChatMetrics](https://platform.claude.com/docs/en/api/http/organization/analytics#analytics_connector_chat_cowork_unified_chat_metrics) { distinct_conversation_connector_used_count }



A connector's use in chat conversations recorded while members had Chat and Cowork unified turned on.

distinct_conversation_connector_used_count: number or null



Same measure as `chat_metrics.distinct_conversation_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



sessions: [AnalyticsConnectorChatCoworkUnifiedSessionsMetrics](https://platform.claude.com/docs/en/api/http/organization/analytics#analytics_connector_chat_cowork_unified_sessions_metrics) { distinct_session_connector_used_count }



A connector's use in Cowork sessions recorded while members had Chat and Cowork unified turned on.

distinct_session_connector_used_count: number or null



Same measure as `cowork_metrics.distinct_session_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsConnectorChatCoworkUnifiedSessionsMetrics object{ distinct_session_connector_used_count }



A connector's use in Cowork sessions recorded while members had Chat and Cowork unified turned on.

distinct_session_connector_used_count: number or null



Same measure as `cowork_metrics.distinct_session_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsConnectorChatMetrics object{ distinct_conversation_connector_used_count }



Claude.ai activity metrics for a single connector on a given day.

distinct_conversation_connector_used_count: number or null



Number of distinct conversations in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsConnectorClaudeCodeMetrics object{ distinct_session_connector_used_count }



Claude Code activity metrics for a single connector on a given day.

distinct_session_connector_used_count: number or null



Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsConnectorCoworkMetrics object{ distinct_session_connector_used_count }



Cowork activity metrics for a single connector on a given day.

distinct_session_connector_used_count: number or null



Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsConnectorGroupBy = "product" or "rbac_group_id" or "user_id"



A dimension to group connector activity by.

One of the following:

"product"



"rbac_group_id"



"user_id"





AnalyticsConnectorOfficeMetrics object{ excel, outlook, powerpoint, word }



Office Agent activity metrics for a single connector on a given day, broken out by Office product.



AnalyticsConnectorOfficeProductMetrics object{ distinct_session_connector_used_count }



Office Agent activity metrics for a single connector on a given day within one Office product.

distinct_session_connector_used_count: number or null



Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsCoreCodeMetrics object{ artifacts_created_count, commit_count, distinct_session_count, 2 more }



Core Claude Code activity metrics for a single user on a given day.

artifacts_created_count: number



Number of artifacts created in Claude Code sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

commit_count: number



Number of commits made via Claude Code

distinct_session_count: number or null



Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.



lines_of_code: [AnalyticsLinesOfCode](https://platform.claude.com/docs/en/api/http/organization/analytics#analytics_lines_of_code) { added_count, removed_count }



Lines of code added and removed via Claude Code.

added_count: number



Lines of code added

removed_count: number



Lines of code removed

pull_request_count: number



Number of pull requests created via Claude Code



AnalyticsCoworkMetrics object{ action_count, artifacts_created_count, connectors_used_count, 14 more }



Cowork activity metrics for a single user on a given day.



AnalyticsDesignMetrics object{ distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count }

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

AnalyticsLinesOfCode object{ added_count, removed_count }



Lines of code added and removed via Claude Code.

added_count: number



Lines of code added

removed_count: number



Lines of code removed



AnalyticsOfficeMetrics object{ excel, outlook, powerpoint, word }



Office Agent activity metrics for a single user on a given day, broken out by Office product.



AnalyticsOfficeProductMetrics object{ connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }

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

AnalyticsOrder = "asc" or "desc"



Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

One of the following:

"asc"



"desc"





AnalyticsPluginActivity object{ claude_code_metrics, cowork_metrics, distinct_user_count, 9 more }



Per-plugin install + invocation activity for a given day.

With `group_by[]=user_id` / `rbac_group_id` / `product` (`cowork`, `claude_code` and `chat_cowork_unified` only on this endpoint) each row is one (plugin, user), (plugin, group), or (plugin, product) cut: the flat `user_id` / `rbac_group_id` / `product` keys carry the cut and the counts are scoped to it.



AnalyticsPluginChatCoworkUnifiedMetrics object{ distinct_session_plugin_used_count }



A plugin's use in Cowork sessions recorded while members had Chat and Cowork unified turned on.

distinct_session_plugin_used_count: number or null



Same measure as `cowork_metrics.distinct_session_plugin_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsPluginClaudeCodeMetrics object{ distinct_session_plugin_used_count }



Claude Code activity metrics for a single plugin on a given day.

distinct_session_plugin_used_count: number or null



Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsPluginCoworkMetrics object{ distinct_session_plugin_used_count }



Cowork activity metrics for a single plugin on a given day.

distinct_session_plugin_used_count: number or null



Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsPluginGroupBy = "product" or "rbac_group_id" or "user_id"



A dimension to group plugin activity by.

One of the following:

"product"



"rbac_group_id"



"user_id"





AnalyticsProjectActivity object{ created_at, created_by, distinct_conversation_count, 7 more }



Per-project activity data for a given day.



AnalyticsProjectGroupBy = "rbac_group_id" or "user_id"



A dimension to group chat project activity by.

One of the following:

"rbac_group_id"



"user_id"





AnalyticsScienceMetrics object{ delegation_count, distinct_session_count, message_count, 2 more }

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



AnalyticsSingleDayActivitySummary object{ assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 29 more }



Per-day entry in the /summaries response.



AnalyticsSkillActivity object{ attributed_list_price, chat_metrics, claude_code_metrics, 15 more }



Per-skill activity data for a given day.



AnalyticsSkillChatCoworkUnifiedChatMetrics object{ distinct_conversation_skill_used_count }



A skill's use in chat conversations recorded while members had Chat and Cowork unified turned on.

distinct_conversation_skill_used_count: number or null



Same measure as `chat_metrics.distinct_conversation_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsSkillChatCoworkUnifiedMetrics object{ chat, sessions }



A skill's use in Chat and Cowork unified on one day: `chat` holds its use in chat conversations and `sessions` its use in Cowork sessions.



chat: [AnalyticsSkillChatCoworkUnifiedChatMetrics](https://platform.claude.com/docs/en/api/http/organization/analytics#analytics_skill_chat_cowork_unified_chat_metrics) { distinct_conversation_skill_used_count }



A skill's use in chat conversations recorded while members had Chat and Cowork unified turned on.

distinct_conversation_skill_used_count: number or null



Same measure as `chat_metrics.distinct_conversation_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



sessions: [AnalyticsSkillChatCoworkUnifiedSessionsMetrics](https://platform.claude.com/docs/en/api/http/organization/analytics#analytics_skill_chat_cowork_unified_sessions_metrics) { distinct_session_skill_used_count }



A skill's use in Cowork sessions recorded while members had Chat and Cowork unified turned on.

distinct_session_skill_used_count: number or null



Same measure as `cowork_metrics.distinct_session_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsSkillChatCoworkUnifiedSessionsMetrics object{ distinct_session_skill_used_count }



A skill's use in Cowork sessions recorded while members had Chat and Cowork unified turned on.

distinct_session_skill_used_count: number or null



Same measure as `cowork_metrics.distinct_session_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsSkillChatMetrics object{ distinct_conversation_skill_used_count }



Claude.ai activity metrics for a single skill on a given day.

distinct_conversation_skill_used_count: number or null



Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsSkillClaudeCodeMetrics object{ distinct_session_skill_used_count }



Claude Code activity metrics for a single skill on a given day.

distinct_session_skill_used_count: number or null



Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsSkillCoworkMetrics object{ distinct_session_skill_used_count }



Cowork activity metrics for a single skill on a given day.

distinct_session_skill_used_count: number or null



Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsSkillGroupBy = "product" or "rbac_group_id" or "user_id"



A dimension to group skill activity by.

One of the following:

"product"



"rbac_group_id"



"user_id"





AnalyticsSkillOfficeMetrics object{ excel, outlook, powerpoint, word }



Office Agent activity metrics for a single skill on a given day, broken out by Office product.



AnalyticsSkillOfficeProductMetrics object{ distinct_session_skill_used_count }



Office Agent activity metrics for a single skill on a given day within one Office product.

distinct_session_skill_used_count: number or null



Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



AnalyticsToolActionCounts object{ accepted_count, rejected_count }



Accepted/rejected counts for a single Claude Code tool type.

accepted_count: number



Number of tool proposals accepted

rejected_count: number



Number of tool proposals rejected



AnalyticsToolActions object{ edit_tool, multi_edit_tool, notebook_edit_tool, write_tool }



Per-tool accepted/rejected counts for Claude Code file modification tools.



AnalyticsUser object{ type: "user", id, email_address }

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

AnalyticsUserActivity object{ chat_metrics, claude_code_metrics, cowork_metrics, 10 more }



Per-user activity data for a given day.

AnalyticsUserGroupBy = "rbac_group_id"



A dimension to group user activity by.

#### Analytics[Summaries](https://platform.claude.com/docs/en/api/http/organization/analytics/summaries)

##### [Get Activity Summaries](https://platform.claude.com/docs/en/api/http/organization/analytics/summaries/list)

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

#### Analytics[Users](https://platform.claude.com/docs/en/api/http/organization/analytics/users)

##### [List User Activity](https://platform.claude.com/docs/en/api/http/organization/analytics/users/list)

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

#### AnalyticsAppsChat[Projects](https://platform.claude.com/docs/en/api/http/organization/analytics/apps/chat/projects)

##### [Get Chat Project Usage](https://platform.claude.com/docs/en/api/http/organization/analytics/apps/chat/projects/list)

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

#### Analytics[Connectors](https://platform.claude.com/docs/en/api/http/organization/analytics/connectors)

##### [Get Connector Usage](https://platform.claude.com/docs/en/api/http/organization/analytics/connectors/list)

GET/v1/organizations/analytics/connectors

Get per-connector usage for a given day, with cursor-based pagination.

#### Analytics[Plugins](https://platform.claude.com/docs/en/api/http/organization/analytics/plugins)

##### [Get Plugin Usage](https://platform.claude.com/docs/en/api/http/organization/analytics/plugins/list)

GET/v1/organizations/analytics/plugins

Get per-plugin install + invocation usage for a given day, with pagination.

#### Analytics[Skills](https://platform.claude.com/docs/en/api/http/organization/analytics/skills)

##### [Get Skill Usage](https://platform.claude.com/docs/en/api/http/organization/analytics/skills/list)

GET/v1/organizations/analytics/skills

Get per-skill usage for a given day, with cursor-based pagination.

#### Analytics[Artifacts](https://platform.claude.com/docs/en/api/http/organization/analytics/artifacts)

##### [Get Artifact Activity](https://platform.claude.com/docs/en/api/http/organization/analytics/artifacts/list)

GET/v1/organizations/analytics/artifacts

Get artifact-creation activity for a given day, broken out by MIME type.
