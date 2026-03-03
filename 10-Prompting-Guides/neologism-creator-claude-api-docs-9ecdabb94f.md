---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:20Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/neologism-creator"
title: "Neologism creator - Claude API Docs"
---

# Neologism creator


Invent new words and provide their definitions based on user-provided concepts or ideas.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| User | Can you help me create a new word for the act of pretending to understand something in order to avoid looking ignorant or uninformed? |

## 

Example output

How about the neologism "fauxprehension" to describe this concept?

Fauxprehension (fəʊprɪˈhɛnʃ(ə)n) - noun Definition: The act of feigning understanding or comprehension of a topic, concept, or situation in order to avoid appearing ignorant, uninformed, or out of the loop. It is the pretense of knowledge or grasp of a subject matter, often employed in social or professional settings to maintain one's image or status.

Etymology: The word "fauxprehension" is a blend of "faux," which comes from the French word meaning false or fake, and "comprehension," which means the action or capability of understanding something.

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
    temperature=1,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Can you help me create a new word for the act of pretending to understand something in order to avoid looking ignorant or uninformed?",
                }
            ],
        }
    ],
)
print(message.content)
```
