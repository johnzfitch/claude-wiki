---
category: "15-Claude-AI-Features"
source_url: "https://support.claude.com/en/articles/10593882-sharing-and-unsharing-chats"
---


Learn how to create shareable links to your chats with Claude. While chats are always private by default, you can easily create snapshots of your conversations to share via direct link. This guide walks you through the process of sharing and unsharing chats.

 

Sharing Chats

To share a chat:

Click the "Share" button in the upper right corner of your chat.

Click the "Share" button in the pop out to create a shareable link.

Once a chat has been shared, anyone with the link can view the chat snapshot. The chat snapshot includes all messages that were sent prior to sharing the chat, including any artifacts. All messages sent after sharing a chat will remain private by default. However, if you unshare the chat and share it again, the snapshot will be updated to include any new messages.

Note: Users on Team and Enterprise plans can only share chats with other members of the same organization, not publicly. Read more here: Project visibility and sharing.

 

Sharing Chats with Files or MCP Integrations

When sharing chats that include uploaded files or MCP (Model Context Protocol) integrations, it's important to understand what information is included in the shared snapshot.

 

Attached files: If you share a chat that contains an attached file, the file itself is not included in the shared snapshot and remains private. Only the conversation and Claude's responses will be visible to anyone with the link.

 

MCP tool calls: When sharing chats that use MCP integrations, the raw data retrieved from MCP tool calls remains hidden in the shared snapshot. Only the final chat output and conversation will be visible to viewers. The underlying tool call data stays private.

 

This ensures that sensitive information from your files and connected tools is protected, even when you share a chat snapshot.

 

Unsharing Chats

To unshare a chat:

Navigate to the "Share" menu.

Click the visibility dropdown.

Change the chat from "Public" to "Private" to disable the direct link.

 

Managing Shared Chats

Users on free, Pro, or Max plans can review a log of shared chats by navigating to Settings > Privacy. Find the Privacy settings section and click “Manage” next to Shared chats:

 

 

This will open a Shared chats modal listing the title, date shared, and link to each chat, allowing you to easily review and access all your previously-shared content. From here, you also have the option to click “Unshare” next to each listed chat to revoke access to the last snapshot you shared:

 

 

If you don’t have any shared chat snapshots, the Shared chats modal will show “No shared content found”:

 

Related Articles
What are artifacts and how do I use them?
Project visibility and sharing
Publishing and sharing artifacts
Getting Started with Local MCP Servers on Claude Desktop
Anthropic Connectors Directory FAQ