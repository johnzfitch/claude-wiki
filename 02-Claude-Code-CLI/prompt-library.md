---
title: "Prompt library - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/prompt-library"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-26T06:38:06Z"
tags: ["claude-code", "prompting"]
---

## On this page

- [What makes these prompts work](#what-makes-these-prompts-work)
- [Where these come from](#where-these-come-from)
- [Related resources](#related-resources)

Use Claude Code

# Prompt library

Copy pageCopy page

Copy-paste prompts for Claude Code, tagged by task and role.

Copy pageCopy page

This is a library of prompts to copy into Claude Code. Use it to explore ways of working you haven’t tried, or when you’re not sure where to start. The prompts are collected from various Anthropic guides, including [Common workflows](common-workflows.md), [Best practices](best-practices.md), and [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code). They’re starting points rather than scripts. Open **Why this works** under any prompt to see the pattern behind it so you can write your own.


[​](#what-makes-these-prompts-work)

What makes these prompts work

The prompts above share a few patterns. Recognizing them helps you adapt any prompt here to your own task. **Describe the outcome, not the steps.** Say what you want and let Claude find the files. The prompt below works without naming a single file path.

```python
add rate limiting to the public API and make sure existing tests still pass
```

**Give it a way to check its own work.** Ask for run, test, compare, or verify in the same prompt so Claude iterates instead of stopping after one attempt. To check the finished change against the running app, run [`/verify`](../08-Plugins-Skills/skills.md#run-and-verify-your-app).

```python
write the migration, run it against the dev database, and confirm the schema matches
```

**Point at a reference.** Name an existing file, test, or pattern to match so the new code is consistent with what you already have.

```python
add a settings page that follows the same layout as the profile page
```

**State the measurable target.** When the goal is performance or coverage, give the metric and threshold so completion is unambiguous.

```python
get the bundle size under 200KB and show me what you removed
```

**Give it the artifact.** Paste errors, logs, screenshots, and plan output directly in the prompt, or type `@` to reference a file. Claude reads the source instead of your description of it.

```python
why is the build failing? @build.log
```

**Say how you want the answer.** Name the format, length, or audience so the explanation fits how you’ll use it. To make a format the default for every response, set an [output style](output-styles.md).

```python
explain how the payment retry logic works as an HTML page with a diagram, then open it in my browser
```

For more on each pattern, see [best practices](best-practices.md).


[​](#where-these-come-from)

Where these come from

These prompts are based on patterns from published Anthropic resources. Each card links to its source:

- [Common workflows](common-workflows.md): step-by-step guides for the core tasks
- [Best practices](best-practices.md): prompting patterns and project setup
- [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code): real workflows from engineering, product, design, and data teams, with deep dives on [legal](https://claude.com/blog/how-anthropic-uses-claude-legal), [marketing](https://claude.com/blog/how-anthropic-uses-claude-marketing), and [cybersecurity](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity)
- [Scaling agentic coding guide](https://resources.anthropic.com/hubfs/Scaling%20agentic%20coding%20across%20your%20organization.pdf): the enterprise adoption guide

For video walkthroughs of these patterns, see the free [Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action) course on [Claude Academy](https://academy.claude.com/).


[​](#related-resources)

Related resources

The prompts on this page are starting points. Once one works for your project, the next step is making it repeatable: save it as a [skill](../08-Plugins-Skills/skills.md) so anyone on your team can run it as a `/command`, and record the conventions Claude learned in [CLAUDE.md](memory.md) so every session starts with that context instead of Claude relearning it. For larger or riskier changes, [plan mode](permission-modes.md#analyze-before-you-edit-with-plan-mode) shows you the file list before any edits happen. If you’re introducing Claude Code across a team, see [administration](../13-Enterprise-Admin/admin-setup.md) for managed settings and policy, and [costs and usage](../17-Billing-Plans/costs.md) for how this work is billed on your plan.
