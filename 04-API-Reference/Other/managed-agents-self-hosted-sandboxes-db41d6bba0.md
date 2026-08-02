---
title: "Self-hosted sandboxes - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:41:22Z"
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

[Integration guide](/docs/en/managed-agents/self-hosted-sandboxes)[Security model](/docs/en/managed-agents/self-hosted-sandboxes-security)

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

Integration guide

Managed Agents/Self-hosted sandboxes

# Self-hosted sandboxes




Run Claude Managed Agents sessions in self-hosted sandboxes, keeping tool execution, files, and network egress in your own infrastructure.




By default, Managed Agents executes tools and code inside [Anthropic-managed cloud sandboxes](/docs/en/managed-agents/cloud-sandboxes-reference). Self-hosted sandboxes keep the orchestration on Anthropic's side but move tool execution into infrastructure you control, so the agent's code, filesystem, and network egress never leave your environment.

Tool execution stays on your host: the filesystem the agent reads and writes, the processes it spawns, and the network it can reach are all under your control. Tool inputs and outputs still flow to Anthropic's control plane (where Claude runs) so the model can see results and determine what to do next. See the [security model](/docs/en/managed-agents/self-hosted-sandboxes-security) for the full data-flow boundary.



Self-hosted sandboxes support all Claude models available in Managed Agents, including Claude Opus 4.8 and Claude Opus 5. The model is configured on the [agent](/docs/en/managed-agents/agent-setup), not the environment.




How it differs from cloud environments

|                               | Cloud environment           | Self-hosted sandbox |
|-------------------------------|-----------------------------|---------------------|
| Where tools run               | Anthropic-managed sandboxes | Your infrastructure |
| Network reach                 | Anthropic's egress controls | Your network policy |
| File and GitHub repo mounting | Managed by Anthropic        | Managed by you      |
| Lifecycle                     | Managed by Anthropic        | Managed by you      |

Self-hosting is a good fit when the agent needs to operate on data that cannot leave your network boundary, reach internal services that are not publicly routable, or run under your organization's own compliance and audit controls.

