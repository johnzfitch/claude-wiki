---
category: "01-Getting-Started"
fetched_at: "2026-02-07T10:04:01Z"
source_url: "https://platform.claude.com/docs/en/get-started"
title: "Get started with Claude - Claude API Docs"
---

First steps

# Get started with Claude

Copy page

Make your first API call to Claude and build a simple web search assistant

Copy page

## 

Prerequisites

- An Anthropic [Console account](/)
- An [API key](/settings/keys)

## 

Call the API

cURL

cURL

Python

Python

TypeScript

TypeScript

Java

Java

1.  1

    Set your API key

    Get your API key at the [Claude Console](/settings/keys) and set it as an environment variable:

    ``` shiki
    export ANTHROPIC_API_KEY='your-api-key-here'
    ```

2.  2

    Make your first API call

    Run this command to create a simple web search assistant:

    ``` shiki
    curl https://api.anthropic.com/v1/messages \
      -H "Content-Type: application/json" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-opus-4-6",
        "max_tokens": 1000,
        "messages": [
          {
            "role": "user", 
            "content": "What should I search for to find the latest developments in renewable energy?"
          }
        ]
      }'
    ```

    **Example output:**

    ``` shiki
    {
      "id": "msg_01HCDu5LRGeP2o7s2xGmxyx8",
      "type": "message", 
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Here are some effective search strategies to find the latest renewable energy developments:\n\n## Search Terms to Use:\n- \"renewable energy news 2024\"\n- \"clean energy breakthrough\"\n- \"solar/wind/battery technology advances\"\n- \"green energy innovations\"\n- \"climate tech developments\"\n- \"energy storage solutions\"\n\n## Best Sources to Check:\n\n**News & Industry Sites:**\n- Renewable Energy World\n- GreenTech Media (now Wood Mackenzie)\n- Energy Storage News\n- CleanTechnica\n- PV Magazine (for solar)\n- WindPower Engineering & Development..."
        }
      ],
      "model": "claude-opus-4-6",
      "stop_reason": "end_turn",
      "usage": {
        "input_tokens": 21,
        "output_tokens": 305
      }
    }
    ```

## 

Next steps

Now that you have made your first Claude API request, it's time to explore what else is possible:

[](/docs/en/build-with-claude/working-with-messages)

Working with Messages

Learn common patterns for the Messages API.

[](/docs/en/api/overview)

Features Overview

Explore Claude's advanced features and capabilities.

[](/docs/en/api/client-sdks)

Client SDKs

Discover Anthropic client libraries.

[](https://platform.claude.com/cookbooks)

Claude Cookbook

Learn with interactive Jupyter notebooks.

Was this page helpful?

- 

- [Prerequisites](#prerequisites)

- [Call the API](#call-the-api)

- [Next steps](#next-steps)

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
