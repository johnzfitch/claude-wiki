---
category: "15-Claude-AI-Features"
fetched_at: "2026-03-12T08:19:48Z"
source_url: "https://support.claude.com/en/articles/12614803-using-the-10x-genomics-extension-in-claude"
title: "Using the 10x Genomics Extension in Claude | Claude Help Center"
---

3.  Using the 10x Genomics Extension in Claude

# Using the 10x Genomics Extension in Claude


The 10x Genomics integration transforms single cell and spatial analysis into a simple, conversational workflow. Biologists can easily analyze their own sequencing data, while core labs can quickly perform batch processing. This article explains how to set up and use the 10x Genomics integration with Claude to advance your analysis workflows.

The 10x Genomics integration is available as a desktop extension in the Claude Desktop App ([download here](https://claude.ai/download)), and it relies upon Claude's ability to use [local connectors via a desktop extension](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop).

## What this integration provides

The 10x Genomics integration enables researchers to create and manage single cell genomics analysis workflows in conversation with Claude. Users can upload data, configure and launch Cell Ranger pipelines, monitor analysis status, and download results using natural language prompts instead of command-line tools or web interfaces. The integration translates conversational requests into actions on the 10x Cloud Analysis platform, streamlining workflows for gene expression, cell multiplexing, and CRISPR screening analyses.

## Who should use the 10x Genomics integration

- **Computational Biologists:** Researchers who analyze single cell genomics data and want to streamline cloud-based analysis workflows

- **Bioinformaticians:** Scientists who process multiple samples and need efficient batch processing capabilities

- **Research Scientists:** Lab researchers who generate single cell data and want an intuitive interface for running standard pipelines

- **Core Facility Managers:** Staff who process samples for multiple research groups and need to manage numerous analyses

## Who can access the 10x Genomics integration

Any user with a 10x Cloud Analysis account ([create a free account here](https://www.10xgenomics.com/products/cloud-analysis))

More details on accessing the integration can be found in the [10x Genomics MCP Server Documentation](https://www.10xgenomics.com/support/software/cloud-analysis/latest/tutorials/cloud-mcp-server).

## Setting up the 10x Genomics integration

The 10x Genomics integration is available as a desktop extension in the Claude Desktop App ([download here](https://claude.ai/download)). For Organization Owners (Team and Enterprise), setting up the integration involves making the extension available to your organization. For individual users, setting up the integration involves installing the extension from inside the Claude Desktop App.

**For Organization Owners (Team and Enterprise)**

1.  Navigate to Organization settings \> Extensions

2.  In the search field, type “10x Genomics”

3.  Click “Enable”

4.  Instruct your team to download the [Claude Desktop App](https://claude.ai/download) to access the integration

**For Individual Claude Users**

1.  Download the [Claude Desktop App](https://claude.ai/download)

2.  Navigate to Settings \> Extensions

3.  Click “Browse extensions”

4.  Click “10x Genomics”

5.  Click “Install”

6.  Follow the instructions to authenticate with your 10x Cloud Analysis account

Learn about [installing desktop extensions from the directory](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop).

Technical details of the 10x Genomics integration can be found in the [10x Genomics MCP Server Documentation](https://www.10xgenomics.com/support/software/cloud-analysis/latest/tutorials/cloud-mcp-server).

**For Claude Code Users**

1.  Command: `/plugin marketplace add anthropics/life-sciences`

2.  Command: `/plugin install 10x-genomics@life-sciences`

3.  Restart Claude Code

4.  Command: `/plugin`

5.  Navigate to “Manage and uninstall plugins" and configure the 10x Genomics MCP with your access token

6.  Restart Claude Code one more time

7.  Verify that the server is connected with `/mcp`

## Common use cases

- Set up a Cell Ranger count analysis

- Set up a Cell Ranger multi analysis with multiplexing

- Batch process multiple samples

- Monitor and download analysis results

- Interpret QC metrics and results

Sample prompts and prompting best practices can be found in the [10x Genomics MCP Server Documentation](https://www.10xgenomics.com/support/software/cloud-analysis/latest/tutorials/cloud-mcp-server).

## More resources from 10x Genomics

- [10x Cloud Analysis support](https://www.10xgenomics.com/support/software/cloud-analysis/latest)

- [Cell Ranger documentation](https://www.10xgenomics.com/support/software/cell-ranger/latest)

- [10x Genomics MCP Server Documentation](https://www.10xgenomics.com/support/software/cloud-analysis/latest/tutorials/cloud-mcp-server)

------------------------------------------------------------------------

Related Articles


Installing Claude Desktop


Getting Started with Local MCP Servers on Claude Desktop


Getting Started with Claude for Life Sciences


Using the BioRender Connector in Claude


Using the Synapse.org connector in Claude
