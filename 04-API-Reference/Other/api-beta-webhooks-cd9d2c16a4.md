---
title: "Webhooks - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/webhooks"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:29Z"
tags: ["api", "hooks"]
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

Webhooks




cURL

# Webhooks

Helpers for receiving and verifying webhook events. Use `unwrap` in your SDK to verify signatures and parse payloads; see the [webhooks guide](/docs/en/managed-agents/webhooks) for handler examples.

Possible `data.type` values:

- `agent.archived`
- `agent.created`
- `agent.deleted`
- `agent.updated`
- `deployment.archived`
- `deployment.created`
- `deployment.deleted`
- `deployment.paused`
- `deployment.unpaused`
- `deployment.updated`
- `deployment_run.failed`
- `deployment_run.started`
- `deployment_run.succeeded`
- `environment.archived`
- `environment.created`
- `environment.deleted`
- `environment.updated`
- `memory_store.archived`
- `memory_store.created`
- `memory_store.deleted`
- `session.archived`
- `session.created`
- `session.deleted`
- `session.idled`
- `session.outcome_evaluation_ended`
- `session.pending`
- `session.requires_action`
- `session.running`
- `session.status_idled`
- `session.status_rescheduled`
- `session.status_run_started`
- `session.status_terminated`
- `session.thread_created`
- `session.thread_idled`
- `session.thread_terminated`
- `session.updated`
- `vault.archived`
- `vault.created`
- `vault.deleted`
- `vault_credential.archived`
- `vault_credential.created`
- `vault_credential.deleted`
- `vault_credential.refresh_failed`

##### ModelsExpand Collapse 



BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_agent_archived_event_data.id)

organization_id: string



