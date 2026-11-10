---
title: "Usage and Cost API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/usage-cost-api"
category: "04-API-Reference/Other"
fetched_at: "2026-11-05T06:37:05Z"
tags: ["api"]
---

# Usage and Cost API

Copy page



The legacy Admin API usage and cost report endpoints for Claude Console organizations. For new integrations, use the Usage and Cost Analytics API.

Copy page





**The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization on the [Organization](playground.md) page (`platform.claude.com/settings/organization`) in the Claude Console.



The Usage and Cost API (`/v1/organizations/usage_report/messages` and `/v1/organizations/cost_report`) is a legacy API and remains supported. For new integrations, use the [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md), which reports usage and cost with more grouping and filtering dimensions. To move an existing integration, see [Migrate from the Usage and Cost API](manage-claude-usage-cost-analytics-api.md#migrate-from-usage-cost-api).

The Usage and Cost Admin API provides programmatic and granular access to historical API usage and cost data for your organization. This data is similar to the information available on the [Usage](playground.md) page (`platform.claude.com/usage`) and the [Cost](playground.md) page (`platform.claude.com/cost`) in the Claude Console.

This API allows you to better monitor, analyze, and optimize your Claude implementations:

- **Accurate usage tracking:** Get precise token counts and usage patterns instead of relying solely on response token counting
- **Cost reconciliation:** Match internal records with Anthropic billing for finance and accounting teams
- **Product performance and improvement:** Monitor product performance while measuring if changes to the system have improved it, or set up alerting
- **[Rate limit](../Endpoints/rate-limits.md) optimization:** Optimize features such as [prompt caching](../Guides/build-with-claude-prompt-caching.md) or specific prompts to use your allocated capacity efficiently.
- **Advanced analysis:** Perform deeper data analysis than what’s available in Console



**Admin API credentials required.** These endpoints are part of the Admin API. You can access them using an [Admin API key](manage-claude-admin-api-keys.md), an OAuth token with the `org:admin` scope, or a personal or service account key that isn’t scoped to a workspace; workspace API keys don’t work. See [Authentication](manage-claude-admin-api.md#authentication) for details.

Claude Enterprise organizations use an Analytics API key with a different API instead; see [Which API do you need?](#which-api-do-you-need).



**Claude Platform on AWS:** The Usage and Cost API endpoints are not available. Use the [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md).



**Claude Models on Google Cloud (Anthropic managed):** Of the Usage and Cost API endpoints, only the [usage endpoint](#usage-api) is available. Call it through the [organization-level base URL](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#making-requests) with Google Cloud credentials instead of an Admin API key. The only predefined [IAM role](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#iam-roles) that allows this call is `roles/claude.admin`. For cost data, use the [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md) or the **Cost** page in the [Claude Console](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#using-the-claude-console).

## Which API do you need?

The API to use depends on which Claude product your organization uses:

| Your organization | API | Key type |
|----|----|----|
| Claude Console (Claude Platform) | The [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md) (recommended), or the legacy Usage and Cost Admin API described on this page | Admin API key (`sk-ant-admin01-...`) or another [Admin API credential](manage-claude-admin-api.md#authentication) |
| Claude Enterprise (claude.ai) | The [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md) (recommended), or the [Claude Enterprise Analytics API](../Admin/http-beta-organization-analytics.md) cost and usage endpoints (legacy) | Analytics API key |

Claude Enterprise parent organizations do not appear in Claude Console and carry no Admin API keys, so for them the Analytics API key is the only path to this data. See [Analytics APIs](manage-claude-analytics-api.md) for how to create each key type and which plans the Claude Enterprise cost data applies to.

## Partner solutions

Leading observability platforms offer ready-to-use integrations for monitoring your Claude API usage and cost, without writing custom code. These integrations provide dashboards, alerting, and analytics to help you manage your API usage effectively.



[CloudZero](https://docs.cloudzero.com/docs/connections-anthropic)

Cloud intelligence platform for tracking and forecasting costs



[Datadog](https://docs.datadoghq.com/integrations/anthropic/)

LLM Observability with automatic tracing and monitoring



[Grafana Cloud](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/integrations/integration-reference/integration-anthropic/)

Agentless integration for easy LLM observability with out-of-the-box dashboards and alerts



[Harness](https://developer.harness.io/docs/cloud-cost-management/provider-integrations/ai-providers/anthropic/)

FinOps platform for cloud and AI cost management

[Honeycomb](https://docs.honeycomb.io/integrations/anthropic-usage-monitoring/)

Advanced querying and visualization through OpenTelemetry



[Tempo](https://help.tempo.io/workforceintelligence/latest/connect-to-anthropic)

Usage and cost attribution to Jira work items



[Vantage](https://docs.vantage.sh/connecting_anthropic)

FinOps platform for LLM cost & usage observability

## Quick start

Get your organization’s daily usage for the last 7 days:

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-08T00:00:00Z&\
ending_at=2025-01-15T00:00:00Z&\
bucket_width=1d" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```



**Set a User-Agent header for integrations**

If you’re building an integration, set your User-Agent header to help Anthropic understand usage patterns:

``` block
User-Agent: YourApp/1.0.0 (https://yourapp.com)
```



## Usage API

Track token consumption across your organization with detailed breakdowns by model, workspace, and service tier with the `/v1/organizations/usage_report/messages` endpoint.

### Key concepts

- **Time buckets:** Aggregate usage data in fixed intervals (`1m`, `1h`, or `1d`).
- **Token tracking:** Measure uncached input, cached input, cache creation, and output tokens.
- **Filtering & grouping:** Filter by API key, workspace, model, service tier, context window, [data residency](manage-claude-data-residency.md), or speed, and group results by these dimensions.
- **Server tool usage:** Track usage of server-side tools such as web search.

For complete parameter details and response schemas, see the [Usage API reference](../Admin/beta-organization-usage-report-retrieve-messages.md).

### Basic examples

#### Daily usage by model

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
group_by[]=model&\
bucket_width=1d" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

#### Hourly usage with filtering

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-15T00:00:00Z&\
ending_at=2025-01-15T23:59:59Z&\
models[]=claude-opus-5-5&\
service_tiers[]=batch&\
context_window[]=0-200k&\
bucket_width=1h" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

#### Filter usage by API keys and workspaces

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
api_key_ids[]=apikey_01Rj2N8SVvo6BePZj99NhmiT&\
api_key_ids[]=apikey_01ABC123DEF456GHI789JKL&\
workspace_ids[]=wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ&\
workspace_ids[]=wrkspc_01XYZ789ABC123DEF456MNO&\
bucket_width=1d" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```



To retrieve your organization’s API key IDs, use the [List API Keys](../Endpoints/organization-api-keys-list.md) endpoint.

To retrieve your organization’s workspace IDs, use the [List Workspaces](../Endpoints/organization-workspaces-list.md) endpoint, or find your organization’s workspace IDs in the Claude Console.

#### Data residency

Track your [data residency controls](manage-claude-data-residency.md) by grouping and filtering usage with the `inference_geo` dimension. This is useful for verifying geographic routing across your organization.

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2026-02-01T00:00:00Z&\
ending_at=2026-02-08T00:00:00Z&\
group_by[]=inference_geo&\
group_by[]=model&\
bucket_width=1d" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

You can also filter to a specific geo. Valid values are `global`, `us`, and `not_available`:

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2026-02-01T00:00:00Z&\
ending_at=2026-02-08T00:00:00Z&\
inference_geos[]=us&\
group_by[]=model&\
bucket_width=1d" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```



Models released before February 2026 (prior to Claude Opus 4.6 and Claude Sonnet 4.6) don’t support the `inference_geo` request parameter, so their usage reports return `"not_available"` for this dimension. You can use `not_available` as a filter value in `inference_geos[]` to target those models.

#### Fast mode

Track [fast mode](../Guides/build-with-claude-fast-mode.md) usage by grouping and filtering with the `speed` dimension. This is useful for monitoring standard versus fast mode usage.

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2026-02-01T00:00:00Z&\
ending_at=2026-02-08T00:00:00Z&\
group_by[]=speed&\
group_by[]=model&\
bucket_width=1d" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

You can also filter to a specific speed. Valid values are `standard` and `fast`:

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2026-02-01T00:00:00Z&\
ending_at=2026-02-08T00:00:00Z&\
speeds[]=fast&\
group_by[]=model&\
bucket_width=1d" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

### Time granularity limits

| Granularity | Default limit | Maximum limit | Use case               |
|-------------|---------------|---------------|------------------------|
| `1m`        | 60 buckets    | 1,440 buckets | Real-time monitoring   |
| `1h`        | 24 buckets    | 168 buckets   | Daily patterns         |
| `1d`        | 7 buckets     | 31 buckets    | Weekly/monthly reports |

## Cost API

Retrieve service-level cost breakdowns in USD with the `/v1/organizations/cost_report` endpoint.

### Key concepts

- **Currency:** All costs are in USD, reported as decimal strings in lowest units (cents).
- **Cost types:** Track token usage, web search, and code execution costs.
- **Grouping:** Group costs by workspace or description for detailed breakdowns. When grouping by `description`, responses include parsed fields such as `model` and `inference_geo`.
- **Time buckets:** Only daily granularity (`1d`) is available.

For complete parameter details and response schemas, see the [Cost API reference](../Admin/beta-organization-cost-report-retrieve.md).



Priority Tier costs use a different billing model and are not included in the cost endpoint. Track Priority Tier usage through the usage endpoint instead.

### Basic example

cURL



```python
curl "https://api.anthropic.com/v1/organizations/cost_report?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-31T00:00:00Z&\
group_by[]=workspace_id&\
group_by[]=description" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

## Pagination

Both endpoints support pagination for large datasets:

1.  Make your initial request.
2.  If `has_more` is `true`, use the `next_page` value in your next request.
3.  Continue until `has_more` is `false`.

cURL



```python
# First request
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-31T00:00:00Z&\
limit=7" \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Response includes: "has_more": true, "next_page": "page_xyz..."

# Next request with pagination
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-31T00:00:00Z&\
limit=7&\
page=page_xyz..." \
  -H "anthropic-version: 2026-10-21" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

## Common use cases

Explore detailed implementations in the [Claude Cookbook](https://platform.claude.com/cookbook):

- **Daily usage reports:** Track token consumption trends
- **Cost attribution:** Allocate expenses by workspace for chargebacks
- **Cache efficiency:** Measure and optimize prompt caching
- **Budget monitoring:** Set up alerts for spending thresholds
- **CSV export:** Generate reports for finance teams

## Frequently asked questions

### How fresh is the data?

Usage and cost data typically appears within 5 minutes of API request completion, though delays might occasionally be longer.

### What’s the recommended polling frequency?

The API supports polling once per minute for sustained use. For short bursts (for example, downloading paginated data), more frequent polling is acceptable. Cache results for dashboards that need frequent updates.

### How do I track code execution usage?

Code execution costs appear in the cost endpoint grouped under `Code Execution Usage` in the description field. Code execution is not included in the usage endpoint.

### How do I track Priority Tier usage?

Filter or group by `service_tier` in the usage endpoint and look for the `priority` value. Priority Tier costs are not available in the cost endpoint.

### What happens with playground usage?

API usage from playground in the Claude Console (and from the legacy Anthropic Workbench before it) is not associated with an API key, so `api_key_id` is `null` even when grouping by that dimension.

### Why does the usage report show a service account that I didn’t create?

Usage from some [Claude Managed Agents](managed-agents-overview.md) sessions is reported under an Anthropic-managed service account (`svac_...`). It isn’t listed with the service accounts that you create. See [Find session usage across your organization](managed-agents-session-observability.md#find-session-usage-across-your-organization).

### How is the default workspace represented?

Usage and costs attributed to the default workspace have a `null` value for `workspace_id`.

### How do I get per-user cost breakdowns for Claude Code?

Call the cost endpoint of the [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md#how-do-i-get-per-user-cost-for-claude-code) with `products[]=claude_code&group_by[]=actor`. For cost by API key, group by `api_key_id` instead. The [Claude Code Analytics API](manage-claude-claude-code-analytics-api.md) also provides per-user estimated costs and productivity metrics.

## See also

Use the Usage and Cost APIs to deliver a better experience for your users, manage costs, and preserve your rate limit. Learn more about some of these other features:

- [Admin API](manage-claude-admin-api.md)
- [Admin API reference](../Admin/http-beta-organization.md)
- [Analytics APIs](manage-claude-analytics-api.md) - Which analytics API and key type your organization needs
- [Pricing](../../17-Billing-Plans/about-claude-pricing.md)
- [Prompt caching](../Guides/build-with-claude-prompt-caching.md) - Optimize costs with caching
- [Batch processing](../Guides/build-with-claude-batch-processing.md) - 50 percent discount on batch requests
- [Rate limits](../Endpoints/rate-limits.md) - Understand usage tiers
- [Rate Limits API](manage-claude-rate-limits-api.md) - Read your configured rate limits and set workspace rate limits
- [Data residency](manage-claude-data-residency.md) - Control inference geography
