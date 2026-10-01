---
title: "Claude for Life Sciences \\ Anthropic"
source_url: "https://www.anthropic.com/news/claude-for-life-sciences"
category: "19-Reference"
fetched_at: "2026-08-28T09:23:09Z"
tags: ["news-research", "search", "skills"]
---

# Claude for Life Sciences

Oct 20, 2025

Increasing the rate of scientific progress is a core part of Anthropic’s public benefit mission.

We are focused on building the tools to allow researchers to make new discoveries – and eventually, to allow AI models to make these discoveries autonomously.

Until recently, scientists typically used Claude for individual tasks, like writing code for statistical analysis or summarizing papers. Pharmaceutical companies and others in industry also use it for tasks across the rest of their business, like sales, to fund new research. Now, our goal is to make Claude capable of supporting the entire process, from early discovery through to translation and commercialization.

To do this, we’re rolling out [several improvements](../18-Industry-UseCases/life-sciences.md) that aim to make Claude a better partner for those who work in the life sciences, including researchers, clinical coordinators, and regulatory affairs managers.

## Making Claude a better research partner

First, we’ve improved Claude’s underlying performance. Our most capable model, Claude Sonnet 4.5, is significantly better than previous models at a range of life sciences tasks. For example, on Protocol QA, a benchmark that tests the model’s understanding and facility with laboratory protocols, Sonnet 4.5 scores 0.83, against a human baseline of 0.79, and Sonnet 4’s performance of 0.74.¹ Sonnet 4.5 shows a similar improvement on its predecessor on BixBench, an evaluation that measures its performance on bioinformatics tasks.

