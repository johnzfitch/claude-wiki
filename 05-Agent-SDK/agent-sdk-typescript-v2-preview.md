---
title: "TypeScript SDK V2 session API (removed) - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview"
category: "05-Agent-SDK"
fetched_at: "2026-09-16T06:23:59Z"
tags: ["agents", "api", "claude-code", "sdk", "typescript"]
---

## On this page

- [Installation](#installation)
- [Quick start](#quick-start)
  - [One-shot prompt](#one-shot-prompt)
  - [Basic session](#basic-session)
  - [Multi-turn conversation](#multi-turn-conversation)
  - [Session resume](#session-resume)
  - [Cleanup](#cleanup)
- [API reference](#api-reference)
  - [unstable_v2_createSession()](#unstable_v2_createsession)
  - [unstable_v2_resumeSession()](#unstable_v2_resumesession)
  - [unstable_v2_prompt()](#unstable_v2_prompt)
  - [SDKSession interface](#sdksession-interface)
- [Feature availability](#feature-availability)
- [See also](#see-also)

SDK references

# TypeScript SDK V2 session API (removed)

Copy pageCopy page

Reference for the removed V2 TypeScript Agent SDK session API, with session-based send/stream patterns for multi-turn conversations.

Copy pageCopy page

The V2 session API is no longer supported. TypeScript Agent SDK 0.3.142 removes `unstable_v2_createSession`, `unstable_v2_resumeSession`, `unstable_v2_prompt`, and the `SDKSession` and `SDKSessionOptions` types.To migrate, use the [`query()` API](agent-sdk-typescript.md) and the [session options](agent-sdk-sessions.md) it accepts. Pass an `AsyncIterable<SDKUserMessage>` for multi-turn conversations, or `options.resume` to continue a saved session. This page is kept for reference if you maintain code on Agent SDK 0.2.x or earlier.

V2 was an experimental session API that removed the need for async generators and yield coordination. Instead of managing generator state across turns, each turn was a separate `send()`/`stream()` cycle. The API surface reduced to creating a session, sending a message, and streaming the response:

- `createSession()` / `resumeSession()`: Start or continue a conversation
- `session.send()`: Send a message
- `session.stream()`: Get the response


[​](#installation)

Installation

Agent SDK 0.2.x is the last version that includes the V2 interface. The package version jumped from 0.2.x directly to 0.3.142, so the removal version above and the install pin below describe the same boundary. To install the last V2-compatible release, pin the major and minor version:

```python
npm install @anthropic-ai/claude-agent-sdk@0.2
```

The SDK bundles a native Claude Code binary for your platform as an optional dependency, so most installs need no separate Claude Code install. See the [quickstart’s install note](agent-sdk-quickstart.md) for the installs that need one.


[​](#quick-start)

Quick start


[​](#one-shot-prompt)

One-shot prompt

For simple single-turn queries where you don’t need to maintain a session, use `unstable_v2_prompt()`. This example sends a math question and logs the answer:

```python
import { unstable_v2_prompt } from "@anthropic-ai/claude-agent-sdk";

const result = await unstable_v2_prompt("What is 2 + 2?", {
  model: "claude-opus-4-7"
});
if (result.subtype === "success") {
  console.log(result.result);
}
```


[​](#basic-session)

Basic session

For interactions beyond a single prompt, create a session. V2 separates sending and streaming into distinct steps:

- `send()` dispatches your message
- `stream()` streams back the response

This explicit separation makes it easier to add logic between turns (like processing responses before sending follow-ups). The example below creates a session, sends “Hello!” to Claude, and prints the text response. It uses [`await using`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html#using-declarations-and-explicit-resource-management) (TypeScript 5.2+) to automatically close the session when the block exits. You can also call `session.close()` manually.

```python
import { unstable_v2_createSession } from "@anthropic-ai/claude-agent-sdk";

await using session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});

await session.send("Hello!");
for await (const msg of session.stream()) {
  // Filter for assistant messages to get human-readable output
  if (msg.type === "assistant") {
    const text = msg.message.content
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("");
    console.log(text);
  }
}
```


[​](#multi-turn-conversation)

Multi-turn conversation

Sessions persist context across multiple exchanges. To continue a conversation, call `send()` again on the same session. Claude remembers the previous turns. This example asks a math question, then asks a follow-up that references the previous answer:

```python
import { unstable_v2_createSession } from "@anthropic-ai/claude-agent-sdk";

await using session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});

// Turn 1
await session.send("What is 5 + 3?");
for await (const msg of session.stream()) {
  // Filter for assistant messages to get human-readable output
  if (msg.type === "assistant") {
    const text = msg.message.content
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("");
    console.log(text);
  }
}

// Turn 2
await session.send("Multiply that by 2");
for await (const msg of session.stream()) {
  if (msg.type === "assistant") {
    const text = msg.message.content
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("");
    console.log(text);
  }
}
```


[​](#session-resume)

Session resume

If you have a session ID from a previous interaction, you can resume it later. This is useful for long-running workflows or when you need to persist conversations across application restarts. This example creates a session, stores its ID, closes it, then resumes the conversation:

```python
import {
  unstable_v2_createSession,
  unstable_v2_resumeSession,
  type SDKMessage
} from "@anthropic-ai/claude-agent-sdk";

// Helper to extract text from assistant messages
function getAssistantText(msg: SDKMessage): string | null {
  if (msg.type !== "assistant") return null;
  return msg.message.content
    .filter((block) => block.type === "text")
    .map((block) => block.text)
    .join("");
}

// Create initial session and have a conversation
const session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});

await session.send("Remember this number: 42");

// Get the session ID from any received message
let sessionId: string | undefined;
for await (const msg of session.stream()) {
  sessionId = msg.session_id;
  const text = getAssistantText(msg);
  if (text) console.log("Initial response:", text);
}

console.log("Session ID:", sessionId);
session.close();

// Later: resume the session using the stored ID
await using resumedSession = unstable_v2_resumeSession(sessionId!, {
  model: "claude-opus-4-7"
});

await resumedSession.send("What number did I ask you to remember?");
for await (const msg of resumedSession.stream()) {
  const text = getAssistantText(msg);
  if (text) console.log("Resumed response:", text);
}
```


[​](#cleanup)

Cleanup

Sessions can be closed manually or automatically using [`await using`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html#using-declarations-and-explicit-resource-management), a TypeScript 5.2+ feature for automatic resource cleanup. If you’re using an older TypeScript version or encounter compatibility issues, use manual cleanup instead. The examples below show only the cleanup pattern and don’t send any messages, so running them produces no output. **Automatic cleanup (TypeScript 5.2+):**

```python
import { unstable_v2_createSession } from "@anthropic-ai/claude-agent-sdk";

await using session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});
// Session closes automatically when the block exits
```

**Manual cleanup:**

```python
import { unstable_v2_createSession } from "@anthropic-ai/claude-agent-sdk";

const session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});
// ... use the session ...
session.close();
```


[​](#api-reference)

API reference


[​](#unstable_v2_createsession)

`unstable_v2_createSession()`

Creates a new session for multi-turn conversations.

```python
function unstable_v2_createSession(options: {
  model: string;
  // Additional options supported
}): SDKSession;
```


[​](#unstable_v2_resumesession)

`unstable_v2_resumeSession()`

Resumes an existing session by ID.

```python
function unstable_v2_resumeSession(
  sessionId: string,
  options: {
    model: string;
    // Additional options supported
  }
): SDKSession;
```


[​](#unstable_v2_prompt)

`unstable_v2_prompt()`

One-shot convenience function for single-turn queries.

```python
function unstable_v2_prompt(
  prompt: string,
  options: {
    model: string;
    // Additional options supported
  }
): Promise<SDKResultMessage>;
```


[​](#sdksession-interface)

SDKSession interface

```python
interface SDKSession {
  readonly sessionId: string;
  send(message: string | SDKUserMessage): Promise<void>;
  stream(): AsyncGenerator<SDKMessage, void>;
  close(): void;
}
```


[​](#feature-availability)

Feature availability

The V2 session API does not support every V1 feature. The following require the [V1 SDK](agent-sdk-typescript.md):

- Session forking (`forkSession` option)
- Some advanced streaming input patterns


[​](#see-also)

See also

- [TypeScript SDK reference (V1)](agent-sdk-typescript.md) - Full V1 SDK documentation
- [SDK overview](agent-sdk-overview.md) - General SDK concepts
- [V2 examples on GitHub](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/hello-world-v2) - Working code examples
