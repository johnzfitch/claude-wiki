---
title: "Self-hosted sandboxes - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes"
category: "04-API-Reference/Other"
fetched_at: "2026-10-20T06:40:27Z"
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fself-hosted-sandboxes)

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

# Self-hosted sandboxes

Copy page



Run Claude Managed Agents sessions in self-hosted sandboxes, keeping tool execution, files, and network egress in your own infrastructure.

Copy page



Self-hosted sandboxes move the agent's tool execution from Anthropic-managed cloud sandboxes into infrastructure you control, while Anthropic keeps running the agent. To learn what that means and decide whether it fits your agent, see [Choosing an agent environment](managed-agents-choosing-an-environment.md).

## How it works

A `self_hosted` environment acts as a work queue. You run an **environment worker**, a process on your own infrastructure that serves that queue:

1.  You create a [session](managed-agents-sessions.md) that targets the environment. Anthropic enqueues the session as a work item.
2.  Your worker claims the work item and downloads the agent's [skills](managed-agents-skills.md) and the session's [memory stores](managed-agents-memory.md).
3.  Claude runs on Anthropic's side and requests tool calls. Your worker runs each call locally and posts the result back.

Tool inputs and outputs still flow to Anthropic's control plane, so the model can see results and determine what to do next. Anthropic stores skills and memory stores. Your sandbox holds a copy for the session. See [Security model](managed-agents-self-hosted-sandboxes-security.md) for the full data-flow boundary.

Self-hosted sandboxes support every Claude model available in Managed Agents. The model is configured on the agent, not the environment.

