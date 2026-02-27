---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:48Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/efficiency-estimator"
title: "Efficiency estimator - Claude API Docs"
---

Prompt Library

# Efficiency estimator

Copy page

Calculate the time complexity of functions and algorithms.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determining the time complexity. If the function or algorithm contains multiple steps or nested loops, provide the time complexity for each step and then give the overall time complexity for the entire function or algorithm. Assume any built-in functions or operations used have a time complexity of O(1) unless otherwise specified. |
| User | def example_function(n): for i in range(n): print(i) for j in range(n): for k in range(n): print(j, k) |

### 

Example output

> To analyze the time complexity of the given function `example_function(n)`, we'll break it down into steps and consider the worst-case scenario.
>
> Step 1: Analyzing the first loop
>
> ``` inline-block
> for i in range(n):
>    print(i)
> ```

> This loop iterates `n` times and performs a constant-time operation (`print(i)`) in each iteration. Therefore, the time complexity of this step is O(n).
>
> Step 2: Analyzing the nested loops
>
> ``` inline-block
> for j in range(n):
>     for k in range(n):
>         print(j, k)
> ```
>
> The outer loop iterates `n` times, and for each iteration, the inner loop also iterates `n` times. In each iteration of the inner loop, a constant-time operation (`print(j, k)`) is performed. Therefore, the time complexity of the nested loops is O(n \* n) = O(n^2).
>
> Step 3: Combining the time complexities  
> The function `example_function(n)` consists of two steps: the first loop and the nested loops. The overall time complexity is the sum of the time complexities of each step.
>
> Time complexity of the first loop: O(n)  
> Time complexity of the nested loops: O(n^2)
>
> To determine the overall time complexity, we consider the dominant term, which is the term with the highest order of growth. In this case, O(n^2) dominates O(n).
>
> Therefore, the overall time complexity of the function `example_function(n)` is O(n^2).
>
> In the worst-case scenario, when `n` is large, the nested loops will dominate the execution time, and the function will have a quadratic time complexity.

------------------------------------------------------------------------

### 

API request

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
    system="Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determining the time complexity. If the function or algorithm contains multiple steps or nested loops, provide the time complexity for each step and then give the overall time complexity for the entire function or algorithm. Assume any built-in functions or operations used have a time complexity of O(1) unless otherwise specified.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "def example_function(n):\n    for i in range(n):\n        print(i)\n\n    for j in range(n):\n        for k in range(n):\n            print(j, k)"
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
