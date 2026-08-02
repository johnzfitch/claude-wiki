---
title: "Multiagent orchestration - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:50Z"
tags: ["agents", "api"]
---

# Multiagent orchestration




Coordinate multiple agents within a single session.




Multiagent orchestration lets one agent coordinate with others to complete complex work. Agents can act in parallel with their own isolated context, which helps improve output quality and can also improve time to completion.

Not sure a multiagent setup fits your problem? See [when to use multiagent systems (and when not to)](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them).



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](/docs/en/api/beta-headers#endpoint-specific-headers).




How it works

All agents share the same sandbox, filesystem, and [vault credentials](/docs/en/managed-agents/vaults), but each agent runs in its own **session thread**, a context-isolated event stream with its own conversation history. The coordinator reports activity in the **primary thread** (which is the same as the session-level [event stream](/docs/en/managed-agents/events-and-streaming)); additional threads are spawned at runtime when the coordinator delegates work.

Threads are persistent: the coordinator can send a follow-up to an agent it called earlier, and that agent retains everything from its previous turns.

Each agent uses its own configuration: model, system prompt, tools, MCP servers, and skills. Session-level [agent configuration overrides](/docs/en/managed-agents/sessions#override-agent-configuration-for-a-session) are the exception; they apply to the coordinator and its `self` copies. Tools, MCP servers, and context are not shared.




What to delegate

Multiagent coordination is best suited for complex tasks that either require work across a variety of surfaces, or where multiple well-scoped tasks contribute to an overall goal.

Patterns that work well:

- **Parallelization:** Fan out independent subtasks simultaneously (searching multiple sources, analyzing separate files) and have the coordinator synthesize the results.
- **Specialization:** Route to agents with domain-focused system prompts and tools, such as a security agent or a documentation agent, rather than loading a single agent with every capability.
- **Escalation:** Consult a more capable agent or model for a subset of complex subtasks.




Configure the coordinator

When [defining your agent](/docs/en/managed-agents/agent-setup), set `multiagent` to declare the roster of agents the coordinator can delegate to:

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
ant beta:agents create <<YAML
name: Engineering Lead
model: claude-opus-5
system: You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.
tools:
  - type: agent_toolset_20260401
multiagent:
  type: coordinator
  agents:
    - type: agent
      id: $REVIEWER_AGENT_ID
    - type: agent
      id: $TEST_WRITER_AGENT_ID
YAML
```

`multiagent.agents` can accept any of the following:

- `{"type": "agent", "id": agent.id}` references a previously created `agent` by ID. If no `version` is specified, the reference is pinned to the latest version of that agent at the time the coordinator is created.
- `{"type": "agent", "id": agent.id, "version": agent.version}` pins a specific agent version.
- `{"type": "self"}` allows the coordinator to spawn copies of itself. If the session was created with [agent configuration overrides](/docs/en/managed-agents/sessions#override-agent-configuration-for-a-session), those overrides also apply to these copies; roster entries referenced by ID are unaffected.

The coordinator's configuration, including its `multiagent.agents` roster, is snapshotted when the coordinator is created or updated. Referenced agents stay pinned to the versions resolved at that time and do not automatically pick up later updates to their definitions. To delegate to a newer version of a referenced agent, [update the coordinator](/docs/en/managed-agents/agent-setup#update-an-agent) so its roster references that version.

The coordinator can only delegate to one level of agents; referencing an agent that has its own `multiagent.agents` roster fails the create or update request with a validation error. A maximum of 20 unique agents can be listed in `multiagent.agents`, but the coordinator can call multiple copies of each agent.




Create the session

Create a session referencing the coordinator. The coordinator delegates to the agents in its roster as needed.

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
session = client.beta.sessions.create(
    agent=coordinator.id,
    environment_id=environment.id,
)
```




Connect agents to MCP servers

MCP servers are agent-scoped (each agent definition declares its own servers and tools), while vault credentials are session-scoped (`vault_ids` passed at session creation apply to every thread). Two implications for your integration:

- To authenticate MCP servers, include a vault credential for every MCP server used across all agents.
- To limit an agent's access, declare only the servers it needs in its agent definition.

[Agent configuration overrides](/docs/en/managed-agents/sessions#override-agent-configuration-for-a-session) at session creation can replace the coordinator's MCP servers and those of its `self` copies.

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
research_agent = client.beta.agents.create(
    name="researcher",
    model="claude-haiku-4-5",
    mcp_servers=[
        {"type": "url", "name": "github", "url": "https://api.githubcopilot.com/mcp/"},
    ],
    tools=[{"type": "mcp_toolset", "mcp_server_name": "github"}],
)

coordinator = client.beta.agents.create(
    name="coordinator",
    model="claude-opus-5",
    tools=[{"type": "agent_toolset_20260401"}],
    multiagent={
        "type": "coordinator",
        "agents": [{"type": "agent", "id": research_agent.id}],
    },
)

session = client.beta.sessions.create(
    agent=coordinator.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
)
print(session.id)
```

In this example, only the researcher declares the GitHub MCP server, so the coordinator does not have access. The session's `vault_ids` supply the GitHub credential to the researcher's thread.



If an agent's MCP calls fail to authenticate after you declare the server, confirm the credential's `mcp_server_url` refers to the same server as the agent's `mcp_servers[].url`. Both URLs are normalized before matching (scheme and host lowercased, default ports and trailing slashes stripped), so differences in host casing, a default port, or a trailing slash don't prevent a match; a different path, subdomain, or non-default port does.




Threads

The **session-level event stream** (`/v1/sessions/{session_id}/events/stream`) is considered the **primary thread**, containing a condensed view of all activity across all threads. You don't see the full activity from subagents, but you do see the start and end of their work, and blocking events such as tool permission requests.

**Session threads** are where you drill into a specific agent's activity.

The session `status` is an aggregation of all agent activity; if at least one thread is `running`, then the overall session status is `running` as well.



A maximum of 25 concurrent threads are supported. The coordinator can call multiple copies of a single agent in the roster, creating multiple threads associated with one `agent`.

List threads

List threads

Interrupt a session thread

Interrupt a session thread

Archive a session thread

Archive a session thread

List all threads associated with a session as follows:

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
for thread in client.beta.sessions.threads.list(session.id):
    print(f"[{thread.agent.name}] {thread.status}")
```

The full list includes the primary thread. `parent_thread_id` is null for the primary thread.




Primary thread events

These events surface multiagent activity on the primary thread at `/v1/sessions/{session_id}/events/stream`. Message-direction events are named relative to the thread whose stream they appear on: `agent.thread_message_received` means a message arrived on this thread from another thread, and `agent.thread_message_sent` means this thread sent one. The task the coordinator delegates, for example, arrives on the child's own stream as an `agent.thread_message_received` event.

| Type                               | Description                                                                                                                                                |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `session.thread_created`           | A thread was created. Includes `session_thread_id` and `agent_name`.                                                                                       |
| `session.thread_status_running`    | A thread started activity.                                                                                                                                 |
| `session.thread_status_idle`       | The agent associated with the thread is awaiting input. Includes a `stop_reason` indicating why the agent stopped.                                         |
| `session.thread_status_terminated` | A thread was archived or encountered a terminal error.                                                                                                     |
| `agent.thread_message_received`    | On the primary thread, an agent sent a report or question to the coordinator. Includes `from_session_thread_id`, `from_agent_name`, and `content`.         |
| `agent.thread_message_sent`        | On the primary thread, the coordinator sent a task or follow-up message to another agent. Includes `to_session_thread_id`, `to_agent_name`, and `content`. |




Session thread events

Critical events are proxied to the primary thread. However, you might still want to investigate a specific agent's reasoning and tool calls. To do so, stream or list the events from the associated session thread.

Each session thread has its own event stream at `/v1/sessions/{session_id}/threads/{thread_id}/stream`, and it accepts the same `event_deltas[]` parameter as the session-level stream, so you can preview a subagent's text as the model generates it. A connection previews only the thread it's reading: a child thread's previews never appear on the session-level stream, so to watch a subagent live, open its own thread stream. See [Preview session thread events](/docs/en/managed-agents/events-and-streaming#preview-session-thread-events) for opting in, accumulating, and reconciling previews.

Stream session thread events

Stream session thread events

List session thread events

List session thread events

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




Tool permissions and custom tools

If a subagent needs something from your client, such as [permission](/docs/en/managed-agents/events-and-streaming#tool-confirmation) to run an `always_ask` tool, or the [result of a custom tool](/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls), the event is cross-posted to the **primary thread** with `session_thread_id` identifying the originating session thread.

```python
{
  "type": "session.thread_status_idle",
  "id": "sevt_01ABC...",
  "session_thread_id": "sth_01DEF...",
  "agent_name": "code-reviewer",
  "stop_reason": {
    "type": "requires_action",
    "event_ids": ["toolu_01XYZ..."]
  }
}
```



Post `user.tool_confirmation` (with `tool_use_id`) or `user.custom_tool_result` (with `custom_tool_use_id`); the server routes the response to the correct thread automatically.

The following example extends the [tool confirmation handler](/docs/en/managed-agents/events-and-streaming#tool-confirmation) to route replies. The same pattern applies to `user.custom_tool_result`.

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
