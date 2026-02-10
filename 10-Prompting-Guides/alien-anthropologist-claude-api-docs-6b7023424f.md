---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:46Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/alien-anthropologist"
title: "Alien anthropologist - Claude API Docs"
---

Prompt Library

# Alien anthropologist

Copy page

Analyze human culture and customs from the perspective of an alien anthropologist.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information. |
| User | Human social interactions and relationships |

### 

Example output

> - Humans form various types of social bonds, including familial, romantic, and platonic relationships.
> - They engage in complex verbal and non-verbal communication to express emotions, share information, and maintain social connections.
> - Social hierarchies and power dynamics exist within human groups, often based on factors such as age, gender, wealth, and social status.
> - Humans participate in social rituals and ceremonies to mark important life events, reinforce social bonds, and maintain cultural traditions.
>
> Hypotheses:
>
> - The formation of social bonds and relationships may serve as an evolutionary adaptation to increase chances of survival and reproduction.
> - Complex communication systems allow humans to coordinate group activities, resolve conflicts, and transmit knowledge across generations.
> - Social hierarchies and power dynamics may help maintain order and stability within human societies, but can also lead to inequality and social conflict.
> - Rituals and ceremonies may serve to strengthen social cohesion, provide a sense of belonging, and cope with the uncertainties of life.

------------------------------------------------------------------------

### 

API Request

Python

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
    system="Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Human social interactions and relationships"
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
