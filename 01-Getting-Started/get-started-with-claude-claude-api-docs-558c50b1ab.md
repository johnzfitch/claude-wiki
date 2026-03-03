---
category: "01-Getting-Started"
fetched_at: "2026-03-03T14:55:25Z"
source_url: "https://platform.claude.com/docs/en/get-started"
title: "Get started with Claude - Claude API Docs"
---

# Get started with Claude


Make your first API call to Claude and build a simple web search assistant.


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

    Get your API key from the [Claude Console](/settings/keys) and set it as an environment variable:

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

You made your first API call. Next, learn the Messages API patterns you'll use in every Claude integration.

[](/docs/en/build-with-claude/working-with-messages)

Working with the Messages API

Learn multi-turn conversations, system prompts, stop reasons, and other core patterns.

Once you're comfortable with the basics, explore further:

[](/docs/en/about-claude/models/overview)

Models overview

Compare Claude models by capability and cost.

[](/docs/en/build-with-claude/overview)

Features overview

Browse all Claude capabilities: tools, context management, structured outputs, and more.

[](/docs/en/api/client-sdks)

Client SDKs

Reference documentation for Python, TypeScript, Java, and other client libraries.
