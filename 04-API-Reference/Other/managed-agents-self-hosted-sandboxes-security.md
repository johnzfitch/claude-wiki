---
title: "Security model - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:42Z"
tags: ["api", "security"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fself-hosted-sandboxes-security)

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

[Integration guide](managed-agents-self-hosted-sandboxes.md)[Security model](managed-agents-self-hosted-sandboxes-security.md)

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

[Managed Agents](managed-agents-overview.md)Self-hosted sandboxes

# Security model

Copy page



Shared responsibility model for self-hosted sandbox environments.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

Anthropic secures the control plane across all environments: session and work queue integrity, multitenant isolation, and agent-context minimization. When you self-host, the following responsibilities fall to you.

## What you own

- **Sandbox image quality and runtime hardening.** Anthropic does not inspect or verify your sandbox image. Follow best practices such as dropping unnecessary Linux capabilities, running as a non-root user, and using a read-only root filesystem.
- **Network egress controls.** Your sandbox's network access is determined by your VPC and firewall rules. Without egress restrictions, a compromised tool execution can reach arbitrary external hosts. Restrict outbound traffic to only the endpoints your tools require.
- **Service key storage and rotation.** The environment service key (`ANTHROPIC_ENVIRONMENT_KEY`) authorizes polling your environment's work queue and submitting results back to sessions. Store it in a secrets manager, not in environment files or sandbox images. Rotate it immediately if you suspect exposure.
- **Isolating untrusted workloads.** The environment service key is scoped to one environment's work queue. If you run untrusted code inside your sandbox, consider provisioning a separate workspace and environment for each trust boundary. This limits each key to a single user's sessions instead of a shared pool.
- **Per-session credentials.** Each work item your worker claims can carry a per-session `secret`, which the SDK worker uses in place of the environment service key. Access to [memory stores](managed-agents-memory.md) requires the `secret`: the memory store endpoints reject the environment key (see [Use memory stores](managed-agents-self-hosted-sandboxes.md#use-memory-stores)). Pass the `secret` only into the sandbox that serves that session, keep it out of images and shared volumes, and never log it.
- **Tool-execution blast radius.** Tools run inside your sandbox with whatever permissions your process has. Apply least privilege to the process user and mount only the directories your tools require.
- **Log retention and session content.** Conversation content and tool outputs pass through your worker and stay in your environment. You are responsible for retaining, redacting, or deleting that data in compliance with your own policies. Anthropic has no visibility into what your worker does with session content once delivered.
- **Memory store contents.** [Memory stores](managed-agents-memory.md) remain hosted by Anthropic, including their version history. When a session attaches one, the worker keeps a working copy under `/mnt/memory/` in your sandbox for the session's duration and syncs changes back. The worker deletes that copy when the session ends, but a worker that exits without running its teardown leaves it behind. Cleaning up leftover copies, the permissions on that path, and isolation between sessions that share a filesystem are your responsibility.
- **Read-only memory stores.** A store attached with `read_only` access is protected from upload, not from local modification. The worker's `write` and `edit` tools refuse to write under its directory, nothing there syncs back, and the memory store endpoints reject writes to it made with the session's `secret`. Other processes in the sandbox can still change the local copy: commands the agent runs through the `bash` tool, and [custom tools](managed-agents-self-hosted-sandboxes.md#serve-custom-tools-from-your-sandbox) or MCP servers you serve from the sandbox, which run with the worker's permissions. Later tool calls in that session read the changed copy until that memory next changes in the store. If the agent must not be able to alter even its local view of such a store, disable the `bash` tool for that agent and give it no custom tool that writes to the sandbox's filesystem.

## What Anthropic cannot do for you

- **Know that your key leaked.** Anthropic can detect anomalous usage patterns, but cannot know your key was compromised. If you suspect `ANTHROPIC_ENVIRONMENT_KEY` leaked, revoke it and generate a replacement immediately. Revocation is validated on every request, so it takes effect on the worker's next call.
- **Verify your worker build.** Anthropic does not inspect your sandbox image or runtime. A supply-chain compromise in your image is not detectable from the control plane.
- **Isolate tools inside your sandbox.** Anthropic's security boundary stops at the sandbox. How you isolate individual tool executions from each other inside that boundary is entirely your responsibility.
- **Enforce data retention in your environment.** Once session content reaches your worker, it is outside Anthropic's data lifecycle controls.
