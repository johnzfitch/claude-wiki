---
category: "05-Agent-SDK"
fetched_at: "2026-02-07T10:05:12Z"
source_url: "https://platform.claude.com/docs/en/api/sdks/go"
title: "Go SDK - Claude API Docs"
---

Client SDKs

# Go SDK

Copy page

Install and configure the Anthropic Go SDK with context-based cancellation and functional options

Copy page

The Anthropic Go library provides convenient access to the Anthropic REST API from applications written in Go.

For API feature documentation with code examples, see the [API reference](/docs/en/api/overview). This page covers Go-specific SDK features and configuration.

## 

Installation

``` shiki
import (
    "github.com/anthropics/anthropic-sdk-go" // imported as anthropic
)
```

Or to pin the version:

``` shiki
go get -u 'github.com/anthropics/anthropic-sdk-go@v1.19.0'
```

## 

Requirements

This library requires Go 1.22+.

## 

Usage

``` shiki
package main

import (
    "context"
    "fmt"

    "github.com/anthropics/anthropic-sdk-go"
    "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
    client := anthropic.NewClient(
        option.WithAPIKey("my-anthropic-api-key"), // defaults to os.LookupEnv("ANTHROPIC_API_KEY")
    )
    message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
        MaxTokens: 1024,
        Messages: []anthropic.MessageParam{
            anthropic.NewUserMessage(anthropic.NewTextBlock("What is a quaternion?")),
        },
        Model: anthropic.ModelClaudeOpus4_6,
    })
    if err != nil {
        panic(err.Error())
    }
    fmt.Printf("%+v\n", message.Content)
}
```

### Conversations

### System prompts

### Streaming

### Tool calling

## 

Request fields

The anthropic library uses the [`omitzero`](https://tip.golang.org/doc/go1.24#encodingjsonpkgencodingjson) semantics from the Go 1.24+ `encoding/json` release for request fields.

Required primitive fields (`int64`, `string`, etc.) feature the tag `` `json:"...,required"` ``. These fields are always serialized, even their zero values.

Optional primitive types are wrapped in a `param.Opt[T]`. These fields can be set with the provided constructors, `anthropic.String(string)`, `anthropic.Int(int64)`, etc.

Any `param.Opt[T]`, map, slice, struct or string enum uses the tag `` `json:"...,omitzero"` ``. Its zero value is considered omitted.

The `param.IsOmitted(any)` function can confirm the presence of any `omitzero` field.

``` shiki
p := anthropic.ExampleParams{
    ID:   "id_xxx",                // required property
    Name: anthropic.String("..."), // optional property

    Point: anthropic.Point{
        X: 0,                // required field will serialize as 0
        Y: anthropic.Int(1), // optional field will serialize as 1
        // ... omitted non-required fields will not be serialized
    },

    Origin: anthropic.Origin{}, // the zero value of [Origin] is considered omitted
}
```

To send `null` instead of a `param.Opt[T]`, use `param.Null[T]()`. To send `null` instead of a struct `T`, use `param.NullStruct[T]()`.

``` shiki
p.Name = param.Null[string]()       // 'null' instead of string
p.Point = param.NullStruct[Point]() // 'null' instead of struct

param.IsNull(p.Name)  // true
param.IsNull(p.Point) // true
```

Request structs contain a `.SetExtraFields(map[string]any)` method which can send non-conforming fields in the request body. Extra fields overwrite any struct fields with a matching key.

For security reasons, only use `SetExtraFields` with trusted data.

To send a custom value instead of a struct, use `param.Override[T](value)`.

``` shiki
// In cases where the API specifies a given type,
// but you want to send something else, use [SetExtraFields]:
p.SetExtraFields(map[string]any{
    "x": 0.01, // send "x" as a float instead of int
})

// Send a number instead of an object
custom := param.Override[anthropic.FooParams](12)
```

### 

Request unions

Unions are represented as a struct with fields prefixed by "Of" for each of its variants, only one field can be non-zero. The non-zero field will be serialized.

Sub-properties of the union can be accessed via methods on the union struct. These methods return a mutable pointer to the underlying data, if present.

``` shiki
// Only one field can be non-zero, use param.IsOmitted() to check if a field is set
type AnimalUnionParam struct {
    OfCat *Cat `json:",omitzero,inline`
    OfDog *Dog `json:",omitzero,inline`
}

