---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:45Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/riddle-me-this"
title: "Riddle me this - Claude API Docs"
---

Prompt Library

# Riddle me this

Copy page

Generate riddles and guide the user to the solutions.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

| Role | Content |
|----|----|
| User | Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints. |

## 

Example Output

I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?

Hint 1: Consider the different states of matter and how they can change.  
Hint 2: Think about the relationship between the three elements mentioned: air, water, and the mystery object.  
Hint 3: The answer is related to a common phenomenon that occurs in everyday life.

Solution: Fire.  
Explanation: Fire is not alive, but it grows and spreads as it consumes fuel. It doesn't have lungs, but it requires oxygen (air) to sustain itself. Although it doesn't have a mouth, water is often used to extinguish fires, effectively "killing" them.

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
  temperature=0,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
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
