---
title: "Analytics - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/analytics"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:35:39Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Analytics

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### Models



BetaAnalyticsActor = [BetaAnalyticsReportUserActor](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_report_user_actor) or [BetaAnalyticsServiceAccountActor](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_service_account_actor) or [BetaAnalyticsFederatedActor](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_federated_actor) or [BetaAnalyticsAPIActor](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_api_actor)



One of the following:



BetaAnalyticsActorType = "api_actor" or "federated_actor" or "service_account_actor" or "user_actor"



Kind of identity a row's usage is attributed to.

One of the following:

"api_actor"



"federated_actor"



"service_account_actor"



"user_actor"





BetaAnalyticsAPIActor object{ type: "api_actor", api_key_id }



type: "api_actor"



api_key_id: string



Tagged API key ID.



BetaAnalyticsArtifactActivity object{ artifact_type, artifacts_created_count, distinct_user_count, 6 more }



Artifact-creation activity for one (`artifact_type`, `is_shared`) bucket on a given day.

Artifacts form a small finite cube — the canonical MIME type (8 values incl. `other`) crossed with shared-vs-private — so the response is the full set of non-empty buckets, not a ranked/paginated list. Claude Code and Cowork artifacts report under `text/html` and are counted from 2026-08-17 onward; earlier days contain claude.ai chat artifacts only. With `group_by[]=product` / `user_id` / `rbac_group_id` each row is further split by the flat group keys and counts are scoped to that cut.



BetaAnalyticsArtifactGroupBy = "product" or "rbac_group_id" or "user_id"

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

BetaAnalyticsChatCoworkUnifiedChatMetrics object{ connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }



Chat activity recorded while members had Chat and Cowork unified turned on.



BetaAnalyticsChatCoworkUnifiedMetrics object{ chat, sessions }



Activity in Chat and Cowork unified for one user on one day: `chat` holds chat activity and `sessions` holds Cowork session activity.



chat: [BetaAnalyticsChatCoworkUnifiedChatMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_chat_cowork_unified_chat_metrics) { connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }



Chat activity recorded while members had Chat and Cowork unified turned on.



sessions: [BetaAnalyticsChatCoworkUnifiedSessionsMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_chat_cowork_unified_sessions_metrics) { action_count, artifacts_created_count, connectors_used_count, 14 more }



Cowork session activity recorded while members had Chat and Cowork unified turned on.



BetaAnalyticsChatCoworkUnifiedSessionsMetrics object{ action_count, artifacts_created_count, connectors_used_count, 14 more }



Cowork session activity recorded while members had Chat and Cowork unified turned on.



BetaAnalyticsChatMetrics object{ connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }



Claude.ai activity metrics for a single user on a given day.



BetaAnalyticsClaudeCodeMetrics object{ core_metrics, tool_actions }



Claude Code activity metrics for a single user on a given day.



BetaAnalyticsClaudeTagCategory = "dm" or "engaged" or "monitoring" or 2 more



One of the following:

"dm"



"engaged"



"monitoring"



"proactive"



"scheduled"





BetaAnalyticsClaudeTagMetrics object{ active_day_count, active_message_count }



Claude Tag activity metrics for a single linked user on a given day.

active_day_count: number or null



1 on a day the user was active in Claude Tag in Slack, otherwise 0. Summed over the window in date-range mode, so it is the number of active days; on grouped rows, the total of each member's active days. Null when Claude Tag data cannot be read for the request. Otherwise, 0 on a row filtered by project, and null on any other row when no covered day was measured.

active_message_count: number or null



Number of the user's Slack messages that made them active: @-mentions, direct messages, group direct message asks, and thread posts Claude answered. Other messages are not counted. Null when Claude Tag data cannot be read for the request. Otherwise, 0 on a row filtered by project, and null on any other row when no covered day was measured.



BetaAnalyticsConnectorActivity object{ chat_metrics, claude_code_metrics, connector_display_name, 14 more }



Per-connector activity data for a given day.



