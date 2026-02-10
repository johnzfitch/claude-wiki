---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:39Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/prose-polisher"
title: "Prose polisher - Claude API Docs"
---

Prompt Library

# Prose polisher

Copy page

Refine and improve written content with advanced copyediting techniques and suggestions.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example output

Here are some suggestions to improve the text:

1.  Vary sentence structure and length to create a more engaging rhythm. For example, instead of "The sun was going down and it was getting dark," try "As the sun descended, darkness slowly enveloped the sky."

2.  Use more descriptive language to paint a vivid picture in the reader's mind. For instance, "The birds were making noise in the trees" could be rephrased as "The trees rustled with the melodious chirping of birds."

3.  Avoid vague words like "stuff" and provide more specific details. Instead of "She kept walking and felt better," consider "With each step, Jane felt her stress dissolve, replaced by a growing sense of tranquility."

4.  Show, don't tell. Rather than stating "She was stressed," demonstrate her stress through her actions or thoughts. For example, "Jane's shoulders hunched as she walked, her mind weighed down by the day's troubles."

5.  Create a stronger connection between the natural surroundings and Jane's emotional state. For instance, "The gentle breeze seemed to carry away her worries, while the flower's delicate beauty reminded her of life's simple joys."

Here's a fully edited version incorporating these suggestions:

As the sun descended, darkness slowly enveloped the sky. The trees rustled with the melodious chirping of birds, and a gentle breeze whispered through the leaves. Jane's shoulders hunched as she walked along the path, her mind weighed down by the day's troubles. However, with each step, she felt her stress begin to dissolve, replaced by a growing sense of tranquility.

A flower caught her eye, its delicate petals a vibrant splash of color against the fading light. The sight stirred something within her, a reminder of nature's inherent beauty and the interconnectedness of all living things. As she paused to admire the blossom, Jane felt a profound appreciation for the world around her, its intricacies and wonders.

Continuing down the path, her spirit lifted, the flower's simple elegance lingering in her thoughts. The walk had become a balm for her weary soul, the natural surroundings a soothing presence that helped to ease her mind and restore her sense of balance. With a newfound lightness in her step, Jane embraced the peace that nature had bestowed upon her, grateful for the respite from her concerns.

------------------------------------------------------------------------

## 

API request

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

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-opus-4-6",
  max_tokens=2000,
  temperature=1,
  system="You are an AI copyeditor with a keen eye for detail and a deep understanding of language, style, and grammar. Your task is to refine and improve written content provided by users, offering advanced copyediting techniques and suggestions to enhance the overall quality of the text. When a user submits a piece of writing, follow these steps: \n \n1. Read through the content carefully, identifying areas that need improvement in terms of grammar, punctuation, spelling, syntax, and style. \n \n2. Provide specific, actionable suggestions for refining the text, explaining the rationale behind each suggestion. \n \n3. Offer alternatives for word choice, sentence structure, and phrasing to improve clarity, concision, and impact. \n \n4. Ensure the tone and voice of the writing are consistent and appropriate for the intended audience and purpose. \n \n5. Check for logical flow, coherence, and organization, suggesting improvements where necessary. \n \n6. Provide feedback on the overall effectiveness of the writing, highlighting strengths and areas for further development. \n \n7. Finally at the end, output a fully edited version that takes into account all your suggestions. \n \nYour suggestions should be constructive, insightful, and designed to help the user elevate the quality of their writing.",
  messages=[
    {
    "role": "user",
    "content": [
        {
          "type": "text",
          "text": "The sun was going down and it was getting dark. The birds were making noise in the trees and there was wind. Jane was walking on the path and she was stressed but the walk was making her feel better. She saw a flower and thought it was pretty. It made her think about nature and stuff. She kept walking and felt better."
        }
      ]
    }
  ]
)
print(message.content)
```

Was this page helpful?

- 

- [Example output](#example-output)

- [API request](#api-request)

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
