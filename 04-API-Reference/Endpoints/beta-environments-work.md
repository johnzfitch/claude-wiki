---
title: "Work - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/environments/work"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:34:55Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [Environments](https://platform.claude.com/docs/en/api/http/beta/environments)

# Work

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

RFC 3339 timestamp of the most recent heartbeat recorded for this work item, or an empty string if none has been recorded

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



type: "work_queue_stats"



The type of object

defaultwork_queue_stats

depth: number



Number of work items waiting to be picked up

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
