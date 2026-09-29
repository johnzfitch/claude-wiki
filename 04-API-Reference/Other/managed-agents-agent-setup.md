---
title: "Define your agent - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/agent-setup"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:38Z"
tags: ["agents", "api"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fagent-setup)

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

[Managed Agents](managed-agents-overview.md)Define your agent

# Define your agent

Copy page



Create a reusable, versioned agent configuration.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

An agent is a reusable, versioned configuration that defines persona and capabilities. It bundles the model, system prompt, tools, MCP servers, and skills that shape how Claude behaves during a session.

Create the agent once as a reusable resource and reference it by ID each time you [start a session](managed-agents-sessions.md). Agents are versioned and easier to manage across many sessions.

## Agent configuration fields

| Field         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`        | Required. A human-readable name for the agent.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `model`       | Required. The Claude [model](../../20-Models/about-claude-models-overview.md) that powers the agent. Accepts a model ID string or an object, for example `{"id": "claude-opus-5"}`. Claude 4.5 and later models are supported. The object form also accepts `speed`, `effort`, and `inference_geo` fields; see the tips under [Create an agent](#create-an-agent), [Effort levels](../Guides/build-with-claude-effort.md#effort-levels), and [Pin the inference geo](#pin-the-inference-geo). |
| `system`      | A [system prompt](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#give-claude-a-role) that defines the agent's behavior and persona. The system prompt is distinct from [user messages](managed-agents-reference.md#event-types), which should describe the work to be done.                                                                                                                                                   |
| `tools`       | The tools available to the agent. Combines [pre-built agent tools](managed-agents-tools.md), [MCP tools](managed-agents-mcp-connector.md), and [custom tools](managed-agents-tools.md#custom-tools).                                                                                                                                                                                                                                             |
| `mcp_servers` | [MCP servers](managed-agents-mcp-connector.md) that provide standardized third-party capabilities.                                                                                                                                                                                                                                                                                                                                                           |
| `skills`      | [Skills](managed-agents-skills.md) that supply domain-specific context with progressive disclosure.                                                                                                                                                                                                                                                                                                                                                          |
| `multiagent`  | A coordinator declaration listing the agents this agent can delegate to. See [Multiagent orchestration](managed-agents-multiagent-orchestration.md).                                                                                                                                                                                                                                                                                                         |
| `description` | A description of what the agent does.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `metadata`    | Arbitrary key-value pairs for your own tracking.                                                                                                                                                                                                                                                                                                                                                                                                                   |

You can also override `model`, `system`, `tools`, `mcp_servers`, and `skills` for a single session without changing the agent. A `model` override replaces the agent's `model` object in full, so the agent's own `effort` isn't carried over. To run the session at a specific effort level, set `effort` inside the override's `model` object. See [Override agent configuration for a session](managed-agents-sessions.md#override-agent-configuration-for-a-session).

## Create an agent

The following example defines a coding agent that uses Claude Opus 5 with access to the pre-built agent toolset. The toolset lets the agent write code, read files, search the web, and more. See the [agent tools reference](managed-agents-tools.md) for the full list of supported tools.

The examples use curl, the `ant` CLI, or one of the SDKs. If you haven't set one up, the [quickstart](managed-agents-quickstart.md#install-the-cli) covers installation and client setup.

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
ant apply coding-assistant.md
```

coding-assistant.md





```python
---
name: Coding Assistant
model: claude-opus-5-5
tools:
  - type: agent_toolset_20260401
---

You are a helpful coding agent.
```

[`ant apply`](cli-sdks-libraries-cli-apply.md) creates the agent from `coding-assistant.md`, prints its ID, and records it in `claude-lock.json`. Commit `claude-lock.json` so the next `ant apply` updates this agent instead of creating a second one.

The response echoes your configuration and adds `id`, `type`, `version`, `created_at`, `updated_at`, and `archived_at` fields, and fills in `model` fields you omit, such as `effort`, with their defaults. The `version` starts at 1 and increments each time an update changes the agent.

```python
{
  "id": "agent_01HqR2k7vXbZ9mNpL3wYcT8f",
  "type": "agent",
  "name": "Coding Assistant",
  "model": {
    "id": "claude-opus-5-5",
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
  "multiagent": null,
  "metadata": {},
  "version": 1,
  "created_at": "2026-04-03T18:24:10.412Z",
  "updated_at": "2026-04-03T18:24:10.412Z",
  "archived_at": null
}
```



The `default_config` on the toolset shows its default [permission policy](managed-agents-permission-policies.md), `always_allow`, which applies unless you configure one.



To use Claude Opus 5.5, Claude Opus 5, or Claude Opus 4.8 with [fast mode](../Guides/build-with-claude-fast-mode.md), pass `model` as an object, for example: `{"id": "claude-opus-5", "speed": "fast"}`. See the fast mode page's [supported models](../Guides/build-with-claude-fast-mode.md#supported-models).



To set the model's effort level, pass `model` as an object, for example: `{"id": "claude-opus-5", "effort": "high"}`. The `effort` field accepts a level string (`low`, `medium`, `high`, `xhigh`, or `max`) or an object such as `{"type": "high"}`. See [Effort levels](../Guides/build-with-claude-effort.md#effort-levels) for what each level does.

### Pin the inference geo