BetaAnalyticsConnectorChatCoworkUnifiedChatMetrics object{ distinct_conversation_connector_used_count }



A connector's use in chat conversations recorded while members had Chat and Cowork unified turned on.

distinct_conversation_connector_used_count: number or null



Same measure as `chat_metrics.distinct_conversation_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsConnectorChatCoworkUnifiedMetrics object{ chat, sessions }



A connector's use in Chat and Cowork unified on one day: `chat` holds its use in chat conversations and `sessions` its use in Cowork sessions.



chat: [BetaAnalyticsConnectorChatCoworkUnifiedChatMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_connector_chat_cowork_unified_chat_metrics) { distinct_conversation_connector_used_count }



A connector's use in chat conversations recorded while members had Chat and Cowork unified turned on.

distinct_conversation_connector_used_count: number or null



Same measure as `chat_metrics.distinct_conversation_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



sessions: [BetaAnalyticsConnectorChatCoworkUnifiedSessionsMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_connector_chat_cowork_unified_sessions_metrics) { distinct_session_connector_used_count }



A connector's use in Cowork sessions recorded while members had Chat and Cowork unified turned on.

distinct_session_connector_used_count: number or null



Same measure as `cowork_metrics.distinct_session_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsConnectorChatCoworkUnifiedSessionsMetrics object{ distinct_session_connector_used_count }



A connector's use in Cowork sessions recorded while members had Chat and Cowork unified turned on.

distinct_session_connector_used_count: number or null



Same measure as `cowork_metrics.distinct_session_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsConnectorChatMetrics object{ distinct_conversation_connector_used_count }



Claude.ai activity metrics for a single connector on a given day.

distinct_conversation_connector_used_count: number or null



Number of distinct conversations in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsConnectorClaudeCodeMetrics object{ distinct_session_connector_used_count }



Claude Code activity metrics for a single connector on a given day.

distinct_session_connector_used_count: number or null



Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsConnectorCoworkMetrics object{ distinct_session_connector_used_count }



Cowork activity metrics for a single connector on a given day.

distinct_session_connector_used_count: number or null



Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsConnectorGroupBy = "product" or "rbac_group_id" or "user_id"

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

BetaAnalyticsConnectorOfficeMetrics object{ excel, outlook, powerpoint, word }



Office Agent activity metrics for a single connector on a given day, broken out by Office product.



BetaAnalyticsConnectorOfficeProductMetrics object{ distinct_session_connector_used_count }



Office Agent activity metrics for a single connector on a given day within one Office product.

distinct_session_connector_used_count: number or null



Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsContextWindow = "0-200k" or "200k-1M"



One of the following:

"0-200k"



"200k-1M"





BetaAnalyticsCoreCodeMetrics object{ artifacts_created_count, commit_count, distinct_session_count, 2 more }

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

lines_of_code: [BetaAnalyticsLinesOfCode](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_lines_of_code) { added_count, removed_count }

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

BetaAnalyticsCostBucketedResult object{ amount, claude_tag_category, claude_tag_user_id, 12 more }





BetaAnalyticsCostReportTimeBucket object{ ending_at, results, starting_at }





BetaAnalyticsCostType = "code_execution" or "tokens" or "web_search"



One of the following:

"code_execution"



"tokens"



"web_search"





BetaAnalyticsCostUsersItem object{ actor, amount, claude_tag_category, 15 more }





BetaAnalyticsCoworkMetrics object{ action_count, artifacts_created_count, connectors_used_count, 14 more }



Cowork activity metrics for a single user on a given day.



BetaAnalyticsDesignMetrics object{ distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count }

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

BetaAnalyticsFederatedActor object{ type: "federated_actor", provider, subject }



type: "federated_actor"





provider: [BetaAnalyticsFederatedActorProvider](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_federated_actor_provider)



The trusted provider that asserted the caller's identity.

One of the following:

subject: string or null



