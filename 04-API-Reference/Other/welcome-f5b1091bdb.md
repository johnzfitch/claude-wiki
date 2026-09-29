---
title: "Intro to Claude - Claude Platform Docs"
source_url: "https://platform.claude.com/en/docs/welcome"
category: "04-API-Reference/Other"
fetched_at: "2026-09-23T06:27:35Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fintro)





SearchCtrlK

First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)[Authentication](/docs/en/manage-claude/authentication)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

[Thinking](/docs/en/build-with-claude/thinking)

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics (beta)](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[Console](/)

MessagesFirst steps

# Intro to Claude

Copy page



Claude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more.

Copy page





Looking to chat with Claude? Visit [claude.ai](https://claude.ai).

Anthropic offers two ways to build with Claude, each suited to different use cases:

|                | Messages API                                | Claude Managed Agents                                                     |
|----------------|---------------------------------------------|---------------------------------------------------------------------------|
| **What it is** | Direct model prompting access               | Pre-built, configurable agent harness that runs in managed infrastructure |
| **Best for**   | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work                                  |

To learn more about each, see [Using the Messages API](/docs/en/build-with-claude/working-with-messages) and the [Claude Managed Agents overview](/docs/en/managed-agents/overview).

## Explore the latest generation of Claude models

If you're unsure which model to use, start with [Claude Opus 5.5](/docs/en/models/opus-5-5/overview) for most workloads. Use [Claude Fable 5.1](/docs/en/models/fable-5-1/overview) for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short. All current models support text and image input, text output, multilingual capabilities, vision, and tool use. Each model's page lists the platforms it's available on.

### [Fable 5.1](/docs/en/models/fable-5-1/overview)

New

Most capableResearchMulti-day tasks

For demanding reasoning and long-horizon agentic work

### [Opus 5.5](/docs/en/models/opus-5-5/overview)

New

Complex projectsAgentsCoding

For long-running agentic coding and knowledge work

### [Sonnet 5](/docs/en/models/sonnet-5/overview)

Everyday tasksWritingCost-efficient

The best combination of speed and intelligence

### [Haiku 4.5](/docs/en/models/haiku-4-5/overview)

FastestLowest costHigh volume

The fastest model with near-frontier intelligence

[Compare models](/docs/en/models/overview)

------------------------------------------------------------------------

## Recommended path for new developers

Follow these steps to go from zero to a working Claude integration.

1.  1

    ### Make your first API call

    Set up your environment, install an SDK, and send your first message to Claude.

    [Go to the quickstart](/docs/en/get-started)

2.  2

    ### Secure your credentials

    Set an expiration when you create your API key. Keep the key out of source control, client-side code, and prompts. Check whether your workload can use Workload Identity Federation instead of a static key.

    [Read the authentication guide](/docs/en/manage-claude/authentication)

3.  3

    ### Understand the Messages API

    Learn the core request and response structure, including multi-turn conversations, system prompts, and stop reasons.

    [Read the Messages API guide](/docs/en/build-with-claude/working-with-messages)

4.  4

    ### Choose the right model

    Compare Claude models by capability and cost to pick the best fit for your use case.

    [See the models overview](/docs/en/models/overview)

5.  5

    ### Explore features and tools

    Discover what Claude can do: extended thinking, web search, file handling, structured outputs, and more.

    [Browse the features overview](/docs/en/build-with-claude/overview)

------------------------------------------------------------------------

## Develop with Claude

Anthropic provides developer tools to help you build and scale applications with Claude.



[Developer Console](/)

Explore and understand the API in your browser with playground.



[API Reference](/docs/en/api/overview)

Explore the full Claude API and client SDK documentation.

[Claude Cookbook](https://platform.claude.com/cookbook)

Learn with interactive Jupyter notebooks covering PDFs, embeddings, and more.

------------------------------------------------------------------------

## Key capabilities

Claude can assist with many tasks that involve text, code, and images.



[Text and code generation](/docs/en/build-with-claude/overview)

Summarize text, answer questions, extract data, translate text, and explain and generate code.



[Vision](/docs/en/build-with-claude/vision)

Process and analyze visual input and generate text and code from images.

------------------------------------------------------------------------

## Support



[Help Center](https://support.claude.com/en/)

Find answers to frequently asked account and billing questions.



[Service Status](https://status.claude.com)

Check the status of Anthropic services.
