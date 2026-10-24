---
title: "Tools - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/tools"
category: "04-API-Reference/Other"
fetched_at: "2026-10-20T06:40:29Z"
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Ftools)

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

[Managed Agents](managed-agents-overview.md)Define your agent

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Tools

Copy page



Configure tools available to your agent.

Copy page



Claude Managed Agents provides a set of built-in tools that Claude can use autonomously within a [session](managed-agents-sessions.md). You control which tools are available by specifying them in the agent configuration.

Claude Managed Agents also supports custom, user-defined tools. Your application executes these tools separately and returns the results to Claude, which uses them to continue the task. To give the agent tools from an MCP server, use the [MCP connector](managed-agents-mcp-connector.md) instead.

## Available tools

The agent toolset includes the following tools. All are enabled by default when you include the toolset in the agent configuration.

| Tool       | Name         | Description                                    |
|------------|--------------|------------------------------------------------|
| Bash       | `bash`       | Execute bash commands in a shell session       |
| Read       | `read`       | Read a file from the sandbox filesystem        |
| Write      | `write`      | Write a file to the sandbox filesystem         |
| Edit       | `edit`       | Perform string replacement in a file           |
| Glob       | `glob`       | Fast file pattern matching using glob patterns |
| Grep       | `grep`       | Text search using regex patterns               |
| Web fetch  | `web_fetch`  | Fetch content from a URL                       |
| Web search | `web_search` | Search the web for information                 |

When a tool output exceeds 100,000 characters (about 25,000 tokens), it is automatically written to a file in the [sandbox](managed-agents-environments.md). The model receives a truncated preview with the file path and can read the full content from there.

## Configuring the toolset

Enable the full toolset with `agent_toolset_20260401` when creating an agent. Use the `configs` array to disable specific tools or override their settings. Each entry is identified by its `name`, which takes a value from the Name column in [Available tools](#available-tools). An entry also accepts an optional `type` field with the same value.

Each config entry can also set a `permission_policy`. The policy controls whether the tool's calls run without confirmation, require confirmation, or are evaluated individually by the server. See [Permission policies](managed-agents-permission-policies.md) for the available policy types.

The following example enables the toolset and disables `web_fetch`:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

CLI



```python
ant apply agent.md
```

agent.md





```python
---
name: Coding Assistant
model: claude-opus-5-5
tools:
  - type: agent_toolset_20260401
    configs:
      - name: web_fetch
        enabled: false
---
```

### Disabling specific tools

To disable a tool, set `enabled: false` in its `configs` entry:

```python
{
  "type": "agent_toolset_20260401",
  "configs": [
    { "name": "web_fetch", "enabled": false },
    { "name": "web_search", "enabled": false }
  ]
}
```



### Enabling only specific tools

The `default_config` object sets the baseline for every tool in the set, and per-tool `configs` entries override it. To start with everything off and enable only what you need, set `default_config.enabled` to `false`:

```python
{
  "type": "agent_toolset_20260401",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "bash", "enabled": true },
    { "name": "read", "enabled": true },
    { "name": "write", "enabled": true }
  ]
}
```



### Restricting web search and web fetch

The `web_search` and `web_fetch` entries also accept domain lists, a cap on fetched content, and a search location. See [Restrict web search and web fetch domains](managed-agents-tools-web-restrictions.md).

### Config entry types in the SDKs

The Python, TypeScript, Go, Java, C#, Ruby, and PHP SDKs type each `configs` entry per tool. The type is a union with one member per built-in tool, discriminated by `type`.

In Go, Java, C#, and PHP, you construct entries from typed values rather than plain dictionaries or hashes. In those SDKs, the element type of `configs` is the union itself, so build each entry from its per-tool member type.

You can omit `type` when you construct an entry, because the server infers it from `name`. Responses always include it. This typing does not change the JSON that an entry serializes to. A request whose entries set only `name`, `enabled`, and `permission_policy` is valid with or without `type`.

## Custom tools

Custom tools are analogous to [user-defined client tools](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md#user-defined-tools-client-executed) in the Messages API. You specify what operations are available and what they return, and Claude determines when and how to call them.

Claude does not run a custom tool itself. It emits a structured request, your code runs the operation, and you return the result to the session.

The following example creates an agent with the built-in toolset and one custom tool, `get_weather`:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

CLI



```python
ant apply agent.md
```

agent.md





```python
---
name: Weather Agent
model: claude-opus-5-5
tools:
  - type: agent_toolset_20260401
  - type: custom
    name: get_weather
    description: Get current weather for a location
    input_schema:
      type: object
      properties:
        location:
          type: string
          description: City name
      required:
        - location
---
```

A custom tool's name can't start with `mcp__` or `ant__`, or match the name of a built-in agent tool. A request that breaks this rule returns a 400 error. An agent that already has a custom tool whose name starts with `ant__` accepts an update only if the update sends `tools` without that name, so rename or remove the tool in your next update. A new session is refused with a 400 error if such a tool is on its agent (after any [overrides](managed-agents-sessions.md#override-agent-configuration-for-a-session)), on an agent in the `predefined_agents` list of `subagents`, or on an agent in the `predefined_agents` list of `workflows`. Sessions that already exist aren't affected.

The agent calls its custom tools during a session. To receive the calls and return results, see [Session event stream](managed-agents-events-and-streaming.md#handling-custom-tool-calls).

For sessions that run in a self-hosted sandbox, the environment worker can [serve custom tools from the sandbox](managed-agents-self-hosted-sandboxes-custom-tools.md). These can include tools that wrap an MCP server inside your network.

### Best practices for custom tool definitions

- **Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. The more context you can give Claude about your tools, the better it is at determining when and how to use them. Aim for three to four sentences for each tool description, more if the tool is complex. Your descriptions should cover:
  - What the tool does
  - When to use it, and when not to
  - What each parameter means and how it affects the tool's behavior
  - Any important caveats or limitations
- **Consolidate related operations into fewer tools.** Group actions such as `create_pr`, `review_pr`, and `merge_pr` into a single tool with an `action` parameter. Fewer, more capable tools reduce selection ambiguity and make your tool surface easier for Claude to navigate.
- **Use meaningful namespacing in tool names.** When your tools span multiple services or resources, prefix names with the resource (for example, `db_query` or `storage_read`). This makes tool selection unambiguous as your library grows.
- **Design tool responses to return only high-signal information.** Return semantic, stable identifiers (for example, slugs or UUIDs) rather than opaque internal references. Include only the fields Claude needs to determine its next step. Bloated responses waste context and make it harder for Claude to extract what matters.

## Next steps



[Restrict web search and web fetch domains](managed-agents-tools-web-restrictions.md)

Control which sites the web tools can reach, cap fetched content, and localize search results.



[MCP connector](managed-agents-mcp-connector.md)

Connect MCP servers to your agents for access to external tools and data sources.



[Permission policies](managed-agents-permission-policies.md)

Control when agent and MCP tools execute.



[Session event stream](managed-agents-events-and-streaming.md)

Send events, stream responses, and interrupt or redirect your session mid-execution.
