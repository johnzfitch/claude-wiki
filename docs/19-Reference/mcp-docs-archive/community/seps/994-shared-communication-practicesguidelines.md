---
source: https://modelcontextprotocol.io/community/seps/994-shared-communication-practicesguidelines.md
downloaded: 2026-02-02T05:34:26.231987
---

> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SEP-994: Shared Communication Practices/Guidelines

> Shared Communication Practices/Guidelines

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
  <Badge color="gray">Process</Badge>
</div>

| Field         | Value                                     |
| ------------- | ----------------------------------------- |
| **SEP**       | 994                                       |
| **Title**     | Shared Communication Practices/Guidelines |
| **Status**    | Final                                     |
| **Type**      | Process                                   |
| **Created**   | 2025-07-17                                |
| **Author(s)** | [@localden](https://github.com/localden)  |
| **Sponsor**   | None                                      |
| **PR**        | [#994](#1002)                             |

***

## Abstract

This SEP establishes the communication strategy and framework for the Model Context Protocol community. It defines the official channels for contributor communication, guidelines for their use, and processes for decision documentation.

## Motivation

As the MCP community grows, clear communication guidelines are essential for:

* **Consistency**: Ensuring all contributors know where and how to communicate
* **Transparency**: Making project decisions visible and accessible
* **Efficiency**: Directing discussions to the most appropriate channels
* **Security**: Establishing proper processes for handling sensitive issues

## Specification

### Communication Channels

The MCP project uses three primary communication channels:

1. **Discord**: For real-time or ad-hoc discussions among contributors
2. **GitHub Discussions**: For structured, longer-form discussions
3. **GitHub Issues**: For actionable tasks, bug reports, and feature requests

Security-sensitive issues follow a separate process defined in SECURITY.md.

### Discord Guidelines

The Discord server is designed for **MCP contributors** and is not intended for general MCP support.

#### Public Channels (Default)

* Open community engagement and collaborative development
* SDK and tooling development discussions
* Working and Interest Group discussions
* Community onboarding and contribution guidance
* Office hours and maintainer availability

#### Private Channels (Exceptions)

Private channels are reserved for:

* Security incidents (CVEs, protocol vulnerabilities)
* People matters (maintainer discussions, code of conduct)
* Coordination requiring immediate focused response

All technical and governance decisions must be documented publicly in GitHub.

### GitHub Discussions

Used for structured, long-form discussion:

* Project roadmap planning
* Announcements and release communications
* Community polls and consensus-building
* Feature requests with context and rationale

### GitHub Issues

Used for actionable items:

* Bug reports with reproducible steps
* Documentation improvements
* CI/CD and infrastructure issues
* Release tasks and milestone tracking

### Decision Records

All MCP decisions are documented publicly:

* **Technical decisions**: GitHub Issues and SEPs
* **Specification changes**: Changelog on the MCP website
* **Process changes**: Community documentation
* **Governance decisions**: GitHub Issues and SEPs

Decision documentation includes:

* Decision makers
* Background context and motivation
* Options considered
* Rationale for chosen approach
* Implementation steps

## Rationale

This framework balances openness with practicality:

* **Public by default**: Maximizes transparency and community participation
* **Private when necessary**: Protects security and personal matters
* **Channel separation**: Keeps discussions organized and searchable
* **Documentation requirements**: Ensures decisions are preserved and discoverable

## Backward Compatibility

This SEP establishes new processes and does not affect existing protocol functionality.

## Reference Implementation

The communication guidelines are published at: [https://modelcontextprotocol.io/community/communication](https://modelcontextprotocol.io/community/communication)

