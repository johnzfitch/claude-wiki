---
category: "10-Prompting-Guides"
fetched_at: "2026-02-22T13:23:45Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/second-grade-simplifier"
title: "Second-grade simplifier - Claude API Docs"
---
# Second-grade simplifier


Make complex text easy for young learners to understand.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner. |
| User | The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur. |

## 

Example Output

Mitochondria are tiny parts inside cells that work like little power stations. They make a special molecule called ATP, which is like the cell's energy money. ATP helps the cell do important jobs and keeps it running smoothly, just like how money helps people buy things they need. Mitochondria are very important because without them, cells wouldn't have the energy to function properly.

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
    temperature=0,
    system="Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur.",
                }
            ],
        }
    ],
)
print(message.content)
```
