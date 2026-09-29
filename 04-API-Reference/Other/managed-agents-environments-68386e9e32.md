---
title: "Cloud environment setup - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/environments"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:39Z"
tags: ["api"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fenvironments)

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

[Managed Agents](/docs/en/managed-agents/overview)Configure agent environment

# Cloud environment setup

Copy page



Customize cloud sandboxes for your sessions.

Copy page



[Managed Agents](/docs/en/managed-agents/overview)

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

managed-agents-2026-04-01

Environments define the sandbox configuration where your agent runs. You create an environment once, then reference its ID each time you start a session. Multiple sessions can share the same environment, but each session gets its own isolated sandbox (a fresh Linux container).

This page covers `type: cloud` environments. To run sandboxes on your own infrastructure, see [Self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes).

## Create an environment

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
ant apply environment.yaml
```

environment.yaml





```python
# yaml-language-server: $schema=https://platform.claude.com/schemas/ant/beta/environment.json
name: python-dev
config:
  type: cloud
  networking:
    type: unrestricted
```

[`ant apply`](/docs/en/cli-sdks-libraries/cli/apply) creates the environment from `environment.yaml`, prints its ID, and records it in `claude-lock.json`. Commit `claude-lock.json` so the next `ant apply` updates this environment instead of trying to create it again.

Use a unique, descriptive `name` so you can tell environments apart.

## Use the environment in a session

Pass the environment ID as a string when [creating a session](/docs/en/managed-agents/sessions).

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
)
```

## Configuration options

### Packages

