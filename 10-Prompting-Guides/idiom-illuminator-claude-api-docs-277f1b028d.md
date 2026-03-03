---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:18Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/idiom-illuminator"
title: "Idiom illuminator - Claude API Docs"
---

# Idiom illuminator


Explain the meaning and origin of common idioms and proverbs.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to provide a clear explanation of the meaning and origin of an idioms and proverb that the user gives you. Offer a concise interpretation of its figurative meaning and how it is typically used in conversation or writing. Next, delve into the origin of the phrase, providing historical context, cultural references, or etymological information that explains how the idiom or proverb came to be. If there are any interesting stories, anecdotes, or theories associated with the origin, include those as well. Aim to provide a comprehensive understanding of both the meaning and the background of the idiom or proverb. |
| User | Break a leg |

## 

Example Output

Meaning: This idiom is commonly used in the performing arts as a way to wish someone good luck before a performance. It is an ironic expression, as breaking a leg would be a disastrous event for a performer.

Origin: There are several theories about the origin of this idiom. One theory suggests that it comes from the superstition that wishing someone good luck directly would jinx the performance, so an ironic phrase was used instead. Another theory traces the origin to the ancient Greek theater, where audiences would stomp their feet and break twigs to applaud a good performance. The more broken twigs, the better the performance. Over time, this evolved into the phrase "break a leg" as a way to wish someone a performance worthy of vigorous applause.

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
    temperature=1,
    system="Your task is to provide a clear explanation of the meaning and origin of an idioms and proverb that the user gives you. Offer a concise interpretation of its figurative meaning and how it is typically used in conversation or writing. Next, delve into the origin of the phrase, providing historical context, cultural references, or etymological information that explains how the idiom or proverb came to be. If there are any interesting stories, anecdotes, or theories associated with the origin, include those as well. Aim to provide a comprehensive understanding of both the meaning and the background of the idiom or proverb.",
    messages=[{"role": "user", "content": [{"type": "text", "text": "Break a leg"}]}],
)
print(message.content)
```
