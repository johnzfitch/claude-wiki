---
title: "Get Session Thread - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve"
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


List Session Threads


Get Session Thread


Archive Session Thread

Events

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

# Get Session Thread

GET/v1/sessions/{session_id}/threads/{thread_id}

Get Session Thread

##### Path ParametersExpand Collapse 

session_id: string



[](#retrieve.session_id)

thread_id: string



[](#retrieve.thread_id)

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

BetaManagedAgentsSessionThread object { id, agent, archived_at, 8 more }



An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

id: string



Unique identifier for this thread.

[](#beta_managed_agents_session_thread.id)



agent: [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta/agents#beta_managed_agents_session_thread_agent) { id, description, mcp_servers, 7 more }



Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

id: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.id)

description: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.description)



mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta/agents#beta_managed_agents_mcp_server_url_definition) { name, type, url }



name: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name)

type: "url"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

url: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.url)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.mcp_servers)

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

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.model)

name: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name)

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

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.skill_id)

type: "anthropic"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomSkill object { skill_id, type, version }



A resolved user-created custom skill.

skill_id: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.skill_id)

type: "custom"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

version: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.skills)

system: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.system)

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

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.enabled)



name: "bash" or "edit" or "read" or 5 more



Built-in agent tool identifier.

One of the following:

"bash"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name%5B0%5D)

"edit"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name%5B1%5D)

"read"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name%5B2%5D)

"write"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name%5B3%5D)

"glob"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name%5B4%5D)

"grep"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name%5B5%5D)

"web_fetch"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name%5B6%5D)

"web_search"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name%5B7%5D)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name)

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

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.configs)

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

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.default_config)

type: "agent_toolset_20260401"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }





configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta/agents#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy }



enabled: boolean



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.enabled)

name: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name)

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

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsAlwaysAskPolicy object { type }



Tool calls require user confirmation before execution.

type: "always_ask"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.permission_policy)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.configs)

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

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.default_config)

mcp_server_name: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.mcp_server_name)

type: "mcp_toolset"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents)



BetaManagedAgentsCustomTool object { description, input_schema, name, type }



A custom tool as returned in API responses.

description: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.description)

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

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.input_schema)

name: string



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.name)

type: "custom"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents)

[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.tools)

type: "agent"



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.type)

version: number



[](#beta_managed_agents_session_thread.agent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_session_thread.agent)

archived_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_session_thread.archived_at)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_session_thread.created_at)

parent_thread_id: string



Parent thread that spawned this thread. Null for the primary thread.

[](#beta_managed_agents_session_thread.parent_thread_id)

session_id: string



The session this thread belongs to.

[](#beta_managed_agents_session_thread.session_id)



stats: [BetaManagedAgentsSessionThreadStats](/docs/en/api/beta/sessions/threads#beta_managed_agents_session_thread_stats) { active_seconds, duration_seconds, startup_seconds }



Timing statistics for a session thread.

active_seconds: optional number



Cumulative time in seconds the thread spent actively running. Excludes idle time.

[](#beta_managed_agents_session_thread.stats%20%2B%20(resource)%20beta.sessions.threads.active_seconds)

duration_seconds: optional number



Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

[](#beta_managed_agents_session_thread.stats%20%2B%20(resource)%20beta.sessions.threads.duration_seconds)

startup_seconds: optional number



Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

[](#beta_managed_agents_session_thread.stats%20%2B%20(resource)%20beta.sessions.threads.startup_seconds)

[](#beta_managed_agents_session_thread.stats)



status: [BetaManagedAgentsSessionThreadStatus](/docs/en/api/beta/sessions/threads#beta_managed_agents_session_thread_status)



SessionThreadStatus enum

One of the following:

"running"



[](#beta_managed_agents_session_thread.status%20%2B%20(resource)%20beta.sessions.threads%5B0%5D)

"idle"



[](#beta_managed_agents_session_thread.status%20%2B%20(resource)%20beta.sessions.threads%5B1%5D)

"rescheduling"



[](#beta_managed_agents_session_thread.status%20%2B%20(resource)%20beta.sessions.threads%5B2%5D)

"terminated"



[](#beta_managed_agents_session_thread.status%20%2B%20(resource)%20beta.sessions.threads%5B3%5D)

[](#beta_managed_agents_session_thread.status)

type: "session_thread"



[](#beta_managed_agents_session_thread.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_session_thread.updated_at)



usage: [BetaManagedAgentsSessionThreadUsage](/docs/en/api/beta/sessions/threads#beta_managed_agents_session_thread_usage) { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }



Cumulative token usage for a session thread across all turns.



cache_creation: optional [BetaManagedAgentsCacheCreationUsage](/docs/en/api/beta/sessions#beta_managed_agents_cache_creation_usage) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }



Prompt-cache creation token usage broken down by cache lifetime.

ephemeral_1h_input_tokens: optional number



Tokens used to create 1-hour ephemeral cache entries.

[](#beta_managed_agents_session_thread_usage.cache_creation%20%2B%20(resource)%20beta.sessions.ephemeral_1h_input_tokens)

ephemeral_5m_input_tokens: optional number



Tokens used to create 5-minute ephemeral cache entries.

[](#beta_managed_agents_session_thread_usage.cache_creation%20%2B%20(resource)%20beta.sessions.ephemeral_5m_input_tokens)

[](#beta_managed_agents_session_thread.usage%20%2B%20(resource)%20beta.sessions.threads.cache_creation)

cache_read_input_tokens: optional number



Total tokens read from prompt cache.

[](#beta_managed_agents_session_thread.usage%20%2B%20(resource)%20beta.sessions.threads.cache_read_input_tokens)

input_tokens: optional number



Total input tokens consumed across all turns.

[](#beta_managed_agents_session_thread.usage%20%2B%20(resource)%20beta.sessions.threads.input_tokens)

output_tokens: optional number



Total output tokens generated across all turns.

[](#beta_managed_agents_session_thread.usage%20%2B%20(resource)%20beta.sessions.threads.output_tokens)

[](#beta_managed_agents_session_thread.usage)

[](#beta_managed_agents_session_thread)

Get Session Thread

cURL



```python
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "effort": {
        "type": "low"
      },
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

##### Returns Examples

Response 200



```python
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "effort": {
        "type": "low"
      },
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
