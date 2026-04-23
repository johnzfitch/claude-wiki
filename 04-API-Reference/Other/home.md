---
title: "Documentation - Claude API Docs"
source_url: "https://platform.claude.com/docs/en/home"
category: "04-API-Reference/Other"
fetched_at: "2026-03-20T10:36:26Z"
tags: ["api"]
---

Everything you need to integrate Claude into your applications. From first API call to production.

What do you want to build?


Quickstart[](/settings/keys)

Get API key[](/docs/en/api)

API reference

Python

TypeScript

Go

Java

Ruby

PHP

C#

cURL

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
  model="claude-sonnet-4-6",
  max_tokens=1024,
  messages=[{
    "role": "user",
    "content": "Hello, Claude"
  }]
)
print(message.content[0].text)
```

Platform

## Choose how you build

Pick the developer surface that matches your approach, and the infrastructure that fits your stack.

### Claude API

Send a request, get a response. You construct every turn, manage conversation state, and write your own tool loop.


Quickstart


API reference


Client SDKs

### Agent SDK

Claude Code as a library. Give Claude a task and the SDK runs the loop with built-in file, shell, and web tools.


Agent SDK quickstart


TypeScript Agent SDK


Python Agent SDK

[AWS Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock)

[Google Cloud Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai)

[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

Developer journey

## From idea to production

Follow the lifecycle or jump to what you need.

1.  1

    ### Get started


    Quickstart


    Get API key


    Choose a model


    Install an SDK


    Try the Workbench

2.  2

    ### Build


    Messages API

    [Extended thinking](/docs/en/build-with-claude/extended-thinking)


    Vision


    Tool use

    [Web search](/docs/en/agents-and-tools/tool-use/web-search-tool)


    Code execution

    [Structured outputs](/docs/en/build-with-claude/structured-outputs)


    Prompt caching

    [Streaming](/docs/en/build-with-claude/streaming)

3.  3

    ### Evaluate & ship

    [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/overview)


    Run evals

    [Batch testing](/docs/en/build-with-claude/batch-processing)


    Safety & guardrails


    Rate limits & errors

    [Cost optimization](/docs/en/about-claude/pricing)

4.  4

    ### Operate


    Workspaces & admin


    API key management


    Usage monitoring


    Model migration

Models

## The Claude model family

Choose the right model for your use case.

Most capable

[Opus 4.6](/docs/en/about-claude/models/overview)

claude-opus-4-6

Best for complex analysis, coding, and creative tasks requiring deep reasoning.

Best balance

[Sonnet 4.6](/docs/en/about-claude/models/overview)

claude-sonnet-4-6

Ideal balance of intelligence and speed for most production workloads.

Fastest

[Haiku 4.5](/docs/en/about-claude/models/overview)

claude-haiku-4-5

Lightning-fast responses for high-volume, latency-sensitive applications.

Resources

## Keep learning


Courses

Interactive courses to master Claude.


Cookbook

Code samples and patterns.


Quickstarts

Deployable starter apps.


What's new

Latest features and updates.


Claude Code

An agentic coding assistant in your terminal.
