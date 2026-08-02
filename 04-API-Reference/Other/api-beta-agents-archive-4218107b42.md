---
title: "Archive Agent - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/agents/archive"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:24Z"
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

Archive




cURL

# Archive Agent

POST/v1/agents/{agent_id}/archive

Archive Agent

##### Path ParametersExpand Collapse 

agent_id: string



[](#archive.agent_id)

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

[](#archive.betas)

##### ReturnsExpand Collapse 

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

Archive Agent

cURL



```python
curl https://api.anthropic.com/v1/agents/$AGENT_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "effort": {
      "type": "low"
    },
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      }
    ],
    "type": "coordinator"
  },
  "name": "My First Agent",
  "skills": [
    {
      "skill_id": "xlsx",
      "type": "anthropic",
      "version": "1"
    },
    {
      "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
      "type": "custom",
      "version": "2"
    }
  ],
  "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
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
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

##### Returns Examples

Response 200



```python
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "effort": {
      "type": "low"
    },
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      }
    ],
    "type": "coordinator"
  },
  "name": "My First Agent",
  "skills": [
    {
      "skill_id": "xlsx",
      "type": "anthropic",
      "version": "1"
    },
    {
      "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
      "type": "custom",
      "version": "2"
    }
  ],
  "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
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
  "updated_at": "2026-03-15T10:00:00Z",
