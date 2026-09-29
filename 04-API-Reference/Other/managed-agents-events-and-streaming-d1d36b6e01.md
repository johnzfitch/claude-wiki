---
title: "Session event stream - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/events-and-streaming"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:48Z"
tags: ["api"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fevents-and-streaming)

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

[Managed Agents](/docs/en/managed-agents/overview)Delegate work to your agent

# Session event stream

Copy page



Send events, stream responses, and interrupt or redirect your session mid-execution.

Copy page



[Managed Agents](/docs/en/managed-agents/overview)

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

managed-agents-2026-04-01

Communication with Claude Managed Agents is event-based. You send user events to the agent, and receive agent and session events back to track status.

## Event types

Events flow in two directions.

- **User events** and **system events** are what you send to the agent: `user.*` events start a session and steer it as it progresses; `system.message` appends system-level context that applies to the accompanying turn and all subsequent turns.
- **Session events**, **span events**, and **agent events** are sent to you for observability into your session state and agent progress. Stream connections that opt in also receive [event deltas](#event-deltas).

Session, span, agent, user, and system event type strings follow a `{domain}.{action}` naming convention. The stream-only delta preview events (`event_start`, `event_delta`) are the exception. See [Event types](/docs/en/managed-agents/reference#event-types) in the reference for the full catalog. [Webhook event types](/docs/en/managed-agents/webhooks#supported-event-types) are separate, and some of their names differ from the stream's (for example, `session.status_idled` rather than `session.status_idle`).

Every persisted event includes a `processed_at` timestamp set when the event finishes processing. On events you send, `processed_at` is null while the event is still queued behind earlier events. The exceptions are `user.define_outcome`, `user.custom_tool_result`, and `user.tool_result`, which are processed on receipt and echoed back with `processed_at` already populated.

## Integrating events

Sending events

Streaming events

Listing past events

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

The call returns as soon as the events are queued, and the interrupt's `processed_at` stays null until the agent applies it. A model response in progress stops immediately. The interrupt can take longer to apply while tool calls are running, and the session stays `running` until it does. The `user.interrupt` event then appears on the stream, and the interrupted turn ends with a `session.status_idle` event. Its `stop_reason` is `end_turn`, the same value as a turn that finishes on its own; there is no stop reason specific to interruption. The agent starts its next turn with the `user.message` you sent after the interrupt.

## Event deltas

By default, the agent's response text reaches the stream as buffered `agent.message` events, each emitted only after the model request that produced it finishes. Event deltas let you render that text incrementally, as a live preview, while the model is still generating it. A preview is not the response: previews are a best-effort display aid, and the buffered `agent.message` is always the authoritative record. A client that ignores previews still receives a complete, correct stream.

### Opt in to previews

Previews are opt-in per stream connection. Add the `event_deltas[]` query parameter to the stream you're reading, repeating it once for each event type you want previewed. Because `[]` is a shell glob pattern, quote the URL whenever you build the request in a shell; the examples percent-encode the brackets as `%5B%5D`, which also works. Both stream endpoints accept the parameter: the session-level stream at `GET /v1/sessions/{session_id}/events/stream`, and each [session thread](/docs/en/managed-agents/multiagent-orchestration)'s own stream at `GET /v1/sessions/{session_id}/threads/{thread_id}/stream`. The accepted values are `agent.message` and `agent.thinking`; any other value returns a 400 error, as does a request with more than 100 values. A subagent's previews appear on [that subagent's own thread stream](#preview-session-thread-events).

When a previewed event begins, the stream emits an `event_start` carrying the upcoming event's type and `id`:

```python
{
  "type": "event_start",
  "event": {
    "type": "agent.message",
    "id": "sevt_01abc..."
  }
}
```



For `agent.message`, the start is followed by `event_delta` events carrying incremental text. Each delta names the event it extends in `event_id` and the content block it extends in `delta.index`:

```python
{
  "type": "event_delta",
  "event_id": "sevt_01abc...",
  "delta": {
    "type": "content_delta",
    "index": 0,
    "content": {
      "type": "text",
      "text": "Here is the summary"
    }
  }
}
```



When an `agent.thinking` event is previewed, only the `event_start` is emitted. No `event_delta` events follow, and the buffered `agent.thinking` event that concludes the preview carries no thinking content; it is a progress signal, not a content carrier.

Unlike persisted events, `event_start` and `event_delta` have no `id` or `processed_at` of their own. The only identifier they carry is the `id` of the event they preview.



Event deltas use a different wire format from [Streaming messages](/docs/en/build-with-claude/streaming), and the difference is intentional. A previewed `agent.message` gets a single `event_start` followed only by `event_delta` events. There are no per-content-block start or stop events and no stop event for the previewed event itself. The delta type is `content_delta`, not `content_block_delta`. Accumulator code written for the Messages API does not carry over unchanged.

### Accumulate and reconcile

Every SDK that supports event deltas includes an accumulator helper that handles the `index` bookkeeping for you. The Go, Java, Ruby, and C# helpers also key the accumulating preview by the event's `id`; with the Python, TypeScript, and PHP helpers you keep that map yourself and fold each delta into the entry for its `id`. The manual pattern also works in every language when you need custom bookkeeping: apply it to the generated event types.

In the manual pattern, treat the preview as a scratch buffer and the buffered event as the record. Key the buffer by `(event_id, index)`. Reconcile per model request: a turn opens with a single `session.status_running` event, then on a turn that completes normally each model request produces, in order, `span.model_request_start`, `event_start`, the `event_delta` events, the buffered `agent.message`, and finally [`span.model_request_end`](/docs/en/managed-agents/reference#event-types) (in the Span events tab). On the wire, this is the previewed portion of that sequence, interleaved with the connection's other buffered events:

``` block
event_start     {"event": {"type": "agent.message", "id": "sevt_01abc..."}}
event_delta     {"event_id": "sevt_01abc...", "delta": {"type": "content_delta", "index": 0, "content": {"type": "text", "text": "..."}}}
...
agent.message   {"id": "sevt_01abc...", "content": [...]}
```



The `event_delta` line repeats once per text fragment. Process each event as it arrives:

1.  On `event_start`, note the announced `id`. The identifiers always line up: `event_start.event.id`, every `event_delta.event_id`, and the buffered `agent.message`'s `id` are the same value.
2.  On each `event_delta`, append `delta.content.text` to the entry at `(event_id, delta.index)` and render the running text. The first delta for an `index` creates that entry.
3.  When the buffered `agent.message` arrives, match it by `id`, discard the accumulated preview, and render the message's content instead.
4.  On `span.model_request_end`, close any preview that has not been reconciled by its buffered event. No more deltas are coming for it. If the turn errors or is interrupted, the buffered event might never arrive; `span.model_request_end` still does.

Guarantees the pattern relies on:

- Concatenating a preview's deltas in arrival order, keyed by `(event_id, index)`, gives a prefix of `content[index].text` in the buffered event (a prefix, not necessarily the whole text, because deltas might be shed under load).
- A connection emits at most one `event_start` per `event_id`, and the buffered event is the last thing that connection delivers for that `id`.

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
# Preview snapshots, keyed by event id. accumulate_managed_agents_event folds each
# event_start / event_delta into an agent.message snapshot; the buffered
# agent.message replaces it.
previews: dict[str, BetaManagedAgentsAgentMessageEvent] = {}

# Opt in to agent.message previews on this connection
with client.beta.sessions.events.stream(
    session.id, event_deltas=["agent.message"]
) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [{"type": "text", "text": "Describe the repo in one sentence."}],
            },
        ],
    )

    for event in stream:
        match event.type:
            case "event_start":
                snapshot = accumulate_managed_agents_event(None, event)
                if snapshot is not None:
                    previews[event.event.id] = snapshot
                print(f"event_start             {event.event.type} {event.event.id}")
            case "event_delta":
                preview = accumulate_managed_agents_event(previews.get(event.event_id), event)
                if preview is not None:
                    previews[event.event_id] = preview
                    text = "".join(block.text for block in preview.content)
                    print(f"event_delta             preview: {text!r}")
            case "agent.message":
                # The buffered event is the record: it replaces and closes the preview
                preview = accumulate_managed_agents_event(previews.pop(event.id, None), event)
                text = "".join(block.text for block in preview.content)
                print(f"agent.message           {event.id} {text!r}")
            case "span.model_request_end":
                # No more deltas are coming. Close any preview whose
                # buffered event never arrived.
                for event_id in previews:
                    print(f"span.model_request_end  closing preview for {event_id}")
                previews.clear()
            case "session.status_idle":
                break
