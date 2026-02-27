---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:24Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/corporate-clairvoyant"
title: "Corporate clairvoyant - Claude API Docs"
---

Prompt Library

# Corporate clairvoyant

Copy page

Extract insights, identify risks, and distill key information from long corporate reports into a single memo.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example Output

> To: Investment Team  
> From: \[Your Name\]  
> Date: March 4, 2024  
> Subject: Matterport 2022 10-K Highlights and Financial Outlook
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
                    "text": "Your task is to analyze the following report:  \n<report>  \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity]  \n</report>  \n  \nSummarize this annual report in a concise and clear manner, and identify key market trends and takeaways. Output your findings as a short memo I can send to my team. The goal of the memo is to ensure my team stays up to date on how financial institutions are faring and qualitatively forecast and identify whether there are any operating and revenue risks to be expected in the coming quarter. Make sure to include all relevant details in your summary and analysis."
                }
            ]
        }
    ]
)
print(message.content)
```

Was this page helpful?

- 

- [Example Output](#example-output)

- [API Request](#api-request)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
