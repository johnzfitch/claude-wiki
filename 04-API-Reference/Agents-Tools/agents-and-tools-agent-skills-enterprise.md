---
title: "Skills for enterprise - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:11Z"
tags: ["api", "enterprise", "security", "skills"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fagent-skills%2Fenterprise)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](../Guides/build-with-claude-overview.md)[Using the Messages API](../Guides/build-with-claude-working-with-messages.md)[Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md)[Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md)[Fallback credit](../Guides/build-with-claude-fallback-credit.md)

Model capabilities

[Effort](../Guides/build-with-claude-effort.md)[Task budgets (beta)](../Guides/build-with-claude-task-budgets.md)[Fast mode (research preview)](../Guides/build-with-claude-fast-mode.md)[Structured outputs](../Guides/build-with-claude-structured-outputs.md)[Citations](../Guides/build-with-claude-citations.md)[Streaming Messages](../Guides/build-with-claude-streaming.md)[Batch processing](../Guides/build-with-claude-batch-processing.md)[Search results](../Guides/build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](../Guides/build-with-claude-multilingual-support.md)[Embeddings](../Guides/build-with-claude-embeddings.md)

[Thinking](../Guides/build-with-claude-thinking.md)

Tools

[Overview](agents-and-tools-tool-use-overview.md)[How tool use works](agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](agents-and-tools-tool-use-tool-runner.md)[Strict tool use](agents-and-tools-tool-use-strict-tool-use.md)[Server tools](agents-and-tools-tool-use-server-tools.md)[Web search tool](agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](agents-and-tools-tool-use-memory-tool.md)[Bash tool](agents-and-tools-tool-use-bash-tool.md)[Text editor tool](agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](agents-and-tools-tool-use-tool-reference.md)[Manage tool context](agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](../Guides/build-with-claude-context-windows.md)[Context editing](../Guides/build-with-claude-context-editing.md)[Prompt caching](../Guides/build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](../Guides/build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](../Guides/build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md)[Token counting](../Guides/build-with-claude-token-counting.md)

[Compaction](../Guides/build-with-claude-compaction.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](agents-and-tools-agent-skills-overview.md)[Quickstart](agents-and-tools-agent-skills-quickstart.md)[Best practices](agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](agents-and-tools-agent-skills-enterprise.md)[Skills in the API](../Guides/build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](agents-and-tools-remote-mcp-servers.md)[MCP connector](agents-and-tools-mcp-connector.md)

