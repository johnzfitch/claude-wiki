---
category: "10-Prompting-Guides"
fetched_at: "2026-02-22T13:24:37Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/riddle-me-this"
title: "Riddle me this - Claude API Docs"
---
# Riddle me this


Generate riddles and guide the user to the solutions.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

| Role | Content |
|----|----|
| User | Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints. |

## 

Example Output

I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?

Hint 1: Consider the different states of matter and how they can change. Hint 2: Think about the relationship between the three elements mentioned: air, water, and the mystery object. Hint 3: The answer is related to a common phenomenon that occurs in everyday life.

Solution: Fire. Explanation: Fire is not alive, but it grows and spreads as it consumes fuel. It doesn't have lungs, but it requires oxygen (air) to sustain itself. Although it doesn't have a mouth, water is often used to extinguish fires, effectively "killing" them.

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
                    "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints.",
                }
            ],
        }
    ],
)
print(message.content)
```
