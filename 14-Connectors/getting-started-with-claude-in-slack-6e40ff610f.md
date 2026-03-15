---
category: "14-Connectors"
fetched_at: "2026-03-15T12:17:01Z"
source_url: "https://support.claude.com/en/articles/11506255-getting-started-with-claude-in-slack"
title: "Getting started with Claude in Slack | Claude Help Center"
---

# Getting started with Claude in Slack

Updated yesterday


You can now integrate Claude and Slack, giving you two ways to use them together: add Claude directly to your Slack workspace, or enable the Slack connector for your Claude apps.

## What is Claude in Slack?

The Claude app is available to users on paid Slack plans. Slack admins must approve the Claude app before individual users can access it.

It’s how we’ve brought Claude’s capabilities directly to Slack, bringing AI assistance into your team’s workspace. This integration allows you to work with Claude without leaving Slack through three convenient surfaces:

**Direct message with Claude**: Start a private conversation with @Claude.


**AI assistant panel**: Click the Claude icon in Slack's AI assistant header to open a panel on the right side of your Slack window, allowing you to access Claude from anywhere in the Slack app.


**Thread participation**: Mention @Claude in any thread to get Claude's help with the conversation.


All surfaces provide the same capabilities that you have enabled in Claude, including web search and connections to your integrated tools, allowing you to seamlessly integrate AI assistance into your existing workflow.

**Note:** Team and Enterprise plan users with access to Claude Code on the web can also route coding tasks directly to Claude Code by mentioning @Claude. See [Using Claude in Slack](https://support.claude.com/en/articles/12461605-using-claude-in-slack#h_adda66b697) for details on this beta feature.

------------------------------------------------------------------------

## Enabling and installing Claude in Slack

### For Slack admins

1.  Go to the [Claude app in the Slack App Marketplace](https://slack.com/marketplace/A08SF47R6P4).

2.  Click "Add to Slack" on the Claude app page.

3.  Review and approve the app for your organization.

4.  Choose whether to deploy org-wide or to specific workspaces.

**To install across all workspaces:**

1.  Navigate to your Slack management workspace at: [https://app.slack.com/manage/\<INSERT_SLACK_ID\>/workspaces/all](https://app.slack.com/manage/%3CINSERT_SLACK_ID%3E/workspaces/all)

    - Find your enterprise's Slack ID using the appropriate lookup method

2.  Navigate to **Integrations → Installed apps → Add to more workspaces**.

3.  Toggle through all relevant workspaces where you'd like to enable Claude.

### For individual users

Once your Slack admin has approved Claude (or if you're on a personal Slack plan):

1.  Find Claude in your apps list (search for "Claude" if it's not immediately visible), or go to the Slack App Marketplace.

2.  Click "Connect Account” to be prompted to connect your Claude account:


3.  In the window that opens, select which organization you would like to connect with Claude for Slack.

4.  Click “Authorize” to allow Claude in Slack to access your Claude chat account:


5.  You should see a confirmation message upon successful connection:


6.  After successful authentication, return to Slack.

7.  Click “+ New Chat” to start a conversation with Claude, or @mention Claude in any Slack conversation to access its capabilities.

**Tip**: Add Claude to your Slack header for quick access by clicking the three dots "..." at the top right and selecting "Add this app to header."

**Enabling Claude Code in Slack (beta)**

Team and Enterprise plan users can route coding tasks from Slack to Claude Code on the web. To enable this capability:

1.  A Claude Owner or Primary Owner must enable Claude Code on the web by navigating to **[Organization settings \> Claude Code](http://claude.ai/admin-settings/claude-code)**.

2.  Individual users must have access to Claude Code on the web.

Once enabled, mentioning @Claude for coding tasks will automatically create a Claude Code session. Learn more about **[using Claude Code in Slack](https://support.claude.com/en/articles/12461605-using-claude-in-slack#h_adda66b697)**.

------------------------------------------------------------------------

## What is the Slack connector?

The Slack connector is available for all paid plans (Pro, Max, Team, and Enterprise).

Enabling the Slack connector allows Claude to search within your Slack workspace’s channels, direct messages, and shared files to pull relevant context into your conversations. Note that members of Team and Enterprise plan organizations will not see the option to enable the Slack connector individually until it’s enabled by an Owner.

**Important:** You must install Claude in Slack before enabling and using the Slack connector.

## Enabling the Slack connector

### Team and Enterprise owners

1.  Log in to your Owner or Primary Owner account and click your initials in the lower left corner.

2.  Navigate to **[Organization settings \> Connectors](https://claude.ai/admin-settings/connectors)**.

3.  Under “Connectors,” click the "Enable" button next to the Slack connector.

4.  Users can then authenticate in their individual connector settings to begin using Slack in Claude.

### Individual Pro, Max, Team, and Enterprise users

1.  Log in to your Claude account and click your initials in the lower left corner.

2.  Navigate to **[Settings \> Connectors](http://claude.ai/settings/connectors)**.

3.  Find the Slack connector and click “Connect.”

4.  Click "Connect" to authenticate with the connector and start using Slack in Claude.

------------------------------------------------------------------------

## Managing your Claude in Slack connections

### Viewing Claude app connection status

1.  Click on the Claude app in your Slack sidebar.

2.  Go to the "Home" tab.

3.  You'll see your connection status, including your connected account email and organization name.

### Disconnecting the Claude app

To disconnect your Claude account from Slack:

1.  Go to the Claude Home tab in Slack.

2.  Under **Disconnect Claude Account**, click the red "Disconnect" button.

3.  Confirm the disconnection.


Disconnecting will:

- Remove the connection between your Claude account and Slack workspace.

- Delete all past Claude conversations in Slack from Claude (within 30 days).

- Preserve conversations in Slack, but Claude won't have awareness of them if you reconnect

### Disconnecting the Slack connector

You can also disconnect the Slack connector from your Claude settings (or you can enable/disable the connector for an individual chat):

1.  Go to [](https://claude.ai/settings/integrations) claude.ai/settings/connectors

2.  Find **Slack** in your list of Connectors.

3.  Click the menu (...) and select "Disconnect."

------------------------------------------------------------------------

## Privacy and data

### Data storage

Your Slack conversations with Claude remain separate from your Claude history, keeping work organized across platforms.

### Data visibility

- Conversations initiated in Slack are not visible in [your Claude chat history](http://claude.ai/recents).

- Conversations initiated in the Claude web app are not accessible in Slack.

- Each platform maintains separate conversation histories.

### Data deletion

- Conversations are automatically deleted from Claude within 30 days if you disconnect the integration or uninstall the app.

- Your conversations in Slack follow your organization's Slack retention policies.

------------------------------------------------------------------------

## Frequently asked questions

### I’m trying to add Claude in Slack but it’s not working – help!

If you are using a company Slack instance and are not assigned to an Admin role, a Slack Admin must approve the Claude app on behalf of your organization before you’re able to download it. If you try to skip this step and install Claude in Slack, you’ll see a **Request to install** prompt where you can send a message to your Slack Admin. Work with them to approve the app and make it available for your team.

------------------------------------------------------------------------

Related Articles


Use connectors to extend Claude's capabilities


Get started with Claude in Chrome


Using Claude in Slack


Getting Started with Claude for Life Sciences


Using interactive connectors in Claude
