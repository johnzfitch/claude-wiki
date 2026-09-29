---
title: "Webhooks - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/webhooks"
category: "04-API-Reference/Other"
fetched_at: "2026-09-10T06:42:24Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Fwebhooks)

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


Webhooks


Unwrap


Parse Unverified


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

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

##### [Unwrap](/docs/en/api/http/beta/webhooks/unwrap)

Function

##### [Parse Unverified](/docs/en/api/http/beta/webhooks/parse_unverified)

Function

##### Models



BetaWebhookAgentArchivedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

organization_id: string



type: "agent.archived"



workspace_id: string





BetaWebhookAgentCreatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

organization_id: string



type: "agent.created"



workspace_id: string





BetaWebhookAgentDeletedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

organization_id: string



type: "agent.deleted"



workspace_id: string





BetaWebhookAgentUpdatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the agent that triggered the event.

organization_id: string



type: "agent.updated"



workspace_id: string





BetaWebhookDeploymentArchivedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

organization_id: string



type: "deployment.archived"



workspace_id: string





BetaWebhookDeploymentCreatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

organization_id: string



type: "deployment.created"



workspace_id: string





BetaWebhookDeploymentDeletedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

organization_id: string



type: "deployment.deleted"



workspace_id: string





BetaWebhookDeploymentPausedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

organization_id: string



type: "deployment.paused"



workspace_id: string





BetaWebhookDeploymentRunFailedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

organization_id: string



type: "deployment_run.failed"



workspace_id: string





BetaWebhookDeploymentRunStartedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

organization_id: string



type: "deployment_run.started"



workspace_id: string





BetaWebhookDeploymentRunSucceededEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the deployment run that triggered the event.

organization_id: string



type: "deployment_run.succeeded"



workspace_id: string





BetaWebhookDeploymentUnpausedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

organization_id: string



type: "deployment.unpaused"



workspace_id: string





BetaWebhookDeploymentUpdatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the deployment that triggered the event.

organization_id: string



type: "deployment.updated"



workspace_id: string





BetaWebhookEnvironmentArchivedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

organization_id: string



type: "environment.archived"



workspace_id: string





BetaWebhookEnvironmentCreatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

organization_id: string



type: "environment.created"



workspace_id: string





BetaWebhookEnvironmentDeletedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

organization_id: string



type: "environment.deleted"



workspace_id: string





BetaWebhookEnvironmentUpdatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the environment that triggered the event.

organization_id: string



type: "environment.updated"



workspace_id: string





BetaWebhookEvent object{ id, created_at, data, type }



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

type: "event"



Object type. Always `event` for webhook payloads.



BetaWebhookEventData = [BetaWebhookSessionCreatedEventData](/docs/en/api/http/beta/webhooks#beta_webhook_session_created_event_data) { id, organization_id, type, workspace_id } or [BetaWebhookSessionPendingEventData](/docs/en/api/http/beta/webhooks#beta_webhook_session_pending_event_data) { id, organization_id, type, workspace_id } or [BetaWebhookSessionRunningEventData](/docs/en/api/http/beta/webhooks#beta_webhook_session_running_event_data) { id, organization_id, type, workspace_id } or 41 more



One of the following:



BetaWebhookMemoryStoreArchivedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

organization_id: string



type: "memory_store.archived"



workspace_id: string





BetaWebhookMemoryStoreCreatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

organization_id: string



type: "memory_store.created"



workspace_id: string





BetaWebhookMemoryStoreDeletedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the memory store that triggered the event.

organization_id: string



type: "memory_store.deleted"



workspace_id: string





BetaWebhookSessionArchivedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.archived"



workspace_id: string





BetaWebhookSessionBudgetReachedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.budget_reached"



workspace_id: string





BetaWebhookSessionCreatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.created"



workspace_id: string





BetaWebhookSessionDeletedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.deleted"



workspace_id: string





BetaWebhookSessionIdledEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.idled"



workspace_id: string





BetaWebhookSessionOutcomeEvaluationEndedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.outcome_evaluation_ended"



workspace_id: string





BetaWebhookSessionPendingEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.pending"



workspace_id: string





BetaWebhookSessionRequiresActionEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.requires_action"



workspace_id: string





BetaWebhookSessionRunningEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.running"



workspace_id: string





BetaWebhookSessionStatusIdledEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.status_idled"



workspace_id: string





BetaWebhookSessionStatusRescheduledEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.status_rescheduled"



workspace_id: string





BetaWebhookSessionStatusRunStartedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.status_run_started"



workspace_id: string





BetaWebhookSessionStatusTerminatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.status_terminated"



workspace_id: string





BetaWebhookSessionThreadCreatedEventData object{ id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

organization_id: string



session_thread_id: string



ID of the session thread this event refers to.

type: "session.thread_created"



workspace_id: string





BetaWebhookSessionThreadIdledEventData object{ id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

organization_id: string



session_thread_id: string



ID of the session thread this event refers to.

type: "session.thread_idled"



workspace_id: string





BetaWebhookSessionThreadTerminatedEventData object{ id, organization_id, session_thread_id, 2 more }



id: string



ID of the session that triggered the event.

organization_id: string



session_thread_id: string



ID of the session thread this event refers to.

type: "session.thread_terminated"



workspace_id: string





BetaWebhookSessionUpdatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the session that triggered the event.

organization_id: string



type: "session.updated"



workspace_id: string





BetaWebhookVaultArchivedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

organization_id: string



type: "vault.archived"



workspace_id: string





BetaWebhookVaultCreatedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

organization_id: string



type: "vault.created"



workspace_id: string





BetaWebhookVaultCredentialArchivedEventData object{ id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

organization_id: string



type: "vault_credential.archived"



vault_id: string



ID of the vault that owns this credential.

workspace_id: string





BetaWebhookVaultCredentialCreatedEventData object{ id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

organization_id: string



type: "vault_credential.created"



vault_id: string



ID of the vault that owns this credential.

workspace_id: string





BetaWebhookVaultCredentialDeletedEventData object{ id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

organization_id: string



type: "vault_credential.deleted"



vault_id: string



ID of the vault that owns this credential.

workspace_id: string





BetaWebhookVaultCredentialRefreshFailedEventData object{ id, organization_id, type, 2 more }



id: string



ID of the vault credential that triggered the event.

organization_id: string



type: "vault_credential.refresh_failed"



vault_id: string



ID of the vault that owns this credential.

workspace_id: string





BetaWebhookVaultDeletedEventData object{ id, organization_id, type, workspace_id }



id: string



ID of the vault that triggered the event.

organization_id: string



type: "vault.deleted"
