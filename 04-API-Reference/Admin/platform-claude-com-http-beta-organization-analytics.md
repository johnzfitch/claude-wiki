---
title: "Analytics - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/organization/analytics"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-04T08:32:22Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Forganization%2Fanalytics)

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

# Analytics

##### Models



BetaAnalyticsArtifactActivity object{ artifact_type, artifacts_created_count, distinct_user_count, 6 more }



Artifact-creation activity for one (`artifact_type`, `is_shared`) bucket on a given day.

Artifacts form a small finite cube — the canonical MIME type (8 values incl. `other`) crossed with shared-vs-private — so the response is the full set of non-empty buckets, not a ranked/paginated list. Claude Code and Cowork artifacts report under `text/html` and are counted from 2026-08-17 onward; earlier days contain claude.ai chat artifacts only. With `group_by[]=product` / `user_id` / `rbac_group_id` each row is further split by the flat group keys and counts are scoped to that cut.

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

BetaAnalyticsConnectorActivity object{ chat_metrics, claude_code_metrics, connector_name, 13 more }



Per-connector activity data for a given day.

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

BetaAnalyticsPluginActivity object{ claude_code_metrics, cowork_metrics, distinct_user_count, 8 more }



Per-plugin install + invocation activity for a given day.

With `group_by[]=user_id` / `rbac_group_id` / `product` (`cowork` / `claude_code` only on this endpoint) each row is one (plugin, user), (plugin, group), or (plugin, product) cut: the flat `user_id` / `rbac_group_id` / `product` keys carry the cut and the counts are scoped to it.

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

BetaAnalyticsProductFilter = "chat" or "claude-tag" or "claude_code" or 4 more



Publicly documented product surfaces. `claude-tag` is Claude Tag, the Claude product in Slack.

One of the following:

"chat"

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

BetaAnalyticsProjectActivity object{ distinct_user_count, message_count, project_id, 8 more }



Per-project activity data for a given day.

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

BetaAnalyticsSingleDayActivitySummary object{ assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 26 more }



Per-day entry in the /summaries response.



BetaAnalyticsSkillActivity object{ chat_metrics, claude_code_metrics, cowork_metrics, 14 more }



Per-skill activity data for a given day.

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

BetaAnalyticsUserActivity object{ chat_metrics, claude_code_metrics, cowork_metrics, 9 more }



Per-user activity data for a given day.



BetaAnalyticsUserActor object{ type: "user_actor", deleted, email, 3 more }

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

The user's full name. Null when the user has not set a name. Returns `"Deleted User"` when the account itself has been deleted, or when the user is no longer a member of the organization or its associated organizations and the organization has chosen to hide the names of removed users. Otherwise, the name stays populated for removed users. Rows for system-minted service accounts render the service name (for example, `"Claude Security"` for usage by Anthropic's security-patching service) or null.

user_id: string



Tagged user ID.

email: string or null⁠Deprecated



Deprecated: use `email_address`, which carries the same value.

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

#### Analytics[Usage Report](http-beta-organization-analytics-usage-report.md)

##### [Get Token Usage Over Time](http-beta-organization-analytics-usage-report-list.md)

GET/v1/organizations/analytics/usage_report

Get token usage over time across a date range.

#### Analytics[User Usage Report](http-beta-organization-analytics-user-usage-report.md)

##### [Get Per-User Token Usage](http-beta-organization-analytics-user-usage-report-list.md)

GET/v1/organizations/analytics/user_usage_report

Get per-user token usage across a date range.

#### Analytics[Cost Report](http-beta-organization-analytics-cost-report.md)

##### [Get Cost Over Time](http-beta-organization-analytics-cost-report-list.md)

GET/v1/organizations/analytics/cost_report

Get cost in USD over time across a date range.

#### Analytics[User Cost Report](http-beta-organization-analytics-user-cost-report.md)

##### [Get Per-User Cost](http-beta-organization-analytics-user-cost-report-list.md)

GET/v1/organizations/analytics/user_cost_report

Get per-user cost in USD across a date range.
