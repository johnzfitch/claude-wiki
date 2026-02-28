---
category: "19-Reference"
fetched_at: "2026-02-24T05:03:44Z"
source_url: "https://www.anthropic.com/news/expanded-legal-protections-api-improvements"
title: "Expanded legal protections and improvements to our API \\ Anthropic"
---
# Expanded legal protections and improvements to our API

Dec 19, 2023

We are introducing new, simplified Commercial Terms of Service with an expanded copyright indemnity, as well as an improved developer experience with our beta Messages API. Customers will now enjoy increased protection and peace of mind as they build with Claude, as well as a more streamlined API that is easier to use.

## Improved terms of service

Our Commercial Terms of Service (previously our services agreement) will enable our customers to retain ownership rights over any outputs they generate through their use of our services and protect them from copyright infringement claims. Under the updated terms, we will defend our customers from any copyright infringement claim made against them for their authorized use of our services or their outputs, and we will pay for any approved settlements or judgments that result. These new terms will be live on January 1, 2024 for Claude API customers and January 2, 2024 for those using Claude through Amazon Bedrock.\
\
For more details, you can review our updated [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), or our [Anthropic on Amazon Bedrock - Commercial Terms of Service](https://www-cdn.anthropic.com/6b68a6508f0210c5fe08f0199caa05c4ee6fb4dc/Anthropic-on-Bedrock-Commercial-Terms-of-Service_Dec_2023.pdf).

## Messages API beta

It’s easy to make subtle mistakes when formatting prompts for our existing API — particularly when prompts are dynamically constructed from a mix of user inputs. The new [Messages API](https://docs.anthropic.com/claude/reference/messages_post) will help you catch errors early in development, particularly with respect to prompt construction, so that you can get the best output from Anthropic's models.

Example request, before:

```
// POST https://api.anthropic.com/v1/complete
{
  "model": "claude-2.1",
  "max_tokens_to_sample": 1024,
  "prompt": "\n\nHuman: Hello, world\n\nAssistant: Hi, I'm Claude!\n\nHuman: Can you create a template for a quarterly executive brief?\n\nAssistant:"
}
```

Copy

After:

```
// POST https://api.anthropic.com/v1/messages
{
  "model": "claude-2.1",
  "max_tokens": 1024,
  "messages": [
    { "role": "user", "content": "Hello, world" },
    { "role": "assistant", "content": "Hi, I'm Claude!" },
    { "role": "user", "content": "Can you create a template for a quarterly executive brief?" }
  ]
}
```

Copy

\

We have many upcoming features planned that are enabled by a richer, structured API. This beta feature is our first step in offering services like robust function calling, which will be coming to the Messages API soon.\
\
In addition to these updates, we plan to broaden access to the Claude API in the coming weeks so developers and enterprises can build with our trusted AI solutions.


## Related content

### Detecting and preventing distillation attacks

[Read more](/news/detecting-and-preventing-distillation-attacks)

### Making frontier cybersecurity capabilities available to defenders

Claude Code Security, a new capability built into Claude Code on the web, is now available in a limited research preview. It scans codebases for security vulnerabilities and suggests targeted software patches for human review, allowing teams to find and fix security issues that traditional methods often miss.

[Read more](/news/claude-code-security)

### Anthropic and the Government of Rwanda sign MOU for AI in health and education

[Read more](/news/anthropic-rwanda-mou)
