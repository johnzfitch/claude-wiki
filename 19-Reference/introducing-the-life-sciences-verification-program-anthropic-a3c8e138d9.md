---
title: "Introducing the Life Sciences Verification Program \\ Anthropic"
source_url: "https://www.anthropic.com/news/life-sciences-verification-program"
category: "19-Reference"
fetched_at: "2026-09-18T06:39:27Z"
tags: ["search"]
---

# Introducing the Life Sciences Verification Program

Sep 17, 2026

Today, we are introducing the Life Sciences Verification Program (LSVP), which gives life science professionals access to our Mythos, Opus, and Sonnet models with a refined set of safeguards more permissive for biology-related work. We have already onboarded dozens of organizations through an early-access program, and are now opening applications to the broader life science community ([apply here](https://claude.com/form/life-sciences-verification-program)). The program is launching in beta, initially for teams and institutions. We will continue to improve the program and expand access to individual Pro and Max plans over time.

The LSVP is designed to enable life science professionals to use our models across a wide range of tasks that are currently blocked in our generally available Fable models, like drug discovery, research biology, clinical development, and manufacturing. It’s built for teams of all kinds—from academic labs to startups, pharma companies, and more.

## **Verification and access types**

To qualify for these grants, each applicant goes through a verification process that includes a review of their research credentials, security standards, and ethical research oversight. Once verified, teams may apply for two types of LSVP grants, “Standard Use” or “High-risk Use,” depending on their access needs. These grants can be used through all our product surfaces, including [Claude Science](https://claude.com/product/claude-science), [Claude.ai](http://claude.ai/redirect/website.v1.7c0989d0-e91f-44eb-99da-39f4473e070f), Claude Code and the API.  
  
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

This data is strictly compartmentalized and cannot be used for model training or accessed by members of Anthropic’s life sciences research teams. For organizations that qualify, we are also working to understand how LSVP can integrate with features from our [Enterprise Frontier Safeguards](https://www.anthropic.com/news/enterprise-frontier-safeguards) (EFS) systems.

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
- [Sales](https://claude.com/solutions/sales)
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
