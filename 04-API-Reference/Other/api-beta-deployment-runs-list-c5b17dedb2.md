---
title: "List Deployment Runs - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/deployment_runs/list"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:21Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fdeployment_runs%2Flist)

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

Deployment Runs


List Deployment Runs


Get Deployment Run

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
3.  [Deployment Runs](/docs/en/api/http/beta/deployment_runs)

# List Deployment Runs

GET/v1/deployment_runs

List Deployment Runs

##### Query parameters



"created_at\[gt\]": optional string



Return runs created strictly after this time (exclusive).

formatdate-time



"created_at\[gte\]": optional string



Return runs created at or after this time (inclusive).

formatdate-time



"created_at\[lt\]": optional string



Return runs created strictly before this time (exclusive).

formatdate-time



"created_at\[lte\]": optional string



Return runs created at or before this time (inclusive).

formatdate-time

deployment_id: optional string



Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent `deployment_id` returns 200 with empty data.

has_error: optional boolean



Filter: true for runs with non-null `error`, false for runs with non-null `session_id`. Omit for all.



limit: optional number



Maximum results per page. Default 20, maximum 1000.

formatint32

page: optional string



Opaque pagination cursor. Pass `next_page` from the previous response. Invalid or expired cursors return 400.



trigger_type: optional [BetaManagedAgentsTriggerType](/docs/en/api/http/beta/deployment_runs#beta_managed_agents_trigger_type)



Filter runs by what triggered them. Omit to return all runs.

One of the following:

"schedule"



The run was fired by the deployment's cron schedule.

"manual"



The run was started manually by creating a session directly against the deployment.

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

##### Returns



data: array of [BetaManagedAgentsDeploymentRun](/docs/en/api/http/beta/deployment_runs#beta_managed_agents_deployment_run) { type: "deployment_run", id, agent, 5 more }



List of deployment runs.

type: "deployment_run"



id: string



Unique identifier for this run (`drun_...`).



agent: [BetaManagedAgentsAgentReference](/docs/en/api/http/beta/agents#beta_managed_agents_agent_reference) { type: "agent", id, version }



Snapshot of the agent at fire time. Always fully resolved — deployments pin agent + version.

type: "agent"



id: string





version: number



formatint32



created_at: string



Time this run record was persisted.

formatdate-time

deployment_id: string



ID of the deployment that produced this run.



error: [BetaManagedAgentsEnvironmentArchivedRunError](/docs/en/api/http/beta/deployment_runs#beta_managed_agents_environment_archived_run_error) or [BetaManagedAgentsAgentArchivedRunError](/docs/en/api/http/beta/deployment_runs#beta_managed_agents_agent_archived_run_error) or [BetaManagedAgentsEnvironmentNotFoundRunError](/docs/en/api/http/beta/deployment_runs#beta_managed_agents_environment_not_found_run_error) or 13 more or null



Populated on creation failure. Null on success. Exactly one of `session_id` or `error` is non-null.

One of the following:



BetaManagedAgentsEnvironmentArchivedRunError object{ type: "environment_archived_error", message }



The deployment's environment was archived.

type: "environment_archived_error"



message: string



Human-readable error description.



BetaManagedAgentsAgentArchivedRunError object{ type: "agent_archived_error", message }



The deployment's agent was archived.

type: "agent_archived_error"



message: string



Human-readable error description.



BetaManagedAgentsEnvironmentNotFoundRunError object{ type: "environment_not_found_error", message }



The deployment's environment no longer exists.

type: "environment_not_found_error"



message: string



Human-readable error description.



BetaManagedAgentsVaultNotFoundRunError object{ type: "vault_not_found_error", message }



A vault referenced by the deployment no longer exists.

type: "vault_not_found_error"



message: string



Human-readable error description.



BetaManagedAgentsVaultArchivedRunError object{ type: "vault_archived_error", message }



A vault referenced by the deployment is archived.

type: "vault_archived_error"



message: string



Human-readable error description.



BetaManagedAgentsFileNotFoundRunError object{ type: "file_not_found_error", message }



A file resource referenced by the deployment no longer exists.

type: "file_not_found_error"



message: string



Human-readable error description.



BetaManagedAgentsMemoryStoreArchivedRunError object{ type: "memory_store_archived_error", message }



A memory store referenced by the deployment is archived.

type: "memory_store_archived_error"



message: string



Human-readable error description.



BetaManagedAgentsSkillNotFoundRunError object{ type: "skill_not_found_error", message }



A skill referenced by the deployment's agent no longer exists.

type: "skill_not_found_error"



message: string



Human-readable error description.



BetaManagedAgentsSessionResourceNotFoundRunError object{ type: "session_resource_not_found_error", message }



A referenced resource no longer exists and its kind was not reported.

type: "session_resource_not_found_error"



message: string



Human-readable error description.



BetaManagedAgentsWorkspaceArchivedRunError object{ type: "workspace_archived_error", message }



The deployment's workspace was archived.

type: "workspace_archived_error"



message: string



Human-readable error description.



BetaManagedAgentsOrganizationDisabledRunError object{ type: "organization_disabled_error", message }



The deployment's organization is disabled.

type: "organization_disabled_error"



message: string



Human-readable error description.



BetaManagedAgentsSessionRateLimitedRunError object{ type: "session_rate_limited_error", message }



Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

type: "session_rate_limited_error"



message: string



Human-readable error description.



BetaManagedAgentsSessionCreationRejectedRunError object{ type: "session_creation_rejected_error", message }



The session create request was rejected with a non-retryable validation error.

type: "session_creation_rejected_error"



message: string



Human-readable error description.



BetaManagedAgentsUnknownRunError object{ type: "unknown_error", message }



An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

type: "unknown_error"



message: string



Human-readable error description.



BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object{ type: "self_hosted_resources_unsupported_error", message }



The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: "self_hosted_resources_unsupported_error"



message: string



Human-readable error description.



BetaManagedAgentsMCPEgressBlockedRunError object{ type: "mcp_egress_blocked_error", message }



An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: "mcp_egress_blocked_error"



message: string



Human-readable error description.

session_id: string or null



Populated on success. Null on creation failure. Exactly one of `session_id` or `error` is non-null.



trigger_context: [BetaManagedAgentsTriggerContext](/docs/en/api/http/beta/deployment_runs#beta_managed_agents_trigger_context)



What triggered this run and trigger-specific metadata.

One of the following:



BetaManagedAgentsScheduleTriggerContext object{ type: "schedule", scheduled_at }



The run was fired by the deployment's cron schedule.

type: "schedule"





scheduled_at: string



The UTC instant at which the cron expression matched in the configured timezone, before jitter is applied. At most one run is recorded per (`deployment_id`, `scheduled_at`) pair.

formatdate-time



BetaManagedAgentsManualTriggerContext object{ type: "manual" }



The run was started manually by creating a session directly against the deployment.

type: "manual"



next_page: optional string or null



Opaque cursor for the next page. Null when no more results.

List Deployment Runs

cURL



```python
curl https://api.anthropic.com/v1/deployment_runs \
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
      "id": "id",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
