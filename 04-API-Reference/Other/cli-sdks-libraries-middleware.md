---
title: "SDK middleware - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/middleware"
category: "04-API-Reference/Other"
fetched_at: "2026-11-05T06:37:08Z"
tags: ["api", "cli", "sdk"]
---

# SDK middleware

Copy page



Intercept and modify the SDK’s requests and responses.

Copy page



SDK middleware

[APIs](#feature-availability)  
Messages APIAvailableManaged AgentsAvailable

[Cloud platforms](#availability-feature-support)  
All platforms

The Claude SDK provides a middleware (or interceptor) hook that lets you run code before a request is sent and after the response is received. Use middleware for cross-cutting concerns such as logging, custom retries, request annotation, and refusal fallback handling.

Each middleware can inspect or replace the request before calling `next()`, and the response after `next()` returns.

## Registering middleware

Each middleware is a function that receives the outgoing request and the next handler. Call `call_next(request)` to forward the request to the rest of the chain (or directly to the SDK core if this is the last middleware), and return its response. Anything before that call runs on the way out; anything after runs on the way back.

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

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

When you register multiple middleware, they apply in the order given: the first middleware’s “before” code runs first, and its “after” code runs last. Middleware registered on the client runs before middleware passed as a per-request option.

In the Go SDK, repeated `option.WithMiddleware` calls concatenate (client first, then method). In the other SDKs, pass an array; later entries wrap inner.

## Replacing the HTTP client

The SDK also accepts a custom HTTP client (for proxy configuration, custom TLS, or connection pooling). Only one HTTP client is used for each SDK client; setting it replaces the default. The custom HTTP client receives requests after all middleware has run.

## Built-in middleware

The SDK ships a refusal-fallback middleware that automatically retries a request Claude declines (`stop_reason: "refusal"`) on a fallback model. [Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md) lists the models whose safety classifiers can decline requests, and [Detect and retry on a fallback model](../Guides/build-with-claude-refusals-and-fallback.md#client-side-fallback) covers setup and per-language examples.

## Availability

SDK middleware is available or in beta, depending on the API.

### API support

[Messages API](../Guides/build-with-claude-working-with-messages.md)

StatusAvailable

Cloud platforms

- All supported platforms

[Managed Agents](managed-agents-overview.md)

Usage

Runs on your SDK client’s calls to the Managed Agents API. It does not see the model calls the agent makes inside its loop.

StatusBeta

Cloud platforms

- Claude API
- [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)
