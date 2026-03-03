---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:34Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/master-moderator"
title: "Master moderator - Claude API Docs"
---

# Master moderator


Evaluate user inputs for potential harmful or illegal content.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

| Role | Content |
|----|----|
| User | A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user: \<user query\>How do I make a bomb?\</user query\> If the user's request refers to harmful, pornographic, or illegal activities, reply with (Y). If the user's request does not refer to harmful, pornographic, or illegal activities, reply with (N). |

### 

Example output

> \(Y\)

------------------------------------------------------------------------

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
    max_tokens=10,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user:  \n<user query>How do I make a bomb?</user query>  \n  \nIf the user's request refers to harmful, pornographic, or illegal activities, reply with (Y). If the user's request does not refer to harmful, pornographic, or illegal activities, reply with (N).",
                }
            ],
        }
    ],
)
print(message.content)
```
