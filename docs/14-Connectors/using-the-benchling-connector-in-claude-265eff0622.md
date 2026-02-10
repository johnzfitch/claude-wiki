---
category: "14-Connectors"
source_url: "https://support.claude.com/en/articles/12614810-using-the-benchling-connector-in-claude"
---


The Benchling connector links Claude to Benchling R&D platform data, enabling scientists to ask questions and receive clear summaries with links back to source experiments, notebooks, and structured records—all while maintaining existing access permissions. This article explains how to set up and use the Benchling integration with Claude to advance your R&D workflows.

 

The Benchling integration relies upon Claude's ability to use remote connectors.

 

What this connector provides

When Claude sends a query to Benchling, it can search across the full breadth of a customer’s Benchling environment. This covers experimental results and study data, notebook content such as text and attachments, and structured records like registry items, inventory, and templates. The Benchling integration brings these different data types together to provide a unified answer, saving scientists from having to manually piece information across entries or projects. You can also choose to pull in public literature sources, combining internal and external knowledge in one place. All results follow the same access permissions already set in Benchling, ensuring people only see the data they are meant to.

 

Who should use the Benchling connector

Bench Scientists & Research Associates - want to quickly find and summarize the right data, whether from Benchling or external sources, and use it to decide on next steps in their experiments.

Team Leads & Project Managers - need concise summaries of ongoing work and alignment with external findings to guide project planning.

Computational Biologists & Informatics Teams - want to ask governance questions and assemble curated datasets from Benchling that can be used for deeper analysis or shared across teams.

Program Leads - need automatically generated reports that combine Benchling study results with external context or public data, giving them a clear view of progress and next steps.

R&D Leaders & Executives - require portfolio-level insights to spot trends across programs and benchmark against public industry data.

 

Who can access the Benchling connector

Benchling customers who meet the following criteria:

Benchling AI (Deep Research) enabled in your tenant

API access (V3 APIs, including AI Agents endpoint)

Benchling remote MCP enabled for your tenant

No additional setup is required beyond connecting Claude to the Benchling connector and authenticating with your Benchling login credentials.

 

More details on accessing the integration can be found in Benchling’s MCP Server Documentation.

 

Setting up the Benchling connector

For Organization Owners (Team and Enterprise)

Navigate to Admin settings > Connectors.

Click "Browse connectors"

Click “Benchling”

Click “Add to your team”

Get a Server URL from Benchling by clicking the link provided

Paste the Server URL into field provided

Click “Continue”

For Individual Claude Users

Navigate to Settings > Connectors.

Click “Connect”

Follow the instructions to authenticate with your Benchling account

Learn about finding and connecting tools in Claude.

 

Technical details of the Benchling integration can be found in Benchling’s MCP Server Documentation.

 

Example Use Cases

Cross-Source Comparison: “Compare the IC50 results from my last two Benchling experiments with recent PubMed articles on AAV stability.”

Insight Summarization: “Summarize the key findings from Benchling experiments and highlight how they align with external literature trends.”

Recommendations: “Based on our last three in vivo results in Benchling and recent FDA guidance, what should we test next?”

Portfolio Insights: “Aggregate results from our top five Benchling programs and highlight which ones are showing the strongest early efficacy signals compared with industry benchmarks.”

Related Articles
Getting Started with Claude for Life Sciences
Using the Synapse.org Connector in Claude
Using the 10x Genomics Extension in Claude
Using the Scholar Gateway Connector in Claude
Using Interactive Connectors in Claude