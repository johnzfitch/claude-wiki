---
title: "Work - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/environments/work"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:26Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fenvironments%2Fwork)

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


Create Environment


List Environments


Get Environment


Update Environment


Delete Environment


Archive Environment

Work


Get Work Item


Poll for Work


Acknowledge Work


Record Heartbeat


Stop Work


List Work Items


Update Work Item


Get Queue Statistics

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

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](http-beta.md)
3.  [Environments](https://platform.claude.com/docs/en/api/http/beta/environments)

# Work

##### [Get Work Item](https://platform.claude.com/docs/en/api/http/beta/environments/work/retrieve)

GET/v1/environments/{environment_id}/work/{work_id}

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Poll for Work](https://platform.claude.com/docs/en/api/http/beta/environments/work/poll)

GET/v1/environments/{environment_id}/work/poll

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Acknowledge Work](https://platform.claude.com/docs/en/api/http/beta/environments/work/ack)

POST/v1/environments/{environment_id}/work/{work_id}/ack

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Record Heartbeat](https://platform.claude.com/docs/en/api/http/beta/environments/work/heartbeat)

POST/v1/environments/{environment_id}/work/{work_id}/heartbeat

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Stop Work](https://platform.claude.com/docs/en/api/http/beta/environments/work/stop)

POST/v1/environments/{environment_id}/work/{work_id}/stop

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [List Work Items](https://platform.claude.com/docs/en/api/http/beta/environments/work/list)

GET/v1/environments/{environment_id}/work

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Update Work Item](https://platform.claude.com/docs/en/api/http/beta/environments/work/update)

POST/v1/environments/{environment_id}/work/{work_id}

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Get Queue Statistics](https://platform.claude.com/docs/en/api/http/beta/environments/work/stats)

GET/v1/environments/{environment_id}/work/stats

Get statistics about the work queue for an environment.

##### Models



BetaSelfHostedWork object{ type: "work", id, acknowledged_at, 10 more }



Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions receive new messages. The environment worker polls for work to execute in a self-hosted sandbox.



BetaSelfHostedWorkHeartbeatResponse object{ type: "work_heartbeat", last_heartbeat, lease_extended, 2 more }



Response after recording a heartbeat for a work item.



type: "work_heartbeat"



The type of response

defaultwork_heartbeat

last_heartbeat: string



RFC 3339 timestamp of the actual heartbeat from DB

lease_extended: boolean



Whether the heartbeat succeeded in extending the lease



state: "queued" or "starting" or "active" or 2 more



Current state of the work item (active/stopping/stopped)

One of the following:

"queued"



"starting"



"active"



"stopping"



"stopped"



ttl_seconds: number



Effective TTL applied to the lease



BetaSelfHostedWorkListResponse object{ data, next_page }



Response when listing work items with cursor-based pagination.



BetaSelfHostedWorkQueueStats object{ type: "work_queue_stats", depth, oldest_queued_at, 2 more }



Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.



type: "work_queue_stats"



The type of object

defaultwork_queue_stats

depth: number



Number of work items waiting to be picked up (lag from consumer group)

oldest_queued_at: string or null



RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty



pending: number



Number of work items being processed (polled but not acknowledged)

default0

workers_polling: number or null



Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.



BetaSelfHostedWorkStopRequest object{ force }



Request to stop a work item.



force: optional boolean



If true, immediately stop work without graceful shutdown

defaultfalse



BetaSelfHostedWorkUpdateRequest object{ metadata }



Request to update work item metadata.

metadata: map\[string\]



Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.



BetaSessionWorkData object{ type: "session", id }



Work data for session work items.

This resource type is used when work represents a session that needs to be executed in a self-hosted environment.

type: "session"



Type of work data

id: string



Session identifier (e.g., 'session\_...')
