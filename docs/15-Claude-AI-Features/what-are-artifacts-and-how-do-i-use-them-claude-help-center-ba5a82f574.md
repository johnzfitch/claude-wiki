---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-10T10:49:40Z"
source_url: "https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them"
title: "What are artifacts and how do I use them? | Claude Help Center"
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

[](#h_f7d007e3b0)

[](#h_446865fd78)

[](#h_3d4e6623c6)

[](#h_9cbf05e668)

[](#h_814c8c8496)

[](#h_8fd83d1dd6)

[](#h_7f1cce77e4)

[](#h_49d1cebabb)

[All Collections](/en/)

[Claude](https://support.claude.com/en/collections/4078531-claude)

[Features and Capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities)

What are artifacts and how do I use them?

# What are artifacts and how do I use them?

Updated this week

Table of contents

[](#h_f7d007e3b0)

[](#h_446865fd78)

[](#h_3d4e6623c6)

[](#h_9cbf05e668)

[](#h_814c8c8496)

[](#h_8fd83d1dd6)

[](#h_7f1cce77e4)

[](#h_49d1cebabb)

Accessing artifacts in the sidebar and Claude-powered artifacts are supported on free, Pro, Max, Team, and Enterprise plans.

Artifacts allow you to turn ideas into shareable apps, tools, or content—build tools, visualizations, and experiences by simply describing what you need. Claude can share substantial, standalone content with you in a dedicated window separate from the main conversation. This makes it easy to work with significant pieces of content that you may want to modify, build upon, or reference later.

------------------------------------------------------------------------

## What are artifacts?

Claude creates an artifact when the content it's sharing meets these criteria:

- It is significant and self-contained, typically over 15 lines.

- It is something you're likely to want to edit, iterate on, or reuse outside the conversation.

- It represents a complex piece of content that stands on its own without requiring extra conversation context.

- It is content you're likely to want to refer back to or use later.

Common examples of artifact content include:

- Documents (Markdown or plain text)

- Code snippets

- Single-page HTML websites

- SVG images

- Diagrams and flowcharts

- Interactive React components

------------------------------------------------------------------------

## Enabling or disabling artifacts

Artifacts are available on all Claude plans: free, Pro, Max, Team, and Enterprise.

To adjust your artifacts preferences:

1.  Click your initials or name in the lower left corner.

2.  Navigate to [Settings \> Capabilities](https://claude.ai/settings/capabilities).

3.  Find **Artifacts** and toggle it on or off.

**Note:** Team and Enterprise administrators may manage some artifact settings at the organization level.

------------------------------------------------------------------------

## Accessing your artifacts

You can access all your artifacts through the dedicated artifacts space in your Claude sidebar. This space allows you to:

- View all your creations in one organized location

- Browse Anthropic-created artifacts for inspiration

- Create new artifacts from scratch or by customizing existing ones

- Manage and organize your artifact collection

Team and Enterprise users can also browse work-focused artifacts shared within their organization.

------------------------------------------------------------------------

## Working with artifacts

When Claude creates an artifact, you'll see the content displayed in a dedicated window to the right of the main chat.

### Edit and iterate

- Ask Claude to modify or update the artifact content

- Changes appear directly in the artifact window

- Switch between different versions using the version selector

- Your edits won't change Claude's memory of the original content

- Edit prior chat messages to create a different version of the conversation, with its own set of artifacts—this lets you explore different directions without losing previous work

### View and export

In the lower right corner of the artifact window, you can:

- View the underlying code of any artifact

- Copy content to your clipboard

- Download files to use outside the conversation

### Multiple artifacts

- Open and work with several artifacts in one conversation

- Use the chat controls (slider icon in upper right) to switch between them

- Select which artifact you want Claude to reference for updates

### Fixing errors

If an artifact generates an error, look for the “Try fixing with Claude” button near the error message. Click the button to automatically copy the error details into a new message, then send it to Claude to diagnose the issue and suggest a fix.

**Note:** While Claude will attempt to fix the error, success isn't guaranteed. Some errors may require additional troubleshooting.

------------------------------------------------------------------------

## AI-powered artifacts

AI-powered artifacts are available on all Claude plans: free, Pro, Max, Team, and Enterprise.

You can build artifacts that embed AI capabilities, turning them into AI-powered apps. Users of your artifacts can access Claude's intelligence through a text-based API—answering questions, generating creative content, providing personalized coaching, playing games, solving problems, and adapting responses based on input.

### Creating AI-powered artifacts

1.  Describe what you want to Claude

2.  Claude writes the code

3.  The app runs on Anthropic's infrastructure

4.  Users authenticate with their Claude account and interact with their own instance of the artifact

### How usage works

When you share AI-powered artifacts, others can use them immediately—no API keys required, and no costs to you. Whether your artifact helps 10 people or 10,000, sharing is free. Usage counts against each user's own Claude subscription limits, not yours.

For Team and Enterprise plans, when you share AI-powered artifacts within your organization, team members can use them without incurring additional costs to the creator.

------------------------------------------------------------------------

## MCP integration

MCP integration for artifacts is available on Pro, Max, Team, and Enterprise plans on Claude web and desktop.

Artifacts can connect to external services through the Model Context Protocol (MCP), enabling interactive applications that read from and write to tools like Asana, Google Calendar, and Slack. In addition to Anthropic's official MCP integrations, artifacts can connect to any [custom MCP servers](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) you've configured.

When an artifact needs to access an MCP tool, you'll be prompted to approve access on first interaction. Your preferences persist for subsequent uses of that artifact.

**Important:** Each user must authenticate MCP servers independently, even when using shared or published artifacts. Organization admins can enable or disable artifact MCP access at the organization level but cannot manage which specific MCP servers artifacts can use.

------------------------------------------------------------------------

## Persistent Storage

Persistent storage for artifacts is available on Pro, Max, Team, and Enterprise plans on Claude web and desktop.

Artifacts can store data across sessions, enabling stateful applications like journals, trackers, and collaborative tools. Storage can be configured as either personal or shared:

- **Personal storage:** Each user maintains their own private data. For example, in a journal artifact, your entries remain visible only to you.

- **Shared storage:** All users see and interact with the same data. For example, in a game leaderboard, everyone sees the same scores and rankings.

When you interact with an artifact that uses shared storage for the first time, you'll see a confirmation dialog explaining that your data will be visible to other users of that artifact.

**Note:** Persistent storage is only available for published artifacts. During development and testing, storage operations will not succeed until the artifact is published.

**Storage specifications:**

- 20 MB storage limit per artifact

- Text-only input—no images, files, or binary data

- Personal and shared storage are isolated

- Unpublishing an artifact permanently deletes all associated storage data

**Privacy consideration:** Artifact creators determine which data uses personal versus shared storage when building the artifact. Before entering sensitive information, consider whether the artifact uses shared storage.

------------------------------------------------------------------------

## Learn More

To share your artifacts publicly, embed them on websites, or discover artifacts created by others, see Publishing and sharing artifacts.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/9547008-publishing-and-sharing-artifacts)

Publishing and sharing artifacts

[](https://support.claude.com/en/articles/9945615-intro-to-artifacts)

Intro to Artifacts

[](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)

Getting started with custom connectors using remote MCP

[](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp)

Pre-built Web Connectors Using Remote MCP

[](https://support.claude.com/en/articles/11649427-use-artifacts-to-visualize-and-create-ai-apps-without-ever-writing-a-line-of-code)

Use artifacts to visualize and create AI apps, without ever writing a line of code

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
