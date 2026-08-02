---
title: "Cloud sandbox reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:37Z"
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

Cloud sandbox reference

Managed Agents/Configure agent environment

# Cloud sandbox reference




Pre-installed packages, databases, and utilities available in cloud sandboxes.




Cloud sandboxes run as isolated Linux containers on Anthropic-managed infrastructure. They come pre-installed with a comprehensive set of programming languages, databases, and utilities. The agent can use these immediately without any installation steps.

These specifications apply to `cloud` environments. Self-hosted sandboxes run on your infrastructure with whatever your worker provides.



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](/docs/en/api/beta-headers#endpoint-specific-headers).




Programming languages

| Language | Version | Package manager |
|----------|---------|-----------------|
| Python   | 3.12+   | pip, uv         |
| Node.js  | 20+     | npm, yarn, pnpm |
| Go       | 1.22+   | go modules      |
| Rust     | 1.77+   | cargo           |
| Java     | 21+     | maven, gradle   |
| Ruby     | 3.3+    | bundler, gem    |
| PHP      | 8.3+    | composer        |
| C/C++    | GCC 13+ | make, cmake     |




Databases

| Database          | Description                                        |
|-------------------|----------------------------------------------------|
| SQLite            | Pre-installed, available immediately               |
| PostgreSQL client | `psql` client for connecting to external databases |
| Redis client      | `redis-cli` for connecting to external instances   |



Database servers (such as PostgreSQL and Redis) are not running in the sandbox by default. The sandbox includes client tools for connecting to external database instances. SQLite is fully available for local use.




Utilities




System tools

- `git` - Version control
- `curl`, `wget` - HTTP clients
- `jq` - JSON processing
- `tar`, `zip`, `unzip` - Archive tools
- `ssh`, `scp` - Remote access (requires a networking mode that allows the destination host)
- `tmux`, `screen` - Terminal multiplexers




Development tools

- `make`, `cmake` - Build systems
- `docker` - Container management (limited availability)
- `ripgrep` (`rg`) - Fast file search
- `tree` - Directory visualization
- `htop` - Process monitoring




Text processing

- `sed`, `awk`, `grep` - Stream editors
- `vim`, `nano` - Text editors
- `diff`, `patch` - File comparison




Sandbox specifications

| Property         | Value                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operating system | Ubuntu 22.04 LTS                                                                                                                                                                   |
| Architecture     | x86_64 (amd64)                                                                                                                                                                     |
| Memory           | Up to 8 GB                                                                                                                                                                         |
| Disk space       | Up to 10 GB                                                                                                                                                                        |
| Network          | API-created environments default to [`unrestricted` networking](/docs/en/managed-agents/environments#networking); sandboxes provisioned through Claude Studio default to `limited` |
