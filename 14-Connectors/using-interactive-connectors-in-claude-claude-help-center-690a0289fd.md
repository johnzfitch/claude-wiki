---
category: "14-Connectors"
fetched_at: "2026-02-10T10:49:36Z"
source_url: "https://support.claude.com/en/articles/13454812-using-interactive-connectors-in-claude"
title: "Using Interactive Connectors in Claude | Claude Help Center"
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

[](#h_08cd95d551)

[](#h_d1afb08f92)

[](#h_49991a9deb)

[](#h_89a2182fc8)

[](#h_d3f43e023a)

[](#h_88cdd90390)

[](#h_20abee644c)

[](#h_b652f3ae07)

[](#h_f81345970d)

[All Collections](/en/)

[Connectors](https://support.claude.com/en/collections/15399129-connectors)

[Pre-Built Connectors](https://support.claude.com/en/collections/17879307-pre-built-connectors)

Using Interactive Connectors in Claude

# Using Interactive Connectors in Claude

Updated this week

Table of contents

[](#h_08cd95d551)

[](#h_d1afb08f92)

[](#h_49991a9deb)

[](#h_89a2182fc8)

[](#h_d3f43e023a)

[](#h_88cdd90390)

[](#h_20abee644c)

[](#h_b652f3ae07)

[](#h_f81345970d)

Interactive connectors are available on Claude web and Claude Desktop for users on Pro, Max, Team, and Enterprise plans.

## What are interactive connectors?

Some connectors can now display live, interactive apps directly within your Claude conversations. Instead of returning text-only responses, these connectors render interfaces — like analytics dashboards, task boards, or design tools — that you can interact with without leaving the chat.

For example, you might ask Claude about your project status, and instead of just describing it, Claude opens your Asana board right in the conversation. You can check off tasks, update statuses, and keep chatting with Claude — all in one place.

## How interactive connectors appear

Interactive connectors display in two ways:

**Inline cards** are compact components embedded directly in the conversation. They're ideal for quick summaries, confirmations, and single actions — like a status update or a message draft ready to send.

**Fullscreen view** provides an immersive interface for complex interactions like data visualizations, document editing, or detailed project views. The conversation input remains available so you can continue talking to Claude while interacting with the connector.

## Interacting with connectors

You can interact directly with elements inside the connector:

- Filter, sort, or drill into data

- Toggle settings, check boxes, or make selections

- Confirm and execute actions (mark complete, send, save)

- Expand and collapse content sections

If you need to ask Claude to modify something, refine a result, or navigate to a different context, type in the conversation input — Claude can interpret your request and update the interface accordingly.

## Which connectors are interactive?

In the [Connectors Directory](https://claude.ai/directory), connectors with this capability are marked with an "Interactive” badge. Current interactive connectors include:

- **Amplitude** — View and interact with analytics dashboards

- **Asana** — Manage tasks and project boards

- **Box** — Work with documents and files

- **Canva** — Create and edit designs

- **Clay** — Manage contacts and outreach

- **Figma** — Review and annotate designs

- **Hex** — Explore data and notebooks

- **Slack** — Draft and send messages

We’re adding support for more interactive connectors over time.

## Getting started with interactive connectors

1.  Navigate to the [Connectors Directory](https://claude.ai/directory).

2.  Look for connectors marked with the "Interactive" badge.

3.  Connect and authenticate with the connector.

4.  Start a conversation with Claude and ask about something the connector handles — the interactive elements will appear automatically when relevant.

**Note:** Interactive connectors are default on when you have the relevant connector enabled. No additional setup is needed.

## Considerations for Team and Enterprise plans

### Can Team and Enterprise owners control interactive connectors separately from standard connectors?

Yes. Team and Enterprise Owners can disable the specific tool calls that render interactive connectors within [Admin settings \> Connectors](https://claude.ai/admin-settings/connectors). This does not disable the connector itself — text-based tool functionality continues to work normally.

## Permissions and Security

### How are interactive connectors secured?

Interactive connectors run in sandboxed iframes with strict Content Security Policies. All communication between the interface and Claude uses auditable JSON-RPC messaging. Servers must predeclare which external domains they need, and the host can review HTML content before rendering.

### Do interactive connectors require additional permissions beyond the connector itself?

No. Interactive connectors use the same permissions you granted when connecting the tool. They don't request additional access to your data.

### Can interactive connectors make purchases or financial transactions?

No. Purchases through third-party interactive connectors are not supported.

## Troubleshooting

### The interface isn't appearing

- Confirm you're using Claude web or Claude Desktop (not mobile).

- Check that the connector is connected and enabled for your current conversation.

- Try starting a new conversation and asking Claude a question that the connector handles.

### The connector isn't responding to interactions

- Check your internet connection.

- Try refreshing the page or restarting Claude Desktop.

- If the issue persists, disconnect and reconnect the connector in [Settings \> Connectors](https://claude.ai/settings/connectors).

### I want to disable interactive connectors

- Team and Enterprise users: Ask your organization Owner to disable the relevant tool calls in [Admin settings \> Connectors](https://claude.ai/admin-settings/connectors).

- Individual users: You can disable specific connector tools via the "Search and tools" menu in your conversation.

## I'm a developer. Where can I learn about building MCP Apps?

MCP Apps is the open-source extension to the Model Context Protocol that powers interactive apps. If you are building your own interactive connector, note that it must meet additional design, security, and testing requirements. See the [Remote MCP Server Submission Guide](https://support.claude.com/en/articles/12922490) for details.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)

Getting started with custom connectors using remote MCP

[](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp)

Pre-built Web Connectors Using Remote MCP

[](https://support.claude.com/en/articles/11724452-using-the-connectors-directory-to-extend-claude-s-capabilities)

Using the Connectors Directory to extend Claude’s capabilities

[](https://support.claude.com/en/articles/12614798-using-the-synapse-org-connector-in-claude)

Using the Synapse.org Connector in Claude

[](https://support.claude.com/en/articles/12614810-using-the-benchling-connector-in-claude)

Using the Benchling Connector in Claude

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
