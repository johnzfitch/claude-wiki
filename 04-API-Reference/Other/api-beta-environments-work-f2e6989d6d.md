---
title: "Work - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/environments/work"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:33Z"
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


Create Environment


List Environments


Get Environment


Update Environment


Delete Environment


Archive Environment

Work


Get Work Item


Poll for Work


Acknowledge Work


Record Heartbeat


Stop Work


List Work Items


Update Work Item


Get Queue Statistics

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

Work




cURL

# Work

##### [Get Work Item](/docs/en/api/beta/environments/work/retrieve)

GET/v1/environments/{environment_id}/work/{work_id}

##### [Poll for Work](/docs/en/api/beta/environments/work/poll)

GET/v1/environments/{environment_id}/work/poll

##### [Acknowledge Work](/docs/en/api/beta/environments/work/ack)

POST/v1/environments/{environment_id}/work/{work_id}/ack

##### [Record Heartbeat](/docs/en/api/beta/environments/work/heartbeat)

POST/v1/environments/{environment_id}/work/{work_id}/heartbeat

##### [Stop Work](/docs/en/api/beta/environments/work/stop)

POST/v1/environments/{environment_id}/work/{work_id}/stop

##### [List Work Items](/docs/en/api/beta/environments/work/list)

GET/v1/environments/{environment_id}/work

##### [Update Work Item](/docs/en/api/beta/environments/work/update)

POST/v1/environments/{environment_id}/work/{work_id}

##### [Get Queue Statistics](/docs/en/api/beta/environments/work/stats)

GET/v1/environments/{environment_id}/work/stats

##### ModelsExpand Collapse 



BetaSelfHostedWork object { id, acknowledged_at, created_at, 10 more }



Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions receive new messages. The environment worker polls for work to execute in a self-hosted sandbox.

id: string



Work identifier (e.g., 'work\_...')

