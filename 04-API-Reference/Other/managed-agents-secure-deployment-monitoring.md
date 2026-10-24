---
title: "Review and monitor agent sessions - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/secure-deployment-monitoring"
category: "04-API-Reference/Other"
fetched_at: "2026-10-22T06:28:19Z"
tags: ["agents", "api"]
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fsecure-deployment-monitoring)

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

[Managed Agents](managed-agents-overview.md)Security

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Review and monitor agent sessions

Copy page



Optionally review each session's events with an offline job. Watch webhooks for sessions that need attention, and see what Managed Agents keeps and for how long.

Copy page



Optionally review each session's events with an offline job. Watch webhooks for sessions that need attention, and delete sessions you no longer need. To limit what an agent can do before it runs, see [Secure your Managed Agents deployment](managed-agents-secure-deployment.md).

## Optionally have an offline reviewer read every transcript

An offline reviewer is a job you run, separate from the sessions it reviews, that reads each session's events after they are written. Long sessions have too many events for a person to read, so the job has Claude read them. The review flags behavior beyond what the agent was granted. For a review prompt, setup steps, and working code, see the [security review recipe](https://platform.claude.com/cookbook/managed-agents-cma-agent-security-review) in the Claude Cookbook.

## Monitor sessions and review retention

Subscribe to the webhooks that tell you when a session needs attention, and delete sessions you no longer need. Verify the signature on each delivery. See [Verify the signature](managed-agents-webhooks.md#verify-the-signature).

| What to watch                                           | Where to see it                                                                                                                                                                                      |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sessions that go idle, for example to wait for approval | The `session.status_idled` webhook. It fires each time a session goes idle, for any reason                                                                                                           |
| Sessions that reach a budget or terminate               | The `session.budget_reached` and `session.status_terminated` webhooks                                                                                                                                |
| Scheduled runs that fail to start a session             | The `deployment_run.failed` and `deployment.paused` webhooks                                                                                                                                         |
| MCP OAuth credentials that cannot refresh               | The `vault_credential.refresh_failed` webhook                                                                                                                                                        |
| Tool calls the server denied or paused                  | `evaluated_permission` on `agent.tool_use` and `agent.mcp_tool_use` events. In a multiagent session, also list each thread's events                                                                  |
| What an agent did in a session                          | The Claude Console session viewer                                                                                                                                                                    |
| Behavior beyond what the agent was granted              | An optional offline review job you run that reads each session's events. See [Optionally have an offline reviewer read every transcript](#optionally-have-an-offline-reviewer-read-every-transcript) |

To see why a session went idle, list its events with `types` set to `session.status_idle`, `order` set to `desc`, and `limit` set to `1`. The event is named `session.status_idle`, and the webhook is named `session.status_idled`. If `stop_reason.type` is `requires_action`, the session is waiting on you, and `stop_reason.event_ids` lists the events it is waiting on. To answer them, see [Answer tool calls that pause the session](managed-agents-events-and-streaming.md#answer-tool-calls-that-pause-the-session). In a self-hosted sandbox, an `agent.tool_use` event can be waiting for your sandbox to return the tool's result. With workflow runs open, a tool call can wait for your answer while the session stays `running`. Answer each call when its event arrives. See [While a run is open](managed-agents-workflow-runs.md#while-a-run-is-open).

A webhook delivery can be missed, so also list your sessions on a schedule and check the idle ones.

See [Subscribe to webhooks](managed-agents-webhooks.md) and [Inspect sessions and track usage](managed-agents-session-observability.md#inspect-a-session-in-the-console).

This list shows what Managed Agents keeps, and for how long:

- **Session history:** Kept until you delete the session. Archiving a session keeps its history. To keep a session's events, copy them to your own logs with the events API before you delete it. A `running` session cannot be deleted. See [Deleting a session](managed-agents-session-operations.md#deleting-a-session).
- **Sandbox state:** Kept for 30 days after the sandbox is created.
- **Files a session produces:** Deleted with the session. Download the files you want to keep first.
- **Files you uploaded, memory stores, and vaults:** Not deleted with the session. Delete them separately.

With a self-hosted sandbox, the copies of tool inputs and outputs on your own infrastructure are yours to retain or delete.

Managed Agents is not currently eligible for Zero Data Retention or HIPAA Business Associate Agreement (BAA) coverage. See [API and data retention](manage-claude-api-and-data-retention.md#feature-eligibility).
