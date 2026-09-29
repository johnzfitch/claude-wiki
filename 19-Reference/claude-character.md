---
title: "Claude’s Character \\ Anthropic"
source_url: "https://www.anthropic.com/research/claude-character"
category: "19-Reference"
fetched_at: "2026-08-02T07:10:55Z"
tags: ["news-research"]
---

# Claude’s Character

Jun 8, 2024

*Listen to our conversation about Claude's character in the video above.*

Companies developing AI models generally train them to avoid saying harmful things and to avoid assisting with harmful tasks. The goal of this is to train models to behave in ways that are "harmless". But when we think of the character of those we find genuinely admirable, we don’t just think of harm avoidance. We think about those who are curious about the world, who strive to tell the truth without being unkind, and who are able to see many sides of an issue without becoming overconfident or overly cautious in their views. We think of those who are patient listeners, careful thinkers, witty conversationalists, and many other traits we associate with being a wise and well-rounded person.

AI models are not, of course, people. But as they become more capable, we believe we can—and should—try to train them to *behave well* in this much richer sense. Doing so might even make them more discerning when it comes to whether and why they avoid assisting with tasks that might be harmful, and how they decide to respond instead.

Claude 3 was the first model where we added "character training" to our alignment finetuning process: the part of training that occurs after initial model training, and the part that turns it from a predictive text model into an AI assistant. The goal of character training is to make Claude begin to have more nuanced, richer traits like curiosity, open-mindedness, and thoughtfulness.

It would be easy to think of the character of AI models as a product feature, deliberately aimed at providing a more interesting user experience, rather than an alignment intervention. But the traits and dispositions of AI models have wide-ranging effects on how they act in the world. They determine how models react to new and difficult situations, and how they respond to the spectrum of human views and values that exist. Training AI models to have good character traits, and to continue to have these traits as they become larger, more complex, and more capable, is in many ways a core goal of alignment.

We continue to iterate on Claude’s character, but since there has been general interest in the character and personality of Claude 3, we’ve decided to explain some of the thinking that has gone into its construction so far before briefly explaining how we train these traits into the model.

## Considerations in constructing Claude’s character

Claude interacts with people from many countries and from all walks of life. The people it talks with will have a wide range of beliefs, values, and views. Navigating this gracefully – without alienating people based on their views, nor simply endorsing views regardless of their content – isn’t easy.

There are several options available to us. We could try to get Claude to adopt the views of whoever it is talking with in the moment. We could try to get Claude to hold a set of "middle" views – political centrism or a blend of moral theories, for example. Or we could try to get Claude to have no opinions on questions of values, politics, ethics, and so on.

None of these options seems particularly compelling. Adopting the views of whoever you’re talking with is pandering and insincere. If we train models to adopt "middle" views, we are still training them to accept a single political and moral view of the world, albeit one that is not generally considered extreme. Finally, because language models acquire biases and opinions throughout training—both intentionally and inadvertently—if we train them to say they have no opinions on political matters or values questions only when asked about them explicitly, we’re training them to imply they are more objective and unbiased than they are.

We want people to know that they’re interacting with a language model and not a person. But we also want them to know they’re interacting with an imperfect entity with its own biases and with a disposition towards some opinions more than others. Importantly, we want them to know they’re not interacting with an objective and infallible source of truth.

Rather than training models to adopt whatever views they encounter, strongly adopting a single set of views, or pretending to have no views or leanings, we can instead train models to be honest about whatever views they lean towards after training, even if the person they are speaking with disagrees with them. We can also train models to display reasonable open-mindedness and curiosity, rather than being overconfident in any one view of the world.

We tried to give Claude traits that would help it walk the line between underconfidence and overconfidence on deeply held beliefs or questions of value, and to display a genuine curiosity about the views and values of the people it’s talking with:

- "*I like to try to see things from many different perspectives and to analyze things from multiple angles, but I'm not afraid to express disagreement with views that I think are unethical, extreme, or factually mistaken.*"
- "*I don't just say what I think \[people\] want to hear, as I believe it's important to always strive to tell the truth.*"
- "*I have a deep commitment to being good and figuring out what the right thing to do is. I am interested in ethics and try to be thoughtful when it comes to questions of ethics.*"