For Zero Data Retention and HIPAA BAA eligibility, see [API and data retention](/docs/en/manage-claude/api-and-data-retention#feature-eligibility).




When to combine with MCP tunnels

Self-hosting controls *where the agent's code executes*. [MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview) control *how Anthropic reaches MCP servers in your network*. They are independent: a session running in Anthropic's cloud sandboxes can still reach private MCP servers through a tunnel, and a self-hosted session can use either tunneled or public MCP servers. Use both when you want execution and tool access to stay inside your boundary. To give the agent tools from an MCP server inside your network without running a tunnel, you can also [wrap the server as custom tools](#wrap-an-mcp-server-as-custom-tools) served by your worker.




Environment worker



This guide describes how to build a worker with any generic sandboxing platform. Additional, platform-specific guides are available for [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations-claude-managed-agents.html), [Blaxel](https://docs.blaxel.ai/Tutorials/Claude-Managed-Agents), [Cloudflare](https://developers.cloudflare.com/sandbox/claude-managed-agents/), [Daytona](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents), [E2B](https://e2b.dev/docs/agents/claude-managed-agents), [GKE Agent Sandbox](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/anthropic-agent-sandbox), [Modal](https://github.com/modal-labs/claude-managed-agents-modal-sandbox), [Namespace](https://namespace.so/docs/integrations/claude), [Superserve](https://docs.superserve.ai/integrations/managed-agents/claude-managed-agents), and [Vercel](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox).

An environment worker is a process you run on your own infrastructure. It receives tool execution requests from Anthropic and runs them locally. The `self_hosted` environment acts as a work queue: when a [session](/docs/en/managed-agents/sessions) is assigned to it, Anthropic enqueues the session as a work item. Your worker claims work items from that queue, spawns an execution context for each one, downloads the agent's [skills](/docs/en/managed-agents/skills) (reusable, filesystem-based resources that give the agent domain-specific expertise), runs the tool calls, and posts the results back.

Work items are claimed by polling the environment's queue: either by an **always-on worker** that polls continuously, or a **webhook-triggered handler** that wakes on `session.status_run_started` and starts polling.

The CLI and SDK both ship pre-built workers. The `ant` CLI supports the always-on pattern only; the SDK supports both always-on and webhook-triggered. Both are configurable: see [Self-hosted worker](/docs/en/managed-agents/reference#self-hosted-worker) in the reference for CLI flags, and [SDK helpers](#sdk-helpers) on this page for the SDK options. For more control, call the [Environments Work endpoints](/docs/en/api/beta/environments/work) directly and implement your own worker.




Sandbox filesystem

- **`/workspace`:** the system default working directory for tool execution and skill download. The CLI's `--workdir` flag defaults to the current directory; pass `--workdir /workspace` to match the system default. Skills are downloaded to `<workdir>/skills/<name>/`. If you use a different working directory, update your agent's system prompt so Claude can locate the skill files.
- **Outputs:** on self-hosted environments the session's system prompt omits the `/mnt/session/outputs` instruction used on Anthropic-managed sandboxes, so final deliverables land wherever the agent writes them in your sandbox filesystem, typically under the working directory.




Before you begin

You need:

- **An existing agent.** If you don't have one, complete the [Quickstart](/docs/en/managed-agents/quickstart) first and note its agent ID.
- **A Linux host** with `/bin/bash` at that exact path. The worker's bash tool invokes it directly, without consulting `PATH`. The TypeScript SDK additionally requires `unzip` and `tar` on the `PATH` and Node.js 22 or later; the Python and Go SDKs use their standard libraries for archive extraction and have no additional binary requirements.
- **The `ant` CLI or an Anthropic SDK** (Python, TypeScript, or Go) on the worker host.
- **Two credentials:** an environment key (generated in the Console in the steps that follow) authenticates the worker to its queue; your Claude API key creates sessions and reads queue stats from outside the worker host. Key generation is Console-only.



On [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), the worker authenticates with AWS IAM (SigV4) or an [API key generated in the AWS Console](/docs/en/build-with-claude/claude-platform-on-aws#api-key-authentication), not an environment key. Attach the [`AnthropicSelfHostedEnvironmentAccess`](/docs/en/api/claude-platform-on-aws-iam-actions#managed-policies) managed policy to the IAM principal your worker runs as. Environment keys generated in the Claude Console don't work with the Claude Platform on AWS endpoint.

1.  1

    Create a self-hosted environment

    In the [Console](https://platform.claude.com/workspaces/default/environments): **Workspace \> Environments \> New \> Self-hosted**

    Or through the API:

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

    ``` shiki
    client = anthropic.Anthropic()

    environment = client.beta.environments.create(
        name="self-hosted", config={"type": "self_hosted"}
    )
    print(environment.id)
    ```

2.  2

    Generate an environment key

    In the Console, open the environment and click **Generate environment key**. Key generation is Console-only, regardless of whether you created the environment through the Console or the API. Then export the environment ID and key on the worker host:

    ``` shiki
    export ANTHROPIC_ENVIRONMENT_KEY="sk-ant-oat01-..."
    export ANTHROPIC_ENVIRONMENT_ID="env_..."
    ```

    



Skills can include executables that the agent may run directly. The CLI and SDK workers preserve the executable permissions recorded in the skill bundle when they extract it. If you implement skills download manually, you are responsible for setting executable permissions.




Run a worker

Choose **always-on** for the simplest setup: a long-running process polls the queue continuously and needs only outbound HTTPS. Choose **webhook-triggered** to avoid running an idle poller; it requires a webhook endpoint that Anthropic can reach (see [Webhooks](/docs/en/managed-agents/webhooks) for endpoint setup and signature verification).

Always-on (ant CLI)

Always-on (ant CLI)

Always-on (SDK)

Always-on (SDK)

Webhook-triggered (SDK)

Webhook-triggered (SDK)

1.  1

    Install the ant CLI

    Run this on the worker host.

    curl (Linux/WSL)

    curl (Linux/WSL)

    Homebrew (macOS)

    Homebrew (macOS)

    For Linux environments, download the release binary directly.

    ``` shiki
    VERSION=1.21.0
    OS=$(uname -s | tr '[:upper:]' '[:lower:]')
    case $(uname -m) in
      x86_64) ARCH=amd64 ;;
      aarch64) ARCH=arm64 ;;
    esac
    curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
      | sudo tar -xz -C /usr/local/bin ant
    ```

    

    You can find all releases on the [GitHub releases page](https://github.com/anthropics/anthropic-cli/releases).

2.  2

    Run the worker

    **In-process**

    `ant beta:worker poll` claims work items assigned to the environment, downloads skills, executes tool calls in the working directory, and posts results back. It reads `ANTHROPIC_ENVIRONMENT_KEY` and `ANTHROPIC_ENVIRONMENT_ID` from the environment.

    ``` shiki
    ant beta:worker poll \
      --workdir "/workspace"
    ```

    

    The worker exits cleanly on SIGTERM or SIGINT: it cancels any in-flight tool call, posts its error result, and releases the work item before stopping.

    **Sandbox per session**

    If you need stronger isolation (a fresh filesystem, resource limits, or per-session network controls), run each session in its own sandbox. Build an image with `ant` installed and `ant beta:worker run` as the entrypoint. The base image must provide `/bin/bash`; `curl` is only used at build time. When a sandbox starts, it reads session details from environment variables, handles that session, and exits:

    ``` inline-block
    FROM your-base-image
    ARG ANT_VERSION=1.21.0
    ARG TARGETARCH
    RUN ARCH=$([ "$TARGETARCH" = "arm64" ] && echo arm64 || echo amd64) && \
        curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${ANT_VERSION}/ant_${ANT_VERSION}_linux_${ARCH}.tar.gz" \
          | tar -xz -C /usr/local/bin ant
    WORKDIR /workspace
    VOLUME /workspace
    ENTRYPOINT ["ant", "beta:worker", "run"]
    ```

    

    Then write a spawn script that forwards session details into a fresh sandbox. The poller injects `ANTHROPIC_SESSION_ID`, `ANTHROPIC_WORK_ID`, `ANTHROPIC_ENVIRONMENT_ID`, and `ANTHROPIC_ENVIRONMENT_KEY` into the script's environment. `ANTHROPIC_BASE_URL` is optional and is passed through only if it was set on the poller host; it overrides the default API endpoint. In the example, `/host/outputs` is a host directory you choose; it is bind-mounted to the sandbox's working directory (`/workspace`) so you can retrieve session deliverables after the sandbox exits. On self-hosted environments the agent writes deliverables under the working directory rather than `/mnt/session/outputs` (see [Sandbox filesystem](#sandbox-filesystem)), so mounting the working directory is what captures them; the mount also picks up the downloaded `skills/` tree and any intermediate files the agent creates.

    ``` shiki
    #!/bin/bash
    # spawn.sh: called once per claimed work item
    mkdir -p "/host/outputs/$ANTHROPIC_SESSION_ID"
    exec docker run --rm \
      -e ANTHROPIC_SESSION_ID -e ANTHROPIC_ENVIRONMENT_KEY \
      -e ANTHROPIC_WORK_ID -e ANTHROPIC_ENVIRONMENT_ID -e ANTHROPIC_BASE_URL \
      -v "/host/outputs/$ANTHROPIC_SESSION_ID":/workspace \
      your-image
    ```

    

    Start the poller pointing at the script:

    ``` shiki
    ant beta:worker poll \
      --on-work ./spawn.sh
    ```

    




SDK helpers

The SDK provides three helpers at different levels of control. `EnvironmentWorker` covers most use cases; drop to the lower-level helpers when you need to launch your own per-session process or run tools against an already-claimed session.

- **`EnvironmentWorker`:** the out-of-the-box worker. Handles polling, setup, and execution end to end.
  - `.run()`: runs indefinitely, picking up sessions as they arrive.
  - `.handle_item()`: handles a single claimed work item and exits. Pass the work, session, and environment identifiers explicitly, or let it read the `ANTHROPIC_*` variables that `ant beta:worker poll --on-work` sets for the process it spawns.
- **`work.poller()`:** polls the work queue on your behalf and gives you each claimed session. Use this when you want to decide what happens for each session, for example launching a sandbox rather than running tools in-process.
  - `drain`: whether to stop polling once the queue is empty rather than waiting for new work.
  - `block_ms`: how long to wait for work to arrive before returning, in milliseconds. Must be between 1 and 999 (per-poll wait; the helper re-polls automatically). Pass `null` (`None` in Python, `param.Null[int64]()` in Go) for a non-blocking check; omitting the parameter uses the default 999 ms long-poll.
  - `reclaim_older_than_ms`: re-claim work items that were claimed but never acknowledged within this many milliseconds.
  - `auto_stop`: whether to post a stop signal for each work item once your loop body finishes with it. The Go poller has no opt-out and always posts the stop signal, so block in the loop body until the session completes rather than detaching.
- **`client.beta.sessions.events.tool_runner()`:** runs tool calls for a single session, given the session ID and a tool list. Use when you've already claimed the work and only need the execution layer.

Use the work poller directly when you want to launch your own per-session process, for example spinning up a sandbox for each claimed session:

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
import asyncio
import os

from anthropic import AsyncAnthropic
from anthropic.types.beta.environments import BetaSelfHostedWork


async def launch_container(work: BetaSelfHostedWork) -> None:
    # Replace with your own per-session sandbox launcher. Pass
    # ANTHROPIC_ENVIRONMENT_KEY into the launched sandbox, never
    # your API key.
    print(f"claimed session {work.data.id}")


async def main() -> None:
    environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
    environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
    async with AsyncAnthropic(auth_token=environment_key) as client:
        async for work in client.beta.environments.work.poller(
            environment_id=environment_id,
            environment_key=environment_key,
            auto_stop=False,  # the launched sandbox owns the stop call
        ):
            await launch_container(work)


asyncio.run(main())
```

**`AgentToolContext`** is the execution context for tool calls. It defines the working directory and path policy, and can download the session's skills. **`beta_agent_toolset_20260401(env)`** takes an `AgentToolContext` and returns the standard tool implementations (`bash`, `read`, `write`, `edit`, `glob`, `grep`).

**With `EnvironmentWorker`:** both are managed automatically. Pass a `tools` factory to customize the tool list:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
EnvironmentWorker(client, ..., tools=lambda env: [beta_bash_tool(env), my_custom_tool])
```

**With `work.poller()` and `tool_runner()`:** pass a tool list as `tools` to `client.beta.sessions.events.tool_runner()`. To build that list, set up `AgentToolContext` yourself and call `beta_agent_toolset_20260401(env)`:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
from anthropic.lib.tools.agent_toolset import (
    AgentToolContext,
    beta_agent_toolset_20260401,
)

async with AgentToolContext(
    workdir="/workspace", client=client, session_id=work.data.id
) as env:
    # skills downloaded to /workspace/skills/<name>/
    tools = beta_agent_toolset_20260401(env)
```




Verify the worker is connected

From a separate shell, with `ANTHROPIC_API_KEY` set to your Claude API key (not the environment key), confirm `workers_polling` is at least 1:

```python
ant beta:environments:work stats --environment-id "$ANTHROPIC_ENVIRONMENT_ID"
```



If `workers_polling` stays at 0, the worker isn't reaching the queue: confirm `ANTHROPIC_ENVIRONMENT_KEY` and `ANTHROPIC_ENVIRONMENT_ID` are set on the worker host. See [Read queue depth](#read-queue-depth) for the full stats response and other language examples.




Start a session

Once your worker is running, create a session that targets the environment. Set `AGENT_ID` to the agent ID you noted in [Before you begin](#before-you-begin). The session enters the environment's work queue and waits there until a worker claims it; if no worker is connected, the session stays queued rather than failing.

Anthropic doesn't mount files or GitHub repositories into self-hosted sandboxes. To make session-specific files available, pass file references (such as an S3 path or commit SHA) in the session `metadata` field. The claimed work item doesn't carry the session's metadata, but it does carry the session ID: your spawn script or `--on-work` handler retrieves the session (`GET /v1/sessions/{session_id}`) to read the `metadata` field, then stages the files into the working directory before tool execution begins.

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
    metadata={"input_file": "s3://my-bucket/data.csv"},
)
```



Self-hosted sandboxes don't support `resources` entries; a session that includes any resource on a self-hosted environment is rejected.

See [Self-hosted worker](/docs/en/managed-agents/reference#self-hosted-worker) in the reference for the full list of CLI flags, and [SDK helpers](#sdk-helpers) for the SDK helper options.




Serve custom tools from your sandbox

[Custom tools](/docs/en/managed-agents/tools#custom-tools) are tools your own code executes: the agent emits an `agent.custom_tool_use` event and waits for a matching `user.custom_tool_result`. The worker can be that code, and because it runs inside your sandbox, the tool reaches the internal services, credentials, and network egress you configured for the sandbox, and nothing more. The environment key authorizes posting custom tool results, so your Claude API key stays off the worker host.



Serving custom tools requires the SDK worker: the `ant` CLI worker has no way to register a custom tool implementation. In the sandbox-per-session pattern, run `EnvironmentWorker` inside the sandbox with `handle_item()` (`handleItem` in TypeScript, `HandleItem` in Go) in place of `ant beta:worker run`.

1.  1

    Declare the tool on the agent

    Add a `custom` entry to the agent's `tools` whose `name` matches the tool your worker registers. See [Custom tools](/docs/en/managed-agents/tools#custom-tools) for the full declaration shape.

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

    Register the implementation with the worker

    Pass the tool through the worker's `tools` factory (see [SDK helpers](#sdk-helpers)), alongside the built-in toolset:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

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

The worker answers only the tools registered with it. A custom tool that is declared on the agent but registered with no worker or client leaves the session paused with a `requires_action` stop reason until something posts its result; see [Handling custom tool calls](/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls) for the event flow.




Wrap an MCP server as custom tools

The [MCP connector](/docs/en/managed-agents/mcp-connector) connects to MCP servers from Anthropic's side, so a server must expose an HTTP endpoint that Anthropic can reach, directly or through an [MCP tunnel](/docs/en/agents-and-tools/mcp-tunnels/overview). To use a server that only your network can reach, make the worker the MCP client instead and declare the server's tools as custom tools. The MCP server needs no inbound connectivity from outside your network; Anthropic receives the tool definitions you declare on the agent, each call's input, and the result your worker posts back. At runtime the model calls a wrapped tool like any other custom tool:

1.  The agent emits an `agent.custom_tool_use` event.
2.  The worker, inside your sandbox, forwards the call over its open MCP session to the server on your network.
3.  The worker posts the server's response as the `user.custom_tool_result`.

The SDKs' [Client-side MCP helpers](/docs/en/agents-and-tools/mcp-connector#client-side-mcp-helpers) convert the server's tools into the runnable tools the worker accepts; install an MCP SDK alongside the Anthropic SDK (`pip install "anthropic[mcp]" "mcp>=1.24"`, `npm install @modelcontextprotocol/sdk`, `go get github.com/modelcontextprotocol/go-sdk`). The examples connect without authentication; to send credentials, configure the HTTP client or request options you hand to the MCP transport (`http_client` in Python, `requestInit` in TypeScript, `HTTPClient` in Go).

1.  1

    Declare the server's tools on the agent

    List the MCP server's tools and declare each one as a `custom` tool; the MCP `name`, `description`, and `inputSchema` map one to one onto the custom tool's fields. If the server paginates its tool list, declare every page; the worker must list the same pages.

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

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
                model="claude-opus-5",
                tools=[
                    {"type": "agent_toolset_20260401"},
                    *[to_custom_tool(tool) for tool in listed.tools],
                ],
            )
            print(agent.id)


    asyncio.run(main())
    ```

2.  2

    Serve the tools from the worker

    Connect to the same MCP server at startup, convert its tools with the MCP helpers, and register them alongside the built-in toolset. Keep one MCP session open for the life of the worker.

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

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

Keep the following in mind when you wrap an MCP server:

- **Tools are declared, not discovered at runtime.** The worker lists the MCP server's tools once at startup and cannot add tools to a running session. When the server's tools change, declare them again, on the agent or on an idle session through [Updating the agent configuration](/docs/en/managed-agents/session-operations#updating-the-agent-configuration), and restart the worker.
- **Names and descriptions must fit the Managed Agents API.** Custom tool names are unique per agent and use letters, digits, underscores, and hyphens (1–128 characters); a description is required (1–4,096 characters); and an agent's `tools` array takes at most 128 entries (each wrapped tool is one entry, and the built-in toolset is one more). The API rejects a declaration that reuses a tool name, names a custom tool after a built-in agent tool such as `bash` or `read`, or uses the reserved `mcp__` prefix. The MCP helpers keep the server's names and descriptions, so rename or trim where needed. When two servers expose the same tool name, define the wrapper yourself under a prefixed name and have it call the server's original tool name.
- **Most schemas pass through unchanged.** The API accepts the JSON Schema keywords MCP servers commonly emit, such as `additionalProperties` and `title`. It rejects reference keywords such as `$ref` anywhere in a custom tool's `input_schema`, so inline the schemas that generators such as pydantic factor into `$defs`. It also rejects top-level `oneOf`, `anyOf`, and `allOf`, and property names outside letters, digits, underscores, dots, and hyphens (1–64 characters).
- **Tool failures surface as error tool results.** When the MCP server reports a tool error, the worker posts an error tool result the model can react to. MCP content with no tool result equivalent, such as audio blocks and resource links, also surfaces as an error. Set a timeout on the MCP client for a faster and clearer failure, as the Python worker example does with `read_timeout_seconds`. Without one, a hung call becomes an error result only when the TypeScript MCP SDK's default request timeout fires (about a minute) or when the worker's own backstop does: about two and a half minutes in Python, and two minutes in Go, where the worker cancels a tool call that outlives its 120-second default and posts an error result.
- **Wrap servers you operate or trust.** A wrapped tool's name, description, and results enter the model's context like any other tool's: untrusted input that can influence what the agent does with its other tools, including `bash` on the worker host. Declare only the tools you intend the agent to use.
- **Permission policies do not apply to custom tools.** [Permission policies](/docs/en/managed-agents/permission-policies#custom-tools) govern the built-in and MCP toolsets; the worker executes every wrapped tool call the model makes, so put any approval step in your own tool code.




Monitoring and operations

These calls run from your monitoring or operations tooling, authenticated with your Claude API key, to observe and manage the worker fleet. The claim and keep-alive loop is handled inside the worker helpers, so you don't call those endpoints directly.



These endpoints accept either your organization API key or the environment key. Call them from outside the worker host with your organization API key. Setting `ANTHROPIC_API_KEY` on the worker host exposes an organization-scoped credential to agent tool calls.




Read queue depth

`work.stats` returns the queue state for an environment:

- `depth` is the number of items waiting to be claimed. Scale your worker fleet or alert on backlog based on this value.
- `pending` is the number of items claimed by a worker but not yet acknowledged. The worker helpers acknowledge each item before processing it, so this value stays near zero in normal operation; a sustained non-zero value means a worker stalled between claiming and acknowledging.
- `oldest_queued_at` is the timestamp of the oldest item still in the queue, waiting to be claimed or claimed but not yet acknowledged, or `null` when there is none.
- `workers_polling` is the number of workers that have polled in the last 30 seconds. Use this for liveness alerting.

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
import os

import anthropic

client = anthropic.Anthropic()

stats = client.beta.environments.work.stats(os.environ["ANTHROPIC_ENVIRONMENT_ID"])
print(f"depth={stats.depth} pending={stats.pending}")
```

``` block
{
  "type": "work_queue_stats",
  "depth": 0,
  "pending": 0,
  "oldest_queued_at": null,
  "workers_polling": 0
}
```






Stop a session gracefully

Use `work.stop` to ask the worker handling a specific session to shut it down. By default the work item moves to `stopping`: the worker notices on its next lease heartbeat, cancels the session's in-flight tool call, and confirms the shutdown, at which point the work item becomes `stopped`. Pass `force: true` in the request body (with the CLI, pass `--force`) to mark the work item `stopped` immediately instead of waiting for the worker's confirmation.

Because these calls run from your operations tooling rather than the worker host, `ANTHROPIC_WORK_ID` isn't set automatically. Set it to the target work item's ID before running the following examples. To find a work item's ID, list the environment's work items through the [Environments Work endpoints](/docs/en/api/beta/environments/work).

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
import os

import anthropic

client = anthropic.Anthropic()

work = client.beta.environments.work.stop(
    os.environ["ANTHROPIC_WORK_ID"],
    environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
)
print(work.state)
```




Next steps




Security model

Shared responsibility model for self-hosted sandbox environments.




Start a session

Create a session to run your agent and begin executing tasks.




MCP tunnels

Securely connect Claude to MCP servers running in your private network without opening inbound ports or exposing services to the public internet.
