---
title: "Get started with Claude Code in the cloud - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/web-quickstart"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-24T06:28:04Z"
tags: ["claude-code"]
---

## On this page

- [How sessions run](#how-sessions-run)
- [Compare ways to run Claude Code](#compare-ways-to-run-claude-code)
- [Connect GitHub](#connect-github)
  - [Connect from your terminal](#connect-from-your-terminal)
  - [Remove the /web-setup token](#remove-the-web-setup-token)
- [Start a task](#start-a-task)
- [Pre-fill sessions](#pre-fill-sessions)
- [Review and iterate](#review-and-iterate)
- [Troubleshoot setup](#troubleshoot-setup)
  - [No repositories appear after connecting GitHub](#no-repositories-appear-after-connecting-github)
  - [The page only shows a GitHub login button](#the-page-only-shows-a-github-login-button)
  - [”Not available for the selected organization”](#%E2%80%9Dnot-available-for-the-selected-organization%E2%80%9D)
  - [/web-setup says “Not signed in to Claude”](#%2Fweb-setup-says-%E2%80%9Cnot-signed-in-to-claude%E2%80%9D)
  - [/web-setup warns that your token doesn’t have the workflow scope](#%2Fweb-setup-warns-that-your-token-doesn%E2%80%99t-have-the-workflow-scope)
  - [/web-setup shows “No commands match” or “Unknown command”](#web-setup-shows-no-commands-match-or-unknown-command)
  - [”Could not create a cloud environment” or “No cloud environment available” when using --cloud](#%E2%80%9Dcould-not-create-a-cloud-environment%E2%80%9D-or-%E2%80%9Cno-cloud-environment-available%E2%80%9D-when-using-cloud)
  - [Setup script failed](#setup-script-failed)
  - [New sessions hang or time out during setup](#new-sessions-hang-or-time-out-during-setup)
  - [Session keeps running after closing the tab](#session-keeps-running-after-closing-the-tab)
- [Next steps](#next-steps)

Claude Code in the cloud

# Get started with Claude Code in the cloud

Copy pageCopy page

Run Claude Code in the cloud from your browser or phone. Connect a GitHub repository, submit a task, and review the PR without local setup.

Copy pageCopy page

Cloud sessions are available on Pro, Max, and Team plans, and for Enterprise users with premium seats or Chat + Claude Code seats.

A cloud session runs Claude Code on cloud infrastructure instead of your machine, Anthropic-managed by default. This quickstart starts one from [claude.ai/code](https://claude.ai/code) in your browser. You can also start one from the Claude mobile app, the Desktop app, or your terminal with `claude --cloud`. You’ll need a GitHub repository to [get started](#connect-github). Claude clones it into an isolated virtual machine, makes changes, and pushes a branch for you to review. Sessions persist across devices, so a task you start on your laptop is ready to review from your phone later. Cloud sessions work well for:

- **Parallel tasks**: run several independent tasks at once, each in its own session and branch, without managing multiple worktrees
- **Repos you don’t have locally**: Claude clones the repo fresh every session, so you don’t need it checked out
- **Tasks that don’t need frequent steering**: submit a well-defined task, do something else, and review the result when Claude is done
- **Code questions and exploration**: understand a codebase or trace how a feature is implemented without a local checkout

For work that needs your local config, tools, or environment, running Claude Code locally or using [Remote Control](remote-control.md) is a better fit.


[​](#how-sessions-run)

How sessions run

The steps below describe Anthropic-hosted sessions. In a [self-hosted environment](../13-Enterprise-Admin/self-hosted-environments.md), the clone and everything after it run on your organization’s own runners, where network boundaries, setup, and push behavior are operator-configured. When you submit a task:

1.  **Clone and prepare**: your repository is cloned to an Anthropic-managed VM, and your [setup script](cloud-environments.md#setup-scripts) runs if configured.
2.  **Configure network**: internet access is set based on your environment’s [access level](cloud-environments.md#access-levels).
3.  **Work**: Claude analyzes code, makes changes, runs tests, and checks its work. You can watch and steer throughout, or step away and come back when it’s done.
4.  **Push the branch**: when Claude reaches a stopping point, it pushes its branch to GitHub. You review the diff, leave inline comments, create a PR, or send another message to keep going.

The session doesn’t close when the branch is pushed. PR creation and further edits all happen within the same conversation.


[​](#compare-ways-to-run-claude-code)

Compare ways to run Claude Code

Claude Code behaves the same everywhere. What changes is where the session runs and whether your local configuration is available:

|                                                   | Cloud session                                                                                                       | Local session                                                                                                                           | Local session with [Remote Control](remote-control.md)    |
|:--------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------|
| **Code runs on**                                  | Cloud VM, Anthropic-managed by default                                                                              | Your machine                                                                                                                            | Your machine                                                    |
| **You start it from**                             | claude.ai/code, the Claude mobile app, the Desktop app with **Cloud** selected, or `claude --cloud`                 | Your terminal, your IDE, or the Desktop app with **Local** selected                                                                     | Your terminal, the VS Code extension, or the Desktop app        |
| **You chat from**                                 | claude.ai, the mobile app, or the Desktop app                                                                       | Where you started it                                                                                                                    | claude.ai or the mobile app, as well as where you started it    |
| **Uses your local config**                        | No, repo only                                                                                                       | Yes                                                                                                                                     | Yes                                                             |
| **Requires GitHub**                               | Yes, or [bundle a local repo](claude-code-on-the-web.md#send-local-repositories-without-github) via `--cloud` | No                                                                                                                                      | No                                                              |
| **Keeps running if you disconnect**               | Yes                                                                                                                 | No                                                                                                                                      | While the session stays open on your machine                    |
| **[Permission modes](permission-modes.md)** | Accept edits, Plan, Auto                                                                                            | All modes in the terminal; see [Switch permission modes](permission-modes.md#switch-permission-modes) for the IDE and Desktop app | Manual, Accept edits, or Plan from claude.ai and the mobile app |
| **Network access**                                | Configurable per environment                                                                                        | Your machine’s network                                                                                                                  | Your machine’s network                                          |

See the [terminal quickstart](../01-Getting-Started/quickstart.md), [Desktop app](../16-Mobile-Desktop/desktop.md), or [Remote Control](remote-control.md) docs to set up local sessions.


[​](#connect-github)

Connect GitHub

Connecting GitHub is a one-time step. If you already use the GitHub CLI, you can [do this from your terminal](#connect-from-your-terminal) instead of the browser.

On Team and Enterprise plans, the **Sign in with GitHub** step works only after an [Owner](../13-Enterprise-Admin/server-managed-settings.md#access-control) of your Claude organization turns on the GitHub connector at [**Admin settings \> Connectors**](https://claude.ai/admin-settings/connectors). Until then, that step shows “GitHub access is required for Claude Code on the web” instead of a sign-in button. After the connector is on, reload [claude.ai/code](https://claude.ai/code) and start again from the first step. A second toggle, [Quick web setup](claude-code-on-the-web.md#github-authentication-options) at [**Admin settings \> Claude Code**](https://claude.ai/admin-settings/claude-code), is optional: with it on, `/web-setup` works and onboarding creates the environment for members.

1

Visit claude.ai/code

Go to [claude.ai/code](https://claude.ai/code) and sign in with your claude.ai account.

2

Sign in with GitHub

After you sign in, claude.ai/code prompts you to connect GitHub. Follow the prompt, and claude.ai/code sends you to GitHub’s authorization page. Approve the authorization request, and GitHub returns you to claude.ai/code. Cloud sessions work with existing GitHub repositories. To start a new project, [create an empty repository on GitHub](https://github.com/new) first.With this connection, a session can clone any public repository, but can work in a private repository only when the Claude GitHub App is installed on it. [Install the Claude GitHub App](https://github.com/apps/claude/installations/new) on each GitHub account or organization whose private repositories you want to use. On a GitHub organization, an organization owner may need to approve the installation. Installing it also enables [Auto-fix](claude-code-on-the-web.md#auto-fix-pull-requests), which lets Claude respond to CI failures and review comments on pull requests in those repositories.If onboarding prompts you to install the Claude GitHub App at this point and you’d rather do it later, click **Skip**.

3

Set up your Default environment

A [cloud environment](cloud-environments.md) is the saved configuration that controls what network access Claude has during sessions and what runs when a session starts. What happens after you connect GitHub depends on your plan:

- **Pro and Max**: onboarding creates an environment named **Default** for you.
- **Team and Enterprise**: onboarding shows a **Create your first cloud environment** form. Leave the prefilled name and network access unchanged and click **Create & finish** to create the **Default** environment. If an Owner has turned on [Quick web setup](claude-code-on-the-web.md#github-authentication-options), onboarding creates **Default** for you instead.

**Default** uses [`Trusted` network access](cloud-environments.md#access-levels): sessions reach [common package registries](cloud-environments.md#default-allowed-domains) and other allowlisted domains, and nothing else through the session’s network. See [Installed tools](cloud-environments.md#installed-tools) for what’s available without any configuration.For a first project, the **Default** environment works as is. To change its network access, add environment variables, or run a [setup script](cloud-environments.md#setup-scripts) before sessions start, [edit it or create additional environments](cloud-environments.md#configure-your-environment).


[​](#connect-from-your-terminal)

Connect from your terminal

If you already use the GitHub CLI (`gh`), you can connect GitHub for cloud sessions from your terminal. This requires the [Claude Code CLI](../01-Getting-Started/quickstart.md). On Team and Enterprise plans, `/web-setup` is available only after an Owner turns on [Quick web setup](claude-code-on-the-web.md#github-authentication-options). When you run `/web-setup`, Claude Code reads the token that `gh auth token` prints, asks you to confirm, and sends the token to Anthropic. Anthropic stores it encrypted with your claude.ai account, and your cloud sessions use it for GitHub access until you [remove it](#remove-the-web-setup-token). A cloud session you start yourself can then access any repository that token can access, with no Claude GitHub App installation. Threads in a [project](claude-projects.md#set-up-github-access) still need the Claude GitHub App. If you already connected GitHub in the browser, `/web-setup` warns you that continuing replaces that connection for your cloud sessions.

Organizations with [Zero Data Retention](zero-data-retention.md) enabled cannot use `/web-setup` or other cloud session features. If the GitHub CLI isn’t installed or isn’t authenticated, Claude Code opens the browser onboarding flow instead.

1

Authenticate with the GitHub CLI

In your shell, authenticate the GitHub CLI if you haven’t already:

```python
gh auth login
```

2

Sign in to Claude

In the Claude Code CLI, run `/login` to sign in with your claude.ai account. Skip this step if you’re already signed in with a claude.ai account. Authenticating with an API key doesn’t count. To check, run `/status` and confirm the **Login method** row shows a claude.ai account.

3

Run /web-setup

In the Claude Code CLI, run:

```python
/web-setup
```

Confirm the prompt to send your `gh` token to your Claude account. On success, Claude Code prints `Connected as <your-github-username>` and opens [claude.ai/code](https://claude.ai/code) in your browser. If you don’t have a cloud environment yet, `/web-setup` creates one with Trusted network access and no setup script. You can [edit the environment or add variables](cloud-environments.md#configure-your-environment) afterward. Once `/web-setup` completes, you can start cloud sessions from your terminal with [`--cloud`](claude-code-on-the-web.md#from-terminal-to-cloud) or set up recurring tasks with [`/schedule`](web-scheduled-tasks.md).


[​](#remove-the-web-setup-token)

Remove the `/web-setup` token

To remove the token from your Claude account, disconnect GitHub at [claude.ai/customize/connectors](https://claude.ai/customize/connectors). Disconnecting deletes the GitHub credentials your cloud sessions use, whether they came from the browser or from `/web-setup`, so cloud sessions lose GitHub access until you connect again. Your local `gh` stays signed in, and the token remains valid on GitHub. To invalidate the token itself, revoke it on GitHub. If you signed in to `gh` through the browser, the token belongs to the **GitHub CLI** entry under [**Settings \> Applications \> Authorized OAuth Apps**](https://github.com/settings/applications) on GitHub, and revoking that entry also signs the GitHub CLI out on your machines. Cloud sessions then lose GitHub access until you run `gh auth login` and `/web-setup` again.


[​](#start-a-task)

Start a task

With GitHub connected and an environment created, you’re ready to submit tasks.

1

Select a repository and branch

From [claude.ai/code](https://claude.ai/code) or the Code tab in the Claude mobile app, click the repository selector below the input box and choose a repository for Claude to work in. Each repository shows a branch selector. Change it to start Claude from a feature branch instead of the default. You can add multiple repositories to work across them in one session.

2

Choose a permission mode

The mode dropdown next to the input shows the mode the session will run in:

- **Auto**: a classifier reviews Claude’s actions instead of asking you. Appears when your organization allows auto mode and the selected model supports it
- **Accept edits**: Claude makes changes and pushes a branch without stopping for approval
- **Plan**: Claude proposes an approach and waits for you to approve it before editing files

Cloud sessions don’t offer Manual or Bypass permissions. See the [full list of permission modes](permission-modes.md#available-modes) for what each one allows.

3

Describe the task and submit

Type a description of what you want and press Enter. Be specific:

- Name the file or function: “Add a README with setup instructions” or “Fix the failing auth test in `tests/test_auth.py`” is better than “fix tests”
- Paste error output if you have it
- Describe the expected behavior, not just the symptom

Claude clones the repositories, runs your setup script if configured, and starts working. Each task gets its own session and its own branch, so you don’t need to wait for one to finish before starting another.


[​](#pre-fill-sessions)

Pre-fill sessions

You can prefill the prompt, repositories, and environment for a new session by adding query parameters to the [claude.ai/code](https://claude.ai/code) URL. Use this to build integrations such as a button in your issue tracker that opens Claude Code with the issue description as the prompt.

| Parameter      | Description                                                                                                                                                      |
|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `prompt`       | Prompt text to prefill in the input box. The alias `q` is also accepted.                                                                                         |
| `prompt_url`   | URL to fetch the prompt text from, for prompts too long to embed in a query string. The URL must allow cross-origin requests. Ignored when `prompt` is also set. |
| `repositories` | Comma-separated list of `owner/repo` slugs to preselect. The alias `repo` is also accepted.                                                                      |
| `environment`  | Name or ID of the [environment](#connect-github) to preselect.                                                                                                   |

URL-encode each value. The example below opens the form with a prompt and a repository already selected:

```python
https://claude.ai/code?prompt=Fix%20the%20login%20bug&repositories=acme/webapp
```


[​](#review-and-iterate)

Review and iterate

When Claude finishes, review the changes, leave feedback on specific lines, and keep going until the diff looks right.

1

Open the diff view

A diff indicator shows lines added and removed across the session, for example `+42 -18`. Select it to open the diff view, with a file list on the left and changes on the right.The diff compares the session’s changes against its base branch by default. To compare against a different branch, select **Compare against** and pick one.

2

Leave inline comments

Select any line in the diff, type your feedback, and press Enter. Comments queue up until you send your next message, then they’re bundled with it. Claude sees “at `src/auth.ts:47`, don’t catch the error here” alongside your main instruction, so you don’t have to describe where the problem is.

3

Create a pull request

When the diff looks right, select **Create PR** at the top of the diff view. You can open it as a full PR, a draft, or jump to GitHub’s compose page with a generated title and description.

4

Keep iterating after the PR

The session stays live after the PR is created. Paste CI failure output or reviewer comments into the chat and ask Claude to address them. To have Claude monitor the PR automatically, see [Auto-fix pull requests](claude-code-on-the-web.md#auto-fix-pull-requests).


[​](#troubleshoot-setup)

Troubleshoot setup


[​](#no-repositories-appear-after-connecting-github)

No repositories appear after connecting GitHub

If you connected GitHub in the browser, sessions can clone any public repository, but a private repository appears only when the Claude GitHub App is installed on the account or organization that owns it and the installation’s repository access includes it. [Install the Claude GitHub App](https://github.com/apps/claude/installations/new) there, or ask an organization owner to install or approve it. If you connected with `/web-setup`, sessions reach every repository your `gh` token can access. Run `gh repo view OWNER/REPO` in your shell to check that your GitHub CLI login can see the repository, and run `/web-setup` again if you’ve switched `gh` accounts since connecting.


[​](#the-page-only-shows-a-github-login-button)

The page only shows a GitHub login button

Cloud sessions require a connected GitHub account. Connect via the browser flow above, or run `/web-setup` from your terminal if you use the GitHub CLI. If you’d rather not connect GitHub at all, see [Remote Control](remote-control.md) to run Claude Code on your own machine and monitor it from your browser or phone.


[​](#”not-available-for-the-selected-organization”)

”Not available for the selected organization”

Enterprise organizations may need an Owner to enable cloud sessions. Contact your Anthropic account team.


[​](#/web-setup-says-“not-signed-in-to-claude”)

`/web-setup` says “Not signed in to Claude”

If `/web-setup` responds with “Not signed in to Claude. Run /login first.”, the CLI doesn’t have a valid claude.ai sign-in. This can also happen when a previous sign-in has expired. Run `/login`, sign in with your claude.ai account, then run `/web-setup` again.


[​](#/web-setup-warns-that-your-token-doesn’t-have-the-workflow-scope)

`/web-setup` warns that your token doesn’t have the `workflow` scope

If `/web-setup` says your GitHub CLI token doesn’t have the `workflow` scope, you can continue, but GitHub can reject some pushes made with that token, such as pushes that change GitHub Actions workflow files. To add the scope, run `gh auth refresh -s workflow` in your shell, then run `/web-setup` again.


[​](#web-setup-shows-no-commands-match-or-unknown-command)

`/web-setup` shows “No commands match” or “Unknown command”

`/web-setup` runs inside the Claude Code CLI, not your shell. Launch `claude` first, then type `/web-setup` at the prompt. If you typed it inside Claude Code and the command menu shows `No commands match "/web-setup"`, or submitting it returns `Unknown command: /web-setup`, the command is hidden because a requirement isn’t met. The cause is usually that you’re authenticated with an API key or third-party provider instead of a claude.ai subscription. Run `/login` to sign in with your claude.ai account. On Team and Enterprise plans, the command is hidden by default: the [Quick web setup toggle](claude-code-on-the-web.md#github-authentication-options) is off until an Owner turns it on. While it’s off, [connect GitHub from the browser](#connect-github) instead. The command is also hidden in two other cases:

- An administrator has disabled cloud sessions for your organization. In this case, submitting `/web-setup` returns [`Cloud sessions are disabled by your organization's policy`](errors.md#cloud-sessions-are-disabled-by-your-organizations-policy). Before v2.1.268, this case also returned `Unknown command: /web-setup`.
- Your Enterprise organization has [Zero Data Retention](zero-data-retention.md) enabled, which makes cloud sessions unavailable.


[​](#”could-not-create-a-cloud-environment”-or-“no-cloud-environment-available”-when-using-cloud)

”Could not create a cloud environment” or “No cloud environment available” when using `--cloud`

Cloud session features create a default cloud environment automatically if you don’t have one. If you see “Could not create a cloud environment”, automatic creation failed. If you see “No cloud environment available”, your CLI predates automatic creation. In either case, run `/web-setup` in the Claude Code CLI, or add an environment from the [environment selector](cloud-environments.md#configure-your-environment) at [claude.ai/code](https://claude.ai/code).


[​](#setup-script-failed)

Setup script failed

The setup script exited with a non-zero status, which blocks the session from starting. Common causes:

- A package install failed because the registry isn’t in your [network access level](cloud-environments.md#access-levels). `Trusted` covers most package managers; `None` blocks them all.
- The script references a file or path that doesn’t exist in a fresh clone.
- A command that works locally needs a different invocation on Ubuntu.

To debug, add `set -x` at the top of the script to see which command failed. For non-critical commands, append `|| true` so they don’t block session start.


[​](#new-sessions-hang-or-time-out-during-setup)

New sessions hang or time out during setup

If new sessions stall on the setup script step or fail with a generic container error before the script finishes, the script is likely exceeding the roughly five-minute time budget for building the [environment cache](cloud-environments.md#environment-caching). Heavy steps such as pulling large Docker images, syncing full dependency trees, or downloading model weights often push the total over the limit, especially when they run one after another. To fix this, trim the script so it reliably finishes in under five minutes:

- Run independent installs in parallel with `&` and a final `wait` instead of running them serially.
- Move the largest downloads out of the setup script and into a [SessionStart hook](cloud-environments.md#setup-scripts-vs-sessionstart-hooks) that launches them in the background, so the session becomes usable while they finish.
- Remove long retry sleeps from the setup script, since a stalled retry loop counts against the budget.


[​](#session-keeps-running-after-closing-the-tab)

Session keeps running after closing the tab

This is by design. Closing the tab or navigating away doesn’t stop the session. It continues running in the background until Claude finishes the current task, then idles. From the sidebar, you can [archive a session](claude-code-on-the-web.md#archive-sessions) to hide it from your list, or [delete it](claude-code-on-the-web.md#delete-sessions) to remove it permanently.


[​](#next-steps)

Next steps

Now that you can submit and review tasks, these pages cover what comes next: starting cloud sessions from your terminal, scheduling recurring work, and giving Claude standing instructions.

- [Use Claude Code in the cloud](claude-code-on-the-web.md): the full reference, including teleporting sessions to your terminal, session sharing, and auto-fixing pull requests
- [Configure cloud environments](cloud-environments.md): network access levels, environment variables, and setup scripts for cloud sessions
- [Routines](web-scheduled-tasks.md): automate work on a schedule, via API call, or in response to GitHub events
- [CLAUDE.md](memory.md): give Claude persistent instructions and context that load at the start of every session
- Install the Claude mobile app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) or [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) to monitor sessions from your phone. From the Claude Code CLI, `/mobile` shows a QR code for [claude.ai/mobile](https://claude.ai/mobile) that opens the right app store for your phone.
