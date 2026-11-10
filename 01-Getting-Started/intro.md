---
title: "Intro to Claude - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/intro"
category: "01-Getting-Started"
fetched_at: "2026-11-05T06:36:16Z"
tags: ["getting-started"]
---

# Intro to Claude

Copy page



Claude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more.

Copy page





Looking to chat with Claude? Visit [claude.ai](https://claude.ai).

Anthropic offers two ways to build with Claude, each suited to different use cases:

|  | Messages API | Claude Managed Agents |
|----|----|----|
| **What it is** | Direct model prompting access | Pre-built, configurable agent harness that runs in managed infrastructure |
| **Best for** | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work |

To learn more about each, see [Using the Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md) and the [Claude Managed Agents overview](../04-API-Reference/Other/managed-agents-overview.md).

## Explore the latest generation of Claude models

If you’re unsure which model to use, start with [Claude Opus 5.5](../20-Models/models-opus-5-5-overview.md) for most workloads. Use [Claude Fable 5.1](../20-Models/models-fable-5-1-overview.md) for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short. All current models support text and image input, text output, multilingual capabilities, vision, and tool use. Each model’s page lists the platforms it’s available on.

### [Fable 5.1](../20-Models/models-fable-5-1-overview.md)

New

Most capableResearchMulti-day tasks

For demanding reasoning and long-horizon agentic work

### [Opus 5.5](../20-Models/models-opus-5-5-overview.md)

New

Complex projectsAgentsCoding

For long-running agentic coding and knowledge work

### [Sonnet 5.5](../20-Models/models-sonnet-5-5-overview.md)

New

Everyday tasksWritingCost-efficient

The best combination of speed and intelligence

### [Haiku 5.5](../20-Models/models-haiku-5-5-overview.md)

New

FastestLowest costHigh volume

For high-volume, latency-sensitive tasks such as classification, extraction, and routing

[Compare models](../20-Models/about-claude-models-overview.md)

------------------------------------------------------------------------

## Recommended path for new developers

Follow these steps to build a working Claude integration.

1.  1

    ### Make your first API call

    Set up your environment, install an SDK, and send your first message to Claude.

    [Go to the quickstart](get-started.md)

2.  2

    ### Secure your credentials

    Set an expiration when you create your API key. Keep the key out of source control, client-side code, and prompts. Check whether your workload can use Workload Identity Federation instead of a static key.

    [Read the authentication guide](../04-API-Reference/Other/manage-claude-authentication.md)

3.  3

    ### Understand the Messages API

    Learn the core request and response structure, including multi-turn conversations, system prompts, and stop reasons.

    [Read the Messages API guide](../04-API-Reference/Guides/build-with-claude-working-with-messages.md)

4.  4

    ### Choose the right model

    Compare Claude models by capability and cost to pick the best fit for your use case.

    [See the models overview](../20-Models/about-claude-models-overview.md)

5.  5

    ### Explore features and tools

    Discover what Claude can do: thinking, web search, file handling, structured outputs, and more.

    [Browse the features overview](../04-API-Reference/Guides/build-with-claude-overview.md)

------------------------------------------------------------------------

## Develop with Claude

Anthropic provides developer tools to help you build and scale applications with Claude.



[Claude Console](../04-API-Reference/Other/playground.md)

Explore and understand the API in your browser with playground.



[API reference](../04-API-Reference/Endpoints/overview.md)

Explore the full Claude API and client SDK documentation.

[Claude Cookbook](https://platform.claude.com/cookbook)

Learn with interactive Jupyter notebooks covering PDFs, embeddings, and more.

------------------------------------------------------------------------

## Key capabilities

Claude can help with many tasks that involve text, code, and images.



[Text and code generation](../04-API-Reference/Guides/build-with-claude-overview.md)

Summarize text, answer questions, extract data, translate text, and explain and generate code.



[Vision](../04-API-Reference/Guides/build-with-claude-vision.md)

Process and analyze visual input and generate text and code from images.

------------------------------------------------------------------------

## Support



[Help Center](https://support.claude.com/en/)

Find answers to frequently asked account and billing questions.



[Service status](https://status.claude.com)

Check the status of Anthropic services.
