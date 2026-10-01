---
title: "Claude Science, an AI workbench for scientists \\ Anthropic"
source_url: "https://www.anthropic.com/news/claude-science-ai-workbench"
category: "19-Reference"
fetched_at: "2026-09-10T06:43:58Z"
tags: ["news-research"]
---

# Claude Science, an AI workbench for scientists, is now available

Jun 30, 2026

[Get started with Claude Science](../15-Claude-AI-Features/product-claude-science.md)

AI has the potential to dramatically accelerate the pace of scientific discovery and the development of healthcare interventions. Since launching our efforts in the life sciences last fall, we’ve worked to improve our model capabilities, make connections to the scientific ecosystem via MCPs and skills, and launch partnerships in an effort to realize this potential.

Today, we’re introducing our most significant expansion of these efforts: [Claude Science](http://claude.com/science), an AI workbench for scientists. Claude Science is an app that integrates the tools and packages that researchers most commonly use, produces auditable artifacts, and provides flexible access to computing resources.

## Introducing Claude Science

Scientific research is often tedious. Researchers must work across dozens of databases, each with their own schema, contend with file formats that require bespoke data pipelines and viewers, and transition between a roster of tools: PubMed, Jupyter, R, a cluster terminal, and more.

Claude Science brings these fragmented tools into a single research environment where scientists can conduct all stages of their work. It helps you analyze literature and execute multi-step research, produces detailed artifacts, and lets you iteratively refine figures and manuscripts until they’re ready for publication. Every output carries an auditable history of how it was made, so you can validate and reproduce the results. Like a Jupyter Notebook, you can access Claude Science wherever you already work—locally on macOS or Linux, or on a remote machine over SSH or with an HPC login node.

Users interact with a generalist coordinating agent with access to over 60 curated skills and connectors pre-configured for genomics, single-cell, proteomics, structural biology, cheminformatics, and more. These agents can spin up others and engage with specialist agents created by users. And a reviewer agent checks citations and calculations, flagging and correcting errors.

We are releasing Claude Science today in beta for Claude Pro, Max, Team, and Enterprise users, and will continue to refine the platform as we collect feedback from users.

## **How it works**

**Rich scientific artifacts, fully reproducible.** Scientific research is inherently visual, so Claude Science generates figures and manuscripts alongside the code that created them. It natively renders rich scientific artifacts, including 3D protein structures, genome browser tracks, chemical structures, and more. You can chat with the agent about any detail, annotating figures and manuscripts in-line so the agent knows what to address to make them publication-ready.

When it generates a figure, Claude Science includes the exact code and environment that produced it, a plain-language description of how it was created, and the full message history. This allows you to understand the inputs, making the work easier to validate and reproduce even months later. You can ask Claude Science to make edits to figures in plain language—removing gridlines, for example, or changing an axis to log scale—and the agent will edit its own code.

**Manages your compute and scales on demand.** Large analyses—folding a protein, for example, or running a genomics pipeline over a massive dataset—often require researchers to shift their focus to setting up a computing job, waiting while it’s sent to a cluster, checking whether it succeeded or failed, and pulling the results back. Claude Science handles this process for you. It drafts a plan, asks before reaching new resources, and lets you review or revoke any decision before writing and submitting the job to the computing resources your lab already uses (your own HPC cluster over SSH, or your Modal account for compute on demand), scaling the analysis from a single GPU to hundreds as needed.

Because its agents work inside a running session that holds context in memory, even massive datasets only need to be loaded once. It runs on your lab’s own infrastructure—your laptop, Linux box, or HPC login node—so large or sensitive datasets never have to leave the systems they’re already on, and only the context needed for each step of the analysis is sent to Claude. As the pipeline runs, a reviewer agent inspects the outputs, flagging incorrect citations, untraceable numbers, and figures that don’t match their underlying code, and self-correcting as it goes. You can fork the session at any point to compare two approaches without losing the original thread.

**Domain-ready on day one**. Scientific knowledge is scattered across hundreds of specialized sources. In biology, for example, relevant data might sit across resources such as UniProt, PDB, Ensembl, Reactome, ClinVar, ChEMBL, GEO—each with its own schema and query language—as well as in journals and preprint servers, and domain-specific open models. When you ask Claude Science a question in plain language, specialist agents query and synthesize across all of these sources so you don’t have to navigate them individually. Claude Science uses the skills in NVIDIA’s [BioNeMo Agent Toolkit](https://nvidianews.nvidia.com/news/nvidia-launches-bionemo-agent-toolkit-giving-ai-agents-the-tools-to-accelerate-scientific-discovery) to connect natively to the life sciences models and libraries in [BioNeMo](https://github.com/NVIDIA-BioNeMo), including Evo 2, Boltz-2, and OpenFold3.

Scientists already have models, datasets, and pipelines they trust. Claude Science can connect to these as well, saving any pipeline as a reusable skill or accessing your lab’s preferred tool using a connector, with future sessions inheriting them automatically. This customizability allows you to access Claude, your proprietary data, and the validated tools you already rely on in one conversation. Claude Science benefits from our partners’ specialized expertise and platforms, while more scientists reach their tools through Claude.

## What scientists are doing with Claude Science

Over the past few months, researchers have worked with Claude Science in beta for tasks like single-cell RNA sequencing analysis, CRISPR screen design, protein structure prediction, cheminformatics, and more.

Manifold Bio designs tissue-targeting medicines—which home to a specific organ or cell type, so the drug acts where it’s needed and spares the rest of the body—and tests how millions of candidate binders corresponding to hundreds of targets distribute through a living body at once. Manifold used Claude Science to nominate the targets for its latest experiments. For each tissue and target, Claude Science assessed surface expression, trafficking, and safety, ranking candidates against the criteria Manifold has learned from its own internal proprietary data. What set Claude Science apart from a general coding assistant, Manifold said, was that it could do this end-to-end, gathering the right data and applying the right judgment with the context of past programs built in.

Jérôme Lecoq, a neuroscientist at the Allen Institute, used Claude Science to build a multi-agent “computational review template” comprising about 20 custom skills geared towards writing long-form reviews. The sub-agents read through thousands of papers, pulling the central claim and the key quantitative finding, and storing them in an evidence state database. Then the pipeline constructs a narrative arc, writing the review section by section and delegating each to its own specialized sub-agent. Within each section, dedicated agents generate quantitative cross-study figures directly from the evidence database. A key component of the workflow, enabled by Claude Science, is the use of actor-critic pairs: one agent creates content while a separate reviewer agent evaluates it for accuracy and citation fidelity.

Before Claude Science, it could take Lecoq’s team as many as two years to write such a review. He now has about 10 reviews, many more than 100 pages, with citations that were checked over by reviewer agents. The team is now working with domain experts to further refine the AI-based critic agents.

And Stephen Francis, an associate professor and epidemiologist at the UCSF Brain Tumor Center, has used Claude Science to support studies on the molecular epidemiology of glioma, a type of primary tumor that begins in the glial cells of the brain. His lab investigates the genetic basis for how thousands of small-effect germline variants combine to shape individual susceptibility. Although this work predated Claude Science, Francis said the app has dramatically accelerated the analysis, enabling comprehensive germline workups across multiple approaches in roughly one-tenth the time it previously took. His group independently validated Claude Science’s results, confirming that it can produce both rapid and robust analyses.

## Getting started with Claude Science

The [Claude Science](http://claude.com/science) app is available in beta on macOS and Linux for Pro, Max, Team, and Enterprise plans. We’re sharing it early so scientists can start to use it on real problems and tell us how to refine it.

Team and Enterprise users will need their admin to enable Claude Science. We now have a Team plan offering discounted seats for active scientific labs at academic institutions and nonprofit research organizations; [learn more here](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md).

We’ll also be supporting up to 50 Claude Science AI for Science projects, providing up to \$30,000 in credits. Modal will also [be providing up to \$2,000 in compute](https://modal.com/blog/modal-integration-brings-scalable-compute-to-claude-science) for select projects. We are looking for projects that span domains and explore the boundaries of science, with an early focus on biology and biomedical research. Applications are open through July 15, 2026, with award notifications sent out by July 31. Projects will run from September 1 to December 1, 2026—[apply here](https://docs.google.com/forms/d/e/1FAIpQLSfwDGfVg2lHJ0cc0oF_ilEnjvr_r4_paYi7VLlr5cLNXASdvA/viewform?usp=dialog).

To stay up-to-date on product announcements, provide feedback, and learn from others in the Claude Science community, join the [AI for Science Discourse community](https://ai4science.discourse.group/invites/UjrKZKwxK3).

Get started with Claude Science at [claude.com/science](http://claude.com/science).


## Related content

### Developing Enterprise Frontier Safeguards with our customers

[Read more](enterprise-frontier-safeguards.md)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](improving-alignment-security-efforts.md)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](model-hardware-standard-research-preview.md)

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
- [Commerce](../18-Industry-UseCases/commerce.md)
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
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

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