animal := AnimalUnionParam{
    OfCat: &Cat{
        Name: "Whiskers",
        Owner: PersonParam{
            Address: AddressParam{Street: "3333 Coyote Hill Rd", Zip: 0},
        },
    },
}

// Mutating a field
if address := animal.GetOwner().GetAddress(); address != nil {
    address.ZipCode = 94304
}
```

## 

Response objects

All fields in response structs are ordinary value types (not pointers or wrappers). Response structs also include a special `JSON` field containing metadata about each property.

``` shiki
type Animal struct {
    Name   string `json:"name,nullable"`
    Owners int    `json:"owners"`
    Age    int    `json:"age"`
    JSON   struct {
        Name        respjson.Field
        Owner       respjson.Field
        Age         respjson.Field
        ExtraFields map[string]respjson.Field
    } `json:"-"`
}
```

To handle optional data, use the `.Valid()` method on the JSON field. `.Valid()` returns true if a field is not `null`, not present, or couldn't be marshaled.

If `.Valid()` is false, the corresponding field will simply be its zero value.

``` shiki
raw := `{"owners": 1, "name": null}`

var res Animal
json.Unmarshal([]byte(raw), &res)

// Accessing regular fields

res.Owners // 1
res.Name   // ""
res.Age    // 0

// Optional field checks

res.JSON.Owners.Valid() // true
res.JSON.Name.Valid()   // false
res.JSON.Age.Valid()    // false

// Raw JSON values

res.JSON.Owners.Raw()                  // "1"
res.JSON.Name.Raw() == "null"          // true
res.JSON.Name.Raw() == respjson.Null   // true
res.JSON.Age.Raw() == ""               // true
res.JSON.Age.Raw() == respjson.Omitted // true
```

These `.JSON` structs also include an `ExtraFields` map containing any properties in the json response that were not specified in the struct. This can be useful for API features not yet present in the SDK.

``` shiki
body := res.JSON.ExtraFields["my_unexpected_field"].Raw()
```

### 

Response unions

In responses, unions are represented by a flattened struct containing all possible fields from each of the object variants. To convert it to a variant use the `.AsFooVariant()` method or the `.AsAny()` method if present.

If a response value union contains primitive values, primitive fields will be alongside the properties but prefixed with `Of` and feature the tag `json:"...,inline"`.

``` shiki
type AnimalUnion struct {
    // From variants [Dog], [Cat]
    Owner Person `json:"owner"`
    // From variant [Dog]
    DogBreed string `json:"dog_breed"`
    // From variant [Cat]
    CatBreed string `json:"cat_breed"`
    // ...

    JSON struct {
        Owner respjson.Field
        // ...
    } `json:"-"`
}

// If animal variant
if animal.Owner.Address.ZipCode == "" {
    panic("missing zip code")
}

// Switch on the variant
switch variant := animal.AsAny().(type) {
case Dog:
case Cat:
default:
    panic("unexpected type")
}
```

## 

Streaming

Use the streaming API for real-time responses:

``` shiki
stream := client.Messages.NewStreaming(context.TODO(), anthropic.MessageNewParams{
    Model:     anthropic.ModelClaudeOpus4_6,
    MaxTokens: 1024,
    Messages: []anthropic.MessageParam{
        anthropic.NewUserMessage(anthropic.NewTextBlock("What is a quaternion?")),
    },
})

message := anthropic.Message{}
for stream.Next() {
    event := stream.Current()
    err := message.Accumulate(event)
    if err != nil {
        panic(err)
    }

    switch eventVariant := event.AsAny().(type) {
        case anthropic.ContentBlockDeltaEvent:
        switch deltaVariant := eventVariant.Delta.AsAny().(type) {
        case anthropic.TextDelta:
            print(deltaVariant.Text)
        }

    }
}

