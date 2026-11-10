---
title: "Memories - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores/memories"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:34:59Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [Memory Stores](https://platform.claude.com/docs/en/api/http/beta/memory_stores)

# Memories

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/create)

POST/v1/memory_stores/{memory_store_id}/memories

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Memories](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/list)

GET/v1/memory_stores/{memory_store_id}/memories

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Retrieve a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/retrieve)

GET/v1/memory_stores/{memory_store_id}/memories/{memory_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/update)

POST/v1/memory_stores/{memory_store_id}/memories/{memory_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Delete a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/delete)

DELETE/v1/memory_stores/{memory_store_id}/memories/{memory_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### Models



BetaManagedAgentsConflictError object{ type: "conflict_error", message }



type: "conflict_error"



message: optional string





BetaManagedAgentsContentSha256Precondition object{ type: "content_sha256", content_sha256 }



A precondition that applies an update only if the memory's current content has the hash in `content_sha256`.

If the hashes differ, the request fails with HTTP status 409. Retrieve the memory and retry. If the memory already has exactly the requested `content` and `path`, the request succeeds even though the hashes differ.

type: "content_sha256"





content_sha256: optional string



Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

pattern^\[a-f0-9\]{64}\$



BetaManagedAgentsDeletedMemory object{ type: "memory_deleted", id }



The confirmation that [Delete a Memory](beta-memory-stores-memories-delete.md) returns.

Deleting a memory doesn't delete its versions. [List Memory Versions](beta-memory-stores-memory-versions-list.md) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted.

See the [memory guide](../Other/managed-agents-memory.md#audit-memory-changes) to learn more about how long versions are kept.

type: "memory_deleted"



id: string



ID of the deleted memory (a `mem_...` value).



BetaManagedAgentsError = [BetaInvalidRequestError](platform-claude-com-http-beta.md#beta_invalid_request_error) or [BetaAuthenticationError](platform-claude-com-http-beta.md#beta_authentication_error) or [BetaBillingError](platform-claude-com-http-beta.md#beta_billing_error) or 9 more



One of the following:



BetaManagedAgentsMemory object{ type: "memory", id, content_sha256, 7 more }



A text document at a path inside a memory store.

`content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

See the [memory guide](../Other/managed-agents-memory.md#view-and-edit-memories) to learn more about working with memories.



BetaManagedAgentsMemoryListItem = [BetaManagedAgentsMemory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories#beta_managed_agents_memory) or [BetaManagedAgentsMemoryPrefix](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories#beta_managed_agents_memory_prefix)



One item in a [List Memories](beta-memory-stores-memories-list.md) response: a `memory`, or a `memory_prefix` marker when `depth` is `1`.

One of the following:



BetaManagedAgentsMemory object{ type: "memory", id, content_sha256, 7 more }



A text document at a path inside a memory store.

`content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

See the [memory guide](../Other/managed-agents-memory.md#view-and-edit-memories) to learn more about working with memories.



BetaManagedAgentsMemoryPrefix object{ type: "memory_prefix", path }



A directory marker that [List Memories](beta-memory-stores-memories-list.md) returns instead of the memories below the requested `depth`.

It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

type: "memory_prefix"



path: string



The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.



BetaManagedAgentsMemoryPathConflictError object{ type: "memory_path_conflict_error", conflicting_memory_id, conflicting_path, message }



The error returned with HTTP status 409 when you create or rename a memory and the path you give is already used by another memory or overlaps another memory's path.

Two paths overlap when one is an ancestor of the other, such as `/notes` and `/notes/todo.md`. To free the path, rename or delete the memory that `conflicting_memory_id` references, then retry. To change that memory instead of creating a new one, update it.

type: "memory_path_conflict_error"





conflicting_memory_id: optional string



The ID of the memory that blocked the write (`mem_...`), or an empty string if that memory can't be identified.

Retry the request when it is empty.

conflicting_path: optional string



The path that blocked the write: the requested path, or the path of a memory that is an ancestor or descendant of it.

message: optional string



A human-readable explanation of the conflict. To handle the error in code, use `conflicting_path` and `conflicting_memory_id` instead.



BetaManagedAgentsMemoryPreconditionFailedError object{ type: "memory_precondition_failed_error", message }



The error returned with HTTP status 409 when a request's precondition doesn't hold for the memory's current state, such as `precondition` on an update or `expected_content_sha256` on a delete.

The error doesn't include the memory's current state. Retrieve the memory to see its current content and `content_sha256` before you retry.

See the [memory guide](../Other/managed-agents-memory.md#safe-content-edits-optimistic-concurrency) to learn more about safe content edits with content hash preconditions.

type: "memory_precondition_failed_error"



message: optional string



A human-readable explanation of why the precondition failed.



BetaManagedAgentsMemoryPrefix object{ type: "memory_prefix", path }



A directory marker that [List Memories](beta-memory-stores-memories-list.md) returns instead of the memories below the requested `depth`.

It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

type: "memory_prefix"



path: string



The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.



BetaManagedAgentsMemoryView = "basic" or "full"

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



BetaManagedAgentsPrecondition object{ type: "content_sha256", content_sha256 }



Optional condition that must hold for an update to apply. When omitted, the update is unconditional. Asserts the current state of the memory being updated. When an update changes `path`, the precondition still refers to the memory's current content, not the destination path. Currently the only supported variant is `content_sha256`.

type: "content_sha256"





content_sha256: optional string



Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.