The `ant` CLI and the Python, TypeScript, and Go SDKs ship pre-built workers. Sandbox providers such as Cloudflare, Daytona, and Modal also publish their own [platform guides](#platform-guides).

## Quickstart

This quickstart runs one always-on worker with the `ant` CLI, sends it a session, and confirms that the agent's tool calls ran on your host.

### Prerequisites

- **An agent:** If you don't have one, complete [Get started with Claude Managed Agents](managed-agents-quickstart.md) first and note the agent ID.
- **A Linux host:** The host needs `/bin/bash` at that exact path. The worker needs only outbound HTTPS.
- **A Claude API key:** You use it from your own machine to create sessions and read queue stats. Keep it off the worker host, where agent tool calls could read it.
- **The `ant` CLI or the SDK on your own machine:** The stats and session steps in this quickstart run there, not on the worker host. Install the CLI the same way the [install step](#run-your-first-session) does for the worker, or install the [SDK](cli-sdks-libraries-overview.md).



On [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), the worker authenticates with AWS IAM (SigV4) or an [API key generated in the AWS Console](../Guides/build-with-claude-claude-platform-on-aws.md#api-key-authentication), not an environment key. Attach the [`AnthropicSelfHostedEnvironmentAccess`](../Endpoints/claude-platform-on-aws-iam-actions.md#managed-policies) managed policy to the IAM principal your worker runs as. Environment keys generated in the Claude Console don't work with the Claude Platform on AWS endpoint.

### Run your first session

1.  1

    ### Create a self-hosted environment

    In the Claude Console, go to the [Environments](playground.md) page (`platform.claude.com/environments`), click **Create environment**, and under **Hosting** select **Self-hosted**.

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

    CLI

    

    ``` shiki
    ant apply environment.yaml
    ```

    environment.yaml
    
    

    ``` shiki
    # yaml-language-server: $schema=https://platform.claude.com/schemas/ant/beta/environment.json
    name: self-hosted
    config:
      type: self_hosted
    ```

2.  2

    ### Generate an environment key

    In the Console, open the environment and click **Generate environment key**. The environment key authenticates the worker to its queue. You can generate one only in the Console, even for an environment you created through the API.

    Export the environment ID and key on the worker host:

    ``` shiki
    export ANTHROPIC_ENVIRONMENT_KEY="sk-ant-oat01-..."
    export ANTHROPIC_ENVIRONMENT_ID="env_..."
    ```

    

3.  3

    ### Install the ant CLI

    Run this on the worker host.

    curl (Linux/WSL)
    Homebrew (macOS)

    curl (Linux/WSL)

    For Linux environments, download the release binary directly.

    ``` shiki
    VERSION=1.42.0
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

    Homebrew (macOS)

    ``` shiki
    brew install anthropics/tap/ant
    ```

    

4.  4

    ### Start the worker

    Create the working directory, then start the worker. `--workdir` defaults to the current directory, so pass `/workspace` to match the system default.

    ``` shiki
    sudo mkdir -p /workspace && sudo chown "$USER" /workspace
    ant beta:worker poll --workdir /workspace
    ```

    

    The worker reads the two variables you exported and polls until you stop it.

5.  5

    ### Verify the worker is connected

    On your own machine, set `ANTHROPIC_API_KEY` to your Claude API key (not the environment key) and `environment_id` to the environment ID. Confirm that `workers_polling` is at least 1:

    cURL
    CLI
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
    client = anthropic.Anthropic()

    stats = client.beta.environments.work.stats(environment_id)
    print(f"workers_polling={stats.workers_polling}")
    ```

    If `workers_polling` stays at 0, see [Troubleshooting](managed-agents-self-hosted-sandboxes-operations.md#troubleshooting).

6.  6

    ### Start a session

    Set `agent_id` to your agent's ID. Create a session that targets the environment, then send it a task:

    cURL
    CLI
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
    session = client.beta.sessions.create(
        agent=agent_id,
        environment_id=environment_id,
    )

    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [
                    {
                        "type": "text",
                        "text": 'Write the output of "uname -a" to hello.txt in your working directory.',
                    },
                ],
            },
        ],
    )
    ```

    The session waits in the environment's queue until a worker claims it. If no worker is connected, the session stays queued rather than failing.

7.  7

    ### Confirm the tools ran on your host

    On the worker host, read the file the agent wrote:

    ``` shiki
    cat /workspace/hello.txt
    ```

    

    The file describes your own host's kernel, so the agent's tool calls ran there. To follow the agent's work as it happens, see [Session event stream](managed-agents-events-and-streaming.md).

## Session resources

Self-hosted sandboxes support `memory_store` resources only. A session on a self-hosted environment that includes a `file` or `github_repository` resource is rejected with a 400 error:

```python
Environment env_... is a self-hosted environment. `resources` are not supported with self-hosted environments.
```



[Deployments](managed-agents-scheduled-deployments.md) that target a self-hosted environment follow the same rule. To give a session its own input files, see [Stage files for a session](managed-agents-self-hosted-sandboxes-workers.md#stage-files-for-a-session).

## Self-hosted sandboxes and MCP tunnels

Self-hosting controls *where the agent's code executes*. [MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md) control *how Anthropic reaches MCP servers in your network*. The two are independent:

- A session in Anthropic's cloud sandboxes can reach private MCP servers through a tunnel. For example, a private MCP server might sit in front of a database or an internal API behind your firewall.
- A self-hosted session can use either tunneled or public MCP servers.

Use both when you want execution and tool access to stay inside your boundary. To skip the tunnel, [wrap the MCP server as custom tools](managed-agents-self-hosted-sandboxes-custom-tools.md#wrap-an-mcp-server-as-custom-tools) that your worker serves.

## Platform guides

These pages describe how to build a worker on any sandboxing platform. Platform-specific guides are also available:

- [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations-claude-managed-agents.html)
- [Blaxel](https://docs.blaxel.ai/Tutorials/Claude-Managed-Agents)
- [Cloudflare](https://developers.cloudflare.com/sandbox/claude-managed-agents/)
- [Daytona](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents)
- [E2B](https://e2b.dev/docs/agents/claude-managed-agents)
- [Fly.io](https://docs.sprites.dev/integrations/claude-managed-agents/)
- [GKE Agent Sandbox](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/anthropic-agent-sandbox)
- [Modal](https://github.com/modal-labs/claude-managed-agents-modal-sandbox)
- [Namespace](https://namespace.so/docs/integrations/claude)
- [Superserve](https://docs.superserve.ai/integrations/managed-agents/claude-managed-agents)
- [Vercel](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox)

## Next steps



[Deploy workers](managed-agents-self-hosted-sandboxes-workers.md)

Run the SDK worker, trigger workers from webhooks, or give each session its own sandbox.



[Memory stores](managed-agents-self-hosted-sandboxes-memory.md)

Prepare the host, configure sync, and handle read-only stores and conflicts.



[Custom tools and MCP servers](managed-agents-self-hosted-sandboxes-custom-tools.md)

Serve your own tools from the worker, including tools from an MCP server inside your network.



[Monitor and troubleshoot](managed-agents-self-hosted-sandboxes-operations.md)

Read queue depth, stop sessions and workers cleanly, and fix common failures.



[Worker reference](managed-agents-self-hosted-sandboxes-reference.md)

CLI flags, environment variables, filesystem paths, and SDK helper options.



[Security model](managed-agents-self-hosted-sandboxes-security.md)

Shared responsibility model for self-hosted sandbox environments.
