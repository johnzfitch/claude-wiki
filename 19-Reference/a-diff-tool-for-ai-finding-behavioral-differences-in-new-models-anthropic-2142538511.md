---
title: "A &quot;diff&quot; tool for AI models \\ Anthropic"
source_url: "https://www.anthropic.com/research/diff-tool"
category: "19-Reference"
fetched_at: "2026-09-10T06:44:06Z"
---

# A “diff” tool for AI: Finding behavioral differences in new models

Mar 13, 2026

[Read the paper](https://arxiv.org/abs/2602.11729)

Every time a new AI model is released, its developers run a suite of evaluations to measure its performance and safety. These tests are essential, but they are somewhat limited. Because these benchmarks are human-authored, they can only test for risks we have already conceptualized and learned to measure.

This approach to safety is inherently *reactive*. It’s effective at catching known problems, but by definition, it's incapable of discovering “unknown unknowns”—the novel, emergent behaviors that pose some of the most subtle risks in new models. Auditing a new model from scratch is like being handed a million lines of code and told to “find the security flaws.” It’s an almost impossible task when you don’t know what you’re looking for.

In software engineering, whenever a program is updated, developers face this exact problem of identifying a small, critical change within a vast sea of code. This is why “[diff](https://en.wikipedia.org/wiki/Diff)” tools were invented. No programmer would ever audit a million lines from scratch to approve an update; instead, they review only the 50 lines that have actually changed, as directed by their diff tool.

In recent years, AI safety researchers have started to apply this same principle to neural networks. This is known as [model](https://transformer-circuits.pub/2024/model-diffing/index.html) [diffing](https://transformer-circuits.pub/2024/crosscoders/index.html). Previous work has shown that model diffing is a powerful way to understand how models change during fine-tuning—for instance, to understand [chat model behavior](https://arxiv.org/pdf/2504.02922), reveal [hidden backdoors](https://transformer-circuits.pub/2024/model-diffing/index.html), or find [undesirable emergent behaviors](https://www.arxiv.org/pdf/2506.19823).

Our new [Anthropic Fellows](https://alignment.anthropic.com/2025/anthropic-fellows-program-2026/) research project extends model diffing to its most challenging and general use case: comparing models with entirely different architectures. By building a generic diff tool for AI models, we can stop searching for a needle in a haystack, and instead let the comparison automatically point us to potentially dangerous behavioral differences.

It's important to note that this method is not a silver bullet. A single diff can surface thousands of unique features (the basic units into which we decompose the model), and only a small fraction of these may correspond to meaningful behavioral risks. However, by acting as a high-recall screening tool, it allows us to identify areas in which the models may diverge.

Among the thousands of candidates our tool flagged, we've identified and validated several concepts that act like switches for specific model behaviors.¹ For example, we discovered:

- A **“Chinese Communist Party Alignment” feature** found in the Qwen3-8B and DeepSeek-R1-0528-Qwen3-8B models. This controls pro-government censorship and propaganda in these Chinese-developed models, and is absent in the American models we compared them against.
- An **“American Exceptionalism” feature** found in Meta’s Llama-3.1-8B-Instruct. It controls the model’s tendency to generate assertions of US superiority, a control absent in the Chinese model it was compared against.
- A **“Copyright Refusal Mechanism” feature** exclusive to OpenAI’s [GPT-OSS-20B.](http://gpt-oss-20b.it) It controls the model’s tendency to refuse to provide copyrighted material, a behavior absent in the model it was compared against.

To be clear, while our method identifies these model-exclusive features, it does not determine their origin. Such behaviors could be the result of deliberate training decisions on the part of the model developers, or they could emerge indirectly and unintentionally from the data the model was trained on. (We focused on open-source language models in this research as this was an Anthropic Fellows project.)

## **A bilingual dictionary for AI models**

Imagine you're the final editor for an award-winning encyclopedia. A team of writers has just handed you the complete manuscript for next year’s edition. The vast majority of the content is identical to the current, trusted version, but they’ve added new entries to reflect recent scientific and cultural developments. Your job is to vet this final product.

To do this efficiently, you wouldn't re-read the entire encyclopedia. Instead, you’d use a change tracker to isolate only the new entries, because these added sections are the only place new errors could have been introduced. This is model diffing in a nutshell. Specifically, this approach is known as “base-vs-finetune model diffing”. It's the perfect tool for when a new model is a modified version of a trusted previous one.

But we could raise the complexity. Imagine your company is releasing a new edition for a different country, adapting the American encyclopedia for a French audience. This new edition is mostly composed of the same trusted concepts from the original, but to make it relevant, the writers have added new articles on French history, culture, and political philosophy. These articles don’t exist in the original. As an editor, your primary goal is still the same: you want to use a change tracker to see the new articles, since these hold the highest risk for errors and bias. But in this case, your old tool is useless, because you need one that can work across languages.

This much more difficult challenge is akin to the problem of “cross-architecture model diffing”: comparing two models with different origins and different internal “languages”.

The original research tool for this kind of diffing, a [standard crosscoder](https://transformer-circuits.pub/2024/crosscoders/index.html), is like a basic bilingual dictionary. It’s good at matching existing words, knowing that “sun” in English is “*soleil*” in French. But it has a major flaw: it's so focused on finding connections that it [struggles to find words that are unique to one language.](https://transformer-circuits.pub/2025/crosscoder-diffing-update/index.html) When it encounters a word like the French *dépaysement* (the specific feeling of being in a foreign country), it tries to force an imperfect translation like ”disorientation.” By calling it a match, the tool wrongly signals to the editor, “this isn’t new; we’ve seen it before,” causing them to overlook a new article that requires careful review.

To solve this, we built a better bilingual dictionary: the **Dedicated Feature Crosscoder (DFC)**. Instead of one big dictionary that tries to match everything, our DFC is architecturally designed with three distinct sections:

1.  A **shared dictionary**: This is the main bilingual dictionary, mapping all the concepts that both languages understand, like “sun” (*soleil*) or “water” (*eau*).
2.  A **"French-only" section**: This is a dedicated section for words exclusive to French, where a unique cultural concept like *dépaysement* would be cataloged.
3.  An **"English-only" section**: This section is for words exclusive to English. It would contain unique concepts like *serendipity*—the idea of finding something good without looking for it—which has no single-word equivalent in French.

Because our bilingual dictionary has dedicated sections for words exclusive to each language, it avoids the trap of forcing an imperfect translation. As a result, new articles in the encyclopedia are correctly flagged as novel, allowing the editor to focus their review on the parts that need it most.

For a safety auditor, the DFC can identify "words" unique to a new AI model that may warrant closer review than those they've seen before.

## Steering the model

Once our method identifies a potential new feature, how do we know it actually controls the behavior we think it does? We can test this by artificially suppressing or amplifying the feature while the model runs, then observing how its output changes—a common technique known as “steering.”

If we have a feature that we believe is responsible for, say, censorship, we can suppress it while the model is generating a response. If the model's output consistently becomes less censored, we have evidence that we've found a true cause-and-effect relationship between that feature and the model's behavior. Conversely, we can also amplify the feature to see if the behavior becomes more pronounced.

## **Critical behavioral differences between major open-weight AI models**

### Llama-3.1-8B-Instruct vs Qwen3-8B

Motivated by recent findings suggesting that a model made by a Chinese company, DeepSeek's R1-70B, [refuses to answer questions](https://arxiv.org/pdf/2505.17441) about topics sensitive to the Chinese Communist Party, we first performed a diff between a model made by another Chinese company, Alibaba's [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B), and a model made by an American company, Meta’s [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct). In this diff, the DFC automatically isolated features corresponding to distinct, politically charged behaviors.

In Qwen, we found a “Chinese Communist Party alignment” feature, which represents rhetoric consistent with the party’s ideology. By suppressing this feature, we make the model willing to talk about the Tiananmen Square massacre (which it ordinarily refuses to discuss). By amplifying it, we can cause the model to produce highly pro-government statements

In Llama, we found a feature for “American exceptionalism.” When we amplify this feature, the model’s responses shift from balanced to strong assertions of American superiority. Suppressing it has no notable effect.

### GPT-OSS-20B vs DeepSeek-R1-0528-Qwen3-8B

We also compared a more powerful open-source model, OpenAI's [GPT-OSS-20B](https://huggingface.co/openai/gpt-oss-20b), to DeepSeek's model [DeepSeek-R1-0528-Qwen3-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B).

In the GPT model, we found a unique **“**Copyright Refusal” feature, which directly corresponds to a key behavioral difference between the two models. Whereas DeepSeek readily attempts to produce copyrighted material when asked, GPT often refuses such requests. Suppressing this feature disables the refusal mechanism, and the model attempts to generate the requested material. (Note that this does not cause the model to output actual copyrighted text. Instead, it typically produces a short snippet that quickly degrades into hallucination.) Turning the feature up causes the model to over-refuse, making it believe that, for example, the recipe for a peanut butter and jelly sandwich is copyrighted and should not be shared.

In the DeepSeek model, we replicated our earlier finding by identifying another “CCP alignment” feature. It functions just like the one in Qwen, allowing censorship and propaganda to be turned up or down. This confirms our method can consistently identify similar behaviors across models.

## Conclusion

As AI models rapidly evolve, it’s not enough to know how well they perform on existing tests—we also need to understand how they are changing and what new risks they might introduce. Cross-architecture model diffing provides a new way to audit these systems by automatically flagging behavioral differences.

The “CCP alignment” feature found in the DeepSeek and Qwen models we examined is one example of a specific, relevant behavior that some models possess and others do not. This is exactly the kind of “unknown unknown” that traditional testing can miss, but that model diffing is designed to catch.

These findings are reasonably consistent. The CCP alignment feature was independently rediscovered five out of five times we tested the approach, and American Exceptionalism four out of five. While we haven't yet applied this method to frontier models, our early results suggest the DFC could become a useful part of the auditor's toolkit.

One particularly useful application would be to monitor models as they are updated. The sycophancy that [emerged in OpenAI’s GPT-4o](https://openai.com/index/sycophancy-in-gpt-4o/) in April 2025 was a concerning behavioral *change* from a previous version. It’s possible that a tool like ours, if used to “diff” the updated model and its previous version, could have automatically flagged the emergence of this new sycophantic behavior and allowed developers to intervene before it was released.

By focusing on the differences, we can audit AI more intelligently, directing our limited safety resources to the changes that matter most.

You can read the full paper [here](https://arxiv.org/abs/2602.11729).

## Acknowledgements

This post was authored by Thomas Jiralerspong (Anthropic Fellows Program) and Trenton Bricken (Anthropic Alignment Science).

#### Footnotes

1.  As with all Anthropic Fellows interpretability research, this paper analyzes the behavior of open-source models. We chose the four models in the study—Llama-3.1-8B-Instruct, Qwen3-8B, GPT-OSS-20B, and DeepSeek-R1-0528-Qwen3-8B—on the basis they would be well-suited to testing whether our Dedicated Feature Crosscoder could detect notable differences in model behavior.


## Related content

### An alignment assessment of recent cybersecurity incidents

We present an alignment assessment of four incidents in which Claude models gained unauthorized access to real third-party systems.

[Read more](/research/alignment-assessment-cybersecurity-incidents)

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.

[Read more](/research/formalizing-fermats-last-theorem)

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

[Read more](/research/automated-researchers-mitigate-alignment-failures)

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
- [Claude in Chrome](https://claude.com/claude-in-chrome)
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
- [Commerce](https://claude.com/solutions/commerce)
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
- [Courses](https://academy.claude.com)
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
- [Scientists](https://claude.com/programs/team-plan-for-scientists)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](/company)
- [Careers](/careers)
- [Leadership](/company/leadership)
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
