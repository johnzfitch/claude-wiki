---
title: "Environments - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/environments"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:34:04Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)

# Environments

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

BetaEnvironmentArchivedErrorDetails object{ error_code }



The environment is archived, so it cannot be updated.

error_code: "environment_archived"





BetaEnvironmentCreateDisabledErrorDetails object{ error_code }



Anthropic has turned off creating environments for this organization. Existing environments still work.

error_code: "environment_create_disabled"



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

BetaEnvironmentNotFoundErrorDetails object{ error_code }



`settings.environment_id` names no Environment within the organization's reach.

error_code: "environment_not_found"





BetaEnvironmentUpdateDisabledErrorDetails object{ error_code }



Anthropic has turned off updating environments for this organization. Existing environments still work as they are.

error_code: "environment_update_disabled"





BetaInvalidConfigTypeChangeErrorDetails object{ error_code }



`config.type` differs from the environment's stored type, which cannot change after creation.

error_code: "invalid_config_type_change"





BetaInvalidMetadataErrorDetails object{ error_code }



`metadata` has too many keys, a key or value that is too long, or a reserved key. The message names each problem.

error_code: "invalid_metadata"



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