Like `speed` and `effort`, `inference_geo` is set through the object form of `model`: pass `model` as an object and set `inference_geo` alongside `id`. The field accepts `"us"` or `"global"`. When it's unset, each model request follows the workspace's default inference geo at the time it's served. See [Data residency](../Guides/build-with-claude-data-residency.md) for the workspace-level geo controls and pricing.

The following example pins an agent to US inference and prints the `inference_geo` value from the agent's `model` object:

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
ant apply geo-pinned-assistant.md
```

geo-pinned-assistant.md





```python
---
name: Geo-pinned assistant
model:
  id: claude-opus-5-5
  inference_geo: us
---

You are a helpful assistant.
```

An `inference_geo` pin is validated against the workspace's [`allowed_inference_geos`](../Guides/build-with-claude-data-residency.md#workspace-level-restrictions) when the agent is saved, when a session is created from it, and on every turn the session serves. If the workspace allowlist narrows so a pin is no longer allowed, new sessions can't be created from the agent and running sessions refuse further turns; pins are never exempted, because workspaces rely on them for compliance and data residency.

Setting `inference_geo` on a model that doesn't support geographic inference pinning returns a 400 error; see [Model availability](../Guides/build-with-claude-data-residency.md#model-availability) for the models that do. In a `multiagent` configuration, the coordinator's pin and every roster member's must all be set to the same value or all be unset; see [Multiagent orchestration](managed-agents-multiagent-orchestration.md). To change or clear the pin later, update the agent's `model` object; supplying `model` without `inference_geo` clears it, as described under [Update semantics](#update-semantics).

## Update an agent

Updating an agent generates a new version when the configuration changes. The `version` field is optional: supply it for optimistic concurrency (a mismatch returns a 409), or omit it to apply the update unconditionally (last write wins). Updates to archived agents are rejected.

With the CLI, edit the agent's file and run `ant apply` again; apply supplies `version` for you.

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
ant apply coding-assistant.md
```

coding-assistant.md





```python
---
name: Coding Assistant
model: claude-opus-5-5
tools:
  - type: agent_toolset_20260401
---

You are a helpful coding agent. Always write tests.
```

The preceding example supplies `version` from the create response, so the update only applies if nothing else has changed the agent since you read it. To apply an update unconditionally, omit `version` from the request:

cURL

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

### Update semantics

- **`version`** is optional and must be at least 1 when supplied. When supplied, the request returns a 409 if it doesn't match the agent's current version, even when the fields you send already match the stored values; re-read the agent and retry. When omitted, the update applies unconditionally and the most recent update silently replaces any concurrent one, with no error to either caller. Supplying `version` is the recommended default for interactive callers, and omitting it fits declarative apply loops, such as a CI job that syncs checked-in agent definitions, where the loop owns the agent.

- **Omitted fields are preserved.** You only need to include the fields you want to change.

- **Scalar fields** (`model`, `system`, `name`, `description`) are replaced with the new value. `system` and `description` can be cleared by passing `null`. `model` and `name` are mandatory and cannot be cleared. Within a `model` object you supply, `effort` is the sole exception: if the model `id` is unchanged, omitting `effort` leaves the stored effort level unchanged. If you change the model `id`, an omitted `effort` resets to the new model's default. Other `model` fields are replaced along with the object: supplying `model` without `inference_geo` clears the agent's inference geo pin.

- **Array fields** (`tools`, `mcp_servers`, `skills`) are fully replaced by the new array. To clear an array field entirely, pass `null` or an empty array.

- **`multiagent`** is replaced as a whole, including its `agents` roster. Pass `null` to clear it.

- **Metadata** is merged at the key level. Keys you provide are added or updated. Keys you omit are preserved. To delete a specific key, set its value to `null`.

- **No-op detection.** If the update produces no change relative to the current version, no new version is created and the existing version is returned.

- **Coordinator rosters are not updated.** Coordinators that reference this agent in their `multiagent.agents` roster keep the version that was pinned when the coordinator was created or last updated, even if the reference omits `version`. To delegate to the new version, [update the coordinator](managed-agents-multiagent-orchestration.md#configure-the-coordinator) so its roster references it.

## Agent lifecycle

| Operation         | Behavior                                                                                            |
|-------------------|-----------------------------------------------------------------------------------------------------|
| **Update**        | Generates a new agent version when the configuration changes.                                       |
| **List versions** | Returns the full version history so you can track changes over time.                                |
| **Archive**       | Makes the agent read-only. New sessions cannot reference it, but existing sessions continue to run. |

### List versions

Fetch the full version history to track how an agent has changed over time. Results are paginated, and the SDK examples fetch every page automatically.

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
for version in client.beta.agents.versions.list(agent.id):
    print(f"Version {version.version}: {version.updated_at.isoformat()}")
```

### Archive an agent

Archiving makes the agent read-only and cannot be undone. Existing sessions continue to run, but new sessions cannot reference the agent. The response sets `archived_at` to the archive timestamp.

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
archived = client.beta.agents.archive(agent.id)

print(f"Archived at: {archived.archived_at.isoformat()}")
```

## Next steps



[Tools](managed-agents-tools.md)

Configure tools available to your agent.



[Skills](managed-agents-skills.md)

Attach reusable, filesystem-based expertise to your agent for domain-specific workflows.



[Start a session](managed-agents-sessions.md)

Create a session to run your agent and begin executing tasks.



[Reference](managed-agents-reference.md)

Event types, self-hosted worker CLI flags, supported MCP server types, rate limits, and branding guidelines for Claude Managed Agents.
