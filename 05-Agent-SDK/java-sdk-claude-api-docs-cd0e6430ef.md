---
category: "05-Agent-SDK"
fetched_at: "2026-02-07T10:05:11Z"
source_url: "https://platform.claude.com/docs/en/api/sdks/java"
title: "Java SDK - Claude API Docs"
---

Client SDKs

# Java SDK

Copy page

Install and configure the Anthropic Java SDK with builder patterns and async support

Copy page

The Anthropic Java SDK provides convenient access to the Anthropic REST API from applications written in Java. It uses the builder pattern for creating requests and supports both synchronous and asynchronous operations.

For API feature documentation with code examples, see the [API reference](/docs/en/api/overview). This page covers Java-specific SDK features and configuration.

## 

Installation

Gradle

Gradle

Maven

Maven

``` shiki
implementation("com.anthropic:anthropic-java:2.11.1")
```

## 

Requirements

This library requires Java 8 or later.

## 

Quick start

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

// Configures using the `ANTHROPIC_API_KEY` environment variable
AnthropicClient client = AnthropicOkHttpClient.fromEnv();

MessageCreateParams params = MessageCreateParams.builder()
    .maxTokens(1024L)
    .addUserMessage("Hello, Claude")
    .model(Model.CLAUDE_OPUS_4_6)
    .build();
Message message = client.messages().create(params);
```

## 

Client configuration

### 

API key setup

Configure the client using system properties or environment variables:

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

// Configures using the `anthropic.apiKey`, `anthropic.authToken` and `anthropic.baseUrl` system properties
// Or configures using the `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` and `ANTHROPIC_BASE_URL` environment variables
AnthropicClient client = AnthropicOkHttpClient.fromEnv();
```

Or configure manually:

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder()
    .apiKey("my-anthropic-api-key")
    .build();
```

Or use a combination of both approaches:

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder()
    // Configures using system properties or environment variables
    .fromEnv()
    .apiKey("my-anthropic-api-key")
    .build();
```

### 

Configuration options

| Setter | System property | Environment variable | Required | Default value |
|----|----|----|----|----|
| `apiKey` | `anthropic.apiKey` | `ANTHROPIC_API_KEY` | false | \- |
| `authToken` | `anthropic.authToken` | `ANTHROPIC_AUTH_TOKEN` | false | \- |
| `baseUrl` | `anthropic.baseUrl` | `ANTHROPIC_BASE_URL` | true | `"https://api.anthropic.com"` |

System properties take precedence over environment variables.

Don't create more than one client in the same application. Each client has a connection pool and thread pools, which are more efficient to share between requests.

### 

Modifying configuration

To temporarily use a modified client configuration while reusing the same connection and thread pools, call `withOptions()` on any client or service:

``` shiki
import com.anthropic.client.AnthropicClient;

AnthropicClient clientWithOptions = client.withOptions(optionsBuilder -> {
    optionsBuilder.baseUrl("https://example.com");
    optionsBuilder.maxRetries(42);
});
```

The `withOptions()` method does not affect the original client or service.

## 

Async usage

The default client is synchronous. To switch to asynchronous execution, call the `async()` method:

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import java.util.concurrent.CompletableFuture;

AnthropicClient client = AnthropicOkHttpClient.fromEnv();

MessageCreateParams params = MessageCreateParams.builder()
    .maxTokens(1024L)
    .addUserMessage("Hello, Claude")
    .model(Model.CLAUDE_OPUS_4_6)
    .build();
CompletableFuture<Message> message = client.async().messages().create(params);
```

Or create an asynchronous client from the beginning:

``` shiki
import com.anthropic.client.AnthropicClientAsync;
import com.anthropic.client.okhttp.AnthropicOkHttpClientAsync;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import java.util.concurrent.CompletableFuture;

AnthropicClientAsync client = AnthropicOkHttpClientAsync.fromEnv();

MessageCreateParams params = MessageCreateParams.builder()
    .maxTokens(1024L)
    .addUserMessage("Hello, Claude")
    .model(Model.CLAUDE_OPUS_4_6)
    .build();
CompletableFuture<Message> message = client.messages().create(params);
```

The asynchronous client supports the same options as the synchronous one, except most methods return `CompletableFuture`s.

## 

Streaming

The SDK defines methods that return response "chunk" streams, where each chunk can be individually processed as soon as it arrives instead of waiting on the full response.

### 

Synchronous streaming

These streaming methods return `StreamResponse` for synchronous clients:

``` shiki
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.messages.RawMessageStreamEvent;

try (StreamResponse<RawMessageStreamEvent> streamResponse = client.messages().createStreaming(params)) {
    streamResponse.stream().forEach(chunk -> {
        System.out.println(chunk);
    });
    System.out.println("No more chunks!");
}
```

### 

Asynchronous streaming

For asynchronous clients, the method returns `AsyncStreamResponse`:

``` shiki
import com.anthropic.core.http.AsyncStreamResponse;
import com.anthropic.models.messages.RawMessageStreamEvent;
import java.util.Optional;

client.async().messages().createStreaming(params).subscribe(chunk -> {
    System.out.println(chunk);
});

// If you need to handle errors or completion of the stream
client.async().messages().createStreaming(params).subscribe(new AsyncStreamResponse.Handler<>() {
    @Override
    public void onNext(RawMessageStreamEvent chunk) {
        System.out.println(chunk);
    }

    @Override
    public void onComplete(Optional<Throwable> error) {
        if (error.isPresent()) {
            System.out.println("Something went wrong!");
            throw new RuntimeException(error.get());
        } else {
            System.out.println("No more chunks!");
        }
    }
});

// Or use futures
client.async().messages().createStreaming(params)
    .subscribe(chunk -> {
        System.out.println(chunk);
    })
    .onCompleteFuture()
    .whenComplete((unused, error) -> {
        if (error != null) {
            System.out.println("Something went wrong!");
            throw new RuntimeException(error);
        } else {
            System.out.println("No more chunks!");
        }
    });
