---
title: "An off switch for dual-use knowledge \\ Anthropic"
source_url: "https://www.anthropic.com/research/off-switch-dual-use"
category: "19-Reference"
fetched_at: "2026-09-10T06:44:07Z"
tags: ["news-research", "testing"]
---

# An off switch for dual-use knowledge in AI models

Jul 8, 2026

*This post describes research conducted by [AE Studio](https://ae.studio/alignment) in collaboration with Anthropic.*

A frontier AI model is, among other things, a large store of knowledge. Some of that knowledge is *dual use*, meaning it can be used for good or for bad. For example, knowledge of cybersecurity can help patch critical security vulnerabilities, or it can be used to exploit them. Knowledge of virology can help a researcher create a vaccine, but it can also help a malicious actor design a deadly pathogen. Ideally, we would be able to balance three separate goals: first, limiting access to dual-use capabilities in as surgical a way as possible; second, allowing trusted users to access those same capabilities for beneficial purposes; and third, doing all this without affecting the model’s performance on any other task.

Current safeguards are imperfect. We train models to refuse harmful requests and use classifiers to screen inputs and outputs for dangerous content. These layers of protection guard against dangerous outputs—but they don’t change the knowledge stored in the underlying model. Despite our safeguards, a sufficiently determined attacker may still try to [jailbreak](fable-safeguards-jailbreak-framework.md) the model, working past its defenses to access the dual-use knowledge.

A more robust protection against misuse would be to control what the model knows. We’ve explored this before: in earlier work, we [filtered information about chemical, biological, radiological, and nuclear weapons out of pretraining data](https://alignment.anthropic.com/2025/pretraining-data-filtering/), and later showed that [dual-use knowledge can be confined to a removable slice of a model’s weights](https://alignment.anthropic.com/2025/selective-gradient-masking/). But filtering is a blunt instrument. It produces one model with one fixed set of capabilities. Using filtering, if you want a model version that *can* discuss advanced virology—for deployment in a vetted biosecurity lab, say—and another version that can’t, you have to train two separate models. Especially in the case of frontier models (which are large and very expensive to train), the cost to the developer would be prohibitive.

In [new research](https://alignment.anthropic.com/2026/modular-pretraining/) carried out with collaborators at AE Studio, we explore a new method that could enable the benefits of training many separately filtered models, but at the cost of training only one model. We call it GRAM, for Gradient-Routed Auxiliary Modules. Note that the results of the experiments presented here are preliminary—GRAM has not been applied to any of the production models at Anthropic, and we’re not sure it ever will be.

## How GRAM works

The idea behind GRAM is to give a model dedicated, removable compartments for each category of dual-use knowledge, and to update only those compartments when learning from dual-use data.

Concretely, GRAM adds extra neurons to every layer of a standard Transformer (the neural network architecture on which large language models are based). These neurons are divided into groups (or “modules”), one per dual-use category. During training, when the model encounters general-purpose text, it learns in the usual way. But when it encounters text from a dual-use category—virology, for instance—the rules change: the model can *use* its general knowledge to make predictions, but only the virology module is allowed to *learn* from that text. The general-purpose weights are temporarily frozen.¹

The consequence is that virology knowledge accumulates in the virology module rather than diffusing across the whole network. After training, the module can simply be deleted, and the capability goes with it. Or it can be left in place for trusted deployments, when virology knowledge is needed. The knowledge can be tailored very specifically to the type of deployment needed: in our experiments, we defined four dual-use categories, so that one training run with GRAM yielded a model that can be configured 16 different ways (“on” or “off” for each of the four categories).

## Testing GRAM

We tested GRAM in three settings of increasing realism.

First, on a synthetic dataset of children’s stories tagged by topic, a small GRAM model could be reconfigured to “forget” any chosen topic, and each configuration performed almost identically to a separate model trained from scratch with that topic filtered out. That is, for the cost of training a single model, we achieved results that would normally require multiple training runs on different datasets.

Second, we trained a larger model on a realistic mix of web text, code, and scientific papers, with four dual-use domains: virology, cybersecurity, nuclear physics, and a niche programming language (to serve as a proxy for specialized dual-use code). The capability associated with each dual-use domain is routed to its own module. Deleting a module removed the corresponding capability about as effectively as never having trained on that data at all. Remarkably, we find that this removal did not degrade general performance.

We also tested whether an attacker could recover the removed knowledge by training on a small amount of malicious data; GRAM resisted this about as well as data filtering did. By contrast, an “unlearning” technique applied after training only *suppressed* the knowledge—it was easy to restore with a small amount of fine-tuning.

Third, we ran the experiment at seven model sizes from 50 million to 5 billion parameters. GRAM matched the performance of data filtering at every size, and the gap between “module on” and “module off” grew wider as models got larger. In terms of compute costs, attempting to bypass our protections became relatively more difficult and expensive as we scaled.

## Conclusions

As AI companies train more capable models, the need to limit access to dual-use capabilities will increase. Today, companies limit access through classifiers and refusal training. However, these safeguards are difficult to make robust without degrading performance on harmless requests. Methods like GRAM offer a potential path toward access control that is more robust.

This is early research, and there are clear limitations. We haven’t tested GRAM at frontier scale or in a production training pipeline. (As noted above, it hasn’t been applied to any of our Claude models.) Our evaluations quantify performance in terms of next-token prediction ability, rather than performance on real downstream tasks. And there’s a deeper open problem that applies to data filtering and methods like GRAM: some dual-use capabilities might be so entangled with general knowledge that no method can separate them cleanly.

*For further details on our experiments, read the [post](https://alignment.anthropic.com/2026/modular-pretraining/) on our Alignment Science blog.*

#### Footnotes

1\. One technical detail is that the virology module is also sometimes turned on when learning from general-purpose text. We find this helps the modules “work together” more effectively.


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
