---
title: "Qualified Health Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/qualified-health"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:46Z"
tags: ["api", "case-studies", "cli", "enterprise", "security"]
---

# Qualified Health and the University of Texas System use Claude to identify patients who need life-saving care

[Get started](healthcare.md#pricing-section)

Industry:  
Healthcare

Company size:  
Large

Product:  
Claude Platform

Location:  
North America

4–6 million patients per year

in Texas qualify for evidence-based interventions but never get identified

1 million+ patient population

at The University of Texas Medical Branch now being screened by protocols built on Claude to identify candidates for intervention

Advancing Claude in healthcare and the life sciences

Transform healthcare from insight to action

[Read more](../19-Reference/healthcare-life-sciences.md)

Claude for Healthcare

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

[Read more](https://claude.com/healthcare)

[Qualified Health](https://www.qualifiedhealthai.com) is a healthcare-native AI platform that identifies patients who qualify for life-saving treatments and improved evidence-based management but who would otherwise go undetected. The [University of Texas System](https://www.utsystem.edu) is one of the largest public university systems in the United States, with health institutions serving patients across Texas.

## With Claude, Qualified Health and the UT System:

- Screen a 2 million patient population to identify candidates for life-saving interventions
- Route eligible patients directly into clinicians' workflows with supporting documentation
- Complete chart reviews in minutes that previously required extensive manual abstraction
- Identify patients who benefit from medication optimization, therapeutic intervention, or further discussion
- Plan to expand from cardiology to primary care, vascular, GI, rheumatology, and neurology by end of 2026

## The problem

In Texas, almost every county experiences some critical physician shortage. Healthcare providers know that catching diseases earlier leads to better outcomes, but the information needed to identify at-risk patients is buried in fragmented clinical data that no human could reasonably review at scale.

"People both want and deserve a level of access to healthcare that our workforce can’t realistically deliver without AI augmentation," said Dr. Peter McCaffrey, Chief Digital and AI Officer at the University of Texas Medical Branch (UTMB).

Healthcare systems spent years digitizing their records, but digitization didn't make the data usable. "The problem we face is literally one of search, retrieval, and comprehension,” McCaffrey said. “It's 90% of what we do. It's where so much of our workforce gets burned out and it’s where most care gaps accumulate. The size and scope of that data are only growing, the breadth of our responsibility to patients is only growing, but our workforce is not keeping pace."

Organizations ended up with vast amounts of unstructured clinical notes, imaging reports, and test results scattered across disconnected systems. A patient may receive a new diagnosis of heart failure and may be started on therapy, but those medications and dosages may not align with the latest guidelines. Meanwhile, a Cardiology team–even at the same hospital–may be aware of the latest guidelines, but they would not be aware of whether newly diagnosed patients are receiving guideline-directed care even though doing so improves mortality. In Texas, an estimated 4–6 million patients qualify for evidence-based interventions each year and never get identified—resulting in preventable deaths, avoidable complications, and growing strain on the healthcare system.

## Claude powers population-scale patient identification

Qualified Health built an AI platform with Claude Sonnet 4.5 to help health systems identify patients who qualify for proven, evidence-based interventions at population scale. Claude was selected following a structured evaluation of multiple models, based on its performance in accurately extracting clinical information, minimizing hallucinations, and producing outputs that are fully traceable to source data, capabilities required for safe use in clinical settings.

The platform integrates fragmented clinical data, such as notes, laboratory results, imaging, and procedural records, and applies precise, guideline-based clinical criteria to determine patient eligibility across a broad set of cardiology practices.

Patients who meet those criteria are surfaced directly into clinicians’ existing workflows for review, with supporting documentation generated to trace each finding back to source data. This approach shortens the path from identification to treatment while preserving clinician oversight, enabling health systems to deliver evidence-based care more consistently and at a scale that was previously infeasible.

## From reactive care to proactive intervention

Justin Norden, MD, a physician and computer scientist, founded Qualified Health to help health systems deploy AI safely and at scale across clinical and administrative operations, enabling clinicians to find and treat patients who would otherwise fall through the cracks. His previous company focused on algorithm safety and trust in high-risk environments before being acquired for autonomous vehicle applications. That background shaped Qualified Health's approach: building the infrastructure needed to monitor, validate, and govern AI performance in high-risk healthcare settings.

"If we caught patients earlier and intervened, that would be better for everyone. That's very well known," said Norden. "What is not yet well known is that today, we have the potential to do that."

The partnership with the UT System began when Dr. McCaffrey was expanding his AI leadership role at UTMB. The institution needed a partner who could help them move fast and demonstrate real value, not just run interesting experiments. "We're not so much interested in, oh, you did something that looks cool on a poster," Dr. McCaffrey explained. "At this stage, we need true examples where AI is deployed in practice and it brings value to care because that is our mandate."

For cardiologists at UTMB’s Sealy Heart and Vascular Institute, the workflow is straightforward. They log into Qualified Health’s platform and see a census of patients who have been pre-screened by AI and who have opportunities for more optimized management in areas like heart-failure and valvular disease. The system then brings forward relevant medical and historical context balanced with evidence-based appropriateness criteria to highlight those who might otherwise go unnoticed but who would benefit from improved management. The Claude-powered AI platform surfaces relevant details from each patient's chart, extracting and synthesizing information that would be impossible to manually compile across a patient population.

"I could spend hours looking through charts and find things to worry about," Norden said. "But you can't do that on 10,000 patients." The system doesn't replace clinical judgment, he added. It amplifies it, enabling clinicians to apply their expertise at a scope that was previously impossible.

## Choosing Claude for clinical accuracy

Qualified Health continuously evaluates multiple large language models through a rigorous internal benchmarking process that combines automated testing with structured review by practicing physicians. Models are assessed on their ability to accurately extract structured clinical information from complex source data, minimize failure modes such as hallucinations, and provide traceable citations back to underlying records.

“Our focus is on precision and reliability,” Norden said. “We need models that can consistently identify the right clinical signals, avoid introducing errors, and make every output fully referenceable to the source data. In our evaluations for this work, Claude demonstrated the strongest performance across those dimensions.”

“Safety is non-negotiable in healthcare,” Norden added. “Anthropic has been a clear leader in building models with strong safety foundations, and that was an important factor in our decision-making.”

The validation process reflects Qualified Health’s roots in algorithmic safety and clinical rigor. Each deployment follows a staged approach that includes retrospective back-testing on historical data, automated evaluations, structured physician review, and controlled rollouts prior to broader use with partners.

“There are no fully automated clinical decisions being made,” Norden emphasized. “Every output is reviewed by clinicians, with direct validation against source data. Human oversight is built into the system by design.”

## The outcome

In the first month of deployment, the platform revealed that as many as a third of patients with heart failure have opportunities for improved optimization in guideline directed medical therapy. In the initial wave of review, this translated into dozens of patients with opportunities for evidence-based improvement in medication management which cardiologists could then validate and notify care teams. “This is a great example of AI actively augmenting the clinical workforce”, McCaffrey said. “It’s well known that many patients with heart failure can benefit from improved pharmacologic management but examining this adherence and medication practice across a population just isn’t feasible; we don’t have the clinician bandwidth for that.”

The approach extends beyond cardiology. "We started in cardiology, but this isn't just a cardiology tool," McCaffrey noted. "It's the same problem everywhere—there's a patient in GI with early cirrhosis, there's someone in vascular with an aneurysm that's never been flagged. The information is there. We just haven't had a scalable way to surface it. The need isn’t for AI to make medical decisions; instead, the need is to bring buried issues to the foreground so that clinicians can make medical decisions."

Cardiology was a deliberate starting point as a specialty with well-established diagnostic criteria, clear clinical guidelines, and availability of proven interventions with life-saving potential.

Building on UTMB's success, the initiative is now expanding system-wide. By the end of 2026, new deployments will help health systems across Texas identify patients eligible for evidence-based treatments in primary care, vascular, gastrointestinal, rheumatology, and neurology specialties. Dr. McCaffrey chairs AI work across all UT System health institutions, and the system views itself as responsible for all Texans across its exceptional geographic, medical, and socioeconomic diversity.

Dr. McCaffrey added: "Being able to scale that intelligence, that clinical reasoning, to everyone, everywhere is a really inherent social good.”


## Related stories


### How League went all in on Claude in a regulated industry


### League cuts product development cycle times in half with Claude


### How can a medical lab keep patients at the center of its work while the caseload keeps growing?


### How Zingage automates care coordination for 400+ home care agencies with Claude

[](https://www.claude.com/)

© 2026 Anthropic PBC

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
- [Security and compliance](https://trust.anthropic.com/)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

## Company

- [Anthropic](https://www.anthropic.com/)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Research](../19-Reference/anthropic-com-research.md)
- [Anthropic news](../19-Reference/news.md)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](../19-Reference/announcing-our-updated-responsible-scaling-policy.md)
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

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
