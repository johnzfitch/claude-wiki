---
category: "15-Claude-AI-Features"
source_url: "https://support.claude.com/en/articles/12012173-getting-started-with-claude-in-chrome"
---


Claude in Chrome is available in beta for all paid plans (Pro, Max, Team, and Enterprise) on the Chrome web browser.

Claude in Chrome is a browser extension that allows Claude to read, click, and navigate websites alongside you. Claude works directly in the side panel while you browse, seeing what you see and taking actions when you ask.

Important: Browser use is a beta feature that allows Claude to interact directly with websites on your behalf, which carries inherent risks. Please review Using Claude in Chrome Safely before use.

 

What's New

After months of testing, Claude in Chrome is now available in beta to users on all paid plans (Pro, Max, Team, and Enterprise).

Note: To follow along with Claude in Chrome updates, refer to our extension-specific release notes.

Claude Code integration

Claude Code and the Chrome extension now work together for a build-test-verify workflow:

Build with Claude Code in your terminal.

Test and verify in the browser with the Chrome extension.

Debug issues using console logs—Claude can read errors, network requests, and DOM state directly.

This integration is especially useful for design verification (comparing Figma mocks to built output), live debugging, and automated testing.

 

Control browser actions from Claude Desktop

Start a task in Claude Desktop and let it handle work in the browser without switching windows. Follow these steps to enable the Claude in Chrome connector in your desktop app:

Click your initials in the lower left corner, then select “Settings.”

Navigate to “Connectors.”

Find Claude in Chrome in the list and click “Configure.”

Toggle the connector on, then download and install the extension if you haven’t already.

 

Completing these steps will add Claude in Chrome to the “Connectors” drop-down on your chats with Claude. This is disabled by default, so you’ll need to enable it manually for each conversation. Note that this connector only works with Haiku 4.5, Sonnet 4.5, or Opus 4.5; if you select another model in your chat window, the connector will be disabled.

 

Record a workflow

Teach Claude a workflow by recording the steps yourself, and Claude learns to repeat them. This is useful for repetitive browser tasks that follow the same pattern each time. To record a workflow:

Click the record icon in the extension panel.

Perform the steps you want Claude to learn.

Stop recording when finished.

Save the workflow as a shortcut for future use.

Console logs

Claude can now read browser console output, including errors, network requests, and DOM state. This helps developers identify and debug issues without leaving the browser.

 

Scheduled tasks

Set recurring browser tasks to run automatically on your schedule. Set it once and Claude handles it from there—daily, weekly, monthly, or annually.

You can schedule your Claude in Chrome shortcuts to run automatically by clicking the clock icon in the upper right corner of the extension panel.

 

Follow Claude’s plan

Use “Ask before acting” to have Claude create a plan for your approval, then let it execute the entire workflow independently within those approved boundaries. Aside from certain high-risk actions, Claude won't ask for permission until it's done or encounters something outside the plan. Learn more about this permission mode in our Claude in Chrome Permissions Guide.

 

Model selection

Pro plans: Claude in Chrome is currently limited to Haiku 4.5.

 

Max, Team, and Enterprise plans: Choose the model that best fits your task.

Opus 4.5: Maximum reasoning power for the most demanding workflows

Sonnet 4.5: Best for complex, multi-step tasks

Haiku 4.5: Optimized for speed and responsiveness

Switch between models anytime based on what you need.

 

 

Installing Claude in Chrome

Open a Google Chrome browser window.

Note: Claude in Chrome is not supported on other Chromium-based web browsers or mobile devices.

Visit the Chrome Web Store to find Claude in Chrome.

Click "Add to Chrome" to install the extension.

Sign in with your Claude account credentials when prompted.

Pin the extension by clicking the puzzle piece icon, then the thumbtack next to "Claude."

Grant the necessary permissions to enable Claude to interact with your browser.

The Claude icon will appear in your Chrome toolbar. Click it to open Claude in a side panel that stays visible while you browse.

 

 

Permissions required to install Claude in Chrome

You will need to grant Claude in Chrome the following permissions to install and use the extension:

Permission

 

Why Claude Needs This

sidePanel

 

This lets Claude appear as a panel on the side of your browser, so you can chat with Claude while browsing any website.

