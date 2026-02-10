---
category: "14-Connectors"
source_url: "https://support.claude.com/en/articles/11506255-getting-started-with-claude-in-slack"
---


You can now integrate Claude and Slack, giving you two ways to use them together: add Claude directly to your Slack workspace, or enable the Slack connector for your Claude apps.

 

What is Claude in Slack?

The Claude app is available to users on paid Slack plans. Slack admins must approve the Claude app before individual users can access it.

It’s how we’ve brought Claude’s capabilities directly to Slack, bringing AI assistance into your team’s workspace. This integration allows you to work with Claude without leaving Slack through three convenient surfaces:

 

Direct message with Claude: Start a private conversation with @Claude.

 

 

AI assistant panel: Click the Claude icon in Slack's AI assistant header to open a panel on the right side of your Slack window, allowing you to access Claude from anywhere in the Slack app.

 

 

 

Thread participation: Mention @Claude in any thread to get Claude's help with the conversation.

 

 

All surfaces provide the same capabilities that you have enabled in Claude, including web search and connections to your integrated tools, allowing you to seamlessly integrate AI assistance into your existing workflow.

Note: Team and Enterprise plan users with access to Claude Code on the web can also route coding tasks directly to Claude Code by mentioning @Claude. See Using Claude in Slack for details on this beta feature.

 

Enabling and installing Claude in Slack
For Slack admins

Go to the Claude app in the Slack App Marketplace.

Click "Add to Slack" on the Claude app page.

Review and approve the app for your organization.

Choose whether to deploy org-wide or to specific workspaces.

To install across all workspaces:

Navigate to your Slack management workspace at: https://app.slack.com/manage/<INSERT_SLACK_ID>/workspaces/all

Find your enterprise's Slack ID using the appropriate lookup method

Navigate to Integrations → Installed apps → Add to more workspaces.

Toggle through all relevant workspaces where you'd like to enable Claude.

For individual users

Once your Slack admin has approved Claude (or if you're on a personal Slack plan):

Find Claude in your apps list (search for "Claude" if it's not immediately visible), or go to the Slack App Marketplace.

Click "Connect Account” to be prompted to connect your Claude account:

In the window that opens, select which organization you would like to connect with Claude for Slack.

Click “Authorize” to allow Claude in Slack to access your Claude chat account:

 

 

You should see a confirmation message upon successful connection:

After successful authentication, return to Slack.

Click “+ New Chat” to start a conversation with Claude, or @mention Claude in any Slack conversation to access its capabilities.

Tip: Add Claude to your Slack header for quick access by clicking the three dots "..." at the top right and selecting "Add this app to header."

Enabling Claude Code in Slack (beta)

Team and Enterprise plan users can route coding tasks from Slack to Claude Code on the web. To enable this capability:

A Claude Owner or Primary Owner must enable Claude Code on the web by navigating to Admin settings > Claude Code.

Individual users must have access to Claude Code on the web.

Once enabled, mentioning @Claude for coding tasks will automatically create a Claude Code session. Learn more about using Claude Code in Slack.

 

What is the Slack connector?

The Slack connector is available for Team and Enterprise plans.

Enabling the Slack connector allows Claude to search within your Slack workspace’s channels, direct messages, and shared files to pull relevant context into your conversations. Note that members of Team and Enterprise plan organizations will not see the option to enable the Slack connector individually until it’s enabled by an Owner.

Important: You must install Claude in Slack before enabling and using the Slack connector.

 

Enabling the Slack connector
Team and Enterprise Owners

Log in to your Owner account and click your initials in the lower left corner.

Navigate to Admin settings > Connectors.

Under “Connectors,” click the "Enable" button next to the Slack connector.

Users can then authenticate in their individual connector settings to begin using Slack in Claude.

Individual Team/Enterprise users

Log in to your Claude account and click your initials in the lower left corner.

Navigate to Settings > Connectors.

Find the Slack connector and click “Connect.”

Click "Connect" to authenticate with the connector and start using Slack in Claude.

 

Managing your Claude in Slack connections
Viewing Claude app connection status

Click on the Claude app in your Slack sidebar.

Go to the "Home" tab.

You'll see your connection status, including your connected account email and organization name.

Disconnecting the Claude app

To disconnect your Claude account from Slack:

Go to the Claude Home tab in Slack.

Under Disconnect Claude Account, click the red "Disconnect" button.

Confirm the disconnection.

 

Disconnecting will:

Remove the connection between your Claude account and Slack workspace.

Delete all past Claude conversations in Slack from Claude (within 30 days).

Preserve conversations in Slack, but Claude won't have awareness of them if you reconnect

Disconnecting the Slack connector

You can also disconnect the Slack connector from your Claude settings (or you can enable/disable the connector for an individual chat):

Go to claude.ai/settings/connectors

Find Slack in your list of Connectors.

Click the menu (...) and select "Disconnect."

 

Privacy and data
Data storage

Your Slack conversations with Claude remain separate from your Claude history, keeping work organized across platforms.

 

Data visibility

Conversations initiated in Slack are not visible in your Claude chat history.

Conversations initiated in the Claude web app are not accessible in Slack.

Each platform maintains separate conversation histories.

Data deletion

Conversations are automatically deleted from Claude within 30 days if you disconnect the integration or uninstall the app.

Your conversations in Slack follow your organization's Slack retention policies.

 

FAQ
I’m trying to add Claude in Slack but it’s not working – help!

If you are using a company Slack instance and are not assigned to an Admin role, a Slack Admin must approve the Claude app on behalf of your organization before you’re able to download it. If you try to skip this step and install Claude in Slack, you’ll see a Request to install prompt where you can send a message to your Slack Admin. Work with them to approve the app and make it available for your team.

Related Articles
Using the Connectors Directory to extend Claude’s capabilities
Getting Started with Claude in Chrome
Using Claude in Slack
Getting Started with Claude for Life Sciences
Using Interactive Connectors in Claude