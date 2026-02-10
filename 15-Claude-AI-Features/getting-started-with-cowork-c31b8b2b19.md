---
category: "15-Claude-AI-Features"
source_url: "https://support.claude.com/en/articles/13345190-getting-started-with-cowork"
---


This article explains how to use Cowork, a research preview that brings Claude Code's agentic capabilities to Claude Desktop for knowledge work beyond coding.

Cowork is available as a research preview for all paid plans (Pro, Max, Team, Enterprise) using the Claude Desktop app on macOS.

 

Download for macOS

 

What is Cowork?

Cowork uses the same agentic architecture that powers Claude Code, now accessible within Claude Desktop and without opening the terminal. Instead of responding to prompts one at a time, Claude can take on complex, multi-step tasks and execute them on your behalf.

 

With Cowork, you can describe an outcome, step away, and come back to finished work—formatted documents, organized files, synthesized research, and more.

Important: 

Cowork is a research preview with unique risks due to its agentic nature and internet access.

Cowork respects your current network egress permissions.

Cowork stores conversation history locally on your computer, so is not subject to Anthropic’s data retention timeframe.

Cowork activity is not captured in Audit Logs, Compliance API, or Data Exports. Do not use Cowork for regulated workloads.

Please review Using Cowork safely for more information.

For important limitations and considerations for Team and Enterprise organizations using Cowork, see Cowork for Team and Enterprise plans.

 

Key capabilities

Direct local file access: Claude can read from and write to your local files without manual uploads or downloads.

Sub-agent coordination: Claude breaks complex work into smaller tasks and coordinates parallel workstreams to complete them.

Professional outputs: Generate polished deliverables like Excel spreadsheets with working formulas, PowerPoint presentations, and formatted documents.

Long-running tasks: Work on complex tasks for extended periods without conversation timeouts or context limits interrupting your progress.

 

 

How Cowork runs your tasks

Cowork runs directly on your computer, giving Claude access to the files you choose to share. Code runs safely in an isolated space, but Claude can make real changes to your files.

 

When you start a task in Cowork, Claude:

Analyzes your request and creates a plan.

Breaks complex work into subtasks when needed.

Executes work in a virtual machine (VM) environment.

Coordinates multiple workstreams in parallel if appropriate.

Delivers finished outputs directly to your file system.

You maintain visibility into what Claude is planning and doing throughout the process so you can steer when it matters, or let Claude run independently.

 

 

Getting started
Requirements

Claude Desktop app: Cowork requires the desktop app for macOS and is not available on web or mobile.

Paid Claude subscription: This research preview is available to paid Claude plans (Pro, Max, Team, Enterprise) only.

Active internet connection: Required throughout the session.

Accessing Cowork

Open Claude Desktop for macOS.

Look for the mode selector that includes "Chat" and the Cowork tab.

Click the Cowork tab to switch modes to “Tasks”.

Describe the task you want Claude to complete.

Review Claude's approach, then let it run.

Note: The Claude Desktop app must remain open while Claude is working. If you close the app, your session will end.

 

What to expect during a task

When Claude is working on a task in Cowork:

Progress indicators show what Claude is doing at each step.

Transparency: Claude surfaces its reasoning and approach so you can follow along.

Steering: You can jump in to course-correct or provide additional direction mid-task.

Parallel work: For complex tasks, Claude may coordinate multiple sub-agents working simultaneously.

Deletion protection: When using Cowork, Claude requires your explicit permission before permanently deleting any files. You will see a permission prompt and will need to select "Allow" before Claude is allowed to perform deletion tasks.

Tasks can run for extended periods depending on complexity. You can monitor progress or step away and return when Claude finishes.

 

 

Customizing Cowork with plugins

Plugins are ready-made bundles that let you customize how Claude works for your role, team, and company when using Cowork. Each plugin combines skills, connectors, slash commands, and sub-agents into a single package.

 

To help you get started, Cowork includes a library of plugins our team built for common knowledge work functions:

Productivity — Manage tasks, calendars, and daily workflows

Enterprise search — Find information across your company's tools and docs

Sales — Research prospects, prep deals, and follow your sales process

Finance — Analyze financials, build models, and track key metrics

Data — Query, visualize, and interpret datasets

Legal — Review documents, flag risks, and track compliance

Marketing — Draft content, plan campaigns, and manage launches

Customer support — Triage issues, draft responses, and surface solutions

Product management — Write specs, prioritize roadmaps, and track progress

Biology research — Search literature, analyze results, and plan experiments

