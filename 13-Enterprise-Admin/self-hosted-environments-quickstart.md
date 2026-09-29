---
title: "Self-hosted environments quickstart - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/self-hosted-environments-quickstart"
category: "13-Enterprise-Admin"
fetched_at: "2026-08-28T09:21:52Z"
tags: ["claude-code", "enterprise"]
---

## On this page

- [Prerequisites](#prerequisites)
  - [Organization and roles](#organization-and-roles)
  - [Host and network](#host-and-network)
  - [Software on the runner host](#software-on-the-runner-host)
- [Set up an environment and runner](#set-up-an-environment-and-runner)
- [Send a follow-up message to a running session](#send-a-follow-up-message-to-a-running-session)
- [What’s next](#what%E2%80%99s-next)

Self-hosted environments

# Self-hosted environments quickstart

Copy pageCopy page

Set up your first self-hosted environment: install Claude Code, create the environment, start a runner, and route a session to it.

Copy pageCopy page

Self-hosted environments are in public beta on Team and Enterprise plans; [Availability and limitations](self-hosted-environments.md#availability-and-limitations) covers the enablement path. This page gets your first session running; see [Self-hosted environments](self-hosted-environments.md) for what they are and [Deploy to production](self-hosted-environments-deploy.md) for hardening and fleet recipes.

A [self-hosted environment](self-hosted-environments.md) runs Claude Code [cloud sessions](../02-Claude-Code-CLI/claude-code-on-the-web.md) on infrastructure your organization operates, executed by runner processes you deploy. This quickstart stands up your first one, the smallest that works: one runner on a single host, running one test session. There are two steps: [create the environment, start a runner, and route a session to it](#set-up-an-environment-and-runner), then [message that session from your terminal](#send-a-follow-up-message-to-a-running-session). You’ll move between two surfaces: claude.ai for creating the environment, checking its status, and routing a session, and a terminal on the host for everything the runner does. By the end you’ll have an environment on the [**Cloud environments** admin page](https://claude.ai/admin-settings/cloud-environments), a runner polling for work, and a session running on your host. Before you connect real repositories or internal systems, work through [Deploy to production](self-hosted-environments-deploy.md), which covers the security posture, egress control, git credentials, and orchestration.


[​](#prerequisites)

Prerequisites


[​](#organization-and-roles)

Organization and roles

The claude.ai side needs:

- **Allow self-hosted environments** turned on by an [Owner](../02-Claude-Code-CLI/cloud-environments.md#organization-shared-environments) on the [**Cloud environments** admin page](https://claude.ai/admin-settings/cloud-environments); the **New** button doesn’t appear until it is. If you don’t hold the role, someone who does can create the environment and hand you its secret; the runner and terminal steps on this page need no claude.ai role, and where a step checks status in the admin UI, the runner’s own log lines give you the same signal.
- A [GitHub connection](../02-Claude-Code-CLI/claude-code-on-the-web.md#github-authentication-options) for your organization, so developers can pick repositories when they start sessions.


[​](#host-and-network)

Host and network

The runner host needs:

- A Linux or macOS host or container with outbound HTTPS to `api.anthropic.com`, to `claude.ai` and the download hosts it redirects to for the install step below, and to your git host for the clone; the [network requirements table](self-hosted-environments-deploy.md#network-requirements) has the full list. Windows isn’t supported as a runner host; run the runner in a Linux container instead. Developer workstations aren’t affected, since sessions start from claude.ai in a browser.
- A clock synchronized to real time, for example with NTP. Authentication fails when the clock is more than five minutes off; see [Troubleshooting](self-hosted-environments-deploy.md#troubleshooting).


[​](#software-on-the-runner-host)

Software on the runner host

Install on the host before you start:

- **Claude Code v2.1.224 or later**, with any of the [standard install methods](../01-Getting-Started/setup.md). The runner is part of the standard `claude` binary, and earlier versions don’t recognize the `self-hosted-runner` subcommand. The native installer’s default `latest` channel carries each release as soon as it’s published; the `stable` channel, the Homebrew `claude-code` cask, and the stable apt, dnf, and apk repositories trail by about a week. To pin the exact version your fleet runs, see [Install a specific version](../01-Getting-Started/setup.md#install-a-specific-version). For container images, see the Dockerfile in [Deploy to production](self-hosted-environments-deploy.md#build-the-runner-image).
- **Git 2.24 or newer**. Some git options on the deploy page need newer versions; [Configure git](self-hosted-environments-deploy.md#configure-git) states each floor.

Confirm the host is ready:

```python
claude self-hosted-runner --help
```

A ready host prints the runner’s usage text, listing flags such as `--environment-secret-file`. On versions older than 2.1.224, the command prints the general `claude --help` output instead; upgrade with `claude update` or reinstall from the `latest` channel.


[​](#set-up-an-environment-and-runner)

Set up an environment and runner

Claude Code includes a guided setup: an interactive Claude Code session that walks you through creating the environment in the admin UI, starts a local runner with the secret file you save, confirms that the runner registers, and writes a cheat sheet to `./runner-setup/CHEAT-SHEET.md`. Run it on a machine where you’ve signed in with `claude auth login` using an account that holds an Owner role; it isn’t available with API keys or third-party model providers. On hosts where an interactive session isn’t possible, use the manual steps below instead. Confirm the [version check](#software-on-the-runner-host) passed first: on versions older than 2.1.224, this command starts an ordinary Claude session with the words as the prompt instead of the guided setup. To start the guided setup, run the setup subcommand and follow the prompts:

```python
claude self-hosted-runner setup
```

To set up manually instead:

1

Create an environment

Go to the [**Cloud environments** page](https://claude.ai/admin-settings/cloud-environments) in admin settings. Under **Self-hosted environments**, select **New**, name the environment, and select **Create**. On the wizard’s second step, select **Copy environment key** to copy the environment secret, which the admin UI labels an environment key. claude.ai shows the secret once, and you can’t retrieve it later; it expires 365 days after creation. The environment’s `ccpool_...` ID stays visible in its detail dialog; you’ll need it for the `aud` check in [token verification](self-hosted-environments-identity.md) and for dispatching [test sessions from CI](self-hosted-environments-testing.md#run-the-test-loop).If you lose the secret or need to rotate it, create a new secret from the environment’s **Configuration** tab, roll the new secret out to your runners, then revoke the old one. Runners holding a revoked secret fail their next authenticated poll and exit, logging `poll auth failed`, and your orchestrator restarts them with the new secret.

2

Start a runner

Create the secret directory. This step and the next need root for the `/etc/claude` path; any path the runner process can read works, so adjust both commands and the `--environment-secret-file` value together if you use a different one.

```python
mkdir -p /etc/claude
```

Write the environment secret to a file. The command below reads from your terminal so the secret stays out of shell history: paste the value you copied, press Enter, then Ctrl-D, and the subshell’s `umask` makes the file readable only by its owner.

```python
(umask 077 && cat > /etc/claude/environment-secret)
```

Choose a base directory, replacing `<writable-dir>` in the runner command below with an absolute path that the runner can write to or create. The runner creates the directory at startup, then checks repositories out and creates per-session directories under it. Without `--base-dir` it uses `/workspace`, which only works if that directory already exists and is writable or you start the runner as root.If the runner can’t create or write to the path, it exits at startup with an error naming the directory instead of registering. See [Troubleshooting](self-hosted-environments-deploy.md#troubleshooting).Then start the runner with `--environment-secret-file` and `--base-dir`. The runner registers with your environment and begins polling for work. If the runner exits, restart it by hand. Production deployments run the runner under an orchestrator that restarts exited runners, normally with a fresh filesystem per restart; [Reuse a pre-warmed checkout](self-hosted-environments-deploy.md#reuse-a-pre-warmed-checkout) covers the supported persistent-disk setup.

```python
claude self-hosted-runner --environment-secret-file '/etc/claude/environment-secret' --base-dir '<writable-dir>'
```

3

Verify the runner appears

Return to the [**Cloud environments** page](https://claude.ai/admin-settings/cloud-environments). Your environment’s status changes from **No runners deployed** to **Healthy** within a few seconds of the runner starting; open the environment and select **Activity** to see the runner itself.

4

Route a session to the environment

Start a session at claude.ai/code and select your environment from the environment picker, where self-hosted environments appear alongside Anthropic-hosted ones. The runner clones with whatever git credentials the host already has, so pick a repository this host can already clone, or a public one; credential options for private repositories in production are on [Configure git](self-hosted-environments-deploy.md#configure-git). The next available runner picks up the queued session and logs `Picked up session <session-id>` along with its active count and capacity, so you can confirm from the runner’s own output which host took the session. Watch the session work and read Claude’s replies at [claude.ai/code](https://claude.ai/code). If the session sits queued instead, see [Troubleshooting](self-hosted-environments-deploy.md#troubleshooting).

The runner exits by design once its active sessions finish; see [Runner lifecycle](self-hosted-environments.md#runner-lifecycle). For production, deploy it under an orchestrator that restarts it on exit. See [Deploy to production](self-hosted-environments-deploy.md).


[​](#send-a-follow-up-message-to-a-running-session)

Send a follow-up message to a running session

Once a session is running on your environment, send it a follow-up from the `claude` CLI on any machine where you’re logged in with `claude auth login`; the command doesn’t need to run from the machine that started the session. The command posts one message:

```python
claude -p "your message" --cloud <session-id>
```

For `<session-id>`, pass the bare `session_...` or `cse_...` ID or the session’s claude.ai/code URL. A successful send prints `Sent to cloud session.` with the session ID and a view link. Accepted ID forms, JSON output, the account and policy requirements, and the error reference are on [Send follow-ups from the CLI](../02-Claude-Code-CLI/claude-code-on-the-web.md#send-follow-ups-from-the-cli), since the command works the same against Anthropic-hosted sessions.


[​](#what’s-next)

What’s next

- [Deploy to production](self-hosted-environments-deploy.md): harden the deployment, control egress, configure git credentials, and run the fleet under Kubernetes or Compose
- [Customize sessions](self-hosted-environments-configuration.md): wrapper scripts, lifecycle hooks, on-demand runners, MCP servers, and permissions
- [Test end to end](self-hosted-environments-testing.md): a CI smoke test that dispatches a session and reads Claude’s replies
