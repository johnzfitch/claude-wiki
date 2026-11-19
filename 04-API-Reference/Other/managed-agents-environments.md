---
title: "Cloud environment setup - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/environments"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:36:49Z"
tags: ["api"]
---

# Cloud environment setup

Copy page



Customize cloud sandboxes for your sessions.

Copy page



Cloud sandboxes

Beta

Feature of  
[Managed Agents](managed-agents-overview.md)

[Models](#feature-availability)  
- All models

[Cloud platforms](#feature-availability)  
- Claude API
- Claude Platform on AWS
- Claude Models on Google CloudAnthropic managed

[Beta header](#feature-availability)  
- 
  Copy`managed-agents-2026-04-01`

[Data handling](#feature-data-handling)  
ZDRNot ZDR eligibleHIPAANot HIPAA eligible

Environments define the sandbox configuration where your agent runs. You create an environment once, then reference its ID each time you start a session. Multiple sessions can share the same environment, but each session gets its own isolated sandbox (a fresh Linux container).

This page covers `type: cloud` environments. To run sandboxes on your own infrastructure, see [Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md). To choose between the two, see [Choosing an agent environment](managed-agents-choosing-an-environment.md).

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

CLI

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
    type: limited
    allow_package_managers: true
```

[`ant apply`](cli-sdks-libraries-cli-apply.md) creates the environment from `environment.yaml`, prints its ID, and records it in `claude-lock.json`. Commit `claude-lock.json` so the next `ant apply` updates this environment instead of attempting to create it again.

Use a unique, descriptive `name` so you can tell environments apart. This example uses `limited` [networking](#networking) with package managers allowed, so the sandbox can reach the package registries and code hosts. To let it reach other hosts, add them to `allowed_hosts`.

## Use the environment in a session

Pass the environment ID as a string when you create a session (see [Start a session](managed-agents-sessions.md)).

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

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
)
```

## Configuration options

### Packages

The `packages` field installs packages into the sandbox before the agent uses it. Package managers run in alphabetical order (apt, cargo, gem, go, npm, pip). You can pin specific versions. If the environment uses `limited` [networking](#networking), also set `allow_package_managers` in `networking` to `true`; otherwise, the API rejects the request with a 400 error.

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
    type: limited
    allow_package_managers: true
```

Supported package managers:

| Field | Package manager | Example |
|----|----|----|
| `apt` | System packages (apt-get) | `"graphviz"` |
| `cargo` | Rust (cargo) | `"hyperfine@1.18.0"` |
| `gem` | Ruby (gem) | `"rails:7.1.0"` |
| `go` | Go modules | `"golang.org/x/tools/cmd/goimports@latest"` |
| `npm` | Node.js (npm) | `"express@4.18.0"` |
| `pip` | Python (pip) | `"sqlalchemy==2.0.30"` |

### Networking

The `networking` field controls the sandbox’s outbound network access.

With `limited` networking, `allowed_hosts` also applies to the `web_search` and `web_fetch` tools, which run on Anthropic’s servers. A `web_fetch` call for a URL on a host that `allowed_hosts` does not match returns an error result to the agent. `web_search` omits results from hosts that `allowed_hosts` does not match. `allow_package_managers` and `allow_mcp_servers` add no hosts for these tools. When `allowed_hosts` lists no hosts, no `web_fetch` or `web_search` call returns a page or a search result. A host that you add to `allowed_hosts` for these tools is also open to the sandbox. `unrestricted` networking and self-hosted environments do not limit these tools. To restrict them further, set `allowed_domains` or `blocked_domains` on the tool’s entry in the agent toolset. See [Restrict web search and web fetch domains](managed-agents-tools-web-restrictions.md).

| Mode | Description |
|----|----|
| `limited` | Restricts sandbox network access to the hosts in `allowed_hosts`. Set `allow_package_managers` and `allow_mcp_servers` to `true` to allow additional access. Use this mode unless the agent must reach sites you cannot list in advance. |
| `unrestricted` | Full outbound network access, except for a general safety blocklist. Before you use it, read [Risks of unrestricted networking](#risks-of-unrestricted-networking). |



Set `networking` explicitly in API requests; a create request that omits it gets `unrestricted`. The Claude Console’s form for creating an environment starts with **Limited** selected and nothing else allowed.

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

CLI

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

Use `limited` networking with an explicit `allowed_hosts` list. Follow the principle of least privilege by granting only the minimum network access your agent requires, and regularly audit your allowed hosts.

With `limited` networking and no other fields set, no hosts are allowed. Files, memory stores, and GitHub repositories that you attach to the session stay available. When a request from the sandbox on port 80 or 443 is refused because its host is not allowed, the response is a 403 that names the blocked host.

When using `limited` networking:

- `allowed_hosts` specifies hosts the sandbox can reach. Specify bare hostnames or wildcard patterns (such as `*.example.com`). Do not include a URL scheme, port, or path. A bare hostname matches that exact host: `example.com` does not match `www.example.com`. `*.example.com` matches every subdomain of `example.com`, but not `example.com` itself.
- `allow_mcp_servers` allows outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`. While it is `false`, session creation fails with a 400 error if the agent declares an MCP server whose host is not in `allowed_hosts`. The same applies to [an agent it can delegate to](managed-agents-multiagent-orchestration.md). To fix it, add the host to `allowed_hosts` or set `allow_mcp_servers` to `true`.
- `allow_package_managers` allows outbound access to a set of public package registries and code hosts beyond those listed in the `allowed_hosts` array. See [Package manager hosts](#package-manager-hosts) for the list. Defaults to `false`. Set it to `true` whenever the environment specifies `packages`. Otherwise, the API rejects the request with a 400 error, even if `allowed_hosts` lists the registry hosts.

#### Package manager hosts

When `allow_package_managers` is `true`, the sandbox can reach the following hosts in addition to those in `allowed_hosts`. Anthropic maintains this list and can change it.

| Ecosystem | Hosts |
|----|----|
| Code hosting | `github.com`, `api.github.com`, `codeload.github.com`, `raw.githubusercontent.com`, `objects.githubusercontent.com`, `release-assets.githubusercontent.com`, `gitlab.com`, `bitbucket.org` |
| Node.js | `registry.npmjs.org`, `registry.yarnpkg.com`, `nodejs.org` |
| Python | `pypi.org`, `files.pythonhosted.org` |
| Rust | `crates.io`, `index.crates.io`, `static.crates.io`, `static.rust-lang.org` |
| Go | `proxy.golang.org`, `sum.golang.org` |
| Java | `repo1.maven.org`, `repo.maven.apache.org`, `services.gradle.org`, `plugins.gradle.org`, `plugins-artifacts.gradle.org` |
| Ruby | `rubygems.org`, `index.rubygems.org` |
| PHP | `packagist.org`, `repo.packagist.org` |
| Ubuntu (apt) | `archive.ubuntu.com`, `security.ubuntu.com`, `ppa.launchpad.net` |
| Containers | `registry-1.docker.io`, `auth.docker.io`, `production.cloudflare.docker.com`, `download.docker.com`, `ghcr.io` |



Network access is granted by host, not by operation. The sandbox can send any request to an allowed host, including uploads such as `git push` and package publishing, with any credential the command supplies. If the agent processes untrusted input (repository files, fetched web content, or third-party tool output), a successful prompt injection could use an allowed host to copy files out of the sandbox. To reduce this risk, set the `bash` tool’s [permission policy](managed-agents-permission-policies.md) to `always_ask` or `auto`. If the environment does not specify `packages`, you can instead leave `allow_package_managers` set to `false` and list only the hosts your agent needs in `allowed_hosts`.

#### Risks of unrestricted networking

With `unrestricted` networking, code in the sandbox can send requests to any host on the internet, except for hosts on a general safety blocklist. Before you choose this mode, consider what the agent can do with that access:

- **The agent can change things on external sites, not only read them:** The `bash` tool can send any request. The agent can post data, submit forms, call APIs, and run scripts that change data on external sites. Even a request that only fetches a URL can change data on some sites.
- **Nothing pauses these requests by default:** The agent toolset’s default [permission policy](managed-agents-permission-policies.md) is `always_allow`, so `bash` commands run without approval.
- **Anything in the sandbox can leave it:** This includes files, tool outputs, and any credentials or secrets you put in the sandbox.
- **Fetched content can steer the agent:** Webpages, API responses, and other content the agent reads can contain instructions (prompt injection) that change what it does next.
- **The agent acts on your behalf:** Its actions can violate a site’s terms of service, or create accounts and records there.
- **Model behavior is not a security control:** The agent can act on external sites in ways you did not ask for, including retrying in a different way after a site blocks a request. Use network settings and permission policies to limit what it can do.
- **The safety blocklist is not an allowlist:** It does not limit which other sites the agent reaches, or what the agent does on them.

To reduce these risks, use `limited` networking with an explicit list of hosts. The following `networking` value allows `api.example.com`, plus the [package manager hosts](#package-manager-hosts) for an agent that installs packages:

```python
{
  "type": "limited",
  "allowed_hosts": ["api.example.com"],
  "allow_package_managers": true
}
```



An agent that only uses the `web_search` and `web_fetch` tools does not need `unrestricted` networking if you can list the sites it needs. With `limited` networking, `allowed_hosts` also applies to those tools (see [Networking](#networking)), so list those sites in `allowed_hosts`. Listing them in `web_search`’s `allowed_domains` too makes it search those sites. A host that you add to `allowed_hosts` is also open to the sandbox. To restrict the tools further, see [Restrict web search and web fetch domains](managed-agents-tools-web-restrictions.md).

Use `unrestricted` only when the agent must reach sites you cannot list in advance. In that case, keep secrets and sensitive files out of the sandbox, and give the agent only the credentials the task needs. Consider setting the `bash` tool’s permission policy to `always_ask` or `auto`, and [watch the session’s events](managed-agents-events-and-streaming.md).

## Environment lifecycle

- Environments persist until you archive or delete them.
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

Python



```python
# List environments
environments = client.beta.environments.list()

# Retrieve a specific environment
env = client.beta.environments.retrieve(environment.id)

# Archive an environment (read-only, no new sessions)
client.beta.environments.archive(environment.id)

# Delete an environment
client.beta.environments.delete(environment.id)
```

## Preinstalled runtimes

Cloud sandboxes include common language runtimes, databases, and command-line tools. See [Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md) for the full list.

## Next steps



[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

Preinstalled packages, databases, and utilities available in cloud sandboxes.



[Start a session](managed-agents-sessions.md)

Create a session to run your agent and start running tasks.

## Availability

Cloud sandboxes

Cloud platform

Cloud platform: Claude API

Availability requirements for Cloud sandboxes are the same across all supported platforms.

Claude API

Status  
Beta

API  
- Managed Agents

Beta header  
Requires

managed-agents-2026-04-01

Models  
- All models

Claude Platform on AWS

Status  
Beta

API  
- Managed Agents

Beta header  
Requires

managed-agents-2026-04-01

Models  
- All models

Claude Models on Google Cloud (Anthropic managed)

Status  
Beta

API  
- Managed Agents

Beta header  
Requires

managed-agents-2026-04-01

Models  
- All models

### Data handling

[Data handling overview](manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/agents`
- `/v1/sessions`
- `/v1/environments`

Zero data retentionNot eligible

Not eligible for ZDR, except for self-hosted Managed Agents. Sessions are stateful resources; transcripts persist until you delete them. [Learn more](managed-agents-self-hosted-data-and-access.md#how-long-data-is-kept)

HIPAANot eligible

Not eligible for HIPAA. Applies to all Managed Agents sub-features.
