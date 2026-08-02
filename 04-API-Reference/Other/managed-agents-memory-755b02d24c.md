---
title: "Using agent memory - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/memory"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:39Z"
tags: ["agents", "api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


First steps

[Overview](/docs/en/managed-agents/overview)[Quickstart](/docs/en/managed-agents/quickstart)[Prototype in Console](/docs/en/managed-agents/onboarding)[Migration](/docs/en/managed-agents/migration)

Define your agent

[Agent setup](/docs/en/managed-agents/agent-setup)[Tools](/docs/en/managed-agents/tools)[MCP connector](/docs/en/managed-agents/mcp-connector)[Permission policies](/docs/en/managed-agents/permission-policies)[Agent Skills](/docs/en/managed-agents/skills)

Configure agent environment

[Cloud environment setup](/docs/en/managed-agents/environments)[Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference)

Self-hosted sandboxes

Delegate work to your agent

[Start a session](/docs/en/managed-agents/sessions)[Session operations](/docs/en/managed-agents/session-operations)[Session event stream](/docs/en/managed-agents/events-and-streaming)[Subscribe to webhooks](/docs/en/managed-agents/webhooks)[Define outcomes](/docs/en/managed-agents/define-outcomes)[Authenticate with vaults](/docs/en/managed-agents/vaults)

Manage agent context

[Access GitHub](/docs/en/managed-agents/github)[Attach and download files](/docs/en/managed-agents/files)

Build persistent memory

[Memory stores](/docs/en/managed-agents/memory)[Dreams](/docs/en/managed-agents/dreams)

Advanced orchestration

[Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration)[Scheduled deployments](/docs/en/managed-agents/scheduled-deployments)

Reference

[Managed Agents reference](/docs/en/managed-agents/reference)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

Images and vision

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)

MCP tunnels

Claude on cloud platforms

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

[](/login)




Managed Agents

Memory stores

Managed Agents/Build persistent memory

# Using agent memory




Give your agents persistent memory that survives across sessions using memory stores.




