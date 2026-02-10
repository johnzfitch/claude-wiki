---
source: https://modelcontextprotocol.io/community/seps/1850-pr-based-sep-workflow.md
downloaded: 2026-02-02T05:34:34.388280
---

> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SEP-1850: PR-Based SEP Workflow

> PR-Based SEP Workflow

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

| Field         | Value                                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------------ |
| **SEP**       | 1850                                                                                                               |
| **Title**     | PR-Based SEP Workflow                                                                                              |
| **Status**    | Final                                                                                                              |
| **Type**      | Process                                                                                                            |
| **Created**   | 2025-11-20                                                                                                         |
| **Accepted**  | 2025-11-28, 8 Yes, 0 No, 0 Absent per vote in Discord.                                                             |
| **Author(s)** | Nick Cooper ([@nickcoai](https://github.com/nickcoai)), David Soria Parra ([@davidsp](https://github.com/davidsp)) |
| **Sponsor**   | David Soria Parra ([@davidsp](https://github.com/davidsp))                                                         |
| **PR**        | [#1850](https://github.com/modelcontextprotocol/specification/pull/1850)                                           |

***

## Abstract

This SEP formalizes the pull request-based SEP workflow that stores proposals as markdown files in the `seps/` directory of the Model Context Protocol specification repository. The workflow assigns SEP numbers from pull request numbers, maintains version history in Git, and replaces the previous GitHub Issues-based process. This establishes a file-based approach as the canonical way to author, review, and accept SEPs.

## Motivation

The issue-based SEP process introduced several challenges:

* **Dispersed content**: Proposal content was scattered across GitHub issues, linked documents, and pull requests, making review and archival difficult.
* **Difficult collaboration**: Maintaining long-form specifications in issue bodies made iterative edits and multi-contributor collaboration harder.
* **Limited version control**: GitHub issues don't provide the same version control capabilities as Git-managed files.
* **Unclear status management**: The process lacked clear mechanisms for tracking status transitions and ensuring consistency between different sources of truth.

A file-based workflow addresses these issues by:

* Keeping every SEP in version control alongside the specification itself
* Providing Git's built-in review tooling, history, and searchability
* Linking SEP numbers to pull requests to eliminate manual bookkeeping
* Surfacing all discussion in the pull request thread
* Using PR labels in conjunction with file status for better discoverability

## Specification

### 1. Canonical Location

* Every SEP lives in `seps/{NUMBER}-{slug}.md` in the specification repository
* The SEP number is always the pull request number that introduces the SEP file
* The `seps/` directory serves as the single source of truth for all SEPs

### 2. Author Workflow

1. **Draft the proposal** in `seps/0000-{slug}.md` using `0000` as a placeholder number
2. **Open a pull request** containing the draft SEP and any supporting materials
3. **Request a sponsor** from the Maintainers list; tag potential sponsors from [MAINTAINERS.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md)
4. **After the PR number is known**, amend the commit to rename the file to `{PR-number}-{slug}.md` and update the header (`SEP-{PR-number}` and `PR: #{PR-number}`)
5. **Wait for sponsor assignment**: Once a sponsor agrees, they will assign themselves and update the status to `Draft`

### 3. Sponsor Responsibilities

A Sponsor is a Core Maintainer or Maintainer who champions the SEP through the review process. The sponsor's responsibilities include:

* **Reviewing the proposal** and providing constructive feedback
* **Requesting changes** based on community input
* **Managing status transitions** by:
  * Ensuring that the `Status` field in the SEP markdown file is accurate
  * Applying matching PR labels to keep them in sync with the file status
  * Communicating status changes via PR comments
* **Initiating formal review** when the SEP is ready (moving from `Draft` to `In-Review`)
* **Raising to Core-Maintainers** ensuring the SEP is presented at the Core Maintainer meeting and that author and sponsor present.
* **Ensuring quality standards** are met before advancing the proposal
* **Tracking implementation** progress and ensuring reference implementations are complete before `Final` status

### 4. Review Flow

Status progression follows: `Draft → In-Review → Accepted → Final`

Additional terminal states: `Rejected`, `Withdrawn`, `Superseded`, `Dormant`

**Dormant status**: If a SEP does not find a sponsor within six months, Core Maintainers may close the PR and mark the SEP as `dormant`.

Reference implementations must be tracked via linked pull requests or issues and must be complete before marking a SEP as `Final`.

### 5. Documentation

* `docs/community/sep-guidelines.mdx` serves as the contributor-facing instructions
* `seps/README.md` provides the concise reference for formatting, naming, sponsor responsibilities, and acceptance criteria
* Both documents must reflect this workflow and be kept in sync

### 6. SEP File Structure

Each SEP must include:

```markdown  theme={null}
# SEP-{NUMBER}: {Title}

- **Status**: Draft | In-Review | Accepted | Rejected | Withdrawn | Final | Superseded | Dormant
- **Type**: Standards Track | Informational | Process
- **Created**: YYYY-MM-DD
- **Author(s)**: Name <email> (@github-username)
- **Sponsor**: @github-username (or "None" if seeking sponsor)
- **PR**: https://github.com/modelcontextprotocol/specification/pull/{NUMBER}

## Abstract

## Motivation

## Specification

## Rationale

## Backward Compatibility

## Security Implications

## Reference Implementation
```

### 7. Status Management via PR Labels

To improve discoverability and filtering:

* Sponsors must apply PR labels that match the SEP status (`draft`, `in-review`, `accepted`, `final`, etc.)
* Both the markdown `Status` field and PR labels should be kept in sync
* The markdown file serves as the canonical record (versioned with the proposal)
* PR labels enable easy filtering and searching for SEPs by status
* Only sponsors should modify status fields and labels; authors should request changes through their sponsor

### 8. Legacy Considerations

* Contributors may optionally open a GitHub Issue for early discussion, but the authoritative SEP text lives in `seps/`
* Issues should link to the relevant file once a pull request exists
* SEP numbers are derived from PR numbers, not issue numbers

## Rationale

### Why File-Based?

Storing SEPs as files keeps authoritative specs versioned with the code, mirroring successful processes used by PEPs (Python Enhancement Proposals) and other standards bodies. This approach:

* Provides built-in version control via Git
* Enables standard code review workflows
* Maintains clear history of all changes
* Supports multi-contributor collaboration
* Integrates naturally with the specification repository

### Why PR Numbers?

Using pull request numbers:

* Eliminates race conditions around manual numbering
* Creates natural traceability between proposal and discussion
* Prevents number conflicts
* Simplifies the contribution process
* Maintains a single discussion thread for review

### Why PR Labels?

Adding PR labels alongside the file status:

* Enables quick filtering of SEPs by status without opening files
* Provides immediate visibility of SEP states in PR lists
* Supports GitHub's search and filter capabilities
* Complements the canonical markdown status field
* Reduces friction for maintainers managing multiple SEPs

### Making This the Primary Process

Maintaining two overlapping canonical processes risked divergence and created confusion for contributors. Establishing the file-based approach as the primary method:

* Reduces cognitive overhead for new contributors
* Ensures consistency in the SEP corpus
* Simplifies maintenance for sponsors
* Aligns with industry best practices

## Backward Compatibility

* Existing issue-based SEPs remain valid and require no migration
* Historical GitHub Issue links continue to work
* Future SEPs should reference the new file locations in `seps/`
* Maintainers may optionally backfill historical SEPs into `seps/` for archival purposes

## Security Implications

No new security considerations beyond the standard code review process for pull requests.

## Reference Implementation

* This pull request (#1850) implements the canonical instructions in both `seps/README.md` and `docs/community/sep-guidelines.mdx`
* The process has been updated to reflect the PR-based workflow with status management via labels
* This SEP document itself serves as an example of the new format

# Vote

This SEP was accepted unanimously by the MCP Core Maintainers with a vote of 8 yes's, 0 no's and 0 absent votes on Friday December 28th, 2025 in a Discord poll.

