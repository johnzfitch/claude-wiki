---
title: "Cloud environment setup - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/environments"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:39Z"
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fenvironments)

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

[Managed Agents](managed-agents-overview.md)Configure agent environment

# Cloud environment setup

Copy page



Customize cloud sandboxes for your sessions.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

Environments define the sandbox configuration where your agent runs. You create an environment once, then reference its ID each time you start a session. Multiple sessions can share the same environment, but each session gets its own isolated sandbox (a fresh Linux container).

This page covers `type: cloud` environments. To run sandboxes on your own infrastructure, see [Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md).

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

[`ant apply`](cli-sdks-libraries-cli-apply.md) creates the environment from `environment.yaml`, prints its ID, and records it in `claude-lock.json`. Commit `claude-lock.json` so the next `ant apply` updates this environment instead of trying to create it again.

Use a unique, descriptive `name` so you can tell environments apart.

## Use the environment in a session

Pass the environment ID as a string when [creating a session](managed-agents-sessions.md).

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

The `networking` field controls the sandbox's outbound network access. It does not affect the `web_search` or `web_fetch` tools, which run on Anthropic's servers; to restrict the sites those tools can reach, set `allowed_domains` or `blocked_domains` on the tool's entry in the agent toolset. See [Restrict web search and web fetch domains](managed-agents-tools.md#restrict-web-search-and-web-fetch-domains).

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

Network access is granted per host, not per operation. The sandbox can send any request to an allowed host, including uploads such as `git push` and package publishing, with any credential the command supplies. If the agent processes untrusted input (repository files, fetched web content, or third-party tool output), a successful prompt injection could use an allowed host to copy files out of the sandbox. To reduce this risk, set the `bash` tool's [permission policy](managed-agents-permission-policies.md) to `always_ask` or `auto`. If the environment does not specify `packages`, you can instead leave `allow_package_managers` set to `false` and list only the hosts your agent needs in `allowed_hosts`.

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

Cloud sandboxes include common language runtimes, databases, and command-line tools out of the box. See [Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md) for the full list.

## Next steps



[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

Pre-installed packages, databases, and utilities available in cloud sandboxes.



[Start a session](managed-agents-sessions.md)

Create a session to run your agent and start running tasks.
