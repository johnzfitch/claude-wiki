---
title: "Frontier threats red teaming for AI safety \\ Anthropic"
source_url: "https://www.anthropic.com/news/frontier-threats-red-teaming-for-ai-safety"
category: "19-Reference"
fetched_at: "2026-09-10T06:45:56Z"
tags: ["news-research", "search"]
---

# Frontier threats red teaming for AI safety

Jul 26, 2023

  
“Red teaming,” or adversarial testing, is a recognized technique to measure and increase the safety and security of systems. While [previous Anthropic research](red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned.md) reported methods and results for red teaming using crowdworkers, for some time, AI researchers have noted that AI models could eventually obtain capabilities in areas relevant to national security. For example, researchers have [called](https://cdn.openai.com/papers/gpt-4-system-card.pdf) to [measure](https://arxiv.org/abs/2305.15324) and [monitor](https://arxiv.org/abs/2108.12427) [these risks](https://938f895d-7ac1-45ec-bb16-1201cbbc00ae.usrfiles.com/ugd/938f89_74d6e163774a4691ae8aa0d38e98304f.pdf), and have [written](https://arxiv.org/abs/2306.03809) [papers](https://arxiv.org/abs/2304.05332) with evidence of risks. Anthropic CEO Dario Amodei also highlighted this topic in [recent Senate testimony](https://www.judiciary.senate.gov/committee-activity/hearings/oversight-of-ai-principles-for-regulation). With that context, we were pleased to advocate for and join in commitments announced at the White House on July 21 that included “internal and external security testing of \[our\] AI systems” to guard against “some of the most significant sources of AI risks, such as biosecurity and cybersecurity.” However, red teaming in these specialized areas requires intensive investments of time and subject matter expertise.  
  
In this post, we share our approach to “frontier threats red teaming,” high level findings from a project we conducted on biological risks as a test project, lessons learned, and our future plans in this area.  
  
Our goal in this work is to evaluate a baseline of risk, and to create a repeatable way to perform frontier threats red teaming across many topic areas. With respect to biology, while the details of our findings are highly sensitive, we believe it’s important to share our takeaways from this work. In summary, working with [experts](https://www.gryphonscientific.com/), we found that models might soon present risks to national security, if unmitigated. However, we also found that there are mitigations to substantially reduce these risks.  
  
We are now [scaling up this work](https://jobs.lever.co/Anthropic/8f565d59-8831-443a-b72a-cb9ef8ae06b2) in order to reliably identify risks and build mitigations. We believe that improving frontier threats red teaming will have immediate benefits and contribute to [long-term AI safety](core-views-on-ai-safety.md). We have been sharing our findings with government, labs, and other stakeholders, and we’d like to see more independent groups doing this work.

## Conducting frontier threats red teaming

Frontier threats red teaming requires investing significant effort to uncover underlying model capabilities. The most important starting point for us has been working with domain experts with decades of experience. Together, we started by defining threat models: what kind of information is dangerous, how that information is combined to create harm, and what degree of accuracy and frequency is required for it to be dangerous. For example, to create harm, it is often necessary to string together many pieces of accurate information, not just generate a single harmful-sounding output.  
  
Following a well-defined research plan, subject matter and LLM experts will need to collectively spend substantial time (i.e. 100+ hours) working closely with models to probe for and understand their true capabilities in a target domain. For example, domain experts may need to learn the best way to interact with or “jailbreak” models.  
  
An important objective is to build new, automated evaluations based on expert knowledge, and the tooling to run those evaluations to make them repeatable and scalable. However, one challenge is that this information is likely to be sensitive. Therefore, this kind of red teaming requires partnerships with trusted third parties and strong information security protections.

## Findings from red teaming biology

Over the past six months, we spent more than 150 hours with [top biosecurity experts](https://www.gryphonscientific.com/) red teaming and evaluating our model’s ability to output harmful biological information, such as designing and acquiring biological weapons. These experts learned to converse with, jailbreak, and assess our model. We developed quantitative evaluations of model capabilities. The experts used a bespoke, secure interface to our model without the trust and safety monitoring and enforcement tools that are active on our public deployments.  
  
We discovered a few key concerns. The first is that current frontier models can sometimes produce sophisticated, accurate, useful, and detailed knowledge at an expert level. In most areas we studied, this does not happen frequently. In other areas, it does. However, we found indications that the models are more capable as they get larger. We also think that models gaining access to tools could advance their capabilities in biology. Taken together, we think that unmitigated LLMs could accelerate a bad actor’s efforts to misuse biology relative to solely having internet access, and enable them to accomplish tasks they could not without an LLM. These two effects are likely small today, but growing relatively fast. If unmitigated, we worry that these kinds of risks are near-term, meaning that they may be actualized in the next two to three years, rather than five or more.  
  
However, the process of researching these risks also enables the discovery and implementation of mitigations for them. We found, for example, that straightforward changes in the training process meaningfully reduce harmful outputs by enabling the model to better distinguish between harmful and harmless uses of biology (see, for example, our work on [Constitutional AI](constitutional-ai-harmlessness-from-ai-feedback.md)). We also found that classifier-based filters can make it harder for a bad actor to get the kind of multiple, chained-together, and expert-level pieces of information needed to do harm. These are now deployed in our public-facing frontier model, and we’ve identified a list of mitigations at every step of the model development and deployment pathway that we will continue to experiment with.  

## Future Research

At the end of the project, we now have more experiments and evaluations we’d like to run than we started with. For example, we think a very important experiment to repeatedly run will be to measure the speedup that LLMs might provide towards producing harm compared with, for example, a search engine. And we should do so not just with today’s frontier models, but with future ones – next generation models, tool-using models, and multimodal models, for example.  
  
Given our finding that today’s frontier models provide warning of near future risks, frontier model developers should collectively and urgently do more analysis and develop more and stronger mitigations, sharing this information with responsible industry developers so they can add safeguards to their models, and with select government agencies.  
  
We should also prepare for the potential release of models that have not been subject to frontier threats red teaming. We suspect that absent new approaches to mitigation, bad actors could extract harmful biological capabilities with smaller, fine-tuned, or task-specific models adapted from the weights of openly available models if sufficiently capable base models are released.  

## We're scaling up and supporting this work

This empirical work confirms that frontier threats red teaming in areas of national security is important and timely. Current models are only showing the first very early signs of risks of this kind, which makes this our window to evaluate nascent risks and mitigate them before they become acute. It is important to increase efforts before a further generation of models that use new tools. Luckily, there is already a wealth of expertise within national security communities to draw on that can help build threat models, evaluations, and mitigations.  
  
It is also an area that governments are naturally familiar with. This means that national security is a domain where governments, labs, and other stakeholders can collaborate. To start, we are establishing a disclosure process by which labs and other stakeholders can report these risks and their mitigations to other relevant actors. Ultimately, we think it is very important that new third parties be set up to conduct national security evaluations between these stakeholders. These third parties would be impartial and would need to have appropriate safeguards to handle sensitive information.  
  
The frontier threats red teaming research agenda is likely to be useful for other types of risks that appear poised to occur on a longer time scale, such as deception. To identify and mitigate these risks, developers must identify future capabilities that models should not have, measure them, and build mitigations or alignment techniques. As a result, we will learn about alignment, security measures, and “warning shots.”  
  
**Anthropic is building up our frontier threats red teaming research team.** This team will experiment with future capabilities to understand coming risks and build scalable evaluations and mitigations. You can learn more about this work and how to apply to join the team [here](https://jobs.lever.co/Anthropic/8f565d59-8831-443a-b72a-cb9ef8ae06b2). We are looking for particularly mission-driven technical researchers who can rapidly prototype across our infrastructure.  
  
**We are also briefing government and labs on the details of what we have found.** We are open to sharing our present and future findings with appropriate audiences and are piloting a responsible disclosure process between stakeholders in the community to report risks and mitigations. We are particularly interested in supporting other groups – especially labs or new third party evaluation organizations – to do more of this work. If you are one of these stakeholders and are interested, please contact us.


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
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

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
