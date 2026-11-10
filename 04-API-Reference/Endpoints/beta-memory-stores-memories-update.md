---
title: "Update a Memory - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores/memories/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:35:50Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [Memory Stores](https://platform.claude.com/docs/en/api/http/beta/memory_stores)
4.  [Memories](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories)

# Update a Memory

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/memory_stores/{memory_store_id}/memories/{memory_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

Update a Memory

##### Path parameters

memory_store_id: string



The ID of the memory store that holds the memory (`memstore_...`).

memory_id: string



The ID of the memory to update (`mem_...`).

##### Query parameters



view: optional [BetaManagedAgentsMemoryView](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories#beta_managed_agents_memory_view)



Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

With `full`, list operations return at most 20 items per page.

One of the following:

"basic"



Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

"full"



Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).



"anthropic-beta": optional array of [AnthropicBeta](platform-claude-com-http-beta.md#anthropic_beta)



This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

One of the following:

string



"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"

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

"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"

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

"cache-diagnosis-2026-04-07"

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

"ce-user-management-2026-07-13"

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

"message-threads-2026-08-12"



"analytics-usage-cost-2026-08-24"



"experimental-claude-tag-2026-10-21"





"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Body

content: optional string or null



New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).



path: optional string or null



The new path of the memory, which renames it. Omit it to keep the current path.

The memory keeps its `id`. A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long. Paths are case-sensitive.

minLength2

maxLength1024

pattern^(/\[^/\]+)+\$



precondition: optional [BetaManagedAgentsPrecondition](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories#beta_managed_agents_precondition) { type: "content_sha256", content_sha256 }



The condition that the memory must meet for the update to apply. Omit it to update unconditionally.

If the condition fails, the request fails with HTTP status 409.

type: "content_sha256"





content_sha256: optional string



Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

pattern^\[a-f0-9\]{64}\$

##### Returns



BetaManagedAgentsMemory object{ type: "memory", id, content_sha256, 7 more }



A text document at a path inside a memory store.

`content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

See the [memory guide](../Other/managed-agents-memory.md#view-and-edit-memories) to learn more about working with memories.

Update a Memory

cURL



```python
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

Response 200



```python
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
