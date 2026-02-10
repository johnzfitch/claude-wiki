---
category: "14-Connectors"
source_url: "https://support.claude.com/en/articles/11724452-using-the-connectors-directory-to-extend-claude-s-capabilities"
---


This guide explains how to browse the Connectors Directory to link Claude to tools and enhance its capabilities.

Web connectors are available on Claude, Claude Desktop, and Claude Mobile (iOS and Android) for users with paid plans (Pro, Max, Team, or Enterprise). Web connectors are also available to some users on free Claude plans. Desktop extensions are available to all users (free included) on Claude Desktop.

What is the Connectors Directory?

The Claude Connectors Directory is a curated collection of recommended tools that you enable to extend Claude's capabilities. It showcases both local and remote connectors and applies to the Claude web app, Claude Desktop, Claude Code, and API (via the MCP Connector). Each connector has a webpage detailing its use cases, read/write capabilities, and availability. These tools allow Claude to connect to your favorite apps and services, access your data, and take actions on your behalf.

 

Browsing available connectors

Users can browse connectors via the directory on Claude and Claude Desktop. It's not possible to browse the connectors directory on Claude for iOS or Android at this time.

You can browse the connectors directory from two different areas:

 

From a chat

Click the “Search and tools” button on the lower left of your chat interface.

From the menu, select “Add connectors.”

Browse the available connectors by category or scroll through the complete list.

From Settings

Navigate to Settings > Connectors.

Look for the Connectors section and click "Browse connectors."

Browse the available connectors by category or scroll through the complete list.

The directory includes connectors for:

Productivity tools: Asana, Notion, Linear, Atlassian

Communication: Intercom

Developer tools: Sentry, Cloudflare

Business tools: Stripe, PayPal, Square, Plaid

Automation: Zapier

Desktop extensions: Filesystem access, iMessage, and other desktop extensions

 

Connecting Claude to a tool

Users can connect Claude to a new tool on Claude and Claude Desktop. It's not possible to add new connectors (custom or from the directory) on Claude for iOS or Android at this time.

To connect Claude to a tool from the directory:

Click on the connector you want to add.

Review the connector's description and capabilities.

Click "Connect" or “Install” to begin the setup process.

Follow the authentication prompts to grant Claude access to your account.

Configure any specific settings or permissions as needed.

Important: When connecting to a tool, you're granting Claude permission to access and potentially modify data within that service based on your account permissions. Only connect to tools you trust and need for your workflows.

 

Using connected tools

Once you connect to a tool on Claude or Claude Desktop, it will be available to use the next time you log in to your account on Claude for iOS or Android.

Once connected, tools become available in your conversations:

Look for the "Search and tools" menu in the chat interface.

Enable the specific tools you want Claude to use for that conversation.

Claude will now be able to invoke these tools when relevant to your requests.

For example, after connecting to Linear, you can ask Claude to "Create a new issue for the login bug" and Claude will use the Linear tool to create the issue in your workspace.

 

Some connectors are interactive and can render live interfaces — like dashboards, task boards, and design tools — directly within your conversation. Look for the "Interactive" badge in the Connectors Directory to find connectors with this capability.

 

Managing your connected tools

To manage your connected tools:

Navigate to Settings > Connectors.

View all your connected tools in the Connectors section.

For each tool, you can:

Disconnect the tool entirely.

Modify connection settings.

Review permissions and access levels.

 

Security considerations

When connecting to tools from the directory:

Review permissions carefully: During the connection process, review what access the tool is requesting.

Use trusted tools: The directory contains recommended tools that meet our quality standards.

Monitor tool usage: Pay attention to what actions Claude is taking with your tools.

Revoke access when needed: Disconnect tools you no longer need or use.

 

Troubleshooting connection issues

If you're having trouble connecting to a tool:

Check your internet connection: Ensure you have a stable connection.

Verify your account access: Make sure you have an active account with the service.

Review permissions: Some tools require specific permissions or account types.

Try reconnecting: If authentication fails, try disconnecting and reconnecting.

 

Custom connectors

In addition to directory connectors, you can also add custom connectors:

In Settings > Connectors, find the Connectors section and click "Add custom connector."

Enter the connector's name and URL.

Follow the same connection process as directory connectors.

Important: Custom connectors allow you to connect Claude to services that have not been verified by Anthropic. Only connect to servers from trusted organizations and review authentication permissions carefully.

Related Articles
Pre-built Web Connectors Using Remote MCP
Anthropic Connectors Directory FAQ
When to Use Desktop and Web Connectors
Connect your tools to unlock a smarter, more capable AI companion
Using Interactive Connectors in Claude