```

### Preview session thread events

In a [multiagent](/docs/en/managed-agents/multiagent-orchestration) session, every session thread has its own event stream at `GET /v1/sessions/{session_id}/threads/{thread_id}/stream`, and it takes the same `event_deltas[]` parameter with the same values. Previews are thread-scoped by design: a connection previews only the thread it's reading. A child thread's previews are delivered on that child's own stream and are never cross-posted to the session-level stream, whose previews stay scoped to the primary thread. To watch a subagent's text as the model generates it, open that subagent's thread stream.

The thread stream's path is easy to get wrong: it is `/threads/{thread_id}/stream`, not `/events/stream` (which exists only at the session level), and there is no `/threads/{thread_id}/events/stream` endpoint.

The preview events themselves don't change. `event_start` and `event_delta` have the same shape on a thread stream as on the session-level stream, and the [accumulate and reconcile](#accumulate-and-reconcile) pattern applies as written. The one adjustment is bookkeeping: run one accumulator instance per stream connection.

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
# List the session's threads and pick a child: child threads carry a non-null
# parent_thread_id, and the primary thread's parent_thread_id is null.
child_thread = next(
    thread
    for thread in client.beta.sessions.threads.list(session.id)
    if thread.parent_thread_id is not None
)

# The child thread's stream takes the same event_deltas parameter as the
# session stream.
with client.beta.sessions.threads.events.stream(
    child_thread.id,
    session_id=session.id,
    event_deltas=["agent.message"],
) as stream:
    for event in stream:
        match event.type:
            case "event_delta":
                print(event.delta.content.text, end="")
            case "agent.message":
                # The buffered event is the authoritative record; render its content
                print()
                for block in event.content:
                    if block.type == "text":
                        print(block.text, end="")
                print()
            case "session.thread_status_idle":
                break
```

