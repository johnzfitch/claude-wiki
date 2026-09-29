---
title: "PHP SDK - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/php"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:40Z"
tags: ["api", "sdk"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fcli-sdks-libraries%2Fsdks%2Fphp)





SearchCtrlK

CLI, SDKs, and libraries

[Overview](cli-sdks-libraries-overview.md)

ant CLI

[Quickstart](cli-sdks-libraries-cli-quickstart.md)[Authentication options](cli-sdks-libraries-cli-authentication.md)[Using the CLI](cli-sdks-libraries-cli-using.md)[Scripting and automation](cli-sdks-libraries-cli-scripting.md)[Manage resources as code](cli-sdks-libraries-cli-apply.md)[Connect to a Managed Agents session](cli-sdks-libraries-cli-sessions-connect.md)

Client SDKs

[Middleware](cli-sdks-libraries-middleware.md)[Python](cli-sdks-libraries-sdks-python.md)[TypeScript](cli-sdks-libraries-sdks-typescript.md)[C#](cli-sdks-libraries-sdks-csharp.md)[Go](cli-sdks-libraries-sdks-go.md)[Java](cli-sdks-libraries-sdks-java.md)[PHP](cli-sdks-libraries-sdks-php.md)[Ruby](cli-sdks-libraries-sdks-ruby.md)

Libraries and integrations

[Apple Foundation Models](cli-sdks-libraries-libraries-apple-foundation-models.md)[OpenAI SDK compatibility](cli-sdks-libraries-libraries-openai-sdk.md)

[Console](usage-limits.md)

[CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)Client SDKs

# PHP SDK

Copy page



Install and configure the Anthropic PHP SDK with value objects and builder patterns

Copy page



The Anthropic PHP library provides convenient access to the Claude API from any PHP 8.1.0+ application.



The PHP SDK is currently in beta. APIs might change between versions.



For API feature documentation with code examples, see the [API reference](../Endpoints/overview.md). This page covers PHP-specific SDK features and configuration.

## Installation

The SDK uses [PSR-18](https://www.php-fig.org/psr/psr-18/) for HTTP and discovers any installed PSR-18 client automatically. [Guzzle](https://docs.guzzlephp.org/) is recommended because the SDK configures it for streaming with no additional setup:

```python
composer require "anthropic-ai/sdk" "guzzlehttp/guzzle:^7"
```



## Requirements

PHP 8.1.0 or higher.

## Usage

This library uses named parameters to specify optional arguments. Parameters with a default value must be set by name.

```python
$client = new Client();

$message = $client->messages->create(
  maxTokens: 1024,
  messages: [['role' => 'user', 'content' => 'Hello, Claude']],
  model: 'claude-opus-5-5',
);

$textBlock = array_find($message->content, static fn ($block): bool => $block->type === 'text');
echo $textBlock->text;
```



For authentication options including Workload Identity Federation, see [Authentication](manage-claude-authentication.md). If your API key is a [personal or service account key](manage-claude-authentication.md#key-types) with access to multiple workspaces, set the workspace ID in the `anthropic-workspace-id` request header; [Select a workspace](manage-claude-authentication.md#select-a-workspace) shows the per-request option for this SDK.

## Value objects

It is recommended to use the static `with` constructor `Base64ImageSource::with(data: "U3RhaW5sZXNzIHJvY2tz", ...)` and named parameters to initialize value objects.

However, builders are also provided `(new Base64ImageSource)->withData("U3RhaW5sZXNzIHJvY2tz")`.

## Streaming

The SDK provides support for streaming responses using Server-Sent Events (SSE).

```python
$client = new Client();

$stream = $client->messages->createStream(
  maxTokens: 1024,
  messages: [['role' => 'user', 'content' => 'Hello, Claude']],
  model: 'claude-opus-5-5',
);

foreach ($stream as $event) {
  echo $event->type . PHP_EOL;
}
```



Streaming requires an HTTP client that returns the response body incrementally. When Guzzle is the discovered PSR-18 client, the SDK configures it for streaming automatically. With a buffering client, the `foreach` loop yields every event at once when the response completes instead of incrementally; if you observe that symptom, install Guzzle or supply a streaming-capable PSR-18 client through the `streamingTransporter` request option:

```python
$client = new Anthropic\Client(
  requestOptions: Anthropic\RequestOptions::with(streamingTransporter: $myStreamingClient),
);
```



## Error handling

When the library is unable to connect to the API, or if the API returns a non-success status code (that is, a 4xx or 5xx response), a subclass of `Anthropic\Core\Exceptions\APIException` is thrown:

```python
<?php
// ...
use Anthropic\Core\Exceptions\APIConnectionException;
use Anthropic\Core\Exceptions\APIStatusException;
use Anthropic\Core\Exceptions\RateLimitException;
// ...
try {
  $message = $client->messages->create(
    maxTokens: 1024,
    messages: [['role' => 'user', 'content' => 'Hello, Claude']],
    model: 'claude-opus-5-5',
  );
} catch (APIConnectionException $e) {
  echo "The server could not be reached", PHP_EOL;
  echo $e->getPrevious()?->getMessage(), PHP_EOL;
} catch (RateLimitException $_) {
  echo "A 429 status code was received; we should back off a bit.", PHP_EOL;
} catch (APIStatusException $e) {
  echo "Another non-200-range status code was received", PHP_EOL;
  echo $e->getMessage();
}
```



Error codes are as follows:

| Cause            | Error Type                     |
|------------------|--------------------------------|
| HTTP 400         | `BadRequestException`          |
| HTTP 401         | `AuthenticationException`      |
| HTTP 403         | `PermissionDeniedException`    |
| HTTP 404         | `NotFoundException`            |
| HTTP 409         | `ConflictException`            |
| HTTP 422         | `UnprocessableEntityException` |
| HTTP 429         | `RateLimitException`           |
| HTTP \>= 500     | `InternalServerException`      |
| Other HTTP error | `APIStatusException`           |
| Timeout          | `APITimeoutException`          |
| Network error    | `APIConnectionException`       |

## Retries

Certain errors are automatically retried two times by default, with a short exponential backoff.

Connection errors (for example, because of a network connectivity problem), 408 Request Timeout, 409 Conflict, 429 Rate Limit, \>=500 Internal errors, and timeouts are all retried by default.

You can use the `maxRetries` option to configure or disable this:

```python
use Anthropic\RequestOptions;
// ...
// Configure the default for all requests:
$client = new Client(requestOptions: RequestOptions::with(maxRetries: 0));

// Or, configure per-request:
$result = $client->messages->create(
  maxTokens: 1024,
  messages: [['role' => 'user', 'content' => 'Hello, Claude']],
  model: 'claude-opus-5-5',
  requestOptions: RequestOptions::with(maxRetries: 5),
);
```



## Pagination

List methods in the Claude API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
$client = new Client();

$page = $client->beta->messages->batches->list(limit: 20);

// fetch items from the current page
foreach ($page->getItems() as $item) {
  echo $item->id, PHP_EOL;
}
// make additional network requests to fetch items from all pages, including and after the current page
foreach ($page->pagingEachItem() as $item) {
  echo $item->id, PHP_EOL;
}
```



## Advanced usage

### Undocumented properties

You can send undocumented parameters to any endpoint, and read undocumented response properties, as follows:



The `extra*` parameters of the same name override the documented parameters.

```python
<?php
// ...
use Anthropic\RequestOptions;
// ...
$message = $client->messages->create(
  maxTokens: 1024,
  messages: [['role' => 'user', 'content' => 'Hello, Claude']],
  model: 'claude-opus-5-5',
  requestOptions: RequestOptions::with(
    extraQueryParams: ['my_query_parameter' => 'value'],
    extraBodyParams: ['my_body_parameter' => 'value'],
    extraHeaders: ['my-header' => 'value'],
  ),
);
```



### Undocumented request parameters

If you want to explicitly send an extra parameter, you can do so with the `extraQueryParams`, `extraBodyParams`, and `extraHeaders` options under `RequestOptions::with()` when making a request, as seen in the preceding example.

### Undocumented endpoints

To make requests to undocumented endpoints while retaining the benefit of authentication, retries, and other client features, you can make requests using `client->request`, as follows:

```python
$client = new Client();

$response = $client->request(
  method: "post",
  path: '/undocumented/endpoint',
  query: ['dog' => 'woof'],
  headers: ['useful-header' => 'interesting-value'],
  body: ['hello' => 'world']
);
```



## Platform integrations



For detailed platform setup guides with code examples, see:

- [Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md)
- [Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)
- [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)
- [Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)
- [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

The PHP SDK supports the following platforms:

- **Agent Platform:** `Anthropic\Vertex\Client`. Use `::fromEnvironment()`.
- **Bedrock:** `Anthropic\Bedrock\MantleClient`. Use `new MantleClient(awsRegion: ...)`.
- **Bedrock (legacy):** `Anthropic\Bedrock\Client`. Use `::fromEnvironment()` or `::withCredentials()`.
- **Claude Platform on AWS:** `Anthropic\Aws\Client` (requires `aws/aws-sdk-php` as a soft dependency). Use `new Anthropic\Aws\Client(workspaceId: ...)` or set `ANTHROPIC_AWS_WORKSPACE_ID`. Available in beta.
- **Foundry:** `Anthropic\Foundry\Client`. Use `::withCredentials()`.

Use `MantleClient` for new projects; `Anthropic\Bedrock\Client` remains for existing applications using the Bedrock `InvokeModel` API.

## Semantic versioning

This package follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions. As the library is in initial development and has a major version of `0`, APIs might change at any time.

This package considers improvements to the (non-runtime) PHPDoc type definitions to be non-breaking changes.

## Additional resources

- [GitHub repository](https://github.com/anthropics/anthropic-sdk-php)
- [Packagist](https://packagist.org/packages/anthropic-ai/sdk)
- [API reference](../Endpoints/overview.md)
- [Streaming Messages](../Guides/build-with-claude-streaming.md)
