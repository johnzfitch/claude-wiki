---
title: "Deployments - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/deployments"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:28Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fdeployments)

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

# Deployments

##### [Create Deployment](/docs/en/api/http/beta/deployments/create)

POST/v1/deployments

##### [List Deployments](/docs/en/api/http/beta/deployments/list)

GET/v1/deployments

##### [Get Deployment](/docs/en/api/http/beta/deployments/retrieve)

GET/v1/deployments/{deployment_id}

##### [Update Deployment](/docs/en/api/http/beta/deployments/update)

POST/v1/deployments/{deployment_id}

##### [Archive Deployment](/docs/en/api/http/beta/deployments/archive)

POST/v1/deployments/{deployment_id}/archive

##### [Run Deployment Now](/docs/en/api/http/beta/deployments/run)

POST/v1/deployments/{deployment_id}/run

##### [Pause Deployment](/docs/en/api/http/beta/deployments/pause)

POST/v1/deployments/{deployment_id}/pause

##### [Unpause Deployment](/docs/en/api/http/beta/deployments/unpause)

POST/v1/deployments/{deployment_id}/unpause

##### Models



BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object{ type: "agent_archived_error" }



The deployment's agent was archived.

type: "agent_archived_error"





BetaManagedAgentsCronSchedule object{ type: "cron", expression, timezone, 2 more }



5-field POSIX cron schedule with computed runtime timestamps.

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

BetaManagedAgentsCronScheduleParams object{ type: "cron", expression, timezone }



5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

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



BetaManagedAgentsDeployment object{ type: "deployment", id, agent, 14 more }



A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.



BetaManagedAgentsDeploymentInitialEvent = [BetaManagedAgentsDeploymentUserMessageEvent](/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_user_message_event) or [BetaManagedAgentsDeploymentUserDefineOutcomeEvent](/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_user_define_outcome_event) or [BetaManagedAgentsDeploymentSystemMessageEvent](/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_system_message_event)



An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

One of the following:



BetaManagedAgentsDeploymentInitialEventParams = [BetaManagedAgentsUserMessageEventParams](/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_message_event_params) or [BetaManagedAgentsUserDefineOutcomeEventParams](/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_define_outcome_event_params) or [BetaManagedAgentsSystemMessageEventParams](/docs/en/api/http/beta/sessions/events#beta_managed_agents_system_message_event_params)



An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

One of the following:



BetaManagedAgentsDeploymentPausedReason = [BetaManagedAgentsManualDeploymentPausedReason](/docs/en/api/http/beta/deployments#beta_managed_agents_manual_deployment_paused_reason) or [BetaManagedAgentsErrorDeploymentPausedReason](/docs/en/api/http/beta/deployments#beta_managed_agents_error_deployment_paused_reason)



Why a deployment is paused. Non-null exactly when `status` is `paused`.

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

error: [BetaManagedAgentsDeploymentPausedReasonError](/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_paused_reason_error)



The failed run's error.

One of the following:



BetaManagedAgentsDeploymentPausedReasonError = [BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError](/docs/en/api/http/beta/deployments#beta_managed_agents_environment_archived_deployment_paused_reason_error) or [BetaManagedAgentsAgentArchivedDeploymentPausedReasonError](/docs/en/api/http/beta/deployments#beta_managed_agents_agent_archived_deployment_paused_reason_error) or [BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError](/docs/en/api/http/beta/deployments#beta_managed_agents_environment_not_found_deployment_paused_reason_error) or 11 more



The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



BetaManagedAgentsDeploymentStatus = "active" or "paused"



Lifecycle status of a deployment.

One of the following:

"active"



The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

"paused"



The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.



BetaManagedAgentsDeploymentSystemMessageEvent object{ type: "system.message", content }



Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

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



BetaManagedAgentsDeploymentUserDefineOutcomeEvent object{ type: "user.define_outcome", description, rubric, max_iterations }



An outcome the agent should work toward. The agent begins work on receipt.



BetaManagedAgentsDeploymentUserMessageEvent object{ type: "user.message", content }



A user message sent to the session.



BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object{ type: "environment_archived_error" }



The deployment's environment was archived.

type: "environment_archived_error"





BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object{ type: "environment_not_found_error" }



The deployment's environment no longer exists.

type: "environment_not_found_error"





BetaManagedAgentsErrorDeploymentPausedReason object{ type: "error", error }



A scheduled fire recorded a failed run whose error auto-pauses the deployment.

type: "error"





error: [BetaManagedAgentsDeploymentPausedReasonError](/docs/en/api/http/beta/deployments#beta_managed_agents_deployment_paused_reason_error)



The failed run's error.

One of the following:



BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object{ type: "file_not_found_error" }



A file resource referenced by the deployment no longer exists.

type: "file_not_found_error"



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

BetaManagedAgentsGitHubRepositoryResourceConfig object{ type: "github_repository", url, checkout, mount_path }



A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.



BetaManagedAgentsManualDeploymentPausedReason object{ type: "manual" }



The caller invoked the pause endpoint on the deployment.

type: "manual"





BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object{ type: "mcp_egress_blocked_error" }



An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: "mcp_egress_blocked_error"





BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object{ type: "memory_store_archived_error" }



A memory store referenced by the deployment is archived.

type: "memory_store_archived_error"



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

BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object{ type: "organization_disabled_error" }



The deployment's organization is disabled.

type: "organization_disabled_error"





BetaManagedAgentsSchedule object{ type: "cron", expression, timezone, 2 more }



A recurring schedule with computed runtime timestamps. Discriminated union — only cron is supported currently.

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

BetaManagedAgentsScheduleParams object{ type: "cron", expression, timezone }



A recurring schedule. Discriminated union — only cron is supported currently.

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



BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object{ type: "self_hosted_resources_unsupported_error" }



The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: "self_hosted_resources_unsupported_error"





BetaManagedAgentsSessionResourceConfig = [BetaManagedAgentsGitHubRepositoryResourceConfig](/docs/en/api/http/beta/deployments#beta_managed_agents_github_repository_resource_config) or [BetaManagedAgentsFileResourceConfig](/docs/en/api/http/beta/deployments#beta_managed_agents_file_resource_config) or [BetaManagedAgentsMemoryStoreResourceConfig](/docs/en/api/http/beta/deployments#beta_managed_agents_memory_store_resource_config)



A configured session resource. Echoes the input minus write-only credentials.

One of the following:



BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object{ type: "session_resource_not_found_error" }



A referenced resource no longer exists and its kind was not reported.

type: "session_resource_not_found_error"





BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object{ type: "skill_not_found_error" }



A skill referenced by the deployment's agent no longer exists.

type: "skill_not_found_error"





BetaManagedAgentsUnknownDeploymentPausedReasonError object{ type: "unknown_error" }



An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: "unknown_error"





BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object{ type: "vault_archived_error" }



A vault referenced by the deployment is archived.

type: "vault_archived_error"





BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object{ type: "vault_not_found_error" }



A vault referenced by the deployment no longer exists.

type: "vault_not_found_error"





BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object{ type: "workspace_archived_error" }



The deployment's workspace was archived.

type: "workspace_archived_error"
