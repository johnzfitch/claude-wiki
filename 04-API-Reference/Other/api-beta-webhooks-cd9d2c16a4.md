---
title: "Webhooks - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/webhooks"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:00Z"
tags: ["api", "hooks"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fwebhooks)

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

# Webhooks

##### Models



BetaWebhookAgentArchivedEventData object{ type: "agent.archived", id, organization_id, workspace_id }



type: "agent.archived"



id: string



ID of the agent that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookAgentCreatedEventData object{ type: "agent.created", id, organization_id, workspace_id }



type: "agent.created"



id: string



ID of the agent that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookAgentDeletedEventData object{ type: "agent.deleted", id, organization_id, workspace_id }



type: "agent.deleted"



id: string



ID of the agent that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookAgentUpdatedEventData object{ type: "agent.updated", id, organization_id, workspace_id }



type: "agent.updated"



id: string



ID of the agent that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookDeploymentArchivedEventData object{ type: "deployment.archived", id, organization_id, workspace_id }



type: "deployment.archived"



id: string



ID of the deployment that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookDeploymentCreatedEventData object{ type: "deployment.created", id, organization_id, workspace_id }



type: "deployment.created"



id: string



ID of the deployment that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookDeploymentDeletedEventData object{ type: "deployment.deleted", id, organization_id, workspace_id }



type: "deployment.deleted"



id: string



ID of the deployment that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookDeploymentPausedEventData object{ type: "deployment.paused", id, organization_id, workspace_id }



type: "deployment.paused"



id: string



ID of the deployment that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookDeploymentRunFailedEventData object{ type: "deployment_run.failed", id, organization_id, workspace_id }



type: "deployment_run.failed"



id: string



ID of the deployment run that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookDeploymentRunStartedEventData object{ type: "deployment_run.started", id, organization_id, workspace_id }



type: "deployment_run.started"



id: string



ID of the deployment run that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookDeploymentRunSucceededEventData object{ type: "deployment_run.succeeded", id, organization_id, workspace_id }



type: "deployment_run.succeeded"



id: string



ID of the deployment run that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookDeploymentUnpausedEventData object{ type: "deployment.unpaused", id, organization_id, workspace_id }



type: "deployment.unpaused"



id: string



ID of the deployment that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookDeploymentUpdatedEventData object{ type: "deployment.updated", id, organization_id, workspace_id }



type: "deployment.updated"



id: string



ID of the deployment that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookEnvironmentArchivedEventData object{ type: "environment.archived", id, organization_id, workspace_id }



type: "environment.archived"



id: string



ID of the environment that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookEnvironmentCreatedEventData object{ type: "environment.created", id, organization_id, workspace_id }



type: "environment.created"



id: string



ID of the environment that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookEnvironmentDeletedEventData object{ type: "environment.deleted", id, organization_id, workspace_id }



type: "environment.deleted"



id: string



ID of the environment that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookEnvironmentUpdatedEventData object{ type: "environment.updated", id, organization_id, workspace_id }



type: "environment.updated"



id: string



ID of the environment that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookEvent object{ type: "event", id, created_at, data }



type: "event"



Object type. Always `event` for webhook payloads.

id: string



Unique event identifier for idempotency.



created_at: string



RFC 3339 timestamp when the event occurred.

formatdate-time



