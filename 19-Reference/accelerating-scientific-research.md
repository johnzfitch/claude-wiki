---
title: "How scientists use Claude to accelerate research \\ Anthropic"
source_url: "https://www.anthropic.com/news/accelerating-scientific-research"
category: "19-Reference"
fetched_at: "2026-09-10T06:46:07Z"
tags: ["agents", "news-research", "search", "testing"]
---

# How scientists are using Claude to accelerate research and discovery

Jan 15, 2026

Last October we launched Claude for Life Sciences—a suite of connectors and skills that made Claude a better scientific collaborator. Since then, [we've invested heavily in making Claude the most capable model for scientific work](healthcare-life-sciences.md#tab-media-0), with Opus 4.5 showing significant improvements in figure interpretation, computational biology, and protein understanding benchmarks. These advances, informed by our partnerships with researchers in academia and industry, reflect our commitment to understanding exactly how scientists are using AI to accelerate progress.

We’ve also been working closely with scientists through our [AI for Science](ai-for-science-program.md) program, which provides free API credits to leading researchers working on high-impact scientific projects around the world.

These researchers have developed custom systems that use Claude in ways that go far beyond tasks like literature reviews or coding assistance. In the labs we spoke to, Claude is a collaborator that works across all stages of the research process: making it easier and more cost-effective to understand which experiments to run, using a variety of tools to help compress projects that normally take months into hours, and finding patterns in massive datasets that humans might overlook. In many cases it’s eliminating bottlenecks, handling tasks that require deep knowledge and have previously been impossible to scale; in some it’s enabling entirely different research approaches than researchers have traditionally been able to take.

In other words, Claude is beginning to reshape how these scientists work—and point them towards novel scientific insights and discoveries.

## Biomni: a general-purpose biomedical agent with access to hundreds of tools and databases

One bottleneck in biological research is the fragmentation of tools: there are hundreds of databases, software packages, and protocols available, and researchers spend substantial time selecting from and mastering various platforms. That’s time that, in a perfect world, would be spent on running experiments, interpreting data, or pursuing new projects.

[Biomni](https://biomni.stanford.edu/), an agentic AI platform from Stanford University, collects hundreds of tools, packages, and data-sets into a single system through which a Claude-powered agent can navigate. Researchers give it requests in plain English; Biomni automatically selects the appropriate resources. It can form hypotheses, design experimental protocols, and perform analyses across more than 25 biological subfields.

Consider the example of a genome-wide association study (GWAS), a search for genetic variants linked to some trait or disease. Perfect pitch, for instance, has a strong genetic basis. Researchers would take a very large group of people—some who are able to produce a musical note without any reference tone, and others you would never invite to karaoke—and scan their genomes for genetic variants that show up more often in one group than another.

The genome scanning is (relatively) simple. It’s the process of analyzing and making sense of the data that’s time-consuming: genomic data comes in messy formats and needs extensive cleaning; researchers must control for confounding and deal with missing data; once they identify any “hits,” they need to figure out what they actually mean—what gene is nearby (since GWAS only points to locations in a genome), what cell types it’s expressed in, what biological pathway it might affect, and so on. Each step might involve different tools, different file formats, and a lot of manual decision-making. It’s a tedious process. A single GWAS can take months. But in an early trial of Biomni, it took 20 minutes.

This might sound too good to be true—can we be sure of the accuracy of this kind of AI analysis? The Biomni team has [validated](https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1.full.pdf) the system through several case studies in different fields. In one, Biomni designed a molecular cloning experiment; in a blind evaluation, the protocol and design matched that of a postdoc with more than five years of experience. In another, Biomni analyzed the data from over 450 wearable data files from 30 different people (a mix of continuous glucose monitoring, temperature, and physical activity) in just 35 minutes—a task estimated to take a human expert three weeks. In a third, Biomni analyzed gene activity data from over 336,000 individual cells taken from human embryonic tissue. The system confirmed regulatory relationships scientists already knew about, but also identified new transcription factors—proteins that control when genes turn on and off—that researchers hadn’t previously connected to human embryonic development.

Biomni isn’t a perfect system, which is why it includes guardrails to detect if Claude has gone off-track. Nor can it yet do everything out of the box. However, where it comes up short, experts can encode their methodology as a [skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-overview.md)—teaching the agent how an expert might approach a problem, rather than letting it improvise. For example, when working with the Undiagnosed Diseases Network on rare disease diagnosis, the team found that Claude's default approach differed substantially from what a clinician would do. So they interviewed an expert, documented their diagnostic process step by step, and taught it to Claude. With that new, previously-tacit knowledge, the agent performed well.

Biomni represents one approach: a general-purpose system that brings hundreds of tools under one roof. But other labs are building more specialized systems—targeting specific bottlenecks in their own research workflows.

## Cheeseman Lab: automating the interpretation of large-scale gene knockout experiments

When scientists want to understand what a gene does, one approach is to remove it from the cell or organism in question and see what breaks. The gene-editing tool CRISPR, which emerged around 2012, made this easy to do precisely at scale. But the utility of CRISPR was still limited: labs could generate far more data than they had the bandwidth to analyze.

This is exactly the challenge faced by Iain Cheeseman’s [lab](https://cheesemanlab.wi.mit.edu/) at the Whitehead Institute and Department of Biology at MIT. Using CRISPR, they knock out thousands of different genes across tens of millions of human cells, then photograph each cell to see what changed. The patterns in those images reveal that genes that do similar jobs tend to produce similar-looking damage when removed. Software can detect these patterns and group genes together automatically—Cheeseman's lab built a pipeline to do exactly this called [Brieflow](https://www.biorxiv.org/content/10.1101/2025.05.26.656231v1) (yes, brie the cheese).

But interpreting what these gene groupings mean—why the genes cluster together, what they might have in common, whether it’s a known biological relationship or something new—still requires a human expert to comb through the scientific literature, gene by gene. It’s slow. A single screen can produce hundreds of clusters, and most never get investigated simply because labs don’t have the time, bandwidth, or in-depth knowledge about the diverse things that cells do.

For years, Cheeseman did all the interpretation himself. He estimates he can recall the function of about 5,000 genes off the top of his head, but it still takes hundreds of hours to analyze this data effectively. To accelerate this process, PhD student Matteo Di Bernardo sought to build a system that would automate Cheeseman’s approach. Working closely with Cheeseman to understand exactly how he approaches interpretation—what data sources he consults, what patterns he looks for, what makes a finding interesting—they built a Claude-powered system called [MozzareLLM](https://github.com/cheeseman-lab/mozzarellm) (you might be seeing a theme developing here).

It takes a cluster of genes and does what an expert like Cheeseman would do: identifies what biological process they might share, flags which genes are well-understood versus poorly studied, and highlights which ones might be worth following up on. Not only does this substantially accelerate their work, but it is also helping them make important additional biological discoveries. Cheeseman finds Claude consistently catches things he missed. “Every time I go through I’m like, I didn’t notice that one! And in each case, these are discoveries that we can understand and verify,” he says.

What helps make MozzareLLM so useful is that it isn’t a one-trick pony: it can incorporate diverse information and reason like a scientist. Most notably, it provides confidence levels in its findings, which Cheeseman emphasizes is crucial. It helps him decide whether or not to invest more resources in following up on its conclusions.

In building MozzareLLM, Di Bernardo tested multiple AI models. Claude outperformed the alternatives—in one case correctly identifying an RNA modification pathway that other models dismissed as random noise.

Cheeseman and Di Bernardo envision making these Claude-annotated datasets public—letting experts in other fields follow up on clusters his lab doesn't have time to pursue. A mitochondrial biologist, for instance, could dive into mitochondrial clusters that Cheeseman's team has flagged but never investigated. As other labs adopt MozzareLLM for their own CRISPR experiments, it could accelerate the interpretation and validation of genes whose functions have remained uncharacterized for years.

## Lundberg Lab: testing AI-led hypothesis generation for which genes to study

The Cheeseman lab uses optical pooled screening—a technique that lets them knock out thousands of genes in a single experiment. Their bottleneck is interpretation. But not every cell type works with pooled approaches. Some labs, such as the [Lundberg Lab at Stanford](https://lundberglab.stanford.edu/), run smaller, focused screens, and their bottleneck comes earlier: deciding which genes to target in the first place.

Because a single focused screen can cost upwards of \$20,000 and costs increase with size, labs typically target a few hundred genes they think are *most likely* to be involved in a given condition. The conventional process involves a team of grad students and postdocs sitting around a Google spreadsheet, adding candidate genes one by one with a sentence of justification, or maybe a link to a paper. It's an educated guessing game, informed by literature reviews, expertise, and intuition, but constrained by human bandwidth. It’s also fallible, based as it is on what other scientists already figured out and written down, and what the humans in the room happen to recall.

The Lundberg Lab is using Claude to flip that approach. Instead of asking “what guesses can we make based on what researchers have already studied?”, their system asks “what *should* be studied, based on molecular properties?”

The team built a map of every known molecule in the cell—proteins, RNA, DNA—and how they relate to each other. They mapped out which proteins bind together, which genes code for which products, and which molecules are structurally similar. They can then give Claude a target—for instance which genes might govern a particular cellular structure or process—and Claude navigates that map to identify candidate genes based on their biological properties and relationships.

The Lundberg lab is currently running an experiment to study how well this approach works. To do so, they needed to identify a topic where very little research had been done (if they’d looked at something well-studied, Claude might already know about the established findings). They chose primary cilia: antenna-like appendages on cells that we still know little about but which are implicated in a variety of developmental and neurological disorders. Next, they’ll run a whole genome screen to see which genes actually affect cilia formation, and establish the ground-truth.

The test is to compare human experts to Claude. The humans will use the spreadsheet approach to make their guesses. Claude will generate its own using the molecular relationship map. If Claude catches (hypothetically) 150 out of 200, and the humans catch 80 out of 200, that's proof the approach works better. Even if they're about equal in discovering the genes, it’s still likely Claude works much faster, and could make the whole research process more efficient.

If the approach works, the team envisions it becoming a standard first step in focused perturbation screening. Instead of gambling on intuition or using brute-force approaches that have become prevalent in contemporary research, labs could make informed bets about which genes to target—getting better results without needing the infrastructure for whole-genome screening.

### Looking forward

None of these systems are perfect. But they point to the ways that in just a few short years scientists have begun to incorporate AI as a research partner capable of far more than basic tasks—indeed, increasingly able to speed up, and in some cases even replace, many different aspects of the research process.

In speaking with these labs, a common theme emerged: the usefulness of the tools they’ve built continues to grow in concert with AI capabilities. Each model release brings noticeable improvements. Where just two years ago earlier models were limited to writing code or summarizing papers, more powerful agents have begun, if slowly, to replicate the very work those papers describe.

As tools advance and AI models continue to grow more intelligent, we’re continuing to watch and learn from how scientific discovery develops along with them.

*For more detail on the expanded Claude for Life Sciences capabilities, [see here](../18-Industry-UseCases/life-sciences.md), and our [tutorials here](https://claude.com/resources/tutorials-category/life-sciences). We’re also continuing to accept [applications](https://docs.google.com/forms/d/e/1FAIpQLSfwDGfVg2lHJ0cc0oF_ilEnjvr_r4_paYi7VLlr5cLNXASdvA/viewform) to our AI for Science program. Applications will be reviewed by our team, including subject matter experts in relevant fields.*


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
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

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