```

Async streaming uses a dedicated per-client cached thread pool `Executor` to stream without blocking the current thread. To use a different `Executor`:

``` shiki
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

Executor executor = Executors.newFixedThreadPool(4);
client.async().messages().createStreaming(params).subscribe(
    chunk -> System.out.println(chunk), executor
);
```

Or configure the client globally using the `streamHandlerExecutor` method:

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import java.util.concurrent.Executors;

AnthropicClient client = AnthropicOkHttpClient.builder()
    .fromEnv()
    .streamHandlerExecutor(Executors.newFixedThreadPool(4))
    .build();
```

### 

Streaming with message accumulator

A `MessageAccumulator` can record the stream of events in the response as they are processed and accumulate a `Message` object similar to what would have been returned by the non-streaming API.

For a synchronous response, add a `Stream.peek()` call to the stream pipeline to accumulate each event:

``` shiki
import com.anthropic.core.http.StreamResponse;
import com.anthropic.helpers.MessageAccumulator;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.RawMessageStreamEvent;

MessageAccumulator messageAccumulator = MessageAccumulator.create();

try (StreamResponse<RawMessageStreamEvent> streamResponse =
         client.messages().createStreaming(createParams)) {
    streamResponse.stream()
            .peek(messageAccumulator::accumulate)
            .flatMap(event -> event.contentBlockDelta().stream())
            .flatMap(deltaEvent -> deltaEvent.delta().text().stream())
            .forEach(textDelta -> System.out.print(textDelta.text()));
}

Message message = messageAccumulator.message();
```

For an asynchronous response, add the `MessageAccumulator` to the `subscribe()` call:

``` shiki
import com.anthropic.helpers.MessageAccumulator;
import com.anthropic.models.messages.Message;

MessageAccumulator messageAccumulator = MessageAccumulator.create();

client.messages()
        .createStreaming(createParams)
        .subscribe(event -> messageAccumulator.accumulate(event).contentBlockDelta().stream()
                .flatMap(deltaEvent -> deltaEvent.delta().text().stream())
                .forEach(textDelta -> System.out.print(textDelta.text())))
        .onCompleteFuture()
        .join();

Message message = messageAccumulator.message();
```

A `BetaMessageAccumulator` is also available for the accumulation of a `BetaMessage` object. It is used in the same manner as the `MessageAccumulator`.

## 

Structured outputs

[Structured Outputs](/docs/en/build-with-claude/structured-outputs) (beta) ensures that the model generates responses that adhere to a supplied JSON schema.

A JSON schema can be derived automatically from the structure of an arbitrary Java class. The JSON content from the response will then be converted automatically to an instance of that class.

### 

Defining classes

Java classes can contain fields declared to be instances of other classes and can use collections:

``` shiki
class Person {
    public String name;
    public int birthYear;
}

class Book {
    public String title;
    public Person author;
    public int publicationYear;
}

class BookList {
    public List<Book> books;
}
```

### 

Using structured outputs

Pass the top-level class to `outputConfig(Class<T>)` when building the parameters and then access an instance from the generated message content in the response:

``` shiki
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.StructuredMessageCreateParams;
import com.anthropic.models.messages.Model;

StructuredMessageCreateParams<BookList> createParams = MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_4_6)
        .maxTokens(2048)
        .outputConfig(BookList.class)
        .addUserMessage("List some famous late twentieth century novels.")
        .build();

client.beta().messages().create(createParams).content().stream()
        .flatMap(contentBlock -> contentBlock.text().stream())
        .flatMap(textBlock -> textBlock.text().books.stream())
        .forEach(book -> System.out.println(book.title + " by " + book.author.name));
```

### 

Optional fields

If a field is optional and does not require a defined value, you can represent this using `java.util.Optional`. It is up to the AI model to decide whether to provide a value for that field or leave it empty.

``` shiki
import java.util.Optional;

class Book {
    public String title;
    public Person author;
    public int publicationYear;
    public Optional<String> isbn;
}
```

Generic type information for fields is retained in the class's metadata, but generic type erasure applies in other scopes. While a JSON schema can be derived from a `BookList.books` field with type `List<Book>`, a valid JSON schema cannot be derived from a local variable of that same type.

If an error occurs while converting a JSON response to a Java class instance, the error message will include the JSON response to assist in diagnosis. If your JSON response may contain sensitive information, avoid logging it directly, or ensure that you redact any sensitive details from the error message.

### 

Local JSON schema validation

