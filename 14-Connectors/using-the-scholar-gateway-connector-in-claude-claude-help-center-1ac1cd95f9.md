---
category: "14-Connectors"
fetched_at: "2026-02-10T10:49:30Z"
source_url: "https://support.claude.com/en/articles/12614815-using-the-scholar-gateway-connector-in-claude"
title: "Using the Scholar Gateway Connector in Claude | Claude Help Center"
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

[](#h_cb895ca2e4)

[](#h_174fd157bb)

[](#h_87f3cbd784)

[](#h_491024c0e0)

[All Collections](/en/)

[Claude for Life Sciences](https://support.claude.com/en/collections/16142619-claude-for-life-sciences)

Using the Scholar Gateway Connector in Claude

# Using the Scholar Gateway Connector in Claude

Updated this week

Table of contents

[](#h_cb895ca2e4)

[](#h_174fd157bb)

[](#h_87f3cbd784)

[](#h_491024c0e0)

The Scholar Gateway by Wiley integration provides authenticated access to the most relevant snippets of scientific research papers to utilize within Claude. This article explains how to set up and use the Scholar Gateway integration with Claude to accelerate your research workflows.

The Scholar Gateway integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## What this integration provides

Currently \>3 million journal articles are available through Scholar Gateway with additional collections, databases and new articles being added all the time.

These datasets cover key STEM subjects including articles from a significant number of leading Life Sciences journals. Specifically, Scholar Gateway has over 300 Life Sciences journals that cover over 900,000 research articles.

Scholar Gateway (Beta) enables AI responses grounded in peer-reviewed sources with verifiable citations and DOI links. Instead of relying on general AI knowledge, Scholar Gateway (Beta) searches current literature from Wiley journals and research databases to deliver evidence-backed answers with complete source metadata. While the Beta currently provides access to Wiley content only, additional publisher sources will be added soon. This enables you to verify that claims are backed with sourced research — ensuring your AI-assisted research meets professional research standards.

## Who can access the Scholar Gateway integration

- Existing subscribers to Wiley journals will need to upgrade their subscription following a trial period to allow AI access.

- New subscribers will need to subscribe subject to a trial period.

More details on accessing the integration can be found in [Wiley’s MCP Server Documentation](https://docs.scholargateway.ai).

## Setting up the Scholar Gateway integration

**For Organization Owners (Team and Enterprise)**

1.  Navigate to Admin settings \> Connectors

2.  Click "Browse connectors"

3.  Click “**Scholar Gateway**”

4.  Click “Add to your team”

**For Individual Claude Users**

1.  Navigate to Settings \> Connectors

2.  Click “Connect”

3.  Follow the instructions to authenticate with your Wiley account

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

**For Claude Code Users**

1.  Command: `/plugin marketplace add anthropics/life-sciences`

2.  Command: `/plugin install wiley-scholar-gateway@life-sciences`

3.  Restart Claude Code

4.  Verify that the server is connected with `/mcp`

Technical details of the Scholar Gateway integration can be found in [Wiley’s MCP Server Documentation](https://docs.scholargateway.ai).

## Common use cases

- Enhanced literature review when planning experiments and research plans, to efficiently identify, summarize, and evaluate relevant literature as individual articles or in aggregation, enabling new ways of doing research and delivering reliable and cited insights in seconds.​

- Information on latest research in a certain field of medicine or pharmaceuticals.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/12614768-getting-started-with-claude-for-life-sciences)

Getting Started with Claude for Life Sciences

[](https://support.claude.com/en/articles/12614795-using-the-biorender-connector-in-claude)

Using the BioRender Connector in Claude

[](https://support.claude.com/en/articles/12614798-using-the-synapse-org-connector-in-claude)

Using the Synapse.org Connector in Claude

[](https://support.claude.com/en/articles/12614801-using-the-pubmed-connector-in-claude)

Using the PubMed Connector in Claude

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
