---
title: "Deployment Runs - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/deployment_runs"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:31Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fdeployment_runs)

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

# Deployment Runs

##### [List Deployment Runs](/docs/en/api/http/beta/deployment_runs/list)

GET/v1/deployment_runs

##### [Get Deployment Run](/docs/en/api/http/beta/deployment_runs/retrieve)

GET/v1/deployment_runs/{deployment_run_id}

##### Models

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

BetaManagedAgentsDeploymentRun object{ type: "deployment_run", id, agent, 5 more }



A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

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

BetaManagedAgentsEnvironmentNotFoundRunError object{ type: "environment_not_found_error", message }



The deployment's environment no longer exists.

type: "environment_not_found_error"

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

BetaManagedAgentsManualTriggerContext object{ type: "manual" }



The run was started manually by creating a session directly against the deployment.

type: "manual"





BetaManagedAgentsMCPEgressBlockedRunError object{ type: "mcp_egress_blocked_error", message }



An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: "mcp_egress_blocked_error"

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

BetaManagedAgentsOrganizationDisabledRunError object{ type: "organization_disabled_error", message }



The deployment's organization is disabled.

type: "organization_disabled_error"



message: string



Human-readable error description.

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

BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object{ type: "self_hosted_resources_unsupported_error", message }



The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: "self_hosted_resources_unsupported_error"

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

BetaManagedAgentsSessionRateLimitedRunError object{ type: "session_rate_limited_error", message }



Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

type: "session_rate_limited_error"

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

BetaManagedAgentsSkillNotFoundRunError object{ type: "skill_not_found_error", message }



A skill referenced by the deployment's agent no longer exists.

type: "skill_not_found_error"



message: string



Human-readable error description.



BetaManagedAgentsTriggerContext = [BetaManagedAgentsScheduleTriggerContext](/docs/en/api/http/beta/deployment_runs#beta_managed_agents_schedule_trigger_context) or [BetaManagedAgentsManualTriggerContext](/docs/en/api/http/beta/deployment_runs#beta_managed_agents_manual_trigger_context)



Describes what triggered a deployment run, with trigger-specific metadata.

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



BetaManagedAgentsTriggerType = "schedule" or "manual"



What triggered a deployment run.

One of the following:

"schedule"



The run was fired by the deployment's cron schedule.

"manual"



The run was started manually by creating a session directly against the deployment.

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

BetaManagedAgentsVaultArchivedRunError object{ type: "vault_archived_error", message }



A vault referenced by the deployment is archived.

type: "vault_archived_error"

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

BetaManagedAgentsWorkspaceArchivedRunError object{ type: "workspace_archived_error", message }



The deployment's workspace was archived.

type: "workspace_archived_error"



message: string



Human-readable error description.
