---
title: "Review and monitor agent sessions - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/secure-deployment-monitoring"
category: "04-API-Reference/Other"
fetched_at: "2026-11-15T06:24:23Z"
tags: ["agents", "api"]
---

# Review and monitor agent sessions

Copy page



Optionally review each session’s events with an offline job. Watch webhooks for sessions that need attention, and see what Managed Agents keeps and for how long.

Copy page



[Managed Agents](managed-agents-overview.md)

Beta

[Models](managed-agents-overview.md#feature-availability)  
- All models

[Cloud platforms](managed-agents-overview.md#feature-availability)  
- Claude API
- Claude Platform on AWS
- Claude Models on Google CloudAnthropic managed

[Beta header](managed-agents-overview.md#feature-availability)  
- 
  Copy`managed-agents-2026-04-01`

[Data handling](managed-agents-overview.md#feature-data-handling)  
ZDRNot ZDR eligibleHIPAANot HIPAA eligible

Optionally review each session’s events with an offline job. Watch webhooks for sessions that need attention, and delete sessions you no longer need. To limit what an agent can do before it runs, see [Secure your Managed Agents deployment](managed-agents-secure-deployment.md).

## Optionally have an offline reviewer read every transcript

An offline reviewer is a job you run, separate from the sessions it reviews, that reads each session’s events after they are written. Long sessions have too many events for a person to read, so the job has Claude read them. The review flags behavior beyond what you granted the agent. For a review prompt, setup steps, and working code, see the [security review recipe](https://platform.claude.com/cookbook/managed-agents-cma-agent-security-review) in the Claude Cookbook.

## Monitor sessions and review retention

Subscribe to the webhooks that tell you when a session needs attention, and delete sessions you no longer need. Verify the signature on each delivery. See [Verify the signature](managed-agents-webhooks.md#verify-the-signature).

| What to watch | Where to see it |
|----|----|
| Sessions that go idle, for example to wait for approval | The `session.status_idled` webhook. It fires each time a session goes idle, for any reason |
| Sessions that reach a budget or terminate | The `session.budget_reached` and `session.status_terminated` webhooks |
| Scheduled runs that fail to start a session | The `deployment_run.failed` and `deployment.paused` webhooks |
| MCP OAuth credentials that cannot refresh | The `vault_credential.refresh_failed` webhook |
| Tool calls the server denied or paused | `evaluated_permission` on `agent.tool_use` and `agent.mcp_tool_use` events. In a multiagent session, also list each thread’s events |
| What an agent did in a session | The Claude Console session viewer |
| Behavior beyond what you granted the agent | An optional offline review job you run that reads each session’s events. See [Optionally have an offline reviewer read every transcript](#optionally-have-an-offline-reviewer-read-every-transcript) |

To see why a session went idle, list its events with `types` set to `session.status_idle`, `order` set to `desc`, and `limit` set to `1`. The event is named `session.status_idle`, and the webhook is named `session.status_idled`. If `stop_reason.type` is `requires_action`, the session is waiting on you, and `stop_reason.event_ids` lists the events it is waiting on. To answer them, see [Answer tool calls that pause the session](managed-agents-events-and-streaming.md#answer-tool-calls-that-pause-the-session). In a self-hosted sandbox, an `agent.tool_use` event can be waiting for your sandbox to return the tool’s result. With workflow runs open, a tool call can wait for your answer while the session stays `running`. Answer each call when its event arrives. See [While a run is open](managed-agents-workflow-runs.md#while-a-run-is-open).

You can miss a webhook delivery, so also list your sessions on a schedule and check the idle ones.

See [Subscribe to webhooks](managed-agents-webhooks.md) and [Inspect sessions and track usage](managed-agents-session-observability.md#inspect-a-session-in-the-console).

This list shows what Managed Agents keeps, and for how long:

- **Session history:** Kept until you delete the session. Archiving a session keeps its history. To keep a session’s events, copy them to your own logs with the events API before you delete it. A `running` session cannot be deleted. See [Deleting a session](managed-agents-session-operations.md#deleting-a-session).
- **Sandbox state:** Kept for 30 days after the sandbox is created.
- **Files a session produces:** Deleted with the session. Download the files you want to keep first.
- **Files you uploaded, memory stores, and vaults:** Not deleted with the session. Delete them separately.

With a self-hosted sandbox, the copies of tool inputs and outputs on your own infrastructure are yours to retain or delete.

Managed Agents is not currently eligible for Zero Data Retention or HIPAA Business Associate Agreement (BAA) coverage. See [API and data retention](manage-claude-api-and-data-retention.md#feature-eligibility).