if stream.Err() != nil {
    panic(stream.Err())
}
```

## 

Error handling

When the API returns a non-success status code, we return an error with type `*anthropic.Error`. This contains the `StatusCode`, `*http.Request`, and `*http.Response` values of the request, as well as the JSON of the error body (much like other response objects in the SDK). The error also includes the `RequestID` from the response headers, which is useful for troubleshooting with Anthropic support.

To handle errors, we recommend that you use the `errors.As` pattern:

``` shiki
_, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
    MaxTokens: 1024,
    Messages: []anthropic.MessageParam{{
        Content: []anthropic.ContentBlockParamUnion{{
            OfText: &anthropic.TextBlockParam{Text: "What is a quaternion?", CacheControl: anthropic.CacheControlEphemeralParam{TTL: anthropic.CacheControlEphemeralTTLTTL5m}, Citations: []anthropic.TextCitationParamUnion{{
                OfCharLocation: &anthropic.CitationCharLocationParam{CitedText: "cited_text", DocumentIndex: 0, DocumentTitle: anthropic.String("x"), EndCharIndex: 0, StartCharIndex: 0},
            }}},
        }},
        Role: anthropic.MessageParamRoleUser,
    }},
    Model: anthropic.ModelClaudeOpus4_6,
})
if err != nil {
    var apierr *anthropic.Error
    if errors.As(err, &apierr) {
        println("Request ID:", apierr.RequestID)
        println(string(apierr.DumpRequest(true)))  // Prints the serialized HTTP request
        println(string(apierr.DumpResponse(true))) // Prints the serialized HTTP response
    }
    panic(err.Error()) // GET "/v1/messages": 400 Bad Request (Request-ID: req_xxx) { ... }
}
```

When other errors occur, they are returned unwrapped; for example, if HTTP transport fails, you might receive `*url.Error` wrapping `*net.OpError`.

## 

Retries

Certain errors will be automatically retried 2 times by default, with a short exponential backoff. We retry by default all connection errors, 408 Request Timeout, 409 Conflict, 429 Rate Limit, and \>=500 Internal errors.

You can use the `WithMaxRetries` option to configure or disable this:

``` shiki
// Configure the default for all requests:
client := anthropic.NewClient(
    option.WithMaxRetries(0), // default is 2
)

// Override per-request:
client.Messages.New(
    context.TODO(),
    anthropic.MessageNewParams{
        MaxTokens: 1024,
        Messages: []anthropic.MessageParam{{
            Content: []anthropic.ContentBlockParamUnion{{
                OfRequestTextBlock: &anthropic.TextBlockParam{Text: "What is a quaternion?"},
            }},
            Role: anthropic.MessageParamRoleUser,
        }},
        Model: anthropic.ModelClaudeOpus4_6,
    },
    option.WithMaxRetries(5),
)
```

## 

Timeouts

Requests do not time out by default; use context to configure a timeout for a request lifecycle.

Note that if a request is [retried](#retries), the context timeout does not start over. To set a per-retry timeout, use `option.WithRequestTimeout()`.

``` shiki
// This sets the timeout for the request, including all the retries.
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Minute)
defer cancel()
client.Messages.New(
    ctx,
    anthropic.MessageNewParams{
        MaxTokens: 1024,
        Messages: []anthropic.MessageParam{{
            Content: []anthropic.ContentBlockParamUnion{{
                OfRequestTextBlock: &anthropic.TextBlockParam{Text: "What is a quaternion?"},
            }},
            Role: anthropic.MessageParamRoleUser,
        }},
        Model: anthropic.ModelClaudeOpus4_6,
    },
    // This sets the per-retry timeout
    option.WithRequestTimeout(20*time.Second),
)
```

## 

Long requests

We highly encourage you use the streaming Messages API for longer running requests.

We do not recommend setting a large `MaxTokens` value without using streaming as some networks may drop idle connections after a certain period of time, which can cause the request to fail or [timeout](#timeouts) without receiving a response from Anthropic.

This SDK will also return an error if a non-streaming request is expected to be above roughly 10 minutes long. Calling `.Messages.NewStreaming()` or [setting a custom timeout](#timeouts) disables this error.

## 

File uploads

Request parameters that correspond to file uploads in multipart requests are typed as `io.Reader`. The contents of the `io.Reader` will by default be sent as a multipart form part with the file name of "anonymous_file" and content-type of "application/octet-stream", so we recommend always specifying a custom content-type with the `anthropic.File(reader io.Reader, filename string, contentType string)` helper we provide to easily wrap any `io.Reader` with the appropriate file name and content type.

``` shiki
// A file from the file system
file, err := os.Open("/path/to/file.json")
anthropic.BetaFileUploadParams{
    File: anthropic.File(file, "custom-name.json", "application/json"),
    Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
}

