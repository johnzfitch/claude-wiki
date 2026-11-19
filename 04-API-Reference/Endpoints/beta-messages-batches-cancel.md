---
title: "Cancel a Message Batch - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/messages/batches/cancel"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:35:36Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [Messages](platform-claude-com-http-beta-messages.md)
4.  [Batches](https://platform.claude.com/docs/en/api/http/beta/messages/batches)

# Cancel a Message Batch

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/messages/batches/{message_batch_id}/cancel

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](../Guides/build-with-claude-batch-processing.md)

##### Path parameters

message_batch_id: string



ID of the Message Batch.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).



"anthropic-beta": optional array of [AnthropicBeta](platform-claude-com-http-beta.md#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

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

BetaMessageBatch object{ type: "message_batch", id, archived_at, 7 more }



Cancel a Message Batch

cURL



```python
curl https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID/cancel \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
