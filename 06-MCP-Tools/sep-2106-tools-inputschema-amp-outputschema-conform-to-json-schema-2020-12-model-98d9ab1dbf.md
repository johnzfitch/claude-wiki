---
title: "SEP-2106: Tools `inputSchema` &amp; `outputSchema` Conform to JSON Schema 2020-12 - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/seps/2106-json-schema-2020-12"
category: "06-MCP-Tools"
fetched_at: "2026-08-02T05:37:02Z"
tags: ["mcp"]
---

## On this page

- [Abstract](#abstract)
- [Motivation](#motivation)
  - [Real-World Impact](#real-world-impact)
  - [Schema Composition Use Cases](#schema-composition-use-cases)
- [Specification](#specification)
  - [1. Loosen inputSchema](#1-loosen-inputschema)
  - [2. Loosen outputSchema](#2-loosen-outputschema)
  - [3. Loosen structuredContent](#3-loosen-structuredcontent)
  - [4. Documentation Updates](#4-documentation-updates)
  - [5. Examples](#5-examples)
  - [Tool returning an array of objects:](#tool-returning-an-array-of-objects)
  - [Tool with composition schema:](#tool-with-composition-schema)
- [Rationale](#rationale)
  - [Why not just allow arrays?](#why-not-just-allow-arrays)
  - [Why not require a wrapper object?](#why-not-require-a-wrapper-object)
  - [Real-World API Patterns](#real-world-api-patterns)
  - [Alignment with JSON Schema 2020-12](#alignment-with-json-schema-2020-12)
  - [SDK Ecosystem Evidence](#sdk-ecosystem-evidence)
  - [OpenAPI Precedent](#openapi-precedent)
- [Backward Compatibility](#backward-compatibility)
  - [Compatibility Matrix](#compatibility-matrix)
  - [TypeScript / SDK Migration](#typescript-%2F-sdk-migration)
  - [Migration Path](#migration-path)
- [Security Implications](#security-implications)
  - [\$ref Dereferencing (SSRF and Fetch-DoS)](#%24ref-dereferencing-ssrf-and-fetch-dos)
  - [Composition-Keyword Resource Use](#composition-keyword-resource-use)
- [Reference Implementation](#reference-implementation)
  - [TypeScript SDK](#typescript-sdk)
  - [Everything Server Demo Tools](#everything-server-demo-tools)
  - [Related Links](#related-links)
  - [Implementation Guidance](#implementation-guidance)
- [Acknowledgments](#acknowledgments)

Final

# SEP-2106: Tools \`inputSchema\` & \`outputSchema\` Conform to JSON Schema 2020-12

Copy pageCopy page

Tools `inputSchema` & `outputSchema` Conform to JSON Schema 2020-12

Copy pageCopy page

FinalStandards Track

This SEP has reached Final status and is preserved as a historical record of the design as accepted. Changes made to the protocol after finalization are not reflected here. Refer to the [current specification](/specification/latest) and its changelog for authoritative requirements.

| Field         | Value                                                                                                                                                                         |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SEP**       | 2106                                                                                                                                                                          |
| **Title**     | Tools `inputSchema` & `outputSchema` Conform to JSON Schema 2020-12                                                                                                           |
| **Status**    | Final                                                                                                                                                                         |
| **Type**      | Standards Track                                                                                                                                                               |
| **Created**   | 2026-01-06                                                                                                                                                                    |
| **Author(s)** | John McBride ([@jpmcb](https://github.com/jpmcb)) — original proposal; Ola Hungerford ([@olaservo](https://github.com/olaservo)) — current shepherd, post-SEP-1850 conversion |
| **Sponsor**   | Ola Hungerford ([@olaservo](https://github.com/olaservo))                                                                                                                     |
| **PR**        | [\#2106](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2106)                                                                                              |

------------------------------------------------------------------------


[​](#abstract)

Abstract

This SEP proposes loosening the restrictions on `inputSchema`, `outputSchema`, and `structuredContent` to better support JSON Schema 2020-12. Specifically:

- **`inputSchema`**: Keeps `type: "object"` required (since tool arguments are objects), but allows any additional JSON Schema properties to support powerful validation compositions (`anyOf`, `oneOf`, `allOf`, etc.)
- **`outputSchema`**: Fully supports JSON Schema 2020-12 since MCP servers may return any valid JSON
- **`structuredContent`**: Accepts any JSON value validated by `outputSchema`

This proposal enables MCP servers to leverage the expressiveness of JSON Schema 2020-12 while maintaining backward compatibility with existing implementations.


[​](#motivation)

Motivation

The current MCP specification restricts tool schemas in ways that conflict with full JSON Schema support:

1.  **inputSchema restriction**: Currently only allows `type`, `properties`, and `required` fields. This prevents use of composition keywords like `anyOf`, `oneOf`, and `allOf` for sophisticated object validation patterns.
2.  **outputSchema restriction**: Also restricted to `type: "object"` with only `properties` and `required`, despite the specification claiming to support “JSON Schema.”
3.  **structuredContent restriction**: Defined as `{ [key: string]: unknown }` (an object with string keys), which prevents returning arrays—a common API response pattern.


[​](#real-world-impact)

Real-World Impact

Consider a weather API tool that returns hourly forecasts:

```python
[
  { "hour": "09:00", "temp": 68, "conditions": "sunny" },
  { "hour": "10:00", "temp": 72, "conditions": "partly cloudy" },
  { "hour": "11:00", "temp": 75, "conditions": "cloudy" }
]
```

Currently, this natural array response is **impossible** because `structuredContent` must be an object. Developers are forced to wrap arrays in unnecessary container objects:

```python
{
  "forecasts": [
    { "hour": "09:00", "temp": 68, "conditions": "sunny" },
    ...
  ]
}
```

This artificial constraint:

- Adds unnecessary nesting to responses
- Conflicts with common REST API patterns
- Prevents direct schema validation of array responses


[​](#schema-composition-use-cases)

Schema Composition Use Cases

The current `inputSchema` restriction prevents legitimate schema patterns. With this SEP, tools can use composition keywords alongside `type: "object"`:

```python
{
  "type": "object",
  "oneOf": [
    { "properties": { "id": { "type": "string" } }, "required": ["id"] },
    { "properties": { "name": { "type": "string" } }, "required": ["name"] }
  ]
}
```

This pattern allows a tool to accept either an ID-based or name-based lookup—a common API design that is currently unsupported because the schema only allows `type`, `properties`, and `required` fields.


[​](#specification)

Specification


[​](#1-loosen-inputschema)

1. Loosen inputSchema

**Current definition:**

```python
inputSchema: {
  type: "object";
  properties?: { [key: string]: object };
  required?: string[];
};
```

**Proposed definition:**

```python
inputSchema: {
  $schema?: string;
  type: "object";
  [key: string]: unknown;
};
```

The `inputSchema` field retains the `type: "object"` requirement (since tool arguments are always objects), but now accepts any additional JSON Schema properties. This enables:

- Composition keywords: `anyOf`, `oneOf`, `allOf`, `not`
- Conditional schemas: `if`/`then`/`else`
- Reference schemas: `$ref`, `$defs`
- Any other valid JSON Schema 2020-12 keywords


[​](#2-loosen-outputschema)

2. Loosen outputSchema

**Current definition:**

```python
outputSchema?: {
  type: "object";
  properties?: { [key: string]: object };
  required?: string[];
};
```

**Proposed definition:**

```python
outputSchema?: {
  $schema?: string;
  [key: string]: unknown;
};
```

The `outputSchema` field accepts any valid JSON Schema 2020-12 object, enabling schemas that validate arrays, primitives, or complex compositions. Unlike `inputSchema`, there is no `type: "object"` requirement since tool outputs can be any valid JSON.


[​](#3-loosen-structuredcontent)

3. Loosen structuredContent

**Current definition:**

```python
structuredContent?: { [key: string]: unknown };
```

**Proposed definition:**

```python
structuredContent?: unknown;
```

The `structuredContent` field accepts any valid JSON value that conforms to the tool’s `outputSchema`. This includes:

- Objects: `{ "key": "value" }`
- Arrays: `[1, 2, 3]` or `[{ "id": "abc" }, { "id": "xyz" }]`
- Primitives: `"string"`, `42`, `true`, `null`


[​](#4-documentation-updates)

4. Documentation Updates

Update `docs/specification/draft/server/tools.mdx`:

- Remove statement that `structuredContent` is “returned as a JSON object”
- Clarify that `structuredContent` can be any JSON value conforming to `outputSchema`
- Add examples demonstrating array responses


[​](#5-examples)

5. Examples


[​](#tool-returning-an-array-of-objects)

Tool returning an array of objects:

```python
{
  "name": "list_users",
  "description": "List all users in the system",
  "inputSchema": {
    "type": "object",
    "properties": {
      "limit": { "type": "integer", "minimum": 1, "maximum": 100 }
    }
  },
  "outputSchema": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "id": { "type": "string" },
        "name": { "type": "string" },
        "email": { "type": "string", "format": "email" }
      },
      "required": ["id", "name"]
    }
  }
}
```

Response:

```python
{
  "content": [
    {
      "type": "text",
      "text": "Found 2 users: Alice (u1, alice@example.com) and Bob (u2, bob@example.com)."
    }
  ],
  "structuredContent": [
    { "id": "u1", "name": "Alice", "email": "alice@example.com" },
    { "id": "u2", "name": "Bob", "email": "bob@example.com" }
  ]
}
```


[​](#tool-with-composition-schema)

Tool with composition schema:

```python
{
  "name": "find_resource",
  "description": "Find a resource by ID or name",
  "inputSchema": {
    "type": "object",
    "oneOf": [
      {
        "properties": { "id": { "type": "string", "format": "uuid" } },
        "required": ["id"]
      },
      {
        "properties": { "name": { "type": "string", "minLength": 1 } },
        "required": ["name"]
      }
    ]
  }
}
```


[​](#rationale)

Rationale


[​](#why-not-just-allow-arrays)

Why not just allow arrays?

While we could simply extend `structuredContent` to allow arrays, this would be an incomplete solution. The root cause is that the schema types are artificially restricted to `type: "object"`. By allowing any valid JSON Schema, we:

1.  Enable the full power of JSON Schema 2020-12
2.  Align with the specification’s claim of JSON Schema support
3.  Provide a consistent, principled approach rather than piecemeal fixes


[​](#why-not-require-a-wrapper-object)

Why not require a wrapper object?

Requiring arrays to be wrapped in objects (e.g., `{ "items": [...] }`) was considered but rejected because:

1.  It adds unnecessary complexity to responses
2.  It conflicts with common API design patterns
3.  It prevents direct schema validation of the actual response structure
4.  JSON Schema already handles array validation elegantly


[​](#real-world-api-patterns)

Real-World API Patterns

Many production APIs return arrays directly:

- **GitHub Events API**: Returns arrays of event objects
- **AccuWeather Search API**: Returns arrays of location matches
- **REST collection endpoints**: Standard `GET /users` returns `[{...}, {...}]`

Forcing wrapper objects creates friction for developers integrating existing APIs with MCP. Generic JSON Schema validation libraries should work without MCP-specific customization.


[​](#alignment-with-json-schema-2020-12)

Alignment with JSON Schema 2020-12

JSON Schema 2020-12 provides powerful features for schema composition and validation. By removing artificial restrictions, MCP aligns with industry standards (OpenAPI 3.1 uses JSON Schema 2020-12) and enables developers to leverage existing JSON Schema knowledge and tooling.


[​](#sdk-ecosystem-evidence)

SDK Ecosystem Evidence

The friction caused by current restrictions is not theoretical. FastMCP, one of the most popular Python SDKs for MCP, has implemented extensive workarounds:

1.  **Explicit error messages** acknowledge the limitation:

    ``` shiki
    raise ValueError(
        f"Output schemas must represent object types due to MCP spec limitations."
    )
    ```
2.  **Auto-wrapping infrastructure** adds complexity:
    - A `_WrappedResult` dataclass wraps non-object returns
    - A custom `x-fastmcp-wrap-result` extension enables client-side unwrapping
    - Both SDK and client need matching wrap/unwrap logic
3.  **Real bugs** have resulted from these workarounds:
    - Issue \#2455: `$ref` schemas without `type: object` broke ALL tools on the server
    - Issue \#2421: Unexpected `{"result": ...}` wrapping confused users

This demonstrates that the current restrictions create genuine ecosystem friction that SEP-2106 would eliminate.


[​](#openapi-precedent)

OpenAPI Precedent

The OpenAPI specification went through a similar evolution. OpenAPI 3.0 used an “extended subset” of JSON Schema with custom restrictions (like requiring `nullable: true` instead of allowing `"null"` as a type). OpenAPI 3.1 made the strategic decision to fully align with JSON Schema 2020-12, accepting breaking changes to eliminate the friction. The result: better tooling compatibility and less ecosystem confusion.

| OpenAPI’s Problem                   | MCP’s Parallel                            |
|-------------------------------------|-------------------------------------------|
| `type` must be string, not array    | `inputSchema` only allows specific fields |
| Couldn’t use standard null handling | Can’t use `oneOf`/`anyOf` in schemas      |
| Custom `nullable` keyword           | Object-only `structuredContent`           |
| Caused tooling confusion            | Causes SDK workarounds                    |

MCP can learn from OpenAPI’s experience rather than repeating the same evolution over several years.


[​](#backward-compatibility)

Backward Compatibility

This change is **wire-format backward compatible** but has nuances depending on the direction of the version mismatch.


[​](#compatibility-matrix)

Compatibility Matrix

|                           | New client (post-SEP)                                        | Old client (pre-SEP)                                                                                                              |
|---------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **New server (post-SEP)** | Fully compatible.                                            | Compatible **only when the server returns object-typed `structuredContent`**. Arrays/primitives in `structuredContent` may break. |
| **Old server (pre-SEP)**  | Fully compatible. Existing object-only schemas remain valid. | Unchanged.                                                                                                                        |

The asymmetry: a new server that takes advantage of array or primitive `structuredContent` (or composition keywords in `inputSchema`) cannot assume an old client will accept the response. Old clients written against the previous wire format may reject `structuredContent` that is not a JSON object, or fail to validate `inputSchema` containing keywords beyond `type`/`properties`/`required`. To remain interoperable with older clients, **servers using array or primitive `structuredContent` MUST also emit a `TextContent` block containing the serialized JSON** (as already recommended in the tools specification). Clients that do not understand non-object `structuredContent` can fall back to the text content.


[​](#typescript-/-sdk-migration)

TypeScript / SDK Migration

Widening the `structuredContent` field type from `{ [key: string]: unknown }` to `unknown` is a **source-breaking change for typed consumers**, even though the wire format is unchanged. Code such as:

```python
const result = await client.callTool({ name: "get_weather", arguments: { ... } });
const temp = result.structuredContent?.temperature;        // previously compiled (type: unknown)
const city = result.structuredContent?.["city"] as string; // previously compiled
```

will no longer type-check after the change, because TypeScript forbids property access on `unknown` without a narrowing guard:

```python
const sc = result.structuredContent;
if (sc && typeof sc === "object" && !Array.isArray(sc)) {
  const temp = (sc as Record<string, unknown>).temperature;
}
```

This break is intentional — the previous type was a lie whenever a tool returned a non-object — but SDK maintainers SHOULD:

- Document the migration in SDK release notes.
- Where ergonomic, provide typed helpers (e.g. generics over a tool’s `outputSchema`) so consumers do not need to write narrowing guards by hand.


[​](#migration-path)

Migration Path

- **Servers**: No migration is required to keep working as before. To use array or primitive `structuredContent`, also emit a serialized `TextContent` fallback.
- **Clients**: Old clients continue to work against object-only servers. To consume the new flexibility, accept any JSON value in `structuredContent` and validate against `outputSchema` if present.
- **SDKs**: Update generated types to mirror the new schema (`unknown` for `structuredContent`, open-ended `inputSchema`/`outputSchema`) and call out the source-breaking type change in release notes.


[​](#security-implications)

Security Implications

JSON Schema validation already handles type checking, value constraints, and required field validation, and implementations MUST continue to validate all inputs and outputs against declared schemas. Allowing the full JSON Schema 2020-12 vocabulary surfaces two areas that warrant explicit guidance.


[​](#$ref-dereferencing-ssrf-and-fetch-dos)

`$ref` Dereferencing (SSRF and Fetch-DoS)

JSON Schema 2020-12 permits `$ref` to point at an absolute URI, not just a JSON Pointer into the same document. A naive implementation that resolves every `$ref` it encounters by issuing an HTTP request gives an attacker a server-side request forgery / fetch amplification primitive: a malicious tool definition can cause the host to fetch arbitrary URLs, including internal metadata endpoints or large payloads designed to exhaust resources. To mitigate this:

- Implementations **MUST NOT** automatically dereference `$ref` values that resolve to a network URI (i.e. anything that is not a same-document JSON Pointer such as `#/$defs/Foo` or an internal `$anchor`).
- “Automatically” here means “as part of normal validation or schema processing, without explicit operator action.” Implementations **MAY** offer an opt-in mode that fetches non-local `$ref`s, but it MUST be disabled by default and SHOULD enforce an allowlist of hosts (or at minimum reject loopback, link-local, and private network addresses), apply timeouts and size limits, and log dereferenced URIs.
- Schemas that fail to validate due to an unresolved external `$ref` SHOULD be rejected rather than silently treated as permissive.


[​](#composition-keyword-resource-use)

Composition-Keyword Resource Use

Composition keywords (`anyOf`, `oneOf`, `allOf`, `if`/`then`/`else`) and `$defs` enable expressive schemas, but pathological combinations can be expensive to validate. Implementations SHOULD apply reasonable bounds — for example, a maximum schema depth, a cap on the total number of subschemas, or a per-validation time budget — to prevent a malicious tool definition from acting as a CPU DoS vector against the validator.


[​](#reference-implementation)

Reference Implementation


[​](#typescript-sdk)

TypeScript SDK

A reference implementation demonstrating the loosened type restrictions:

- **Branch**: [olaservo/typescript-sdk@sep-834-v1x](https://github.com/olaservo/typescript-sdk/tree/sep-834-v1x)
- **npm**: `@olaservo/mcp-sdk@1.25.2-sep834.4`
- **Key changes**:
  - `inputSchema`: Retains `type: "object"` but allows any additional JSON Schema properties (compositions like `oneOf`/`anyOf`)
  - `outputSchema`: Any valid JSON Schema object (arrays, primitives, objects, compositions)
  - `structuredContent`: Any JSON value (objects, arrays, or primitives)
  - McpServer high-level API updated to support array and primitive outputSchema


[​](#everything-server-demo-tools)

Everything Server Demo Tools

Three demo tools added to the `everything` server demonstrating SEP-2106 capabilities:

- **Branch**: [olaservo/servers@sep-834-json-schema-2020-12](https://github.com/olaservo/servers/tree/sep-834-json-schema-2020-12/src/everything)
- **npm**: `@olaservo/mcp-server-everything-sep834@1.1.0-sep834.1`
- **Tools**:
  - `get-weather-forecast`: Returns **raw array** of hourly forecasts directly in `structuredContent`
    - Matches the exact example from SEP-2106’s Motivation section
    - `outputSchema`: `z.array(HourlyForecastSchema)` - array type at root
    - `structuredContent`: `[{hour, temp, conditions}, ...]` - direct array
  - `find-by-id-or-name`: Demonstrates flexible input patterns (accepts `id` OR `name`)
  - `get-count`: Returns **raw number** directly in `structuredContent` (not wrapped in object)
    - `outputSchema`: `z.number()` - primitive type at root
    - `structuredContent`: `42` - direct primitive


[​](#related-links)

Related Links

- Original PR: [https://github.com/modelcontextprotocol/modelcontextprotocol/pull/881](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/881)
- Related issue: [https://github.com/modelcontextprotocol/modelcontextprotocol/issues/834](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/834)
- `outputSchema` type restriction inconsistency: [https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1906](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1906)
- TypeScript SDK schema types: [https://github.com/modelcontextprotocol/typescript-sdk/issues/1149](https://github.com/modelcontextprotocol/typescript-sdk/issues/1149)
- SEP-2200 (Clarify Tool Result Content and Model Visibility): [https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2200](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2200)


[​](#implementation-guidance)

Implementation Guidance

SDK implementations will need to:

1.  Update `inputSchema` types to retain `type: "object"` but allow any additional JSON Schema properties
2.  Update `outputSchema` types to allow any valid JSON Schema (remove `type: "object"` constraint)
3.  Update `structuredContent` types to accept any valid JSON value
4.  Update JSON Schema definitions accordingly


[​](#acknowledgments)

Acknowledgments

This proposal builds on discussions in GitHub issue \#834 and incorporates feedback from the MCP community.
