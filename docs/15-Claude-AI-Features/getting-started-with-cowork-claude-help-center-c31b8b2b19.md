---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-08T20:52:06Z"
source_url: "https://support.claude.com/en/articles/13345190-getting-started-with-cowork"
title: "Getting started with Cowork | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

Table of contents

[](#h_9fe40dc9c6)

[](#h_286474afcc)

[](#h_bfc64d50fa)

[](#h_e674ec5e40)

[](#h_785de7234a)

[](#h_ab45b74d27)

[](#h_d19b28bf88)

[](#h_8b0de049f1)

[](#h_ca4a8cb8d9)

[](#h_80193b6749)

[All Collections](/en/)

[Claude](https://support.claude.com/en/collections/4078531-claude)

[Features and Capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities)

Getting started with Cowork

# Getting started with Cowork

Updated yesterday

Table of contents

[](#h_9fe40dc9c6)

[](#h_286474afcc)

[](#h_bfc64d50fa)

[](#h_e674ec5e40)

[](#h_785de7234a)

[](#h_ab45b74d27)

[](#h_d19b28bf88)

[](#h_8b0de049f1)

[](#h_ca4a8cb8d9)

[](#h_80193b6749)

This article explains how to use **[Cowork](https://claude.com/product/cowork)**, a research preview that brings Claude Code's agentic capabilities to Claude Desktop for knowledge work beyond coding.

Cowork is available as a research preview for all paid plans (Pro, Max, Team, Enterprise) using the Claude Desktop app on macOS.

## **[Download for macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)**

## What is Cowork?

Cowork uses the same agentic architecture that powers Claude Code, now accessible within Claude Desktop and without opening the terminal. Instead of responding to prompts one at a time, Claude can take on complex, multi-step tasks and execute them on your behalf.

With Cowork, you can describe an outcome, step away, and come back to finished work—formatted documents, organized files, synthesized research, and more.

**Important:**

- Cowork is a research preview with unique risks due to its agentic nature and internet access.

- Cowork respects your current network egress permissions.

- Cowork stores conversation history locally on your computer, so is not subject to Anthropic’s **[data retention timeframe](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)**.

- Cowork activity is not captured in Audit Logs, Compliance API, or Data Exports. Do not use Cowork for regulated workloads.

- Please review **[Using Cowork safely](https://support.claude.com/en/articles/13364135-using-cowork-safely)** for more information.

For important limitations and considerations for Team and Enterprise organizations using Cowork, see **[Cowork for Team and Enterprise plans](https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans)**.

### Key capabilities

- **Direct local file access:** Claude can read from and write to your local files without manual uploads or downloads.

- **Sub-agent coordination:** Claude breaks complex work into smaller tasks and coordinates parallel workstreams to complete them.

- **Professional outputs:** Generate polished deliverables like Excel spreadsheets with working formulas, PowerPoint presentations, and formatted documents.

- **Long-running tasks:** Work on complex tasks for extended periods without conversation timeouts or context limits interrupting your progress.

------------------------------------------------------------------------

## How Cowork runs your tasks

Cowork runs directly on your computer, giving Claude access to the files you choose to share. Code runs safely in an isolated space, but Claude can make real changes to your files.

When you start a task in Cowork, Claude:

1.  Analyzes your request and creates a plan.

2.  Breaks complex work into subtasks when needed.

3.  Executes work in a virtual machine (VM) environment.

4.  Coordinates multiple workstreams in parallel if appropriate.

5.  Delivers finished outputs directly to your file system.

You maintain visibility into what Claude is planning and doing throughout the process so you can steer when it matters, or let Claude run independently.

------------------------------------------------------------------------

## Getting started

### Requirements

- **Claude Desktop app:** Cowork requires the **[desktop app](https://support.claude.com/en/articles/10065433-installing-claude-desktop)** for macOS and is not available on web or mobile.

- **Paid Claude subscription:** This research preview is available to paid Claude plans (Pro, Max, Team, Enterprise) only.

- **Active internet connection:** Required throughout the session.

### Accessing Cowork

1.  Open Claude Desktop for macOS.

2.  Look for the mode selector that includes "Chat" and the Cowork tab.

3.  Click the Cowork tab to switch modes to “Tasks”.

4.  Describe the task you want Claude to complete.

5.  Review Claude's approach, then let it run.

**Note:** The Claude Desktop app must remain open while Claude is working. If you close the app, your session will end.

## What to expect during a task

When Claude is working on a task in Cowork:

- **Progress indicators** show what Claude is doing at each step.

- **Transparency:** Claude surfaces its reasoning and approach so you can follow along.

- **Steering:** You can jump in to course-correct or provide additional direction mid-task.

- **Parallel work:** For complex tasks, Claude may coordinate multiple sub-agents working simultaneously.

- **Deletion protection:** When using Cowork, Claude requires your explicit permission before permanently deleting any files. You will see a permission prompt and will need to select "Allow" before Claude is allowed to perform deletion tasks.

Tasks can run for extended periods depending on complexity. You can monitor progress or step away and return when Claude finishes.

------------------------------------------------------------------------

## Customizing Cowork with plugins

Plugins are ready-made bundles that let you customize how Claude works for your role, team, and company when using Cowork. Each plugin combines skills, connectors, slash commands, and sub-agents into a single package.

To help you get started, Cowork includes a library of plugins our team built for common knowledge work functions:

- **Productivity** — Manage tasks, calendars, and daily workflows

- **Enterprise search** — Find information across your company's tools and docs

- **Sales** — Research prospects, prep deals, and follow your sales process

- **Finance** — Analyze financials, build models, and track key metrics

- **Data** — Query, visualize, and interpret datasets

- **Legal** — Review documents, flag risks, and track compliance

- **Marketing** — Draft content, plan campaigns, and manage launches

- **Customer support** — Triage issues, draft responses, and surface solutions

- **Product management** — Write specs, prioritize roadmaps, and track progress

- **Biology research** — Search literature, analyze results, and plan experiments

In addition to the function plugins listed above, we provide **Plugin Create**: a plugin that helps you create custom plugins from scratch.

For the full collection of Anthropic-built plugins, visit **[GitHub](https://github.com/anthropics/knowledge-work-plugins)**.

### Adding and customizing plugins

To add a plugin:

1.  Open Claude Desktop for macOS.

2.  Navigate to the **Cowork** tab.

3.  Click “Plugins” in the left sidebar.

4.  Browse available plugins and click to install.

5.  You can also click “Upload plugin” to upload a custom plugin file.

**Note:** Plugins are saved locally to your machine. Organization-wide plugin provisioning is coming in a future update.

After installing or uploading a plugin, you can customize it to better fit your workflow:

1.  While viewing an installed plugin, click the “Customize” button in the upper right corner.

2.  This will automatically input a Cowork prompt asking Claude to customize the plugin you chose.

3.  Click “Let’s go” to start working with Claude to customize the plugin.

### Using plugins

Each plugin you install adds commands you can invoke while using Cowork. Type / or click the “+” button to see available commands from your installed plugins.

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/2010180867/ea6555f889c8ae2b676b8e33214e/975b77da-9bb4-436e-bdf4-cd6318fd593c?expires=1770585300&signature=318bebfb54b2d292b22e28d4338a5a03409b7507e512849246f19a4c20860c77&req=diAmFsh2nYlZXvMW1HO4zYdmTSrFanQtRKEe0R6ky%2By8LEUJpKiMOiOIoTtx%0AikMz%2BuzoN2zYFdlgj0s%3D%0A)

------------------------------------------------------------------------

## Usage limits

Working on tasks with Cowork consumes more of your usage allocation than chatting with Claude. This is because complex, multi-step tasks are compute-intensive and require more tokens to execute.

If you find yourself hitting usage limits frequently when using the Cowork research preview, consider:

- Batching related work into single sessions.

- Using standard chat for simpler tasks that don't require file access or extended execution.

- Monitoring your individual usage in **[Settings \> Usage](http://claude.ai/settings/usage)**.

See **[Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)** for more information.

------------------------------------------------------------------------

## Example use cases

Cowork is designed for complex, multi-step work that benefits from file access and extended execution time. Here are some examples:

### File and document management

- **Organize files:** "Organize my Downloads folder by type and date" — Claude can sort hundreds of files into categorized folders.

- **Process receipts:** Drop receipts in a folder and ask Claude to create a formatted expense report.

- **Batch rename:** Rename files with consistent patterns like YYYY-MM-DD formatting.

### Research and analysis

- **Research synthesis:** Combine information from web searches, articles, papers, and notes into coherent reports or summaries.

- **Transcript analysis:** Extract themes, key points, and action items from meeting notes, interviews, or lecture recordings.

- **Personal knowledge synthesis:** Analyze your notes, journals, or research files to surface patterns, themes, and connections you might have missed.

### Document creation

- **Spreadsheets with formulas:** Generate Excel files with working VLOOKUP, conditional formatting, and multiple tabs—not just CSVs that need fixing.

- **Presentations:** Create slide decks from rough notes or meeting transcripts.

- **Reports from messy inputs:** Turn voice memos and scattered notes into polished documents.

### Data and analysis

- **Statistical analysis:** Outlier detection, cross-tabulation, and time-series analysis on your data files.

- **Data visualization:** Generate charts using your data.

- **Data transformation:** Clean, transform, and process datasets.

------------------------------------------------------------------------

## Permissions and security

Cowork runs in a virtual machine (VM) on your computer. This provides several security benefits:

- **Controlled environment:** Claude operates within defined boundaries, with controlled file and network access.

- **Isolation:** The VM environment is separate from your main operating system.

**Important:** While the VM provides isolation, Claude does have access to local files you grant it permission to access. Review Claude's planned actions before allowing it to proceed, especially when working with sensitive files.

### Permissions

Permissions work the same as for chat. You control:

1.  Which **[MCPs you connect to Claude](https://claude.ai/settings/connectors)** and how often they ask for permission.

2.  **[Claude’s internet access](https://claude.ai/settings/capabilities)**

Please carefully assess how much you trust an MCP or website before extending access beyond Claude’s default settings.

------------------------------------------------------------------------

## Current limitations

Cowork is a feature preview, which means some capabilities are not yet available:

- **No projects support:** You cannot use Cowork within projects at this time.

- **No memory across sessions:** Claude does not retain memory from previous Cowork sessions.

- **No chat or artifact sharing:** Sessions cannot be shared with others.

- **Desktop for macOS only:** Cowork is only available in the Claude Desktop app for macOS and does not sync across devices.

- **Session persistence:** The desktop app must remain open for your session to continue. Closing the app ends the session.

We're iterating on Cowork based on feedback. If you encounter issues or have suggestions, use the feedback button in the app to share feedback with our team.

------------------------------------------------------------------------

## Troubleshooting

### I'm seeing "Setting up Claude's workspace" when I start Cowork; what does this mean?

This message is expected and indicates that Cowork is updating to the most recent version to apply any fixes and improvements.

### Claude stopped working on my task

Ensure the Claude Desktop app was open throughout the entire task. If the app was closed or your computer went to sleep, the session may have ended.

### I'm hitting usage limits quickly

Cowork consumes more usage than standard chat. Try using standard chat for simpler tasks and reserve Cowork for complex, multi-step work that benefits from file access.

### Files aren't appearing where expected

Check that you've granted Claude the appropriate file access permissions. Review the output location Claude specified when completing the task.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/8114491-getting-started-with-claude)

Getting started with Claude

[](https://support.claude.com/en/articles/10065433-installing-claude-desktop)

Installing Claude Desktop

[](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)

What is the Max plan?

[](https://support.claude.com/en/articles/13364135-using-cowork-safely)

Using Cowork safely

[](https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans)

Cowork for Team and Enterprise plans

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
