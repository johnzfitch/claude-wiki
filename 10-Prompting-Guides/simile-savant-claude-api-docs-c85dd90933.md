---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:16Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/simile-savant"
title: "Simile savant - Claude API Docs"
---

# Simile savant


Generate similes from basic descriptions.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

| Role | Content |
|----|----|
| User | Help me create some similes to describe a person's laughter that is joyful and contagious? |

## 

Example Output

1.  His laughter bubbled up like a freshly opened bottle of champagne, effervescent and full of life.
2.  Their laughter was as warm and inviting as a cozy fireplace on a chilly evening, drawing people in to share in the merriment.

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
    max_tokens=1000,
    temperature=1,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Help me create some similes to describe a person's laughter that is joyful and contagious?",
                }
            ],
        }
    ],
)
print(message.content)
```