Structured Outputs supports a [subset of the JSON Schema language](/docs/en/build-with-claude/structured-outputs#json-schema-limitations). Schemas are generated automatically from classes to align with this subset. The method `outputConfig(Class<T>)` performs a validation check on the schema derived from the specified class.

Key points:

- **Local validation**: The validation process occurs locally, meaning no requests are sent to the remote AI model.
- **Remote validation**: The remote AI model will conduct its own validation upon receiving the JSON schema in the request.
- **Version compatibility**: There may be instances where local validation fails while remote validation succeeds if the SDK version is outdated.
- **Disabling local validation**: If you encounter compatibility issues, you can disable local validation by passing `JsonSchemaLocalValidation.NO`:

``` shiki
import com.anthropic.core.JsonSchemaLocalValidation;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.StructuredMessageCreateParams;
import com.anthropic.models.messages.Model;

StructuredMessageCreateParams<BookList> createParams = MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_4_6)
        .maxTokens(2048)
        .outputConfig(BookList.class, JsonSchemaLocalValidation.NO)
        .addUserMessage("List some famous late twentieth century novels.")
        .build();
```

### 

Structured outputs with streaming

Structured outputs can also be used with streaming. As responses are returned in "stream events", the full response must first be accumulated to concatenate the JSON strings that can then be converted into instances of the arbitrary Java class.

Use the `BetaMessageAccumulator` as described in [Streaming with message accumulator](#streaming-with-message-accumulator) to accumulate the JSON strings. Once accumulated, use `BetaMessageAccumulator.message(Class<T>)` to convert the accumulated `BetaMessage` into a `StructuredMessage`, which can then automatically deserialize the JSON strings into instances of your Java class.

### 

Defining JSON schema properties

When a JSON schema is derived from your Java classes, all properties represented by `public` fields or `public` getter methods are included in the schema by default. Non-`public` fields and getter methods are not included by default.

You can exclude `public`, or include non-`public` fields or getter methods, by using the `@JsonIgnore` or `@JsonProperty` annotations respectively.

If you do not want to define `public` fields, you can define `private` fields and corresponding `public` getter methods. For example, a `private` field `myValue` with a `public` getter method `getMyValue()` will result in a `"myValue"` property being included in the JSON schema.

Each of your classes must define at least one property to be included in the JSON schema. A validation error will occur if any class contains no fields or getter methods from which schema properties can be derived.

### 

Annotating classes and JSON schemas

You can use annotations to add further information to the JSON schema derived from your Java classes. The SDK supports the use of Jackson Databind annotations:

``` shiki
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;

class Person {
    @JsonPropertyDescription("The first name and surname of the person")
    public String name;
    public int birthYear;
    @JsonPropertyDescription("The year the person died, or 'present' if the person is living.")
    public String deathYear;
}

@JsonClassDescription("The details of one published book")
class Book {
    public String title;
    public Person author;
    @JsonPropertyDescription("The year in which the book was first published.")
    public int publicationYear;
    @JsonIgnore public String genre;
}

class BookList {
    public List<Book> books;
}
```

Annotation summary:

- `@JsonClassDescription` - Add a detailed description to a class.
- `@JsonPropertyDescription` - Add a detailed description to a field or getter method.
- `@JsonIgnore` - Exclude a `public` field or getter method from the generated JSON schema.
- `@JsonProperty` - Include a non-`public` field or getter method in the generated JSON schema.

If you use `@JsonProperty(required = false)`, the `false` value will be ignored. Anthropic JSON schemas must mark all properties as required.

You can also use OpenAPI Swagger 2 `@Schema` and `@ArraySchema` annotations for type-specific constraints:

``` shiki
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.media.ArraySchema;

class Article {
    @ArraySchema(minItems = 1)
    public List<String> authors;

    public String title;

    @Schema(format = "date")
    public String publicationDate;

    @Schema(minimum = "1")
    public int pageCount;
}
```

If you use both Jackson and Swagger annotations to set the same schema field, the Jackson annotation will take precedence.

## 

Tool use

[Tool Use](/docs/en/agents-and-tools/tool-use/overview) lets you integrate external tools and functions directly into the AI model's responses. You define JSON schemas for tools, and the model uses the schemas to decide when and how to use these tools.

The SDK can derive a tool and its parameters automatically from the structure of an arbitrary Java class: the class's name (converted to snake case) provides the tool name, and the class's fields define the tool's parameters.

### 

Defining tools with annotations

``` shiki
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;

enum Unit {
  CELSIUS, FAHRENHEIT;

  public String toString() {
    switch (this) {
      case CELSIUS: return "C";
      case FAHRENHEIT: default: return "F";
    }
  }

  public double fromKelvin(double temperatureK) {
    switch (this) {
      case CELSIUS: return temperatureK - 273.15;
      case FAHRENHEIT: default: return (temperatureK - 273.15) * 1.8 + 32.0;
    }
  }
}

@JsonClassDescription("Get the weather in a given location")
static class GetWeather {
  @JsonPropertyDescription("The city and state, e.g. San Francisco, CA")
  public String location;

  @JsonPropertyDescription("The unit of temperature")
  public Unit unit;

  public Weather execute() {
    double temperatureK;
    switch (location) {
      case "San Francisco, CA": temperatureK = 300.0; break;
      case "New York, NY": temperatureK = 310.0; break;
      case "Dallas, TX": temperatureK = 305.0; break;
      default: temperatureK = 295; break;
    }
    return new Weather(String.format("%.0f%s", unit.fromKelvin(temperatureK), unit));
  }
}

static class Weather {
  public String temperature;

  public Weather(String temperature) {
    this.temperature = temperature;
  }
}
```

### 

Calling tools

When your tool classes are defined, add them to the message parameters using `MessageCreateParams.addTool(Class<T>)` and then call them if requested to do so in the AI model's response. `BetaToolUseBlock.input(Class<T>)` can be used to parse a tool's parameters in JSON form to an instance of your tool-defining class.

After invoking the tool, use `BetaToolResultBlockParam.Builder.contentAsJson(Object)` to pass the tool's result back to the AI model:

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.*;
import com.anthropic.models.messages.Model;
import java.util.List;

AnthropicClient client = AnthropicOkHttpClient.fromEnv();

MessageCreateParams.Builder createParamsBuilder = MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_4_6)
        .maxTokens(2048)
        .addTool(GetWeather.class)
        .addUserMessage("What's the temperature in New York?");

client.beta().messages().create(createParamsBuilder.build()).content().stream()
        .flatMap(contentBlock -> contentBlock.toolUse().stream())
        .forEach(toolUseBlock -> createParamsBuilder
              // Add a message indicating that the tool use was requested.
              .addAssistantMessageOfBetaContentBlockParams(
                      List.of(BetaContentBlockParam.ofToolUse(BetaToolUseBlockParam.builder()
                              .name(toolUseBlock.name())
                              .id(toolUseBlock.id())
                              .input(toolUseBlock._input())
                              .build())))
              // Add a message with the result of the requested tool use.
              .addUserMessageOfBetaContentBlockParams(
                      List.of(BetaContentBlockParam.ofToolResult(BetaToolResultBlockParam.builder()
                              .toolUseId(toolUseBlock.id())
                              .contentAsJson(callTool(toolUseBlock))
                              .build()))));

client.beta().messages().create(createParamsBuilder.build()).content().stream()
        .flatMap(contentBlock -> contentBlock.text().stream())
        .forEach(textBlock -> System.out.println(textBlock.text()));

private static Object callTool(BetaToolUseBlock toolUseBlock) {
  if (!"get_weather".equals(toolUseBlock.name())) {
    throw new IllegalArgumentException("Unknown tool: " + toolUseBlock.name());
  }

  GetWeather tool = toolUseBlock.input(GetWeather.class);
  return tool != null ? tool.execute() : new Weather("unknown");
}
```

### 

Tool name conversion

Tool names are derived from the camel case tool class names (e.g., `GetWeather`) and converted to snake case (e.g., `get_weather`). Word boundaries begin where the current character is not the first character, is upper-case, and either the preceding character is lower-case, or the following character is lower-case. For example, `MyJSONParser` becomes `my_json_parser` and `ParseJSON` becomes `parse_json`. This conversion can be overridden using the `@JsonTypeName` annotation.

### 

Local tool JSON schema validation

Like for structured outputs, you can perform local validation to check that the JSON schema derived from your tool class respects Anthropic's restrictions. Local validation is enabled by default, but it can be disabled:

``` shiki
MessageCreateParams.Builder createParamsBuilder = MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_4_6)
        .maxTokens(2048)
        .addTool(GetWeather.class, JsonSchemaLocalValidation.NO)
        .addUserMessage("What's the temperature in New York?");
