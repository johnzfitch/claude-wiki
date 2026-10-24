---
title: "Session event stream - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/events-and-streaming"
category: "04-API-Reference/Other"
fetched_at: "2026-10-20T06:40:24Z"
tags: ["agents", "api"]
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fevents-and-streaming)

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

[Managed Agents](managed-agents-overview.md)Delegate work to your agent

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Session event stream

Copy page



Send events, stream responses, and interrupt or redirect your session mid-execution.

Copy page



Communication with Claude Managed Agents is event-based. You open a stream to follow a session, send events to direct it, and answer it when it pauses for input.

## Event types

Events flow in two directions: you send events to the agent, and the session sends events back to you.

- **Events you send:** `user.*` events start a session and steer it as it progresses. [`system.message`](#send-system-messages) events append system-level context.
- **Events you receive:** Session events, span events, and agent events report the session's state and the agent's progress.

These event type strings follow a `{domain}.{action}` naming convention. See [Event types](managed-agents-reference.md#event-types) in the reference for the full catalog.

[Webhook event types](managed-agents-webhooks.md#supported-event-types) are separate, and some of their names differ from the stream's. For example, webhooks use `session.status_idled` rather than `session.status_idle`.

## Stream events

Stream events from the session to receive real-time updates as the agent works. A stream delivers only the events emitted after it opens, so open the stream before you send events to avoid a race condition.

cURL

CLI

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
# Open the stream first, then send the user message
with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [{"type": "text", "text": "Summarize the repo README"}],
            },
        ],
    )

    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    if block.type == "text":
                        print(block.text, end="")
            case "session.status_idle":
                break
            case "session.error":
                error_message = event.error.message if event.error else "unknown"
                print(f"\n[Error: {error_message}]")
                break
```

The session reports errors through the `session.error` event. See [Event types](managed-agents-reference.md#event-types) for its fields.

The agent's response text arrives as buffered `agent.message` events, each emitted only after the model request that produced it finishes. To render the text while the model is still generating it, see [Preview responses with event deltas](managed-agents-event-deltas.md).

### Reconnect without missing events

To reconnect to an existing session without missing events, combine a new stream with the event history:

1.  Open a new stream.
2.  [List the full event history](#list-past-events) to seed a set of seen event IDs.
3.  Tail the live stream, skipping any events already returned by the history list.

cURL

CLI

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
with client.beta.sessions.events.stream(session.id) as stream:
    # Stream is open and buffering. List history before tailing live.
    history = client.beta.sessions.events.list(session.id)
    seen_event_ids = {past_event.id for past_event in history}

    # Tail live events, skipping anything already seen
    for event in stream:
        if event.type == "event_start" or event.type == "event_delta":
            # Delta previews aren't enabled on this connection.
            continue
        if event.id in seen_event_ids:
            continue
        seen_event_ids.add(event.id)
        match event.type:
            case "agent.message":
                for block in event.content:
                    if block.type == "text":
                        print(block.text, end="")
            case "session.status_idle":
                break
```

## Send events

Send a `user.message` event to start or continue the agent's work:

cURL

