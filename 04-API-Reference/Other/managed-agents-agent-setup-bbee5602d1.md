---
title: "Define your agent - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/agent-setup"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:42:14Z"
tags: ["agents", "api"]
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

Agent setup

Managed Agents/Define your agent

# Define your agent




Create a reusable, versioned agent configuration.




An agent is a reusable, versioned configuration that defines persona and capabilities. It bundles the model, system prompt, tools, MCP servers, and skills that shape how Claude behaves during a session.

Create the agent once as a reusable resource and reference it by ID each time you [start a session](/docs/en/managed-agents/sessions). Agents are versioned and easier to manage across many sessions.



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](/docs/en/api/beta-headers#endpoint-specific-headers).




Agent configuration fields

| Field         | Description                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`        | Required. A human-readable name for the agent.                                                                                                                                                                                                                                                                                                                                                                  |
| `model`       | Required. The Claude [model](/docs/en/about-claude/models/overview) that powers the agent. Accepts a model ID string or an object, for example `{"id": "claude-opus-5"}`. Claude 4.5 and later models are supported. The object form also accepts a `speed` and an `effort` level; see the tips under [Create an agent](#create-an-agent) and [Effort levels](/docs/en/build-with-claude/effort#effort-levels). |
| `system`      | A [system prompt](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role) that defines the agent's behavior and persona. The system prompt is distinct from [user messages](/docs/en/managed-agents/reference#event-types), which should describe the work to be done.                                                                                                |
| `tools`       | The tools available to the agent. Combines [pre-built agent tools](/docs/en/managed-agents/tools), [MCP tools](/docs/en/managed-agents/mcp-connector), and [custom tools](/docs/en/managed-agents/tools#custom-tools).                                                                                                                                                                                          |
| `mcp_servers` | [MCP servers](/docs/en/managed-agents/mcp-connector) that provide standardized third-party capabilities.                                                                                                                                                                                                                                                                                                        |
| `skills`      | [Skills](/docs/en/managed-agents/skills) that supply domain-specific context with progressive disclosure.                                                                                                                                                                                                                                                                                                       |
| `multiagent`  | A coordinator declaration listing the agents this agent can delegate to. See [Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration).                                                                                                                                                                                                                                                      |
| `description` | A description of what the agent does.                                                                                                                                                                                                                                                                                                                                                                           |
| `metadata`    | Arbitrary key-value pairs for your own tracking.                                                                                                                                                                                                                                                                                                                                                                |

You can also override `model`, `system`, `tools`, `mcp_servers`, and `skills` for a single session without changing the agent. An `effort` level set inside a per-session `model` override isn't applied; set it on the agent instead. See [Override agent configuration for a session](/docs/en/managed-agents/sessions#override-agent-configuration-for-a-session).




Create an agent

The following example defines a coding agent that uses Claude Opus 5 with access to the pre-built agent toolset. The toolset lets the agent write code, read files, search the web, and more. See the [agent tools reference](/docs/en/managed-agents/tools) for the full list of supported tools.

The examples use curl, the `ant` CLI, or one of the SDKs. If you haven't set one up, the [quickstart](/docs/en/managed-agents/quickstart#install-the-cli) covers installation and client setup.

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
agent=$(ant beta:agents create \
  --name "Coding Assistant" \
  --model '{id: claude-opus-5}' \
  --system "You are a helpful coding agent." \
  --tool '{type: agent_toolset_20260401}' \
  --format json)

AGENT_ID=$(jq -r '.id' <<< "$agent")
AGENT_VERSION=$(jq -r '.version' <<< "$agent")
```



To use Claude Opus 5 or Claude Opus 4.8 with [fast mode](/docs/en/build-with-claude/fast-mode), pass `model` as an object, for example: `{"id": "claude-opus-5", "speed": "fast"}`. See [Fast mode](/docs/en/build-with-claude/fast-mode#supported-models) for supported models.



To set the model's effort level, pass `model` as an object, for example: `{"id": "claude-opus-5", "effort": "high"}`. The `effort` field accepts a level string (`low`, `medium`, `high`, `xhigh`, or `max`) or an object such as `{"type": "high"}`. See [Effort levels](/docs/en/build-with-claude/effort#effort-levels) for what each level does.

The response echoes your configuration and adds `id`, `type`, `version`, `created_at`, `updated_at`, and `archived_at` fields, and fills in `model` fields you omit, such as `effort`, with their defaults. The `version` starts at 1 and increments each time an update changes the agent.

```python
{
  "id": "agent_01HqR2k7vXbZ9mNpL3wYcT8f",
  "type": "agent",
  "name": "Coding Assistant",
  "model": {
    "id": "claude-opus-5",
    "effort": { "type": "high" },
    "speed": "standard"
  },
  "system": "You are a helpful coding agent.",
  "description": null,
  "tools": [
    {
      "type": "agent_toolset_20260401",
      "default_config": {
        "permission_policy": { "type": "always_allow" }
      }
    }
  ],
  "skills": [],
  "mcp_servers": [],
  "metadata": {},
  "version": 1,
  "created_at": "2026-04-03T18:24:10.412Z",
  "updated_at": "2026-04-03T18:24:10.412Z",
  "archived_at": null
}
```



The `default_config` on the toolset shows its default [permission policy](/docs/en/managed-agents/permission-policies), `always_allow`, which applies unless you configure one.




Update an agent

Updating an agent generates a new version when the configuration changes. The `version` field is optional: supply it for optimistic concurrency (a mismatch returns a 409), or omit it to apply the update unconditionally (last write wins). Updates to archived agents are rejected.

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
ant beta:agents update \
  --agent-id "$AGENT_ID" \
  --version "$AGENT_VERSION" \
  --system "You are a helpful coding agent. Always write tests."
```

The preceding example supplies `version` from the create response, so the update only applies if nothing else has changed the agent since you read it. To apply an update unconditionally, omit `version` from the request:

curl



```python
updated_agent=$(curl -fsSL "https://api.anthropic.com/v1/agents/$AGENT_ID" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{
    "description": "Writes and reviews code."
  }')

echo "New version: $(jq -r '.version' <<< "$updated_agent")"
```




Update semantics

- **`version`** is optional and must be at least 1 when supplied. When supplied, the request returns a 409 if it doesn't match the agent's current version, even when the fields you send already match the stored values; re-read the agent and retry. When omitted, the update applies unconditionally and the most recent update silently replaces any concurrent one, with no error to either caller. Supplying `version` is the recommended default for interactive callers, and omitting it fits declarative apply loops, such as a CI job that syncs checked-in agent definitions, where the loop owns the agent.

- **Omitted fields are preserved.** You only need to include the fields you want to change.

- **Scalar fields** (`model`, `system`, `name`, `description`) are replaced with the new value. `system` and `description` can be cleared by passing `null`. `model` and `name` are mandatory and cannot be cleared. Within a `model` object you supply, `effort` is the exception: if the model `id` is unchanged, omitting `effort` leaves the stored effort level unchanged. If you change the model `id`, an omitted `effort` resets to the new model's default.

- **Array fields** (`tools`, `mcp_servers`, `skills`) are fully replaced by the new array. To clear an array field entirely, pass `null` or an empty array.

- **`multiagent`** is replaced as a whole, including its `agents` roster. Pass `null` to clear it.

- **Metadata** is merged at the key level. Keys you provide are added or updated. Keys you omit are preserved. To delete a specific key, set its value to `null`.

- **No-op detection.** If the update produces no change relative to the current version, no new version is created and the existing version is returned.

- **Coordinator rosters are not updated.** Coordinators that reference this agent in their `multiagent.agents` roster keep the version that was pinned when the coordinator was created or last updated, even if the reference omits `version`. To delegate to the new version, [update the coordinator](/docs/en/managed-agents/multiagent-orchestration#configure-the-coordinator) so its roster references it.




Agent lifecycle

| Operation         | Behavior                                                                                            |
|-------------------|-----------------------------------------------------------------------------------------------------|
| **Update**        | Generates a new agent version when the configuration changes.                                       |
| **List versions** | Returns the full version history so you can track changes over time.                                |
| **Archive**       | Makes the agent read-only. New sessions cannot reference it, but existing sessions continue to run. |




List versions

Fetch the full version history to track how an agent has changed over time. Results are paginated, and the SDK examples fetch every page automatically.

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
ant beta:agents:versions list --agent-id "$AGENT_ID"
```




Archive an agent

Archiving makes the agent read-only and cannot be undone. Existing sessions continue to run, but new sessions cannot reference the agent. The response sets `archived_at` to the archive timestamp.

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
ant beta:agents archive --agent-id "$AGENT_ID"
```




Next steps




Tools

Configure tools available to your agent.




Skills

Attach reusable, filesystem-based expertise to your agent for domain-specific workflows.




Start a session

Create a session to run your agent and begin executing tasks.




Reference

Event types, self-hosted worker CLI flags, supported MCP server types, rate limits, and branding guidelines for Claude Managed Agents.
