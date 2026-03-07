---
category: "06-MCP-Tools"
fetched_at: "2026-03-07T01:05:27Z"
source_url: "https://modelcontextprotocol.io/specification/2025-11-25/schema"
title: "Schema Reference - Model Context Protocol"
---

# Schema Reference


## 

[​](#json-rpc)

JSON-RPC

### 

[​](#jsonrpcerrorresponse)

`JSONRPCErrorResponse`

interface JSONRPCErrorResponse {\
  [jsonrpc](#jsonrpcerrorresponse-jsonrpc): “2.0”;\
  [id](#jsonrpcerrorresponse-id)?: [RequestId](#requestid);\
  [error](#jsonrpcerrorresponse-error): [Error](#error);\
}

A response to a request that indicates an error occurred.

jsonrpc: “2.0”[](#jsonrpcerrorresponse-jsonrpc)

id?: RequestId[](#jsonrpcerrorresponse-id)

error: Error[](#jsonrpcerrorresponse-error)

### 

[​](#jsonrpcmessage)

`JSONRPCMessage`

JSONRPCMessage: [JSONRPCRequest](#jsonrpcrequest) \| [JSONRPCNotification](#jsonrpcnotification) \| [JSONRPCResponse](#jsonrpcresponse)

Refers to any valid JSON-RPC object that can be decoded off the wire, or encoded to be sent.

### 

[​](#jsonrpcnotification)

`JSONRPCNotification`

interface JSONRPCNotification {\
  [method](#jsonrpcnotification-method): string;\
  [params](#jsonrpcnotification-params)?: { \[key: string\]: any };\
  [jsonrpc](#jsonrpcnotification-jsonrpc): “2.0”;\
}

A notification which does not expect a response.

method: string[](#jsonrpcnotification-method)

Inherited from Notification.method

params?: { \[key: string\]: any }[](#jsonrpcnotification-params)

Inherited from Notification.params

jsonrpc: “2.0”[](#jsonrpcnotification-jsonrpc)

### 

[​](#jsonrpcrequest)

`JSONRPCRequest`

interface JSONRPCRequest {\
  [method](#jsonrpcrequest-method): string;\
  [params](#jsonrpcrequest-params)?: { \[key: string\]: any };\
  [jsonrpc](#jsonrpcrequest-jsonrpc): “2.0”;\
  [id](#jsonrpcrequest-id): [RequestId](#requestid);\
}

A request that expects a response.

method: string[](#jsonrpcrequest-method)

Inherited from Request.method

params?: { \[key: string\]: any }[](#jsonrpcrequest-params)

Inherited from Request.params

jsonrpc: “2.0”[](#jsonrpcrequest-jsonrpc)

id: RequestId[](#jsonrpcrequest-id)

### 

[​](#jsonrpcresponse)

`JSONRPCResponse`

JSONRPCResponse: [JSONRPCResultResponse](#jsonrpcresultresponse) \| [JSONRPCErrorResponse](#jsonrpcerrorresponse)

A response to a request, containing either the result or error.

### 

[​](#jsonrpcresultresponse)

`JSONRPCResultResponse`

interface JSONRPCResultResponse {\
  [jsonrpc](#jsonrpcresultresponse-jsonrpc): “2.0”;\
  [id](#jsonrpcresultresponse-id): [RequestId](#requestid);\
  [result](#jsonrpcresultresponse-result): [Result](#result);\
}

A successful (non-error) response to a request.

jsonrpc: “2.0”[](#jsonrpcresultresponse-jsonrpc)

id: RequestId[](#jsonrpcresultresponse-id)

result: Result[](#jsonrpcresultresponse-result)

## 

[​](#common-types)

Common Types

### 

[​](#annotations)

`Annotations`

interface Annotations {\
  [audience](#annotations-audience)?: [Role](#role)\[\];\
  [priority](#annotations-priority)?: number;\
  [lastModified](#annotations-lastmodified)?: string;\
}

Optional annotations for the client. The client can use annotations to inform how objects are used or displayed

audience?: Role\[\][](#annotations-audience)

Describes who the intended audience of this object or data is.

It can include multiple entries to indicate content useful for multiple audiences (e.g., `[“user”, “assistant”]`).

priority?: number[](#annotations-priority)

Describes how important this data is for operating the server.

A value of 1 means “most important,” and indicates that the data is effectively required, while 0 means “least important,” and indicates that the data is entirely optional.

lastModified?: string[](#annotations-lastmodified)

The moment the resource was last modified, as an ISO 8601 formatted string.

Should be an ISO 8601 formatted string (e.g., “2025-01-12T15:00:58Z”).

Examples: last activity timestamp in an open file, timestamp when the resource was attached, etc.

### 

[​](#cursor)

`Cursor`

Cursor: string

An opaque token used to represent a cursor for pagination.

### 

[​](#emptyresult)

`EmptyResult`

EmptyResult: [Result](#result)

A response that indicates success but carries no data.

### 

[​](#error)

`Error`

interface Error {\
  [code](#error-code): number;\
  [message](#error-message): string;\
  [data](#error-data)?: unknown;\
}

code: number[](#error-code)

The error type that occurred.

message: string[](#error-message)

A short description of the error. The message SHOULD be limited to a concise single sentence.

data?: unknown[](#error-data)

Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).

### 

[​](#icon)

`Icon`

interface Icon {\
  [src](#icon-src): string;\
  [mimeType](#icon-mimetype)?: string;\
  [sizes](#icon-sizes)?: string\[\];\
  [theme](#icon-theme)?: “light” \| “dark”;\
}

An optionally-sized icon that can be displayed in a user interface.

src: string[](#icon-src)

A standard URI pointing to an icon resource. May be an HTTP/HTTPS URL or a `data:` URI with Base64-encoded image data.

Consumers SHOULD takes steps to ensure URLs serving icons are from the same domain as the client/server or a trusted domain.

Consumers SHOULD take appropriate precautions when consuming SVGs as they can contain executable JavaScript.

mimeType?: string[](#icon-mimetype)

Optional MIME type override if the source MIME type is missing or generic. For example: `“image/png”`, `“image/jpeg”`, or `“image/svg+xml”`.

sizes?: string\[\][](#icon-sizes)

Optional array of strings that specify sizes at which the icon can be used. Each string should be in WxH format (e.g., `“48x48”`, `“96x96”`) or `“any”` for scalable formats like SVG.

If not provided, the client should assume that the icon can be used at any size.

theme?: “light” \| “dark”[](#icon-theme)

Optional specifier for the theme this icon is designed for. `light` indicates the icon is designed to be used with a light background, and `dark` indicates the icon is designed to be used with a dark background.

If not provided, the client should assume the icon can be used with any theme.

### 

[​](#logginglevel)

`LoggingLevel`

LoggingLevel:\
  \| “debug”\
  \| “info”\
  \| “notice”\
  \| “warning”\
  \| “error”\
  \| “critical”\
  \| “alert”\
  \| “emergency”

The severity of a log message.

These map to syslog message severities, as specified in RFC-5424: [](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1)[https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1)

### 

[​](#progresstoken)

`ProgressToken`

ProgressToken: string \| number

A progress token, used to associate progress notifications with the original request.

### 

[​](#requestid)

`RequestId`

RequestId: string \| number

A uniquely identifying ID for a request in JSON-RPC.

### 

[​](#result)

`Result`

interface Result {\
  [\_meta](#result-_meta)?: { \[key: string\]: unknown };\
  \[key: string\]: unknown;\
}

\_meta?: { \[key: string\]: unknown }[](#result-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

### 

[​](#role)

`Role`

Role: “user” \| “assistant”

The sender or recipient of messages and data in a conversation.

## 

[​](#content)

Content

### 

[​](#audiocontent)

`AudioContent`

interface AudioContent {\
  [type](#audiocontent-type): “audio”;\
  [data](#audiocontent-data): string;\
  [mimeType](#audiocontent-mimetype): string;\
  [annotations](#audiocontent-annotations)?: [Annotations](#annotations);\
  [\_meta](#audiocontent-_meta)?: { \[key: string\]: unknown };\
}

Audio provided to or from an LLM.

type: “audio”[](#audiocontent-type)

data: string[](#audiocontent-data)

The base64-encoded audio data.

mimeType: string[](#audiocontent-mimetype)

The MIME type of the audio. Different providers may support different audio types.

annotations?: Annotations[](#audiocontent-annotations)

Optional annotations for the client.

\_meta?: { \[key: string\]: unknown }[](#audiocontent-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

### 

[​](#blobresourcecontents)

`BlobResourceContents`

interface BlobResourceContents {\
  [uri](#blobresourcecontents-uri): string;\
  [mimeType](#blobresourcecontents-mimetype)?: string;\
  [\_meta](#blobresourcecontents-_meta)?: { \[key: string\]: unknown };\
  [blob](#blobresourcecontents-blob): string;\
}

uri: string[](#blobresourcecontents-uri)

The URI of this resource.

Inherited from ResourceContents.uri

mimeType?: string[](#blobresourcecontents-mimetype)

The MIME type of this resource, if known.

Inherited from ResourceContents.mimeType

\_meta?: { \[key: string\]: unknown }[](#blobresourcecontents-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from ResourceContents.\_meta

blob: string[](#blobresourcecontents-blob)

A base64-encoded string representing the binary data of the item.

### 

[​](#contentblock)

`ContentBlock`

ContentBlock:\
  \| [TextContent](#textcontent)\
  \| [ImageContent](#imagecontent)\
  \| [AudioContent](#audiocontent)\
  \| [ResourceLink](#resourcelink)\
  \| [EmbeddedResource](#embeddedresource)

### 

[​](#embeddedresource)

`EmbeddedResource`

interface EmbeddedResource {\
  [type](#embeddedresource-type): “resource”;\
  [resource](#embeddedresource-resource): [TextResourceContents](#textresourcecontents) \| [BlobResourceContents](#blobresourcecontents);\
  [annotations](#embeddedresource-annotations)?: [Annotations](#annotations);\
  [\_meta](#embeddedresource-_meta)?: { \[key: string\]: unknown };\
}

The contents of a resource, embedded into a prompt or tool call result.

It is up to the client how best to render embedded resources for the benefit of the LLM and/or the user.

type: “resource”[](#embeddedresource-type)

resource: TextResourceContents \| BlobResourceContents[](#embeddedresource-resource)

annotations?: Annotations[](#embeddedresource-annotations)

Optional annotations for the client.

\_meta?: { \[key: string\]: unknown }[](#embeddedresource-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

### 

[​](#imagecontent)

`ImageContent`

interface ImageContent {\
  [type](#imagecontent-type): “image”;\
  [data](#imagecontent-data): string;\
  [mimeType](#imagecontent-mimetype): string;\
  [annotations](#imagecontent-annotations)?: [Annotations](#annotations);\
  [\_meta](#imagecontent-_meta)?: { \[key: string\]: unknown };\
}

An image provided to or from an LLM.

type: “image”[](#imagecontent-type)

data: string[](#imagecontent-data)

The base64-encoded image data.

mimeType: string[](#imagecontent-mimetype)

The MIME type of the image. Different providers may support different image types.

annotations?: Annotations[](#imagecontent-annotations)

Optional annotations for the client.

\_meta?: { \[key: string\]: unknown }[](#imagecontent-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

### 

[​](#resourcelink)

`ResourceLink`

interface ResourceLink {\
  [icons](#resourcelink-icons)?: [Icon](#icon)\[\];\
  [name](#resourcelink-name): string;\
  [title](#resourcelink-title)?: string;\
  [uri](#resourcelink-uri): string;\
  [description](#resourcelink-description)?: string;\
  [mimeType](#resourcelink-mimetype)?: string;\
  [annotations](#resourcelink-annotations)?: [Annotations](#annotations);\
  [size](#resourcelink-size)?: number;\
  [\_meta](#resourcelink-_meta)?: { \[key: string\]: unknown };\
  [type](#resourcelink-type): “resource_link”;\
}

A resource that the server is capable of reading, included in a prompt or tool call result.

Note: resource links returned by tools are not guaranteed to appear in the results of `resources/list` requests.

icons?: Icon\[\][](#resourcelink-icons)

Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:

- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:

- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)

Inherited from [Resource](#resource).[icons](#resource-icons)

name: string[](#resourcelink-name)

Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn’t present).

Inherited from [Resource](#resource).[name](#resource-name)

title?: string[](#resourcelink-title)

Intended for UI and end-user contexts — optimized to be human-readable and easily understood, even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for Tool, where `annotations.title` should be given precedence over using `name`, if present).

Inherited from [Resource](#resource).[title](#resource-title)

uri: string[](#resourcelink-uri)

The URI of this resource.

Inherited from [Resource](#resource).[uri](#resource-uri)

description?: string[](#resourcelink-description)

A description of what this resource represents.

This can be used by clients to improve the LLM’s understanding of available resources. It can be thought of like a “hint” to the model.

Inherited from [Resource](#resource).[description](#resource-description)

mimeType?: string[](#resourcelink-mimetype)

The MIME type of this resource, if known.

Inherited from [Resource](#resource).[mimeType](#resource-mimetype)

annotations?: Annotations[](#resourcelink-annotations)

Optional annotations for the client.

Inherited from [Resource](#resource).[annotations](#resource-annotations)

size?: number[](#resourcelink-size)

The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known.

This can be used by Hosts to display file sizes and estimate context window usage.

Inherited from [Resource](#resource).[size](#resource-size)

\_meta?: { \[key: string\]: unknown }[](#resourcelink-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Resource](#resource).[\_meta](#resource-_meta)

type: “resource_link”[](#resourcelink-type)

### 

[​](#textcontent)

`TextContent`

interface TextContent {\
  [type](#textcontent-type): “text”;\
  [text](#textcontent-text): string;\
  [annotations](#textcontent-annotations)?: [Annotations](#annotations);\
  [\_meta](#textcontent-_meta)?: { \[key: string\]: unknown };\
}

Text provided to or from an LLM.

type: “text”[](#textcontent-type)

text: string[](#textcontent-text)

The text content of the message.

annotations?: Annotations[](#textcontent-annotations)

Optional annotations for the client.

\_meta?: { \[key: string\]: unknown }[](#textcontent-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

### 

[​](#textresourcecontents)

`TextResourceContents`

interface TextResourceContents {\
  [uri](#textresourcecontents-uri): string;\
  [mimeType](#textresourcecontents-mimetype)?: string;\
  [\_meta](#textresourcecontents-_meta)?: { \[key: string\]: unknown };\
  [text](#textresourcecontents-text): string;\
}

uri: string[](#textresourcecontents-uri)

The URI of this resource.

Inherited from ResourceContents.uri

mimeType?: string[](#textresourcecontents-mimetype)

The MIME type of this resource, if known.

Inherited from ResourceContents.mimeType

\_meta?: { \[key: string\]: unknown }[](#textresourcecontents-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from ResourceContents.\_meta

text: string[](#textresourcecontents-text)

The text of the item. This must only be set if the item can actually be represented as text (not binary data).

## 

[​](#completion/complete)

`completion/complete`

### 

[​](#completerequest)

`CompleteRequest`

interface CompleteRequest {\
  [jsonrpc](#completerequest-jsonrpc): “2.0”;\
  [id](#completerequest-id): [RequestId](#requestid);\
  [method](#completerequest-method): “completion/complete”;\
  [params](#completerequest-params): [CompleteRequestParams](#completerequestparams);\
}

A request from the client to the server, to ask for completion options.

jsonrpc: “2.0”[](#completerequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#completerequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “completion/complete”[](#completerequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: CompleteRequestParams[](#completerequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#completerequestparams)

`CompleteRequestParams`

interface CompleteRequestParams {\
  [\_meta](#completerequestparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [ref](#completerequestparams-ref): [PromptReference](#promptreference) \| [ResourceTemplateReference](#resourcetemplatereference);\
  [argument](#completerequestparams-argument): { name: string; value: string };\
  [context](#completerequestparams-context)?: { arguments?: { \[key: string\]: string } };\
}

Parameters for a `completion/complete` request.

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#completerequestparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from RequestParams.\_meta

ref: PromptReference \| ResourceTemplateReference[](#completerequestparams-ref)

argument: { name: string; value: string }[](#completerequestparams-argument)

The argument’s information

Type Declaration

- name: string

  The name of the argument

- value: string

  The value of the argument to use for completion matching.

context?: { arguments?: { \[key: string\]: string } }[](#completerequestparams-context)

Additional, optional context for completions

Type Declaration

- `Optional`arguments?: { \[key: string\]: string }

  Previously-resolved variables in a URI template or prompt.

### 

[​](#completeresult)

`CompleteResult`

interface CompleteResult {\
  [\_meta](#completeresult-_meta)?: { \[key: string\]: unknown };\
  [completion](#completeresult-completion): { values: string\[\]; total?: number; hasMore?: boolean };\
  \[key: string\]: unknown;\
}

The server’s response to a completion/complete request

\_meta?: { \[key: string\]: unknown }[](#completeresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Result](#result).[\_meta](#result-_meta)

completion: { values: string\[\]; total?: number; hasMore?: boolean }[](#completeresult-completion)

Type Declaration

- values: string\[\]

  An array of completion values. Must not exceed 100 items.

- `Optional`total?: number

  The total number of completion options available. This can exceed the number of values actually sent in the response.

- `Optional`hasMore?: boolean

  Indicates whether there are additional completion options beyond those provided in the current response, even if the exact total is unknown.

### 

[​](#promptreference)

`PromptReference`

interface PromptReference {\
  [name](#promptreference-name): string;\
  [title](#promptreference-title)?: string;\
  [type](#promptreference-type): “ref/prompt”;\
}

Identifies a prompt.

name: string[](#promptreference-name)

Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn’t present).

Inherited from BaseMetadata.name

title?: string[](#promptreference-title)

Intended for UI and end-user contexts — optimized to be human-readable and easily understood, even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for Tool, where `annotations.title` should be given precedence over using `name`, if present).

Inherited from BaseMetadata.title

type: “ref/prompt”[](#promptreference-type)

### 

[​](#resourcetemplatereference)

`ResourceTemplateReference`

interface ResourceTemplateReference {\
  [type](#resourcetemplatereference-type): “ref/resource”;\
  [uri](#resourcetemplatereference-uri): string;\
}

A reference to a resource or resource template definition.

type: “ref/resource”[](#resourcetemplatereference-type)

uri: string[](#resourcetemplatereference-uri)

The URI or URI template of the resource.

## 

[​](#elicitation/create)

`elicitation/create`

### 

[​](#elicitrequest)

`ElicitRequest`

interface ElicitRequest {\
  [jsonrpc](#elicitrequest-jsonrpc): “2.0”;\
  [id](#elicitrequest-id): [RequestId](#requestid);\
  [method](#elicitrequest-method): “elicitation/create”;\
  [params](#elicitrequest-params): [ElicitRequestParams](#elicitrequestparams);\
}

A request from the server to elicit additional information from the user via the client.

jsonrpc: “2.0”[](#elicitrequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#elicitrequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “elicitation/create”[](#elicitrequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: ElicitRequestParams[](#elicitrequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#elicitrequestparams)

`ElicitRequestParams`

ElicitRequestParams: [ElicitRequestFormParams](#elicitrequestformparams) \| [ElicitRequestURLParams](#elicitrequesturlparams)

The parameters for a request to elicit additional information from the user via the client.

### 

[​](#elicitresult)

`ElicitResult`

interface ElicitResult {\
  [\_meta](#elicitresult-_meta)?: { \[key: string\]: unknown };\
  [action](#elicitresult-action): “accept” \| “decline” \| “cancel”;\
  [content](#elicitresult-content)?: { \[key: string\]: string \| number \| boolean \| string\[\] };\
  \[key: string\]: unknown;\
}

The client’s response to an elicitation request.

\_meta?: { \[key: string\]: unknown }[](#elicitresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Result](#result).[\_meta](#result-_meta)

action: “accept” \| “decline” \| “cancel”[](#elicitresult-action)

The user action in response to the elicitation.

- “accept”: User submitted the form/confirmed the action
- “decline”: User explicitly decline the action
- “cancel”: User dismissed without making an explicit choice

content?: { \[key: string\]: string \| number \| boolean \| string\[\] }[](#elicitresult-content)

The submitted form data, only present when action is “accept” and mode was “form”. Contains values matching the requested schema. Omitted for out-of-band mode responses.

### 

[​](#booleanschema)

`BooleanSchema`

interface BooleanSchema {\
  [type](#booleanschema-type): “boolean”;\
  [title](#booleanschema-title)?: string;\
  [description](#booleanschema-description)?: string;\
  [default](#booleanschema-default)?: boolean;\
}

type: “boolean”[](#booleanschema-type)

title?: string[](#booleanschema-title)

description?: string[](#booleanschema-description)

default?: boolean[](#booleanschema-default)

### 

[​](#elicitrequestformparams)

`ElicitRequestFormParams`

interface ElicitRequestFormParams {\
  [task](#elicitrequestformparams-task)?: [TaskMetadata](#taskmetadata);\
  [\_meta](#elicitrequestformparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [mode](#elicitrequestformparams-mode)?: “form”;\
  [message](#elicitrequestformparams-message): string;\
  [requestedSchema](#elicitrequestformparams-requestedschema): {\
    \$schema?: string;\
    type: “object”;\
    properties: { \[key: string\]: [PrimitiveSchemaDefinition](#primitiveschemadefinition) };\
    required?: string\[\];\
  };\
}

The parameters for a request to elicit non-sensitive information from the user via a form in the client.

task?: TaskMetadata[](#elicitrequestformparams-task)

If specified, the caller is requesting task-augmented execution for this request. The request will return a CreateTaskResult immediately, and the actual result can be retrieved later via tasks/result.

Task augmentation is subject to capability negotiation - receivers MUST declare support for task augmentation of specific request types in their capabilities.

Inherited from TaskAugmentedRequestParams.task

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#elicitrequestformparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from TaskAugmentedRequestParams.\_meta

mode?: “form”[](#elicitrequestformparams-mode)

The elicitation mode.

message: string[](#elicitrequestformparams-message)

The message to present to the user describing what information is being requested.

requestedSchema: { \$schema?: string; type: “object”; properties: { \[key: string\]: PrimitiveSchemaDefinition }; required?: string\[\]; }[](#elicitrequestformparams-requestedschema)

A restricted subset of JSON Schema. Only top-level properties are allowed, without nesting.

### 

[​](#elicitrequesturlparams)

`ElicitRequestURLParams`

interface ElicitRequestURLParams {\
  [task](#elicitrequesturlparams-task)?: [TaskMetadata](#taskmetadata);\
  [\_meta](#elicitrequesturlparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [mode](#elicitrequesturlparams-mode): “url”;\
  [message](#elicitrequesturlparams-message): string;\
  [elicitationId](#elicitrequesturlparams-elicitationid): string;\
  [url](#elicitrequesturlparams-url): string;\
}

The parameters for a request to elicit information from the user via a URL in the client.

task?: TaskMetadata[](#elicitrequesturlparams-task)

If specified, the caller is requesting task-augmented execution for this request. The request will return a CreateTaskResult immediately, and the actual result can be retrieved later via tasks/result.

Task augmentation is subject to capability negotiation - receivers MUST declare support for task augmentation of specific request types in their capabilities.

Inherited from TaskAugmentedRequestParams.task

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#elicitrequesturlparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from TaskAugmentedRequestParams.\_meta

mode: “url”[](#elicitrequesturlparams-mode)

The elicitation mode.

message: string[](#elicitrequesturlparams-message)

The message to present to the user explaining why the interaction is needed.

elicitationId: string[](#elicitrequesturlparams-elicitationid)

The ID of the elicitation, which must be unique within the context of the server. The client MUST treat this ID as an opaque value.

url: string[](#elicitrequesturlparams-url)

The URL that the user should navigate to.

### 

[​](#enumschema)

`EnumSchema`

EnumSchema:\
  \| [SingleSelectEnumSchema](#singleselectenumschema)\
  \| [MultiSelectEnumSchema](#multiselectenumschema)\
  \| [LegacyTitledEnumSchema](#legacytitledenumschema)

### 

[​](#legacytitledenumschema)

`LegacyTitledEnumSchema`

interface LegacyTitledEnumSchema {\
  [type](#legacytitledenumschema-type): “string”;\
  [title](#legacytitledenumschema-title)?: string;\
  [description](#legacytitledenumschema-description)?: string;\
  [enum](#legacytitledenumschema-enum): string\[\];\
  [enumNames](#legacytitledenumschema-enumnames)?: string\[\];\
  [default](#legacytitledenumschema-default)?: string;\
}

Use TitledSingleSelectEnumSchema instead. This interface will be removed in a future version.

type: “string”[](#legacytitledenumschema-type)

title?: string[](#legacytitledenumschema-title)

description?: string[](#legacytitledenumschema-description)

enum: string\[\][](#legacytitledenumschema-enum)

enumNames?: string\[\][](#legacytitledenumschema-enumnames)

(Legacy) Display names for enum values. Non-standard according to JSON schema 2020-12.

default?: string[](#legacytitledenumschema-default)

### 

[​](#multiselectenumschema)

`MultiSelectEnumSchema`

MultiSelectEnumSchema:\
  \| [UntitledMultiSelectEnumSchema](#untitledmultiselectenumschema)\
  \| [TitledMultiSelectEnumSchema](#titledmultiselectenumschema)

### 

[​](#numberschema)

`NumberSchema`

interface NumberSchema {\
  [type](#numberschema-type): “number” \| “integer”;\
  [title](#numberschema-title)?: string;\
  [description](#numberschema-description)?: string;\
  [minimum](#numberschema-minimum)?: number;\
  [maximum](#numberschema-maximum)?: number;\
  [default](#numberschema-default)?: number;\
}

type: “number” \| “integer”[](#numberschema-type)

title?: string[](#numberschema-title)

description?: string[](#numberschema-description)

minimum?: number[](#numberschema-minimum)

maximum?: number[](#numberschema-maximum)

default?: number[](#numberschema-default)

### 

[​](#primitiveschemadefinition)

`PrimitiveSchemaDefinition`

PrimitiveSchemaDefinition:\
  \| [StringSchema](#stringschema)\
  \| [NumberSchema](#numberschema)\
  \| [BooleanSchema](#booleanschema)\
  \| [EnumSchema](#enumschema)

Restricted schema definitions that only allow primitive types without nested objects or arrays.

### 

[​](#singleselectenumschema)

`SingleSelectEnumSchema`

SingleSelectEnumSchema:\
  \| [UntitledSingleSelectEnumSchema](#untitledsingleselectenumschema)\
  \| [TitledSingleSelectEnumSchema](#titledsingleselectenumschema)

### 

[​](#stringschema)

`StringSchema`

interface StringSchema {\
  [type](#stringschema-type): “string”;\
  [title](#stringschema-title)?: string;\
  [description](#stringschema-description)?: string;\
  [minLength](#stringschema-minlength)?: number;\
  [maxLength](#stringschema-maxlength)?: number;\
  [format](#stringschema-format)?: “uri” \| “email” \| “date” \| “date-time”;\
  [default](#stringschema-default)?: string;\
}

type: “string”[](#stringschema-type)

title?: string[](#stringschema-title)

description?: string[](#stringschema-description)

minLength?: number[](#stringschema-minlength)

maxLength?: number[](#stringschema-maxlength)

format?: “uri” \| “email” \| “date” \| “date-time”[](#stringschema-format)

default?: string[](#stringschema-default)

### 

[​](#titledmultiselectenumschema)

`TitledMultiSelectEnumSchema`

interface TitledMultiSelectEnumSchema {\
  [type](#titledmultiselectenumschema-type): “array”;\
  [title](#titledmultiselectenumschema-title)?: string;\
  [description](#titledmultiselectenumschema-description)?: string;\
  [minItems](#titledmultiselectenumschema-minitems)?: number;\
  [maxItems](#titledmultiselectenumschema-maxitems)?: number;\
  [items](#titledmultiselectenumschema-items): { anyOf: { const: string; title: string }\[\] };\
  [default](#titledmultiselectenumschema-default)?: string\[\];\
}

Schema for multiple-selection enumeration with display titles for each option.

type: “array”[](#titledmultiselectenumschema-type)

title?: string[](#titledmultiselectenumschema-title)

Optional title for the enum field.

description?: string[](#titledmultiselectenumschema-description)

Optional description for the enum field.

minItems?: number[](#titledmultiselectenumschema-minitems)

Minimum number of items to select.

maxItems?: number[](#titledmultiselectenumschema-maxitems)

Maximum number of items to select.

items: { anyOf: { const: string; title: string }\[\] }[](#titledmultiselectenumschema-items)

Schema for array items with enum options and display labels.

Type Declaration

- anyOf: { const: string; title: string }\[\]

  Array of enum options with values and display labels.

default?: string\[\][](#titledmultiselectenumschema-default)

Optional default value.

### 

[​](#titledsingleselectenumschema)

`TitledSingleSelectEnumSchema`

interface TitledSingleSelectEnumSchema {\
  [type](#titledsingleselectenumschema-type): “string”;\
  [title](#titledsingleselectenumschema-title)?: string;\
  [description](#titledsingleselectenumschema-description)?: string;\
  [oneOf](#titledsingleselectenumschema-oneof): { const: string; title: string }\[\];\
  [default](#titledsingleselectenumschema-default)?: string;\
}

Schema for single-selection enumeration with display titles for each option.

type: “string”[](#titledsingleselectenumschema-type)

title?: string[](#titledsingleselectenumschema-title)

Optional title for the enum field.

description?: string[](#titledsingleselectenumschema-description)

Optional description for the enum field.

oneOf: { const: string; title: string }\[\][](#titledsingleselectenumschema-oneof)

Array of enum options with values and display labels.

Type Declaration

- const: string

  The enum value.

- title: string

  Display label for this option.

default?: string[](#titledsingleselectenumschema-default)

Optional default value.

### 

[​](#untitledmultiselectenumschema)

`UntitledMultiSelectEnumSchema`

interface UntitledMultiSelectEnumSchema {\
  [type](#untitledmultiselectenumschema-type): “array”;\
  [title](#untitledmultiselectenumschema-title)?: string;\
  [description](#untitledmultiselectenumschema-description)?: string;\
  [minItems](#untitledmultiselectenumschema-minitems)?: number;\
  [maxItems](#untitledmultiselectenumschema-maxitems)?: number;\
  [items](#untitledmultiselectenumschema-items): { type: “string”; enum: string\[\] };\
  [default](#untitledmultiselectenumschema-default)?: string\[\];\
}

Schema for multiple-selection enumeration without display titles for options.

type: “array”[](#untitledmultiselectenumschema-type)

title?: string[](#untitledmultiselectenumschema-title)

Optional title for the enum field.

description?: string[](#untitledmultiselectenumschema-description)

Optional description for the enum field.

minItems?: number[](#untitledmultiselectenumschema-minitems)

Minimum number of items to select.

maxItems?: number[](#untitledmultiselectenumschema-maxitems)

Maximum number of items to select.

items: { type: “string”; enum: string\[\] }[](#untitledmultiselectenumschema-items)

Schema for the array items.

Type Declaration

- type: “string”

- enum: string\[\]

  Array of enum values to choose from.

default?: string\[\][](#untitledmultiselectenumschema-default)

Optional default value.

### 

[​](#untitledsingleselectenumschema)

`UntitledSingleSelectEnumSchema`

interface UntitledSingleSelectEnumSchema {\
  [type](#untitledsingleselectenumschema-type): “string”;\
  [title](#untitledsingleselectenumschema-title)?: string;\
  [description](#untitledsingleselectenumschema-description)?: string;\
  [enum](#untitledsingleselectenumschema-enum): string\[\];\
  [default](#untitledsingleselectenumschema-default)?: string;\
}

Schema for single-selection enumeration without display titles for options.

type: “string”[](#untitledsingleselectenumschema-type)

title?: string[](#untitledsingleselectenumschema-title)

Optional title for the enum field.

description?: string[](#untitledsingleselectenumschema-description)

Optional description for the enum field.

enum: string\[\][](#untitledsingleselectenumschema-enum)

Array of enum values to choose from.

default?: string[](#untitledsingleselectenumschema-default)

Optional default value.

## 

[​](#initialize)

`initialize`

### 

[​](#initializerequest)

`InitializeRequest`

interface InitializeRequest {\
  [jsonrpc](#initializerequest-jsonrpc): “2.0”;\
  [id](#initializerequest-id): [RequestId](#requestid);\
  [method](#initializerequest-method): “initialize”;\
  [params](#initializerequest-params): [InitializeRequestParams](#initializerequestparams);\
}

This request is sent from the client to the server when it first connects, asking it to begin initialization.

jsonrpc: “2.0”[](#initializerequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#initializerequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “initialize”[](#initializerequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: InitializeRequestParams[](#initializerequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#initializerequestparams)

`InitializeRequestParams`

interface InitializeRequestParams {\
  [\_meta](#initializerequestparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [protocolVersion](#initializerequestparams-protocolversion): string;\
  [capabilities](#initializerequestparams-capabilities): [ClientCapabilities](#clientcapabilities);\
  [clientInfo](#initializerequestparams-clientinfo): [Implementation](#implementation);\
}

Parameters for an `initialize` request.

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#initializerequestparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from RequestParams.\_meta

protocolVersion: string[](#initializerequestparams-protocolversion)

The latest version of the Model Context Protocol that the client supports. The client MAY decide to support older versions as well.

capabilities: ClientCapabilities[](#initializerequestparams-capabilities)

clientInfo: Implementation[](#initializerequestparams-clientinfo)

### 

[​](#initializeresult)

`InitializeResult`

interface InitializeResult {\
  [\_meta](#initializeresult-_meta)?: { \[key: string\]: unknown };\
  [protocolVersion](#initializeresult-protocolversion): string;\
  [capabilities](#initializeresult-capabilities): [ServerCapabilities](#servercapabilities);\
  [serverInfo](#initializeresult-serverinfo): [Implementation](#implementation);\
  [instructions](#initializeresult-instructions)?: string;\
  \[key: string\]: unknown;\
}

After receiving an initialize request from the client, the server sends this response.

\_meta?: { \[key: string\]: unknown }[](#initializeresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Result](#result).[\_meta](#result-_meta)

protocolVersion: string[](#initializeresult-protocolversion)

The version of the Model Context Protocol that the server wants to use. This may not match the version that the client requested. If the client cannot support this version, it MUST disconnect.

capabilities: ServerCapabilities[](#initializeresult-capabilities)

serverInfo: Implementation[](#initializeresult-serverinfo)

instructions?: string[](#initializeresult-instructions)

Instructions describing how to use the server and its features.

This can be used by clients to improve the LLM’s understanding of available tools, resources, etc. It can be thought of like a “hint” to the model. For example, this information MAY be added to the system prompt.

### 

[​](#clientcapabilities)

`ClientCapabilities`

interface ClientCapabilities {\
  [experimental](#clientcapabilities-experimental)?: { \[key: string\]: object };\
  [roots](#clientcapabilities-roots)?: { listChanged?: boolean };\
  [sampling](#clientcapabilities-sampling)?: { context?: object; tools?: object };\
  [elicitation](#clientcapabilities-elicitation)?: { form?: object; url?: object };\
  [tasks](#clientcapabilities-tasks)?: {\
    list?: object;\
    cancel?: object;\
    requests?: {\
      sampling?: { createMessage?: object };\
      elicitation?: { create?: object };\
    };\
  };\
}

Capabilities a client may support. Known capabilities are defined here, in this schema, but this is not a closed set: any client can define its own, additional capabilities.

experimental?: { \[key: string\]: object }[](#clientcapabilities-experimental)

Experimental, non-standard capabilities that the client supports.

roots?: { listChanged?: boolean }[](#clientcapabilities-roots)

Present if the client supports listing roots.

Type Declaration

- `Optional`listChanged?: boolean

  Whether the client supports notifications for changes to the roots list.

sampling?: { context?: object; tools?: object }[](#clientcapabilities-sampling)

Present if the client supports sampling from an LLM.

Type Declaration

- `Optional`context?: object

  Whether the client supports context inclusion via includeContext parameter. If not declared, servers SHOULD only use `includeContext: “none”` (or omit it).

- `Optional`tools?: object

  Whether the client supports tool use via tools and toolChoice parameters.

elicitation?: { form?: object; url?: object }[](#clientcapabilities-elicitation)

Present if the client supports elicitation from the server.

tasks?: { list?: object; cancel?: object; requests?: { sampling?: { createMessage?: object }; elicitation?: { create?: object }; }; }[](#clientcapabilities-tasks)

Present if the client supports task-augmented requests.

Type Declaration

- `Optional`list?: object

  Whether this client supports tasks/list.

- `Optional`cancel?: object

  Whether this client supports tasks/cancel.

- `Optional`requests?: { sampling?: { createMessage?: object }; elicitation?: { create?: object } }

  Specifies which request types can be augmented with tasks.

  - `Optional`sampling?: { createMessage?: object }

    Task support for sampling-related requests.

    - `Optional`createMessage?: object

      Whether the client supports task-augmented sampling/createMessage requests.

  - `Optional`elicitation?: { create?: object }

    Task support for elicitation-related requests.

    - `Optional`create?: object

      Whether the client supports task-augmented elicitation/create requests.

### 

[​](#implementation)

`Implementation`

interface Implementation {\
  [icons](#implementation-icons)?: [Icon](#icon)\[\];\
  [name](#implementation-name): string;\
  [title](#implementation-title)?: string;\
  [version](#implementation-version): string;\
  [description](#implementation-description)?: string;\
  [websiteUrl](#implementation-websiteurl)?: string;\
}

Describes the MCP implementation.

icons?: Icon\[\][](#implementation-icons)

Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:

- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:

- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)

Inherited from Icons.icons

name: string[](#implementation-name)

Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn’t present).

Inherited from BaseMetadata.name

title?: string[](#implementation-title)

Intended for UI and end-user contexts — optimized to be human-readable and easily understood, even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for Tool, where `annotations.title` should be given precedence over using `name`, if present).

Inherited from BaseMetadata.title

version: string[](#implementation-version)

description?: string[](#implementation-description)

An optional human-readable description of what this implementation does.

This can be used by clients or servers to provide context about their purpose and capabilities. For example, a server might describe the types of resources or tools it provides, while a client might describe its intended use case.

websiteUrl?: string[](#implementation-websiteurl)

An optional URL of the website for this implementation.

### 

[​](#servercapabilities)

`ServerCapabilities`

interface ServerCapabilities {\
  [experimental](#servercapabilities-experimental)?: { \[key: string\]: object };\
  [logging](#servercapabilities-logging)?: object;\
  [completions](#servercapabilities-completions)?: object;\
  [prompts](#servercapabilities-prompts)?: { listChanged?: boolean };\
  [resources](#servercapabilities-resources)?: { subscribe?: boolean; listChanged?: boolean };\
  [tools](#servercapabilities-tools)?: { listChanged?: boolean };\
  [tasks](#servercapabilities-tasks)?: {\
    list?: object;\
    cancel?: object;\
    requests?: { tools?: { call?: object } };\
  };\
}

Capabilities that a server may support. Known capabilities are defined here, in this schema, but this is not a closed set: any server can define its own, additional capabilities.

experimental?: { \[key: string\]: object }[](#servercapabilities-experimental)

Experimental, non-standard capabilities that the server supports.

logging?: object[](#servercapabilities-logging)

Present if the server supports sending log messages to the client.

completions?: object[](#servercapabilities-completions)

Present if the server supports argument autocompletion suggestions.

prompts?: { listChanged?: boolean }[](#servercapabilities-prompts)

Present if the server offers any prompt templates.

Type Declaration

- `Optional`listChanged?: boolean

  Whether this server supports notifications for changes to the prompt list.

resources?: { subscribe?: boolean; listChanged?: boolean }[](#servercapabilities-resources)

Present if the server offers any resources to read.

Type Declaration

- `Optional`subscribe?: boolean

  Whether this server supports subscribing to resource updates.

- `Optional`listChanged?: boolean

  Whether this server supports notifications for changes to the resource list.

tools?: { listChanged?: boolean }[](#servercapabilities-tools)

Present if the server offers any tools to call.

Type Declaration

- `Optional`listChanged?: boolean

  Whether this server supports notifications for changes to the tool list.

tasks?: { list?: object; cancel?: object; requests?: { tools?: { call?: object } }; }[](#servercapabilities-tasks)

Present if the server supports task-augmented requests.

Type Declaration

- `Optional`list?: object

  Whether this server supports tasks/list.

- `Optional`cancel?: object

  Whether this server supports tasks/cancel.

- `Optional`requests?: { tools?: { call?: object } }

  Specifies which request types can be augmented with tasks.

  - `Optional`tools?: { call?: object }

    Task support for tool-related requests.

    - `Optional`call?: object

      Whether the server supports task-augmented tools/call requests.

## 

[​](#logging/setlevel)

`logging/setLevel`

### 

[​](#setlevelrequest)

`SetLevelRequest`

interface SetLevelRequest {\
  [jsonrpc](#setlevelrequest-jsonrpc): “2.0”;\
  [id](#setlevelrequest-id): [RequestId](#requestid);\
  [method](#setlevelrequest-method): “logging/setLevel”;\
  [params](#setlevelrequest-params): [SetLevelRequestParams](#setlevelrequestparams);\
}

A request from the client to the server, to enable or adjust logging.

jsonrpc: “2.0”[](#setlevelrequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#setlevelrequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “logging/setLevel”[](#setlevelrequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: SetLevelRequestParams[](#setlevelrequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#setlevelrequestparams)

`SetLevelRequestParams`

interface SetLevelRequestParams {\
  [\_meta](#setlevelrequestparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [level](#setlevelrequestparams-level): [LoggingLevel](#logginglevel);\
}

Parameters for a `logging/setLevel` request.

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#setlevelrequestparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from RequestParams.\_meta

level: LoggingLevel[](#setlevelrequestparams-level)

The level of logging that the client wants to receive from the server. The server should send all logs at this level and higher (i.e., more severe) to the client as notifications/message.

## 

[​](#notifications/cancelled)

`notifications/cancelled`

### 

[​](#cancellednotification)

`CancelledNotification`

interface CancelledNotification {\
  [jsonrpc](#cancellednotification-jsonrpc): “2.0”;\
  [method](#cancellednotification-method): “notifications/cancelled”;\
  [params](#cancellednotification-params): [CancelledNotificationParams](#cancellednotificationparams);\
}

This notification can be sent by either side to indicate that it is cancelling a previously-issued request.

The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished.

This notification indicates that the result will be unused, so any associated processing SHOULD cease.

A client MUST NOT attempt to cancel its `initialize` request.

For task cancellation, use the `tasks/cancel` request instead of this notification.

jsonrpc: “2.0”[](#cancellednotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/cancelled”[](#cancellednotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params: CancelledNotificationParams[](#cancellednotification-params)

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

### 

[​](#cancellednotificationparams)

`CancelledNotificationParams`

interface CancelledNotificationParams {\
  [\_meta](#cancellednotificationparams-_meta)?: { \[key: string\]: unknown };\
  [requestId](#cancellednotificationparams-requestid)?: [RequestId](#requestid);\
  [reason](#cancellednotificationparams-reason)?: string;\
}

Parameters for a `notifications/cancelled` notification.

\_meta?: { \[key: string\]: unknown }[](#cancellednotificationparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from NotificationParams.\_meta

requestId?: RequestId[](#cancellednotificationparams-requestid)

The ID of the request to cancel.

This MUST correspond to the ID of a request previously issued in the same direction. This MUST be provided for cancelling non-task requests. This MUST NOT be used for cancelling tasks (use the `tasks/cancel` request instead).

reason?: string[](#cancellednotificationparams-reason)

An optional string describing the reason for the cancellation. This MAY be logged or presented to the user.

## 

[​](#notifications/initialized)

`notifications/initialized`

### 

[​](#initializednotification)

`InitializedNotification`

interface InitializedNotification {\
  [jsonrpc](#initializednotification-jsonrpc): “2.0”;\
  [method](#initializednotification-method): “notifications/initialized”;\
  [params](#initializednotification-params)?: NotificationParams;\
}

This notification is sent from the client to the server after initialization has finished.

jsonrpc: “2.0”[](#initializednotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/initialized”[](#initializednotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params?: NotificationParams[](#initializednotification-params)

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## 

[​](#notifications/tasks/status)

`notifications/tasks/status`

### 

[​](#taskstatusnotification)

`TaskStatusNotification`

interface TaskStatusNotification {\
  [jsonrpc](#taskstatusnotification-jsonrpc): “2.0”;\
  [method](#taskstatusnotification-method): “notifications/tasks/status”;\
  [params](#taskstatusnotification-params): [TaskStatusNotificationParams](#taskstatusnotificationparams);\
}

An optional notification from the receiver to the requestor, informing them that a task’s status has changed. Receivers are not required to send these notifications.

jsonrpc: “2.0”[](#taskstatusnotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/tasks/status”[](#taskstatusnotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params: TaskStatusNotificationParams[](#taskstatusnotification-params)

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

### 

[​](#taskstatusnotificationparams)

`TaskStatusNotificationParams`

TaskStatusNotificationParams: NotificationParams & [Task](#task)

Parameters for a `notifications/tasks/status` notification.

## 

[​](#notifications/message)

`notifications/message`

### 

[​](#loggingmessagenotification)

`LoggingMessageNotification`

interface LoggingMessageNotification {\
  [jsonrpc](#loggingmessagenotification-jsonrpc): “2.0”;\
  [method](#loggingmessagenotification-method): “notifications/message”;\
  [params](#loggingmessagenotification-params): [LoggingMessageNotificationParams](#loggingmessagenotificationparams);\
}

JSONRPCNotification of a log message passed from server to client. If no logging/setLevel request has been sent from the client, the server MAY decide which messages to send automatically.

jsonrpc: “2.0”[](#loggingmessagenotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/message”[](#loggingmessagenotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params: LoggingMessageNotificationParams[](#loggingmessagenotification-params)

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

### 

[​](#loggingmessagenotificationparams)

`LoggingMessageNotificationParams`

interface LoggingMessageNotificationParams {\
  [\_meta](#loggingmessagenotificationparams-_meta)?: { \[key: string\]: unknown };\
  [level](#loggingmessagenotificationparams-level): [LoggingLevel](#logginglevel);\
  [logger](#loggingmessagenotificationparams-logger)?: string;\
  [data](#loggingmessagenotificationparams-data): unknown;\
}

Parameters for a `notifications/message` notification.

\_meta?: { \[key: string\]: unknown }[](#loggingmessagenotificationparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from NotificationParams.\_meta

level: LoggingLevel[](#loggingmessagenotificationparams-level)

The severity of this log message.

logger?: string[](#loggingmessagenotificationparams-logger)

An optional name of the logger issuing this message.

data: unknown[](#loggingmessagenotificationparams-data)

The data to be logged, such as a string message or an object. Any JSON serializable type is allowed here.

## 

[​](#notifications/progress)

`notifications/progress`

### 

[​](#progressnotification)

`ProgressNotification`

interface ProgressNotification {\
  [jsonrpc](#progressnotification-jsonrpc): “2.0”;\
  [method](#progressnotification-method): “notifications/progress”;\
  [params](#progressnotification-params): [ProgressNotificationParams](#progressnotificationparams);\
}

An out-of-band notification used to inform the receiver of a progress update for a long-running request.

jsonrpc: “2.0”[](#progressnotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/progress”[](#progressnotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params: ProgressNotificationParams[](#progressnotification-params)

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

### 

[​](#progressnotificationparams)

`ProgressNotificationParams`

interface ProgressNotificationParams {\
  [\_meta](#progressnotificationparams-_meta)?: { \[key: string\]: unknown };\
  [progressToken](#progressnotificationparams-progresstoken): [ProgressToken](#progresstoken);\
  [progress](#progressnotificationparams-progress): number;\
  [total](#progressnotificationparams-total)?: number;\
  [message](#progressnotificationparams-message)?: string;\
}

Parameters for a `notifications/progress` notification.

\_meta?: { \[key: string\]: unknown }[](#progressnotificationparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from NotificationParams.\_meta

progressToken: ProgressToken[](#progressnotificationparams-progresstoken)

The progress token which was given in the initial request, used to associate this notification with the request that is proceeding.

progress: number[](#progressnotificationparams-progress)

The progress thus far. This should increase every time progress is made, even if the total is unknown.

total?: number[](#progressnotificationparams-total)

Total number of items to process (or total progress required), if known.

message?: string[](#progressnotificationparams-message)

An optional message describing the current progress.

## 

[​](#notifications/prompts/list_changed)

`notifications/prompts/list_changed`

### 

[​](#promptlistchangednotification)

`PromptListChangedNotification`

interface PromptListChangedNotification {\
  [jsonrpc](#promptlistchangednotification-jsonrpc): “2.0”;\
  [method](#promptlistchangednotification-method): “notifications/prompts/list_changed”;\
  [params](#promptlistchangednotification-params)?: NotificationParams;\
}

An optional notification from the server to the client, informing it that the list of prompts it offers has changed. This may be issued by servers without any previous subscription from the client.

jsonrpc: “2.0”[](#promptlistchangednotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/prompts/list_changed”[](#promptlistchangednotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params?: NotificationParams[](#promptlistchangednotification-params)

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## 

[​](#notifications/resources/list_changed)

`notifications/resources/list_changed`

### 

[​](#resourcelistchangednotification)

`ResourceListChangedNotification`

interface ResourceListChangedNotification {\
  [jsonrpc](#resourcelistchangednotification-jsonrpc): “2.0”;\
  [method](#resourcelistchangednotification-method): “notifications/resources/list_changed”;\
  [params](#resourcelistchangednotification-params)?: NotificationParams;\
}

An optional notification from the server to the client, informing it that the list of resources it can read from has changed. This may be issued by servers without any previous subscription from the client.

jsonrpc: “2.0”[](#resourcelistchangednotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/resources/list_changed”[](#resourcelistchangednotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params?: NotificationParams[](#resourcelistchangednotification-params)

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## 

[​](#notifications/resources/updated)

`notifications/resources/updated`

### 

[​](#resourceupdatednotification)

`ResourceUpdatedNotification`

interface ResourceUpdatedNotification {\
  [jsonrpc](#resourceupdatednotification-jsonrpc): “2.0”;\
  [method](#resourceupdatednotification-method): “notifications/resources/updated”;\
  [params](#resourceupdatednotification-params): [ResourceUpdatedNotificationParams](#resourceupdatednotificationparams);\
}

A notification from the server to the client, informing it that a resource has changed and may need to be read again. This should only be sent if the client previously sent a resources/subscribe request.

jsonrpc: “2.0”[](#resourceupdatednotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/resources/updated”[](#resourceupdatednotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params: ResourceUpdatedNotificationParams[](#resourceupdatednotification-params)

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

### 

[​](#resourceupdatednotificationparams)

`ResourceUpdatedNotificationParams`

interface ResourceUpdatedNotificationParams {\
  [\_meta](#resourceupdatednotificationparams-_meta)?: { \[key: string\]: unknown };\
  [uri](#resourceupdatednotificationparams-uri): string;\
}

Parameters for a `notifications/resources/updated` notification.

\_meta?: { \[key: string\]: unknown }[](#resourceupdatednotificationparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from NotificationParams.\_meta

uri: string[](#resourceupdatednotificationparams-uri)

The URI of the resource that has been updated. This might be a sub-resource of the one that the client actually subscribed to.

## 

[​](#notifications/roots/list_changed)

`notifications/roots/list_changed`

### 

[​](#rootslistchangednotification)

`RootsListChangedNotification`

interface RootsListChangedNotification {\
  [jsonrpc](#rootslistchangednotification-jsonrpc): “2.0”;\
  [method](#rootslistchangednotification-method): “notifications/roots/list_changed”;\
  [params](#rootslistchangednotification-params)?: NotificationParams;\
}

A notification from the client to the server, informing it that the list of roots has changed. This notification should be sent whenever the client adds, removes, or modifies any root. The server should then request an updated list of roots using the ListRootsRequest.

jsonrpc: “2.0”[](#rootslistchangednotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/roots/list_changed”[](#rootslistchangednotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params?: NotificationParams[](#rootslistchangednotification-params)

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## 

[​](#notifications/tools/list_changed)

`notifications/tools/list_changed`

### 

[​](#toollistchangednotification)

`ToolListChangedNotification`

interface ToolListChangedNotification {\
  [jsonrpc](#toollistchangednotification-jsonrpc): “2.0”;\
  [method](#toollistchangednotification-method): “notifications/tools/list_changed”;\
  [params](#toollistchangednotification-params)?: NotificationParams;\
}

An optional notification from the server to the client, informing it that the list of tools it offers has changed. This may be issued by servers without any previous subscription from the client.

jsonrpc: “2.0”[](#toollistchangednotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/tools/list_changed”[](#toollistchangednotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params?: NotificationParams[](#toollistchangednotification-params)

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## 

[​](#notifications/elicitation/complete)

`notifications/elicitation/complete`

### 

[​](#elicitationcompletenotification)

`ElicitationCompleteNotification`

interface ElicitationCompleteNotification {\
  [jsonrpc](#elicitationcompletenotification-jsonrpc): “2.0”;\
  [method](#elicitationcompletenotification-method): “notifications/elicitation/complete”;\
  [params](#elicitationcompletenotification-params): { elicitationId: string };\
}

An optional notification from the server to the client, informing it of a completion of a out-of-band elicitation request.

jsonrpc: “2.0”[](#elicitationcompletenotification-jsonrpc)

Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc)

method: “notifications/elicitation/complete”[](#elicitationcompletenotification-method)

Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method)

params: { elicitationId: string }[](#elicitationcompletenotification-params)

Type Declaration

- elicitationId: string

  The ID of the elicitation that completed.

Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## 

[​](#ping)

`ping`

### 

[​](#pingrequest)

`PingRequest`

interface PingRequest {\
  [jsonrpc](#pingrequest-jsonrpc): “2.0”;\
  [id](#pingrequest-id): [RequestId](#requestid);\
  [method](#pingrequest-method): “ping”;\
  [params](#pingrequest-params)?: RequestParams;\
}

A ping, issued by either the server or the client, to check that the other party is still alive. The receiver must promptly respond, or else may be disconnected.

jsonrpc: “2.0”[](#pingrequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#pingrequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “ping”[](#pingrequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params?: RequestParams[](#pingrequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

## 

[​](#tasks)

`tasks`

### 

[​](#createtaskresult)

`CreateTaskResult`

interface CreateTaskResult {\
  [\_meta](#createtaskresult-_meta)?: { \[key: string\]: unknown };\
  [task](#createtaskresult-task): [Task](#task);\
  \[key: string\]: unknown;\
}

A response to a task-augmented request.

\_meta?: { \[key: string\]: unknown }[](#createtaskresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Result](#result).[\_meta](#result-_meta)

task: Task[](#createtaskresult-task)

### 

[​](#relatedtaskmetadata)

`RelatedTaskMetadata`

interface RelatedTaskMetadata {\
  [taskId](#relatedtaskmetadata-taskid): string;\
}

Metadata for associating messages with a task. Include this in the `_meta` field under the key `io.modelcontextprotocol/related-task`.

taskId: string[](#relatedtaskmetadata-taskid)

The task identifier this message is associated with.

### 

[​](#task)

`Task`

interface Task {\
  [taskId](#task-taskid): string;\
  [status](#task-status): [TaskStatus](#taskstatus);\
  [statusMessage](#task-statusmessage)?: string;\
  [createdAt](#task-createdat): string;\
  [lastUpdatedAt](#task-lastupdatedat): string;\
  [ttl](#task-ttl): number \| null;\
  [pollInterval](#task-pollinterval)?: number;\
}

Data associated with a task.

taskId: string[](#task-taskid)

The task identifier.

status: TaskStatus[](#task-status)

Current task state.

statusMessage?: string[](#task-statusmessage)

Optional human-readable message describing the current task state. This can provide context for any status, including:

- Reasons for “cancelled” status
- Summaries for “completed” status
- Diagnostic information for “failed” status (e.g., error details, what went wrong)

createdAt: string[](#task-createdat)

ISO 8601 timestamp when the task was created.

lastUpdatedAt: string[](#task-lastupdatedat)

ISO 8601 timestamp when the task was last updated.

ttl: number \| null[](#task-ttl)

Actual retention duration from creation in milliseconds, null for unlimited.

pollInterval?: number[](#task-pollinterval)

Suggested polling interval in milliseconds.

### 

[​](#taskmetadata)

`TaskMetadata`

interface TaskMetadata {\
  [ttl](#taskmetadata-ttl)?: number;\
}

Metadata for augmenting a request with task execution. Include this in the `task` field of the request parameters.

ttl?: number[](#taskmetadata-ttl)

Requested duration in milliseconds to retain task from creation.

### 

[​](#taskstatus)

`TaskStatus`

TaskStatus: “working” \| “input_required” \| “completed” \| “failed” \| “cancelled”

The status of a task.

## 

[​](#tasks/get)

`tasks/get`

### 

[​](#gettaskrequest)

`GetTaskRequest`

interface GetTaskRequest {\
  [jsonrpc](#gettaskrequest-jsonrpc): “2.0”;\
  [id](#gettaskrequest-id): [RequestId](#requestid);\
  [method](#gettaskrequest-method): “tasks/get”;\
  [params](#gettaskrequest-params): { taskId: string };\
}

A request to retrieve the state of a task.

jsonrpc: “2.0”[](#gettaskrequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#gettaskrequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “tasks/get”[](#gettaskrequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: { taskId: string }[](#gettaskrequest-params)

Type Declaration

- taskId: string

  The task identifier to query.

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#gettaskresult)

`GetTaskResult`

GetTaskResult: [Result](#result) & [Task](#task)

The response to a tasks/get request.

## 

[​](#tasks/result)

`tasks/result`

### 

[​](#gettaskpayloadrequest)

`GetTaskPayloadRequest`

interface GetTaskPayloadRequest {\
  [jsonrpc](#gettaskpayloadrequest-jsonrpc): “2.0”;\
  [id](#gettaskpayloadrequest-id): [RequestId](#requestid);\
  [method](#gettaskpayloadrequest-method): “tasks/result”;\
  [params](#gettaskpayloadrequest-params): { taskId: string };\
}

A request to retrieve the result of a completed task.

jsonrpc: “2.0”[](#gettaskpayloadrequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#gettaskpayloadrequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “tasks/result”[](#gettaskpayloadrequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: { taskId: string }[](#gettaskpayloadrequest-params)

Type Declaration

- taskId: string

  The task identifier to retrieve results for.

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#gettaskpayloadresult)

`GetTaskPayloadResult`

interface GetTaskPayloadResult {\
  [\_meta](#gettaskpayloadresult-_meta)?: { \[key: string\]: unknown };\
  \[key: string\]: unknown;\
}

The response to a tasks/result request. The structure matches the result type of the original request. For example, a tools/call task would return the CallToolResult structure.

\_meta?: { \[key: string\]: unknown }[](#gettaskpayloadresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Result](#result).[\_meta](#result-_meta)

## 

[​](#tasks/list)

`tasks/list`

### 

[​](#listtasksrequest)

`ListTasksRequest`

interface ListTasksRequest {\
  [jsonrpc](#listtasksrequest-jsonrpc): “2.0”;\
  [id](#listtasksrequest-id): [RequestId](#requestid);\
  [params](#listtasksrequest-params)?: PaginatedRequestParams;\
  [method](#listtasksrequest-method): “tasks/list”;\
}

A request to retrieve a list of tasks.

jsonrpc: “2.0”[](#listtasksrequest-jsonrpc)

Inherited from PaginatedRequest.jsonrpc

id: RequestId[](#listtasksrequest-id)

Inherited from PaginatedRequest.id

params?: PaginatedRequestParams[](#listtasksrequest-params)

Inherited from PaginatedRequest.params

method: “tasks/list”[](#listtasksrequest-method)

Overrides PaginatedRequest.method

### 

[​](#listtasksresult)

`ListTasksResult`

interface ListTasksResult {\
  [\_meta](#listtasksresult-_meta)?: { \[key: string\]: unknown };\
  [nextCursor](#listtasksresult-nextcursor)?: string;\
  [tasks](#listtasksresult-tasks): [Task](#task)\[\];\
  \[key: string\]: unknown;\
}

The response to a tasks/list request.

\_meta?: { \[key: string\]: unknown }[](#listtasksresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from PaginatedResult.\_meta

nextCursor?: string[](#listtasksresult-nextcursor)

An opaque token representing the pagination position after the last returned result. If present, there may be more results available.

Inherited from PaginatedResult.nextCursor

tasks: Task\[\][](#listtasksresult-tasks)

## 

[​](#tasks/cancel)

`tasks/cancel`

### 

[​](#canceltaskrequest)

`CancelTaskRequest`

interface CancelTaskRequest {\
  [jsonrpc](#canceltaskrequest-jsonrpc): “2.0”;\
  [id](#canceltaskrequest-id): [RequestId](#requestid);\
  [method](#canceltaskrequest-method): “tasks/cancel”;\
  [params](#canceltaskrequest-params): { taskId: string };\
}

A request to cancel a task.

jsonrpc: “2.0”[](#canceltaskrequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#canceltaskrequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “tasks/cancel”[](#canceltaskrequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: { taskId: string }[](#canceltaskrequest-params)

Type Declaration

- taskId: string

  The task identifier to cancel.

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#canceltaskresult)

`CancelTaskResult`

CancelTaskResult: [Result](#result) & [Task](#task)

The response to a tasks/cancel request.

## 

[​](#prompts/get)

`prompts/get`

### 

[​](#getpromptrequest)

`GetPromptRequest`

interface GetPromptRequest {\
  [jsonrpc](#getpromptrequest-jsonrpc): “2.0”;\
  [id](#getpromptrequest-id): [RequestId](#requestid);\
  [method](#getpromptrequest-method): “prompts/get”;\
  [params](#getpromptrequest-params): [GetPromptRequestParams](#getpromptrequestparams);\
}

Used by the client to get a prompt provided by the server.

jsonrpc: “2.0”[](#getpromptrequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#getpromptrequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “prompts/get”[](#getpromptrequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: GetPromptRequestParams[](#getpromptrequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#getpromptrequestparams)

`GetPromptRequestParams`

interface GetPromptRequestParams {\
  [\_meta](#getpromptrequestparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [name](#getpromptrequestparams-name): string;\
  [arguments](#getpromptrequestparams-arguments)?: { \[key: string\]: string };\
}

Parameters for a `prompts/get` request.

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#getpromptrequestparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from RequestParams.\_meta

name: string[](#getpromptrequestparams-name)

The name of the prompt or prompt template.

arguments?: { \[key: string\]: string }[](#getpromptrequestparams-arguments)

Arguments to use for templating the prompt.

### 

[​](#getpromptresult)

`GetPromptResult`

interface GetPromptResult {\
  [\_meta](#getpromptresult-_meta)?: { \[key: string\]: unknown };\
  [description](#getpromptresult-description)?: string;\
  [messages](#getpromptresult-messages): [PromptMessage](#promptmessage)\[\];\
  \[key: string\]: unknown;\
}

The server’s response to a prompts/get request from the client.

\_meta?: { \[key: string\]: unknown }[](#getpromptresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Result](#result).[\_meta](#result-_meta)

description?: string[](#getpromptresult-description)

An optional description for the prompt.

messages: PromptMessage\[\][](#getpromptresult-messages)

### 

[​](#promptmessage)

`PromptMessage`

interface PromptMessage {\
  [role](#promptmessage-role): [Role](#role);\
  [content](#promptmessage-content): [ContentBlock](#contentblock);\
}

Describes a message returned as part of a prompt.

This is similar to `SamplingMessage`, but also supports the embedding of resources from the MCP server.

role: Role[](#promptmessage-role)

content: ContentBlock[](#promptmessage-content)

## 

[​](#prompts/list)

`prompts/list`

### 

[​](#listpromptsrequest)

`ListPromptsRequest`

interface ListPromptsRequest {\
  [jsonrpc](#listpromptsrequest-jsonrpc): “2.0”;\
  [id](#listpromptsrequest-id): [RequestId](#requestid);\
  [params](#listpromptsrequest-params)?: PaginatedRequestParams;\
  [method](#listpromptsrequest-method): “prompts/list”;\
}

Sent from the client to request a list of prompts and prompt templates the server has.

jsonrpc: “2.0”[](#listpromptsrequest-jsonrpc)

Inherited from PaginatedRequest.jsonrpc

id: RequestId[](#listpromptsrequest-id)

Inherited from PaginatedRequest.id

params?: PaginatedRequestParams[](#listpromptsrequest-params)

Inherited from PaginatedRequest.params

method: “prompts/list”[](#listpromptsrequest-method)

Overrides PaginatedRequest.method

### 

[​](#listpromptsresult)

`ListPromptsResult`

interface ListPromptsResult {\
  [\_meta](#listpromptsresult-_meta)?: { \[key: string\]: unknown };\
  [nextCursor](#listpromptsresult-nextcursor)?: string;\
  [prompts](#listpromptsresult-prompts): [Prompt](#prompt)\[\];\
  \[key: string\]: unknown;\
}

The server’s response to a prompts/list request from the client.

\_meta?: { \[key: string\]: unknown }[](#listpromptsresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from PaginatedResult.\_meta

nextCursor?: string[](#listpromptsresult-nextcursor)

An opaque token representing the pagination position after the last returned result. If present, there may be more results available.

Inherited from PaginatedResult.nextCursor

prompts: Prompt\[\][](#listpromptsresult-prompts)

### 

[​](#prompt)

`Prompt`

interface Prompt {\
  [icons](#prompt-icons)?: [Icon](#icon)\[\];\
  [name](#prompt-name): string;\
  [title](#prompt-title)?: string;\
  [description](#prompt-description)?: string;\
  [arguments](#prompt-arguments)?: [PromptArgument](#promptargument)\[\];\
  [\_meta](#prompt-_meta)?: { \[key: string\]: unknown };\
}

A prompt or prompt template that the server offers.

icons?: Icon\[\][](#prompt-icons)

Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:

- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:

- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)

Inherited from Icons.icons

name: string[](#prompt-name)

Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn’t present).

Inherited from BaseMetadata.name

title?: string[](#prompt-title)

Intended for UI and end-user contexts — optimized to be human-readable and easily understood, even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for Tool, where `annotations.title` should be given precedence over using `name`, if present).

Inherited from BaseMetadata.title

description?: string[](#prompt-description)

An optional description of what this prompt provides

arguments?: PromptArgument\[\][](#prompt-arguments)

A list of arguments to use for templating the prompt.

\_meta?: { \[key: string\]: unknown }[](#prompt-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

### 

[​](#promptargument)

`PromptArgument`

interface PromptArgument {\
  [name](#promptargument-name): string;\
  [title](#promptargument-title)?: string;\
  [description](#promptargument-description)?: string;\
  [required](#promptargument-required)?: boolean;\
}

Describes an argument that a prompt can accept.

name: string[](#promptargument-name)

Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn’t present).

Inherited from BaseMetadata.name

title?: string[](#promptargument-title)

Intended for UI and end-user contexts — optimized to be human-readable and easily understood, even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for Tool, where `annotations.title` should be given precedence over using `name`, if present).

Inherited from BaseMetadata.title

description?: string[](#promptargument-description)

A human-readable description of the argument.

required?: boolean[](#promptargument-required)

Whether this argument must be provided.

## 

[​](#resources/list)

`resources/list`

### 

[​](#listresourcesrequest)

`ListResourcesRequest`

interface ListResourcesRequest {\
  [jsonrpc](#listresourcesrequest-jsonrpc): “2.0”;\
  [id](#listresourcesrequest-id): [RequestId](#requestid);\
  [params](#listresourcesrequest-params)?: PaginatedRequestParams;\
  [method](#listresourcesrequest-method): “resources/list”;\
}

Sent from the client to request a list of resources the server has.

jsonrpc: “2.0”[](#listresourcesrequest-jsonrpc)

Inherited from PaginatedRequest.jsonrpc

id: RequestId[](#listresourcesrequest-id)

Inherited from PaginatedRequest.id

params?: PaginatedRequestParams[](#listresourcesrequest-params)

Inherited from PaginatedRequest.params

method: “resources/list”[](#listresourcesrequest-method)

Overrides PaginatedRequest.method

### 

[​](#listresourcesresult)

`ListResourcesResult`

interface ListResourcesResult {\
  [\_meta](#listresourcesresult-_meta)?: { \[key: string\]: unknown };\
  [nextCursor](#listresourcesresult-nextcursor)?: string;\
  [resources](#listresourcesresult-resources): [Resource](#resource)\[\];\
  \[key: string\]: unknown;\
}

The server’s response to a resources/list request from the client.

\_meta?: { \[key: string\]: unknown }[](#listresourcesresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from PaginatedResult.\_meta

nextCursor?: string[](#listresourcesresult-nextcursor)

An opaque token representing the pagination position after the last returned result. If present, there may be more results available.

Inherited from PaginatedResult.nextCursor

resources: Resource\[\][](#listresourcesresult-resources)

### 

[​](#resource)

`Resource`

interface Resource {\
  [icons](#resource-icons)?: [Icon](#icon)\[\];\
  [name](#resource-name): string;\
  [title](#resource-title)?: string;\
  [uri](#resource-uri): string;\
  [description](#resource-description)?: string;\
  [mimeType](#resource-mimetype)?: string;\
  [annotations](#resource-annotations)?: [Annotations](#annotations);\
  [size](#resource-size)?: number;\
  [\_meta](#resource-_meta)?: { \[key: string\]: unknown };\
}

A known resource that the server is capable of reading.

icons?: Icon\[\][](#resource-icons)

Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:

- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:

- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)

Inherited from Icons.icons

name: string[](#resource-name)

Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn’t present).

Inherited from BaseMetadata.name

title?: string[](#resource-title)

Intended for UI and end-user contexts — optimized to be human-readable and easily understood, even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for Tool, where `annotations.title` should be given precedence over using `name`, if present).

Inherited from BaseMetadata.title

uri: string[](#resource-uri)

The URI of this resource.

description?: string[](#resource-description)

A description of what this resource represents.

This can be used by clients to improve the LLM’s understanding of available resources. It can be thought of like a “hint” to the model.

mimeType?: string[](#resource-mimetype)

The MIME type of this resource, if known.

annotations?: Annotations[](#resource-annotations)

Optional annotations for the client.

size?: number[](#resource-size)

The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known.

This can be used by Hosts to display file sizes and estimate context window usage.

\_meta?: { \[key: string\]: unknown }[](#resource-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

## 

[​](#resources/read)

`resources/read`

### 

[​](#readresourcerequest)

`ReadResourceRequest`

interface ReadResourceRequest {\
  [jsonrpc](#readresourcerequest-jsonrpc): “2.0”;\
  [id](#readresourcerequest-id): [RequestId](#requestid);\
  [method](#readresourcerequest-method): “resources/read”;\
  [params](#readresourcerequest-params): [ReadResourceRequestParams](#readresourcerequestparams);\
}

Sent from the client to the server, to read a specific resource URI.

jsonrpc: “2.0”[](#readresourcerequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#readresourcerequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “resources/read”[](#readresourcerequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: ReadResourceRequestParams[](#readresourcerequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#readresourcerequestparams)

`ReadResourceRequestParams`

interface ReadResourceRequestParams {\
  [\_meta](#readresourcerequestparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [uri](#readresourcerequestparams-uri): string;\
}

Parameters for a `resources/read` request.

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#readresourcerequestparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from ResourceRequestParams.\_meta

uri: string[](#readresourcerequestparams-uri)

The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.

Inherited from ResourceRequestParams.uri

### 

[​](#readresourceresult)

`ReadResourceResult`

interface ReadResourceResult {\
  [\_meta](#readresourceresult-_meta)?: { \[key: string\]: unknown };\
  [contents](#readresourceresult-contents): ([TextResourceContents](#textresourcecontents) \| [BlobResourceContents](#blobresourcecontents))\[\];\
  \[key: string\]: unknown;\
}

The server’s response to a resources/read request from the client.

\_meta?: { \[key: string\]: unknown }[](#readresourceresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Result](#result).[\_meta](#result-_meta)

contents: (TextResourceContents \| BlobResourceContents)\[\][](#readresourceresult-contents)

## 

[​](#resources/subscribe)

`resources/subscribe`

### 

[​](#subscriberequest)

`SubscribeRequest`

interface SubscribeRequest {\
  [jsonrpc](#subscriberequest-jsonrpc): “2.0”;\
  [id](#subscriberequest-id): [RequestId](#requestid);\
  [method](#subscriberequest-method): “resources/subscribe”;\
  [params](#subscriberequest-params): [SubscribeRequestParams](#subscriberequestparams);\
}

Sent from the client to request resources/updated notifications from the server whenever a particular resource changes.

jsonrpc: “2.0”[](#subscriberequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#subscriberequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “resources/subscribe”[](#subscriberequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: SubscribeRequestParams[](#subscriberequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#subscriberequestparams)

`SubscribeRequestParams`

interface SubscribeRequestParams {\
  [\_meta](#subscriberequestparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [uri](#subscriberequestparams-uri): string;\
}

Parameters for a `resources/subscribe` request.

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#subscriberequestparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from ResourceRequestParams.\_meta

uri: string[](#subscriberequestparams-uri)

The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.

Inherited from ResourceRequestParams.uri

## 

[​](#resources/templates/list)

`resources/templates/list`

### 

[​](#listresourcetemplatesrequest)

`ListResourceTemplatesRequest`

interface ListResourceTemplatesRequest {\
  [jsonrpc](#listresourcetemplatesrequest-jsonrpc): “2.0”;\
  [id](#listresourcetemplatesrequest-id): [RequestId](#requestid);\
  [params](#listresourcetemplatesrequest-params)?: PaginatedRequestParams;\
  [method](#listresourcetemplatesrequest-method): “resources/templates/list”;\
}

Sent from the client to request a list of resource templates the server has.

jsonrpc: “2.0”[](#listresourcetemplatesrequest-jsonrpc)

Inherited from PaginatedRequest.jsonrpc

id: RequestId[](#listresourcetemplatesrequest-id)

Inherited from PaginatedRequest.id

params?: PaginatedRequestParams[](#listresourcetemplatesrequest-params)

Inherited from PaginatedRequest.params

method: “resources/templates/list”[](#listresourcetemplatesrequest-method)

Overrides PaginatedRequest.method

### 

[​](#listresourcetemplatesresult)

`ListResourceTemplatesResult`

interface ListResourceTemplatesResult {\
  [\_meta](#listresourcetemplatesresult-_meta)?: { \[key: string\]: unknown };\
  [nextCursor](#listresourcetemplatesresult-nextcursor)?: string;\
  [resourceTemplates](#listresourcetemplatesresult-resourcetemplates): [ResourceTemplate](#resourcetemplate)\[\];\
  \[key: string\]: unknown;\
}

The server’s response to a resources/templates/list request from the client.

\_meta?: { \[key: string\]: unknown }[](#listresourcetemplatesresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from PaginatedResult.\_meta

nextCursor?: string[](#listresourcetemplatesresult-nextcursor)

An opaque token representing the pagination position after the last returned result. If present, there may be more results available.

Inherited from PaginatedResult.nextCursor

resourceTemplates: ResourceTemplate\[\][](#listresourcetemplatesresult-resourcetemplates)

### 

[​](#resourcetemplate)

`ResourceTemplate`

interface ResourceTemplate {\
  [icons](#resourcetemplate-icons)?: [Icon](#icon)\[\];\
  [name](#resourcetemplate-name): string;\
  [title](#resourcetemplate-title)?: string;\
  [uriTemplate](#resourcetemplate-uritemplate): string;\
  [description](#resourcetemplate-description)?: string;\
  [mimeType](#resourcetemplate-mimetype)?: string;\
  [annotations](#resourcetemplate-annotations)?: [Annotations](#annotations);\
  [\_meta](#resourcetemplate-_meta)?: { \[key: string\]: unknown };\
}

A template description for resources available on the server.

icons?: Icon\[\][](#resourcetemplate-icons)

Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:

- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:

- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)

Inherited from Icons.icons

name: string[](#resourcetemplate-name)

Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn’t present).

Inherited from BaseMetadata.name

title?: string[](#resourcetemplate-title)

Intended for UI and end-user contexts — optimized to be human-readable and easily understood, even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for Tool, where `annotations.title` should be given precedence over using `name`, if present).

Inherited from BaseMetadata.title

uriTemplate: string[](#resourcetemplate-uritemplate)

A URI template (according to RFC 6570) that can be used to construct resource URIs.

description?: string[](#resourcetemplate-description)

A description of what this template is for.

This can be used by clients to improve the LLM’s understanding of available resources. It can be thought of like a “hint” to the model.

mimeType?: string[](#resourcetemplate-mimetype)

The MIME type for all resources that match this template. This should only be included if all resources matching this template have the same type.

annotations?: Annotations[](#resourcetemplate-annotations)

Optional annotations for the client.

\_meta?: { \[key: string\]: unknown }[](#resourcetemplate-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

## 

[​](#resources/unsubscribe)

`resources/unsubscribe`

### 

[​](#unsubscriberequest)

`UnsubscribeRequest`

interface UnsubscribeRequest {\
  [jsonrpc](#unsubscriberequest-jsonrpc): “2.0”;\
  [id](#unsubscriberequest-id): [RequestId](#requestid);\
  [method](#unsubscriberequest-method): “resources/unsubscribe”;\
  [params](#unsubscriberequest-params): [UnsubscribeRequestParams](#unsubscriberequestparams);\
}

Sent from the client to request cancellation of resources/updated notifications from the server. This should follow a previous resources/subscribe request.

jsonrpc: “2.0”[](#unsubscriberequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#unsubscriberequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “resources/unsubscribe”[](#unsubscriberequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: UnsubscribeRequestParams[](#unsubscriberequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#unsubscriberequestparams)

`UnsubscribeRequestParams`

interface UnsubscribeRequestParams {\
  [\_meta](#unsubscriberequestparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [uri](#unsubscriberequestparams-uri): string;\
}

Parameters for a `resources/unsubscribe` request.

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#unsubscriberequestparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from ResourceRequestParams.\_meta

uri: string[](#unsubscriberequestparams-uri)

The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.

Inherited from ResourceRequestParams.uri

## 

[​](#roots/list)

`roots/list`

### 

[​](#listrootsrequest)

`ListRootsRequest`

interface ListRootsRequest {\
  [jsonrpc](#listrootsrequest-jsonrpc): “2.0”;\
  [id](#listrootsrequest-id): [RequestId](#requestid);\
  [method](#listrootsrequest-method): “roots/list”;\
  [params](#listrootsrequest-params)?: RequestParams;\
}

Sent from the server to request a list of root URIs from the client. Roots allow servers to ask for specific directories or files to operate on. A common example for roots is providing a set of repositories or directories a server should operate on.

This request is typically used when the server needs to understand the file system structure or access specific locations that the client has permission to read from.

jsonrpc: “2.0”[](#listrootsrequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#listrootsrequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “roots/list”[](#listrootsrequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params?: RequestParams[](#listrootsrequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#listrootsresult)

`ListRootsResult`

interface ListRootsResult {\
  [\_meta](#listrootsresult-_meta)?: { \[key: string\]: unknown };\
  [roots](#listrootsresult-roots): [Root](#root)\[\];\
  \[key: string\]: unknown;\
}

The client’s response to a roots/list request from the server. This result contains an array of Root objects, each representing a root directory or file that the server can operate on.

\_meta?: { \[key: string\]: unknown }[](#listrootsresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Result](#result).[\_meta](#result-_meta)

roots: Root\[\][](#listrootsresult-roots)

### 

[​](#root)

`Root`

interface Root {\
  [uri](#root-uri): string;\
  [name](#root-name)?: string;\
  [\_meta](#root-_meta)?: { \[key: string\]: unknown };\
}

Represents a root directory or file that the server can operate on.

uri: string[](#root-uri)

The URI identifying the root. This *must* start with file:// for now. This restriction may be relaxed in future versions of the protocol to allow other URI schemes.

name?: string[](#root-name)

An optional name for the root. This can be used to provide a human-readable identifier for the root, which may be useful for display purposes or for referencing the root in other parts of the application.

\_meta?: { \[key: string\]: unknown }[](#root-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

## 

[​](#sampling/createmessage)

`sampling/createMessage`

### 

[​](#createmessagerequest)

`CreateMessageRequest`

interface CreateMessageRequest {\
  [jsonrpc](#createmessagerequest-jsonrpc): “2.0”;\
  [id](#createmessagerequest-id): [RequestId](#requestid);\
  [method](#createmessagerequest-method): “sampling/createMessage”;\
  [params](#createmessagerequest-params): [CreateMessageRequestParams](#createmessagerequestparams);\
}

A request from the server to sample an LLM via the client. The client has full discretion over which model to select. The client should also inform the user before beginning sampling, to allow them to inspect the request (human in the loop) and decide whether to approve it.

jsonrpc: “2.0”[](#createmessagerequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#createmessagerequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “sampling/createMessage”[](#createmessagerequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: CreateMessageRequestParams[](#createmessagerequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#createmessagerequestparams)

`CreateMessageRequestParams`

interface CreateMessageRequestParams {\
  [task](#createmessagerequestparams-task)?: [TaskMetadata](#taskmetadata);\
  [\_meta](#createmessagerequestparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [messages](#createmessagerequestparams-messages): [SamplingMessage](#samplingmessage)\[\];\
  [modelPreferences](#createmessagerequestparams-modelpreferences)?: [ModelPreferences](#modelpreferences);\
  [systemPrompt](#createmessagerequestparams-systemprompt)?: string;\
  [includeContext](#createmessagerequestparams-includecontext)?: “none” \| “thisServer” \| “allServers”;\
  [temperature](#createmessagerequestparams-temperature)?: number;\
  [maxTokens](#createmessagerequestparams-maxtokens): number;\
  [stopSequences](#createmessagerequestparams-stopsequences)?: string\[\];\
  [metadata](#createmessagerequestparams-metadata)?: object;\
  [tools](#createmessagerequestparams-tools)?: [Tool](#tool)\[\];\
  [toolChoice](#createmessagerequestparams-toolchoice)?: [ToolChoice](#toolchoice);\
}

Parameters for a `sampling/createMessage` request.

task?: TaskMetadata[](#createmessagerequestparams-task)

If specified, the caller is requesting task-augmented execution for this request. The request will return a CreateTaskResult immediately, and the actual result can be retrieved later via tasks/result.

Task augmentation is subject to capability negotiation - receivers MUST declare support for task augmentation of specific request types in their capabilities.

Inherited from TaskAugmentedRequestParams.task

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#createmessagerequestparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from TaskAugmentedRequestParams.\_meta

messages: SamplingMessage\[\][](#createmessagerequestparams-messages)

modelPreferences?: ModelPreferences[](#createmessagerequestparams-modelpreferences)

The server’s preferences for which model to select. The client MAY ignore these preferences.

systemPrompt?: string[](#createmessagerequestparams-systemprompt)

An optional system prompt the server wants to use for sampling. The client MAY modify or omit this prompt.

includeContext?: “none” \| “thisServer” \| “allServers”[](#createmessagerequestparams-includecontext)

A request to include context from one or more MCP servers (including the caller), to be attached to the prompt. The client MAY ignore this request.

Default is “none”. Values “thisServer” and “allServers” are soft-deprecated. Servers SHOULD only use these values if the client declares ClientCapabilities.sampling.context. These values may be removed in future spec releases.

temperature?: number[](#createmessagerequestparams-temperature)

maxTokens: number[](#createmessagerequestparams-maxtokens)

The requested maximum number of tokens to sample (to prevent runaway completions).

The client MAY choose to sample fewer tokens than the requested maximum.

stopSequences?: string\[\][](#createmessagerequestparams-stopsequences)

metadata?: object[](#createmessagerequestparams-metadata)

Optional metadata to pass through to the LLM provider. The format of this metadata is provider-specific.

tools?: Tool\[\][](#createmessagerequestparams-tools)

Tools that the model may use during generation. The client MUST return an error if this field is provided but ClientCapabilities.sampling.tools is not declared.

toolChoice?: ToolChoice[](#createmessagerequestparams-toolchoice)

Controls how the model uses tools. The client MUST return an error if this field is provided but ClientCapabilities.sampling.tools is not declared. Default is `{ mode: “auto” }`.

### 

[​](#createmessageresult)

`CreateMessageResult`

interface CreateMessageResult {\
  [\_meta](#createmessageresult-_meta)?: { \[key: string\]: unknown };\
  [model](#createmessageresult-model): string;\
  [stopReason](#createmessageresult-stopreason)?: string;\
  [role](#createmessageresult-role): [Role](#role);\
  [content](#createmessageresult-content): [SamplingMessageContentBlock](#samplingmessagecontentblock) \| [SamplingMessageContentBlock](#samplingmessagecontentblock)\[\];\
  \[key: string\]: unknown;\
}

The client’s response to a sampling/createMessage request from the server. The client should inform the user before returning the sampled message, to allow them to inspect the response (human in the loop) and decide whether to allow the server to see it.

\_meta?: { \[key: string\]: unknown }[](#createmessageresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Result](#result).[\_meta](#result-_meta)

model: string[](#createmessageresult-model)

The name of the model that generated the message.

stopReason?: string[](#createmessageresult-stopreason)

The reason why sampling stopped, if known.

Standard values:

- “endTurn”: Natural end of the assistant’s turn
- “stopSequence”: A stop sequence was encountered
- “maxTokens”: Maximum token limit was reached
- “toolUse”: The model wants to use one or more tools

This field is an open string to allow for provider-specific stop reasons.

role: Role[](#createmessageresult-role)

Inherited from [SamplingMessage](#samplingmessage).[role](#samplingmessage-role)

content: SamplingMessageContentBlock \| SamplingMessageContentBlock\[\][](#createmessageresult-content)

Inherited from [SamplingMessage](#samplingmessage).[content](#samplingmessage-content)

### 

[​](#modelhint)

`ModelHint`

interface ModelHint {\
  [name](#modelhint-name)?: string;\
}

Hints to use for model selection.

Keys not declared here are currently left unspecified by the spec and are up to the client to interpret.

name?: string[](#modelhint-name)

A hint for a model name.

The client SHOULD treat this as a substring of a model name; for example:

- `claude-3-5-sonnet` should match `claude-3-5-sonnet-20241022`
- `sonnet` should match `claude-3-5-sonnet-20241022`, `claude-3-sonnet-20240229`, etc.
- `claude` should match any Claude model

The client MAY also map the string to a different provider’s model name or a different model family, as long as it fills a similar niche; for example:

- `gemini-1.5-flash` could match `claude-3-haiku-20240307`

### 

[​](#modelpreferences)

`ModelPreferences`

interface ModelPreferences {\
  [hints](#modelpreferences-hints)?: [ModelHint](#modelhint)\[\];\
  [costPriority](#modelpreferences-costpriority)?: number;\
  [speedPriority](#modelpreferences-speedpriority)?: number;\
  [intelligencePriority](#modelpreferences-intelligencepriority)?: number;\
}

The server’s preferences for model selection, requested of the client during sampling.

Because LLMs can vary along multiple dimensions, choosing the “best” model is rarely straightforward. Different models excel in different areas—some are faster but less capable, others are more capable but more expensive, and so on. This interface allows servers to express their priorities across multiple dimensions to help clients make an appropriate selection for their use case.

These preferences are always advisory. The client MAY ignore them. It is also up to the client to decide how to interpret these preferences and how to balance them against other considerations.

hints?: ModelHint\[\][](#modelpreferences-hints)

Optional hints to use for model selection.

If multiple hints are specified, the client MUST evaluate them in order (such that the first match is taken).

The client SHOULD prioritize these hints over the numeric priorities, but MAY still use the priorities to select from ambiguous matches.

costPriority?: number[](#modelpreferences-costpriority)

How much to prioritize cost when selecting a model. A value of 0 means cost is not important, while a value of 1 means cost is the most important factor.

speedPriority?: number[](#modelpreferences-speedpriority)

How much to prioritize sampling speed (latency) when selecting a model. A value of 0 means speed is not important, while a value of 1 means speed is the most important factor.

intelligencePriority?: number[](#modelpreferences-intelligencepriority)

How much to prioritize intelligence and capabilities when selecting a model. A value of 0 means intelligence is not important, while a value of 1 means intelligence is the most important factor.

### 

[​](#samplingmessage)

`SamplingMessage`

interface SamplingMessage {\
  [role](#samplingmessage-role): [Role](#role);\
  [content](#samplingmessage-content): [SamplingMessageContentBlock](#samplingmessagecontentblock) \| [SamplingMessageContentBlock](#samplingmessagecontentblock)\[\];\
  [\_meta](#samplingmessage-_meta)?: { \[key: string\]: unknown };\
}

Describes a message issued to or received from an LLM API.

role: Role[](#samplingmessage-role)

content: SamplingMessageContentBlock \| SamplingMessageContentBlock\[\][](#samplingmessage-content)

\_meta?: { \[key: string\]: unknown }[](#samplingmessage-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

### 

[​](#samplingmessagecontentblock)

`SamplingMessageContentBlock`

SamplingMessageContentBlock:\
  \| [TextContent](#textcontent)\
  \| [ImageContent](#imagecontent)\
  \| [AudioContent](#audiocontent)\
  \| [ToolUseContent](#toolusecontent)\
  \| [ToolResultContent](#toolresultcontent)

### 

[​](#toolchoice)

`ToolChoice`

interface ToolChoice {\
  [mode](#toolchoice-mode)?: “none” \| “required” \| “auto”;\
}

Controls tool selection behavior for sampling requests.

mode?: “none” \| “required” \| “auto”[](#toolchoice-mode)

Controls the tool use ability of the model:

- “auto”: Model decides whether to use tools (default)
- “required”: Model MUST use at least one tool before completing
- “none”: Model MUST NOT use any tools

### 

[​](#toolresultcontent)

`ToolResultContent`

interface ToolResultContent {\
  [type](#toolresultcontent-type): “tool_result”;\
  [toolUseId](#toolresultcontent-tooluseid): string;\
  [content](#toolresultcontent-content): [ContentBlock](#contentblock)\[\];\
  [structuredContent](#toolresultcontent-structuredcontent)?: { \[key: string\]: unknown };\
  [isError](#toolresultcontent-iserror)?: boolean;\
  [\_meta](#toolresultcontent-_meta)?: { \[key: string\]: unknown };\
}

The result of a tool use, provided by the user back to the assistant.

type: “tool_result”[](#toolresultcontent-type)

toolUseId: string[](#toolresultcontent-tooluseid)

The ID of the tool use this result corresponds to.

This MUST match the ID from a previous ToolUseContent.

content: ContentBlock\[\][](#toolresultcontent-content)

The unstructured result content of the tool use.

This has the same format as CallToolResult.content and can include text, images, audio, resource links, and embedded resources.

structuredContent?: { \[key: string\]: unknown }[](#toolresultcontent-structuredcontent)

An optional structured result object.

If the tool defined an outputSchema, this SHOULD conform to that schema.

isError?: boolean[](#toolresultcontent-iserror)

Whether the tool use resulted in an error.

If true, the content typically describes the error that occurred. Default: false

\_meta?: { \[key: string\]: unknown }[](#toolresultcontent-_meta)

Optional metadata about the tool result. Clients SHOULD preserve this field when including tool results in subsequent sampling requests to enable caching optimizations.

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

### 

[​](#toolusecontent)

`ToolUseContent`

interface ToolUseContent {\
  [type](#toolusecontent-type): “tool_use”;\
  [id](#toolusecontent-id): string;\
  [name](#toolusecontent-name): string;\
  [input](#toolusecontent-input): { \[key: string\]: unknown };\
  [\_meta](#toolusecontent-_meta)?: { \[key: string\]: unknown };\
}

A request from the assistant to call a tool.

type: “tool_use”[](#toolusecontent-type)

id: string[](#toolusecontent-id)

A unique identifier for this tool use.

This ID is used to match tool results to their corresponding tool uses.

name: string[](#toolusecontent-name)

The name of the tool to call.

input: { \[key: string\]: unknown }[](#toolusecontent-input)

The arguments to pass to the tool, conforming to the tool’s input schema.

\_meta?: { \[key: string\]: unknown }[](#toolusecontent-_meta)

Optional metadata about the tool use. Clients SHOULD preserve this field when including tool uses in subsequent sampling requests to enable caching optimizations.

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

## 

[​](#tools/call)

`tools/call`

### 

[​](#calltoolrequest)

`CallToolRequest`

interface CallToolRequest {\
  [jsonrpc](#calltoolrequest-jsonrpc): “2.0”;\
  [id](#calltoolrequest-id): [RequestId](#requestid);\
  [method](#calltoolrequest-method): “tools/call”;\
  [params](#calltoolrequest-params): [CallToolRequestParams](#calltoolrequestparams);\
}

Used by the client to invoke a tool provided by the server.

jsonrpc: “2.0”[](#calltoolrequest-jsonrpc)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc)

id: RequestId[](#calltoolrequest-id)

Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id)

method: “tools/call”[](#calltoolrequest-method)

Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method)

params: CallToolRequestParams[](#calltoolrequest-params)

Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### 

[​](#calltoolrequestparams)

`CallToolRequestParams`

interface CallToolRequestParams {\
  [task](#calltoolrequestparams-task)?: [TaskMetadata](#taskmetadata);\
  [\_meta](#calltoolrequestparams-_meta)?: { progressToken?: [ProgressToken](#progresstoken); \[key: string\]: unknown };\
  [name](#calltoolrequestparams-name): string;\
  [arguments](#calltoolrequestparams-arguments)?: { \[key: string\]: unknown };\
}

Parameters for a `tools/call` request.

task?: TaskMetadata[](#calltoolrequestparams-task)

If specified, the caller is requesting task-augmented execution for this request. The request will return a CreateTaskResult immediately, and the actual result can be retrieved later via tasks/result.

Task augmentation is subject to capability negotiation - receivers MUST declare support for task augmentation of specific request types in their capabilities.

Inherited from TaskAugmentedRequestParams.task

\_meta?: { progressToken?: ProgressToken; \[key: string\]: unknown }[](#calltoolrequestparams-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Type Declaration

- \[key: string\]: unknown

- `Optional`progressToken?: [ProgressToken](#progresstoken)

  If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications.

Inherited from TaskAugmentedRequestParams.\_meta

name: string[](#calltoolrequestparams-name)

The name of the tool.

arguments?: { \[key: string\]: unknown }[](#calltoolrequestparams-arguments)

Arguments to use for the tool call.

### 

[​](#calltoolresult)

`CallToolResult`

interface CallToolResult {\
  [\_meta](#calltoolresult-_meta)?: { \[key: string\]: unknown };\
  [content](#calltoolresult-content): [ContentBlock](#contentblock)\[\];\
  [structuredContent](#calltoolresult-structuredcontent)?: { \[key: string\]: unknown };\
  [isError](#calltoolresult-iserror)?: boolean;\
  \[key: string\]: unknown;\
}

The server’s response to a tool call.

\_meta?: { \[key: string\]: unknown }[](#calltoolresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from [Result](#result).[\_meta](#result-_meta)

content: ContentBlock\[\][](#calltoolresult-content)

A list of content objects that represent the unstructured result of the tool call.

structuredContent?: { \[key: string\]: unknown }[](#calltoolresult-structuredcontent)

An optional JSON object that represents the structured result of the tool call.

isError?: boolean[](#calltoolresult-iserror)

Whether the tool call ended in an error.

If not set, this is assumed to be false (the call was successful).

Any errors that originate from the tool SHOULD be reported inside the result object, with `isError` set to true, *not* as an MCP protocol-level error response. Otherwise, the LLM would not be able to see that an error occurred and self-correct.

However, any errors in *finding* the tool, an error indicating that the server does not support tool calls, or any other exceptional conditions, should be reported as an MCP error response.

## 

[​](#tools/list)

`tools/list`

### 

[​](#listtoolsrequest)

`ListToolsRequest`

interface ListToolsRequest {\
  [jsonrpc](#listtoolsrequest-jsonrpc): “2.0”;\
  [id](#listtoolsrequest-id): [RequestId](#requestid);\
  [params](#listtoolsrequest-params)?: PaginatedRequestParams;\
  [method](#listtoolsrequest-method): “tools/list”;\
}

Sent from the client to request a list of tools the server has.

jsonrpc: “2.0”[](#listtoolsrequest-jsonrpc)

Inherited from PaginatedRequest.jsonrpc

id: RequestId[](#listtoolsrequest-id)

Inherited from PaginatedRequest.id

params?: PaginatedRequestParams[](#listtoolsrequest-params)

Inherited from PaginatedRequest.params

method: “tools/list”[](#listtoolsrequest-method)

Overrides PaginatedRequest.method

### 

[​](#listtoolsresult)

`ListToolsResult`

interface ListToolsResult {\
  [\_meta](#listtoolsresult-_meta)?: { \[key: string\]: unknown };\
  [nextCursor](#listtoolsresult-nextcursor)?: string;\
  [tools](#listtoolsresult-tools): [Tool](#tool)\[\];\
  \[key: string\]: unknown;\
}

The server’s response to a tools/list request from the client.

\_meta?: { \[key: string\]: unknown }[](#listtoolsresult-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

Inherited from PaginatedResult.\_meta

nextCursor?: string[](#listtoolsresult-nextcursor)

An opaque token representing the pagination position after the last returned result. If present, there may be more results available.

Inherited from PaginatedResult.nextCursor

tools: Tool\[\][](#listtoolsresult-tools)

### 

[​](#tool)

`Tool`

interface Tool {\
  [icons](#tool-icons)?: [Icon](#icon)\[\];\
  [name](#tool-name): string;\
  [title](#tool-title)?: string;\
  [description](#tool-description)?: string;\
  [inputSchema](#tool-inputschema): {\
    \$schema?: string;\
    type: “object”;\
    properties?: { \[key: string\]: object };\
    required?: string\[\];\
  };\
  [execution](#tool-execution)?: [ToolExecution](#toolexecution);\
  [outputSchema](#tool-outputschema)?: {\
    \$schema?: string;\
    type: “object”;\
    properties?: { \[key: string\]: object };\
    required?: string\[\];\
  };\
  [annotations](#tool-annotations)?: [ToolAnnotations](#toolannotations);\
  [\_meta](#tool-_meta)?: { \[key: string\]: unknown };\
}

Definition for a tool the client can call.

icons?: Icon\[\][](#tool-icons)

Optional set of sized icons that the client can display in a user interface.

Clients that support rendering icons MUST support at least the following MIME types:

- `image/png` - PNG images (safe, universal compatibility)
- `image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)

Clients that support rendering icons SHOULD also support:

- `image/svg+xml` - SVG images (scalable but requires security precautions)
- `image/webp` - WebP images (modern, efficient format)

Inherited from Icons.icons

name: string[](#tool-name)

Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn’t present).

Inherited from BaseMetadata.name

title?: string[](#tool-title)

Intended for UI and end-user contexts — optimized to be human-readable and easily understood, even by those unfamiliar with domain-specific terminology.

If not provided, the name should be used for display (except for Tool, where `annotations.title` should be given precedence over using `name`, if present).

Inherited from BaseMetadata.title

description?: string[](#tool-description)

A human-readable description of the tool.

This can be used by clients to improve the LLM’s understanding of available tools. It can be thought of like a “hint” to the model.

inputSchema: { \$schema?: string; type: “object”; properties?: { \[key: string\]: object }; required?: string\[\]; }[](#tool-inputschema)

A JSON Schema object defining the expected parameters for the tool.

execution?: ToolExecution[](#tool-execution)

Execution-related properties for this tool.

outputSchema?: { \$schema?: string; type: “object”; properties?: { \[key: string\]: object }; required?: string\[\]; }[](#tool-outputschema)

An optional JSON Schema object defining the structure of the tool’s output returned in the structuredContent field of a CallToolResult.

Defaults to JSON Schema 2020-12 when no explicit \$schema is provided. Currently restricted to type: “object” at the root level.

annotations?: ToolAnnotations[](#tool-annotations)

Optional additional tool information.

Display name precedence order is: title, annotations.title, then name.

\_meta?: { \[key: string\]: unknown }[](#tool-_meta)

See [General fields: `_meta`](/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.

### 

[​](#toolannotations)

`ToolAnnotations`

interface ToolAnnotations {\
  [title](#toolannotations-title)?: string;\
  [readOnlyHint](#toolannotations-readonlyhint)?: boolean;\
  [destructiveHint](#toolannotations-destructivehint)?: boolean;\
  [idempotentHint](#toolannotations-idempotenthint)?: boolean;\
  [openWorldHint](#toolannotations-openworldhint)?: boolean;\
}

Additional properties describing a Tool to clients.

NOTE: all properties in ToolAnnotations are **hints**. They are not guaranteed to provide a faithful description of tool behavior (including descriptive properties like `title`).

Clients should never make tool use decisions based on ToolAnnotations received from untrusted servers.

title?: string[](#toolannotations-title)

A human-readable title for the tool.

readOnlyHint?: boolean[](#toolannotations-readonlyhint)

If true, the tool does not modify its environment.

Default: false

destructiveHint?: boolean[](#toolannotations-destructivehint)

If true, the tool may perform destructive updates to its environment. If false, the tool performs only additive updates.

(This property is meaningful only when `readOnlyHint == false`)

Default: true

idempotentHint?: boolean[](#toolannotations-idempotenthint)

If true, calling the tool repeatedly with the same arguments will have no additional effect on its environment.

(This property is meaningful only when `readOnlyHint == false`)

Default: false

openWorldHint?: boolean[](#toolannotations-openworldhint)

If true, this tool may interact with an “open world” of external entities. If false, the tool’s domain of interaction is closed. For example, the world of a web search tool is open, whereas that of a memory tool is not.

Default: true

### 

[​](#toolexecution)

`ToolExecution`

interface ToolExecution {\
  [taskSupport](#toolexecution-tasksupport)?: “forbidden” \| “optional” \| “required”;\
}

Execution-related properties for a tool.

taskSupport?: “forbidden” \| “optional” \| “required”[](#toolexecution-tasksupport)

Indicates whether this tool supports task-augmented execution. This allows clients to handle long-running operations through polling the task system.

- “forbidden”: Tool does not support task-augmented execution (default when absent)
- “optional”: Tool may support task-augmented execution
- “required”: Tool requires task-augmented execution

Default: “forbidden”