To make Claude more useful for scientific work, we’re now adding several [new connectors](https://www.anthropic.com/04-API-Reference/Other/connectors-claude.md) to scientific platforms, the ability to use Agent Skills, and life sciences-specific support in the form of a prompt library and dedicated support.

## Connecting Claude to scientific tools

[**Connectors**](https://claude.ai/redirect/website.v1.bd9ffd4a-36b1-44b4-a428-f9aac5bf307a/settings/connectors) allow Claude to access other platforms and tools directly. We’re adding several new connectors that are designed to make it easier to use Claude for scientific discovery:

- **Benchling** gives Claude the ability to respond to scientists’ questions with links back to source experiments, notebooks, and records;
- **BioRender** connects Claude to its extensive library of vetted scientific figures, icons, and templates;
- **PubMed** provides access to millions of biomedical research articles and clinical studies;
- **Scholar Gateway developed by Wiley** provides access to authoritative, peer-reviewed scientific content within Claude to accelerate research discovery;
- **Synapse.org** allows scientists to share and analyze data together in public or private projects;
- **10x Genomics** allows researchers to conduct single cell and spatial analysis in natural language.

These connectors add to our existing set, which includes general purpose tools like Google Workspace and Microsoft SharePoint, OneDrive, Outlook, and Teams. Claude can also already work directly with Databricks to provide analytics for large-scale bioinformatics research, and Snowflake to search through large datasets using natural language questions.

## Developing skills for Claude

Last week, we released [Agent Skills:](skills.md) folders including instructions, scripts, and resources that Claude can use to improve how it performs specific tasks. Skills are a natural fit for scientific work, since they allow Claude to consistently and predictably follow specific protocols and procedures.

We’re developing a number of scientific skills for Claude, beginning with **`single-cell-rna-qc`** This skill performs quality control and filtering on single-cell RNA sequencing data, using [scverse](https://scverse.org/) best practices:

In addition to the skills we’re creating, scientists can build their own. For more information and guidance, including setting up custom skills, see [here](https://www.anthropic.com/99-Other/using-skills-in-claude-a1bdb5a95a.md).

## Using Claude for Life Sciences

Claude can be used for life sciences tasks like the following:

- **Research, like literature reviews and developing hypotheses:** Claude can cite and summarize biomedical literature and generate testable ideas based on what it finds.

- **Generating protocols**: With the Benchling connector, Claude can draft study protocols, standard operating procedures and consent documents.
- **Bioinformatics and data analysis**: Process and analyze genomic data with Claude Code. Claude can present its results in [slides, docs](create-files.md), or code notebook format.
- **Clinical and regulatory compliance**: Claude can draft and review regulatory submissions, and compile compliance data.

In addition, to help scientists get started quickly, we’re creating a [library of prompts](https://www.anthropic.com/01-Getting-Started/getting-started-with-claude-for-life-sciences.md) that should elicit best results on tasks like the above.

## Partnerships and customers

We’re providing hands-on support from dedicated subject matter experts in our Applied AI and customer-facing teams.

We’re also partnering with companies who specialize in helping organizations adopt AI for life sciences work. These include Caylent, Deloitte, Accenture, KPMG, PwC, Quantium, Slalom, Tribe AI, and Turing, along with our cloud partners, AWS and Google Cloud.

Many of our existing customers and partners have already been using Claude for a broad range of real-world scientific tasks:

> Claude, paired with internal knowledge libraries, is integral to Sanofi's AI transformation and used by most Sanofians daily in our Concierge app. We're seeing efficiency gains across the value-chain, while our enterprise deployment has enhanced how teams work. This collaboration with Anthropic augments human expertise to deliver life-changing medicines faster to patients worldwide.
>
> Emmanuel Frenehard  
> Chief Digital Officer, Sanofi

> AI in R&D works through an ecosystem. Anthropic brings the best technologies while prioritizing access, governance, and interoperability. Benchling is uniquely positioned to contribute. For over a decade, scientists have trusted us as their source of truth for experimental data and workflows. Now we're building AI that powers the next chapter of R&D.
>
> Ashu Singhal  
> Co-founder and President, Benchling

> Broad Institute scientists pursue the most ambitious questions in biology and medicine, creating tools to empower scientists everywhere. We're working with Manifold on Terra Powered by Manifold. AI agents built on Claude enable scientists to work at entirely new scale and efficiency, exploring scientific domains in previously impossible ways.
>
> Heather Jankins  
> Head of Data Science Platform, Broad Institute of MIT and Harvard

> 10x's single cell and spatial analysis capabilities traditionally required computational expertise. Now, with Claude, researchers perform analytical tasks—aligning reads, generating matrices, clustering, secondary analysis—through plain English conversation. This lowers the barrier for new users while scaling to meet the needs of advanced research teams.
>
> Serge Saxonov  
> Co-founder and CEO, 10x Genomics

> We see tremendous potential in Claude streamlining how we bring drugs to market. The ability to pull from clinical data sources and create GxP-compliant outputs will help us bring life-changing cancer therapies to patients faster while maintaining the highest quality standards. We see Claude powering AI applications across several major functions at our company.
>
> Hisham Hamadeh  
> Senior Vice President, Global Head of Data, Digital and AI, Genmab

> Healthcare analytics demands AI purpose-built for our industry's complexity and rigor. Komodo Health's partnership with Anthropic delivers transparent, auditable solutions designed for regulated healthcare environments. Together, we're enabling healthcare and life sciences teams to transform weeks-long analytical workflows into actionable intelligence in minutes.
>
> Arif Nathoo, MD  
> CEO and Co-founder, Komodo Health

> We've consistently been one of the first movers when it comes to document and content automation in pharma development. Our work with Anthropic and Claude has set a new standard — we're not just automating tasks, we're transforming how medicines get from discovery to the patients who need them.
>
> Louise Lind Skov  
> Director Content Digitalisation, Novo Nordisk

> Claude Code and partnership with Anthropic have been extremely valuable for developing Paper2Agent, our moonshot to transform passive research papers into interactive AI agents that can act as virtual corresponding authors and co-scientists.
>
> James Zou  
> Associate Professor, Stanford University

> At PwC, responsible AI is a trust imperative. We pair our deep sector insight with Claude's agentic intelligence to reimagine how clinical, regulatory, and commercial teams operate. Together, we're not just streamlining processes—we're elevating quality, accelerating discovery, and building systems where confidence scales alongside innovation.  
>
> Matt Wood  
> US and Global Commercial Technology and Innovation Officer, PwC

> Claude Code has become a powerful accelerator for us at Schrödinger. For the projects where it fits best, Claude Code allows us to turn ideas into working code in minutes instead of hours, enabling us to move up to 10x faster in some cases. As we continue to work with Claude, we are excited to see how we can further transform the way we build and customize our software.
>
> Pat Lorton  
> EVP, Chief Technology Officer, and Chief Operating Officer, Schrödinger

> When creating an AI agent for bioinformatics analyses, we focused on three key factors: top software development, life sciences alignment, and startup support. We evaluated half a dozen platforms, and Claude was the standout leader. We're excited to continue this collaboration and bring cutting-edge AI agents into biotech research.  
>
> Alfredo Andere  
> Co-Founder and CEO, Latch Bio

> At EvolutionaryScale, we’re building next-generation AI systems to model the living world. Anthropic’s frontier models accelerate our ability to reason about complex biological data and translate it into scientific insight, helping us push the boundaries of what’s possible in life science discovery.
>
> Sal Candido  
> Co-founder and Chief Technology Officer, EvolutionaryScale

> At Manifold, our mission is to power faster, leaner life sciences. Building with Claude has enabled us to develop AI agents that translate questions in the semantic space of scientists to execution in the technical space of specialized datasets and tools. Together, we’re transforming how life sciences R&D will happen in the years ahead.
>
> Sourav Dey PhD  
> Co-founder and Chief AI Officer, Manifold

> At FutureHouse, Claude helps power both our bioinformatics and literature analysis workflows. Claude is our model of choice for accurate figure analyses and orchestrating non-linear searches through the literature.
>
> Andrew White  
> Co-founder and Head of Science, FutureHouse

> Claude has been invaluable for Axiom as we build AI to predict drug toxicity. We've used billions of tokens in Claude Code for many PRs. Claude agents with MCP servers are core to our scientific work, directly querying databases to interpret, transform, and test data correlations, helping us identify the most useful features for predicting clinical drug toxicity.
>
> Alex Beatson  
> Co-founder, Axiom Bio

01 / 15

## Supporting the life sciences

In addition to the updates described above, we’re supporting life sciences research through our [AI for Science](ai-for-science-program.md) program. This program provides free API credits to support leading researchers working on high-impact scientific projects around the world.

Our partnerships with these labs helps us identify new applications for Claude, while helping scientists answer some of their most pressing questions. We continue to welcome [submissions](https://docs.google.com/forms/d/e/1FAIpQLSfwDGfVg2lHJ0cc0oF_ilEnjvr_r4_paYi7VLlr5cLNXASdvA/viewform) for project ideas.

Jonah Cool and Eric Kauderer-Abrams, who lead partnerships and R&D for Life Sciences at Anthropic, respectively, discuss this and other recent work below.

## Getting started

To learn more about Claude for Life Sciences or set up a demo with our team, see [here](https://claude.com/contact-sales/life-sciences).

[Claude for Life Sciences](../18-Industry-UseCases/life-sciences.md) is available through Claude.com and on the AWS Marketplace, with Google Cloud Marketplace availability coming soon.

#### Footnotes

¹ Protocol QA score (multiple choice format) with 10 shot prompting. For more, see our [Sonnet 4.5 System Card](https://assets.anthropic.com/m/12f214efcc2f457a/original/Claude-Sonnet-4-5-System-Card.pdf), pages 132-133.


## Related content

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](model-hardware-standard-research-preview.md)

### Expanding our support for scientists

Starting today, 10,000 scientists around the world can get Claude at no cost to start. Verified principal investigators qualify for a Claude Team subscription plan and then add their research team to Standard seats for free, or Premium seats for \$15 per month, for up to a year.

[Read more](expanding-support-for-scientists.md)

### Funding better evaluations of AI’s impact on wellbeing

We’re launching a \$5 million grant program to fund independent research into how AI impacts users’ wellbeing.

[Read more](wellbeing-research-grants.md)

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](https://www.anthropic.com/15-Claude-AI-Features/claude-opus-4-6-anthropic.md)
- [Sonnet](https://www.anthropic.com/15-Claude-AI-Features/claude-sonnet-4-6-anthropic.md)
- [Haiku](https://www.anthropic.com/15-Claude-AI-Features/claude-haiku-4-5-anthropic.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../18-Industry-UseCases/enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud-vertex-ai.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://academy.claude.com)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Research Labs](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Leadership](company-leadership.md)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](anthropic-com-research.md)
- [News](news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](../15-Claude-AI-Features/claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
