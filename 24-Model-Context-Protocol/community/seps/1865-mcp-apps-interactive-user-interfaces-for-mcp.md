---
source: https://modelcontextprotocol.io/community/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp.md
downloaded: 2026-02-02T05:34:34.955469
---

> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SEP-1865: MCP Apps - Interactive User Interfaces for MCP

> MCP Apps - Interactive User Interfaces for MCP

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
  <Badge color="gray">Extensions Track</Badge>
</div>

| Field         | Value                                                                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SEP**       | 1865                                                                                                                                                                              |
| **Title**     | MCP Apps - Interactive User Interfaces for MCP                                                                                                                                    |
| **Status**    | Final                                                                                                                                                                             |
| **Type**      | Extensions Track                                                                                                                                                                  |
| **Created**   | 2025-11-21                                                                                                                                                                        |
| **Author(s)** | Ido Salomon ([@idosal](https://github.com/idosal)), Liad Yosef ([@liadyosef](https://github.com/liadyosef)), Olivier Chafik ([@olivierchafik](https://github.com/olivierchafik)), |
| **Sponsor**   | None (seeking sponsor)                                                                                                                                                            |
| **PR**        | [#1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865)                                                                                                   |

***

## Abstract

This SEP proposes an extension to MCP (per SEP-1724) that enables servers to deliver interactive
user interfaces to hosts. MCP Apps introduces a standardized pattern for declaring UI resources via
the `ui://` URI scheme, associating them with tools through metadata, and facilitating
bi-directional communication between the UI and the host using MCP's JSON-RPC base protocol. This
extension addresses the growing community need for rich, interactive experiences in MCP-enabled
applications, maintaining security, auditability, and alignment with MCP's core architecture. The
initial specification focuses on HTML resources (`text/html;profile=mcp-app`) with a clear path for
future extensions.

## Motivation

MCP lacks a standardized way for servers to deliver rich, interactive user interfaces to hosts.
This gap blocks many use cases that require visual presentation and interactivity that go beyond
plain text or structured data. As more hosts adopt this capability, the risk of fragmentation and
interoperability challenges grows.

[MCP-UI](https://mcpui.dev/) has demonstrated the viability and value of MCP apps built on UI
resources and serves as a community playground for the UI spec and SDK. Fueled by a dedicated
community, it developed the bi-directional communication model and the HTML, external URL, and
remote DOM content types. MCP-UI's adopters, including hosts and providers such as Postman,
HuggingFace, Shopify, Goose, and ElevenLabs, have provided critical insights and contributions to
the community.

OpenAI's [Apps SDK](https://developers.openai.com/apps-sdk/), launched in November 2025, further
validated the demand for rich UI experiences within conversational AI interfaces. The Apps SDK
enables developers to build rich, interactive applications inside ChatGPT using MCP as its
backbone.

The architecture of both the Apps SDK and MCP-UI has significantly informed the design of this
specification.

However, without formal standardization:

* Servers cannot reliably expect UI support via MCP
* Each host may implement slightly different behaviors
* Security and auditability patterns are inconsistent
* Developers must maintain separate implementations or adapters for different hosts (e.g., MCP-UI
  vs. Apps SDK)

This SEP addresses the current limitations through an optional, backwards-compatible extension that
unifies the approaches pioneered by MCP-UI and the Apps SDK into a single, open standard.

## Specification

The full specification can be found at
[modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/draft/apps.mdx).

At a high level, MCP Apps extends the Model Context Protocol to enable servers to deliver
interactive user interfaces to hosts. This extension introduces:

* **UI Resources:** Predeclared resources using the `ui://` URI scheme
* **Resource Discovery:** Tools reference UI resources via metadata
* **Bi-directional Communication:** UI iframes communicate with hosts using standard MCP JSON-RPC
  protocol
* **Security Model:** Mandatory iframe sandboxing with auditable communication

This specification focuses on HTML content (`text/html;profile=mcp-app`) as the initial content
type, with extensibility for future formats.

As an extension, MCP Apps is optional and must be explicitly negotiated between clients and servers
through the extension capabilities mechanism (see Capability Negotiation section in the
[full specification](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/draft/apps.mdx)).

## Rationale

### Predeclared resources vs. inline embedding

UI is modeled as predeclared resources (`ui://`), referenced by tools via metadata. This allows:

* Hosts to prefetch templates before tool execution, improving performance
* Separation of presentation (template) from data (tool results), facilitating caching
* Security review of UI resources

**Alternatives considered:**

* **Embedded resources:** Current MCP-UI approach, where resources are returned in tool results.
  Although it's more convenient for server development, it was deferred due to the gaps in
  performance optimization and the challenges in the UI review process.
* **Resource links:** Predeclare the resources but return links in tool results. Deferred due to
  the gaps in performance optimization.

### Reusing MCP JSON-RPC instead of a custom protocol

Reuses existing MCP infrastructure (type definitions, SDKs, etc.). JSON-RPC offers advanced
capabilities (timeouts, errors, etc.).

**Alternatives considered:**

* **Custom message protocol:** Current MCP-UI approach with message types like tool, intent,
  prompt, etc. These message types can be translated to a subset of the proposed JSON-RPC messages.
* **Global API object:** Rejected because it requires host-specific injection and doesn't work with
  external iframe sources. Syntactic sugar may still be added on the server/UI side.

### HTML-only MVP

* HTML is universally supported and well-understood
* Simplest security model (standard iframe sandbox)
* Allows screenshot/preview generation (e.g., via html2canvas)
* Sufficient for most observed use cases
* Provides a clear baseline for future extensions

**Alternatives considered:**

* **Include external URLs in MVP:** This is one of the easiest content types for servers to adopt,
  as it's possible to embed regular apps. However, it was deferred due to concerns around model
  visibility, inability to screenshot content, and review process. It may effectively be supported
  with the SEP's new `externalIframes` capability.

## Backward Compatibility

The proposal is an optional extension to the core protocol. Existing implementations continue
working without changes.

## Security Implications

Hosting interactive UI content from potentially untrusted MCP servers requires careful security
consideration.

Based on the threat model, MCP Apps proposes the following mitigations:

* **Iframe sandboxing**: All UI content runs in sandboxed iframes with restricted permissions
* **Predeclared templates**: Hosts can review HTML content before rendering
* **Auditable messages**: All UI-to-host communication goes through loggable JSON-RPC
* **User consent**: Hosts can require explicit approval for UI-initiated tool calls

A full threat model analysis and mitigations are available in the
[full specification](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/draft/apps.mdx).

## Reference Implementation

* [MCP-UI](https://github.com/idosal/mcp-ui) client and server SDKs support the patterns proposed
  in this spec.
* [ext-apps](https://github.com/modelcontextprotocol/ext-apps) repository contains a prototype
  implementation by Olivier Chafik.

