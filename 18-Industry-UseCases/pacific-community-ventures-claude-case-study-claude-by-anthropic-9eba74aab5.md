---
title: "Pacific Community Ventures Claude case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/pacific-community-ventures"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:41Z"
tags: ["enterprise", "security"]
---

# Pacific Community Ventures scales worker feedback 10x with Claude

[Try Claude](https://claude.ai)

Industry:  
Beneficial Deployments

Company size:  
Small

Product:  
[Claude Platform](https://claude.com/platform/api)[Claude for Nonprofits](https://claude.com/solutions/nonprofits)

Location:  
North America

~300 workers reached

in one nationwide voice survey, up from 12 in a comparable focus group

10x+ the scale of qualitative research

the team can now run with Claude

[Pacific Community Ventures](https://www.pacificcommunityventures.org/) (PCV) is a mission-driven community lender that backs small business owners who can't access capital or quality mentorship from traditional banks, with the goal of creating good jobs in the communities it serves. That work runs two ways: conducting research that centers the workers and owners behind the numbers and moving capital to entrepreneurs that conventional finance overlooks. They’re making it happen with two Claude-powered solutions built by their team: AIKKA, PCV's voice survey tool, and an underwriting co-pilot in early development.

## With Claude, Pacific Community Ventures:

- Reached close to 300 small business workers in a single nationwide voice survey, uncovering a level of insight depth that had previously required a 12-person focus group run over several weeks.
- Scaled its qualitative research to 10x of what the same small team could manage before.
- Collected responses in clients' native languages and tagged them for sentiment and theme at scale.
- Shifted its data scientists from coding every response to running spot checks, freeing time for deeper analysis.
- Synthesized anonymized worker feedback for small business owners, creating feedback loops to strengthen retention and job satisfaction, a practice often out of reach for small business owners.

## The challenge

## Lending fairly at scale

PCV's research only works if it reflects what people actually experience, and its lending only works if it reaches the people the rest of finance won't. Both halves of the work share a problem: the tools built to do them at scale tend to lose the individual person. "We could send standard surveys out at scale, but you don't get into the real nuance," said Sachi Shenoy, Chief Data Officer at Pacific Community Ventures. "You don't lift people's voices and their stories in that format."

On the research side, PCV faced a tradeoff. A multiple-choice survey could reach hundreds of clients at once but reduced their answers to checkboxes, while the one-on-one conversations that captured real depth reached only a handful. On the lending side, the question is who gets a fair hearing. The entrepreneurs PCV serves often apply with sparse financials, no credit score, and no banking history, the exact profile a conventional risk model is built to screen out. Underwriters have always made those calls through hours of conversation. The question was whether AI could speed that up without importing the biases community lenders exist to correct.

Q&A

A conversation with Pacific Community Ventures on building AI for fair lending

[Read more](https://claude.com/customers/pacific-community-ventures-qa)

## The solution

## A voice survey that captures what people mean

PCV's answer on the research side is AIKKA, a smartphone tool it built more than three years ago. Clients who opt in answer open-ended questions by speaking, up to five minutes at a time, in their native language. An engine transcribes every response, and Claude tags it for sentiment, emotion, and theme, feeding a dashboard that updates as answers arrive. While the underlying technology supports a broad range of languages, PCV’s testing has confirmed accuracy specifically in English, Spanish, Hindi, and Punjabi.

The choice of AI model mattered. Building AIKKA, the team ran the same voice transcripts through several providers, watching how each categorized, or "coded," the responses. "When we compared across providers for the level of nuance and the accuracy of the coding, Claude always won out," Shenoy said.

The gap showed up on the messy, human answers. A worker might be upbeat about some things and unsure about others. Other providers averaged it out: mostly positive, call it positive. Claude held onto the contradictions.

"Claude would say something like, 'tepid positivity mixed with uncertainty, and there's uncertainty around how long this respondent might remain in their job, which is leading to some hesitation,'" Shenoy explained. "It was going so much deeper. It seemed to have its finger on the pulse of human emotion." PCV moved to Claude exclusively, running AIKKA on Claude Opus through the API. The surveys run as part of PCV's national Good Jobs Community of Practice program among small business owners and their workers.

## An underwriting co-pilot built on Claude

Underwriting turns on the same thing AIKKA does, the story underneath the financials. The predictive credit risk model PCV is building is entirely its own. It is a machine learning classifier, not a large language model, trained only on PCV's historical inclusive lending data. That is by design.

"It is designed for us, by us, with us,” said Bulbul Gupta, CEO and President of Pacific Community Ventures. “We did not want a financial model trained on what traditional finance considers successful, because that would bring in exclusion to the very entrepreneurs we exist to include.”

A classifier only reads numbers, though. In practice, underwriters balance financial indicators with qualitative signals to reach a decision. Without Claude, an applicant might go through three or four rounds of phone calls while an underwriter builds an evidence base. "They might not have a long banking history or a strong credit score, but we're going to take a bet on this entrepreneur based on full context," Shenoy explained.

This is PCV's second Claude build: an underwriting co-pilot. Through the API, Claude will read applications and pull out the qualitative information underwriters rely on, then tag and quantify it to feed the predictive model. The team is starting with the backlog, running Claude over historical applications. The co-pilot will do the same for every new application that comes in.

The work is early. PCV has set aside two months for testing, with a rollout targeted for late September if all goes well. The co-pilot augments the underwriters' decisions in a way that "never replaces the human,” Shenoy said.

"What we're hoping is that this helps us speed up the decisions to get to yes, and allows our underwriting team to spend more time building trust and outreach in our communities and getting more maybe’s to yes," Gupta added. "That helps us deploy affordable capital into the communities faster, scaling efficiencies at an important time for our economy. As a nonprofit responsible small business lender, it is a rare competitive advantage our field needs to compete with much larger venture backed fintechs who offer higher rates."

Nonprofits

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

[Read more](/solutions/nonprofits)

## The outcome

## **Capturing depth at scale**

The clearest proof is on the research side. Using Claude as the engine, PCV's most recent worker voice survey reached close to 300 workers nationwide for a research paper on job quality. The comparison Shenoy reaches for is a focus group of 12, run by the same team over several weeks two years earlier.

"An effort like that would have been nearly impossible for a relatively small team," Shenoy said. "Now we're surfacing the same depth of information from 300 people in a much shorter amount of time. And we're just getting started."

That single survey reflects a broader shift. Across its qualitative research, the team now works at 10x or more its old scale, and how it spends its time has changed too. In AIKKA's early days, the data scientist still reviewed nearly everything by hand. Over the past year, confidence in Claude's tagging grew enough that the team moved to spot checks, which freed them for the analysis itself.

"Claude has brought the analysis time down massively," Gupta added. "It's still on our team to monitor, evaluate, and assess the insights, and communicate the ‘so what’ to external stakeholders." The reach points back to the owners PCV serves, most of them small businesses without the HR teams larger companies rely on to hear their people. Workers tell an anonymous survey things they would never say to their boss, and PCV packages those responses, names stripped out, into feedback loops around retention and satisfaction that owners can act on.

"Being able to share that feedback back with business owners has been game-changing for them," Shenoy said. The worker surveys show what the approach can do at scale. The underwriting work is where PCV hopes to feel it next.

## Related stories


### Mercy Corps on what AI makes possible in humanitarian work


### Mercy Corps accelerates global humanitarian response to community feedback with Claude


### The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude


### How the Epilepsy Foundation uses Claude across the organization

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
