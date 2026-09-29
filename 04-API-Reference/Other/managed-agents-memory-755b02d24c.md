---
title: "Using agent memory - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/memory"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:49Z"
tags: ["agents", "api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fmemory)





SearchCtrlK

First steps

[Overview](/docs/en/managed-agents/overview)[Quickstart](/docs/en/managed-agents/quickstart)[Build in Console](/docs/en/managed-agents/onboarding)[Migration](/docs/en/managed-agents/migration)

Define your agent

[Agent setup](/docs/en/managed-agents/agent-setup)[Tools](/docs/en/managed-agents/tools)[MCP connector](/docs/en/managed-agents/mcp-connector)[Permission policies](/docs/en/managed-agents/permission-policies)[Agent Skills](/docs/en/managed-agents/skills)

Configure agent environment

[Cloud environment setup](/docs/en/managed-agents/environments)[Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference)

[Self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes)

Delegate work to your agent

[Start a session](/docs/en/managed-agents/sessions)[Session operations](/docs/en/managed-agents/session-operations)[Session event stream](/docs/en/managed-agents/events-and-streaming)[Session budgets](/docs/en/managed-agents/budgets)[Subscribe to webhooks](/docs/en/managed-agents/webhooks)[Define outcomes](/docs/en/managed-agents/define-outcomes)[Authenticate with vaults](/docs/en/managed-agents/vaults)

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

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

[Console](/)

[Managed Agents](/docs/en/managed-agents/overview)Build persistent memory

# Using agent memory

Copy page



Give your agents persistent memory that survives across sessions using memory stores.

Copy page



Using agent memory

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

agent-memory-2026-07-22

Each Managed Agents session starts with a fresh context by default. When a session ends, any state the agent built up is gone. Memory stores let the agent carry information across sessions: user preferences, project conventions, prior mistakes, and domain context.



Don't combine `agent-memory-2026-07-22` with `managed-agents-2026-04-01` on a memory store request: sending both returns a `400` error. If your code sets beta headers explicitly, replace `managed-agents-2026-04-01` with `agent-memory-2026-07-22` on memory store calls rather than adding a second value. Session endpoints, including attaching a memory store to a session, still use `managed-agents-2026-04-01`.

`GET /v1/memory_stores/{memory_store_id}/memories` behaves the same under either header: results come back in a stable, server-defined order, and `path_prefix` and `depth` apply the same way.

## Overview

A **memory store** is a workspace-scoped collection of text documents optimized for Claude. When you attach a store to a session, it is mounted as a directory inside the session's sandbox. The agent reads and writes it with the same file tools it uses for the rest of the filesystem, and a note describing each mount is automatically added to the system prompt, telling the agent where to look. The [agent toolset](/docs/en/managed-agents/tools) is required for these interactions; make sure to enable it during [agent creation](/docs/en/managed-agents/agent-setup). On [self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes#use-memory-stores), that directory is not a live mount. Instead, the SDK's environment worker downloads each attached store into your sandbox before the agent's tools run and keeps that copy in sync with the store.

Each **memory** in a store is addressed by a path and can be read and edited directly through the API or the Claude Console, allowing for tuning, importing, and exporting.

Every change to a memory creates an immutable **memory version**, giving you an audit trail and point-in-time recovery for everything the agent writes.

## Create a memory store

Give the store a `name` and a `description`. The description is passed to the agent, telling it what the store contains.

cURL

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
ant apply memory_store.yaml
```

memory_store.yaml





```python
# yaml-language-server: $schema=https://platform.claude.com/schemas/ant/beta/memory_store.json
name: User Preferences
description: Per-user preferences and project context.
```

The memory store `id` (`memstore_...`) is what you pass when attaching the store to a session.

### Seed it with content (optional)

Pre-load a store with reference material before any agent runs:

cURL

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
client.beta.memory_stores.memories.create(
    store.id,
    path="/formatting_standards.md",
    content="All reports use GAAP formatting. Dates are ISO-8601...",
)
```



Individual memories within the store are capped at 100 kB (~25k tokens). A store holds a maximum of 10,000 memories. Structure memory as many small focused files, not a few large ones.

## Attach a memory store to a session

Memory stores are attached in the session's `resources[]` array when the [session is created](/docs/en/managed-agents/sessions#creating-a-session). Unlike file resources, memory stores can only be attached at session creation time; adding or removing one from a running session is not supported. You attach memory stores the same way for sessions on cloud and [self-hosted environments](/docs/en/managed-agents/self-hosted-sandboxes#use-memory-stores); self-hosted environments accept only `memory_store` resources.

Optionally include `instructions` to provide session-specific guidance for how the agent should use this store. It is shown to the agent alongside the store's `name` and `description`, and is capped at 4,096 characters.

You can configure `access` as well. It defaults to `read_write` (shown explicitly in the following example), but `read_only` is also supported.

cURL

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
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
        {
            "type": "memory_store",
            "memory_store_id": store.id,
            "access": "read_write",
            "instructions": "User preferences and project context. Check before starting any task.",
        }
    ],
)
```



Memory stores attach with `read_write` access by default. If the agent processes untrusted input (user-supplied prompts, fetched web content, or third-party tool output), a successful prompt injection could write malicious content into the store. Later sessions then read that content as trusted memory. Use `read_only` for reference material, shared lookups, and any store the agent does not need to modify.

A maximum of **8 memory stores** are supported per session. Attach multiple stores when different parts of memory have different owners or access rules. Common reasons:

- **Shared reference material:** one read-only store attached to many sessions (standards, conventions, domain knowledge), kept separate from each session's own read-write store.
- **Mapping to your product's structure:** one store per end user, per team, or per project, while sharing a single agent configuration.
- **Different lifecycles:** a store that outlives any single session, or one you want to archive on its own schedule.

### How the agent accesses memory

Each attached store is mounted inside the session's sandbox as a directory under `/mnt/memory/`. The directory name is the store's display name sanitized to a filesystem-safe slug (lowercased; non-alphanumeric runs become a single hyphen), so a store named "Demo Memory" mounts at `/mnt/memory/demo-memory/`. The exact path is returned in the `mount_path` field on the session's memory-store resource; read it from there rather than constructing it yourself. The agent reads and writes the store with the standard [agent toolset](/docs/en/managed-agents/tools). Writes under the mount path are persisted back to the store and stay in sync across sessions that share it; writes to any other path under `/mnt/memory/` fail, because the sandbox mounts that parent directory read-only. A short description of each mount (display name, mount path, access mode, store `description`, and any `instructions`) is automatically added to the system prompt.

`access` is enforced at the filesystem level: a `read_only` mount rejects writes, while writes to a `read_write` mount produce [memory versions](#audit-memory-changes) attributed to the session.



On [self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes#use-memory-stores), each store's directory is a local copy that the SDK worker manages rather than a live mount. The worker reconciles each copy with its store after tool calls, at most once per sync interval (15 seconds by default), and once more when the session ends. The agent's `write` and `edit` tools change only the local copy; the worker uploads those changes at its next sync, so another session running on a self-hosted sandbox sees a change only after both workers have synced. Paths under `/mnt/memory/` outside the store directories are not scratch space there: the worker's file tools refuse to write to them, and anything a shell command writes there is never synced to a store.

For a `read_only` store, the worker's `write` and `edit` tools refuse changes under that directory and the worker never uploads anything from it. To learn how the worker resolves write conflicts, and what the `bash` tool can still change in a read-only store's local copy, see [Read-only stores and conflicts](/docs/en/managed-agents/self-hosted-sandboxes#read-only-stores-and-conflicts).

The agent's reads and writes appear in the [event stream](/docs/en/managed-agents/events-and-streaming) as ordinary `agent.tool_use` and `agent.tool_result` events for whichever tool touched the mount.

## View and edit memories

Memory stores can be managed directly through the API. Use this for building review workflows, correcting bad memories, or seeding stores before any session runs.

### List memories

List the memories in a store. Results are returned in a stable, server-defined order.

- `path_prefix` scopes the list to one directory. It must end with `/` and matches whole path segments, so `path_prefix=/notes/` returns `/notes/todo.md` but not `/notes-archive/todo.md`.
- `depth` controls how deep the listing goes below `path_prefix`: omit it (or pass `0`) to list the whole subtree, or pass `1` to list only the immediate children. Other values return a `400` error.

cURL

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
page = client.beta.memory_stores.memories.list(
    store.id,
    path_prefix="/",
)
for item in page.data:
    print(item.type, item.path)
```

