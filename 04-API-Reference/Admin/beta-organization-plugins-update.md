---
title: "Update Plugin - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugins/update"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-18T06:27:22Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins)

# Update Plugin

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/plugins/{plugin_id}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Change which stored version of an organization-owned Plugin is served to members, for example to roll back to an earlier one. This pins the served version: later uploads are stored but no longer change what is served, and pinning cannot currently be undone, here or in claude.ai.

Pass the version as `served_version_id`: an earlier one to roll back, a later one to start serving a version that was stored without being served, or the one already served to pin it without changing what is served. No new version is created.

When the organization has content scanning enabled, a version whose `content_scan.status` is `processing` is refused with a 409 (`error_code` `scan_pending`; retry once the scan finishes). A version whose `content_scan.status` is `errored`, or whose `content_scan.assessment` is `fail` or `unknown`, is refused with a 400 (`error_code` `scan_failed`); a `warn` is accepted. If the scan outcome cannot be read at that moment, the request fails with a retryable 503 instead. When the Plugin is in the organization's library marketplace, a version other than the one served is also refused with a 409 when an organization skill that this API does not list has since taken the name of one of its skills: `error_code` `skill_name_taken`, with that name in `details.skill_name`. A member-owned Plugin cannot be updated here (403).

This endpoint does not write installation settings; they are written at `/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

##### Path parameters

plugin_id: string



ID of the Plugin (prefixed `plugin_`).

##### Headers



"anthropic-beta": array of [AnthropicBeta](../Endpoints/platform-claude-com-http-beta.md#anthropic_beta)



This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

One of the following:

string



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"output-128k-2025-02-19"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"



"ce-plugins-2026-09-01"



"spend-limit-reads-2026-09-26"



"telemetry-destinations-2026-08-11"



"webhooks-2026-10-07"



"admin-user-sign-out-2026-10-08"



"message-threads-2026-08-12"



"analytics-usage-cost-2026-08-24"



"experimental-claude-tag-2026-10-21"



"user-profiles-billing-2026-10-01"





"message-batches-2024-09-24"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"prompt-caching-2024-07-31"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"pdfs-2024-09-25"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"token-counting-2024-11-01"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"token-efficient-tools-2025-02-19"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"files-api-2025-04-14"⁠Deprecated



Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14



"extended-cache-ttl-2025-04-11"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"skills-2025-10-02"⁠Deprecated



Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02



"cache-diagnosis-2026-04-07"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"ce-user-management-2026-07-13"⁠Deprecated



This value is no longer needed. Remove it from your requests.

##### Body

served_version_id: string



Serve this version of the Plugin (prefixed `pluginver_`) and pin the served version to it; `latest` is not accepted.

##### Returns



BetaPlugin object{ type: "plugin", id, components, 16 more }



Update Plugin

cURL



```python
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "served_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8"
        }'
```

Response 200



```python
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
