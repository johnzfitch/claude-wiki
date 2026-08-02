---
title: "Agents - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/agents"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:21Z"
tags: ["agents", "api"]
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


Create Agent


List Agents


Get Agent


Update Agent


Archive Agent

Versions

Environments

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

Agents




cURL

# Agents

##### [Create Agent](/docs/en/api/beta/agents/create)

POST/v1/agents

##### [List Agents](/docs/en/api/beta/agents/list)

GET/v1/agents

##### [Get Agent](/docs/en/api/beta/agents/retrieve)

GET/v1/agents/{agent_id}

##### [Update Agent](/docs/en/api/beta/agents/update)

POST/v1/agents/{agent_id}

##### [Archive Agent](/docs/en/api/beta/agents/archive)

POST/v1/agents/{agent_id}/archive

##### ModelsExpand Collapse 



BetaManagedAgentsAgent object { id, archived_at, created_at, 12 more }



A Managed Agents `agent`.

id: string



[](#beta_managed_agents_agent.id)

archived_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_agent.archived_at)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_agent.created_at)

description: string



[](#beta_managed_agents_agent.description)

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

[](#beta_managed_agents_agent.mcp_servers)

metadata: map\[string\]



[](#beta_managed_agents_agent.metadata)

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

[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents.id)

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

[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMedium object { type }



Medium effort. Balances latency and reasoning depth.

type: "medium"



[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortHigh object { type }



High effort. Favors reasoning depth.

type: "high"



[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortXhigh object { type }



Extra-high effort. Not all models accept this level.

type: "xhigh"



[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsEffortMax object { type }



Maximum effort. Favors reasoning depth over latency.

type: "max"



[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents.effort)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents.speed%5B0%5D)

"fast"



[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents.speed%5B1%5D)

[](#beta_managed_agents_agent.model%20%2B%20(resource)%20beta.agents.speed)

[](#beta_managed_agents_agent.model)



multiagent: [BetaManagedAgentsMultiagent](/docs/en/api/beta/sessions#beta_managed_agents_multiagent) { agents, type }



Resolved coordinator topology with a concrete agent roster.



agents: array of [BetaManagedAgentsAgentReference](/docs/en/api/beta/agents#beta_managed_agents_agent_reference) { id, type, version }



Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: string



[](#beta_managed_agents_agent.multiagent%20%2B%20(resource)%20beta.agents.id)

type: "agent"



[](#beta_managed_agents_agent.multiagent%20%2B%20(resource)%20beta.agents.type)

version: number



[](#beta_managed_agents_agent.multiagent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_agent.multiagent%20%2B%20(resource)%20beta.sessions.agents)

type: "coordinator"



[](#beta_managed_agents_agent.multiagent%20%2B%20(resource)%20beta.sessions.type)

[](#beta_managed_agents_agent.multiagent)

name: string



[](#beta_managed_agents_agent.name)

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

[](#beta_managed_agents_agent.skills)

system: string



[](#beta_managed_agents_agent.system)

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

[](#beta_managed_agents_agent.tools)

type: "agent"



[](#beta_managed_agents_agent.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_agent.updated_at)

version: number



The agent's current version. Starts at 1 and increments when the agent is modified.

[](#beta_managed_agents_agent.version)

[](#beta_managed_agents_agent)



BetaManagedAgentsAgentReference object { id, type, version }



A resolved agent reference with a concrete version.

id: string



[](#beta_managed_agents_agent_reference.id)

type: "agent"



[](#beta_managed_agents_agent_reference.type)

version: number



[](#beta_managed_agents_agent_reference.version)

[](#beta_managed_agents_agent_reference)



BetaManagedAgentsAgentToolConfig object { enabled, name, permission_policy }



Configuration for a specific agent tool.

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

[](#beta_managed_agents_agent_tool_config)



BetaManagedAgentsAgentToolConfigParams object { name, enabled, permission_policy }



Configuration override for a specific tool within a toolset.

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

[](#beta_managed_agents_agent_tool_config_params)



BetaManagedAgentsAgentToolsetDefaultConfig object { enabled, permission_policy }



Resolved default configuration for agent tools.

enabled: boolean



[](#beta_managed_agents_agent_toolset_default_config.enabled)

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

[](#beta_managed_agents_agent_toolset_default_config.permission_policy)

[](#beta_managed_agents_agent_toolset_default_config)



BetaManagedAgentsAgentToolsetDefaultConfigParams object { enabled, permission_policy }



Default configuration for all tools in a toolset.

enabled: optional boolean



Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

[](#beta_managed_agents_agent_toolset_default_config_params.enabled)

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

[](#beta_managed_agents_agent_toolset_default_config_params.permission_policy)

[](#beta_managed_agents_agent_toolset_default_config_params)

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

BetaManagedAgentsAgentToolset20260401BashInput object { command, restart, timeout_ms }



Input payload for the `bash` tool of the `agent_toolset_20260401` toolset. All fields are optional; a normal invocation supplies `command`, while `restart=true` (with no `command`) reboots the runner-side bash session.

command: optional string



Shell command to execute. Omit only when `restart` is true.

[](#beta_managed_agents_agent_toolset20260401_bash_input.command)

restart: optional boolean



When true, restart the persistent bash session instead of running a command. Subsequent calls without `restart` will run against the fresh session.

[](#beta_managed_agents_agent_toolset20260401_bash_input.restart)

timeout_ms: optional number



Per-call timeout in milliseconds. Defaults to the runner-wide tool timeout when omitted or zero.

[](#beta_managed_agents_agent_toolset20260401_bash_input.timeout_ms)

[](#beta_managed_agents_agent_toolset20260401_bash_input)



BetaManagedAgentsAgentToolset20260401EditInput object { file_path, new_string, old_string, replace_all }



Input payload for the `edit` tool. Performs a string replacement in the named file; by default `old_string` must occur exactly once.

file_path: string



Path of the file to edit.

[](#beta_managed_agents_agent_toolset20260401_edit_input.file_path)

new_string: string



Replacement text.

[](#beta_managed_agents_agent_toolset20260401_edit_input.new_string)

old_string: string



Substring to find and replace.

[](#beta_managed_agents_agent_toolset20260401_edit_input.old_string)

replace_all: optional boolean



When true, replace every occurrence of `old_string` instead of requiring a unique match.

[](#beta_managed_agents_agent_toolset20260401_edit_input.replace_all)

[](#beta_managed_agents_agent_toolset20260401_edit_input)



BetaManagedAgentsAgentToolset20260401GlobInput object { pattern, path }



Input payload for the `glob` tool. Returns paths matching a doublestar glob pattern, newest first.

pattern: string



Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns are only permitted when the runner is configured to allow them.

[](#beta_managed_agents_agent_toolset20260401_glob_input.pattern)

path: optional string



Optional directory root to search under. Defaults to the runner's working directory.

[](#beta_managed_agents_agent_toolset20260401_glob_input.path)

[](#beta_managed_agents_agent_toolset20260401_glob_input)



BetaManagedAgentsAgentToolset20260401GrepInput object { pattern, path }



Input payload for the `grep` tool. Searches file contents for a regular expression, returning matching lines.

pattern: string



Regular expression to search for.

[](#beta_managed_agents_agent_toolset20260401_grep_input.pattern)

path: optional string



Optional directory root to search under. Defaults to the runner's working directory.

[](#beta_managed_agents_agent_toolset20260401_grep_input.path)

[](#beta_managed_agents_agent_toolset20260401_grep_input)

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

BetaManagedAgentsAgentToolset20260401ReadInput object { file_path, view_range }



Input payload for the `read` tool. Reads file contents relative to the runner's working directory (or absolute when the runner permits).

file_path: string



Path of the file to read.

[](#beta_managed_agents_agent_toolset20260401_read_input.file_path)

view_range: optional array of number



Optional `[start_line, end_line]` 1-indexed inclusive range. When omitted the entire file is returned. `end_line` of 0 or negative means "to end of file".

[](#beta_managed_agents_agent_toolset20260401_read_input.view_range)

[](#beta_managed_agents_agent_toolset20260401_read_input)



BetaManagedAgentsAgentToolset20260401WriteInput object { content, file_path }



Input payload for the `write` tool. Writes (overwriting) the entire file contents.

content: string



Full file contents to write.

[](#beta_managed_agents_agent_toolset20260401_write_input.content)

file_path: string



Path of the file to write.

[](#beta_managed_agents_agent_toolset20260401_write_input.file_path)

[](#beta_managed_agents_agent_toolset20260401_write_input)

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



BetaManagedAgentsCustomToolInputSchema object { type, properties, required }



JSON Schema for custom tool input parameters.

type: "object"



[](#beta_managed_agents_custom_tool_input_schema.type)

properties: optional map\[unknown\]



[](#beta_managed_agents_custom_tool_input_schema.properties)

required: optional array of string



[](#beta_managed_agents_custom_tool_input_schema.required)

[](#beta_managed_agents_custom_tool_input_schema)

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



BetaManagedAgentsEffortHigh object { type }



High effort. Favors reasoning depth.

type: "high"



[](#beta_managed_agents_effort_high.type)

[](#beta_managed_agents_effort_high)



BetaManagedAgentsEffortLow object { type }



Low effort. Favors latency over reasoning depth.

type: "low"



[](#beta_managed_agents_effort_low.type)

[](#beta_managed_agents_effort_low)



BetaManagedAgentsEffortMax object { type }



Maximum effort. Favors reasoning depth over latency.

type: "max"



[](#beta_managed_agents_effort_max.type)

[](#beta_managed_agents_effort_max)



BetaManagedAgentsEffortMedium object { type }



Medium effort. Balances latency and reasoning depth.

type: "medium"



[](#beta_managed_agents_effort_medium.type)

[](#beta_managed_agents_effort_medium)



BetaManagedAgentsEffortXhigh object { type }



Extra-high effort. Not all models accept this level.

type: "xhigh"



[](#beta_managed_agents_effort_xhigh.type)

[](#beta_managed_agents_effort_xhigh)



BetaManagedAgentsMCPServerURLDefinition object { name, type, url }



URL-based MCP server connection as returned in API responses.

name: string



[](#beta_managed_agents_mcp_server_url_definition.name)

type: "url"



[](#beta_managed_agents_mcp_server_url_definition.type)

url: string



[](#beta_managed_agents_mcp_server_url_definition.url)

[](#beta_managed_agents_mcp_server_url_definition)



BetaManagedAgentsMCPToolConfig object { enabled, name, permission_policy }



Resolved configuration for a specific MCP tool.

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

[](#beta_managed_agents_mcp_tool_config)



BetaManagedAgentsMCPToolConfigParams object { name, enabled, permission_policy }



Configuration override for a specific MCP tool.

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

[](#beta_managed_agents_mcp_tool_config_params)

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

BetaManagedAgentsMCPToolsetDefaultConfig object { enabled, permission_policy }



Resolved default configuration for all tools from an MCP server.

enabled: boolean



[](#beta_managed_agents_mcp_toolset_default_config.enabled)

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

[](#beta_managed_agents_mcp_toolset_default_config.permission_policy)

[](#beta_managed_agents_mcp_toolset_default_config)



BetaManagedAgentsMCPToolsetDefaultConfigParams object { enabled, permission_policy }



Default configuration for all tools from an MCP server.

enabled: optional boolean



Whether tools are enabled by default. Defaults to true if not specified.

[](#beta_managed_agents_mcp_toolset_default_config_params.enabled)

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

[](#beta_managed_agents_mcp_toolset_default_config_params.permission_policy)

[](#beta_managed_agents_mcp_toolset_default_config_params)

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

BetaManagedAgentsModelConfig object { id, effort, speed }

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

[](#beta_managed_agents_model_config.id)

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

[](#beta_managed_agents_model_config.effort)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_managed_agents_model_config.speed%5B0%5D)

"fast"



[](#beta_managed_agents_model_config.speed%5B1%5D)

[](#beta_managed_agents_model_config.speed)

[](#beta_managed_agents_model_config)

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



BetaManagedAgentsMultiagentCoordinator object { agents, type }

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

[](#beta_managed_agents_multiagent_coordinator.agents)

type: "coordinator"



[](#beta_managed_agents_multiagent_coordinator.type)

[](#beta_managed_agents_multiagent_coordinator)



BetaManagedAgentsMultiagentCoordinatorParams object { agents, type }

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

[](#beta_managed_agents_multiagent_coordinator_params.agents)

type: "coordinator"



[](#beta_managed_agents_multiagent_coordinator_params.type)

[](#beta_managed_agents_multiagent_coordinator_params)



BetaManagedAgentsMultiagentSelfParams object { type }



Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: "self"



[](#beta_managed_agents_multiagent_self_params.type)

[](#beta_managed_agents_multiagent_self_params)



BetaManagedAgentsSessionThreadAgent object { id, description, mcp_servers, 7 more }



Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

[](#beta_managed_agents_session_thread_agent)



BetaManagedAgentsSkillParams = [BetaManagedAgentsAnthropicSkillParams](/docs/en/api/beta/agents#beta_managed_agents_anthropic_skill_params) { skill_id, type, version } or [BetaManagedAgentsCustomSkillParams](/docs/en/api/beta/agents#beta_managed_agents_custom_skill_params) { skill_id, type, version }



Skill to load in the session container.

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

[](#beta_managed_agents_skill_params)



BetaManagedAgentsURLMCPServerParams object { name, type, url }



URL-based MCP server connection.

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

[](#beta_managed_agents_url_mcp_server_params)

#### AgentsVersions

##### [List Agent Versions](/docs/en/api/beta/agents/versions/list)

GET/v1/agents/{agent_id}/versions