See the [List memories reference](/docs/en/api/beta/memory_stores/memories/list) for full parameters and response schema.

### Read a memory

Fetching an individual memory returns the full content.

cURL

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
retrieved = client.beta.memory_stores.memories.retrieve(
    mem.id,
    memory_store_id=store.id,
)
print(retrieved.content)
```

See the [Retrieve a memory reference](/docs/en/api/beta/memory_stores/memories/retrieve) for full parameters and response schema.

### Create a memory

`memories.create` creates a memory at a given `path`. Create does not overwrite; to change an existing memory, use [`memories.update`](#update-a-memory).

cURL

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
mem = client.beta.memory_stores.memories.create(
    store.id,
    path="/preferences/formatting.md",
    content="Always use tabs, not spaces.",
)
```

See the [Create a memory reference](/docs/en/api/beta/memory_stores/memories/create) for full parameters and response schema.

### Update a memory

`memories.update` modifies an existing memory by ID. You can change `content`, `path` (a rename), or both. The example renames a memory to an archive path:

cURL

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
client.beta.memory_stores.memories.update(
    mem.id,
    memory_store_id=store.id,
    path="/archive/2026_q1_formatting.md",
)
```

See the [Update a memory reference](/docs/en/api/beta/memory_stores/memories/update) for full parameters and response schema.

#### Safe content edits (optimistic concurrency)

To avoid clobbering a concurrent write, pass a `content_sha256` precondition. The update only applies if the stored content hash still matches the one you read; on mismatch, re-read the memory and retry against the fresh state.

cURL

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
client.beta.memory_stores.memories.update(
    memory_id=mem.id,
    memory_store_id=store.id,
    content="CORRECTED: Always use 2-space indentation.",
    precondition={"type": "content_sha256", "content_sha256": mem.content_sha256},
)
```

