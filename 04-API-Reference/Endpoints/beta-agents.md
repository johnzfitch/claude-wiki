---
title: "Agents - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/agents"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:29Z"
tags: ["agents", "api"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fagents)

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


Create Agent


List Agents


Get Agent


Update Agent


Archive Agent

Versions

Environments

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

# Agents

##### [Create Agent](https://platform.claude.com/docs/en/api/http/beta/agents/create)

POST/v1/agents

##### [List Agents](https://platform.claude.com/docs/en/api/http/beta/agents/list)

GET/v1/agents

##### [Get Agent](https://platform.claude.com/docs/en/api/http/beta/agents/retrieve)

GET/v1/agents/{agent_id}

##### [Update Agent](https://platform.claude.com/docs/en/api/http/beta/agents/update)

POST/v1/agents/{agent_id}

##### [Archive Agent](https://platform.claude.com/docs/en/api/http/beta/agents/archive)

POST/v1/agents/{agent_id}/archive

##### Models



BetaManagedAgentsAdvisor object{ type: "advisor", model }



Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

type: "advisor"



model: string



The advisor model id.



BetaManagedAgentsAgent object{ type: "agent", id, archived_at, 12 more }



A Managed Agents `agent`.



BetaManagedAgentsAgentReference object{ type: "agent", id, version }



A resolved agent reference with a concrete version.

type: "agent"



id: string





version: number



formatint32



BetaManagedAgentsAgentToolConfig = [BetaManagedAgentsBashToolConfig](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_bash_tool_config) or [BetaManagedAgentsEditToolConfig](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_edit_tool_config) or [BetaManagedAgentsReadToolConfig](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_read_tool_config) or 5 more



Configuration for a specific agent tool.

One of the following:



BetaManagedAgentsAgentToolConfigParams = [BetaManagedAgentsBashToolConfigParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_bash_tool_config_params) or [BetaManagedAgentsEditToolConfigParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_edit_tool_config_params) or [BetaManagedAgentsReadToolConfigParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_read_tool_config_params) or 5 more



Configuration override for a specific tool within a toolset.

One of the following:



BetaManagedAgentsAgentToolsetDefaultConfig object{ enabled, permission_policy }



Resolved default configuration for agent tools.



BetaManagedAgentsAgentToolsetDefaultConfigParams object{ enabled, permission_policy }



Default configuration for all tools in a toolset.



BetaManagedAgentsAgentToolset20260401 object{ type: "agent_toolset_20260401", configs, default_config }





BetaManagedAgentsAgentToolset20260401BashInput object{ command, restart, timeout_ms }



Input payload for the `bash` tool of the `agent_toolset_20260401` toolset. All fields are optional; a normal invocation supplies `command`, while `restart=true` (with no `command`) reboots the runner-side bash session.

command: optional string



Shell command to execute. Omit only when `restart` is true.

restart: optional boolean



When true, restart the persistent bash session instead of running a command. Subsequent calls without `restart` will run against the fresh session.



timeout_ms: optional number



Per-call timeout in milliseconds. Defaults to the runner-wide tool timeout when omitted or zero.

minimum0



BetaManagedAgentsAgentToolset20260401EditInput object{ file_path, new_string, old_string, replace_all }



Input payload for the `edit` tool. Performs a string replacement in the named file; by default `old_string` must occur exactly once.

file_path: string



Path of the file to edit.

new_string: string



Replacement text.

old_string: string



Substring to find and replace.

replace_all: optional boolean



When true, replace every occurrence of `old_string` instead of requiring a unique match.



BetaManagedAgentsAgentToolset20260401GlobInput object{ pattern, path }



Input payload for the `glob` tool. Returns paths matching a doublestar glob pattern, newest first.

pattern: string



Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns are only permitted when the runner is configured to allow them.

path: optional string



Optional directory root to search under. Defaults to the runner's working directory.



BetaManagedAgentsAgentToolset20260401GrepInput object{ pattern, path }



Input payload for the `grep` tool. Searches file contents for a regular expression, returning matching lines.

pattern: string



Regular expression to search for.

path: optional string



Optional directory root to search under. Defaults to the runner's working directory.



BetaManagedAgentsAgentToolset20260401Params object{ type: "agent_toolset_20260401", configs, default_config }



Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.



BetaManagedAgentsAgentToolset20260401ReadInput object{ file_path, view_range }



Input payload for the `read` tool. Reads file contents relative to the runner's working directory (or absolute when the runner permits).

