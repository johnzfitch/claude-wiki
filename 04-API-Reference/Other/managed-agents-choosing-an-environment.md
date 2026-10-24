---
title: "Choosing an agent environment - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/choosing-an-environment"
category: "04-API-Reference/Other"
fetched_at: "2026-10-23T06:28:53Z"
tags: ["agents", "api"]
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fchoosing-an-environment)

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

[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)[Claude Models on Google Cloud (Anthropic managed)](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

[Console](playground.md)

[Managed Agents](managed-agents-overview.md)Configure agent environment

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Choosing an agent environment

Copy page



Decide whether Claude Managed Agents tools and code run in an Anthropic-managed cloud environment or a self-hosted sandbox, and see what changes if you switch.

Copy page



An environment sets where your agent's tools and code run. They run in a sandbox. A sandbox is an isolated workspace, such as a container, where the agent runs commands and works on files. You have two options:

- **Cloud environment:** Anthropic runs the sandbox for you. Each session gets its own fresh Linux container on Anthropic-managed infrastructure, with common languages, databases, and utilities already installed. You choose its network rules and any extra packages to install.
- **Self-hosted sandbox:** You run the sandbox on your own infrastructure. Claude still runs on Anthropic's side and determines which tool to call next. A program that you run, called a worker, carries out the agent's bash and file tool calls on your machines and sends each result back. It can also serve custom tools.

The agent definition is the same whichever you choose. You set the model, prompt, and tools on the [agent](managed-agents-agent-setup.md), not on the environment.

## Start with a cloud environment

If you're not sure which to choose, or you're new to Claude Managed Agents, start with a [cloud environment](managed-agents-environments.md), as the [quickstart](managed-agents-quickstart.md) does. Anthropic runs an isolated container for each session, with common languages and tools already installed, so there is nothing for you to host. Choose a self-hosted sandbox only if tools must run on infrastructure you control.

## Compare the options

The table compares the two options.

|                                     | [Cloud environment](managed-agents-environments.md) (default)                                                                                                                                                | [Self-hosted sandbox](managed-agents-self-hosted-sandboxes.md)                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Where tools and code run            | An Anthropic-managed sandbox                                                                                                                                                                                       | Your worker, on your infrastructure                                                                                       |
| What reaches Anthropic              | The [conversation history](managed-agents-events-and-streaming.md#list-past-events), [tool results](managed-agents-tools.md#available-tools), the sandbox's files and state, skills, and memory stores | The conversation history, tool results, skills, and memory stores. The sandbox's files and processes stay on your worker. |
| What you operate                    | Nothing                                                                                                                                                                                                            | The worker hosts, their hardening, their network limits, and the environment key your worker authenticates with           |
| Network reach                       | Network rules you set on the environment                                                                                                                                                                           | Your own network policy                                                                                                   |
| File and GitHub repository mounting | Managed by Anthropic                                                                                                                                                                                               | Managed by you                                                                                                            |
| Memory stores                       | Mounted by Anthropic at `/mnt/memory/`                                                                                                                                                                             | Downloaded to `/mnt/memory/` and synced by the worker                                                                     |
| Sandbox lifecycle                   | Managed by Anthropic                                                                                                                                                                                               | Managed by you                                                                                                            |
| Choose it when                      | The default. You don't need tools to run on your own infrastructure.                                                                                                                                               | Tools must run on infrastructure you control.                                                                             |

## When to choose a self-hosted sandbox

A self-hosted sandbox fits when the agent needs to do one of the following:

- **Work on data that can't leave your network:** The agent's files and processes stay on your worker. What a tool returns to the model still reaches the Managed Agents service.
- **Reach internal services that aren't publicly routable:** The agent's bash and file tools, and any custom tools your worker serves, run inside your network. Anthropic, not your worker, connects to the agent's MCP servers. A private one might be in front of your internal ticket system or company wiki. To reach it, you can use an [MCP tunnel](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md) with either option. MCP tunnels are in research preview and need an access request. See [Self-hosted sandboxes and MCP tunnels](managed-agents-self-hosted-sandboxes.md#self-hosted-sandboxes-and-mcp-tunnels).
- **Run under your organization's own compliance and audit controls:** Tools run on hosts that you configure, log, and audit.

## What a self-hosted sandbox doesn't change

With either option, the conversation history and tool results go to the Managed Agents service, which Anthropic operates. That is how the model receives the result of each tool call. The web search and web fetch tools also run on Anthropic's side, not in the sandbox. See [Restrict web search and web fetch domains](managed-agents-tools-web-restrictions.md). Neither option changes the compliance coverage of Managed Agents or how long it keeps conversation history. See [API and data retention](manage-claude-api-and-data-retention.md#feature-eligibility).

## What you take on and give up with a self-hosted sandbox

A self-hosted sandbox makes you the operator of the worker hosts. You harden the sandbox image, control network egress, store and rotate the environment key, and isolate sessions from each other. The [Security model](managed-agents-self-hosted-sandboxes-security.md) page has the detail.

You also give up these cloud environment features:

- [`file` and `github_repository` session resources](managed-agents-self-hosted-sandboxes.md#session-resources). You [stage input files yourself](managed-agents-self-hosted-sandboxes-workers.md#stage-files-for-a-session), and you are responsible for mounting your own GitHub repository too.
- [Repository skill discovery](managed-agents-skills.md#load-skills-from-a-github-repository).
- [Environment variable credentials](managed-agents-vaults.md#add-a-credential) in vaults.
- The [pre-installed runtimes and packages](managed-agents-cloud-sandboxes-reference.md) of a cloud sandbox. A self-hosted sandbox has whatever your worker provides.

## Differences on Claude Platform on AWS

If you use Claude Managed Agents through Claude Platform on AWS, Anthropic still operates the service. There, a self-hosted sandbox can't use memory stores, workers don't use an environment key, and MCP tunnels aren't available. See [Claude Managed Agents on Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md#claude-managed-agents) and [Features not supported](../Guides/build-with-claude-claude-platform-on-aws.md#features-not-supported).

## Differences on Claude Models on Google Cloud (Anthropic managed)

If you use Claude Managed Agents through Claude Models on Google Cloud (Anthropic managed), Anthropic still operates the service. There, memory stores aren't supported in a self-hosted sandbox, and MCP tunnels aren't available. Workers authenticate with Google Cloud credentials, not an environment key, and you write your own, because the pre-built workers in the `ant` CLI and the Python, TypeScript, and Go SDKs don't work there. See [Feature support](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#feature-support) in the Claude Models on Google Cloud (Anthropic managed) guide.

## Switch from a cloud environment to a self-hosted sandbox

To switch to a self-hosted sandbox, you keep the agent, create a `self_hosted` environment, and reference its ID in new sessions and deployments.

- **What carries over:** The agent definition, the API key, Google Cloud credentials, or AWS credentials your application uses, your skills, your MCP servers, and your [memory stores](managed-agents-self-hosted-sandboxes-memory.md).
- **What is new:** A `self_hosted` environment, an environment key that you generate in the Claude Console, and a worker that you run. The [self-hosted sandboxes quickstart](managed-agents-self-hosted-sandboxes.md#quickstart) covers all three.
- **What stops working:** The features listed in [What you take on and give up with a self-hosted sandbox](#what-you-take-on-and-give-up-with-a-self-hosted-sandbox).

On Claude Platform on AWS, memory stores don't carry over to a self-hosted sandbox, and the worker doesn't use an environment key. See [Differences on Claude Platform on AWS](#differences-on-claude-platform-on-aws).

On Claude Models on Google Cloud (Anthropic managed), memory stores aren't supported in a self-hosted sandbox, and you write your own worker, which doesn't use an environment key. See [Differences on Claude Models on Google Cloud (Anthropic managed)](#differences-on-claude-models-on-google-cloud-anthropic-managed).
