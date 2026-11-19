---
title: "SDK middleware - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/middleware"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:36:38Z"
tags: ["api", "cli", "sdk"]
---

# SDK middleware

Copy page



Intercept and modify the SDK’s requests and responses.

Copy page



SDK middleware

[Models](#feature-availability)  
- All models

[APIs](#feature-availability)  
- Messages API
- Managed Agents[\* Beta](#availability-beta-on-claude-api)

[Cloud platforms](#feature-availability)  
- All platforms

The Anthropic SDK provides a middleware (or interceptor) hook that runs your code before the SDK sends a request and after it receives the response. Use middleware for cross-cutting concerns such as logging, custom retries, request annotation, and retrying a declined request on a [fallback model](#built-in-middleware).

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

To register more than one middleware, pass them all, as in `middleware=[first, second]`.

## Replacing the HTTP client

The SDK also accepts a custom HTTP client (for proxy configuration, custom TLS, or connection pooling). Only one HTTP client is used for each SDK client; setting it replaces the default. The custom HTTP client receives requests after all middleware has run.

## Built-in middleware

The SDK ships a refusal-fallback middleware that automatically retries a request Claude declines (`stop_reason: "refusal"`) on a fallback model. [Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md) lists the models whose safety classifiers can decline requests, and [Detect and retry on a fallback model](../Guides/build-with-claude-refusals-and-fallback.md#client-side-fallback) covers setup and per-language examples.

## Availability

SDK middleware

Cloud platform

Cloud platform: Claude API

Claude API

APIs  
- Messages API
- Managed Agents Beta

Models  
- All models

Amazon Bedrock

API  
- Messages API

Models  
- All models

Amazon Bedrock (bedrock-runtime)

API  
- Messages API

Models  
- All models

Claude Platform on AWS

APIs  
- Messages API
- Managed Agents Beta

Models  
- All models

Claude Models on Google Cloud (Anthropic managed)

API  
- Messages API

Models  
- All models

Claude Models on Google Cloud (Google managed)

API  
- Messages API

Models  
- All models

Microsoft Foundry

API  
- Messages API

Models  
- All models
