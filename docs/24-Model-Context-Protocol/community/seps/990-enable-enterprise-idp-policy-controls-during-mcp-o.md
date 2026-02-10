---
source: https://modelcontextprotocol.io/community/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md
downloaded: 2026-02-02T05:34:25.101309
---

> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SEP-990: Enable enterprise IdP policy controls during MCP OAuth flows

> Enable enterprise IdP policy controls during MCP OAuth flows

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

| Field         | Value                                                        |
| ------------- | ------------------------------------------------------------ |
| **SEP**       | 990                                                          |
| **Title**     | Enable enterprise IdP policy controls during MCP OAuth flows |
| **Status**    | Final                                                        |
| **Type**      | Standards Track                                              |
| **Created**   | 2025-06-04                                                   |
| **Author(s)** | Aaron Parecki ([@aaronpk](https://github.com/aaronpk))       |
| **Sponsor**   | None                                                         |
| **PR**        | [#990](#646)                                                 |

***

## Abstract

This extension is designed to facilitate secure and interoperable authorization of MCP clients within corporate environments, leveraging existing enterprise identity infrastructure.

* For end users, this removes the need to manually connect and authorize the MCP Client to individual services within the organization.
* For enterprise admins, this enables visibility and control over which MCP Servers are able to be used within the organization.

## How Has This Been Tested?

We have an end to end implementation of this [here](https://github.com/oktadev/okta-cross-app-access-mcp), and in-progress MCP implementations with some partners.

## Breaking Changes

This is designed to augment the existing OAuth profile by providing an alternative when used under an enterprise IdP. MCP clients can opt in to this profile when necessary.

## Additional Context

For more background on this problem, you can refer to my blog post about this here:

[Enterprise-Ready MCP](https://aaronparecki.com/2025/05/12/27/enterprise-ready-mcp)

I also presented this at the MCP Dev Summit in May.

A high level overview of the flow is below:

```mermaid  theme={null}
sequenceDiagram
    participant UA as Browser
    participant C as MCP Client
    participant MAS as MCP Authorization Server
    participant MRS as MCP Resource Server
    participant IdP as Identity Provider

    rect rgb(255,255,225)
    C-->>UA: Redirect to IdP
    UA->>+IdP: Redirect to IdP
    Note over IdP: User Logs In
    IdP-->>-UA: IdP Authorization Code
    UA->>C: IdP Authorization Code
    C->>+IdP: Token Request with IdP Authorization Code
    IdP-->-C: ID Token
    end

    note over C: User is logged<br>in to MCP Client.<br>Client stores ID Token.

    C->+IdP: Exchange ID Token for ID-JAG
    note over IdP: Evaluate Policy
    IdP-->-C: Responds with ID-JAG
    C->+MAS: Token Request with ID-JAG
    note over MAS: Validate ID-JAG
    MAS-->-C: MCP Access Token

    loop
    C->>+MRS: Call MCP API with Access Token
    MRS-->>-C: MCP Response with Data
    end
```

> \[!IMPORTANT]
> **State:** Ready to Review

