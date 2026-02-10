---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-08T20:51:47Z"
source_url: "https://support.claude.com/en/articles/12012173-getting-started-with-claude-in-chrome"
title: "Getting Started with Claude in Chrome | Claude Help Center"
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

[](#h_080b7c3c68)

[](#h_dfd70563b5)

[](#h_e0aabae2db)

[](#h_a7c5ffba87)

[](#h_221b991813)

[](#h_a065fbe86e)

[](#h_d6e2b494dc)

[All Collections](/en/)

[Claude in Chrome](https://support.claude.com/en/collections/18031491-claude-in-chrome)

Getting Started with Claude in Chrome

# Getting Started with Claude in Chrome

Updated yesterday

Table of contents

[](#h_080b7c3c68)

[](#h_dfd70563b5)

[](#h_e0aabae2db)

[](#h_a7c5ffba87)

[](#h_221b991813)

[](#h_a065fbe86e)

[](#h_d6e2b494dc)

Claude in Chrome is available in beta for all paid plans (Pro, Max, Team, and Enterprise) on the Chrome web browser.

Claude in Chrome is a browser extension that allows Claude to read, click, and navigate websites alongside you. Claude works directly in the side panel while you browse, seeing what you see and taking actions when you ask.

**Important:** Browser use is a beta feature that allows Claude to interact directly with websites on your behalf, which carries inherent risks. Please review [Using Claude in Chrome Safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely) before use.

## What's New

After months of testing, Claude in Chrome is now available in beta to users on all paid plans (Pro, Max, Team, and Enterprise).

**Note:** To follow along with Claude in Chrome updates, refer to our [extension-specific release notes](https://support.claude.com/en/articles/12306336-claude-for-chrome-release-notes).

### Claude Code integration

Claude Code and the Chrome extension now work together for a build-test-verify workflow:

- Build with Claude Code in your terminal.

- Test and verify in the browser with the Chrome extension.

- Debug issues using console logs—Claude can read errors, network requests, and DOM state directly.

This integration is especially useful for design verification (comparing Figma mocks to built output), live debugging, and automated testing.

### Control browser actions from Claude Desktop

Start a task in Claude Desktop and let it handle work in the browser without switching windows. Follow these steps to enable the Claude in Chrome connector in your desktop app:

1.  Click your initials in the lower left corner, then select “Settings.”

2.  Navigate to “Connectors.”

3.  Find **Claude in Chrome** in the list and click “Configure.”

4.  Toggle the connector on, then download and install the extension if you haven’t already.

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1892696502/a23969725f631e99b9e4c47ec6e9/89803b8f-4f3c-4983-8b4d-63aec687ea1a?expires=1770585300&signature=de46d221f07ae7e86dc852a4752955932313508f7c9371a799348e2129f8f681&req=dSguFM93m4RfW%2FMW1HO4zdOew4tZ4LZ6hnw73Y7ib%2Bd6GUqkglt3F5z6IkwO%0A5m%2BRyra8UCL1VhLuwmQ%3D%0A)

Completing these steps will add Claude in Chrome to the “Connectors” drop-down on your chats with Claude. This is disabled by default, so you’ll need to enable it manually for each conversation. Note that this connector only works with Haiku 4.5, Sonnet 4.5, or Opus 4.5; if you select another model in your chat window, the connector will be disabled.

### Record a workflow

Teach Claude a workflow by recording the steps yourself, and Claude learns to repeat them. This is useful for repetitive browser tasks that follow the same pattern each time. To record a workflow:

1.  Click the record icon in the extension panel.

2.  Perform the steps you want Claude to learn.

3.  Stop recording when finished.

4.  Save the workflow as a shortcut for future use.

### Console logs

Claude can now read browser console output, including errors, network requests, and DOM state. This helps developers identify and debug issues without leaving the browser.

### Scheduled tasks

Set recurring browser tasks to run automatically on your schedule. Set it once and Claude handles it from there—daily, weekly, monthly, or annually.

You can schedule your Claude in Chrome shortcuts to run automatically by clicking the clock icon in the upper right corner of the extension panel.

### Follow Claude’s plan

Use “Ask before acting” to have Claude create a plan for your approval, then let it execute the entire workflow independently within those approved boundaries. Aside from [certain high-risk actions](https://support.claude.com/en/articles/12902446-claude-for-chrome-permissions-guide#h_b7ded56289), Claude won't ask for permission until it's done or encounters something outside the plan. Learn more about this permission mode in our [Claude in Chrome Permissions Guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide).

## Model selection

**Pro plans:** Claude in Chrome is currently limited to Haiku 4.5.

**Max, Team, and Enterprise plans:** Choose the model that best fits your task.

- **Opus 4.5**: Maximum reasoning power for the most demanding workflows

- **Sonnet 4.5**: Best for complex, multi-step tasks

- **Haiku 4.5**: Optimized for speed and responsiveness

Switch between models anytime based on what you need.

------------------------------------------------------------------------

## Installing Claude in Chrome

1.  Open a Google Chrome browser window.

    1.  **Note:** Claude in Chrome is not supported on other Chromium-based web browsers or mobile devices.

2.  Visit the [Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) to find Claude in Chrome.

3.  Click "Add to Chrome" to install the extension.

4.  Sign in with your Claude account credentials when prompted.

5.  Pin the extension by clicking the puzzle piece icon, then the thumbtack next to "Claude."

6.  Grant the necessary permissions to enable Claude to interact with your browser.

The Claude icon will appear in your Chrome toolbar. Click it to open Claude in a side panel that stays visible while you browse.

------------------------------------------------------------------------

## Permissions required to install Claude in Chrome

You will need to grant Claude in Chrome the following permissions to install and use the extension:

[TABLE]

Refer to the [Google Chrome Permissions documentation](https://developer.chrome.com/docs/extensions/reference/permissions-list) for more information.

## Core Capabilities

### Multi-tab functionality

Claude can manage multiple browser tabs simultaneously. Drag tabs into Claude's designated tab group to enable Claude to view and interact with all grouped tabs at once—eliminating the need to manually switch between tabs to compile information.

### Enhanced site navigation

Claude has built-in knowledge of how to navigate popular platforms including Slack, Google Calendar, Gmail, Google Docs, and GitHub. Simple commands like "schedule a meeting" or "update the doc" work without detailed step-by-step instructions. We're continuously expanding Claude's site-specific capabilities.

### Background workflows

Claude handles complex, multi-step workflows and keeps working even when you switch tabs (as long as Chrome is open). Enable notifications to receive alerts when Claude requires permission or completes a task, allowing you to focus on other work while Claude processes tasks in the background.

### Visual context sharing

Share visual information directly with Claude by uploading images or capturing screenshots of specific screen regions. Point Claude to the exact button, field, or detail—much faster than describing complex layouts in words.

### Image uploads

Give Claude an image and tell it where to upload, whether it's an expense report, form attachment, or picture upload.

### Shortcuts

Save your best-working prompts as shortcuts (also called /slash commands) and reuse these proven workflows instantly:

1.  After crafting a prompt that works well, save it as a shortcut.

2.  Access your saved shortcuts by typing "/" in the chat.

3.  Select your shortcut to instantly apply the same instructions.

4.  Edit or delete shortcuts through the extension settings.

You can also schedule shortcuts to automate recurring tasks.

### Contextual suggestions

Get prompt suggestions and helpful tips based on the website you're visiting, so you always have a starting point with Claude.

------------------------------------------------------------------------

## For Team and Enterprise users

If you're using Claude in Chrome on a Team or Enterprise plan, your admin may have configured settings that affect your experience:

- **Extension availability:** Your admin controls whether the extension is enabled for your organization.

- **Site access:** Your admin can restrict which websites Claude is allowed to access using allowlists and blocklists.

If you're unable to install or use the extension, contact your organization's admin. For admin documentation, see [Claude in Chrome Admin Controls](https://support.claude.com/en/articles/13065128-claude-for-chrome-admin-controls).

------------------------------------------------------------------------

## Next Steps

- [Claude in Chrome Permissions Guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide): Learn how to control what Claude can access and do within the extension.

- [Using Claude in Chrome Safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely): Understand risks and best practices.

- [Claude in Chrome Troubleshooting](https://support.claude.com/en/articles/12902405-claude-in-chrome-troubleshooting): Get help with common issues.

- [Claude in Chrome Admin Controls](https://support.claude.com/en/articles/13065128-claude-for-chrome-admin-controls): For Team and Enterprise admins managing the extension for their organization.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/12306336-claude-in-chrome-release-notes)

Claude in Chrome Release Notes

[](https://support.claude.com/en/articles/12431227-simplify-your-browsing-experience-with-claude-in-chrome)

Simplify your browsing experience with Claude in Chrome

[](https://support.claude.com/en/articles/12902405-claude-in-chrome-troubleshooting)

Claude in Chrome Troubleshooting

[](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)

Using Claude in Chrome Safely

[](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls)

Claude in Chrome Admin Controls

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
