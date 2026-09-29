---
title: "Start a session - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/sessions"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:51Z"
tags: ["api", "authentication", "mcp"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fsessions)

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

[Managed Agents](managed-agents-overview.md)Delegate work to your agent

# Start a session

Copy page



Create a session to run your agent and begin executing tasks.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

A session is an agent instance within an environment. Each session references an [agent](managed-agents-agent-setup.md) and an [environment](managed-agents-environments.md) (both created separately), and maintains conversation history across multiple interactions. Sessions follow a two-step lifecycle: first [create the session](#creating-a-session), then [send a user event](#starting-the-session) to start work. You can also collapse both steps into one call with [`initial_events`](#seed-the-session-with-initial-events).

## Creating a session

A session requires an `agent` ID and an `environment` ID. Agents are versioned resources; passing in the `agent` ID as a string creates the session with the latest agent version.

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
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
)
```

To pin a session to a specific agent version, pass an object. This lets you control exactly which version runs and stage rollouts of new versions independently.

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
pinned_session = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": 1},
    environment_id=environment.id,
)
```

### Seed the session with initial events

You can create a session and start its work in one call. `initial_events` is an optional array of initial [events](managed-agents-reference.md#event-types) to send to the session at creation, processed in order. It supports `user.message` and [`user.define_outcome`](managed-agents-define-outcomes.md) events, and accepts a maximum of 50 events. A non-empty list starts the agent loop in the same call: the session is created directly in the `running` status, with no further request.

The following example creates a session with a single `user.message` in `initial_events`:

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
seeded_session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    initial_events=[
        {
            "type": "user.message",
            "content": [
                {"type": "text", "text": "List the files in the working directory."}
            ],
        },
    ],
)
# initial_events are not echoed on the create response; read them back
# from the session's event list.
for event in client.beta.sessions.events.list(seeded_session.id):
    if event.type == "user.message":
        for block in event.content:
            if block.type == "text":
                print(f"Seeded event: {block.text}")
```

No other event type is accepted. Events that respond to an agent turn (`user.tool_confirmation`, `user.tool_result`, and `user.custom_tool_result`) aren't accepted because no agent turn exists yet, and `user.interrupt` isn't accepted because there is no turn to stop. Unlike `initial_events` on a scheduled deployment, a session's `initial_events` don't accept `system.message`.

Each event in `initial_events` is validated and persisted before the create response returns, in list order, with a server-assigned ID, exactly as if you had posted it to the [send events](managed-agents-events-and-streaming.md) endpoint immediately after creation. Per-event content rules are also the same as on that endpoint. An empty list is equivalent to omitting the field. Validation is all-or-nothing: if any event fails validation, the whole request is rejected and no session is created.

The create request is rejected in the following cases:

| Condition                                                                                                                      | Status |
|--------------------------------------------------------------------------------------------------------------------------------|--------|
| More than one `user.define_outcome` event                                                                                      | 400    |
| A `user.define_outcome` event without a `rubric`                                                                               | 400    |
| More than 100 file-sourced [`document` content blocks](../Guides/build-with-claude-files.md#document-blocks) across the whole list | 400    |
| A request body over 32 MB                                                                                                      | 413    |

A `user.define_outcome` event in `initial_events` is accepted under the same conditions as sending one to an existing session; see [Define outcomes](managed-agents-define-outcomes.md).

### Override agent configuration for a session

You can pass `agent` in three forms: an agent ID string, a pinned-version object (`type: "agent"`), or an overrides object. The overrides form changes parts of the agent's configuration for a single session. Use it to try a different model or grant an extra tool in one session without versioning the agent. For the overrides form, set `type` to `agent_with_overrides` and pass the agent's `id` and optionally a `version` (omit `version` to use the agent's latest version). Then include any of `model`, `system`, `tools`, `mcp_servers`, or `skills` with the values the session should use.

Each overridable field follows the same three rules:

- **Omit the field:** The session inherits the value from the agent version it references.
- **Set the field to `null`, or to an empty array for list fields:** The session runs with that field cleared. This rule applies in full to `system` and `skills`. There are three exceptions:
  - `model` is never clearable. A session always needs a model, so `model: null` returns a 400 `agent_model_required` error.
  - Clearing `tools` returns a 400 error when the session's effective `skills` is non-empty, because skills require the `read` tool. Otherwise, `tools: null` and `tools: []` clear the field.
  - Clearing `mcp_servers` returns a 400 error when the session's effective `tools` still contains an `mcp_toolset` that references one of the agent's servers. Override `tools` in the same request to remove those `mcp_toolset` entries, then clear `mcp_servers`.
- **Set the field to a value:** The value replaces the agent's value in full. Overrides never merge with the agent's configuration, so a `tools` override must list every tool the session should have. Likewise, a `model` override replaces the agent's `model` object in full, so the agent's own `effort` isn't carried over. To run the session at a specific effort level, set `effort` inside the override's `model` object. A level the model doesn't support returns a 400 error, and a `model` override without `effort` runs at that model's default effort level.

Overrides apply only to the session you create. They do not modify the agent resource or create a new agent version, so other sessions that reference the same agent are unaffected.

In the response, the `agent` object reflects the configuration the session runs with after the overrides are applied. Its `id` and `version` still identify the agent and version the overrides are applied to. This lets you trace a session back to its base agent.

The following example starts a session that overrides the model and clears the system prompt:

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
override_session = client.beta.sessions.create(
    agent={
        "type": "agent_with_overrides",
        "id": agent.id,
        "model": {"id": "claude-sonnet-5"},
        "system": None,  # clear the agent's system prompt for this session
    },
    environment_id=environment.id,
)
# The response's agent is the resolved snapshot with the overrides applied.
print(f"Model: {override_session.agent.model.id}")
print(f"System: {override_session.agent.system}")
```

