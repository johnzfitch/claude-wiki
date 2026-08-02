---
title: "Sessions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:38:50Z"
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

Sessions


Create Session


List Sessions


Get Session


Update Session


Delete Session


Archive Session

Events

Resources

Threads

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

Sessions




cURL

# Sessions

##### [Create Session](/docs/en/api/beta/sessions/create)

POST/v1/sessions

##### [List Sessions](/docs/en/api/beta/sessions/list)

GET/v1/sessions

##### [Get Session](/docs/en/api/beta/sessions/retrieve)

GET/v1/sessions/{session_id}

##### [Update Session](/docs/en/api/beta/sessions/update)

POST/v1/sessions/{session_id}

##### [Delete Session](/docs/en/api/beta/sessions/delete)

DELETE/v1/sessions/{session_id}

##### [Archive Session](/docs/en/api/beta/sessions/archive)

POST/v1/sessions/{session_id}/archive

##### ModelsExpand Collapse 



BetaManagedAgentsAgentMessagePreview object { id, type }



id: string



The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

[](#beta_managed_agents_agent_message_preview.id)

type: "agent.message"



[](#beta_managed_agents_agent_message_preview.type)

[](#beta_managed_agents_agent_message_preview)



BetaManagedAgentsAgentParams object { id, type, version }



Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string



The `agent` ID.

[](#beta_managed_agents_agent_params.id)

type: "agent"



[](#beta_managed_agents_agent_params.type)

version: optional number



The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

[](#beta_managed_agents_agent_params.version)

[](#beta_managed_agents_agent_params)



BetaManagedAgentsAgentThinkingPreview object { id, type }



id: string



The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

[](#beta_managed_agents_agent_thinking_preview.id)

type: "agent.thinking"



[](#beta_managed_agents_agent_thinking_preview.type)

[](#beta_managed_agents_agent_thinking_preview)



BetaManagedAgentsAgentWithOverridesParams object { id, type, mcp_servers, 5 more }



Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

id: string



The `agent` ID.

[](#beta_managed_agents_agent_with_overrides_params.id)

type: "agent_with_overrides"



[](#beta_managed_agents_agent_with_overrides_params.type)



mcp_servers: optional array of [BetaManagedAgentsURLMCPServerParams](/docs/en/api/beta/agents#beta_managed_agents_url_mcp_server_params) { name, type, url }



Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

name: string



Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

[](#beta_managed_agents_url_mcp_server_params.name)

type: "url"



[](#beta_managed_agents_url_mcp_server_params.type)

url: string



Endpoint URL for the MCP server.

[](#beta_managed_agents_url_mcp_server_params.url)

[](#beta_managed_agents_agent_with_overrides_params.mcp_servers)



model: optional [BetaManagedAgentsModel](/docs/en/api/beta/agents#beta_managed_agents_model) or [BetaManagedAgentsModelConfigParams](/docs/en/api/beta/agents#beta_managed_agents_model_config_params) { id, effort, speed }



Replacement model. Accepts the model string, e.g. `claude-opus-4-6`, or a `model_config` object. Omit to use the agent's model.

One of the following:



BetaManagedAgentsModel = "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#beta_managed_agents_model%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_managed_agents_model%5B0%5D%5B1%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model%5B0%5D%5B2%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model%5B0%5D%5B3%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model%5B0%5D%5B4%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model%5B0%5D%5B5%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_managed_agents_model%5B0%5D%5B6%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model%5B0%5D%5B7%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model%5B0%5D%5B8%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model%5B0%5D%5B9%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model%5B0%5D%5B10%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_managed_agents_model%5B0%5D%5B11%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_managed_agents_model%5B0%5D%5B12%5D)

[](#beta_managed_agents_model%5B0%5D)

string



[](#beta_managed_agents_model%5B1%5D)

[](#beta_managed_agents_model)



BetaManagedAgentsModelConfigParams object { id, effort, speed }



An object that defines additional configuration control over model use



id: [BetaManagedAgentsModel](/docs/en/api/beta/agents#beta_managed_agents_model)



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B1%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B2%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B3%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B4%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B5%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B6%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B7%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B8%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B9%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B10%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B11%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B12%5D)

[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B0%5D)

string



[](#beta_managed_agents_model_config_params.id%20%2B%20(resource)%20beta.agents%5B1%5D)

[](#beta_managed_agents_model_config_params.id)



effort: optional "low" or "medium" or "high" or 2 more or [BetaManagedAgentsEffortLow](/docs/en/api/beta/agents#beta_managed_agents_effort_low) { type } or [BetaManagedAgentsEffortMedium](/docs/en/api/beta/agents#beta_managed_agents_effort_medium) { type } or 3 more



How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

One of the following:



BetaManagedAgentsEffortLevel = "low" or "medium" or "high" or 2 more



How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

One of the following:

"low"



[](#beta_managed_agents_model_config_params.effort%5B0%5D%5B0%5D)

"medium"



[](#beta_managed_agents_model_config_params.effort%5B0%5D%5B1%5D)

"high"



[](#beta_managed_agents_model_config_params.effort%5B0%5D%5B2%5D)

"xhigh"



[](#beta_managed_agents_model_config_params.effort%5B0%5D%5B3%5D)

"max"



[](#beta_managed_agents_model_config_params.effort%5B0%5D%5B4%5D)

[](#beta_managed_agents_model_config_params.effort%5B0%5D)



BetaManagedAgentsEffortLow object { type }



Low effort. Favors latency over reasoning depth.

type: "low"



[](#beta_managed_agents_effort_low.type)

[](#beta_managed_agents_effort_low)



BetaManagedAgentsEffortMedium object { type }



Medium effort. Balances latency and reasoning depth.

type: "medium"



[](#beta_managed_agents_effort_medium.type)

[](#beta_managed_agents_effort_medium)



BetaManagedAgentsEffortHigh object { type }



High effort. Favors reasoning depth.

type: "high"



[](#beta_managed_agents_effort_high.type)

[](#beta_managed_agents_effort_high)



BetaManagedAgentsEffortXhigh object { type }



Extra-high effort. Not all models accept this level.

type: "xhigh"



[](#beta_managed_agents_effort_xhigh.type)

[](#beta_managed_agents_effort_xhigh)



BetaManagedAgentsEffortMax object { type }



Maximum effort. Favors reasoning depth over latency.

type: "max"



[](#beta_managed_agents_effort_max.type)

[](#beta_managed_agents_effort_max)

[](#beta_managed_agents_model_config_params.effort)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_managed_agents_model_config_params.speed%5B0%5D)

"fast"



[](#beta_managed_agents_model_config_params.speed%5B1%5D)

[](#beta_managed_agents_model_config_params.speed)

[](#beta_managed_agents_model_config_params)

[](#beta_managed_agents_agent_with_overrides_params.model)



skills: optional array of [BetaManagedAgentsSkillParams](/docs/en/api/beta/agents#beta_managed_agents_skill_params)



Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

One of the following:



BetaManagedAgentsAnthropicSkillParams object { skill_id, type, version }



An Anthropic-managed skill.

skill_id: string



Identifier of the Anthropic skill (e.g., "xlsx").

[](#beta_managed_agents_anthropic_skill_params.skill_id)

type: "anthropic"



[](#beta_managed_agents_anthropic_skill_params.type)

version: optional string



Version to pin. Defaults to latest if omitted.

[](#beta_managed_agents_anthropic_skill_params.version)

[](#beta_managed_agents_anthropic_skill_params)



BetaManagedAgentsCustomSkillParams object { skill_id, type, version }



A user-created custom skill.

skill_id: string



Tagged ID of the custom skill (e.g., "skill_01XJ5...").

[](#beta_managed_agents_custom_skill_params.skill_id)

type: "custom"



[](#beta_managed_agents_custom_skill_params.type)

version: optional string



Version to pin. Defaults to latest if omitted.

[](#beta_managed_agents_custom_skill_params.version)

[](#beta_managed_agents_custom_skill_params)

[](#beta_managed_agents_agent_with_overrides_params.skills)

system: optional string



Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

[](#beta_managed_agents_agent_with_overrides_params.system)



tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset20260401_params) { type, configs, default_config } or [BetaManagedAgentsMCPToolsetParams](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_params) { mcp_server_name, type, configs, default_config } or [BetaManagedAgentsCustomToolParams](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_params) { description, input_schema, name, type }



Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

One of the following:



BetaManagedAgentsAgentToolset20260401Params object { type, configs, default_config }



Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: "agent_toolset_20260401"



[](#beta_managed_agents_agent_toolset20260401_params.type)



configs: optional array of [BetaManagedAgentsAgentToolConfigParams](/docs/en/api/beta/agents#beta_managed_agents_agent_tool_config_params) { name, enabled, permission_policy }



Per-tool configuration overrides.



name: "bash" or "edit" or "read" or 5 more



Built-in agent tool identifier.

One of the following:

"bash"



[](#beta_managed_agents_agent_tool_config_params.name%5B0%5D)

"edit"



[](#beta_managed_agents_agent_tool_config_params.name%5B1%5D)

"read"



[](#beta_managed_agents_agent_tool_config_params.name%5B2%5D)

"write"



[](#beta_managed_agents_agent_tool_config_params.name%5B3%5D)

"glob"



[](#beta_managed_agents_agent_tool_config_params.name%5B4%5D)

"grep"



[](#beta_managed_agents_agent_tool_config_params.name%5B5%5D)

"web_fetch"



[](#beta_managed_agents_agent_tool_config_params.name%5B6%5D)

"web_search"



[](#beta_managed_agents_agent_tool_config_params.name%5B7%5D)

[](#beta_managed_agents_agent_tool_config_params.name)

enabled: optional boolean



Whether this tool is enabled and available to Claude. Overrides the default_config setting.

[](#beta_managed_agents_agent_tool_config_params.enabled)



permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_always_allow_policy.type)

[](#beta_managed_agents_always_allow_policy)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_always_ask_policy.type)

[](#beta_managed_agents_always_ask_policy)

[](#beta_managed_agents_agent_tool_config_params.permission_policy)

[](#beta_managed_agents_agent_toolset20260401_params.configs)



default_config: optional [BetaManagedAgentsAgentToolsetDefaultConfigParams](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset_default_config_params) { enabled, permission_policy }



Default configuration for all tools in a toolset.

enabled: optional boolean



Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_agent_toolset20260401_params.default_config)

[](#beta_managed_agents_agent_toolset20260401_params)



BetaManagedAgentsMCPToolsetParams object { mcp_server_name, type, configs, default_config }



Configuration for tools from an MCP server defined in `mcp_servers`.

mcp_server_name: string



Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

[](#beta_managed_agents_mcp_toolset_params.mcp_server_name)

type: "mcp_toolset"



[](#beta_managed_agents_mcp_toolset_params.type)



configs: optional array of [BetaManagedAgentsMCPToolConfigParams](/docs/en/api/beta/agents#beta_managed_agents_mcp_tool_config_params) { name, enabled, permission_policy }



Per-tool configuration overrides.

name: string



Name of the MCP tool to configure. 1-128 characters.

[](#beta_managed_agents_mcp_tool_config_params.name)

enabled: optional boolean



Whether this tool is enabled. Overrides the `default_config` setting.

[](#beta_managed_agents_mcp_tool_config_params.enabled)



permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_always_allow_policy.type)

[](#beta_managed_agents_always_allow_policy)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_always_ask_policy.type)

[](#beta_managed_agents_always_ask_policy)

[](#beta_managed_agents_mcp_tool_config_params.permission_policy)

[](#beta_managed_agents_mcp_toolset_params.configs)



default_config: optional [BetaManagedAgentsMCPToolsetDefaultConfigParams](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_default_config_params) { enabled, permission_policy }



Default configuration for all tools from an MCP server.

enabled: optional boolean



Whether tools are enabled by default. Defaults to true if not specified.

[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_mcp_toolset_params.default_config)

[](#beta_managed_agents_mcp_toolset_params)



BetaManagedAgentsCustomToolParams object { description, input_schema, name, type }



A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: string



Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-4096 characters.

[](#beta_managed_agents_custom_tool_params.description)



input_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_input_schema) { type, properties, required }



JSON Schema for custom tool input parameters.

type: "object"



[](#beta_managed_agents_custom_tool_params.input_schema%20%2B%20(resource)%20beta.agents.type)

properties: optional map\[unknown\]



[](#beta_managed_agents_custom_tool_params.input_schema%20%2B%20(resource)%20beta.agents.properties)

required: optional array of string



[](#beta_managed_agents_custom_tool_params.input_schema%20%2B%20(resource)%20beta.agents.required)

[](#beta_managed_agents_custom_tool_params.input_schema)

name: string



Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

[](#beta_managed_agents_custom_tool_params.name)

type: "custom"



[](#beta_managed_agents_custom_tool_params.type)

[](#beta_managed_agents_custom_tool_params)

[](#beta_managed_agents_agent_with_overrides_params.tools)

version: optional number



The specific `agent` version to use. Omit to use the latest version.

[](#beta_managed_agents_agent_with_overrides_params.version)

[](#beta_managed_agents_agent_with_overrides_params)



BetaManagedAgentsBranchCheckout object { name, type }



name: string



Branch name to check out.

[](#beta_managed_agents_branch_checkout.name)

type: "branch"



[](#beta_managed_agents_branch_checkout.type)

[](#beta_managed_agents_branch_checkout)



BetaManagedAgentsCacheCreationUsage object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }



Prompt-cache creation token usage broken down by cache lifetime.

ephemeral_1h_input_tokens: optional number



Tokens used to create 1-hour ephemeral cache entries.

[](#beta_managed_agents_cache_creation_usage.ephemeral_1h_input_tokens)

ephemeral_5m_input_tokens: optional number



Tokens used to create 5-minute ephemeral cache entries.

[](#beta_managed_agents_cache_creation_usage.ephemeral_5m_input_tokens)

[](#beta_managed_agents_cache_creation_usage)



BetaManagedAgentsCommitCheckout object { sha, type }



sha: string



Full commit SHA to check out.

[](#beta_managed_agents_commit_checkout.sha)

type: "commit"



[](#beta_managed_agents_commit_checkout.type)

[](#beta_managed_agents_commit_checkout)



BetaManagedAgentsDeletedSession object { id, type }



Confirmation that a `session` has been permanently deleted.

id: string



[](#beta_managed_agents_deleted_session.id)

type: "session_deleted"



[](#beta_managed_agents_deleted_session.type)

[](#beta_managed_agents_deleted_session)



BetaManagedAgentsDeltaContent object { content, type, index }





content: [BetaManagedAgentsTextBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_text_block) { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_delta_content.content%20%2B%20(resource)%20beta.sessions.events.text)

type: "text"



[](#beta_managed_agents_delta_content.content%20%2B%20(resource)%20beta.sessions.events.type)

[](#beta_managed_agents_delta_content.content)

type: "content_delta"



[](#beta_managed_agents_delta_content.type)

index: optional number



Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

[](#beta_managed_agents_delta_content.index)

[](#beta_managed_agents_delta_content)



BetaManagedAgentsDeltaEvent object { delta, event_id, type }



An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.



delta: [BetaManagedAgentsDeltaContent](/docs/en/api/beta/sessions#beta_managed_agents_delta_content) { content, type, index }



One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.



content: [BetaManagedAgentsTextBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_text_block) { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_delta_content.content%20%2B%20(resource)%20beta.sessions.events.text)

type: "text"



[](#beta_managed_agents_delta_content.content%20%2B%20(resource)%20beta.sessions.events.type)

[](#beta_managed_agents_delta_event.delta%20%2B%20(resource)%20beta.sessions.content)

type: "content_delta"



[](#beta_managed_agents_delta_event.delta%20%2B%20(resource)%20beta.sessions.type)

index: optional number



Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

[](#beta_managed_agents_delta_event.delta%20%2B%20(resource)%20beta.sessions.index)

[](#beta_managed_agents_delta_event.delta)

event_id: string



The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

[](#beta_managed_agents_delta_event.event_id)

type: "event_delta"



[](#beta_managed_agents_delta_event.type)

[](#beta_managed_agents_delta_event)



BetaManagedAgentsDeltaType = "agent.message" or "agent.thinking"



EventDeltaType enum

One of the following:

"agent.message"



[](#beta_managed_agents_delta_type%5B0%5D)

"agent.thinking"



[](#beta_managed_agents_delta_type%5B1%5D)

[](#beta_managed_agents_delta_type)



BetaManagedAgentsFileResourceParams object { file_id, type, mount_path }



Mount a file uploaded via the Files API into the session.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_resource_params.file_id)

type: "file"



[](#beta_managed_agents_file_resource_params.type)

mount_path: optional string



Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

[](#beta_managed_agents_file_resource_params.mount_path)

[](#beta_managed_agents_file_resource_params)



BetaManagedAgentsGitHubRepositoryResourceParams object { authorization_token, type, url, 2 more }



Mount a GitHub repository into the session's container.

authorization_token: string




[](#beta_managed_agents_github_repository_resource_params.authorization_token)

type: "github_repository"



[](#beta_managed_agents_github_repository_resource_params.type)

url: string



Github URL of the repository

[](#beta_managed_agents_github_repository_resource_params.url)



checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta/sessions#beta_managed_agents_branch_checkout) { name, type } or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta/sessions#beta_managed_agents_commit_checkout) { sha, type }



Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



BetaManagedAgentsBranchCheckout object { name, type }



name: string



Branch name to check out.

[](#beta_managed_agents_branch_checkout.name)

type: "branch"



[](#beta_managed_agents_branch_checkout.type)

[](#beta_managed_agents_branch_checkout)



BetaManagedAgentsCommitCheckout object { sha, type }



sha: string



Full commit SHA to check out.

[](#beta_managed_agents_commit_checkout.sha)

type: "commit"



[](#beta_managed_agents_commit_checkout.type)

[](#beta_managed_agents_commit_checkout)

[](#beta_managed_agents_github_repository_resource_params.checkout)

mount_path: optional string



Mount path in the container. Defaults to `/workspace/<repo-name>`.

[](#beta_managed_agents_github_repository_resource_params.mount_path)

[](#beta_managed_agents_github_repository_resource_params)



BetaManagedAgentsMemoryStoreResourceParam object { memory_store_id, type, access, instructions }



Parameters for attaching a memory store to an agent session.

memory_store_id: string



The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

[](#beta_managed_agents_memory_store_resource_param.memory_store_id)

type: "memory_store"



[](#beta_managed_agents_memory_store_resource_param.type)



access: optional "read_write" or "read_only"



Access mode for an attached memory store.

One of the following:

"read_write"



[](#beta_managed_agents_memory_store_resource_param.access%5B0%5D)

"read_only"



[](#beta_managed_agents_memory_store_resource_param.access%5B1%5D)

[](#beta_managed_agents_memory_store_resource_param.access)

instructions: optional string



Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[](#beta_managed_agents_memory_store_resource_param.instructions)

[](#beta_managed_agents_memory_store_resource_param)



BetaManagedAgentsMultiagent object { agents, type }



Resolved coordinator topology with a concrete agent roster.



agents: array of [BetaManagedAgentsAgentReference](/docs/en/api/beta/agents#beta_managed_agents_agent_reference) { id, type, version }



Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: string



[](#beta_managed_agents_agent_reference.id)

type: "agent"



[](#beta_managed_agents_agent_reference.type)

version: number



[](#beta_managed_agents_agent_reference.version)

[](#beta_managed_agents_multiagent.agents)

type: "coordinator"



[](#beta_managed_agents_multiagent.type)

[](#beta_managed_agents_multiagent)



BetaManagedAgentsMultiagentParams object { agents, type }



A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



agents: array of [BetaManagedAgentsMultiagentRosterEntryParams](/docs/en/api/beta/sessions#beta_managed_agents_multiagent_roster_entry_params)



Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

One of the following:

string



[](#beta_managed_agents_multiagent_roster_entry_params%5B0%5D)



BetaManagedAgentsAgentParams object { id, type, version }



Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string



The `agent` ID.

[](#beta_managed_agents_agent_params.id)

type: "agent"



[](#beta_managed_agents_agent_params.type)

version: optional number



The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

[](#beta_managed_agents_agent_params.version)

[](#beta_managed_agents_agent_params)



BetaManagedAgentsMultiagentSelfParams object { type }



Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: "self"



[](#beta_managed_agents_multiagent_self_params.type)

[](#beta_managed_agents_multiagent_self_params)

[](#beta_managed_agents_multiagent_params.agents)

type: "coordinator"



[](#beta_managed_agents_multiagent_params.type)

[](#beta_managed_agents_multiagent_params)



BetaManagedAgentsMultiagentRosterEntryParams = string or [BetaManagedAgentsAgentParams](/docs/en/api/beta/sessions#beta_managed_agents_agent_params) { id, type, version } or [BetaManagedAgentsMultiagentSelfParams](/docs/en/api/beta/agents#beta_managed_agents_multiagent_self_params) { type }



An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

One of the following:

string



[](#beta_managed_agents_multiagent_roster_entry_params%5B0%5D)



BetaManagedAgentsAgentParams object { id, type, version }



Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string



The `agent` ID.

[](#beta_managed_agents_agent_params.id)

type: "agent"



[](#beta_managed_agents_agent_params.type)

version: optional number



The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

[](#beta_managed_agents_agent_params.version)

[](#beta_managed_agents_agent_params)



BetaManagedAgentsMultiagentSelfParams object { type }



Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: "self"



[](#beta_managed_agents_multiagent_self_params.type)

[](#beta_managed_agents_multiagent_self_params)

[](#beta_managed_agents_multiagent_roster_entry_params)



BetaManagedAgentsOutcomeEvaluationResource object { completed_at, description, explanation, 4 more }



Evaluation state for a single outcome defined via a define_outcome event.

completed_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_outcome_evaluation_resource.completed_at)

description: string



What the agent should produce.

[](#beta_managed_agents_outcome_evaluation_resource.description)

explanation: string



Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

[](#beta_managed_agents_outcome_evaluation_resource.explanation)

iteration: number



0-indexed revision cycle the outcome is currently on.

[](#beta_managed_agents_outcome_evaluation_resource.iteration)

outcome_id: string



Server-generated outc\_ ID for this outcome.

[](#beta_managed_agents_outcome_evaluation_resource.outcome_id)

result: string



Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

[](#beta_managed_agents_outcome_evaluation_resource.result)

type: "outcome_evaluation"



[](#beta_managed_agents_outcome_evaluation_resource.type)

[](#beta_managed_agents_outcome_evaluation_resource)



BetaManagedAgentsSession object { id, agent, archived_at, 13 more }



A Managed Agents `session`.

id: string



[](#beta_managed_agents_session.id)



agent: [BetaManagedAgentsSessionAgent](/docs/en/api/beta/sessions#beta_managed_agents_session_agent) { id, description, mcp_servers, 8 more }



Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.id)

description: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.description)



mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta/agents#beta_managed_agents_mcp_server_url_definition) { name, type, url }



name: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name)

type: "url"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.type)

url: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.url)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.mcp_servers)



model: [BetaManagedAgentsModelConfig](/docs/en/api/beta/agents#beta_managed_agents_model_config) { id, effort, speed }



Model identifier and configuration.



id: [BetaManagedAgentsModel](/docs/en/api/beta/agents#beta_managed_agents_model)



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B1%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B2%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B3%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B4%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B5%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B6%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B7%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B8%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B9%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B10%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B11%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B12%5D)

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D)

string



[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B1%5D)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.id)



effort: optional [BetaManagedAgentsEffortLow](/docs/en/api/beta/agents#beta_managed_agents_effort_low) { type } or [BetaManagedAgentsEffortMedium](/docs/en/api/beta/agents#beta_managed_agents_effort_medium) { type } or [BetaManagedAgentsEffortHigh](/docs/en/api/beta/agents#beta_managed_agents_effort_high) { type } or 2 more



How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

One of the following:



BetaManagedAgentsEffortLow object { type }



Low effort. Favors latency over reasoning depth.

type: "low"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMedium object { type }



Medium effort. Balances latency and reasoning depth.

type: "medium"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortHigh object { type }



High effort. Favors reasoning depth.

type: "high"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortXhigh object { type }



Extra-high effort. Not all models accept this level.

type: "xhigh"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMax object { type }



Maximum effort. Favors reasoning depth over latency.

type: "max"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.effort)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.speed%5B0%5D)

"fast"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.speed%5B1%5D)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.speed)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.model)



multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](/docs/en/api/beta/sessions#beta_managed_agents_session_multiagent_coordinator) { agents, type }



Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta/agents#beta_managed_agents_session_thread_agent) { id, description, mcp_servers, 7 more }



Full `agent` definitions the coordinator may spawn as session threads.

id: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.id)

description: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.description)



mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta/agents#beta_managed_agents_mcp_server_url_definition) { name, type, url }



name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)

type: "url"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

url: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.url)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.mcp_servers)



model: [BetaManagedAgentsModelConfig](/docs/en/api/beta/agents#beta_managed_agents_model_config) { id, effort, speed }



Model identifier and configuration.



id: [BetaManagedAgentsModel](/docs/en/api/beta/agents#beta_managed_agents_model)



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B1%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B2%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B3%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B4%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B5%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B6%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B7%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B8%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B9%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B10%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B11%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B12%5D)

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D)

string



[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B1%5D)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.id)



effort: optional [BetaManagedAgentsEffortLow](/docs/en/api/beta/agents#beta_managed_agents_effort_low) { type } or [BetaManagedAgentsEffortMedium](/docs/en/api/beta/agents#beta_managed_agents_effort_medium) { type } or [BetaManagedAgentsEffortHigh](/docs/en/api/beta/agents#beta_managed_agents_effort_high) { type } or 2 more



How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

One of the following:



BetaManagedAgentsEffortLow object { type }



Low effort. Favors latency over reasoning depth.

type: "low"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMedium object { type }



Medium effort. Balances latency and reasoning depth.

type: "medium"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortHigh object { type }



High effort. Favors reasoning depth.

type: "high"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortXhigh object { type }



Extra-high effort. Not all models accept this level.

type: "xhigh"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMax object { type }



Maximum effort. Favors reasoning depth over latency.

type: "max"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.effort)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed%5B0%5D)

"fast"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed%5B1%5D)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.model)

name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)



skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta/agents#beta_managed_agents_anthropic_skill) { skill_id, type, version } or [BetaManagedAgentsCustomSkill](/docs/en/api/beta/agents#beta_managed_agents_custom_skill) { skill_id, type, version }



One of the following:



BetaManagedAgentsAnthropicSkill object { skill_id, type, version }



A resolved Anthropic-managed skill.

skill_id: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.skill_id)

type: "anthropic"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomSkill object { skill_id, type, version }



A resolved user-created custom skill.

skill_id: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.skill_id)

type: "custom"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.skills)

system: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.system)



tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset20260401) { configs, default_config, type } or [BetaManagedAgentsMCPToolset](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type } or [BetaManagedAgentsCustomTool](/docs/en/api/beta/agents#beta_managed_agents_custom_tool) { description, input_schema, name, type }



One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }





configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.enabled)



name: "bash" or "edit" or "read" or 5 more



Built-in agent tool identifier.

One of the following:

"bash"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B0%5D)

"edit"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B1%5D)

"read"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B2%5D)

"write"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B3%5D)

"glob"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B4%5D)

"grep"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B5%5D)

"web_fetch"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B6%5D)

"web_search"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B7%5D)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.configs)



default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for agent tools.

enabled: boolean



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.default_config)

type: "agent_toolset_20260401"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }





configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.enabled)

name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.configs)



default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for all tools from an MCP server.

enabled: boolean



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.default_config)

mcp_server_name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.mcp_server_name)

type: "mcp_toolset"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomTool object { description, input_schema, name, type }



A custom tool as returned in API responses.

description: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.description)



input_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_input_schema) { type, properties, required }



JSON Schema for custom tool input parameters.

type: "object"



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.type)

properties: optional map\[unknown\]



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.properties)

required: optional array of string



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.required)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.input_schema)

name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)

type: "custom"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.tools)

type: "agent"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

version: number



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.sessions.agents)

type: "coordinator"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.sessions.type)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.multiagent)

name: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.name)



skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta/agents#beta_managed_agents_anthropic_skill) { skill_id, type, version } or [BetaManagedAgentsCustomSkill](/docs/en/api/beta/agents#beta_managed_agents_custom_skill) { skill_id, type, version }



One of the following:



BetaManagedAgentsAnthropicSkill object { skill_id, type, version }



A resolved Anthropic-managed skill.

skill_id: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.skill_id)

type: "anthropic"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomSkill object { skill_id, type, version }



A resolved user-created custom skill.

skill_id: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.skill_id)

type: "custom"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.skills)

system: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.system)



tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset20260401) { configs, default_config, type } or [BetaManagedAgentsMCPToolset](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type } or [BetaManagedAgentsCustomTool](/docs/en/api/beta/agents#beta_managed_agents_custom_tool) { description, input_schema, name, type }



One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }





configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.enabled)



name: "bash" or "edit" or "read" or 5 more



Built-in agent tool identifier.

One of the following:

"bash"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name%5B0%5D)

"edit"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name%5B1%5D)

"read"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name%5B2%5D)

"write"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name%5B3%5D)

"glob"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name%5B4%5D)

"grep"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name%5B5%5D)

"web_fetch"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name%5B6%5D)

"web_search"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name%5B7%5D)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.configs)



default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for agent tools.

enabled: boolean



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.default_config)

type: "agent_toolset_20260401"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }





configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.enabled)

name: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.configs)



default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for all tools from an MCP server.

enabled: boolean



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.default_config)

mcp_server_name: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.mcp_server_name)

type: "mcp_toolset"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomTool object { description, input_schema, name, type }



A custom tool as returned in API responses.

description: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.description)



input_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_input_schema) { type, properties, required }



JSON Schema for custom tool input parameters.

type: "object"



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.type)

properties: optional map\[unknown\]



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.properties)

required: optional array of string



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.required)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.input_schema)

name: string



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.name)

type: "custom"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.tools)

type: "agent"



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.type)

version: number



[](#beta_managed_agents_session.agent%20%2B%20(resource)%20beta.sessions.version)

[](#beta_managed_agents_session.agent)

archived_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_session.archived_at)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_session.created_at)

environment_id: string



[](#beta_managed_agents_session.environment_id)

metadata: map\[string\]



[](#beta_managed_agents_session.metadata)



outcome_evaluations: array of [BetaManagedAgentsOutcomeEvaluationResource](/docs/en/api/beta/sessions#beta_managed_agents_outcome_evaluation_resource) { completed_at, description, explanation, 4 more }



Per-outcome evaluation state. One entry per define_outcome event sent to the session.

completed_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_outcome_evaluation_resource.completed_at)

description: string



What the agent should produce.

[](#beta_managed_agents_outcome_evaluation_resource.description)

explanation: string



Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

[](#beta_managed_agents_outcome_evaluation_resource.explanation)

iteration: number



0-indexed revision cycle the outcome is currently on.

[](#beta_managed_agents_outcome_evaluation_resource.iteration)

outcome_id: string



Server-generated outc\_ ID for this outcome.

[](#beta_managed_agents_outcome_evaluation_resource.outcome_id)

result: string



Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

[](#beta_managed_agents_outcome_evaluation_resource.result)

type: "outcome_evaluation"



[](#beta_managed_agents_outcome_evaluation_resource.type)

[](#beta_managed_agents_session.outcome_evaluations)



resources: array of [BetaManagedAgentsSessionResource](/docs/en/api/beta/sessions/resources#beta_managed_agents_session_resource)



One of the following:



BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }



id: string



[](#beta_managed_agents_github_repository_resource.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_github_repository_resource.created_at)

mount_path: string



[](#beta_managed_agents_github_repository_resource.mount_path)

type: "github_repository"



[](#beta_managed_agents_github_repository_resource.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_github_repository_resource.updated_at)

url: string



[](#beta_managed_agents_github_repository_resource.url)



checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta/sessions#beta_managed_agents_branch_checkout) { name, type } or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta/sessions#beta_managed_agents_commit_checkout) { sha, type }



One of the following:



BetaManagedAgentsBranchCheckout object { name, type }



name: string



Branch name to check out.

[](#beta_managed_agents_branch_checkout.name)

type: "branch"



[](#beta_managed_agents_branch_checkout.type)

[](#beta_managed_agents_branch_checkout)



BetaManagedAgentsCommitCheckout object { sha, type }



sha: string



Full commit SHA to check out.

[](#beta_managed_agents_commit_checkout.sha)

type: "commit"



[](#beta_managed_agents_commit_checkout.type)

[](#beta_managed_agents_commit_checkout)

[](#beta_managed_agents_github_repository_resource.checkout)

[](#beta_managed_agents_github_repository_resource)



BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }



id: string



[](#beta_managed_agents_file_resource.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_file_resource.created_at)

file_id: string



[](#beta_managed_agents_file_resource.file_id)

mount_path: string



[](#beta_managed_agents_file_resource.mount_path)

type: "file"



[](#beta_managed_agents_file_resource.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_file_resource.updated_at)

[](#beta_managed_agents_file_resource)



BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }



A memory store attached to an agent session.

memory_store_id: string



The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

[](#beta_managed_agents_memory_store_resource.memory_store_id)

type: "memory_store"



[](#beta_managed_agents_memory_store_resource.type)



access: optional "read_write" or "read_only"



Access mode for an attached memory store.

One of the following:

"read_write"



[](#beta_managed_agents_memory_store_resource.access%5B0%5D)

"read_only"



[](#beta_managed_agents_memory_store_resource.access%5B1%5D)

[](#beta_managed_agents_memory_store_resource.access)

description: optional string



Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

[](#beta_managed_agents_memory_store_resource.description)

instructions: optional string



Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[](#beta_managed_agents_memory_store_resource.instructions)

mount_path: optional string



Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

[](#beta_managed_agents_memory_store_resource.mount_path)

name: optional string



Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

[](#beta_managed_agents_memory_store_resource.name)

[](#beta_managed_agents_memory_store_resource)

[](#beta_managed_agents_session.resources)



stats: [BetaManagedAgentsSessionStats](/docs/en/api/beta/sessions#beta_managed_agents_session_stats) { active_seconds, duration_seconds }



Timing statistics for a session.

active_seconds: optional number



Cumulative time in seconds the session spent in running status. Excludes idle time.

[](#beta_managed_agents_session.stats%20%2B%20(resource)%20beta.sessions.active_seconds)

duration_seconds: optional number



Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

[](#beta_managed_agents_session.stats%20%2B%20(resource)%20beta.sessions.duration_seconds)

[](#beta_managed_agents_session.stats)



status: "rescheduling" or "running" or "idle" or "terminated"



SessionStatus enum

One of the following:

"rescheduling"



[](#beta_managed_agents_session.status%5B0%5D)

"running"



[](#beta_managed_agents_session.status%5B1%5D)

"idle"



[](#beta_managed_agents_session.status%5B2%5D)

"terminated"



[](#beta_managed_agents_session.status%5B3%5D)

[](#beta_managed_agents_session.status)

title: string



[](#beta_managed_agents_session.title)

type: "session"



[](#beta_managed_agents_session.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_session.updated_at)



usage: [BetaManagedAgentsSessionUsage](/docs/en/api/beta/sessions#beta_managed_agents_session_usage) { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }



Cumulative token usage for a session across all turns.



cache_creation: optional [BetaManagedAgentsCacheCreationUsage](/docs/en/api/beta/sessions#beta_managed_agents_cache_creation_usage) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }



Prompt-cache creation token usage broken down by cache lifetime.

ephemeral_1h_input_tokens: optional number



Tokens used to create 1-hour ephemeral cache entries.

[](#beta_managed_agents_session_usage.cache_creation%20%2B%20(resource)%20beta.sessions.ephemeral_1h_input_tokens)

ephemeral_5m_input_tokens: optional number



Tokens used to create 5-minute ephemeral cache entries.

[](#beta_managed_agents_session_usage.cache_creation%20%2B%20(resource)%20beta.sessions.ephemeral_5m_input_tokens)

[](#beta_managed_agents_session.usage%20%2B%20(resource)%20beta.sessions.cache_creation)

cache_read_input_tokens: optional number



Total tokens read from prompt cache.

[](#beta_managed_agents_session.usage%20%2B%20(resource)%20beta.sessions.cache_read_input_tokens)

input_tokens: optional number



Total input tokens consumed across all turns.

[](#beta_managed_agents_session.usage%20%2B%20(resource)%20beta.sessions.input_tokens)

output_tokens: optional number



Total output tokens generated across all turns.

[](#beta_managed_agents_session.usage%20%2B%20(resource)%20beta.sessions.output_tokens)

[](#beta_managed_agents_session.usage)

vault_ids: array of string



Vault IDs attached to the session at creation. Empty when no vaults were supplied.

[](#beta_managed_agents_session.vault_ids)

deployment_id: optional string



Deployment ID when the session was created from a deployment reference. Null otherwise.

[](#beta_managed_agents_session.deployment_id)

[](#beta_managed_agents_session)



BetaManagedAgentsSessionAgent object { id, description, mcp_servers, 8 more }



Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string



[](#beta_managed_agents_session_agent.id)

description: string



[](#beta_managed_agents_session_agent.description)



mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta/agents#beta_managed_agents_mcp_server_url_definition) { name, type, url }



name: string



[](#beta_managed_agents_mcp_server_url_definition.name)

type: "url"



[](#beta_managed_agents_mcp_server_url_definition.type)

url: string



[](#beta_managed_agents_mcp_server_url_definition.url)

[](#beta_managed_agents_session_agent.mcp_servers)



model: [BetaManagedAgentsModelConfig](/docs/en/api/beta/agents#beta_managed_agents_model_config) { id, effort, speed }



Model identifier and configuration.



id: [BetaManagedAgentsModel](/docs/en/api/beta/agents#beta_managed_agents_model)



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B1%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B2%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B3%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B4%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B5%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B6%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B7%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B8%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B9%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B10%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B11%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B12%5D)

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D)

string



[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B1%5D)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.id)



effort: optional [BetaManagedAgentsEffortLow](/docs/en/api/beta/agents#beta_managed_agents_effort_low) { type } or [BetaManagedAgentsEffortMedium](/docs/en/api/beta/agents#beta_managed_agents_effort_medium) { type } or [BetaManagedAgentsEffortHigh](/docs/en/api/beta/agents#beta_managed_agents_effort_high) { type } or 2 more



How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

One of the following:



BetaManagedAgentsEffortLow object { type }



Low effort. Favors latency over reasoning depth.

type: "low"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMedium object { type }



Medium effort. Balances latency and reasoning depth.

type: "medium"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortHigh object { type }



High effort. Favors reasoning depth.

type: "high"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortXhigh object { type }



Extra-high effort. Not all models accept this level.

type: "xhigh"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMax object { type }



Maximum effort. Favors reasoning depth over latency.

type: "max"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.effort)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.speed%5B0%5D)

"fast"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.speed%5B1%5D)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.speed)

[](#beta_managed_agents_session_agent.model)



multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](/docs/en/api/beta/sessions#beta_managed_agents_session_multiagent_coordinator) { agents, type }



Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta/agents#beta_managed_agents_session_thread_agent) { id, description, mcp_servers, 7 more }



Full `agent` definitions the coordinator may spawn as session threads.

id: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.id)

description: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.description)



mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta/agents#beta_managed_agents_mcp_server_url_definition) { name, type, url }



name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)

type: "url"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

url: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.url)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.mcp_servers)



model: [BetaManagedAgentsModelConfig](/docs/en/api/beta/agents#beta_managed_agents_model_config) { id, effort, speed }



Model identifier and configuration.



id: [BetaManagedAgentsModel](/docs/en/api/beta/agents#beta_managed_agents_model)



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B1%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B2%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B3%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B4%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B5%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B6%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B7%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B8%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B9%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B10%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B11%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B12%5D)

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D)

string



[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B1%5D)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.id)



effort: optional [BetaManagedAgentsEffortLow](/docs/en/api/beta/agents#beta_managed_agents_effort_low) { type } or [BetaManagedAgentsEffortMedium](/docs/en/api/beta/agents#beta_managed_agents_effort_medium) { type } or [BetaManagedAgentsEffortHigh](/docs/en/api/beta/agents#beta_managed_agents_effort_high) { type } or 2 more



How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

One of the following:



BetaManagedAgentsEffortLow object { type }



Low effort. Favors latency over reasoning depth.

type: "low"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMedium object { type }



Medium effort. Balances latency and reasoning depth.

type: "medium"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortHigh object { type }



High effort. Favors reasoning depth.

type: "high"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortXhigh object { type }



Extra-high effort. Not all models accept this level.

type: "xhigh"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMax object { type }



Maximum effort. Favors reasoning depth over latency.

type: "max"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.effort)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed%5B0%5D)

"fast"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed%5B1%5D)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.model)

name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)



skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta/agents#beta_managed_agents_anthropic_skill) { skill_id, type, version } or [BetaManagedAgentsCustomSkill](/docs/en/api/beta/agents#beta_managed_agents_custom_skill) { skill_id, type, version }



One of the following:



BetaManagedAgentsAnthropicSkill object { skill_id, type, version }



A resolved Anthropic-managed skill.

skill_id: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.skill_id)

type: "anthropic"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomSkill object { skill_id, type, version }



A resolved user-created custom skill.

skill_id: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.skill_id)

type: "custom"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.skills)

system: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.system)



tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset20260401) { configs, default_config, type } or [BetaManagedAgentsMCPToolset](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type } or [BetaManagedAgentsCustomTool](/docs/en/api/beta/agents#beta_managed_agents_custom_tool) { description, input_schema, name, type }



One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }





configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.enabled)



name: "bash" or "edit" or "read" or 5 more



Built-in agent tool identifier.

One of the following:

"bash"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B0%5D)

"edit"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B1%5D)

"read"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B2%5D)

"write"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B3%5D)

"glob"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B4%5D)

"grep"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B5%5D)

"web_fetch"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B6%5D)

"web_search"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B7%5D)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.configs)



default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for agent tools.

enabled: boolean



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.default_config)

type: "agent_toolset_20260401"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }





configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.enabled)

name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.configs)



default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for all tools from an MCP server.

enabled: boolean



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.default_config)

mcp_server_name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.mcp_server_name)

type: "mcp_toolset"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomTool object { description, input_schema, name, type }



A custom tool as returned in API responses.

description: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.description)



input_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_input_schema) { type, properties, required }



JSON Schema for custom tool input parameters.

type: "object"



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.type)

properties: optional map\[unknown\]



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.properties)

required: optional array of string



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.required)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.input_schema)

name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)

type: "custom"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.tools)

type: "agent"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

version: number



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.sessions.agents)

type: "coordinator"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.sessions.type)

[](#beta_managed_agents_session_agent.multiagent)

name: string



[](#beta_managed_agents_session_agent.name)



skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta/agents#beta_managed_agents_anthropic_skill) { skill_id, type, version } or [BetaManagedAgentsCustomSkill](/docs/en/api/beta/agents#beta_managed_agents_custom_skill) { skill_id, type, version }



One of the following:



BetaManagedAgentsAnthropicSkill object { skill_id, type, version }



A resolved Anthropic-managed skill.

skill_id: string



[](#beta_managed_agents_anthropic_skill.skill_id)

type: "anthropic"



[](#beta_managed_agents_anthropic_skill.type)

version: string



[](#beta_managed_agents_anthropic_skill.version)

[](#beta_managed_agents_anthropic_skill)



BetaManagedAgentsCustomSkill object { skill_id, type, version }



A resolved user-created custom skill.

skill_id: string



[](#beta_managed_agents_custom_skill.skill_id)

type: "custom"



[](#beta_managed_agents_custom_skill.type)

version: string



[](#beta_managed_agents_custom_skill.version)

[](#beta_managed_agents_custom_skill)

[](#beta_managed_agents_session_agent.skills)

system: string



[](#beta_managed_agents_session_agent.system)



tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset20260401) { configs, default_config, type } or [BetaManagedAgentsMCPToolset](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type } or [BetaManagedAgentsCustomTool](/docs/en/api/beta/agents#beta_managed_agents_custom_tool) { description, input_schema, name, type }



One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }





configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_agent_tool_config.enabled)



name: "bash" or "edit" or "read" or 5 more



Built-in agent tool identifier.

One of the following:

"bash"



[](#beta_managed_agents_agent_tool_config.name%5B0%5D)

"edit"



[](#beta_managed_agents_agent_tool_config.name%5B1%5D)

"read"



[](#beta_managed_agents_agent_tool_config.name%5B2%5D)

"write"



[](#beta_managed_agents_agent_tool_config.name%5B3%5D)

"glob"



[](#beta_managed_agents_agent_tool_config.name%5B4%5D)

"grep"



[](#beta_managed_agents_agent_tool_config.name%5B5%5D)

"web_fetch"



[](#beta_managed_agents_agent_tool_config.name%5B6%5D)

"web_search"



[](#beta_managed_agents_agent_tool_config.name%5B7%5D)

[](#beta_managed_agents_agent_tool_config.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_always_allow_policy.type)

[](#beta_managed_agents_always_allow_policy)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_always_ask_policy.type)

[](#beta_managed_agents_always_ask_policy)

[](#beta_managed_agents_agent_tool_config.permission_policy)

[](#beta_managed_agents_agent_toolset20260401.configs)



default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for agent tools.

enabled: boolean



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_agent_toolset20260401.default_config)

type: "agent_toolset_20260401"



[](#beta_managed_agents_agent_toolset20260401.type)

[](#beta_managed_agents_agent_toolset20260401)



BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }





configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_mcp_tool_config.enabled)

name: string



[](#beta_managed_agents_mcp_tool_config.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_always_allow_policy.type)

[](#beta_managed_agents_always_allow_policy)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_always_ask_policy.type)

[](#beta_managed_agents_always_ask_policy)

[](#beta_managed_agents_mcp_tool_config.permission_policy)

[](#beta_managed_agents_mcp_toolset.configs)



default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for all tools from an MCP server.

enabled: boolean



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_mcp_toolset.default_config)

mcp_server_name: string



[](#beta_managed_agents_mcp_toolset.mcp_server_name)

type: "mcp_toolset"



[](#beta_managed_agents_mcp_toolset.type)

[](#beta_managed_agents_mcp_toolset)



BetaManagedAgentsCustomTool object { description, input_schema, name, type }



A custom tool as returned in API responses.

description: string



[](#beta_managed_agents_custom_tool.description)



input_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_input_schema) { type, properties, required }



JSON Schema for custom tool input parameters.

type: "object"



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.type)

properties: optional map\[unknown\]



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.properties)

required: optional array of string



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.required)

[](#beta_managed_agents_custom_tool.input_schema)

name: string



[](#beta_managed_agents_custom_tool.name)

type: "custom"



[](#beta_managed_agents_custom_tool.type)

[](#beta_managed_agents_custom_tool)

[](#beta_managed_agents_session_agent.tools)

type: "agent"



[](#beta_managed_agents_session_agent.type)

version: number



[](#beta_managed_agents_session_agent.version)

[](#beta_managed_agents_session_agent)



BetaManagedAgentsSessionAgentUpdate object { mcp_servers, tools }



Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.



mcp_servers: optional array of [BetaManagedAgentsURLMCPServerParams](/docs/en/api/beta/agents#beta_managed_agents_url_mcp_server_params) { name, type, url }



Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

name: string



Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

[](#beta_managed_agents_url_mcp_server_params.name)

type: "url"



[](#beta_managed_agents_url_mcp_server_params.type)

url: string



Endpoint URL for the MCP server.

[](#beta_managed_agents_url_mcp_server_params.url)

[](#beta_managed_agents_session_agent_update.mcp_servers)



tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset20260401_params) { type, configs, default_config } or [BetaManagedAgentsMCPToolsetParams](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_params) { mcp_server_name, type, configs, default_config } or [BetaManagedAgentsCustomToolParams](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_params) { description, input_schema, name, type }



Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

One of the following:



BetaManagedAgentsAgentToolset20260401Params object { type, configs, default_config }



Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: "agent_toolset_20260401"



[](#beta_managed_agents_agent_toolset20260401_params.type)



configs: optional array of [BetaManagedAgentsAgentToolConfigParams](/docs/en/api/beta/agents#beta_managed_agents_agent_tool_config_params) { name, enabled, permission_policy }



Per-tool configuration overrides.



name: "bash" or "edit" or "read" or 5 more



Built-in agent tool identifier.

One of the following:

"bash"



[](#beta_managed_agents_agent_tool_config_params.name%5B0%5D)

"edit"



[](#beta_managed_agents_agent_tool_config_params.name%5B1%5D)

"read"



[](#beta_managed_agents_agent_tool_config_params.name%5B2%5D)

"write"



[](#beta_managed_agents_agent_tool_config_params.name%5B3%5D)

"glob"



[](#beta_managed_agents_agent_tool_config_params.name%5B4%5D)

"grep"



[](#beta_managed_agents_agent_tool_config_params.name%5B5%5D)

"web_fetch"



[](#beta_managed_agents_agent_tool_config_params.name%5B6%5D)

"web_search"



[](#beta_managed_agents_agent_tool_config_params.name%5B7%5D)

[](#beta_managed_agents_agent_tool_config_params.name)

enabled: optional boolean



Whether this tool is enabled and available to Claude. Overrides the default_config setting.

[](#beta_managed_agents_agent_tool_config_params.enabled)



permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_always_allow_policy.type)

[](#beta_managed_agents_always_allow_policy)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_always_ask_policy.type)

[](#beta_managed_agents_always_ask_policy)

[](#beta_managed_agents_agent_tool_config_params.permission_policy)

[](#beta_managed_agents_agent_toolset20260401_params.configs)



default_config: optional [BetaManagedAgentsAgentToolsetDefaultConfigParams](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset_default_config_params) { enabled, permission_policy }



Default configuration for all tools in a toolset.

enabled: optional boolean



Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_agent_toolset20260401_params.default_config)

[](#beta_managed_agents_agent_toolset20260401_params)



BetaManagedAgentsMCPToolsetParams object { mcp_server_name, type, configs, default_config }



Configuration for tools from an MCP server defined in `mcp_servers`.

mcp_server_name: string



Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

[](#beta_managed_agents_mcp_toolset_params.mcp_server_name)

type: "mcp_toolset"



[](#beta_managed_agents_mcp_toolset_params.type)



configs: optional array of [BetaManagedAgentsMCPToolConfigParams](/docs/en/api/beta/agents#beta_managed_agents_mcp_tool_config_params) { name, enabled, permission_policy }



Per-tool configuration overrides.

name: string



Name of the MCP tool to configure. 1-128 characters.

[](#beta_managed_agents_mcp_tool_config_params.name)

enabled: optional boolean



Whether this tool is enabled. Overrides the `default_config` setting.

[](#beta_managed_agents_mcp_tool_config_params.enabled)



permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_always_allow_policy.type)

[](#beta_managed_agents_always_allow_policy)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_always_ask_policy.type)

[](#beta_managed_agents_always_ask_policy)

[](#beta_managed_agents_mcp_tool_config_params.permission_policy)

[](#beta_managed_agents_mcp_toolset_params.configs)



default_config: optional [BetaManagedAgentsMCPToolsetDefaultConfigParams](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_default_config_params) { enabled, permission_policy }



Default configuration for all tools from an MCP server.

enabled: optional boolean



Whether tools are enabled by default. Defaults to true if not specified.

[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_mcp_toolset_params.default_config)

[](#beta_managed_agents_mcp_toolset_params)



BetaManagedAgentsCustomToolParams object { description, input_schema, name, type }



A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: string



Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-4096 characters.

[](#beta_managed_agents_custom_tool_params.description)



input_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_input_schema) { type, properties, required }



JSON Schema for custom tool input parameters.

type: "object"



[](#beta_managed_agents_custom_tool_params.input_schema%20%2B%20(resource)%20beta.agents.type)

properties: optional map\[unknown\]



[](#beta_managed_agents_custom_tool_params.input_schema%20%2B%20(resource)%20beta.agents.properties)

required: optional array of string



[](#beta_managed_agents_custom_tool_params.input_schema%20%2B%20(resource)%20beta.agents.required)

[](#beta_managed_agents_custom_tool_params.input_schema)

name: string



Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

[](#beta_managed_agents_custom_tool_params.name)

type: "custom"



[](#beta_managed_agents_custom_tool_params.type)

[](#beta_managed_agents_custom_tool_params)

[](#beta_managed_agents_session_agent_update.tools)

[](#beta_managed_agents_session_agent_update)



BetaManagedAgentsSessionMultiagentCoordinator object { agents, type }



Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta/agents#beta_managed_agents_session_thread_agent) { id, description, mcp_servers, 7 more }



Full `agent` definitions the coordinator may spawn as session threads.

id: string



[](#beta_managed_agents_session_thread_agent.id)

description: string



[](#beta_managed_agents_session_thread_agent.description)



mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta/agents#beta_managed_agents_mcp_server_url_definition) { name, type, url }



name: string



[](#beta_managed_agents_mcp_server_url_definition.name)

type: "url"



[](#beta_managed_agents_mcp_server_url_definition.type)

url: string



[](#beta_managed_agents_mcp_server_url_definition.url)

[](#beta_managed_agents_session_thread_agent.mcp_servers)



model: [BetaManagedAgentsModelConfig](/docs/en/api/beta/agents#beta_managed_agents_model_config) { id, effort, speed }



Model identifier and configuration.



id: [BetaManagedAgentsModel](/docs/en/api/beta/agents#beta_managed_agents_model)



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B1%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B2%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B3%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B4%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B5%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B6%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B7%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B8%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B9%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B10%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B11%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B12%5D)

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D)

string



[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B1%5D)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.id)



effort: optional [BetaManagedAgentsEffortLow](/docs/en/api/beta/agents#beta_managed_agents_effort_low) { type } or [BetaManagedAgentsEffortMedium](/docs/en/api/beta/agents#beta_managed_agents_effort_medium) { type } or [BetaManagedAgentsEffortHigh](/docs/en/api/beta/agents#beta_managed_agents_effort_high) { type } or 2 more



How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

One of the following:



BetaManagedAgentsEffortLow object { type }



Low effort. Favors latency over reasoning depth.

type: "low"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMedium object { type }



Medium effort. Balances latency and reasoning depth.

type: "medium"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortHigh object { type }



High effort. Favors reasoning depth.

type: "high"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortXhigh object { type }



Extra-high effort. Not all models accept this level.

type: "xhigh"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMax object { type }



Maximum effort. Favors reasoning depth over latency.

type: "max"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.effort)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed%5B0%5D)

"fast"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed%5B1%5D)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed)

[](#beta_managed_agents_session_thread_agent.model)

name: string



[](#beta_managed_agents_session_thread_agent.name)



skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta/agents#beta_managed_agents_anthropic_skill) { skill_id, type, version } or [BetaManagedAgentsCustomSkill](/docs/en/api/beta/agents#beta_managed_agents_custom_skill) { skill_id, type, version }



One of the following:



BetaManagedAgentsAnthropicSkill object { skill_id, type, version }



A resolved Anthropic-managed skill.

skill_id: string



[](#beta_managed_agents_anthropic_skill.skill_id)

type: "anthropic"



[](#beta_managed_agents_anthropic_skill.type)

version: string



[](#beta_managed_agents_anthropic_skill.version)

[](#beta_managed_agents_anthropic_skill)



BetaManagedAgentsCustomSkill object { skill_id, type, version }



A resolved user-created custom skill.

skill_id: string



[](#beta_managed_agents_custom_skill.skill_id)

type: "custom"



[](#beta_managed_agents_custom_skill.type)

version: string



[](#beta_managed_agents_custom_skill.version)

[](#beta_managed_agents_custom_skill)

[](#beta_managed_agents_session_thread_agent.skills)

system: string



[](#beta_managed_agents_session_thread_agent.system)



tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset20260401) { configs, default_config, type } or [BetaManagedAgentsMCPToolset](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type } or [BetaManagedAgentsCustomTool](/docs/en/api/beta/agents#beta_managed_agents_custom_tool) { description, input_schema, name, type }



One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }





configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_agent_tool_config.enabled)



name: "bash" or "edit" or "read" or 5 more



Built-in agent tool identifier.

One of the following:

"bash"



[](#beta_managed_agents_agent_tool_config.name%5B0%5D)

"edit"



[](#beta_managed_agents_agent_tool_config.name%5B1%5D)

"read"



[](#beta_managed_agents_agent_tool_config.name%5B2%5D)

"write"



[](#beta_managed_agents_agent_tool_config.name%5B3%5D)

"glob"



[](#beta_managed_agents_agent_tool_config.name%5B4%5D)

"grep"



[](#beta_managed_agents_agent_tool_config.name%5B5%5D)

"web_fetch"



[](#beta_managed_agents_agent_tool_config.name%5B6%5D)

"web_search"



[](#beta_managed_agents_agent_tool_config.name%5B7%5D)

[](#beta_managed_agents_agent_tool_config.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_always_allow_policy.type)

[](#beta_managed_agents_always_allow_policy)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_always_ask_policy.type)

[](#beta_managed_agents_always_ask_policy)

[](#beta_managed_agents_agent_tool_config.permission_policy)

[](#beta_managed_agents_agent_toolset20260401.configs)



default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for agent tools.

enabled: boolean



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_agent_toolset20260401.default_config)

type: "agent_toolset_20260401"



[](#beta_managed_agents_agent_toolset20260401.type)

[](#beta_managed_agents_agent_toolset20260401)



BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }





configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_mcp_tool_config.enabled)

name: string



[](#beta_managed_agents_mcp_tool_config.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_always_allow_policy.type)

[](#beta_managed_agents_always_allow_policy)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_always_ask_policy.type)

[](#beta_managed_agents_always_ask_policy)

[](#beta_managed_agents_mcp_tool_config.permission_policy)

[](#beta_managed_agents_mcp_toolset.configs)



default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for all tools from an MCP server.

enabled: boolean



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_mcp_toolset.default_config)

mcp_server_name: string



[](#beta_managed_agents_mcp_toolset.mcp_server_name)

type: "mcp_toolset"



[](#beta_managed_agents_mcp_toolset.type)

[](#beta_managed_agents_mcp_toolset)



BetaManagedAgentsCustomTool object { description, input_schema, name, type }



A custom tool as returned in API responses.

description: string



[](#beta_managed_agents_custom_tool.description)



input_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_input_schema) { type, properties, required }



JSON Schema for custom tool input parameters.

type: "object"



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.type)

properties: optional map\[unknown\]



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.properties)

required: optional array of string



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.required)

[](#beta_managed_agents_custom_tool.input_schema)

name: string



[](#beta_managed_agents_custom_tool.name)

type: "custom"



[](#beta_managed_agents_custom_tool.type)

[](#beta_managed_agents_custom_tool)

[](#beta_managed_agents_session_thread_agent.tools)

type: "agent"



[](#beta_managed_agents_session_thread_agent.type)

version: number



[](#beta_managed_agents_session_thread_agent.version)

[](#beta_managed_agents_session_multiagent_coordinator.agents)

type: "coordinator"



[](#beta_managed_agents_session_multiagent_coordinator.type)

[](#beta_managed_agents_session_multiagent_coordinator)



BetaManagedAgentsSessionStats object { active_seconds, duration_seconds }



Timing statistics for a session.

active_seconds: optional number



Cumulative time in seconds the session spent in running status. Excludes idle time.

[](#beta_managed_agents_session_stats.active_seconds)

duration_seconds: optional number



Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

[](#beta_managed_agents_session_stats.duration_seconds)

[](#beta_managed_agents_session_stats)



BetaManagedAgentsSessionUpdatedEvent object { id, processed_at, type, 3 more }



Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: string



Unique identifier for this event.

[](#beta_managed_agents_session_updated_event.id)

processed_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_session_updated_event.processed_at)

type: "session.updated"



[](#beta_managed_agents_session_updated_event.type)



agent: optional [BetaManagedAgentsSessionAgent](/docs/en/api/beta/sessions#beta_managed_agents_session_agent) { id, description, mcp_servers, 8 more }



Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.id)

description: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.description)



mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta/agents#beta_managed_agents_mcp_server_url_definition) { name, type, url }



name: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name)

type: "url"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.type)

url: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.url)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.mcp_servers)



model: [BetaManagedAgentsModelConfig](/docs/en/api/beta/agents#beta_managed_agents_model_config) { id, effort, speed }



Model identifier and configuration.



id: [BetaManagedAgentsModel](/docs/en/api/beta/agents#beta_managed_agents_model)



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B1%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B2%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B3%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B4%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B5%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B6%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B7%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B8%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B9%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B10%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B11%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B12%5D)

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D)

string



[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B1%5D)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.id)



effort: optional [BetaManagedAgentsEffortLow](/docs/en/api/beta/agents#beta_managed_agents_effort_low) { type } or [BetaManagedAgentsEffortMedium](/docs/en/api/beta/agents#beta_managed_agents_effort_medium) { type } or [BetaManagedAgentsEffortHigh](/docs/en/api/beta/agents#beta_managed_agents_effort_high) { type } or 2 more



How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

One of the following:



BetaManagedAgentsEffortLow object { type }



Low effort. Favors latency over reasoning depth.

type: "low"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMedium object { type }



Medium effort. Balances latency and reasoning depth.

type: "medium"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortHigh object { type }



High effort. Favors reasoning depth.

type: "high"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortXhigh object { type }



Extra-high effort. Not all models accept this level.

type: "xhigh"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMax object { type }



Maximum effort. Favors reasoning depth over latency.

type: "max"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.effort)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.speed%5B0%5D)

"fast"



[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.speed%5B1%5D)

[](#beta_managed_agents_session_agent.model%20%2B%20(resource)%20beta.agents.speed)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.model)



multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](/docs/en/api/beta/sessions#beta_managed_agents_session_multiagent_coordinator) { agents, type }



Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta/agents#beta_managed_agents_session_thread_agent) { id, description, mcp_servers, 7 more }



Full `agent` definitions the coordinator may spawn as session threads.

id: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.id)

description: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.description)



mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta/agents#beta_managed_agents_mcp_server_url_definition) { name, type, url }



name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)

type: "url"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

url: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.url)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.mcp_servers)



model: [BetaManagedAgentsModelConfig](/docs/en/api/beta/agents#beta_managed_agents_model_config) { id, effort, speed }



Model identifier and configuration.



id: [BetaManagedAgentsModel](/docs/en/api/beta/agents#beta_managed_agents_model)



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B1%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B2%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B3%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B4%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B5%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B6%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B7%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B8%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B9%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B10%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B11%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D%5B12%5D)

[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B0%5D)

string



[](#beta_managed_agents_model_config.id%20%2B%20(resource)%20beta.agents%5B1%5D)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.id)



effort: optional [BetaManagedAgentsEffortLow](/docs/en/api/beta/agents#beta_managed_agents_effort_low) { type } or [BetaManagedAgentsEffortMedium](/docs/en/api/beta/agents#beta_managed_agents_effort_medium) { type } or [BetaManagedAgentsEffortHigh](/docs/en/api/beta/agents#beta_managed_agents_effort_high) { type } or 2 more



How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

One of the following:



BetaManagedAgentsEffortLow object { type }



Low effort. Favors latency over reasoning depth.

type: "low"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMedium object { type }



Medium effort. Balances latency and reasoning depth.

type: "medium"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortHigh object { type }



High effort. Favors reasoning depth.

type: "high"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortXhigh object { type }



Extra-high effort. Not all models accept this level.

type: "xhigh"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMax object { type }



Maximum effort. Favors reasoning depth over latency.

type: "max"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.effort)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed%5B0%5D)

"fast"



[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed%5B1%5D)

[](#beta_managed_agents_session_thread_agent.model%20%2B%20(resource)%20beta.agents.speed)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.model)

name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)



skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta/agents#beta_managed_agents_anthropic_skill) { skill_id, type, version } or [BetaManagedAgentsCustomSkill](/docs/en/api/beta/agents#beta_managed_agents_custom_skill) { skill_id, type, version }



One of the following:



BetaManagedAgentsAnthropicSkill object { skill_id, type, version }



A resolved Anthropic-managed skill.

skill_id: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.skill_id)

type: "anthropic"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomSkill object { skill_id, type, version }



A resolved user-created custom skill.

skill_id: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.skill_id)

type: "custom"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.skills)

system: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.system)



tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset20260401) { configs, default_config, type } or [BetaManagedAgentsMCPToolset](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type } or [BetaManagedAgentsCustomTool](/docs/en/api/beta/agents#beta_managed_agents_custom_tool) { description, input_schema, name, type }



One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }





configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.enabled)



name: "bash" or "edit" or "read" or 5 more



Built-in agent tool identifier.

One of the following:

"bash"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B0%5D)

"edit"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B1%5D)

"read"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B2%5D)

"write"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B3%5D)

"glob"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B4%5D)

"grep"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B5%5D)

"web_fetch"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B6%5D)

"web_search"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name%5B7%5D)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.configs)



default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for agent tools.

enabled: boolean



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.default_config)

type: "agent_toolset_20260401"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }





configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.enabled)

name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.configs)



default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for all tools from an MCP server.

enabled: boolean



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.default_config)

mcp_server_name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.mcp_server_name)

type: "mcp_toolset"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomTool object { description, input_schema, name, type }



A custom tool as returned in API responses.

description: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.description)



input_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_input_schema) { type, properties, required }



JSON Schema for custom tool input parameters.

type: "object"



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.type)

properties: optional map\[unknown\]



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.properties)

required: optional array of string



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.required)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.input_schema)

name: string



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.name)

type: "custom"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.tools)

type: "agent"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

version: number



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.sessions.agents)

type: "coordinator"



[](#beta_managed_agents_session_agent.multiagent%20%2B%20(resource)%20beta.sessions.type)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.multiagent)

name: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.name)



skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta/agents#beta_managed_agents_anthropic_skill) { skill_id, type, version } or [BetaManagedAgentsCustomSkill](/docs/en/api/beta/agents#beta_managed_agents_custom_skill) { skill_id, type, version }



One of the following:



BetaManagedAgentsAnthropicSkill object { skill_id, type, version }



A resolved Anthropic-managed skill.

skill_id: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.skill_id)

type: "anthropic"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomSkill object { skill_id, type, version }



A resolved user-created custom skill.

skill_id: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.skill_id)

type: "custom"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.skills)

system: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.system)



tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset20260401) { configs, default_config, type } or [BetaManagedAgentsMCPToolset](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type } or [BetaManagedAgentsCustomTool](/docs/en/api/beta/agents#beta_managed_agents_custom_tool) { description, input_schema, name, type }



One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }





configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.enabled)



name: "bash" or "edit" or "read" or 5 more



Built-in agent tool identifier.

One of the following:

"bash"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name%5B0%5D)

"edit"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name%5B1%5D)

"read"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name%5B2%5D)

"write"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name%5B3%5D)

"glob"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name%5B4%5D)

"grep"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name%5B5%5D)

"web_fetch"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name%5B6%5D)

"web_search"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name%5B7%5D)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.configs)



default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for agent tools.

enabled: boolean



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.default_config)

type: "agent_toolset_20260401"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }





configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.enabled)

name: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.configs)



default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy }



Resolved default configuration for all tools from an MCP server.

enabled: boolean



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.enabled)



permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_allow_policy) { type } or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta/agents#beta_managed_agents_always_ask_policy) { type }



Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type }



Tool calls are automatically approved without user confirmation.

type: "always_allow"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_mcp_toolset.default_config%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.default_config)

mcp_server_name: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.mcp_server_name)

type: "mcp_toolset"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomTool object { description, input_schema, name, type }



A custom tool as returned in API responses.

description: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.description)



input_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta/agents#beta_managed_agents_custom_tool_input_schema) { type, properties, required }



JSON Schema for custom tool input parameters.

type: "object"



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.type)

properties: optional map\[unknown\]



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.properties)

required: optional array of string



[](#beta_managed_agents_custom_tool.input_schema%20%2B%20(resource)%20beta.agents.required)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.input_schema)

name: string



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.name)

type: "custom"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.tools)

type: "agent"



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.type)

version: number



[](#beta_managed_agents_session_updated_event.agent%20%2B%20(resource)%20beta.sessions.version)

[](#beta_managed_agents_session_updated_event.agent)

metadata: optional map\[string\]



The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

[](#beta_managed_agents_session_updated_event.metadata)

title: optional string



The session's new title. Present only when the update changed it.

[](#beta_managed_agents_session_updated_event.title)

[](#beta_managed_agents_session_updated_event)



BetaManagedAgentsSessionUsage object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }



Cumulative token usage for a session across all turns.



cache_creation: optional [BetaManagedAgentsCacheCreationUsage](/docs/en/api/beta/sessions#beta_managed_agents_cache_creation_usage) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }



Prompt-cache creation token usage broken down by cache lifetime.

ephemeral_1h_input_tokens: optional number



Tokens used to create 1-hour ephemeral cache entries.

[](#beta_managed_agents_session_usage.cache_creation%20%2B%20(resource)%20beta.sessions.ephemeral_1h_input_tokens)

ephemeral_5m_input_tokens: optional number



Tokens used to create 5-minute ephemeral cache entries.

[](#beta_managed_agents_session_usage.cache_creation%20%2B%20(resource)%20beta.sessions.ephemeral_5m_input_tokens)

[](#beta_managed_agents_session_usage.cache_creation)

cache_read_input_tokens: optional number



Total tokens read from prompt cache.

[](#beta_managed_agents_session_usage.cache_read_input_tokens)

input_tokens: optional number



Total input tokens consumed across all turns.

[](#beta_managed_agents_session_usage.input_tokens)

output_tokens: optional number



Total output tokens generated across all turns.

[](#beta_managed_agents_session_usage.output_tokens)

[](#beta_managed_agents_session_usage)



BetaManagedAgentsStartEvent object { event, type }



Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.



event: [BetaManagedAgentsStartEventPreview](/docs/en/api/beta/sessions#beta_managed_agents_start_event_preview)



The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

One of the following:



BetaManagedAgentsAgentMessagePreview object { id, type }



id: string



The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

[](#beta_managed_agents_start_event.event%20%2B%20(resource)%20beta.sessions.id)

type: "agent.message"



[](#beta_managed_agents_start_event.event%20%2B%20(resource)%20beta.sessions.type)

[](#beta_managed_agents_start_event.event%20%2B%20(resource)%20beta.sessions)



BetaManagedAgentsAgentThinkingPreview object { id, type }



id: string



The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

[](#beta_managed_agents_start_event.event%20%2B%20(resource)%20beta.sessions.id)

type: "agent.thinking"



[](#beta_managed_agents_start_event.event%20%2B%20(resource)%20beta.sessions.type)

[](#beta_managed_agents_start_event.event%20%2B%20(resource)%20beta.sessions)

[](#beta_managed_agents_start_event.event)

type: "event_start"



[](#beta_managed_agents_start_event.type)

[](#beta_managed_agents_start_event)



BetaManagedAgentsStartEventPreview = [BetaManagedAgentsAgentMessagePreview](/docs/en/api/beta/sessions#beta_managed_agents_agent_message_preview) { id, type } or [BetaManagedAgentsAgentThinkingPreview](/docs/en/api/beta/sessions#beta_managed_agents_agent_thinking_preview) { id, type }



One of the following:



BetaManagedAgentsAgentMessagePreview object { id, type }



id: string



The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

[](#beta_managed_agents_agent_message_preview.id)

type: "agent.message"



[](#beta_managed_agents_agent_message_preview.type)

[](#beta_managed_agents_agent_message_preview)



BetaManagedAgentsAgentThinkingPreview object { id, type }



id: string



The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

[](#beta_managed_agents_agent_thinking_preview.id)

type: "agent.thinking"



[](#beta_managed_agents_agent_thinking_preview.type)

[](#beta_managed_agents_agent_thinking_preview)

[](#beta_managed_agents_start_event_preview)



BetaManagedAgentsSystemContentBlock object { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_system_content_block.text)

type: "text"



[](#beta_managed_agents_system_content_block.type)

[](#beta_managed_agents_system_content_block)



BetaManagedAgentsSystemMessageEvent object { id, content, type, processed_at }



A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: string



Unique identifier for this event.

[](#beta_managed_agents_system_message_event.id)



content: array of [BetaManagedAgentsSystemContentBlock](/docs/en/api/beta/sessions#beta_managed_agents_system_content_block) { text, type }



System content blocks. Text-only.

text: string



The text content.

[](#beta_managed_agents_system_content_block.text)

type: "text"



[](#beta_managed_agents_system_content_block.type)

[](#beta_managed_agents_system_message_event.content)

type: "system.message"



[](#beta_managed_agents_system_message_event.type)

processed_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_system_message_event.processed_at)

[](#beta_managed_agents_system_message_event)



BetaManagedAgentsUserToolResultEvent object { id, tool_use_id, type, 4 more }



Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string



Unique identifier for this event.

[](#beta_managed_agents_user_tool_result_event.id)

tool_use_id: string



The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

[](#beta_managed_agents_user_tool_result_event.tool_use_id)

type: "user.tool_result"



[](#beta_managed_agents_user_tool_result_event.type)



content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_text_block) { text, type } or [BetaManagedAgentsImageBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_image_block) { source, type } or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_document_block) { source, type, context, title } or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_block) { citations, content, source, 2 more }



The result content returned by the tool.

One of the following:



BetaManagedAgentsTextBlock object { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_text_block.text)

type: "text"



[](#beta_managed_agents_text_block.type)

[](#beta_managed_agents_text_block)



BetaManagedAgentsImageBlock object { source, type }



Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_image_source) { data, media_type, type } or [BetaManagedAgentsURLImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_image_source) { type, url } or [BetaManagedAgentsFileImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_image_source) { file_id, type }



Union type for image source variants.

One of the following:



BetaManagedAgentsBase64ImageSource object { data, media_type, type }



Base64-encoded image data.

data: string



Base64-encoded image data.

[](#beta_managed_agents_base64_image_source.data)

media_type: string



MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

[](#beta_managed_agents_base64_image_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_image_source.type)

[](#beta_managed_agents_base64_image_source)



BetaManagedAgentsURLImageSource object { type, url }



Image referenced by URL.

type: "url"



[](#beta_managed_agents_url_image_source.type)

url: string



URL of the image to fetch.

[](#beta_managed_agents_url_image_source.url)

[](#beta_managed_agents_url_image_source)



BetaManagedAgentsFileImageSource object { file_id, type }



Image referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_image_source.file_id)

type: "file"



[](#beta_managed_agents_file_image_source.type)

[](#beta_managed_agents_file_image_source)

[](#beta_managed_agents_image_block.source)

type: "image"



[](#beta_managed_agents_image_block.type)

[](#beta_managed_agents_image_block)



BetaManagedAgentsDocumentBlock object { source, type, context, title }



Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_document_source) { data, media_type, type } or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_plain_text_document_source) { data, media_type, type } or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_document_source) { type, url } or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_document_source) { file_id, type }



Union type for document source variants.

One of the following:



BetaManagedAgentsBase64DocumentSource object { data, media_type, type }



Base64-encoded document data.

data: string



Base64-encoded document data.

[](#beta_managed_agents_base64_document_source.data)

media_type: string



MIME type of the document (e.g., "application/pdf").

[](#beta_managed_agents_base64_document_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_document_source.type)

[](#beta_managed_agents_base64_document_source)



BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }



Plain text document content.

data: string



The plain text content.

[](#beta_managed_agents_plain_text_document_source.data)

media_type: "text/plain"



MIME type of the text content. Must be "text/plain".

[](#beta_managed_agents_plain_text_document_source.media_type)

type: "text"



[](#beta_managed_agents_plain_text_document_source.type)

[](#beta_managed_agents_plain_text_document_source)



BetaManagedAgentsURLDocumentSource object { type, url }



Document referenced by URL.

type: "url"



[](#beta_managed_agents_url_document_source.type)

url: string



URL of the document to fetch.

[](#beta_managed_agents_url_document_source.url)

[](#beta_managed_agents_url_document_source)



BetaManagedAgentsFileDocumentSource object { file_id, type }



Document referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_document_source.file_id)

type: "file"



[](#beta_managed_agents_file_document_source.type)

[](#beta_managed_agents_file_document_source)

[](#beta_managed_agents_document_block.source)

type: "document"



[](#beta_managed_agents_document_block.type)

context: optional string



Additional context about the document for the model.

[](#beta_managed_agents_document_block.context)

title: optional string



The title of the document.

[](#beta_managed_agents_document_block.title)

[](#beta_managed_agents_document_block)



BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }



A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_citations) { enabled }



Citation settings for a search result.

enabled: boolean



Whether citations are enabled for this search result.

[](#beta_managed_agents_search_result_block.citations%20%2B%20(resource)%20beta.sessions.events.enabled)

[](#beta_managed_agents_search_result_block.citations)



content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_content) { text, type }



Array of text content blocks from the search result.

text: string



The text content.

[](#beta_managed_agents_search_result_content.text)

type: "text"



[](#beta_managed_agents_search_result_content.type)

[](#beta_managed_agents_search_result_block.content)

source: string



The URL source of the search result.

[](#beta_managed_agents_search_result_block.source)

title: string



The title of the search result.

[](#beta_managed_agents_search_result_block.title)

type: "search_result"



[](#beta_managed_agents_search_result_block.type)

[](#beta_managed_agents_search_result_block)

[](#beta_managed_agents_user_tool_result_event.content)

is_error: optional boolean



Whether the tool execution resulted in an error.

[](#beta_managed_agents_user_tool_result_event.is_error)

processed_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_user_tool_result_event.processed_at)

session_thread_id: optional string



Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

[](#beta_managed_agents_user_tool_result_event.session_thread_id)

[](#beta_managed_agents_user_tool_result_event)

#### SessionsEvents

##### [List Events](/docs/en/api/beta/sessions/events/list)

GET/v1/sessions/{session_id}/events

##### [Send Events](/docs/en/api/beta/sessions/events/send)

POST/v1/sessions/{session_id}/events

##### [Stream Events](/docs/en/api/beta/sessions/events/stream)

GET/v1/sessions/{session_id}/events/stream

#### SessionsResources

##### [Add Session Resource](/docs/en/api/beta/sessions/resources/add)

POST/v1/sessions/{session_id}/resources

##### [List Session Resources](/docs/en/api/beta/sessions/resources/list)

GET/v1/sessions/{session_id}/resources

##### [Get Session Resource](/docs/en/api/beta/sessions/resources/retrieve)

GET/v1/sessions/{session_id}/resources/{resource_id}

##### [Update Session Resource](/docs/en/api/beta/sessions/resources/update)

POST/v1/sessions/{session_id}/resources/{resource_id}

##### [Delete Session Resource](/docs/en/api/beta/sessions/resources/delete)

DELETE/v1/sessions/{session_id}/resources/{resource_id}

#### SessionsThreads

##### [List Session Threads](/docs/en/api/beta/sessions/threads/list)

GET/v1/sessions/{session_id}/threads

##### [Get Session Thread](/docs/en/api/beta/sessions/threads/retrieve)

GET/v1/sessions/{session_id}/threads/{thread_id}

##### [Archive Session Thread](/docs/en/api/beta/sessions/threads/archive)

POST/v1/sessions/{session_id}/threads/{thread_id}/archive

#### SessionsThreadsEvents

##### [List Session Thread Events](/docs/en/api/beta/sessions/threads/events/list)

GET/v1/sessions/{session_id}/threads/{thread_id}/events

##### [Stream Session Thread Events](/docs/en/api/beta/sessions/threads/events/stream)

GET/v1/sessions/{session_id}/threads/{thread_id}/stream