CLI

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
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [
                {
                    "type": "text",
                    "text": "Analyze the performance of the sort function in utils.py",
                },
            ],
        },
    ],
)
```

Every event in the session's history includes a `processed_at` timestamp, set when the event finishes processing. On events you send, `processed_at` is `None` while the event is still queued behind earlier events. The exceptions are `user.define_outcome`, `user.custom_tool_result`, and `user.tool_result`, which are processed on receipt and echoed back with `processed_at` already populated.

## Respond when the session goes idle

A `session.status_idle` event means the agent has stopped and is waiting for input. Its `stop_reason.type` says why:

| `stop_reason.type` | Why the session stopped                                                                               | What to do                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `end_turn`         | The agent finished its turn, or [you interrupted it](#interrupt-the-agent).                           | [Send a `user.message`](#resume-an-idle-session) when you have more work for the agent.        |
| `requires_action`  | One or more tool calls need an answer from you, such as a custom tool call or a confirmation request. | [Answer each blocking tool call](#answer-tool-calls-that-pause-the-session).                   |
| `budget_reached`   | The session's tracked list cost reached its [budget](managed-agents-budgets.md).                | [Change or remove the budget](managed-agents-budgets.md#resume-a-session-at-its-budget). |

No event you send resumes a session paused at its budget. The work that the budget paused resumes automatically when you change the budget to a value above the consumed list cost, or remove it. When the work resumes, the session emits a `workflow_run.status_running` event for each [workflow run that the budget paused](managed-agents-workflow-runs.md#budgets-and-limits). A run that an interrupt paused stays paused; see [Resume a session at its budget](managed-agents-budgets.md#resume-a-session-at-its-budget). See [When a session reaches its budget](managed-agents-budgets.md#when-a-session-reaches-its-budget) for the events that mark the pause and the events the session still accepts.

## Answer tool calls that pause the session

A session pauses when the agent invokes a [custom tool](managed-agents-tools.md#custom-tools), and when a tool call needs your confirmation under a [permission policy](managed-agents-permission-policies.md). Both pauses follow the same sequence:

1.  The session emits the tool call as an `agent.custom_tool_use`, `agent.tool_use`, or `agent.mcp_tool_use` event.
2.  The session pauses with a `session.status_idle` event whose `stop_reason.type` is `requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array.
3.  For each blocking event ID, send a [`user.custom_tool_result`](#return-a-custom-tool-result) or a [`user.tool_confirmation`](#confirm-a-tool-call) event. A custom tool result doesn't have to wait for step 2.
4.  Once all blocking events are resolved, the session transitions back to `running`.

In a multiagent session, a subagent's blocking events are cross-posted to the primary thread. See [Tool permissions and custom tools](managed-agents-session-threads.md#tool-permissions-and-custom-tools).

### Return a custom tool result

The `agent.custom_tool_use` event contains the tool name and input. Run the tool in your system. Then send a `user.custom_tool_result` event, passing the event ID in the `custom_tool_use_id` parameter along with the result content.

You can send the result as soon as the `agent.custom_tool_use` event arrives, without waiting for `session.status_idle`. The session still emits `session.status_idle` with a `requires_action` stop reason for the call, and your client can ignore it. A second result for the same call is accepted and has no effect.

When you [reconnect](#reconnect-without-missing-events) to a paused session, `stop_reason.event_ids` on the latest `session.status_idle` event lists the calls to answer.

The following example answers each call as it arrives:

cURL

CLI

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
with client.beta.sessions.events.stream(session.id) as stream:
    for event in stream:
        match event.type:
            case "agent.custom_tool_use":
                # Execute the tool
                result = call_tool(event.name, event.input)

                # Send the result back
                client.beta.sessions.events.send(
                    session.id,
                    events=[
                        {
                            "type": "user.custom_tool_result",
                            "custom_tool_use_id": event.id,
                            "content": [{"type": "text", "text": result}],
                        },
                    ],
                )
            case "session.status_idle":
                if event.stop_reason and event.stop_reason.type == "end_turn":
                    break
```

If the agent has [workflow runs](managed-agents-workflow-runs.md) open, a custom tool call can arrive while the session stays `running`. The `requires_action` idle event arrives only when none of the [session's threads](managed-agents-session-threads.md) is working. Don't wait for it: answer each call when its `agent.custom_tool_use` event arrives. The sample in [Follow a run](managed-agents-workflow-runs.md#follow-a-run) shows how.

### Confirm a tool call

Send a `user.tool_confirmation` event, passing the event ID in the `tool_use_id` parameter. Set `result` to `"allow"` or `"deny"`. See [Respond to confirmation requests](managed-agents-permission-policies.md#respond-to-confirmation-requests) for which calls wait for a confirmation and how to explain a denial.

The following example approves every pending call:

cURL

CLI

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
with client.beta.sessions.events.stream(session.id) as stream:
    for event in stream:
        if event.type == "session.status_idle" and (stop_reason := event.stop_reason):
            match stop_reason.type:
                case "requires_action":
                    for event_id in stop_reason.event_ids:
                        # Approve the pending tool call
                        client.beta.sessions.events.send(
                            session.id,
                            events=[
                                {
                                    "type": "user.tool_confirmation",
                                    "tool_use_id": event_id,
                                    "result": "allow",
                                },
                            ],
                        )
                case "end_turn":
                    break
```

The previous example approves each call after the session goes idle. If the agent has [workflow runs](managed-agents-workflow-runs.md) open, a tool call can wait for your confirmation while the session stays `running`. Don't wait for the idle event: when an `agent.tool_use` or `agent.mcp_tool_use` event arrives whose [`evaluated_permission`](managed-agents-permission-policies.md#see-how-each-call-was-evaluated) is `ask`, answer it. The sample in [Follow a run](managed-agents-workflow-runs.md#follow-a-run) answers custom tool calls this way, and its introduction says how to add confirmations.

## Resume an idle session

Sessions persist between interactions. To resume a session, send a `user.message` event to it as usual:

cURL

CLI

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
# Resume a previously created session by sending it a new user.message event.
# In production, pass the stored ID of the session you want to resume.
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [
                {
                    "type": "text",
                    "text": "Now run the tests against the changes you made earlier.",
                },
            ],
        },
    ],
)
```

Conversation history is preserved unless the session is explicitly deleted. When a session goes idle, its sandbox is checkpointed. The checkpoint preserves the full sandbox state, including the filesystem, installed packages, and any files the agent created.



Sandbox state is preserved for only 30 days after the sandbox is created, and activity does not extend this window. After 30 days the sandbox state (files, installed tools, and so on) is unrecoverable, and a resumed session starts from a fresh sandbox. If your workflow depends on sandbox contents, have the agent write important artifacts to [outputs](managed-agents-define-outcomes.md#retrieving-deliverables) before the window ends.

## Interrupt the agent

Send a `user.interrupt` event to stop the agent mid-execution, then follow up with a `user.message` event to redirect it:

cURL

CLI

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
# Agent is currently analyzing a file...
# Interrupt with a new direction:
client.beta.sessions.events.send(
    session.id,
    events=[
        {"type": "user.interrupt"},
        {
            "type": "user.message",
            "content": [
                {
                    "type": "text",
                    "text": "Instead, focus on fixing the bug in line 42.",
                },
            ],
        },
    ],
)
```

