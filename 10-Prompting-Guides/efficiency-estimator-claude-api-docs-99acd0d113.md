---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:31Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/efficiency-estimator"
title: "Efficiency estimator - Claude API Docs"
---

# Efficiency estimator


Calculate the time complexity of functions and algorithms.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

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
> ``` shiki
> for i in range(n):
>     print(i)
> ```

> This loop iterates `n` times and performs a constant-time operation (`print(i)`) in each iteration. Therefore, the time complexity of this step is O(n).
>
> Step 2: Analyzing the nested loops
>
> ``` shiki
> for j in range(n):
>     for k in range(n):
>         print(j, k)
> ```
>
> The outer loop iterates `n` times, and for each iteration, the inner loop also iterates `n` times. In each iteration of the inner loop, a constant-time operation (`print(j, k)`) is performed. Therefore, the time complexity of the nested loops is O(n \* n) = O(n^2).
>
> Step 3: Combining the time complexities The function `example_function(n)` consists of two steps: the first loop and the nested loops. The overall time complexity is the sum of the time complexities of each step.
>
> Time complexity of the first loop: O(n) Time complexity of the nested loops: O(n^2)
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
                    "text": "def example_function(n):\n    for i in range(n):\n        print(i)\n\n    for j in range(n):\n        for k in range(n):\n            print(j, k)",
                }
            ],
        }
    ],
)
print(message.content)
```
