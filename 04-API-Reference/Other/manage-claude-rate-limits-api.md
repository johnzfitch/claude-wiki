---
title: "Rate Limits API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/rate-limits-api"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:36Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Frate-limits-api)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Workspaces](manage-claude-workspaces.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

Data & compliance

[Data residency](../Guides/build-with-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](usage-limits.md)

[Admin](manage-claude-admin-api.md)Monitoring

# Rate Limits API

Copy page



Programmatically query your organization's API rate limits with the Rate Limits API.

Copy page





**The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.

The Rate Limits API provides programmatic access to the rate limits configured for your organization and its workspaces. This is the same information shown on the [Rate limits](usage-limits.md) page in the Claude Console.

Use this API to:

- **Keep gateways and proxies in sync:** Read your current limits at startup and on a schedule instead of hardcoding values that drift when Anthropic adjusts them.
- **Power internal alerting:** Compare usage data from the [Usage and Cost API](manage-claude-usage-cost-api.md) against your configured limits.
- **Audit workspace configuration:** Verify that workspace overrides match what your provisioning automation expects.



**Admin API credentials required.** These endpoints are part of the Admin API. You can access them using an [Admin API key](manage-claude-admin-api-keys.md), an OAuth token with the `org:admin` scope, or a personal or service account key that isn't scoped to a workspace; workspace API keys don't work. See [Authentication](manage-claude-admin-api.md#authentication) for details.

The SDK and CLI examples on this page construct the default client, which reads the Admin API key from the `ANTHROPIC_API_KEY` environment variable. The SDKs expose these endpoints as `client.beta.organization.rate_limits` and `client.beta.organization.workspaces.rate_limits`; the Python, TypeScript, C#, Go, and Java list methods return an iterator that follows `next_page` for you, while the PHP, Ruby, and curl examples read one page.

## Quick start

List the rate limits configured for your organization:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

rate_limits = client.beta.organization.rate_limits.list()

for group in rate_limits:
    models = f" ({', '.join(group.models)})" if group.models else ""
    print(f"{group.group_type}{models}")
    for limit in group.limits:
        print(f"  {limit.type}: {limit.value}")
```

## Organization rate limits

The `/v1/organizations/rate_limits` endpoint returns the rate limits applied at the organization level for the Messages API and its supporting resources. Limits for other products, such as [Claude Managed Agents](managed-agents-overview.md), are not included.

### Key concepts

- **Rate limit groups:** Each entry in the response represents one rate limit group. Model rate limits are grouped so that several model versions share a single set of limits, and other groups cover resources such as the Message Batches API, the Files API, the Token Counting API, agent skills, and the web search tool.
- **`group_type`:** Identifies which category of limits the entry covers. See [Filtering by group type](#filtering-by-group-type) for the list of values.
- **`models` list:** For `model_group` entries, the `models` field lists every model ID and alias that counts against that group's limits. Use this list to look up which group any model string falls under. For other group types, `models` is `null`.
- **`limits` list:** Each group carries a list of `{type, value}` pairs. The `type` field identifies the limiter (such as `requests_per_minute`, `input_tokens_per_minute`, or `output_tokens_per_minute`) and `value` is the configured limit. See [Rate limits](../Endpoints/rate-limits.md) for how each limiter is measured and enforced.

For complete parameter details and response schemas, see the [Organization Rate Limits API reference](../Admin/beta-organization-rate-limits-list.md).

### List all organization rate limits

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

rate_limits = client.beta.organization.rate_limits.list()

for group in rate_limits:
    models = f" ({', '.join(group.models)})" if group.models else ""
    print(f"{group.group_type}{models}")
    for limit in group.limits:
        print(f"  {limit.type}: {limit.value}")
```

```python
{
  "data": [
    {
      "type": "rate_limit",
      "group_type": "model_group",
      "models": ["claude-opus-5-5"],
      "limits": [
        { "type": "requests_per_minute", "value": 4000 },
        { "type": "input_tokens_per_minute", "value": 10000000 },
        { "type": "output_tokens_per_minute", "value": 800000 }
      ]
    },
    {
      "type": "rate_limit",
      "group_type": "model_group",
      "models": [
        "claude-opus-4-5",
        "claude-opus-4-5-20251101",
        "claude-opus-4-6",
        "claude-opus-4-7",
        "claude-opus-4-8"
      ],
      "limits": [
        { "type": "requests_per_minute", "value": 4000 },
        { "type": "input_tokens_per_minute", "value": 10000000 },
        { "type": "output_tokens_per_minute", "value": 800000 }
      ]
    },
    {
      "type": "rate_limit",
      "group_type": "batch",
      "models": null,
      "limits": [{ "type": "enqueued_batch_requests", "value": 500000 }]
    }
  ],
  "next_page": null
}
```



### Look up the limits for a specific model

Pass any model ID or alias as the `model` query parameter to return only the entry that contains it:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

rate_limits = client.beta.organization.rate_limits.list(model="claude-opus-5")

for group in rate_limits:
    models = f" ({', '.join(group.models)})" if group.models else ""
    print(f"{group.group_type}{models}")
    for limit in group.limits:
        print(f"  {limit.type}: {limit.value}")
```

If the model string doesn't match any group, the endpoint returns a 404 error. The `model` parameter is supported on the organization endpoint only; the workspace endpoint doesn't accept it.

## Workspace rate limits

The `/v1/organizations/workspaces/{workspace_id}/rate_limits` endpoint returns the rate limit overrides configured for a single workspace.

The response only includes overrides, so anything missing from it is inherited from the organization:

- A group that is absent from `data` has no workspace override at all. The workspace inherits the organization-level limits for that group (it is not unlimited).
- Within a group that is present, a limiter type that is absent from `limits[]` has no workspace override for that limiter. The workspace inherits the organization value for it.
- For each limiter that is present, `org_limit` is the organization-level value for the same limiter, or `null` if the organization has no configured limit for that limiter type.

For complete parameter details and response schemas, see the [Workspace Rate Limits API reference](../Admin/beta-organization-workspaces-rate-limits-list.md).



To retrieve your organization's workspace IDs, use the [List Workspaces](../Admin/beta-organization-workspaces-list.md) endpoint, or find them in the [Claude Console](usage-limits.md). The default workspace cannot have rate limit overrides, so it has no entry on this endpoint; use the organization endpoint to read its limits.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

rate_limits = client.beta.organization.workspaces.rate_limits.list(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
)

for group in rate_limits:
    models = f" ({', '.join(group.models)})" if group.models else ""
    print(f"{group.group_type}{models}")
    for limit in group.limits:
        print(f"  {limit.type}: {limit.value}")
```

```python
{
  "data": [
    {
      "type": "workspace_rate_limit",
      "group_type": "model_group",
      "models": ["claude-opus-5-5"],
      "limits": [
        { "type": "requests_per_minute", "value": 1000, "org_limit": 4000 },
        { "type": "input_tokens_per_minute", "value": 500000, "org_limit": 10000000 }
      ]
    },
    {
      "type": "workspace_rate_limit",
      "group_type": "model_group",
      "models": [
        "claude-opus-4-5",
        "claude-opus-4-5-20251101",
        "claude-opus-4-6",
        "claude-opus-4-7",
        "claude-opus-4-8"
      ],
      "limits": [
        { "type": "requests_per_minute", "value": 1000, "org_limit": 4000 },
        { "type": "input_tokens_per_minute", "value": 500000, "org_limit": 10000000 }
      ]
    }
  ],
  "next_page": null
}
```



## Filtering by group type

Both endpoints accept an optional `group_type` query parameter that restricts the response to a single category:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

rate_limits = client.beta.organization.rate_limits.list(group_type="batch")

for group in rate_limits:
    models = f" ({', '.join(group.models)})" if group.models else ""
    print(f"{group.group_type}{models}")
    for limit in group.limits:
        print(f"  {limit.type}: {limit.value}")
```

Valid values are `model_group`, `batch`, `token_count`, `files`, `skills`, and `web_search`.

## Pagination

Both endpoints accept a `page` query parameter and return a `next_page` field. Responses are currently always a single page, so `next_page` is `null`. Loop on `next_page` so your client paginates correctly without changes when the response grows.

## Frequently asked questions

### Which model strings appear in the `models` list?

Every model ID and alias that counts against the group, including dated IDs (such as `claude-sonnet-4-5-20250929`) and undated aliases (such as `claude-sonnet-4-5`). Look up any model string you pass to the Messages API and you'll find it in exactly one `model_group` entry.

### What does it mean if a group is missing from the workspace response?

The workspace has no override for that group and inherits the organization-level limit. Query the organization endpoint to see the inherited values.

### Can I update rate limits with this API?

No. To set workspace rate limits, open the workspace in the [Claude Console](usage-limits.md) and use the **Rate limits** tab.

## See also

- [Rate limits](../Endpoints/rate-limits.md)
- [Admin API](manage-claude-admin-api.md)
- [Admin API reference](../Admin/http-beta-organization.md)
- [Workspaces](manage-claude-workspaces.md)
- [Usage and Cost API](manage-claude-usage-cost-api.md)
