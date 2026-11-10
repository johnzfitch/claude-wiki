---
title: "Versions - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/versioning"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:36:20Z"
tags: ["api"]
---

# Versions

Copy page



When making API requests, you must send an `anthropic-version` request header. For example, `anthropic-version: 2026-10-21`. If you are using the [client SDKs](../Other/cli-sdks-libraries-overview.md), this is handled for you automatically.

Copy page



For any given API version, Anthropic preserves:

- Existing input parameters
- Existing output parameters

However, Anthropic may do the following:

- Add additional optional inputs
- Add additional values to the output
- Change conditions for specific error types
- Add new variants to enum-like output values (for example, streaming event types)

Generally, if you are using the API as documented in this reference, Anthropic will not break your usage.

## Version history

Anthropic recommends using the latest API version whenever possible.

- `2026-10-21`
  - [Migrating to API version 2026-10-21](migration-2026-10-21.md) shows how to upgrade.
  - Available on the Claude API, [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), [Claude Models on Google Cloud (Anthropic managed)](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md), [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md), and [Claude Models on Google Cloud (Google managed)](../Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md). On [Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md), it’s available for Claude 4.7 and later models. For other models on Bedrock, see the [migration guide for API version 2026-10-21](migration-2026-10-21.md#upgrade).
  - Messages API:
    - A request that places a `document` block directly in an `assistant` message returns a 400 error.
    - Sending a `text` block with a non-empty `citations` array in a `user` message, directly or inside a `search_result` block, returns a 400 error.
    - The `temperature`, `top_p`, and `top_k` request parameters are removed. A request that sends any of them returns a 400 error on every model.
  - Admin API:
    - [RBAC groups](../Admin/beta-organization-rbac-groups-list.md) no longer return `roles`. Use `role_ids` instead.
    - [RBAC group members](../Admin/beta-organization-rbac-groups-members-list.md), and the response to removing one, no longer return `group_id`. Use `rbac_group_id` instead.
    - [RBAC roles](../Admin/beta-organization-rbac-roles-list.md) no longer return `name`. Use `display_name` instead.
    - [Organization](organization-rate-limits-list.md) and [workspace](organization-workspaces-rate-limits-list.md) rate-limit entries, and the response to [setting a workspace’s rate limits](organization-workspaces-rate-limits-update.md), no longer return `group_type`. Use `group.type` instead.
    - [API keys](organization-api-keys-list.md) no longer return `workspace_id`. Use `scope.workspace_id` instead, which gives the workspace’s real ID even for the Default Workspace (an all-workspaces key has no `workspace_id` in `scope`).
  - Claude Enterprise Analytics API:
    - The per-user [usage](../Admin/beta-organization-analytics-user-usage-report-list.md) and [cost](../Admin/beta-organization-analytics-user-cost-report-list.md) reports no longer have `actor.email`. Use `actor.email_address` instead.
    - The [activity summaries](../Admin/beta-organization-analytics-summaries-list.md) response no longer has `summaries`. Use `data` instead.
- `2023-06-01`
  - New format for [streaming](../Guides/build-with-claude-streaming.md) server-sent events (SSE):
    - Completions are incremental. For example, `" Hello"`, `" my"`, `" name"`, `" is"`, `" Claude." ` instead of `" Hello"`, `" Hello my"`, `" Hello my name"`, `" Hello my name is"`, `" Hello my name is Claude."`.
    - All events are [named events](https://developer.mozilla.org/en-US/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents#named%5Fevents), rather than [data-only events](https://developer.mozilla.org/en-US/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents#data-only%5Fmessages).
    - Removed unnecessary `data: [DONE]` event.
  - Removed legacy `exception` and `truncated` values in responses.
- `2023-01-01`: Initial release.