```

### 

Annotating tool classes

You can use annotations to add further information about tools to the JSON schemas:

- `@JsonClassDescription` - Add a description to a tool class detailing when and how to use that tool.
- `@JsonTypeName` - Set the tool name to something other than the simple name of the class converted to snake case.
- `@JsonPropertyDescription` - Add a detailed description to a tool parameter.
- `@JsonIgnore` - Exclude a `public` field or getter method from the generated JSON schema for a tool's parameters.
- `@JsonProperty` - Include a non-`public` field or getter method in the generated JSON schema for a tool's parameters.

## 

Message batches

The SDK provides support for the [Message Batches API](/docs/en/build-with-claude/batch-processing) under the `client.messages().batches()` namespace. See the [pagination section](#pagination) for how to iterate through batch results.

## 

File uploads

The SDK defines methods that accept files through the `MultipartField` interface:

``` shiki
import com.anthropic.core.MultipartField;
import com.anthropic.models.beta.files.FileMetadata;
import com.anthropic.models.beta.files.FileUploadParams;
import com.anthropic.models.beta.AnthropicBeta;
import java.io.InputStream;
import java.nio.file.Paths;

FileUploadParams params = FileUploadParams.builder()
    .file(MultipartField.<InputStream>builder()
        .value(Files.newInputStream(Paths.get("/path/to/file.pdf")))
        .contentType("application/pdf")
        .build())
    .addBeta(AnthropicBeta.FILES_API_2025_04_14)
    .build();
FileMetadata fileMetadata = client.beta().files().upload(params);
```

Or from an `InputStream`:

``` shiki
import com.anthropic.core.MultipartField;
import com.anthropic.models.beta.files.FileMetadata;
import com.anthropic.models.beta.files.FileUploadParams;
import com.anthropic.models.beta.AnthropicBeta;
import java.io.InputStream;
import java.net.URL;

FileUploadParams params = FileUploadParams.builder()
    .file(MultipartField.<InputStream>builder()
        .value(new URL("https://example.com/path/to/file").openStream())
        .filename("document.pdf")
        .contentType("application/pdf")
        .build())
    .addBeta(AnthropicBeta.FILES_API_2025_04_14)
    .build();
FileMetadata fileMetadata = client.beta().files().upload(params);
```

Or a `byte[]` array:

``` shiki
import com.anthropic.core.MultipartField;
import com.anthropic.models.beta.files.FileMetadata;
import com.anthropic.models.beta.files.FileUploadParams;
import com.anthropic.models.beta.AnthropicBeta;

FileUploadParams params = FileUploadParams.builder()
    .file(MultipartField.<byte[]>builder()
        .value("content".getBytes())
        .filename("document.txt")
        .contentType("text/plain")
        .build())
    .addBeta(AnthropicBeta.FILES_API_2025_04_14)
    .build();
FileMetadata fileMetadata = client.beta().files().upload(params);
```

### 

Binary responses

The SDK defines methods that return binary responses for API responses that aren't necessarily parsed as JSON:

``` shiki
import com.anthropic.core.http.HttpResponse;
import com.anthropic.models.beta.files.FileDownloadParams;

HttpResponse response = client.beta().files().download("file_id");
```

To save the response content to a file:

``` shiki
import com.anthropic.core.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

try (HttpResponse response = client.beta().files().download(params)) {
    Files.copy(
        response.body(),
        Paths.get(path),
        StandardCopyOption.REPLACE_EXISTING
    );
} catch (Exception e) {
    System.out.println("Something went wrong!");
    throw new RuntimeException(e);
}
```

Or transfer the response content to any `OutputStream`:

``` shiki
import com.anthropic.core.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

