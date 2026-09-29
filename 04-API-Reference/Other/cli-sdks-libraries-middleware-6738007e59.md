---
title: "SDK middleware - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/middleware"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:29Z"
tags: ["api", "cli", "sdk"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fcli-sdks-libraries%2Fmiddleware)





SearchCtrlK

CLI, SDKs, and libraries

[Overview](/docs/en/cli-sdks-libraries/overview)

ant CLI

[Quickstart](/docs/en/cli-sdks-libraries/cli/quickstart)[Authentication options](/docs/en/cli-sdks-libraries/cli/authentication)[Using the CLI](/docs/en/cli-sdks-libraries/cli/using)[Scripting and automation](/docs/en/cli-sdks-libraries/cli/scripting)[Manage resources as code](/docs/en/cli-sdks-libraries/cli/apply)[Connect to a Managed Agents session](/docs/en/cli-sdks-libraries/cli/sessions-connect)

Client SDKs

[Middleware](/docs/en/cli-sdks-libraries/middleware)[Python](/docs/en/cli-sdks-libraries/sdks/python)[TypeScript](/docs/en/cli-sdks-libraries/sdks/typescript)[C#](/docs/en/cli-sdks-libraries/sdks/csharp)[Go](/docs/en/cli-sdks-libraries/sdks/go)[Java](/docs/en/cli-sdks-libraries/sdks/java)[PHP](/docs/en/cli-sdks-libraries/sdks/php)[Ruby](/docs/en/cli-sdks-libraries/sdks/ruby)

Libraries and integrations

[Apple Foundation Models](/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)[OpenAI SDK compatibility](/docs/en/cli-sdks-libraries/libraries/openai-sdk)

[Console](/)

[CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)Client SDKs

# SDK middleware

Copy page



Intercept and modify requests and responses in the Anthropic SDKs.

Copy page



The Anthropic SDKs provide a middleware (or interceptor) hook that lets you run code before a request is sent and after the response is received. Use middleware for cross-cutting concerns such as logging, custom retries, request annotation, and refusal fallback handling.

Each middleware can inspect or replace the request before calling `next()`, and the response after `next()` returns.

## Registering middleware

Each middleware is a function that receives the outgoing request and a `next` callable. Call `next` to forward the request to the rest of the chain (or directly to the SDK core if this is the last middleware), and return its response. Anything before the `next` call runs on the way out; anything after runs on the way back.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
def logging_middleware(request: APIRequest, call_next: CallNext) -> APIResponse[Any]:
    # Before the request
    print(f"-> {request.method} {request.url}")

    # Forward the request to the rest of the chain
    response = call_next(request)

    # After the request
    print(f"<- {response.status_code}")

    return response


client = Anthropic(middleware=[logging_middleware])
```

## Middleware ordering

When you register multiple middleware, they apply in the order given: the first middleware's "before" code runs first, and its "after" code runs last. Middleware registered on the client runs before middleware passed as a per-request option.

In the Go SDK, repeated `option.WithMiddleware` calls concatenate (client first, then method). In the other SDKs, pass an array; later entries wrap inner.

## Replacing the HTTP client

Each SDK also accepts a custom HTTP client (for proxy configuration, custom TLS, or connection pooling). Only one HTTP client is used per SDK client; setting it replaces the default. The custom HTTP client receives requests after all middleware has run.

## Built-in middleware

The SDKs ship a refusal-fallback middleware that automatically retries requests Claude Fable 5 declines on a fallback model. See [Detect and retry on a fallback model](/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback) for setup and per-language examples.
