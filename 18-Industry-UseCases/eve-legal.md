---
title: "Eve Legal Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/eve-legal"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:17Z"
tags: ["api", "case-studies", "enterprise", "security"]
---

# Eve Legal helps plaintiff law firms settle cases 60 days faster with Claude

[Try Claude](https://claude.ai)

Industry:  
Legal

Company size:  
Startup

Product:  
[Claude Platform](https://claude.com/platform/api)[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)

Location:  
North America

60 days faster settlement times

for firms on Eve

Cut engineering triage from three hours to minutes

with its internal Claude-powered developer tool

[Eve Legal](https://www.eve.legal/) is an AI-native platform for plaintiff-side law firms. Roughly two years after launch, over 1,700 firms run on the platform, 500 of them added this quarter alone. Claude runs the platform's heaviest workflows: analyzing a firm's operations and lawyer performance, dissecting case files that stretch to 70,000 pages, and drafting demand letters in each firm's house style. It also monitors thousands of cases across a firm each night, deploying agents based on the findings.

## With Claude, Eve Legal helps plaintiff law firms:

- Settle cases up to 60 days faster
- Increase settlement values by up to 30%
- Take on up to 30 additional cases per lawyer per year
- Turn case files of 2,000 to 100,000 pages into legal work output automatically
- Process 12.5 million documents a month
- Answer, prioritize, and sign potential clients automatically with voice agents
- Cut engineering triage from three hours to minutes with Wall-E, its internal Claude-powered developer tool

## The challenge

## Contingency law runs on hours nobody bills

Most plaintiff firms don't work on retainer. They typically take cases on contingency and get paid only when a case settles, so every hour spent on manual casework is an hour the firm absorbs itself until an outcome. The casework can often be demanding. For example, for personal injury attorneys, a single case file arrives as anywhere from 2,000 to 100,000 pages of unstructured records, which a paralegal previously analyzed line by line to build a medical chronology. It includes the ledger of a client’s injuries, the treatment timeline, what it cost, and what came after, all before any can go out.

That labor puts a hard ceiling on how many cases a firm can take, and clients’ cases that don't justify the hours often go unrepresented. Software previously built for the industry typically focused on tracking the labor as opposed to actually taking on the labor. Eve was started to take on all of the heavy manual labor that the legal profession entails," said Jay Madheswaran, CEO & Co-Founder of Eve.

Claude for Statrtups

Join the founders building on Claude. Access community and resources to accelerate your growth.

[Read more](../15-Claude-AI-Features/programs-startups.md)

## The solution

## A 400-suite benchmark where Claude keeps coming out on top

For Eve, taking on that labor started with a decision about how central AI would be. "We went all-in on AI from the start," Madheswaran said. "It's not, 'How can an attorney work with AI to do this task?' Instead, Eve created a new world where attorneys ask, 'What work do I need to approve that Eve has already done for me?'"

Eve evaluates model candidates against a proprietary benchmark it calls PlaintiffBench: around 420 test suites run against every model the company uses. "We are only willing to move forward on a model when we have confidence in those benchmarks," said Matt Noe, Co-founder and Chief Product Officer.

Claude Opus 4.8 is the production default for the platform's most complex work. Injury cases hinge on timelines, so a model has to reason precisely about when treatments happened and in what order; Noe names Claude's temporal reasoning as the standout. Accuracy across enormous records matters just as much. "Faithfulness and grounding on long documents is another dimension where we measure models, and Claude always stands at the top," Noe noted.

Firms hand Eve their document templates, noting that Eve’s drafts must sound like the firm wrote them. "We found Claude models, in particular Opus, really give us the style adherence of the law firm," Noe said. "It's very personalized to the lawyer's style of writing." Eve routes its hardest scenarios and long, multi-turn tasks to Claude Opus, and uses Claude Sonnet for lighter extraction work.

## One custom harness, routing traffic across three clouds

Inside Eve, those models carry a case through its entire lifecycle. When a new document lands, Claude classifies it, triggers the right workflow, extracts its contents, and builds it into the chronology and downstream drafts, all of which lawyers work with conversationally, chatting with their cases directly inside Eve. Claude also works at the top of the funnel: Eve transcribes calls coming into a firm's call center and scores each one, so intake teams know immediately which cases they can genuinely help with. These workflows earned their autonomy about a year ago, when Eve moved the whole system from a retrieval-augmented generation (RAG) architecture to an agentic one.

Eve built the infrastructure around the models itself. The harness reaches Claude through three routes, the native Claude Platform, Amazon Bedrock, and Google Cloud, switching between them automatically so workflows keep running as the company grows. The same engineering care goes to the output itself. "The work product that plaintiff lawyers ship has to have really high quality," Noe noted. "We really take pride in delivering that quality of product work for them that they can put in front of their clients."

Eve turns the same tooling on itself, building Claude Code into every engineering workflow, including Wall-E, its internal developer productivity system. When a support ticket or production incident hits Slack, Wall-E spins up an isolated environment where Claude agent loops debug the issue and open a merge request, cutting triage from three to four hours down to minutes. Even the finance team runs on it: Claude-built dashboards flag when the cost of a workflow, like writing a demand draft, creeps up week over week.

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## The outcome

## Two months faster to settlement

Firms on Eve settle cases up to 60 days faster, case life cycles run 50% faster, and settlement values are up 30% across customers. "Even the best lawyers at a firm are like, 'Oh, wait, I missed this,'" he said. The gains compound overnight. "You're creating agents powered by Claude that are taking on the work while you are sleeping," Madheswaran explained, "so that when you wake up, you're approving legal work that has been done overnight."

The platform processes more than 12.5 million documents a month. The capacity Eve frees up lets lawyers, in Madheswaran’s words, "get back to practicing law." Firms take on up to 30 additional cases per lawyer per year across personal injury, immigration, and labor and employment. At a firm of 100 or 1,000 people, that compounds into thousands more people represented than before. That reclaimed time goes to the clients themselves. "Eve’s taking on those tasks so that they can actually deal with the human element of what is oftentimes the worst thing that's ever happened to a client," Madheswaran said. "It's nice when altruism and a business model work hand in hand."

None of it is left to chance: a dedicated AI outcomes team guides every new firm through its first 90 days, automating 80% of the work the firm previously did manually. Last month, Eve expanded from managing cases to optimizing firms: attorney workloads, case prioritization, and revenue projections. Next on the roadmap are deeper agentic workflows, multi-step drafting, and agents that learn from a firm's feedback on everything from writing style to case strategy. "Personalizing it per case, per lawyer, and per organization," Noe said. "Those are all the areas where we are pushing towards."

## Related stories


### Spellbook runs 530,000 contract reviews a month with Claude


### EvenUp cuts document drafting from 15 hours to 15 minutes with Claude


### GC AI powers legal workflows for 1,500 companies, saving lawyers 14 hours a week with Claude


### Thomson Reuters CTO on piloting Cowork with Claude Enterprise

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
