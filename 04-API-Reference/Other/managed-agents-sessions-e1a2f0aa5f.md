---
title: "Start a session - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/sessions"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:42Z"
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

Start a session

Managed Agents/Delegate work to your agent

# Start a session




Create a session to run your agent and begin executing tasks.




A session is an agent instance within an environment. Each session references an [agent](/docs/en/managed-agents/agent-setup) and an [environment](/docs/en/managed-agents/environments) (both created separately), and maintains conversation history across multiple interactions. Sessions follow a two-step lifecycle: first [create the session](#creating-a-session), then [send a user event](#starting-the-session) to start work. You can also collapse both steps into one call with [`initial_events`](#seed-the-session-with-initial-events).



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](/docs/en/api/beta-headers#endpoint-specific-headers).




Creating a session

A session requires an `agent` ID and an `environment` ID. Agents are versioned resources; passing in the `agent` ID as a string starts the session with the latest agent version.

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
ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID"
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
ant beta:sessions create <<YAML
agent:
  type: agent
  id: $AGENT_ID
  version: 1
environment_id: $ENVIRONMENT_ID
YAML
```




Seed the session with initial events

You can create a session and start its work in one call. `initial_events` is an optional array of initial [events](/docs/en/managed-agents/reference#event-types) to send to the session at creation, processed in order. It supports `user.message` and [`user.define_outcome`](/docs/en/managed-agents/define-outcomes) events, and accepts a maximum of 50 events. A non-empty list starts the agent loop in the same call: the session is created directly in the `running` status, with no further request.

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
SEEDED_SESSION_ID=$(ant beta:sessions create \
  --transform id --raw-output <<YAML
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
initial_events:
  - type: user.message
    content:
      - type: text
        text: List the files in the working directory.
YAML
)

# initial_events aren't echoed on the create response; list the session's
# events to see the seeded message.
echo "Seeded event: $(ant beta:sessions:events list \
  --session-id "$SEEDED_SESSION_ID" \
  --format raw \
  --transform 'data.#(type=="user.message").content.0.text' --raw-output)"
```

No other event type is accepted. Events that respond to an agent turn (`user.tool_confirmation`, `user.tool_result`, and `user.custom_tool_result`) aren't accepted because no agent turn exists yet, and `user.interrupt` isn't accepted because there is no turn to stop. Unlike `initial_events` on a scheduled deployment, a session's `initial_events` don't accept `system.message`.

Each event in `initial_events` is validated and persisted before the create response returns, in list order, with a server-assigned ID, exactly as if you had posted it to the [send events](/docs/en/managed-agents/events-and-streaming) endpoint immediately after creation. Per-event content rules are also the same as on that endpoint. An empty list is equivalent to omitting the field. Validation is all-or-nothing: if any event fails validation, the whole request is rejected and no session is created.

The create request is rejected in the following cases:

| Condition                                                                                                                      | Status |
|--------------------------------------------------------------------------------------------------------------------------------|--------|
| More than one `user.define_outcome` event                                                                                      | 400    |
| A `user.define_outcome` event without a `rubric`                                                                               | 400    |
| More than 100 file-sourced [`document` content blocks](/docs/en/build-with-claude/files#document-blocks) across the whole list | 400    |
| A request body over 32 MB                                                                                                      | 413    |

A `user.define_outcome` event in `initial_events` is accepted under the same conditions as sending one to an existing session; see [Define outcomes](/docs/en/managed-agents/define-outcomes).




Override agent configuration for a session

You can pass `agent` in three forms: an agent ID string, a pinned-version object (`type: "agent"`), or an overrides object. The overrides form changes parts of the agent's configuration for a single session. Use it to try a different model or grant an extra tool in one session without versioning the agent. For the overrides form, set `type` to `agent_with_overrides` and pass the agent's `id` and optionally a `version` (omit `version` to use the agent's latest version). Then include any of `model`, `system`, `tools`, `mcp_servers`, or `skills` with the values the session should use.

Each overridable field follows the same three rules:

- **Omit the field:** The session inherits the value from the agent version it references.
- **Set the field to `null`, or to an empty array for list fields:** The session runs with that field cleared. This rule applies in full to `system` and `skills`. There are three exceptions:
  - `model` is never clearable. A session always needs a model, so `model: null` returns a 400 `agent_model_required` error.
  - Clearing `tools` returns a 400 error when the session's effective `skills` is non-empty, because skills require the `read` tool. Otherwise, `tools: null` and `tools: []` clear the field.
  - Clearing `mcp_servers` returns a 400 error when the session's effective `tools` still contains an `mcp_toolset` that references one of the agent's servers. Override `tools` in the same request to remove those `mcp_toolset` entries, then clear `mcp_servers`.
- **Set the field to a value:** The value replaces the agent's value in full. Overrides never merge with the agent's configuration, so a `tools` override must list every tool the session should have. There is one exception:
  - An `effort` level inside a per-session `model` override isn't applied. Set `effort` on the [agent](/docs/en/managed-agents/agent-setup#agent-configuration-fields) instead.

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
# The response's `agent` is the resolved snapshot: each override replaces that
# field for this session only, and the agent resource keeps its id and version.
ant beta:sessions create \
  --transform 'agent.{id,version,model,system}' \
  --format json <<YAML
agent:
  type: agent_with_overrides
  id: $AGENT_ID
  model:
    id: claude-sonnet-5
  system: null
environment_id: $ENVIRONMENT_ID
YAML
```



The agent defines how Claude behaves within the session, including the model, system prompt, tools, and MCP servers. See [Define your agent](/docs/en/managed-agents/agent-setup) for details.




MCP authentication through vaults

If your agent uses MCP tools that require authentication, pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials. Anthropic manages token refresh on your behalf. See [Authenticate with vaults](/docs/en/managed-agents/vaults) for how to create vaults and register credentials.

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
ant beta:sessions create <<YAML
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
vault_ids:
  - $VAULT_ID
YAML
```




Starting the session

Creating a session without `initial_events` registers the session but does not start any work; the environment's sandbox is provisioned when the session first needs it. To delegate a task, send events to the session using a [user event](/docs/en/managed-agents/reference#event-types). To supply the first event in the create request instead, see [Seed the session with initial events](#seed-the-session-with-initial-events). The session acts as a state machine that tracks progress while events drive the actual execution.

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
ant beta:sessions:events send \
  --session-id "$SESSION_ID" <<'YAML'
events:
  - type: user.message
    content:
      - type: text
        text: List the files in the working directory.
YAML
```

See [Session event stream](/docs/en/managed-agents/events-and-streaming) for how to stream the agent's responses and handle tool confirmations.

See [Session statuses](/docs/en/managed-agents/session-operations#session-statuses) for the statuses a session moves through.




Next steps




Session operations

Retrieve, list, update, archive, and delete Claude Managed Agents sessions.




Session event stream

Send events, stream responses, and interrupt or redirect your session mid-execution.


Scheduled deployments

Create and manage deployments with the Claude API: run an agent on a recurring cron schedule and inspect its run history.
