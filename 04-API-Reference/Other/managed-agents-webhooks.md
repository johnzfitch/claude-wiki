---
title: "Subscribe to webhooks - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/webhooks"
category: "04-API-Reference/Other"
fetched_at: "2026-10-20T06:38:00Z"
tags: ["api", "hooks"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fwebhooks)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[Web tool restrictions](managed-agents-tools-web-restrictions.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Choose an environment](managed-agents-choosing-an-environment.md)[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Event deltas](managed-agents-event-deltas.md)[Inspect and track usage](managed-agents-session-observability.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Session threads](managed-agents-session-threads.md)[Workflow runs](managed-agents-workflow-runs.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

Security

[Secure your deployment](managed-agents-secure-deployment.md)[Review and monitor sessions](managed-agents-secure-deployment-monitoring.md)[Risks and boundaries](managed-agents-secure-deployment-risks.md)

Reference

[Managed Agents reference](managed-agents-reference.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)

[Console](playground.md)

[Managed Agents](managed-agents-overview.md)Delegate work to your agent

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Subscribe to webhooks

Copy page



Get notified when major events happen without polling.

Copy page



Sessions are long-running interactions. While most real-time interactions happen through the [SSE event stream](managed-agents-events-and-streaming.md), webhooks notify you of major state changes.

Webhook events return the event `type` and `id`, not the full object. When you receive a webhook event, you need to fetch the object directly with a `GET` call. This avoids delivering stale data on retries and keeps every delivery small.

## Supported event types

Session events

Vault events

Agent events

Deployment events

Deployment run events

Environment events

Memory store events

Session events

Some of these events are named differently from the matching events on the session's [event stream](managed-agents-events-and-streaming.md). For example, the stream's `session.status_idle` and `session.status_running` correspond to the `session.status_idled` and `session.status_run_started` webhook events.

| Event                              | Trigger                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `session.status_run_started`       | Agent execution started. This triggers at every session status transition to `running`.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `session.status_idled`             | Agent awaiting input, for example, a tool permission approval or a new user message.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `session.budget_reached`           | The session reached its [budget](managed-agents-budgets.md) and paused. Fires at most once for each budget value you set; changing the budget arms it again.                                                                                                                                                                                                                                                                                                                                                               |
| `session.status_rescheduled`       | A transient error occurred and the session is retrying automatically.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `session.status_terminated`        | The session terminated, either because of an unrecoverable error or because it was archived.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `session.thread_created`           | New [multiagent thread](managed-agents-session-threads.md) opened: an additional agent called by the agent that the session runs is starting work, or the session's [advisor](managed-agents-multiagent-orchestration.md#give-the-session-an-advisor) is being consulted. It also fires for each thread of a [workflow run](managed-agents-workflow-runs.md#a-runs-threads), and so do the other two thread events in this table.                                                                              |
| `session.thread_idled`             | An agent in a [multiagent interaction](managed-agents-session-threads.md) is waiting for input.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `session.thread_terminated`        | A [multiagent thread](managed-agents-session-threads.md) terminated, either because the thread was archived or because it exhausted its retries. A subagent that finishes its work goes `idle`, not `terminated` (an advisor thread terminates once its consultation completes, and a workflow run's threads terminate when the server archives them, by the end of the run). Fires for child threads only; the primary thread's end, including archiving the whole session, surfaces only as `session.status_terminated`. |
| `session.outcome_evaluation_ended` | [Outcome evaluation](managed-agents-define-outcomes.md) for a single iteration completed.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `session.updated`                  | Session properties changed (for example, its name or configuration was updated).                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `session.deleted`                  | Session permanently deleted. There is no object left to fetch, so treat the event itself as final.                                                                                                                                                                                                                                                                                                                                                                                                                               |

Vault events

| Event                             | Trigger                                                                                                                                                                 |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `vault.created`                   | Vault created.                                                                                                                                                          |
| `vault.archived`                  | Vault archived. A `vault_credential.archived` event is also emitted for each underlying credential.                                                                     |
| `vault.deleted`                   | Vault deleted. A `vault_credential.deleted` event is also emitted for each underlying credential. There is no object left to fetch, so treat the event itself as final. |
| `vault_credential.created`        | Credential created.                                                                                                                                                     |
| `vault_credential.archived`       | Credential archived, either directly or as a result of vault archival.                                                                                                  |
| `vault_credential.deleted`        | Credential deleted, either directly or as a result of vault deletion. There is no object left to fetch, so treat the event itself as final.                             |
| `vault_credential.refresh_failed` | An `mcp_oauth` credential cannot be refreshed (invalid refresh token, or irrecoverable error from the OAuth server).                                                    |

Agent events

These events track the lifecycle of the agent resources in your workspace, and are distinct from the agent events delivered on a session's event stream.

| Event            | Trigger                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `agent.created`  | Agent created.                                                                                                                                                       |
| `agent.updated`  | A [new version of the agent](managed-agents-agent-setup.md#update-an-agent) was published. Updates that do not create a new version do not trigger this event. |
| `agent.archived` | Agent archived.                                                                                                                                                      |
| `agent.deleted`  | Agent permanently deleted. There is no object left to fetch, so treat the event itself as final.                                                                     |

Deployment events

| Event                 | Trigger                                                                                                                                                                                                                                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `deployment.created`  | [Scheduled deployment](managed-agents-scheduled-deployments.md) created.                                                                                                                                                                                                                                                          |
| `deployment.updated`  | Deployment properties changed (for example, its schedule was updated).                                                                                                                                                                                                                                                                  |
| `deployment.paused`   | Deployment paused, either by request or automatically when a scheduled run fails with an unrecoverable error, such as an archived subagent or an archived environment. Recoverable failures, including rate limits, don't pause the deployment. See [Failure behavior](managed-agents-scheduled-deployments.md#failure-behavior). |
| `deployment.unpaused` | Deployment unpaused, resuming its schedule.                                                                                                                                                                                                                                                                                             |
| `deployment.archived` | Deployment archived, either directly or because its agent was archived. If the agent is deleted instead, a scheduled deployment is archived at its next scheduled run; a deployment without a schedule is not archived automatically.                                                                                                   |
| `deployment.deleted`  | Deployment permanently deleted. There is no object left to fetch, so treat the event itself as final.                                                                                                                                                                                                                                   |

Deployment run events

| Event                      | Trigger                                                                                                                                                                                                                                                                                                                                        |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `deployment_run.started`   | A scheduled run started. Only scheduled runs emit `deployment_run` events; [manual runs](managed-agents-scheduled-deployments.md#trigger-a-manual-run) do not.                                                                                                                                                                           |
| `deployment_run.succeeded` | A scheduled run created its session. The event carries the same `data.id` (the run ID) as the run's `deployment_run.started` event. To follow the session's work, subscribe to its session events (the Session events tab), or fetch the [deployment run](managed-agents-scheduled-deployments.md#deployment-runs) for its `session_id`. |
| `deployment_run.failed`    | A scheduled run did not create a session. The event carries the same `data.id` as the run's `deployment_run.started` event. Fetch the [deployment run](managed-agents-scheduled-deployments.md#deployment-runs) for the error details.                                                                                                   |

Environment events

| Event                  | Trigger                                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `environment.created`  | Environment created.                                                                                                                            |
| `environment.updated`  | Environment updated with at least one changed field. A no-op update emits nothing.                                                              |
| `environment.archived` | Environment archived. Re-archiving an already-archived environment emits nothing.                                                               |
| `environment.deleted`  | Environment deleted, including delete of an already-archived environment. There is no object left to fetch, so treat the event itself as final. |

An environment's [work items](managed-agents-self-hosted-sandboxes.md) emit no webhook events.

Memory store events

| Event                   | Trigger                                                                                                                                                                                                                                                                                             |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `memory_store.created`  | Memory store created, either by you or by an Anthropic-operated process that clones one of your existing stores.                                                                                                                                                                                    |
| `memory_store.archived` | Memory store archived. Re-archiving an already-archived store emits nothing.                                                                                                                                                                                                                        |
| `memory_store.deleted`  | Memory store deleted, including delete of an already-archived store. Deleting a store cascades to its memories and memory versions without emitting per-memory events; the single `memory_store.deleted` event is the signal. There is no object left to fetch, so treat the event itself as final. |

Individual [memories](managed-agents-memory.md) and memory versions emit no webhook events.

## Register an endpoint

In the Claude Console, go to the [Webhooks](https://platform.claude.com/settings/workspaces/default/webhooks) page (`platform.claude.com/settings/workspaces/default/webhooks`). Each endpoint belongs to one workspace. Select the workspace you want in the workspace picker in the sidebar.

A webhook endpoint consists of:

- **URL:** Must be HTTPS on port 443 with a publicly resolvable hostname.
- **Event types:** The list of `data.type` values this endpoint receives. An endpoint only receives events it's subscribed to.
- **Signing secret:** A 32-byte `whsec_`-prefixed secret generated at creation. It's shown only once, so store it securely to verify webhook deliveries.

## Verify the signature

Every delivery carries the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers. Use the SDK's `unwrap()` helper to verify the signature and parse the event in one step. It throws if the signature is invalid or the payload is more than 5 minutes old.

Set `ANTHROPIC_WEBHOOK_SIGNING_KEY` to the `whsec_`-prefixed secret shown at endpoint creation.

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
from flask import Flask, request
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_WEBHOOK_SIGNING_KEY from env
app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # unwrap() raises if the signature is invalid or the payload is stale
        event = client.beta.webhooks.unwrap(
            request.get_data(as_text=True),
            headers=dict(request.headers),
        )
    except Exception:
        return "invalid signature", 400

    if event.data.type == "session.status_idled":
        print("session idled:", event.data.id)
    # handle other event types

    return "", 200
```

## Handle an event

Parse the body, switch on `data.type`, and fetch the resource by ID. Return any `2xx` to acknowledge. Any other response counts against the endpoint: a `3xx` disables it immediately (redirects are never followed), while other failures are retried; see [Delivery behavior](#delivery-behavior) for the retry and auto-disable rules.

Every event payload has the same structure, including the event type, identifier, and the timestamp of when the event occurred.

```python
{
  "type": "event",
  "id": "whe_9d5c1f7e...",
  "created_at": "2026-03-18T14:05:22Z",
  "data": {
    "type": "session.status_idled",
    "id": "sesn_01XYZ...",
    "organization_id": "8a3d2f1e-...",
    "workspace_id": "c7b0e4d9-..."
  }
}
```



Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
if event.data.type == "session.status_idled":
    session = client.beta.sessions.retrieve(event.data.id)
    notify_user(session)
return "", 204
```

The top-level `event.id` is unique per event, not per delivery. If you receive the same `event.id` twice, it's a retry and you can discard it.

## Delivery behavior

- **Duplicates:** An endpoint can receive the same event more than once, and every attempt delivers the same top-level `event.id` (the same value as the `webhook-id` header). Deduplicate on it.

- **Subscription scope:** An event is delivered only to endpoints subscribed to its type at the moment it's emitted. An event emitted while no endpoint is subscribed to its type is never delivered, and subscribing later doesn't backfill it, so subscribe to an event type before you need it.

- **Ordering is not guaranteed.** Events aren't delivered in the order they occurred: `session.status_idled` might arrive before `session.outcome_evaluation_ended` even if the outcome was produced first, and a `.deleted` event can arrive before the `.archived` event for the same resource. Drive your state from the resource you fetch, not from the order events arrive in.

- **Retries:** For each endpoint and event, Anthropic makes up to three delivery attempts (a response that triggers auto-disable, described later in this section, is never retried) with jittered exponential backoff between 5 and 120 seconds. Every attempt delivers the same `event.id`. After the last attempt fails, the event is dropped: it isn't queued for later delivery and there's no signal that it was lost. Webhooks aren't a durable log, so if you need to observe every transition, reconcile by listing or fetching the resource through the API.

- **Timestamps:** The `webhook-timestamp` header is stamped when a delivery attempt is signed and is regenerated on every retry, so retries aren't rejected by the SDK's freshness check. It's the clock for the delivery attempt, not for the event: use the event payload's `created_at` for when the event occurred.

- **Auto-disable:** An endpoint is automatically set to `disabled` with a machine-readable `disabled_reason` in three cases:

  - The endpoint returns a `3xx` response. Redirects are never followed; this disables the endpoint immediately, on the first attempt, with the reason `auto-disabled: endpoint URL returned a redirect (3xx)`. If your endpoint moves, update the URL in Console and re-enable the endpoint.
  - The endpoint's URL resolves to a non-public IP address when Anthropic connects. This disables the endpoint immediately, with the reason `auto-disabled: endpoint URL resolved to an invalid address`.
  - Deliveries to the endpoint fail continuously for a sustained period, with the reason `auto-disabled after sustained delivery failures`. The trigger is how long the endpoint has been failing without interruption, not a delivery count. A single `2xx` resets the window, so one flaky event can't disable the endpoint.

  All three are reversible: re-enable the endpoint in Console after you resolve the issue. Events emitted while the endpoint was disabled aren't replayed.
