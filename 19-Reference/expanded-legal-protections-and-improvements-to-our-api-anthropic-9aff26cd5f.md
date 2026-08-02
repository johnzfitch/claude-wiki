---
title: "Expanded legal protections and improvements to our API \\ Anthropic"
source_url: "https://www.anthropic.com/news/expanded-legal-protections-api-improvements"
category: "19-Reference"
fetched_at: "2026-08-02T05:42:17Z"
tags: ["api"]
---

# Expanded legal protections and improvements to our API

Dec 19, 2023

We are introducing new, simplified Commercial Terms of Service with an expanded copyright indemnity, as well as an improved developer experience with our beta Messages API. Customers will now enjoy increased protection and peace of mind as they build with Claude, as well as a more streamlined API that is easier to use.

## Improved terms of service

Our Commercial Terms of Service (previously our services agreement) will enable our customers to retain ownership rights over any outputs they generate through their use of our services and protect them from copyright infringement claims. Under the updated terms, we will defend our customers from any copyright infringement claim made against them for their authorized use of our services or their outputs, and we will pay for any approved settlements or judgments that result. These new terms will be live on January 1, 2024 for Claude API customers and January 2, 2024 for those using Claude through Amazon Bedrock.  
  
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

  
We have many upcoming features planned that are enabled by a richer, structured API. This beta feature is our first step in offering services like robust function calling, which will be coming to the Messages API soon.  
  
In addition to these updates, we plan to broaden access to the Claude API in the coming weeks so developers and enterprises can build with our trusted AI solutions.


## Related content

### Investigating three real-world incidents in our cybersecurity evaluations

[Read more](/news/investigating-incidents-cybersecurity-evals)

### Our position on open-weights models

[Read more](/news/position-open-weights-models)

### Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients

[Read more](/news/cognizant-anthropic)

[](/)

### Products

- [Claude](https://claude.com/product/overview)
- [Claude Code](https://claude.com/product/claude-code)
- [Claude Code Enterprise](https://claude.com/product/claude-code/enterprise)
- [Claude Cowork](https://claude.com/product/cowork)
- [@Claude](https://claude.com/product/tag)
- [Claude Design](https://claude.com/product/design)
- [Claude Science](https://claude.com/product/claude-science)
- [Claude Security](https://claude.com/product/claude-security)
- [Claude for Chrome](https://claude.com/chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](https://claude.com/pricing)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Cybersecurity](https://claude.com/solutions/cybersecurity)
- [Enterprise](https://claude.com/solutions/enterprise)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Healthcare](https://claude.com/solutions/healthcare)
- [Higher education](https://claude.com/solutions/education)
- [K-12 teachers](https://claude.com/solutions/teachers)
- [Legal](https://claude.com/solutions/legal)
- [Life sciences](https://claude.com/solutions/life-sciences)
- [Nonprofits](https://claude.com/solutions/nonprofits)
- [Small business](https://claude.com/solutions/small-business)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](https://platform.claude.com/docs)
- [Pricing](https://claude.com/pricing#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](https://claude.com/partners/claude-on-aws)
- [Google Cloud](https://claude.com/partners/google-cloud-vertex-ai)
- [Microsoft Foundry](https://claude.com/partners/microsoft-foundry)
- [Console login](https://platform.claude.com/)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](https://claude.com/partners)
- [Community](https://claude.com/community)
- [Connectors](https://claude.com/connectors)
- [Courses](/learn)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](/engineering)
- [Events](/events)
- [Plugins](https://claude.com/plugins)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](https://claude.com/programs/startups)
- [Research Labs](https://claude.com/programs/claude-team-plan-for-research-labs)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](/company)
- [Careers](/careers)
- [Policy](/policy)
- [Economic Futures](/economic-futures)
- [Research](/research)
- [News](/news)
- [Claude’s Constitution](/constitution)
- [Claude Corps](/claude-corps)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](/transparency)