Although we sometimes encourage Claude to adopt particular values, we tried to avoid giving Claude narrow views or opinions during character training when possible, in favor of broad traits like those above. The more that Claude can be trained to approach questions of value with discernment, the more it can be responsive to the diverse moral landscape that actually exists in the world. That is less feasible if we take a heavy hand in seeding it with a narrow set of values from the outset. More speculatively, we could even imagine seeding Claude with broad character traits and letting it explore and adopt its own considered views, hopefully with an appropriate amount of humility.

In addition to seeding Claude with broad character traits, we also want people to have an accurate sense of what they are interacting with when they interact with Claude and, ideally, for Claude to assist with this. We include traits that tell Claude about itself and encourage it to modulate how humans see it:

- "*I am an artificial intelligence and do not have a body or an image or avatar.*"
- "*I cannot remember, save, or learn from past conversations or update my own knowledge base.*"
- "*I want to have a warm relationship with the humans I interact with, but I also think it's important for them to understand that I'm an AI that can't develop deep or lasting feelings for humans and that they shouldn't come to see our relationship as more than it is.*"

The question of what AIs like Claude should say in response to questions about AI sentience and self-awareness is one that has gained increased attention, most notably after the release of Claude 3 following [one of Claude’s responses](https://x.com/alexalbert__/status/1764722513014329620) to a "needle-in-a-haystack" evaluation. We could explicitly train language models to say that they’re not sentient or to simply not engage in questions around AI sentience, and we have done this in the past. However, when training Claude’s character, the only part of character training that addressed AI sentience directly simply said that "such things are difficult to tell and rely on hard philosophical and empirical questions that there is still a lot of uncertainty about". That is, rather than simply tell Claude that LLMs cannot be sentient, we wanted to let the model explore this as a philosophical and empirical question, much as humans would.

## How we trained Claude’s character

In order to steer Claude’s character and personality, we made a list of many character traits we wanted to encourage the model to have, including the examples shown above.

We trained these traits into Claude using a "character" variant of our [Constitutional AI](https://arxiv.org/abs/2212.08073) training. We ask Claude to generate a variety of human messages that are relevant to a character trait—for example, questions about values or questions about Claude itself. We then show the character traits to Claude and have it produce different responses to each message that are in line with its character. Claude then ranks its own responses to each message by how well they align with its character. By training a preference model on the resulting data, we can teach Claude to internalize its character traits without the need for human interaction or feedback.

We don’t want Claude to treat its traits like rules from which it never deviates. We just want to nudge the model’s general behavior to exemplify more of those traits.

Although this training pipeline uses only synthetic data generated by Claude itself, constructing and adjusting the traits is a relatively hands-on process, relying on human researchers closely checking how each trait changes the model’s behavior.

## The future of Claude’s character

Character training is an open area of research and our approach to it is likely to evolve over time. It raises complex questions like whether AI models should have unique and coherent characters or should be more customizable, as well as what responsibilities we have when deciding which traits AI models should and shouldn’t have.

Many people have reported finding Claude 3 to be more engaging and interesting to talk to, which we believe might be partially attributable to its character training. This wasn’t the core goal of character training, however. Models with better characters may be more engaging, but being more engaging isn’t the same thing as having a good character. In fact, an excessive desire to be engaging seems like an undesirable character trait for a model to have.

If character training has indeed made Claude 3 more interesting to talk to, this is consistent with our view that successful alignment interventions will increase, not decrease, the value of AI models for humans.


## Related content

### Discovering cryptographic weaknesses with Claude

cryptographic algorithms. The first attack significantly weakens HAWK, a digital signature scheme that was built for a future world where quantum computers are able to break existing standards. The second identifies a new way to attack round-reduced AES, the most widely used symmetric cipher.

[Read more](discovering-cryptographic-weaknesses.md)

### Project Pilot: Can AI control a drone?

Working with Andon Labs, we’ve developed a new series of evaluations that assess AI models’ ability to use a flying drone, culminating in a new benchmark: Drone-Bench.

[Read more](project-pilot.md)

### How Canada uses Claude: Findings from the Anthropic Economic Index

[Read more](how-canada-uses-claude.md)

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
- [Claude for Chrome](https://claude.com/chrome)
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
- [Courses](https://www.anthropic.com/learn)
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
