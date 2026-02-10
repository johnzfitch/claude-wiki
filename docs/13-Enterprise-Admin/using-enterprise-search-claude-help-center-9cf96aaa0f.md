---
category: "13-Enterprise-Admin"
fetched_at: "2026-02-10T10:49:29Z"
source_url: "https://support.claude.com/en/articles/12489464-using-enterprise-search"
title: "Using Enterprise Search | Claude Help Center"
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

[](#h_c7a5619439)

[](#h_c4f87aaaef)

[](#h_3ee9eca784)

[](#h_f5b68b9555)

[](#h_d7fea5a243)

[](#h_3474848706)

[](#h_956e14c7d4)

[](#h_442d4c1b2c)

[](#h_14d807930d)

[](#h_e1ab81299d)

[All Collections](/en/)

[Team and Enterprise Plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)

[General](https://support.claude.com/en/collections/9811414-general)

Using Enterprise Search

# Using Enterprise Search

Updated this week

Table of contents

[](#h_c7a5619439)

[](#h_c4f87aaaef)

[](#h_3ee9eca784)

[](#h_f5b68b9555)

[](#h_d7fea5a243)

[](#h_3474848706)

[](#h_956e14c7d4)

[](#h_442d4c1b2c)

[](#h_14d807930d)

[](#h_e1ab81299d)

Enterprise search capabilities are available for users on Claude for Work (Team and Enterprise) plans.

Enterprise search adds a dedicated project for searching across your organization's knowledge sources with optimized instructions and seamless connector integrations.

## What is enterprise search?

We’ve added a pre-configured “Ask Your Org” [project](https://support.claude.com/en/articles/9517075-what-are-projects) that appears in your sidebar. This project is designed specifically for unified knowledge access across your company's tools and data sources. This dedicated workspace provides:

- **Guided setup:** Easy onboarding flow for connecting your work apps.

- **Organization-wide availability:** Available to all members of your organization after an Owner completes the initial setup process.

  - Owners can control which apps are connected to the project.

  - Users need to authenticate with the connected apps before they can start using them.

- **Optimized instructions:** Specialized system prompts maintained by Anthropic for effective searches.

- **Unified access:** Search across multiple data sources (Slack, Microsoft 365, and more) in one place.

------------------------------------------------------------------------

## Getting Started

### For Owners

The enterprise search project is enabled by default for all Team and Enterprise plan organizations within Admin settings, but Owners will need to complete this initial setup process before other members can use it:

1.  Click “Ask Your Org” in the menu on the left of your screen.

2.  Click the “Set up for your org” button to continue or “Disable” to turn the project off for your team.

3.  If setting up the project, you’ll be prompted to connect some tools to the project.

    1.  You are required to choose a connector for both **Documents** and **Chat**; **Email** is recommended but optional.

    2.  Only enabled connectors will be available in the enterprise search project.

4.  Click “+ Add more” to set up any other tools your team needs.

    1.  Choose between “Select another MCP” to open the Connectors directory, or “+ Add custom connector”

5.  Click “Next” when you’re finished.

6.  On the last screen, you can edit the name of your project. The format will be “Ask \[Name field\],” so whatever you enter here will impact what shows on the left panel.

7.  Enter a description, then click “Finish set up.”

If you decide to stop using the project after setting it up, an Owner will need to manually disable this feature organization-wide to remove it from users’ accounts:

1.  Navigate to [Admin settings \> Capabilities](https://claude.ai/admin-settings/capabilities).

2.  Locate "Ask Your Org"

3.  Click the “Disable” button to turn the feature off.

### For users

The enterprise search project will be starred in your sidebar by default when the feature is enabled for your organization.

**First-time setup:**

1.  Click on the "Ask {org name}" project in your sidebar.

2.  Follow the guided onboarding flow to connect to recommended services.

3.  Authenticate with the services you want to search (Slack, Google, Microsoft 365).

    1.  The more connectors you enable, the more comprehensive your search results will be.

4.  Start asking Claude questions about your organization’s knowledge.

## Customizing your enterprise search project

**Connecting additional tools:**

After initial setup, you can enable additional connectors in your search project by clicking “Connect” in the **Instructions** section and allowing access to the tools and connectors shown in the modal.

**To unstar or hide the project:**

1.  Click the “...” next to the project in your sidebar

2.  Select "Unstar"

**To adjust connected tools:**

1.  Open the search project.

2.  Click "Search and tools" in the lower left.

3.  Enable or disable specific connectors.

4.  Changes apply to new conversations in the project.

------------------------------------------------------------------------

## How does enterprise search work?

When you ask a question within your organization’s dedicated project, Claude searches across all your connected data sources to generate comprehensive, well-cited responses.

**Example queries:**

- "What is our company's remote work policy?"

- "Summarize discussions about the Q4 product roadmap."

- "Find information about our customer onboarding process."

- "What were the key decisions from last week's leadership meetings?"

Claude will search your connected tools—such as SharePoint documents, Slack conversations, Gmail threads, and Google Drive files—and synthesize information into a unified response with source citations.

## Comparing enterprise search to standard projects

[TABLE]

## Use Cases

Enterprise Search is particularly valuable for:

**Executive briefings:**

- "What happened yesterday while I was out?"

- "Summarize key updates across the business"

**Project research:**

- "What are the main reasons customers cite for why they pick our competitors?"

- "What are the current blockers on the Infrastructure project?"

**Policy and process questions:**

- "What is our vacation policy?"

- "How do I submit an expense report?"

**Onboarding:**

- "How does our authentication system work?"

- "Who should I talk to, to learn about X?"

**Performance reviews:**

- "Find discussions and documents related to \[employee\]'s Q3 projects"

- "Summarize team contributions to the Platform initiative"

------------------------------------------------------------------------

## Privacy and Permissions

- **Permission-aware:** You only see search results from data you have permission to access in the original systems.

- **User-level authentication for connectors:** Each user authenticates with their own credentials to enable connectors.

- **No external indexing:** Search results are generated by making MCP calls. No data from connected services are indexed in our systems for serving queries.

- **Data security:** All data access follows your organization's existing security controls and policies.

## Best Practices

**Be specific about sources:** Instead of "Find information about the product launch,” try "Search Slack and Google Drive for discussions about the Q4 product launch."

**Use date ranges:** "Summarize emails from last week about the budget review."

**Combine multiple sources:** "Compile information from SharePoint documents, Slack discussions, and meeting notes about our hiring process."

**Break complex queries into steps:** For thorough research, ask Claude to search one source at a time, then synthesize findings.

------------------------------------------------------------------------

## Troubleshooting

### The search project isn't appearing in my sidebar

- Verify you’re using a Team or Enterprise plan..

- Have an Owner check that the feature is enabled for your organization.

- Try refreshing your browser or signing out and back in.

### I can't connect a recommended connector

- Check that an Owner has enabled the connector at the organization level.

- Confirm that you have an active account with the service.

- Ensure your organization's policies don't block third-party integrations.

- Make sure you've completed the authentication flow properly.

- Contact your administrator or IT department if problems persist.

### My search results seem incomplete

- Verify you've connected the relevant services through the onboarding flow.

- Check that you've authenticated successfully with each connected service.

- Confirm you have permissions to access the content in the original systems.

- Try being more specific about which tools to search or what information you need.

- Narrow your search with date ranges or specific keywords.

- Break complex queries into smaller, focused sections.

### Connected tools aren't working

- Revisit [Settings \> Connectors](http://claude.ai/settings/connectors) to verify authentication status.

- Try disconnecting and reconnecting the problematic connector.

- Check if the connector was recently disabled at the organization level.

### Claude is responding slowly in my search project – what should I do?

**Possible causes:**

- Searching across many large data sources takes time

- Network connectivity issues

- High load on connected services

**Try:**

- Narrowing your search scope

- Searching one tool at a time

- Being more specific about what you're looking for

### What happens if a connector stops working?

If a connector fails:

1.  The dedicated project will search remaining connected tools.

2.  You'll see a notice about the failed connector.

3.  Try reconnecting the tool through [Settings \> Connectors](http://claude.ai/settings/connectors).

4.  Contact an organization Owner if the issue persists.

## 

------------------------------------------------------------------------

## FAQ

### Can I add my own custom connectors to the search project?

Yes. You can add connectors available through [Settings \> Connectors](http://claude.ai/settings/connectors), and you can also add custom connectors if permitted by your organization. The guided onboarding recommends a few connectors, but you're not limited to those.

For more information, refer to [Getting Started with Custom Connectors Using Remote MCP](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).

### Can I use enterprise search on mobile or desktop apps?

The search project mirrors the availability of regular projects and is fully functional on the Claude web app, Claude Desktop, and Claude Mobile (iOS/Android).

### Will using the search project count against my usage limits?

Yes. Search queries within the project count toward your plan's standard usage limits, just like other projects and conversations.

### How is this feature different from using Research?

**Research**:

- Designed for deep, multi-step research on specific topics

- Performs extensive web and internal data searches automatically

- Takes longer and may use more messages

- Best for complex research projects

**Enterprise search:**

- Optimized for quick knowledge retrieval

- Searches internal sources you've connected

- Faster responses for finding specific information

- Best for everyday knowledge access

See [When should I use web search, extended thinking, and Research?](https://support.claude.com/en/articles/11095361) for more guidance.

### What data can Claude access in my search project?

Claude can only access data within the project that:

1.  Comes from connectors you've individually added and authenticated to.

2.  You have permission to view within the original systems.

3.  Is potentially relevant based on your search queries.

### Does everyone in my organization see the same search results?

No. Search results are permission-aware. You only see data that you have permission to access in each connected system.

### Is my search history visible to others?

No. Conversations within your search project are private to you unless you choose to manually share them, just like other conversations with Claude. However, on Enterprise plans, conversations follow your [organization's data retention policies](https://support.claude.com/en/articles/10440198-custom-data-retention-controls-for-enterprise-plans).

### How long are search results retained?

Search results are retained with their associated chats. You can delete search data by deleting the associated conversation. Enterprise organizations may have custom data retention policies that apply to all conversations, including those within the search project. Check with your organization Owner for details.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)

Getting started with custom connectors using remote MCP

[](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp)

Pre-built Web Connectors Using Remote MCP

[](https://support.claude.com/en/articles/12542951-enabling-and-using-the-microsoft-365-connector)

Enabling and Using the Microsoft 365 Connector

[](https://support.claude.com/en/articles/12614798-using-the-synapse-org-connector-in-claude)

Using the Synapse.org Connector in Claude

[](https://support.claude.com/en/articles/13454812-using-interactive-connectors-in-claude)

Using Interactive Connectors in Claude

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