### Delete a memory

cURL

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
client.beta.memory_stores.memories.delete(
    mem.id,
    memory_store_id=store.id,
)
```

See the [Delete a memory reference](/docs/en/api/beta/memory_stores/memories/delete) for full parameters and response schema.

## Audit memory changes

Every mutation to a memory creates an immutable **memory version** (`memver_...`). Use the version endpoints to audit who changed what and when, to inspect or restore a prior snapshot, and to scrub sensitive content out of history with redact.

Versions belong to the store (not the individual memory) and are not deleted when the memory itself is deleted, so the audit trail also covers deleted memories, subject to the retention described below. Versions are retained for 30 days after they are written; however, the recent versions of a live memory are always kept regardless of age, so memories that change infrequently might retain history beyond 30 days. The live `memories.retrieve` call always returns the latest version; the version endpoints give you the retained history.

There is no dedicated restore endpoint; to roll back, retrieve the version you want and write its `content` back with `memories.update` (or `memories.create` if the parent memory has been deleted, provided the version you want is still retained).

Past memory versions might be deleted after 30 days. To preserve memory history for longer, export versions through the API.

### List versions

List version history for a store, newest first. The example filters to a single memory's history:

cURL

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
versions = client.beta.memory_stores.memory_versions.list(
    store.id,
    memory_id=mem.id,
)
for version in versions:
    print(f"{version.id}: {version.operation}")

version_id = versions.data[1].id
```

See the [List memory versions reference](/docs/en/api/beta/memory_stores/memory_versions/list) for full parameters and response schema.

### Retrieve a version

Fetching an individual version returns the same fields as the list response plus the full `content` body.

cURL

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
version = client.beta.memory_stores.memory_versions.retrieve(
    version_id,
    memory_store_id=store.id,
)
print(version.content)
```

See the [Retrieve a memory version reference](/docs/en/api/beta/memory_stores/memory_versions/retrieve) for full parameters and response schema.

### Redact a version

Redact scrubs content out of a historical version while preserving the audit trail (who did what, when). Use it for compliance workflows such as removing leaked secrets, PII, or user deletion requests.

A version that is the current head of a live memory cannot be redacted. Write a new version first (or delete the memory), then redact the old one.

cURL

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
client.beta.memory_stores.memory_versions.redact(
    version_id,
    memory_store_id=store.id,
)
```

See the [Redact a memory version reference](/docs/en/api/beta/memory_stores/memory_versions/redact) for full parameters and response schema.

## Manage memory stores

In addition to [`create`](/docs/en/api/beta/memory_stores/create), memory stores support [`retrieve`](/docs/en/api/beta/memory_stores/retrieve), [`update`](/docs/en/api/beta/memory_stores/update), [`list`](/docs/en/api/beta/memory_stores/list), [`archive`](/docs/en/api/beta/memory_stores/archive), and [`delete`](/docs/en/api/beta/memory_stores/delete).

### List stores

List stores in the workspace. Archived stores are excluded by default; pass `include_archived: true` to include them.

cURL

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
for memory_store in client.beta.memory_stores.list(include_archived=True):
    print(memory_store.id, memory_store.name, memory_store.archived_at)
```

See the [List memory stores reference](/docs/en/api/beta/memory_stores/list) for full parameters and response schema.

### Archive a store

Archiving makes a store read-only and prevents it from being attached to new sessions. Archiving is one-way; there is no unarchive.

cURL

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
client.beta.memory_stores.archive(store.id)
```

See the [Archive a memory store reference](/docs/en/api/beta/memory_stores/archive) for full parameters and response schema.

To permanently remove a store along with all of its memories and versions, use [`memory_stores.delete`](/docs/en/api/beta/memory_stores/delete).

## Best practices for memory management

When a store reaches its 10,000-memory limit, writes to new memories fail: both direct `memories.create` calls and the agent's file writes to unmapped paths. Existing memories remain readable and editable. The following practices help you stay well under the limit and recover gracefully if you reach it.

- **Use focused stores.** Rather than one large general-purpose store, use smaller purpose-built stores: one per user, one for shared domain knowledge, and one for project-specific context. Each store has its own 10,000-memory limit, so keeping stores scoped reduces the chance any single one fills up.

- **Condense or prune before the store fills up.** Delete stale or redundant memories with `memories.delete`. You can also run a [dreaming session](/docs/en/managed-agents/dreams), which consolidates fragmented content into a separate new output store rather than modifying the original. Switch your sessions over to that output store, then archive or delete the original.

- **Attach a new store when it makes sense.** If a store has grown beyond its useful scope, attach a fresh one for new content and attach the original with `read_only` access. The agent can read from both while only writing to the new one.

- **Limit write access where appropriate.** Sessions that only read shared reference material don't need `read_write`. Keeping write access scoped to sessions that actually add new memories makes it easier to track where growth is coming from.
