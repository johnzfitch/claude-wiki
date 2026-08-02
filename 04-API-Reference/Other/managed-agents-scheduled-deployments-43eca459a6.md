---
title: "Scheduled deployments - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/scheduled-deployments"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:41Z"
tags: ["api"]
---

# Scheduled deployments




Create and manage deployments with the Claude API: run an agent on a recurring cron schedule and inspect its run history.




A **scheduled deployment** allows an [agent](/docs/en/managed-agents/agent-setup) to start [sessions](/docs/en/managed-agents/sessions) autonomously, enabling task completion over a predictable cadence. You create and manage deployments with the Deployments API, part of the Claude API.

For the launch context and examples of what teams run on schedules, see [scheduled deployments and vaults in Claude Managed Agents](https://claude.com/blog/whats-new-in-claude-managed-agents) on the blog.



All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.




Create a scheduled deployment

When creating a deployment, you pass the [session configurations](/docs/en/managed-agents/sessions) required for execution, in addition to a `schedule`.

- Deployments require [agent configuration](/docs/en/managed-agents/agent-setup) and [environment configuration](/docs/en/managed-agents/environments), and optionally accept [files](/docs/en/managed-agents/files), [GitHub](/docs/en/managed-agents/github), [memory stores](/docs/en/managed-agents/memory), and [vaults](/docs/en/managed-agents/vaults).
- Deployments also require at least one initial event, a `user.message` or `user.define_outcome`, that starts each session's work.
- In the `schedule`, you define a cron `expression` and a `timezone`. Maximum granularity supported is at the minute level.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
DEPLOYMENT_ID=$(ant beta:deployments create <<YAML | jq -er '.id'
name: Weekly compliance scan
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
initial_events:
  - type: user.message
    content:
      - type: text
        text: Run the weekly compliance scan.
schedule:
  type: cron
  expression: "0 20 * * 5"
  timezone: America/New_York
YAML
)
```

The response includes a deployment object with a populated `schedule.upcoming_runs_at` with the next upcoming fire times, to confirm your schedule was set correctly.

```python
{
  "id": "depl_01xyz",
  "status": "active",
  "paused_reason": null,
  "schedule": {
    "type": "cron",
    "expression": "0 20 * * 5",
    "timezone": "America/New_York",
    "last_run_at": null,
    "upcoming_runs_at": [
      "2026-05-09T00:00:00Z",
      "2026-05-16T00:00:00Z",
      "2026-05-23T00:00:00Z"
    ]
  }
}
```



The upcoming run timestamps reflect the exact schedule configured. However, to distribute load, actual execution applies jitter of up to 15% of the interval between runs, with a minimum of 5 seconds and a maximum of 9 minutes.

A maximum of **1,000 scheduled deployments** is supported per organization. Contact Anthropic support if you need more.

See the [Create Deployment reference](/docs/en/api/beta/deployments/create) for full parameters and response schema.




Cron and timezone semantics

- **Expression:** Standard POSIX cron (`minute hour day-of-month month day-of-week`). You can generate and validate these cron expressions in the [Claude Console](https://platform.claude.com/workspaces/default/deployments).
- **Timezone:** IANA timezone identifier (for example, `"America/Los_Angeles"`).
- **DST:** Cron schedules use literal wall-clock matching, so `"0 20 * * *"` in `America/New_York` fires at 8

  PM local time regardless of whether EST or EDT is in effect.



Wall-clock times that do not exist on a spring-forward day (such as 2 AM) are not triggered. Wall-clock times that occur twice on a fall-back day fire twice. Schedule outside the 1–3 AM local window, or use UTC, when missed or duplicate executions are unacceptable.




Deployment runs

Deployments can fail to trigger for a variety of reasons: for example, if the `environment` resource has been archived, or if session creation is rate-limited. Each attempt at executing a deployment generates a **deployment run** record, allowing you to track successes and failures independent of the session lifecycle.

Successful deployments generate active sessions, and a successful deployment run contains the associated `session_id`. To follow a session's lifecycle, track the session events through the [event stream](/docs/en/managed-agents/events-and-streaming) or [webhooks](/docs/en/managed-agents/webhooks). Deployment lifecycle changes and the outcome of each scheduled run are also delivered as webhook events, listed in the Deployment events and Deployment run events tabs of [Supported event types](/docs/en/managed-agents/webhooks#supported-event-types).

List all deployment runs for a deployment as follows:

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:deployment-runs list --deployment-id "$DEPLOYMENT_ID"
```

You can additionally filter on deployment runs with errors:

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:deployment-runs list --deployment-id "$DEPLOYMENT_ID" --has-error
```

A failed run includes an `error` with a `type` describing why session creation was rejected (for example, `environment_archived_error`, `agent_archived_error`, or `session_rate_limited_error`). See the [List Deployment Runs reference](/docs/en/api/beta/deployment_runs/list) for all filter parameters and the response schema.

```python
{
  "type": "deployment_run",
  "id": "drun_01abc124",
  "deployment_id": "depl_01xyz",
  "trigger_context": { "type": "schedule", "scheduled_at": "2026-05-09T00:00:00Z" },
  "session_id": null,
  "error": {
    "type": "environment_archived_error",
    "message": "environment `env_01abc` is archived"
  },
  "agent": { "type": "agent", "id": "agent_01ghi789", "version": 3 },
  "created_at": "2026-05-09T00:00:01Z"
}
```



To retrieve a single run by ID, call [`GET /v1/deployment_runs/{deployment_run_id}`](/docs/en/api/beta/deployment_runs/retrieve). A [`deployment_run` webhook event](/docs/en/managed-agents/webhooks#supported-event-types) carries the run ID as its `data.id`.




Managing deployment lifecycle

Each lifecycle change emits a [webhook event](/docs/en/managed-agents/webhooks#supported-event-types), so you can react to a paused, unpaused, or archived deployment without polling; see the Deployment events tab.

**Pause** suppresses scheduled triggers on a go-forward basis; running sessions from a prior deployment run continue to execute. Manual runs through the `run` endpoint are still allowed while paused. Pausing sets `paused_reason` to `{"type": "manual"}`; unpausing clears it.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:deployments pause --deployment-id "$DEPLOYMENT_ID"
```

**Unpause** resumes the schedule from the next scheduled occurrence. Missed triggers are not backfilled.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:deployments unpause --deployment-id "$DEPLOYMENT_ID"
```

**Archive**, unlike **pause**, is terminal: the schedule terminates and the deployment cannot be modified.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:deployments archive --deployment-id "$DEPLOYMENT_ID"
```




Failure behavior

Session creation rate-limit responses are recorded immediately as a `session_rate_limited_error` run without retry; the schedule attempts again at the next scheduled occurrence. Rate limits on underlying API calls within a session are handled by the session itself.

If a deployment's agent has been archived, the deployment is automatically archived in the same operation. If the agent has been deleted, the next scheduled trigger detects the missing agent and automatically archives the deployment. In both cases no deployment run is recorded. If a subagent referenced by the agent has been archived, the next trigger records a failed run with `error.type: "agent_archived_error"` and the deployment is automatically paused so you can update the agent and resume. Other unrecoverable session-creation errors, such as an archived environment or vault, behave the same way: the trigger records a failed run and the deployment is automatically paused. The deployment's `paused_reason.error.type` mirrors the failed run's `error.type`.




Trigger a manual run

To run a deployment outside its schedule, call the [`run` endpoint](/docs/en/api/beta/deployments/run). This creates a session immediately and writes a deployment run with `trigger_context.type: "manual"`. This allows you to test a deployment before committing to the schedule.

curl

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant beta:deployments run --deployment-id "$DEPLOYMENT_ID"
```
