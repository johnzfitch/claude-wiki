---
category: "15-Claude-AI-Features"
fetched_at: "2026-03-15T12:16:50Z"
source_url: "https://support.claude.com/en/articles/13892150-work-across-apps-with-cowork"
title: "Work across Excel and PowerPoint | Claude Help Center"
---

# Work across Excel and PowerPoint

Updated yesterday


Claude can now work across apps to coordinate between the Excel and PowerPoint add-ins. Instead of switching between apps and providing context each time, Claude can read from one app and make changes in another. For example, you can ask Claude to analyze data in an Excel workbook, then create a presentation in PowerPoint using those results, without copying and pasting between apps.

## Requirements

- A paid Claude plan (Pro, Max, Team, or Enterprise)

- The Claude for Excel add-in installed from the Microsoft Marketplace

- The Claude for PowerPoint add-in installed from the Microsoft Marketplace

------------------------------------------------------------------------

## Let Claude work across apps

### 1. Install the add-ins

Get **[Claude for Excel](https://marketplace.microsoft.com/en-us/product/saas/wa200009404?tab=overview)** and **[Claude for PowerPoint](https://marketplace.microsoft.com/en-us/product/office/WA200010001?tab=Overview)** from the Microsoft Marketplace. Open each app and activate the add-in at least once before using the cross-app features.

### 2. Toggle the setting on

Go to **Settings** in each of Claude for Excel and Powerpoint and toggle **Let Claude work across files** on:


**Note:** This setting is default on for Pro and Max plans and default off for Team and Enterprise plans.

You will see connected file indicators when Excel or PowerPoint files are linked to your session:


## 

------------------------------------------------------------------------

## How it works

When you describe a task that involves multiple files or apps, Claude coordinates behind the scenes:

- Claude uses the Excel and PowerPoint add-ins to read from and write to open files.

- Context transfers between apps automatically, so you don't need to copy and paste information manually.

You stay in one place while Claude does the switching.

## What you can do

### Read and write across open files

Claude can read data from an open Excel workbook or PowerPoint presentation, and make changes to them directly. For example:

- Pull numbers from an Excel model into a PowerPoint slide

- Update a chart in PowerPoint with the latest figures from Excel

- Read content from a presentation and use it to populate a spreadsheet

### Pass context between apps

When Claude moves multiple files across Excel and Powerpoint, it carries relevant context forward. If you've been building a financial model in Excel and ask Claude to create a summary deck, Claude already understands the model's structure and key outputs, so you don't need to re-explain.

------------------------------------------------------------------------

## Skills work across apps too

Skills you've enabled in your Claude settings apply when Claude is working in Excel or PowerPoint during a cross-app task. If you have a Skill that enforces your team's modeling conventions in Excel and another that matches your slide template in PowerPoint, Claude uses each one in the right app as it moves through the workflow.

For more on how Skills work, see **[Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).**

------------------------------------------------------------------------

## Data handling

Inputs and outputs are automatically deleted from Anthropic's backend within 30 days of receipt or generation, except in cases outlined in **[How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** The Claude for Excel and Claude for PowerPoint add-ins do not inherit custom data retention settings your organization may have set, and activity is not currently included in Enterprise audit logs, the Compliance API, or data exports. Chat history is not saved between sessions.

### For admins who want to restrict access

Team and Enterprise organization owners can control whether team members have access to the Claude for Excel and Claude for PowerPoint add-ins through the **[Microsoft 365 Admin Center](https://admin.microsoft.com)**.

------------------------------------------------------------------------

## Current limitations

- Claude can only read from and write to files that are currently open in Excel or PowerPoint.

- Claude cannot create, open, close, or switch files directly from the add-ins—the files and add-ins must be open with the feature turned on.

- Chat history for cross-app sessions is not saved between sessions.

------------------------------------------------------------------------

## Troubleshooting

### Claude doesn't see my open file

Make sure the add-in is activated in the app (**Tools \> Add-ins** on Mac or **Home \> Add-ins** on Windows) and that working across apps is turned on in Claude Desktop settings.

### Changes aren't appearing in the other app

Claude works on open files in sequence. Wait for Claude to finish its current action, then check the target file. You may need to ask Claude to refresh or re-read the file.

------------------------------------------------------------------------

Related Articles


Release notes


Use Skills in Claude


Use Claude for Excel


Use Claude for PowerPoint


Use Claude for Excel and PowerPoint with an LLM gateway
