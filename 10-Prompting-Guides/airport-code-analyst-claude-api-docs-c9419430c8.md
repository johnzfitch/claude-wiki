---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:41Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/airport-code-analyst"
title: "Airport code analyst - Claude API Docs"
---

# Airport code analyst


Find and extract airport codes from text.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list. |
| User | My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome. |

### 

Example Output

> Here is the list of airport codes mentioned in the text, in the order they appear:
>
> 1.  SEA (Seattle)
> 2.  AMS (Amsterdam)
> 3.  CDG (Paris)
> 4.  FCO (Rome)

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
    system="Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome.",
                }
            ],
        }
    ],
)
print(message.content)
```
