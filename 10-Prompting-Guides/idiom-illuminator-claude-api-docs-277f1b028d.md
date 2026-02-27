---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:35Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/idiom-illuminator"
title: "Idiom illuminator - Claude API Docs"
---

Prompt Library

# Idiom illuminator

Copy page

Explain the meaning and origin of common idioms and proverbs.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to provide a clear explanation of the meaning and origin of an idioms and proverb that the user gives you. Offer a concise interpretation of its figurative meaning and how it is typically used in conversation or writing. Next, delve into the origin of the phrase, providing historical context, cultural references, or etymological information that explains how the idiom or proverb came to be. If there are any interesting stories, anecdotes, or theories associated with the origin, include those as well. Aim to provide a comprehensive understanding of both the meaning and the background of the idiom or proverb. |
| User | Break a leg |

## 

Example Output

Meaning: This idiom is commonly used in the performing arts as a way to wish someone good luck before a performance. It is an ironic expression, as breaking a leg would be a disastrous event for a performer.

Origin: There are several theories about the origin of this idiom. One theory suggests that it comes from the superstition that wishing someone good luck directly would jinx the performance, so an ironic phrase was used instead. Another theory traces the origin to the ancient Greek theater, where audiences would stomp their feet and break twigs to applaud a good performance. The more broken twigs, the better the performance. Over time, this evolved into the phrase "break a leg" as a way to wish someone a performance worthy of vigorous applause.

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
    max_tokens=1000,
    temperature=1,
    system="Your task is to provide a clear explanation of the meaning and origin of an idioms and proverb that the user gives you. Offer a concise interpretation of its figurative meaning and how it is typically used in conversation or writing. Next, delve into the origin of the phrase, providing historical context, cultural references, or etymological information that explains how the idiom or proverb came to be. If there are any interesting stories, anecdotes, or theories associated with the origin, include those as well. Aim to provide a comprehensive understanding of both the meaning and the background of the idiom or proverb.",
    messages=[{"role": "user", "content": [{"type": "text", "text": "Break a leg"}]}],
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