The read loop exits on [`session.thread_status_idle`](/docs/en/managed-agents/reference#event-types), the event emitted when the session thread's turn finishes and the thread goes idle.

### Limitations

Previews are tuned for responsiveness. Build against these constraints:

- **Best effort:** Under load, the server might shed deltas for an event. When it does, you receive a contiguous prefix of the text and then no further deltas for that event. The buffered `agent.message` still arrives complete. Never treat an accumulated preview as final.
- **No replay on reconnect:** Deltas are delivered only to the connection that opted in, while it is open. This applies to the session-level stream and to each session thread stream alike, and a connection opened after a model request started receives no deltas for that in-flight event. If the stream drops, follow the [reconnect procedure](#integrating-events) in the Streaming events tab: reopen the stream and list the event history. The history includes any buffered events emitted while you were disconnected, including the `agent.message` your preview was waiting for. There is no way to re-request missed deltas.
- **One thread, text only:** Previews cover assistant text on the thread the connection is reading. Tool use, tool results, MCP results, and activity on any other [session thread](/docs/en/managed-agents/multiagent-orchestration) are never previewed on that connection.
- **Start-only `agent.thinking`:** An `agent.thinking` preview emits only the `event_start` as a signal that a thinking block has started; no `event_delta` events follow it.
- **Never persisted:** `event_start` and `event_delta` exist only on the live stream. They do not appear in the session's event history (`GET /v1/sessions/{session_id}/events`) or in any session thread's event history.

### Troubleshoot previews

If the stream doesn't behave as you expect:

| You see                                                             | What it means                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A stream with buffered events but no `event_start` or `event_delta` | The connection you're reading didn't opt in (`event_deltas[]` applies per connection, not per session), or the turn never touched the thread you're streaming. Previews are thread-scoped, so list the session's threads (`GET /v1/sessions/{session_id}/threads`) to find which one ran. |
| A 404 on the stream URL                                             | The path or an ID is wrong, or the request carries no managed-agents beta header at all. The thread endpoints are beta-gated, so without the header they don't exist.                                                                                                                     |
| A 400 naming `event_deltas`                                         | Only `agent.message` and `agent.thinking` are accepted.                                                                                                                                                                                                                                   |

## Additional scenarios

### Handling custom tool calls

When the agent invokes a [custom tool](/docs/en/managed-agents/tools#custom-tools):

1.  The session emits an `agent.custom_tool_use` event containing the tool name and input.
2.  The session pauses with a `session.status_idle` event containing `stop_reason: requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array.
3.  Execute the tool in your system and send a `user.custom_tool_result` event for each, passing the event ID in the `custom_tool_use_id` parameter along with the result content.
4.  Once all blocking events are resolved, the session transitions back to `running`.

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
with client.beta.sessions.events.stream(session.id) as stream:
    for event in stream:
        if event.type == "session.status_idle" and (stop_reason := event.stop_reason):
            match stop_reason.type:
                case "requires_action":
                    for event_id in stop_reason.event_ids:
                        # Look up the custom tool use event and execute it
                        tool_event = events_by_id[event_id]
                        result = call_tool(tool_event.name, tool_event.input)

                        # Send the result back
                        client.beta.sessions.events.send(
                            session.id,
                            events=[
                                {
                                    "type": "user.custom_tool_result",
                                    "custom_tool_use_id": event_id,
                                    "content": [{"type": "text", "text": result}],
                                },
                            ],
                        )
                case "end_turn":
                    break
```

### Tool confirmation

A tool call waits for your confirmation under an `always_ask` [permission policy](/docs/en/managed-agents/permission-policies), or under `auto` when the server reaches no determination. When that happens:

1.  The session emits an `agent.tool_use` or `agent.mcp_tool_use` event.
2.  The session pauses with a `session.status_idle` event whose `stop_reason.type` is `requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array.
3.  Send a `user.tool_confirmation` event for each, passing the event ID in the `tool_use_id` parameter. Set `result` to `"allow"` or `"deny"`. Use `deny_message` to explain a denial.
4.  Once all blocking events are resolved, the session transitions back to `running`.

Each `agent.tool_use` and `agent.mcp_tool_use` event carries `evaluated_permission` (`allow`, `ask`, or `deny`), and only events whose `evaluated_permission` is `"ask"` wait for a confirmation. Most events also carry an `evaluation` object that records which policy produced that outcome, described under [See how each call was evaluated](/docs/en/managed-agents/permission-policies#see-how-each-call-was-evaluated). For example, a `bash` call paused under an `always_ask` policy appears on the stream as follows:

```python
{
  "type": "agent.tool_use",
  "id": "sevt_01def...",
  "name": "bash",
  "input": {
    "command": "pip install -r requirements.txt"
  },
  "evaluated_permission": "ask",
  "evaluation": {
    "type": "always_ask"
  },
  "processed_at": "2026-03-25T14:01:45Z"
}
```



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

### Resuming an idle session

Sessions persist between interactions. Conversation history is preserved unless the session is explicitly deleted. When a session goes idle, its sandbox is checkpointed, preserving the full sandbox state, including the filesystem, installed packages, and any files the agent created. This allows you to resume cleanly from inactivity.



While session history is persisted until deleted, sandbox state is only preserved for 30 days after the sandbox is created. Activity does not extend this window: after 30 days the sandbox state (files, installed tools, and so on) is unrecoverable, and a resumed session starts from a fresh sandbox. If your workflow depends on sandbox contents, have the agent write important artifacts to [outputs](/docs/en/managed-agents/define-outcomes#retrieving-deliverables) before the window ends.

To resume a session, send a `user.message` event to it as usual:

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

### Reaching a session budget

A session created with a [budget](/docs/en/managed-agents/budgets) pauses instead of overspending. When the session's tracked list cost reaches the cap, the platform pauses each thread before its next model request, and the session goes idle with a `stop_reason` of `budget_reached` rather than terminating. The request that carried the total past the cap runs to completion, so the `list_cost` reported by the `session.usage` snapshot can read [at or a fraction past the cap](/docs/en/managed-agents/budgets#when-a-session-reaches-its-budget). On the stream, the pause arrives as three events, in order:

1.  `session.thread_status_idle` with `stop_reason: budget_reached`, for each thread as it pauses.
2.  `session.usage`, a snapshot of the session's cumulative usage and tracked list cost.
3.  `session.status_idle` with `stop_reason: budget_reached`. The `session.usage` event always immediately precedes this idle.

A thread whose final request both crosses the cap and completes its turn reports `end_turn` on its own `session.thread_status_idle` event while the session still reports `budget_reached`; key on the session-level `stop_reason` to detect the pause.

While the session is at its cap, it accepts only the events that settle work already in flight: `user.tool_confirmation`, `user.tool_result`, `user.custom_tool_result`, and `user.interrupt`. Any event that would start new work, including `user.message`, is rejected with a 400 error naming that list. When a session has both a thread waiting on a tool ask and a thread paused at the cap, the session-level `stop_reason` is `requires_action`, not `budget_reached`: settling the ask doesn't trigger a model request, so respond to it as usual.

No event resumes a session paused at its cap. Instead, update the session's budget: changing the cap to any value above the consumed list cost, or removing the budget by updating the session with `"budget": null`, resumes the paused work automatically. See [Session budgets](/docs/en/managed-agents/budgets) for how list cost is tracked and the full budget update semantics.

### Sending system messages



`system.message` is supported by Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, Claude Mythos 5, Claude Opus 5.5, Claude Opus 5, and Claude Opus 4.8. If the agent's primary model does not support mid-conversation system injection, the event is rejected with a `model_does_not_support_mid_conversation_system` validation error. Subagent models are not checked, because `system.message` lands on the primary thread only.

Send a `system.message` event to give the agent privileged system-level context that applies to the accompanying turn and all subsequent turns. Unlike the `system` field on the agent definition (which sets the top-level system prompt), `system.message` content is appended to the session's system context as a `role: "system"` turn rather than replacing that prompt. Use it when the agent needs updated system-level guidance mid-session: a different persona, revised constraints, or context fetched at runtime that should shape the model's behavior going forward.

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

While the session is idle with `stop_reason: requires_action`, a `system.message` is accepted only when it trails a tool result event in the same request; sent on its own or with a `user.message`, it is rejected until the pending tool events are resolved. `content` accepts 1–1000 text items.

### Tracking usage

The session object includes a `usage` field with the session's cumulative usage: token counts, server tool use, active time, and the tracked list cost. Fetch the session after it goes idle to read the latest totals.

```python
{
  "id": "sesn_01...",
  "status": "idle",
  "usage": {
    "input_tokens": 5000,
    "output_tokens": 3200,
    "cache_read_input_tokens": 20000,
    "cache_creation": {
      "ephemeral_5m_input_tokens": 2000,
      "ephemeral_1h_input_tokens": 0
    },
    "list_cost": {
      "amount": "187",
      "currency": "USD"
    },
    "active_seconds": 342.5,
    "server_tool_use": {
      "web_search_requests": 3,
      "web_fetch_requests": 0
    }
  }
}
```



`input_tokens` reports uncached input tokens and `output_tokens` reports total output tokens across all model calls in the session. The `cache_read_input_tokens` field reports tokens read from the prompt cache, and the `cache_creation` object breaks down cache-creation tokens by cache lifetime (`ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`). Cache entries use a 5-minute TTL by default, so back-to-back turns within that window benefit from cache reads, which reduce per-token cost.

`list_cost` is the session's cumulative consumption priced at public list rates, as a whole number of cents in a string, with a currency code. `active_seconds` is the cumulative time during which the session had at least one thread running; overlapping activity from concurrent threads is counted once, unlike the `active_seconds` in the session's `stats` object, which sums each thread's own active time. This deduplicated figure is the duration the session's runtime cost is priced on. `server_tool_use` counts server-executed tool requests for pricing: web search requests are priced into list cost per request, and web fetch requests carry no per-request charge and aren't metered, so `web_fetch_requests` reads `0`. Each [session thread](/docs/en/managed-agents/multiagent-orchestration)'s own `usage` carries `list_cost` and `active_seconds` too. Per-thread figures are rounded independently and exclude the session's running-time cost, so they don't sum exactly to the session's `list_cost`; the session figure is the authoritative one.

You don't have to poll the session to observe these totals. The `session.usage` event carries the same cumulative snapshot (the `usage` object, plus the session's `budget`, which is `null` when the session has none) on the session stream and in the event history. It is emitted on idle transitions rather than on a timer: the session emits one immediately before it goes idle, whatever the stop reason, and one when a thread pauses at a [session budget](/docs/en/managed-agents/budgets). A stream reader therefore sees the final cost of a turn, or of the work that hit a budget, without an extra fetch.

To enforce a spend limit, set a [session budget](/docs/en/managed-agents/budgets) rather than polling usage and stopping the session yourself. The platform prices the session's consumption continuously and pauses each thread before its next model request once the session's list cost reaches the cap; see [Reaching a session budget](#reaching-a-session-budget) for what that looks like on the stream.

## Console observability

The Claude Console includes a session viewer for inspecting what an agent did without writing any code. In the Console sidebar, under **Managed Agents**, select **Sessions** to see every session in the workspace with its status, agent, token usage, cost, and creation time, then select a session to open it. The session viewer is only accessible to Developers and Admins. It shows:

- **Timeline minimap:** A zoomable overview of the session's activity over time, with one lane per thread in [multiagent](/docs/en/managed-agents/multiagent-orchestration) sessions. Select a lane to view that thread, or select a mark to jump to its event.
- **Transcript:** The conversation grouped by model request, including thinking, tool calls with their inputs and results, and message text as it streams. You can filter the events and copy or download them as JSON.
- **Inspector:** A resizable side panel with details about the session, in five tabs:
  - **Session** shows the session's details and metadata, its cumulative cost over time, and spend against the session's [budget](/docs/en/managed-agents/budgets) when one is set.
  - **Events** lists every raw event on the current thread in the order the server sent it; select an event to see its JSON. A message that streamed while the page was open also has a **Deltas** view of its [event deltas](#event-deltas).
  - **Tools** lists the tools the session's agents are configured with, along with call counts, failures, and median duration; select a tool to see its calls and jump to one in the transcript.
  - **Resources** lists mounted [files](/docs/en/managed-agents/files), [repositories](/docs/en/managed-agents/github), and [memory stores](/docs/en/managed-agents/memory) at their container paths, including the memories in each store and the changes this session made to them, plus files the agent wrote to `/mnt/session/outputs` and the [skills](/docs/en/managed-agents/skills) attached to the session's agents.
  - **Threads** lists every thread with its status, context size, and cost. Select a thread to view its details, such as the agent, model, context usage, and cost.

Append `?event={event_id}` to a session URL to open the session at a specific event.

With `ant beta:sessions connect`, you can open the same viewer from the `ant` CLI or follow the session in your terminal. See [Connect to a Managed Agents session from your terminal](/docs/en/cli-sdks-libraries/cli/sessions-connect).

## Debugging tips

- **Check session events:** Session errors are conveyed through the `session.error` event
- **Review tool results:** Tool execution failures often explain unexpected agent behavior
- **Track token usage:** Monitor token consumption to optimize prompts and reduce costs
- **Use system prompts:** Add logging instructions to the system prompt to make the agent explain its reasoning
- **Troubleshoot previews:** If a stream that opts in to event deltas doesn't behave as you expect, see [Troubleshoot previews](#troubleshoot-previews)