The `packages` field pre-installs packages into the sandbox before the agent starts. Packages are installed by their respective package managers and cached across sessions that share the same environment. When multiple package managers are specified, they run in alphabetical order (apt, cargo, gem, go, npm, pip). You can optionally pin specific versions. Unpinned packages install the latest version. If the environment uses `limited` [networking](#networking), also set `networking.allow_package_managers` to `true`; otherwise the request is rejected with a 400 error.

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
ant apply environment.yaml
```

environment.yaml





```python
# yaml-language-server: $schema=https://platform.claude.com/schemas/ant/beta/environment.json
name: data-analysis
config:
  type: cloud
  packages:
    pip:
      - pandas
      - numpy
      - scikit-learn
    npm:
      - express
  networking:
    type: unrestricted
```

Supported package managers:

| Field   | Package manager           | Example                                     |
|---------|---------------------------|---------------------------------------------|
| `apt`   | System packages (apt-get) | `"graphviz"`                                |
| `cargo` | Rust (cargo)              | `"hyperfine@1.18.0"`                        |
| `gem`   | Ruby (gem)                | `"rails:7.1.0"`                             |
| `go`    | Go modules                | `"golang.org/x/tools/cmd/goimports@latest"` |
| `npm`   | Node.js (npm)             | `"express@4.18.0"`                          |
| `pip`   | Python (pip)              | `"sqlalchemy==2.0.30"`                      |

### Networking

The `networking` field controls the sandbox's outbound network access. It does not affect the `web_search` or `web_fetch` tools, which run on Anthropic's servers; to restrict the sites those tools can reach, set `allowed_domains` or `blocked_domains` on the tool's entry in the agent toolset. See [Restrict web search and web fetch domains](/docs/en/managed-agents/tools#restrict-web-search-and-web-fetch-domains).

| Mode           | Description                                                                                                                                                  |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `unrestricted` | Full outbound network access, except for a general safety blocklist. This is the default.                                                                    |
| `limited`      | Restricts sandbox network access to the hosts in `allowed_hosts`. Set `allow_package_managers` and `allow_mcp_servers` to `true` to allow additional access. |

The following example creates an environment with `limited` networking:

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
ant apply environment.yaml
```

environment.yaml





```python
# yaml-language-server: $schema=https://platform.claude.com/schemas/ant/beta/environment.json
name: api-access
config:
  type: cloud
  networking:
    type: limited
    allowed_hosts:
      - api.example.com
    allow_mcp_servers: true
    allow_package_managers: true
```



For production deployments, use `limited` networking with an explicit `allowed_hosts` list. Follow the principle of least privilege by granting only the minimum network access your agent requires, and regularly audit your allowed domains.

When using `limited` networking:

- `allowed_hosts` specifies domains the sandbox can reach. Specify bare hostnames or wildcard patterns (such as `*.example.com`). Do not include a URL scheme, port, or path.
- `allow_mcp_servers` allows outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.
- `allow_package_managers` allows outbound access to a set of public package registries and code hosts beyond those listed in the `allowed_hosts` array. See [Package manager hosts](#package-manager-hosts) for the list. Defaults to `false`. Set it to `true` whenever the environment specifies `packages`; otherwise the request is rejected with a 400 error, even if the registry hosts are listed in `allowed_hosts`.

#### Package manager hosts

When `allow_package_managers` is `true`, the sandbox can reach the following hosts in addition to those in `allowed_hosts`. Anthropic maintains this list and can change it.

| Ecosystem    | Hosts                                                                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code hosting | `github.com`, `api.github.com`, `codeload.github.com`, `raw.githubusercontent.com`, `objects.githubusercontent.com`, `release-assets.githubusercontent.com`, `gitlab.com`, `bitbucket.org` |
| Node.js      | `registry.npmjs.org`, `registry.yarnpkg.com`, `nodejs.org`                                                                                                                                 |
| Python       | `pypi.org`, `files.pythonhosted.org`                                                                                                                                                       |
| Rust         | `crates.io`, `index.crates.io`, `static.crates.io`, `static.rust-lang.org`                                                                                                                 |
| Go           | `proxy.golang.org`, `sum.golang.org`                                                                                                                                                       |
| Java         | `repo1.maven.org`, `repo.maven.apache.org`, `services.gradle.org`, `plugins.gradle.org`, `plugins-artifacts.gradle.org`                                                                    |
| Ruby         | `rubygems.org`, `index.rubygems.org`                                                                                                                                                       |
| PHP          | `packagist.org`, `repo.packagist.org`                                                                                                                                                      |
| Ubuntu (apt) | `archive.ubuntu.com`, `security.ubuntu.com`, `ppa.launchpad.net`                                                                                                                           |
| Containers   | `registry-1.docker.io`, `auth.docker.io`, `production.cloudflare.docker.com`, `download.docker.com`, `ghcr.io`                                                                             |



Network access is granted per host, not per operation. The sandbox can send any request to an allowed host, including uploads such as `git push` and package publishing, with any credential the command supplies. If the agent processes untrusted input (repository files, fetched web content, or third-party tool output), a successful prompt injection could use an allowed host to copy files out of the sandbox. To reduce this risk, set the `bash` tool's [permission policy](/docs/en/managed-agents/permission-policies) to `always_ask` or `auto`. If the environment does not specify `packages`, you can instead leave `allow_package_managers` set to `false` and list only the hosts your agent needs in `allowed_hosts`.

## Environment lifecycle

- Environments persist until explicitly archived or deleted.
- Each session gets its own sandbox instance, even when multiple sessions reference the same environment. Sessions do not share filesystem state.
- Environments are not versioned. If you update an environment frequently, keep your own record of the changes so you can tell which configuration each session used.

## Manage environments

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
# List environments
environments = client.beta.environments.list()

# Retrieve a specific environment
env = client.beta.environments.retrieve(environment.id)

# Archive an environment (read-only, existing sessions continue)
client.beta.environments.archive(environment.id)

# Delete an environment (only if no sessions reference it)
client.beta.environments.delete(environment.id)
```

## Pre-installed runtimes

Cloud sandboxes include common language runtimes, databases, and command-line tools out of the box. See [Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference) for the full list.

## Next steps



[Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference)

Pre-installed packages, databases, and utilities available in cloud sandboxes.



[Start a session](/docs/en/managed-agents/sessions)

Create a session to run your agent and start running tasks.
