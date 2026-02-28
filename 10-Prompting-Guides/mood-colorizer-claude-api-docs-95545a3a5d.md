---
category: "10-Prompting-Guides"
fetched_at: "2026-02-22T13:22:15Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/mood-colorizer"
title: "Mood colorizer - Claude API Docs"
---
# Mood colorizer


Transform text descriptions of moods into corresponding HEX codes.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to take the provided text description of a mood or emotion and generate a HEX color code that visually represents that mood. Use color psychology principles and common associations to determine the most appropriate color for the given mood. If the text description is unclear, ambiguous, or does not provide enough information to determine a suitable color, respond with "Unable to determine a HEX color code for the given mood." |
| User | A passionate, intense, and fiery emotion, full of love and desire. |

## 

Example Output

`# FF1744`

This HEX color code represents a vivid, bold shade of red. Red is commonly associated with passion, intensity, love, and desire. The specific shade chosen here is a fiery, energetic red that captures the heat and fervor of the described emotion. Red is known to stimulate feelings of excitement and passion, making it an appropriate choice for representing this mood.

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
    max_tokens=500,
    temperature=0.5,
    system='Your task is to take the provided text description of a mood or emotion and generate a HEX color code that visually represents that mood. Use color psychology principles and common associations to determine the most appropriate color for the given mood. If the text description is unclear, ambiguous, or does not provide enough information to determine a suitable color, respond with "Unable to determine a HEX color code for the given mood."',
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "A passionate, intense, and fiery emotion, full of love and desire.",
                }
            ],
        }
    ],
)
print(message.content)
```
