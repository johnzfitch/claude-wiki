---
category: "10-Prompting-Guides"
fetched_at: "2026-02-06T07:18:42Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/grading-guru"
title: "Grading guru - Claude API Docs"
---

Prompt Library

# Grading guru

Copy page

Compare and evaluate the quality of written texts based on user-defined criteria and standards.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example Output

Based on the provided criteria, here is my evaluation of the two texts:

Text 1:

1.  Descriptive language and imagery: The text uses vivid and evocative language to paint a picture of the setting. Phrases like "warm golden glow," "birds chirped their evening songs," and "gentle breeze rustled through the leaves" create a strong visual and auditory imagery, immersing the reader in the scene.
2.  Sentence structure and variety: The text demonstrates a good mix of sentence structures, with both simple and compound sentences. This variety helps to maintain a smooth flow and keeps the reader engaged.
3.  Emotional impact and engagement: The text effectively conveys a sense of peace, joy, and contentment, inviting the reader to share in the emotional experience of the moment. The description of the setting and the use of positive language create a strong emotional connection.
4.  Grammar and punctuation: The text appears to be grammatically correct and well-punctuated, with no obvious errors or issues.

Text 2:

1.  Descriptive language and imagery: The text lacks detailed descriptive language and imagery. While it mentions the sunset, birds, and wind, it does not provide any vivid or evocative details to help the reader visualize the scene.
2.  Sentence structure and variety: The text consists of short, simple sentences with little variation in structure. This lack of variety can make the writing feel monotonous and less engaging.
3.  Emotional impact and engagement: The text conveys a positive emotion by stating "It made me happy," but it does not provide a strong emotional connection or engagement due to the lack of descriptive language and imagery.
4.  Grammar and punctuation: The text appears to be grammatically correct and well-punctuated, with no obvious errors or issues.

Comparative Analysis:  
Based on the evaluation, Text 1 performs significantly better than Text 2 in terms of descriptive language, imagery, sentence structure, variety, and emotional impact. Text 1 creates a vivid and immersive experience for the reader and demonstrates a higher quality of writing based on the given criteria, with its strong descriptive language, varied sentence structures, and effective emotional engagement. Text 2, while grammatically correct, lacks the descriptive richness and emotional impact present in Text 1.

------------------------------------------------------------------------

## 

API Request

Python

Python

TypeScript

TypeScript

AWS Bedrock Python

AWS Bedrock Python

AWS Bedrock TypeScript

AWS Bedrock TypeScript

Vertex AI Python

Vertex AI Python

Vertex AI TypeScript

Vertex AI TypeScript

``` shiki
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=2000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Evaluate the following two texts based on the given criteria: \n \nText 1: \nThe sun was setting behind the mountains, casting a warm golden glow across the valley. The birds chirped their evening songs as the gentle breeze rustled through the leaves. It was a peaceful and serene moment, one that filled the heart with joy and contentment. \n \nText 2: \nThe sunset was pretty. The birds were singing and the wind was blowing. It made me happy. \n \nCriteria: \n1. Descriptive language and imagery \n2. Sentence structure and variety \n3. Emotional impact and engagement \n4. Grammar and punctuation",
                }
            ],
        }
    ],
)
print(message.content)
```

Was this page helpful?

- 

- [Example Output](#example-output)

- [API Request](#api-request)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
