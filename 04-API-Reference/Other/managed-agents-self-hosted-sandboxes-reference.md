---
title: "Self-hosted worker reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference"
category: "04-API-Reference/Other"
fetched_at: "2026-11-03T06:23:34Z"
tags: ["api", "cli", "sdk"]
---

# Self-hosted worker reference

Copy page



Reference for self-hosted sandbox workers: ant CLI flags, environment variables, host requirements, filesystem paths, and SDK helper options.

Copy page



[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Feature of  
[Managed Agents](managed-agents-overview.md)

[Cloud platforms](managed-agents-self-hosted-sandboxes.md#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableClaude Models on Google CloudAnthropic managedAvailable

[Beta header](managed-agents-self-hosted-sandboxes.md#feature-beta-headers)  
- `managed-agents-2026-04-01`
  

[Data handling](managed-agents-self-hosted-sandboxes.md#feature-data-handling)  
Not ZDR eligibleNot HIPAA eligible

This page documents the pre-built workers that serve a `self_hosted` environment. For task-oriented guides, start with [Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md) and [Deploy self-hosted workers](managed-agents-self-hosted-sandboxes-workers.md).

## CLI commands and flags

| Command | Description |
|----|----|
| `ant beta:worker poll` | Claims work items from the environment’s queue and runs each session in process. With `--on-work`, calls your script for each work item instead. |
| `ant beta:worker run` | Handles one claimed session and exits. Use it as the entrypoint of a per-session sandbox. |

| Flag | Description |
|----|----|
| `--environment-id` | The environment to poll for work. Also reads from `ANTHROPIC_ENVIRONMENT_ID`. |
| `--environment-key` | Authenticates the worker with this environment. Also reads from `ANTHROPIC_ENVIRONMENT_KEY`. |
| `--workdir` | Directory where skills are downloaded and tools read and write files. Defaults to `.` (the current directory). |
| `--on-work` | Script to call for each claimed work item instead of running tools in-process. Receives session details as environment variables and the work item as JSON on standard input. |
| `--max-idle` | How long the worker waits while a session is idle before `ant beta:worker run` exits or `ant beta:worker poll` moves on to the next work item. Idle time with a [`requires_action` stop reason](managed-agents-events-and-streaming.md#respond-when-the-session-goes-idle) does not count. Defaults to `60s`. Set it to `0` to turn off the timeout. With an `--on-work` script, `ant beta:worker poll` ignores this flag. Pass it instead to the `ant beta:worker run` command that your script starts. |
| `--log-format` | Log output format. Use `json` for structured log ingestion. Defaults to `text`. |

## Environment variables

| Variable | Description | Set by |
|----|----|----|
| `ANTHROPIC_ENVIRONMENT_ID` | The environment whose queue the worker serves. | You, on the worker host. The poller passes it to the `--on-work` script. |
| `ANTHROPIC_ENVIRONMENT_KEY` | Authenticates the worker to its queue. | You, on the worker host. The poller passes it to the `--on-work` script. |
| `ANTHROPIC_SESSION_ID` | The session that a claimed work item represents. | The poller, for the `--on-work` script. |
| `ANTHROPIC_WORK_ID` | The claimed work item. | The poller, for the `--on-work` script. |
| `ANTHROPIC_WORK_SECRET` | The work item’s per-session secret. | You. The poller does not set it. See [Forward the work item’s secret](managed-agents-self-hosted-sandboxes-workers.md#forward-the-work-items-secret). |
| `ANTHROPIC_BASE_URL` | Overrides the default API endpoint. Optional. | You, on the worker host. |
| `ANTHROPIC_WEBHOOK_SIGNING_KEY` | Verifies incoming webhook payloads. | You, on a webhook handler host. |

## Host requirements

| Worker | Requirement |
|----|----|
| All workers | A Linux or macOS host with `/bin/bash` at that exact path. The worker’s bash tool invokes it directly, without consulting `PATH`. On macOS, that is the system Bash 3.2. |
| TypeScript SDK | `unzip` and `tar` on the `PATH`, and Node.js 22 or later. |
| Python and Go SDKs | No additional binaries. These SDKs use their standard libraries for archive extraction. |

[Memory stores](managed-agents-self-hosted-sandboxes-memory.md#requirements) add their own requirements.

On macOS, the root volume is read-only, so `mkdir` can’t create `/workspace`. Set the worker’s working directory to one that you can write to, such as a `workspace` directory in your home directory. To use memory stores on macOS, first [prepare the macOS host](managed-agents-self-hosted-sandboxes-memory.md#prepare-a-macos-host).

## Sandbox filesystem

| Path | Contents |
|----|----|
| `/workspace` | The system default working directory for tool execution and skill download. If you use a different working directory, update your agent’s system prompt so Claude can locate the skill files. |
| `<workdir>/skills/<name>/` | The agent’s downloaded skills. |
| `/mnt/memory/<store>/` | One directory per attached memory store, at the store’s `mount_path` (for example, `/mnt/memory/user-preferences/`). The worker creates these directories when it claims the session and removes them when the session ends. |

On self-hosted environments the session’s system prompt omits the `/mnt/session/outputs` instruction used on Anthropic-managed sandboxes. Final deliverables land wherever the agent writes them in your sandbox filesystem, typically under the working directory.

Skills can include executables that the agent may run directly. The CLI and SDK workers preserve the executable permissions recorded in the skill bundle when they extract it. If you implement skills download manually, you are responsible for setting executable permissions.

## SDK helpers

The Python, TypeScript, and Go SDKs provide three helpers at different levels of control:

| Helper | What it does | Use it when |
|----|----|----|
| [`EnvironmentWorker`](#environment-worker) | Handles polling, setup, and execution end to end. | Most cases. |
| [`work.poller()`](#work-poller) | Polls the work queue and gives you each claimed session. | You determine what happens for each session, for example launching a sandbox rather than running tools in-process. |
| [`client.beta.sessions.events.tool_runner()`](#session-tool-runner) | Runs tool calls for a single session, given the session ID and a tool list. | You’ve already claimed the work and only need the execution layer. |

### EnvironmentWorker

| Method | Description |
|----|----|
| `run()` | Runs indefinitely, picking up sessions as they arrive. |
| `handle_item()` | Handles a single claimed work item and returns. Pass the work, session, and environment identifiers and the `work_secret` explicitly, or let it read the [`ANTHROPIC_*` variables](#environment-variables). |

| Option | Description |
|----|----|
| `tools` | A factory that receives the session’s `AgentToolContext` and returns the tool list. Defaults to the standard agent toolset. |
| `memory_sync_interval` | How often attached memory stores reconcile with the server while the session runs. See [Sync interval](managed-agents-self-hosted-sandboxes-memory.md#sync-interval). |
| `memory_sync_deletions` | Whether files the agent deletes locally are also deleted from the store. See [Deletions](managed-agents-self-hosted-sandboxes-memory.md#deletions). |

`EnvironmentWorker` manages the `AgentToolContext` and the toolset automatically. Pass a `tools` factory to customize the tool list:

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
EnvironmentWorker(client, ..., tools=lambda env: [beta_bash_tool(env), my_custom_tool])
```

### Work poller

| Option | Description |
|----|----|
| `drain` | Whether to stop polling once the queue is empty rather than waiting for new work. |
| `block_ms` | How long each poll waits for work to arrive before returning, in milliseconds. Must be between 1 and 999; the helper re-polls automatically. Pass `None` for a non-blocking check. Defaults to a 999ms long-poll. |
| `reclaim_older_than_ms` | Re-claims work items that were claimed but never acknowledged within this many milliseconds. |
| `auto_stop` | Whether to post a stop signal for each work item once your loop body finishes with it. Set it to `False` when whatever runs the work item posts the stop itself. `handle_item()` does, and so does a sandbox you launch that owns the stop call. |

For a complete example, see [Launch sandboxes from the SDK poller](managed-agents-self-hosted-sandboxes-workers.md#launch-sandboxes-from-the-sdk-poller).

### Session tool runner

`client.beta.sessions.events.tool_runner()` takes a tool list as `tools`. To build that list, set up `AgentToolContext` yourself and call `beta_agent_toolset_20260401(env)`:

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
from anthropic.lib.tools.agent_toolset import (
    AgentToolContext,
    beta_agent_toolset_20260401,
)

async with AgentToolContext(
    workdir="/workspace", client=client, session_id=work.data.id
) as env:
    # skills downloaded to /workspace/skills/<name>/
    tools = beta_agent_toolset_20260401(env)
```

### AgentToolContext and the agent toolset

`AgentToolContext` is the execution context for tool calls. It defines the working directory and path policy, and can download the session’s skills.

| Option | Description |
|----|----|
| `allowed_roots` | Directories, in addition to the working directory, that the file tools (`read`, `write`, `edit`, `glob`, `grep`) can reach. |
| `read_only_roots` | Directories under which `write` and `edit` refuse paths. |

`EnvironmentWorker` adds the session’s memory store directories to `allowed_roots` itself, and the directories of stores attached with `access: "read_only"` to `read_only_roots`.

The confinement is a guardrail for the file tools only, not a sandbox. It does not constrain `bash`.

`beta_agent_toolset_20260401(env)` takes an `AgentToolContext` and returns the standard tool implementations (`bash`, `read`, `write`, `edit`, `glob`, `grep`).
