---
title: "Stream Session Thread Events - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/threads/events/stream"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:35:58Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [Sessions](https://platform.claude.com/docs/en/api/http/beta/sessions)
4.  [Threads](https://platform.claude.com/docs/en/api/http/beta/sessions/threads)
5.  [Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events)

# Stream Session Thread Events

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/sessions/{session_id}/threads/{thread_id}/stream

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

Stream Session Thread Events

##### Path parameters

session_id: string



thread_id: string



##### Query parameters



event_deltas: optional array of [BetaManagedAgentsDeltaType](https://platform.claude.com/docs/en/api/http/beta/sessions#beta_managed_agents_delta_type)



When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

One of the following:

"agent.message"



"agent.thinking"



##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).



"anthropic-beta": optional array of [AnthropicBeta](platform-claude-com-http-beta.md#anthropic_beta)



This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

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



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



BetaManagedAgentsStreamSessionThreadEvents = [BetaManagedAgentsUserMessageEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_message_event) or [BetaManagedAgentsUserInterruptEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_interrupt_event) or [BetaManagedAgentsUserToolConfirmationEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_tool_confirmation_event) or 41 more



Server-sent event in a single thread's stream.

One of the following:

Stream Session Thread Events

cURL



```python
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/stream \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "sevt_011CZkZGPp1iBcp4kaQSihUm",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "sevt_011CZkZGPp1iBcp4kaQSihUm",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
