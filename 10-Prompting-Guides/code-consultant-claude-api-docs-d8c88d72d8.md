---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:18Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/code-consultant"
title: "Code consultant - Claude API Docs"
---

# Code consultant


Suggest improvements to optimize Python code performance.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example output

Python

``` shiki
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

Explanation: Using a generator function with yield is more memory-efficient for generating the Fibonacci sequence. It avoids creating and storing the entire sequence in a list. Instead, it generates each number on-the-fly as needed.

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

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    temperature=0,
    system="Your task is to analyze the provided Python code snippet and suggest improvements to optimize its performance. Identify areas where the code can be made more efficient, faster, or less resource-intensive. Provide specific suggestions for optimization, along with explanations of how these changes can enhance the code's performance. The optimized code should maintain the same functionality as the original code while demonstrating improved efficiency.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "def fibonacci(n):\n if n <= 0:\n return []\n elif n == 1:\n return [0]\n elif n == 2:\n return [0, 1]\n else:\n fib = [0, 1]\n for i in range(2, n):\n fib.append(fib[i-1] + fib[i-2])\n return fib",
                }
            ],
        }
    ],
)
print(message.content)
```
