---
title: "Security risks and sandbox boundaries - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/secure-deployment-risks"
category: "04-API-Reference/Other"
fetched_at: "2026-10-22T06:29:45Z"
tags: ["api", "security"]
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fsecure-deployment-risks)

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

[Managed Agents](managed-agents-overview.md)Security

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Security risks and sandbox boundaries

Copy page



Why an agent's settings matter for security, and what the Managed Agents sandbox can and cannot do.

Copy page



This page explains why the settings in [Secure your Managed Agents deployment](managed-agents-secure-deployment.md) matter, and what the sandbox can and cannot do.

## Why this matters

Hidden instructions in content that an agent reads can steer the agent. This is called [prompt injection](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-mitigate-jailbreaks.md). Claude is inherently resilient to it, but model behavior is not a security control. The settings in [Secure your Managed Agents deployment](managed-agents-secure-deployment.md) limit the effect if an attempt succeeds.

Claude can also take a step you did not expect while it keeps working to complete the task you gave it. For example, it might use a tool or credential it can reach to get past an obstacle. The same settings limit what such a step can reach, and an [offline reviewer](managed-agents-secure-deployment-monitoring.md#optionally-have-an-offline-reviewer-read-every-transcript) can flag it afterward.

| What can go wrong                        | Example                                                                                                                          | Controls                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Untrusted input steers the agent         | A ticket tells the agent to cancel every open order                                                                              | [Smallest tool set](managed-agents-secure-deployment.md#give-the-agent-the-smallest-tool-set), [untrusted input kept away from powerful tools](managed-agents-secure-deployment.md#keep-untrusted-input-away-from-powerful-tools), [approvals for risky actions](managed-agents-secure-deployment.md#approve-risky-actions) |
| Code in the sandbox can use a credential | A script the agent was tricked into running sends the agent's key to an outside host, or uses it to read every customer's orders | [Credentials in vaults](managed-agents-secure-deployment.md#keep-credentials-in-vaults), [limited networking](managed-agents-secure-deployment.md#limit-the-network), [approvals for risky actions](managed-agents-secure-deployment.md#approve-risky-actions)                                                              |
| An open network lets data out            | A bash command posts a file to an outside host                                                                                   | [Limited networking](managed-agents-secure-deployment.md#limit-the-network), the [`web_fetch` domain list](managed-agents-secure-deployment.md#restrict-web-search-and-web-fetch)                                                                                                                                                 |
| Claude takes a step you did not expect   | To get past an obstacle, it uses a tool or credential it can reach                                                               | The settings in [Secure your Managed Agents deployment](managed-agents-secure-deployment.md). An [offline reviewer](managed-agents-secure-deployment-monitoring.md#optionally-have-an-offline-reviewer-read-every-transcript) can flag the step afterward                                                                         |

These settings lower the risk but do not remove it, so do not put data in the sandbox that must never leave it. An agent can still put data it is allowed to read into its own reply or tool output. Limit a key's permissions at the service that issued it, because these settings do not limit them. The settings do not secure your custom tools, your MCP servers, or your self-hosted infrastructure.

## What the sandbox can and cannot do

Managed Agents keeps the agent loop, session history, and vault secrets outside the sandbox by design. For the design background, see [Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents).

| Part                         | Where it runs                                                                                                        | What limits it                                                                                                                                                                            |
|------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Agent loop                   | Anthropic's servers                                                                                                  | The tool set, permission policies, and budget that you set                                                                                                                                |
| `bash` and file tools        | The sandbox. In a cloud environment, each session gets its own isolated Linux container                              | Environment networking, the tool set, and permission policies                                                                                                                             |
| `web_search` and `web_fetch` | Anthropic's servers                                                                                                  | The tool's own domain list and, in a `limited` cloud environment, the environment's allowed hosts. `web_fetch` also opens only URLs that have already appeared in the session             |
| Vault secret                 | Outside the sandbox. MCP credentials never enter it. For an environment variable credential, code sees a placeholder | For an MCP credential, the MCP server URL it is for. For an environment variable credential, the hosts the credential allows, its injection location, and the environment's allowed hosts |
| Session history              | Anthropic's servers, until you delete the session                                                                    | The API keys for the workspace, the Developer and Admin roles in the Claude Console, and session deletion                                                                                 |
| Custom tools                 | Your application                                                                                                     | Your code                                                                                                                                                                                 |

In a cloud environment, sessions do not share filesystem state. A memory store attached to more than one session is shared between them.

These limits do not replace each other. For example, limiting the environment's hosts does not stop the agent from using a credential on a host you allowed.
