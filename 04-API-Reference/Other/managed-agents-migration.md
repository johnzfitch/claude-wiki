---
title: "Migration - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/migration"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:40Z"
tags: ["agents", "api", "sdk"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fmigration)

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

[Managed Agents](managed-agents-overview.md)First steps

# Migration

Copy page



Move an existing agent built on the Messages API or the Claude Agent SDK to Claude Managed Agents.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

Claude Managed Agents replaces your hand-written agent loop with managed infrastructure. This page covers what changes when you migrate from a custom loop built on the [Messages API](../Guides/build-with-claude-working-with-messages.md) or from the [Claude Agent SDK](../../05-Agent-SDK/agent-sdk-overview.md).

## From a Messages API agent loop

If you built an agent by calling `messages.create` in a `while` loop, running tool calls yourself, and appending results to the conversation history, most of that code goes away.

### What you stop managing

| Before                                                                                           | After                                                                                                                      |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| You maintain the conversation history array and pass it back on every turn.                      | The session stores history server-side. Send events, receive events.                                                       |
| You iterate `tool_use` content blocks, run each tool, and loop back with `tool_result` messages. | Pre-built tools run inside the sandbox automatically. You only handle custom tools through `agent.custom_tool_use` events. |
| You provision your own sandbox for running agent-generated code.                                 | The session sandbox handles code execution, file operations, and bash.                                                     |
| You decide when the loop is done.                                                                | The session emits `session.status_idle` when the agent has nothing more to do.                                             |

### Code comparison

**Before** (Messages API loop, simplified):

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
messages = [{"role": "user", "content": task}]
while True:
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        messages=messages,
        tools=tools,
    )
    messages.append({"role": "assistant", "content": response.content})
    if response.stop_reason == "end_turn":
        break
    for block in response.content:
        if block.type == "tool_use":
            result = execute_tool(block.name, block.input)
            messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    ],
                }
            )
```

**After** (Claude Managed Agents):

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
agent = client.beta.agents.create(
    name="Task Runner",
    model="claude-opus-5-5",
    tools=[{"type": "agent_toolset_20260401"}],
)

session = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": agent.version},
    environment_id=environment.id,
)

with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[{"type": "user.message", "content": [{"type": "text", "text": task}]}],
    )
    for event in stream:
        if event.type == "session.status_idle":
            break
```

### What you still control

- **System prompt and model:** Same fields, now on the agent definition.
- **Custom tools:** Still declared with JSON Schema. Execution moves from inline handling to responding to `agent.custom_tool_use` events. See [Session event stream](managed-agents-events-and-streaming.md).
- **Web search and web fetch settings:** Same `allowed_domains`, `blocked_domains`, `max_content_tokens`, and `user_location` fields, now set once on the `web_search` and `web_fetch` entries of the agent toolset's `configs` array instead of on every request. The `max_uses`, `citations`, and `cache_control` fields are not available. See [Restrict web search and web fetch domains](managed-agents-tools.md#restrict-web-search-and-web-fetch-domains).
- **Context:** You can still inject context through the system prompt, [file resources](managed-agents-files.md), or [skills](managed-agents-skills.md).

## From the Claude Agent SDK

If you built with the [Claude Agent SDK](../../05-Agent-SDK/agent-sdk-overview.md), you're already working with agents, tools, and sessions as concepts. The difference is where they run: the SDK runs in a process you operate, while Managed Agents runs in Anthropic's infrastructure. Most of the migration is mapping SDK configuration objects to their API-side equivalents.

### What changes

| Agent SDK                                                           | Managed Agents                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ClaudeAgentOptions(...)` constructed per run                       | `client.beta.agents.create(...)` once; the Agent is persisted and versioned server-side. See [Agent setup](managed-agents-agent-setup.md).                                                                                                   |
| `async with ClaudeSDKClient(...)` or `query(...)`                   | `client.beta.sessions.create(...)` then send and receive [events](managed-agents-events-and-streaming.md).                                                                                                                                   |
| Functions defined with `@tool`, dispatched automatically by the SDK | Declare as `{"type": "custom", ...}` on the Agent; your client handles `agent.custom_tool_use` events and replies with `user.custom_tool_result`. See [Tools](managed-agents-tools.md).                                                      |
| Built-in tools run in your process against your filesystem          | `{"type": "agent_toolset_20260401"}` runs the same tools inside the session sandbox against `/workspace`.                                                                                                                                          |
| `cwd`, `add_dirs` point at local paths                              | Upload or mount [files](managed-agents-files.md) as session resources.                                                                                                                                                                       |
| `system_prompt` and the `CLAUDE.md` hierarchy                       | A single `system` string on the Agent. Each update that changes the agent produces a new server-side version; pin sessions to a specific version to promote or roll back without a deploy. See [Agent setup](managed-agents-agent-setup.md). |
| `mcp_servers` configured and authenticated in one place             | Declare servers on the Agent; provide credentials through a [Vault](managed-agents-vaults.md) on the Session.                                                                                                                                |
| `permission_mode`, `can_use_tool`                                   | Per-tool [`permission_policy`](managed-agents-permission-policies.md) (`always_allow`, `always_ask`, or `auto`); send `user.tool_confirmation` events for calls that pause for your approval.                                                |

### Code comparison

**Before** (Agent SDK):

Python

TypeScript



```python
from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    create_sdk_mcp_server,
    tool,
)


