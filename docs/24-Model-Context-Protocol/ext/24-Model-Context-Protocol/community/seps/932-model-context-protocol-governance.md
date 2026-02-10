---
source: https://modelcontextprotocol.io/community/seps/932-model-context-protocol-governance.md
downloaded: 2026-02-02T05:34:22.846458
---

> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SEP-932: Model Context Protocol Governance

> Model Context Protocol Governance

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

| Field         | Value                             |
| ------------- | --------------------------------- |
| **SEP**       | 932                               |
| **Title**     | Model Context Protocol Governance |
| **Status**    | Final                             |
| **Type**      | Process                           |
| **Created**   | 2025-07-08                        |
| **Author(s)** | David Soria Parra                 |
| **Sponsor**   | None                              |
| **PR**        | [#932](#931)                      |

***

## Abstract

This SEP establishes the formal governance model for the Model Context Protocol (MCP) project. It defines the organizational structure, decision-making processes, and contribution guidelines necessary for transparent and effective project stewardship. The proposal introduces a hierarchical governance structure with clear roles and responsibilities, along with the Specification Enhancement Proposal (SEP) process for managing protocol changes.

## Motivation

As the Model Context Protocol grows in adoption and complexity, the need for formal governance becomes critical. The current informal decision-making process lacks:

1. **Transparency**: Community members have no clear visibility into how decisions are made
2. **Participation Pathways**: Contributors lack defined ways to influence project direction
3. **Accountability**: No formal structure exists for resolving disputes or contentious issues
4. **Scalability**: Ad-hoc processes cannot scale with growing community and technical complexity

Without formal governance, the project risks:

* Fragmentation of the ecosystem
* Unclear or inconsistent technical decisions
* Reduced community trust and participation
* Inability to effectively manage contributions at scale

## Rationale

The proposed governance model draws inspiration from successful open source projects like Python, PyTorch, and Rust. Key design decisions include:

### Hierarchical Structure

We chose a hierarchical model (Contributors → Maintainers → Core Maintainers → Lead Maintainers) that is effectively how the project decisions are made today. From there we will continue to evolve governance in the best interest of the project.

### Individual vs Corporate Membership

Membership is explicitly tied to individuals rather than companies to:

* Ensure decisions prioritize protocol integrity over corporate interests
* Prevent capture by any single organization
* Maintain continuity when individuals change employers

### SEP Process

The Specification Enhancement Proposal process ensures:

* All protocol changes undergo thorough review
* Community input is systematically collected
* Design decisions are documented for posterity
* Implementation precedes finalization

## Specification

### Governance Structure

#### Contributors

* Any individual who files issues, submits pull requests, or participates in discussions
* No formal membership or approval required

#### Maintainers

* Responsible for specific components (SDKs, documentation, etc.)
* Appointed by Core Maintainers
* Have write/admin access to their repositories
* May establish component-specific processes

#### Core Maintainers

* Deep understanding of MCP specification required
* Responsible for protocol evolution and project direction
* Meet bi-weekly for decisions
* Can veto maintainer decisions by majority vote
* Current members listed in governance documentation

#### Lead Maintainers

* Justin Spahr-Summers and David Soria Parra
* Can veto any decision
* Appoint/remove Core Maintainers
* Admin access to all infrastructure

## Backwards Compatibility

N/A

## Reference Implementation

See #931

1. **Documentation Files**:
   * `/docs/community/governance.mdx` - Full governance documentation
   * `/docs/community/sep-guidelines.mdx` - SEP process guidelines

## Security Implications

N/A

