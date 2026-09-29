---
title: "Work across M365 apps - Claude.ai Documentation"
source_url: "https://support.claude.com/en/articles/13892150-work-across-microsoft-365-apps"
category: "15-Claude-AI-Features"
fetched_at: "2026-09-14T06:27:27Z"
---

## On this page

- [Requirements](#requirements)
- [Enable cross-app mode](#enable-cross-app-mode)
- [How it works](#how-it-works)
- [What you can do](#what-you-can-do)
  - [Read and write across open apps](#read-and-write-across-open-apps)
  - [Pass context between apps](#pass-context-between-apps)
- [Skills work across apps](#skills-work-across-apps)
- [Manage access as an admin](#manage-access-as-an-admin)
- [Data handling](#data-handling)
- [Current limitations](#current-limitations)
- [Troubleshooting](#troubleshooting)
  - [Claude doesn’t see my open file](#claude-doesn%E2%80%99t-see-my-open-file)
  - [Changes aren’t appearing in the other app](#changes-aren%E2%80%99t-appearing-in-the-other-app)

Features

# Work across M365 apps

Copy pageCopy page

Let Claude read from one Microsoft 365 app and make changes in another in a single conversation.

Copy pageCopy page

Claude can coordinate between the Excel, PowerPoint, Word, and Outlook add-ins in your Microsoft 365 suite. Instead of switching between apps and re-providing context each time, Claude can read from one app and make changes in another.

Working across apps is available when you sign in with your Claude account directly. It is not supported when connecting through Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an LLM gateway.


[​](#requirements)

Requirements

Install each Claude for M365 add-in and confirm your plan before turning on cross-app mode.

- A paid Claude plan: Pro, Max, Team, or Enterprise.
- [Claude for Excel](/docs/office-agents/excel) installed from the Microsoft AppSource.
- [Claude for PowerPoint](/docs/office-agents/powerpoint) installed from the Microsoft AppSource.
- [Claude for Word](/docs/office-agents/word) installed from the Microsoft AppSource.
- [Claude for Outlook](/docs/office-agents/outlook) installed from the Microsoft AppSource.


[​](#enable-cross-app-mode)

Enable cross-app mode

1

Install each add-in

Install Claude for Excel, PowerPoint, Word, and Outlook from the Microsoft AppSource. Open each app and activate the add-in at least once before using cross-app features.

2

Enable per add-in

Open Settings in each add-in and turn on “Let Claude work across files”. Pro and Max plans have this on by default; Team and Enterprise plans default to off. The toggle is per-device, so enable it in every host you want to coordinate from.

Once enabled, connected-app indicators appear in the sidebar when other Excel, PowerPoint, Word, or Outlook sessions are linked.


[​](#how-it-works)

How it works

When you describe a task that involves multiple files or apps, Claude coordinates automatically:

- Claude uses the Excel, PowerPoint, Word, and Outlook add-ins to read from and write to open files and email threads.
- Context transfers between apps automatically, so you don’t need to copy and paste information manually.

You stay in one place while Claude does the switching.


[​](#what-you-can-do)

What you can do


[​](#read-and-write-across-open-apps)

Read and write across open apps

Claude can read data from an open Excel workbook, PowerPoint presentation, Word document, or Outlook email thread, and make changes to them directly. For example:

- Pull numbers from an Excel model into a PowerPoint slide or a Word memo.
- Update a chart in PowerPoint with the latest figures from Excel.
- Read content from a presentation and use it to populate a spreadsheet.
- Summarize a Word document into PowerPoint slides.
- Draft a Word memo using data from an Excel workbook.
- Open an attached letter of intent in Word with the Outlook thread already loaded as context.
- Pull figures from an email thread into an open Excel model.


[​](#pass-context-between-apps)

Pass context between apps

Claude carries relevant context forward when working across multiple files. If you’ve been building a financial model in Excel and ask Claude to create a summary deck or draft an investment memo, Claude already understands the model’s structure and key outputs, so you don’t need to re-explain.


[​](#skills-work-across-apps)

Skills work across apps

Skills you’ve enabled in your Claude settings apply when Claude is working in Excel, PowerPoint, Word, or Outlook during a cross-app task. If you have a Skill that enforces your team’s modeling conventions in Excel and another that matches your slide template in PowerPoint, Claude uses each one in the right app as it moves through the workflow. For more on Skills, see [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).


[​](#manage-access-as-an-admin)

Manage access as an admin

Team and Enterprise organization owners can control whether team members can access this capability.

1

Open organization settings

Go to Organization settings, Office agents.

2

Toggle the setting

Turn “Let Claude work across apps” on or off.

Admins can also manage member access to the Claude for Excel, PowerPoint, Word, and Outlook add-ins through the Microsoft 365 Admin Center.


[​](#data-handling)

Data handling

Inputs and outputs are deleted from Anthropic’s backend within 30 days of receipt or generation, except in cases outlined in [How long do you store my organization’s data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data). The Claude for M365 add-ins do not inherit custom data retention settings your organization may have set, and activity is not included in Enterprise audit logs or data exports. For Enterprise organizations with the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) enabled, add-in sessions are included in the Compliance API. This coverage is in public beta and requires no additional setup: the same Compliance Access Keys apply. Chat history is stored locally in your browser, not on Anthropic’s servers, and can be cleared from Settings at any time.


[​](#current-limitations)

Current limitations

- Claude can only read from and write to files that are currently open in Excel, PowerPoint, or Word, and the email or event currently open in Outlook.
- Claude cannot create, open, close, or switch files directly. The files and add-ins must be open with the feature turned on.


[​](#troubleshooting)

Troubleshooting


[​](#claude-doesn’t-see-my-open-file)

Claude doesn’t see my open file

Make sure the add-in is activated in the app (Tools, Add-ins on Mac or Home, Add-ins on Windows) and that working across apps is turned on in the add-in settings.


[​](#changes-aren’t-appearing-in-the-other-app)

Changes aren’t appearing in the other app

Claude works on open files in sequence. Wait for Claude to finish its current action, then check the target file. You may need to ask Claude to refresh or re-read the file.
