---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:07Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/corporate-clairvoyant"
title: "Corporate clairvoyant - Claude API Docs"
---

# Corporate clairvoyant


Extract insights, identify risks, and distill key information from long corporate reports into a single memo.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example Output

> To: Investment Team From: \[Your Name\] Date: March 4, 2024 Subject: Matterport 2022 10-K Highlights and Financial Outlook
>
> Hi team,
>
> I have identified some key takeaways from Matterport's 2022 annual report:
>
> Financial Performance:
>
> - Revenue increased 22% to \$136.1M in 2022, driven by growth in subscription and services revenue
> - However, gross margin decreased from 54% to 38% due to increased costs from product revenue and supply chain challenges
> - Operating losses widened to \$275.5M as the company invested heavily in R&D and sales & marketing to drive growth
> - Ended 2022 with \$476.9M in cash and investments to fund operations
>
> Business Highlights:
>
> - Subscriber base grew 39% to over 701,000 at end of 2022. Spaces under management reached 9.2 million
> - Expanded platform with launch of Matterport Axis motorized mount, Pro3 camera, and major updates to cloud software
> - Completed acquisitions of Enview (AI for 3D spatial data) and VHT Studios (real estate marketing) to enhance offerings
> - Signed notable partnerships with Burns & McDonnell and CGS to deliver Matterport's solutions to their enterprise customers
>
> Outlook:
>
> - Matterport sees a massive market opportunity in digitizing the world's buildings and spaces (estimates \$240B+ TAM)
> - Focused on driving adoption with large enterprise customers across key verticals like real estate, AEC, facilities management, and more
> - Will continue investing in R&D and international expansion to penetrate the largely untapped global building market
> - Near-term growth and margins may be impacted by macroeconomic headwinds and supply chain issues
> - However, healthy liquidity position and relatively sticky customer base provide downside protection
>
> In summary, Matterport delivered strong top-line growth in 2022 as it made progress penetrating a huge global market. While profitability remains challenged as the company invests heavily for growth, its balance sheet looks solid. Apart from some ongoing supply chain issues, the underlying business momentum appears intact based on key operating metrics. Barring a severe economic downturn, Matterport seems well-positioned to continue gaining share in the nascent building digitization space.

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
    max_tokens=2000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Your task is to analyze the following report:  \n<report>  \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity]  \n</report>  \n  \nSummarize this annual report in a concise and clear manner, and identify key market trends and takeaways. Output your findings as a short memo I can send to my team. The goal of the memo is to ensure my team stays up to date on how financial institutions are faring and qualitatively forecast and identify whether there are any operating and revenue risks to be expected in the coming quarter. Make sure to include all relevant details in your summary and analysis.",
                }
            ],
        }
    ],
)
print(message.content)
```
