---
title: "Environments - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/environments"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:37Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fenvironments)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments


Create Environment


List Environments


Get Environment


Update Environment


Delete Environment


Archive Environment

Work

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](http-beta.md)

# Environments

##### [Create Environment](https://platform.claude.com/docs/en/api/http/beta/environments/create)

POST/v1/environments

Create a new environment with the specified configuration.

##### [List Environments](https://platform.claude.com/docs/en/api/http/beta/environments/list)

GET/v1/environments

List environments with pagination support.

##### [Get Environment](https://platform.claude.com/docs/en/api/http/beta/environments/retrieve)

GET/v1/environments/{environment_id}

Retrieve a specific environment by ID.

##### [Update Environment](https://platform.claude.com/docs/en/api/http/beta/environments/update)

POST/v1/environments/{environment_id}

Update an existing environment's configuration.

##### [Delete Environment](https://platform.claude.com/docs/en/api/http/beta/environments/delete)

DELETE/v1/environments/{environment_id}

Delete an environment by ID. Returns a confirmation of the deletion.

##### [Archive Environment](https://platform.claude.com/docs/en/api/http/beta/environments/archive)

POST/v1/environments/{environment_id}/archive

Archive an environment by ID. Archived environments cannot be used to create new sessions.

##### Models



BetaCloudConfig object{ type: "cloud", networking, packages }



`cloud` environment configuration.



BetaCloudConfigParams object{ type: "cloud", networking, packages }



Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the existing value.



BetaEnvironment object{ type: "environment", id, archived_at, 7 more }



Unified Environment resource for both cloud and self-hosted environments.



BetaEnvironmentDeleteResponse object{ type: "environment_deleted", id }



Response after deleting an environment.



type: "environment_deleted"



The type of response

defaultenvironment_deleted

id: string



Environment identifier



BetaLimitedNetwork object{ type: "limited", allow_mcp_servers, allow_package_managers, allowed_hosts }



Limited network access.

type: "limited"



Network policy type

allow_mcp_servers: boolean



Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow_package_managers: boolean



Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed_hosts: array of string



Specifies domains the container can reach.



BetaLimitedNetworkParams object{ type: "limited", allow_mcp_servers, allow_package_managers, allowed_hosts }



Limited network request params.

Fields default to null; on update, omitted fields preserve the existing value.

type: "limited"



Network policy type

allow_mcp_servers: optional boolean or null



Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow_package_managers: optional boolean or null



Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false` on creation. Must be `true` when `packages` are specified.

allowed_hosts: optional array of string or null



Specifies domains the container can reach.



BetaPackages object{ type: "packages", apt, cargo, 4 more }



Packages (and their versions) available in this environment.



type: optional "packages"



Package configuration type

defaultpackages

apt: array of string



Ubuntu/Debian packages to install

cargo: array of string



Rust packages to install

gem: array of string



Ruby packages to install

go: array of string



Go packages to install

npm: array of string



Node.js packages to install

pip: array of string



Python packages to install



BetaPackagesParams object{ type: "packages", apt, cargo, 4 more }



Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Under `limited` networking, requires `networking.allow_package_managers` to be `true`.



BetaSelfHostedConfig object{ type: "self_hosted" }



Configuration for self-hosted environments.

type: "self_hosted"



Environment type



BetaSelfHostedConfigParams object{ type: "self_hosted" }



Request params for `self_hosted` environment configuration.

type: "self_hosted"



Environment type



BetaUnrestrictedNetwork object{ type: "unrestricted" }



Unrestricted network access.

type: "unrestricted"



Network policy type

#### Environments[Work](https://platform.claude.com/docs/en/api/http/beta/environments/work)

##### [Get Work Item](https://platform.claude.com/docs/en/api/http/beta/environments/work/retrieve)

GET/v1/environments/{environment_id}/work/{work_id}

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Poll for Work](https://platform.claude.com/docs/en/api/http/beta/environments/work/poll)

GET/v1/environments/{environment_id}/work/poll

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Acknowledge Work](https://platform.claude.com/docs/en/api/http/beta/environments/work/ack)

POST/v1/environments/{environment_id}/work/{work_id}/ack

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Record Heartbeat](https://platform.claude.com/docs/en/api/http/beta/environments/work/heartbeat)

POST/v1/environments/{environment_id}/work/{work_id}/heartbeat

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Stop Work](https://platform.claude.com/docs/en/api/http/beta/environments/work/stop)

POST/v1/environments/{environment_id}/work/{work_id}/stop

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [List Work Items](https://platform.claude.com/docs/en/api/http/beta/environments/work/list)

GET/v1/environments/{environment_id}/work

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Update Work Item](https://platform.claude.com/docs/en/api/http/beta/environments/work/update)

POST/v1/environments/{environment_id}/work/{work_id}

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Get Queue Statistics](https://platform.claude.com/docs/en/api/http/beta/environments/work/stats)

GET/v1/environments/{environment_id}/work/stats

Get statistics about the work queue for an environment.
