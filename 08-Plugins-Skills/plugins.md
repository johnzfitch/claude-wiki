---
title: "Plugins overview - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/plugins"
category: "08-Plugins-Skills"
fetched_at: "2026-09-30T06:31:53Z"
tags: ["claude-code", "plugins"]
---

## On this page

- [Understand what a plugin is](#understand-what-a-plugin-is)
  - [Decide whether you need a plugin](#decide-whether-you-need-a-plugin)
  - [What an enabled plugin adds to your sessions](#what-an-enabled-plugin-adds-to-your-sessions)
- [Get plugins from a marketplace](#get-plugins-from-a-marketplace)
  - [Make an installed plugin available in your session](#make-an-installed-plugin-available-in-your-session)
- [Tell Anthropic’s marketplaces from third-party ones](#tell-anthropic%E2%80%99s-marketplaces-from-third-party-ones)
- [Understand install scopes](#understand-install-scopes)
- [Next steps](#next-steps)

Plugins

# Plugins overview

Copy pageCopy page

Understand what a Claude Code plugin is, when you need one instead of a standalone skill or MCP server, and which page to read to install or create one.

Copy pageCopy page

A Claude Code plugin is a directory of skills, agents, hooks, MCP servers, or other components that Claude Code installs and loads as one unit. Most plugins come from a marketplace, which is a catalog that lists plugins and where to fetch each one. You can also load a plugin from a folder someone gives you, or [build your own](plugins-create.md).

Start on claude.com instead if either of these describes you:

- **You use claude.ai chat or Cowork and not Claude Code**: see [Plugins on claude.ai and in Cowork](https://claude.com/docs/plugins/overview)
- **You built an MCP server and want it in Anthropic’s directory**: see [Publish to the directory](https://claude.com/docs/directory/publish)

To try a plugin now, run `/plugin` in a Claude Code terminal session and install one from the **Discover** tab, which lists the plugins from Anthropic’s official marketplace and any marketplace you’ve added. From there:

- [Install and manage plugins](discover-plugins.md): the full install steps, scopes, and other surfaces
- [Create a plugin](plugins-create.md): build your own
- [Decide whether you need a plugin](#decide-whether-you-need-a-plugin): whether a plugin is the right tool for what you want


[​](#understand-what-a-plugin-is)

Understand what a plugin is

A plugin is a directory of components, usually with a manifest. The manifest, a JSON file at `.claude-plugin/plugin.json`, gives the plugin its name and can add a version, a description, and other [metadata](plugins-reference.md). The components are what the plugin adds to Claude Code, such as:

- [**Skills**](plugins-components.md#skills): `SKILL.md` instructions Claude loads when relevant, and that you can also run as a command
- [**Agents**](plugins-components.md#agents): subagent definitions Claude can delegate to
- [**Hooks**](plugins-components.md#hooks): commands Claude Code runs at points in its lifecycle, such as after every edit
- [**MCP servers**](plugins-components.md#mcp-servers): tool servers Claude Code connects to while the plugin is enabled

This diagram shows a plugin named `my-plugin` that holds one of each of those components, and what you get from each file once the plugin loads.

For every component type a plugin can hold, with an example of each, see [Plugin components](plugins-components.md). To see where each piece is located in a plugin’s directory, use the [plugin explorer](plugins-components.md#explore-the-plugin-directory) on that page.


[​](#decide-whether-you-need-a-plugin)

Decide whether you need a plugin

Skills, subagents, hooks, and MCP servers all work on their own, without a plugin. A skill you save in `~/.claude/skills/`, for example, is available in every project on your machine. To set one up on its own, see [Skills](skills.md), [Subagents](../09-Agents-Patterns/sub-agents.md), [Hooks](../07-Hooks/hooks-guide.md), or [MCP](../06-MCP-Tools/General/mcp.md). Use a plugin when you want several skills, subagents, hooks, or MCP servers packaged as one unit. Install one to get a setup someone else built, with one command and updates from its marketplace. Make one to give your own setup to teammates, install it in many projects, or publish versioned releases.


[​](#what-an-enabled-plugin-adds-to-your-sessions)

What an enabled plugin adds to your sessions

An enabled plugin is part of every session, not only the sessions where you use it. That has a few consequences worth knowing before you install one:

- **Context and usage**: for each skill, agent, and command that [Claude can invoke on its own](skills.md#control-who-invokes-a-skill), the name and description are in Claude’s context on every turn so that Claude knows it exists. Those tokens count toward your usage and leave less room in the [context window](../02-Claude-Code-CLI/context-window.md) even in sessions where nothing from the plugin runs. The full text of a skill or agent loads only when it’s used. What the plugin’s MCP servers add per turn follows [MCP tool search](../06-MCP-Tools/General/mcp.md#scale-with-mcp-tool-search).
- **Processes**: MCP servers the plugin defines run alongside each session where it’s enabled, and its hooks fire at their events.
- **Permissions**: what the plugin runs, it runs as you. See [Plugin security and trust](plugins-security.md) for what to review first.

You can check a plugin’s footprint at each stage:

- **Before you install**: open the plugin from the **Marketplaces** tab in `/plugin`. Plugins in Anthropic’s official marketplace show a **Context cost** estimate there.
- **After you install**: [Measure what a plugin costs](plugins-measure.md#measure-what-a-plugin-costs) shows how to read a plugin’s footprint, and the **Installed** tab’s **Not used recently** group lists plugins you could turn off.
- **To stop it without uninstalling**: disable the plugin with `/plugin` or, in your shell, `claude plugin disable`. See [Manage installed plugins](discover-plugins.md#manage-installed-plugins).


[​](#get-plugins-from-a-marketplace)

Get plugins from a marketplace

A marketplace is a repository or directory with a `.claude-plugin/marketplace.json` file that lists plugins and where to fetch each one. It’s a catalog, not a hosted store. You add a marketplace once, then install plugins from it by name, such as `commit-commands@claude-plugins-official`.

A plugin marketplace isn’t [Claude Marketplace](https://claude.com/marketplace). Claude Marketplace is the website at claude.com/marketplace where you browse plugins, connectors, partner products, and service partners. It isn’t a marketplace you add with `/plugin marketplace add`.

Claude Code adds Anthropic’s official marketplace the first time you start an interactive terminal session, unless a [managed policy](plugins-org.md#allow-the-official-marketplace-and-your-own) blocks it. Claude Code adds no other marketplace on its own, including Anthropic’s community and demo marketplaces. To distinguish the three Anthropic marketplaces, read [Anthropic’s marketplaces](plugins-anthropic-marketplaces.md). To see what the official one lists, open the **Discover** tab of `/plugin` in a session or browse [Claude Marketplace](https://claude.com/marketplace/plugins). This diagram shows the path from a marketplace to your session. A marketplace lists a plugin, you install that plugin, and Claude Code loads its components.

[Install and manage plugins](discover-plugins.md#install-a-plugin) has the install steps for each place you run Claude Code. While you’re developing a plugin, you don’t need a marketplace: load it straight from its folder with `--plugin-dir`, as [Develop without a marketplace](plugins-create.md#develop-without-a-marketplace) shows.


[​](#make-an-installed-plugin-available-in-your-session)

Make an installed plugin available in your session

Before a plugin you installed gives you a skill you can run, it has to be present at each of these layers:

- **Settings**: your settings list the marketplaces you’ve added and the plugins that are enabled.
- **Disk**: `~/.claude/plugins/` holds what Claude Code has fetched and installed.
- **Session**: plugins load at startup, or when you [reload plugins](plugins-loading.md#check-which-stage-a-plugin-reached).

Read [Plugin loading reference](plugins-loading.md) for the rules at each layer, including which settings file takes precedence and where the files are on disk.


[​](#tell-anthropic’s-marketplaces-from-third-party-ones)

Tell Anthropic’s marketplaces from third-party ones

A marketplace’s name places it in one of three tiers. Claude Code accepts the official and community names only for marketplaces sourced from `github.com/anthropics/` repositories:

- **Official**: marketplaces with one of Anthropic’s [official marketplace names](plugins-security.md#official-marketplace-names), including `claude-plugins-official` and the demo marketplace `claude-code-plugins`.
- **Community**: marketplaces with one of Anthropic’s community names, such as `claude-community`. [Identify Anthropic’s marketplaces by name](plugins-security.md#marketplace-tiers) lists them.
- **Third-party**: every other marketplace. A marketplace your coworker or your organization publishes is third-party.

Whatever the tier, a plugin you install can run code with your user privileges. Read [Plugin security and trust](plugins-security.md) for how to review a plugin before you install it. Through [managed settings](../02-Claude-Code-CLI/settings.md#settings-files), an organization can allowlist or block marketplaces, force-install plugins, and turn off session-only loading. Read [Manage plugins for your organization](plugins-org.md) for those controls.


[​](#understand-install-scopes)

Understand install scopes

When you install a plugin, you pick a scope, and the scope decides who the plugin is enabled for:

- **User scope**: enabled for you in every project on this computer
- **Project scope**: enabled for everyone who works in this repository, through the committed `.claude/settings.json`. Each collaborator still [installs it on their own machine](plugins-loading.md#enabled-in-project-settings-but-not-installed)
- **Local scope**: enabled for you in this repository only

A plugin you install at user scope in the terminal, the desktop app’s local sessions, or the VS Code extension is available in the other two on that computer, because all three read the same settings files. See [Choose an install scope](discover-plugins.md#choose-an-install-scope) for how to pick one. A cloud session, including one in the browser at claude.ai/code, doesn’t load the plugins in your local settings. For install steps in the terminal, VS Code, and the desktop app, and for what a cloud session loads, see [Install a plugin](discover-plugins.md#install-a-plugin).

The same plugin format also installs on claude.ai and in Cowork, where a different set of components loads. For those surfaces, see [Plugins on claude.ai and in Cowork](https://claude.com/docs/plugins/overview) on claude.com and its [component support table](https://claude.com/docs/plugins/platform-support#compare-component-support-by-app).


[​](#next-steps)

Next steps

Most people start by installing a plugin from Anthropic’s official marketplace, which Claude Code adds the first time you start an interactive terminal session. Run `/plugin` in a terminal session to browse it, or follow [Install and manage plugins](discover-plugins.md), which also covers the desktop app and VS Code. To see what’s in that marketplace before you open Claude Code, browse [Claude Marketplace](https://claude.com/marketplace/plugins) on the web. To build your own, [Create a plugin](plugins-create.md) starts with an empty directory and ends with a working plugin. Once you’ve installed or built a plugin, these pages cover what comes next:

- **Share what you built**: [Publish and distribute a plugin](plugins-publish.md), through your own marketplace or [Anthropic’s directory](plugins-publish.md#submit-to-anthropics-directory)
- **Check whether it works and is used**: [Test plugins with evals](plugin-evals.md) and [Measure plugin cost and usage](plugins-measure.md)
- **Run a marketplace for your team**: [Create a marketplace](plugin-marketplaces.md), then [Host and maintain a marketplace](plugins-host-marketplace.md)
- **Set plugin policy for an organization**: [Manage plugins for your organization](plugins-org.md)
- **Fix a problem**: [Troubleshoot plugins](plugins-troubleshooting.md)
