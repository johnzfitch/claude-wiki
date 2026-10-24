---
title: "Preview responses with event deltas - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/event-deltas"
category: "04-API-Reference/Other"
fetched_at: "2026-10-22T06:29:44Z"
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fevent-deltas)

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

# Preview responses with event deltas

Copy page



Render the agent's response text as a live preview while the model is still generating it.

Copy page



By default, the agent's response text reaches the [session event stream](managed-agents-events-and-streaming.md) as buffered `agent.message` events. Each one is emitted only after the model request that produced it completes. Event deltas let you render that text incrementally, as a live preview, while the model is still generating it.

Previews are a best-effort display aid, and the buffered `agent.message` is always the authoritative record. A client that ignores previews still receives a complete, correct stream.

## Opt in to previews

Previews are opt-in for each stream connection. Add the `event_deltas[]` query parameter to the stream you're reading, and repeat it once for each event type you want previewed. The accepted values are `agent.message` and `agent.thinking`. Any other value returns a 400 error, as does a request with more than 100 values.

Both stream endpoints accept the parameter:

- **Session-level stream:** `GET /v1/sessions/{session_id}/events/stream`
- **Session thread stream:** `GET /v1/sessions/{session_id}/threads/{thread_id}/stream`

A subagent's previews appear on [that subagent's own thread stream](#preview-session-thread-events).

`[]` is a shell glob pattern, so quote the URL whenever you build the request in a shell. The examples percent-encode the brackets as `%5B%5D`, which also works.

### Preview events

When a previewed event starts, the stream emits an `event_start` carrying the upcoming event's type and `id`:

``` block
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

``` block
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

For `agent.thinking`, only the `event_start` is emitted, as a signal that a thinking block has started. No `event_delta` events follow. The buffered `agent.thinking` event that concludes the preview is a progress signal and carries no thinking content.

Unlike persisted events, `event_start` and `event_delta` have no `id` or `processed_at` of their own. The only identifier they carry is the `id` of the event they preview. Their type strings are also the exception to the `{domain}.{action}` naming convention of persisted events.



Event deltas use a different wire format from [Streaming messages](../Guides/build-with-claude-streaming.md), and the difference is intentional. A previewed `agent.message` gets a single `event_start` followed only by `event_delta` events. There are no per-content-block start or stop events and no stop event for the previewed event itself. The delta type is `content_delta`, not `content_block_delta`. Accumulator code written for the Messages API does not carry over unchanged.

## Accumulate and reconcile

Every SDK that supports event deltas includes an [accumulator helper](#sdk-accumulator-helpers) that handles the `index` bookkeeping for you. The manual pattern in this section works in every language when you need custom bookkeeping. Apply it to the generated event types.

In the manual pattern, hold preview text in a temporary map keyed by `(event_id, index)`, and treat the buffered event as the record. Reconcile the two for each model request.

A turn opens with a single `session.status_running` event. On a turn that completes normally, each model request then produces these events, in order:

1.  `span.model_request_start`
2.  `event_start`
3.  The `event_delta` events
4.  The buffered `agent.message`
5.  [`span.model_request_end`](managed-agents-reference.md#event-types) (in the **Span events** tab)

On the wire, this is the previewed portion of that sequence, interleaved with the connection's other buffered events:

``` block
event_start     {"event": {"type": "agent.message", "id": "sevt_01abc..."}}
event_delta     {"event_id": "sevt_01abc...", "delta": {"type": "content_delta", "index": 0, "content": {"type": "text", "text": "..."}}}
...
agent.message   {"id": "sevt_01abc...", "content": [...]}
```



The `event_delta` line repeats once for each text fragment. Process each event as it arrives:

1.  On `event_start`, note the announced `id`. The identifiers always line up: `event_start.event.id`, every `event_delta.event_id`, and the buffered `agent.message`'s `id` are the same value.
2.  On each `event_delta`, append `delta.content.text` to the entry at `(event_id, delta.index)` and render the running text. The first delta for an `index` creates that entry.
3.  When the buffered `agent.message` arrives, match it by `id`, discard the accumulated preview, and render the message's content instead.
4.  On `span.model_request_end`, close any preview that has not been reconciled by its buffered event. No more deltas are coming for it. If the turn errors or is interrupted, the buffered event might never arrive, but `span.model_request_end` still does.

The pattern relies on two guarantees:

- Concatenating a preview's deltas in arrival order, keyed by `(event_id, index)`, gives a prefix of `content[index].text` in the buffered event. It is not necessarily the whole text, because deltas might be [shed under load](#limitations).
- A connection emits at most one `event_start` for each `event_id`, and the buffered event is the last thing that connection delivers for that `id`.

### SDK accumulator helpers

Each SDK's helper handles the `index` bookkeeping. The Go, Java, Ruby, and C# helpers also key the accumulating preview by the event's `id`. With the Python, TypeScript, and PHP helpers, keep that map yourself and fold each delta into the entry for its `id`.

The following examples opt in to `agent.message` previews and reconcile them with the buffered event:

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
                "content": [
                    {"type": "text", "text": "Describe the repo in one sentence."}
                ],
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
                preview = accumulate_managed_agents_event(
                    previews.get(event.event_id), event
                )
                if preview is not None:
                    previews[event.event_id] = preview
                    text = "".join(block.text for block in preview.content)
                    print(f"event_delta             preview: {text!r}")
            case "agent.message":
                # The buffered event is the record: it replaces and closes the preview
                preview = accumulate_managed_agents_event(
                    previews.pop(event.id, None), event
                )
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

## Preview session thread events

In a [multiagent](managed-agents-multiagent-orchestration.md) session, every session thread has its own event stream. It takes the same `event_deltas[]` parameter with the same values.

A connection previews only the thread it's reading. The session-level stream previews the primary thread, and a child thread's previews are never cross-posted to it. To watch a subagent's text as the model generates it, open that subagent's thread stream.

A thread stream's path ends in `/threads/{thread_id}/stream`. `/events/stream` exists only at the session level, so there is no `/threads/{thread_id}/events/stream` endpoint.

`event_start` and `event_delta` have the same shape on a thread stream as on the session-level stream, and the [accumulate and reconcile](#accumulate-and-reconcile) pattern applies as written. Run one accumulator instance for each stream connection.

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
# List the session's threads and pick a child: child threads have a non-null
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

The read loop exits on [`session.thread_status_idle`](managed-agents-reference.md#event-types), the event emitted when the session thread's turn completes and the thread goes idle.

## Limitations

- **Best effort:** Under load, the server might shed deltas for an event. When it does, you receive a contiguous prefix of the text and then no further deltas for that event. The buffered `agent.message` still arrives complete. Never treat an accumulated preview as final.
- **No replay on reconnect:** Deltas are delivered only to the connection that opted in, while it is open. This applies to the session-level stream and to each session thread stream alike. A connection opened after a model request started receives no deltas for that in-flight event. There is no way to re-request missed deltas.
- **One thread, text only:** Previews cover assistant text on [the thread the connection is reading](#preview-session-thread-events). Tool use, tool results, and MCP results are never previewed.
- **Never persisted:** `event_start` and `event_delta` exist only on the live stream. They do not appear in the session's event history (`GET /v1/sessions/{session_id}/events`) or in any session thread's event history.

## Troubleshoot previews

| You see                                                             | What it means                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A stream with buffered events but no `event_start` or `event_delta` | The connection you're reading didn't opt in, or the turn never touched the thread you're streaming. `event_deltas[]` applies per connection, not per session. To find which thread ran, list the session's threads (`GET /v1/sessions/{session_id}/threads`).                                                                     |
| A stream that drops during a preview                                | Deltas are not replayed. Follow the [reconnect procedure](managed-agents-events-and-streaming.md#reconnect-without-missing-events): reopen the stream and list the event history. The history includes any buffered events emitted while you were disconnected, including the `agent.message` your preview was waiting for. |
| A 404 on the stream URL                                             | The path or an ID is wrong, or the request carries no managed-agents beta header at all. The thread endpoints are beta-gated, so without the header they don't exist.                                                                                                                                                             |
| A 400 naming `event_deltas`                                         | Only `agent.message` and `agent.thinking` are accepted.                                                                                                                                                                                                                                                                           |

## Next steps



[Session event stream](managed-agents-events-and-streaming.md)

Send events, stream responses, and interrupt or redirect your session while it runs.



[Multiagent orchestration](managed-agents-multiagent-orchestration.md)

Coordinate multiple agents within a single session.
