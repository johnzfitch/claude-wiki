---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:27Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/tongue-twister"
title: "Tongue twister - Claude API Docs"
---

# Tongue twister


Create challenging tongue twisters.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

| Role | Content |
|----|----|
| User | Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters. |

## 

Example Output

Tongue Twister 1: The shrewd shrew chewed through the shiny, shimmering shoe.

Tongue Twister 2: Brisk breezes blew by the blue-blooded, blabbering, babbling baboon.

Tongue Twister 3: The perplexed piper picked a peck of pickled peppers while practicing his piping.

Tongue Twister 4: Six sleek, slick, slender sleds slid swiftly down the steep, snowy slope.

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
                    "text": "Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters.",
                }
            ],
        }
    ],
)
print(message.content)
```
