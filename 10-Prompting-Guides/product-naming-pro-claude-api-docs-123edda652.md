---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:37Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/product-naming-pro"
title: "Product naming pro - Claude API Docs"
---

# Product naming pro


Create catchy product names from descriptions and keywords.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression. |
| User | Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers. Keywords: immersive, comfortable, high-fidelity, long-lasting, convenient |

## 

Example output

> 1.  SoundOasis Elite 2.AudioZen Nomad 3.Serenity Pro 4.Tranquility Touch 5.Harmonix Journey 6.SonicSolace Roam 7.Auditory Bliss 8.Quietude Quest 9.Euphony Excursion 10.Acoustica Wanderlust

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
    temperature=1,
    system="Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers.  \n  \nKeywords: immersive, comfortable, high-fidelity, long-lasting, convenient",
                }
            ],
        }
    ],
)
print(message.content)
```
