---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:49Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/direction-decoder"
title: "Direction decoder - Claude API Docs"
---

Prompt Library

# Direction decoder

Copy page

Transform natural language into step-by-step directions.

Copy page

> Copy this prompt into our developer [Console](/login?selectAccount=true&returnTo=%2Fdashboard%3F) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details. |
| User | To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea. |

### 

Example output

> 1.  Fill a kettle with water and place it on the stove to boil.
> 2.  While waiting for the water to boil, select a mug and place a tea bag inside it.
> 3.  Once the water reaches a boil, carefully pour the hot water into the mug, over the tea bag.
> 4.  Allow the tea to steep in the hot water for the desired amount of time, typically 2-5 minutes, depending on the preferred strength.
> 5.  After the steeping time has elapsed, remove the tea bag from the mug and discard it.
> 6.  Add milk and sugar to the tea, according to your taste preferences.
> 7.  Using a spoon, stir the tea, milk, and sugar together until well combined.
> 8.  Your cup of tea is now ready to enjoy. Drink it while it's still hot.

------------------------------------------------------------------------

## 

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
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
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
