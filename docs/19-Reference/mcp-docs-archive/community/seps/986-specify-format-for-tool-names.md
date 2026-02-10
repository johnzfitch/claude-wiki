---
source: https://modelcontextprotocol.io/community/seps/986-specify-format-for-tool-names.md
downloaded: 2026-02-02T05:34:24.532731
---

> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SEP-986: Specify Format for Tool Names

> Specify Format for Tool Names

export const Badge = ({children, color = "gray"}) => {
  const styles = {
    green: {
      light: {
        bg: "#dcfce7",
        text: "#166534"
      },
      dark: {
        bg: "#14532d",
        text: "#86efac"
      }
    },
    blue: {
      light: {
        bg: "#dbeafe",
        text: "#1e40af"
      },
      dark: {
        bg: "#1e3a5f",
        text: "#93c5fd"
      }
    },
    yellow: {
      light: {
        bg: "#fef9c3",
        text: "#854d0e"
      },
      dark: {
        bg: "#713f12",
        text: "#fde047"
      }
    },
    red: {
      light: {
        bg: "#fee2e2",
        text: "#991b1b"
      },
      dark: {
        bg: "#7f1d1d",
        text: "#fca5a5"
      }
    },
    orange: {
      light: {
        bg: "#ffedd5",
        text: "#9a3412"
      },
      dark: {
        bg: "#7c2d12",
        text: "#fdba74"
      }
    },
    purple: {
      light: {
        bg: "#f3e8ff",
        text: "#6b21a8"
      },
      dark: {
        bg: "#581c87",
        text: "#d8b4fe"
      }
    },
    gray: {
      light: {
        bg: "#f3f4f6",
        text: "#1f2937"
      },
      dark: {
        bg: "#374151",
        text: "#d1d5db"
      }
    }
  };
  const s = styles[color] || styles.gray;
  return <>
      <style>{`
        .badge-${color} { background-color: ${s.light.bg}; color: ${s.light.text}; }
        .dark .badge-${color}, [data-theme="dark"] .badge-${color} { background-color: ${s.dark.bg}; color: ${s.dark.text}; }
        @media (prefers-color-scheme: dark) {
          .badge-${color}:not(.light *) { background-color: ${s.dark.bg}; color: ${s.dark.text}; }
        }
      `}</style>
      <span className={`badge-${color} inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium`}>
        {children}
      </span>
    </>;
};

<div className="flex items-center gap-2 mb-4">
  <Badge color="green">Final</Badge>
  <Badge color="gray">Standards Track</Badge>
</div>

| Field         | Value                                                                  |
| ------------- | ---------------------------------------------------------------------- |
| **SEP**       | 986                                                                    |
| **Title**     | Specify Format for Tool Names                                          |
| **Status**    | Final                                                                  |
| **Type**      | Standards Track                                                        |
| **Created**   | 2025-07-16                                                             |
| **Author(s)** | kentcdodds                                                             |
| **Sponsor**   | None                                                                   |
| **PR**        | [#986](https://github.com/modelcontextprotocol/specification/pull/986) |

***

## Abstract

The Model Context Protocol (MCP) currently lacks a standardized format for tool names, resulting in inconsistencies and confusion for both implementers and users. This SEP proposes a clear, flexible standard for tool names: tool names should be 1–64 characters, case-sensitive, and may include alphanumeric characters, underscores (\_), dashes (-), dots (.), and forward slashes (/). This aims to maximize compatibility, clarity, and interoperability across MCP implementations while accommodating a wide range of naming conventions.

## Motivation

Without a prescribed format for tool names, MCP implementations have adopted a variety of naming conventions, including different separators, casing, and character sets. This inconsistency can lead to confusion, errors in tool invocation, and difficulties in documentation and automation. Standardizing the allowed characters and length will:

* Make tool names predictable and interoperable across clients.
* Allow for hierarchical and namespaced tool names (e.g., using / and .).
* Support both human-readable and machine-generated names.
* Avoid unnecessary restrictions that could block valid use cases.

## Rationale

Community discussion highlighted the need for flexibility in tool naming. While some conventions (like lower-kebab-case) are common, many tools and clients use uppercase, underscores, dots, and slashes for namespacing or clarity. The proposed pattern—allowing a-z, A-Z, 0-9, \_, -, ., and /—is based on patterns used in major clients (e.g., VS Code, Claude) and aligns with common conventions in programming and APIs. Restricting spaces and commas avoids parsing issues and ambiguity. The length limit (1–64) is generous enough for most use cases but prevents abuse.

## Specification

* Tool names SHOULD be between 1 and 64 characters in length (inclusive).
* Tool names are case-sensitive.
* Allowed characters: uppercase and lowercase ASCII letters (A-Z, a-z), digits
  (0-9), underscore (\_), dash (-), dot (.), and forward slash (/).
* Tool names SHOULD NOT contain spaces, commas, or other special characters.
* Tool names SHOULD be unique within their namespace.
* Example valid tool names:
  * getUser
  * user-profile/update
  * DATA\_EXPORT\_v2
  * admin.tools.list

## Backwards Compatibility

This change is not backwards compatible for existing tools that use disallowed characters or exceed the new length limits. To minimize disruption:

* Existing non-conforming tool names SHOULD be supported as aliases for at least one major version, with a deprecation warning.
* Tool authors SHOULD update their documentation and code to use the new format.
* A migration guide SHOULD be provided to assist implementers in updating their tool names.

## Reference Implementation

A reference implementation can be provided by updating the MCP core library to enforce the new tool name validation rules at registration time. Existing tools can be updated to provide aliases for their new conforming names, with warnings for deprecated formats. Example code and migration scripts can be included in the MCP repository.

## Security Implications

None. Standardizing tool name format does not introduce new security risks.

