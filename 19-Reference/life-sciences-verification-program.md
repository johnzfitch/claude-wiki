---
title: "Introducing the Life Sciences Verification Program \\ Anthropic"
source_url: "https://www.anthropic.com/news/life-sciences-verification-program"
category: "19-Reference"
fetched_at: "2026-09-18T06:39:27Z"
tags: ["news-research", "search"]
---

# Introducing the Life Sciences Verification Program

Sep 17, 2026

Today, we are introducing the Life Sciences Verification Program (LSVP), which gives life science professionals access to our Mythos, Opus, and Sonnet models with a refined set of safeguards more permissive for biology-related work. We have already onboarded dozens of organizations through an early-access program, and are now opening applications to the broader life science community ([apply here](https://claude.com/form/life-sciences-verification-program)). The program is launching in beta, initially for teams and institutions. We will continue to improve the program and expand access to individual Pro and Max plans over time.

The LSVP is designed to enable life science professionals to use our models across a wide range of tasks that are currently blocked in our generally available Fable models, like drug discovery, research biology, clinical development, and manufacturing. It’s built for teams of all kinds—from academic labs to startups, pharma companies, and more.

## **Verification and access types**

To qualify for these grants, each applicant goes through a verification process that includes a review of their research credentials, security standards, and ethical research oversight. Once verified, teams may apply for two types of LSVP grants, “Standard Use” or “High-risk Use,” depending on their access needs. These grants can be used through all our product surfaces, including [Claude Science](../15-Claude-AI-Features/product-claude-science.md), [Claude.ai](http://claude.ai/redirect/website.v1.7c0989d0-e91f-44eb-99da-39f4473e070f), Claude Code and the API.  
  
**Standard Use** grants are suitable for most life science work, including the majority of biology research and development workflows. These grants can be extended to entire teams for diverse, daily workloads, and are renewed once a year. They give those teams access to our Mythos, Opus, and Sonnet models, with refined classifiers that are more permissive for science tasks than our generally available models. Standard Use grants apply to Mythos 5.1, Opus 5, and Sonnet 5 today, and to future models as they launch. They’re specifically designed to enable the full breadth of life science activities in areas spanning basic science, R&D, supply chain and manufacturing, clinical development, quality assurance, regulatory affairs, investing and diligence, and more.

Although we expect Standard Use to cover the majority of access needs, some work carries a higher potential for misuse and therefore requires additional vetting.

**High-risk Use** is an add-on grant for teams working in areas blocked under Standard Use. It removes all safeguards that block life sciences requests. This grant applies to a single research project as opposed to a full team, and must be renewed every six months. Typically, a single researcher with dual-use work would have access to one Standard Use grant for diverse, daily activities, and one or more High-risk Use grants which only apply to work on specific projects (for example, characterizing how one specific family of viral vectors is recognized by human immune pathways).

High-risk grants for Claude Opus 5 and Claude Sonnet 5 are available today. We are working with the US government to make high-risk grants more broadly available for Claude Mythos, but at the time of this launch they will remain limited to a small set of entities with additional vetting.

All other safeguards, such as cyber classifiers, will remain in place under LSVP grants.

## Enabling trusted access through shared responsibility

As we’ve shown in our recent [threat report](https://www.anthropic.com/threat-intelligence-report-september-2026), there are increasingly sophisticated misuse attempts happening on our platform, including attempts that could support biological weapons development. In biology, where it’s often not possible to differentiate between a user doing valid work (e.g. research a viral pathogen to develop vaccines against it) and pursuing harm (e.g. trying to increase the transmissibility of a virus maliciously), the most concerning threat models are ones where valid access has been diverted or overtaken by an actor with bad intent. Indeed, insider threats and rogue-use have been major factors in significant biosafety incidents and scares. In developing the LSVP’s safeguards, we aimed to protect against three concerning threat models in particular:

- *Access compromise:* Malware or account takeover diverting access to a bad actor
- *Insider threats:* Rogue or coerced employees intentionally taking malicious action or diverting their access to a bad actor
- *Agent misuse:* Agents, especially working in swarms or over long-horizon tasks, taking unintended dangerous actions

In order to defend against these threats and in close collaboration with enterprise CISOs, we designed the new LSVP safeguards around the concept of shared responsibility by monitoring usage against the *intended use-case* for the model access. Because we vet the LSVP organizations for their life sciences credibility and oversight, we can empower them to specify for themselves what constitutes safe usage for teams or projects within their program.

Each entity’s access is tied to the use cases it has specified in its grant applications, and we continuously monitor LSVP traffic to identify usage or patterns that are outside the stated safe scope. Should unauthorized activity occur, we can flag these cases to organization admins to take action within pre-agreed timeframes for triaging and remediating incidents. The use cases should include high-level descriptions of the intended work, like one would share in a job listing, and not include any sensitive information or IP.

## How monitoring works in LSVP

Serious misuse is often spread across many requests and sessions to look disconnected and evade detection. In the LSVP, we are shifting safeguards from real-time blocking, where we reject potentially harmful access at the time of each request, to offline monitoring, which allows us to more clearly identify potential misuse across patterns of behavior. Shifting enforcement from real-time blocking to offline monitoring allows legitimate work to proceed with fewer interruptions, but it requires us to retain data associated with flagged activity for review. For LSVP traffic, we are requiring data retention for 30 days to be able to do this monitoring effectively.

This data is strictly compartmentalized and cannot be used for model training or accessed by members of Anthropic’s life sciences research teams. For organizations that qualify, we are also working to understand how LSVP can integrate with features from our [Enterprise Frontier Safeguards](enterprise-frontier-safeguards.md) (EFS) systems.

## What researchers are saying

> Xaira is making biology more computable, generating biological data at unprecedented scale and building foundation models of cell, protein and disease biology that turn it into the next generation of life-changing medicines. We’re excited to put Anthropic's frontier models to work across our drug discovery engine, and we believe pairing trusted access with intelligence is the right way to realize AI’s promise in biology.
>
> Xaira Therapeutics

> Edison’s mission is to accelerate science and the discovery and development of new medicines. With the Life Sciences Verification Program, we are excited to be able to bring Anthropic’s most intelligent models to bear on these problems. We look forward to collaborating with Anthropic further to end disease and improve the lives of patients everywhere.
>
> Edison Scientific

> At Manifold Bio, we’re building a massively parallel interface into living systems to enable powerful AI to create medicines. We look forward to putting frontier intelligence to work safely in our engine, and we welcome Anthropic’s approach of pairing access with accountability.
>
> Manifold Bio

01 / 03

## Applications and availability

Organizations interested in joining the LSVP can [submit an application here](https://claude.com/form/life-sciences-verification-program). We expect to enroll hundreds of organizations within the first week, and to scale the program further to support the majority of the life science community in the coming weeks.

Today, LSVP is available in our first-party console for API usage, as well as in Claude for Enterprise and Team plans. We do not yet support individual plans but are working to expand access for these users. It is also not yet available on third-party platforms.

As a beta, LSVP is not available for BAA-enabled orgs. This means customers with PHI data should use separate non-BAA orgs with non-HIPAA.

In API and Claude Science, users can switch between grants natively. In [Claude.ai](http://claude.ai/redirect/website.v1.7c0989d0-e91f-44eb-99da-39f4473e070f) and Claude Code, initially only a preselected default grant applies (except while using Claude Code with API authentication). This should be fine for the vast majority of users, who will only ever require a Standard Use grant. However, we will improve support and portability of these LSVP features over time.

## What comes next

Providing these frontier capabilities is part of our broader efforts in supporting the life sciences community in our shared mission to accelerate curing disease and improving human health. We will share more about new products, research collaborations, and improvements to the program in the coming months.


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
- [Sales](../18-Industry-UseCases/sales.md)
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