storage

 

This lets Claude save your preferences so they're still there when you close and reopen your browser.

scripting

 

This lets Claude read text on webpages so it can help you with tasks.

debugger

 

This is what allows Claude to actually control your browser – clicking buttons, typing text, and taking screenshots – when you ask it to complete tasks for you.

tabGroups

 

This lets Claude organize tabs it opens into a separate group with a different color, so you can easily tell which tabs Claude is using versus your personal browsing.

tabs

 

This lets Claude open, close, and switch between browser tabs when completing tasks for you.

alarms

 

This lets Claude run scheduled tasks at specific times you choose – like checking something on a website at a set time every day.

notifications

 

This lets Claude send you a notification on your computer when it finishes a task or needs you to take action.

system.display

 

This lets Claude know the size of your screen so it can accurately click in the right places when automating tasks.

webNavigation

 

 This lets Claude intervene if it detects that you are on a high-risk website.

declarativeNetRequestWithHostAccess

 

This lets the extension identify itself to Anthropic's servers, helping us understand how the browser extension is being used and troubleshoot any issues.

offscreen

 

This lets Claude play notification sounds in the background when your attention is needed.

nativeMessaging

 

 This will let the extension seamlessly integrate with other Anthropic products on your computer like Claude Desktop or Claude Code once we enable that capability.

downloads

 

This lets Claude download files from websites and open them when you ask it to save or work with files as part of an automated workflow.

unlimitedStorage

 

This lets Claude store more data locally (like complex instructions for a detailed workflow) beyond the normal limits that Chrome sets for extensions.

Refer to the Google Chrome Permissions documentation for more information.

 

Core Capabilities
Multi-tab functionality

Claude can manage multiple browser tabs simultaneously. Drag tabs into Claude's designated tab group to enable Claude to view and interact with all grouped tabs at once—eliminating the need to manually switch between tabs to compile information.

 

Enhanced site navigation

Claude has built-in knowledge of how to navigate popular platforms including Slack, Google Calendar, Gmail, Google Docs, and GitHub. Simple commands like "schedule a meeting" or "update the doc" work without detailed step-by-step instructions. We're continuously expanding Claude's site-specific capabilities.

 

Background workflows

Claude handles complex, multi-step workflows and keeps working even when you switch tabs (as long as Chrome is open). Enable notifications to receive alerts when Claude requires permission or completes a task, allowing you to focus on other work while Claude processes tasks in the background.

 

Visual context sharing

Share visual information directly with Claude by uploading images or capturing screenshots of specific screen regions. Point Claude to the exact button, field, or detail—much faster than describing complex layouts in words.

 

Image uploads

Give Claude an image and tell it where to upload, whether it's an expense report, form attachment, or picture upload.

 

Shortcuts

Save your best-working prompts as shortcuts (also called /slash commands) and reuse these proven workflows instantly:

After crafting a prompt that works well, save it as a shortcut.

Access your saved shortcuts by typing "/" in the chat.

Select your shortcut to instantly apply the same instructions.

Edit or delete shortcuts through the extension settings.

You can also schedule shortcuts to automate recurring tasks.

 

Contextual suggestions

Get prompt suggestions and helpful tips based on the website you're visiting, so you always have a starting point with Claude.

 

 

For Team and Enterprise users

If you're using Claude in Chrome on a Team or Enterprise plan, your admin may have configured settings that affect your experience:

Extension availability: Your admin controls whether the extension is enabled for your organization.

Site access: Your admin can restrict which websites Claude is allowed to access using allowlists and blocklists.

If you're unable to install or use the extension, contact your organization's admin. For admin documentation, see Claude in Chrome Admin Controls.

 

 

Next Steps

Claude in Chrome Permissions Guide: Learn how to control what Claude can access and do within the extension.

Using Claude in Chrome Safely: Understand risks and best practices.

Claude in Chrome Troubleshooting: Get help with common issues.

Claude in Chrome Admin Controls: For Team and Enterprise admins managing the extension for their organization.

Related Articles
Claude in Chrome Release Notes
Simplify your browsing experience with Claude in Chrome
Claude in Chrome Troubleshooting
Using Claude in Chrome Safely
Claude in Chrome Admin Controls