The provider's identifier for the caller: on `aws`, the IAM principal ARN (one role is one actor across its sessions); on `gcp`, the caller's IAM principal identifier as Google Cloud reports it, such as `serviceAccount:<email>`, `user:<email>`, or a `principal://...` URI.



BetaAnalyticsFederatedActorAWSProvider object{ type: "aws", account_id, signed_principal }



type: "aws"



account_id: string



The AWS account the organization is bound to.

signed_principal: string



The AWS-signed ARN of the IAM principal that made the requests.



BetaAnalyticsFederatedActorAzureProvider object{ type: "azure", subscription_id }



type: "azure"



subscription_id: string



The Azure subscription the organization is bound to.



BetaAnalyticsFederatedActorGCPProvider object{ type: "gcp", project_number }



type: "gcp"



project_number: string



The Google Cloud project the organization is bound to.



BetaAnalyticsFederatedActorOIDCProvider object{ type: "oidc", issuer }



type: "oidc"



issuer: string or null



The federation issuer's URL.



BetaAnalyticsFederatedActorProvider = [BetaAnalyticsFederatedActorAWSProvider](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_federated_actor_aws_provider) or [BetaAnalyticsFederatedActorAzureProvider](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_federated_actor_azure_provider) or [BetaAnalyticsFederatedActorGCPProvider](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_federated_actor_gcp_provider) or [BetaAnalyticsFederatedActorOIDCProvider](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_federated_actor_oidc_provider)



One of the following:



BetaAnalyticsGroupedCostType = "code_execution" or "session_usage" or "tokens" or "web_search"



One of the following:

"code_execution"



"session_usage"



"tokens"



"web_search"





BetaAnalyticsInferenceGeoFilter = "global" or "not_available" or "us"



One of the following:

"global"



"not_available"



"us"





BetaAnalyticsLinesOfCode object{ added_count, removed_count }



Lines of code added and removed via Claude Code.

added_count: number



Lines of code added

removed_count: number



Lines of code removed



BetaAnalyticsOfficeMetrics object{ excel, outlook, powerpoint, word }



Office Agent activity metrics for a single user on a given day, broken out by Office product.



BetaAnalyticsOfficeProductMetrics object{ connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }

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

BetaAnalyticsOrder = "asc" or "desc"



Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

One of the following:

"asc"



"desc"





BetaAnalyticsPluginActivity object{ claude_code_metrics, cowork_metrics, distinct_user_count, 9 more }



Per-plugin install + invocation activity for a given day.

With `group_by[]=user_id` / `rbac_group_id` / `product` (`cowork`, `claude_code` and `chat_cowork_unified` only on this endpoint) each row is one (plugin, user), (plugin, group), or (plugin, product) cut: the flat `user_id` / `rbac_group_id` / `product` keys carry the cut and the counts are scoped to it.



BetaAnalyticsPluginChatCoworkUnifiedMetrics object{ distinct_session_plugin_used_count }



A plugin's use in Cowork sessions recorded while members had Chat and Cowork unified turned on.

distinct_session_plugin_used_count: number or null