The call returns as soon as the events are queued. The interrupt then takes effect in this order:

1.  The agent applies the interrupt. Until then, the interrupt's `processed_at` stays `None` and the session stays `running`. A model response in progress stops immediately, but the interrupt can take longer to apply while tool calls are running.
2.  The `user.interrupt` event appears on the stream, and the interrupted turn ends with a `session.status_idle` event.
3.  The agent starts its next turn with the `user.message` you sent after the interrupt.

The idle event's `stop_reason.type` is `end_turn`, the same value as a turn that finishes on its own. If workflow runs are open, the interrupt ends none of them. A run that's running can keep the session `running`, so the `session.status_idle` event in step 2 might not arrive. See [Interrupt a session with runs open](managed-agents-workflow-runs.md#interrupt-a-session-with-runs-open).

## List past events

Retrieve the full event history for a session:

cURL

CLI

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
events = client.beta.sessions.events.list(session.id)
for event in events.data:
    print(f"[{event.type}] {event.processed_at}")
```

Pass a `types` filter to return only specific event types:

cURL

CLI

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
events = client.beta.sessions.events.list(
    session.id,
    types=["agent.tool_use", "agent.tool_result"],
)
for event in events.data:
    print(f"[{event.type}] {event.processed_at}")
```

## Send system messages

On a [supported model](#supported-models), send a `system.message` event to give the agent privileged system-level context. The context applies to the accompanying turn and all subsequent turns. Use it when the agent needs updated system-level guidance mid-session, for example a different persona, revised constraints, or context fetched at runtime.

The event's `content` accepts 1–1000 text items. The content is appended to the session's system context as a `role: "system"` turn. It doesn't replace the top-level system prompt, which the `system` field on the agent definition sets.

cURL

CLI

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
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "system.message",
            "content": [
                {
                    "type": "text",
                    "text": "The user's current timezone is America/New_York.",
                },
            ],
        },
    ],
)
```

### Supported models

`system.message` is supported by these models:

- Claude Fable 5.1
- Claude Mythos 5.1
- Claude Fable 5
- Claude Mythos 5
- Claude Opus 5.5
- Claude Opus 5
- Claude Opus 4.8
- Claude Sonnet 5.5
- Claude Haiku 5.5

If the agent's primary model does not support mid-conversation system injection, the event is rejected with a `model_does_not_support_mid_conversation_system` validation error. Subagent models are not checked, because `system.message` lands on the primary thread only.

### System messages while a tool call is pending

While the session is idle with a `requires_action` stop reason, a `system.message` must trail a tool result event in the same request. Sent on its own or with a `user.message`, it is rejected until the pending tool events are resolved.

## Next steps



[Preview responses with event deltas](managed-agents-event-deltas.md)

Render the agent's response text while the model is still generating it.



[Inspect sessions and track usage](managed-agents-session-observability.md)

Inspect a session in the Claude Console and read its token usage and list cost.



[Subscribe to webhooks](managed-agents-webhooks.md)

Get notified when major events happen without polling.



[Event types](managed-agents-reference.md#event-types)

Look up every event type a session can send or receive.
