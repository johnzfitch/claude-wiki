---
title: "Claude can now connect to your world | Claude by Anthropic"
source_url: "https://www.claude.com/blog/integrations"
category: "14-Connectors"
fetched_at: "2026-11-18T06:27:25Z"
tags: ["connectors"]
---

# Claude can now connect to your world

Claude can now connect to your apps and tools through Integrations, while advanced Research searches across the web, Google Workspace, and connected services to quickly deliver comprehensive reports.

- 

  Category[Product updates](https://www.claude.com/resources/product-updates)
- 

  ProductClaude apps
- 

  DateMay 1, 2025
- 

  Reading time5 min
- 


Today we're announcing Integrations, a new way to connect your apps and tools to Claude. We're also expanding Claude's [Research](../19-Reference/research.md) capabilities with an advanced mode that searches the web, your Google Workspace, and now your Integrations too. Claude can research for up to 45 minutes before delivering a comprehensive report, complete with citations. In addition to these updates, we're making web search available globally for all Claude users on paid plans.

### Integrations

Last November, we launched the [Model Context Protocol](../19-Reference/model-context-protocol.md) (MCP)—an open standard connecting AI apps to tools and data. Until now, support for MCP was limited to Claude Desktop through local servers. Today, we're introducing Integrations, allowing Claude to work seamlessly with remote MCP servers across the web and desktop apps. Developers can build and host servers that enhance Claude’s capabilities, while users can discover and connect any number of these to Claude.

When you connect your tools to Claude, it gains deep context about your work—understanding project histories, task statuses, and organizational knowledge—and can take actions across every surface. Claude becomes a more informed collaborator, helping you execute complex projects in one place with expert assistance at every step.

To start, you can choose from Integrations for 10 popular services, including [Atlassian’s Jira and Confluence](https://www.atlassian.com/platform/remote-mcp-server), [Zapier](https://zapier.com/mcp), [Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare/tree/main), [Intercom](https://www.intercom.com/blog/introducing-model-context-protocol-fin), [Asana](https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server), [Square](https://developer.squareup.com/docs/mcp), [Sentry](https://docs.sentry.io/product/sentry-mcp/), [PayPal](https://www.paypal.ai/), [Linear](https://linear.app/changelog/2025-05-01-mcp), and [Plaid](https://api.dashboard.plaid.com/mcp/sse)—with more to follow from companies like Stripe, GitLab and Box. Developers can also create their own Integrations in as little as 30 minutes using our documentation or solutions like [Cloudflare](https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/) that provide built-in OAuth authentication, transport handling, and integrated deployment.

Each integration drastically expands what Claude can do. Zapier, for example, connects thousands of apps through pre-built workflows, automating processes across your software stack. With the [Zapier Integration](https://zapier.com/mcp), Claude can access these apps and your custom workflows through conversation—even automatically pulling sales data from [HubSpot](https://developers.hubspot.com/mcp) and preparing meeting briefs based on your calendar.

With access to Atlassian’s Jira and Confluence, Claude can collaborate with you on building new products, managing tasks more effectively, and scaling your work by summarizing and creating multiple Confluence pages and Jira work items at once.

Connect Intercom to respond faster to user feedback. Intercom's AI agent Fin, now an MCP client, can take actions like filing bugs in Linear when users report issues. Chat with Claude to identify patterns and debug using Intercom's conversation history and user attributes—managing the entire workflow from user feedback to bug resolution in one conversation.

### Advanced Research

We're introducing several new updates to build on our recently-released [Research](../19-Reference/research.md) capability. Claude can now conduct deeper investigations across hundreds of internal and external sources, delivering more comprehensive reports in anywhere from five to 45 minutes.

With its new ability to do more complex research, available when you toggle on the Research button, Claude breaks down your request into smaller parts, investigating each deeply before compiling a comprehensive report. While most reports complete in five to 15 minutes, Claude may take up to 45 minutes for more complex investigations—work that would typically take hours of manual research.

We've also expanded Claude's data access. We launched Research with support for web search and Google Workspace, but now with Integrations, Claude can also search any application you connect.

When Claude incorporates information from sources, it provides clear citations that link directly to the original material. This transparency ensures you can confidently use Claude's research findings, knowing exactly where each insight originated.

### Getting started

Integrations and advanced Research are now available in beta on the Max, Team, and Enterprise plans, and will soon be available on Pro. Web search is now globally available to all [Claude.ai](http://claude.ai) paid plans. For more information on getting started with Integrations, MCP servers, and security and privacy practices when connecting data sources to Claude, visit our [Help Center](https://support.anthropic.com/en/articles/11175166-about-integrations-using-remote-mcp). ***‍***

***Update:** Expanded availability. (June 3, 2025)*

Integrations and Research are now available on the Pro, Max, Ultra, Team, and Enterprise plans. Web search is available globally on all Claude plans.


## Related articles

Explore more product news and best practices for teams building with Claude.


ArticleNov 17, 2026

### Linked billing on the Claude Platform

Claude Platform


ArticleNov 12, 2026

### Operate Claude Managed Agents inside your security perimeter

Introducing self-hosted Claude Managed Agents. Now you can run agents in your own environment, whether that’s in your own cloud or on-premise. You host the agents, credentials, and session history, and choose where requests to Claude are sent.

Claude PlatformClaude Managed Agents


ArticleNov 12, 2026

### Introducing Claude for Manufacturing

A new plugin with 17 skills and four connectors helps manufacturers draft quotes, quality reports, and supplier requests from the systems they already run.


ArticleNov 12, 2026

### Introducing Claude Meetings

Add Claude to your video call and get the work started while you talk
