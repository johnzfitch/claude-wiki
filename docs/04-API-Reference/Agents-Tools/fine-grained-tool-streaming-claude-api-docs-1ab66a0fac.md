---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:21Z"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming"
title: "Fine-grained tool streaming - Claude API Docs"
---

Tools

# Fine-grained tool streaming

Copy page

Copy page

Fine-grained tool streaming is generally available on all models and all platforms, with no beta header required. It enables [streaming](/docs/en/build-with-claude/streaming) of tool use parameter values without buffering or JSON validation, reducing the latency to begin receiving large parameters.

When using fine-grained tool streaming, you may potentially receive invalid or partial JSON inputs. Make sure to account for these edge cases in your code.

## 

How to use fine-grained tool streaming

Fine-grained tool streaming is available on all models and all platforms (Claude API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry). To use it, set `eager_input_streaming` to `true` on any tool where you want fine-grained streaming enabled, and enable streaming on your request.

Here's an example of how to use fine-grained tool streaming with the API:

Shell

``` shiki
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 65536,
    "tools": [
      {
        "name": "make_file",
        "description": "Write text to a file",
        "eager_input_streaming": true,
        "input_schema": {
          "type": "object",
          "properties": {
            "filename": {
              "type": "string",
              "description": "The filename to write text to"
            },
            "lines_of_text": {
              "type": "array",
              "description": "An array of lines of text to write to the file"
            }
          },
          "required": ["filename", "lines_of_text"]
        }
      }
    ],
    "messages": [
      {
        "role": "user",
        "content": "Can you write a long poem and make a file called poem.txt?"
      }
    ],
    "stream": true
  }' | jq '.usage'
```

In this example, fine-grained tool streaming enables Claude to stream the lines of a long poem into the tool call `make_file` without buffering to validate if the `lines_of_text` parameter is valid JSON. This means you can see the parameter stream as it arrives, without having to wait for the entire parameter to buffer and validate.

With fine-grained tool streaming, tool use chunks start streaming faster, and are often longer and contain fewer word breaks. This is due to differences in chunking behavior.

Example:

Without fine-grained streaming (15s delay):

``` inline-block
Chunk 1: '{"'
Chunk 2: 'query": "Ty'
Chunk 3: 'peScri'
Chunk 4: 'pt 5.0 5.1 '
Chunk 5: '5.2 5'
Chunk 6: '.3'
Chunk 8: ' new f'
Chunk 9: 'eatur'
...
```

With fine-grained streaming (3s delay):

``` inline-block
Chunk 1: '{"query": "TypeScript 5.0 5.1 5.2 5.3'
Chunk 2: ' new features comparison'
```

Because fine-grained streaming sends parameters without buffering or JSON validation, there is no guarantee that the resulting stream will complete in a valid JSON string. Particularly, if the [stop reason](/docs/en/build-with-claude/handling-stop-reasons) `max_tokens` is reached, the stream may end midway through a parameter and may be incomplete. You will generally have to write specific support to handle when `max_tokens` is reached.

## 

Handling invalid JSON in tool responses

When using fine-grained tool streaming, you may receive invalid or incomplete JSON from the model. If you need to pass this invalid JSON back to the model in an error response block, you may wrap it in a JSON object to ensure proper handling (with a reasonable key). For example:

``` shiki
{
  "INVALID_JSON": "<your invalid json string>"
}
```

This approach helps the model understand that the content is invalid JSON while preserving the original malformed data for debugging purposes.

When wrapping invalid JSON, make sure to properly escape any quotes or special characters in the invalid JSON string to maintain valid JSON structure in the wrapper object.

Was this page helpful?

- 

- [How to use fine-grained tool streaming](#how-to-use-fine-grained-tool-streaming)

- [Handling invalid JSON in tool responses](#handling-invalid-json-in-tool-responses)

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