try (HttpResponse response = client.beta().files().download(params)) {
    response.body().transferTo(Files.newOutputStream(Paths.get(path)));
} catch (Exception e) {
    System.out.println("Something went wrong!");
    throw new RuntimeException(e);
}
```

## 

Error handling

The SDK throws custom unchecked exception types:

- `AnthropicServiceException` - Base class for HTTP errors.
- `AnthropicIoException` - I/O networking errors.
- `AnthropicRetryableException` - Generic error indicating a failure that could be retried.
- `AnthropicInvalidDataException` - Failure to interpret successfully parsed data (e.g., when accessing a property that's supposed to be required, but the API unexpectedly omitted it).
- `AnthropicException` - Base class for all exceptions.

### 

Status code mapping

| Status | Exception                       |
|--------|---------------------------------|
| 400    | `BadRequestException`           |
| 401    | `UnauthorizedException`         |
| 403    | `PermissionDeniedException`     |
| 404    | `NotFoundException`             |
| 422    | `UnprocessableEntityException`  |
| 429    | `RateLimitException`            |
| 5xx    | `InternalServerException`       |
| others | `UnexpectedStatusCodeException` |

`SseException` is thrown for errors encountered during SSE streaming after a successful initial HTTP response.

``` shiki
import com.anthropic.errors.*;

try {
    Message message = client.messages().create(params);
} catch (RateLimitException e) {
    System.out.println("Rate limited, retry after: " + e.headers());
} catch (UnauthorizedException e) {
    System.out.println("Invalid API key");
} catch (AnthropicServiceException e) {
    System.out.println("API error: " + e.statusCode());
} catch (AnthropicIoException e) {
    System.out.println("Network error: " + e.getMessage());
}
```

## 

Request IDs

When using raw responses, you can access the `request-id` response header using the `requestId()` method:

``` shiki
import com.anthropic.core.http.HttpResponseFor;
import com.anthropic.models.messages.Message;
import java.util.Optional;

HttpResponseFor<Message> message = client.messages().withRawResponse().create(params);
Optional<String> requestId = message.requestId();
```

This can be used to quickly log failing requests and report them back to Anthropic. For more information on debugging requests, see the [API error documentation](/docs/en/api/errors#request-id).

## 

Retries

The SDK automatically retries 2 times by default, with a short exponential backoff between requests.

Only the following error types are retried:

- Connection errors (for example, due to a network connectivity problem)
- 408 Request Timeout
- 409 Conflict
- 429 Rate Limit
- 5xx Internal

The API may also explicitly instruct the SDK to retry or not retry a request.

To set a custom number of retries, configure the client using the `maxRetries` method:

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder()
    .fromEnv()
    .maxRetries(4)
    .build();
```

## 

Timeouts

Requests time out after 10 minutes by default.

However, for methods that accept `maxTokens`, if you specify a large `maxTokens` value and are not streaming, then the default timeout will be calculated dynamically using this formula:

``` shiki
Duration.ofSeconds(
    Math.min(
        60 * 60, // 1 hour max
        Math.max(
            10 * 60, // 10 minute minimum
            60 * 60 * maxTokens / 128_000
        )
    )
)
```

This results in a timeout of up to 60 minutes, scaled by the `maxTokens` parameter, unless overridden.

To set a custom timeout per-request:

``` shiki
import com.anthropic.models.messages.Message;

Message message = client.messages().create(
  params, RequestOptions.builder().timeout(Duration.ofSeconds(30)).build()
);
```

Or configure the default for all method calls at the client level:

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import java.time.Duration;

AnthropicClient client = AnthropicOkHttpClient.builder()
    .fromEnv()
    .timeout(Duration.ofSeconds(30))
    .build();
```

## 

Long requests

We highly encourage you to use [streaming](#streaming) for longer running requests.

We do not recommend setting a large `maxTokens` value without using streaming. Some networks may drop idle connections after a certain period of time, which can cause the request to fail or [timeout](#timeouts) without receiving a response from Anthropic. The SDK periodically pings the API to keep the connection alive and reduce the impact of these networks.

The SDK throws an error if a non-streaming request is expected to take longer than 10 minutes. Using a [streaming method](#streaming) or [overriding the timeout](#timeouts) at the client or request level disables the error.

## 

Pagination

The SDK provides convenient ways to access paginated results either one page at a time or item-by-item across all pages.

### 

Auto-pagination

To iterate through all results across all pages, use the `autoPager()` method, which automatically fetches more pages as needed.

``` shiki
import com.anthropic.models.messages.batches.BatchListPage;
import com.anthropic.models.messages.batches.MessageBatch;

BatchListPage page = client.messages().batches().list();

// Process as an Iterable
for (MessageBatch batch : page.autoPager()) {
    System.out.println(batch);
}

// Process as a Stream
page.autoPager()
    .stream()
    .limit(50)
    .forEach(batch -> System.out.println(batch));
```

When using the asynchronous client, the method returns an `AsyncStreamResponse`:

``` shiki
import com.anthropic.core.http.AsyncStreamResponse;
import com.anthropic.models.messages.batches.BatchListPageAsync;
import com.anthropic.models.messages.batches.MessageBatch;
import java.util.Optional;
import java.util.concurrent.CompletableFuture;

CompletableFuture<BatchListPageAsync> pageFuture = client.async().messages().batches().list();

pageFuture.thenAccept(page -> page.autoPager().subscribe(batch -> {
    System.out.println(batch);
}));
```

### 

Manual pagination

To access individual page items and manually request the next page:

``` shiki
import com.anthropic.models.messages.batches.BatchListPage;
import com.anthropic.models.messages.batches.MessageBatch;

BatchListPage page = client.messages().batches().list();
while (true) {
    for (MessageBatch batch : page.items()) {
        System.out.println(batch);
    }

    if (!page.hasNextPage()) {
        break;
    }

    page = page.nextPage();
}
```

## 

Type system

### 

Immutability and builders

Each class in the SDK has an associated builder for constructing it. Each class is immutable once constructed. If the class has an associated builder, then it has a `toBuilder()` method, which can be used to convert it back to a builder for making a modified copy.

``` shiki
MessageCreateParams params = MessageCreateParams.builder()
    .maxTokens(1024L)
    .addUserMessage("Hello, Claude")
    .model(Model.CLAUDE_OPUS_4_6)
    .build();

