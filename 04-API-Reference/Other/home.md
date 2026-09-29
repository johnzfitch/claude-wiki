---
title: "Documentation - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/home"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:41Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fhome)





Claude Platform

# Start building with Claude

Everything you need to integrate Claude into your applications. From first API call to production.

SearchCtrlK

[Quickstart](../../01-Getting-Started/get-started.md)[Get API key](usage-limits.md)[API reference](../Endpoints/overview.md)

Python

TypeScript

Go

Java

Ruby

PHP

C#

cURL

CLI



```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
  model="claude-opus-5-5",
  max_tokens=1024,
  messages=[{
    "role": "user",
    "content": "Hello, Claude"
  }]
)
for block in message.content:
    if block.type == "text":
        print(block.text)
```

Platform

## Choose how you build

Pick the developer surface that matches your approach, and the infrastructure that fits your stack.

### Messages

Direct model access. You construct every turn, manage conversation state, and write your own tool loop.

[Quickstart](../../01-Getting-Started/get-started.md)[API reference](../Endpoints/messages-create.md)[Client SDKs](cli-sdks-libraries-overview.md)

### Managed Agents

Fully managed agent infrastructure. Deploy and manage autonomous agents in stateful sessions with persistent event history.

[Quickstart](managed-agents-quickstart.md)[API reference](../Endpoints/beta-sessions.md)[Define your agent](managed-agents-agent-setup.md)

Claude is also available on these cloud platforms:

[Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md)

[Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)

[Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

Developer journey

## From idea to production

Follow the lifecycle or jump to what you need.

Messages

Managed Agents

1.  1

    ### Get started

    [Quickstart](../../01-Getting-Started/get-started.md)

    [Get API key](usage-limits.md)

    [Choose a model](../../20-Models/about-claude-models-overview.md)

    [Install an SDK](cli-sdks-libraries-overview.md)

    [Try the API in playground](usage-limits.md)

2.  2

    ### Build

    [Messages API](../Endpoints/messages-create.md)

    [Thinking](../Guides/build-with-claude-thinking.md)

    [Vision](../Guides/build-with-claude-vision.md)

    [Tool use](../Agents-Tools/agents-and-tools-tool-use-overview.md)

    [Web search](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)

    [Code execution](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)

    [Structured outputs](../Guides/build-with-claude-structured-outputs.md)

    [Prompt caching](../Guides/build-with-claude-prompt-caching.md)

    [Streaming](../Guides/build-with-claude-streaming.md)

3.  3

    ### Evaluate and ship

    [Prompting best practices](../../10-Prompting-Guides/build-with-claude-prompt-engineering-overview.md)

    [Run evals](../Test-Evaluate/test-and-evaluate-develop-tests.md)

    [Batch testing](../Guides/build-with-claude-batch-processing.md)

    [Safety and guardrails](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-increase-consistency.md)

    [Rate limits and errors](../Endpoints/rate-limits.md)

    [Cost optimization](../../17-Billing-Plans/about-claude-pricing.md)

4.  4

    ### Operate

    [Workspaces and admin](manage-claude-workspaces.md)

    [API key management](usage-limits.md)

    [Usage monitoring](manage-claude-usage-cost-api.md)

    [Model migration](../../20-Models/about-claude-models-migration-guide.md)

Models

## The Claude model family

Choose the right model for your use case.

### [Fable 5.1](../../20-Models/models-fable-5-1-overview.md)

New

Most capableResearchMulti-day tasks

For demanding reasoning and long-horizon agentic work

### [Opus 5.5](../../20-Models/models-opus-5-5-overview.md)

New

Complex projectsAgentsCoding

For long-running agentic coding and knowledge work

### [Sonnet 5](../../20-Models/models-sonnet-5-overview.md)

Everyday tasksWritingCost-efficient

The best combination of speed and intelligence

### [Haiku 4.5](../../20-Models/models-haiku-4-5-overview.md)

FastestLowest costHigh volume

The fastest model with near-frontier intelligence

Resources

## Keep learning



[Courses](https://academy.claude.com/courses)

Interactive courses to master Claude.



[Cookbook](https://platform.claude.com/cookbook)

Code samples and patterns.



[Quickstarts](https://github.com/anthropics/anthropic-quickstarts)

Deployable starter apps.



[What's new](../../20-Models/release-notes-overview.md)

Latest features and updates.



[Claude Code](../../02-Claude-Code-CLI/code-home.md)

An agentic coding assistant in your terminal.