// A file from a string
anthropic.BetaFileUploadParams{
    File: anthropic.File(strings.NewReader("my file contents"), "custom-name.json", "application/json"),
    Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
}
```

The file name and content-type can also be customized by implementing `Name() string` or `ContentType() string` on the run-time type of `io.Reader`. Note that `os.File` implements `Name() string`, so a file returned by `os.Open` will be sent with the file name on disk.

## 

Pagination

This library provides some conveniences for working with paginated list endpoints.

You can use `.ListAutoPaging()` methods to iterate through items across all pages:

``` shiki
iter := client.Messages.Batches.ListAutoPaging(context.TODO(), anthropic.MessageBatchListParams{
    Limit: anthropic.Int(20),
})
// Automatically fetches more pages as needed.
for iter.Next() {
    messageBatch := iter.Current()
    fmt.Printf("%+v\n", messageBatch)
}
if err := iter.Err(); err != nil {
    panic(err.Error())
}
```

Or you can use simple `.List()` methods to fetch a single page and receive a standard response object with additional helper methods like `.GetNextPage()`:

``` shiki
page, err := client.Messages.Batches.List(context.TODO(), anthropic.MessageBatchListParams{
    Limit: anthropic.Int(20),
})
for page != nil {
    for _, batch := range page.Data {
        fmt.Printf("%+v\n", batch)
    }
    page, err = page.GetNextPage()
}
if err != nil {
    panic(err.Error())
}
```

## 

RequestOptions

This library uses the functional options pattern. Functions defined in the `option` package return a `RequestOption`, which is a closure that mutates a `RequestConfig`. These options can be supplied to the client or at individual requests. For example:

``` shiki
client := anthropic.NewClient(
    // Adds a header to every request made by the client
    option.WithHeader("X-Some-Header", "custom_header_info"),
)

client.Messages.New(context.TODO(), ...,
    // Override the header
    option.WithHeader("X-Some-Header", "some_other_custom_header_info"),
    // Add an undocumented field to the request body, using sjson syntax
    option.WithJSONSet("some.json.path", map[string]string{"my": "object"}),
)
```

The request option `option.WithDebugLog(nil)` may be helpful while debugging.

See the [full list of request options](https://pkg.go.dev/github.com/anthropics/anthropic-sdk-go/option).

## 

HTTP client customization

### 

Middleware

We provide `option.WithMiddleware` which applies the given middleware to requests.

``` shiki
func Logger(req *http.Request, next option.MiddlewareNext) (res *http.Response, err error) {
    // Before the request
    start := time.Now()
    LogReq(req)

    // Forward the request to the next handler
    res, err = next(req)

    // Handle stuff after the request
    LogRes(res, err, time.Since(start))

    return res, err
}

client := anthropic.NewClient(
    option.WithMiddleware(Logger),
)
```

When multiple middlewares are provided as variadic arguments, the middlewares are applied left to right. If `option.WithMiddleware` is given multiple times, for example first in the client then the method, the middleware in the client will run first and the middleware given in the method will run next.

You may also replace the default `http.Client` with `option.WithHTTPClient(client)`. Only one http client is accepted (this overwrites any previous client) and receives requests after any middleware has been applied.

## 

Platform integrations

For detailed platform setup guides, see:

- [Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock)
- [Google Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai)

### 

Amazon Bedrock

To use this library with [Amazon Bedrock](https://aws.amazon.com/bedrock/claude/), use the bedrock request option `bedrock.WithLoadDefaultConfig(...)` which reads the [default config](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

Importing the `bedrock` library also globally registers a decoder for `application/vnd.amazon.eventstream` for streaming.

``` shiki
package main

import (
    "github.com/anthropics/anthropic-sdk-go"
    "github.com/anthropics/anthropic-sdk-go/bedrock"
)

func main() {
    client := anthropic.NewClient(
        bedrock.WithLoadDefaultConfig(context.Background()),
    )
}
```

If you already have an `aws.Config`, you can also use it directly with `bedrock.WithConfig(cfg)`.

Read more about Anthropic and Amazon Bedrock in [Claude on Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock).

### 

Google Vertex AI

To use this library with [Google Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude), use the request option `vertex.WithGoogleAuth(...)` which reads the [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials).

``` shiki
package main

import (
    "context"

    "github.com/anthropics/anthropic-sdk-go"
    "github.com/anthropics/anthropic-sdk-go/vertex"
)

