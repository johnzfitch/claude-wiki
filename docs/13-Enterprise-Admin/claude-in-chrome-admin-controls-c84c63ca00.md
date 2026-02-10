---
category: "13-Enterprise-Admin"
source_url: "https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls"
---


Claude in Chrome admin controls are available in beta for Team and Enterprise plans.

This article explains how Team and Enterprise Owners can manage Claude in Chrome for their organization.

 

Claude in Chrome is a browser extension that allows Claude to read, click, and navigate websites on behalf of your users. As an Owner, you control whether the extension is available for users to install and which sites they can access.

Important: Before enabling Claude in Chrome for your organization, review Using Claude in Chrome Safely to understand the risks of browser-based AI, including prompt injection attacks.

Accessing Claude in Chrome settings

To manage Claude in Chrome settings for your organization:

Sign in to Claude with your Owner account.

Navigate to Admin settings > Claude in Chrome.

 

Enabling or disabling the extension

Use the toggle to enable or disable Claude in Chrome for your entire organization.

Team plans: The extension is enabled by default. Disable it if you prefer users not to have access.

Enterprise plans: The extension is disabled by default. Enable it when you're ready for users to access the feature.

Note: When you enable the extension for an Enterprise organization, users are not automatically notified. You may want to communicate availability through your internal channels.

 

Configuring site access

Use allowlists and blocklists to control which websites Claude can access when users are working with the extension.

 

Allowlist: Specify which sites Claude is permitted to access by adding them to the allowlist. We recommend starting with a restrictive allowlist, especially during initial rollout.

 

Blocklist: Specify sites Claude should never access, regardless of other settings, by adding them to the blocklist. This adds an extra layer of protection beyond Claude's default blocked categories.

 

Recommendation: Start with a more restrictive allowlist for the security of your organization's data, then expand access over time as you become comfortable with the extension's behavior.

 

Managing user access on Claude Desktop

Users with both Claude in Chrome and Claude Desktop installed will now have the option to start a task on the desktop app and let it handle work in the browser without switching windows.

If you want to disable this for members of your organization, you can toggle the extension off entirely, or edit your Enterprise configuration.

Disable the Chrome extension in admin settings:

Click your initials in the lower left corner, then select “Admin settings.”

Navigate to “Connectors.”

Find Claude in Chrome in the list and click “Configure.”

Toggle the connector off.

Alternatively, disable isLocalDevMcpEnabled in your Enterprise configuration.

 

Deployment options

Once enabled, users can access Claude in Chrome in two ways:

Self-service: Users install the extension themselves from the Chrome Web Store.

Managed deployment: Use your existing Chrome management tools (Google Workspace admin console or MDM) to deploy the extension to specific users or groups.

Most Enterprise organizations already have Chrome extension management in place. You can use these existing controls to limit which employees can install the extension during a pilot phase.

 

Running a pilot

To test Claude in Chrome with a subset of users before broader rollout:

Enable the extension at the organization level.

Configure a restrictive allowlist limiting Claude to specific, trusted sites.

Use your IT controls to limit which employees can install the extension.

Share Using Claude in Chrome Safely with pilot users.

Gather feedback and expand access over time.

 

Educating your users

We recommend sharing these resources with users before they start using Claude in Chrome:

Getting Started with Claude in Chrome: Installation and core capabilities

Using Claude in Chrome Safely: Risks and best practices

Claude in Chrome Permissions Guide: How users control what Claude can access

Related Articles
Getting Started with Local MCP Servers on Claude Desktop
Getting Started with Claude in Chrome
Claude in Chrome Release Notes
Using Claude in Chrome Safely
Claude in Chrome Permissions Guide