Each Managed Agents session starts with a fresh context by default. When a session ends, any state the agent built up is gone. Memory stores let the agent carry information across sessions: user preferences, project conventions, prior mistakes, and domain context.



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](/docs/en/api/beta-headers#endpoint-specific-headers).



Don't combine `agent-memory-2026-07-22` with `managed-agents-2026-04-01` on a memory store request: sending both returns a `400` error. If your code sets beta headers explicitly, replace `managed-agents-2026-04-01` with `agent-memory-2026-07-22` on memory store calls rather than adding a second value. Session endpoints, including attaching a memory store to a session, still use `managed-agents-2026-04-01`.

On July 22, 2026, the `managed-agents-2026-04-01` header adopts the same list behavior on `GET /v1/memory_stores/{memory_store_id}/memories`; sending `agent-memory-2026-07-22` opts you into that behavior now. Page cursors from requests made without the header aren't valid with it, so restart from the first page.




Overview

A **memory store** is a workspace-scoped collection of text documents optimized for Claude. When you attach a store to a session, it is mounted as a directory inside the session's sandbox. The agent reads and writes it with the same file tools it uses for the rest of the filesystem, and a note describing each mount is automatically added to the system prompt, telling the agent where to look. The [agent toolset](/docs/en/managed-agents/tools) is required for these interactions; make sure to enable it during [agent creation](/docs/en/managed-agents/agent-setup).

Each **memory** in a store is addressed by a path and can be read and edited directly through the API or Console, allowing for tuning, importing, and exporting.

Every change to a memory creates an immutable **memory version**, giving you an audit trail and point-in-time recovery for everything the agent writes.




Create a memory store

Give the store a `name` and a `description`. The description is passed to the agent, telling it what the store contains.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
store_id=$(ant beta:memory-stores create \
  --name "User Preferences" \
  --description "Per-user preferences and project context." \
  --transform id --raw-output)
```

The memory store `id` (`memstore_...`) is what you pass when attaching the store to a session.




Seed it with content (optional)

Pre-load a store with reference material before any agent runs:

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:memory-stores:memories create \
  --memory-store-id "$store_id" \
  --path "/formatting_standards.md" \
  --content "All reports use GAAP formatting. Dates are ISO-8601..." \
  > /dev/null
```



Individual memories within the store are capped at 100 kB (~25k tokens). A store holds a maximum of 2,000 memories. Structure memory as many small focused files, not a few large ones.




Attach a memory store to a session

Memory stores are attached in the session's `resources[]` array when the session is created. Unlike file and repository resources, memory stores can only be attached at session creation time; adding or removing one from a running session is not supported.

Optionally include `instructions` to provide session-specific guidance for how the agent should use this store. It is shown to the agent alongside the store's `name` and `description`, and is capped at 4,096 characters.

You can configure `access` as well. It defaults to `read_write` (shown explicitly in the following example), but `read_only` is also supported.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:sessions create <<YAML
agent: $agent_id
environment_id: $environment_id
resources:
  - type: memory_store
    memory_store_id: $store_id
    access: read_write
    instructions: User preferences and project context. Check before starting any task.
YAML
```



Memory stores attach with `read_write` access by default. If the agent processes untrusted input (user-supplied prompts, fetched web content, or third-party tool output), a successful prompt injection could write malicious content into the store. Later sessions then read that content as trusted memory. Use `read_only` for reference material, shared lookups, and any store the agent does not need to modify.

A maximum of **8 memory stores** are supported per session. Attach multiple stores when different parts of memory have different owners or access rules. Common reasons:

- **Shared reference material:** one read-only store attached to many sessions (standards, conventions, domain knowledge), kept separate from each session's own read-write store.
- **Mapping to your product's structure:** one store per end user, per team, or per project, while sharing a single agent configuration.
- **Different lifecycles:** a store that outlives any single session, or one you want to archive on its own schedule.




How the agent accesses memory

Each attached store is mounted inside the session's sandbox as a directory under `/mnt/memory/`. The directory name is the store's display name sanitized to a filesystem-safe slug (lowercased; non-alphanumeric runs become a single hyphen), so a store named "Demo Memory" mounts at `/mnt/memory/demo-memory/`. The exact path is returned in the `mount_path` field on the session's memory-store resource; read it from there rather than constructing it yourself. The agent reads and writes the store with the standard [agent toolset](/docs/en/managed-agents/tools). Writes under the mount path are persisted back to the store and stay in sync across sessions that share it; writes to any other path under `/mnt/memory/` land in container-local scratch and are lost when the session ends. A short description of each mount (display name, mount path, access mode, store `description`, and any `instructions`) is automatically added to the system prompt.

`access` is enforced at the filesystem level: a `read_only` mount rejects writes, while writes to a `read_write` mount produce [memory versions](#audit-memory-changes) attributed to the session.

The agent's reads and writes appear in the [event stream](/docs/en/managed-agents/events-and-streaming) as ordinary `agent.tool_use` and `agent.tool_result` events for whichever tool touched the mount.




View and edit memories

Memory stores can be managed directly through the API. Use this for building review workflows, correcting bad memories, or seeding stores before any session runs.




List memories

List the memories in a store. Results are returned in a stable, server-defined order.

- `path_prefix` scopes the list to one directory. It must end with `/` and matches whole path segments, so `path_prefix=/notes/` returns `/notes/todo.md` but not `/notes-archive/todo.md`.
- `depth` controls how deep the listing goes below `path_prefix`: omit it (or pass `0`) to list the whole subtree, or pass `1` to list only the immediate children. Other values return a `400` error.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:memory-stores:memories list \
  --memory-store-id "$store_id" \
  --path-prefix "/"
```

See the [List memories reference](/docs/en/api/beta/memory_stores/memories/list) for full parameters and response schema.




Read a memory

Fetching an individual memory returns the full content.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:memory-stores:memories retrieve \
  --memory-store-id "$store_id" \
  --memory-id "$mem_id"
```

See the [Retrieve a memory reference](/docs/en/api/beta/memory_stores/memories/retrieve) for full parameters and response schema.




Create a memory

`memories.create` creates a memory at a given `path`. Create does not overwrite; to change an existing memory, use [`memories.update`](#update-a-memory).

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
mem=$(ant beta:memory-stores:memories create \
  --memory-store-id "$store_id" \
  --path "/preferences/formatting.md" \
  --content "Always use tabs, not spaces." \
  --format json)
mem_id=$(jq -r '.id' <<< "$mem")
mem_sha=$(jq -r '.content_sha256' <<< "$mem")
```

See the [Create a memory reference](/docs/en/api/beta/memory_stores/memories/create) for full parameters and response schema.




Update a memory

`memories.update` modifies an existing memory by ID. You can change `content`, `path` (a rename), or both. The example renames a memory to an archive path:

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:memory-stores:memories update \
  --memory-store-id "$store_id" \
  --memory-id "$mem_id" \
  --path "/archive/2026_q1_formatting.md" \
  > /dev/null
```

See the [Update a memory reference](/docs/en/api/beta/memory_stores/memories/update) for full parameters and response schema.




Safe content edits (optimistic concurrency)

To avoid clobbering a concurrent write, pass a `content_sha256` precondition. The update only applies if the stored content hash still matches the one you read; on mismatch, re-read the memory and retry against the fresh state.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:memory-stores:memories update \
  --memory-store-id "$store_id" \
  --memory-id "$mem_id" \
  --content "CORRECTED: Always use 2-space indentation." \
  --precondition "{type: content_sha256, content_sha256: $mem_sha}" \
  > /dev/null
```




Delete a memory

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:memory-stores:memories delete \
  --memory-store-id "$store_id" \
  --memory-id "$mem_id" \
  > /dev/null
```

See the [Delete a memory reference](/docs/en/api/beta/memory_stores/memories/delete) for full parameters and response schema.




Audit memory changes

Every mutation to a memory creates an immutable **memory version** (`memver_...`). Use the version endpoints to audit who changed what and when, to inspect or restore a prior snapshot, and to scrub sensitive content out of history with redact.

Versions belong to the store (not the individual memory) and survive even after the memory itself is deleted, so the audit trail stays complete. Versions are retained for 30 days; however, the recent versions are always kept regardless of age, so memories that change infrequently might retain history beyond 30 days. The live `memories.retrieve` call always returns the latest version; the version endpoints give you the retained history.

There is no dedicated restore endpoint; to roll back, retrieve the version you want and write its `content` back with `memories.update` (or `memories.create` if the parent memory has been deleted, because versions outlive their parent).

Past memory versions might be deleted after 30 days. To preserve memory history for longer, export versions through the API.




List versions

List version history for a store, newest first. The example filters to a single memory's history:

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
versions=$(ant beta:memory-stores:memory-versions list \
  --memory-store-id "$store_id" \
  --memory-id "$mem_id" \
  --format json)
# `list --format json` emits one JSON object per item.
jq -r '"\(.id): \(.operation)"' <<< "$versions"
version_id=$(jq -rs '.[1].id' <<< "$versions")
```

See the [List memory versions reference](/docs/en/api/beta/memory_stores/memory_versions/list) for full parameters and response schema.




Retrieve a version

Fetching an individual version returns the same fields as the list response plus the full `content` body.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:memory-stores:memory-versions retrieve \
  --memory-store-id "$store_id" \
  --memory-version-id "$version_id"
```

See the [Retrieve a memory version reference](/docs/en/api/beta/memory_stores/memory_versions/retrieve) for full parameters and response schema.




Redact a version

Redact scrubs content out of a historical version while preserving the audit trail (who did what, when). Use it for compliance workflows such as removing leaked secrets, PII, or user deletion requests.

A version that is the current head of a live memory cannot be redacted. Write a new version first (or delete the memory), then redact the old one.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:memory-stores:memory-versions redact \
  --memory-store-id "$store_id" \
  --memory-version-id "$version_id"
```

See the [Redact a memory version reference](/docs/en/api/beta/memory_stores/memory_versions/redact) for full parameters and response schema.




Manage memory stores

In addition to [`create`](/docs/en/api/beta/memory_stores/create), memory stores support [`retrieve`](/docs/en/api/beta/memory_stores/retrieve), [`update`](/docs/en/api/beta/memory_stores/update), [`list`](/docs/en/api/beta/memory_stores/list), [`archive`](/docs/en/api/beta/memory_stores/archive), and [`delete`](/docs/en/api/beta/memory_stores/delete).




List stores

List stores in the workspace. Archived stores are excluded by default; pass `include_archived: true` to include them.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:memory-stores list --include-archived
```

See the [List memory stores reference](/docs/en/api/beta/memory_stores/list) for full parameters and response schema.




Archive a store

Archiving makes a store read-only and prevents it from being attached to new sessions. Archiving is one-way; there is no unarchive.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:memory-stores archive --memory-store-id "$store_id"
```

See the [Archive a memory store reference](/docs/en/api/beta/memory_stores/archive) for full parameters and response schema.

To permanently remove a store along with all of its memories and versions, use [`memory_stores.delete`](/docs/en/api/beta/memory_stores/delete).




Best practices for memory management

When a store reaches its 2,000-memory limit, writes to new memories fail: both direct `memories.create` calls and the agent's file writes to unmapped paths. Existing memories remain readable and editable. The following practices help you stay well under the limit and recover gracefully if you reach it.

- **Use focused stores.** Rather than one large general-purpose store, use smaller purpose-built stores: one per user, one for shared domain knowledge, and one for project-specific context. Each store has its own 2,000-memory limit, so keeping stores scoped reduces the chance any single one fills up.

- **Condense or prune before the store fills up.** Delete stale or redundant memories with `memories.delete`. You can also run a [dreaming session](/docs/en/managed-agents/dreams), which consolidates fragmented content into a separate new output store rather than modifying the original. Switch your sessions over to that output store, then archive or delete the original.

- **Attach a new store when it makes sense.** If a store has grown beyond its useful scope, attach a fresh one for new content and attach the original with `read_only` access. The agent can read from both while only writing to the new one.

- **Limit write access where appropriate.** Sessions that only read shared reference material don't need `read_write`. Keeping write access scoped to sessions that actually add new memories makes it easier to track where growth is coming from.
