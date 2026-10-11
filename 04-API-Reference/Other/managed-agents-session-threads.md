---
title: "Session threads - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/session-threads"
category: "04-API-Reference/Other"
fetched_at: "2026-10-10T06:24:58Z"
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fsession-threads)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[Web tool restrictions](managed-agents-tools-web-restrictions.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Event deltas](managed-agents-event-deltas.md)[Inspect and track usage](managed-agents-session-observability.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Session threads](managed-agents-session-threads.md)[Workflow runs](managed-agents-workflow-runs.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

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

[Managed Agents](managed-agents-overview.md)Advanced orchestration

# Session threads

Copy page



List, interrupt, and archive the threads of a multiagent session, read their events, and handle tool permissions across them.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

In a [multiagent session](managed-agents-multiagent-orchestration.md), each agent works in its own **session thread**. This page covers how to list, interrupt, and archive threads, the events they send, and how tool permissions work across them. A [workflow run](managed-agents-workflow-runs.md) creates session threads too.

## Primary thread and session threads

The **session-level event stream** (`/v1/sessions/{session_id}/events/stream`) is considered the **primary thread**, containing a condensed view of all activity across all threads. You don't see the full activity from [subagents](managed-agents-multiagent-orchestration.md#delegate-to-subagents), but you do see the start and end of their work, and blocking events such as tool permission requests.

**Session threads** are where you drill into a specific agent's activity.

The session `status` is an aggregation of all agent activity; if at least one thread is `running`, then the overall session status is `running` as well. A [workflow run](managed-agents-workflow-runs.md) that's running can keep the session `running` too, even while none of its threads is working. When no thread is working and a thread waits on your client, the session is `idle`; see [Know when the work is done](managed-agents-workflow-runs.md#know-when-the-work-is-done).

A [session budget](managed-agents-budgets.md) is a single shared cap across all of a session's threads. As the cap is reached, threads pause independently, and each thread's cost is priced at the thread's own served model.



A session can have at most 25 child threads at a time. Idle threads count until you archive them, and the primary thread doesn't count. The primary thread's agent can call multiple copies of a single subagent, creating multiple threads associated with one `agent`. [Advisor](managed-agents-multiagent-orchestration.md#give-the-session-an-advisor) consultation threads are exempt from this limit. So are a [workflow run](managed-agents-workflow-runs.md)'s threads.

## List threads

List all threads associated with a session as follows:

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
for thread in client.beta.sessions.threads.list(session.id):
    agent = thread.agent
    label = agent.type if agent.type == "advisor" else agent.name
    print(f"[{label}] {thread.status}")
```

The full list includes the primary thread. `parent_thread_id` is `null` for the primary thread. Every other thread is a child thread. `workflow_run_id` is `null` except on [a run's threads](managed-agents-workflow-runs.md#a-runs-threads).

To list only threads that have certain statuses, add `statuses[]` to the request, and repeat it to give more than one status, as in `?statuses[]=running&statuses[]=idle`. Leave it out to return threads of every status.

## Interrupt a session thread

Send `user.interrupt` with `session_thread_id` to stop a specific thread. Omitting `session_thread_id` interrupts every non-archived thread in the session, including the primary. In a session with dynamic workflows, an interrupt ends no run, and one that names a run's thread stops nothing. An interrupt closes other child threads' pending tool calls, but don't rely on it to close a run thread's. See [Interrupt a session with runs open](managed-agents-workflow-runs.md#interrupt-a-session-with-runs-open).

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
client.beta.sessions.events.send(
    session.id,
    events=[{"type": "user.interrupt", "session_thread_id": thread.id}],
)
```

Against a subagent's thread blocked on `requires_action`, the interrupt closes each pending tool call with an error tool result ("Tool execution was interrupted before completion. Please retry.") and re-emits `session.thread_status_idle` with `stop_reason: end_turn` directly; the model is not sampled. Against a child thread that's idle with `end_turn` or `budget_reached`, the interrupt is a no-op. An interrupt that names a terminated thread returns a 400 error. An interrupted child doesn't send the primary thread's agent the report it sends when a turn ends. While that agent waits on the child, it doesn't start another turn until something else reaches it, such as a `user.message` or another thread's report.

## Archive a session thread

Optionally archive a session thread when it has completed its work. Archiving a thread frees its place under the 25-child-thread limit. The server archives a [workflow run](managed-agents-workflow-runs.md)'s threads itself. You don't need to archive them, and you can't while the run is open.

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
archived = client.beta.sessions.threads.archive(thread.id, session_id=session.id)
print(archived.status, archived.archived_at)
```

Archive only succeeds if the thread is `idle`. A thread parked on `requires_action` counts as idle and can be archived directly; only a running thread must be interrupted first:

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
client.beta.sessions.events.send(
    session.id,
    events=[{"type": "user.interrupt", "session_thread_id": thread.id}],
)
archived = client.beta.sessions.threads.archive(thread.id, session_id=session.id)
print(archived.status, archived.archived_at)
```

## Primary thread events

These events surface multiagent activity on the primary thread at `/v1/sessions/{session_id}/events/stream`. Message-direction events are named relative to the thread whose stream they appear on: `agent.thread_message_received` means a message arrived on this thread from another thread, and `agent.thread_message_sent` means this thread sent one. The task that the primary thread's agent delegates, for example, arrives on the child's own stream as an `agent.thread_message_received` event.

| Type                               | Description                                                                                                                                                                                |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `session.thread_created`           | A thread was created. Includes `session_thread_id` and `agent_name`.                                                                                                                       |
| `session.thread_status_running`    | A thread started activity.                                                                                                                                                                 |
| `session.thread_status_idle`       | The agent associated with the thread is awaiting input. Includes a `stop_reason` indicating why the agent stopped.                                                                         |
| `session.thread_status_terminated` | A thread terminated and accepts no further input, for example because it was archived or encountered an unrecoverable error. An advisor thread also terminates when its consultation ends. |
| `agent.thread_message_received`    | On the primary thread, a subagent sent the primary thread's agent a report or question. Includes `from_session_thread_id`, `from_agent_name`, and `content`.                               |
| `agent.thread_message_sent`        | On the primary thread, the primary thread's agent sent a subagent a task or follow-up message. Includes `to_session_thread_id`, `to_agent_name`, and `content`.                            |

Advisor consultations emit these same thread events under the reserved name `anthropic.advisor` (as `agent_name` on the thread lifecycle events and `from_agent_name` on the advice delivery); see [Give the session an advisor](managed-agents-multiagent-orchestration.md#give-the-session-an-advisor) for the sequence.

A [workflow run](managed-agents-workflow-runs.md)'s threads show on the primary stream as follows:

- **Lifecycle events:** Each run thread sends `session.thread_created`, with the run's `workflow_run_id`, and its `session.thread_status_running`, `session.thread_status_idle`, and `session.thread_status_terminated` events.
- **Message events:** A run thread's prompt, an `agent.thread_message_received` event, stays on its own stream.
- **Run events:** `workflow_run.*` events also arrive on this stream; see [Run events](managed-agents-workflow-runs.md#run-events).
- **Tool calls that wait on you:** A run thread's tool calls that need your client are cross-posted to this stream, as for any child thread. See [Tool permissions and custom tools](#tool-permissions-and-custom-tools).

## Session thread events

Critical events are proxied to the primary thread. However, you might still want to investigate a specific agent's reasoning and tool calls. To do so, stream or list the events from the associated session thread.

Each session thread has its own event stream at `/v1/sessions/{session_id}/threads/{thread_id}/stream`, and it accepts the same `event_deltas[]` parameter as the session-level stream, so you can preview a subagent's text as the model generates it. A connection previews only the thread it's reading: a child thread's previews never appear on the session-level stream, so to watch a subagent live, open its own thread stream. See [Preview session thread events](managed-agents-event-deltas.md#preview-session-thread-events) for opting in, accumulating, and reconciling previews.

In a workflow run, the server runs a workflow: a program that the primary thread's agent writes. On each of the run's threads, the first `agent.thread_message_received` is the prompt that the workflow wrote. Its `from_session_thread_id` is the primary thread's ID, and it has no `from_agent_name`. The API doesn't guarantee the prompt's text, so don't parse it. The thread's `session.thread_status_terminated` event, on the primary thread's stream, tells you the thread is done. No event records the result it returned to the workflow.

A thread's stream doesn't replay earlier events. Right after `session.thread_created`, the event list of a run's thread can be empty, because the server writes the thread's first event after it. So open the thread's stream first, then list the thread's events, and skip each streamed event whose `id` the list returned.

Stream session thread events

List session thread events

Stream session thread events

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
with client.beta.sessions.threads.events.stream(
    thread.id,
    session_id=session.id,
) as stream:
    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    if block.type == "text":
                        print(block.text, end="")
            case "session.thread_status_idle":
                break
```

List session thread events

List all past session thread events to pull a complete history.

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
for event in client.beta.sessions.threads.events.list(
    thread.id,
    session_id=session.id,
):
    print(f"[{event.type}] {event.processed_at}")
```

## Tool permissions and custom tools

If a subagent needs something from your client, such as [permission](managed-agents-events-and-streaming.md#tool-confirmation) to run a tool call or the [result of a custom tool](managed-agents-events-and-streaming.md#handling-custom-tool-calls), the event is cross-posted to the **primary thread** with `session_thread_id` identifying the originating session thread. A tool call needs your permission under `always_ask`, or under [`auto`](managed-agents-permission-policies.md#let-the-server-evaluate-each-call-with-auto) when the server reaches no determination.

```python
{
  "type": "session.thread_status_idle",
  "id": "sevt_01ABC...",
  "session_thread_id": "sthr_01DEF...",
  "agent_name": "code-reviewer",
  "stop_reason": {
    "type": "requires_action",
    "event_ids": ["sevt_01XYZ..."]
  }
}
```



Post `user.tool_confirmation` (with `tool_use_id`) or `user.custom_tool_result` (with `custom_tool_use_id`); the server routes the response to the correct thread automatically. The response can appear on the primary thread and on the subagent's thread with different `id` values. To match the two copies, compare `type` and `tool_use_id` (or `custom_tool_use_id`), not `id`.

The session goes `idle` only when no thread is `running`, so `session.status_idle` can arrive long after a subagent's call. You don't have to wait for it: send the `user.custom_tool_result` as soon as the cross-posted `agent.custom_tool_use` event arrives.

Under `auto`, your `user.message` events can lead the server to allow a call it would otherwise deny. Nothing in a subagent's thread counts as your intent. Your client posts no messages there, and the messages that the primary thread's agent sends the subagent don't count. When the server denies a call under `auto`, nothing is cross-posted: the event and the error tool result appear only on the subagent's own [thread stream](#session-thread-events), and the subagent keeps running.

The following example goes inside the event loop of the [tool confirmation handler](managed-agents-events-and-streaming.md#tool-confirmation). For each ID in `stop_reason.event_ids`, it sends a `user.tool_confirmation` that allows the call. The same pattern applies to `user.custom_tool_result`.

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
for event_id in stop.event_ids:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.tool_confirmation",
                "tool_use_id": event_id,
                "result": "allow",
            }
        ],
    )
```

The previous pattern answers the calls that an idle event lists. On the primary stream, a subagent's `session.thread_status_idle` event can arrive before the `agent.tool_use` or `agent.mcp_tool_use` events that its `stop_reason.event_ids` lists. A `user.tool_confirmation` for a call whose event hasn't arrived yet can return 400. To avoid that, answer each call whose [`evaluated_permission`](managed-agents-permission-policies.md#see-how-each-call-was-evaluated) is `ask` when its own event arrives on the primary stream.