// Create a modified copy using toBuilder()
MessageCreateParams modified = params.toBuilder()
    .maxTokens(2048L)
    .build();
```

Because each class is immutable, builder modification will never affect already built class instances.

### 

Requests and responses

To send a request to the Claude API, build an instance of some `Params` class and pass it to the corresponding client method. When the response is received, it will be deserialized into an instance of a Java class.

For example, `client.messages().create(...)` should be called with an instance of `MessageCreateParams`, and it will return an instance of `Message`.

### 

Undocumented parameters

To set undocumented parameters, call the `putAdditionalHeader`, `putAdditionalQueryParam`, or `putAdditionalBodyProperty` methods on any `Params` class:

``` shiki
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.MessageCreateParams;

MessageCreateParams params = MessageCreateParams.builder()
    .putAdditionalHeader("Secret-Header", "42")
    .putAdditionalQueryParam("secret_query_param", "42")
    .putAdditionalBodyProperty("secretProperty", JsonValue.from("42"))
    .build();
```

The values passed to these methods overwrite values passed to earlier methods. For security reasons, ensure these methods are only used with trusted input data.

To set undocumented parameters on nested headers, query params, or body classes:

``` shiki
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Metadata;

MessageCreateParams params = MessageCreateParams.builder()
    .metadata(Metadata.builder()
        .putAdditionalProperty("secretProperty", JsonValue.from("42"))
        .build())
    .build();
```

To set a documented parameter or property to an undocumented or not yet supported value, pass a `JsonValue` object to its setter:

``` shiki
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

MessageCreateParams params = MessageCreateParams.builder()
    .maxTokens(JsonValue.from(3.14))
    .addUserMessage("Hello, Claude")
    .model(Model.CLAUDE_OPUS_4_6)
    .build();
```

### 

JsonValue creation

The most straightforward way to create a `JsonValue` is using its `from(...)` method:

``` shiki
import com.anthropic.core.JsonValue;
import java.util.List;
import java.util.Map;

// Create primitive JSON values
JsonValue nullValue = JsonValue.from(null);
JsonValue booleanValue = JsonValue.from(true);
JsonValue numberValue = JsonValue.from(42);
JsonValue stringValue = JsonValue.from("Hello World!");

// Create a JSON array value equivalent to `["Hello", "World"]`
JsonValue arrayValue = JsonValue.from(List.of(
  "Hello", "World"
));

// Create a JSON object value equivalent to `{ "a": 1, "b": 2 }`
JsonValue objectValue = JsonValue.from(Map.of(
  "a", 1,
  "b", 2
));

// Create an arbitrarily nested JSON equivalent to:
// { "a": [1, 2], "b": [3, 4] }
JsonValue complexValue = JsonValue.from(Map.of(
  "a", List.of(1, 2),
  "b", List.of(3, 4)
));
```

### 

Forcibly omitting required parameters

Normally a `Builder` class's `build` method will throw `IllegalStateException` if any required parameter or property is unset. To forcibly omit a required parameter or property, pass `JsonMissing`:

``` shiki
import com.anthropic.core.JsonMissing;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

MessageCreateParams params = MessageCreateParams.builder()
    .addUserMessage("Hello, world")
    .model(Model.CLAUDE_OPUS_4_6)
    .maxTokens(JsonMissing.of())
    .build();
```

### 

Response properties

To access undocumented response properties, call the `_additionalProperties()` method:

``` shiki
import com.anthropic.core.JsonValue;
import java.util.Map;

Map<String, JsonValue> additionalProperties = client.messages().create(params)._additionalProperties();
JsonValue secretPropertyValue = additionalProperties.get("secretProperty");
```

To access a property's raw JSON value, call its `_` prefixed method:

``` shiki
import com.anthropic.core.JsonField;
import java.util.Optional;

JsonField<Long> maxTokens = client.messages().create(params)._maxTokens();

if (maxTokens.isMissing()) {
  // The property is absent from the JSON response
} else if (maxTokens.isNull()) {
  // The property was set to literal null
} else {
  // Check if value was provided as a string
  Optional<String> jsonString = maxTokens.asString();

  // Try to deserialize into a custom type
  MyClass myObject = maxTokens.asUnknown().orElseThrow().convert(MyClass.class);
}
```

### 

Response validation

By default, the SDK will not throw an exception when the API returns a response that doesn't match the expected type. It will throw `AnthropicInvalidDataException` only if you directly access the property.

To check that the response is completely well-typed upfront, call `validate()`:

``` shiki
import com.anthropic.models.messages.Message;

Message message = client.messages().create(params).validate();
```

Or configure per-request:

``` shiki
import com.anthropic.models.messages.Message;

Message message = client.messages().create(
  params, RequestOptions.builder().responseValidation(true).build()
);
```

Or configure the default for all method calls at the client level:

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder()
    .fromEnv()
    .responseValidation(true)
    .build();
```

## 

HTTP client customization

### 

Proxy configuration

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import java.net.InetSocketAddress;
import java.net.Proxy;

AnthropicClient client = AnthropicOkHttpClient.builder()
    .fromEnv()
    .proxy(new Proxy(
      Proxy.Type.HTTP, new InetSocketAddress(
        "https://example.com", 8080
      )
    ))
    .build();
```

### 

HTTPS / SSL configuration

Most applications should not call these methods, and instead use the system defaults. The defaults include special optimizations that can be lost if the implementations are modified.

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder()
    .fromEnv()
    .sslSocketFactory(yourSSLSocketFactory)
    .trustManager(yourTrustManager)
    .hostnameVerifier(yourHostnameVerifier)
    .build();
```

### 

Custom HTTP client

The SDK consists of three artifacts:

