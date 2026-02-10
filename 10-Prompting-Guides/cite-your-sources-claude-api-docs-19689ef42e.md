---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:28Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/cite-your-sources"
title: "Cite your sources - Claude API Docs"
---

Prompt Library

# Cite your sources

Copy page

Get answers to questions about a document's content with relevant citations supporting the response.

Copy page

We recommend using the [citation feature](/docs/en/build-with-claude/citations) built into the API instead of a prompt based approach. Using the API citation feature will improve citation quality, ensure that all returned citations are valid, and potentially reduce the number of needed output tokens.

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example output

Quotes:  
\[1\] "We have recently experienced rapid growth. Our subscribers have grown approximately 49-fold from December 31, 2018 to December 31, 2022. Our revenue increased by approximately 22% to \$136.1 million for the year ended December 31, 2022, from approximately \$111.2 million for the year ended December 31, 2021."  
\[2\] "Our gross profit decreased by \$8.1 million or 14%, to \$51.8 million for the year ended December 31, 2022, from \$60.0 million for the year ended December 31, 2021, primarily attributable to certain disruptive and incremental costs due to the global supply chain constraints in fiscal year 2022."  
\[3\] "Our net dollar expansion rate of 103% for the three months ended December 31, 2022 demonstrates the stickiness and growth potential of our platform."

Answer:  
Matterport has experienced rapid subscriber and revenue growth in recent years. \[1\] However, their gross profit declined in 2022 due to supply chain issues. \[2\] Their net dollar expansion rate indicates strong subscriber retention and potential for continued growth. \[3\] Overall, despite the dip in gross profit, Matterport's subscriber and revenue growth, along with their platform's stickiness, suggest the company is doing relatively well.

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
    max_tokens=2000,
    temperature=0,
    system='You are an expert research assistant. Here is a document you will answer questions about: \n<doc> \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity] \n</doc> \n \nFirst, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short. \n \nIf there are no relevant quotes, write "No relevant quotes" instead. \n \nThen, answer the question, starting with "Answer:". Do not include or reference quoted content verbatim in the answer. Don\'t say "According to Quote [1]" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences. \n \nThus, the format of your overall response should look like what\'s shown between the <example></example> tags. Make sure to follow the formatting and spacing exactly. \n<example> \nQuotes: \n[1] "Company X reported revenue of \$12 million in 2021." \n[2] "Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%." \n \nAnswer: \nCompany X earned \$12 million. [1] Almost 90% of it was from widget sales. [2] \n</example> \n \nIf the question cannot be answered by the document, say so.',
    messages=[
        {
            "role": "user",
            "content": [{"type": "text", "text": "Is Matterport doing well?"}],
        }
    ],
)
print(message.content)
```

Was this page helpful?

- 

- [Example output](#example-output)

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
