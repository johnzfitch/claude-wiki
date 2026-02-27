---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:46Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/code-clarifier"
title: "Code clarifier - Claude API Docs"
---

Prompt Library

# Code clarifier

Copy page

Simplify and explain complex code in plain language.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms to make the explanation accessible to someone with minimal coding knowledge. Avoid using technical jargon unless absolutely necessary, and provide clear explanations for any jargon used. The goal is to help the reader understand what the code does and how it works at a high level. |
| User | import random def bubble\*sort(arr): n = len(arr) for i in range(n-1): for j in range(n-i-1): if arr\[j\] \> arr\[j+1\]: arr\[j\], arr\[j+1\] = arr\[j+1\], arr\[j\] return arr numbers = \[random.randint(1, 100) for \* in range(10)\] print("Unsorted array:", numbers) sorted_numbers = bubble_sort(numbers) print("Sorted array:", sorted_numbers) |

### 

Example Output

> This code demonstrates the implementation of the bubble sort algorithm, which is used to sort a list of numbers in ascending order. Let's break it down step by step:
>
> 1.  The code starts by importing the 'random' module, which will be used to generate random numbers for the example.
>
> 2.  The 'bubble_sort' function is defined, which takes an array (list) of numbers as input. This function will perform the sorting operation.
>
> 3.  Inside the 'bubble_sort' function, the variable 'n' is assigned the length of the input array. This will be used to determine the number of iterations needed for sorting.
>
> 4.  The first loop, controlled by the variable 'i', iterates 'n-1' times. This is because after 'n-1' passes, the largest number will be at the end of the array, so we don't need to compare it again.
>
> 5.  The second loop, controlled by the variable 'j', iterates 'n-i-1' times. This is because after each pass, the largest number among the unsorted elements will be placed at the end, so we don't need to compare it in the next pass.
>
> 6.  Inside the second loop, there is an if statement that compares adjacent elements in the array. If the element at index 'j' is greater than the element at index 'j+1', they are swapped. This ensures that the larger element moves towards the end of the array.
>
> 7.  The swapping is done using the Python syntax 'arr\[j\], arr\[j+1\] = arr\[j+1\], arr\[j\]', which simultaneously assigns the values of 'arr\[j+1\]' to 'arr\[j\]' and 'arr\[j\]' to 'arr\[j+1\]'.
>
> 8.  After all the iterations are complete, the sorted array is returned by the 'bubble_sort' function.
>
> 9.  In the example code, a list of 10 random numbers between 1 and 100 is generated using a list comprehension: '\[random.randint(1, 100) for \_ in range(10)\]'. The underscore '\_' is used as a placeholder variable since we don't need the index values.
>
> 10. The unsorted array is printed to show the initial order of the numbers.
>
> 11. The 'bubble_sort' function is called with the 'numbers' array as input, and the sorted array is stored in the 'sorted_numbers' variable.
>
> 12. Finally, the sorted array is printed to display the numbers in ascending order.
>
> In simpler terms, imagine you have a list of numbers that are out of order. The bubble sort algorithm works by comparing each number with the one next to it, and if they are in the wrong order, it swaps them. This process is repeated multiple times until the entire list is sorted. It's like bubbles rising to the surface, with the larger numbers gradually moving towards the end of the list in each pass.

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
    system="Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms to make the explanation accessible to someone with minimal coding knowledge. Avoid using technical jargon unless absolutely necessary, and provide clear explanations for any jargon used. The goal is to help the reader understand what the code does and how it works at a high level.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "import random\n\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n-1):\n        for j in range(n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\nnumbers = [random.randint(1, 100) for _ in range(10)]\nprint(\"Unsorted array:\", numbers)\nsorted_numbers = bubble_sort(numbers)\nprint(\"Sorted array:\", sorted_numbers)"
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
