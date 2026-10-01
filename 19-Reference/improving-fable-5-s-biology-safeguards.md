---
title: "Improving Fable 5's safeguards \\ Anthropic"
source_url: "https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards"
category: "19-Reference"
fetched_at: "2026-09-10T06:44:00Z"
tags: ["news-research"]
---

# Improving Fable 5's biology safeguards

Aug 7, 2026

We’re making updates to Claude Fable 5’s biology safeguards in a way that substantially reduces false positives. Fable 5 users will now experience many fewer “fallbacks”—where the system switches to a less capable model after they make a biology-related query. In our testing, this update reduced *biology-related* fallbacks by about 85% across our product surfaces.¹

Fable 5 will thus be able to assist with a wider range of biology tasks.

In practice, users should see far fewer fallbacks on everyday health and educational questions—for example, interpreting lab results, understanding symptoms, and learning about biology in an educational context. Healthcare professionals will be able to receive more support from Fable 5 on clinical tasks.

We believe the greatest opportunity for AI to positively affect the world is in biology and medicine, and we're investing significantly in building a responsible way to give biologists frontier access. Today, Fable still falls back to Opus 5 for requests we consider dual-use—including virology, toxicology, and molecular design—so it isn't yet usable for professional biology research and drug development. We're committed to closing that gap through trusted access pathways for frontier biology capabilities.

### Why we built strong biology safeguards

Our objective is to get Fable 5’s frontier capabilities into the hands of as many of our users as possible, as quickly as possible. However, to do so, we need to manage the increasing risks that come with models this capable. One such risk is in the field of biology: Fable 5 can now outperform experts on some highly complex biological tasks and provide operational support on others. That means that it can provide genuine assistance to a researcher developing a new medical treatment (which is the reason we’re so keen to widen access to the model via both classifier improvements and trusted access programs). But in the wrong hands, those same capabilities could be used by a malicious actor, for example in developing a biological weapon. Our [capability assessments](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf) show that Fable 5 could provide significant *uplift* to such an actor—that is, it could provide them with capabilities they could not find anywhere else.

It’s often difficult to tell apart beneficial and harmful uses of AI in biology. For example, in some cases researching a treatment for a disease requires scientists to produce the dangerous compounds that *cause* that disease in the first place. This is most obvious for live vaccines, which require scientists to grow the same pathogen they’re aiming to prevent. It’s also the case for some medicines. To develop the drug captopril, which treats hypertension, scientists isolated toxic components of snake venom that crash blood pressure in humans. As new biological capabilities develop on the frontier of AI, we need to be cautious to ensure that the new risks they pose do not materialize ahead of their potential scientific benefits.

Sophisticated actors who wish to use our models to do harm know how to exploit this ambiguity to obscure their intent, making dangerous tasks look like ordinary research pursuits. The US Intelligence Community’s [2026 Annual Threat Assessment](https://www.dni.gov/files/ODNI/documents/assessments/ATA-2026-Unclassified-Report.pdf) makes clear that such actors exist, and that advances in biotechnology including synthetic biology and genomic editing *“could lead to novel biological threats.”* It notes that several state actors likely maintain active offensive biological and chemical weapons programs—programs that could be accelerated by access to the raw capabilities of frontier AI models.

Because of our concerns about these “dual-use” capabilities (those that could be used for beneficial or harmful purposes, and where the line between them is not always easy to draw), we intentionally launched Fable 5 with almost all biology queries blocked. This enabled us to make the model available for users in other domains. We knew this would be frustrating for legitimate biology users: it would result in a high number of false positives in the near term, where users asking biology-related questions would have their requests blocked and sent to a less capable model. Nevertheless, we chose to make this tradeoff because the cost of Fable being misused in a dual-use domain like biology could potentially be [catastrophic](https://cdn.sanity.io/files/4zrzovbb/website/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf).

### How our biology safeguards work

One of the core ways we protect against misuse in biology is via safety *classifiers:* smaller, automated AI systems that detect when Fable 5 is asked to perform a safeguarded biology task, or produce a harmful output (we've [previously written](fable-safeguards-jailbreak-framework.md) about our similar classifiers in the domain of cybersecurity).

In the case of Fable 5, when a classifier fires, the model re-routes the user’s request to Opus 5, a capable model that does not have the same level of biological capability as Fable 5 and which cannot provide as much assistance to a malicious user. This is the fallback that users see when their requests are blocked.

Developing precise, robust classifiers is not a straightforward task. For a classifier to work rapidly and consistently, it has to learn the difference between what we consider “in scope” and “out of scope” for the topics and queries we consider to be potentially harmful. It takes time and iteration to tune the classifiers, avoiding both false positives (where classifiers fire on out-of-scope content) and false negatives (where in-scope content is missed). We also require our classifiers to be robust to attempts to bypass them (known as jailbreaks), which requires even further research and testing.

Starting with a very broad biology classifier meant that we could give our users access to Fable 5 while we continued our research aimed at refining it. The alternative—holding back the model until much more safeguards progress was made—would have delayed the model’s general access, and its potential benefits to our users, by weeks or months.

Over the past several weeks, we've carefully rewritten the classifier’s constitution (which consists of a collection of rules to help the model discern between safeguarded and allowed content), taking care to carve out benign uses in detail. We solicited feedback on the changes from a diverse range of experts (both internal and external to Anthropic). We then developed updated training data for the classifier based on that constitution, and retrained it, and verified the new classifier would still generally trigger for harmful and dual-use research biology content but would now enable a wider range of benign and beneficial uses.

As is illustrated in the diagram below, these updates meant that—compared to at the time of Fable 5’s launch—the classifier will trigger for many fewer benign biology-related requests.

## Conclusions

There’s still much more to be done to refine our safeguards. There will inevitably remain false positives—requests that fall within the classifier’s safety margin where the request is very low-risk but where the classifier still fires. As we noted above, Fable will continue to block dual-use professional biology and drug development queries because of potential dual-use risk. We are fully committed to developing a safe, scalable path for researchers to use our most capable models via trusted access pathways.

We hope you’ll continue to share your feedback with us so we can improve our safeguards even further.

#### Footnotes

¹ As a result, we expect the total number of fallbacks—for biology–related or any other reasons—will also be reduced: by roughly 67% on [Claude.ai](http://Claude.ai), 55% on Cowork, 17% on Claude Code, and 7% on the Claude Platform.


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
