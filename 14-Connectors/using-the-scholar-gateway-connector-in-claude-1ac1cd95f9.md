---
category: "14-Connectors"
fetched_at: "2026-03-12T08:19:48Z"
source_url: "https://support.claude.com/en/articles/12614815-using-the-scholar-gateway-connector-in-claude"
title: "Using the Scholar Gateway Connector in Claude | Claude Help Center"
---

3.  Using the Scholar Gateway Connector in Claude

# Using the Scholar Gateway Connector in Claude


The Scholar Gateway by Wiley integration provides authenticated access to the most relevant snippets of scientific research papers to utilize within Claude. This article explains how to set up and use the Scholar Gateway integration with Claude to accelerate your research workflows.

The Scholar Gateway integration relies upon Claude's ability to **[use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory)**.

## What this integration provides

Currently \>3 million journal articles are available through Scholar Gateway with additional collections, databases and new articles being added all the time.

These datasets cover key STEM subjects including articles from a significant number of leading Life Sciences journals. Specifically, Scholar Gateway has over 300 Life Sciences journals that cover over 900,000 research articles.

Scholar Gateway (Beta) enables AI responses grounded in peer-reviewed sources with verifiable citations and DOI links. Instead of relying on general AI knowledge, Scholar Gateway (Beta) searches current literature from Wiley journals and research databases to deliver evidence-backed answers with complete source metadata. While the Beta currently provides access to Wiley content only, additional publisher sources will be added soon. This enables you to verify that claims are backed with sourced research — ensuring your AI-assisted research meets professional research standards.

## Who can access the Scholar Gateway integration

- Existing subscribers to Wiley journals will need to upgrade their subscription following a trial period to allow AI access.

- New subscribers will need to subscribe subject to a trial period.

More details on accessing the integration can be found in **[Wiley’s MCP Server Documentation](https://docs.scholargateway.ai)**.

## Setting up the Scholar Gateway integration

**For Organization Owners (Team and Enterprise)**

1.  Navigate to Organization settings \> Connectors

2.  Click "Browse connectors"

3.  Click “**Scholar Gateway**”

4.  Click “Add to your team”

**For Individual Claude Users**

1.  Navigate to Settings \> Connectors

2.  Click “Connect”

3.  Follow the instructions to authenticate with your Wiley account

Learn about **[finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory)**.

**For Claude Code Users**

1.  Command: `/plugin marketplace add anthropics/life-sciences`

2.  Command: `/plugin install wiley-scholar-gateway@life-sciences`

3.  Restart Claude Code

4.  Verify that the server is connected with `/mcp`

Technical details of the Scholar Gateway integration can be found in **[Wiley’s MCP Server Documentation](https://docs.scholargateway.ai)**.

## Common use cases

- Enhanced literature review when planning experiments and research plans, to efficiently identify, summarize, and evaluate relevant literature as individual articles or in aggregation, enabling new ways of doing research and delivering reliable and cited insights in seconds.​

- Information on latest research in a certain field of medicine or pharmaceuticals.

------------------------------------------------------------------------

Related Articles


Getting Started with Claude for Life Sciences


Using the BioRender Connector in Claude


Using the Synapse.org connector in Claude


Using the PubMed Connector in Claude


Using the Benchling Connector in Claude