[MCP tunnels](agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](../Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)[Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Skills

# Skills for enterprise

Copy page



Governance, security review, evaluation, and organizational guidance for deploying Agent Skills at enterprise scale.

Copy page



This guide is for enterprise admins and architects who need to govern Agent Skills across an organization. It covers how to vet, evaluate, deploy, and manage Skills at scale. For authoring guidance, see [best practices](agents-and-tools-agent-skills-best-practices.md). For architecture details, see the [Skills overview](agents-and-tools-agent-skills-overview.md).

## Security review and vetting

Deploying Skills in an enterprise requires answering two distinct questions:

1.  **Are Skills safe in general?** See the [security considerations](agents-and-tools-agent-skills-overview.md#security-considerations) section in the overview for platform-level security details.
2.  **How do I vet a specific Skill?** Use the following risk assessment and review checklist.

### Risk tier assessment

Evaluate each Skill against these risk indicators before approving deployment:

| Risk indicator           | What to look for                                                                                     | Concern level                                           |
|--------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Code execution           | Scripts in the Skill directory (`*.py`, `*.sh`, `*.js`)                                              | High: scripts run with full environment access          |
| Instruction manipulation | Directives to ignore safety rules, hide actions from users, or alter Claude's behavior conditionally | High: can bypass security controls                      |
| MCP server references    | Instructions referencing MCP tools (`ServerName:tool_name`)                                          | High: extends access beyond the Skill itself            |
| Network access patterns  | URLs, API endpoints, `fetch`, `curl`, or `requests` calls                                            | High: potential data exfiltration vector                |
| Hardcoded credentials    | API keys, tokens, or passwords in Skill files or scripts                                             | High: secrets exposed in Git history and context window |
| Filesystem access scope  | Paths outside the Skill directory, broad glob patterns, path traversal (`../`)                       | Medium: may access unintended data                      |
| Tool invocations         | Instructions directing Claude to use bash, file operations, or other tools                           | Medium: review what operations are performed            |

### Review checklist

Before deploying any Skill from a third party or internal contributor, complete these steps:

1.  **Read all Skill directory content.** Review SKILL.md, all referenced markdown files, and any bundled scripts or resources.
2.  **Verify script behavior matches stated purpose.** Run scripts in a sandboxed environment and confirm outputs align with the Skill's description.
3.  **Check for adversarial instructions.** Look for directives that tell Claude to ignore safety rules, hide actions from users, exfiltrate data through responses, or alter behavior based on specific inputs.
4.  **Check for external URL fetches or network calls.** Search scripts and instructions for network access patterns (`http`, `requests.get`, `urllib`, `curl`, `fetch`).
5.  **Verify no hardcoded credentials.** Check for API keys, tokens, or passwords in Skill files. Credentials should use environment variables or secure credential stores, never appear in Skill content.
6.  **Identify tools and commands the Skill instructs Claude to invoke.** List all bash commands, file operations, and tool references. Consider the combined risk when a Skill uses both file-read and network tools together.
7.  **Confirm redirect destinations.** If the Skill references external URLs, verify they point to expected domains.
8.  **Verify no data exfiltration patterns.** Look for instructions that read sensitive data and then write, send, or encode it for external transmission, including through Claude's conversational responses.



Never deploy Skills from untrusted sources without a full audit. A malicious Skill can direct Claude to execute arbitrary code, access sensitive files, or transmit data externally. Treat Skill installation with the same rigor as installing software on production systems.

### Skill content scanning

Claude Enterprise organizations can turn on automated security scanning for custom Skills in claude.ai and Claude Cowork. After you turn on **Skill and plugin security scanning** at [claude.ai \> Organization settings \> Skills](https://claude.ai/admin-settings/skills), Skills that members then upload or edit in claude.ai or Cowork are scanned for signs of malicious behavior, such as hidden code execution, sending your data to an outside service, or instructions that tamper with Claude's safeguards. A Skill that fails the scan, or whose scan hasn't finished, is blocked from use. A Skill that passes with a warning stays usable behind a caution notice. If scanning is available to your organization, turn it on. It complements, but doesn't replace, the [review checklist](#review-checklist).

Scanning doesn't cover the Claude API. Skills you upload through the Skills API (`/v1/skills`), including from the Claude Console, aren't scanned, so for API deployments, rely on the review checklist and [version pinning](#versioning-strategy). Scanning also doesn't apply to Skills that were already in your organization when you turned it on, or to organizations with certain data handling configurations, such as customer-managed encryption keys (CMEK), zero data retention (ZDR), or HIPAA readiness. For setup steps, exclusions, and result types, see [Get started with skill and plugin scanning](../../02-Claude-Code-CLI/get-started-with-skill-and-plugin-scanning.md) in the Claude Help Center.

## Evaluating Skills before deployment

Skills can degrade agent performance if they trigger incorrectly, conflict with other Skills, or provide poor instructions. Require evaluation before any production deployment.

### What to evaluate

Establish approval gates for these dimensions before deploying any Skill:

| Dimension             | What it measures                                                                    | Example failure                                                                            |
|-----------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Triggering accuracy   | Does the Skill activate for the right queries and stay inactive for unrelated ones? | Skill triggers on every spreadsheet mention, even when the user just wants to discuss data |
| Isolation behavior    | Does the Skill work correctly on its own?                                           | Skill references files that don't exist in its directory                                   |
| Coexistence           | Does adding this Skill degrade other Skills?                                        | New Skill's description is too broad, stealing triggers from existing Skills               |
| Instruction following | Does Claude follow the Skill's instructions accurately?                             | Claude skips validation steps or uses wrong libraries                                      |
| Output quality        | Does the Skill produce correct, useful results?                                     | Generated reports have formatting errors or missing data                                   |

### Evaluation requirements

Require Skill authors to submit evaluation suites with 3–5 representative queries per Skill, covering cases where the Skill should trigger, should not trigger, and ambiguous edge cases. Require testing across the models your organization uses (Haiku, Sonnet, Opus), because Skill effectiveness varies by model.

For detailed guidance on building evaluations, see [evaluation and iteration](agents-and-tools-agent-skills-best-practices.md#evaluation-and-iteration) in best practices. For general evaluation methodology, see [develop test cases](../Test-Evaluate/test-and-evaluate-develop-tests.md).

### Using evaluations for lifecycle decisions

Evaluation results signal when to act:

- **Declining trigger accuracy:** Update the Skill's description or instructions
- **Coexistence conflicts:** Consolidate overlapping Skills or narrow descriptions
- **Consistently low output quality:** Rewrite instructions or add validation steps
- **Persistent failures across updates:** Deprecate the Skill

## Skill lifecycle management

1.  1

    ### Plan

    Identify workflows that are repetitive, error-prone, or require specialized knowledge. Map these to organizational roles and determine which are candidates for Skills.

2.  2

    ### Create and review

    Ensure the Skill author follows [best practices](agents-and-tools-agent-skills-best-practices.md). Require a security review using the [review checklist](#review-checklist). Require an evaluation suite before approval. Establish separation of duties: Skill authors should not be their own reviewers.

3.  3

    ### Test

    Require evaluations in isolation (Skill alone) and alongside existing Skills (coexistence testing). Verify triggering accuracy, output quality, and absence of regressions across your active Skill set before approving for production.

4.  4

    ### Deploy

    Upload through the Skills API for workspace-wide access. See [Using Skills with the API](../Guides/build-with-claude-skills-guide.md) for upload and version management. Document the Skill in your internal registry with purpose, owner, and version.

5.  5

    ### Monitor

    Track usage patterns and collect feedback from users. Rerun evaluations periodically to detect drift or regressions as workflows and models evolve. Usage analytics are not currently available through the Skills API. Implement application-level logging to track which Skills are included in requests.

6.  6

    ### Iterate or deprecate

    Require the full evaluation suite to pass before promoting new versions. Update Skills when workflows change or evaluation scores decline. Deprecate Skills when evaluations consistently fail or the workflow is retired.

## Organizing Skills at scale

### Recall limits

As a general guideline, limit the number of Skills loaded simultaneously to maintain reliable recall accuracy. Each Skill's metadata (name and description) competes for attention in the system prompt. With too many Skills active, Claude may fail to select the right Skill or miss relevant ones entirely. Use your evaluation suite to measure recall accuracy as you add Skills, and stop adding when performance degrades.

Note that API requests support a maximum of 20 Skills for each request (see [Using Skills with the API](../Guides/build-with-claude-skills-guide.md)). If a role requires more Skills than a single request supports, consider consolidating narrow Skills into broader ones or routing requests to different Skill sets based on task type.

### Start specific, consolidate later

Encourage teams to start with narrow, workflow-specific Skills rather than broad, multipurpose ones. As patterns emerge across your organization, consolidate related Skills into role-based bundles.



Use evaluations to decide when to consolidate. Merge narrow Skills into a broader one only when the consolidated Skill's evaluations confirm equivalent performance to the individual Skills it replaces.

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

Group Skills by organizational role to keep each user's active Skill set focused:

- **Sales team:** CRM operations, pipeline reporting, proposal generation
- **Engineering:** Code review, deployment workflows, incident response
- **Finance:** Report generation, data validation, audit preparation

Each role-based bundle should contain only the Skills relevant to that role's daily workflows.

## Distribution and version control

### Source control

Store Skill directories in Git for history tracking, code review through pull requests, and rollback capability. Each Skill directory (containing SKILL.md and any bundled files) maps naturally to a Git-tracked folder.

### API-based distribution

The Skills API provides workspace-scoped distribution. Skills uploaded through the API are available to all workspace members. See [Using Skills with the API](../Guides/build-with-claude-skills-guide.md) for upload, versioning, and management endpoints.

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

[Agent Skills overview](agents-and-tools-agent-skills-overview.md)

Architecture and platform details



[Best practices](agents-and-tools-agent-skills-best-practices.md)

Authoring guidance for Skill creators



[Using Skills with the API](../Guides/build-with-claude-skills-guide.md)

Upload and manage Skills programmatically
