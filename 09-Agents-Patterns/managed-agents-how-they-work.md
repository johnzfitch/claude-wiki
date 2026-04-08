---
source_url: "https://platform.claude.com/docs/en/managed-agents/how-managed-agents-work"
category: "Agents-Patterns"
fetched_at: "2026-04-08"
---

# Session event stream

Send events, stream responses, and interrupt or redirect your session mid-execution.

---

> Note: The original URL `/docs/en/managed-agents/how-managed-agents-work` returned 404. This content is sourced from the events-and-streaming page, which covers how managed agents work through their event-based communication model.

Communication with Claude Managed Agents is event-based. You send user events to the agent, and receive agent and session events back to track status.

> All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## Event types

Events flow in two directions.
- **User events** are what you send to the agent to kick off a session and steer it as it progresses.
- **Session events**, **span events**, and **agent events** are sent to you for observability into your session state and agent progress.

Event type strings follow a `{domain}.{action}` naming convention.

### User events

| Type | Description |
| --- | --- |
| `user.message` | A user message with text content. |
| `user.interrupt` | Stop the agent mid-execution. |
| `user.custom_tool_result` | Response to a custom tool call from the agent. |
| `user.tool_confirmation` | Approve or deny an agent or MCP tool call when a permission policy requires confirmation. |
| `user.define_outcome` | Define an [outcome](/docs/en/managed-agents/define-outcomes) for the agent to work toward. |

### Agent events

| Type | Description |
| --- | --- |
| `agent.message` | Agent response containing text content blocks. |
| `agent.thinking` | Agent thinking content, emitted separately from messages. |
| `agent.tool_use` | Agent invoked a pre-built agent tool (bash, file operations, and so on). |
| `agent.tool_result` | Result of a pre-built agent tool execution. |
| `agent.mcp_tool_use` | Agent invoked an MCP server tool. |
| `agent.mcp_tool_result` | Result of an MCP tool execution. |
| `agent.custom_tool_use` | Agent invoked one of your custom tools. Respond with a `user.custom_tool_result` event. |
| `agent.thread_context_compacted` | Conversation history was compacted to fit the context window. |
| `agent.thread_message_sent` | Agent sent a message to another [multiagent](/docs/en/managed-agents/multi-agent) thread. |
| `agent.thread_message_received` | Agent received a message from another [multiagent](/docs/en/managed-agents/multi-agent) thread. |

### Session events

| Type | Description |
| --- | --- |
| `session.status_running` | Agent is actively processing. |
| `session.status_idle` | Agent finished its current task and is waiting for input. Includes a `stop_reason` indicating why the agent stopped. |
| `session.status_rescheduled` | A transient error occurred and the session is retrying automatically. |
| `session.status_terminated` | Session ended due to an unrecoverable error. |
| `session.error` | An error occurred during processing. Includes a typed `error` object with a `retry_status`. |
| `session.outcome_evaluated` | An [outcome](/docs/en/managed-agents/define-outcomes) evaluation has reached a terminal status. |
| `session.thread_created` | The coordinator spawned a new [multiagent](/docs/en/managed-agents/multi-agent) thread. |
| `session.thread_idle` | A [multiagent](/docs/en/managed-agents/multi-agent) thread finished its current work. |

### Span events

Span events are observability markers that wrap activity for timing and usage tracking.

| Type | Description |
| --- | --- |
| `span.model_request_start` | A model inference call has started. |
| `span.model_request_end` | A model inference call has completed. Includes `model_usage` with token counts. |
| `span.outcome_evaluation_start` | [Outcome](/docs/en/managed-agents/define-outcomes) evaluation has started. |
| `span.outcome_evaluation_ongoing` | Heartbeat during an ongoing [outcome](/docs/en/managed-agents/define-outcomes) evaluation. |
| `span.outcome_evaluation_end` | [Outcome](/docs/en/managed-agents/define-outcomes) evaluation has completed. |

Every event includes a `processed_at` timestamp indicating when the event was recorded server-side. If `processed_at` is null, it means the event has been queued by the harness and will be handled after preceding events finish processing.

See the [session events API reference](/docs/en/api/beta/sessions/events/stream) for the full schema of each event type.

## Integrating events

### Sending events

Send a `user.message` event to start or continue the agent's work:

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

```typescript
await client.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.message",
      content: [
        {
          type: "text",
          text: "Analyze the performance of the sort function in utils.py"
        }
      ]
    }
  ]
});
```

Send a `user.interrupt` event to stop the agent mid-execution, then follow up with a `user.message` event to redirect it:

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

The agent will acknowledge the interruption and switch to the new task.

### Streaming responses

Stream events from the session to receive real-time updates as the agent works. Only events emitted after the stream is opened are delivered, so open the stream before sending events to avoid a race condition.

```python
# Open the stream first, then send the user message
with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [
                    {"type": "text", "text": "Summarize the repo README"},
                ],
            },
        ],
    )

    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    if block.type == "text":
                        print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[Tool: {event.name}]")
            case "session.status_idle":
                print("\nDone.")
                break
```

```typescript
const stream = await client.beta.sessions.events.stream(session.id);

await client.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.message",
      content: [
        { type: "text", text: "Summarize the repo README" }
      ]
    }
  ]
});

for await (const event of stream) {
  if (event.type === "agent.message") {
    for (const block of event.content) {
      if (block.type === "text") process.stdout.write(block.text);
    }
  } else if (event.type === "agent.tool_use") {
    console.log(`\n[Tool: ${event.name}]`);
  } else if (event.type === "session.status_idle") {
    console.log("\nDone.");
    break;
  }
}
```

### Handling custom tool calls

When the agent calls a custom tool, you receive an `agent.custom_tool_use` event and must respond with a `user.custom_tool_result` event:

```python
for event in stream:
    if event.type == "agent.custom_tool_use":
        # Execute the tool in your application
        result = execute_custom_tool(event.name, event.input)

        # Send the result back to the agent
        client.beta.sessions.events.send(
            session.id,
            events=[
                {
                    "type": "user.custom_tool_result",
                    "tool_use_id": event.id,
                    "content": [{"type": "text", "text": result}],
                },
            ],
        )
```

### Fetching event history

Retrieve the full event history for a session:

```python
events = client.beta.sessions.events.list(session.id)
for event in events:
    print(f"{event.type}: {event.processed_at}")
```

```typescript
const events = await client.beta.sessions.events.list(session.id);
for (const event of events.data) {
  console.log(`${event.type}: ${event.processed_at}`);
}
```
