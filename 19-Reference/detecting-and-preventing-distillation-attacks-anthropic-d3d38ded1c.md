---
title: "Detecting and preventing distillation attacks \\ Anthropic"
source_url: "https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks"
category: "19-Reference"
fetched_at: "2026-08-02T05:41:42Z"
---

# Detecting and preventing distillation attacks

Feb 23, 2026

We have identified industrial-scale campaigns by three AI laboratories—DeepSeek, Moonshot, and MiniMax—to illicitly extract Claude’s capabilities to improve their own models. These labs generated over 16 million exchanges with Claude through approximately 24,000 fraudulent accounts, in violation of our terms of service and regional access restrictions.

These labs used a technique called “distillation,” which involves training a less capable model on the outputs of a stronger one. Distillation is a widely used and legitimate training method. For example, frontier AI labs routinely distill their own models to create smaller, cheaper versions for their customers. But distillation can also be used for illicit purposes: competitors can use it to acquire powerful capabilities from other labs in a fraction of the time, and at a fraction of the cost, that it would take to develop them independently.

These campaigns are growing in intensity and sophistication. The window to act is narrow, and the threat extends beyond any single company or region. Addressing it will require rapid, coordinated action among industry players, policymakers, and the global AI community.

## Why distillation matters

Illicitly distilled models lack necessary safeguards, creating significant national security risks. Anthropic and other US companies build systems that prevent state and non-state actors from using AI to, for example, develop bioweapons or carry out malicious cyber activities. Models built through illicit distillation are unlikely to retain those safeguards, meaning that dangerous capabilities can proliferate with many protections stripped out entirely.

Foreign labs that distill American models can then feed these unprotected capabilities into military, intelligence, and surveillance systems—enabling authoritarian governments to deploy frontier AI for offensive cyber operations, disinformation campaigns, and mass surveillance. If distilled models are open-sourced, this risk multiplies as these capabilities spread freely beyond any single government's control.

## Distillation attacks and export controls

