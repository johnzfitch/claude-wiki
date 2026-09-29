---
title: "Update Agent - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/agents/update"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:20Z"
tags: ["agents", "api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fagents%2Fupdate)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


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

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)
3.  [Agents](/docs/en/api/http/beta/agents)

# Update Agent

POST/v1/agents/{agent_id}

Update Agent

##### Path parameters

agent_id: string



Unique identifier of the agent to update.

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/http/beta#anthropic_beta)

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

description: optional string or null



Description. Omit to preserve; send empty string or null to clear.

maxLength2048



mcp_servers: optional array of [BetaManagedAgentsURLMCPServerParams](/docs/en/api/http/beta/agents#beta_managed_agents_url_mcp_server_params) { type: "url", name, url } or null



MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

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

metadata: optional map\[string\] or null



Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.



model: optional [BetaManagedAgentsModel](/docs/en/api/http/beta/agents#beta_managed_agents_model) or [BetaManagedAgentsModelConfigParams](/docs/en/api/http/beta/agents#beta_managed_agents_model_config_params)



Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

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

multiagent: optional [BetaManagedAgentsMultiagentParams](/docs/en/api/http/beta/sessions#beta_managed_agents_multiagent_params) { type: "coordinator", agents } or null



Multiagent orchestration configuration. Full replacement. Omit to preserve; send null to clear.



name: optional string



Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

maxLength256



skills: optional array of [BetaManagedAgentsSkillParams](/docs/en/api/http/beta/agents#beta_managed_agents_skill_params) or null



Skills. Full replacement. Omit to preserve; send empty array or null to clear.

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

System prompt. Omit to preserve; send empty string or null to clear.

maxLength100000



tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](/docs/en/api/http/beta/agents#beta_managed_agents_agent_toolset20260401_params) or [BetaManagedAgentsMCPToolsetParams](/docs/en/api/http/beta/agents#beta_managed_agents_mcp_toolset_params) or [BetaManagedAgentsCustomToolParams](/docs/en/api/http/beta/agents#beta_managed_agents_custom_tool_params) or null



Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

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

input_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/http/beta/agents#beta_managed_agents_custom_tool_input_schema) { type: "object", properties, required }

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

version: optional number



The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally.

formatint32

##### Returns



BetaManagedAgentsAgent object{ type: "agent", id, archived_at, 12 more }



A Managed Agents `agent`.

Update Agent

cURL



```python
curl https://api.anthropic.com/v1/agents/$AGENT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "description": "updated",
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
          "version": 1
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