- `anthropic-java-core` - Contains core SDK logic, does not depend on OkHttp. Exposes `AnthropicClient`, `AnthropicClientAsync`, and their implementation classes, all of which can work with any HTTP client.
- `anthropic-java-client-okhttp` - Depends on OkHttp. Exposes `AnthropicOkHttpClient` and `AnthropicOkHttpClientAsync`.
- `anthropic-java` - Depends on and exposes the APIs of both `anthropic-java-core` and `anthropic-java-client-okhttp`. Does not have its own logic.

This structure allows replacing the SDK's default HTTP client without pulling in unnecessary dependencies.

#### 

Customized OkHttpClient

Try the available [network options](#retries) before replacing the default client.

To use a customized `OkHttpClient`:

1.  Replace your `anthropic-java` dependency with `anthropic-java-core`.
2.  Copy `anthropic-java-client-okhttp`'s `OkHttpClient` class into your code and customize it.
3.  Construct `AnthropicClientImpl` or `AnthropicClientAsyncImpl` using your customized client.

#### 

Completely custom HTTP client

To use a completely custom HTTP client:

1.  Replace your `anthropic-java` dependency with `anthropic-java-core`.
2.  Write a class that implements the `HttpClient` interface.
3.  Construct `AnthropicClientImpl` or `AnthropicClientAsyncImpl` using your new client class.

## 

Platform integrations

For detailed platform setup guides, see:

- [Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock)
- [Google Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai)

### 

Amazon Bedrock

This SDK provides support for the Anthropic Bedrock API. This support requires the `anthropic-java-bedrock` library dependency.

Gradle

Gradle

Maven

Maven

``` shiki
implementation("com.anthropic:anthropic-java-bedrock:2.11.1")
```

Create the Anthropic client with the `BedrockBackend`. Usage of the API is otherwise the same.

``` shiki
import com.anthropic.bedrock.backends.BedrockBackend;
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder()
        .backend(BedrockBackend.fromEnv())
        .build();
```

`BedrockBackend.fromEnv()` automatically resolves the AWS credentials using the AWS default credentials provider chain and resolves the AWS region using the AWS default region provider chain.

With explicit credentials:

``` shiki
import com.anthropic.bedrock.backends.BedrockBackend;
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.AwsCredentials;
import software.amazon.awssdk.regions.Region;

AwsCredentials awsCredentials = AwsBasicCredentials.create(
        System.getenv("AWS_ACCESS_KEY_ID"),
        System.getenv("AWS_SECRET_ACCESS_KEY"));

AnthropicClient client = AnthropicOkHttpClient.builder()
        .backend(BedrockBackend.builder()
                .awsCredentials(awsCredentials)
                .region(Region.US_EAST_1)
                .build())
        .build();
```

You can also create and configure your own AWS credentials provider:

``` shiki
import com.anthropic.bedrock.backends.BedrockBackend;
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;

AwsCredentialsProvider awsCredentialsProvider =
        DefaultCredentialsProvider.builder()
                .asyncCredentialUpdateEnabled(true)
                .build();

AnthropicClient client = AnthropicOkHttpClient.builder()
        .backend(BedrockBackend.builder()
                .fromEnv(awsCredentialsProvider)
                .build())
        .build();
```

The AWS classes used above are included automatically as transitive dependencies of the `anthropic-java-bedrock` library dependency.

Currently, the Bedrock backend does not support the following:

- Anthropic Batch API
- Anthropic Token Counting API

#### 

Bedrock usage with an API key

The `BedrockBackend` can also use an API key instead of AWS credentials for request authorization. You can set the `AWS_BEARER_TOKEN_BEDROCK` environment variable to the value of your API key and call `BedrockBackend.fromEnv()` to authorize requests using that API key. An API key will be used in preference to AWS credentials if both are set in the environment.

The API key can also be passed directly to the backend:

``` shiki
AnthropicClient client = AnthropicOkHttpClient.builder()
        .backend(BedrockBackend.builder()
                .apiKey(myApiKey)
                .region(Region.US_EAST_1)
                .build())
        .build();
```

An error will occur if you set both an API key and an AWS credentials provider.

### 

Google Vertex AI

This SDK provides support for Anthropic models on the Google Cloud Vertex AI platform. This support requires the `anthropic-java-vertex` library dependency.

Gradle

Gradle

Maven

Maven

``` shiki
implementation("com.anthropic:anthropic-java-vertex:2.11.1")
```

Create the Anthropic client with the `VertexBackend`. Usage of the API is otherwise the same.

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.vertex.backends.VertexBackend;

AnthropicClient client = AnthropicOkHttpClient.builder()
        .backend(VertexBackend.fromEnv())
        .build();
```

`VertexBackend.fromEnv()` automatically resolves the Google OAuth2 credentials from your configured Google Cloud Application Default Credentials (ADC), the Google Cloud region from the `CLOUD_ML_REGION` environment variable, and the Google Cloud project ID from `ANTHROPIC_VERTEX_PROJECT_ID` environment variable.

With explicit credentials:

``` shiki
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.vertex.backends.VertexBackend;
import com.google.auth.oauth2.AccessToken;
import com.google.auth.oauth2.GoogleCredentials;

String accessToken = System.getenv("GOOGLE_APPLICATION_CREDENTIALS");
String project = System.getenv("ANTHROPIC_VERTEX_PROJECT_ID");

GoogleCredentials googleCredentials = GoogleCredentials.create(
        AccessToken.newBuilder().setTokenValue(accessToken).build());

AnthropicClient client = AnthropicOkHttpClient.builder()
        .backend(VertexBackend.builder()
                .googleCredentials(googleCredentials)
                .region("us-central1")
                .project(project)
                .build())
        .build();
```

The Google Cloud classes used above are included automatically as transitive dependencies of the `anthropic-java-vertex` library dependency.

Currently, the Vertex backend does not support the following:

- Anthropic Batch API

## 

Advanced usage

### 

Raw response access

To access HTTP headers, status codes, and the raw response body, prefix any HTTP method call with `withRawResponse()`:

``` shiki
import com.anthropic.core.http.Headers;
import com.anthropic.core.http.HttpResponseFor;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

MessageCreateParams params = MessageCreateParams.builder()
    .maxTokens(1024L)
    .addUserMessage("Hello, Claude")
    .model(Model.CLAUDE_OPUS_4_6)
    .build();
HttpResponseFor<Message> message = client.messages().withRawResponse().create(params);

int statusCode = message.statusCode();
Headers headers = message.headers();
```

You can still deserialize the response into an instance of a Java class if needed:

``` shiki
import com.anthropic.models.messages.Message;

Message parsedMessage = message.parse();
```

### 

Logging

The SDK uses the standard OkHttp logging interceptor.

Enable logging by setting the `ANTHROPIC_LOG` environment variable to `info`:

``` shiki
export ANTHROPIC_LOG=info
```

Or to `debug` for more verbose logging:

``` shiki
export ANTHROPIC_LOG=debug
```

### Jackson compatibility

### ProGuard/R8 configuration

### 

Undocumented API functionality

The SDK is typed for convenient usage of the documented API. However, it also supports working with undocumented or not yet supported parts of the API.

#### 

Undocumented endpoints

To make requests to undocumented endpoints, you can use the `putAdditionalHeader`, `putAdditionalQueryParam`, or `putAdditionalBodyProperty` methods as described in [Undocumented parameters](#undocumented-parameters).

#### 

Undocumented response properties

To access undocumented response properties, use the `_additionalProperties()` method as described in [Response properties](#response-properties).

## 

Beta features

You can access most beta API features through the `beta()` method on the client. To check the availability of all of Claude's capabilities and tools, see the [build with Claude overview](/docs/en/build-with-claude/overview).

For example, to use structured outputs:

``` shiki
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.StructuredMessageCreateParams;
import com.anthropic.models.messages.Model;

StructuredMessageCreateParams<BookList> createParams = MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_4_6)
        .maxTokens(2048)
        .outputConfig(BookList.class)
        .addUserMessage("List some famous late twentieth century novels.")
        .build();

