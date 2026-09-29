---
title: "Carta Healthcare Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/carta-healthcare"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:53Z"
tags: ["api", "cli", "enterprise", "security"]
---

# Carta Healthcare cuts clinical data processing time by 66% with Claude

[Get started](https://claude.com/solutions/healthcare#pricing-section)

Industry:  
Healthcare

Company size:  
Medium

Product:  
Claude Platform

Partner:  
AWS

Location:  
North America

Up to 66% reduction

in time required for clinical data abstraction

+50% cost savings

on abstraction work while maintaining the industry's highest quality data

Advancing Claude in healthcare and the life sciences

Transform healthcare from insight to action

[Read more](https://www.anthropic.com/news/healthcare-life-sciences)

Claude for Healthcare

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

[Read more](https://claude.com/healthcare)

[Carta Healthcare](https://www.carta.healthcare/) began with a simple frustration at Stanford Children’s Hospital: slow, manual data collection was holding back meaningful progress. That challenge sparked a new idea to pair AI with clinical expertise, to make clinical data abstraction faster, higher quality and lower cost, what Carta refers to as “hybrid intelligence.”

## With Claude, Carta Healthcare:

- Reduces clinical data abstraction time by up to 66% while improving data quality
- Enabled processing of clinically complex questions that were previously impossible to automate
- Achieve 98-99% Inter-rater Reliability (IRR) scores, which is the healthcare industry's gold standard for data quality
- Transformed clinicians from manual data hunters into high-value validators and users of data to drive healthcare improvement

## The problem

Every day, hospitals generate mountains of clinical documentation, including physician notes, lab results, medication records, surgical reports, and more. Buried in these records are answers to critical questions that clinical registries need: Did this surgical patient develop an infection within 30 days? What was their BMI at admission? Were antibiotics administered within the correct window before incision? What was the door-to-balloon time?

Extracting these answers is called clinical data abstraction, and it is painstaking work. Trained abstractors spend, on average, one hour per case manually combing through clinical notes and documents, hunting for specific details buried in the electronic medical record. For complex cases, that time can stretch to five or six hours. A single health system might need to abstract more than 22,000 surgical cases per year, spending over 11,000 hours of labor annually.

But the challenge is not only the volume. Clinical documentation is messy, inconsistent, and often scattered across multiple systems and formats. Even within the same hospital, the “right answer” to a registry question may require interpretation, reconciliation of conflicting notes, and deep understanding of clinical intent. That complexity is why traditional automation attempts often fall short, and why purely manual workflows remain expensive and difficult to sustain.

“Hospital information systems are very complex and traditional data extraction and integration workflows inside hospitals are notoriously brittle, vary widely from system to system, and often break when electronic medical records are upgraded,” said Andrew Crowder, Vice President of Engineering and CISO at Carta Healthcare. “We needed an approach that insulated us from these inconsistencies and allowed us to deliver value without being tied to fragile, site-specific processes.”

## Choosing Claude

Security was the deciding factor in Carta Healthcare's model selection. Handling sensitive medical information, including protected health information, requires rigorous data privacy controls. Claude's availability in Amazon Bedrock provided the confidence Carta Healthcare needed with data privacy protections and assurance that customer data wouldn't be used for model training.

"While other models were available in Amazon Bedrock, no other model showed the capability for reasoning and understanding we found in Anthropic's models," said Crowder. "In addition, the published research on bias and model alignment has allowed us to pass rigorous hospital AI reviews."

That combination of security infrastructure, reasoning capability, and documented research on model alignment allowed Carta Healthcare to clear the high bar of hospital IT and AI review boards, a prerequisite for any system handling patient data.

## Building a clinical-grade AI system

Claude powers Carta Healthcare's Lighthouse platform, serving as the AI engine for clinical registry abstraction. Claude interprets both structured and unstructured medical data semantically, understanding the clinical context to formulate answers, provide justifications, and surface direct citations from medical records. The system can find evidence that's easy to miss in manual reviews, such as documentation buried deep in a chart or originating from encounters years earlier.

Carta Healthcare implemented a two-phase extraction pipeline. In the first phase, Claude Haiku 3.5 and Sonnet 4 extracted relevant information from medical documentation, processing both structured data and unstructured clinical notes. In the second phase, Claude Sonnet synthesized all extracted evidence to formulate suggested answers to registry questions, scoring and ranking the evidence. This approach improved accuracy and reduced the validation burden for abstractors. They now validate findings rather than hunt for them.

Because the system is built around Claude's ability to understand natural language, clinical experts can improve it directly. When abstractors notice an issue, the team adjusts prompts rather than rewriting code—changes that can be tested in production the same day. This keeps the people who understand clinical nuance in control of how the system behaves.

## The outcome

For one large health system abstracting over 22,000 surgical cases annually across 14 hospitals, the results were immediate. Time per case dropped from 30 minutes to 15-22 minutes for routine cases. For complex cases—the ones that used to consume five or six hours of an abstractor's day—time dropped to 90 minutes. Annual time savings reached between 3,667 and 6,050 hours, with Inter-rater Reliability consistently at 99%.

At a large multi-entity health system, manual abstraction for NSQIP cases was a constant strain. With over 22,000 cases annually across 14 hospitals, each taking about 30 minutes to abstract, the workload was immense leading to more than 11,000 hours of labor every year. The process was slow, expensive, and prone to human error. Before using Carta Healthcare’s Lighthouse platform, one experienced abstractor was quite skeptical of AI. She was experienced and clinically sharp, and worried that AI would not meet her expectations.

But she saw potential. She met with Carta Healthcare’s product team, shared detailed feedback, and worked closely with engineering to refine the platform. Her clinical expertise was critical—she knew when something didn’t look right, and her input helped shape Lighthouse into a tool she could rely on.

Today, she trusts Lighthouse completely. For complex cases, she even uses it as a second set of eyes, double-checking occurrences as well as catching subtle details like post-op medications that might otherwise slip through. As she puts it, “Lighthouse doesn’t replace my judgment, it enhances it.” The impact has been dramatic:

Selecting Claude as the core LLM has fundamentally changed Carta Healthcare's business model. By automating the cognitive work of abstracting unstructured clinical data, Claude and Lighthouse transformed the company's clinicians “from manual data hunters into high-value validators,” explained Crowder. Carta Healthcare reports 100% customer retention; 90% of customers also expand their engagement over time.

Looking ahead, Carta Healthcare plans to expand their AI capabilities to handle more complex registry scenarios, including cases with multiple procedures. "We are excited to grow both our usage of Anthropic's models." Crowder said. "We also look forward to expanding our technical relationship as we explore new possibilities with Claude."

## Related stories


### How League went all in on Claude in a regulated industry


### League cuts product development cycle times in half with Claude


### How can a medical lab keep patients at the center of its work while the caseload keeps growing?


### How Zingage automates care coordination for 400+ home care agencies with Claude

[](/)

© 2026 Anthropic PBC

## Products

- [Claude](/product/overview)
- [Claude Code](/product/claude-code)
- [Claude Cowork](/product/cowork)
- [@Claude](/product/tag)
- [Claude Science](/product/claude-science)
- [Claude Security](/product/claude-security)
- [Download app](/download)
- [Pricing](/pricing)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](/features/artifacts)
- [Design](/product/design)
- [Connectors](/marketplace/connectors-plugins)
- [Plugins](/marketplace/plugins)
- [Skills](/skills)

## Extensions

- [Claude in Chrome](/claude-in-chrome)
- [Claude for Microsoft 365](/claude-for-microsoft-365)

## Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

## Enterprise

- [Overview](/solutions/enterprise)
- [Claude Code for Enterprise](/product/claude-code/enterprise)

## Departments

- [Customer support](/solutions/customer-support)
- [Cybersecurity](/solutions/cybersecurity)
- [Legal](/solutions/legal)
- [Sales](/solutions/sales)

## Industries

- [Financial services](/solutions/financial-services)
- [Government](/solutions/government)
- [Healthcare](/solutions/healthcare)
- [Higher education](/solutions/education)
- [K-12 teachers](/solutions/teachers)
- [Life sciences](/solutions/life-sciences)
- [Nonprofits](/solutions/nonprofits)
- [Small business](/solutions/small-business)

## Programs

- [Startups](/programs/startups)
- [Scientists](/programs/team-plan-for-scientists)

## Developers

- [Developer docs](https://code.claude.com/docs/en/overview)
- [Developer blog](https://claude.dev)
- [Community](/community)
- [Console](https://platform.claude.com/docs/en/home)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](/platform/api)
- [Marketplace](/marketplace)
- [Claude on AWS](/partners/claude-on-aws)
- [Google Cloud](/partners/google-cloud)
- [Microsoft Foundry](/partners/microsoft-foundry)

## Resources

- [Blog](/blog)
- [Claude partner network](/partners)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](/customers)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](/partners/powered-by-claude)
- [Service partners](/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](/check-files)
- [Regional compliance](/regional-compliance)
- [Report abuse](/form/anthropic-content-reporting)
- [Security and compliance](https://trust.anthropic.com/)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

## Company

- [Anthropic](https://www.anthropic.com/)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Research](https://www.anthropic.com/research)
- [Anthropic news](https://www.anthropic.com/news)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Transparency](https://anthropic.com/transparency)

## Terms and policies

- Privacy choices
- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Terms of Service: US K-12](https://anthropic.com/legal/k12-terms)
- [Data Processing Agreement: US K-12](https://anthropic.com/legal/k12-dpa)
- [Usage Policy](https://www.anthropic.com/legal/aup)

## Products

- [Claude](/product/overview)
- [Claude Code](/product/claude-code)
- [Claude Cowork](/product/cowork)
- [@Claude](/product/tag)
- [Claude Science](/product/claude-science)
- [Claude Security](/product/claude-security)
- [Download app](/download)
- [Pricing](/pricing)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](/features/artifacts)
- [Design](/product/design)
- [Connectors](/marketplace/connectors-plugins)
- [Plugins](/marketplace/plugins)
- [Skills](/skills)

## Extensions

- [Claude in Chrome](/claude-in-chrome)
- [Claude for Microsoft 365](/claude-for-microsoft-365)

## Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

## Enterprise

- [Overview](/solutions/enterprise)
- [Claude Code for Enterprise](/product/claude-code/enterprise)

## Departments

- [Customer support](/solutions/customer-support)
- [Cybersecurity](/solutions/cybersecurity)
- [Legal](/solutions/legal)
- [Sales](/solutions/sales)

## Industries

- [Financial services](/solutions/financial-services)
- [Government](/solutions/government)
- [Healthcare](/solutions/healthcare)
- [Higher education](/solutions/education)
- [K-12 teachers](/solutions/teachers)
- [Life sciences](/solutions/life-sciences)
- [Nonprofits](/solutions/nonprofits)
- [Small business](/solutions/small-business)

## Programs

- [Startups](/programs/startups)
- [Scientists](/programs/team-plan-for-scientists)

## Developers

- [Developer docs](https://code.claude.com/docs/en/overview)
- [Developer blog](https://claude.dev)
- [Community](/community)
- [Console](https://platform.claude.com/docs/en/home)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](/platform/api)
- [Marketplace](/marketplace)
- [Claude on AWS](/partners/claude-on-aws)
- [Google Cloud](/partners/google-cloud)
- [Microsoft Foundry](/partners/microsoft-foundry)

## Resources

- [Blog](/blog)
- [Claude partner network](/partners)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](/customers)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](/partners/powered-by-claude)
- [Service partners](/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](/check-files)
- [Regional compliance](/regional-compliance)
- [Report abuse](/form/anthropic-content-reporting)