file_path: string



Path of the file to read.



view_range: optional array of number



Optional `[start_line, end_line]` 1-indexed inclusive range. When omitted the entire file is returned. `end_line` of 0 or negative means "to end of file".

minItems2

maxItems2



BetaManagedAgentsAgentToolset20260401WriteInput object{ content, file_path }



Input payload for the `write` tool. Writes (overwriting) the entire file contents.

content: string



Full file contents to write.

file_path: string



Path of the file to write.



BetaManagedAgentsAlwaysAllowPolicy object{ type: "always_allow" }



Tool calls are automatically approved without user confirmation.

type: "always_allow"





BetaManagedAgentsAlwaysAskPolicy object{ type: "always_ask" }



Tool calls require user confirmation before execution.

type: "always_ask"





BetaManagedAgentsAnthropicSkill object{ type: "anthropic", skill_id, version }



A resolved Anthropic-managed skill.

type: "anthropic"



skill_id: string



version: string





BetaManagedAgentsAnthropicSkillParams object{ type: "anthropic", skill_id, version }



An Anthropic-managed skill.

type: "anthropic"





skill_id: string



Identifier of the Anthropic skill (e.g., "xlsx").

minLength1

maxLength64



version: optional string or null



Version to pin. Defaults to latest if omitted.

minLength1

maxLength64



BetaManagedAgentsAutoPolicy object{ type: "auto" }



The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

type: "auto"





BetaManagedAgentsBashToolConfig object{ type: "bash", enabled, name, permission_policy }



Configuration for the bash tool.



BetaManagedAgentsBashToolConfigParams object{ type: "bash", name, enabled, permission_policy }



Configuration override for the bash tool.



BetaManagedAgentsCustomSkill object{ type: "custom", skill_id, version }



A resolved user-created custom skill.

type: "custom"



skill_id: string



version: string





BetaManagedAgentsCustomSkillParams object{ type: "custom", skill_id, version }



A user-created custom skill.

type: "custom"





skill_id: string



Tagged ID of the custom skill (e.g., "skill_01XJ5...").

minLength1

maxLength64



version: optional string or null



Version to pin. Defaults to latest if omitted.

minLength1

maxLength64



BetaManagedAgentsCustomTool object{ type: "custom", description, input_schema, name }



A custom tool as returned in API responses.

type: "custom"



description: string





input_schema: [BetaManagedAgentsCustomToolInputSchema](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_custom_tool_input_schema) { type: "object", properties, required }



JSON Schema for custom tool input parameters.

type: "object"



properties: optional map\[unknown\] or null



required: optional array of string or null



name: string





BetaManagedAgentsCustomToolInputSchema object{ type: "object", properties, required }



JSON Schema for custom tool input parameters.

type: "object"



properties: optional map\[unknown\] or null



required: optional array of string or null





BetaManagedAgentsCustomToolParams object{ type: "custom", description, input_schema, name }



A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

type: "custom"





description: string



Description of what the tool does, shown to the agent to help it decide when to use the tool.

minLength1



input_schema: [BetaManagedAgentsCustomToolInputSchema](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_custom_tool_input_schema) { type: "object", properties, required }



JSON Schema defining the expected input parameters for the tool.

type: "object"



properties: optional map\[unknown\] or null



required: optional array of string or null





name: string



Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

minLength1

maxLength128



BetaManagedAgentsEditToolConfig object{ type: "edit", enabled, name, permission_policy }



Configuration for the edit tool.



BetaManagedAgentsEditToolConfigParams object{ type: "edit", name, enabled, permission_policy }



Configuration override for the edit tool.



BetaManagedAgentsEffortHigh object{ type: "high" }



High effort. Favors reasoning depth.

type: "high"





BetaManagedAgentsEffortLow object{ type: "low" }



Low effort. Favors latency over reasoning depth.

type: "low"





BetaManagedAgentsEffortMax object{ type: "max" }



Maximum effort. Favors reasoning depth over latency.

type: "max"





BetaManagedAgentsEffortMedium object{ type: "medium" }



Medium effort. Balances latency and reasoning depth.

type: "medium"





BetaManagedAgentsEffortXhigh object{ type: "xhigh" }



Extra-high effort. Not all models accept this level.

type: "xhigh"





BetaManagedAgentsGlobToolConfig object{ type: "glob", enabled, name, permission_policy }



Configuration for the glob tool.



BetaManagedAgentsGlobToolConfigParams object{ type: "glob", name, enabled, permission_policy }