In addition to the function plugins listed above, we provide Plugin Create: a plugin that helps you create custom plugins from scratch.

 

For the full collection of Anthropic-built plugins, visit GitHub.

 

Adding and customizing plugins

To add a plugin:

Open Claude Desktop for macOS.

Navigate to the Cowork tab.

Click “Plugins” in the left sidebar.

Browse available plugins and click to install.

You can also click “Upload plugin” to upload a custom plugin file.

Note: Plugins are saved locally to your machine. Organization-wide plugin provisioning is coming in a future update.

After installing or uploading a plugin, you can customize it to better fit your workflow:

While viewing an installed plugin, click the “Customize” button in the upper right corner.

This will automatically input a Cowork prompt asking Claude to customize the plugin you chose.

Click “Let’s go” to start working with Claude to customize the plugin.

 

Using plugins

Each plugin you install adds commands you can invoke while using Cowork. Type / or click the “+” button to see available commands from your installed plugins.

 

 

 

Usage limits

Working on tasks with Cowork consumes more of your usage allocation than chatting with Claude. This is because complex, multi-step tasks are compute-intensive and require more tokens to execute.

 

If you find yourself hitting usage limits frequently when using the Cowork research preview, consider:

Batching related work into single sessions.

Using standard chat for simpler tasks that don't require file access or extended execution.

Monitoring your individual usage in Settings > Usage.

See Usage limit best practices for more information.

 

 

Example use cases

Cowork is designed for complex, multi-step work that benefits from file access and extended execution time. Here are some examples:

 

File and document management

Organize files: "Organize my Downloads folder by type and date" — Claude can sort hundreds of files into categorized folders.

Process receipts: Drop receipts in a folder and ask Claude to create a formatted expense report.

Batch rename: Rename files with consistent patterns like YYYY-MM-DD formatting.

Research and analysis

Research synthesis: Combine information from web searches, articles, papers, and notes into coherent reports or summaries.

Transcript analysis: Extract themes, key points, and action items from meeting notes, interviews, or lecture recordings.

Personal knowledge synthesis: Analyze your notes, journals, or research files to surface patterns, themes, and connections you might have missed.

Document creation

Spreadsheets with formulas: Generate Excel files with working VLOOKUP, conditional formatting, and multiple tabs—not just CSVs that need fixing.

Presentations: Create slide decks from rough notes or meeting transcripts.

Reports from messy inputs: Turn voice memos and scattered notes into polished documents.

Data and analysis

Statistical analysis: Outlier detection, cross-tabulation, and time-series analysis on your data files.

Data visualization: Generate charts using your data.

Data transformation: Clean, transform, and process datasets.

 

 

Permissions and security

Cowork runs in a virtual machine (VM) on your computer. This provides several security benefits:

Controlled environment: Claude operates within defined boundaries, with controlled file and network access.

Isolation: The VM environment is separate from your main operating system.

Important: While the VM provides isolation, Claude does have access to local files you grant it permission to access. Review Claude's planned actions before allowing it to proceed, especially when working with sensitive files.

Permissions

Permissions work the same as for chat. You control:

Which MCPs you connect to Claude and how often they ask for permission.

Claude’s internet access

Please carefully assess how much you trust an MCP or website before extending access beyond Claude’s default settings.

 

 

Current limitations

Cowork is a feature preview, which means some capabilities are not yet available:

No projects support: You cannot use Cowork within projects at this time.

No memory across sessions: Claude does not retain memory from previous Cowork sessions.

No chat or artifact sharing: Sessions cannot be shared with others.

No GSuite support: Cowork is not compatible with the GSuite connector. 

Desktop for macOS only: Cowork is only available in the Claude Desktop app for macOS and does not sync across devices.

Session persistence: The desktop app must remain open for your session to continue. Closing the app ends the session.

We're iterating on Cowork based on feedback. If you encounter issues or have suggestions, use the feedback button in the app to share feedback with our team.

 

 

Troubleshooting
Claude stopped working on my task

Ensure the Claude Desktop app was open throughout the entire task. If the app was closed or your computer went to sleep, the session may have ended.

 

I'm hitting usage limits quickly

Cowork consumes more usage than standard chat. Try using standard chat for simpler tasks and reserve Cowork for complex, multi-step work that benefits from file access.

 

Files aren't appearing where expected

Check that you've granted Claude the appropriate file access permissions. Review the output location Claude specified when completing the task.

Related Articles
Getting started with Claude
Installing Claude Desktop
What is the Max plan?
Using Cowork safely
Cowork for Team and Enterprise plans