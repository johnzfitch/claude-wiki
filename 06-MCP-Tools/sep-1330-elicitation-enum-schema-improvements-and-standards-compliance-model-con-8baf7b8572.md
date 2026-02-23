---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:13Z"
source_url: "https://modelcontextprotocol.io/community/seps/1330-elicitation-enum-schema-improvements-and-standards"
title: "SEP-1330: Elicitation Enum Schema Improvements and Standards Compliance - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Final

SEP-1330: Elicitation Enum Schema Improvements and Standards Compliance

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/community/contributing)
  Contributing to MCP

&nbsp;

- [](/community/communication)
  Contributor Communication

##### Governance

- [](/community/governance)
  Governance and Stewardship
- [](/community/sep-guidelines)
  SEP Guidelines
- [](/community/sdk-tiers)
  SDK Tiering System
- [](/community/working-interest-groups)
  Working and Interest Groups
- [](/community/antitrust)
  Antitrust Policy

##### SEPs

- [](/community/seps)
  SEP Index

- Final

  - [](/community/seps/932-model-context-protocol-governance)
    SEP-932: Model Context Protocol Governance
  - [](/community/seps/973-expose-additional-metadata-for-implementations-res)
    SEP-973: Expose additional metadata for Implemen…
  - [](/community/seps/985-align-oauth-20-protected-resource-metadata-with-rf)
    SEP-985: Align OAuth 2.0 Protected Resource Meta…
  - [](/community/seps/986-specify-format-for-tool-names)
    SEP-986: Specify Format for Tool Names
  - [](/community/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o)
    SEP-990: Enable enterprise IdP policy controls d…
  - [](/community/seps/991-enable-url-based-client-registration-using-oauth-c)
    SEP-991: Enable URL-based Client Registration us…
  - [](/community/seps/994-shared-communication-practicesguidelines)
    SEP-994: Shared Communication Practices/Guidelin…
  - [](/community/seps/1024-mcp-client-security-requirements-for-local-server-)
    SEP-1024: MCP Client Security Requirements for Lo…
  - [](/community/seps/1034--support-default-values-for-all-primitive-types-in)
    SEP-1034: Support default values for all primitiv…
  - [](/community/seps/1036-url-mode-elicitation-for-secure-out-of-band-intera)
    SEP-1036: URL Mode Elicitation for secure out-of-…
  - [](/community/seps/1046-support-oauth-client-credentials-flow-in-authoriza)
    SEP-1046: Support OAuth client credentials flow i…
  - [](/community/seps/1302-formalize-working-groups-and-interest-groups-in-mc)
    SEP-1302: Formalize Working Groups and Interest G…
  - [](/community/seps/1303-input-validation-errors-as-tool-execution-errors)
    SEP-1303: Input Validation Errors as Tool Executi…
  - [](/community/seps/1319-decouple-request-payload-from-rpc-methods-definiti)
    SEP-1319: Decouple Request Payload from RPC Metho…
  - [](/community/seps/1330-elicitation-enum-schema-improvements-and-standards)
    SEP-1330: Elicitation Enum Schema Improvements an…
  - [](/community/seps/1577--sampling-with-tools)
    SEP-1577: Sampling With Tools
  - [](/community/seps/1613-establish-json-schema-2020-12-as-default-dialect-f)
    SEP-1613: Establish JSON Schema 2020-12 as Defaul…
  - [](/community/seps/1686-tasks)
    SEP-1686: Tasks
  - [](/community/seps/1699-support-sse-polling-via-server-side-disconnect)
    SEP-1699: Support SSE polling via server-side dis…
  - [](/community/seps/1730-sdks-tiering-system)
    SEP-1730: SDKs Tiering System
  - [](/community/seps/1850-pr-based-sep-workflow)
    SEP-1850: PR-Based SEP Workflow
  - [](/community/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp)
    SEP-1865: MCP Apps - Interactive User Interfaces…
  - [](/community/seps/2085-governance-succession-and-amendment)
    SEP-2085: Governance Succession and Amendment Pro…
  - [](/community/seps/2133-extensions)
    SEP-2133: Extensions

- Draft

##### Roadmap

- [](/development/roadmap)
  Roadmap

##### Examples

- [](/clients)
  Example Clients
- [](/examples)
  Example Servers

On this page

