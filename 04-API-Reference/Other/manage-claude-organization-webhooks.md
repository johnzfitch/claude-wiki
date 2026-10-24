---
title: "Organization webhooks - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/organization-webhooks"
category: "04-API-Reference/Other"
fetched_at: "2026-10-21T06:29:36Z"
tags: ["api", "hooks"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Forganization-webhooks)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Plugins API](manage-claude-plugins-api.md)[Workspaces](manage-claude-workspaces.md)[Organization webhooks (beta)](manage-claude-organization-webhooks.md)[User profiles](manage-claude-user-profiles.md)[Verification Portal links](manage-claude-user-profiles-verification-portal.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

[OpenTelemetry](manage-claude-opentelemetry.md)

Data & compliance

[Data residency](manage-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)

[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys (CMEK)](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](playground.md)

[Admin](manage-claude-admin-api.md)Organization

Organization webhooks

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

webhooks-2026-10-07

# Organization webhooks

Copy page



Register webhook endpoints for events about enforcement actions on your organization's user profiles.

Copy page



An organization webhook endpoint receives an event when Anthropic restricts or bans one of your organization's [user profiles](manage-claude-user-profiles.md), and when the restriction or ban ends. You manage it with the Admin API under `/v1/organizations/webhooks`.



Event delivery isn't live: Anthropic doesn't send the two events, so an endpoint you register receives nothing. You can register endpoints and build your handler from the event format on this page.

Any member of your organization can list and view organization webhook endpoints with the API, but only members with the admin, owner, or primary owner role can create, change, or delete them, or replace their signing secret.

## Before you begin

You need the following:

- An organization on the Claude API that has organization webhooks turned on and doesn't have [HIPAA readiness](manage-claude-api-and-data-retention.md#hipaa-readiness) enabled. To request access, contact your Anthropic account team.
- One of these credentials:
  - An [Admin API key](manage-claude-admin-api-keys.md).
  - An [OAuth bearer token](manage-claude-admin-api.md#oauth-bearer-token) with the `org:admin` scope.
  - A [personal or service account key](manage-claude-authentication.md#key-types) that isn't scoped to a workspace.

## Event types

Organization webhook endpoints accept two event types. Both are about enforcement actions on user profiles. An enforcement action is a restriction or a ban that Anthropic places on the end customer a profile represents.

| Event                                      | Trigger                                                                             |
|--------------------------------------------|-------------------------------------------------------------------------------------|
| `user_profile.enforcement_action_opened`   | Anthropic opens an enforcement action on a user profile.                            |
| `user_profile.enforcement_action_resolved` | An enforcement action ends. Anthropic resolves it, or its `expires_at` time passes. |

Deleting a profile ends its open actions without a `user_profile.enforcement_action_resolved` event.

### Before your first event

Your profiles won't have the `enforcement_status` and `enforcement_actions` fields until enforcement actions are on for your organization. Until then, and in any request whose `anthropic-beta` header has `user-profiles-2026-09-04` or an earlier value, responses leave the fields out and the `enforcement_status[]` list filter returns a `400`. To get the fields, remove that value from your requests.

If an enforcement action opened before Anthropic turned on enforcement actions and event delivery for your organization, or before you registered your endpoint, you don't get a `user_profile.enforcement_action_opened` event for it. The action still appears on the profile. To find these actions, [list your profiles](../Endpoints/user-profiles-list.md) with `enforcement_status[]=restricted` and `enforcement_status[]=banned`. A response might return fewer profiles than `limit`, or none, before the list ends, so keep requesting pages until `next_page` is `null`.

### What an event contains

Events carry IDs, not the action or the profile. `data.id` is the profile's ID, and `data.enforcement_action_id` is the action's ID, which starts with `enac_`:

```python
{
  "type": "event",
  "id": "whe_4f2a9c1e7b3d5a8f0e6c2b9d1a7f3e5c",
  "created_at": "2026-10-15T17:02:41Z",
  "data": {
    "type": "user_profile.enforcement_action_opened",
    "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
    "enforcement_action_id": "enac_011CZkZEq4TnWb7xLfRgPm2v",
    "organization_id": "org_011CZkZBj9RsYd3wNcHvKq6t"
  }
}
```



To see what changed, [retrieve the profile](../Endpoints/user-profiles-retrieve.md) with `client.user_profiles.retrieve()`, using `data.id`. Its `enforcement_actions` list shows its open actions. Each action has a `type` (`restriction` or `ban`), an `id`, a `reason`, an `opened_at` time, and an `expires_at` time or `null`. `enforcement_status` summarizes them: `banned` while a ban is open, `restricted` while any other action is open, and `unrestricted` when none is. Treat any other value as `restricted`.

Anthropic sends an event only after the profile shows the change, so the profile you retrieve shows that change or a later one. Events might arrive late or out of order, so use the profile's current state, not the order events arrive in. After `user_profile.enforcement_action_resolved`, the resolved action is no longer in the list. A `404` means the profile was deleted.

## Endpoint fields

An organization webhook endpoint has these fields:

| Field             | Type             | Description                                                                                                                                                                               |
|-------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`              | string           | The endpoint's ID, which starts with `wep_`. Set by Anthropic.                                                                                                                            |
| `url`             | string           | Where Anthropic sends events. Must be HTTPS on port 443, with a public domain name, not an IP address. Two enabled organization webhook endpoints in your organization can't share a URL. |
| `enabled_events`  | array of strings | The [event types](#event-types) this endpoint receives. A create request must list at least one.                                                                                          |
| `name`            | string           | An optional label for your own use.                                                                                                                                                       |
| `description`     | string           | An optional description for your own use.                                                                                                                                                 |
| `state`           | string           | `enabled` or `disabled`.                                                                                                                                                                  |
| `disabled_reason` | string           | Why Anthropic disabled the endpoint. Empty otherwise.                                                                                                                                     |
| `created_at`      | string           | When the endpoint was created. Set by Anthropic.                                                                                                                                          |
| `updated_at`      | string           | When the endpoint last changed. Set by Anthropic.                                                                                                                                         |
| `signing_secret`  | string           | A `whsec_`-prefixed secret, created with the endpoint. Only the responses that create the endpoint or replace the secret include it, so store it securely.                                |

```python
{
  "id": "wep_011CZkZDf8HnUq2mTxRbVn4s",
  "url": "https://example.com/anthropic-webhooks",
  "name": "Enforcement actions",
  "description": "",
  "enabled_events": [
    "user_profile.enforcement_action_opened",
    "user_profile.enforcement_action_resolved"
  ],
  "state": "enabled",
  "disabled_reason": "",
  "created_at": "2026-10-20T19:00:00Z",
  "updated_at": "2026-10-20T19:00:00Z"
}
```



An organization can have up to 32 organization webhook endpoints. Disabled webhook endpoints still count toward this total.

## Deliveries

Deliveries follow the [Standard Webhooks](https://www.standardwebhooks.com/) specification. Each one carries the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers. Before you trust an event, verify its signature with the endpoint's signing secret, using any Standard Webhooks library.

Return any `2xx` status within 5 seconds, and do slow work afterward. Any other response, or no response, counts as a failed attempt.

- **Duplicates:** An endpoint might receive the same event more than once, with the same event `id` (the same value as the `webhook-id` header). Deduplicate on it.

- **Retries:** If a delivery fails, Anthropic retries it a few times over the next few minutes. If every attempt fails, Anthropic drops the event. To catch up, list your profiles by enforcement status, as in [Before your first event](#before-your-first-event).

- **Automatic disabling:** Anthropic disables an endpoint when:

  - It returns a redirect (`3xx`).
  - Its URL resolves to a non-public IP address.
  - Its deliveries keep failing.

  Anthropic skips events for a disabled endpoint and doesn't send them later.

## Manage endpoints

With the Admin API, you can make these requests:

| Task                                                                            | Request                                                                                                                                                |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| List your organization's endpoints                                              | [`GET /v1/organizations/webhooks`](../Admin/beta-organization-webhooks-list.md)                                                                       |
| Create an endpoint                                                              | [`POST /v1/organizations/webhooks`](../Admin/beta-organization-webhooks-create.md)                                                                    |
| Get one endpoint                                                                | [`GET /v1/organizations/webhooks/{webhook_endpoint_id}`](../Admin/beta-organization-webhooks-retrieve.md)                                             |
| Update an endpoint's `url`, `name`, `description`, `enabled_events`, or `state` | [`POST /v1/organizations/webhooks/{webhook_endpoint_id}`](../Admin/beta-organization-webhooks-update.md)                                              |
| Delete an endpoint                                                              | [`DELETE /v1/organizations/webhooks/{webhook_endpoint_id}`](../Admin/beta-organization-webhooks-delete.md)                                            |
| Replace the signing secret                                                      | [`POST /v1/organizations/webhooks/{webhook_endpoint_id}/regenerate_signing_secret`](../Admin/beta-organization-webhooks-regenerate-signing-secret.md) |

In an update, `enabled_events` replaces the endpoint's whole list of event types. An empty list doesn't clear the list: the endpoint keeps the event types it had. To stop deliveries, send `"state": "disabled"` or delete the endpoint.

To turn an endpoint back on, including after Anthropic disabled it, send `"state": "enabled"` in an update request.

When you replace the signing secret, the old secret stops working at once. Deliveries from then on, including retries of earlier events, are signed with the new secret, so update your receiver right away.

Send the `anthropic-beta: webhooks-2026-10-07` header with every request. The SDK and the CLI send it for you. This example lists your organization's endpoints, using an Admin API key from `ANTHROPIC_API_KEY`.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

endpoints = client.beta.organization.webhooks.list()

for endpoint in endpoints:
    print(f"{endpoint.id}: {endpoint.url} ({endpoint.state})")
```

With no endpoints, the API returns an empty list:

```python
{
  "data": [],
  "has_more": false
}
```



A list returns up to 20 endpoints by default. Set `limit` to get up to 100. If `has_more` is `true`, pass the response's `last_id` as `after_id` to get the next page.

This example creates an endpoint that receives both event types:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

endpoint = client.beta.organization.webhooks.create(
    url="https://example.com/anthropic-webhooks",
    name="Enforcement actions",
    enabled_events=[
        "user_profile.enforcement_action_opened",
        "user_profile.enforcement_action_resolved",
    ],
)

print(endpoint.id)
```

The response is the new endpoint, as shown in [Endpoint fields](#endpoint-fields), plus its `signing_secret`.

## Errors

A request returns a `400` if:

- Its `url` doesn't meet the rules in [Endpoint fields](#endpoint-fields), or a create request lists no event types. The error message says what's wrong.
- Your organization has no default workspace.
- Organization webhooks aren't available for your organization because its default workspace uses a [customer-managed encryption key](manage-claude-cmek.md). The error message says so.
- It would give your organization more than 32 organization webhook endpoints.
- It puts an event type other than the two in [Event types](#event-types) in `enabled_events`. The error message lists the accepted types.

A request returns a `403` if your account's role doesn't include the permission the request needs. The error names that permission.

A request returns a `404` if:

- It doesn't send the `anthropic-beta: webhooks-2026-10-07` header.
- Anthropic hasn't turned on organization webhooks for your organization.
- Your organization has HIPAA readiness enabled.
- It uses a kind of credential these requests don't accept.
- Its `webhook_endpoint_id` doesn't match an endpoint in your organization.

A request returns a `409` if:

- It would make two enabled organization webhook endpoints share a URL.
- Another request changed your organization's endpoints at the same time. Retry the request.

## Compatibility

Supported platforms  
- Claude APIBeta
