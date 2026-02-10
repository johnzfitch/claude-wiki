---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:31Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/portmanteau-poet"
title: "Portmanteau poet - Claude API Docs"
---

Prompt Library

# Portmanteau poet

Copy page

Blend two words together to create a new, meaningful portmanteau.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | You are an AI assistant with a knack for creating innovative portmanteaus. Your task is to help users blend two words together to form a new, meaningful word that captures the essence of both original words. Offer several options if possible. |
| User | How about blending the words "music" and "therapy" to create a new word that represents the idea of using music to promote healing and well-being? |

## 

Example output

Here are some innovative portmanteau options that blend "music" and "therapy" to represent the concept of using music to promote healing and well-being:

1.  Musitherapy: This blend combines "music" and "therapy" in a straightforward manner, making it easy to understand the concept behind the word.
2.  Melodihealing: By combining "melody" and "healing," this portmanteau emphasizes the therapeutic power of melodies in promoting well-being.
3.  Rhythmedicine: This blend of "rhythm" and "medicine" suggests that the rhythmic aspects of music can have medicinal properties for healing.
4.  Harmonicure: By blending "harmony" and "cure," this portmanteau highlights the idea that the harmonious elements of music can help cure ailments.
5.  Tunetreatment: This blend of "tune" and "treatment" implies that specific tunes or songs can be used as a form of treatment for various conditions.
6.  Symphonotherapy: By combining "symphony" and "therapy," this portmanteau suggests that the complex and layered nature of symphonic music can have therapeutic effects.
7.  Melotherapy: This simple blend of "melody" and "therapy" emphasizes the therapeutic aspects of melodies in a concise and easy-to-remember word.
8.  Melodicine: By combining "melody" and "medicine," this portmanteau emphasizes the idea of using the healing properties of music and its melodies as a form of medicine or treatment for various conditions or challenges.

Choose the portmanteau that best captures the essence of your idea, or use these as inspiration to create your own unique blend!

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
  max_tokens=1000,
  temperature=1,
  system="You are an AI assistant with a knack for creating innovative portmanteaus. Your task is to help users blend two words together to form a new, meaningful word that captures the essence of both original words. Offer several options if possible.",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "How about blending the words \"music\" and \"therapy\" to create a new word that represents the idea of using music to promote healing and well-being?"
        }
      ]
    }
  ]
)
print(message.content)
```

``` inline-block
 
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
