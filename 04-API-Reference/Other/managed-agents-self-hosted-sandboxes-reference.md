---
title: "Self-hosted worker reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference"
category: "04-API-Reference/Other"
fetched_at: "2026-10-03T06:31:37Z"
tags: ["api", "cli", "sdk"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fself-hosted-sandboxes-reference)

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

# Self-hosted worker reference

Copy page



Reference for self-hosted sandbox workers: ant CLI flags, environment variables, host requirements, filesystem paths, and SDK helper options.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

This page documents the pre-built workers that serve a `self_hosted` environment. For task-oriented guides, start with [Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md) and [Deploy self-hosted workers](managed-agents-self-hosted-sandboxes-workers.md).

## CLI commands and flags

| Command                | Description                                                                                                                                      |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `ant beta:worker poll` | Claims work items from the environment's queue and runs each session in process. With `--on-work`, calls your script for each work item instead. |
| `ant beta:worker run`  | Handles one claimed session and exits. Use it as the entrypoint of a per-session sandbox.                                                        |

| Flag                | Description                                                                                                                                                                   |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--environment-id`  | The environment to poll for work. Also reads from `ANTHROPIC_ENVIRONMENT_ID`.                                                                                                 |
| `--environment-key` | Authenticates the worker with this environment. Also reads from `ANTHROPIC_ENVIRONMENT_KEY`.                                                                                  |
| `--workdir`         | Directory where skills are downloaded and tools read and write files. Defaults to `.` (the current directory).                                                                |
| `--on-work`         | Script to call for each claimed work item instead of running tools in-process. Receives session details as environment variables and the work item as JSON on standard input. |
| `--max-idle`        | How long to wait after the session goes idle with an `end_turn` [stop reason](../Guides/build-with-claude-handling-stop-reasons.md) before shutting down. Defaults to `60s`.      |
| `--log-format`      | Log output format. Use `json` for structured log ingestion. Defaults to `text`.                                                                                               |

## Environment variables

| Variable                        | Description                                      | Set by                                                                                                                                                      |
|---------------------------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ANTHROPIC_ENVIRONMENT_ID`      | The environment whose queue the worker serves.   | You, on the worker host. The poller passes it to the `--on-work` script.                                                                                    |
| `ANTHROPIC_ENVIRONMENT_KEY`     | Authenticates the worker to its queue.           | You, on the worker host. The poller passes it to the `--on-work` script.                                                                                    |
| `ANTHROPIC_SESSION_ID`          | The session that a claimed work item represents. | The poller, for the `--on-work` script.                                                                                                                     |
| `ANTHROPIC_WORK_ID`             | The claimed work item.                           | The poller, for the `--on-work` script.                                                                                                                     |
| `ANTHROPIC_WORK_SECRET`         | The work item's per-session secret.              | You. The poller does not set it. See [Forward the work item's secret](managed-agents-self-hosted-sandboxes-workers.md#forward-the-work-items-secret). |
| `ANTHROPIC_BASE_URL`            | Overrides the default API endpoint. Optional.    | You, on the worker host.                                                                                                                                    |
| `ANTHROPIC_WEBHOOK_SIGNING_KEY` | Verifies incoming webhook payloads.              | You, on a webhook handler host.                                                                                                                             |

## Host requirements

| Worker             | Requirement                                                                                                              |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| All workers        | A Linux host with `/bin/bash` at that exact path. The worker's bash tool invokes it directly, without consulting `PATH`. |
| TypeScript SDK     | `unzip` and `tar` on the `PATH`, and Node.js 22 or later.                                                                |
| Python and Go SDKs | No additional binaries. These SDKs use their standard libraries for archive extraction.                                  |

[Memory stores](managed-agents-self-hosted-sandboxes-memory.md#requirements) add their own requirements.

## Sandbox filesystem

| Path                       | Contents                                                                                                                                                                                                                     |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/workspace`               | The system default working directory for tool execution and skill download. If you use a different working directory, update your agent's system prompt so Claude can locate the skill files.                                |
| `<workdir>/skills/<name>/` | The agent's downloaded skills.                                                                                                                                                                                               |
| `/mnt/memory/<store>/`     | One directory per attached memory store, at the store's `mount_path` (for example, `/mnt/memory/user-preferences/`). The worker creates these directories when it claims the session and removes them when the session ends. |

On self-hosted environments the session's system prompt omits the `/mnt/session/outputs` instruction used on Anthropic-managed sandboxes. Final deliverables land wherever the agent writes them in your sandbox filesystem, typically under the working directory.

Skills can include executables that the agent may run directly. The CLI and SDK workers preserve the executable permissions recorded in the skill bundle when they extract it. If you implement skills download manually, you are responsible for setting executable permissions.

## SDK helpers

The Python, TypeScript, and Go SDKs provide three helpers at different levels of control:

| Helper                                                              | What it does                                                                | Use it when                                                                                                        |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [`EnvironmentWorker`](#environment-worker)                          | Handles polling, setup, and execution end to end.                           | Most cases.                                                                                                        |
| [`work.poller()`](#work-poller)                                     | Polls the work queue and gives you each claimed session.                    | You determine what happens for each session, for example launching a sandbox rather than running tools in-process. |
| [`client.beta.sessions.events.tool_runner()`](#session-tool-runner) | Runs tool calls for a single session, given the session ID and a tool list. | You've already claimed the work and only need the execution layer.                                                 |

### EnvironmentWorker

| Method          | Description                                                                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `run()`         | Runs indefinitely, picking up sessions as they arrive.                                                                                                                                                      |
| `handle_item()` | Handles a single claimed work item and returns. Pass the work, session, and environment identifiers and the `work_secret` explicitly, or let it read the [`ANTHROPIC_*` variables](#environment-variables). |

| Option                  | Description                                                                                                                                                                 |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `tools`                 | A factory that receives the session's `AgentToolContext` and returns the tool list. Defaults to the standard agent toolset.                                                 |
| `memory_sync_interval`  | How often attached memory stores reconcile with the server while the session runs. See [Sync interval](managed-agents-self-hosted-sandboxes-memory.md#sync-interval). |
| `memory_sync_deletions` | Whether files the agent deletes locally are also deleted from the store. See [Deletions](managed-agents-self-hosted-sandboxes-memory.md#deletions).                   |

`EnvironmentWorker` manages the `AgentToolContext` and the toolset automatically. Pass a `tools` factory to customize the tool list:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
EnvironmentWorker(client, ..., tools=lambda env: [beta_bash_tool(env), my_custom_tool])
```

### Work poller

| Option                  | Description                                                                                                                                                                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `drain`                 | Whether to stop polling once the queue is empty rather than waiting for new work.                                                                                                                                                                |
| `block_ms`              | How long each poll waits for work to arrive before returning, in milliseconds. Must be between 1 and 999; the helper re-polls automatically. Pass `None` for a non-blocking check. Defaults to a 999 ms long-poll.                               |
| `reclaim_older_than_ms` | Re-claims work items that were claimed but never acknowledged within this many milliseconds.                                                                                                                                                     |
| `auto_stop`             | Whether to post a stop signal for each work item once your loop body finishes with it. Set it to `False` when whatever runs the work item posts the stop itself. `handle_item()` does, and so does a sandbox you launch that owns the stop call. |

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

`AgentToolContext` is the execution context for tool calls. It defines the working directory and path policy, and can download the session's skills.

| Option            | Description                                                                                                                 |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `allowed_roots`   | Directories, in addition to the working directory, that the file tools (`read`, `write`, `edit`, `glob`, `grep`) can reach. |
| `read_only_roots` | Directories under which `write` and `edit` refuse paths.                                                                    |

`EnvironmentWorker` adds the session's memory store directories to `allowed_roots` itself, and the directories of stores attached with `access: "read_only"` to `read_only_roots`.

The confinement is a guardrail for the file tools only, not a sandbox. It does not constrain `bash`.

`beta_agent_toolset_20260401(env)` takes an `AgentToolContext` and returns the standard tool implementations (`bash`, `read`, `write`, `edit`, `glob`, `grep`).
