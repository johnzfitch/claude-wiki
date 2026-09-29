---
title: "Permission policies - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/permission-policies"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:41Z"
tags: ["api"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fpermission-policies)

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

# Permission policies

Copy page



Control when agent and MCP tools execute.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

Permission policies control whether server-executed tools (the pre-built agent toolset and MCP toolset) run automatically, wait for your approval, or have each call evaluated by the server. Custom tools are executed by your application and controlled by you, so they are not governed by permission policies.

## Permission policy types

| Policy         | Behavior                                                                                                                                                                               |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `always_allow` | The tool executes automatically with no confirmation.                                                                                                                                  |
| `always_ask`   | The session pauses and waits for your approval before executing. See [Respond to confirmation requests](#respond-to-confirmation-requests) for the event flow.                         |
| `auto`         | The server evaluates each call and runs it, denies it, or pauses for your approval. See [Let the server evaluate each call with `auto`](#let-the-server-evaluate-each-call-with-auto). |

Each toolset kind has its own default: the agent toolset defaults to `always_allow`, and MCP toolsets default to `always_ask`.

A permission policy controls when an enabled tool runs. To remove a tool from the agent entirely, disable it instead. See [Disabling specific tools](managed-agents-tools.md#disabling-specific-tools).

## Set a policy for a toolset

You set permission policies in the agent's `tools` configuration when you create the agent, and you can change them later by [updating the agent](managed-agents-agent-setup.md#update-an-agent). Running sessions keep the toolset configuration they were created with. Updates apply to sessions created afterward.

### Agent toolset permissions

When creating an agent, you can apply a policy to every tool in `agent_toolset_20260401` using `default_config.permission_policy`:

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
name: Coding Assistant
model: claude-opus-5-5
tools:
  - type: agent_toolset_20260401
    default_config:
      permission_policy:
        type: always_ask
---
```

`default_config` is optional. If you omit it, the agent toolset is enabled with the default permission policy, `always_allow`.

### MCP toolset permissions

MCP toolsets default to `always_ask`. This ensures that new tools added to an MCP server do not execute in your application without approval. To auto-approve tools from a trusted MCP server, set `default_config.permission_policy` on the `mcp_toolset` entry.

The `mcp_server_name` must match the `name` of a server in the `mcp_servers` array.

This example connects a GitHub MCP server and allows its tools to run without confirmation:

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
name: Dev Assistant
model: claude-opus-5-5
mcp_servers:
  - type: url
    name: github
    url: https://mcp.example.com/github
tools:
  - type: agent_toolset_20260401
  - type: mcp_toolset
    mcp_server_name: github
    default_config:
      permission_policy:
        type: always_allow
---
```

## Override an individual tool policy

Use the `configs` array to override the default for individual tools. The `name` values for the agent toolset are listed in [Available tools](managed-agents-tools.md#available-tools). This example allows the full agent toolset by default but requires confirmation before any bash command runs:

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
name: Coding Assistant
model: claude-opus-5-5
tools:
  - type: agent_toolset_20260401
    default_config:
      permission_policy:
        type: always_allow
    configs:
      - name: bash
        permission_policy:
          type: always_ask
---
```

Pass this `tools` configuration in the agent create request (the CLI tab shows the complete command). MCP toolsets support the same per-tool overrides, with `name` set to the tool name reported by the MCP server. See [Configure which MCP tools are available](managed-agents-mcp-connector.md#configure-which-mcp-tools-are-available).

## Let the server evaluate each call with `auto`

With the `auto` permission policy, the server evaluates each call before it runs. Because the evaluation considers the tool, the call's input, and the session's content up to that point, the server can treat two calls to the same tool differently. Each call has one of three outcomes:

- **The call runs.** When the server determines that the call is safe, the tool runs as it would under `always_allow`.
- **The call is denied.** When the server evaluates the call as high-risk, the tool does not run. The agent receives an error tool result with the content `Permission to use {tool_name} has been denied.` and `is_error: true`. The session keeps running, and your client cannot override the denial.
- **The call pauses for your approval.** When the server reaches no determination, the session pauses as it does under `always_ask`. See [Respond to confirmation requests](#respond-to-confirmation-requests).

To turn on `auto`, set `permission_policy` to `{"type": "auto"}`. It goes in the same two places as the other policies: a toolset's [`default_config`](#set-a-policy-for-a-toolset) for the whole toolset, or a [`configs` entry](#override-an-individual-tool-policy) for one tool. The agent toolset and MCP toolsets both accept it. No toolset uses `auto` by default.

The following example sets `auto` as the default for the agent toolset and for the `github` MCP toolset, and overrides `bash` to `always_ask`:

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
name: Ops Agent
model: claude-opus-5-5
mcp_servers:
  - type: url
    name: github
    url: https://mcp.example.com/github
tools:
  - type: agent_toolset_20260401
    default_config:
      permission_policy:
        type: auto
    configs:
      - name: bash
        permission_policy:
          type: always_ask
  - type: mcp_toolset
    mcp_server_name: github
    default_config:
      permission_policy:
        type: auto
---
```

What you post in `user.message` events counts as your intent, and it can lead the server to allow a call it would otherwise deny. The server does not read intent from a tool result, a fetched webpage, an MCP server's response, or a message between [session threads](managed-agents-multiagent-orchestration.md#tool-permissions-and-custom-tools). It assesses that content but does not take instructions from it. The server evaluates some calls as high-risk no matter who asks. If you relay untrusted end-user input in `user.message` events, the server reads that input as your intent too, and it can get a call allowed. Configure `always_ask` on the tools you would not let that end user run without review.



`auto` is not a human checkpoint. If the server determines that a call is safe, the call runs before anyone sees it, and its effects might not be reversible. If a person must review a tool's calls before they run, configure `always_ask` on that tool.

## See how each call was evaluated

Under any permission policy, each `agent.tool_use` and `agent.mcp_tool_use` event carries `evaluated_permission`, the outcome of the call's permission check: `"allow"`, `"ask"`, or `"deny"`. Most events also carry an `evaluation` object whose `type` names the policy that produced that outcome. Under `auto`, the object also records the server's determination, plus a `reason_code` when the outcome is `ask` or `deny`.

For example, when `bash` is under `auto` and the server evaluates a call as high-risk, the denied call appears on the event stream as follows:

```python
{
  "type": "agent.tool_use",
  "id": "sevt_01pqr...",
  "name": "bash",
  "input": {
    "command": "rm -rf /workspace/reports"
  },
  "evaluated_permission": "deny",
  "evaluation": {
    "type": "auto",
    "evaluated_permission": {
      "type": "deny",
      "reason_code": "high_risk"
    }
  },
  "processed_at": "2026-03-25T14:05:12Z"
}
```



The `evaluation` object takes one of the forms in the following table.

| `evaluation`                                                                                | Top-level `evaluated_permission` | Meaning                                                                                  |
|---------------------------------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------|
| `{"type": "always_allow"}`                                                                  | `"allow"`                        | The resolved policy is `always_allow`, so the call ran.                                  |
| `{"type": "always_ask"}`                                                                    | `"ask"`                          | The resolved policy is `always_ask`, so the call paused for your approval.               |
| `{"type": "auto", "evaluated_permission": {"type": "allow"}}`                               | `"allow"`                        | Under `auto`, the server determined that the call was safe, and it ran.                  |
| `{"type": "auto", "evaluated_permission": {"type": "ask", "reason_code": "indeterminate"}}` | `"ask"`                          | Under `auto`, the server reached no determination, so the call paused for your approval. |
| `{"type": "auto", "evaluated_permission": {"type": "deny", "reason_code": "high_risk"}}`    | `"deny"`                         | Under `auto`, the server evaluated the call as high-risk and denied it.                  |

When `evaluation.type` is `"auto"`, its nested `evaluated_permission.type` repeats the event's top-level `evaluated_permission`, so you can read the outcome from either field. A `reason_code` is a value for your client to branch on and keep in audit records, not text to display to end users.

`evaluation` is absent in two cases. When the agent names a tool that is not enabled in the session, the server denies the call without evaluating a policy: the event carries `evaluated_permission: "deny"` and no `evaluation`. Events recorded before `evaluation` was introduced also omit it: read those as `always_allow` when `evaluated_permission` is `"allow"` and as `always_ask` when it is `"ask"`.

Write your client to tolerate an `evaluation.type` or `reason_code` it does not recognize. `agent.custom_tool_use` events carry neither field, because permission policies do not govern [custom tools](#custom-tools).

## Respond to confirmation requests

A tool call evaluates to `ask` under an `always_ask` policy, or under `auto` when the server reaches no determination. When that happens:

1.  The session emits an `agent.tool_use` or `agent.mcp_tool_use` event.
2.  The session pauses with a `session.status_idle` event whose `stop_reason.type` is `requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array. The session waits indefinitely for a response.
3.  Send a `user.tool_confirmation` event for each blocking event, passing the event ID in the `tool_use_id` parameter. Set `result` to `"allow"` or `"deny"`. Use `deny_message` to explain a denial. You can send several confirmations in a single `events` request.
4.  Once all blocking events are resolved, the session transitions back to `running`. Allowed tools execute. Denied tools do not run, and the agent receives a tool result saying the call was rejected, including your `deny_message`.

If you send a `user.tool_confirmation` for an event whose `evaluated_permission` is not `ask`, the API rejects it with a 400 error. That includes calls the server denied under `auto`: your client cannot override them.

To answer interactively instead, use `ant beta:sessions connect`, which shows the waiting call and sends this event when you allow or deny it. See [Connect to a Managed Agents session from your terminal](cli-sdks-libraries-cli-sessions-connect.md#follow-and-steer-the-session).

In the following examples, the tool-use event IDs come from the `stop_reason.event_ids` array of the `session.status_idle` event. Learn more about receiving events in the [Session event stream](managed-agents-events-and-streaming.md#integrating-events) guide, or [subscribe to webhooks](managed-agents-webhooks.md) to be notified when a session pauses for input.

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
# Allow the tool to execute
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.tool_confirmation",
            "tool_use_id": agent_tool_use_event.id,
            "result": "allow",
        },
    ],
)

# Or deny it with an explanation
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.tool_confirmation",
            "tool_use_id": mcp_tool_use_event.id,
            "result": "deny",
            "deny_message": "Don't create issues in the production project. Use the staging project.",
        },
    ],
)
```

## Custom tools

Permission policies do not apply to custom tools. When the agent invokes a custom tool, your application receives an `agent.custom_tool_use` event and is responsible for deciding whether to execute it before sending back a `user.custom_tool_result`. See [Session event stream](managed-agents-events-and-streaming.md#handling-custom-tool-calls) for the full flow.

## Next steps



[Skills](managed-agents-skills.md)

Attach reusable, filesystem-based expertise to your agent for domain-specific workflows.



[Session event stream](managed-agents-events-and-streaming.md)

Send events, stream responses, and interrupt or redirect your session mid-execution.
