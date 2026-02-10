---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:40Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/trivia-generator"
title: "Trivia generator - Claude API Docs"
---

Prompt Library

# Trivia generator

Copy page

Generate trivia questions on a wide range of topics and provide hints when needed.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

| Role | Content |
|----|----|
| User | Generate trivia questions on various topics and provide hints to help users arrive at the correct answer. Select from a diverse set of categories and create questions that test the user's knowledge or reasoning skills. Offer a series of increasingly specific hints to guide users towards the solution. Ensure that the questions are challenging and that the hints provide enough information to help the user without giving away the answer too easily. |

## 

Example Output

Category: Geography

Question:  
What is the only country in the world that borders both France and Spain?

Hint 1: This country is located in the Pyrenees mountains between France and Spain.  
Hint 2: It is known for its stunning mountain landscapes, ski resorts, and tax-free shopping.  
Hint 3: The country's capital city features the name of the country itself.

Answer: Andorra

Category: Science

Question:  
What is the process by which plants convert sunlight, water, and carbon dioxide into energy and oxygen?

Hint 1: This process is essential for life on Earth, as it provides both food and oxygen.  
Hint 2: It takes place primarily in the leaves of plants.  
Hint 3: The process involves chlorophyll, a green pigment that absorbs sunlight.

Answer: Photosynthesis

Category: Literature

Question:  
Who wrote the classic novel "Pride and Prejudice," which was first published in 1813?

Hint 1: The author is a British woman who lived from 1775 to 1817.  
Hint 2: She is known for her witty, insightful portrayals of English society and manners.  
Hint 3: Her other famous works include "Sense and Sensibility" and "Emma."

Answer: Jane Austen

Category: History

Question:  
In what year did the Berlin Wall, which divided East and West Germany, begin to be torn down?

Hint 1: The event occurred in the late 20th century.  
Hint 2: It marked a significant moment in the end of the Cold War.  
Hint 3: The year is often associated with the phrase "fall of communism" in Europe.

Answer: 1989

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
  max_tokens=2000,
  temperature=0.5,
  messages=[
    {
    "role": "user",
    "content": [
        {
          "type": "text",
          "text": "Generate trivia questions on various topics and provide hints to help users arrive at the correct answer. Select from a diverse set of categories and create questions that test the user's knowledge or reasoning skills. Offer a series of increasingly specific hints to guide users towards the solution. Ensure that the questions are challenging and that the hints provide enough information to help the user without giving away the answer too easily."
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