Same measure as `cowork_metrics.distinct_session_plugin_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsPluginClaudeCodeMetrics object{ distinct_session_plugin_used_count }



Claude Code activity metrics for a single plugin on a given day.

distinct_session_plugin_used_count: number or null



Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsPluginCoworkMetrics object{ distinct_session_plugin_used_count }



Cowork activity metrics for a single plugin on a given day.

distinct_session_plugin_used_count: number or null



Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsPluginGroupBy = "product" or "rbac_group_id" or "user_id"

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

BetaAnalyticsProductFilter = "chat" or "chat_cowork_unified" or "claude-tag" or 5 more



Publicly documented product surfaces. `claude-tag` is Claude Tag, the Claude product in Slack. `chat_cowork_unified` is Chat and Cowork unified, Cowork's features inside claude.ai chat: chat and Cowork usage by a member who has it turned on is reported under this value instead of `chat` or `cowork`. It is accepted as a filter only where Chat and Cowork unified is available.

One of the following:

"chat"



"chat_cowork_unified"



"claude-tag"



"claude_code"



"claude_design"



"claude_in_chrome"



"cowork"



"office_agent"





BetaAnalyticsProjectActivity object{ created_at, created_by, distinct_conversation_count, 7 more }



Per-project activity data for a given day.



BetaAnalyticsProjectGroupBy = "rbac_group_id" or "user_id"



A dimension to group chat project activity by.

One of the following:

"rbac_group_id"



"user_id"





BetaAnalyticsReportUserActor object{ type: "user_actor", deleted, email_address, 2 more }



type: "user_actor"



Actor type. Always `"user_actor"`.

deleted: boolean



True when the account has been deleted, or when the user is no longer a member of the organization or its associated organizations (for example, their membership was removed or they were deprovisioned via your identity provider). `email_address` stays populated for removed users and is null when the account has been deleted. `name` follows the rules described on that field. The `user_id` is still populated for reconciliation.

email_address: string or null



The user's current email address, including for users who are no longer members of the organization. Null when the account has been deleted and for system-minted service accounts.

name: string or null



The user's current full name. Null when the user has not set one. `"Deleted User"` when the account has been deleted, or when the user is no longer a member and the organization hides removed users' names.

user_id: string



Tagged user ID.



BetaAnalyticsScienceMetrics object{ delegation_count, distinct_session_count, message_count, 2 more }

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

BetaAnalyticsServerToolUse object{ web_search_requests }



web_search_requests: number



The number of web search requests made.



BetaAnalyticsServiceAccountActor object{ type: "service_account_actor", service_account_id }



type: "service_account_actor"



service_account_id: string



Tagged service account ID.



BetaAnalyticsServiceTier = "batch" or "flex" or "flex_discount" or 3 more



One of the following:

"batch"



"flex"



"flex_discount"



"priority"



"priority_on_demand"



"standard"





BetaAnalyticsSingleDayActivitySummary object{ assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 32 more }



Per-day entry in the /summaries response.



BetaAnalyticsSkillActivity object{ attributed_list_price, chat_metrics, claude_code_metrics, 15 more }



Per-skill activity data for a given day.



BetaAnalyticsSkillChatCoworkUnifiedChatMetrics object{ distinct_conversation_skill_used_count }



A skill's use in chat conversations recorded while members had Chat and Cowork unified turned on.

distinct_conversation_skill_used_count: number or null



Same measure as `chat_metrics.distinct_conversation_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsSkillChatCoworkUnifiedMetrics object{ chat, sessions }



A skill's use in Chat and Cowork unified on one day: `chat` holds its use in chat conversations and `sessions` its use in Cowork sessions.



chat: [BetaAnalyticsSkillChatCoworkUnifiedChatMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_skill_chat_cowork_unified_chat_metrics) { distinct_conversation_skill_used_count }



A skill's use in chat conversations recorded while members had Chat and Cowork unified turned on.

distinct_conversation_skill_used_count: number or null



Same measure as `chat_metrics.distinct_conversation_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



sessions: [BetaAnalyticsSkillChatCoworkUnifiedSessionsMetrics](platform-claude-com-http-beta-organization-analytics.md#beta_analytics_skill_chat_cowork_unified_sessions_metrics) { distinct_session_skill_used_count }



A skill's use in Cowork sessions recorded while members had Chat and Cowork unified turned on.

distinct_session_skill_used_count: number or null



Same measure as `cowork_metrics.distinct_session_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsSkillChatCoworkUnifiedSessionsMetrics object{ distinct_session_skill_used_count }



A skill's use in Cowork sessions recorded while members had Chat and Cowork unified turned on.

distinct_session_skill_used_count: number or null



