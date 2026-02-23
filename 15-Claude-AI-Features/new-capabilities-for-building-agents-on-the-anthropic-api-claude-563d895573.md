---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-22T10:55:32Z"
last_modified: "Sat, 21 Feb 2026 19:44:20 GMT"
source_url: "https://claude.com/blog/agent-capabilities-api"
title: "New capabilities for building agents on the Anthropic API | Claude"
---

# New capabilities for building agents on the Anthropic API

Claude now offers code execution, MCP server connections, file storage, and extended prompt caching through the API—giving developers powerful tools to build agents that analyze data, connect to external systems, and maintain context for longer periods of time.

[](#)

[](#)

- 

  Category

  [Product announcements](https://claude.com/blog/category/announcements)

- 

  Product

  Claude Developer Platform

- 

  Date

  May 22, 2025

- 

  Reading time

  5

  min

- 

  Share

  [Copy link](#)
  https://claude.com/blog/agent-capabilities-api

Today, we're announcing four new capabilities on the Anthropic API that enable developers to build more powerful AI agents: the code execution tool, MCP connector, Files API, and the ability to cache prompts for up to one hour.

### Building better AI agents

Together with [Claude Opus 4 and Sonnet 4](https://www.anthropic.com/news/claude-4), these beta features enable developers to build agents that execute code for advanced data analysis, connect to external systems through MCP servers, store and access files efficiently across sessions, and maintain context for up to 60 minutes with cost-effective caching—without building custom infrastructure.

For example, a project management AI agent can use the MCP connector with Asana to reference tasks and assign work, upload relevant reports via the Files API, analyze progress and risks with the code execution tool, and maintain full context throughout—all while keeping costs down through extended prompt caching.

These capabilities join existing features like [web search](https://www.anthropic.com/news/web-search-api) and [citations](https://www.anthropic.com/news/introducing-citations-api) as part of a comprehensive toolkit for building AI agents. Read on to explore each new capability in detail.

### Code execution tool

We're introducing a [code execution tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool) on the Anthropic API, giving Claude the ability to run Python code in a sandboxed environment to produce computational results and data visualizations. This transforms Claude from a code-writing assistant into a data analyst that can iterate on visualizations, clean datasets, and derive insights directly within API calls.

With the code execution tool, Claude can load datasets, generate exploratory charts, identify patterns, and iteratively refine outputs based on execution results—all within a single interaction. This means that Claude can handle complex analytical tasks end-to-end, rather than just suggesting code for you to run separately.

Key use cases include:

- **Financial modeling**: Generate financial projections, analyze investment portfolios, and calculate complex financial metrics.
- **Scientific computing**: Execute simulations, process experimental data, and analyze research datasets.
- **Business intelligence**: Create automated reports, analyze sales data, and generate performance dashboards.
- **Document processing**: Extract and transform data across formats, generate formatted reports, and automate document workflows.
- **Statistical analysis**: Perform regression analysis, hypothesis testing, and predictive modeling on datasets.

Organizations receive 50 free hours of usage with the code execution tool per day, then pay \$0.05 per hour per container for additional usage. Explore the [documentation](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool) to learn more about pricing.

### MCP connector

The [MCP connector](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector) on the Anthropic API enables developers to connect Claude to any remote Model Context Protocol (MCP) server without writing client code.

Previously, connecting to MCP servers required building your own client harness to handle MCP connections. Now, the Anthropic API handles all connection management, tool discovery, and error handling automatically. Simply add a remote MCP server URL to your API request and you can immediately access powerful third-party tools, dramatically reducing the complexity of building tool-enabled agents.

When Claude receives a request with MCP servers configured, it automatically:

- Connects to the specified MCP servers
- Retrieves available tools
- Reasons about what tool to call and what arguments to pass
- Executes tool calls agentically until a sufficient result is achieved
- Manages authentication and error handling
- Returns the enhanced response with integrated data

The growing ecosystem of remote MCP servers means you can easily add capabilities to your AI applications without building one-off integrations. You can integrate with any remote MCP server, including those from [Zapier](https://zapier.com/mcp) and [Asana](https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server). See more remote MCP servers in our [documentation](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers).

### Files API

The [Files API](https://docs.anthropic.com/en/docs/build-with-claude/files) simplifies how developers store and access documents when building with Claude. Instead of managing file uploads in every request, you can now upload documents once and reference them repeatedly across conversations.

This streamlines development workflows, particularly for applications that need to work with large document sets such as knowledge bases, technical documentation, or datasets.

The Files API will integrate with the code execution tool, enabling Claude to access and process uploaded files directly during code execution and produce files such as charts and graphs as part of the response. This means developers can upload a dataset through the Files API once, then have Claude analyze it across multiple sessions without re-uploading.

### Extended prompt caching

Developers can now choose between our standard 5-minute time to live (TTL) for [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) or opt for an [extended 1-hour TTL](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration-beta) at an [additional cost](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pricing)—a 12x improvement that can reduce expenses for long-running agent workflows. With extended caching, customers can provide Claude with extensive background knowledge and examples while reducing costs by up to 90% and latency by up to 85% for long prompts.

This makes it practical to build agents that maintain context over extended periods, whether they're handling multi-step workflows, analyzing complex documents, or coordinating with other systems. Long-running agent applications that previously faced prohibitive costs can now operate efficiently at scale.

### Getting started

All of these features are now available in public beta on the Anthropic API. [Visit our documentation](https://docs.anthropic.com/en/docs/overview) to learn more or [watch the keynote](https://www.youtube.com/live/EvtPBaaykdo) from our developer conference to see these capabilities in action.

No items found.

[Prev](#)

Prev

0/5

[Next](#)

Next

eBook

## 

[](#)

FAQ

No items found.

[](#)

## Related posts

Explore more product news and best practices for teams building with Claude.

Feb 20, 2026

### Bringing automated preview, review, and merge to Claude Code on desktop

Claude Code

[Bringing automated preview, review, and merge to Claude Code on desktop](#)

Bringing automated preview, review, and merge to Claude Code on desktop

[Bringing automated preview, review, and merge to Claude Code on desktop](/blog/preview-review-and-merge-with-claude-code)

Bringing automated preview, review, and merge to Claude Code on desktop

Feb 17, 2026

### Increase web search accuracy and efficiency with dynamic filtering

Product announcements

[Increase web search accuracy and efficiency with dynamic filtering](#)

Increase web search accuracy and efficiency with dynamic filtering

[Increase web search accuracy and efficiency with dynamic filtering](/blog/improved-web-search-with-dynamic-filtering)

Increase web search accuracy and efficiency with dynamic filtering

Jan 12, 2026

### Cowork: Claude Code for the rest of your work

Product announcements

[Cowork: Claude Code for the rest of your work](#)

Cowork: Claude Code for the rest of your work

[Cowork: Claude Code for the rest of your work](/blog/cowork-research-preview)

Cowork: Claude Code for the rest of your work

Jan 26, 2026

### Your favorite work tools are now interactive connectors inside Claude

Product announcements

[Your favorite work tools are now interactive connectors inside Claude](#)

Your favorite work tools are now interactive connectors inside Claude

[Your favorite work tools are now interactive connectors inside Claude](/blog/interactive-tools-in-claude)

Your favorite work tools are now interactive connectors inside Claude

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)

See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)

Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

[Subscribe](#)

Subscribe

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.
