---
title: "Compliance API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/compliance-api"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:34Z"
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fcompliance-api)

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

[Admin](manage-claude-admin-api.md)Compliance API

# Compliance API

Copy page



Programmatic access to your organization's Claude activity, chats, files, projects, sessions in Claude apps, and users for compliance, audit, and governance.

Copy page



The Compliance API gives Claude Enterprise and Claude Console customers programmatic access to their organization's Activity Feed. For Claude Enterprise organizations, it also covers the directory of users, roles, and groups across every linked organization; the effective settings in force for each organization; the underlying chats, files, and projects in claude.ai organizations; and Cowork, Claude Code, Claude Science, Claude for Microsoft 365, and Claude in Chrome sessions. Security, legal, and compliance teams use it to audit activity, retrieve or delete content, and feed events into downstream tooling.



Two key types unlock the Compliance API. A **Compliance Access Key** (created in claude.ai) reaches every endpoint, and an **Admin API key** (created in Claude Console) reaches the Activity Feed only. See [Which key do you need?](manage-claude-compliance-api-access.md#which-key-do-you-need) for the full key-type comparison.

The following call returns the most recent activity event in your organization. Any key with the `read:compliance_activities` scope can make it. To create a key and grant it that scope, see [Set up the Compliance API](manage-claude-compliance-api-access.md).

cURL



```python
curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/activities?limit=1" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01"
```

A successful response returns a JSON object containing `data` (an array of `Activity` records), `has_more`, `first_id`, and `last_id`:

Response



```python
{
  "data": [
    {
      "id": "activity_01XyDMpzjS89pFZXqSFUBDr6",
      "created_at": "2026-04-10T08:09:10Z",
      "organization_id": "org_01Wv6QeBcDfGhJkLmNpQrSt8",
      "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
      "actor": {
        "type": "user_actor",
        "email_address": "user@example.com",
        "user_id": "user_01TuVwXyZaBcDeFgH2JkLmN4",
        "ip_address": "192.0.2.34",
        "user_agent": "Mozilla/5.0..."
      },
      "type": "claude_chat_created",
      "claude_chat_id": "claude_chat_01XyDMpzjS89pFZXqSFUBDr6",
      "claude_project_id": "claude_proj_01KGp4eZNug9ri4kE35RSppq"
    }
  ],
  "has_more": true,
  "first_id": "activity_01XyDMpzjS89pFZXqSFUBDr6",
  "last_id": "activity_01XyDMpzjS89pFZXqSFUBDr6"
}
```

------------------------------------------------------------------------

## How the Compliance API works

Every endpoint lives under `/v1/compliance/*` on `https://api.anthropic.com`, authenticates through the `x-api-key` header, and takes the [`anthropic-version`](../Endpoints/versioning.md) header on every request. To provision a key, see [Set up the Compliance API](manage-claude-compliance-api-access.md).

The Activity Feed (`GET /v1/compliance/activities`) is available to any key that carries the `read:compliance_activities` scope; see [Query the Activity Feed](manage-claude-compliance-activity-feed.md) for filters, pagination, and the full `Activity` object. The remaining endpoints require a Compliance Access Key carrying the relevant scope.

A Claude Enterprise tenant has one parent organization (the top-level container that centralizes identity) with linked organizations of two kinds: claude.ai organizations, where users chat and store content, and Claude Console organizations, where users manage Claude API workloads. For a key that covers the parent organization, the directory endpoints (organizations, users, roles, and groups) return data from every linked organization of either kind. The content endpoints (chats, files, projects, project attachments, and sessions) serve Claude Enterprise data only. The chat, file, and project endpoints return claude.ai chats, files, and projects. The session endpoints return transcripts of Cowork, Claude Code, Claude Science, Claude for Microsoft 365, and Claude in Chrome sessions on users' machines (local sessions), captured while users are signed in with their Claude Enterprise account. They also return transcripts of Cowork sessions started on claude.ai web or mobile, which run in the cloud in Anthropic-managed environments (remote sessions). A standalone Claude Console organization (one with no parent organization) is not part of a Claude Enterprise tenant; it uses Admin API keys and can query the Activity Feed only.

All `/v1/compliance/*` endpoints share a rate limit of 600 requests per minute per parent organization (for a standalone Claude Console organization, per organization). The local session endpoints count only against that shared limit, and the remote session endpoints carry a second request budget on top. See [429 Too Many Requests](manage-claude-compliance-errors.md#429-too-many-requests) for the response headers and retry contract.

------------------------------------------------------------------------

## Versioning

Send the `anthropic-version` header on every request; see [API versions](../Endpoints/versioning.md) for the available versions.

------------------------------------------------------------------------

## Compliance API versus related features

A few adjacent features overlap with the Compliance API; here is how to choose.

### Export audit logs

The audit log export is a separate feature in [claude.ai \> Organization settings \> Data and privacy](https://claude.ai/admin-settings/data-privacy-controls) that lets owners and primary owners download a CSV of organization events. It's significantly narrower than the Compliance API: a capped lookback window, CSV download only, and no access to chat, file, or project content. Standardize on the Compliance API for ongoing programmatic use.

### Analytics API

Anthropic provides two analytics APIs: the Claude Enterprise Analytics API and the [Claude Code Analytics API](manage-claude-claude-code-analytics-api.md). Both return aggregated usage and cost figures for IT, FinOps, and platform teams, whereas the Compliance API returns per-event records for security, legal, and compliance teams. The two API families answer different questions, use different keys, and are provisioned separately.

### OpenTelemetry logging

[Cowork's OpenTelemetry logging](../../15-Claude-AI-Features/monitor-claude-cowork-activity-with-opentelemetry.md) and [Claude Code monitoring](../../13-Enterprise-Admin/monitoring-usage.md) stream per-event telemetry, including token, cost, and host metadata, to a collector you run as activity happens, whereas the Compliance API returns retained per-session transcripts from Anthropic on request and works with your existing Compliance Access Key. OpenTelemetry logging can also capture prompts and responses, but Anthropic recommends the Compliance API for retrieving the content of Cowork and Claude Code sessions. For a table comparing local sessions, remote sessions, and OpenTelemetry logging, see the introduction to [Retrieve session transcripts](manage-claude-compliance-sessions.md).

### Inference hooks

[Inference hooks](manage-claude-inference-hooks.md) (beta) act inline: your organization's AI security server receives each governed prompt before inference and can deny it in real time, whereas the Compliance API retrieves records after the fact and returns richer data, such as organization settings and full non-text files.

------------------------------------------------------------------------

## In this section

[Set up the Compliance API](manage-claude-compliance-api-access.md)

Enable the Compliance API for your organization, then create a Compliance Access Key (with scoped permissions) or an Admin API key, and learn which to use.

[Query the Activity Feed](manage-claude-compliance-activity-feed.md)

Retrieve, filter, and paginate the shared Activity Feed. Supported by both key types.

[Retrieve and delete chats, files, and projects](manage-claude-compliance-content-data.md)

Read chat content, files, and project attachments; delete chats, files, and projects on demand. Compliance Access Key required.

[Retrieve session transcripts](manage-claude-compliance-sessions.md)

List the sessions your users run in Claude apps and agents, such as Cowork and Claude Code, and retrieve their transcripts. Compliance Access Key required.

[List organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)

Enumerate linked organizations, members, roles, and directory groups, and read each organization's effective settings.

[Design your compliance integration](manage-claude-compliance-integration-patterns.md)

Choose a feed-consumption pattern, plan SIEM correlation, and decide your retention approach.

[Handle Compliance API errors](manage-claude-compliance-errors.md)

Common 400, 401, 403, 404, 409, 429, and 5xx responses from the Compliance API, with the cause and fix for each.

[API reference](../Endpoints/http-compliance.md)

Endpoint paths, parameters, and response schemas for every Compliance API call.

[Compliance API FAQ](manage-claude-compliance-faq.md)

Answers to common key, scope, availability, and integration questions.
