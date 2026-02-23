---
category: "02-Claude-Code-CLI"
fetched_at: "2026-02-23T00:45:37Z"
source_url: "https://code.claude.com/docs/en/common-workflows"
title: "Common workflows - Claude Code Docs"
---

[Skip to main content](#content-area)

[Claude Code Docs home page](/docs)

English

Search...

⌘K

Ask AI

- [Claude Developer Platform](https://platform.claude.com/)
- [Claude Code on the Web](https://claude.ai/code)
- [](https://claude.ai/code)
  Claude Code on the Web

Search...

Navigation

Core concepts

Common workflows

[Getting started](/docs/en/overview)

[Build with Claude Code](/docs/en/sub-agents)

[Deployment](/docs/en/third-party-integrations)

[Administration](/docs/en/setup)

[Configuration](/docs/en/settings)

[Reference](/docs/en/cli-reference)

[Resources](/docs/en/legal-and-compliance)

##### Getting started

- [](/docs/en/overview)
  Overview
- [](/docs/en/quickstart)
  Quickstart
- [](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
  Changelog

##### Core concepts

- [](/docs/en/how-claude-code-works)
  How Claude Code works
- [](/docs/en/features-overview)
  Extend Claude Code
- [](/docs/en/common-workflows)
  Common workflows
- [](/docs/en/best-practices)
  Best practices

##### Platforms and integrations

- [](/docs/en/claude-code-on-the-web)
  Claude Code on the web

- Claude Code on desktop

- [](/docs/en/chrome)
  Chrome extension (beta)

- [](/docs/en/vs-code)
  Visual Studio Code

- [](/docs/en/jetbrains)
  JetBrains IDEs

- [](/docs/en/github-actions)
  GitHub Actions

- [](/docs/en/gitlab-ci-cd)
  GitLab CI/CD

- [](/docs/en/slack)
  Claude Code in Slack

On this page

- [Understand new codebases](#understand-new-codebases)
- [Get a quick codebase overview](#get-a-quick-codebase-overview)
- [Find relevant code](#find-relevant-code)
- [Fix bugs efficiently](#fix-bugs-efficiently)
- [Refactor code](#refactor-code)
- [Use specialized subagents](#use-specialized-subagents)
- [Use Plan Mode for safe code analysis](#use-plan-mode-for-safe-code-analysis)
- [When to use Plan Mode](#when-to-use-plan-mode)
- [How to use Plan Mode](#how-to-use-plan-mode)
- [Example: Planning a complex refactor](#example-planning-a-complex-refactor)
- [Configure Plan Mode as default](#configure-plan-mode-as-default)
- [Work with tests](#work-with-tests)
- [Create pull requests](#create-pull-requests)
- [Handle documentation](#handle-documentation)
- [Work with images](#work-with-images)
- [Reference files and directories](#reference-files-and-directories)
- [Use extended thinking (thinking mode)](#use-extended-thinking-thinking-mode)
- [Configure thinking mode](#configure-thinking-mode)
- [How extended thinking works](#how-extended-thinking-works)
- [Resume previous conversations](#resume-previous-conversations)
- [Name your sessions](#name-your-sessions)
- [Use the session picker](#use-the-session-picker)
- [Run parallel Claude Code sessions with Git worktrees](#run-parallel-claude-code-sessions-with-git-worktrees)
- [Subagent worktrees](#subagent-worktrees)
- [Worktree cleanup](#worktree-cleanup)
- [Manage worktrees manually](#manage-worktrees-manually)
- [Non-git version control](#non-git-version-control)
- [Get notified when Claude needs your attention](#get-notified-when-claude-needs-your-attention)
- [Use Claude as a unix-style utility](#use-claude-as-a-unix-style-utility)
- [Add Claude to your verification process](#add-claude-to-your-verification-process)
- [Pipe in, pipe out](#pipe-in-pipe-out)
- [Control output format](#control-output-format)
- [Ask Claude about its capabilities](#ask-claude-about-its-capabilities)
- [Example questions](#example-questions)
- [Next steps](#next-steps)

Core concepts

# Common workflows

Copy page

Step-by-step guides for exploring codebases, fixing bugs, refactoring, testing, and other everyday tasks with Claude Code.

Copy page

This page covers practical workflows for everyday development: exploring unfamiliar code, debugging, refactoring, writing tests, creating PRs, and managing sessions. Each section includes example prompts you can adapt to your own projects. For higher-level patterns and tips, see [Best practices](/docs/en/best-practices).

## 

[​](#understand-new-codebases)

Understand new codebases

### 

[​](#get-a-quick-codebase-overview)

Get a quick codebase overview

Suppose you’ve just joined a new project and need to understand its structure quickly.

1

[](#)

Navigate to the project root directory

Report incorrect code

Copy

Ask AI

``` shiki
cd /path/to/project 
```

2

[](#)

Start Claude Code

Report incorrect code

Copy

Ask AI

``` shiki
claude 
```

3

[](#)

Ask for a high-level overview

Report incorrect code

Copy

Ask AI

``` shiki
> give me an overview of this codebase 
```

4

[](#)

Dive deeper into specific components

Report incorrect code

Copy

Ask AI

``` shiki
> explain the main architecture patterns used here 
```

Report incorrect code

Copy

Ask AI

``` shiki
> what are the key data models?
```

Report incorrect code

Copy

Ask AI

``` shiki
> how is authentication handled?
```

Tips:

- Start with broad questions, then narrow down to specific areas
- Ask about coding conventions and patterns used in the project
- Request a glossary of project-specific terms

### 

[​](#find-relevant-code)

Find relevant code

Suppose you need to locate code related to a specific feature or functionality.

1

[](#)

Ask Claude to find relevant files

Report incorrect code

Copy

Ask AI

``` shiki
> find the files that handle user authentication 
```

2

[](#)

Get context on how components interact

Report incorrect code

Copy

Ask AI

``` shiki
> how do these authentication files work together? 
```

3

[](#)

Understand the execution flow

Report incorrect code

Copy

Ask AI

``` shiki
> trace the login process from front-end to database 
```

Tips:

- Be specific about what you’re looking for
- Use domain language from the project
- Install a [code intelligence plugin](/docs/en/discover-plugins#code-intelligence) for your language to give Claude precise “go to definition” and “find references” navigation

------------------------------------------------------------------------

## 

[​](#fix-bugs-efficiently)

Fix bugs efficiently

Suppose you’ve encountered an error message and need to find and fix its source.

1

[](#)

Share the error with Claude

Report incorrect code

Copy

Ask AI

``` shiki
> I'm seeing an error when I run npm test 
```

2

[](#)

Ask for fix recommendations

Report incorrect code

Copy

Ask AI

``` shiki
> suggest a few ways to fix the @ts-ignore in user.ts 
```

3

[](#)

Apply the fix

Report incorrect code

Copy

Ask AI

``` shiki
> update user.ts to add the null check you suggested 
```

Tips:

- Tell Claude the command to reproduce the issue and get a stack trace
- Mention any steps to reproduce the error
- Let Claude know if the error is intermittent or consistent

------------------------------------------------------------------------

## 

[​](#refactor-code)

Refactor code

Suppose you need to update old code to use modern patterns and practices.

1

[](#)

Identify legacy code for refactoring

Report incorrect code

Copy

Ask AI

``` shiki
> find deprecated API usage in our codebase 
```

2

[](#)

Get refactoring recommendations

Report incorrect code

Copy

Ask AI

``` shiki
> suggest how to refactor utils.js to use modern JavaScript features 
```

3

[](#)

Apply the changes safely

Report incorrect code

Copy

Ask AI

``` shiki
> refactor utils.js to use ES2024 features while maintaining the same behavior 
```

4

[](#)

Verify the refactoring

Report incorrect code

Copy

Ask AI

``` shiki
> run tests for the refactored code 
```

Tips:

- Ask Claude to explain the benefits of the modern approach
- Request that changes maintain backward compatibility when needed
- Do refactoring in small, testable increments

------------------------------------------------------------------------

## 

[​](#use-specialized-subagents)

Use specialized subagents

Suppose you want to use specialized AI subagents to handle specific tasks more effectively.

1

[](#)

View available subagents

Report incorrect code

Copy

Ask AI

``` shiki
> /agents
```

This shows all available subagents and lets you create new ones.

2

[](#)

Use subagents automatically

Claude Code automatically delegates appropriate tasks to specialized subagents:

Report incorrect code

Copy

Ask AI

``` shiki
> review my recent code changes for security issues
```

Report incorrect code

Copy

Ask AI

``` shiki
> run all tests and fix any failures
```

3

[](#)

Explicitly request specific subagents

Report incorrect code

Copy

Ask AI

``` shiki
> use the code-reviewer subagent to check the auth module
```

Report incorrect code

Copy

Ask AI

``` shiki
> have the debugger subagent investigate why users can't log in
```

4

[](#)

Create custom subagents for your workflow

Report incorrect code

Copy

Ask AI

``` shiki
> /agents
```

Then select “Create New subagent” and follow the prompts to define:

- A unique identifier that describes the subagent’s purpose (for example, `code-reviewer`, `api-designer`).
- When Claude should use this agent
- Which tools it can access
- A system prompt describing the agent’s role and behavior

Tips:

- Create project-specific subagents in `.claude/agents/` for team sharing
- Use descriptive `description` fields to enable automatic delegation
- Limit tool access to what each subagent actually needs
- Check the [subagents documentation](/docs/en/sub-agents) for detailed examples

------------------------------------------------------------------------

## 

[​](#use-plan-mode-for-safe-code-analysis)

Use Plan Mode for safe code analysis

Plan Mode instructs Claude to create a plan by analyzing the codebase with read-only operations, perfect for exploring codebases, planning complex changes, or reviewing code safely. In Plan Mode, Claude uses [`AskUserQuestion`](/docs/en/settings#tools-available-to-claude) to gather requirements and clarify your goals before proposing a plan.

### 

[​](#when-to-use-plan-mode)

When to use Plan Mode

- **Multi-step implementation**: When your feature requires making edits to many files
- **Code exploration**: When you want to research the codebase thoroughly before changing anything
- **Interactive development**: When you want to iterate on the direction with Claude

### 

[​](#how-to-use-plan-mode)

How to use Plan Mode

**Turn on Plan Mode during a session** You can switch into Plan Mode during a session using **Shift+Tab** to cycle through permission modes. If you are in Normal Mode, **Shift+Tab** first switches into Auto-Accept Mode, indicated by `⏵⏵ accept edits on` at the bottom of the terminal. A subsequent **Shift+Tab** will switch into Plan Mode, indicated by `⏸ plan mode on`. **Start a new session in Plan Mode** To start a new session in Plan Mode, use the `--permission-mode plan` flag:

Report incorrect code

Copy

Ask AI

``` shiki
claude --permission-mode plan
```

**Run “headless” queries in Plan Mode** You can also run a query in Plan Mode directly with `-p` (that is, in [“headless mode”](/docs/en/headless)):

Report incorrect code

Copy

Ask AI

``` shiki
claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"
```

### 

[​](#example-planning-a-complex-refactor)

Example: Planning a complex refactor

Report incorrect code

Copy

Ask AI

``` shiki
claude --permission-mode plan
```

Report incorrect code

Copy

Ask AI

``` shiki
> I need to refactor our authentication system to use OAuth2. Create a detailed migration plan.
```

Claude analyzes the current implementation and create a comprehensive plan. Refine with follow-ups:

Report incorrect code

Copy

Ask AI

``` shiki
> What about backward compatibility?
> How should we handle database migration?
```

Press `Ctrl+G` to open the plan in your default text editor, where you can edit it directly before Claude proceeds.

### 

[​](#configure-plan-mode-as-default)

Configure Plan Mode as default

Report incorrect code

Copy

Ask AI

``` shiki
// .claude/settings.json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

See [settings documentation](/docs/en/settings#available-settings) for more configuration options.

------------------------------------------------------------------------

## 

[​](#work-with-tests)

Work with tests

Suppose you need to add tests for uncovered code.

1

[](#)

Identify untested code

Report incorrect code

Copy

Ask AI

``` shiki
> find functions in NotificationsService.swift that are not covered by tests 
```

2

[](#)

Generate test scaffolding

Report incorrect code

Copy

Ask AI

``` shiki
> add tests for the notification service 
```

3

[](#)

Add meaningful test cases

Report incorrect code

Copy

Ask AI

``` shiki
> add test cases for edge conditions in the notification service 
```

4

[](#)

Run and verify tests

Report incorrect code

Copy

Ask AI

``` shiki
> run the new tests and fix any failures 
```

Claude can generate tests that follow your project’s existing patterns and conventions. When asking for tests, be specific about what behavior you want to verify. Claude examines your existing test files to match the style, frameworks, and assertion patterns already in use. For comprehensive coverage, ask Claude to identify edge cases you might have missed. Claude can analyze your code paths and suggest tests for error conditions, boundary values, and unexpected inputs that are easy to overlook.

------------------------------------------------------------------------

## 

[​](#create-pull-requests)

Create pull requests

You can create pull requests by asking Claude directly (“create a pr for my changes”) or by using the `/commit-push-pr` skill, which commits, pushes, and opens a PR in one step.

Report incorrect code

Copy

Ask AI

``` shiki
> /commit-push-pr
```

If you have a Slack MCP server configured and specify channels in your CLAUDE.md (for example, “post PR URLs to \#team-prs”), the skill automatically posts the PR URL to those channels. For more control over the process, guide Claude through it step-by-step or [create your own skill](/docs/en/skills):

1

[](#)

Summarize your changes

Report incorrect code

Copy

Ask AI

``` shiki
> summarize the changes I've made to the authentication module
```

2

[](#)

Generate a pull request

Report incorrect code

Copy

Ask AI

``` shiki
> create a pr
```

3

[](#)

Review and refine

Report incorrect code

Copy

Ask AI

``` shiki
> enhance the PR description with more context about the security improvements
```

When you create a PR using `gh pr create`, the session is automatically linked to that PR. You can resume it later with `claude --from-pr <number>`.

Review Claude’s generated PR before submitting and ask Claude to highlight potential risks or considerations.

## 

[​](#handle-documentation)

Handle documentation

Suppose you need to add or update documentation for your code.

1

[](#)

Identify undocumented code

Report incorrect code

Copy

Ask AI

``` shiki
> find functions without proper JSDoc comments in the auth module 
```

2

[](#)

Generate documentation

Report incorrect code

Copy

Ask AI

``` shiki
> add JSDoc comments to the undocumented functions in auth.js 
```

3

[](#)

Review and enhance

Report incorrect code

Copy

Ask AI

``` shiki
> improve the generated documentation with more context and examples 
```

4

[](#)

Verify documentation

Report incorrect code

Copy

Ask AI

``` shiki
> check if the documentation follows our project standards 
```

Tips:

- Specify the documentation style you want (JSDoc, docstrings, etc.)
- Ask for examples in the documentation
- Request documentation for public APIs, interfaces, and complex logic

------------------------------------------------------------------------

## 

[​](#work-with-images)

Work with images

Suppose you need to work with images in your codebase, and you want Claude’s help analyzing image content.

1

[](#)

Add an image to the conversation

You can use any of these methods:

1.  Drag and drop an image into the Claude Code window
2.  Copy an image and paste it into the CLI with ctrl+v (Do not use cmd+v)
3.  Provide an image path to Claude. E.g., “Analyze this image: /path/to/your/image.png”

2

[](#)

Ask Claude to analyze the image

Report incorrect code

Copy

Ask AI

``` shiki
> What does this image show?
```

Report incorrect code

Copy

Ask AI

``` shiki
> Describe the UI elements in this screenshot
```

Report incorrect code

Copy

Ask AI

``` shiki
> Are there any problematic elements in this diagram?
```

3

[](#)

Use images for context

Report incorrect code

Copy

Ask AI

``` shiki
> Here's a screenshot of the error. What's causing it?
```

Report incorrect code

Copy

Ask AI

``` shiki
> This is our current database schema. How should we modify it for the new feature?
```

4

[](#)

Get code suggestions from visual content

Report incorrect code

Copy

Ask AI

``` shiki
> Generate CSS to match this design mockup
```

Report incorrect code

Copy

Ask AI

``` shiki
> What HTML structure would recreate this component?
```

Tips:

- Use images when text descriptions would be unclear or cumbersome
- Include screenshots of errors, UI designs, or diagrams for better context
- You can work with multiple images in a conversation
- Image analysis works with diagrams, screenshots, mockups, and more
- When Claude references images (for example, `[Image #1]`), `Cmd+Click` (Mac) or `Ctrl+Click` (Windows/Linux) the link to open the image in your default viewer

------------------------------------------------------------------------

## 

[​](#reference-files-and-directories)

Reference files and directories

Use @ to quickly include files or directories without waiting for Claude to read them.

1

[](#)

Reference a single file

Report incorrect code

Copy

Ask AI

``` shiki
> Explain the logic in @src/utils/auth.js
```

This includes the full content of the file in the conversation.

2

[](#)

Reference a directory

Report incorrect code

Copy

Ask AI

``` shiki
> What's the structure of @src/components?
```

This provides a directory listing with file information.

3

[](#)

Reference MCP resources

Report incorrect code

Copy

Ask AI

``` shiki
> Show me the data from @github:repos/owner/repo/issues
```

This fetches data from connected MCP servers using the format @server:resource. See [MCP resources](/docs/en/mcp#use-mcp-resources) for details.

Tips:

- File paths can be relative or absolute
- @ file references add `CLAUDE.md` in the file’s directory and parent directories to context
- Directory references show file listings, not contents
- You can reference multiple files in a single message (for example, “@file1.js and @file2.js”)

------------------------------------------------------------------------

## 

[​](#use-extended-thinking-thinking-mode)

Use extended thinking (thinking mode)

[Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) is enabled by default, giving Claude space to reason through complex problems step-by-step before responding. This reasoning is visible in verbose mode, which you can toggle on with `Ctrl+O`. Additionally, Opus 4.6 introduces adaptive reasoning: instead of a fixed thinking token budget, the model dynamically allocates thinking based on your [effort level](/docs/en/model-config#adjust-effort-level) setting. Extended thinking and adaptive reasoning work together to give you control over how deeply Claude reasons before responding. Extended thinking is particularly valuable for complex architectural decisions, challenging bugs, multi-step implementation planning, and evaluating tradeoffs between different approaches.

Phrases like “think”, “think hard”, “ultrathink”, and “think more” are interpreted as regular prompt instructions and don’t allocate thinking tokens.

### 

[​](#configure-thinking-mode)

Configure thinking mode

Thinking is enabled by default, but you can adjust or disable it.

[TABLE]

To view Claude’s thinking process, press `Ctrl+O` to toggle verbose mode and see the internal reasoning displayed as gray italic text.

### 

[​](#how-extended-thinking-works)

How extended thinking works

Extended thinking controls how much internal reasoning Claude performs before responding. More thinking provides more space to explore solutions, analyze edge cases, and self-correct mistakes. **With Opus 4.6**, thinking uses adaptive reasoning: the model dynamically allocates thinking tokens based on the [effort level](/docs/en/model-config#adjust-effort-level) you select (low, medium, high). This is the recommended way to tune the tradeoff between speed and reasoning depth. **With other models**, thinking uses a fixed budget of up to 31,999 tokens from your output budget. You can limit this with the [`MAX_THINKING_TOKENS`](/docs/en/settings#environment-variables) environment variable, or disable thinking entirely via `/config` or the `Option+T`/`Alt+T` toggle. `MAX_THINKING_TOKENS` is ignored when using Opus 4.6, since adaptive reasoning controls thinking depth instead. The one exception: setting `MAX_THINKING_TOKENS=0` still disables thinking entirely on any model.

You’re charged for all thinking tokens used, even though Claude 4 models show summarized thinking

------------------------------------------------------------------------

## 

[​](#resume-previous-conversations)

Resume previous conversations

When starting Claude Code, you can resume a previous session:

- `claude --continue` continues the most recent conversation in the current directory
- `claude --resume` opens a conversation picker or resumes by name
- `claude --from-pr 123` resumes sessions linked to a specific pull request

From inside an active session, use `/resume` to switch to a different conversation. Sessions are stored per project directory. The `/resume` picker shows sessions from the same git repository, including worktrees.

### 

[​](#name-your-sessions)

Name your sessions

Give sessions descriptive names to find them later. This is a best practice when working on multiple tasks or features.

1

[](#)

Name the current session

Use `/rename` during a session to give it a memorable name:

Report incorrect code

Copy

Ask AI

``` shiki
> /rename auth-refactor
```

You can also rename any session from the picker: run `/resume`, navigate to a session, and press `R`.

2

[](#)

Resume by name later

From the command line:

Report incorrect code

Copy

Ask AI

``` shiki
claude --resume auth-refactor
```

Or from inside an active session:

Report incorrect code

Copy

Ask AI

``` shiki
> /resume auth-refactor
```

### 

[​](#use-the-session-picker)

Use the session picker

The `/resume` command (or `claude --resume` without arguments) opens an interactive session picker with these features: **Keyboard shortcuts in the picker:**

| Shortcut  | Action                                            |
|:----------|:--------------------------------------------------|
| `↑` / `↓` | Navigate between sessions                         |
| `→` / `←` | Expand or collapse grouped sessions               |
| `Enter`   | Select and resume the highlighted session         |
| `P`       | Preview the session content                       |
| `R`       | Rename the highlighted session                    |
| `/`       | Search to filter sessions                         |
| `A`       | Toggle between current directory and all projects |
| `B`       | Filter to sessions from your current git branch   |
| `Esc`     | Exit the picker or search mode                    |

**Session organization:** The picker displays sessions with helpful metadata:

- Session name or initial prompt
- Time elapsed since last activity
- Message count
- Git branch (if applicable)

Forked sessions (created with `/rewind` or `--fork-session`) are grouped together under their root session, making it easier to find related conversations.

Tips:

- **Name sessions early**: Use `/rename` when starting work on a distinct task—it’s much easier to find “payment-integration” than “explain this function” later
- Use `--continue` for quick access to your most recent conversation in the current directory
- Use `--resume session-name` when you know which session you need
- Use `--resume` (without a name) when you need to browse and select
- For scripts, use `claude --continue --print "prompt"` to resume in non-interactive mode
- Press `P` in the picker to preview a session before resuming it
- The resumed conversation starts with the same model and configuration as the original

How it works:

1.  **Conversation Storage**: All conversations are automatically saved locally with their full message history
2.  **Message Deserialization**: When resuming, the entire message history is restored to maintain context
3.  **Tool State**: Tool usage and results from the previous conversation are preserved
4.  **Context Restoration**: The conversation resumes with all previous context intact

------------------------------------------------------------------------

## 

[​](#run-parallel-claude-code-sessions-with-git-worktrees)

Run parallel Claude Code sessions with Git worktrees

When working on multiple tasks at once, you need each Claude session to have its own copy of the codebase so changes don’t collide. Git worktrees solve this by creating separate working directories that each have their own files and branch, while sharing the same repository history and remote connections. This means you can have Claude working on a feature in one worktree while fixing a bug in another, without either session interfering with the other. Use the `--worktree` (`-w`) flag to create an isolated worktree and start Claude in it. The value you pass becomes the worktree directory name and branch name:

Report incorrect code

Copy

Ask AI

``` shiki
# Start Claude in a worktree named "feature-auth"
# Creates .claude/worktrees/feature-auth/ with a new branch
claude --worktree feature-auth

# Start another session in a separate worktree
claude --worktree bugfix-123
```

If you omit the name, Claude generates a random one automatically:

Report incorrect code

Copy

Ask AI

``` shiki
# Auto-generates a name like "bright-running-fox"
claude --worktree
```

Worktrees are created at `<repo>/.claude/worktrees/<name>` and branch from the default remote branch. The worktree branch is named `worktree-<name>`. You can also ask Claude to “work in a worktree” or “start a worktree” during a session, and it will create one automatically.

### 

[​](#subagent-worktrees)

Subagent worktrees

Subagents can also use worktree isolation to work in parallel without conflicts. Ask Claude to “use worktrees for your agents” or configure it in a [custom subagent](/docs/en/sub-agents#supported-frontmatter-fields) by adding `isolation: worktree` to the agent’s frontmatter. Each subagent gets its own worktree that is automatically cleaned up when the subagent finishes without changes.

### 

[​](#worktree-cleanup)

Worktree cleanup

When you exit a worktree session, Claude handles cleanup based on whether you made changes:

- **No changes**: the worktree and its branch are removed automatically
- **Changes or commits exist**: Claude prompts you to keep or remove the worktree. Keeping preserves the directory and branch so you can return later. Removing deletes the worktree directory and its branch, discarding all uncommitted changes and commits

To clean up worktrees outside of a Claude session, use [manual worktree management](#manage-worktrees-manually).

Add `.claude/worktrees/` to your `.gitignore` to prevent worktree contents from appearing as untracked files in your main repository.

### 

[​](#manage-worktrees-manually)

Manage worktrees manually

For more control over worktree location and branch configuration, create worktrees with Git directly. This is useful when you need to check out a specific existing branch or place the worktree outside the repository.

Report incorrect code

Copy

Ask AI

``` shiki
# Create a worktree with a new branch
git worktree add ../project-feature-a -b feature-a

# Create a worktree with an existing branch
git worktree add ../project-bugfix bugfix-123

# Start Claude in the worktree
cd ../project-feature-a && claude

# Clean up when done
git worktree list
git worktree remove ../project-feature-a
```

Learn more in the [official Git worktree documentation](https://git-scm.com/docs/git-worktree).

Remember to initialize your development environment in each new worktree according to your project’s setup. Depending on your stack, this might include running dependency installation (`npm install`, `yarn`), setting up virtual environments, or following your project’s standard setup process.

### 

[​](#non-git-version-control)

Non-git version control

Worktree isolation works with git by default. For other version control systems like SVN, Perforce, or Mercurial, configure [WorktreeCreate and WorktreeRemove hooks](/docs/en/hooks#worktreecreate) to provide custom worktree creation and cleanup logic. When configured, these hooks replace the default git behavior when you use `--worktree`. For automated coordination of parallel sessions with shared tasks and messaging, see [agent teams](/docs/en/agent-teams).

------------------------------------------------------------------------

## 

[​](#get-notified-when-claude-needs-your-attention)

Get notified when Claude needs your attention

When you kick off a long-running task and switch to another window, you can set up desktop notifications so you know when Claude finishes or needs your input. This uses the `Notification` [hook event](/docs/en/hooks-guide#get-notified-when-claude-needs-input), which fires whenever Claude is waiting for permission, idle and ready for a new prompt, or completing authentication.

1

[](#)

Open the hooks menu

Type `/hooks` and select `Notification` from the list of events.

2

[](#)

Configure the matcher

Select `+ Match all (no filter)` to fire on all notification types. To notify only for specific events, select `+ Add new matcher…` and enter one of these values:

| Matcher              | Fires when                                      |
|:---------------------|:------------------------------------------------|
| `permission_prompt`  | Claude needs you to approve a tool use          |
| `idle_prompt`        | Claude is done and waiting for your next prompt |
| `auth_success`       | Authentication completes                        |
| `elicitation_dialog` | Claude is asking you a question                 |

3

[](#)

Add your notification command

Select `+ Add new hook…` and enter the command for your OS:

- macOS

- Linux

- Windows (PowerShell)

Uses [`osascript`](https://ss64.com/mac/osascript.html) to trigger a native macOS notification through AppleScript:

Report incorrect code

Copy

Ask AI

``` shiki
osascript -e 'display notification "Claude Code needs your attention" with title "Claude Code"'
```

Uses `notify-send`, which is pre-installed on most Linux desktops with a notification daemon:

Report incorrect code

Copy

Ask AI

``` shiki
notify-send 'Claude Code' 'Claude Code needs your attention'
```

Uses PowerShell to show a native message box through .NET’s Windows Forms:

Report incorrect code

Copy

Ask AI

``` shiki
powershell.exe -Command "[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); [System.Windows.Forms.MessageBox]::Show('Claude Code needs your attention', 'Claude Code')"
```

4

[](#)

Save to user settings

Select `User settings` to apply the notification across all your projects.

For the full walkthrough with JSON configuration examples, see [Automate workflows with hooks](/docs/en/hooks-guide#get-notified-when-claude-needs-input). For the complete event schema and notification types, see the [Notification reference](/docs/en/hooks#notification).

------------------------------------------------------------------------

## 

[​](#use-claude-as-a-unix-style-utility)

Use Claude as a unix-style utility

### 

[​](#add-claude-to-your-verification-process)

Add Claude to your verification process

Suppose you want to use Claude Code as a linter or code reviewer. **Add Claude to your build script:**

Report incorrect code

Copy

Ask AI

``` shiki
// package.json
{
    ...
    "scripts": {
        ...
        "lint:claude": "claude -p 'you are a linter. please look at the changes vs. main and report any issues related to typos. report the filename and line number on one line, and a description of the issue on the second line. do not return any other text.'"
    }
}
```

Tips:

- Use Claude for automated code review in your CI/CD pipeline
- Customize the prompt to check for specific issues relevant to your project
- Consider creating multiple scripts for different types of verification

### 

[​](#pipe-in-pipe-out)

Pipe in, pipe out

Suppose you want to pipe data into Claude, and get back data in a structured format. **Pipe data through Claude:**

Report incorrect code

Copy

Ask AI

``` shiki
cat build-error.txt | claude -p 'concisely explain the root cause of this build error' > output.txt
```

Tips:

- Use pipes to integrate Claude into existing shell scripts
- Combine with other Unix tools for powerful workflows
- Consider using —output-format for structured output

### 

[​](#control-output-format)

Control output format

Suppose you need Claude’s output in a specific format, especially when integrating Claude Code into scripts or other tools.

1

[](#)

Use text format (default)

Report incorrect code

Copy

Ask AI

``` shiki
cat data.txt | claude -p 'summarize this data' --output-format text > summary.txt
```

This outputs just Claude’s plain text response (default behavior).

2

[](#)

Use JSON format

Report incorrect code

Copy

Ask AI

``` shiki
cat code.py | claude -p 'analyze this code for bugs' --output-format json > analysis.json
```

This outputs a JSON array of messages with metadata including cost and duration.

3

[](#)

Use streaming JSON format

Report incorrect code

Copy

Ask AI

``` shiki
cat log.txt | claude -p 'parse this log file for errors' --output-format stream-json
```

This outputs a series of JSON objects in real-time as Claude processes the request. Each message is a valid JSON object, but the entire output is not valid JSON if concatenated.

Tips:

- Use `--output-format text` for simple integrations where you just need Claude’s response
- Use `--output-format json` when you need the full conversation log
- Use `--output-format stream-json` for real-time output of each conversation turn

------------------------------------------------------------------------

## 

[​](#ask-claude-about-its-capabilities)

Ask Claude about its capabilities

Claude has built-in access to its documentation and can answer questions about its own features and limitations.

### 

[​](#example-questions)

Example questions

Report incorrect code

Copy

Ask AI

``` shiki
> can Claude Code create pull requests?
```

Report incorrect code

Copy

Ask AI

``` shiki
> how does Claude Code handle permissions?
```

Report incorrect code

Copy

Ask AI

``` shiki
> what skills are available?
```

Report incorrect code

Copy

Ask AI

``` shiki
> how do I use MCP with Claude Code?
```

Report incorrect code

Copy

Ask AI

``` shiki
> how do I configure Claude Code for Amazon Bedrock?
```

Report incorrect code

Copy

Ask AI

``` shiki
> what are the limitations of Claude Code?
```

Claude provides documentation-based answers to these questions. For executable examples and hands-on demonstrations, refer to the specific workflow sections above.

Tips:

- Claude always has access to the latest Claude Code documentation, regardless of the version you’re using
- Ask specific questions to get detailed answers
- Claude can explain complex features like MCP integration, enterprise configurations, and advanced workflows

------------------------------------------------------------------------

## 

[​](#next-steps)

Next steps

[](/docs/en/best-practices)

## Best practices

Patterns for getting the most out of Claude Code

[](/docs/en/how-claude-code-works)

## How Claude Code works

Understand the agentic loop and context management

[](/docs/en/features-overview)

## Extend Claude Code

Add skills, hooks, MCP, subagents, and plugins

[](https://github.com/anthropics/claude-code/tree/main/.devcontainer)

## Reference implementation

Clone our development container reference implementation

Was this page helpful?

Yes

No

[Extend Claude Code](/docs/en/features-overview)[Best practices](/docs/en/best-practices)

[Claude Code Docs home page](/docs)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

Company

[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)

Help and security

[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)

Learn

[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)

Terms and policies

[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)

Assistant

Responses are generated using AI and may contain mistakes.
