---
title: "Usage - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/analytics/usage"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-07T06:23:49Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Analytics](platform-claude-com-http-beta-organization-analytics.md)

# Usage

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Get Token Usage By Dimension](platform-claude-com-http-beta-organization-analytics-usage-list.md)

GET/v1/organizations/analytics/usage

Requires `anthropic-beta: ``analytics-usage-cost-2026-08-24`. [How to send beta headers](../Endpoints/beta-headers.md)

Get token usage across a date range, broken out by dimension.

##### Models



BetaAnalyticsUsageGroup object{ actor, actor_type, agent_id, 16 more }



The dimension values one usage row is broken out by; each is null unless its dimension is in `group_by[]`.



BetaAnalyticsUsageGroupBy = "actor" or "actor_type" or "agent_id" or 16 more



One of the following:

"actor"



"actor_type"



"agent_id"



"api_key_id"



"claude_tag_category"



"claude_tag_user_id"



"context_window"



"deployment_id"



"environment_id"



"inference_geo"



"model"



"product"



"rbac_group_id"



"service_tier"



"session_id"



"slack_channel_id"



"speed"



"user_profile_id"



"workspace_id"





BetaAnalyticsUsageItem object{ ending_at, group, starting_at, usage }





BetaAnalyticsUsageMetrics object{ cache_creation, cache_read_input_tokens, output_tokens, 4 more }



The token usage of one row.



BetaAnalyticsUsageOrderBy = "output_tokens" or "requests" or "time" or 2 more
