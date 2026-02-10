---
source: https://modelcontextprotocol.io/community/seps/1699-support-sse-polling-via-server-side-disconnect.md
downloaded: 2026-02-02T05:34:33.147363
---

> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SEP-1699: Support SSE polling via server-side disconnect

> Support SSE polling via server-side disconnect

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

| Field         | Value                                                                    |
| ------------- | ------------------------------------------------------------------------ |
| **SEP**       | 1699                                                                     |
| **Title**     | Support SSE polling via server-side disconnect                           |
| **Status**    | Final                                                                    |
| **Type**      | Standards Track                                                          |
| **Created**   | 2025-10-22                                                               |
| **Author(s)** | Jonathan Hefner ([@jonathanhefner](https://github.com/jonathanhefner))   |
| **Sponsor**   | None                                                                     |
| **PR**        | [#1699](https://github.com/modelcontextprotocol/specification/pull/1699) |

***

## Abstract

This SEP proposes changes to the Streamable HTTP transport in order to mitigate issues regarding long-running connections and resumability.

## Motivation

The Streamable HTTP transport spec [does not allow](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/04c6e1f0ea6544c7df307fb2d7c637efe34f58d3/docs/specification/draft/basic/transports.mdx?plain=1#L109-L111) servers to close a connection while computing a result. In other words, barring client-side disconnection, servers must maintain potentially long-running connections.

## Specification

When a server starts an SSE stream, it MUST immediately send an SSE event consisting of an [`id`](https://html.spec.whatwg.org/multipage/server-sent-events.html#:~:text=field%20name%20is%20%22id%22) and an empty [`data`](https://html.spec.whatwg.org/multipage/server-sent-events.html#:~:text=field%20name%20is%20%22data%22) string in order to prime the client to reconnect with that event ID as the `Last-Event-ID`.

Note that the SSE standard explicitly [permits setting `data` to an empty string](https://html.spec.whatwg.org/multipage/server-sent-events.html#:~:text=data%20buffer%20is%20an%20empty%20string), and says that the appropriate client-side handling is to record the `id` for `Last-Event-ID` but otherwise ignore the event (i.e., not call the event handler callback).

At any point after the server has sent an event ID to the client, the server MAY disconnect at will. Specifically, [this part of the MCP spec](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/04c6e1f0ea6544c7df307fb2d7c637efe34f58d3/docs/specification/draft/basic/transports.mdx?plain=1#L109-L111) will be changed from:

> The server **SHOULD NOT** close the SSE stream before sending the JSON-RPC *response* for the received JSON-RPC *request*

To:

> The server **MAY** close the connection before sending the JSON-RPC *response* if it has sent an SSE event with an event ID to the client

If a server disconnects, the client will interpret the disconnection the same as a network failure, and will attempt to reconnect. In order to prevent clients from reconnecting / polling excessively, the server SHOULD send an SSE event with a [`retry`](https://html.spec.whatwg.org/multipage/server-sent-events.html#:~:text=field%20name%20is%20%22retry%22) field indicating how long the client should wait before reconnecting. Clients MUST respect the `retry` field.

## Rationale

Servers may disconnect at will, avoiding long-running connections. Sending a `retry` field will prevent the client from hammering the server with inappropriate reconnection attempts.

## Backward Compatibility

* **New Client + Old Server**: No changes. No backward incompatibility.
* **Old Client + New Server**: Client should interpret an at-will disconnect the same as a network failure. `retry` field is part of the SSE standard. No backward incompatibility if client already implements proper SSE resuming logic.

## Additional Information

This SEP supersedes (in part) [SEP-1335](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1335).

