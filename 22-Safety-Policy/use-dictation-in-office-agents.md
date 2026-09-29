---
title: "Use dictation in Claude for M365 - Claude.ai Documentation"
source_url: "https://support.claude.com/en/articles/14479591-use-dictation-in-office-agents"
category: "22-Safety-Policy"
fetched_at: "2026-09-14T06:26:59Z"
tags: ["safety"]
---

## On this page

- [Use dictation](#use-dictation)
- [How it works](#how-it-works)
- [Why dictation is not available with third-party authentication](#why-dictation-is-not-available-with-third-party-authentication)

Features

# Use dictation in Claude for M365

Copy pageCopy page

Speak your prompts instead of typing them in Claude for Excel, PowerPoint, Word, and Outlook.

Copy pageCopy page

Dictation lets you speak prompts instead of typing them. Click the microphone icon in the chat input, speak, and see your words appear in the composer in real time.

Dictation requires the desktop version of Excel, PowerPoint, Word, or Outlook. It is not available in Office on the web because browser-hosted add-ins cannot access the microphone. On the web, use your operating system’s built-in dictation or your Office application’s dictation feature instead.Dictation is also available only for organizations using direct Claude authentication. It is not supported when Claude for M365 connects through a third-party platform such as Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an LLM gateway. See [Use Claude for M365 with third-party platforms](https://support.claude.com/docs/office-agents/third-party-platforms) for platform support details.


[​](#use-dictation)

Use dictation

1

Start listening

Click the microphone icon on the right side of the chat input. The placeholder changes to “Listening…” and the button highlights.

2

Speak your prompt

Words appear in the composer as you talk.

3

Stop or send

Click the microphone again to stop, or press Enter to stop and send in one step.

To select a different microphone, hover over the microphone icon and click the arrow that appears.


[​](#how-it-works)

How it works

When you start dictating, the add-in streams your audio to Anthropic’s transcription service, the same infrastructure that powers dictation in the Claude apps. The transcribed text displays in real time in the composer. Nothing is transcribed on your device. Audio is streamed to Anthropic, which uses a contracted speech-to-text subprocessor to generate the transcript. Audio is not retained after transcription; only the resulting text remains in your composer.


[​](#why-dictation-is-not-available-with-third-party-authentication)

Why dictation is not available with third-party authentication

In third-party environments, Claude for M365 does not send prompts to Anthropic directly. Spoken audio is effectively a prompt, so dictation is not offered there. Use your operating system’s built-in dictation or your Office application’s dictation feature instead.
