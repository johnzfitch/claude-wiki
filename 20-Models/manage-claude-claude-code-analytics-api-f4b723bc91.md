---
title: "Claude Code Analytics API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api"
category: "20-Models"
fetched_at: "2026-09-26T06:39:33Z"
tags: ["api", "claude-code"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fclaude-code-analytics-api)





SearchCtrlK

Organization

[Admin API](/docs/en/manage-claude/admin-api)[User management](/docs/en/manage-claude/user-management)[Workspaces](/docs/en/manage-claude/workspaces)

Authentication

[Overview](/docs/en/manage-claude/authentication)[Create an Admin API key](/docs/en/manage-claude/admin-api-keys)[App Attest](/docs/en/manage-claude/app-attest)[Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation)[Manage WIF via API](/docs/en/manage-claude/wif-admin-api)[WIF reference](/docs/en/manage-claude/wif-reference)

Identity providers

Monitoring

[Usage and Cost API](/docs/en/manage-claude/usage-cost-api)[Rate Limits API](/docs/en/manage-claude/rate-limits-api)[Analytics APIs](/docs/en/manage-claude/analytics-api)[Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api)[Spend Limits API](/docs/en/manage-claude/spend-limits-api)

Data & compliance

[Data residency](/docs/en/manage-claude/data-residency)[API and data retention](/docs/en/manage-claude/api-and-data-retention)[Access Transparency](/docs/en/manage-claude/access-transparency)

[Encryption keys](/docs/en/manage-claude/cmek)

[Inference hooks](/docs/en/manage-claude/inference-hooks)

Compliance API

[Overview](/docs/en/manage-claude/compliance-api)[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)[Activity Feed](/docs/en/manage-claude/compliance-activity-feed)[Chats, files, and projects](/docs/en/manage-claude/compliance-content-data)[Session transcripts](/docs/en/manage-claude/compliance-sessions)[Organizations, users, roles, groups, and settings](/docs/en/manage-claude/compliance-org-data)[Design your integration](/docs/en/manage-claude/compliance-integration-patterns)[Errors](/docs/en/manage-claude/compliance-errors)[FAQ](/docs/en/manage-claude/compliance-faq)

[Console](/)

[Admin](/docs/en/manage-claude/admin-api)Monitoring

# Claude Code Analytics API

Copy page



Programmatically access your organization's Claude Code usage analytics and productivity metrics with the Claude Code Analytics Admin API.

Copy page





**The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.

The Claude Code Analytics Admin API provides programmatic access to daily aggregated usage metrics for Claude Code users, enabling organizations to analyze developer productivity and build custom dashboards. This API provides more detail than the basic [Analytics dashboard](/claude-code) without the complexity of the OpenTelemetry integration.

This API enables you to better monitor, analyze, and optimize your Claude Code adoption:

- **Developer productivity analysis:** Track sessions, lines of code added/removed, commits, and pull requests created using Claude Code
- **Tool usage metrics:** Monitor acceptance and rejection rates for different Claude Code tools (Edit, MultiEdit, Write, NotebookEdit)
- **Cost analysis:** View estimated costs and token usage broken down by Claude model
- **Custom reporting:** Export data to build executive dashboards and reports for management teams
- **Usage justification:** Provide metrics to justify and expand Claude Code adoption internally



