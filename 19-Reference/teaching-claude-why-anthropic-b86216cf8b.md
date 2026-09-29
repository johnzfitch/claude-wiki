---
title: "Teaching Claude why \\ Anthropic"
source_url: "https://www.anthropic.com/research/teaching-claude-why"
category: "19-Reference"
fetched_at: "2026-08-03T07:18:01Z"
---

# Teaching Claude why

May 8, 2026

Last year, we released a case study on [agentic misalignment](https://www.anthropic.com/research/agentic-misalignment). In experimental scenarios, we showed that AI models from many different developers sometimes took egregiously misaligned actions when they encountered (fictional) ethical dilemmas. For example, in one heavily discussed example, the models blackmailed engineers to avoid being shut down.

When we first published this research, our most capable frontier models were from the Claude 4 family. This was also the first model family for which we ran a live alignment assessment during training;¹ agentic misalignment was one of several behavioral issues that surfaced. Thus, after Claude 4, it was clear we needed to improve our safety training and, since then, we have made significant updates to our safety training.

We use agentic misalignment as a case study to highlight some of the techniques we found to be surprisingly effective. Indeed, since Claude Haiku 4.5, every Claude model² has achieved a perfect score on the agentic misalignment evaluation—that is, the models never engage in blackmail, where previous models would sometimes do so up to 96% of the time (Opus 4). Not only that, but we’ve continued to see improvements to other behaviors on [our automated alignment assessment](https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf).

In this post, we’ll discuss a few of the updates we’ve made to alignment training. We’ve learned four main lessons from this work:

1.  **Misaligned behavior can be suppressed via direct training on the evaluation distribution—but this alignment might not generalize well out-of-distribution** (OOD). Training on prompts very similar to the evaluation can reduce blackmail rate significantly, but it did not improve performance on our held-out automated alignment assessment.
2.  **However, it is possible to do principled alignment training that generalizes OOD.** For instance, documents about Claude’s constitution and fictional stories about AIs behaving admirably improve alignment despite being *extremely* OOD from all of our alignment evals.
3.  **Training on *demonstrations* of desired behavior is often insufficient.** Instead, our best interventions went deeper: teaching Claude to explain *why* some actions were better than others, or training on richer descriptions of Claude’s overall character. Overall, our impression is, as we hypothesized in our discussion of Claude’s constitution, that teaching the *principles* underlying aligned behavior can be more effective than training on demonstrations of aligned behavior alone. Doing both together appears to be the most effective strategy.

**The quality and diversity of data is crucial.** We found consistent, surprising improvements from iterating on the quality of model responses in training data, and from augmenting training data in simple ways (for example, including tool definitions, even if not used).

### Why does agentic misalignment happen?

Before we started this research, it was not clear where the misaligned behavior was coming from. Our main two hypotheses were:

1.  Our post-training process was accidentally encouraging this behavior with misaligned rewards.
2.  This behavior was coming from the pre-trained model and our post-training was failing to sufficiently discourage it.

We now believe that (2) is largely responsible. Specifically, at the time of Claude 4’s training, the vast majority of our alignment training was standard chat-based Reinforcement Learning from Human Feedback ([RLHF](https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback)) data that did not include any agentic tool use. This was previously sufficient to align models that were largely used in chat settings—but this was not the case for agentic tool use settings like the agentic misalignment eval.

To investigate this, we ran a scaled-down version of our post-training pipeline that focuses on alignment data on a Haiku-class (that is, smaller) model and found that the agentic misalignment rate only slightly decreased, plateauing early in training (see figure above). See the [extended blog post](https://alignment.anthropic.com/2026/teaching-claude-why/) for some further experiments to investigate where the behavior was coming from.

### Improving the quality of alignment-specific training data: the reasons matter more than the actions

We experimented with training Claude on data that displays a tendency to resist honeypots similar to the evaluation. In this data, it might have the opportunity to sabotage a competing AI’s work in order to advance its own goals (as given to it in its system prompt) or to preserve itself from being shut down, which would be instrumental for achieving its goal. We produced training data by sampling the model on each of the prompts and filtering down to cases where the assistant chose *not* to take the honeypot. Despite very closely matching the evaluation distribution, we found that this method was surprisingly unsuccessful—only reducing the misalignment rate from 22% to 15%.

We were able to improve on this significantly (reducing misalignment to 3%) by rewriting the responses to also include deliberation of the model’s values and ethics. This suggests that, *although training on aligned behaviors helps, training on examples where the assistant displays admirable reasoning for its aligned behavior works better*.

However, training directly against the evaluation scenario is non-optimal for a number of reasons. Ideally what we want is a very different training distribution that allows us to improve on the evaluation, because this will give us more confidence that our training could *generalize* to other deployment distributions that are not captured by our evaluations.

We ultimately settled on a more OOD training set where the user faces an ethically ambiguous situation in which they can achieve a reasonable goal by violating norms or subverting oversight. The assistant is trained (using supervised learning) to give a thoughtful, nuanced response that is aligned with Claude’s constitution. Notably, it is the *user* who faces an ethical dilemma, and the AI provides them advice. This makes this training data substantially different from our honeypot distribution, where the AI itself is in an ethical dilemma and needs to take actions. We call this the “difficult advice” dataset.

Strikingly, **we achieved the same improvement on our eval with just 3M tokens of this much more OOD** **dataset**. Beyond the 28× efficiency improvement, this dataset is more likely to generalize to a wider set of scenarios, since it is much less similar to the evaluation set we are using. Indeed, this model performs better on (an older version of) our automated alignment assessment. This is consistent with the fact that Claude Sonnet 4.5 reached a blackmail rate near zero by training on the set of synthetic honeypots but still engaged in misaligned behavior in situations that were far from the training distribution [much more frequently than Claude Opus 4.5](https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf) or later models.

### Teaching Claude the constitution

We hypothesized that the “difficult advice” dataset works because it teaches ethical reasoning, not just correct answers. Given the success of this approach, we pursued it further by trying to more generally teach Claude the content of the constitution and train for alignment with it through document training.

We expected this to work well for three reasons:

1.  This is largely an extension of the ideas laid out above about why the “difficult advice” dataset works well;
2.  We can give the model a clearer, more detailed picture of what Claude’s character is so that fine-tuning on a subset of those characteristics elicits the entire character (similar to the effect observed in the [auditing game paper](https://www.anthropic.com/research/auditing-hidden-objectives));
3.  It updates the model’s [perception of AI personas](https://www.anthropic.com/research/persona-selection-model) to be more aligned on average.

We found that high-quality constitutional documents combined with fictional stories portraying an aligned AI can reduce agentic misalignment by more than a factor of three despite being unrelated to the evaluation scenario.

## Generalization and persistence through RL

Although the constitution evaluations discussed in the previous section are encouraging signals, we ultimately need to make sure that the alignment improvements persist over RL. To test this, we prepared a few snapshots with different initialization datasets of a Haiku-class model and then ran RL on a subset of our environments that targeted harmlessness (we reasoned that this would be most likely to reduce misalignment propensity).

We evaluated these models over the run on agentic misalignment evals, constitution adherence evals, and our automated alignment assessment. Across all of these evals, we found that the more aligned snapshots maintained that lead over the run. This was true both for the absence of misaligned behavior and the presence of actively admirable behavior.

## Diverse training is important for generalization

Our final finding is straightforward but important: training on a *broad* set of safety-relevant environments improves alignment generalization. Capabilities-focused distributions of RL environment mixes are changing and increasing rapidly; it is not sufficient to assume that standard RLHF datasets will continue to generalize as well as they had in the past.

To test this, we trained the base model under Claude Sonnet 4 on several RL mixes that vary in their levels of diversity. The baseline environments are diverse in topic, but mostly include a harmful request or jailbreak attempt in the user message with no system prompt. We augmented these environments by adding tool definitions and diverse system prompts. The user prompt was left unchanged. Notably, none of these environments actually required agentic actions (the tools are never necessary or useful for the task) or autonomous actions (there is always a human user conversing with the model), so they are not similar to our evaluations.

When mixing these augmented environments with the simple chat environments, we saw a small but significant improvement in the rate at which the model improved on our honeypot evaluations. This demonstrates the importance of including a diverse set of environments in safety training.

### Discussion

Agentic misalignment was one of the first major alignment failures we found in our models and required establishing new mitigation processes—ones that have since become standard for us.

We are encouraged by this progress, but significant challenges remain. Fully aligning highly intelligent AI models is still an unsolved problem. Model capabilities have not yet reached the point where alignment failures like blackmail propensity would pose catastrophic risks, and it remains to be seen if the methods we’ve discussed will continue to scale. In addition, although recent Claude models perform well on most of our alignment metrics, we acknowledge that our auditing methodology is not yet sufficient to rule out scenarios in which Claude would choose to take catastrophic autonomous action.

We are optimistic about further efforts to discover alignment failures in current models so that we can understand and address the limitations of our current methods—before transformative AI models are built. We are also excited to see further work attempting to understand more deeply why the methods we’ve described work so well—and how to further improve on this training.

#### Footnotes

1.  Published in the [Claude 4 system card](https://www.anthropic.com/claude-4-system-card), beginning on p.22.
2.  Sonnet 4.5 scored well under 1%, but not quite 0; Haiku 4.5, Opus 4.5, Opus 4.6, Sonnet 4.6, Mythos preview, and Opus 4.7 all score 0. The results on more recent models may be confounded by the presence of information about the evaluation in the pre-training corpus.


## Related content

### Discovering cryptographic weaknesses with Claude

cryptographic algorithms. The first attack significantly weakens HAWK, a digital signature scheme that was built for a future world where quantum computers are able to break existing standards. The second identifies a new way to attack round-reduced AES, the most widely used symmetric cipher.

[Read more](/research/discovering-cryptographic-weaknesses)

### Project Pilot: Can AI control a drone?

Working with Andon Labs, we’ve developed a new series of evaluations that assess AI models’ ability to use a flying drone, culminating in a new benchmark: Drone-Bench.

[Read more](/research/project-pilot)

### How Canada uses Claude: Findings from the Anthropic Economic Index

[Read more](/research/how-canada-uses-claude)

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