Configuration override for the glob tool.



BetaManagedAgentsGrepToolConfig object{ type: "grep", enabled, name, permission_policy }



Configuration for the grep tool.



BetaManagedAgentsGrepToolConfigParams object{ type: "grep", name, enabled, permission_policy }



Configuration override for the grep tool.



BetaManagedAgentsMCPServerURLDefinition object{ type: "url", name, url }



URL-based MCP server connection as returned in API responses.

type: "url"



name: string



url: string





BetaManagedAgentsMCPToolConfig object{ enabled, name, permission_policy }



Resolved configuration for a specific MCP tool.



BetaManagedAgentsMCPToolConfigParams object{ name, enabled, permission_policy }



Configuration override for a specific MCP tool.



BetaManagedAgentsMCPToolset object{ type: "mcp_toolset", configs, default_config, mcp_server_name }





BetaManagedAgentsMCPToolsetDefaultConfig object{ enabled, permission_policy }



Resolved default configuration for all tools from an MCP server.



BetaManagedAgentsMCPToolsetDefaultConfigParams object{ enabled, permission_policy }



Default configuration for all tools from an MCP server.



BetaManagedAgentsMCPToolsetParams object{ type: "mcp_toolset", mcp_server_name, configs, default_config }



Configuration for tools from an MCP server defined in `mcp_servers`.



BetaManagedAgentsModel = string or "claude-opus-5-5" or "claude-fable-5-1" or "claude-sonnet-5" or 12 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModelConfig object{ id, effort, inference_geo, speed }



Model identifier and configuration.



BetaManagedAgentsModelConfigParams object{ id, effort, inference_geo, speed }



An object that defines additional configuration control over model use



BetaManagedAgentsMultiagentCoordinator object{ type: "coordinator", agents }



Resolved coordinator topology with a concrete agent roster.



BetaManagedAgentsMultiagentCoordinatorParams object{ type: "coordinator", agents }



A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



BetaManagedAgentsMultiagentSelfParams object{ type: "self" }



Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: "self"





BetaManagedAgentsReadToolConfig object{ type: "read", enabled, name, permission_policy }



Configuration for the read tool.



BetaManagedAgentsReadToolConfigParams object{ type: "read", name, enabled, permission_policy }



Configuration override for the read tool.



BetaManagedAgentsSessionThreadAgent object{ type: "agent", id, description, 7 more }



Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.



BetaManagedAgentsSkillParams = [BetaManagedAgentsAnthropicSkillParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_anthropic_skill_params) or [BetaManagedAgentsCustomSkillParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_custom_skill_params)



Skill to load in the session container.

One of the following:



BetaManagedAgentsURLMCPServerParams object{ type: "url", name, url }



URL-based MCP server connection.

type: "url"





name: string



Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

minLength1

maxLength255



url: string



Endpoint URL for the MCP server.

maxLength2048



BetaManagedAgentsUserLocation object{ type: "approximate", city, country, 2 more }



Approximate user location for search result localization.

type: "approximate"



Location precision. Only "approximate" is supported.



city: optional string or null



City name.

minLength1

maxLength255

country: optional string or null



Two-letter ISO 3166-1 country code, uppercase.



region: optional string or null



Region or state name.

minLength1

maxLength255



timezone: optional string or null



IANA timezone identifier, e.g. "America/Los_Angeles".

minLength1

maxLength255



BetaManagedAgentsWebFetchToolConfig object{ type: "web_fetch", enabled, name, 4 more }



Configuration for the web_fetch tool.



BetaManagedAgentsWebFetchToolConfigParams object{ type: "web_fetch", name, allowed_domains, 4 more }



Configuration override for the web_fetch tool.



BetaManagedAgentsWebSearchToolConfig object{ type: "web_search", enabled, name, 4 more }



Configuration for the web_search tool.



BetaManagedAgentsWebSearchToolConfigParams object{ type: "web_search", name, allowed_domains, 4 more }



Configuration override for the web_search tool.



BetaManagedAgentsWriteToolConfig object{ type: "write", enabled, name, permission_policy }



Configuration for the write tool.



BetaManagedAgentsWriteToolConfigParams object{ type: "write", name, enabled, permission_policy }



Configuration override for the write tool.

#### Agents[Versions](https://platform.claude.com/docs/en/api/http/beta/agents/versions)

##### [List Agent Versions](https://platform.claude.com/docs/en/api/http/beta/agents/versions/list)

GET/v1/agents/{agent_id}/versions
