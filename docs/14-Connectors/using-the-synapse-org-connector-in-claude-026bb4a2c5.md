---
category: "14-Connectors"
source_url: "https://support.claude.com/en/articles/12614798-using-the-synapse-org-connector-in-claude"
---


The Synapse.org integration by Sage Bionetworks allows researchers to discover biomedical data across all of Synapse, see the structure of projects, and retrieve information on their data assets for authorized users. This article explains how to set up and use the Synapse.org integration with Claude to advance your research and analysis workflows.

 

The Synapse.org integration relies upon Claude's ability to use remote connectors.

 

What this integration provides

Services include search and (meta)data retrieval services. Data access will be governed by the access controls defined for each project. Some data are publicly available, while others require approval from Synapse’s governance team prior to access.

 

Who can access the Synapse.org integration

Individuals who have a registered Synapse account (register for free)

Data access may be subject to use restriction from contributors

More details on accessing the integration can be found in Synapse’s MCP Server Documentation.

 

Setting up the Synapse.org integration

For Organization Owners (Team and Enterprise)

Navigate to Admin settings > Connectors

Click "Browse connectors"

Click “Synapse.org”

Click “Add to your team”

For Individual Claude Users

Navigate to Settings > Connectors

Click “Connect”

Follow the instructions to authenticate with your Synapse.org account

Learn about finding and connecting tools in Claude.

 

For Claude Code Users

Command: /plugin marketplace add anthropics/life-sciences

Command: /plugin install synapse@life-sciences

Restart Claude Code

Verify that the server is connected with /mcp

Technical details of the Synapse.org integration can be found in Synapse’s MCP Server Documentation.

 

Common use cases

Search for reusable scientific data across all of the Synapse.org platform

“Find RNA-seq datasets related to Alzheimer's disease in Synapse”

“Search Synapse for single-cell transcriptomics datasets”

"Find genomic sequencing data for plexiform neurofibromas in the NF Data Portal”

Authorized users can see hierarchy of folders, files, tables, datasets within projects to help organize and monitor data assets

“Explain the files and folders in the public AACR Project GENIE project”

“Give me a quick overview of the data assets in the SEA-AD challenge project with agentic track (syn66496696)?”

Get custom metadata of entities in Synapse

“What are the annotations and metadata for file syn4553239?”

“Show me the custom metadata fields for dataset syn66364675”

Get provenance information for entities in Synapse to help understand past data processing

“What's the processing history for file syn51543273?”

“Show me the data lineage and upstream dependencies for the dataset syn68719289”

 

Related Articles
Using the BioRender Connector in Claude
Using the PubMed Connector in Claude
Using the Benchling Connector in Claude
Using the Scholar Gateway Connector in Claude
Using Interactive Connectors in Claude