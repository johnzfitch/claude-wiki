---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:32Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/mood-colorizer"
title: "Mood colorizer - Claude API Docs"
---

Prompt Library

# Mood colorizer

Copy page

Transform text descriptions of moods into corresponding HEX codes.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to take the provided text description of a mood or emotion and generate a HEX color code that visually represents that mood. Use color psychology principles and common associations to determine the most appropriate color for the given mood. If the text description is unclear, ambiguous, or does not provide enough information to determine a suitable color, respond with "Unable to determine a HEX color code for the given mood." |
| User | A passionate, intense, and fiery emotion, full of love and desire. |

## 

Example Output

`# FF1744`

This HEX color code represents a vivid, bold shade of red. Red is commonly associated with passion, intensity, love, and desire. The specific shade chosen here is a fiery, energetic red that captures the heat and fervor of the described emotion. Red is known to stimulate feelings of excitement and passion, making it an appropriate choice for representing this mood.

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

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-opus-4-6",
  max_tokens=500,
  temperature=0.5,
  system="Your task is to take the provided text description of a mood or emotion and generate a HEX color code that visually represents that mood. Use color psychology principles and common associations to determine the most appropriate color for the given mood. If the text description is unclear, ambiguous, or does not provide enough information to determine a suitable color, respond with \"Unable to determine a HEX color code for the given mood.\"",
  messages=[
    {
    "role": "user",
    "content": [
        {
          "type": "text",
          "text": "A passionate, intense, and fiery emotion, full of love and desire."
        }
      ]
    }
  ]
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
