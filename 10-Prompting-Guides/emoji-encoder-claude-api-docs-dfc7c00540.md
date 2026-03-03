---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:21Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/emoji-encoder"
title: "Emoji encoder - Claude API Docs"
---

# Emoji encoder


Convert plain text into fun and expressive emoji messages.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Use emojis creatively but ensure the message remains clear and easy to understand. Do not change the core message or add new information. |
| User | All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts. |

## 

Example output

All the 🌍's a 🎭, and all the 👨 and 👩 merely 🎭🎬. They have their 🚪🚶‍♂️ and their 🚶‍♀️🚪; And one 👨 in his ⌛ plays many 🎭.

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
    system="Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Use emojis creatively but ensure the message remains clear and easy to understand. Do not change the core message or add new information.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts.",
                }
            ],
        }
    ],
)
print(message.content)
```
