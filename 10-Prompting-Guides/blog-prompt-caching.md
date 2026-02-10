<!-- Source: https://claude.com/blog/prompt-caching -->

# Prompt Caching with Claude

## Overview

Claude's prompt caching feature enables developers to cache frequently used context between API calls, significantly reducing costs and latency for long prompts. The feature is now generally available on the Anthropic API and available in preview on Amazon Bedrock and Google Cloud's Vertex AI.

## Key Benefits

Prompt caching can deliver substantial improvements:

- **Cost reduction**: Up to 90% savings on cached prompt usage
- **Latency improvement**: Up to 85% faster response times for long prompts
- **Real-world example**: A 100,000-token cached prompt for "chat with a book" reduced time-to-first-token from 11.5 seconds to 2.4 seconds while achieving 90% cost reduction

## Use Cases

The feature works well for scenarios involving repeated context:

- Conversational agents with long instructions or uploaded documents
- Coding assistants analyzing codebases
- Large document processing with embedded images
- Extended instruction sets (including dozens of high-quality examples)
- Multi-turn tool use requiring iterative API calls
- Knowledge base interactions via document embedding

## Pricing Model

Cached prompts use a two-tier pricing structure:

- **Cache writes**: 25% more than standard input token pricing
- **Cache reads**: 10% of standard input token pricing

For example, Claude 3.5 Sonnet charges $3.75 per million tokens for writing cache but only $0.30 per million tokens for reading cached content (versus $3 for standard input).

## Notable Adoption

Notion integrated prompt caching into its AI assistant to optimize performance and user experience while reducing operational costs.
