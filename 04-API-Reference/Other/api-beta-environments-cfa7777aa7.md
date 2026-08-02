---
title: "Environments - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/environments"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:38:15Z"
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

Environments




cURL

# Environments

##### [Create Environment](/docs/en/api/beta/environments/create)

POST/v1/environments

##### [List Environments](/docs/en/api/beta/environments/list)

GET/v1/environments

##### [Get Environment](/docs/en/api/beta/environments/retrieve)

GET/v1/environments/{environment_id}

##### [Update Environment](/docs/en/api/beta/environments/update)

POST/v1/environments/{environment_id}

##### [Delete Environment](/docs/en/api/beta/environments/delete)

DELETE/v1/environments/{environment_id}

##### [Archive Environment](/docs/en/api/beta/environments/archive)

POST/v1/environments/{environment_id}/archive

##### ModelsExpand Collapse 

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

BetaCloudConfigParams object { type, networking, packages }



Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the existing value.

type: "cloud"



Environment type

[](#beta_cloud_config_params.type)



networking: optional [BetaUnrestrictedNetwork](/docs/en/api/beta/environments#beta_unrestricted_network) { type } or [BetaLimitedNetworkParams](/docs/en/api/beta/environments#beta_limited_network_params) { type, allow_mcp_servers, allow_package_managers, allowed_hosts }



Network configuration policy. Omit on update to preserve the existing value.

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

BetaLimitedNetworkParams object { type, allow_mcp_servers, allow_package_managers, allowed_hosts }



Limited network request params.

Fields default to null; on update, omitted fields preserve the existing value.

type: "limited"



Network policy type

[](#beta_limited_network_params.type)

allow_mcp_servers: optional boolean



Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

[](#beta_limited_network_params.allow_mcp_servers)

allow_package_managers: optional boolean



Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

[](#beta_limited_network_params.allow_package_managers)

allowed_hosts: optional array of string



Specifies domains the container can reach.

[](#beta_limited_network_params.allowed_hosts)

[](#beta_limited_network_params)

[](#beta_cloud_config_params.networking)



packages: optional [BetaPackagesParams](/docs/en/api/beta/environments#beta_packages_params) { apt, cargo, gem, 4 more }



Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: optional array of string



Ubuntu/Debian packages to install

[](#beta_cloud_config_params.packages%20%2B%20(resource)%20beta.environments.apt)

cargo: optional array of string



Rust packages to install

[](#beta_cloud_config_params.packages%20%2B%20(resource)%20beta.environments.cargo)

gem: optional array of string



Ruby packages to install

[](#beta_cloud_config_params.packages%20%2B%20(resource)%20beta.environments.gem)

go: optional array of string



Go packages to install

[](#beta_cloud_config_params.packages%20%2B%20(resource)%20beta.environments.go)

npm: optional array of string



Node.js packages to install

[](#beta_cloud_config_params.packages%20%2B%20(resource)%20beta.environments.npm)

pip: optional array of string



Python packages to install

[](#beta_cloud_config_params.packages%20%2B%20(resource)%20beta.environments.pip)

type: optional "packages"



Package configuration type

[](#beta_cloud_config_params.packages%20%2B%20(resource)%20beta.environments.type)

[](#beta_cloud_config_params.packages)

[](#beta_cloud_config_params)

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



BetaEnvironmentDeleteResponse object { id, type }



Response after deleting an environment.

id: string



Environment identifier

[](#beta_environment_delete_response.id)

type: "environment_deleted"



The type of response

[](#beta_environment_delete_response.type)

[](#beta_environment_delete_response)

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



BetaLimitedNetworkParams object { type, allow_mcp_servers, allow_package_managers, allowed_hosts }



Limited network request params.

Fields default to null; on update, omitted fields preserve the existing value.

type: "limited"



Network policy type

[](#beta_limited_network_params.type)

allow_mcp_servers: optional boolean



Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

[](#beta_limited_network_params.allow_mcp_servers)

allow_package_managers: optional boolean



Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

[](#beta_limited_network_params.allow_package_managers)

allowed_hosts: optional array of string



Specifies domains the container can reach.

[](#beta_limited_network_params.allowed_hosts)

[](#beta_limited_network_params)



BetaPackages object { apt, cargo, gem, 4 more }



Packages (and their versions) available in this environment.

apt: array of string



Ubuntu/Debian packages to install

[](#beta_packages.apt)

cargo: array of string



Rust packages to install

[](#beta_packages.cargo)

gem: array of string



Ruby packages to install

[](#beta_packages.gem)

go: array of string



Go packages to install

[](#beta_packages.go)

npm: array of string



Node.js packages to install

[](#beta_packages.npm)

pip: array of string



Python packages to install

[](#beta_packages.pip)

type: optional "packages"



Package configuration type

[](#beta_packages.type)

[](#beta_packages)



BetaPackagesParams object { apt, cargo, gem, 4 more }



Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: optional array of string



Ubuntu/Debian packages to install

[](#beta_packages_params.apt)

cargo: optional array of string



Rust packages to install

[](#beta_packages_params.cargo)

gem: optional array of string



Ruby packages to install

[](#beta_packages_params.gem)

go: optional array of string



Go packages to install

[](#beta_packages_params.go)

npm: optional array of string



Node.js packages to install

[](#beta_packages_params.npm)

pip: optional array of string



Python packages to install

[](#beta_packages_params.pip)

type: optional "packages"



Package configuration type

[](#beta_packages_params.type)

[](#beta_packages_params)



BetaSelfHostedConfig object { type }



Configuration for self-hosted environments.

type: "self_hosted"



Environment type

[](#beta_self_hosted_config.type)

[](#beta_self_hosted_config)



BetaSelfHostedConfigParams object { type }



Request params for `self_hosted` environment configuration.

type: "self_hosted"



Environment type

[](#beta_self_hosted_config_params.type)

[](#beta_self_hosted_config_params)



BetaUnrestrictedNetwork object { type }



Unrestricted network access.

type: "unrestricted"



Network policy type

[](#beta_unrestricted_network.type)

[](#beta_unrestricted_network)

#### EnvironmentsWork

##### [Get Work Item](/docs/en/api/beta/environments/work/retrieve)

GET/v1/environments/{environment_id}/work/{work_id}

##### [Poll for Work](/docs/en/api/beta/environments/work/poll)

GET/v1/environments/{environment_id}/work/poll

##### [Acknowledge Work](/docs/en/api/beta/environments/work/ack)

POST/v1/environments/{environment_id}/work/{work_id}/ack

##### [Record Heartbeat](/docs/en/api/beta/environments/work/heartbeat)

POST/v1/environments/{environment_id}/work/{work_id}/heartbeat

##### [Stop Work](/docs/en/api/beta/environments/work/stop)

POST/v1/environments/{environment_id}/work/{work_id}/stop

##### [List Work Items](/docs/en/api/beta/environments/work/list)

GET/v1/environments/{environment_id}/work

##### [Update Work Item](/docs/en/api/beta/environments/work/update)

POST/v1/environments/{environment_id}/work/{work_id}

##### [Get Queue Statistics](/docs/en/api/beta/environments/work/stats)

GET/v1/environments/{environment_id}/work/stats