func main() {
    client := anthropic.NewClient(
        vertex.WithGoogleAuth(context.Background(), "us-central1", "id-xxx"),
    )
}
```

If you already have `*google.Credentials`, you can also use it directly with `vertex.WithCredentials(ctx, region, projectId, creds)`.

Read more about Anthropic and Google Vertex AI in [Claude on Google Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai).

## 

Advanced usage

### 

Accessing raw response data (e.g. response headers)

You can access the raw HTTP response data by using the `option.WithResponseInto()` request option. This is useful when you need to examine response headers, status codes, or other details.

``` shiki
// Create a variable to store the HTTP response
var response *http.Response
message, err := client.Messages.New(
    context.TODO(),
    anthropic.MessageNewParams{
        MaxTokens: 1024,
        Messages: []anthropic.MessageParam{{
            Content: []anthropic.ContentBlockParamUnion{{
                OfText: &anthropic.TextBlockParam{Text: "What is a quaternion?", CacheControl: anthropic.CacheControlEphemeralParam{TTL: anthropic.CacheControlEphemeralTTLTTL5m}, Citations: []anthropic.TextCitationParamUnion{{
                    OfCharLocation: &anthropic.CitationCharLocationParam{CitedText: "cited_text", DocumentIndex: 0, DocumentTitle: anthropic.String("x"), EndCharIndex: 0, StartCharIndex: 0},
                }}},
            }},
            Role: anthropic.MessageParamRoleUser,
        }},
        Model: anthropic.ModelClaudeOpus4_6,
    },
    option.WithResponseInto(&response),
)
if err != nil {
    // handle error
}
fmt.Printf("%+v\n", message)

fmt.Printf("Status Code: %d\n", response.StatusCode)
fmt.Printf("Headers: %+#v\n", response.Header)
```

### 

Making custom/undocumented requests

This library is typed for convenient access to the documented API. If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### 

Undocumented endpoints

To make requests to undocumented endpoints, you can use `client.Get`, `client.Post`, and other HTTP verbs. `RequestOptions` on the client, such as retries, will be respected when making these requests.

``` shiki
var (
    // params can be an io.Reader, a []byte, an encoding/json serializable object,
    // or a "...Params" struct defined in this library.
    params map[string]any

    // result can be an []byte, *http.Response, a encoding/json deserializable object,
    // or a model defined in this library.
    result *http.Response
)
err := client.Post(context.Background(), "/unspecified", params, &result)
if err != nil {
    ...
}
```

#### 

Undocumented request params

To make requests using undocumented parameters, you may use either the `option.WithQuerySet()` or the `option.WithJSONSet()` methods.

``` shiki
params := FooNewParams{
    ID:   "id_xxxx",
    Data: FooNewParamsData{
        FirstName: anthropic.String("John"),
    },
}
client.Foo.New(context.Background(), params, option.WithJSONSet("data.last_name", "Doe"))
```

#### 

Undocumented response properties

To access undocumented response properties, you may either access the raw JSON of the response as a string with `result.JSON.RawJSON()`, or get the raw JSON of a particular field on the result with `result.JSON.Foo.Raw()`.

Any fields that are not present on the response struct will be saved and can be accessed by `result.JSON.ExtraFields()` which returns the extra fields as a `map[string]Field`.

## 

Additional resources

- [GitHub repository](https://github.com/anthropics/anthropic-sdk-go)
- [Go package documentation](https://pkg.go.dev/github.com/anthropics/anthropic-sdk-go)
- [API reference](/docs/en/api/overview)
- [Streaming guide](/docs/en/build-with-claude/streaming)

Was this page helpful?

- 

- [Installation](#installation)

- [Requirements](#requirements)

- [Usage](#usage)

- [Request fields](#request-fields)

- [Request unions](#request-unions)

- [Response objects](#response-objects)

- [Response unions](#response-unions)

- [Streaming](#streaming)

- [Error handling](#error-handling)

- [Retries](#retries)

- [Timeouts](#timeouts)

- [Long requests](#long-requests)

- [File uploads](#file-uploads)

- [Pagination](#pagination)

- [RequestOptions](#request-options)

- [HTTP client customization](#http-client-customization)

- [Middleware](#middleware)

- [Platform integrations](#platform-integrations)

- [Amazon Bedrock](#amazon-bedrock)

- [Google Vertex AI](#google-vertex-ai)

- [Advanced usage](#advanced-usage)

- [Accessing raw response data (e.g. response headers)](#accessing-raw-response-data-e-g-response-headers)

- [Making custom/undocumented requests](#making-custom-undocumented-requests)

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
