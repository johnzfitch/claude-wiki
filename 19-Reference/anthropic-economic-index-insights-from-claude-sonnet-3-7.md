---
title: "Anthropic Economic Index: Insights from Claude 3.7 Sonnet \\ Anthropic"
source_url: "https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7"
category: "19-Reference"
fetched_at: "2026-08-26T06:29:23Z"
tags: ["news-research"]
---

# Anthropic Economic Index: Insights from Claude 3.7 Sonnet

Mar 27, 2025

Last month, we launched the [Anthropic Economic Index](https://www.anthropic.com/economic-index)—a new initiative where we’re regularly releasing data and research aimed at understanding AI's effects on labor markets and the economy over time.

Today, we’re releasing our second research report from the Index, covering usage data on Claude.ai following the launch of [Claude 3.7 Sonnet](claude-3-7-sonnet.md)—our newest and most capable model with strengths in agentic coding and a new “extended thinking” mode.

Briefly, our latest results are the following:

- Since the launch of Claude 3.7 Sonnet, we’ve observed a rise in the share of usage for coding, as well as educational, science, and healthcare applications;
- People use Claude 3.7 Sonnet’s new “extended thinking” mode predominantly for technical tasks, including those associated with occupations like computer science researchers, software developers, multimedia animators, and video game designers;
- We're releasing data on augmentation / automation breakdowns on a task- and occupation-level. For example, tasks associated with copywriters and editors show the highest amount of *task iteration*, where the human and model co-write something together. By contrast, tasks associated with translators and interpreters show among the highest amounts of *directive* behavior—where the model completes the task with minimal human involvement.

In addition, we’re releasing a first-of-its-kind bottom-up taxonomy of usage on Claude.ai. This new dataset covers 630 granular categories ranging from “Help resolve household plumbing, water, and maintenance issues” to “Provide guidance on battery technologies and charging systems.” We hope this bottom-up taxonomy will be useful for researchers, and reveal use-cases that might be missed by top-down approaches which map usage onto a list of predefined tasks.

The datasets for these analyses are [freely available to download](https://huggingface.co/datasets/Anthropic/EconomicIndex/).

Read on for more details on our findings.

## What’s changed since the launch of Claude 3.7 Sonnet?

Last month, we introduced Claude 3.7 Sonnet, our most capable model yet with an “extended thinking mode”. We reran our [previous analysis](the-anthropic-economic-index.md) on data from the 11 days following the launch, covering 1 million anonymized Claude.ai Free and Pro conversations. The vast majority of the data we analyzed was from Claude 3.7 Sonnet, as it is set as the default on Claude.ai and our mobile app.

As a reminder, our privacy-preserving analysis tool, [Clio](clio.md), maps each conversation to one of 17,000 tasks in the U.S. Department of Labor’s O\*NET database. We then look at the overall patterns in the occupations and high-level occupational categories associated with those tasks.

When looking at the breakdown of these 1 million conversations, we see that the proportion of usage in several occupational categories has increased modestly, including coding, education and the sciences. While this increase in coding usage was expected due to Claude 3.7 Sonnet’s improved scores on coding benchmarks, the increase in these other categories could reflect either ongoing diffusion of AI throughout the economy, novel applications of coding to those domains, or unexpected capability improvements in the model.

##  How are people using extended thinking mode?

Claude 3.7 Sonnet features a new “extended thinking” mode which, when activated by the user, enables the model to think for longer when answering more complex questions.

Our analysis reveals that Claude 3.7 Sonnet's extended thinking mode is predominantly used in technical and creative problem-solving contexts. Tasks associated with computer and information research scientists lead with almost 10% using extended thinking, followed by software developers at around 8%. Tasks associated with digital creative roles like multimedia artists (~7%) and video game designers (~6%) also show substantial usage.

While these early usage patterns reveal insights about when people choose to use extended thinking mode, many important questions remain about this new model capability. To enable further research in this space, we’re releasing a new dataset that maps each O\*NET task to its associated thinking mode fraction. This dataset is available on our [Hugging Face page](https://huggingface.co/datasets/Anthropic/EconomicIndex/).

## How does augmentation vs. automation vary by task and occupation?

In our last report, we analyzed how AI usage varied between *augmentative* uses, like learning or iterating on an output, and *automative* uses, like asking the model to directly complete a task or debug errors. Our analysis shows the balance of augmentation and automation is essentially unchanged in our new data, with augmentation still comprising 57% of usage. However, we did see some change in *types* of automation and augmentation uses—for example, we saw *learning* interactions, where the user asks Claude for information or explanation about different topics, rise from ~23% to ~28%.  

  
We received a number of requests via our [researcher input form](https://docs.google.com/forms/d/e/1FAIpQLSfDEdY-mT5lcXPaDSv-0Ci1rSXGlbIJierxkUbNB7_07-kddw/viewform) to release automation and augmentation data at the level of tasks and occupations. We do just that in this report, providing this data on our [Hugging Face page](https://huggingface.co/datasets/Anthropic/EconomicIndex/).

When splitting the data by high-level occupational categories, we find some categories are highly augmentative; for example, Community and Social Service tasks, which includes education and guidance counseling, approach 75% augmentation. At the other end of the extreme, tasks associated with production or computer and mathematical occupations, we see the balance skew closer to 50-50%. We don’t see any occupational categories where automation dominates.

  
Getting more granular, we can also look at specific occupations within these occupational categories, as well as tasks associated with that occupation. For example, tasks associated with copywriters and editors show the highest amount of *task iteration*, where the user iterates on various writing and editing tasks with the model. By contrast, tasks associated with Translators and Interpreters show among the highest amounts of *directive* behavior—where the model is used for translating documents with minimal human involvement. Note that the O\*NET descriptions may not be optimally representative of what Claude is being used for—for example, while we see usage in the occupation “fine artists, including painters, sculptors, and illustrators,” Claude is probably used far more for creating digital art than for painting or sculpture.

## A bottom-up taxonomy of usage on Claude.ai

Our research so far has relied on the O\*NET dataset of tasks and occupations, which was created and maintained by the US Department of Labor. While O\*NET covers a very large number of tasks, O\*NET may not be the best taxonomy to describe the capabilities of general purpose models which can be used for tasks which are not present in O\*NET—and thus might be missed by our analysis.

To address this gap, we’re releasing a new bottom-up dataset of user activity patterns on Claude.ai. This dataset was also created with Clio, and uses the same dataset of anonymized conversations used for the above analysis, meaning that it enables comparisons between top-down and bottom-up approaches. It consists of 630 granular clusters, with associated descriptions, prevalence metrics, and automation/augmentation breakdowns, organized into three levels of hierarchy.

While we leave detailed analysis of this dataset to future work, we highlight a few particularly interesting clusters:

- Help with water management systems and infrastructure projects
- Create physics-based simulations with interactive visualization capabilities
- Help me with font selection, implementation, and troubleshooting
- Help me create or improve job application materials
- Provide guidance on battery technologies and charging systems
- Help with time zone handling in code and databases

## Conclusion

As models continue to advance, so too must our measurement of their economic impacts. In our second report, covering data since the launch of Claude 3.7 Sonnet, we find relatively modest increases in coding, education, and scientific use cases, and no change in the balance of augmentation and automation. We find that Claude’s new extended thinking mode is used with the highest frequency in technical domains and tasks, and identify patterns in automation / augmentation patterns across tasks and occupations. We release datasets for both of these analyses.

In the coming months, we aim to continue tracking these metrics and developing new ones as capabilities improve and models continue to be applied across the economy.

## Work with us

If you’re interested in [working](https://www.anthropic.com/jobs) at Anthropic to research the effects of AI on the labor market, we encourage you to apply for our Societal Impacts Research Scientist and Research Engineer roles, as well as our Economist role.

## Appendix

We share a few additional results and technical details in this appendix.

### Task Curve

We also recompute the “depth of task usage” plot from our original paper. We find generally a very similar curve to our first analysis. If anything we see slightly less area under the curve for the newer model—perhaps owing to an increase in concentration in our sample of conversations towards coding. That said, while we haven’t seen a dramatic change in this curve over the last two months, we will continue to monitor as model capabilities and product surfaces continue to advance.

### Full change across occupational categories

###  Results for other interaction modes

## Additional methodological details

While we mainly follow the methodology of our original report, we make a few changes which we document here for transparency:

- In contrast to our last report, we do not filter based on whether conversations are relevant to an occupational category. Instead, we simply filter out conversations that flagged our safety classifiers. We find these approaches lead to similar results as our original analysis, while preserving more data that we can release via our bottom-up taxonomy of usage.
- We use Claude 3.7 Sonnet in place of all cases where we previously used Claude 3.5 Sonnet. We found that using our newer model increased the accuracy of classifications according to the internal benchmarks we use to assess Clio’s accuracy.


## Related content

### Funding better evaluations of AI’s impact on wellbeing

We’re launching a \$5 million grant program to fund independent research into how AI impacts users’ wellbeing.

[Read more](wellbeing-research-grants.md)

### How Claude’s text watermark works

In this article, we share answers to some of the questions we’ve received about how our chosen watermarking method works, whether it affects Claude’s outputs, and why we’re making this change.

[Read more](claude-text-watermark.md)

### Improving Fable 5's biology safeguards

We’re making updates to Claude Fable 5’s biology safeguards in a way that substantially reduces false positives. Fable 5 users will now experience many fewer “fallbacks”—where the system switches to a less capable model after they make a biology-related query.

[Read more](improving-fable-5-s-biology-safeguards.md)

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
- [Research Labs](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

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
