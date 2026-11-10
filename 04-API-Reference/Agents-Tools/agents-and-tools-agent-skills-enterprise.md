---
title: "Skills for enterprise - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-11-05T06:35:05Z"
tags: ["api", "enterprise", "security", "skills"]
---

# Skills for enterprise

Copy page



Governance, security review, evaluation, and organizational guidance for deploying Agent Skills at enterprise scale.

Copy page



This guide is for enterprise admins and architects who need to govern Agent Skills across an organization. It covers how to vet, evaluate, deploy, and manage Skills at scale. For authoring guidance, see [Skill authoring best practices](agents-and-tools-agent-skills-best-practices.md). For architecture details, see [Agent Skills](agents-and-tools-agent-skills-overview.md).

## Security review and vetting

Deploying Skills in an enterprise requires answering two distinct questions:

1.  **Are Skills safe in general?** See the [security considerations](agents-and-tools-agent-skills-overview.md#security-considerations) section in the overview for platform-level security details.
2.  **How do I vet a specific Skill?** Use the following risk assessment and review checklist.

### Risk tier assessment

Evaluate each Skill against these risk indicators before approving deployment:

| Risk indicator | What to look for | Concern level |
|----|----|----|
| Code execution | Scripts in the Skill directory (`*.py`, `*.sh`, `*.js`) | High: scripts run with full environment access |
| Instruction manipulation | Directives to ignore safety rules, hide actions from users, or alter Claude’s behavior conditionally | High: can bypass security controls |
| MCP server references | Instructions referencing MCP tools (`ServerName:tool_name`) | High: extends access beyond the Skill itself |
| Network access patterns | URLs, API endpoints, `fetch`, `curl`, or `requests` calls | High: potential data exfiltration vector |
| Hardcoded credentials | API keys, tokens, or passwords in Skill files or scripts | High: secrets exposed in Git history and context window |
| Filesystem access scope | Paths outside the Skill directory, broad glob patterns, path traversal (`../`) | Medium: might access unintended data |
| Tool calls | Instructions directing Claude to use bash, file operations, or other tools | Medium: review what operations are performed |

### Review checklist

Before deploying any Skill from a third party or internal contributor, complete these steps:

1.  **Read all Skill directory content.** Review `SKILL.md`, all referenced markdown files, and any bundled scripts or resources.
2.  **Verify script behavior matches stated purpose.** Run scripts in a sandboxed environment and confirm outputs align with the Skill’s description.
3.  **Check for adversarial instructions.** Look for directives that tell Claude to ignore safety rules, hide actions from users, exfiltrate data through responses, or alter behavior based on specific inputs.
4.  **Check for external URL fetches or network calls.** Search scripts and instructions for network access patterns (`http`, `requests.get`, `urllib`, `curl`, `fetch`).
5.  **Verify no hardcoded credentials.** Check for API keys, tokens, or passwords in Skill files. Credentials should use environment variables or secure credential stores, never appear in Skill content.
6.  **Identify tools and commands the Skill instructs Claude to run.** List all bash commands, file operations, and tool references. Consider the combined risk when a Skill uses both file-read and network tools together.
7.  **Confirm redirect destinations.** If the Skill references external URLs, verify they point to expected domains.
8.  **Verify no data exfiltration patterns.** Look for instructions that read sensitive data and then write, send, or encode it for external transmission, including through Claude’s conversational responses.



Never deploy Skills from untrusted sources without a full audit. A malicious Skill can direct Claude to run arbitrary code, access sensitive files, or transmit data externally. Treat Skill installation with the same rigor as installing software on production systems.

### Skill content scanning

Claude Enterprise organizations can turn on automated security scanning for custom Skills in claude.ai and Claude Cowork. The setting is **Skill and plugin security scanning** at [claude.ai \> Organization settings \> Skills](https://claude.ai/admin-settings/skills).

After you turn on the setting, scanning applies to Skills that members then upload or edit in claude.ai or Cowork. Each scan checks for signs of malicious behavior. These signs include hidden code execution, transfer of your data to an outside service, and instructions that tamper with Claude’s safeguards.

Whether a Skill is usable depends on its scan:

- A Skill that fails the scan is blocked from use.
- A Skill whose scan hasn’t completed is blocked from use.
- A Skill that passes with a warning stays usable behind a caution notice.

Organization owners can allow some Skills that failed the scan. So can members whose [custom role](../Other/manage-claude-user-management.md#custom-roles) can manage **Libraries**.

If scanning is available to your organization, turn it on. Scanning complements, but doesn’t replace, the [review checklist](#review-checklist).

Scanning doesn’t cover the Claude API. Skills you upload through the Skills API (`/v1/skills`), including from the Claude Console, aren’t scanned, so for API deployments, rely on the review checklist and [version pinning](#versioning-strategy). Scanning also doesn’t apply to Skills that were already in your organization when you turned it on, or to organizations with certain data handling configurations, such as customer-managed encryption keys (CMEK), zero data retention (ZDR), or HIPAA readiness. For setup steps, exclusions, and result types, see [Get started with skill and plugin scanning](../../15-Claude-AI-Features/get-started-with-skill-and-plugin-scanning.md) in the Claude Help Center.

## Evaluating Skills before deployment

Skills can degrade agent performance if they trigger incorrectly, conflict with other Skills, or provide poor instructions. Require evaluation before any production deployment.

### What to evaluate

Establish approval gates for these dimensions before deploying any Skill:

| Dimension | What it measures | Example failure |
|----|----|----|
| Triggering accuracy | Does the Skill activate for the right queries and stay inactive for unrelated ones? | Skill triggers on every spreadsheet mention, even when the user just wants to discuss data |
| Isolation behavior | Does the Skill work correctly on its own? | Skill references files that don’t exist in its directory |
| Coexistence | Does adding this Skill degrade other Skills? | New Skill’s description is too broad, stealing triggers from existing Skills |
| Instruction following | Does Claude follow the Skill’s instructions accurately? | Claude skips validation steps or uses wrong libraries |
| Output quality | Does the Skill produce correct, useful results? | Generated reports have formatting errors or missing data |

### Evaluation requirements

Require Skill authors to submit evaluation suites with 3–5 representative queries for each Skill, covering cases where the Skill should trigger, cases where it should not trigger, and ambiguous edge cases. Require testing across the models your organization uses (Haiku, Sonnet, Opus), because Skill effectiveness varies by model.

For detailed guidance on building evaluations, see [evaluation and iteration](agents-and-tools-agent-skills-best-practices.md#evaluation-and-iteration) in Skill authoring best practices. For general evaluation methodology, see [Define success criteria and build evaluations](../Test-Evaluate/test-and-evaluate-develop-tests.md).

### Using evaluations for lifecycle decisions

Evaluation results signal when to act:

- **Declining trigger accuracy:** Update the Skill’s description or instructions
- **Coexistence conflicts:** Consolidate overlapping Skills or narrow descriptions
- **Consistently low output quality:** Rewrite instructions or add validation steps
- **Persistent failures across updates:** Deprecate the Skill

## Skill lifecycle management

1.  1

    ### Plan

    Identify workflows that are repetitive or error-prone, or that require specialized knowledge. Map these to organizational roles and determine which are candidates for Skills.

2.  2

    ### Create and review

    Ensure the Skill author follows [best practices](agents-and-tools-agent-skills-best-practices.md). Require a security review using the [review checklist](#review-checklist). Require an evaluation suite before approval. Establish separation of duties: Skill authors should not be their own reviewers.

3.  3

    ### Test

    Require evaluations in isolation (Skill alone) and alongside existing Skills (coexistence testing). Verify triggering accuracy, output quality, and absence of regressions across your active Skill set before approving for production.

4.  4

    ### Deploy

    Upload through the Skills API for workspace-wide access. See [Using Agent Skills with the API](../Guides/build-with-claude-skills-guide.md) for upload and version management. Document the Skill in your internal registry with purpose, owner, and version.

5.  5

    ### Monitor

    Track usage patterns and collect feedback from users. Rerun evaluations periodically to detect drift or regressions as workflows and models evolve. Usage analytics are not currently available through the Skills API. Implement application-level logging to track which Skills are included in requests.

6.  6

    ### Iterate or deprecate

    Require the full evaluation suite to pass before promoting new versions. Update Skills when workflows change or evaluation scores decline. Deprecate Skills when evaluations consistently fail or the workflow is retired.

## Organizing Skills at scale

### Recall limits

As a general guideline, limit the number of Skills loaded simultaneously to maintain reliable recall accuracy. Each Skill’s metadata (name and description) competes for attention in the system prompt. With too many Skills active, Claude might fail to select the right Skill or miss relevant ones entirely. Use your evaluation suite to measure recall accuracy as you add Skills, and stop adding when performance degrades.

Note that API requests support a maximum of 20 Skills for each request (see [Using Agent Skills with the API](../Guides/build-with-claude-skills-guide.md)). If a role requires more Skills than a single request supports, consider consolidating narrow Skills into broader ones or routing requests to different Skill sets based on task type.

### Start specific, consolidate later

Encourage teams to start with narrow, workflow-specific Skills rather than broad, multipurpose ones. As patterns emerge across your organization, consolidate related Skills into role-based bundles.



Use evaluations to decide when to consolidate. Merge narrow Skills into a broader one only when the consolidated Skill’s evaluations confirm equivalent performance to the individual Skills it replaces.

**Example progression:**

- Start: `formatting-sales-reports`, `querying-pipeline-data`, `updating-crm-records`
- Consolidate: `sales-operations` (when evals confirm equivalent performance)

### Naming and cataloging

Use consistent naming conventions across your organization. The [naming conventions](agents-and-tools-agent-skills-best-practices.md#naming-conventions) section in best practices provides formatting guidance.

Maintain an internal registry for each Skill with:

- **Purpose:** What workflow the Skill supports
- **Owner:** Team or individual responsible for maintenance
- **Version:** Current deployed version
- **Dependencies:** MCP servers, packages, or external services required
- **Evaluation status:** Last evaluation date and results

### Role-based bundles

Group Skills by organizational role to keep each user’s active Skill set focused:

- **Sales team:** CRM operations, pipeline reporting, proposal generation
- **Engineering:** Code review, deployment workflows, incident response
- **Finance:** Report generation, data validation, audit preparation

Each role-based bundle should contain only the Skills relevant to that role’s daily workflows.

## Distribution and version control

### Source control

Store Skill directories in Git for history tracking, code review through pull requests, and rollback capability. Each Skill directory (containing `SKILL.md` and any bundled files) maps naturally to a Git-tracked folder.

### API-based distribution

The Skills API provides workspace-scoped distribution. Skills uploaded through the API are available to all workspace members. See [Using Agent Skills with the API](../Guides/build-with-claude-skills-guide.md) for upload, versioning, and management endpoints.

### Versioning strategy

- **Production:** Pin Skills to specific versions. If you omit `version`, requests use the latest version, so a new version uploaded by anyone in the workspace immediately changes what production agents run. Run the full evaluation suite before promoting a new version. Treat every update as a new deployment requiring full security review.
- **Development and testing:** Use latest versions to validate changes before production promotion.
- **Rollback plan:** Maintain the previous version as a fallback. If a new version fails evaluations in production, revert to the last known-good version immediately.
- **Integrity verification:** Compute checksums of reviewed Skills and verify them at deployment time. Use signed commits in your Skill repository to ensure provenance.

### Cross-surface considerations



Custom Skills do not sync across surfaces. Skills uploaded to the API are not available on claude.ai or in Claude Code, and vice versa. Each surface requires separate uploads and management.

Maintain Skill source files in Git as the single source of truth. If your organization deploys Skills across multiple surfaces, implement your own synchronization process to keep them consistent. For full details, see [cross-surface availability](agents-and-tools-agent-skills-overview.md#cross-surface-availability).

## Next steps



[Agent Skills](agents-and-tools-agent-skills-overview.md)

Architecture and platform details



[Skill authoring best practices](agents-and-tools-agent-skills-best-practices.md)

Authoring guidance for Skill creators



[Using Agent Skills with the API](../Guides/build-with-claude-skills-guide.md)

Upload and manage Skills programmatically
