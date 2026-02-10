---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:19Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/structured-outputs"
title: "Structured outputs - Claude API Docs"
---

Capabilities

# Structured outputs

Copy page

Get validated JSON results from agent workflows

Copy page

Structured outputs constrain Claude's responses to follow a specific schema, ensuring valid, parseable output for downstream processing. Two complementary features are available:

- **JSON outputs** (`output_config.format`): Get Claude's response in a specific JSON format
- **Strict tool use** (`strict: true`): Guarantee schema validation on tool names and inputs

The `output_format` parameter has been moved to `output_config.format`. The old `output_format` parameter still works temporarily but is deprecated and will be removed in a future API version. Update your code to use `output_config: {format: {...}}` instead.

These features can be used independently or together in the same request.

Structured outputs are generally available on the Claude API and Amazon Bedrock for Claude Opus 4.6, Claude Sonnet 4.5, Claude Opus 4.5, and Claude Haiku 4.5. Structured outputs remain in public beta on Microsoft Foundry.

**Migrating from beta?** The `output_format` parameter has moved to `output_config.format`, and beta headers are no longer required. The old beta header (`structured-outputs-2025-11-13`) and `output_format` parameter will continue working for a transition period. See code examples below for the updated API shape.

## 

Why use structured outputs

Without structured outputs, Claude can generate malformed JSON responses or invalid tool inputs that break your applications. Even with careful prompting, you may encounter:

- Parsing errors from invalid JSON syntax
- Missing required fields
- Inconsistent data types
- Schema violations requiring error handling and retries

Structured outputs guarantee schema-compliant responses through constrained decoding:

- **Always valid**: No more `JSON.parse()` errors
- **Type safe**: Guaranteed field types and required fields
- **Reliable**: No retries needed for schema violations

## 

JSON outputs

JSON outputs control Claude's response format, ensuring Claude returns valid JSON matching your schema. Use JSON outputs when you need to:

- Control Claude's response format
- Extract data from images or text
- Generate structured reports
- Format API responses

### 

Quick start

Shell

``` shiki
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm."
      }
    ],
    "output_config": {
      "format": {
        "type": "json_schema",
        "schema": {
          "type": "object",
          "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "plan_interest": {"type": "string"},
            "demo_requested": {"type": "boolean"}
          },
          "required": ["name", "email", "plan_interest", "demo_requested"],
          "additionalProperties": false
        }
      }
    }
  }'
```

**Response format:** Valid JSON matching your schema in `response.content[0].text`

``` shiki
{
  "name": "John Smith",
  "email": "john@example.com",
  "plan_interest": "Enterprise",
  "demo_requested": true
}
```

### 

How it works

