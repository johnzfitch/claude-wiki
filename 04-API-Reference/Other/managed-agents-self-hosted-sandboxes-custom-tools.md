---
title: "Custom tools in self-hosted sandboxes - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools"
category: "04-API-Reference/Other"
fetched_at: "2026-10-19T06:28:31Z"
tags: ["api", "mcp"]
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fself-hosted-sandboxes-custom-tools)

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

[Overview and quickstart](managed-agents-self-hosted-sandboxes.md)[Deploy workers](managed-agents-self-hosted-sandboxes-workers.md)[Memory stores](managed-agents-self-hosted-sandboxes-memory.md)[Custom tools and MCP servers](managed-agents-self-hosted-sandboxes-custom-tools.md)[Monitor and troubleshoot](managed-agents-self-hosted-sandboxes-operations.md)[Worker reference](managed-agents-self-hosted-sandboxes-reference.md)[Security model](managed-agents-self-hosted-sandboxes-security.md)

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

[Managed Agents](managed-agents-overview.md)Self-hosted sandboxes

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Custom tools in self-hosted sandboxes

Copy page



Serve custom tools from a self-hosted sandbox worker, and wrap an MCP server inside your network as custom tools without running a tunnel.

Copy page



[Custom tools](managed-agents-tools.md#custom-tools) are tools your own code executes: the agent emits an `agent.custom_tool_use` event and waits for a matching `user.custom_tool_result`. Your worker can be that code. Because it runs inside your sandbox, the tool reaches the internal services, credentials, and network egress you configured for the sandbox, and nothing more.

The environment key authorizes posting custom tool results, so your Claude API key stays off the worker host.



Serving custom tools requires the SDK worker. The `ant` CLI worker has no way to register a custom tool implementation. In the sandbox-per-session pattern, [run the SDK worker inside the sandbox](managed-agents-self-hosted-sandboxes-workers.md#run-the-sdk-worker-inside-the-sandbox).

## Serve a custom tool

1.  1

    ### Declare the tool on the agent

    Add a `custom` entry to the agent's `tools` whose `name` matches the tool your worker registers. See [Custom tools](managed-agents-tools.md#custom-tools) for the full declaration shape.

    ``` shiki
    {
      "type": "custom",
      "name": "get_order_status",
      "description": "Look up an order in the internal fulfillment system by order ID.",
      "input_schema": {
        "type": "object",
        "properties": {
          "order_id": { "type": "string", "description": "The order ID" }
        },
        "required": ["order_id"]
      }
    }
    ```

    

2.  2

    ### Register the implementation with the worker

    Pass the tool through the worker's `tools` factory (see [`EnvironmentWorker`](managed-agents-self-hosted-sandboxes-reference.md#environment-worker)), alongside the built-in toolset:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    import asyncio
    import os
    from anthropic import AsyncAnthropic, beta_async_tool
    from anthropic.lib.environments import EnvironmentWorker
    from anthropic.lib.tools.agent_toolset import beta_agent_toolset_20260401


    @beta_async_tool
    async def get_order_status(order_id: str) -> str:
        """Look up an order in the internal fulfillment system by order ID."""
        # Runs on the worker host: call anything the sandbox can reach.
        return f"Order {order_id}: shipped"


    async def main() -> None:
        environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
        environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
        async with AsyncAnthropic(auth_token=environment_key) as client:
            await EnvironmentWorker(
                client,
                environment_id=environment_id,
                environment_key=environment_key,
                workdir="/workspace",
                tools=lambda env: [*beta_agent_toolset_20260401(env), get_order_status],
            ).run()


    asyncio.run(main())
    ```

The worker answers only the tools registered with it. If a tool is declared on the agent but no worker or client serves it, the session pauses with a `requires_action` stop reason. It stays paused until something posts the result. See [Answer tool calls that pause the session](managed-agents-events-and-streaming.md#answer-tool-calls-that-pause-the-session) for the event flow.

## Wrap an MCP server as custom tools

The [MCP connector](managed-agents-mcp-connector.md) connects to MCP servers from Anthropic's side. A server must therefore expose an HTTP endpoint that Anthropic can reach, directly or through an [MCP tunnel](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md).

To use a server that only your network can reach, make the worker the MCP client instead and declare the server's tools as custom tools. The MCP server needs no inbound connectivity from outside your network. Anthropic receives the tool definitions you declare on the agent, each call's input, and the result your worker posts back.

At runtime the model calls a wrapped tool like any other custom tool:

1.  The agent emits an `agent.custom_tool_use` event.
2.  The worker, inside your sandbox, forwards the call over its open MCP session to the server on your network.
3.  The worker posts the server's response as the `user.custom_tool_result`.

### Install an MCP SDK

The SDK's [Client-side MCP helpers](../Agents-Tools/agents-and-tools-mcp-connector.md#client-side-mcp-helpers) convert the server's tools into the runnable tools the worker accepts. Install an MCP SDK alongside the Anthropic SDK: `pip install "anthropic[mcp]" "mcp>=1.24"`.

The examples connect without authentication. To send credentials, configure the `http_client` you hand to the MCP transport.

### Declare and serve the tools

1.  1

    ### Declare the server's tools on the agent

    List the MCP server's tools and declare each one as a `custom` tool. The MCP `name`, `description`, and `inputSchema` map one to one onto the custom tool's fields. If the server paginates its tool list, declare every page; the worker must list the same pages.

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    import asyncio
    from typing import Any, cast
    from anthropic import AsyncAnthropic
    from anthropic.types.beta import BetaManagedAgentsCustomToolParams
    from mcp import ClientSession, types
    # Requires mcp >= 1.24, which renamed streamablehttp_client to streamable_http_client.
    from mcp.client.streamable_http import streamable_http_client

    MCP_SERVER_URL = "http://mcp.internal.example.com:8000/mcp"


    def to_custom_tool(tool: types.Tool) -> BetaManagedAgentsCustomToolParams:
        # The MCP fields map one to one onto a custom tool declaration. The cast
        # hands the schema dictionary to the SDK's typed parameter unchanged.
        return {
            "type": "custom",
            "name": tool.name,
            "description": tool.description or tool.name,
            "input_schema": cast(Any, tool.inputSchema),
        }


    async def main() -> None:
        # Run this wherever you create agents, not on the worker host: it
        # authenticates with your Claude API key (ANTHROPIC_API_KEY).
        async with (
            streamable_http_client(MCP_SERVER_URL) as (read, write, _),
            ClientSession(read, write) as mcp_session,
            AsyncAnthropic() as client,
        ):
            await mcp_session.initialize()
            listed = await mcp_session.list_tools()
            agent = await client.beta.agents.create(
                name="Internal tools agent",
                model="claude-opus-5-5",
                tools=[
                    {"type": "agent_toolset_20260401"},
                    *[to_custom_tool(tool) for tool in listed.tools],
                ],
            )
            print(agent.id)


    asyncio.run(main())
    ```

2.  2

    ### Serve the tools from the worker

    Connect to the same MCP server at startup, convert its tools with `async_mcp_tool`, and register them alongside `beta_agent_toolset_20260401`. Keep one MCP session open for the life of the worker.

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    import asyncio
    import os
    from datetime import timedelta
    from anthropic import AsyncAnthropic
    from anthropic.lib.environments import EnvironmentWorker
    from anthropic.lib.tools.agent_toolset import beta_agent_toolset_20260401
    from anthropic.lib.tools.mcp import async_mcp_tool
    from mcp import ClientSession
    # Requires mcp >= 1.24, which renamed streamablehttp_client to streamable_http_client.
    from mcp.client.streamable_http import streamable_http_client

    MCP_SERVER_URL = "http://mcp.internal.example.com:8000/mcp"


    async def main() -> None:
        environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
        environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
        # Connect to the MCP server once at startup and keep the session open for
        # the life of the worker. The timeout turns a hung tool call into an error
        # result instead of a stalled call.
        async with (
            streamable_http_client(MCP_SERVER_URL) as (read, write, _),
            ClientSession(read, write, read_timeout_seconds=timedelta(seconds=60)) as mcp_session,
            AsyncAnthropic(auth_token=environment_key) as client,
        ):
            await mcp_session.initialize()
            listed = await mcp_session.list_tools()
            mcp_tools = [async_mcp_tool(tool, mcp_session) for tool in listed.tools]
            await EnvironmentWorker(
                client,
                environment_id=environment_id,
                environment_key=environment_key,
                workdir="/workspace",
                tools=lambda env: [*beta_agent_toolset_20260401(env), *mcp_tools],
            ).run()


    asyncio.run(main())
    ```

## Limits and behavior

### Tools are declared, not discovered at runtime

The worker lists the MCP server's tools once at startup and cannot add tools to a running session. When the server's tools change:

1.  Declare them again, on the agent or on an idle session through [Updating the agent configuration](managed-agents-session-operations.md#updating-the-agent-configuration).
2.  Restart the worker.

### Declarations must fit the Managed Agents API

The MCP helpers keep the server's names and descriptions, and most schemas pass through unchanged. Rename, trim, or inline where a declaration breaks one of these rules:

| Field                     | Rule                                                                                                                                                                                                                                                                                          |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`                    | Unique per agent. Letters, digits, underscores, and hyphens, 1–128 characters. Cannot match a built-in agent tool such as `bash` or `read`, or use the reserved `mcp__` prefix or `ant__` prefix.                                                                                             |
| `description`             | Required and non-empty.                                                                                                                                                                                                                                                                       |
| `input_schema`            | Accepts the JSON Schema keywords MCP servers commonly emit, such as `additionalProperties` and `title`. Rejects reference keywords such as `$ref` anywhere, and top-level `oneOf`, `anyOf`, and `allOf`. Property names use letters, digits, underscores, dots, and hyphens, 1–64 characters. |
| The agent's `tools` array | At most 256 entries. Each wrapped tool is one entry, and the built-in toolset is one more.                                                                                                                                                                                                    |

Two cases need extra work:

- **Two servers expose the same tool name:** Define the wrapper yourself under a prefixed name and have it call the server's original tool name.
- **A generator such as pydantic factors schemas into `$defs`:** Inline those schemas before you declare the tool.

### Tool failures surface as error tool results

When the MCP server reports a tool error, the worker posts an error tool result the model can react to. MCP content with no tool result equivalent, such as audio blocks and resource links, also surfaces as an error.

Set a timeout on the MCP client for a faster and clearer failure, as the Python worker example does with `read_timeout_seconds`. See [A wrapped MCP tool call hangs](managed-agents-self-hosted-sandboxes-operations.md#a-wrapped-mcp-tool-call-hangs) for what happens without one.

### Wrap only servers you operate or trust

A wrapped tool's name, description, and results enter the model's context like any other tool's. They are untrusted input that can influence what the agent does with its other tools, including `bash` on the worker host. Declare only the tools you intend the agent to use.

### Permission policies do not apply

[Permission policies](managed-agents-permission-policies.md#custom-tools) govern the built-in and MCP toolsets. The worker executes every wrapped tool call the model makes, so put any approval step in your own tool code.
