---
title: "Mercy Corps Claude for Nonprofits case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/mercy-corps"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:42Z"
tags: ["enterprise", "security"]
---

# Mercy Corps accelerates global humanitarian response to community feedback with Claude

[Try Claude](https://claude.ai)

Industry:  
Beneficial Deployments

Company size:  
Large

Product:  
[Claude for Nonprofits](https://claude.com/solutions/nonprofits)[Claude Enterprise](https://claude.com/solutions/enterprise)

Location:  
North America

From a week to an hour

to analyze community feedback in CARM pilot testing

88% average time reduction

across tracked tasks in the 13-team pilot midline survey

[Mercy Corps,](https://www.mercycorps.org/) which will become Prosper Global later in 2026 as part of its organizational evolution, is a global humanitarian organization running more than 200 programs across 30+ countries. Its Community Accountability Reporting Mechanism, CARM, offers the people it serves a pathway to speak up, whether that means asking a question, making a suggestion, or reporting that something has gone wrong. Claude now helps CARM teams translate, tag, and grade that feedback in a fraction of the time it once took.

## With Claude, Mercy Corps:

- Cut community feedback analysis from a week to about an hour
- Reduced time on tracked tasks by an average of 88% across a 13-team pilot
- Reached 75% agreement between Claude's proposed severity grades and trained human graders in controlled testing
- Saved more than 540 hours in a single month across 29 tracked tasks
- Completed vendor security review and a formal privacy impact assessment with a single provider

## The challenge

## When a serious report waits in a queue

Community feedback mechanisms are a baseline expectation across humanitarian work, part of the sector's accountability to the people it serves. CARM is Mercy Corps' answer. It gives participants in Mercy Corps programs and the people living around them a way to tell the organization what is working, what is not, and when something has gone wrong. That includes questions about assistance to safeguarding concerns and complaints about staff conduct. Reports arrive through hotlines, forms, help desks, and in-person conversations, very often in one of dozens of local languages, from Burmese and Ukrainian to Spanish and French. Before Claude, someone had to transcribe each report, translate it, read it, decide which theme it fell under, grade its severity against the organization's guidance, and route it for action.

Most reports are ordinary program feedback. Some are not. "The whole point of accountability is that the person who raised the concern trusts that we hear it, act on it and report back in a timely manner," said Nayid Orozco, AI Solutions and Delivery Manager at Mercy Corps. "If a serious report sits in a queue unread or gets logged as routine when it should have been escalated, we have not just missed a data point. We have let down someone who took a risk to speak up, and we may have left a protection issue unaddressed."

The strain showed up in three places: volume, language, and consistency. Teams had more feedback than they could process quickly, local dialects were hard to translate and respond to, and two people could grade the same case differently. The cost was staff time and delay. "Speed and correct severity grading are the difference between a mechanism that protects people and one that just collects forms," Orozco said.

Q&A: Mercy Corps

Read the Q&A with AI Solutions and Delivery Manager Nayid Orozco on AI's biggest shift in humanitarian work.

[Read more](https://claude.com/customers/mercy-corps-qa)

## The solution

## Criteria that could disqualify a model

For triage that could touch safeguarding, the first questions "were not about speed," Orozco recalled. "They were about data, responsibility and control." Mercy Corps needed a provider that would not train on its data, that held inputs for as short a window as possible, and that could show real certifications rather than promises. Anthropic's commercial terms met both requirements, and together with ISO 27001, ISO 42001, and SOC 2 certifications, they "are what let us even start the conversation," Orozco said.

"What would have disqualified a model was any ambiguity on data use, or any sign that it would confidently invent things on sensitive content," Orozco explained. "We tested by running real cases through it and checking the output, not by taking it on trust."

A CARM colleague ran 20 real feedback cases through Claude, graded against the team's standard guidance, then compared the results to the original human grades. Claude agreed about 75% of the time. "The most useful part was the disagreements," Orozco noted. Some traced to genuine ambiguity in the rubric, and a few prompted the team to look again at whether the original human grade was right. "It gave us a baseline for automated grading, and it worked as an audit of our own consistency," he said. "The reason it gave us confidence to continue was that the divergences were explainable and instructive, not random." The team initially found that Claude sometimes changed its grade when the same case was run again. However, after refining the grading definitions and guidance provided to Claude, the system produced more consistent and accurate classifications.

Trust also had to be earned on the procurement side, not just in the model's answers. Mercy Corps works with Anthropic through the Claude Enterprise interface for day-to-day work and the Claude API for production work such as automated grading, under one set of commercial terms and one Data Processing Agreement. The team completed its vendor forms and a formal privacy impact assessment from Anthropic's published documentation. "For a nonprofit that does not have a large procurement or security team, that consolidation genuinely shortened the review," he added.

## How it works: A person still owns the decision

In the current test flow, a report comes in, often in a local language. Direct identifiers and the most sensitive content are screened and redacted, then Claude translates it into clear English, tags it by theme, and proposes a severity grade against the team's six-level grading matrix with a short rationale. A CARM staff member reviews that output against the original and confirms or adjusts the grade. The work runs through the Claude Enterprise interface with grading guidance loaded as shared project knowledge.

"Claude never makes the final call," Orozco said. "It speeds up translation, tagging and a first-pass grade, but a trained staff member always reviews the output and owns the decision. Communities can trust the process because accountability still rests with a person, not a model."

"We are still in a testing phase here, not a fully integrated production system," Orozco emphasized. "CARM is deliberately piloting Claude and checking its results case by case before we trust it with anything live." The model the team is working toward is a shared Claude Project holding the CARM grading guidance and standard prompts, so the staff member who handles feedback in any country, what Mercy Corps calls a focal point, can get consistent translation, theme tagging, and a suggested grade without building the setup themselves. In the coming months, Mercy Corps plans to connect this to Zendesk, its CARM feedback management system.

"The rollout is less about the technology and more about people," he noted. "It means training focal points on how to prompt and, just as importantly, how to sanity check what comes back." The team is expanding only as the testing gives it confidence.

Nonprofits

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

[Read more](/solutions/nonprofits)

## The outcome

## A week of analysis in about an hour

CARM team members report that feedback analysis that used to take up to a week now takes about an hour, and a report that took 8 hours to produce now takes 30 minutes. The speed ensures serious reports no longer sit unread in a queue, and the people who raised them hear back sooner.

The gains extend well beyond one team. Emily Joy, a director on Mercy Corps' corporate partnerships team, pointed to "the work that Claude has enabled that just wouldn't have been possible before." On the monitoring, evaluation, and learning (MEL) side, a research design estimated at roughly 280 person-hours was completed in about 20, and a market dataset analysis for Mercy Corps' Sudan research went from about a week to a day and a half, with its processing script now in production. Staff without developer skills, she said, "are now able to run reports and get those questions answered that they would not have been able to self-serve before."

In Mercy Corps' pilot midline survey of 42 users across 13 teams, 98% reported faster workflows, the average time reduction across tracked tasks was 88%, and more than 540 hours were saved across 29 tracked tasks in a single month.

"The reaction that stuck with me was a MEL colleague saying their biggest worry was that Claude might go away after the pilot," Orozco recalled. "When the loudest complaint is fear of losing the tool, that tells you something about how embedded it had become."

Next comes moving CARM from testing into a real rollout, taking the shared project to feedback staff in more countries. "Underneath all of it, we are building an AI adoption and governance framework so that expansion stays deliberate and responsible rather than ad hoc," Orozco said. Moving the heavier production work onto the Claude API is, in his words, what makes that scale "realistic rather than theoretical."

## Related stories


### Mercy Corps on what AI makes possible in humanitarian work


### The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude


### How the Epilepsy Foundation uses Claude across the organization


### Building dignity-driven AI: A conversation with the National Domestic Workers Alliance

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
