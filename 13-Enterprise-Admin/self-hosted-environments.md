---
title: "Self-hosted environments - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/self-hosted-environments"
category: "13-Enterprise-Admin"
fetched_at: "2026-09-30T06:30:56Z"
tags: ["claude-code", "enterprise"]
---

## On this page

- [How self-hosted environments work](#how-self-hosted-environments-work)
- [Availability and limitations](#availability-and-limitations)
- [Why self-host](#why-self-host)
- [Environments, runners, and sessions](#environments-runners-and-sessions)
  - [Key concepts](#key-concepts)
  - [Session lifecycle](#session-lifecycle)
  - [Runner lifecycle](#runner-lifecycle)
  - [Network paths](#network-paths)
- [What stays on your infrastructure](#what-stays-on-your-infrastructure)
- [Get started](#get-started)

Self-hosted environments

# Self-hosted environments

Copy pageCopy page

Run Claude Code cloud sessions on infrastructure you control: set up a self-hosted environment, deploy runners, and route sessions to your own compute.

Copy pageCopy page

Self-hosted environments are in public beta on Team and Enterprise plans and are off by default. See [Availability and limitations](#availability-and-limitations) for the enablement path and what’s excluded.

A self-hosted environment executes Claude Code cloud sessions on infrastructure your organization operates. A [cloud session](../02-Claude-Code-CLI/claude-code-on-the-web.md) is any session that runs somewhere other than the developer’s machine: developers start them from claude.ai, the mobile and desktop apps, the terminal with [`claude --cloud`](../02-Claude-Code-CLI/claude-code-on-the-web.md#from-terminal-to-cloud), and [scheduled routines](../02-Claude-Code-CLI/web-scheduled-tasks.md), and by default they execute on Anthropic’s infrastructure. In a self-hosted environment, those same sessions execute inside your network, and the developer experience is otherwise the same apart from the differences in [Availability and limitations](#availability-and-limitations) and the deploy page’s [known issues](self-hosted-environments-deploy.md#known-issues-and-limitations). If your team doesn’t use cloud sessions, there’s nothing here to configure: sessions in a terminal or IDE always run on the developer’s own machine. If you want to run Claude Code on your own always-on machine and drive it from other devices, use [Remote Control](../02-Claude-Code-CLI/remote-control.md), which is also available on Pro and Max plans. When you’re ready to set up, go straight to the [quickstart](self-hosted-environments-quickstart.md); to review the security posture first, start with [Deploy to production](self-hosted-environments-deploy.md). The rest of this page explains how self-hosting works and when to choose it.


[​](#how-self-hosted-environments-work)

How self-hosted environments work

Self-hosting has three parts:

- **Environment**: a named destination that cloud sessions can be sent to. Your organization creates environments in claude.ai admin settings, and each one groups a set of runners.
- **Runner**: a program running on hosts inside your network. Runners execute the sessions; the idea is the same as a self-hosted CI runner.
- **Session**: one Claude Code task a developer started.

When a developer starts a cloud session, the session-start UI shows an environment picker listing Anthropic-hosted environments alongside any your organization has created. If they choose yours, Anthropic’s control plane places the session on your environment’s queue, where a runner claims it, clones the repository the developer chose, and starts a Claude Code process on your host to run it. The runner authenticates to your git host with credentials you configure; [Configure git](self-hosted-environments-deploy.md#configure-git) covers the options. Sessions reach your internal services from inside your network, and your git host the same way when it’s internal; the traffic to Anthropic, queue polling, the session’s event stream, and model inference, is outbound HTTPS to `api.anthropic.com`, with the short list of further hosts sessions can reach in [Network requirements](self-hosted-environments-deploy.md#network-requirements). Anthropic never connects into your network.

The two Claude Code boxes in the diagram are session processes: one runner executing two sessions at once, up to its configured capacity. A runner serves one [owner](#key-concepts) at a time and locks to that owner when it claims its first session, so checked-out code never mixes between owners; [Runner lifecycle](#runner-lifecycle) covers the rule. You can start runners yourself and keep them running, or run the [autoscaling orchestrator](self-hosted-environments-configuration.md#on-demand-runners), a second process you host, which starts runners as sessions queue; each runner exits on its own when its work finishes. Either way, you set the environment up once, and it appears in the picker on every supported surface.


[​](#availability-and-limitations)

Availability and limitations

Check these before planning a rollout:

- **Plans**: public beta for Team and Enterprise organizations. Self-hosted environments are off by default; an [Owner](../02-Claude-Code-CLI/cloud-environments.md#organization-shared-environments) turns on **Allow self-hosted environments** on the [**Cloud environments** admin page](https://claude.ai/admin-settings/cloud-environments), which requires [cloud sessions](../02-Claude-Code-CLI/claude-code-on-the-web.md) to be enabled for the organization.
- **Zero Data Retention**: unavailable for organizations with [Zero Data Retention](../02-Claude-Code-CLI/zero-data-retention.md) enabled.
- **Model inference**: sessions use the Anthropic API, and inference can’t be routed through [Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry](../02-Claude-Code-CLI/third-party-integrations.md), or an [LLM gateway](llm-gateway.md).
- **Surfaces**: sessions started from [claude.ai/code](https://claude.ai/code), the mobile and desktop apps, [scheduled routines](../02-Claude-Code-CLI/web-scheduled-tasks.md), and the terminal, with [`claude --cloud`](../02-Claude-Code-CLI/claude-code-on-the-web.md#from-terminal-to-cloud) or an [`--environment` dispatch](self-hosted-environments-testing.md#run-the-test-loop), can run in self-hosted environments. [Claude Tag](https://claude.com/docs/claude-tag/overview) sessions can run in them too, but Claude can’t use [Access bundles](https://claude.com/docs/claude-tag/concepts/glossary#access-bundle) in those sessions yet. [Claude Security](../02-Claude-Code-CLI/claude-security.md) and [Code Review](../02-Claude-Code-CLI/code-review.md) sessions don’t route to them yet. Support for those two surfaces follows separately.
- **Repositories**: sessions check out repositories from GitHub; see [GitHub authentication options](../02-Claude-Code-CLI/claude-code-on-the-web.md#github-authentication-options). For a GitHub Enterprise Server host, see its [network requirements](../02-Claude-Code-CLI/github-enterprise-server.md#network-requirements).
- **Billing**: sessions in a self-hosted environment consume your organization’s Claude Code usage the same way sessions in Anthropic-hosted environments do.


[​](#why-self-host)

Why self-host

Most teams are better served by Anthropic-hosted environments, which need no infrastructure to run or maintain. Self-hosting is for teams whose network, tooling, or compliance requirements call for keeping session execution on infrastructure they control. If that’s you, plan for the operational ownership it carries: you build and maintain the runner image, operate the fleet, and control its network. In exchange, self-hosting gives you network access, custom tooling, and compliance control:

- **Network access**: sessions run inside your network and can reach internal services, databases, and registries without exposing them to the public internet
- **Custom tooling**: pre-install compilers, SDKs, and internal CLIs in your runner image so every session starts ready to build
- **Compliance**: repository checkouts and build artifacts stay on infrastructure you control. Session content still goes to `api.anthropic.com` for model inference.


[​](#environments-runners-and-sessions)

Environments, runners, and sessions

Environments are managed on the **Cloud environments** page in claude.ai admin settings; runners are processes you start and manage on your own infrastructure.


[​](#key-concepts)

Key concepts

These terms appear throughout the self-hosted pages:

| Term               | What it is                                                                                                                                                                                              |
|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Environment        | A named group of your runners, created in claude.ai settings. Sessions are routed to an environment, not to an individual runner.                                                                       |
| Environment secret | The single shared credential runners use to authenticate and register with the environment. Shown once at environment creation, labeled **environment key** in the admin UI.                            |
| Runner             | The long-lived process you deploy. A runner registers with the environment, receives a runner token, and polls for sessions.                                                                            |
| Session            | One Claude Code task, started from claude.ai, the mobile app, or another Anthropic surface such as a scheduled routine or an agent. Each session runs as a child Claude Code process the runner spawns. |

In API fields, token claims, and metric names, the environment appears as `pool`, and the environment ID is the `pool_id`. The [reference](self-hosted-environments-reference.md) maps the two spellings, including the deprecated `pool` flag names. A runner serves one owner at a time. The first session a runner picks up locks the runner to that session’s owner, and the runner then runs sessions only for that owner, up to a configured capacity. Who the owner is depends on how the session started:

- **Sessions a user starts**: the owner is that user’s account.
- **Claude Tag channel sessions**: Claude runs them with no user account attached, so the owner is the [Claude Tag agent](https://claude.com/docs/claude-tag/concepts/glossary#agent-identity) that started the session. Every channel session that agent starts has the same owner, whoever sent the Slack message, so a runner locked to it serves sessions that different people started when you run it at a `--capacity` above one or with a positive `--drain-grace-sec`. A runner locked to a user never picks these up, and a runner locked to a Claude Tag agent never picks up a user’s sessions.

The minimum fleet size is therefore the number of owners you expect to be active at once, counting users and Claude Tag agents.


[​](#session-lifecycle)

Session lifecycle

When a developer starts a session and selects your environment, Anthropic’s control plane places the session on the environment’s queue. From there:

1.  A runner with free capacity claims the session and holds a lease on it.
2.  The runner clones the repository into its working directory and spawns a child Claude Code process.
3.  The child streams events back over HTTPS while the runner keeps polling; each poll refreshes the lease and doubles as the heartbeat.
4.  If the runner stops polling for about 60 seconds, the server requeues the session for another runner.

The runner gives each poll request 10 seconds. When a request times out, is lost, or gets a response the runner can’t parse, the runner keeps serving its live sessions and retries after a second or two instead of waiting for the next scheduled poll. For example, an intercepting proxy that answers the poll with its own page produces a response the runner can’t parse. Each time another request fails in one of those ways, the runner doubles the gap before the next retry, up to 20 seconds, and shortens the gap whenever the lease is close to expiring.


[​](#runner-lifecycle)

Runner lifecycle

The first session a runner picks up locks the runner to that session’s owner, and the runner runs up to `--capacity` concurrent sessions for that owner. While the runner has active sessions and hasn’t received a shutdown signal or reached its retire time, the runner keeps claiming the locked owner’s queued work. What happens once they finish depends on [`--drain-grace-sec`](self-hosted-environments-reference.md#runner-cli-flags):

- **At the default of `0`**: the runner exits as soon as its active sessions finish, without polling for more, so the orchestrator you deploy it under, such as Kubernetes, can restart it with a fresh disk, ready to serve any owner.
- **At a positive value**: the runner keeps polling the locked owner’s queue for that many seconds before exiting.

This lifecycle isolates each owner’s checked-out code without requiring the runner to delete disk state between owners. How your infrastructure stops a runner decides whether you need `--retire-at`. A kill that delivers `SIGTERM` needs no flag: the runner drains as [Shutdown timing](self-hosted-environments-deploy.md#shutdown-timing) describes, or keeps serving the sessions it already holds when you set [`--defer-shutdown-max-min`](self-hosted-environments-deploy.md#defer-the-drain-past-the-first-signal). If your infrastructure instead destroys hosts at a known wall-clock time without a signal, or with a grace period too short to drain, such as a sandbox lifetime cap or spot-instance reclamation, pass `--retire-at <epoch-seconds>` set to a few minutes before that time. At the retire time:

1.  The runner stops taking new work.
2.  The runner releases each active session through the same release path the [`--release-idle-session-min`](self-hosted-environments-reference.md#runner-cli-flags) flag uses, so the session resumes on a fresh runner when the user sends their next message. When the runner releases each session depends on its state:
    - The runner releases a session that’s mid-turn as soon as that turn finishes.
    - When a turn finishes and leaves background tasks running, the runner waits up to 60 seconds for them, then releases the session even if they’re still running. If the tasks have finished but the follow-up turn that reads their results hasn’t run yet, the runner keeps the session until that turn finishes, and waits no longer than [`SELF_HOSTED_RUNNER_BG_RESULT_GRACE_MS`](self-hosted-environments-reference.md#environment-variable-only-settings) for that turn to start.
3.  The runner exits 0 once all its sessions are released.

A turn that outlives the kill is still lost; [Shutdown timing](self-hosted-environments-deploy.md#shutdown-timing) covers sizing the margin. Without `--retire-at`, a signal-less host kill is indistinguishable from a crash: the control plane records a lost worker rather than a clean release, and the session requeues to another runner.


[​](#network-paths)

Network paths

The runner and its sessions make several kinds of outbound connection, and no inbound connectivity from Anthropic is required:

- **Control plane**: the runner polls `api.anthropic.com` for work and posts setup-progress and failure events, all outbound HTTPS. Polling doubles as the runner’s heartbeat.
- **SCM connector**: the optional orchestrator [SCM connector](self-hosted-environments-reference.md#scm-connector-flags) tunnel is the only WebSocket connection.
- **Git**: the runner clones from and pushes to your git host over HTTPS or SSH, authenticated with credentials your deployment provides; [Configure git](self-hosted-environments-deploy.md#configure-git) covers the options, including per-session minted credentials and the [Anthropic git proxy](self-hosted-environments-deploy.md#use-the-anthropic-git-proxy), which routes git through `api.anthropic.com` instead.
- **Session child**: the child Claude Code process holds the session’s event stream to `api.anthropic.com`, and makes its own outbound calls for model inference and for git commands run during the session. See [Network requirements](self-hosted-environments-deploy.md#network-requirements) for the full egress list. The [diagram above](#how-self-hosted-environments-work) shows these paths, apart from the optional SCM connector.

Model inference uses the Anthropic API. The control plane delivers the API endpoint to each session, and the session authenticates with an Anthropic-issued, session-scoped OAuth token, so inference can’t be routed through [Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry](../02-Claude-Code-CLI/third-party-integrations.md), or an [LLM gateway](llm-gateway.md) in self-hosted environments. Corporate egress proxies are supported. The runner and the optional [autoscaling orchestrator](self-hosted-environments-configuration.md#on-demand-runners) honor the proxy and mTLS environment variables described in [Network configuration](network-config.md), such as `HTTPS_PROXY` and `NO_PROXY`; set them in each process’s environment. The variables cover control-plane calls, the orchestrator’s [SCM connector](self-hosted-environments-reference.md#scm-connector-flags) WebSocket, and the built-in clone for HTTPS remotes, and sessions inherit them from the runner. Session streaming uses server-sent events over HTTPS, so a proxy in the path must not buffer responses. If your proxy also requires a `Proxy-Authorization` header, the runner can add it to each connection it opens to the proxy; see [Authenticate to an egress proxy](self-hosted-environments-deploy.md#authenticate-to-an-egress-proxy).


[​](#what-stays-on-your-infrastructure)

What stays on your infrastructure

Repository checkouts, build artifacts, secrets, and any files a session creates or modifies stay on the machines you provision. The conversation itself, including prompts, responses, and tool results, goes to `api.anthropic.com` for model inference, and Anthropic stores the session transcript so you can resume the session from another [supported surface](#availability-and-limitations). A self-hosted environment moves session execution into your network. The control plane remains Anthropic-hosted: session orchestration, queueing, and the claude.ai interface continue to run on Anthropic’s infrastructure.


[​](#get-started)

Get started

The self-hosted environments pages are organized by what you’re doing:

- [Quickstart](self-hosted-environments-quickstart.md): install Claude Code, create an environment, start a runner, and route your first session
- [Deploy to production](self-hosted-environments-deploy.md): security hardening, network egress, git credentials, Kubernetes and Compose recipes, known issues, and troubleshooting
- [Customize sessions](self-hosted-environments-configuration.md): wrapper scripts for per-session credentials, lifecycle hooks, on-demand runners, MCP servers, and permissions
- [Test end to end](self-hosted-environments-testing.md): a CI smoke test that verifies a runner image before you promote it
- [Reference](self-hosted-environments-reference.md): every CLI flag, environment variable, metric, and the health endpoint
- [Verify session identity](self-hosted-environments-identity.md): validate the session token from your own services before granting access