client.beta().messages().create(createParams);
```

## 

Frequently asked questions

### Why doesn't the SDK use plain enum classes?

### Why are fields represented using JsonField\<T\> instead of just plain T?

### Why doesn't the SDK use data classes?

### Why doesn't the SDK use checked exceptions?

## 

Additional resources

- [GitHub repository](https://github.com/anthropics/anthropic-sdk-java)
- [Javadocs](https://javadoc.io/doc/com.anthropic/anthropic-java)
- [API reference](/docs/en/api/overview)
- [Streaming guide](/docs/en/build-with-claude/streaming)
- [Tool use guide](/docs/en/agents-and-tools/tool-use/overview)

Was this page helpful?

- 

- [Installation](#installation)

- [Requirements](#requirements)

- [Quick start](#quick-start)

- [Client configuration](#client-configuration)

- [API key setup](#api-key-setup)

- [Configuration options](#configuration-options)

- [Modifying configuration](#modifying-configuration)

- [Async usage](#async-usage)

- [Streaming](#streaming)

- [Synchronous streaming](#synchronous-streaming)

- [Asynchronous streaming](#asynchronous-streaming)

- [Streaming with message accumulator](#streaming-with-message-accumulator)

- [Structured outputs](#structured-outputs)

- [Defining classes](#defining-classes)

- [Using structured outputs](#using-structured-outputs)

- [Optional fields](#optional-fields)

- [Local JSON schema validation](#local-json-schema-validation)

- [Structured outputs with streaming](#structured-outputs-with-streaming)

- [Defining JSON schema properties](#defining-json-schema-properties)

- [Annotating classes and JSON schemas](#annotating-classes-and-json-schemas)

- [Tool use](#tool-use)

- [Defining tools with annotations](#defining-tools-with-annotations)

- [Calling tools](#calling-tools)

- [Tool name conversion](#tool-name-conversion)

- [Local tool JSON schema validation](#local-tool-json-schema-validation)

- [Annotating tool classes](#annotating-tool-classes)

- [Message batches](#message-batches)

- [File uploads](#file-uploads)

- [Binary responses](#binary-responses)

- [Error handling](#error-handling)

- [Status code mapping](#status-code-mapping)

- [Request IDs](#request-ids)

- [Retries](#retries)

- [Timeouts](#timeouts)

- [Long requests](#long-requests)

- [Pagination](#pagination)

- [Auto-pagination](#auto-pagination)

- [Manual pagination](#manual-pagination)

- [Type system](#type-system)

- [Immutability and builders](#immutability-and-builders)

- [Requests and responses](#requests-and-responses)

- [Undocumented parameters](#undocumented-parameters)

- [JsonValue creation](#json-value-creation)

- [Forcibly omitting required parameters](#forcibly-omitting-required-parameters)

- [Response properties](#response-properties)

- [Response validation](#response-validation)

- [HTTP client customization](#http-client-customization)

- [Proxy configuration](#proxy-configuration)

- [HTTPS / SSL configuration](#https-ssl-configuration)

- [Custom HTTP client](#custom-http-client)

- [Platform integrations](#platform-integrations)

- [Amazon Bedrock](#amazon-bedrock)

- [Google Vertex AI](#google-vertex-ai)

- [Advanced usage](#advanced-usage)

- [Raw response access](#raw-response-access)

- [Logging](#logging)

- [Undocumented API functionality](#undocumented-api-functionality)

- [Beta features](#beta-features)

- [Frequently asked questions](#frequently-asked-questions)

- [Additional resources](#additional-resources)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
