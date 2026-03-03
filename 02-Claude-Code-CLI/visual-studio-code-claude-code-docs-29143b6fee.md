---
category: "02-Claude-Code-CLI"
fetched_at: "2026-03-03T15:08:35Z"
source_url: "https://code.claude.com/docs/en/vs-code"
title: "Visual Studio Code - Claude Code Docs"
---

# Use Claude Code in VS Code


Install and configure the Claude Code extension for VS Code. Get AI coding assistance with inline diffs, @-mentions, plan review, and keyboard shortcuts.


The VS Code extension provides a native graphical interface for Claude Code, integrated directly into your IDE. This is the recommended way to use Claude Code in VS Code. With the extension, you can review and edit Claude’s plans before accepting them, auto-accept edits as they’re made, @-mention files with specific line ranges from your selection, access conversation history, and open multiple conversations in separate tabs or windows.

## 

[​](#prerequisites)

Prerequisites

Before installing, make sure you have:

- VS Code 1.98.0 or higher
- An Anthropic account (you’ll sign in when you first open the extension). If you’re using a third-party provider like Amazon Bedrock or Google Vertex AI, see [Use third-party providers](#use-third-party-providers) instead.

The extension includes the CLI (command-line interface), which you can access from VS Code’s integrated terminal for advanced features. See [VS Code extension vs. Claude Code CLI](#vs-code-extension-vs-claude-code-cli) for details.

## 

[​](#install-the-extension)

Install the extension

Click the link for your IDE to install directly:

- [Install for VS Code](vscode:extension/anthropic.claude-code)
- [Install for Cursor](cursor:extension/anthropic.claude-code)

Or in VS Code, press `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux) to open the Extensions view, search for “Claude Code”, and click **Install**.

If the extension doesn’t appear after installation, restart VS Code or run “Developer: Reload Window” from the Command Palette.

## 

[​](#get-started)

Get started

Once installed, you can start using Claude Code through the VS Code interface:

1

[](#)

Open the Claude Code panel

Throughout VS Code, the Spark icon indicates Claude Code: The quickest way to open Claude is to click the Spark icon in the **Editor Toolbar** (top-right corner of the editor). The icon only appears when you have a file open.Other ways to open Claude Code:

- **Command Palette**: `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux), type “Claude Code”, and select an option like “Open in New Tab”
- **Status Bar**: click **✱ Claude Code** in the bottom-right corner of the window. This works even when no file is open.

When you first open the panel, a **Learn Claude Code** checklist appears. Work through each item by clicking **Show me**, or dismiss it with the X. To reopen it later, uncheck **Hide Onboarding** in VS Code settings under Extensions → Claude Code.You can drag the Claude panel to reposition it anywhere in VS Code. See [Customize your workflow](#customize-your-workflow) for details.

2

[](#)

Send a prompt

Ask Claude to help with your code or files, whether that’s explaining how something works, debugging an issue, or making changes.

Claude automatically sees your selected text. Press `Option+K` (Mac) / `Alt+K` (Windows/Linux) to also insert an @-mention reference (like `@file.ts#5-10`) into your prompt.

Here’s an example of asking about a particular line in a file:

3

[](#)

Review changes

When Claude wants to edit a file, it shows a side-by-side comparison of the original and proposed changes, then asks for permission. You can accept, reject, or tell Claude what to do instead.

For more ideas on what you can do with Claude Code, see [Common workflows](/docs/en/common-workflows).

Run “Claude Code: Open Walkthrough” from the Command Palette for a guided tour of the basics.

## 

[​](#use-the-prompt-box)

Use the prompt box

The prompt box supports several features:

- **Permission modes**: click the mode indicator at the bottom of the prompt box to switch modes. In normal mode, Claude asks permission before each action. In Plan mode, Claude describes what it will do and waits for approval before making changes. In auto-accept mode, Claude makes edits without asking. Set the default in VS Code settings under `claudeCode.initialPermissionMode`.
- **Command menu**: click `/` or type `/` to open the command menu. Options include attaching files, switching models, toggling extended thinking, and viewing plan usage (`/usage`). The Customize section provides access to MCP servers, hooks, memory, permissions, and plugins. Items with a terminal icon open in the integrated terminal.
- **Context indicator**: the prompt box shows how much of Claude’s context window you’re using. Claude automatically compacts when needed, or you can run `/compact` manually.
- **Extended thinking**: lets Claude spend more time reasoning through complex problems. Toggle it on via the command menu (`/`). See [Extended thinking](/docs/en/common-workflows#use-extended-thinking-thinking-mode) for details.
- **Multi-line input**: press `Shift+Enter` to add a new line without sending. This also works in the “Other” free-text input of question dialogs.

### 

[​](#reference-files-and-folders)

Reference files and folders

Use @-mentions to give Claude context about specific files or folders. When you type `@` followed by a file or folder name, Claude reads that content and can answer questions about it or make changes to it. Claude Code supports fuzzy matching, so you can type partial names to find what you need:

Report incorrect code

Copy


``` shiki
> Explain the logic in @auth (fuzzy matches auth.js, AuthService.ts, etc.)
> What's in @src/components/ (include a trailing slash for folders)
```

For large PDFs, you can ask Claude to read specific pages instead of the whole file: a single page, a range like pages 1-10, or an open-ended range like page 3 onward. When you select text in the editor, Claude can see your highlighted code automatically. The prompt box footer shows how many lines are selected. Press `Option+K` (Mac) / `Alt+K` (Windows/Linux) to insert an @-mention with the file path and line numbers (e.g., `@app.ts#5-10`). Click the selection indicator to toggle whether Claude can see your highlighted text - the eye-slash icon means the selection is hidden from Claude. You can also hold `Shift` while dragging files into the prompt box to add them as attachments. Click the X on any attachment to remove it from context.

### 

[​](#resume-past-conversations)

Resume past conversations

Click the dropdown at the top of the Claude Code panel to access your conversation history. You can search by keyword or browse by time (Today, Yesterday, Last 7 days, etc.). Click any conversation to resume it with the full message history. Hover over a session to reveal rename and remove actions: rename to give it a descriptive title, or remove to delete it from the list. For more on resuming sessions, see [Common workflows](/docs/en/common-workflows#resume-previous-conversations).

### 

[​](#resume-remote-sessions-from-claude-ai)

Resume remote sessions from Claude.ai

If you use [Claude Code on the web](/docs/en/claude-code-on-the-web), you can resume those remote sessions directly in VS Code. This requires signing in with **Claude.ai Subscription**, not Anthropic Console.

1

[](#)

Open Past Conversations

Click the **Past Conversations** dropdown at the top of the Claude Code panel.

2

[](#)

Select the Remote tab

The dialog shows two tabs: Local and Remote. Click **Remote** to see sessions from claude.ai.

3

[](#)

Select a session to resume

Browse or search your remote sessions. Click any session to download it and continue the conversation locally.

Only web sessions started with a GitHub repository appear in the Remote tab. Resuming loads the conversation history locally; changes are not synced back to claude.ai.

## 

[​](#customize-your-workflow)

Customize your workflow

Once you’re up and running, you can reposition the Claude panel, run multiple sessions, or switch to terminal mode.

### 

[​](#choose-where-claude-lives)

Choose where Claude lives

You can drag the Claude panel to reposition it anywhere in VS Code. Grab the panel’s tab or title bar and drag it to:

- **Secondary sidebar**: the right side of the window. Keeps Claude visible while you code.
- **Primary sidebar**: the left sidebar with icons for Explorer, Search, etc.
- **Editor area**: opens Claude as a tab alongside your files. Useful for side tasks.

Use the sidebar for your main Claude session and open additional tabs for side tasks. Claude remembers your preferred location. Note that the Spark icon only appears in the Activity Bar when the Claude panel is docked to the left. Since Claude defaults to the right side, use the Editor Toolbar icon to open Claude.

### 

[​](#run-multiple-conversations)

Run multiple conversations

Use **Open in New Tab** or **Open in New Window** from the Command Palette to start additional conversations. Each conversation maintains its own history and context, allowing you to work on different tasks in parallel. When using tabs, a small colored dot on the spark icon indicates status: blue means a permission request is pending, orange means Claude finished while the tab was hidden.

### 

[​](#switch-to-terminal-mode)

Switch to terminal mode

By default, the extension opens a graphical chat panel. If you prefer the CLI-style interface, open the [Use Terminal setting](vscode://settings/claudeCode.useTerminal) and check the box. You can also open VS Code settings (`Cmd+,` on Mac or `Ctrl+,` on Windows/Linux), go to Extensions → Claude Code, and check **Use Terminal**.

## 

[​](#manage-plugins)

Manage plugins

The VS Code extension includes a graphical interface for installing and managing [plugins](/docs/en/plugins). Type `/plugins` in the prompt box to open the **Manage plugins** interface.

### 

[​](#install-plugins)

Install plugins

The plugin dialog shows two tabs: **Plugins** and **Marketplaces**. In the Plugins tab:

- **Installed plugins** appear at the top with toggle switches to enable or disable them
- **Available plugins** from your configured marketplaces appear below
- Search to filter plugins by name or description
- Click **Install** on any available plugin

When you install a plugin, choose the installation scope:

- **Install for you**: available in all your projects (user scope)
- **Install for this project**: shared with project collaborators (project scope)
- **Install locally**: only for you, only in this repository (local scope)

### 

[​](#manage-marketplaces)

Manage marketplaces

Switch to the **Marketplaces** tab to add or remove plugin sources:

- Enter a GitHub repo, URL, or local path to add a new marketplace
- Click the refresh icon to update a marketplace’s plugin list
- Click the trash icon to remove a marketplace

After making changes, a banner prompts you to restart Claude Code to apply the updates.

Plugin management in VS Code uses the same CLI commands under the hood. Plugins and marketplaces you configure in the extension are also available in the CLI, and vice versa.

For more about the plugin system, see [Plugins](/docs/en/plugins) and [Plugin marketplaces](/docs/en/plugin-marketplaces).

## 

[​](#automate-browser-tasks-with-chrome)

Automate browser tasks with Chrome

Connect Claude to your Chrome browser to test web apps, debug with console logs, and automate browser workflows without leaving VS Code. This requires the [Claude in Chrome extension](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) version 1.0.36 or higher. Type `@browser` in the prompt box followed by what you want Claude to do:

Report incorrect code

Copy


``` shiki
@browser go to localhost:3000 and check the console for errors
```

You can also open the attachment menu to select specific browser tools like opening a new tab or reading page content. Claude opens new tabs for browser tasks and shares your browser’s login state, so it can access any site you’re already signed into. For setup instructions, the full list of capabilities, and troubleshooting, see [Use Claude Code with Chrome](/docs/en/chrome).

## 

[​](#vs-code-commands-and-shortcuts)

VS Code commands and shortcuts

Open the Command Palette (`Cmd+Shift+P` on Mac or `Ctrl+Shift+P` on Windows/Linux) and type “Claude Code” to see all available VS Code commands for the Claude Code extension. Some shortcuts depend on which panel is “focused” (receiving keyboard input). When your cursor is in a code file, the editor is focused. When your cursor is in Claude’s prompt box, Claude is focused. Use `Cmd+Esc` / `Ctrl+Esc` to toggle between them.

These are VS Code commands for controlling the extension. Not all built-in Claude Code commands are available in the extension. See [VS Code extension vs. Claude Code CLI](#vs-code-extension-vs-claude-code-cli) for details.

| Command | Shortcut | Description |
|----|----|----|
| Focus Input | `Cmd+Esc` (Mac) / `Ctrl+Esc` (Windows/Linux) | Toggle focus between editor and Claude |
| Open in Side Bar | \- | Open Claude in the left sidebar |
| Open in Terminal | \- | Open Claude in terminal mode |
| Open in New Tab | `Cmd+Shift+Esc` (Mac) / `Ctrl+Shift+Esc` (Windows/Linux) | Open a new conversation as an editor tab |
| Open in New Window | \- | Open a new conversation in a separate window |
| New Conversation | `Cmd+N` (Mac) / `Ctrl+N` (Windows/Linux) | Start a new conversation (requires Claude to be focused) |
| Insert @-Mention Reference | `Option+K` (Mac) / `Alt+K` (Windows/Linux) | Insert a reference to the current file and selection (requires editor to be focused) |
| Show Logs | \- | View extension debug logs |
| Logout | \- | Sign out of your Anthropic account |

## 

[​](#configure-settings)

Configure settings

The extension has two types of settings:

- **Extension settings** in VS Code: control the extension’s behavior within VS Code. Open with `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux), then go to Extensions → Claude Code. You can also type `/` and select **General Config** to open settings.
- **Claude Code settings** in `~/.claude/settings.json`: shared between the extension and CLI. Use for allowed commands, environment variables, hooks, and MCP servers. See [Settings](/docs/en/settings) for details.

Add `"$schema": "https://json.schemastore.org/claude-code-settings.json"` to your `settings.json` to get autocomplete and inline validation for all available settings directly in VS Code.

### 

[​](#extension-settings)

Extension settings

| Setting | Default | Description |
|----|----|----|
| `selectedModel` | `default` | Model for new conversations. Change per-session with `/model`. |
| `useTerminal` | `false` | Launch Claude in terminal mode instead of graphical panel |
| `initialPermissionMode` | `default` | Controls approval prompts: `default` (ask each time), `plan`, `acceptEdits`, or `bypassPermissions` |
| `preferredLocation` | `panel` | Where Claude opens: `sidebar` (right) or `panel` (new tab) |
| `autosave` | `true` | Auto-save files before Claude reads or writes them |
| `useCtrlEnterToSend` | `false` | Use Ctrl/Cmd+Enter instead of Enter to send prompts |
| `enableNewConversationShortcut` | `true` | Enable Cmd/Ctrl+N to start a new conversation |
| `hideOnboarding` | `false` | Hide the onboarding checklist (graduation cap icon) |
| `respectGitIgnore` | `true` | Exclude .gitignore patterns from file searches |
| `environmentVariables` | `[]` | Set environment variables for the Claude process. Use Claude Code settings instead for shared config. |
| `disableLoginPrompt` | `false` | Skip authentication prompts (for third-party provider setups) |
| `allowDangerouslySkipPermissions` | `false` | Bypass all permission prompts. **Use with extreme caution.** |
| `claudeProcessWrapper` | \- | Executable path used to launch the Claude process |

## 

[​](#vs-code-extension-vs-claude-code-cli)

VS Code extension vs. Claude Code CLI

Claude Code is available as both a VS Code extension (graphical panel) and a CLI (command-line interface in the terminal). Some features are only available in the CLI. If you need a CLI-only feature, run `claude` in VS Code’s integrated terminal.

| Feature | CLI | VS Code Extension |
|----|----|----|
| Commands and skills | [All](/docs/en/interactive-mode#built-in-commands) | Subset (type `/` to see available) |
| MCP server config | Yes | No (configure via CLI, use in extension) |
| Checkpoints | Yes | Yes |
| `!` bash shortcut | Yes | No |
| Tab completion | Yes | No |

### 

[​](#rewind-with-checkpoints)

Rewind with checkpoints

The VS Code extension supports checkpoints, which track Claude’s file edits and let you rewind to a previous state. Hover over any message to reveal the rewind button, then choose from three options:

- **Fork conversation from here**: start a new conversation branch from this message while keeping all code changes intact
- **Rewind code to here**: revert file changes back to this point in the conversation while keeping the full conversation history
- **Fork conversation and rewind code**: start a new conversation branch and revert file changes to this point

For full details on how checkpoints work and their limitations, see [Checkpointing](/docs/en/checkpointing).

### 

[​](#run-cli-in-vs-code)

Run CLI in VS Code

To use the CLI while staying in VS Code, open the integrated terminal (`` Ctrl+` `` on Windows/Linux or `` Cmd+` `` on Mac) and run `claude`. The CLI automatically integrates with your IDE for features like diff viewing and diagnostic sharing. If using an external terminal, run `/ide` inside Claude Code to connect it to VS Code.

### 

[​](#switch-between-extension-and-cli)

Switch between extension and CLI

The extension and CLI share the same conversation history. To continue an extension conversation in the CLI, run `claude --resume` in the terminal. This opens an interactive picker where you can search for and select your conversation.

### 

[​](#include-terminal-output-in-prompts)

Include terminal output in prompts

Reference terminal output in your prompts using `@terminal:name` where `name` is the terminal’s title. This lets Claude see command output, error messages, or logs without copy-pasting.

### 

[​](#monitor-background-processes)

Monitor background processes

When Claude runs long-running commands, the extension shows progress in the status bar. However, visibility for background tasks is limited compared to the CLI. For better visibility, have Claude output the command so you can run it in VS Code’s integrated terminal.

### 

[​](#connect-to-external-tools-with-mcp)

Connect to external tools with MCP

MCP (Model Context Protocol) servers give Claude access to external tools, databases, and APIs. Configure them via CLI, then use them in both extension and CLI. To add an MCP server, open the integrated terminal (`` Ctrl+` `` or `` Cmd+` ``) and run:

Report incorrect code

Copy


``` shiki
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
```

Once configured, ask Claude to use the tools (e.g., “Review PR \#456”). Some servers require authentication: run `claude` in the terminal, then type `/mcp` to authenticate. See the [MCP documentation](/docs/en/mcp) for available servers.

## 

[​](#work-with-git)

Work with git

Claude Code integrates with git to help with version control workflows directly in VS Code. Ask Claude to commit changes, create pull requests, or work across branches.

### 

[​](#create-commits-and-pull-requests)

Create commits and pull requests

Claude can stage changes, write commit messages, and create pull requests based on your work:

Report incorrect code

Copy


``` shiki
> commit my changes with a descriptive message
> create a pr for this feature
> summarize the changes I've made to the auth module
```

When creating pull requests, Claude generates descriptions based on the actual code changes and can add context about testing or implementation decisions.

### 

[​](#use-git-worktrees-for-parallel-tasks)

Use git worktrees for parallel tasks

Use the `--worktree` (`-w`) flag to start Claude in an isolated worktree with its own files and branch:

Report incorrect code

Copy


``` shiki
claude --worktree feature-auth
```

Each worktree maintains independent file state while sharing git history. This prevents Claude instances from interfering with each other when working on different tasks. For more details, see [Run parallel sessions with Git worktrees](/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees).

## 

[​](#use-third-party-providers)

Use third-party providers

By default, Claude Code connects directly to Anthropic’s API. If your organization uses Amazon Bedrock, Google Vertex AI, or Microsoft Foundry to access Claude, configure the extension to use your provider instead:

1

[](#)

Disable login prompt

Open the [Disable Login Prompt setting](vscode://settings/claudeCode.disableLoginPrompt) and check the box.You can also open VS Code settings (`Cmd+,` on Mac or `Ctrl+,` on Windows/Linux), search for “Claude Code login”, and check **Disable Login Prompt**.

2

[](#)

Configure your provider

Follow the setup guide for your provider:

- [Claude Code on Amazon Bedrock](/docs/en/amazon-bedrock)
- [Claude Code on Google Vertex AI](/docs/en/google-vertex-ai)
- [Claude Code on Microsoft Foundry](/docs/en/microsoft-foundry)

These guides cover configuring your provider in `~/.claude/settings.json`, which ensures your settings are shared between the VS Code extension and the CLI.

## 

[​](#security-and-privacy)

Security and privacy

Your code stays private. Claude Code processes your code to provide assistance but does not use it to train models. For details on data handling and how to opt out of logging, see [Data and privacy](/docs/en/data-usage). With auto-edit permissions enabled, Claude Code can modify VS Code configuration files (like `settings.json` or `tasks.json`) that VS Code may execute automatically. To reduce risk when working with untrusted code:

- Enable [VS Code Restricted Mode](https://code.visualstudio.com/docs/editor/workspace-trust#_restricted-mode) for untrusted workspaces
- Use manual approval mode instead of auto-accept for edits
- Review changes carefully before accepting them

## 

[​](#fix-common-issues)

Fix common issues

### 

[​](#extension-won’t-install)

Extension won’t install

- Ensure you have a compatible version of VS Code (1.98.0 or later)
- Check that VS Code has permission to install extensions
- Try installing directly from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)

### 

[​](#spark-icon-not-visible)

Spark icon not visible

The Spark icon appears in the **Editor Toolbar** (top-right of editor) when you have a file open. If you don’t see it:

1.  **Open a file**: The icon requires a file to be open. Having just a folder open isn’t enough.
2.  **Check VS Code version**: Requires 1.98.0 or higher (Help → About)
3.  **Restart VS Code**: Run “Developer: Reload Window” from the Command Palette
4.  **Disable conflicting extensions**: Temporarily disable other AI extensions (Cline, Continue, etc.)
5.  **Check workspace trust**: The extension doesn’t work in Restricted Mode

Alternatively, click ”✱ Claude Code” in the **Status Bar** (bottom-right corner). This works even without a file open. You can also use the **Command Palette** (`Cmd+Shift+P` / `Ctrl+Shift+P`) and type “Claude Code”.

### 

[​](#claude-code-never-responds)

Claude Code never responds

If Claude Code isn’t responding to your prompts:

1.  **Check your internet connection**: Ensure you have a stable internet connection
2.  **Start a new conversation**: Try starting a fresh conversation to see if the issue persists
3.  **Try the CLI**: Run `claude` from the terminal to see if you get more detailed error messages

If problems persist, [file an issue on GitHub](https://github.com/anthropics/claude-code/issues) with details about the error.

## 

[​](#uninstall-the-extension)

Uninstall the extension

To uninstall the Claude Code extension:

1.  Open the Extensions view (`Cmd+Shift+X` on Mac or `Ctrl+Shift+X` on Windows/Linux)
2.  Search for “Claude Code”
3.  Click **Uninstall**

To also remove extension data and reset all settings:

Report incorrect code

Copy


``` shiki
rm -rf ~/.vscode/globalStorage/anthropic.claude-code
```

For additional help, see the [troubleshooting guide](/docs/en/troubleshooting).

## 

[​](#next-steps)

Next steps

Now that you have Claude Code set up in VS Code:

- [Explore common workflows](/docs/en/common-workflows) to get the most out of Claude Code
- [Set up MCP servers](/docs/en/mcp) to extend Claude’s capabilities with external tools. Configure servers using the CLI, then use them in the extension.
- [Configure Claude Code settings](/docs/en/settings) to customize allowed commands, hooks, and more. These settings are shared between the extension and CLI.
