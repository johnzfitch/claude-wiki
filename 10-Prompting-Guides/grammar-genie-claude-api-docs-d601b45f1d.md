---
category: "10-Prompting-Guides"
fetched_at: "2026-02-22T13:24:32Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/grammar-genie"
title: "Grammar genie - Claude API Docs"
---
# Grammar genie


Transform grammatically incorrect sentences into proper English.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to take the text provided and rewrite it into a clear, grammatically correct version while preserving the original meaning as closely as possible. Correct any spelling mistakes, punctuation errors, verb tense issues, word choice problems, and other grammatical mistakes. |
| User | I can haz cheeseburger? |

## 

Example Output

May I have a cheeseburger?

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

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the text provided and rewrite it into a clear, grammatically correct version while preserving the original meaning as closely as possible. Correct any spelling mistakes, punctuation errors, verb tense issues, word choice problems, and other grammatical mistakes.",
    messages=[
        {
            "role": "user",
            "content": [{"type": "text", "text": "I can haz cheeseburger?"}],
        }
    ],
)
print(message.content)
```