1.  1

    Define your JSON schema

    Create a JSON schema that describes the structure you want Claude to follow. The schema uses standard JSON Schema format with some limitations (see [JSON Schema limitations](#json-schema-limitations)).

2.  2

    Add the output_config.format parameter

    Include the `output_config.format` parameter in your API request with `type: "json_schema"` and your schema definition.

3.  3

    Parse the response

    Claude's response will be valid JSON matching your schema, returned in `response.content[0].text`.

### 

Working with JSON outputs in SDKs

The SDKs provide helpers that make it easier to work with JSON outputs, including schema transformation, automatic validation, and integration with popular schema libraries.

SDK helper methods (like `.parse()` and Pydantic/Zod integration) still accept `output_format` as a convenience parameter. The SDK handles the translation to `output_config.format` internally. The examples below show the SDK helper syntax.

#### 

Using native schema definitions

Instead of writing raw JSON schemas, you can use familiar schema definition tools in your language. Each SDK provides class-based or library-based schema support:

- **Python**: [Pydantic](https://docs.pydantic.dev/) models
- **TypeScript**: [Zod](https://zod.dev/) schemas
- **Java**: Plain Java classes with annotation support (see [Java SDK structured outputs](/docs/en/api/sdks/java#using-structured-outputs))
- **Ruby**: `Anthropic::BaseModel` classes (see [Ruby SDK](/docs/en/api/sdks/ruby#input-schema-and-tool-calling))

Python

``` shiki
from pydantic import BaseModel
from anthropic import Anthropic, transform_schema

class ContactInfo(BaseModel):
    name: str
    email: str
    plan_interest: str
    demo_requested: bool

client = Anthropic()

# With .create() - requires transform_schema()
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm."
        }
    ],
    output_config={
        "format": {
            "type": "json_schema",
            "schema": transform_schema(ContactInfo),
        }
    }
)

print(response.content[0].text)

# With .parse() - can pass Pydantic model directly
response = client.messages.parse(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm."
        }
    ],
    output_format=ContactInfo,
)

print(response.parsed_output)
```

#### 

SDK-specific methods

Each SDK provides helpers that make working with structured outputs easier. See individual SDK pages for full details.

Python

Python

Java

Java

**`client.messages.parse()` (Recommended)**

The `parse()` method automatically transforms your Pydantic model, validates the response, and returns a `parsed_output` attribute.

### Example usage

**`transform_schema()` helper**

For when you need to manually transform schemas before sending, or when you want to modify a Pydantic-generated schema. Unlike `client.messages.parse()`, which transforms provided schemas automatically, this gives you the transformed schema so you can further customize it.

### Example usage

#### 

How SDK transformation works

The Python and TypeScript SDKs automatically transform schemas with unsupported features:

1.  **Remove unsupported constraints** (e.g., `minimum`, `maximum`, `minLength`, `maxLength`)
2.  **Update descriptions** with constraint info (e.g., "Must be at least 100"), when the constraint is not directly supported with structured outputs
3.  **Add `additionalProperties: false`** to all objects
4.  **Filter string formats** to supported list only
5.  **Validate responses** against your original schema (with all constraints)

This means Claude receives a simplified schema, but your code still enforces all constraints through validation.

**Example:** A Pydantic field with `minimum: 100` becomes a plain integer in the sent schema, but the description is updated to "Must be at least 100", and the SDK validates the response against the original constraint.

### 

Common use cases

### Data extraction

### Classification

### API response formatting

## 

Strict tool use

Strict tool use validates tool parameters, ensuring Claude calls your functions with correctly-typed arguments. Use strict tool use when you need to:

- Validate tool parameters
- Build agentic workflows
- Ensure type-safe function calls
- Handle complex tools with nested properties

### 

Why strict tool use matters for agents

Building reliable agentic systems requires guaranteed schema conformance. Without strict mode, Claude might return incompatible types (`"2"` instead of `2`) or missing required fields, breaking your functions and causing runtime errors.

Strict tool use guarantees type-safe parameters:

- Functions receive correctly-typed arguments every time
- No need to validate and retry tool calls
- Production-ready agents that work consistently at scale

For example, suppose a booking system needs `passengers: int`. Without strict mode, Claude might provide `passengers: "two"` or `passengers: "2"`. With `strict: true`, the response will always contain `passengers: 2`.

### 

Quick start

Shell

``` shiki
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "What is the weather in San Francisco?"}
    ],
    "tools": [{
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "strict": true,
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"]
          }
        },
        "required": ["location"],
        "additionalProperties": false
      }
    }]
  }'
```

**Response format:** Tool use blocks with validated inputs in `response.content[x].input`

``` shiki
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

### 

How it works

1.  1

    Define your tool schema

    Create a JSON schema for your tool's `input_schema`. The schema uses standard JSON Schema format with some limitations (see [JSON Schema limitations](#json-schema-limitations)).

2.  2

    Add strict: true

    Set `"strict": true` as a top-level property in your tool definition, alongside `name`, `description`, and `input_schema`.

3.  3

    Handle tool calls

    When Claude uses the tool, the `input` field in the tool_use block will strictly follow your `input_schema`, and the `name` will always be valid.

### 

Common use cases

### Validated tool inputs

### Agentic workflow with multiple validated tools

## 

Using both features together

JSON outputs and strict tool use solve different problems and can be used together:

- **JSON outputs** control Claude's response format (what Claude says)
- **Strict tool use** validates tool parameters (how Claude calls your functions)

When combined, Claude can call tools with guaranteed-valid parameters AND return structured JSON responses. This is useful for agentic workflows where you need both reliable tool calls and structured final outputs.

Python

``` shiki
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Help me plan a trip to Paris for next month"}],
    # JSON outputs: structured response format
    output_config={
        "format": {
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"},
                    "next_steps": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["summary", "next_steps"],
                "additionalProperties": False
            }
        }
    },
    # Strict tool use: guaranteed tool parameters
    tools=[{
        "name": "search_flights",
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {
                "destination": {"type": "string"},
                "date": {"type": "string", "format": "date"}
            },
            "required": ["destination", "date"],
            "additionalProperties": False
        }
    }]
)
```

## 

Important considerations

### 

Grammar compilation and caching

Structured outputs use constrained sampling with compiled grammar artifacts. This introduces some performance characteristics to be aware of:

- **First request latency**: The first time you use a specific schema, there will be additional latency while the grammar is compiled
- **Automatic caching**: Compiled grammars are cached for 24 hours from last use, making subsequent requests much faster
- **Cache invalidation**: The cache is invalidated if you change:
  - The JSON schema structure
  - The set of tools in your request (when using both structured outputs and tool use)
  - Changing only `name` or `description` fields does not invalidate the cache

### 

Prompt modification and token costs

When using structured outputs, Claude automatically receives an additional system prompt explaining the expected output format. This means:

- Your input token count will be slightly higher
- The injected prompt costs you tokens like any other system prompt
- Changing the `output_config.format` parameter will invalidate any [prompt cache](/docs/en/build-with-claude/prompt-caching) for that conversation thread

### 

JSON Schema limitations

Structured outputs support standard JSON Schema with some limitations. Both JSON outputs and strict tool use share these limitations.

### Supported features

### Not supported

### Pattern support (regex)

The Python and TypeScript SDKs can automatically transform schemas with unsupported features by removing them and adding constraints to field descriptions. See [SDK-specific methods](#sdk-specific-methods) for details.

### 

Invalid outputs

While structured outputs guarantee schema compliance in most cases, there are scenarios where the output may not match your schema:

**Refusals** (`stop_reason: "refusal"`)

Claude maintains its safety and helpfulness properties even when using structured outputs. If Claude refuses a request for safety reasons:

- The response will have `stop_reason: "refusal"`
- You'll receive a 200 status code
- You'll be billed for the tokens generated
- The output may not match your schema because the refusal message takes precedence over schema constraints

**Token limit reached** (`stop_reason: "max_tokens"`)

If the response is cut off due to reaching the `max_tokens` limit:

- The response will have `stop_reason: "max_tokens"`
- The output may be incomplete and not match your schema
- Retry with a higher `max_tokens` value to get the complete structured output

### 

Schema validation errors

If your schema uses unsupported features or is too complex, you'll receive a 400 error:

**"Too many recursive definitions in schema"**

- Cause: Schema has excessive or cyclic recursive definitions
- Solution: Simplify schema structure, reduce nesting depth

**"Schema is too complex"**

- Cause: Schema exceeds complexity limits
- Solution: Break into smaller schemas, simplify structure, or reduce the number of tools marked as `strict: true`

For persistent issues with valid schemas, [contact support](https://support.claude.com/en/articles/9015913-how-to-get-support) with your schema definition.

## 

Feature compatibility

**Works with:**

- **[Batch processing](/docs/en/build-with-claude/batch-processing)**: Process structured outputs at scale with 50% discount
- **[Token counting](/docs/en/build-with-claude/token-counting)**: Count tokens without compilation
- **[Streaming](/docs/en/build-with-claude/streaming)**: Stream structured outputs like normal responses
- **Combined usage**: Use JSON outputs (`output_config.format`) and strict tool use (`strict: true`) together in the same request

**Incompatible with:**

- **[Citations](/docs/en/build-with-claude/citations)**: Citations require interleaving citation blocks with text, which conflicts with strict JSON schema constraints. Returns 400 error if citations enabled with `output_config.format`.
- **Message Prefilling**: Incompatible with JSON outputs

**Grammar scope**: Grammars apply only to Claude's direct output, not to tool use calls, tool results, or thinking tags (when using [Extended Thinking](/docs/en/build-with-claude/extended-thinking)). Grammar state resets between sections, allowing Claude to think freely while still producing structured output in the final response.

Was this page helpful?

- 

- [Why use structured outputs](#why-use-structured-outputs)

- [JSON outputs](#json-outputs)

- [Quick start](#quick-start)

- [How it works](#how-it-works)

- [Working with JSON outputs in SDKs](#working-with-json-outputs-in-sdks)

- [Common use cases](#common-use-cases)

- [Strict tool use](#strict-tool-use)

- [Why strict tool use matters for agents](#why-strict-tool-use-matters-for-agents)

- [Quick start](#quick-start-2)

- [How it works](#how-it-works-2)

- [Common use cases](#common-use-cases-2)

- [Using both features together](#using-both-features-together)

- [Important considerations](#important-considerations)

- [Grammar compilation and caching](#grammar-compilation-and-caching)

- [Prompt modification and token costs](#prompt-modification-and-token-costs)

- [JSON Schema limitations](#json-schema-limitations)

- [Invalid outputs](#invalid-outputs)

- [Schema validation errors](#schema-validation-errors)

- [Feature compatibility](#feature-compatibility)

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
