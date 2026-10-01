---
title: "Create Agent - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/agents/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:32Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fagents%2Fcreate)

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
3.  [Agents](https://platform.claude.com/docs/en/api/http/beta/agents)

# Create Agent

POST/v1/agents

Create Agent

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](http-beta.md#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string





"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 45 more



One of the following:

"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"cache-diagnosis-2026-04-07"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"ce-user-management-2026-07-13"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"





"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Body



model: [BetaManagedAgentsModel](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_model) or [BetaManagedAgentsModelConfigParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_model_config_params)



Model identifier. Accepts the [model string](../../20-Models/about-claude-models-overview.md#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control

One of the following:



BetaManagedAgentsModel = string or "claude-opus-5-5" or "claude-fable-5-1" or "claude-sonnet-5" or 12 more



The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModelConfigParams object{ id, effort, inference_geo, speed }



An object that defines additional configuration control over model use



name: string



Human-readable name for the agent.

minLength1

maxLength256



description: optional string or null



Description of what the agent does.

maxLength2048



mcp_servers: optional array of [BetaManagedAgentsURLMCPServerParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_url_mcp_server_params) { type: "url", name, url }



MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/api/beta/agents/managed-agents-mcp-connector-212f0c2926.md).

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

metadata: optional map\[string\]



Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.



multiagent: optional [BetaManagedAgentsMultiagentParams](https://platform.claude.com/docs/en/api/http/beta/sessions#beta_managed_agents_multiagent_params) { type: "coordinator", agents } or null



Multiagent orchestration configuration. Currently supports the `coordinator` topology with a roster of 1-20 agents.



skills: optional array of [BetaManagedAgentsSkillParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_skill_params)



Skills available to the agent.

One of the following:

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

system: optional string or null



System prompt for the agent.

maxLength100000



tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_agent_toolset20260401_params) or [BetaManagedAgentsMCPToolsetParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_mcp_toolset_params) or [BetaManagedAgentsCustomToolParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_custom_tool_params)



Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

One of the following:



BetaManagedAgentsAgentToolset20260401Params object{ type: "agent_toolset_20260401", configs, default_config }



Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.



BetaManagedAgentsMCPToolsetParams object{ type: "mcp_toolset", mcp_server_name, configs, default_config }



Configuration for tools from an MCP server defined in `mcp_servers`.

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

##### Returns



BetaManagedAgentsAgent object{ type: "agent", id, archived_at, 12 more }



A Managed Agents `agent`.

Create Agent

cURL



```python
curl https://api.anthropic.com/v1/agents \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "model": "claude-opus-5",
          "name": "My First Agent",
          "description": "A general-purpose starter agent.",
          "metadata": {
            "foo": "bar"
          },
          "multiagent": {
            "agents": [
              "agent_011CZkYqphY8vELVzwCUpqiQ",
              {
                "type": "self"
              }
            ],
            "type": "coordinator"
          },
          "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user'\''s task end to end.",
          "tools": [
            {
              "type": "agent_toolset_20260401"
            }
          ]
        }'
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
    "id": "claude-opus-5",
    "effort": {
      "type": "low"
    },
    "inference_geo": "inference_geo",
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
          },
          "type": "bash"
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
    "id": "claude-opus-5",
    "effort": {
      "type": "low"
    },
    "inference_geo": "inference_geo",
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
          },
          "type": "bash"
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