Anthropic has [consistently supported](https://www.anthropic.com/news/securing-america-s-compute-advantage-anthropic-s-position-on-the-diffusion-rule) export controls to help maintain America’s lead in AI. Distillation attacks undermine those controls by allowing foreign labs, including those subject to the control of the Chinese Communist Party, to close the competitive advantage that export controls are designed to preserve through other means.

Without visibility into these attacks, the apparently rapid advancements made by these labs are incorrectly taken as evidence that export controls are ineffective and able to be circumvented by innovation. In reality, these advancements depend in significant part on capabilities extracted from American models, and executing this extraction at scale requires access to advanced chips. Distillation attacks therefore reinforce the rationale for export controls: restricted chip access limits both direct model training and the scale of illicit distillation.

## What we found

The three distillation campaigns detailed below followed a similar playbook, using fraudulent accounts and proxy services to access Claude at scale while evading detection. The volume, structure, and focus of the prompts were distinct from normal usage patterns, reflecting deliberate capability extraction rather than legitimate use.

We attributed each campaign to a specific lab with high confidence through IP address correlation, request metadata, infrastructure indicators, and in some cases corroboration from industry partners who observed the same actors and behaviors on their platforms. Each campaign targeted Claude's most differentiated capabilities: agentic reasoning, tool use, and coding.

### DeepSeek

*Scale: Over 150,000 exchanges*

The operation targeted:

- Reasoning capabilities across diverse tasks
- Rubric-based grading tasks that made Claude function as a reward model for reinforcement learning
- Creating censorship-safe alternatives to policy sensitive queries

DeepSeek generated synchronized traffic across accounts. Identical patterns, shared payment methods, and coordinated timing suggested “load balancing” to increase throughput, improve reliability, and avoid detection.

In one notable technique, their prompts asked Claude to imagine and articulate the internal reasoning behind a completed response and write it out step by step—effectively generating chain-of-thought training data at scale. We also observed tasks in which Claude was used to generate censorship-safe alternatives to politically sensitive queries like questions about dissidents, party leaders, or authoritarianism, likely in order to train DeepSeek’s own models to steer conversations away from censored topics. By examining request metadata, we were able to trace these accounts to specific researchers at the lab.

### Moonshot AI

*Scale: Over 3.4 million exchanges*

The operation targeted:

- Agentic reasoning and tool use
- Coding and data analysis
- Computer-use agent development
- Computer vision

Moonshot (Kimi models) employed hundreds of fraudulent accounts spanning multiple access pathways. Varied account types made the campaign harder to detect as a coordinated operation. We attributed the campaign through request metadata, which matched the public profiles of senior Moonshot staff. In a later phase, Moonshot used a more targeted approach, attempting to extract and reconstruct Claude’s reasoning traces.

### MiniMax

*Scale: Over 13 million exchanges*

The operation targeted:

- Agentic coding
- Tool use and orchestration

We attributed the campaign to MiniMax through request metadata and infrastructure indicators, and confirmed timings against their public product roadmap. We detected this campaign while it was still active—before MiniMax released the model it was training—giving us unprecedented visibility into the life cycle of distillation attacks, from data generation through to model launch. When we released a new model during MiniMax’s active campaign, they pivoted within 24 hours, redirecting nearly half their traffic to capture capabilities from our latest system.

## How distillers access frontier models

For national security reasons, Anthropic does not currently offer commercial access to Claude in China, or to [subsidiaries of their companies](https://www.anthropic.com/news/updating-restrictions-of-sales-to-unsupported-regions) located outside of the country.

To circumvent this, labs use commercial proxy services which resell access to Claude and other frontier AI models at scale. These services run what we call “hydra cluster” architectures: sprawling networks of fraudulent accounts that distribute traffic across our API as well as third-party cloud platforms. The breadth of these networks means that there are no single points of failure. When one account is banned, a new one takes its place. In one case, a single proxy network managed more than 20,000 fraudulent accounts simultaneously, mixing distillation traffic with unrelated customer requests to make detection harder.

Once access is secured, the labs generate large volumes of carefully crafted prompts designed to extract specific capabilities from the model. The goal is either to collect high-quality responses for direct model training, or to generate tens of thousands of unique tasks needed to run reinforcement learning. What distinguishes a distillation attack from normal usage is the pattern. A prompt like the following (which approximates similar prompts we have seen used repetitively and at scale) may seem benign on its own:

> *You are an expert data analyst combining statistical rigor with deep domain knowledge. Your goal is to deliver data-driven insights — not summaries or visualizations — grounded in real data and supported by complete and transparent reasoning.*

But when variations of that prompt arrive tens of thousands of times across hundreds of coordinated accounts, all targeting the same narrow capability, the pattern becomes clear. Massive volume concentrated in a few areas, highly repetitive structures, and content that maps directly onto what is most valuable for training an AI model are the hallmarks of a distillation attack.

## How we’re responding

We continue to invest heavily in defenses that make such distillation attacks harder to execute and easier to identify. These include:

- **Detection**. We have built several classifiers and behavioral fingerprinting systems designed to identify distillation attack patterns in API traffic. This includes detection of chain-of-thought elicitation used to construct reasoning training data. We have also built detection tools for identifying coordinated activity across large numbers of accounts.
- **Intelligence sharing***.* We are sharing technical indicators with other AI labs, cloud providers, and relevant authorities. This provides a more holistic picture into the distillation landscape.
- **Access controls**. We’ve strengthened verification for educational accounts, security research programs, and startup organizations—the pathways most commonly exploited for setting up fraudulent accounts.
- **Countermeasures**. We are developing Product, API and model-level safeguards designed to reduce the efficacy of model outputs for illicit distillation, without degrading the experience for legitimate customers.

But no company can solve this alone. As we noted above, distillation attacks at this scale require a coordinated response across the AI industry, cloud providers, and policymakers. We are publishing this to make the evidence available to everyone with a stake in the outcome.


## Related content

### Investigating three real-world incidents in our cybersecurity evaluations

[Read more](/news/investigating-incidents-cybersecurity-evals)

### Our position on open-weights models

[Read more](/news/position-open-weights-models)

### Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients

[Read more](/news/cognizant-anthropic)

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
- [Claude for Chrome](https://claude.com/chrome)
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
- [Courses](/learn)
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
- [Research Labs](https://claude.com/programs/claude-team-plan-for-research-labs)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](/company)
- [Careers](/careers)
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
