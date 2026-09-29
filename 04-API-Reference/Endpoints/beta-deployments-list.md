---
title: "List Deployments - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/deployments/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:34Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fdeployments%2Flist)

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

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](http-beta.md)
3.  [Deployments](https://platform.claude.com/docs/en/api/http/beta/deployments)

# List Deployments

GET/v1/deployments

List Deployments

##### Query parameters

agent_id: optional string



Filter by agent ID.



"created_at\[gte\]": optional string



Return deployments created at or after this time (inclusive).

formatdate-time



"created_at\[lte\]": optional string



Return deployments created at or before this time (inclusive).

formatdate-time

include_archived: optional boolean



When true, includes archived deployments. Default: false (exclude archived).



limit: optional number



Maximum results per page. Default 20, maximum 100.

formatint32

page: optional string



Opaque pagination cursor.



status: optional [BetaManagedAgentsDeploymentStatus](https://platform.claude.com/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_status)



Filter by status: `active` or `paused`. Omit for both. To include archived deployments, use `include_archived` instead; the two cannot be combined.

One of the following:

"active"



The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

"paused"



The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

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

##### Returns



data: array of [BetaManagedAgentsDeployment](https://platform.claude.com/docs/en/api/http/beta/deployments#beta_managed_agents_deployment) { type: "deployment", id, agent, 14 more }



List of deployments.

type: "deployment"



id: string



Unique identifier for this deployment.



agent: [BetaManagedAgentsAgentReference](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_agent_reference) { type: "agent", id, version }



Reference to the agent this deployment runs, resolved to a concrete version.

type: "agent"



id: string





version: number



formatint32



archived_at: string or null



Time the deployment was archived. Null if not archived.

formatdate-time



created_at: string



Time the deployment was created.

formatdate-time

description: string or null



Description of what the deployment does.

environment_id: string



ID of the `environment` where sessions run.



initial_events: array of [BetaManagedAgentsDeploymentInitialEvent](https://platform.claude.com/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_initial_event)



Events sent to each session immediately after creation.

One of the following:



BetaManagedAgentsDeploymentUserMessageEvent object{ type: "user.message", content }



A user message sent to the session.



BetaManagedAgentsDeploymentUserDefineOutcomeEvent object{ type: "user.define_outcome", description, rubric, max_iterations }



An outcome the agent should work toward. The agent begins work on receipt.



BetaManagedAgentsDeploymentSystemMessageEvent object{ type: "system.message", content }



Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

type: "system.message"





content: array of [BetaManagedAgentsSystemContentBlock](https://platform.claude.com/docs/en/api/http/beta/sessions#beta_managed_agents_system_content_block) { type: "text", text }



System content blocks to append. Text-only.

type: "text"





text: string



The text content.

minLength1

metadata: map\[string\]



Arbitrary key-value metadata. Maximum 16 pairs.

name: string



Human-readable name.



paused_reason: [BetaManagedAgentsDeploymentPausedReason](https://platform.claude.com/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_paused_reason) or null



Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

One of the following:



BetaManagedAgentsManualDeploymentPausedReason object{ type: "manual" }



The caller invoked the pause endpoint on the deployment.

type: "manual"





BetaManagedAgentsErrorDeploymentPausedReason object{ type: "error", error }



A scheduled fire recorded a failed run whose error auto-pauses the deployment.

type: "error"





error: [BetaManagedAgentsDeploymentPausedReasonError](https://platform.claude.com/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_paused_reason_error)



The failed run's error.

One of the following:



resources: array of [BetaManagedAgentsSessionResourceConfig](https://platform.claude.com/docs/en/api/http/beta/deployments#beta_managed_agents_session_resource_config)



Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

One of the following:



BetaManagedAgentsGitHubRepositoryResourceConfig object{ type: "github_repository", url, checkout, mount_path }



A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.



BetaManagedAgentsFileResourceConfig object{ type: "file", file_id, mount_path }



A file mounted into each session's container.

type: "file"



file_id: string



ID of a previously uploaded file.

mount_path: optional string or null



Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



BetaManagedAgentsMemoryStoreResourceConfig object{ type: "memory_store", memory_store_id, access, instructions }



A memory store attached to each session created from this deployment.

type: "memory_store"



memory_store_id: string



The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.



access: optional "read_write" or "read_only" or null



Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

One of the following:

"read_write"



"read_only"



instructions: optional string or null



Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



schedule: [BetaManagedAgentsSchedule](https://platform.claude.com/docs/en/api/http/beta/deployments#beta_managed_agents_schedule) { type: "cron", expression, timezone, 2 more } or null



Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

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

IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

minLength1



last_run_at: optional string or null



Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

formatdate-time

upcoming_runs_at: optional array of string



Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



status: [BetaManagedAgentsDeploymentStatus](https://platform.claude.com/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_status)



Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

One of the following:

"active"



The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

"paused"



The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.



updated_at: string



Time the deployment was last updated.

formatdate-time

vault_ids: array of string



Vault IDs supplying stored credentials for sessions created from this deployment.



budget: optional [BetaManagedAgentsBudgetLimit](https://platform.claude.com/docs/en/api/http/beta/sessions#beta_managed_agents_budget_limit) { type: "limit", max_list_cost } or null



Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

type: "limit"





max_list_cost: [BetaMonetaryAmount](http-beta.md#beta_monetary_amount) { amount, currency }



Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

amount: string



Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is \$25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

currency: [BetaCurrency](http-beta.md#beta_currency)



Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

next_page: optional string or null



Opaque cursor for the next page. Null when no more results.

List Deployments

cURL



```python
curl https://api.anthropic.com/v1/deployments \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