- [Abstract](#abstract)
- [Motivation](#motivation)
- [Specification](#specification)
- [1. Mark Current EnumSchema with Non-Standard enumNames Property as “Legacy”](#1-mark-current-enumschema-with-non-standard-enumnames-property-as-%E2%80%9Clegacy%E2%80%9D)
- [2. Define Single Selection Enums (with Titled and Untitled varieties)](#2-define-single-selection-enums-with-titled-and-untitled-varieties)
- [3. Introduce Multiple Selection Enums (with Titled and Untitled varieties)](#3-introduce-multiple-selection-enums-with-titled-and-untitled-varieties)
- [4. Combine All Varieties as EnumSchema](#4-combine-all-varieties-as-enumschema)
- [5. Extend ElicitResult](#5-extend-elicitresult)
- [Instance Schema Examples](#instance-schema-examples)
- [Single-Select Without Titles (No change)](#single-select-without-titles-no-change)
- [Legacy Single Select With Titles](#legacy-single-select-with-titles)
- [Single-Select with Titles](#single-select-with-titles)
- [Multi-Select Without Titles](#multi-select-without-titles)
- [Multi-Select with Titles](#multi-select-with-titles)
- [Rationale](#rationale)
- [Backwards Compatibility](#backwards-compatibility)
- [Reference Implementation](#reference-implementation)
- [Security Considerations](#security-considerations)
- [Appendix](#appendix)
- [Validations](#validations)
- [Legacy Single Selection](#legacy-single-selection)
- [Single Selection](#single-selection)
- [Multiple Selection](#multiple-selection)
- [JSON meta-schema](#json-meta-schema)

Final

# SEP-1330: Elicitation Enum Schema Improvements and Standards Compliance

Copy page

Elicitation Enum Schema Improvements and Standards Compliance

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 1330 |
| **Title** | Elicitation Enum Schema Improvements and Standards Compliance |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-08-11 |
| **Author(s)** | chughtapan |
| **Sponsor** | None |
| **PR** | [\#1330](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1330) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP proposes improvements to enum schema definitions in MCP, deprecating the non-standard `enumNames` property in favor of JSON Schema-compliant patterns, and introducing additional support for multi-select enum schemas in addition to single choice schemas. The new schemas have been validated against the JSON specification. **Schema Changes:** [https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1148](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1148) Typescript SDK Changes: [https://github.com/modelcontextprotocol/typescript-sdk/pull/1077](https://github.com/modelcontextprotocol/typescript-sdk/pull/1077) Python SDK Changes: [https://github.com/modelcontextprotocol/python-sdk/pull/1246](https://github.com/modelcontextprotocol/python-sdk/pull/1246) **Client Implementation:** [https://github.com/evalstate/fast-agent/pull/324/files](https://github.com/evalstate/fast-agent/pull/324/files) **Working Demo:** [https://asciinema.org/a/anBvJdqEmTjw0JkKYOooQa5Ta](https://asciinema.org/a/anBvJdqEmTjw0JkKYOooQa5Ta)

## 

[​](#motivation)

Motivation

The existing schema for enums uses a non-standard approach to adding titles to enumerated values. It also limits use of enums in Elicitation (and any other schema object that should adopt `EnumSchema` in the future) to a single selection model. It is a common pattern to ask the user to select multiple entries. In the UI, this amounts to the difference between using checkboxes or radio buttons. For these reasons, we propose the following non-breaking minor improvements to the `EnumSchema` for improving user and developer experience.

- Keep the existing `EnumSchema` as “Legacy”
  - It uses a non-standard approach for adding titles to enumerated values
  - Mark it as Legacy but still support it for now.
  - As per @dsp-ant When we have a proper deprecation strategy, we’ll mark it deprecated
- Introduce the distinction between Untitled and Titled enums.
  - If the enumerated values are sufficient, no separate title need be specified for each value.
  - If the enumerated values are not optimal for display, a title may be specified for each value.
- Introduce the distinction between Single and Multi-select enums.
  - If only one value can be selected, a Single select schema can be used
  - If more than one value can be selected, a Multi-select schema can be used
- In `ElicitResponse`, add array as an `additionalProperty` type
  - Allows multiple selection of enumerated values to be returned to the server

## 

[​](#specification)

Specification

### 

[​](#1-mark-current-enumschema-with-non-standard-enumnames-property-as-“legacy”)

1. Mark Current `EnumSchema` with Non-Standard `enumNames` Property as “Legacy”

The current MCP specification uses a non-standard `enumNames` property for providing display names for enum values. We propose to mark `enumNames` property as legacy, suggest using `TitledSingleSelectEnum`, a standards compliant enum type we define below.

Copy

``` shiki
// Continue to support the current EnumSchema as Legacy

/**
 * Legacy: Use TitledSingleSelectEnumSchema instead.
 * This interface will be removed in a future version.
 */
export interface LegacyEnumSchema {
  type: "string";
  title?: string;
  description?: string;
  enum: string[];
  enumNames?: string[]; // Titles for enum values (non-standard, legacy)
}
```

### 

[​](#2-define-single-selection-enums-with-titled-and-untitled-varieties)

2. Define Single Selection Enums (with Titled and Untitled varieties)

Enums may or may not need titles. The enumerated values may be human readable and fine for display. In which case an untitled implementation using the JSON Schema keyword `enum` is simpler. Adding titles requires the `enum` array to be replaced with an array of objects using `const` and `title`.

Copy

``` shiki
// Single select enum without titles
export type UntitledSingleSelectEnumSchema = {
  type: "string";
  title?: string;
  description?: string;
  enum: string[]; // Plain enum without titles
};

// Single select enum with titles
export type TitledSingleSelectEnumSchema = {
  type: "string";
  title?: string;
  description?: string;
  oneOf: Array<{
    const: string; // Enum value
    title: string; // Display name for enum value
  }>;
};

// Combined single selection enumeration
export type SingleSelectEnumSchema =
  | UntitledSingleSelectEnumSchema
  | TitledSingleSelectEnumSchema;
```

### 

[​](#3-introduce-multiple-selection-enums-with-titled-and-untitled-varieties)

3. Introduce Multiple Selection Enums (with Titled and Untitled varieties)

While elicitation does not support arbitrary JSON types like arrays and objects so clients can display the selection choice easily, multiple selection enumerations can be easily implemented.

Copy

``` shiki
// Multiple select enums without titles
export type UntitledMultiSelectEnumSchema = {
  type: "array";
  title?: string;
  description?: string;
  minItems?: number; // Minimum number of items to choose
  maxItems?: number; // Maximum number of items to choose
  items: {
    type: "string";
    enum: string[]; // Plain enum without titles
  };
};

// Multiple select enums with titles
export type TitledMultiSelectEnumSchema = {
  type: "array";
  title?: string;
  description?: string;
  minItems?: number; // Minimum number of items to choose
  maxItems?: number; // Maximum number of items to choose
  items: {
    oneOf: Array<{
      const: string; // Enum value
      title: string; // Display name for enum value
    }>;
  };
};

// Combined Multiple select enumeration
export type MultiSelectEnumSchema =
  | UntitledMultiSelectEnumSchema
  | TitledMultiSelectEnumSchema;
```

### 

[​](#4-combine-all-varieties-as-enumschema)

4. Combine All Varieties as `EnumSchema`

The final `EnumSchema` rolls up the legacy, multi-select, and single-select schemas as one, defined as:

Copy

``` shiki
// Combined legacy, multiple, and single select enumeration
export type EnumSchema =
  | SingleSelectEnumSchema
  | MultiSelectEnumSchema
  | LegacyEnumSchema;
```

### 

[​](#5-extend-elicitresult)

5. Extend ElicitResult

The current elicitation result schema only allows returning primitive types. We extend this to include string arrays for MultiSelectEnums:

Copy

``` shiki
export interface ElicitResult extends Result {
  action: "accept" | "decline" | "cancel";
  content?: { [key: string]: string | number | boolean | string[] }; // string[] is new
}
```

## 

[​](#instance-schema-examples)

Instance Schema Examples

### 

[​](#single-select-without-titles-no-change)

Single-Select Without Titles (No change)

Copy

``` shiki
{
  "type": "string",
  "title": "Color Selection",
  "description": "Choose your favorite color",
  "enum": ["Red", "Green", "Blue"],
  "default": "Green"
}
```

### 

[​](#legacy-single-select-with-titles)

Legacy Single Select With Titles

Copy

``` shiki
{
  "type": "string",
  "title": "Color Selection",
  "description": "Choose your favorite color",
  "enum": ["#FF0000", "#00FF00", "#0000FF"],
  “enumNames”: ["Red", "Green", "Blue"],
  "default": "Green"
}
```

### 

[​](#single-select-with-titles)

Single-Select with Titles

Copy

``` shiki
{
  "type": "string",
  "title": "Color Selection",
  "description": "Choose your favorite color",
  "oneOf": [
    { "const": "#FF0000", "title": "Red" },
    { "const": "#00FF00", "title": "Green" },
    { "const": "#0000FF", "title": "Blue" }
  ],
  "default": "#00FF00"
}
```

### 

[​](#multi-select-without-titles)

Multi-Select Without Titles

Copy

``` shiki
{
  "type": "array",
  "title": "Color Selection",
  "description": "Choose your favorite colors",
  "minItems": 1,
  "maxItems": 3,
  "items": {
    "type": "string",
    "enum": ["Red", "Green", "Blue"]
  },
  "default": ["Green"]
}
```

### 

[​](#multi-select-with-titles)

Multi-Select with Titles

Copy

``` shiki
{
  "type": "array",
  "title": "Color Selection",
  "description": "Choose your favorite colors",
  "minItems": 1,
  "maxItems": 3,
  "items": {
    "anyOf": [
      { "const": "#FF0000", "title": "Red" },
      { "const": "#00FF00", "title": "Green" },
      { "const": "#0000FF", "title": "Blue" }
    ]
  },
  "default": ["Green"]
}
```

## 

[​](#rationale)

Rationale

1.  **Standards Compliance**: Aligns with official JSON Schema specification. Standard patterns work with existing JSON Schema validators
2.  **Flexibility**: Supports both plain enums and enums with display names for single and multiple choice enums.
3.  **Client Implementation:** shows that the additional overhead of implementing a group of checkboxes v/s a single checkbox is minimal: [https://github.com/evalstate/fast-agent/pull/324/files](https://github.com/evalstate/fast-agent/pull/324/files)

## 

[​](#backwards-compatibility)

Backwards Compatibility

The `LegacyEnumSchema` type maintains backwards compatible during the migration period. Existing implementations using `enumNames` will continue to work until a protocol-wide deprecation strategy is implemented, and this schema is removed.

## 

[​](#reference-implementation)

Reference Implementation

**Schema Changes:** [https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1148](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1148) Typescript SDK Changes: [https://github.com/modelcontextprotocol/typescript-sdk/pull/1077](https://github.com/modelcontextprotocol/typescript-sdk/pull/1077) Python SDK Changes: [https://github.com/modelcontextprotocol/python-sdk/pull/1246](https://github.com/modelcontextprotocol/python-sdk/pull/1246) **Client Implementation:** [https://github.com/evalstate/fast-agent/pull/324/files](https://github.com/evalstate/fast-agent/pull/324/files) **Working Demo:** [https://asciinema.org/a/anBvJdqEmTjw0JkKYOooQa5Ta](https://asciinema.org/a/anBvJdqEmTjw0JkKYOooQa5Ta)

## 

[​](#security-considerations)

Security Considerations

No security implications identified. This change is purely about schema structure and standards compliance.

## 

[​](#appendix)

Appendix

### 

[​](#validations)

Validations

Using stored validations in the JSON Schema Validator at [https://www.jsonschemavalidator.net/](https://www.jsonschemavalidator.net/) we validate:

- All of the example instance schemas from this document against the proposed JSON meta-schema `EnumSchema` in the next section.
- Valid and invalid values against the example instance schemas from this document.

#### 

[​](#legacy-single-selection)

Legacy Single Selection

- `EnumSchema` validating a [legacy single select instance schema with titles](https://www.jsonschemavalidator.net/s/lsK7Bn0C)
- The legacy titled single select instance schema validating [a correct single selection](https://www.jsonschemavalidator.net/s/GSk7rnRe)
- The legacy titled single select instance schema validating [an incorrect single selection](https://www.jsonschemavalidator.net/s/3kYvxsVP)

#### 

[​](#single-selection)

Single Selection

- `EnumSchema` validating a [single select instance schema without titles](https://www.jsonschemavalidator.net/s/MBlHW5IQ)
- `EnumSchema` validating a [single select instance schema with titles](https://www.jsonschemavalidator.net/s/s38xt4JV)
- The untitled single select instance schema validating [a correct single selection](https://www.jsonschemavalidator.net/s/M0hkYoeG)
- The untitled single select instance schema invalidating [an incorrect single selection](https://www.jsonschemavalidator.net/s/3Try4BCt)
- The titled single select instance schema validating [a correct single selection](https://www.jsonschemavalidator.net/s/4oDbv9yt)
- The titled single select instance schema invalidating [an incorrect single selection](https://www.jsonschemavalidator.net/s/A2KlNzLH)

#### 

[​](#multiple-selection)

Multiple Selection

- `EnumSchema` validating the [multi-select instance schema without titles](https://www.jsonschemavalidator.net/s/4uc3Ndsq)
- `EnumSchema` validating the [multi-select instance schema with titles](https://www.jsonschemavalidator.net/s/TmkIqqXI)
- The untitled multi-select instance schema validating [a correct multiple selection](https://www.jsonschemavalidator.net/s/IE8Bkvtg) The untitled multi-select instance schema validating invalidating [an incorrect multiple selection](https://www.jsonschemavalidator.net/s/8tlqjUgW) The titled multi-select instance schema validating [a correct multiple selection](https://www.jsonschemavalidator.net/s/Nb1Rw1qa) The titled multi-select instance schema validating invalidating [an incorrect multiple selection](https://www.jsonschemavalidator.net/s/MRfyqrVC)

### 

[​](#json-meta-schema)

JSON meta-schema

This is our proposal for the replacement of the current `EnumSchema` in the specification’s `schema.json`.

Copy

``` shiki
{
  "$schema": "https://json-schema.org/draft-07/schema",
  "definitions": {
    // New Definitions Follow
    "UntitledSingleSelectEnumSchema": {
      "type": "object",
      "properties": {
        "type": { "const": "string" },
        "title": { "type": "string" },
        "description": { "type": "string" },
        "enum": {
          "type": "array",
          "items": { "type": "string" },
          "minItems": 1
        }
      },
      "required": ["type", "enum"],
      "additionalProperties": false
    },

    "UntitledMultiSelectEnumSchema": {
      "type": "object",
      "properties": {
        "type": { "const": "array" },
        "title": { "type": "string" },
        "description": { "type": "string" },
        "minItems": {
          "type": "number",
          "minimum": 0
        },
        "maxItems": {
          "type": "number",
          "minimum": 0
        },
        "items": {
          "type": "object",
          "properties": {
            "type": { "const": "string" },
            "enum": {
              "type": "array",
              "items": { "type": "string" },
              "minItems": 1
            }
          },
          "required": ["type", "enum"],
          "additionalProperties": false
        }
      },
      "required": ["type", "items"],
      "additionalProperties": false
    },

    "TitledSingleSelectEnumSchema": {
      "type": "object",
      "required": ["type", "anyOf"],
      "properties": {
        "type": { "const": "string" },
        "title": { "type": "string" },
        "description": { "type": "string" },
        "anyOf": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["const", "title"],
            "properties": {
              "const": { "type": "string" },
              "title": { "type": "string" }
            },
            "additionalProperties": false
          }
        }
      },
      "additionalProperties": false
    },

    "TitledMultiSelectEnumSchema": {
      "type": "object",
      "required": ["type", "anyOf"],
      "properties": {
        "type": { "const": "array" },
        "title": { "type": "string" },
        "description": { "type": "string" },
        "anyOf": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["const", "title"],
            "properties": {
              "const": { "type": "string" },
              "title": { "type": "string" }
            },
            "additionalProperties": false
          }
        }
      },
      "additionalProperties": false
    },

    "LegacyEnumSchema": {
      "properties": {
        "type": {
          "type": "string",
          "const": "string"
        },
        "title": { "type": "string" },
        "description": { "type": "string" },
        "enum": {
          "type": "array",
          "items": { "type": "string" }
        },
        "enumNames": {
          "type": "array",
          "items": { "type": "string" }
        }
      },
      "required": ["enum", "type"],
      "type": "object"
    },

    "EnumSchema": {
      "oneOf": [
        { "$ref": "#/definitions/UntitledSingleSelectEnumSchema" },
        { "$ref": "#/definitions/UntitledMultiSelectEnumSchema" },
        { "$ref": "#/definitions/TitledSingleSelectEnumSchema" },
        { "$ref": "#/definitions/TitledMultiSelectEnumSchema" },
        { "$ref": "#/definitions/LegacyEnumSchema" }
      ]
    }
  }
}
```

Was this page helpful?

Yes

No

[SEP-1319: Decouple Request Payload from RPC Metho…](/community/seps/1319-decouple-request-payload-from-rpc-methods-definiti)[SEP-1577: Sampling With Tools](/community/seps/1577--sampling-with-tools)

[github](https://github.com/modelcontextprotocol)
