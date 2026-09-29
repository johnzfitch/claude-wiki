---
title: "Install and manage plugins - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/discover-plugins"
category: "08-Plugins-Skills"
fetched_at: "2026-09-29T06:29:32Z"
tags: ["claude-code", "plugins"]
---

## On this page

- [Install a plugin](#install-a-plugin)
  - [Choose an install scope](#choose-an-install-scope)
  - [JetBrains, non-interactive runs, and the Agent SDK](#other-places-you-run-claude-code)
  - [Plugins from your claude.ai account](#plugins-from-your-claude-ai-account)
  - [Install from your shell](#install-from-your-shell)
- [Add a marketplace](#add-a-marketplace)
  - [Add a marketplace and install in one command](#add-a-marketplace-and-install-in-one-command)
  - [Add a private marketplace](#add-a-private-marketplace)
  - [Add a marketplace from claude.ai](#add-from-claude-ai)
- [Manage installed plugins](#manage-installed-plugins)
  - [Manage plugins synced from claude.ai](#manage-plugins-synced-from-claude-ai)
  - [Uninstall a plugin the project enables](#uninstall-a-plugin-the-project-enables)
  - [See what an installed plugin adds to your sessions](#see-what-an-installed-plugin-adds-to-your-sessions)
  - [Find plugins you no longer use](#find-plugins-you-no-longer-use)
  - [Plugins with dependencies](#plugins-with-dependencies)
  - [Manage plugins from your shell](#manage-plugins-from-your-shell)
- [Keep plugins updated](#keep-plugins-updated)
  - [Turn auto-update on or off for a marketplace](#turn-auto-update-on-or-off-for-a-marketplace)
  - [Update one plugin now](#update-one-plugin-now)
  - [Auto-update from a private marketplace](#auto-update-from-a-private-marketplace)
- [Manage marketplaces](#manage-marketplaces)
- [Next steps](#next-steps)

Use plugins

# Install and manage plugins

Copy pageCopy page

Install Claude Code plugins from a marketplace on any surface you use, choose an install scope, and update or remove them later.

Copy pageCopy page

Installing a plugin adds its skills, agents, hooks, and MCP servers to Claude Code on your machine. This page is for anyone using plugins on their own machine or account, whether in the terminal, the desktop app, an IDE, or a cloud session: it covers installing, choosing a scope, adding marketplaces, and keeping plugins updated.

These cases are covered on other pages:

- **You use claude.ai chat or Cowork, not Claude Code**: see [Plugins on claude.ai and in Cowork](https://claude.com/docs/plugins/overview)
- **Claude Code printed an error**: find it in [Troubleshoot plugins](plugins-troubleshooting.md)

Start with [Install a plugin](#install-a-plugin). If someone sent you an install command whose `@` name isn’t `claude-plugins-official`, [add that marketplace](#add-a-marketplace) first.


[​](#install-a-plugin)

Install a plugin

As an example, this section installs [`commit-commands`](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/commit-commands) from [Anthropic’s official marketplace](plugins-anthropic-marketplaces.md), which adds commands for committing, pushing, and opening pull requests. The same steps install any other plugin: substitute its name and its marketplace’s name wherever `commit-commands` and `claude-plugins-official` appear. If that plugin comes from a different marketplace, [add the marketplace](#add-a-marketplace) first. Pick the tab for where you run Claude Code.

- Terminal

- Desktop app

- VS Code

- Cloud session

Start Claude Code with `claude` in your project, then:

1

Open the plugin's details with the install command

Run `/plugin install` with the plugin’s name and marketplace. In a session, this command doesn’t install right away: it opens the `/plugin` panel on that plugin’s details so you can review it and choose a scope first.

```python
/plugin install commit-commands@claude-plugins-official
```

To browse instead, run `/plugin` with no plugin name: the panel opens on the **Discover** tab, which lists plugins from every marketplace you’ve added, and you can type to search, then press **Enter** on a plugin to open its details.

2

Review what the plugin adds

The details pane shows the plugin’s description. It can also show:

- **Will install**: the commands, agents, skills, hooks, and MCP and LSP servers the plugin adds.
- **Last updated**: shown for a plugin in Anthropic’s official marketplace.
- **Context cost**: for a plugin in Anthropic’s official marketplace, two token estimates. **Every turn** is what the plugin adds to each message you send, and **When invoked** is what its skills and agents add once Claude loads them. The estimates appear when you open the plugin by naming its marketplace, as the step 1 command does, or from the **Marketplaces** tab. The details pane you reach from the **Discover** list doesn’t show them.

Plugins from a local or custom marketplace can show `Components will be discovered at installation` instead.A plugin can run hooks and MCP servers, so read the pane before you install. See [Plugin security and trust](plugins-security.md).

3

Choose a scope

Select one of the three install options:

- **Install for you (user scope)**: you get the plugin in every project on this machine
- **Install for all collaborators on this repository (project scope)**: it’s enabled for everyone who works in this repository
- **Install for you, in this repo only (local scope)**: you get it in this repository only

[Choose an install scope](#choose-an-install-scope) says which settings file each one writes to and which applies when the same plugin is set at more than one.After you select a scope, Claude Code installs the plugin along with any dependencies it declares, then prints an install summary.

4

Read the install summary

The last sentence of the summary tells you whether the plugin is usable in this session yet:

- **Active now**: `Plugin is now active.` No reload is needed.
- **Reload needed**: `Run /reload-plugins to activate.` The panel closes and Claude Code runs that reload for you. If the reload would [invalidate the prompt cache](../02-Claude-Code-CLI/prompt-caching.md#enabling-or-disabling-a-plugin), it warns and leaves the plugin pending instead. Run `/reload-plugins --force` to activate it anyway, which costs one uncached request.
- **Load failed**: `The plugin couldn't be loaded`. Open the **Errors** tab in `/plugin` for the reason, then see [After install: plugin not working](plugins-troubleshooting.md#plugin-installed-but-not-working).

5

Confirm the plugin works

Type `/` and look for the plugin’s skills under its name, in the form `/<plugin>:<skill>`. For `commit-commands`, `/commit-commands:commit` appears. Two other places list the plugin too:

- Open the **Installed** tab in `/plugin`, which lists the plugin with its scope.
- In your shell, run `claude plugin list`, which prints the same list with `Version`, `Scope`, and `Status` lines.

If `/commit-commands:commit` doesn’t appear, see [After install: plugin not working](plugins-troubleshooting.md#plugin-installed-but-not-working).

Installing from any other marketplace requires one extra step first: [add the marketplace](#add-a-marketplace). Claude Code adds Anthropic’s official marketplace for you the first time you start an interactive terminal session, which is why the example skips that step. If you found a plugin on [claude.com/marketplace](https://claude.com/marketplace), its **Claude Code** button copies the install command in its [shell form](#install-from-your-shell), `claude plugin install <name>@claude-plugins-official`.

In a local or SSH session in the desktop app’s **Code** tab:

1

Open the plugin browser

Click the **+** button next to the prompt box and select **Plugins**, then **Add plugin**. The plugin browser opens with the plugins from your marketplaces.

2

Select the plugin

Find `commit-commands` and select it.

3

Choose a scope

Choose a [scope](#choose-an-install-scope): your user account, this project, or local-only.

To enable, disable, or uninstall later, use **+ \> Plugins \> Manage plugins**. The plugin browser isn’t available in the desktop app’s cloud sessions. See [Install plugins in the desktop app](../16-Mobile-Desktop/desktop.md#install-plugins).

In the Claude Code panel in VS Code:

1

Open Manage plugins

Type `/plugins` in the prompt box to open **Manage plugins**.

2

Install the plugin

On the **Plugins** tab, search for `commit-commands` and click **Install**. If the tab lists no plugins, add `anthropics/claude-plugins-official` on the **Marketplaces** tab first.

3

Choose a scope

Choose a [scope](#choose-an-install-scope): **Install for you**, **Install for this project**, or **Install locally**.

Your changes apply to open sessions without a restart. See [Manage plugins in VS Code](../03-IDE-Integrations/vs-code.md#manage-plugins).

A [cloud session](../02-Claude-Code-CLI/cloud-environments.md), including [the browser at claude.ai/code](../02-Claude-Code-CLI/claude-code-on-the-web.md), has no plugin browser and doesn’t load the plugins you installed on your own machine or the ones your repository’s `.claude/settings.json` turns on. For plugins your organization distributes through managed settings, see [Manage plugins for your organization](plugins-org.md).See [which parts of your setup are also available in a cloud session](../02-Claude-Code-CLI/cloud-environments.md#what-carries-over-from-your-setup) for the rest of your setup.


[​](#choose-an-install-scope)

Choose an install scope

A plugin’s install scope decides who gets the plugin and which settings file records it as enabled:

- **User scope**: the plugin is enabled for you in every project on this machine. The entry goes in `enabledPlugins` in `~/.claude/settings.json`.
- **Project scope**: the plugin is enabled for everyone who works in this repository. The entry goes in `.claude/settings.json`, which you commit. Committing that entry turns the plugin on for your collaborators but doesn’t download it to their machines, so each collaborator also runs `claude plugin install <name>@<marketplace> --scope project` once; see [Enabled in project settings but not installed](plugins-loading.md#enabled-in-project-settings-but-not-installed).
- **Local scope**: the plugin is enabled for you in this repository only. The entry goes in `.claude/settings.local.json`.

Some plugins are set by their author to start turned off, through the [`defaultEnabled`](plugins-reference.md#defaultenabled) field. Such a plugin is installed but stays off until you turn it on with `claude plugin enable <name>` in your shell, or from the **Installed** tab of `/plugin` in a session. When the same plugin is set at several scopes, the local setting overrides the project setting, and the project setting overrides the user setting. See [Find where a plugin is enabled](plugins-loading.md#find-where-a-plugin-is-enabled) for the full rule. The terminal, the desktop app’s local sessions, and the VS Code extension on one computer read the same settings files, so a plugin you install at user scope in any of them is available in the other two.


[​](#other-places-you-run-claude-code)

JetBrains, non-interactive runs, and the Agent SDK

Some places you run Claude Code have no plugin browser of their own:

- **JetBrains IDEs**: the JetBrains plugin runs Claude Code in the IDE’s terminal, so use the **Terminal** tab’s steps there.
- **`claude -p` and other non-interactive runs**: `/plugin` doesn’t run, and Claude replies `/plugin isn't available in this environment.` Plugins you already installed do load. Install and manage them from your shell with [`claude plugin` commands](#install-from-your-shell).
- **Agent SDK**: load plugins through the SDK’s plugin option. See [Load plugins in the Agent SDK](../05-Agent-SDK/agent-sdk-plugins.md).

If Claude Code reports that a plugin enabled in the repository’s `.claude/settings.json` isn’t installed, see [Enabled in project settings but not installed](plugins-loading.md#enabled-in-project-settings-but-not-installed).

If you’re a plugin author testing a copy of your plugin on disk, start Claude Code from your shell with `--plugin-dir` to load it for one session instead of installing it. See [Flags that load a plugin for one session](plugins-cli-reference.md#flags-that-load-a-plugin-for-one-session).


[​](#plugins-from-your-claude-ai-account)

Plugins from your claude.ai account

Your claude.ai account is a separate source of plugins, alongside the marketplaces you install from:

- **What arrives**: every plugin you turn on for your claude.ai account, and every plugin your organization turns on for its members. In a terminal session they sync in the background each time you start Claude Code while signed in with that account; in Cowork sessions they download when the session starts.
- **Where you see them**: in `/plugin` and `claude plugin list` under the ID `<name>@synced`. You can turn one off at your own scope unless your organization requires it.
- **What doesn’t go the other way**: plugins you install with `/plugin` or `claude plugin install` stay on this machine and aren’t added to your claude.ai account.

For sync timing, sign-in requirements, and turning sync off, see [Plugins synced from claude.ai](plugins-loading.md#synced-plugins).


[​](#install-from-your-shell)

Install from your shell

Run `claude plugin install` in your shell to install a plugin without starting a Claude Code session, for example from a setup script.

- **Scope**: user scope by default. Pass `--scope project` or `--scope local` to change it.
- **When the plugins load**: plugins it installs load the next time you start Claude Code, or when you run `/reload-plugins` in a session that’s already open.
- **The marketplace must be added first**: on a machine where no one has opened an interactive Claude Code session yet, the official marketplace isn’t registered, so a script that installs from it runs `claude plugin marketplace add anthropics/claude-plugins-official` before the install.

```python
claude plugin install formatter@your-org --scope project
```

The command prints `Successfully installed plugin: formatter@your-org (scope: project)` when it finishes. Some plugins install by running a command that their marketplace names, called a [`command` source](plugins-marketplace-reference.md#command-plugin-source). Claude Code shows you that command and asks you to accept it before it runs. A script has no one to answer that prompt, so pass `--yes` there to accept it. For every `claude plugin install` flag, see [plugin install](plugins-cli-reference.md#plugin-install).


[​](#add-a-marketplace)

Add a marketplace

You only need this section when the plugin you want isn’t in Anthropic’s official marketplace, for example one a coworker published or one from Anthropic’s community marketplace. A marketplace is a catalog of plugins, and Claude Code has to know about a marketplace before you can install from it. You add a marketplace once. After that, its plugins appear on the **Discover** tab and install with `/plugin install <plugin>@<marketplace>` in a session or `claude plugin install <plugin>@<marketplace>` in your shell, where `<marketplace>` is the name the marketplace registered under. To do both in one step, see [Add a marketplace and install in one command](#add-a-marketplace-and-install-in-one-command). In a Claude Code session, run `/plugin marketplace add` followed by the marketplace’s source: a GitHub repository, a git repository on any host, a local directory or file, or a hosted `marketplace.json`.

| Source                     | What you type                                                                                                                                                                                                                       | Example                                                                                                                        |
|:---------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| GitHub repository          | `owner/repo`. Add `#ref` to pin a branch or tag.                                                                                                                                                                                    | `/plugin marketplace add anthropics/claude-code`, or `/plugin marketplace add your-org/plugins#v1.2.0` to pin the `v1.2.0` tag |
| Git repository on any host | The full clone URL. Add `#ref` to pin a branch or tag.                                                                                                                                                                              | `/plugin marketplace add https://gitlab.example.com/your-group/your-marketplace.git#v1.0.0`                                    |
| Local directory or file    | A relative or absolute path to a directory that holds `.claude-plugin/marketplace.json`, or to the JSON file itself. Start a relative path with `./` or `../`, because Claude Code reads a bare `name/name` as a GitHub repository. | `/plugin marketplace add ./my-marketplace`                                                                                     |
| Hosted `marketplace.json`  | Its `https://` URL                                                                                                                                                                                                                  | `/plugin marketplace add https://example.com/marketplace.json`                                                                 |

From your shell, `claude plugin marketplace add` takes the same sources.

`/plugin market` also works as a shorter form of `/plugin marketplace`.

Include the `https://` prefix on every URL, or use the `git@host:path` form for SSH. If you type a bare `gitlab.example.com/your-group/your-marketplace.git`, Claude Code reads it as GitHub `owner/repo` shorthand and rejects it. When the command succeeds, it prints `Successfully added marketplace: <name>`, and the marketplace’s plugins appear on the **Discover** tab the next time you open `/plugin`, with no reload needed. If it fails, match the error message in [Troubleshoot plugins](plugins-troubleshooting.md#add-a-marketplace).


[​](#add-a-marketplace-and-install-in-one-command)

Add a marketplace and install in one command

To install a plugin from a marketplace you haven’t added yet, run `/plugin install` in a Claude Code session and name the marketplace source with `--marketplace`. Requires Claude Code v2.1.275 or later.

```python
/plugin install deploy-helper --marketplace your-org/plugins
```

The source takes [the same forms as `/plugin marketplace add`](#add-a-marketplace), such as GitHub `owner/repo`, a git URL, or a local path, except that it can’t contain spaces. Give the plugin name by itself, without an `@marketplace` suffix. If you haven’t added that marketplace yet, Claude Code shows the source it resolved and asks you to confirm before adding it. Once the marketplace is added, the plugin’s details open and you choose an [installation scope](#install-a-plugin). If the source matches a marketplace you’ve already added, Claude Code skips the confirmation and opens the plugin’s details in that marketplace.


[​](#add-a-private-marketplace)

Add a private marketplace

A private marketplace is one in a repository you need credentials to clone, on GitHub or any other git host. You add it with the same `/plugin marketplace add` or `claude plugin marketplace add` command as a public one. Claude Code clones it with the git credentials already on your machine and never prompts, so each way of connecting has a requirement:

- **HTTPS**: your git credential helpers apply, so access you set up with `gh auth login`, the macOS Keychain, or `git-credential-store` works. Interactive prompts are suppressed, so a host you have never authenticated to fails instead of asking for a password.
- **SSH**: the host must already be in your `known_hosts` file and the key must work without a passphrase prompt, because the host-fingerprint and passphrase prompts are suppressed too.
- **GitHub `owner/repo` shorthand**: Claude Code checks whether your SSH key authenticates to `github.com`, then clones over SSH if it does and over HTTPS if it doesn’t. Set [`CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1`](../02-Claude-Code-CLI/env-vars.md#variables) to skip that check and always clone over HTTPS.

The same credentials apply when you run `/plugin install`, `/plugin marketplace update`, and `claude plugin update`. On a GitHub Enterprise Server host, see [Plugin marketplaces on GHES](../02-Claude-Code-CLI/github-enterprise-server.md#plugin-marketplaces-on-ghes) for the credentials each operation needs. If your organization registers the marketplace for you through managed settings, you don’t add it yourself. See [Pre-install and require plugins](plugins-org.md#pre-install-and-require-plugins).


[​](#add-from-claude-ai)

Add a marketplace from claude.ai

In terminal sessions where [plugins sync from your claude.ai account](plugins-loading.md#synced-plugins), claude.ai can also list plugin marketplaces for you, such as your organization’s plugin library and your own claude.ai uploads. You add one of these by its name rather than by a source. Adding a marketplace from claude.ai requires Claude Code v2.1.273 or later. Add a claude.ai marketplace from the `/plugin` panel or from your shell:

- **Inside a session**: run `/plugin` and go to the **Marketplaces** tab, which lists the marketplaces from claude.ai. Select one there to add it.
- **From your shell**: run `claude plugin marketplace list`, which prints them in a `From claude.ai:` section. Then run `claude plugin marketplace add` with the `--claudeai` flag and the name shown in the list.

For example, this command adds a marketplace named `claudeai-organization-library`:

```python
claude plugin marketplace add --claudeai claudeai-organization-library
```

Claude Code registers the marketplace under a local name that starts with `claudeai-`, derived from the name that claude.ai lists it under. For example, a marketplace listed as “Organization library” becomes `claudeai-organization-library`. Install its plugins by that name, for example with `claude plugin install <plugin>@claudeai-organization-library`. If you sign out, or sign in to a different claude.ai organization, the marketplace stays configured but shows no plugins, and the plugins you already installed from it keep loading. The `From claude.ai:` section can also list git-based marketplaces shared through claude.ai, and it prints a source for each of those. Add them by that source as in [Add a marketplace](#add-a-marketplace), not with `--claudeai`.


[​](#manage-installed-plugins)

Manage installed plugins

The **Installed** tab in `/plugin` lists your plugins with actions to enable, disable, update, or uninstall each one. In a Claude Code session, run `/plugin` and press **Tab** to reach it, or run `/plugin enable`, `/plugin disable`, or `/plugin uninstall` to open the panel and make that change there. Disabled plugins are grouped under a collapsed header at the bottom of the list. Use these keys on the list:

- Type to filter by name or description.
- Press **Space** to enable or disable the selected plugin, and **f** to favorite it.
- Press **Enter** to open a plugin’s details. The menu there offers **Disable plugin** or **Enable plugin**, **Update now**, and **Uninstall**. Plugins that take settings also offer **Configure options**.

The tab can also show plugins at **Managed** scope. Your organization installed those through [managed settings](../02-Claude-Code-CLI/settings.md#settings-files), and you can’t enable, disable, or uninstall them here. For a synced plugin that your organization requires on claude.ai, see [Manage plugins synced from claude.ai](#manage-plugins-synced-from-claude-ai). When you close the `/plugin` panel with pending changes you made in it, Claude Code runs `/reload-plugins` for you to apply them. If the reload would [invalidate the prompt cache](../02-Claude-Code-CLI/prompt-caching.md#enabling-or-disabling-a-plugin), it warns and leaves the changes pending instead. Run `/reload-plugins --force` to apply them anyway.


[​](#manage-plugins-synced-from-claude-ai)

Manage plugins synced from claude.ai

The **Installed** tab in `/plugin` also lists the [plugins synced from your claude.ai account](plugins-loading.md#synced-plugins), with `synced` as their source. Synced plugins appear in terminal sessions on Claude Code v2.1.273 or later.

- **Enable or disable**: use the **Installed** tab, unless your organization marked the plugin as required.
- **Remove**: turn the plugin off on claude.ai.

When Claude Code syncs an added, updated, or removed plugin into an interactive session, you see `Plugins changed. Run /reload-plugins to activate.` Run `/reload-plugins` to load the change in that session, or leave it for the next time you start Claude Code.


[​](#uninstall-a-plugin-the-project-enables)

Uninstall a plugin the project enables

When you choose **Uninstall** for a plugin that this repository’s `.claude/settings.json` enables, whether from the **Installed** tab or with `/plugin uninstall`, Claude Code asks whether to disable it for you or uninstall it for everyone:

- **Disable for me**: press **y**. Claude Code writes `false` for the plugin in your `.claude/settings.local.json` and leaves it installed for the project.
- **Uninstall for everyone**: press **u**. Claude Code removes the plugin from the shared `.claude/settings.json`.


[​](#see-what-an-installed-plugin-adds-to-your-sessions)

See what an installed plugin adds to your sessions

In your shell, run `claude plugin details <name>` for an installed plugin. The `Always-on` line is the number of tokens the plugin adds to every session where it’s enabled, and the per-component rows show which skill or agent contributes most. For the full output and what each figure means, see [Measure what a plugin costs](plugins-measure.md#measure-what-a-plugin-costs).


[​](#find-plugins-you-no-longer-use)

Find plugins you no longer use

On the **Installed** tab in `/plugin`, plugins you installed yourself and haven’t used recently appear under a **Not used recently** header, and each plugin’s details show a **Last used** line. Use that header and that line to find plugins that still add startup and context cost, then disable or uninstall them.


[​](#plugins-with-dependencies)

Plugins with dependencies

A plugin can declare other plugins that it depends on. When you install, disable, or uninstall such a plugin from a marketplace, Claude Code acts on those dependencies too:

- **Install**: Claude Code also installs and enables the plugin’s declared dependencies at the same scope. The success message lists them.
- **Enable**: Claude Code also enables the plugin’s dependencies that are installed but disabled. If a declared dependency isn’t installed, the enable fails and the message tells you to install it first.
- **Disable**: when another enabled plugin still needs the one you named, Claude Code refuses and prints a chained command that disables both in the right order.
- **Uninstall**: auto-installed dependencies stay until you run `claude plugin prune` in your shell; see [plugin prune](plugins-cli-reference.md#plugin-prune).

If you loaded the plugin with `--plugin-dir` instead, see [Test a plugin and its dependency locally](plugins-dependencies.md#test-a-plugin-and-its-dependency-locally).


[​](#manage-plugins-from-your-shell)

Manage plugins from your shell

You can also manage plugins without starting a Claude Code session. In your shell, run `claude plugin install`, `enable`, `disable`, or `uninstall` as ordinary terminal commands; they change the same settings the `/plugin` panel does. Each takes `--scope` to target one scope, and uses a default scope when you omit it:

- `enable` and `disable` act on the most specific scope whose settings already list the plugin.
- `install` and `uninstall` act on user scope.

For example, these commands disable and re-enable a plugin, then uninstall it at project scope:

```python
claude plugin disable formatter@your-org
claude plugin enable formatter@your-org
claude plugin uninstall formatter@your-org --scope project
```


[​](#keep-plugins-updated)

Keep plugins updated

Plugins update automatically when the marketplace they came from has auto-update turned on. After a session starts, Claude Code refreshes those marketplaces and updates the on-disk copies of the plugins you installed from them. The running session keeps the versions it already loaded. After an update, you see `Plugin updated: <name> · Run /reload-plugins to apply`, and the next session loads the new versions automatically. These are the auto-update defaults for each kind of marketplace:

- **On by default**: `claude-plugins-official` and the other [official marketplace names](plugins-security.md#official-marketplace-names) except `knowledge-work-plugins` and `first-party-plugins`, plus [marketplaces added from claude.ai](#add-from-claude-ai).
- **Off by default**: every other marketplace, including the community marketplace, third-party marketplaces, and local development marketplaces.

For when auto-update runs, which plugins it skips, and the environment variables that turn it off, see [When auto-update runs](plugins-loading.md#when-auto-update-runs).


[​](#turn-auto-update-on-or-off-for-a-marketplace)

Turn auto-update on or off for a marketplace

In a Claude Code session, run `/plugin` and go to the **Marketplaces** tab. Select the marketplace, then select **Enable auto-update** or **Disable auto-update**.


[​](#update-one-plugin-now)

Update one plugin now

In a session, open the plugin on the **Installed** tab in `/plugin` and select **Update now**, or in your shell run `claude plugin update <plugin>@<marketplace>`.


[​](#auto-update-from-a-private-marketplace)

Auto-update from a private marketplace

For a private marketplace, see [What background auto-update does with credentials](plugins-host-marketplace.md#what-background-auto-update-does-with-credentials) for how background auto-updates authenticate over SSH and HTTPS, and [Troubleshoot plugins](plugins-troubleshooting.md#add-a-marketplace) for the messages you see when they fail.


[​](#manage-marketplaces)

Manage marketplaces

The **Marketplaces** tab in `/plugin` lists every marketplace you registered, along with its source. Select one to browse its plugins, update its listing, turn auto-update on or off, or remove it. You can also list, update, and remove marketplaces with commands, from your shell or inside a session:

| Action                         | In your shell                             | Inside a session                    |
|:-------------------------------|:------------------------------------------|:------------------------------------|
| List marketplaces              | `claude plugin marketplace list`          | `/plugin marketplace list`          |
| Update a marketplace’s listing | `claude plugin marketplace update <name>` | `/plugin marketplace update <name>` |
| Remove a marketplace           | `claude plugin marketplace remove <name>` | `/plugin marketplace remove <name>` |

When you remove a marketplace, Claude Code uninstalls every plugin you installed from it and removes their `enabledPlugins` entries from your settings files. The **Marketplaces** tab names those plugins before it asks you to confirm.


[​](#next-steps)

Next steps

- [Anthropic’s marketplaces](plugins-anthropic-marketplaces.md): how the official, community, and demo marketplaces differ and where to browse each one
- [Plugin loading reference](plugins-loading.md): why a plugin loaded, didn’t load, or didn’t change after an update
- [Plugin security and trust](plugins-security.md): what to review before you install a plugin from a marketplace you don’t know
- [Troubleshoot plugins](plugins-troubleshooting.md): install and marketplace error messages with their fixes
- [Create a plugin](plugins-create.md): build your own
