---
title: "Epilepsy Foundation Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/epilepsy-foundation"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:35Z"
tags: ["api", "enterprise", "security"]
---

# The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude

[Try Claude](https://claude.ai)

Industry:  
Beneficial Deployments

Company size:  
Medium

Product:  
[Claude Platform](https://claude.com/platform/api)

Partner:  
AWS

Location:  
North America

60,000 interactions with Sage

reached in under a year, before any major promotion

2.5x more interactions per session

From 1.2 to 3 since launch, as trust in Sage grew

[The Epilepsy Foundation](https://www.epilepsy.com/) is the leading nonprofit serving people with epilepsy across the United States. The organization is built around a simple mission: no one should face epilepsy alone. For more than two decades, its website, epilepsy.com, has been the authoritative source for epilepsy and seizure information. Today, a Claude-powered assistant named Sage turns that library into a personal conversation for anyone who needs one.

## With Claude, the Epilepsy Foundation achieved:

- 60,000 interactions with Sage, the Foundation's AI epilepsy assistant, in under a year, before any major promotion push
- 2.5x more interactions per session since launch, from 1.2 to 3 since launch, as trust in Sage increased
- Every answer grounded in 3,200 pages of medically reviewed content, with helpline and partner fallbacks
- Half a day to test and deploy each new Claude model, using a 20-question clinical benchmark
- Weekly, at-scale analysis of Sage conversations to surface community needs and refine guardrails

## The challenge

## People getting lost in 20 years of content

[Epilepsy.com](http://epilepsy.com) is the source people turn to when epilepsy enters their lives, whether they have just been diagnosed, are caring for a child, or are supporting a loved one. Somewhere between 8 to 10 million unique visitors come to the site each year, with about 35% coming from outside the United States. It’s trusted because every page is reviewed by the Foundation's expert editorial board, which is drawn from the nation's leading epileptologists and neurologists. These editors write or review every page and ensure that nothing is published without their sign-off. "There's no other place anywhere that has the depth and breadth of content that we have," said Sarah Klein, Chief Engagement Officer at the Epilepsy Foundation.

With such a wealth of content, the challenge arose when visitors needed to find the right information. The library consisted of tens of thousands of pages, and finding the right answer took real persistence. "People got lost in the rabbit hole of what was at one point 50,000 pages of content," Klein recalled. "You would have to be really committed to finding what you needed to find."

No fixed path could fit everyone. "No two people have the same epilepsy journey," Klein added. The site was strong at guiding a visitor to the right page, but building a route through content that met each person where they were proved much harder. At the scariest moments—a parent up at night or someone still absorbing a diagnosis—that gap sent people away from the one expert-vetted source and into the rest of the internet, where nothing had been checked.

Q&A: The Epilepsy Foundation

How the Epilepsy Foundation uses Claude across the organization

[Read more](https://claude.com/customers/epilepsy-foundation-qa)

## The solution

## Choosing a model with empathy built in

To tackle this challenge, the Foundation decided to build Sage. Sage itself is an AI epilepsy assistant: a conversational agent, built on Claude. The team started by treating model selection as a clinical question. They wrote 20 baseline questions, 10 a caregiver might ask and 10 from a person with epilepsy, and had its medical editors and researchers write the answer an expert would give. They ran the same questions through five models and scored each on accuracy, empathy, tone, and recommendations.

What they needed was a model that could handle sensitive medical questions with care, not just return accurate facts. Claude stood out on the dimension that mattered most for a vulnerable audience. "I think it was the empathy at the core of the model," said David-Alexandre Jost, the Foundation's Chief Technology and Innovations Officer. "Even though we didn't bake this into our own prompt, at the core, the Claude models were very empathetic."

On healthcare questions, the difference was just as clear: where other models stayed general, Claude went into the specifics and offered real recommendations. Reaching that feel with another model would have meant heavy prompt engineering. Claude arrived with it, so the team could focus on the experience instead of coaxing the model into the right tone.

With the model selected, where to run Sage was the next decision. The Foundation had already partnered with Amazon Web Services (AWS) and moved to the cloud to build a governed foundation three years prior. Security, access controls, and HIPAA compliance were in place before any application sat on top of it. So when Sage was ready, running it on Claude through Amazon Bedrock was the natural next step. Amazon Bedrock also gave them room to grow: Sage could scale from a few hundred conversations a day to several thousand without rebuilding. And because AWS runs the underlying systems, the Foundation's small team can spend its time on the Sage experience itself. Bedrock is model-agnostic, so the team can move fast when a new Claude model ships.

"When a new version of your Claude models comes out, it's usually available the same day on AWS," Jost said. "We just deploy it into our environment, create a test agent, and that takes about half a day." Getting a brand-new model into a working test in half a day is quick, and Jost noted it would be far harder on a system less tightly integrated. Every new Claude Opus and Claude Haiku release then goes through the same 20-question benchmark, and the same human reviewers, before it reaches production.

## Grounding every answer in vetted content

Sage is built on Claude Haiku 4.5 and runs as a widget on epilepsy.com. Every session is anonymous, and every question is answered only from a knowledge base of 3,200 pages of editorial-board-approved content. When the answer is not there, Sage says so and points the person to the Foundation's Helpline or a partner such as a local Affiliate office or the Rare Epilepsy Network, rather than guessing. "Our goal is to bring hallucinations to zero," as Jost put it. That grounding is what lets the Foundation stand behind every response.

Jost is careful not to call Sage a chatbot. "A chatbot is usually a one-way conversation,” he said. “I have a question, it matches the question to some content and delivers an answer. But Sage wants to have a conversation with you. It will not only answer your question but dig deeper on the why, so it can move you in the right direction." If someone asks about a type of seizure and mentions a pregnancy, Sage asks what medication they take, because that combination can matter.

Over time, the team noticed Sage doing useful things no one had explicitly programmed. For example, Sage began offering guidance pulled from the Foundation's vetted articles, like how to handle a situation at school or how to make the most of a few minutes with a neurologist. "We don't have to prompt everything into our agent," he added. "A lot of this is prompted from the knowledge base we created."

Beneficial Deployments

Accelerate the work that matters most

[Read more](https://www.anthropic.com/news/claude-for-nonprofits)

## The outcome

## 60,000 interactions driven organically

In less than a year, Sage passed 60,000 conversations, before the Foundation had done much to promote it. A typical week now brings about 1,000 unique sessions and 2,700 interactions, comfortably ahead of the team's early goal of 200 a day. Depth grew with volume, too: the average session has grown from 1.2 interactions at launch to 3, and power users go 20 to 25 turns deep in a single session. "People are trusting Sage more and more, because it gives them value in the conversation," Jost said. "Once you have that trust, they share more, and that context helps the next step."

The conversations that stay with the team are the ones the count does not capture. One Sunday night, a mother typed in: "My daughter just had a seizure. How long will she be confused? She's 19." Sage explained what was happening, that the confusion could last minutes to hours, walked her through how to keep her daughter safe, and offered the Helpline.

Another user had lived with uncontrolled seizures for two years, along with severe anxiety and worsening ADHD, and had just left an appointment where her neurologist waved off her symptoms. She spent an hour with Sage working through her history, then asked it to save the chat as a reference for her next visit, because she did not want to forget anything and knew she would. Sage generated a structured document organized by symptom, with a timeline and her questions. "This is actually spectacular," she wrote back. "I'm so glad I found this feature." Jost added that this wasn’t actually a feature, but Sage’s behavior adjusting in real time. "This is Sage creating a tool based on the need of that user," Jost said.

That pattern points to where the Foundation is headed. Power users are treating Sage as a diary, which matters most for community members with cognitive challenges, and the current version cannot carry memory across sessions yet. The next iteration, Sage Next, is being built on [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) with authentication and short-term and long-term memory, so Sage can carry what someone shared weeks ago into a later conversation. "The vision for Sage was to really help you navigate all of that content,” Jost said. “But now Sage is more than this. It's your companion in your epilepsy journey."

## Related stories


### Mercy Corps on what AI makes possible in humanitarian work


### Mercy Corps accelerates global humanitarian response to community feedback with Claude


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