#### Pin the inference geo for a session

Because a `model` override replaces the agent's `model` object in full, it also sets or clears the model's [`inference_geo`](../Guides/build-with-claude-data-residency.md) pin for the session: an override that includes `inference_geo` pins the geography that serves the session's model requests, and one that omits it clears the agent's pin so the session follows the workspace's `default_inference_geo`. The overridden value is validated against the workspace's `allowed_inference_geos` when the session is created.

The following example starts a session from an agent whose model has no geo pin, pins the session's model requests to US inference by including `inference_geo` in the `model` override, and prints the value echoed in the response's `agent.model`:

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
session = client.beta.sessions.create(
    agent={
        "type": "agent_with_overrides",
        "id": agent.id,
        # Replaces the agent's `model` in full: restate `id`, add `inference_geo` to pin.
        "model": {"id": "claude-opus-5-5", "inference_geo": "us"},
    },
    environment_id=environment.id,
)
print(f"Inference geo: {session.agent.model.inference_geo}")
```



The agent defines how Claude behaves within the session, including the model, system prompt, tools, and MCP servers. See [Define your agent](managed-agents-agent-setup.md) for details.

### Set a session budget

To cap what a session can spend, pass the optional `budget` object when you create it. A budget is a hard ceiling on the session's list cost: the platform prices everything the session consumes at public list rates, and the session stops issuing new model requests once that running total reaches `max_list_cost`. Set `type` to `limit` and give `max_list_cost` an `amount` and a `currency`. `amount` is a whole number of US cents written as a string, such as `"2500"` for \$25.00; the API takes a string rather than a number so no floating-point rounding is ever applied. `USD` is the only currency currently supported. When the session reaches the cap, it pauses and goes idle with the stop reason `budget_reached`. The cap is enforced between model requests, so the request that crosses it finishes first and the session's final list cost can land [a fraction past the cap](managed-agents-budgets.md#when-a-session-reaches-its-budget). A budget can only be attached at creation: you can [change or remove](managed-agents-session-operations.md#updating-the-session-budget) it later, but you can't add one to a session created without it.

The following example creates a session with a \$25.00 budget; the response echoes the `budget` on the session resource:

cURL



```python
curl -fsSL https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": "$AGENT_ID",
  "environment_id": "$ENVIRONMENT_ID",
  "budget": {
    "type": "limit",
    "max_list_cost": {"amount": "2500", "currency": "USD"}
  }
}
EOF
```

See [Session budgets](managed-agents-budgets.md) for how enforcement works, what counts toward list cost, and how budgets behave in multiagent sessions.

## MCP authentication through vaults

If your agent uses MCP tools that require authentication, pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials. Anthropic manages token refresh on your behalf. See [Authenticate with vaults](managed-agents-vaults.md) for how to create vaults and register credentials.

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
vault_session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
)
```

## Starting the session

Creating a session without `initial_events` registers the session but does not start any work; the environment's sandbox begins provisioning as soon as the session is created, so the first tool call does not wait on it. To delegate a task, send events to the session using a [user event](managed-agents-reference.md#event-types). To supply the first event in the create request instead, see [Seed the session with initial events](#seed-the-session-with-initial-events). The session acts as a state machine that tracks progress while events drive the actual execution.

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
                {"type": "text", "text": "List the files in the working directory."}
            ],
        },
    ],
)
```

See [Session event stream](managed-agents-events-and-streaming.md) for how to stream the agent's responses and handle tool confirmations.

See [Session statuses](managed-agents-session-operations.md#session-statuses) for the statuses a session moves through.

## Next steps



[Session operations](managed-agents-session-operations.md)

Retrieve, list, update, archive, and delete Claude Managed Agents sessions.



[Session event stream](managed-agents-events-and-streaming.md)

Send events, stream responses, and interrupt or redirect your session mid-execution.



[Scheduled deployments](managed-agents-scheduled-deployments.md)

Create and manage deployments with the Claude API: run an agent on a recurring cron schedule and inspect its run history.
