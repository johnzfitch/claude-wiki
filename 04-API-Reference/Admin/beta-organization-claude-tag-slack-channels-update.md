---
title: "Update Slack Channel - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/claude_tag/slack_channels/update"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-16T06:24:58Z"
tags: ["api", "slack"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Claude Tag](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag)
5.  [Slack Channels](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels)

# Update Slack Channel

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/claude_tag/slack_channels/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Change the settings a Slack channel stores. The update is partial: a setting left out is unchanged, and a setting sent as null is cleared, so the channel inherits it. If any value is refused, no setting in the request is stored. A group direct message takes no settings and returns 400.

##### Path parameters

id: string



The channel's identifier, starting with `slch_`.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).



"anthropic-beta": optional array of [AnthropicBeta](../Endpoints/platform-claude-com-http-beta.md#anthropic_beta)



This endpoint is in beta: requests must send `experimental-claude-tag-2026-10-21` in this header.

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



settings: [BetaClaudeTagSettingsUpdate](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag#beta_claude_tag_settings_update) { enabled, environment_id, guest_policy, 3 more }



The settings to change.

##### Returns



BetaClaudeTagSlackChannel object{ type: "slack_channel", id, created_at, 4 more }



A Slack channel set up for Claude Tag, with the settings it stores or, with `include_inherited`, the settings that apply in it.

Update Slack Channel

cURL



```python
curl https://api.anthropic.com/v1/organizations/claude_tag/slack_channels/$ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: experimental-claude-tag-2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "settings": {}
        }'
```

Response 200



```python
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "settings": {
    "enabled": true,
    "environment_id": "environment_id",
    "guest_policy": {
      "type": "allow"
    },
    "instructions": "instructions",
    "model": "model",
    "reply_mode": {
      "type": "automatic"
    }
  },
  "slack": {
    "channel_id": "xx",
    "workspace_id": "xx"
  },
  "sources": {
    "enabled": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "environment_id": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "guest_policy": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "instructions": [
      {
        "slack_channel_id": "slack_channel_id",
        "type": "slack_channel"
      }
    ],
    "model": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "reply_mode": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    }
  },
  "type": "slack_channel",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "settings": {
    "enabled": true,
    "environment_id": "environment_id",
    "guest_policy": {
      "type": "allow"
    },
    "instructions": "instructions",
    "model": "model",
    "reply_mode": {
      "type": "automatic"
    }
  },
  "slack": {
    "channel_id": "xx",
    "workspace_id": "xx"
  },
  "sources": {
    "enabled": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "environment_id": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "guest_policy": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "instructions": [
      {
        "slack_channel_id": "slack_channel_id",
        "type": "slack_channel"
      }
    ],
    "model": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "reply_mode": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    }
  },
  "type": "slack_channel",
  "updated_at": "2019-12-27T18:11:19.117Z"
