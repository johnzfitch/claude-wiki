---
title: "Anthropic's marketplaces - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/plugins/anthropic-marketplaces"
category: "08-Plugins-Skills"
fetched_at: "2026-11-13T06:32:45Z"
last_modified: "Fri, 13 Nov 2026 06:21:44 GMT"
tags: ["claude-code", "plugins"]
---

## On this page

Back to top

- [Anthropic’s marketplaces](#anthropic%E2%80%99s-marketplaces)
  - [Deprecated claude-code-plugins marketplace](#deprecated-claude-code-plugins-marketplace)
- [Find plugins in the official marketplace](#find-plugins-in-the-official-marketplace)
- [Browse and install from Anthropic’s marketplaces](#browse-and-install-from-anthropic%E2%80%99s-marketplaces)
  - [Add the community marketplace](#add-the-community-marketplace)
- [Third-party marketplaces](#third-party-marketplaces)
- [Next steps](#next-steps)

Use plugins

# Anthropic's marketplaces

Copy pageCopy page

Anthropic’s official and community plugin marketplaces for Claude Code: their names, repositories, how you add each, and where to browse their plugins.

Copy pageCopy page

Anthropic publishes two general-purpose plugin marketplaces for Claude Code: [official](https://github.com/anthropics/claude-plugins-official) and [community](https://github.com/anthropics/claude-plugins-community). Each is a catalog of plugins in its own GitHub repository. When you install a plugin from one of them in a Claude Code session, you type the marketplace’s name after `@`, as in `/plugin install commit-commands@claude-plugins-official`. Use this page to distinguish the two marketplaces and to find where to check whether the official one holds a given plugin.

These cases are covered on other pages:

- **How to install a plugin**: see [Install plugins](discover-plugins.md)
- **A failed install**: see [Troubleshoot plugins](plugins-troubleshooting.md)

Go to the part of the page you need:

- To distinguish the two marketplaces by repository, marketplace name, and how you get each one, see [Anthropic’s marketplaces](#anthropic%E2%80%99s-marketplaces).
- To find a plugin in the official marketplace, see [Find plugins in the official marketplace](#find-plugins-in-the-official-marketplace).


[​](#anthropic’s-marketplaces)

Anthropic’s marketplaces

A marketplace is a catalog of plugins that a repository defines in its `.claude-plugin/marketplace.json` file. The official and community marketplaces each come from their own GitHub repository. Anthropic also publishes topic-specific marketplaces, such as `anthropics/skills` and `anthropics/knowledge-work-plugins`, which you add in a Claude Code session with `/plugin marketplace add <owner>/<repo>`. This table gives each marketplace’s repository and marketplace name, which is what you type after `@` when you install a plugin from that marketplace. The community marketplace’s name is `claude-community`, not its repository name.

|  | Official | Community |
|:---|:---|:---|
| Repository | [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official) | [`anthropics/claude-plugins-community`](https://github.com/anthropics/claude-plugins-community) |
| Marketplace name | `claude-plugins-official` | `claude-community` |
| What’s in it | Plugins Anthropic maintains, plus plugins from partners and other authors | Third-party plugins that their authors submitted to Anthropic |
| How you get it | Claude Code adds it the first time you start an interactive terminal session, unless a [managed policy](plugins-org.md#allow-the-official-marketplace-and-your-own) or `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL` blocks it. See [Marketplace `claude-plugins-official` not found](plugins-troubleshooting.md#marketplace-claude-plugins-official-not-found) if it’s missing | You add it in a Claude Code session with `/plugin marketplace add anthropics/claude-plugins-community` |

If you wrote a plugin and want other people to install it, see [Publish a plugin](plugins-publish.md), which covers your own marketplace and submitting to Anthropic’s directory.


[​](#deprecated-claude-code-plugins-marketplace)

Deprecated `claude-code-plugins` marketplace

The `claude-code-plugins` marketplace in `anthropics/claude-code` is deprecated. To add a plugin, run `claude plugin install <plugin>@claude-plugins-official` in your shell, and skip any tutorial step that runs `/plugin marketplace add anthropics/claude-code`.

Unless you have one of the two plugins below, you can leave your `claude-code-plugins` plugins and the marketplace as they are. They update from the `claude-plugins-official` repository.

- **`ralph-wiggum`**: this plugin is now `ralph-loop`, and its commands start with `/ralph-loop:`. If those commands aren’t available, run `claude plugin install ralph-loop@claude-plugins-official` in your shell.
- **`claude-opus-4-5-migration`**: this plugin is retired, so remove it by running `claude plugin uninstall claude-opus-4-5-migration@claude-code-plugins` in your shell.

If any other plugin stopped working, see [Plugin installed but not working](plugins-troubleshooting.md#plugin-installed-but-not-working).


[​](#find-plugins-in-the-official-marketplace)

Find plugins in the official marketplace

By default, Claude Code adds the official marketplace, `claude-plugins-official`, for you. Most of what it lists comes from partners and other authors rather than from Anthropic: tool vendors publish plugins that connect Claude Code to their services, and Anthropic maintains a smaller set of its own, such as `commit-commands`, `code-review`, `feature-dev`, and the [language server plugins](plugins-code-intelligence.md). The catalog changes often, so this page doesn’t list it. To see what’s in it, use the **Discover** tab of `/plugin` in a Claude Code session, which you can search, or browse [Claude Marketplace](https://claude.com/marketplace/plugins) on the web.


[​](#browse-and-install-from-anthropic’s-marketplaces)

Browse and install from Anthropic’s marketplaces

You can search Anthropic’s marketplaces for a plugin in Claude Code, on the web, or on GitHub:

- **In Claude Code, by browsing**: run `/plugin` in an interactive session. Its **Discover** tab lists the plugins from your marketplaces.
- **In Claude Code, by name**: run `/plugin install <name>` in a session, which looks the name up in your marketplaces. If the plugin is in one of them, its details open in the `/plugin` panel, and nothing installs until you choose an [installation scope](discover-plugins.md#install-a-plugin) and confirm there. If it isn’t, you see `Plugin "<name>" not found in any marketplace`.
- **On the web**: search the full catalog on [Claude Marketplace](https://claude.com/marketplace/plugins), which shows install counts and marks some plugins **Anthropic verified**.
- **On GitHub**: open `.claude-plugin/marketplace.json` in the marketplace’s repository, such as [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official). That file is the catalog itself.

Anthropic’s directory is separate from these marketplaces. The directory is the catalog on claude.ai. A plugin you add from the directory on claude.ai reaches Claude Code through [account sync](plugins-loading.md#synced-plugins). To list your own plugin there, see [Submit to Anthropic’s directory](plugins-publish.md#submit-to-anthropics-directory). To install from the desktop app or from a script, or to see what a cloud session loads, see [Install plugins](discover-plugins.md).


[​](#add-the-community-marketplace)

Add the community marketplace

The community marketplace isn’t registered until you add it. In a Claude Code session, run `/plugin marketplace add anthropics/claude-plugins-community`, then install with the `@claude-community` suffix. If `claude-plugins-official` isn’t on the **Marketplaces** tab of `/plugin`, add it the same way with `/plugin marketplace add anthropics/claude-plugins-official`. For `not found` errors and marketplaces that won’t add, see [Troubleshoot plugins](plugins-troubleshooting.md#install-a-plugin).


[​](#third-party-marketplaces)

Third-party marketplaces

Many popular plugins aren’t in any Anthropic marketplace. They’re in their authors’ own marketplaces, usually a GitHub repository with a `.claude-plugin/marketplace.json` at its root. Anthropic doesn’t review third-party marketplaces, so read [Plugin security and trust](plugins-security.md) before you add one. To use a third-party marketplace, add its repository in a Claude Code session with `/plugin marketplace add <owner>/<repo>`, then install with `/plugin install <plugin>@<marketplace-name>`. The marketplace name is the `name` field of that `marketplace.json`, and Claude Code prints it once it has added the marketplace. For other ways to add a marketplace, see [Add a marketplace](discover-plugins.md#add-a-marketplace).


[​](#next-steps)

Next steps

- [Install and manage plugins](discover-plugins.md): install a plugin from one of these marketplaces and choose a scope
- [Plugin security and trust](plugins-security.md): what a plugin can do on your machine and how to review one before you install it
- [Code intelligence plugins](plugins-code-intelligence.md): install one of the official marketplace’s language-server plugins
- [Create a marketplace](plugins-create-marketplace.md): run your own marketplace alongside Anthropic’s
