---
title: "AI for Science rare disease research grants \\ Anthropic"
source_url: "https://www.anthropic.com/news/rare-disease-research-grants"
category: "19-Reference"
fetched_at: "2026-09-10T06:45:56Z"
tags: ["news-research", "search"]
---

# Apply for Anthropic’s AI for Science rare disease research grants

Jul 20, 2026

Last spring, we announced [Anthropic’s AI for Science program](ai-for-science-program.md), an initiative designed to accelerate scientific research and discovery through access to our API. Since launching, we have supported researchers working on a variety of high-impact projects, ranging from drug repurposing to quantum simulation. Throughout this initiative, we have found that projects are more generative when multiple AI for Science grantees are working on related questions and exchanging tips. So we now plan to launch thematic calls for projects within the broader AI for Science program.

Today, we are sharing a focused call for applications centered specifically on rare genetic diseases. Accepted applicants will receive up to \$50,000 in Claude credits over six months, with the goal of building a community of researchers looking into how AI can reshape our understanding of rare disease. This program has two tracks: one for scientists doing basic research, and another for early-stage biotechs working on speeding up clinical development for rare diseases.

Rare disease research is an area where knowledge of fundamental science is limited. In aggregate, rare diseases are among the most prevalent conditions on the planet (an estimated 400 million people live with one of [more than 7,000 rare diseases](https://pmc.ncbi.nlm.nih.gov/articles/PMC11881545/)).¹ But these conditions are scattered across small populations, making it challenging for clinicians to build patient registries, identify promising therapeutic targets, and design clinical trials. Moreover, rare diseases are typically characterized by their unique features (such as a specific genetic variation or combination of symptoms) that are often studied in isolation, making it nearly impossible to spot mechanisms shared across diseases. Finally, rare diseases face a challenge endemic to all drug development: the time it takes to move promising drug candidates into patient trials.

We think AI can help with these and related challenges. AI makes it possible to accurately model rare genetic diseases and detect patterns across them. It also helps researchers synthesize findings across a large corpus of literature, quickly extract information from limited datasets, and create shared terminology, all of which informs how researchers can better use the information they *do* have, even as more work is done to generate more data and address challenges pertaining to access and geography. To explore where AI can be most helpful, we’ve made rare diseases the focus of our current call for AI for Science projects.

### **Track one: Scaling our basic science partnerships**

The first track of our rare disease research grants program aims to foster collaboration between clinical researchers, patient organizations, and data scientists to increase the pace of progress in basic science and the discovery of the mechanisms underlying rare diseases.

An early partner in this effort is the Monarch Initiative, an international consortium working to improve diagnosis and mechanism discovery for patients with rare diseases. Monarch develops standards and resources such as the [Mondo Disease Ontology](http://mondo.monarchinitiative.org/), a computational framework and coding system that reconciles disease definitions scattered across OMIM, Orphanet, ICD, and dozens of other sources; as well as the [Monarch Knowledge Graph](https://monarchinitiative.org/kg/about), which integrates genotype-phenotype data across species to aid diagnostics and mechanism discovery.

Most recently, Monarch contributors have been stitching data and knowledge together in a new agent-friendly mechanistic disease classification library called [DisMech](https://github.com/monarch-initiative/dismech), where Claude can read case reports, variant databases, registry schemas, raw public data, and more, and point out mechanistic similarities between diseases at an unmatched pace and scale. Monarch is inviting our AI for Science grantees to use and contribute to its resources, such as Mondo and DisMech, to reveal new mechanistic hypotheses that will support developing treatments.

Monarch’s work on improving the interoperability of rare disease data and knowledge is a place where Claude can already have a major impact. However, there’s more work to be done to gather better and more data, improve diagnostic infrastructure, and promote patient-led approaches across the rare disease ecosystem, and make the information accessible to agentic science. We will continue to partner with Monarch and others to approach this problem from the angles where AI is less obviously applicable, and we’ll share what we learn as we do.

### **Track two: Scaling our biotech partnerships**

The second track of our rare disease research grants program will support biotechnologists and early-stage biotechs working to accelerate drug development for rare diseases. Today, it takes [one to two years](https://www.nejm.org/doi/full/10.1056/NEJMoa1813279) to move from a confirmed genetic diagnosis to a treatment available to patients, with much of this time spent waiting in queues for certified manufacturing slots, running safety studies sequentially instead of in parallel, and hand-assembling the thousands of pages of chemistry and regulatory documentation required for in-patient testing.

We think it is possible to radically compress phases of this process with Claude—in particular, by making it easier to complete documentation (for example, drafting and reviewing the regulatory dossier), but also by speeding up therapeutic strategy selection (for example, by analyzing whether a target is druggable across a suite of modalities, such as small molecules, antibodies, genetic medicines, and so on) and looking for shared mechanisms across individual genetic therapies, which could allow them to be approved under a single “[basket trial](https://mrctcenter.org/glossaryterm/basket-trial/)” instead of requiring a separate IND for each patient.

Although many aspects of drug development are difficult to expedite because of manufacturing constraints or safety testing, we believe much can be done to move more quickly. By granting API credits and [Claude Science](claude-science-ai-workbench.md) access to the many biotechnologists and startups working in this space, we hope to encourage the experiments necessary to explore and identify such solutions.

We also hope grantees will amplify and emulate the efforts of our other partners working in rare disease therapeutics. For example, [Every Cure](https://everycure.org/), one of our existing AI for Science grantees, is using Claude to identify drug repurposing opportunities across millions of candidates ; the [Centre for Population Genomics](https://populationgenomics.org.au/), a collaboration between the Garvan Institute and the Murdoch Children’s Research Institute, is building a Claude-based system that drafts variant classifications for expert review, one of the biggest bottlenecks in diagnosing rare genetic conditions; and the [Violet Research Institute,](https://www.violetresearch.org/) a small nonprofit researching ultra-rare genetic diseases (defined as extremely rare genetic disorders affecting fewer than 1 in 50,000 births), is using Claude to navigate FDA guidelines, run bioinformatics pipelines, analyze experimental data, draft regulatory filings, and more.

### **Next steps**

To apply to either track of the AI for Science rare disease research program, [fill out this application](https://docs.google.com/forms/d/e/1FAIpQLSfwDGfVg2lHJ0cc0oF_ilEnjvr_r4_paYi7VLlr5cLNXASdvA/viewform). We will be accepting applications through August 2, 2026 at 11:59 PM PST. Accepted applicants can use their credits to access Claude Opus or other generally available models approved for use in biology. Projects that may run up against our bio classifiers may be eligible for exemptions. Examples of track one projects include:

- Propose and rank mechanistic links between distinct rare diseases that share a gene or pathway, suggesting candidate disease relationships with evidence an expert can validate in Monarch’s DisMech.
- Curate and summarize patient organization data to conduct or improve existing natural history studies.
- Build evaluations that measure how well models handle rare disease tasks—such as revealing candidate mechanisms for variants of unknown significance, phenotype-to-disease matching, and mechanism prediction—including an honest accounting of where they fail.

Outputs from this track will be made publicly available at [Monarchinitiative.org](http://monarchinitiative.org). The program will be augmented by additional community-building efforts, such as future rare disease hackathons. Stay up to date with the Monarch Initiative at [monarchinitiative.org/community/get-involved](https://monarchinitiative.org/community/get-involved).

Examples of track two projects include:

- Justify starting doses from sparse data: synthesize PK/PD modeling, allometric scaling, and precedent from related modalities to build first-in-human dose rationales for bespoke therapies where traditional dose-ranging studies are impossible.
- Mine natural history data and case reports to identify measurable biomarkers and functional endpoints sensitive enough to show a response within the timeframe an N-of-1 or ultra-rare program can afford.
- Draft, cross-check, and precedent-mine regulatory documentation (IND sections, investigator brochures, CMC modules), compressing months of dossier assembly into days of expert review.

This rare disease grant program ties directly into our mission and work in beneficial deployments to extend the benefits of AI to areas that might not emerge naturally through market forces. However, rare disease is simply too big a problem for one organization or one approach. We also want to be honest about AI’s limitations in this space. Although Claude may help shorten therapeutic development timelines and curate biological data more efficiently than human teams alone, it cannot help in areas where the data is too paltry or too poorly organized for agents to reach. It may also struggle to address the aspects of the “diagnostic odyssey” that relate to challenges like insurance authorization or access to diagnostic facilities and infrastructure. We hope this program will be complemented by efforts by other organizations and research institutions to generate more high-quality, longitudinal data, as well as those that encourage robust public-private partnerships.

We're looking forward to seeing how this new group of grantees will work together and with our other AI for Science partners to advance basic science and discovery in rare diseases, and how these projects can contribute to broader scientific initiatives.  
  
**Footnote**

1.  Other [sources place the number of rare diseases as high as 10,000](https://pmc.ncbi.nlm.nih.gov/articles/PMC7771654/). There is also no agreed-upon definition of what a rare disease even is, despite the oft-cited claim that as many as [1 in 10 people](https://www.fda.gov/patients/rare-diseases-fda) in the US have a rare disease. Various terminologies (Orphanet, OMIM, GARD, ICD, the NCI Thesaurus, and dozens more) each define “disease” differently; some exclude chromosomal disorders (such as conditions like Pallister-Killian syndrome); some ignore diseases with environmental causes (such as congenital Zika syndrome); and some require a single anatomical system to classify them, ignoring the many multi-system rare diseases (such as Fanconi anemia, with its mix of bone marrow failure, congenital malformations, and cancer risk).


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
