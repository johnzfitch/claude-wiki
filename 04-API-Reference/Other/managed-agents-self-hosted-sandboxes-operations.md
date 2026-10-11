---
title: "Monitor and troubleshoot self-hosted workers - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations"
category: "04-API-Reference/Other"
fetched_at: "2026-10-03T06:31:36Z"
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fself-hosted-sandboxes-operations)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

[Overview and quickstart](managed-agents-self-hosted-sandboxes.md)[Deploy workers](managed-agents-self-hosted-sandboxes-workers.md)[Memory stores](managed-agents-self-hosted-sandboxes-memory.md)[Custom tools and MCP servers](managed-agents-self-hosted-sandboxes-custom-tools.md)[Monitor and troubleshoot](managed-agents-self-hosted-sandboxes-operations.md)[Worker reference](managed-agents-self-hosted-sandboxes-reference.md)[Security model](managed-agents-self-hosted-sandboxes-security.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

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

[Console](usage-limits.md)

[Managed Agents](managed-agents-overview.md)Self-hosted sandboxes

# Monitor and troubleshoot self-hosted workers

Copy page



Read queue depth, stop sessions and workers without losing work, and fix common self-hosted sandbox failures.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

The monitoring calls on this page run from your monitoring or operations tooling, authenticated with your Claude API key. The worker helpers handle the claim and keep-alive loop, so you don't call those endpoints directly.



These endpoints accept either your organization API key or the environment key. Call them from outside the worker host with your organization API key. Setting `ANTHROPIC_API_KEY` on the worker host exposes an organization-scoped credential to agent tool calls.

## Read queue depth

`client.beta.environments.work.stats()` returns the queue state for an environment:

| Field              | Meaning                                                                                                                                                         | Use it to                                                                                             |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `depth`            | Items waiting to be claimed.                                                                                                                                    | Scale your worker fleet or alert on backlog.                                                          |
| `pending`          | Items claimed by a worker but not yet acknowledged. The worker helpers acknowledge each item before processing it, so this stays near zero in normal operation. | Detect a worker that stalled between claiming and acknowledging: alert on a sustained non-zero value. |
| `oldest_queued_at` | Timestamp of the oldest item still in the queue, either waiting to be claimed or claimed but not yet acknowledged. `null` when there is none.                   | See how long the oldest item has waited.                                                              |
| `workers_polling`  | Workers that have polled in the last 30 seconds.                                                                                                                | Alert on liveness.                                                                                    |

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
import os

import anthropic

client = anthropic.Anthropic()

stats = client.beta.environments.work.stats(os.environ["ANTHROPIC_ENVIRONMENT_ID"])
print(f"depth={stats.depth} pending={stats.pending}")
```

``` block
{
  "type": "work_queue_stats",
  "depth": 0,
  "pending": 0,
  "oldest_queued_at": null,
  "workers_polling": 0
}
```



## Stop a session gracefully

Use `client.beta.environments.work.stop()` to ask the worker handling a specific session to shut it down.

By default the work item moves to `stopping`. The worker notices on its next lease heartbeat, cancels the session's in-flight tool call, and confirms the shutdown. The work item then becomes `stopped`.

Pass `force=True` to mark the work item `stopped` immediately instead of waiting for the worker's confirmation.

Because these calls run from your operations tooling rather than the worker host, `ANTHROPIC_WORK_ID` isn't set automatically. Set it to the target work item's ID before running the following examples. To find a work item's ID, list the environment's work items through the [Environments Work endpoints](../Endpoints/beta-environments-work.md).

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
import os

import anthropic

client = anthropic.Anthropic()

work = client.beta.environments.work.stop(
    os.environ["ANTHROPIC_WORK_ID"],
    environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
)
print(work.state)
```

## Stop workers gracefully

A worker that is cancelled while a session runs stops its in-flight work before it exits. If the session has [memory stores](managed-agents-self-hosted-sandboxes-memory.md) attached, the worker skips the final sync but still uploads changed files and removes the store directories.

A killed process runs no teardown. To stop a worker cleanly:

1.  **Make sure SIGTERM and SIGINT cancel the worker.** How depends on the worker:

    | Worker                             | What to do                                                                                                                             |
    |------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
    | `ant` CLI                          | Nothing. The CLI handles both signals itself: it cancels any in-flight tool call, posts its error result, and releases the work item.  |
    | SDK worker that is its own process | `EnvironmentWorker` installs no signal handlers. Cancel the worker from a signal handler, as the standalone worker examples do.        |
    | SDK worker inside a webhook server | Cancel the worker from the server's own shutdown hook, as the webhook examples do. The worker must not take over the server's signals. |

2.  **Stop the worker with SIGTERM, and allow at least 30 seconds before any hard kill.** The final upload can take that long. Docker sends SIGKILL 10 seconds after the stop signal by default. Raise that limit with `--stop-timeout` on `docker run`, or with your orchestrator's termination grace period.

If a worker is killed before its teardown runs, any memory edits that had not synced are lost. On a long-lived host, also remove the leftover store directory under `/mnt/memory/` before the next session that attaches that store. A sandbox that serves one session and is then discarded needs no cleanup.

## Troubleshooting

### The worker doesn't connect

If `workers_polling` stays at 0, the worker isn't reaching the queue. Confirm that `ANTHROPIC_ENVIRONMENT_KEY` and `ANTHROPIC_ENVIRONMENT_ID` are set on the worker host.

### A session stays queued

No worker is claiming work. A queued session waits rather than failing. Check `workers_polling` and `depth` in [Read queue depth](#read-queue-depth).

### Memory stores fail to mount

The worker logs mount and background sync failures rather than reporting them to the session. Only read-only refusals reach the agent, as tool errors (see [Read-only stores and conflicts](managed-agents-self-hosted-sandboxes-memory.md#read-only-stores-and-conflicts)).

If the worker cannot mount a memory store when it claims a session, it fails the work item. The session emits no error event and stays idle.

| Symptom                                                                                                                                 | Cause                                                                                                                                                                                | Fix                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The worker log contains `the work item carried no sessions token` (in Go, the `ErrSessionMemoryNoToken` error) and the work item fails. | The work item's per-session `secret` did not reach the worker. Either your code did not forward it, or memory stores on self-hosted sandboxes are not enabled for your organization. | [Forward the work item's secret](managed-agents-self-hosted-sandboxes-workers.md#forward-the-work-items-secret). If the worker polls and runs sessions in one process and still logs this, contact support.           |
| The worker log contains `something already exists at the memory store's path`.                                                          | A directory left over from a previous session, usually one whose worker was killed before its teardown ran.                                                                          | Remove the leftover directory that the log line names. Edits in it that had not synced are lost.                                                                                                                            |
| The worker log contains `cannot create the memory store's folder` and `the worker host must make this mount path writable`.             | The user the worker runs as cannot create directories under `/mnt/memory`.                                                                                                           | Create `/mnt/memory` and `chown` it to that user. See [Prepare the host](managed-agents-self-hosted-sandboxes-memory.md#prepare-the-host).                                                                            |
| The session sits `idle` with a `requires_action` stop reason and no error event shortly after a worker claimed it.                      | The worker failed the work item because it could not mount a memory store, for one of the preceding reasons.                                                                         | Fix the cause on the host, then send a [`user.interrupt`](managed-agents-events-and-streaming.md#integrating-events) event. The session's work is queued again, and the next worker that claims it retries the mount. |

### A custom tool call never returns

If the session sits paused with a `requires_action` stop reason, no worker or client serves that tool. See [Serve a custom tool](managed-agents-self-hosted-sandboxes-custom-tools.md#serve-a-custom-tool).

### A wrapped MCP tool call hangs

Without a timeout on the MCP client, a hung call to a [wrapped MCP server](managed-agents-self-hosted-sandboxes-custom-tools.md#wrap-an-mcp-server-as-custom-tools) becomes an error tool result only when a backstop fires:

| SDK        | Backstop                                                       | Fires after                  |
|------------|----------------------------------------------------------------|------------------------------|
| Python     | The worker's own tool call limit                               | About two and a half minutes |
| TypeScript | The MCP SDK's default request timeout                          | About a minute               |
| Go         | The worker cancels a tool call that outlives its default limit | 120 seconds                  |
