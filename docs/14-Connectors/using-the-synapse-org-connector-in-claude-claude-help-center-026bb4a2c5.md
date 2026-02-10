---
category: "14-Connectors"
fetched_at: "2026-02-10T10:49:30Z"
source_url: "https://support.claude.com/en/articles/12614798-using-the-synapse-org-connector-in-claude"
title: "Using the Synapse.org Connector in Claude | Claude Help Center"
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

[](#h_38ea08e92f)

[](#h_1345a32636)

[](#h_b2bf2d27b5)

[](#h_2d346b4c8a)

[All Collections](/en/)

[Claude for Life Sciences](https://support.claude.com/en/collections/16142619-claude-for-life-sciences)

Using the Synapse.org Connector in Claude

# Using the Synapse.org Connector in Claude

Updated this week

Table of contents

[](#h_38ea08e92f)

[](#h_1345a32636)

[](#h_b2bf2d27b5)

[](#h_2d346b4c8a)

The Synapse.org integration by Sage Bionetworks allows researchers to discover biomedical data across all of Synapse, see the structure of projects, and retrieve information on their data assets for authorized users. This article explains how to set up and use the Synapse.org integration with Claude to advance your research and analysis workflows.

The Synapse.org integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## What this integration provides

Services include search and (meta)data retrieval services. Data access will be governed by the access controls defined for each project. Some data are publicly available, while others require approval from Synapse’s governance team prior to access.

## Who can access the Synapse.org integration

- Individuals who have a registered Synapse account ([register for free](https://accounts.synapse.org/register1?appId=synapse.org))

- Data access may be subject to use restriction from contributors

More details on accessing the integration can be found in [Synapse’s MCP Server Documentation](https://github.com/susheel/synapse-mcp?tab=readme-ov-file#synapse-mcp-server).

## Setting up the Synapse.org integration

**For Organization Owners (Team and Enterprise)**

1.  Navigate to Admin settings \> Connectors

2.  Click "Browse connectors"

3.  Click “**Synapse.org**”

4.  Click “Add to your team”

**For Individual Claude Users**

1.  Navigate to Settings \> Connectors

2.  Click “Connect”

3.  Follow the instructions to authenticate with your Synapse.org account

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

**For Claude Code Users**

1.  Command: `/plugin marketplace add anthropics/life-sciences`

2.  Command: `/plugin install synapse@life-sciences`

3.  Restart Claude Code

4.  Verify that the server is connected with `/mcp`

Technical details of the Synapse.org integration can be found in [Synapse’s MCP Server Documentation](https://github.com/susheel/synapse-mcp?tab=readme-ov-file#synapse-mcp-server).

## Common use cases

- Search for reusable scientific data across all of the Synapse.org platform

  - *“Find RNA-seq datasets related to Alzheimer's disease in Synapse”*

  - *“Search Synapse for single-cell transcriptomics datasets”*

  - *"Find genomic sequencing data for plexiform neurofibromas in the NF Data Portal”*

- Authorized users can see hierarchy of folders, files, tables, datasets within projects to help organize and monitor data assets

  - *“Explain the files and folders in the public AACR Project GENIE project”*

  - *“Give me a quick overview of the data assets in the SEA-AD challenge project with agentic track (syn66496696)?”*

- Get custom metadata of entities in Synapse

  - *“What are the annotations and metadata for file syn4553239?”*

  - *“Show me the custom metadata fields for dataset syn66364675”*

- Get provenance information for entities in Synapse to help understand past data processing

  - *“What's the processing history for file syn51543273?”*

  - *“Show me the data lineage and upstream dependencies for the dataset syn68719289”*

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/12614768-getting-started-with-claude-for-life-sciences)

Getting Started with Claude for Life Sciences

[](https://support.claude.com/en/articles/12614795-using-the-biorender-connector-in-claude)

Using the BioRender Connector in Claude

[](https://support.claude.com/en/articles/12614801-using-the-pubmed-connector-in-claude)

Using the PubMed Connector in Claude

[](https://support.claude.com/en/articles/12614810-using-the-benchling-connector-in-claude)

Using the Benchling Connector in Claude

[](https://support.claude.com/en/articles/12614815-using-the-scholar-gateway-connector-in-claude)

Using the Scholar Gateway Connector in Claude

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
