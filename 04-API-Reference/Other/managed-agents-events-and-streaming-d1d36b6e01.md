---
title: "Session event stream - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/events-and-streaming"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:38Z"
tags: ["api"]
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

Session event stream

Managed Agents/Delegate work to your agent

# Session event stream




Send events, stream responses, and interrupt or redirect your session mid-execution.




Communication with Claude Managed Agents is event-based. You send user events to the agent, and receive agent and session events back to track status.



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](/docs/en/api/beta-headers#endpoint-specific-headers).




Event types

Events flow in two directions.

- **User events** and **system events** are what you send to the agent: `user.*` events kick off a session and steer it as it progresses; `system.message` appends system-level context that applies to the accompanying turn and all subsequent turns.
- **Session events**, **span events**, and **agent events** are sent to you for observability into your session state and agent progress. Stream connections that opt in also receive [event deltas](#event-deltas).

Session, span, agent, user, and system event type strings follow a `{domain}.{action}` naming convention. The stream-only delta preview events (`event_start`, `event_delta`) are the exception. See [Event types](/docs/en/managed-agents/reference#event-types) in the reference for the full catalog.

Every persisted event includes a `processed_at` timestamp set when the event finishes processing. On events you send, `processed_at` is null while the event is still queued behind earlier events. The exceptions are `user.define_outcome`, `user.custom_tool_result`, and `user.tool_result`, which are processed on receipt and echoed back with `processed_at` already populated.




Integrating events

Sending events

Sending events

Streaming events

Streaming events

Listing past events

Listing past events

Send a `user.message` event to start or continue the agent's work:

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

The agent acknowledges the interruption and switches to the new task. The interrupted turn ends with a `session.status_idle` event whose `stop_reason` is `end_turn`, the same value as a turn that finishes on its own; there is no stop reason specific to interruption.




Event deltas

By default, the agent's response text reaches the stream as buffered `agent.message` events, each emitted only after the model request that produced it finishes. Event deltas let you render that text incrementally, as a live preview, while the model is still generating it. A preview is not the response: previews are a best-effort display aid, and the buffered `agent.message` is always the authoritative record. A client that ignores previews still receives a complete, correct stream.




Opt in to previews

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



Event deltas use a different wire format from [Streaming messages](/docs/en/build-with-claude/streaming), and the difference is intentional. A previewed `agent.message` gets a single `event_start` followed only by `event_delta` events. There are no per-content-block start or stop events and no stop event for the previewed event itself. The delta type is `content_delta`, not `content_block_delta`. Accumulator code written for the Messages API does not carry over unchanged.




Accumulate and reconcile

Every SDK that supports event deltas includes an accumulator helper that keys the preview by the event's `id` and handles the `index` bookkeeping for you (event deltas are not currently available in the PHP SDK; see the PHP tabs that follow). The manual pattern also works in every language when you need custom bookkeeping: apply it to the generated event types.

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
4.  On `span.model_request_end`, close any preview that has not been reconciled by its buffered event. No more deltas are coming for it. If the turn errors or is interrupted, the buffered event may never arrive; `span.model_request_end` still does.

Guarantees the pattern relies on:

- Concatenating a preview's deltas in arrival order, keyed by `(event_id, index)`, gives a prefix of `content[index].text` in the buffered event (a prefix, not necessarily the whole text, because deltas may be shed under load).
- A connection emits at most one `event_start` per `event_id`, and the buffered event is the last thing that connection delivers for that `id`.

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




Preview session thread events

In a [multiagent](/docs/en/managed-agents/multiagent-orchestration) session, every session thread has its own event stream at `GET /v1/sessions/{session_id}/threads/{thread_id}/stream`, and it takes the same `event_deltas[]` parameter with the same values. Previews are thread-scoped by design: a connection previews only the thread it's reading. A child thread's previews are delivered on that child's own stream and are never cross-posted to the session-level stream, whose previews stay scoped to the primary thread. To watch a subagent's text as the model generates it, open that subagent's thread stream.

The thread stream's path is easy to get wrong: it is `/threads/{thread_id}/stream`, not `/events/stream` (which exists only at the session level), and there is no `/threads/{thread_id}/events/stream` endpoint.

The preview events themselves don't change. `event_start` and `event_delta` have the same shape on a thread stream as on the session-level stream, and the [accumulate and reconcile](#accumulate-and-reconcile) pattern applies as written. The one adjustment is bookkeeping: run one accumulator instance per stream connection.

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
# List the session's threads and pick a child: child threads carry a non-null
# parent_thread_id, and the primary thread's parent_thread_id is null.
THREAD_ID=$(
  curl --fail-with-body -sS \
    "https://api.anthropic.com/v1/sessions/$SESSION_ID/threads?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" |
    jq -er 'first(.data[] | select(.parent_thread_id != null)).id'
)

# The child thread's stream takes the same event_deltas[] parameter as the
# session stream. Percent-encode the brackets (%5B%5D) and quote the URL.
exec {stream}< <(
  curl --fail-with-body -sS -N \
    "https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/stream?beta=true&event_deltas%5B%5D=agent.message" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "accept: text/event-stream"
)

while IFS= read -r -u "$stream" event_line; do
  [[ $event_line == data:* ]] || continue
  event_json=${event_line#data: }
  case $(jq -r '.type' <<<"$event_json") in
    event_delta)
      jq -j '.delta.content.text' <<<"$event_json"
      ;;
    agent.message)
      # The buffered event is the authoritative record; render its content.
      printf '\n'
      jq -j '.content[] | select(.type == "text") | .text' <<<"$event_json"
      printf '\n'
      ;;
    session.thread_status_idle)
      break
      ;;
  esac
done
exec {stream}<&-
```

The read loop exits on [`session.thread_status_idle`](/docs/en/managed-agents/reference#event-types), the event emitted when the session thread's turn finishes and the thread goes idle.




Limitations

Previews are tuned for responsiveness. Build against these constraints:

- **Best effort:** Under load, the server may shed deltas for an event. When it does, you receive a contiguous prefix of the text and then no further deltas for that event. The buffered `agent.message` still arrives complete. Never treat an accumulated preview as final.
- **No replay on reconnect:** Deltas are delivered only to the connection that opted in, while it is open. This applies to the session-level stream and to each session thread stream alike, and a connection opened after a model request started receives no deltas for that in-flight event. If the stream drops, follow the [reconnect procedure](#integrating-events) in the Streaming events tab: reopen the stream and list the event history. The history includes any buffered events emitted while you were disconnected, including the `agent.message` your preview was waiting for. There is no way to re-request missed deltas.
- **One thread, text only:** Previews cover assistant text on the thread the connection is reading. Tool use, tool results, MCP results, and activity on any other [session thread](/docs/en/managed-agents/multiagent-orchestration) are never previewed on that connection.
- **Start-only `agent.thinking`:** An `agent.thinking` preview emits only the `event_start` as a signal that a thinking block has started; no `event_delta` events follow it.
- **Never persisted:** `event_start` and `event_delta` exist only on the live stream. They do not appear in the session's event history (`GET /v1/sessions/{session_id}/events`) or in any session thread's event history.




Troubleshoot previews

If the stream doesn't behave as you expect:

| You see                                                             | What it means                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A stream with buffered events but no `event_start` or `event_delta` | The connection you're reading didn't opt in (`event_deltas[]` applies per connection, not per session), or the turn never touched the thread you're streaming. Previews are thread-scoped, so list the session's threads (`GET /v1/sessions/{session_id}/threads`) to find which one ran. |
| A 404 on the stream URL                                             | The path or an ID is wrong, or the request carries no managed-agents beta header at all. The thread endpoints are beta-gated, so without the header they don't exist.                                                                                                                     |
| A 400 naming `event_deltas`                                         | Only `agent.message` and `agent.thinking` are accepted.                                                                                                                                                                                                                                   |




Additional scenarios




Handling custom tool calls

When the agent invokes a [custom tool](/docs/en/managed-agents/tools#custom-tools):

1.  The session emits an `agent.custom_tool_use` event containing the tool name and input.
2.  The session pauses with a `session.status_idle` event containing `stop_reason: requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array.
3.  Execute the tool in your system and send a `user.custom_tool_result` event for each, passing the event ID in the `custom_tool_use_id` parameter along with the result content.
4.  Once all blocking events are resolved, the session transitions back to `running`.

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




Tool confirmation

When a [permission policy](/docs/en/managed-agents/permission-policies) requires confirmation before a tool executes:

1.  The session emits an `agent.tool_use` or `agent.mcp_tool_use` event.
2.  The session pauses with a `session.status_idle` event containing `stop_reason: requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array.
3.  Send a `user.tool_confirmation` event for each, passing the event ID in the `tool_use_id` parameter. Set `result` to `"allow"` or `"deny"`. Use `deny_message` to explain a denial.
4.  Once all blocking events are resolved, the session transitions back to `running`.

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




Resuming an idle session

Sessions persist between interactions. Conversation history is preserved unless the session is explicitly deleted. When a session goes idle, its sandbox is checkpointed, preserving the full sandbox state, including the filesystem, installed packages, and any files the agent created. This allows you to resume cleanly from inactivity.



While session history is persisted until deleted, sandbox state is only preserved for 30 days after the sandbox is created. Activity does not extend this window: after 30 days the sandbox state (files, installed tools, and so on) is unrecoverable, and a resumed session starts from a fresh sandbox. If your workflow depends on sandbox contents, have the agent write important artifacts to [outputs](/docs/en/managed-agents/define-outcomes#retrieving-deliverables) before the window ends.

To resume a session, send a `user.message` event to it as usual:

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
# In production, pass the stored ID of the session you want to resume.
ant beta:sessions:events send --session-id "$SESSION_ID" <<'YAML'
events:
  - type: user.message
    content:
      - type: text
        text: Now run the tests against the changes you made earlier.
YAML
```




Sending system messages



`system.message` is currently supported by Claude Opus 4.8, Claude Fable 5, Claude Mythos 5, and Claude Opus 5. If the agent's primary model does not support mid-conversation system injection, the event is rejected with a `model_does_not_support_mid_conversation_system` validation error; subagent models are not checked, because `system.message` lands on the primary thread only.

Send a `system.message` event to give the agent privileged system-level context that applies to the accompanying turn and all subsequent turns. Unlike the `system` field on the agent definition (which sets the top-level system prompt), `system.message` content is appended to the session's system context as a `role: "system"` turn rather than replacing that prompt. Use it when the agent needs updated system-level guidance mid-session: a different persona, revised constraints, or context fetched at runtime that should shape the model's behavior going forward.

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
ant beta:sessions:events send --session-id "$SESSION_ID" <<'YAML'
events:
  - type: system.message
    content:
      - type: text
        text: "The user's current timezone is America/New_York."
YAML
```

While the session is idle with `stop_reason: requires_action`, a `system.message` is accepted only when it trails a tool result event in the same request; sent on its own or with a `user.message`, it is rejected until the pending tool events are resolved. `content` accepts 1–1000 text items.




Tracking usage

The session object includes a `usage` field with cumulative token statistics. Fetch the session after it goes idle to read the latest totals, and use them to track costs, enforce budgets, or monitor consumption.

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
    }
  }
}
```



`input_tokens` reports uncached input tokens and `output_tokens` reports total output tokens across all model calls in the session. The `cache_read_input_tokens` field reports tokens read from the prompt cache, and the `cache_creation` object breaks down cache-creation tokens by cache lifetime (`ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`). Cache entries use a 5-minute TTL by default, so back-to-back turns within that window benefit from cache reads, which reduce per-token cost.




Console observability

The Console provides a visual timeline view of your agent sessions. Navigate to the Claude Managed Agents section in the Console to see:

- **Session list:** All sessions with their status, creation time, and agent
- **Tracing view:** A chronological view of events (content, timestamps, token usage) within a session. Tracing views are only accessible to Developers and Admins.
- **Tool execution:** Details of each tool call and its result




Debugging tips

- **Check session events:** Session errors are conveyed through the `session.error` event
- **Review tool results:** Tool execution failures often explain unexpected agent behavior
- **Track token usage:** Monitor token consumption to optimize prompts and reduce costs
- **Use system prompts:** Add logging instructions to the system prompt to make the agent explain its reasoning
- **Troubleshoot previews:** If a stream that opts in to event deltas doesn't behave as you expect, see [Troubleshoot previews](#troubleshoot-previews)
