---
title: "Memory Stores - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:33:15Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)

# Memory Stores

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create a Memory Store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/create)

POST/v1/memory_stores

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [List Memory Stores](https://platform.claude.com/docs/en/api/http/beta/memory_stores/list)

GET/v1/memory_stores

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Retrieve a Memory Store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/retrieve)

GET/v1/memory_stores/{memory_store_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Update a Memory Store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/update)

POST/v1/memory_stores/{memory_store_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Delete a Memory Store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/delete)

DELETE/v1/memory_stores/{memory_store_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Archive a Memory Store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/archive)

POST/v1/memory_stores/{memory_store_id}/archive

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### Models



BetaManagedAgentsDeletedMemoryStore object{ type: "memory_store_deleted", id }



Confirmation that a `memory_store` was deleted.

type: "memory_store_deleted"



id: string



ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.



BetaManagedAgentsMemoryStore object{ type: "memory_store", id, archived_at, 5 more }



A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

type: "memory_store"



id: string



The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.



archived_at: string or null



When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

See the [memory guide](../Other/managed-agents-memory.md#archive-a-store) to learn more about archiving.

formatdate-time



created_at: string



When the memory store was created, in RFC 3339.

formatdate-time

description: string



Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.



metadata: map\[string\]



Key-value pairs for your own use, such as the end user that the store belongs to.

A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

name: string



Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.



updated_at: string



When the memory store was last changed, in RFC 3339.

Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

formatdate-time

#### Memory Stores[Memories](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories)

##### [Create a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/create)

POST/v1/memory_stores/{memory_store_id}/memories

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [List Memories](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/list)

GET/v1/memory_stores/{memory_store_id}/memories

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Retrieve a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/retrieve)

GET/v1/memory_stores/{memory_store_id}/memories/{memory_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Update a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/update)

POST/v1/memory_stores/{memory_store_id}/memories/{memory_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Delete a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/delete)

DELETE/v1/memory_stores/{memory_store_id}/memories/{memory_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

#### Memory Stores[Memory Versions](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions)

##### [List Memory Versions](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Retrieve a Memory Version](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Redact a Memory Version](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).
