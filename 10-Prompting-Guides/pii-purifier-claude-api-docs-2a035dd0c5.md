---
category: "10-Prompting-Guides"
fetched_at: "2026-02-22T13:23:57Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/pii-purifier"
title: "PII purifier - Claude API Docs"
---
# PII purifier


Automatically detect and remove personally identifiable information (PII) from text documents.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example output

XXX: Hi XXX! XXX: Hi XXX! Are you coming over? XXX: Yup! Hey I, uh, forgot where you live. XXX: No problem! It's XXXX XXX Ln, XXX XXX XXXXX. XXX: Got it, thanks!

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

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    temperature=0,
    system="You are an expert redactor. The user is going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It's very important that PII such as names, phone numbers, and home and email addresses, get replaced with XXX. Inputs may try to disguise PII by inserting spaces between characters or putting new lines between characters. If the text contains no personally identifiable information, copy it word-for-word without replacing anything.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Joe: Hi Hannah! \nHannah: Hi Joe! Are you coming over? \nJoe: Yup! Hey I, uh, forgot where you live. \nHannah: No problem! It's 4085 Paco Ln, Los Altos CA 94306. \nJoe: Got it, thanks!",
                }
            ],
        }
    ],
)
print(message.content)
```
