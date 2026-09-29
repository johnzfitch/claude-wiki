---
title: "Improving Fable 5&#x27;s safeguards \\ Anthropic"
source_url: "https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards"
category: "19-Reference"
fetched_at: "2026-09-10T06:44:00Z"
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

One of the core ways we protect against misuse in biology is via safety *classifiers:* smaller, automated AI systems that detect when Fable 5 is asked to perform a safeguarded biology task, or produce a harmful output (we've [previously written](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework) about our similar classifiers in the domain of cybersecurity).

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

[Read more](/news/enterprise-frontier-safeguards)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](/news/improving-alignment-security-efforts)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](/news/model-hardware-standard-research-preview)

[](/)

### Products

- [Claude](https://claude.com/product/overview)
- [Claude Code](https://claude.com/product/claude-code)
- [Claude Code Enterprise](https://claude.com/product/claude-code/enterprise)
- [Claude Cowork](https://claude.com/product/cowork)
- [@Claude](https://claude.com/product/tag)
- [Claude Design](https://claude.com/product/design)
- [Claude Science](https://claude.com/product/claude-science)
- [Claude Security](https://claude.com/product/claude-security)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](https://claude.com/pricing)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Commerce](https://claude.com/solutions/commerce)
- [Customer support](https://claude.com/solutions/customer-support)
- [Cybersecurity](https://claude.com/solutions/cybersecurity)
- [Enterprise](https://claude.com/solutions/enterprise)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Healthcare](https://claude.com/solutions/healthcare)
- [Higher education](https://claude.com/solutions/education)
- [K-12 teachers](https://claude.com/solutions/teachers)
- [Legal](https://claude.com/solutions/legal)
- [Life sciences](https://claude.com/solutions/life-sciences)
- [Nonprofits](https://claude.com/solutions/nonprofits)
- [Small business](https://claude.com/solutions/small-business)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](https://platform.claude.com/docs)
- [Pricing](https://claude.com/pricing#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](https://claude.com/partners/claude-on-aws)
- [Google Cloud](https://claude.com/partners/google-cloud-vertex-ai)
- [Microsoft Foundry](https://claude.com/partners/microsoft-foundry)
- [Console login](https://platform.claude.com/)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](https://claude.com/partners)
- [Community](https://claude.com/community)
- [Connectors](https://claude.com/connectors)
- [Courses](https://academy.claude.com)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](/engineering)
- [Events](/events)
- [Plugins](https://claude.com/plugins)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](https://claude.com/programs/startups)
- [Scientists](https://claude.com/programs/team-plan-for-scientists)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](/company)
- [Careers](/careers)
- [Leadership](/company/leadership)
- [Policy](/policy)
- [Economic Futures](/economic-futures)
- [Research](/research)
- [News](/news)
- [Claude’s Constitution](/constitution)
- [Claude Corps](/claude-corps)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](/transparency)