[](#beta_webhook_agent_archived_event_data.organization_id)

type: "agent.archived"



[](#beta_webhook_agent_archived_event_data.type)

workspace_id: string



[](#beta_webhook_agent_archived_event_data.workspace_id)

[](#beta_webhook_agent_archived_event_data)



BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_agent_created_event_data.id)

organization_id: string



[](#beta_webhook_agent_created_event_data.organization_id)

type: "agent.created"



[](#beta_webhook_agent_created_event_data.type)

workspace_id: string



[](#beta_webhook_agent_created_event_data.workspace_id)

[](#beta_webhook_agent_created_event_data)



BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_agent_deleted_event_data.id)

organization_id: string



[](#beta_webhook_agent_deleted_event_data.organization_id)

type: "agent.deleted"



[](#beta_webhook_agent_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_agent_deleted_event_data.workspace_id)

[](#beta_webhook_agent_deleted_event_data)



BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_agent_updated_event_data.id)

organization_id: string



[](#beta_webhook_agent_updated_event_data.organization_id)

type: "agent.updated"



[](#beta_webhook_agent_updated_event_data.type)

workspace_id: string



[](#beta_webhook_agent_updated_event_data.workspace_id)

[](#beta_webhook_agent_updated_event_data)



BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_archived_event_data.id)

organization_id: string



[](#beta_webhook_deployment_archived_event_data.organization_id)

type: "deployment.archived"



[](#beta_webhook_deployment_archived_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_archived_event_data.workspace_id)

[](#beta_webhook_deployment_archived_event_data)



BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_created_event_data.id)

organization_id: string



[](#beta_webhook_deployment_created_event_data.organization_id)

type: "deployment.created"



[](#beta_webhook_deployment_created_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_created_event_data.workspace_id)

[](#beta_webhook_deployment_created_event_data)



BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_deleted_event_data.id)

organization_id: string



[](#beta_webhook_deployment_deleted_event_data.organization_id)

type: "deployment.deleted"



[](#beta_webhook_deployment_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_deleted_event_data.workspace_id)

[](#beta_webhook_deployment_deleted_event_data)



BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_paused_event_data.id)

organization_id: string



[](#beta_webhook_deployment_paused_event_data.organization_id)

type: "deployment.paused"



[](#beta_webhook_deployment_paused_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_paused_event_data.workspace_id)

[](#beta_webhook_deployment_paused_event_data)



BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#beta_webhook_deployment_run_failed_event_data.id)

organization_id: string



[](#beta_webhook_deployment_run_failed_event_data.organization_id)

type: "deployment_run.failed"



[](#beta_webhook_deployment_run_failed_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_run_failed_event_data.workspace_id)

[](#beta_webhook_deployment_run_failed_event_data)



BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#beta_webhook_deployment_run_started_event_data.id)

organization_id: string



[](#beta_webhook_deployment_run_started_event_data.organization_id)

type: "deployment_run.started"



[](#beta_webhook_deployment_run_started_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_run_started_event_data.workspace_id)

[](#beta_webhook_deployment_run_started_event_data)



BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#beta_webhook_deployment_run_succeeded_event_data.id)

organization_id: string



[](#beta_webhook_deployment_run_succeeded_event_data.organization_id)

type: "deployment_run.succeeded"



[](#beta_webhook_deployment_run_succeeded_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_run_succeeded_event_data.workspace_id)

[](#beta_webhook_deployment_run_succeeded_event_data)



BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_unpaused_event_data.id)

organization_id: string



[](#beta_webhook_deployment_unpaused_event_data.organization_id)

type: "deployment.unpaused"



[](#beta_webhook_deployment_unpaused_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_unpaused_event_data.workspace_id)

[](#beta_webhook_deployment_unpaused_event_data)



BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_updated_event_data.id)

organization_id: string



[](#beta_webhook_deployment_updated_event_data.organization_id)

type: "deployment.updated"



[](#beta_webhook_deployment_updated_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_updated_event_data.workspace_id)

[](#beta_webhook_deployment_updated_event_data)



BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_environment_archived_event_data.id)

organization_id: string



[](#beta_webhook_environment_archived_event_data.organization_id)

type: "environment.archived"



[](#beta_webhook_environment_archived_event_data.type)

workspace_id: string



[](#beta_webhook_environment_archived_event_data.workspace_id)

[](#beta_webhook_environment_archived_event_data)



BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_environment_created_event_data.id)

organization_id: string



[](#beta_webhook_environment_created_event_data.organization_id)

type: "environment.created"



[](#beta_webhook_environment_created_event_data.type)

workspace_id: string



[](#beta_webhook_environment_created_event_data.workspace_id)

[](#beta_webhook_environment_created_event_data)



BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_environment_deleted_event_data.id)

organization_id: string



[](#beta_webhook_environment_deleted_event_data.organization_id)

type: "environment.deleted"



[](#beta_webhook_environment_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_environment_deleted_event_data.workspace_id)

[](#beta_webhook_environment_deleted_event_data)



BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_environment_updated_event_data.id)

organization_id: string



[](#beta_webhook_environment_updated_event_data.organization_id)

type: "environment.updated"



[](#beta_webhook_environment_updated_event_data.type)

workspace_id: string



[](#beta_webhook_environment_updated_event_data.workspace_id)

[](#beta_webhook_environment_updated_event_data)



BetaWebhookEvent object { id, created_at, data, type }



id: string



Unique event identifier for idempotency.

[](#beta_webhook_event.id)

created_at: string



RFC 3339 timestamp when the event occurred.

[](#beta_webhook_event.created_at)



data: [BetaWebhookEventData](/docs/en/api/beta/webhooks#beta_webhook_event_data)



One of the following:



BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.created"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.pending"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.running"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.idled"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.requires_action"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.archived"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.deleted"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.status_rescheduled"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.status_run_started"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.status_idled"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.status_terminated"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.session_thread_id)

type: "session.thread_created"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.session_thread_id)

type: "session.thread_idled"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.session_thread_id)

type: "session.thread_terminated"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.outcome_evaluation_ended"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault.created"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault.archived"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault.deleted"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault_credential.created"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.vault_id)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault_credential.archived"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.vault_id)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault_credential.deleted"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.vault_id)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault_credential.refresh_failed"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.vault_id)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.updated"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "agent.created"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "agent.archived"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "agent.deleted"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.paused"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment_run.failed"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.created"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.updated"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.unpaused"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "agent.updated"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.archived"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment_run.started"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.deleted"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment_run.succeeded"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "environment.created"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "environment.updated"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "environment.archived"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "environment.deleted"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "memory_store.created"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "memory_store.archived"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "memory_store.deleted"



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#beta_webhook_event.data%20%2B%20(resource)%20beta.webhooks)

[](#beta_webhook_event.data)

type: "event"



Object type. Always `event` for webhook payloads.

[](#beta_webhook_event.type)

[](#beta_webhook_event)



BetaWebhookEventData = [BetaWebhookSessionCreatedEventData](/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data) { id, organization_id, type, workspace_id } or [BetaWebhookSessionPendingEventData](/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data) { id, organization_id, type, workspace_id } or [BetaWebhookSessionRunningEventData](/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data) { id, organization_id, type, workspace_id } or 40 more



One of the following:



BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_created_event_data.id)

organization_id: string



[](#beta_webhook_session_created_event_data.organization_id)

type: "session.created"



[](#beta_webhook_session_created_event_data.type)

workspace_id: string



[](#beta_webhook_session_created_event_data.workspace_id)

[](#beta_webhook_session_created_event_data)



BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_pending_event_data.id)

organization_id: string



[](#beta_webhook_session_pending_event_data.organization_id)

type: "session.pending"



[](#beta_webhook_session_pending_event_data.type)

workspace_id: string



[](#beta_webhook_session_pending_event_data.workspace_id)

[](#beta_webhook_session_pending_event_data)



BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_running_event_data.id)

organization_id: string



[](#beta_webhook_session_running_event_data.organization_id)

type: "session.running"



[](#beta_webhook_session_running_event_data.type)

workspace_id: string



[](#beta_webhook_session_running_event_data.workspace_id)

[](#beta_webhook_session_running_event_data)



BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_idled_event_data.id)

organization_id: string



[](#beta_webhook_session_idled_event_data.organization_id)

type: "session.idled"



[](#beta_webhook_session_idled_event_data.type)

workspace_id: string



[](#beta_webhook_session_idled_event_data.workspace_id)

[](#beta_webhook_session_idled_event_data)



BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_requires_action_event_data.id)

organization_id: string



[](#beta_webhook_session_requires_action_event_data.organization_id)

type: "session.requires_action"



[](#beta_webhook_session_requires_action_event_data.type)

workspace_id: string



[](#beta_webhook_session_requires_action_event_data.workspace_id)

[](#beta_webhook_session_requires_action_event_data)



BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_archived_event_data.id)

organization_id: string



[](#beta_webhook_session_archived_event_data.organization_id)

type: "session.archived"



[](#beta_webhook_session_archived_event_data.type)

workspace_id: string



[](#beta_webhook_session_archived_event_data.workspace_id)

[](#beta_webhook_session_archived_event_data)



BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_deleted_event_data.id)

organization_id: string



[](#beta_webhook_session_deleted_event_data.organization_id)

type: "session.deleted"



[](#beta_webhook_session_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_session_deleted_event_data.workspace_id)

[](#beta_webhook_session_deleted_event_data)



BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_status_rescheduled_event_data.id)

organization_id: string



[](#beta_webhook_session_status_rescheduled_event_data.organization_id)

type: "session.status_rescheduled"



[](#beta_webhook_session_status_rescheduled_event_data.type)

workspace_id: string



[](#beta_webhook_session_status_rescheduled_event_data.workspace_id)

[](#beta_webhook_session_status_rescheduled_event_data)



BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_status_run_started_event_data.id)

organization_id: string



[](#beta_webhook_session_status_run_started_event_data.organization_id)

type: "session.status_run_started"



[](#beta_webhook_session_status_run_started_event_data.type)

workspace_id: string



[](#beta_webhook_session_status_run_started_event_data.workspace_id)

[](#beta_webhook_session_status_run_started_event_data)



BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_status_idled_event_data.id)

organization_id: string



[](#beta_webhook_session_status_idled_event_data.organization_id)

type: "session.status_idled"



[](#beta_webhook_session_status_idled_event_data.type)

workspace_id: string



[](#beta_webhook_session_status_idled_event_data.workspace_id)

[](#beta_webhook_session_status_idled_event_data)



BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_status_terminated_event_data.id)

organization_id: string



[](#beta_webhook_session_status_terminated_event_data.organization_id)

type: "session.status_terminated"



[](#beta_webhook_session_status_terminated_event_data.type)

workspace_id: string



[](#beta_webhook_session_status_terminated_event_data.workspace_id)

[](#beta_webhook_session_status_terminated_event_data)



BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_thread_created_event_data.id)

organization_id: string



[](#beta_webhook_session_thread_created_event_data.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#beta_webhook_session_thread_created_event_data.session_thread_id)

type: "session.thread_created"



[](#beta_webhook_session_thread_created_event_data.type)

workspace_id: string



[](#beta_webhook_session_thread_created_event_data.workspace_id)

[](#beta_webhook_session_thread_created_event_data)



BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_thread_idled_event_data.id)

organization_id: string



[](#beta_webhook_session_thread_idled_event_data.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#beta_webhook_session_thread_idled_event_data.session_thread_id)

type: "session.thread_idled"



[](#beta_webhook_session_thread_idled_event_data.type)

workspace_id: string



[](#beta_webhook_session_thread_idled_event_data.workspace_id)

[](#beta_webhook_session_thread_idled_event_data)



BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_thread_terminated_event_data.id)

organization_id: string



[](#beta_webhook_session_thread_terminated_event_data.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#beta_webhook_session_thread_terminated_event_data.session_thread_id)

type: "session.thread_terminated"



[](#beta_webhook_session_thread_terminated_event_data.type)

workspace_id: string



[](#beta_webhook_session_thread_terminated_event_data.workspace_id)

[](#beta_webhook_session_thread_terminated_event_data)



BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_outcome_evaluation_ended_event_data.id)

organization_id: string



[](#beta_webhook_session_outcome_evaluation_ended_event_data.organization_id)

type: "session.outcome_evaluation_ended"



[](#beta_webhook_session_outcome_evaluation_ended_event_data.type)

workspace_id: string



[](#beta_webhook_session_outcome_evaluation_ended_event_data.workspace_id)

[](#beta_webhook_session_outcome_evaluation_ended_event_data)



BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#beta_webhook_vault_created_event_data.id)

organization_id: string



[](#beta_webhook_vault_created_event_data.organization_id)

type: "vault.created"



[](#beta_webhook_vault_created_event_data.type)

workspace_id: string



[](#beta_webhook_vault_created_event_data.workspace_id)

[](#beta_webhook_vault_created_event_data)



BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#beta_webhook_vault_archived_event_data.id)

organization_id: string



[](#beta_webhook_vault_archived_event_data.organization_id)

type: "vault.archived"



[](#beta_webhook_vault_archived_event_data.type)

workspace_id: string



[](#beta_webhook_vault_archived_event_data.workspace_id)

[](#beta_webhook_vault_archived_event_data)



BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#beta_webhook_vault_deleted_event_data.id)

organization_id: string



[](#beta_webhook_vault_deleted_event_data.organization_id)

type: "vault.deleted"



[](#beta_webhook_vault_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_vault_deleted_event_data.workspace_id)

[](#beta_webhook_vault_deleted_event_data)



BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_vault_credential_created_event_data.id)

organization_id: string



[](#beta_webhook_vault_credential_created_event_data.organization_id)

type: "vault_credential.created"



[](#beta_webhook_vault_credential_created_event_data.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_vault_credential_created_event_data.vault_id)

workspace_id: string



[](#beta_webhook_vault_credential_created_event_data.workspace_id)

[](#beta_webhook_vault_credential_created_event_data)



BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_vault_credential_archived_event_data.id)

organization_id: string



[](#beta_webhook_vault_credential_archived_event_data.organization_id)

type: "vault_credential.archived"



[](#beta_webhook_vault_credential_archived_event_data.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_vault_credential_archived_event_data.vault_id)

workspace_id: string



[](#beta_webhook_vault_credential_archived_event_data.workspace_id)

[](#beta_webhook_vault_credential_archived_event_data)



BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_vault_credential_deleted_event_data.id)

organization_id: string



[](#beta_webhook_vault_credential_deleted_event_data.organization_id)

type: "vault_credential.deleted"



[](#beta_webhook_vault_credential_deleted_event_data.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_vault_credential_deleted_event_data.vault_id)

workspace_id: string



[](#beta_webhook_vault_credential_deleted_event_data.workspace_id)

[](#beta_webhook_vault_credential_deleted_event_data)



BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_vault_credential_refresh_failed_event_data.id)

organization_id: string



[](#beta_webhook_vault_credential_refresh_failed_event_data.organization_id)

type: "vault_credential.refresh_failed"



[](#beta_webhook_vault_credential_refresh_failed_event_data.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_vault_credential_refresh_failed_event_data.vault_id)

workspace_id: string



[](#beta_webhook_vault_credential_refresh_failed_event_data.workspace_id)

[](#beta_webhook_vault_credential_refresh_failed_event_data)



BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_updated_event_data.id)

organization_id: string



[](#beta_webhook_session_updated_event_data.organization_id)

type: "session.updated"



[](#beta_webhook_session_updated_event_data.type)

workspace_id: string



[](#beta_webhook_session_updated_event_data.workspace_id)

[](#beta_webhook_session_updated_event_data)



BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_agent_created_event_data.id)

organization_id: string



[](#beta_webhook_agent_created_event_data.organization_id)

type: "agent.created"



[](#beta_webhook_agent_created_event_data.type)

workspace_id: string



[](#beta_webhook_agent_created_event_data.workspace_id)

[](#beta_webhook_agent_created_event_data)



BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_agent_archived_event_data.id)

organization_id: string



[](#beta_webhook_agent_archived_event_data.organization_id)

type: "agent.archived"



[](#beta_webhook_agent_archived_event_data.type)

workspace_id: string



[](#beta_webhook_agent_archived_event_data.workspace_id)

[](#beta_webhook_agent_archived_event_data)



BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_agent_deleted_event_data.id)

organization_id: string



[](#beta_webhook_agent_deleted_event_data.organization_id)

type: "agent.deleted"



[](#beta_webhook_agent_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_agent_deleted_event_data.workspace_id)

[](#beta_webhook_agent_deleted_event_data)



BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_paused_event_data.id)

organization_id: string



[](#beta_webhook_deployment_paused_event_data.organization_id)

type: "deployment.paused"



[](#beta_webhook_deployment_paused_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_paused_event_data.workspace_id)

[](#beta_webhook_deployment_paused_event_data)



BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#beta_webhook_deployment_run_failed_event_data.id)

organization_id: string



[](#beta_webhook_deployment_run_failed_event_data.organization_id)

type: "deployment_run.failed"



[](#beta_webhook_deployment_run_failed_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_run_failed_event_data.workspace_id)

[](#beta_webhook_deployment_run_failed_event_data)



BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_created_event_data.id)

organization_id: string



[](#beta_webhook_deployment_created_event_data.organization_id)

type: "deployment.created"



[](#beta_webhook_deployment_created_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_created_event_data.workspace_id)

[](#beta_webhook_deployment_created_event_data)



BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_updated_event_data.id)

organization_id: string



[](#beta_webhook_deployment_updated_event_data.organization_id)

type: "deployment.updated"



[](#beta_webhook_deployment_updated_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_updated_event_data.workspace_id)

[](#beta_webhook_deployment_updated_event_data)



BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_unpaused_event_data.id)

organization_id: string



[](#beta_webhook_deployment_unpaused_event_data.organization_id)

type: "deployment.unpaused"



[](#beta_webhook_deployment_unpaused_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_unpaused_event_data.workspace_id)

[](#beta_webhook_deployment_unpaused_event_data)



BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#beta_webhook_agent_updated_event_data.id)

organization_id: string



[](#beta_webhook_agent_updated_event_data.organization_id)

type: "agent.updated"



[](#beta_webhook_agent_updated_event_data.type)

workspace_id: string



[](#beta_webhook_agent_updated_event_data.workspace_id)

[](#beta_webhook_agent_updated_event_data)



BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_archived_event_data.id)

organization_id: string



[](#beta_webhook_deployment_archived_event_data.organization_id)

type: "deployment.archived"



[](#beta_webhook_deployment_archived_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_archived_event_data.workspace_id)

[](#beta_webhook_deployment_archived_event_data)



BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#beta_webhook_deployment_run_started_event_data.id)

organization_id: string



[](#beta_webhook_deployment_run_started_event_data.organization_id)

type: "deployment_run.started"



[](#beta_webhook_deployment_run_started_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_run_started_event_data.workspace_id)

[](#beta_webhook_deployment_run_started_event_data)



BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#beta_webhook_deployment_deleted_event_data.id)

organization_id: string



[](#beta_webhook_deployment_deleted_event_data.organization_id)

type: "deployment.deleted"



[](#beta_webhook_deployment_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_deleted_event_data.workspace_id)

[](#beta_webhook_deployment_deleted_event_data)



BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#beta_webhook_deployment_run_succeeded_event_data.id)

organization_id: string



[](#beta_webhook_deployment_run_succeeded_event_data.organization_id)

type: "deployment_run.succeeded"



[](#beta_webhook_deployment_run_succeeded_event_data.type)

workspace_id: string



[](#beta_webhook_deployment_run_succeeded_event_data.workspace_id)

[](#beta_webhook_deployment_run_succeeded_event_data)



BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_environment_created_event_data.id)

organization_id: string



[](#beta_webhook_environment_created_event_data.organization_id)

type: "environment.created"



[](#beta_webhook_environment_created_event_data.type)

workspace_id: string



[](#beta_webhook_environment_created_event_data.workspace_id)

[](#beta_webhook_environment_created_event_data)



BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_environment_updated_event_data.id)

organization_id: string



[](#beta_webhook_environment_updated_event_data.organization_id)

type: "environment.updated"



[](#beta_webhook_environment_updated_event_data.type)

workspace_id: string



[](#beta_webhook_environment_updated_event_data.workspace_id)

[](#beta_webhook_environment_updated_event_data)



BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_environment_archived_event_data.id)

organization_id: string



[](#beta_webhook_environment_archived_event_data.organization_id)

type: "environment.archived"



[](#beta_webhook_environment_archived_event_data.type)

workspace_id: string



[](#beta_webhook_environment_archived_event_data.workspace_id)

[](#beta_webhook_environment_archived_event_data)



BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#beta_webhook_environment_deleted_event_data.id)

organization_id: string



[](#beta_webhook_environment_deleted_event_data.organization_id)

type: "environment.deleted"



[](#beta_webhook_environment_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_environment_deleted_event_data.workspace_id)

[](#beta_webhook_environment_deleted_event_data)



BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#beta_webhook_memory_store_created_event_data.id)

organization_id: string



[](#beta_webhook_memory_store_created_event_data.organization_id)

type: "memory_store.created"



[](#beta_webhook_memory_store_created_event_data.type)

workspace_id: string



[](#beta_webhook_memory_store_created_event_data.workspace_id)

[](#beta_webhook_memory_store_created_event_data)



BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#beta_webhook_memory_store_archived_event_data.id)

organization_id: string



[](#beta_webhook_memory_store_archived_event_data.organization_id)

type: "memory_store.archived"



[](#beta_webhook_memory_store_archived_event_data.type)

workspace_id: string



[](#beta_webhook_memory_store_archived_event_data.workspace_id)

[](#beta_webhook_memory_store_archived_event_data)



BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#beta_webhook_memory_store_deleted_event_data.id)

organization_id: string



[](#beta_webhook_memory_store_deleted_event_data.organization_id)

type: "memory_store.deleted"



[](#beta_webhook_memory_store_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_memory_store_deleted_event_data.workspace_id)

[](#beta_webhook_memory_store_deleted_event_data)

[](#beta_webhook_event_data)



BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#beta_webhook_memory_store_archived_event_data.id)

organization_id: string



[](#beta_webhook_memory_store_archived_event_data.organization_id)

type: "memory_store.archived"



[](#beta_webhook_memory_store_archived_event_data.type)

workspace_id: string



[](#beta_webhook_memory_store_archived_event_data.workspace_id)

[](#beta_webhook_memory_store_archived_event_data)



BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#beta_webhook_memory_store_created_event_data.id)

organization_id: string



[](#beta_webhook_memory_store_created_event_data.organization_id)

type: "memory_store.created"



[](#beta_webhook_memory_store_created_event_data.type)

workspace_id: string



[](#beta_webhook_memory_store_created_event_data.workspace_id)

[](#beta_webhook_memory_store_created_event_data)



BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#beta_webhook_memory_store_deleted_event_data.id)

organization_id: string



[](#beta_webhook_memory_store_deleted_event_data.organization_id)

type: "memory_store.deleted"



[](#beta_webhook_memory_store_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_memory_store_deleted_event_data.workspace_id)

[](#beta_webhook_memory_store_deleted_event_data)



BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_archived_event_data.id)

organization_id: string



[](#beta_webhook_session_archived_event_data.organization_id)

type: "session.archived"



[](#beta_webhook_session_archived_event_data.type)

workspace_id: string



[](#beta_webhook_session_archived_event_data.workspace_id)

[](#beta_webhook_session_archived_event_data)



BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_created_event_data.id)

organization_id: string



[](#beta_webhook_session_created_event_data.organization_id)

type: "session.created"



[](#beta_webhook_session_created_event_data.type)

workspace_id: string



[](#beta_webhook_session_created_event_data.workspace_id)

[](#beta_webhook_session_created_event_data)



BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_deleted_event_data.id)

organization_id: string



[](#beta_webhook_session_deleted_event_data.organization_id)

type: "session.deleted"



[](#beta_webhook_session_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_session_deleted_event_data.workspace_id)

[](#beta_webhook_session_deleted_event_data)



BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_idled_event_data.id)

organization_id: string



[](#beta_webhook_session_idled_event_data.organization_id)

type: "session.idled"



[](#beta_webhook_session_idled_event_data.type)

workspace_id: string



[](#beta_webhook_session_idled_event_data.workspace_id)

[](#beta_webhook_session_idled_event_data)



BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_outcome_evaluation_ended_event_data.id)

organization_id: string



[](#beta_webhook_session_outcome_evaluation_ended_event_data.organization_id)

type: "session.outcome_evaluation_ended"



[](#beta_webhook_session_outcome_evaluation_ended_event_data.type)

workspace_id: string



[](#beta_webhook_session_outcome_evaluation_ended_event_data.workspace_id)

[](#beta_webhook_session_outcome_evaluation_ended_event_data)



BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_pending_event_data.id)

organization_id: string



[](#beta_webhook_session_pending_event_data.organization_id)

type: "session.pending"



[](#beta_webhook_session_pending_event_data.type)

workspace_id: string



[](#beta_webhook_session_pending_event_data.workspace_id)

[](#beta_webhook_session_pending_event_data)



BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_requires_action_event_data.id)

organization_id: string



[](#beta_webhook_session_requires_action_event_data.organization_id)

type: "session.requires_action"



[](#beta_webhook_session_requires_action_event_data.type)

workspace_id: string



[](#beta_webhook_session_requires_action_event_data.workspace_id)

[](#beta_webhook_session_requires_action_event_data)



BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_running_event_data.id)

organization_id: string



[](#beta_webhook_session_running_event_data.organization_id)

type: "session.running"



[](#beta_webhook_session_running_event_data.type)

workspace_id: string



[](#beta_webhook_session_running_event_data.workspace_id)

[](#beta_webhook_session_running_event_data)



BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_status_idled_event_data.id)

organization_id: string



[](#beta_webhook_session_status_idled_event_data.organization_id)

type: "session.status_idled"



[](#beta_webhook_session_status_idled_event_data.type)

workspace_id: string



[](#beta_webhook_session_status_idled_event_data.workspace_id)

[](#beta_webhook_session_status_idled_event_data)



BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_status_rescheduled_event_data.id)

organization_id: string



[](#beta_webhook_session_status_rescheduled_event_data.organization_id)

type: "session.status_rescheduled"



[](#beta_webhook_session_status_rescheduled_event_data.type)

workspace_id: string



[](#beta_webhook_session_status_rescheduled_event_data.workspace_id)

[](#beta_webhook_session_status_rescheduled_event_data)



BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_status_run_started_event_data.id)

organization_id: string



[](#beta_webhook_session_status_run_started_event_data.organization_id)

type: "session.status_run_started"



[](#beta_webhook_session_status_run_started_event_data.type)

workspace_id: string



[](#beta_webhook_session_status_run_started_event_data.workspace_id)

[](#beta_webhook_session_status_run_started_event_data)



BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_status_terminated_event_data.id)

organization_id: string



[](#beta_webhook_session_status_terminated_event_data.organization_id)

type: "session.status_terminated"



[](#beta_webhook_session_status_terminated_event_data.type)

workspace_id: string



[](#beta_webhook_session_status_terminated_event_data.workspace_id)

[](#beta_webhook_session_status_terminated_event_data)



BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_thread_created_event_data.id)

organization_id: string



[](#beta_webhook_session_thread_created_event_data.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#beta_webhook_session_thread_created_event_data.session_thread_id)

type: "session.thread_created"



[](#beta_webhook_session_thread_created_event_data.type)

workspace_id: string



[](#beta_webhook_session_thread_created_event_data.workspace_id)

[](#beta_webhook_session_thread_created_event_data)



BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_thread_idled_event_data.id)

organization_id: string



[](#beta_webhook_session_thread_idled_event_data.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#beta_webhook_session_thread_idled_event_data.session_thread_id)

type: "session.thread_idled"



[](#beta_webhook_session_thread_idled_event_data.type)

workspace_id: string



[](#beta_webhook_session_thread_idled_event_data.workspace_id)

[](#beta_webhook_session_thread_idled_event_data)



BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_thread_terminated_event_data.id)

organization_id: string



[](#beta_webhook_session_thread_terminated_event_data.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#beta_webhook_session_thread_terminated_event_data.session_thread_id)

type: "session.thread_terminated"



[](#beta_webhook_session_thread_terminated_event_data.type)

workspace_id: string



[](#beta_webhook_session_thread_terminated_event_data.workspace_id)

[](#beta_webhook_session_thread_terminated_event_data)



BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#beta_webhook_session_updated_event_data.id)

organization_id: string



[](#beta_webhook_session_updated_event_data.organization_id)

type: "session.updated"



[](#beta_webhook_session_updated_event_data.type)

workspace_id: string



[](#beta_webhook_session_updated_event_data.workspace_id)

[](#beta_webhook_session_updated_event_data)



BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#beta_webhook_vault_archived_event_data.id)

organization_id: string



[](#beta_webhook_vault_archived_event_data.organization_id)

type: "vault.archived"



[](#beta_webhook_vault_archived_event_data.type)

workspace_id: string



[](#beta_webhook_vault_archived_event_data.workspace_id)

[](#beta_webhook_vault_archived_event_data)



BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#beta_webhook_vault_created_event_data.id)

organization_id: string



[](#beta_webhook_vault_created_event_data.organization_id)

type: "vault.created"



[](#beta_webhook_vault_created_event_data.type)

workspace_id: string



[](#beta_webhook_vault_created_event_data.workspace_id)

[](#beta_webhook_vault_created_event_data)



BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_vault_credential_archived_event_data.id)

organization_id: string



[](#beta_webhook_vault_credential_archived_event_data.organization_id)

type: "vault_credential.archived"



[](#beta_webhook_vault_credential_archived_event_data.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_vault_credential_archived_event_data.vault_id)

workspace_id: string



[](#beta_webhook_vault_credential_archived_event_data.workspace_id)

[](#beta_webhook_vault_credential_archived_event_data)



BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_vault_credential_created_event_data.id)

organization_id: string



[](#beta_webhook_vault_credential_created_event_data.organization_id)

type: "vault_credential.created"



[](#beta_webhook_vault_credential_created_event_data.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_vault_credential_created_event_data.vault_id)

workspace_id: string



[](#beta_webhook_vault_credential_created_event_data.workspace_id)

[](#beta_webhook_vault_credential_created_event_data)



BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_vault_credential_deleted_event_data.id)

organization_id: string



[](#beta_webhook_vault_credential_deleted_event_data.organization_id)

type: "vault_credential.deleted"



[](#beta_webhook_vault_credential_deleted_event_data.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_vault_credential_deleted_event_data.vault_id)

workspace_id: string



[](#beta_webhook_vault_credential_deleted_event_data.workspace_id)

[](#beta_webhook_vault_credential_deleted_event_data)



BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#beta_webhook_vault_credential_refresh_failed_event_data.id)

organization_id: string



[](#beta_webhook_vault_credential_refresh_failed_event_data.organization_id)

type: "vault_credential.refresh_failed"



[](#beta_webhook_vault_credential_refresh_failed_event_data.type)

vault_id: string



ID of the vault that owns this credential.

[](#beta_webhook_vault_credential_refresh_failed_event_data.vault_id)

workspace_id: string



[](#beta_webhook_vault_credential_refresh_failed_event_data.workspace_id)

[](#beta_webhook_vault_credential_refresh_failed_event_data)



BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#beta_webhook_vault_deleted_event_data.id)

organization_id: string



[](#beta_webhook_vault_deleted_event_data.organization_id)

type: "vault.deleted"



[](#beta_webhook_vault_deleted_event_data.type)

workspace_id: string



[](#beta_webhook_vault_deleted_event_data.workspace_id)

[](#beta_webhook_vault_deleted_event_data)



UnwrapWebhookEvent object { id, created_at, data, type }



id: string



Unique event identifier for idempotency.

[](#unwrap_webhook_event.id)

created_at: string



RFC 3339 timestamp when the event occurred.

[](#unwrap_webhook_event.created_at)



data: [BetaWebhookEventData](/docs/en/api/beta/webhooks#beta_webhook_event_data)



One of the following:



BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.created"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.pending"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.running"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.idled"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.requires_action"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.archived"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.deleted"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.status_rescheduled"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.status_run_started"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.status_idled"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.status_terminated"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.session_thread_id)

type: "session.thread_created"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.session_thread_id)

type: "session.thread_idled"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

session_thread_id: string



ID of the session thread this event refers to.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.session_thread_id)

type: "session.thread_terminated"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.outcome_evaluation_ended"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault.created"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault.archived"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault.deleted"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault_credential.created"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

vault_id: string



ID of the vault that owns this credential.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.vault_id)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault_credential.archived"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

vault_id: string



ID of the vault that owns this credential.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.vault_id)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault_credential.deleted"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

vault_id: string



ID of the vault that owns this credential.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.vault_id)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "vault_credential.refresh_failed"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

vault_id: string



ID of the vault that owns this credential.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.vault_id)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "session.updated"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "agent.created"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "agent.archived"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "agent.deleted"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.paused"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment_run.failed"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.created"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.updated"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.unpaused"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "agent.updated"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.archived"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment_run.started"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment.deleted"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "deployment_run.succeeded"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "environment.created"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "environment.updated"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "environment.archived"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "environment.deleted"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "memory_store.created"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "memory_store.archived"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)



BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.id)

organization_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.organization_id)

type: "memory_store.deleted"



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.type)

workspace_id: string



[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks.workspace_id)

[](#unwrap_webhook_event.data%20%2B%20(resource)%20beta.webhooks)

[](#unwrap_webhook_event.data)

type: "event"



Object type. Always `event` for webhook payloads.

[](#unwrap_webhook_event.type)
