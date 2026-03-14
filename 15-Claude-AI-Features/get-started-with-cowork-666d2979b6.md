---
category: "15-Claude-AI-Features"
fetched_at: "2026-03-14T10:16:51Z"
source_url: "https://support.claude.com/en/articles/13345190-get-started-with-cowork"
title: "Get started with Cowork | Claude Help Center"
---

# Get started with Cowork

Updated today


This article explains how to use **[Cowork](https://claude.com/product/cowork)**, a research preview that brings Claude Code's agentic capabilities to Claude Desktop for knowledge work beyond coding.

## Availability

Cowork is available as a research preview for paid plans (Pro, Max, Team, Enterprise) on:

- **Claude Desktop for macOS**

  - **[Click here](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)** to download

- **Claude Desktop for Windows** (x64 only)

  - Cowork requires the latest version of Claude for Windows. Download or update at **[claude.com/download](https://claude.com/download)**.

  - Windows arm64 is not supported.

------------------------------------------------------------------------

## What is Cowork?

Cowork uses the same agentic architecture that powers Claude Code, now accessible within Claude Desktop and without opening the terminal. Instead of responding to prompts one at a time, Claude can take on complex, multi-step tasks and execute them on your behalf.

With Cowork, you can describe an outcome, step away, and come back to finished work—formatted documents, organized files, synthesized research, and more. With the introduction of scheduled tasks, Claude can complete work for you automatically—something that isn't possible in regular chats outside of Cowork.

**Important:**

- Cowork is a research preview with unique risks due to its agentic nature and internet access.

- Cowork respects your current network egress permissions.

  - Network egress permissions don't apply to the web search tool.

- Cowork stores conversation history locally on your computer, so is not subject to Anthropic’s **[data retention timeframe](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)**.

- Cowork activity is not captured in Audit Logs, Compliance API, or Data Exports. Do not use Cowork for regulated workloads.

- Please review **[Use Cowork safely](https://support.claude.com/en/articles/13364135-using-cowork-safely)** for more information.

For important limitations and considerations for Team and Enterprise organizations using Cowork, see **[Cowork for Team and Enterprise plans](https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans)**.

### Key capabilities

- **Direct local file access:** Claude can read from and write to your local files without manual uploads or downloads.

- **Sub-agent coordination:** Claude breaks complex work into smaller tasks and coordinates parallel workstreams to complete them.

- **Professional outputs:** Generate polished deliverables like Excel spreadsheets with working formulas, PowerPoint presentations, and formatted documents.

- **Long-running tasks:** Work on complex tasks for extended periods without conversation timeouts or context limits interrupting your progress.

- **Scheduled tasks:** Create and save tasks that you can have Claude run on-demand, or automatically on a cadence of your choosing.

- **Spreadsheets and presentations:** Cowork can produce spreadsheets and slides that can be further edited with Claude for Excel and Powerpoint.

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

## Get started

### Requirements

- **Claude Desktop app:** Cowork requires the **[desktop app](https://support.claude.com/en/articles/10065433-installing-claude-desktop)** for macOS or Windows and is not available on web or mobile.

- **Paid Claude subscription:** This research preview is available to paid Claude plans (Pro, Max, Team, Enterprise) only.

- **Active internet connection:** Required throughout the session.

### Accessing Cowork

1.  Open Claude Desktop.

2.  Look for the mode selector that includes "Chat" and the Cowork tab.

3.  Click the "Cowork" tab to switch modes to “Tasks”.

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

## Add global and folder instructions

### Global instructions

You can give Claude standing instructions that apply to every Cowork session. Use this to specify your preferred tone, output format, or background on your role.

To set global instructions:

1.  Navigate to Settings \> Cowork within Claude Desktop.

2.  Click “Edit” next to **Global instructions**.

3.  Type your instructions in the text box and click “Save”:


### Folder instructions

Folder instructions add project-specific context to Cowork when you select a local folder. Claude can also update these on its own during a session.

------------------------------------------------------------------------

## Cowork plugins

Plugins customize how Claude works for your role, team, and company in Cowork. Each one bundles skills, connectors, and sub-agents into a single package. For details on finding, installing, and customizing plugins, see **[Use plugins in Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)**.

------------------------------------------------------------------------

## Schedule recurring tasks

You can set up tasks that Claude runs automatically or on demand. To schedule a task, type `/schedule` in any Cowork task. You can also click “Scheduled” in the left sidebar to view, create, and manage your scheduled tasks.

Scheduled tasks only run while your computer is awake and the Claude Desktop app is open.

For more in-depth details, see **[Schedule recurring tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork)**.

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

- **No memory across sessions:** Claude does not retain memory from previous Cowork sessions.

- **No chat or artifact sharing:** Sessions cannot be shared with others.

- **Desktop only:** Cowork is only available in the Claude Desktop app and does not sync across devices.

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


Installing Claude Desktop


Use Cowork safely


Use Cowork on Team and Enterprise plans


Install financial services plugins for Cowork


Schedule recurring tasks in Cowork