[](#beta_self_hosted_work.id)

acknowledged_at: string



RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

[](#beta_self_hosted_work.acknowledged_at)

created_at: string



RFC 3339 timestamp when work was created

[](#beta_self_hosted_work.created_at)



data: [BetaSessionWorkData](/docs/en/api/beta/environments/work#beta_session_work_data) { id, type }



The actual work to be performed

id: string



Session identifier (e.g., 'session\_...')

[](#beta_self_hosted_work.data%20%2B%20(resource)%20beta.environments.work.id)

type: "session"



Type of work data

[](#beta_self_hosted_work.data%20%2B%20(resource)%20beta.environments.work.type)

[](#beta_self_hosted_work.data)

environment_id: string



Environment identifier this work belongs to (e.g., `env_...`)

[](#beta_self_hosted_work.environment_id)

latest_heartbeat_at: string



RFC 3339 timestamp of the most recent heartbeat

[](#beta_self_hosted_work.latest_heartbeat_at)

metadata: map\[string\]



User-provided metadata key-value pairs associated with this work item

[](#beta_self_hosted_work.metadata)

secret: string



Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

[](#beta_self_hosted_work.secret)

started_at: string



RFC 3339 timestamp when work execution started

[](#beta_self_hosted_work.started_at)



state: "queued" or "starting" or "active" or 2 more



Current state of the work item

One of the following:

"queued"



[](#beta_self_hosted_work.state%5B0%5D)

"starting"



[](#beta_self_hosted_work.state%5B1%5D)

"active"



[](#beta_self_hosted_work.state%5B2%5D)

"stopping"



[](#beta_self_hosted_work.state%5B3%5D)

"stopped"



[](#beta_self_hosted_work.state%5B4%5D)

[](#beta_self_hosted_work.state)

stop_requested_at: string



RFC 3339 timestamp when stop was requested

[](#beta_self_hosted_work.stop_requested_at)

stopped_at: string



RFC 3339 timestamp when work execution stopped

[](#beta_self_hosted_work.stopped_at)

type: "work"



The type of object (always 'work')

[](#beta_self_hosted_work.type)

[](#beta_self_hosted_work)



BetaSelfHostedWorkHeartbeatResponse object { last_heartbeat, lease_extended, state, 2 more }



Response after recording a heartbeat for a work item.

last_heartbeat: string



RFC 3339 timestamp of the actual heartbeat from DB

[](#beta_self_hosted_work_heartbeat_response.last_heartbeat)

lease_extended: boolean



Whether the heartbeat succeeded in extending the lease

[](#beta_self_hosted_work_heartbeat_response.lease_extended)



state: "queued" or "starting" or "active" or 2 more



Current state of the work item (active/stopping/stopped)

One of the following:

"queued"



[](#beta_self_hosted_work_heartbeat_response.state%5B0%5D)

"starting"



[](#beta_self_hosted_work_heartbeat_response.state%5B1%5D)

"active"



[](#beta_self_hosted_work_heartbeat_response.state%5B2%5D)

"stopping"



[](#beta_self_hosted_work_heartbeat_response.state%5B3%5D)

"stopped"



[](#beta_self_hosted_work_heartbeat_response.state%5B4%5D)

[](#beta_self_hosted_work_heartbeat_response.state)

ttl_seconds: number



Effective TTL applied to the lease

[](#beta_self_hosted_work_heartbeat_response.ttl_seconds)

type: "work_heartbeat"



The type of response

[](#beta_self_hosted_work_heartbeat_response.type)

[](#beta_self_hosted_work_heartbeat_response)



BetaSelfHostedWorkListResponse object { data, next_page }



Response when listing work items with cursor-based pagination.



data: array of [BetaSelfHostedWork](/docs/en/api/beta/environments/work#beta_self_hosted_work) { id, acknowledged_at, created_at, 10 more }



List of work items

id: string



Work identifier (e.g., 'work\_...')

[](#beta_self_hosted_work.id)

acknowledged_at: string



RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

[](#beta_self_hosted_work.acknowledged_at)

created_at: string



RFC 3339 timestamp when work was created

[](#beta_self_hosted_work.created_at)



data: [BetaSessionWorkData](/docs/en/api/beta/environments/work#beta_session_work_data) { id, type }



The actual work to be performed

id: string



Session identifier (e.g., 'session\_...')

[](#beta_self_hosted_work.data%20%2B%20(resource)%20beta.environments.work.id)

type: "session"



Type of work data

[](#beta_self_hosted_work.data%20%2B%20(resource)%20beta.environments.work.type)

[](#beta_self_hosted_work.data)

environment_id: string



Environment identifier this work belongs to (e.g., `env_...`)

[](#beta_self_hosted_work.environment_id)

latest_heartbeat_at: string



RFC 3339 timestamp of the most recent heartbeat

[](#beta_self_hosted_work.latest_heartbeat_at)

metadata: map\[string\]



User-provided metadata key-value pairs associated with this work item

[](#beta_self_hosted_work.metadata)

secret: string



Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

[](#beta_self_hosted_work.secret)

started_at: string



RFC 3339 timestamp when work execution started

[](#beta_self_hosted_work.started_at)



state: "queued" or "starting" or "active" or 2 more



Current state of the work item

One of the following:

"queued"



[](#beta_self_hosted_work.state%5B0%5D)

"starting"



[](#beta_self_hosted_work.state%5B1%5D)

"active"



[](#beta_self_hosted_work.state%5B2%5D)

"stopping"



[](#beta_self_hosted_work.state%5B3%5D)

"stopped"



[](#beta_self_hosted_work.state%5B4%5D)

[](#beta_self_hosted_work.state)

stop_requested_at: string



RFC 3339 timestamp when stop was requested

[](#beta_self_hosted_work.stop_requested_at)

stopped_at: string



RFC 3339 timestamp when work execution stopped

[](#beta_self_hosted_work.stopped_at)

type: "work"



The type of object (always 'work')

[](#beta_self_hosted_work.type)

[](#beta_self_hosted_work_list_response.data)

next_page: string



Opaque cursor for fetching the next page of results

[](#beta_self_hosted_work_list_response.next_page)

[](#beta_self_hosted_work_list_response)



BetaSelfHostedWorkQueueStats object { depth, oldest_queued_at, pending, 2 more }



Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

depth: number



Number of work items waiting to be picked up (lag from consumer group)

[](#beta_self_hosted_work_queue_stats.depth)

oldest_queued_at: string



RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

[](#beta_self_hosted_work_queue_stats.oldest_queued_at)

pending: number



Number of work items being processed (polled but not acknowledged)

[](#beta_self_hosted_work_queue_stats.pending)

type: "work_queue_stats"



The type of object

[](#beta_self_hosted_work_queue_stats.type)

workers_polling: number



Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

[](#beta_self_hosted_work_queue_stats.workers_polling)

[](#beta_self_hosted_work_queue_stats)



BetaSelfHostedWorkStopRequest object { force }



Request to stop a work item.

force: optional boolean



If true, immediately stop work without graceful shutdown

[](#beta_self_hosted_work_stop_request.force)

[](#beta_self_hosted_work_stop_request)



BetaSelfHostedWorkUpdateRequest object { metadata }



Request to update work item metadata.

metadata: map\[string\]



Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

[](#beta_self_hosted_work_update_request.metadata)

[](#beta_self_hosted_work_update_request)



BetaSessionWorkData object { id, type }



Work data for session work items.

This resource type is used when work represents a session that needs to be executed in a self-hosted environment.

id: string



Session identifier (e.g., 'session\_...')

[](#beta_session_work_data.id)

type: "session"



Type of work data

[](#beta_session_work_data.type)
