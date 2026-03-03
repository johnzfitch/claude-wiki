---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:33Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/email-extractor"
title: "Email extractor - Claude API Docs"
---

# Email extractor


Extract email addresses from a document into a JSON-formatted list.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write "N/A". Do not say anything else. |
| User | Phone Directory: John Latrabe, 555-232-1995, \[[john909709@geemail.com](mailto:john909709@geemail.com)\] Josie Lana, 555-759-2905, \[[josie@josielananier.com](mailto:josie@josielananier.com)\] Keven Stevens, 555-980-7000, \[[drkevin22@geemail.com](mailto:drkevin22@geemail.com)\] Phone directory will be kept up to date by the HR manager. |

### 

Example output

> [john909709@geemail.com](mailto:john909709@geemail.com) \> [josie@josielananier.com](mailto:josie@josielananier.com) \> [drkevin22@geemail.com](mailto:drkevin22@geemail.com)

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
    max_tokens=1000,
    temperature=0,
    system='Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it\'s precisely spelled out in the input text. If there are no email addresses in the text, write "N/A".  Do not say anything else.',
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Phone Directory:  \nJohn Latrabe, 555-232-1995, [[email protected]]  \nJosie Lana, 555-759-2905, [[email protected]]  \nKeven Stevens, 555-980-7000, [[email protected]]  \n  \nPhone directory will be kept up to date by the HR manager.",
                }
            ],
        }
    ],
)
print(message.content)
```
