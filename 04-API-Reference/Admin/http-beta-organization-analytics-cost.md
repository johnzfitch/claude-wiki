---
title: "Cost - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/analytics/cost"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-15T06:23:47Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Analytics](platform-claude-com-http-beta-organization-analytics.md)

# Cost

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Get Cost By Dimension](platform-claude-com-http-beta-organization-analytics-cost-list.md)

GET/v1/organizations/analytics/cost

Requires `anthropic-beta: ``analytics-usage-cost-2026-08-24`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Get cost in USD across a date range, broken out by dimension.

##### Models



BetaAnalyticsCostGroup object{ actor, actor_type, agent_id, 19 more }



The dimension values one cost row is broken out by, including `cost_type` and `token_type`.



BetaAnalyticsCostGroupBy = "actor" or "actor_type" or "agent_id" or 19 more



One of the following:



BetaAnalyticsCostItem object{ cost, ending_at, group, starting_at }





BetaAnalyticsCostMetrics object{ amount, currency, list_amount, requests }



The cost of one row.

amount: string



Amount (post-discount, pre-credit) in fractional cents (minor units).



currency: string



Currency code for the cost amount. Currently always `"USD"`.

defaultUSD

list_amount: string



List-price amount (pre-discount) in fractional cents.

requests: number or null



Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).



BetaAnalyticsCostOrderBy = "amount" or "list_amount" or "time"
