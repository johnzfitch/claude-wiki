---
title: "Get Environment - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/environments/retrieve"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:55Z"
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


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments


Create Environment


List Environments


Get Environment


Update Environment


Delete Environment


Archive Environment

Work

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Retrieve




cURL

# Get Environment

GET/v1/environments/{environment_id}

Retrieve a specific environment by ID.

##### Path ParametersExpand Collapse 

environment_id: string



[](#retrieve.environment_id)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string



[](#anthropic_beta%5B0%5D)



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more



One of the following:

"message-batches-2024-09-24"



[](#anthropic_beta%5B1%5D%5B0%5D)

"prompt-caching-2024-07-31"



[](#anthropic_beta%5B1%5D%5B1%5D)

"computer-use-2024-10-22"



[](#anthropic_beta%5B1%5D%5B2%5D)

"computer-use-2025-01-24"



[](#anthropic_beta%5B1%5D%5B3%5D)

"pdfs-2024-09-25"



[](#anthropic_beta%5B1%5D%5B4%5D)

"token-counting-2024-11-01"



[](#anthropic_beta%5B1%5D%5B5%5D)

"token-efficient-tools-2025-02-19"



[](#anthropic_beta%5B1%5D%5B6%5D)

"output-128k-2025-02-19"



[](#anthropic_beta%5B1%5D%5B7%5D)

"files-api-2025-04-14"



[](#anthropic_beta%5B1%5D%5B8%5D)

"mcp-client-2025-04-04"



[](#anthropic_beta%5B1%5D%5B9%5D)

"mcp-client-2025-11-20"



[](#anthropic_beta%5B1%5D%5B10%5D)

"dev-full-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B11%5D)

"interleaved-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B12%5D)

"code-execution-2025-05-22"



[](#anthropic_beta%5B1%5D%5B13%5D)

"extended-cache-ttl-2025-04-11"



[](#anthropic_beta%5B1%5D%5B14%5D)

"context-1m-2025-08-07"



[](#anthropic_beta%5B1%5D%5B15%5D)

"context-management-2025-06-27"



[](#anthropic_beta%5B1%5D%5B16%5D)

"model-context-window-exceeded-2025-08-26"



[](#anthropic_beta%5B1%5D%5B17%5D)

"skills-2025-10-02"



[](#anthropic_beta%5B1%5D%5B18%5D)

"fast-mode-2026-02-01"



[](#anthropic_beta%5B1%5D%5B19%5D)

"output-300k-2026-03-24"



[](#anthropic_beta%5B1%5D%5B20%5D)

"user-profiles-2026-03-24"



[](#anthropic_beta%5B1%5D%5B21%5D)

"advisor-tool-2026-03-01"



[](#anthropic_beta%5B1%5D%5B22%5D)

"managed-agents-2026-04-01"



[](#anthropic_beta%5B1%5D%5B23%5D)

"cache-diagnosis-2026-04-07"



[](#anthropic_beta%5B1%5D%5B24%5D)

"dreaming-2026-04-21"



[](#anthropic_beta%5B1%5D%5B25%5D)

"thinking-token-count-2026-05-13"



[](#anthropic_beta%5B1%5D%5B26%5D)

"server-side-fallback-2026-06-01"



[](#anthropic_beta%5B1%5D%5B27%5D)

"server-side-fallback-2026-07-01"



[](#anthropic_beta%5B1%5D%5B28%5D)

"fallback-credit-2026-06-01"



[](#anthropic_beta%5B1%5D%5B29%5D)

"fallback-credit-2026-07-01"



[](#anthropic_beta%5B1%5D%5B30%5D)

"agent-memory-2026-07-22"



[](#anthropic_beta%5B1%5D%5B31%5D)

[](#anthropic_beta%5B1%5D)

[](#retrieve.betas)

##### ReturnsExpand Collapse 



BetaEnvironment object { id, archived_at, config, 7 more }



Unified Environment resource for both cloud and self-hosted environments.

id: string



Environment identifier (e.g., 'env\_...')

[](#beta_environment.id)

archived_at: string



RFC 3339 timestamp when environment was archived, or null if not archived

[](#beta_environment.archived_at)



config: [BetaCloudConfig](/docs/en/api/beta/environments#beta_cloud_config) { networking, packages, type } or [BetaSelfHostedConfig](/docs/en/api/beta/environments#beta_self_hosted_config) { type }



Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:



BetaCloudConfig object { networking, packages, type }



`cloud` environment configuration.



networking: [BetaUnrestrictedNetwork](/docs/en/api/beta/environments#beta_unrestricted_network) { type } or [BetaLimitedNetwork](/docs/en/api/beta/environments#beta_limited_network) { allow_mcp_servers, allow_package_managers, allowed_hosts, type }



Network configuration policy.

One of the following:



BetaUnrestrictedNetwork object { type }



Unrestricted network access.

type: "unrestricted"



Network policy type

[](#beta_unrestricted_network.type)

[](#beta_unrestricted_network)



BetaLimitedNetwork object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }



Limited network access.

allow_mcp_servers: boolean



Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

[](#beta_limited_network.allow_mcp_servers)

allow_package_managers: boolean



Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

[](#beta_limited_network.allow_package_managers)

allowed_hosts: array of string



Specifies domains the container can reach.

[](#beta_limited_network.allowed_hosts)

type: "limited"



Network policy type

[](#beta_limited_network.type)

[](#beta_limited_network)

[](#beta_cloud_config.networking)



packages: [BetaPackages](/docs/en/api/beta/environments#beta_packages) { apt, cargo, gem, 4 more }



Package manager configuration.

apt: array of string



Ubuntu/Debian packages to install

[](#beta_cloud_config.packages%20%2B%20(resource)%20beta.environments.apt)

cargo: array of string



Rust packages to install

[](#beta_cloud_config.packages%20%2B%20(resource)%20beta.environments.cargo)

gem: array of string



Ruby packages to install

[](#beta_cloud_config.packages%20%2B%20(resource)%20beta.environments.gem)

go: array of string



Go packages to install

[](#beta_cloud_config.packages%20%2B%20(resource)%20beta.environments.go)

npm: array of string



Node.js packages to install

[](#beta_cloud_config.packages%20%2B%20(resource)%20beta.environments.npm)

pip: array of string



Python packages to install

[](#beta_cloud_config.packages%20%2B%20(resource)%20beta.environments.pip)

type: optional "packages"



Package configuration type

[](#beta_cloud_config.packages%20%2B%20(resource)%20beta.environments.type)

[](#beta_cloud_config.packages)

type: "cloud"



Environment type

[](#beta_cloud_config.type)

[](#beta_cloud_config)



BetaSelfHostedConfig object { type }



Configuration for self-hosted environments.

type: "self_hosted"



Environment type

[](#beta_self_hosted_config.type)

[](#beta_self_hosted_config)

[](#beta_environment.config)

created_at: string



RFC 3339 timestamp when environment was created

[](#beta_environment.created_at)

description: string



User-provided description for the environment

[](#beta_environment.description)

metadata: map\[string\]



User-provided metadata key-value pairs

[](#beta_environment.metadata)

name: string



Human-readable name for the environment

[](#beta_environment.name)

type: "environment"



The type of object (always 'environment')

[](#beta_environment.type)

updated_at: string



RFC 3339 timestamp when environment was last updated

[](#beta_environment.updated_at)



scope: optional "organization" or "account"



The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

"organization"



[](#beta_environment.scope%5B0%5D)

"account"



[](#beta_environment.scope%5B1%5D)

[](#beta_environment.scope)

[](#beta_environment)

Get Environment

cURL



```python
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
