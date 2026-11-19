---
title: "Strict tool use - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-11-13T06:33:57Z"
tags: ["agents", "api"]
---

# Strict tool use

Copy page



Enforce JSON Schema compliance on Claude’s tool inputs with grammar-constrained sampling.

Copy page



Strict tool use

Feature of  
[Structured outputs](../Guides/build-with-claude-structured-outputs.md)

[Models](#feature-availability)  
- All models

[APIs](#feature-availability)  
- Messages API

[Cloud platforms](#feature-availability)  
- Claude API
- Amazon Bedrock
- Amazon Bedrockbedrock-runtime
- Claude Platform on AWS
- Claude Models on Google CloudGoogle managed
- Microsoft Foundry

[Data handling](#feature-data-handling)  
ZDRQualifiedZDR eligible (qualified)HIPAAHIPAA eligible

Setting `strict: true` on a tool definition guarantees Claude’s tool inputs match your JSON Schema by constraining the model’s token sampling to schema-valid outputs (a technique called grammar-constrained sampling). This page covers why strict mode matters for agents, how to enable it, and common use cases. For the supported JSON Schema subset, see [JSON Schema limitations](../Guides/build-with-claude-structured-outputs.md#json-schema-limitations). For non-strict schema guidance, see [Define tools](agents-and-tools-tool-use-implement-tool-use.md).

Strict tool use validates tool parameters, ensuring Claude calls your functions with correctly typed arguments. Use strict tool use when you need to:

- Validate tool parameters
- Build agentic workflows
- Ensure type-safe function calls
- Handle complex tools with nested properties

## Why strict tool use matters for agents

Building reliable agentic systems requires guaranteed schema conformance. Without strict mode, Claude might return incompatible types (`"2"` instead of `2`) or omit required fields, breaking your functions and causing runtime errors.

Strict tool use guarantees type-safe parameters:

- Correctly typed function arguments every time
- No need to validate and retry tool calls
- Production-ready agents that work consistently at scale

For example, suppose a booking system needs `passengers: int`. Without strict mode, Claude might provide `passengers: "two"` or `passengers: "2"`. With `strict: true`, the response always contains `passengers: 2`.

## Quick start

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "strict": True,  # Enable strict mode
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit of temperature, either 'celsius' or 'fahrenheit'",
                    },
                },
                "required": ["location"],
                "additionalProperties": False,
            },
        }
    ],
)
print(response.content)
```

**Response format:** Tool use blocks with validated inputs in `response.content[x].input`

Output



```python
{
  "type": "tool_use",
  "name": "get_weather",
  "input": {
    "location": "San Francisco, CA"
  }
}
```

**Guarantees:**

- Tool `input` strictly follows the `input_schema`
- Tool `name` is always valid (from provided tools or server tools)

## How it works

1.  1

    ### Define your tool schema

    Create a JSON schema for your tool’s `input_schema`. The schema uses standard JSON Schema format with some limitations (see [JSON Schema limitations](../Guides/build-with-claude-structured-outputs.md#json-schema-limitations)).

2.  2

    ### Add strict: true

    Set `"strict": true` as a top-level property in your tool definition, alongside `name`, `description`, and `input_schema`.

3.  3

    ### Handle tool calls

    When Claude uses the tool, the `input` field in the `tool_use` block strictly follows your `input_schema`, and the `name` is always valid.

The [computer use](agents-and-tools-tool-use-computer-use-tool.md) and [browser use](agents-and-tools-tool-use-browser-use-tool.md) toolset entries (`computer_toolset_20260801` and `browser_toolset_20260801`) don’t accept `strict: true`; a request that sets it on either entry is rejected.

## Common use cases

### Validated tool inputs

Ensure tool parameters exactly match your schema:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = Anthropic()
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Search for flights to Tokyo departing June 1, 2026",
        }
    ],
    tools=[
        {
            "name": "search_flights",
            "strict": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "destination": {"type": "string"},
                    "departure_date": {"type": "string", "format": "date"},
                    "passengers": {
                        "type": "integer",
                        "enum": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    },
                },
                "required": ["destination", "departure_date"],
                "additionalProperties": False,
            },
        }
    ],
)

print(response)
```

### Agentic workflow with multiple validated tools

Build reliable multistep agents with guaranteed tool parameters:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = Anthropic()
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Help me plan a trip from New York to Paris for 2 people, departing June 1, 2026",
        }
    ],
    tools=[
        {
            "name": "search_flights",
            "strict": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "origin": {"type": "string"},
                    "destination": {"type": "string"},
                    "departure_date": {"type": "string", "format": "date"},
                    "travelers": {"type": "integer", "enum": [1, 2, 3, 4, 5, 6]},
                },
                "required": ["origin", "destination", "departure_date"],
                "additionalProperties": False,
            },
        },
        {
            "name": "search_hotels",
            "strict": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "check_in": {"type": "string", "format": "date"},
                    "guests": {"type": "integer", "enum": [1, 2, 3, 4]},
                },
                "required": ["city", "check_in"],
                "additionalProperties": False,
            },
        },
    ],
)

print(response)
```

## Data retention

Strict tool use compiles tool `input_schema` definitions into grammars using the same pipeline as [structured outputs](../Guides/build-with-claude-structured-outputs.md). Tool schemas are temporarily cached for up to 24 hours since last use. Prompts and responses are not retained beyond the API response.

Strict tool use is HIPAA eligible, but **protected health information (PHI) must not be included in tool schema definitions**. The API caches compiled schemas separately from message content, and these cached schemas do not receive the same PHI protections as prompts and responses. Do not include PHI in `input_schema` property names, `enum` values, `const` values, or `pattern` regular expressions. PHI should only appear in message content (prompts and responses), where it is protected under HIPAA safeguards.

## Next steps



[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)

Fetch and read content from specific URLs to bring live web content into Claude’s context.



[Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md)

Cache tool definitions across turns to reduce cost and latency.



[Structured outputs](../Guides/build-with-claude-structured-outputs.md)

Get validated JSON responses using the same grammar-constrained sampling.



[Define tools](agents-and-tools-tool-use-implement-tool-use.md)

Specify tool schemas, write effective descriptions, and control when Claude calls your tools.

## Availability

Strict tool use

Cloud platform

Cloud platform: Claude API

Availability requirements for Strict tool use are the same across all supported platforms.

Claude API

API  
- Messages API

Models  
- All models

Amazon Bedrock

API  
- Messages API

Models  
- All models

Amazon Bedrock (bedrock-runtime)

API  
- Messages API

Models  
- All models

Claude Platform on AWS

API  
- Messages API

Models  
- All models

Claude Models on Google Cloud (Google managed)

API  
- Messages API

Models  
- All models

Microsoft Foundry

API  
- Messages API

Models  
- All models

### Data handling

[Data handling overview](../Other/manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/messages`

Zero data retentionEligible (qualified)

Excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

Your prompts and Claude’s outputs are not stored. Only the JSON schema is cached, for up to 24 hours since last use. This also covers strict tool use (`strict: true` on tools), which uses the same grammar pipeline. [Learn more](../Guides/build-with-claude-structured-outputs.md#data-retention)

HIPAAEligible

PHI must not be included in JSON schema definitions; see PHI handling guidelines. [Learn more](../Other/manage-claude-api-and-data-retention.md#phi-handling-guidelines)
