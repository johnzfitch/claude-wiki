---
title: "Security model - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:42Z"
tags: ["api", "security"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fself-hosted-sandboxes-security)





SearchCtrlK

First steps

[Overview](/docs/en/managed-agents/overview)[Quickstart](/docs/en/managed-agents/quickstart)[Build in Console](/docs/en/managed-agents/onboarding)[Migration](/docs/en/managed-agents/migration)

Define your agent

[Agent setup](/docs/en/managed-agents/agent-setup)[Tools](/docs/en/managed-agents/tools)[MCP connector](/docs/en/managed-agents/mcp-connector)[Permission policies](/docs/en/managed-agents/permission-policies)[Agent Skills](/docs/en/managed-agents/skills)

Configure agent environment

[Cloud environment setup](/docs/en/managed-agents/environments)[Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference)

[Self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes)

[Integration guide](/docs/en/managed-agents/self-hosted-sandboxes)[Security model](/docs/en/managed-agents/self-hosted-sandboxes-security)

Delegate work to your agent

[Start a session](/docs/en/managed-agents/sessions)[Session operations](/docs/en/managed-agents/session-operations)[Session event stream](/docs/en/managed-agents/events-and-streaming)[Session budgets](/docs/en/managed-agents/budgets)[Subscribe to webhooks](/docs/en/managed-agents/webhooks)[Define outcomes](/docs/en/managed-agents/define-outcomes)[Authenticate with vaults](/docs/en/managed-agents/vaults)

Manage agent context

[Access GitHub](/docs/en/managed-agents/github)[Attach and download files](/docs/en/managed-agents/files)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration)[Scheduled deployments](/docs/en/managed-agents/scheduled-deployments)

Reference

[Managed Agents reference](/docs/en/managed-agents/reference)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

[Console](/)

[Managed Agents](/docs/en/managed-agents/overview)Self-hosted sandboxes

# Security model

Copy page



Shared responsibility model for self-hosted sandbox environments.

Copy page



[Managed Agents](/docs/en/managed-agents/overview)

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

managed-agents-2026-04-01

Anthropic secures the control plane across all environments: session and work queue integrity, multitenant isolation, and agent-context minimization. When you self-host, the following responsibilities fall to you.

## What you own

- **Sandbox image quality and runtime hardening.** Anthropic does not inspect or verify your sandbox image. Follow best practices such as dropping unnecessary Linux capabilities, running as a non-root user, and using a read-only root filesystem.
- **Network egress controls.** Your sandbox's network access is determined by your VPC and firewall rules. Without egress restrictions, a compromised tool execution can reach arbitrary external hosts. Restrict outbound traffic to only the endpoints your tools require.
- **Service key storage and rotation.** The environment service key (`ANTHROPIC_ENVIRONMENT_KEY`) authorizes polling your environment's work queue and submitting results back to sessions. Store it in a secrets manager, not in environment files or sandbox images. Rotate it immediately if you suspect exposure.
- **Isolating untrusted workloads.** The environment service key is scoped to one environment's work queue. If you run untrusted code inside your sandbox, consider provisioning a separate workspace and environment for each trust boundary. This limits each key to a single user's sessions instead of a shared pool.
- **Per-session credentials.** Each work item your worker claims can carry a per-session `secret`, which the SDK worker uses in place of the environment service key. Access to [memory stores](/docs/en/managed-agents/memory) requires the `secret`: the memory store endpoints reject the environment key (see [Use memory stores](/docs/en/managed-agents/self-hosted-sandboxes#use-memory-stores)). Pass the `secret` only into the sandbox that serves that session, keep it out of images and shared volumes, and never log it.
- **Tool-execution blast radius.** Tools run inside your sandbox with whatever permissions your process has. Apply least privilege to the process user and mount only the directories your tools require.
- **Log retention and session content.** Conversation content and tool outputs pass through your worker and stay in your environment. You are responsible for retaining, redacting, or deleting that data in compliance with your own policies. Anthropic has no visibility into what your worker does with session content once delivered.
- **Memory store contents.** [Memory stores](/docs/en/managed-agents/memory) remain hosted by Anthropic, including their version history. When a session attaches one, the worker keeps a working copy under `/mnt/memory/` in your sandbox for the session's duration and syncs changes back. The worker deletes that copy when the session ends, but a worker that exits without running its teardown leaves it behind. Cleaning up leftover copies, the permissions on that path, and isolation between sessions that share a filesystem are your responsibility.
- **Read-only memory stores.** A store attached with `read_only` access is protected from upload, not from local modification. The worker's `write` and `edit` tools refuse to write under its directory, nothing there syncs back, and the memory store endpoints reject writes to it made with the session's `secret`. Other processes in the sandbox can still change the local copy: commands the agent runs through the `bash` tool, and [custom tools](/docs/en/managed-agents/self-hosted-sandboxes#serve-custom-tools-from-your-sandbox) or MCP servers you serve from the sandbox, which run with the worker's permissions. Later tool calls in that session read the changed copy until that memory next changes in the store. If the agent must not be able to alter even its local view of such a store, disable the `bash` tool for that agent and give it no custom tool that writes to the sandbox's filesystem.

## What Anthropic cannot do for you

- **Know that your key leaked.** Anthropic can detect anomalous usage patterns, but cannot know your key was compromised. If you suspect `ANTHROPIC_ENVIRONMENT_KEY` leaked, revoke it and generate a replacement immediately. Revocation is validated on every request, so it takes effect on the worker's next call.
- **Verify your worker build.** Anthropic does not inspect your sandbox image or runtime. A supply-chain compromise in your image is not detectable from the control plane.
- **Isolate tools inside your sandbox.** Anthropic's security boundary stops at the sandbox. How you isolate individual tool executions from each other inside that boundary is entirely your responsibility.
- **Enforce data retention in your environment.** Once session content reaches your worker, it is outside Anthropic's data lifecycle controls.