@tool("get_weather", "Get the current weather for a city.", {"city": str})
async def get_weather(args: dict) -> dict:
    return {"content": [{"type": "text", "text": f"{args['city']}: 18°C, clear"}]}


options = ClaudeAgentOptions(
    model="claude-opus-5-5",
    system_prompt="You are a concise weather assistant.",
    mcp_servers={
        "weather": create_sdk_mcp_server("weather", "1.0", tools=[get_weather])
    },
)

async with ClaudeSDKClient(options=options) as agent:
    await agent.query("What's the weather in Tokyo?")
    async for msg in agent.receive_response():
        print(msg)
```

**After** (Managed Agents):

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
from anthropic import Anthropic

client = Anthropic()

agent = client.beta.agents.create(
    name="weather-agent",
    model="claude-opus-5-5",
    system="You are a concise weather assistant.",
    tools=[
        {
            "type": "custom",
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "input_schema": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        }
    ],
)
environment = client.beta.environments.create(
    name="weather-env",
    config={"type": "cloud", "networking": {"type": "unrestricted"}},
)

session = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": agent.version},
    environment_id=environment.id,
)


def get_weather(city: str) -> str:
    return f"{city}: 18°C, clear"


with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [{"type": "text", "text": "What's the weather in Tokyo?"}],
            }
        ],
    )
    for event in stream:
        match event.type:
            case "agent.message":
                print(
                    "".join(
                        block.text for block in event.content if block.type == "text"
                    )
                )
            case "agent.custom_tool_use":
                result = get_weather(**event.input)
                client.beta.sessions.events.send(
                    session.id,
                    events=[
                        {
                            "type": "user.custom_tool_result",
                            "custom_tool_use_id": event.id,
                            "content": [{"type": "text", "text": result}],
                        }
                    ],
                )
            case "session.status_idle":
                if event.stop_reason and event.stop_reason.type == "end_turn":
                    break
```

The Agent and Environment are created once and reused across sessions. The tool function still runs in your process; the difference is that you read the `agent.custom_tool_use` event and send the result explicitly instead of the SDK dispatching it for you.

### Features that move to your client

The tradeoff for Anthropic running the agent loop is that a few things the SDK handled automatically become your client's responsibility.

| SDK feature                        | Managed Agents approach                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plan mode                          | Run a planning-only session first, then a second session to run the plan.                                                                                                                                                                                                                                                                                                                                          |
| Output styles, slash commands      | Apply in your client before sending `user.message` or after receiving `agent.message`.                                                                                                                                                                                                                                                                                                                             |
| `PreToolUse` / `PostToolUse` hooks | Your client already sees every `agent.custom_tool_use` event before responding; put the logic there. For built-in tools, use `permission_policy: always_ask` to review every call. [`auto`](managed-agents-permission-policies.md#let-the-server-evaluate-each-call-with-auto) lets the server evaluate each call instead, but if the server evaluates a call as safe, it runs without reaching your client. |
| `max_turns`                        | Count turns client-side.                                                                                                                                                                                                                                                                                                                                                                                           |

## Migration checklist

1.  [Create an environment](managed-agents-environments.md) with the networking and runtimes your agent needs.
2.  Port your system prompt and tool selection to an [agent definition](managed-agents-agent-setup.md).
3.  Replace your loop with [`sessions.create`](managed-agents-sessions.md) and [`sessions.events.stream`](managed-agents-events-and-streaming.md).
4.  For any local files the agent reads, upload them through the [Files API](managed-agents-files.md) and mount them as `resources`.
5.  For any custom tool handlers, move execution into your event loop as responses to `agent.custom_tool_use` events.
6.  Verify with a test session before pointing production traffic at the new flow.

## Migrating between model versions

When a new Claude model is released, migrating a Claude Managed Agents integration is typically a one-field change: update `model` on your [agent definition](managed-agents-agent-setup.md) and the change takes effect on the next session you create.

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
ant apply agent.md
```

agent.md





```python
---
name: Task Runner
model: claude-opus-5-5
tools:
  - type: agent_toolset_20260401
---

You are a task automation agent. Complete the task you are given end to end.
```

Most model-level behavior changes documented in the [Messages API migration guide](../../20-Models/about-claude-models-migration-guide.md) do not require action on your side:

- **Request parameter changes** (`max_tokens` defaults, `thinking` configuration) are handled by the Claude Managed Agents runtime. These fields are not exposed on the agent definition.
- **Assistant message prefilling** does not exist in the event-based session model, so its removal on newer models is a no-op.
- **Tool argument JSON escaping** is parsed by the runtime before you receive `agent.custom_tool_use` events. You see structured data, not raw strings.

The behavior descriptions in the Messages API guide (what the model does differently) still apply. The migration steps (how to change your request code) do not.