Same measure as `cowork_metrics.distinct_session_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsSkillChatMetrics object{ distinct_conversation_skill_used_count }



Claude.ai activity metrics for a single skill on a given day.

distinct_conversation_skill_used_count: number or null



Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsSkillClaudeCodeMetrics object{ distinct_session_skill_used_count }



Claude Code activity metrics for a single skill on a given day.

distinct_session_skill_used_count: number or null



Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsSkillCoworkMetrics object{ distinct_session_skill_used_count }



Cowork activity metrics for a single skill on a given day.

distinct_session_skill_used_count: number or null



Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsSkillGroupBy = "product" or "rbac_group_id" or "user_id"

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

BetaAnalyticsSkillOfficeMetrics object{ excel, outlook, powerpoint, word }



Office Agent activity metrics for a single skill on a given day, broken out by Office product.



BetaAnalyticsSkillOfficeProductMetrics object{ distinct_session_skill_used_count }



Office Agent activity metrics for a single skill on a given day within one Office product.

distinct_session_skill_used_count: number or null



Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



BetaAnalyticsSpeed = "fast" or "standard"



One of the following:

"fast"



"standard"





BetaAnalyticsTimeBucketWidth = "1d" or "1h" or "1m"



One of the following:

"1d"



"1h"



"1m"





BetaAnalyticsTokenType = "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more



One of the following:

"cache_creation.ephemeral_1h_input_tokens"



"cache_creation.ephemeral_5m_input_tokens"



"cache_read_input_tokens"



"output_tokens"



"uncached_input_tokens"





BetaAnalyticsToolActionCounts object{ accepted_count, rejected_count }



Accepted/rejected counts for a single Claude Code tool type.

accepted_count: number



Number of tool proposals accepted

rejected_count: number



Number of tool proposals rejected



BetaAnalyticsToolActions object{ edit_tool, multi_edit_tool, notebook_edit_tool, write_tool }



Per-tool accepted/rejected counts for Claude Code file modification tools.



BetaAnalyticsUsageBucketedResult object{ cache_creation, cache_read_input_tokens, claude_tag_category, 12 more }





BetaAnalyticsUsageCostInferenceGeo = "global" or "us"



One of the following:

"global"



"us"





BetaAnalyticsUsageCostProductFilter = "chat" or "chat_cowork_unified" or "claude_code" or 9 more



Publicly documented product surfaces. `claude_tag` is Claude Tag, the Claude product in Slack. `chat_cowork_unified` is Chat and Cowork unified, Cowork's features inside claude.ai chat: chat and Cowork usage by a member who has it turned on is reported under this value instead of `chat` or `cowork`. It is accepted as a filter only where Chat and Cowork unified is available.

One of the following:

"chat"



"chat_cowork_unified"



"claude_code"



"claude_console"



"claude_design"



"claude_in_chrome"



"claude_tag"



"cowork"



"managed_agents_api"



"message_batches_api"



"messages_api"



"office_agent"





BetaAnalyticsUsageCostSortOrder = "asc" or "desc"



One of the following:

"asc"



"desc"





BetaAnalyticsUsageReportTimeBucket object{ ending_at, results, starting_at }





BetaAnalyticsUsageUsersItem object{ actor, cache_creation, cache_read_input_tokens, 16 more }



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

BetaAnalyticsUserActivity object{ chat_metrics, claude_code_metrics, cowork_metrics, 11 more }



Per-user activity data for a given day.



BetaAnalyticsUserActor object{ type: "user_actor", deleted, email_address, 2 more }



type: "user_actor"



Actor type. Always `"user_actor"`.

deleted: boolean



True when the account has been deleted, or when the user is no longer a member of the organization or its associated organizations (for example, their membership was removed or they were deprovisioned via your identity provider). `email_address` stays populated for removed users and is null when the account has been deleted. `name` follows the rules described on that field. The `user_id` is still populated for reconciliation.

email_address: string or null



The user's email address, including for users who are no longer members of the organization or its associated organizations. Null when the account has been deleted (check `deleted`) and for system-minted service accounts, which have no person's mailbox behind them (check `name`).

name: string or null



The user's full name. Null when the user has not set a name. Returns `"Deleted User"` when the account itself has been deleted, or when the user is no longer a member of the organization or its associated organizations and the organization has chosen to hide the names of removed users. Otherwise, the name stays populated for removed users. Rows for system-minted service accounts render the service name (for example, `"Claude Security"`) or null.

user_id: string



Tagged user ID.

BetaAnalyticsUserGroupBy = "rbac_group_id"



A dimension to group user activity by.

#### Analytics[Summaries](http-beta-organization-analytics-summaries.md)

##### [Get Activity Summaries](http-beta-organization-analytics-summaries-list.md)

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

#### Analytics[Users](platform-claude-com-http-beta-organization-analytics-users.md)

##### [List User Activity](platform-claude-com-http-beta-organization-analytics-users-list.md)

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

#### AnalyticsAppsChat[Projects](http-beta-organization-analytics-apps-chat-projects.md)

##### [Get Chat Project Usage](http-beta-organization-analytics-apps-chat-projects-list.md)

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

#### Analytics[Connectors](http-beta-organization-analytics-connectors.md)

##### [Get Connector Usage](platform-claude-com-http-beta-organization-analytics-connectors-list.md)

GET/v1/organizations/analytics/connectors

Get per-connector usage for a given day, with cursor-based pagination.

#### Analytics[Plugins](platform-claude-com-http-beta-organization-analytics-plugins.md)

##### [Get Plugin Usage](platform-claude-com-http-beta-organization-analytics-plugins-list.md)

GET/v1/organizations/analytics/plugins

Get per-plugin install + invocation usage for a given day, with pagination.

#### Analytics[Skills](http-beta-organization-analytics-skills.md)

##### [Get Skill Usage](platform-claude-com-http-beta-organization-analytics-skills-list.md)

GET/v1/organizations/analytics/skills

Get per-skill usage for a given day, with cursor-based pagination.

#### Analytics[Artifacts](http-beta-organization-analytics-artifacts.md)

##### [Get Artifact Activity](platform-claude-com-http-beta-organization-analytics-artifacts-list.md)

GET/v1/organizations/analytics/artifacts

Get artifact-creation activity for a given day, broken out by MIME type.

#### Analytics[Usage](platform-claude-com-http-beta-organization-analytics-usage.md)

##### [Get Token Usage By Dimension](platform-claude-com-http-beta-organization-analytics-usage-list.md)

GET/v1/organizations/analytics/usage

Requires `anthropic-beta: ``analytics-usage-cost-2026-08-24`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Get token usage across a date range, broken out by dimension.

#### Analytics[Cost](platform-claude-com-http-beta-organization-analytics-cost.md)

##### [Get Cost By Dimension](platform-claude-com-http-beta-organization-analytics-cost-list.md)

GET/v1/organizations/analytics/cost

Requires `anthropic-beta: ``analytics-usage-cost-2026-08-24`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Get cost in USD across a date range, broken out by dimension.

#### Analytics[Usage Report](http-beta-organization-analytics-usage-report.md)

##### [Get Token Usage Over Time](http-beta-organization-analytics-usage-report-list.md)

GET/v1/organizations/analytics/usage_report

\[Legacy\] Get token usage over time across a date range.

#### Analytics[User Usage Report](http-beta-organization-analytics-user-usage-report.md)

##### [Get Per-User Token Usage](http-beta-organization-analytics-user-usage-report-list.md)

GET/v1/organizations/analytics/user_usage_report

\[Legacy\] Get per-user token usage across a date range.

#### Analytics[Cost Report](http-beta-organization-analytics-cost-report.md)

##### [Get Cost Over Time](http-beta-organization-analytics-cost-report-list.md)

GET/v1/organizations/analytics/cost_report

\[Legacy\] Get cost in USD over time across a date range.

#### Analytics[User Cost Report](http-beta-organization-analytics-user-cost-report.md)

##### [Get Per-User Cost](http-beta-organization-analytics-user-cost-report-list.md)

GET/v1/organizations/analytics/user_cost_report

\[Legacy\] Get per-user cost in USD across a date range.