data: [BetaWebhookEventData](/docs/en/api/http/beta/webhooks#beta_webhook_event_data)



One of the following:



BetaWebhookEventData = [BetaWebhookSessionCreatedEventData](/docs/en/api/http/beta/webhooks#beta_webhook_session_created_event_data) or [BetaWebhookSessionPendingEventData](/docs/en/api/http/beta/webhooks#beta_webhook_session_pending_event_data) or [BetaWebhookSessionRunningEventData](/docs/en/api/http/beta/webhooks#beta_webhook_session_running_event_data) or 41 more



One of the following:



BetaWebhookMemoryStoreArchivedEventData object{ type: "memory_store.archived", id, organization_id, workspace_id }



type: "memory_store.archived"



id: string



ID of the memory store that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookMemoryStoreCreatedEventData object{ type: "memory_store.created", id, organization_id, workspace_id }



type: "memory_store.created"



id: string



ID of the memory store that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookMemoryStoreDeletedEventData object{ type: "memory_store.deleted", id, organization_id, workspace_id }



type: "memory_store.deleted"



id: string



ID of the memory store that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionArchivedEventData object{ type: "session.archived", id, organization_id, workspace_id }



type: "session.archived"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionBudgetReachedEventData object{ type: "session.budget_reached", id, organization_id, workspace_id }



type: "session.budget_reached"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionCreatedEventData object{ type: "session.created", id, organization_id, workspace_id }



type: "session.created"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionDeletedEventData object{ type: "session.deleted", id, organization_id, workspace_id }



type: "session.deleted"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionIdledEventData object{ type: "session.idled", id, organization_id, workspace_id }



type: "session.idled"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionOutcomeEvaluationEndedEventData object{ type: "session.outcome_evaluation_ended", id, organization_id, workspace_id }



type: "session.outcome_evaluation_ended"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionPendingEventData object{ type: "session.pending", id, organization_id, workspace_id }



type: "session.pending"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionRequiresActionEventData object{ type: "session.requires_action", id, organization_id, workspace_id }



type: "session.requires_action"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionRunningEventData object{ type: "session.running", id, organization_id, workspace_id }



type: "session.running"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionStatusIdledEventData object{ type: "session.status_idled", id, organization_id, workspace_id }



type: "session.status_idled"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionStatusRescheduledEventData object{ type: "session.status_rescheduled", id, organization_id, workspace_id }



type: "session.status_rescheduled"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionStatusRunStartedEventData object{ type: "session.status_run_started", id, organization_id, workspace_id }



type: "session.status_run_started"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionStatusTerminatedEventData object{ type: "session.status_terminated", id, organization_id, workspace_id }



type: "session.status_terminated"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookSessionThreadCreatedEventData object{ type: "session.thread_created", id, organization_id, 2 more }



type: "session.thread_created"



id: string



ID of the session that triggered the event.

organization_id: string



session_thread_id: string



ID of the session thread this event refers to.

workspace_id: string





BetaWebhookSessionThreadIdledEventData object{ type: "session.thread_idled", id, organization_id, 2 more }



type: "session.thread_idled"



id: string



ID of the session that triggered the event.

organization_id: string



session_thread_id: string



ID of the session thread this event refers to.

workspace_id: string





BetaWebhookSessionThreadTerminatedEventData object{ type: "session.thread_terminated", id, organization_id, 2 more }



type: "session.thread_terminated"



id: string



ID of the session that triggered the event.

organization_id: string



session_thread_id: string



ID of the session thread this event refers to.

workspace_id: string





BetaWebhookSessionUpdatedEventData object{ type: "session.updated", id, organization_id, workspace_id }



type: "session.updated"



id: string



ID of the session that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookVaultArchivedEventData object{ type: "vault.archived", id, organization_id, workspace_id }



type: "vault.archived"



id: string



ID of the vault that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookVaultCreatedEventData object{ type: "vault.created", id, organization_id, workspace_id }



type: "vault.created"



id: string



ID of the vault that triggered the event.

organization_id: string



workspace_id: string





BetaWebhookVaultCredentialArchivedEventData object{ type: "vault_credential.archived", id, organization_id, 2 more }



type: "vault_credential.archived"



id: string



ID of the vault credential that triggered the event.

organization_id: string



vault_id: string



ID of the vault that owns this credential.

workspace_id: string





BetaWebhookVaultCredentialCreatedEventData object{ type: "vault_credential.created", id, organization_id, 2 more }



type: "vault_credential.created"



id: string



ID of the vault credential that triggered the event.

organization_id: string



vault_id: string



ID of the vault that owns this credential.

workspace_id: string





BetaWebhookVaultCredentialDeletedEventData object{ type: "vault_credential.deleted", id, organization_id, 2 more }



type: "vault_credential.deleted"



id: string



ID of the vault credential that triggered the event.

organization_id: string



vault_id: string



ID of the vault that owns this credential.

workspace_id: string





BetaWebhookVaultCredentialRefreshFailedEventData object{ type: "vault_credential.refresh_failed", id, organization_id, 2 more }



type: "vault_credential.refresh_failed"



id: string



ID of the vault credential that triggered the event.

organization_id: string



vault_id: string



ID of the vault that owns this credential.

workspace_id: string





BetaWebhookVaultDeletedEventData object{ type: "vault.deleted", id, organization_id, workspace_id }



type: "vault.deleted"



id: string



ID of the vault that triggered the event.
