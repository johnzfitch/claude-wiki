---
title: "Claude Code by Anthropic | AI Coding Agent, Terminal, IDE"
source_url: "https://www.claude.com/product/claude-code"
category: "15-Claude-AI-Features"
fetched_at: "2026-09-29T06:32:52Z"
tags: ["agents", "claude-ai", "claude-code", "slack"]
---

# Claude Code

Hand Claude a bug fix, test, or multi-day migration. Steer and review from your terminal, IDE, Slack, or web.

Claude Code is included in Claude Pro and Max plans. [See plans](#pricing)

[Download for macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)[Read documentation](../02-Claude-Code-CLI/code-home.md)

(opens in new tab)

Available for macOS, Linux, and Windows.

Other ways to use Claude Code:

- [Terminal (opens in new tab)](../01-Getting-Started/quickstart.md#step-1-install-claude-code)
- [Web (opens in new tab)](https://claude.ai/code)
- [iOS (opens in new tab)](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684)
- [Android (opens in new tab)](https://play.google.com/store/apps/details?id=com.anthropic.claude)
- [GitHub (opens in new tab)](../02-Claude-Code-CLI/github-actions.md)
- [VS Code (opens in new tab)](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
- [JetBrains (opens in new tab)](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)
- [Slack (opens in new tab)](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)

Home

Code

New session

Routines

Customize

More

Pinned

Add a dark mode toggle to settings

Scheduled

Weekly dependency audit

Recents

Fix the double-charge bug in checkout

Write tests for the payments module

Explain what this repo does

Layout's broken on mobile

Debug flaky CI tests

Susan Sample

acme-storefront/Fix the double-charge bug in checkout

We're seeing duplicate charges when customers double-click the pay button. Can you find and fix it?

I can reproduce it: the checkout form fires two `POST /charges` requests when the button is clicked twice before the first response lands. Tracing where the idempotency key should be.

just now

Read 3 files, searched the checkout flow

Ran agent · Reproduce the double-submit against a test charge

Root cause: `createCharge()` generates a new idempotency key per call instead of per checkout session, so the gateway treats the second click as a fresh charge. Fixing that and disabling the button while a charge is in flight.

just now

Edited **charges.ts** +9 -3

Auto

Opus

Extra high

Home

Code

New session

Routines

Customize

More

Pinned

Add a dark mode toggle to settings

Scheduled

Weekly dependency audit

Recents

Fix the double-charge bug in checkout

Write tests for the payments module

Explain what this repo does

Layout's broken on mobile

Debug flaky CI tests

Susan Sample

acme-dashboard/Add a dark mode toggle to settings

Add a dark mode toggle to the settings page. Should remember the choice and follow the system default until they pick one.

There's already a `ThemeProvider` wrapping the app but it's hard-wired to light. I'll lift the mode into context, persist it to `localStorage`, and add a Light / Dark segmented control under **Settings → Appearance**.

just now

Read 4 files, searched the codebase

Edited **ThemeProvider.tsx** +18 -2

src/theme/ThemeProvider.tsx

10`export`` ``function`` ``ThemeProvider``({``children``}:`` ``{``children``:`` ``ReactNode``})`` ``{`

11+` ``const`` ``prefersDark`` ``=`` ``useMediaQuery``('(``prefers``-``color``-``scheme``:`` ``dark``)')`

12` ``const`` ``stored`` ``=`` ``localStorage``.``getItem``('``theme``')`

13+` ``const`` ``[``mode``,`` ``setMode``]`` ``=`` ``useState``(``stored`` ``??`` ``(``prefersDark`` ``?`` ``'dark'`` ``:`` ``'light'``))`

14` `

15+` ``useEffect``(()`` ``=>`` ``{`

16+` ``localStorage``.``setItem``('``theme``',`` ``mode``)`

17+` ``},`` ``[``mode``])`

18` `

19` ``return`` ``(`

20` ``<``ThemeContext``.``Provider`` ``value``={{``mode``,`` ``setMode``}}>`

21` ``{``children``}`

Edited **settings.tsx** +21 -0

Edited **tokens.css** +24 -0

Ran 2 commands

Done — the **Appearance** section now has the toggle. Preview's on the right; flip it and the whole app should follow. Reduce-motion and density rows are stubbed so the page doesn't look bare.

just now

\#112acme-dashboardclaude/settings-dark-mode-Xk4fq CI

Auto

Opus

Extra high

localhost:5173/settings

Appearance

Theme

Choose how the dashboard looks.

Light

Dark

Density

Compact rows for power users.

Default

Compact

Reduce motion

Disable animations and transitions.

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

## Get started with Claude Code

Individual

Team & Enterprise

### Pro

Claude Code is included in your Pro plan. Perfect for short coding sprints in small codebases.

\$17

Per month with annual subscription discount (\$200 billed up front). \$20 if billed monthly.

[Try Claude (opens in new tab)](https://claude.ai/login?plan=pro)

### Max 5x

Claude Code is included in your Max plan. Great value for everyday use in larger codebases.

\$100

Per month

[Try Claude (opens in new tab)](https://claude.ai/login?plan=max)

### Max 20x

Even more Claude Code included in your Max plan. Great value for power users with the most access to Claude models.

\$200

Per month

[Try Claude (opens in new tab)](https://claude.ai/login?plan=max)

[Usage limits apply](../22-Safety-Policy/usage-limit-best-practices.md). Prices shown don't include applicable tax. Price and plans are subject to change at Anthropic's discretion.

[Usage limits apply](../22-Safety-Policy/usage-limit-best-practices.md). Price and plans are subject to change at Anthropic's discretion.

## Latest feature announcements


### **Projects:** Group related coding sessions so you can run and easily supervise multiple Claude agents at once. Available on Claude Code Desktop.

BlogSep 17, 2026


### **Auto mode by default:** Claude Code now runs in auto mode by default on Pro, Max, and Team plans, so it can work longer while still catching risky commands.

BlogAug 7, 2026


### **Self-hosted environments:** Run Claude Code sessions on your own infrastructure, inside your network and next to your internal services. Now in public beta.

BlogAug 6, 2026


### **Artifacts:** Preview in-progress work as a live, interactive artifact built from your session context, and share it with your team.

BlogJun 18, 2026

[View changelog](../02-Claude-Code-CLI/changelog.md)

(opens in new tab)

## What Claude Code can take on

Claude Code builds the plan, asks clarifying questions, and handles work that runs for hours or days.

Get Claude Code

- [Desktop](https://www.claude.com/download)
- [VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
- [JetBrains](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)
- [On the web](https://claude.ai/code)
- [Slack](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)

curl -fsSL https://claude.ai/install.sh \| bash

Or read the [documentation](../02-Claude-Code-CLI/code-home.md)

[Try Claude Code (opens in new tab)](https://claude.ai/code)[Developer docs (opens in new tab)](../02-Claude-Code-CLI/code-home.md)

Onboarding

Triage issues

Migrate code

``` Terminal-module-scss-module__gNncDq__pre
I'm new to this codebase. Can you explain it to me?

⏺︎ I'll analyze the Excalidraw codebase structure and provide a high-level overview.

⏺︎ Analyze(what: "Excalidraw codebase structure and provide a high-level overview of what it is, its main components, and how they're organized. Focus on understanding the project's purpose, architecture, and key features.")

Excalidraw is an open-source virtual whiteboard application with a hand-drawn style. It's designed for creating diagrams, wireframes, and collaborative drawings.

## Purpose
- Web-based drawing tool with infinite canvas
- Hand-drawn aesthetic with support for shapes, arrows, text
- End-to-end encrypted collaboration
- Works offline as a PWA (Progressive Web App)

## Architecture
The project is organized as a monorepo with these main components:

1. Core Package (packages/excalidraw)
- React component library for embedding Excalidraw in any application
- Handles drawing, rendering, and core functionality
- Uses roughjs for the hand-drawn style
- Includes export capabilities (PNG, SVG)

2. Web Application (excalidraw-app/)
- Full-featured web app at excalidraw.com
- Built on top of the core package
- Adds collaboration features, local storage, sharing

3. Support Packages
- common - Shared utilities and constants
- element - Element manipulation and type definitions
- math - Mathematical functions for drawing
- utils - General utility functions

4. Examples
- Integration examples (Next.js, browser script)
- Shows how to embed Excalidraw in different environments

5. Documentation (dev-docs/)
- API documentation
- Integration guides
- Component documentation

## Key Features
- Real-time collaboration with end-to-end encryption
- Export to various formats (PNG, SVG, JSON)
- Customizable drawing tools (rectangle, circle, arrows, freehand)
- Dark mode support
- Localization
- Library of shapes and components
- Arrow bindings and labels
- Image support

## Technology Stack
- React for UI
- TypeScript for type safety
- Firebase for collaboration backend
- Jotai for state management
- Vite for development and building
- IndexedDB/LocalStorage for offline storage

The architecture allows for both using Excalidraw as a component in other applications and as a standalone web application with additional features.
```

- ### Code onboarding

  Claude Code maps and explains entire codebases in a few seconds. It uses agentic search to understand project structure and dependencies without you having to manually select context files.

- ### Turn issues into PRs

  Stop bouncing between tools. Claude Code works with GitHub, GitLab, and your command line tools to read issues, write code, run tests, and open pull requests.

- ### Run multi-hour refactors and migrations

  Claude Code follows imports across the repo, runs your tests, and keeps going when something breaks.

## Meets you where you code

### Start in your terminal

Super powerful terminal integration. Works with all your CLI tools alongside any IDE.

curl -fsSL https://claude.ai/install.sh \| bash

Or read the [documentation](../02-Claude-Code-CLI/code-home.md)

[Try Claude Code (opens in new tab)](https://claude.ai/code)[Developer docs (opens in new tab)](../02-Claude-Code-CLI/code-home.md)

### Integrate with your editor

Native extensions for VS Code (+ Cursor, Devin Desktop) and JetBrains IDEs.

[VS Code (opens in new tab)](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)[JetBrains (opens in new tab)](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)

### Access anywhere

Quick access from browser, mobile app, or Claude on desktop. Great for parallel work or on-the-go coding.

[Open in browser (opens in new tab)](https://claude.ai/code)[Download app](https://www.claude.com/download)

## Kick off coding tasks in Slack

[Add to Slack (opens in new tab)](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)[Learn more](../14-Connectors/claude-for-slack.md)

## What developers are saying

- 

  > “Claude Code has dramatically accelerated our team's coding efficiency. I can now write EDA code in a notebook—pulling data, training a model, and evaluating it with basic metrics—and then ask Claude to convert that into a Metaflow pipeline. This process saves 1-2 days of routine (and often boring!) work per model.”

  Anton Biryukov, Staff Software Engineer

  [Read story](../18-Industry-UseCases/ramp.md)

- 

  > “With Claude, we're not just automating customer service—we're elevating it to truly human quality. This lets support teams think more strategically about customer experience and what makes interactions genuinely valuable.”

  Fergal Reid, VP of AI

  [Read story](../18-Industry-UseCases/intercom.md)

- 

  > “Claude Code is moving our team up a level: we decide what needs to happen, and smooth the process so it can build and verify end-to-end. A big part of my job now is to keep as many instances of Claude Code busy as possible.”

  Simon Last, Co-founder

  [Read story](../18-Industry-UseCases/notion.md)

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

## Connects with your favorite command line tools

Your terminal is where real work happens. Claude Code connects with the tools that power development—deployment, databases, monitoring, version control. Rather than adding another interface to juggle, it enhances your existing stack.

## FAQ

### How do I get started with Claude?

You can access Claude Code with a Claude Pro or Max plan, a Team or Enterprise plan, or a Claude Console account. [Download Claude Code](../02-Claude-Code-CLI/code-home.md) and sign in with your respective Claude or Console credentials.

### What kind of tasks can Claude Code handle?

Claude Code can handle routine work like bug fixes and testing, and larger jobs like refactors and new features that are long-running and asynchronous.

You set the direction as the architect and orchestrator, and Claude Code does the work. Describe what you want and it plans, writes code, runs tests, and opens pull requests. It can work on several tasks at once, and surface decisions you need to make for it to keep going.

### How does Claude Code work with my existing tools?

Claude Code runs in your terminal and works alongside your preferred IDE and development tools without requiring you to change your workflow. Claude Code can also use command line tools (like Git) and MCP servers (like GitHub) to extend its own capabilities using your tools.

### Is Claude Code secure?

Yes. Claude Code runs locally in your terminal and talks directly to model APIs without requiring a backend server or remote code index. It also asks for permission before making changes to your files or running commands.

### What are the system requirements to run Claude Code?

Claude Code works on macOS, Linux, and Windows. [See full system requirements](../01-Getting-Started/setup.md#system-requirements).

### How much does Claude Code cost?

When used with a Claude Console account, Claude Code consumes API tokens at [standard API pricing](../17-Billing-Plans/pricing.md#api).

### Does Claude Code work with the Claude desktop app?

Yes. Max, Pro, Team, and Enterprise users can access Claude Code on the [Claude desktop app](https://claude.com/download).

### What is fast mode on Claude Code?

Fast mode is a high-speed configuration for Opus 5.5, making the model 2.5x faster at a higher cost per token. Fast mode is available:

- In research preview on Claude Code, and is priced at \$8/\$40 per million tokens.
- On consumption-based plans.
- Via usage credits for users on subscription plans.

## Get the technical rundown


### Claude Code documentation

Developer docs


### Common workflows

Developer docs


### Using CLAUDE.md files

Blog


### Introduction to agentic coding

Blog


### How Anthropic teams use Claude Code

Blog


### Fix software bugs faster with Claude

Blog

## Create what’s exciting. Maintain what’s essential.

Use Claude Code where you work

Get Claude Code

- [Desktop](https://www.claude.com/download)
- [VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
- [JetBrains](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)
- [On the web](https://claude.ai/code)
- [Slack](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)

curl -fsSL https://claude.ai/install.sh \| bash

Or read the [documentation](../02-Claude-Code-CLI/code-home.md)

[Try Claude Code (opens in new tab)](https://claude.ai/code)[Developer docs (opens in new tab)](../02-Claude-Code-CLI/code-home.md)