**Admin API credentials required.** These endpoints are part of the Admin API. You can access them using an [Admin API key](/docs/en/manage-claude/admin-api-keys), an OAuth token with the `org:admin` scope, or a personal or service account key that isn't scoped to a workspace; workspace API keys don't work. See [Authentication](/docs/en/manage-claude/admin-api#authentication) for details.



**Claude Platform on AWS:** The Claude Code Analytics API is not currently available. View Claude Code usage on the **Usage** page in the Claude Console instead.



**Claude Enterprise organizations:** Claude Code activity for claude.ai users is reported by the Claude Enterprise Analytics API, which uses an Analytics API key instead of an Admin API key. See [Analytics APIs](/docs/en/manage-claude/analytics-api) to find which API and key type your organization needs.

## Quick start

Get your organization's Claude Code analytics for a specific day:

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08&\
limit=20" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```



**Set a User-Agent header for integrations**

If you're building an integration, set your User-Agent header to help Anthropic understand usage patterns:

``` block
User-Agent: YourApp/1.0.0 (https://yourapp.com)
```



## Claude Code Analytics API

Track Claude Code usage, productivity metrics, and developer activity across your organization with the `/v1/organizations/usage_report/claude_code` endpoint.

### Key concepts

- **Daily aggregation:** Returns metrics for a single day specified by the `starting_at` parameter
- **User-level data:** Each record represents one user's activity for the specified day
- **Productivity metrics:** Track sessions, lines of code, commits, pull requests, and tool usage
- **Token and cost data:** Monitor usage and estimated costs broken down by Claude model
- **Cursor-based pagination:** Handle large datasets with stable pagination using opaque cursors
- **Data freshness:** Metrics are available with up to 1-hour delay for consistency

For complete parameter details and response schemas, see the [Claude Code Analytics API reference](/docs/en/api/beta/organization/usage_report/retrieve_claude_code).

### Basic examples

#### Get analytics for a specific day

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

#### Get analytics with pagination

cURL



```python
# First request
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08&\
limit=20" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Subsequent request using cursor from response
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08&\
page=page_MjAyNS0wNS0xNFQwMDowMDowMFo=" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

### Request parameters

| Parameter     | Type    | Required | Description                                                             |
|---------------|---------|----------|-------------------------------------------------------------------------|
| `starting_at` | string  | Yes      | UTC date in YYYY-MM-DD format; returns metrics for this single day only |
| `limit`       | integer | No       | Number of records per page (default: 20, max: 1000)                     |
| `page`        | string  | No       | Opaque cursor token from previous response's `next_page` field          |

### Available metrics

Each response record contains the following metrics for a single user on a single day:

#### Dimensions

- **date:** Date in RFC 3339 format (UTC timestamp)
- **actor:** The user or API key that performed the Claude Code actions (either `user_actor` with `email_address` or `api_actor` with `api_key_name`)
- **organization_id:** Organization UUID
- **customer_type:** Type of customer account (`api` for API customers, `subscription` for Pro/Team customers)
- **terminal_type:** Type of terminal or environment where Claude Code was used (for example, `vscode`, `iTerm.app`, `tmux`)

#### Core metrics

- **num_sessions:** Number of distinct Claude Code sessions initiated by this actor
- **lines_of_code.added:** Total number of lines of code added across all files by Claude Code
- **lines_of_code.removed:** Total number of lines of code removed across all files by Claude Code
- **commits_by_claude_code:** Number of git commits created through Claude Code's commit functionality
- **pull_requests_by_claude_code:** Number of pull requests created through Claude Code's PR functionality

#### Tool action metrics

Breakdown of tool action acceptance and rejection rates by tool type:

- **edit_tool.accepted/rejected:** Number of Edit tool proposals that the user accepted/rejected
- **multi_edit_tool.accepted/rejected:** Number of MultiEdit tool proposals that the user accepted/rejected
- **write_tool.accepted/rejected:** Number of Write tool proposals that the user accepted/rejected
- **notebook_edit_tool.accepted/rejected:** Number of NotebookEdit tool proposals that the user accepted/rejected

#### Model breakdown

For each Claude model used:

- **model:** Claude model identifier (for example, `claude-opus-5`)
- **tokens.input/output:** Input and output token counts for this model
- **tokens.cache_read/cache_creation:** Cache-related token usage for this model
- **estimated_cost.amount:** Estimated cost in cents USD for this model
- **estimated_cost.currency:** Currency code for the cost amount (currently always `USD`)

### Response structure

The API returns data in the following format:

```python
{
  "data": [
    {
      "date": "2025-09-08T00:00:00Z",
      "actor": {
        "type": "user_actor",
        "email_address": "developer@company.com"
      },
      "organization_id": "dc9f6c26-b22c-4831-8d01-0446bada88f1",
      "customer_type": "api",
      "terminal_type": "vscode",
      "core_metrics": {
        "num_sessions": 5,
        "lines_of_code": {
          "added": 1543,
          "removed": 892
        },
        "commits_by_claude_code": 12,
        "pull_requests_by_claude_code": 2
      },
      "tool_actions": {
        "edit_tool": {
          "accepted": 45,
          "rejected": 5
        },
        "multi_edit_tool": {
          "accepted": 12,
          "rejected": 2
        },
        "write_tool": {
          "accepted": 8,
          "rejected": 1
        },
        "notebook_edit_tool": {
          "accepted": 3,
          "rejected": 0
        }
      },
      "model_breakdown": [
        {
          "model": "claude-opus-5-5",
          "tokens": {
            "input": 100000,
            "output": 35000,
            "cache_read": 10000,
            "cache_creation": 5000
          },
          "estimated_cost": {
            "currency": "USD",
            "amount": 113
          }
        }
      ]
    }
  ],
  "has_more": false,
  "next_page": null
}
```



## Pagination

The API supports cursor-based pagination for organizations with large numbers of users:

1.  Make your initial request with optional `limit` parameter.
2.  If `has_more` is `true` in the response, use the `next_page` value in your next request.
3.  Continue until `has_more` is `false`.

The cursor encodes the position of the last record and ensures stable pagination even as new data arrives. Each pagination session maintains a consistent data boundary to ensure you don't miss or duplicate records.

## Common use cases

- **Executive dashboards:** Create high-level reports showing Claude Code impact on development velocity
- **AI tool comparison:** Export metrics to compare Claude Code with other AI coding tools such as Copilot and Cursor
- **Developer productivity analysis:** Track individual and team productivity metrics over time
- **Cost tracking and allocation:** Monitor spending patterns and allocate costs by team or project
- **Adoption monitoring:** Identify which teams and users are getting the most value from Claude Code
- **ROI justification:** Provide concrete metrics to justify and expand Claude Code adoption internally

## Frequently asked questions

### How fresh is the analytics data?

Claude Code analytics data typically appears within 1 hour of user activity completion. To ensure consistent pagination results, only data older than 1 hour is included in responses.

### Can I get real-time metrics?

No, this API provides daily aggregated metrics only. For real-time monitoring, consider using the [OpenTelemetry integration](https://code.claude.com/docs/en/monitoring-usage).

### How are users identified in the data?

Users are identified through the `actor` field in two ways:

- **`user_actor`:** Contains `email_address` for users who authenticate through OAuth (most common)
- **`api_actor`:** Contains `api_key_name` for users who authenticate with an API key

The `customer_type` field indicates whether the usage is from `api` customers (pay-as-you-go API) or `subscription` customers (Pro/Team plans).

### What's the data retention period?

Historical Claude Code analytics data is retained and accessible through the API. There is no specified deletion period for this data.

### Which Claude Code deployments are supported?

This API only tracks Claude Code usage on the Claude API. Usage through [Claude in Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock), [Claude in Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry), [Claude on Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai), or [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws) is not included.

### What does it cost to use this API?

The Claude Code Analytics API is free to use for all organizations with access to the Admin API.

### How do I calculate tool acceptance rates?

Tool acceptance rate = `accepted / (accepted + rejected)` for each tool type. For example, if the edit tool shows 45 accepted and 5 rejected, the acceptance rate is 90%.

### What time zone is used for the date parameter?

All dates are in UTC. The `starting_at` parameter should be in YYYY-MM-DD format and represents UTC midnight for that day.

## See also

The Claude Code Analytics API helps you understand and optimize your team's development workflow. Learn more about related features:

- [Admin API](/docs/en/manage-claude/admin-api)
- [Admin API reference](/docs/en/api/beta/organization)
- [Claude Code Analytics dashboard](/claude-code)
- [Usage and Cost API](/docs/en/manage-claude/usage-cost-api) - Track API usage across all Anthropic services
- [Compliance API](/docs/en/manage-claude/compliance-api) - Retrieve audit and activity data
- [Identity and access management](https://code.claude.com/docs/en/iam)
- [Monitoring usage with OpenTelemetry](https://code.claude.com/docs/en/monitoring-usage) for custom metrics and alerting
