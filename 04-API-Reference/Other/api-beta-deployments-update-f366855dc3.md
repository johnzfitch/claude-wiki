---
title: "Update Deployment - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/deployments/update"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:29Z"
tags: ["api"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fdeployments%2Fupdate)

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

Environments

Sessions

Deployments


Create Deployment


List Deployments


Get Deployment


Update Deployment


Archive Deployment


Run Deployment Now


Pause Deployment


Unpause Deployment

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
3.  [Deployments](/docs/en/api/http/beta/deployments)

# Update Deployment

POST/v1/deployments/{deployment_id}

Update Deployment

##### Path parameters

deployment_id: string



Unique identifier of the deployment to update.

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

agent: optional string or [BetaManagedAgentsAgentParams](/docs/en/api/http/beta/sessions#beta_managed_agents_agent_params)



Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

One of the following:

string





BetaManagedAgentsAgentParams object{ type: "agent", id, version }



Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

type: "agent"





id: string



The `agent` ID.

minLength1

maxLength128



version: optional number



The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

formatint32



budget: optional [BetaManagedAgentsBudgetLimit](/docs/en/api/http/beta/sessions#beta_managed_agents_budget_limit) { type: "limit", max_list_cost } or null



Spend ceiling for future sessions. Full replacement. Omit to preserve; send null to clear (sessions created afterwards are uncapped). The deployment agent's model must have a public list price, or the request is rejected; a multiagent roster is re-validated in full when each fire copies the cap, which fails closed the same way.

type: "limit"





max_list_cost: [BetaMonetaryAmount](/docs/en/api/http/beta#beta_monetary_amount) { amount, currency }



Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

amount: string



Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is \$25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

currency: [BetaCurrency](/docs/en/api/http/beta#beta_currency)



Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.



description: optional string or null



Description. Omit to preserve; send empty string or null to clear.

maxLength2048



environment_id: optional string



ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

maxLength128



initial_events: optional array of [BetaManagedAgentsDeploymentInitialEventParams](/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_initial_event_params)



Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

One of the following:



BetaManagedAgentsUserMessageEventParams object{ type: "user.message", content }



Parameters for sending a user message to the session.



BetaManagedAgentsUserDefineOutcomeEventParams object{ type: "user.define_outcome", description, rubric, max_iterations }



Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.



BetaManagedAgentsSystemMessageEventParams object{ type: "system.message", content }



Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

type: "system.message"





content: array of [BetaManagedAgentsSystemContentBlock](/docs/en/api/http/beta/sessions#beta_managed_agents_system_content_block) { type: "text", text }



System content blocks to append. Text-only.

type: "text"





text: string



The text content.

minLength1

metadata: optional map\[string\] or null



Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.



name: optional string



Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

maxLength256



resources: optional array of [BetaManagedAgentsGitHubRepositoryResourceParams](/docs/en/api/http/beta/sessions#beta_managed_agents_github_repository_resource_params) or [BetaManagedAgentsFileResourceParams](/docs/en/api/http/beta/sessions#beta_managed_agents_file_resource_params) or [BetaManagedAgentsMemoryStoreResourceParam](/docs/en/api/http/beta/sessions#beta_managed_agents_memory_store_resource_param) or null



Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

One of the following:



BetaManagedAgentsGitHubRepositoryResourceParams object{ type: "github_repository", url, authorization_token, 2 more }



Mount a GitHub repository into the session's container.



BetaManagedAgentsFileResourceParams object{ type: "file", file_id, mount_path }



Mount a file uploaded via the Files API into the session.

type: "file"





file_id: string



ID of a previously uploaded file.

minLength1

maxLength128



mount_path: optional string or null



Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

minLength1

maxLength4096



BetaManagedAgentsMemoryStoreResourceParam object{ type: "memory_store", memory_store_id, access, instructions }



Parameters for attaching a memory store to an agent session.

type: "memory_store"



memory_store_id: string



The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.



access: optional "read_write" or "read_only" or null



Access mode for the mounted store. Defaults to read_write. read_only mounts the store as a read-only filesystem.

One of the following:

"read_write"



"read_only"





instructions: optional string or null



Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

maxLength4096



schedule: optional [BetaManagedAgentsScheduleParams](/docs/en/api/http/beta/deployments#beta_managed_agents_schedule_params) { type: "cron", expression, timezone } or null



Cron schedule. Full replacement. Omit to preserve; send null to clear (revert to manual-only).

type: "cron"





expression: string



5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, \#, and ? - is not supported, nor are predefined shortcuts (@daily).

minLength1

maxLength256



timezone: string



Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

minLength1

vault_ids: optional array of string or null



Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

##### Returns



BetaManagedAgentsDeployment object{ type: "deployment", id, agent, 14 more }



A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

Update Deployment

cURL



```python
curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "schedule": {
            "expression": "0 9 * * 1-5",
            "timezone": "America/Los_Angeles",
            "type": "cron"
          }
        }'
```

Response 200



```python
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

##### Returns Examples

Response 200



```python
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
