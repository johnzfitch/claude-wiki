---
title: "Documentation - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/home"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:39Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console






Browse

Claude Platform

# Start building with Claude

Everything you need to integrate Claude into your applications. From first API call to production.



What do you want to build?


[Quickstart](/docs/en/get-started)[Get API key](/settings/keys)[API reference](/docs/en/api/overview)

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
  model="claude-opus-5",
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

[Quickstart](/docs/en/get-started)[API reference](/docs/en/api/messages/create)[Client SDKs](/docs/en/api/client-sdks)

### Managed Agents

Fully managed agent infrastructure. Deploy and manage autonomous agents in stateful sessions with persistent event history.

[Quickstart](/docs/en/managed-agents/quickstart)[API reference](/docs/en/api/beta/sessions)[Define your agent](/docs/en/managed-agents/agent-setup)

[Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

Developer journey

## From idea to production

Follow the lifecycle or jump to what you need.

Messages

Managed Agents

1.  1

    ### Get started

    [Quickstart](/docs/en/get-started)[Get API key](/settings/keys)[Choose a model](/docs/en/about-claude/models/overview)[Install an SDK](/docs/en/api/client-sdks)[Try the Workbench](/playground)

2.  2

    ### Build

    [Messages API](/docs/en/api/messages/create)[Thinking](/docs/en/build-with-claude/thinking)[Vision](/docs/en/build-with-claude/vision)[Tool use](/docs/en/agents-and-tools/tool-use/overview)[Web search](/docs/en/agents-and-tools/tool-use/web-search-tool)[Code execution](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Streaming](/docs/en/build-with-claude/streaming)

3.  3

    ### Evaluate and ship

    [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/overview)[Run evals](/docs/en/test-and-evaluate/develop-tests)[Batch testing](/docs/en/build-with-claude/batch-processing)[Safety and guardrails](/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)[Rate limits and errors](/docs/en/api/rate-limits)[Cost optimization](/docs/en/about-claude/pricing)

4.  4

    ### Operate

    [Workspaces and admin](/docs/en/build-with-claude/workspaces)[API key management](/settings/keys)[Usage monitoring](/docs/en/build-with-claude/usage-cost-api)[Model migration](/docs/en/about-claude/models/migration-guide)

Models

## The Claude model family

Choose the right model for your use case.

Most capable

[Fable 5](/docs/en/about-claude/models/overview)

claude-fable-5

Highest capability for the most demanding reasoning and long-horizon agentic work.

Advanced

[Opus 5](/docs/en/about-claude/models/overview)

claude-opus-5

Excellent for complex analysis, coding, and creative tasks requiring deep reasoning.

Best balance

[Sonnet 5](/docs/en/about-claude/models/overview)

claude-sonnet-5

Ideal balance of intelligence and speed for most production workloads.

Fastest

[Haiku 4.5](/docs/en/about-claude/models/overview)

claude-haiku-4-5

Lightning-fast responses for high-volume, latency-sensitive applications.

Resources

## Keep learning




Courses



Interactive courses to master Claude.




Cookbook



Code samples and patterns.




Quickstarts



Deployable starter apps.




What's new

Latest features and updates.


Claude Code



An agentic coding assistant in your terminal.
