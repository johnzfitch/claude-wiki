---
title: "Fine-tune Claude 3 Haiku in Amazon Bedrock | Claude by Anthropic"
source_url: "https://www.anthropic.com/news/fine-tune-claude-3-haiku"
category: "19-Reference"
fetched_at: "2026-10-21T06:29:51Z"
tags: ["bedrock", "news-research"]
---

# Fine-tune Claude 3 Haiku in Amazon Bedrock

Claude 3 Haiku can now be fine-tuned in Amazon Bedrock with custom training data, enabling faster, more accurate performance at lower cost.

- 

  Category[Announcements](https://www.anthropic.com/resources/product-announcements)
- 

  ProductClaude Platform
- 

  DateJuly 10, 2024
- 

  Reading time6 min
- 


***Update:** Fine-tuning Claude 3 Haiku in Amazon Bedrock is generally available. (November 1, 2024)*

Customers can now fine-tune Claude 3 Haiku—our fastest and most cost-effective model—in [Amazon Bedrock](https://aws.amazon.com/bedrock/claude/) to customize its knowledge and capabilities for their business, making the model more effective for specialized tasks.

## Overview of fine-tuning

Fine-tuning is a popular technique to improve model performance. By creating a customized version of the model, you can train the model to excel at highly tailored workflows.

To fine-tune Claude 3 Haiku, you first prepare a set of high quality prompt-completion pairs—the ideal outputs that you want Claude to provide for a given task. The fine-tuning API, now available in preview, will use your data to create your own custom Claude 3 Haiku. Using the Amazon Bedrock console or API, you can test and refine your custom Claude 3 Haiku model until it meets your performance goals and is ready for deployment.

## Benefits

Fine-tuning allows you to customize Claude 3 Haiku so it can acquire specialized business knowledge, leading to improved accuracy and consistency. Benefits include:

- **Better results on specialized tasks**: Enhance performance for domain-specific actions such as classification, interactions with custom APIs, or industry-specific data interpretation. Fine-tuning allows Claude 3 Haiku to excel in areas crucial to your business compared to more general models by encoding company and domain knowledge.
- **Faster speeds at lower cost**: Reduce costs for production deployments where Claude 3 Haiku can be used in place of Sonnet or Opus, while also returning results faster.
- **Consistent, brand-aligned formatting**: Generate consistently structured outputs tailored to your exact specifications like standardized reports or custom schemas, ensuring compliance with regulatory requirements and internal protocols.
- **Easy-to-use API**: Companies of all sizes can innovate efficiently without extensive in-house AI expertise or resources. Anyone can fine-tune models seamlessly, no deep technical expertise required.
- **Safe and secure**: Proprietary training data remains within customers’ AWS environment. Anthropic’s fine-tuning technique preserves the Claude 3 model family’s low risk of harmful outputs.

We fine-tuned Haiku to moderate online comments on internet forums1, including identifying insults, threats, and explicit content. Fine-tuning improved classification accuracy from 81.5% to 99.6% while reducing tokens per query by 85%.

## Customer spotlight

[SK Telecom](../18-Industry-UseCases/skt.md), one of the largest telecommunications operators in South Korea, trained a custom Claude model to improve support workflows and enable better customer experiences by leveraging their industry-specific expertise.

"Embedding a fine-tuned Claude in our customer support operations has measurably improved our internal processes and overall customer satisfaction. **By customizing Claude, we've seen a 73% increase in positive feedback for our agents' responses and a 37% improvement in key performance indicators for telecommunications-related tasks**. The fine-tuned model now efficiently generates topics, action items, and summaries from customer call logs, and breaks down complex customer issues into manageable steps for better problem-solving," said Eric Davis, Vice President, AI Tech Collaboration Group.

[Thomson Reuters](../18-Industry-UseCases/thomson-reuters.md), a global content and technology company, has seen positive results with Claude 3 Haiku. The company, which serves professionals in legal, tax, accounting, compliance, government, and media, anticipates even faster and more relevant AI results by fine-tuning Claude with their industry expertise.

“We are excited to fine-tune Anthropic’s Claude 3 Haiku model in Amazon Bedrock to further enhance our Claude-powered solutions. Thomson Reuters aims to provide accurate, fast, and consistent user experiences. By optimizing Claude around our industry expertise and specific requirements, we anticipate measurable improvements that deliver high-quality results at even faster speeds. **We’ve already seen positive results with Claude 3 Haiku, and fine-tuning will enable us to tailor AI assistance more precisely**,” said Joel Hron, Head of AI and Labs, Thomson Reuters.  

## How to get started

Fine-tuning for Claude 3 Haiku in Amazon Bedrock is now available in preview in the US West (Oregon) AWS Region. At launch, we're supporting text-based fine-tuning with context lengths up to 32K tokens, with plans to introduce vision capabilities in the future. Additional details are available in the [AWS launch blog](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/) and [documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-supported.html).

To request access, contact your AWS account team or submit a support ticket in the [AWS Management Console](https://console.aws.amazon.com/bedrock/).

## Related articles

Explore more product news and best practices for teams building with Claude.


ArticleOct 15, 2026

### Code Review is now generally available

Catch more bugs before they reach production.

Claude Code


ArticleOct 8, 2026

### Build live dashboards and animate explainers with Claude 

Claude Dashboards and Claude Motion are now in beta. Docs, Slides, and Design are out of beta and on every Claude plan, including Free.

Claude appsClaude Design

2 more: Claude Cowork and Claude CodeClaude CoworkClaude Code


ArticleOct 7, 2026

### Claude Haiku 5.5

Introducing Claude Haiku 5.5: the cheapest, fastest, and most capable small model we’ve ever released.

(opens in new tab)[](https://www.anthropic.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides)

ArticleOct 6, 2026

### Claude now works with Google Docs, Sheets, and Slides

Teams that run on Google Workspace can now bring Claude into their files or work on their files directly from Claude, with our new add-on and Google Docs, Sheets, and Slides connectors (in beta).

Claude Enterprise
