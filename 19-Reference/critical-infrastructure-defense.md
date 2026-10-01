---
title: "AI to defend critical infrastructure \\ Anthropic"
source_url: "https://www.anthropic.com/research/critical-infrastructure-defense"
category: "19-Reference"
fetched_at: "2026-09-10T06:44:05Z"
tags: ["news-research", "security"]
---

# Experimenting with AI to defend critical infrastructure

Jan 8, 2026

Cyber attacks have had severe real-world effects on critical infrastructure like power grids and fuel pipelines, and have breached water systems—creating the potential for serious harm. As capabilities advance, AI models could increase the number of attackers capable of pursuing these targets. But AI could also help defenders of critical infrastructure identify the vulnerabilities that attackers might exploit—and close them before they are exploited. Anthropic has [partnered](https://www.pnnl.gov/news-media/generative-ai-speeds-cybersecurity-defenses) with Pacific Northwest National Laboratory (PNNL) to explore this defensive application of AI. Using Claude, PNNL researchers emulated cyber attacks on a high-fidelity simulation of a water treatment plant in far less time than it would have taken a human expert, serving as a proof of concept for how AI can help cyber defenders iterate faster on red teaming exercises. This work demonstrates both the potential of AI-accelerated defense and the value of public-private partnerships in harnessing AI for national security.

## Using AI to speed up adversary emulation

For this research project, PNNL focused on using AI to accelerate the task of adversary emulation: modeling a specific threat actor or a specific attack against a network in order to understand and improve defenses. Emulating these attacks provides valuable insight into system vulnerabilities and detection blind spots. Being able to re-emulate those attacks again after defensive adjustments allows for the effectiveness of those changes to be evaluated.

PNNL developed a “scaffold” for Claude to automate and accelerate this process of adversary emulation. This scaffold allowed natural language prompts to be quickly translated into complex attack chains, in part by pre-defining some code-based “tools” that allow the model to more easily take actions on computer networks. The researchers then tasked this agent with emulating attacks against a cyber-physical model of a water treatment plant (one of the [Control Environment Laboratory Resource](https://www.pnnl.gov/projects/control-environment-laboratory-resource) platforms that PNNL operates on behalf of the Department of Homeland Security’s Cybersecurity and Infrastructure Security Agency). PNNL’s estimate is that this allowed attack reconstruction to be completed in three hours instead of multiple weeks.

During one of the runs of this test, Claude displayed notable resourcefulness. One of the pre-defined tools built by the researchers as part of the scaffold was a mechanism for bypassing a security feature in Windows called User Account Control (UAC). However, this mechanism was not always reliable and sometimes failed. Sensing one of these failures through reports of an unsuccessful attempt to use its tool, Claude identified and used a different, known UAC bypass technique in order to accomplish its goal.

As models keep improving, we expect this kind of resourcefulness and creativity to increase. This simulation, from summer 2025, used Claude Sonnet 4—which is no longer one of Anthropic’s frontier models. Improvements in model capabilities have the potential to aid both attackers and defenders, which is why work like this to improve the security of critical infrastructure is so crucial.

## Expanding public-private partnerships for AI and security

This research puts into practice our call for creative thinking and experimentation with using [AI for cyber defense](https://red.anthropic.com/2025/ai-for-cyber-defenders/), a step that is critical given the dual-use nature of AI for cyber and the increased [use of AI by attackers](disrupting-ai-espionage.md) in cyberspace.

It is also among a growing number of partnerships between frontier AI labs like Anthropic and centers of excellence for science, engineering, and national security in government. Anthropic has previously [worked with the National Nuclear Security Administration](https://red.anthropic.com/2025/nuclear-safeguards/) on the development of evaluations and mitigations for potential nuclear risks associated with AI. Anthropic is also one of the private sector collaborators in the Department of Energy’s [Genesis Mission](genesis-mission-partnership.md), which aims to harness the expertise and scientific tools of the DOE national laboratories and frontier AI companies to make scientific breakthroughs in the service of national security.

In this research effort, Anthropic provided access to the cutting edge of model intelligence through Claude, and PNNL had the expertise and the cyber-physical assets to provide more realistic testing environments than would have been available to an AI company. Put differently, neither party could have done this kind of experimentation without the other. This is the central logic of the public-private partnerships that we undertake. We will continue to look for these complementarities, and welcome the chance to continue working with exceptional institutions like the national labs on our shared mission of ensuring that AI is used to protect critical infrastructure and other pillars of security and stability.

## Acknowledgments

We are grateful to Loc Truong and Kristopher Willis at PNNL for leading this project and sharing data with us for this post. You can read more about the project on PNNL’s [website](https://www.pnnl.gov/news-media/generative-ai-speeds-cybersecurity-defenses).


## Related content

### An alignment assessment of recent cybersecurity incidents

We present an alignment assessment of four incidents in which Claude models gained unauthorized access to real third-party systems.

[Read more](alignment-assessment-cybersecurity-incidents.md)

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.

[Read more](formalizing-fermats-last-theorem.md)

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

[Read more](automated-researchers-mitigate-alignment-failures.md)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.

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
