---
title: "Memory stores in self-hosted sandboxes - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory"
category: "04-API-Reference/Other"
fetched_at: "2026-10-19T06:28:05Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fself-hosted-sandboxes-memory)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[Web tool restrictions](managed-agents-tools-web-restrictions.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Choose an environment](managed-agents-choosing-an-environment.md)[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

[Overview and quickstart](managed-agents-self-hosted-sandboxes.md)[Deploy workers](managed-agents-self-hosted-sandboxes-workers.md)[Memory stores](managed-agents-self-hosted-sandboxes-memory.md)[Custom tools and MCP servers](managed-agents-self-hosted-sandboxes-custom-tools.md)[Monitor and troubleshoot](managed-agents-self-hosted-sandboxes-operations.md)[Worker reference](managed-agents-self-hosted-sandboxes-reference.md)[Security model](managed-agents-self-hosted-sandboxes-security.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Event deltas](managed-agents-event-deltas.md)[Inspect and track usage](managed-agents-session-observability.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Session threads](managed-agents-session-threads.md)[Workflow runs](managed-agents-workflow-runs.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

Security

[Secure your deployment](managed-agents-secure-deployment.md)[Review and monitor sessions](managed-agents-secure-deployment-monitoring.md)[Risks and boundaries](managed-agents-secure-deployment-risks.md)

Reference

[Managed Agents reference](managed-agents-reference.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)

[Console](playground.md)

[Managed Agents](managed-agents-overview.md)Self-hosted sandboxes

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Memory stores in self-hosted sandboxes

Copy page



Attach memory stores to Claude Managed Agents sessions that run in self-hosted sandboxes: prepare the host, configure sync, and handle read-only stores and conflicts.

Copy page



Sessions on a self-hosted environment attach [memory stores](managed-agents-memory.md) exactly as sessions on cloud environments do. List them in `resources` when you create the session, as shown in [Attach a memory store to a session](managed-agents-memory.md#attach-a-memory-store-to-a-session). A session accepts up to 8 memory stores.

The difference is who materializes the store. On a self-hosted environment your worker, rather than Anthropic's infrastructure, downloads each store into the sandbox and syncs the agent's changes back.

## Requirements

- **A worker that mounts memory stores:** Use `ant` CLI 1.33.0 or later, or `EnvironmentWorker` from the Python, TypeScript, or Go SDK.
- **A POSIX filesystem:** Windows hosts are not supported, because the worker requires `O_NOFOLLOW` when it opens memory files. A case-sensitive filesystem is recommended, so that memory paths that differ only in case do not collide.
- **A writable `/mnt/memory` directory:** See [Prepare the host](#prepare-the-host).
- **The work item's secret:** If your own code launches the worker, [forward the work item's secret](managed-agents-self-hosted-sandboxes-workers.md#forward-the-work-items-secret) to it.



Memory stores cannot be attached to sessions on self-hosted environments on [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md).

## Prepare the host

Before you start the worker, create the parent directory and make it writable by the user the worker runs as:

```python
sudo mkdir -p /mnt/memory && sudo chown "$USER" /mnt/memory
```



Do not create the per-store directories yourself. The worker creates each store's `mount_path` directory (for example, `/mnt/memory/user-preferences`) when a session starts and removes it when the session ends. If something already exists at that path, the worker refuses to start the session's work.

In the [sandbox-per-session pattern](managed-agents-self-hosted-sandboxes-workers.md#run-one-sandbox-per-session), the sandbox image needs a writable `/mnt/memory`. You don't need to bind-mount the memory directories to the host, because the worker uploads their contents to the store before the sandbox exits.

### Isolate sessions that share a store

Two sessions cannot mount the same store on one host at the same time, because both need the same path. If your sessions attach the same store, run one session per filesystem. Giving each session [its own sandbox](managed-agents-self-hosted-sandboxes-workers.md#run-one-sandbox-per-session) satisfies this rule.

## How the worker handles memory

When the worker claims a work item whose session has memory stores attached, it:

1.  **Downloads each store to its `mount_path`.** This is the same directory under `/mnt/memory/` that cloud sessions use, and the session's system prompt describes it to the agent. For example, a store named "User Preferences" lands at `/mnt/memory/user-preferences/`.
2.  **Opens those directories to the file tools.** The agent works on memories with the same file tools it uses in the working directory.
3.  **Reconciles changes after tool calls,** at most once per sync interval (15 seconds by default). Memories that changed in the store are written to disk, and files the agent changed are uploaded to the store.
4.  **Runs a final sync when the session ends.** It flushes any uploads still pending for up to 30 seconds, then removes the directories it created.

The memory store on Anthropic's side remains the source of truth. [Memory versions](managed-agents-memory.md#audit-memory-changes), redaction, and viewing or editing memories in the Console work as they do for cloud sessions. The agent's memory reads and writes appear in the [event stream](managed-agents-events-and-streaming.md) as ordinary tool events.

Because each worker syncs on an interval, a change written in one session becomes visible to another running session only after both have synced. That is typically well under a minute at the default interval. Sessions on cloud sandboxes see each other's changes almost immediately.

Each store directory contains a marker file named `.anthropic-memory-store` that ties the directory to its store. Leave it in place: the worker does not sync a directory whose marker is missing or altered.



A worker that is killed rather than stopped runs no teardown, so unsynced edits are lost and the store directories stay behind. See [Stop workers gracefully](managed-agents-self-hosted-sandboxes-operations.md#stop-workers-gracefully).

## Configure sync

Two `EnvironmentWorker` options control memory behavior. Set them wherever you construct the worker, including in a webhook handler. The `ant` CLI worker always uses the defaults.

### Sync interval

`memory_sync_interval` sets how often attached stores reconcile with the server while the session runs.

| Setting                | Value      |
|------------------------|------------|
| Default                | 15 seconds |
| Minimum                | 5 seconds  |
| Example (10 seconds)   | `10`       |
| Disable memory support | `None`     |

A shorter interval narrows the window in which another session sees stale memories, at the cost of more memory store requests.

Disable memory support only on workers whose sessions attach no memory stores. A disabled worker neither downloads nor syncs stores, so a session with stores attached runs without them even though its system prompt still describes them.

While memory support is enabled, a work item that arrives without a `secret` for a session with attached stores fails rather than running without memory. See [Memory stores fail to mount](managed-agents-self-hosted-sandboxes-operations.md#memory-stores-fail-to-mount).

### Deletions

`memory_sync_deletions` sets whether a file the agent deletes locally is also deleted from the store. Uploads and downloads are unaffected.

| Value                 | Behavior                                                                                                                                         |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `"enabled"` (default) | Deletes the memory from the store once a later sync confirms the file is still gone.                                                             |
| `"log_only"`          | Runs the same checks but only logs what it would have deleted. Use it to watch what your workers would delete before you trust the enabled mode. |
| `"disabled"`          | Never deletes from the store.                                                                                                                    |

For example, to sync every 10 seconds and only log the deletes the worker would have made:

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
worker = EnvironmentWorker(
    client,
    environment_id=environment_id,
    environment_key=environment_key,
    workdir="/workspace",
    memory_sync_interval=10,  # seconds
    memory_sync_deletions="log_only",
)
```

## Read-only stores and conflicts

For a store attached with `access: "read_only"`, the `write` and `edit` tools refuse to change files inside its directory. The worker never uploads anything from it.

Changes made through `bash`, or through a custom tool or MCP server you serve from the sandbox, are not blocked locally. They are never synced to the store, and the next remote change to that memory overwrites them. If the local copy itself must stay unchanged during the session:

- Disable the `bash` tool for that agent, and give it no custom tool that writes to the sandbox's filesystem.
- Do not mount the store path read-only. The worker itself must create the directory and write the downloaded memories into it.

Conflicts resolve in favor of the store. Suppose the agent changes a memory file that also changed in the store since the session last synced it. At the next sync, the worker keeps the store's version, overwrites the local file with it, and logs a warning. The `write` and `edit` tools themselves succeed and no error reaches the agent. If the agent's change still applies, it can re-read the file after the sync and make the change again.

## Troubleshooting

See [Memory stores fail to mount](managed-agents-self-hosted-sandboxes-operations.md#memory-stores-fail-to-mount) for the worker's log messages and their fixes.
