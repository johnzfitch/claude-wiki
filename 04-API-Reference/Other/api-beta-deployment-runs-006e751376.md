---
title: "Deployment Runs - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/deployment_runs"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:23Z"
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

Deployments

Deployment Runs


List Deployment Runs


Get Deployment Run

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

Deployment runs




cURL

# Deployment Runs

##### [List Deployment Runs](/docs/en/api/beta/deployment_runs/list)

GET/v1/deployment_runs

##### [Get Deployment Run](/docs/en/api/beta/deployment_runs/retrieve)

GET/v1/deployment_runs/{deployment_run_id}

##### ModelsExpand Collapse 



BetaManagedAgentsAgentArchivedRunError object { message, type }



The deployment's agent was archived.

message: string



Human-readable error description.

[](#beta_managed_agents_agent_archived_run_error.message)

type: "agent_archived_error"



[](#beta_managed_agents_agent_archived_run_error.type)

[](#beta_managed_agents_agent_archived_run_error)



BetaManagedAgentsDeploymentRun object { id, agent, created_at, 5 more }



A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

id: string



Unique identifier for this run (`drun_...`).

[](#beta_managed_agents_deployment_run.id)



agent: [BetaManagedAgentsAgentReference](/docs/en/api/beta/agents#beta_managed_agents_agent_reference) { id, type, version }



A resolved agent reference with a concrete version.

id: string



[](#beta_managed_agents_deployment_run.agent%20%2B%20(resource)%20beta.agents.id)

type: "agent"



[](#beta_managed_agents_deployment_run.agent%20%2B%20(resource)%20beta.agents.type)

version: number



[](#beta_managed_agents_deployment_run.agent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_deployment_run.agent)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_deployment_run.created_at)

deployment_id: string



ID of the deployment that produced this run.

[](#beta_managed_agents_deployment_run.deployment_id)



error: [BetaManagedAgentsEnvironmentArchivedRunError](/docs/en/api/beta/deployment_runs#beta_managed_agents_environment_archived_run_error) { message, type } or [BetaManagedAgentsAgentArchivedRunError](/docs/en/api/beta/deployment_runs#beta_managed_agents_agent_archived_run_error) { message, type } or [BetaManagedAgentsEnvironmentNotFoundRunError](/docs/en/api/beta/deployment_runs#beta_managed_agents_environment_not_found_run_error) { message, type } or 13 more



Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:



BetaManagedAgentsEnvironmentArchivedRunError object { message, type }



The deployment's environment was archived.

message: string



Human-readable error description.

[](#beta_managed_agents_environment_archived_run_error.message)

type: "environment_archived_error"



[](#beta_managed_agents_environment_archived_run_error.type)

[](#beta_managed_agents_environment_archived_run_error)



BetaManagedAgentsAgentArchivedRunError object { message, type }



The deployment's agent was archived.

message: string



Human-readable error description.

[](#beta_managed_agents_agent_archived_run_error.message)

type: "agent_archived_error"



[](#beta_managed_agents_agent_archived_run_error.type)

[](#beta_managed_agents_agent_archived_run_error)



BetaManagedAgentsEnvironmentNotFoundRunError object { message, type }



The deployment's environment no longer exists.

message: string



Human-readable error description.

[](#beta_managed_agents_environment_not_found_run_error.message)

type: "environment_not_found_error"



[](#beta_managed_agents_environment_not_found_run_error.type)

[](#beta_managed_agents_environment_not_found_run_error)



BetaManagedAgentsVaultNotFoundRunError object { message, type }



A vault referenced by the deployment no longer exists.

message: string



Human-readable error description.

[](#beta_managed_agents_vault_not_found_run_error.message)

type: "vault_not_found_error"



[](#beta_managed_agents_vault_not_found_run_error.type)

[](#beta_managed_agents_vault_not_found_run_error)



BetaManagedAgentsVaultArchivedRunError object { message, type }



A vault referenced by the deployment is archived.

message: string



Human-readable error description.

[](#beta_managed_agents_vault_archived_run_error.message)

type: "vault_archived_error"



[](#beta_managed_agents_vault_archived_run_error.type)

[](#beta_managed_agents_vault_archived_run_error)



BetaManagedAgentsFileNotFoundRunError object { message, type }



A file resource referenced by the deployment no longer exists.

message: string



Human-readable error description.

[](#beta_managed_agents_file_not_found_run_error.message)

type: "file_not_found_error"



[](#beta_managed_agents_file_not_found_run_error.type)

[](#beta_managed_agents_file_not_found_run_error)



BetaManagedAgentsMemoryStoreArchivedRunError object { message, type }



A memory store referenced by the deployment is archived.

message: string



Human-readable error description.

[](#beta_managed_agents_memory_store_archived_run_error.message)

type: "memory_store_archived_error"



[](#beta_managed_agents_memory_store_archived_run_error.type)

[](#beta_managed_agents_memory_store_archived_run_error)



BetaManagedAgentsSkillNotFoundRunError object { message, type }



A skill referenced by the deployment's agent no longer exists.

message: string



Human-readable error description.

[](#beta_managed_agents_skill_not_found_run_error.message)

type: "skill_not_found_error"



[](#beta_managed_agents_skill_not_found_run_error.type)

[](#beta_managed_agents_skill_not_found_run_error)



BetaManagedAgentsSessionResourceNotFoundRunError object { message, type }



A referenced resource no longer exists and its kind was not reported.

message: string



Human-readable error description.

[](#beta_managed_agents_session_resource_not_found_run_error.message)

type: "session_resource_not_found_error"



[](#beta_managed_agents_session_resource_not_found_run_error.type)

[](#beta_managed_agents_session_resource_not_found_run_error)



BetaManagedAgentsWorkspaceArchivedRunError object { message, type }



The deployment's workspace was archived.

message: string



Human-readable error description.

[](#beta_managed_agents_workspace_archived_run_error.message)

type: "workspace_archived_error"



[](#beta_managed_agents_workspace_archived_run_error.type)

[](#beta_managed_agents_workspace_archived_run_error)



BetaManagedAgentsOrganizationDisabledRunError object { message, type }



The deployment's organization is disabled.

message: string



Human-readable error description.

[](#beta_managed_agents_organization_disabled_run_error.message)

type: "organization_disabled_error"



[](#beta_managed_agents_organization_disabled_run_error.type)

[](#beta_managed_agents_organization_disabled_run_error)



BetaManagedAgentsSessionRateLimitedRunError object { message, type }



Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: string



Human-readable error description.

[](#beta_managed_agents_session_rate_limited_run_error.message)

type: "session_rate_limited_error"



[](#beta_managed_agents_session_rate_limited_run_error.type)

[](#beta_managed_agents_session_rate_limited_run_error)



BetaManagedAgentsSessionCreationRejectedRunError object { message, type }



The session create request was rejected with a non-retryable validation error.

message: string



Human-readable error description.

[](#beta_managed_agents_session_creation_rejected_run_error.message)

type: "session_creation_rejected_error"



[](#beta_managed_agents_session_creation_rejected_run_error.type)

[](#beta_managed_agents_session_creation_rejected_run_error)



BetaManagedAgentsUnknownRunError object { message, type }



An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: string



Human-readable error description.

[](#beta_managed_agents_unknown_run_error.message)

type: "unknown_error"



[](#beta_managed_agents_unknown_run_error.type)

[](#beta_managed_agents_unknown_run_error)



BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object { message, type }



The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: string



Human-readable error description.

[](#beta_managed_agents_self_hosted_resources_unsupported_run_error.message)

type: "self_hosted_resources_unsupported_error"



[](#beta_managed_agents_self_hosted_resources_unsupported_run_error.type)

[](#beta_managed_agents_self_hosted_resources_unsupported_run_error)



BetaManagedAgentsMCPEgressBlockedRunError object { message, type }



An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: string



Human-readable error description.

[](#beta_managed_agents_mcp_egress_blocked_run_error.message)

type: "mcp_egress_blocked_error"



[](#beta_managed_agents_mcp_egress_blocked_run_error.type)

[](#beta_managed_agents_mcp_egress_blocked_run_error)

[](#beta_managed_agents_deployment_run.error)

session_id: string



Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

[](#beta_managed_agents_deployment_run.session_id)



trigger_context: [BetaManagedAgentsTriggerContext](/docs/en/api/beta/deployment_runs#beta_managed_agents_trigger_context)



Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:



BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type }



The run was fired by the deployment's cron schedule.

scheduled_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_deployment_run.trigger_context%20%2B%20(resource)%20beta.deployment_runs.scheduled_at)

type: "schedule"



[](#beta_managed_agents_deployment_run.trigger_context%20%2B%20(resource)%20beta.deployment_runs.type)

[](#beta_managed_agents_deployment_run.trigger_context%20%2B%20(resource)%20beta.deployment_runs)



BetaManagedAgentsManualTriggerContext object { type }



The run was started manually by creating a session directly against the deployment.

type: "manual"



[](#beta_managed_agents_deployment_run.trigger_context%20%2B%20(resource)%20beta.deployment_runs.type)

[](#beta_managed_agents_deployment_run.trigger_context%20%2B%20(resource)%20beta.deployment_runs)

[](#beta_managed_agents_deployment_run.trigger_context)

type: "deployment_run"



[](#beta_managed_agents_deployment_run.type)

[](#beta_managed_agents_deployment_run)



BetaManagedAgentsEnvironmentArchivedRunError object { message, type }



The deployment's environment was archived.

message: string



Human-readable error description.

[](#beta_managed_agents_environment_archived_run_error.message)

type: "environment_archived_error"



[](#beta_managed_agents_environment_archived_run_error.type)

[](#beta_managed_agents_environment_archived_run_error)



BetaManagedAgentsEnvironmentNotFoundRunError object { message, type }



The deployment's environment no longer exists.

message: string



Human-readable error description.

[](#beta_managed_agents_environment_not_found_run_error.message)

type: "environment_not_found_error"



[](#beta_managed_agents_environment_not_found_run_error.type)

[](#beta_managed_agents_environment_not_found_run_error)



BetaManagedAgentsFileNotFoundRunError object { message, type }



A file resource referenced by the deployment no longer exists.

message: string



Human-readable error description.

[](#beta_managed_agents_file_not_found_run_error.message)

type: "file_not_found_error"



[](#beta_managed_agents_file_not_found_run_error.type)

[](#beta_managed_agents_file_not_found_run_error)



BetaManagedAgentsManualTriggerContext object { type }



The run was started manually by creating a session directly against the deployment.

type: "manual"



[](#beta_managed_agents_manual_trigger_context.type)

[](#beta_managed_agents_manual_trigger_context)



BetaManagedAgentsMCPEgressBlockedRunError object { message, type }



An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: string



Human-readable error description.

[](#beta_managed_agents_mcp_egress_blocked_run_error.message)

type: "mcp_egress_blocked_error"



[](#beta_managed_agents_mcp_egress_blocked_run_error.type)

[](#beta_managed_agents_mcp_egress_blocked_run_error)



BetaManagedAgentsMemoryStoreArchivedRunError object { message, type }



A memory store referenced by the deployment is archived.

message: string



Human-readable error description.

[](#beta_managed_agents_memory_store_archived_run_error.message)

type: "memory_store_archived_error"



[](#beta_managed_agents_memory_store_archived_run_error.type)

[](#beta_managed_agents_memory_store_archived_run_error)



BetaManagedAgentsOrganizationDisabledRunError object { message, type }



The deployment's organization is disabled.

message: string



Human-readable error description.

[](#beta_managed_agents_organization_disabled_run_error.message)

type: "organization_disabled_error"



[](#beta_managed_agents_organization_disabled_run_error.type)

[](#beta_managed_agents_organization_disabled_run_error)



BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type }



The run was fired by the deployment's cron schedule.

scheduled_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_schedule_trigger_context.scheduled_at)

type: "schedule"



[](#beta_managed_agents_schedule_trigger_context.type)

[](#beta_managed_agents_schedule_trigger_context)



BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object { message, type }



The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: string



Human-readable error description.

[](#beta_managed_agents_self_hosted_resources_unsupported_run_error.message)

type: "self_hosted_resources_unsupported_error"



[](#beta_managed_agents_self_hosted_resources_unsupported_run_error.type)

[](#beta_managed_agents_self_hosted_resources_unsupported_run_error)



BetaManagedAgentsSessionCreationRejectedRunError object { message, type }



The session create request was rejected with a non-retryable validation error.

message: string



Human-readable error description.

[](#beta_managed_agents_session_creation_rejected_run_error.message)

type: "session_creation_rejected_error"



[](#beta_managed_agents_session_creation_rejected_run_error.type)

[](#beta_managed_agents_session_creation_rejected_run_error)



BetaManagedAgentsSessionRateLimitedRunError object { message, type }



Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: string



Human-readable error description.

[](#beta_managed_agents_session_rate_limited_run_error.message)

type: "session_rate_limited_error"



[](#beta_managed_agents_session_rate_limited_run_error.type)

[](#beta_managed_agents_session_rate_limited_run_error)



BetaManagedAgentsSessionResourceNotFoundRunError object { message, type }



A referenced resource no longer exists and its kind was not reported.

message: string



Human-readable error description.

[](#beta_managed_agents_session_resource_not_found_run_error.message)

type: "session_resource_not_found_error"



[](#beta_managed_agents_session_resource_not_found_run_error.type)

[](#beta_managed_agents_session_resource_not_found_run_error)



BetaManagedAgentsSkillNotFoundRunError object { message, type }



A skill referenced by the deployment's agent no longer exists.

message: string



Human-readable error description.

[](#beta_managed_agents_skill_not_found_run_error.message)

type: "skill_not_found_error"



[](#beta_managed_agents_skill_not_found_run_error.type)

[](#beta_managed_agents_skill_not_found_run_error)



BetaManagedAgentsTriggerContext = [BetaManagedAgentsScheduleTriggerContext](/docs/en/api/beta/deployment_runs#beta_managed_agents_schedule_trigger_context) { scheduled_at, type } or [BetaManagedAgentsManualTriggerContext](/docs/en/api/beta/deployment_runs#beta_managed_agents_manual_trigger_context) { type }



Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:



BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type }



The run was fired by the deployment's cron schedule.

scheduled_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_schedule_trigger_context.scheduled_at)

type: "schedule"



[](#beta_managed_agents_schedule_trigger_context.type)

[](#beta_managed_agents_schedule_trigger_context)



BetaManagedAgentsManualTriggerContext object { type }



The run was started manually by creating a session directly against the deployment.

type: "manual"



[](#beta_managed_agents_manual_trigger_context.type)

[](#beta_managed_agents_manual_trigger_context)

[](#beta_managed_agents_trigger_context)



BetaManagedAgentsTriggerType = "schedule" or "manual"



What triggered a deployment run.

One of the following:

"schedule"



[](#beta_managed_agents_trigger_type%5B0%5D)

"manual"



[](#beta_managed_agents_trigger_type%5B1%5D)

[](#beta_managed_agents_trigger_type)



BetaManagedAgentsUnknownRunError object { message, type }



An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: string



Human-readable error description.

[](#beta_managed_agents_unknown_run_error.message)

type: "unknown_error"



[](#beta_managed_agents_unknown_run_error.type)

[](#beta_managed_agents_unknown_run_error)



BetaManagedAgentsVaultArchivedRunError object { message, type }



A vault referenced by the deployment is archived.

message: string



Human-readable error description.

[](#beta_managed_agents_vault_archived_run_error.message)

type: "vault_archived_error"



[](#beta_managed_agents_vault_archived_run_error.type)

[](#beta_managed_agents_vault_archived_run_error)



BetaManagedAgentsVaultNotFoundRunError object { message, type }



A vault referenced by the deployment no longer exists.

message: string



Human-readable error description.

[](#beta_managed_agents_vault_not_found_run_error.message)

type: "vault_not_found_error"



[](#beta_managed_agents_vault_not_found_run_error.type)

[](#beta_managed_agents_vault_not_found_run_error)



BetaManagedAgentsWorkspaceArchivedRunError object { message, type }



The deployment's workspace was archived.

message: string



Human-readable error description.

[](#beta_managed_agents_workspace_archived_run_error.message)

type: "workspace_archived_error"



[](#beta_managed_agents_workspace_archived_run_error.type)

[](#beta_managed_agents_workspace_archived_run_error)
