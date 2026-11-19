---
title: "Claude Security | Fix vulnerabilities with AI cybersecurity"
source_url: "https://www.claude.com/product/claude-security"
category: "15-Claude-AI-Features"
fetched_at: "2026-11-18T06:29:34Z"
tags: ["claude-ai", "security"]
---

# Claude Security

From scan to fix, done seamlessly

Claude scans your codebase with Claude Mythos, validates findings, and suggests patches you can review and approve. Available in public beta for Claude Enterprise.

[Contact sales](https://www.claude.com/contact-sales)[Read the tutorial](https://academy.claude.com/tutorials/getting-started-with-claude-security)

## How teams use Claude Security

Claude reasons through your code like a skilled security researcher. It understands context, traces data flows, and catches vulnerabilities that pattern-matching tools miss. Then it suggests and tracks fixes.

### Keep up with your code

Claude runs a deep first scan, then keeps scanning as your code changes. It traces data flows across files and repositories to find vulnerabilities traditional scanners might not detect.

### Validate findings

Every finding passes adversarial verification before it reaches your team. A threat model your team can edit decides what’s worth flagging.

### Review, fix, and track

Every finding includes a recommended patch for your team to review and approve. Claude marks it fixed once the fix ships, so vulnerabilities get closed instead of piling up in a backlog.

The Claude Security Plugin for Claude Code is now in beta

Scan, validate, and patch directly inside Claude Code while keeping all code inside your environment.

[Learn more (opens in new tab)](../02-Claude-Code-CLI/claude-security.md)

## Built for security teams, used by Anthropic

### Transparency and visibility

See details about every finding: the vulnerability, why it matters, and the proposed fix

### Targeted patches

Suggested fixes that maintain your code's structure and style

### Fits your existing workflow

Get findings into your tools through webhooks and the API, then review and resolve them without leaving Claude Code

### Full remediation control

Teams stay in control, with every patch requiring human review and approval

### Powered by Claude Mythos

Scan your codebase with our most cyber-capable model

Security resources

[Contact sales](https://www.claude.com/contact-sales)[Read the tutorial](https://academy.claude.com/tutorials/getting-started-with-claude-security)


Claude Security Plugin for Claude Code in beta

Docs


Claude Security is now in public beta

Blog


Evaluating and mitigating the growing risk of LLM-discovered 0-days

Blog


Experimenting with AI to defend critical infrastructure

Blog

## FAQ

### Where is this available?

Admins can enable Claude Security in the [admin console](http://claude.ai/admin-settings/claude-code). See the getting started guide for [setup steps](https://academy.claude.com/tutorials/getting-started-with-claude-security).

The [Claude Security plugin](../02-Claude-Code-CLI/claude-security.md) is now available in beta for all Claude Code users.

### What Mythos access does this give me?

Claude Security is powered by our full family of models, including Claude Mythos, with no Cyber Verification Program access required.

Create a project, connect your repositories, and Claude Security scans them using our most capable models for cyber, including Claude Mythos models. Validated findings come back with severity ratings and suggested fixes, which you can open in Claude Code and fix using the models available in your account.

*Scans powered by Claude Mythos models are only available in the Claude Security app on Claude.ai. The Claude Security plugin for Claude Code uses the models available in your Claude Code account.*

### What are the security risks I should know about?

Claude can make mistakes, so you should always review proposed patches before applying them, especially for critical systems.

### What types of vulnerabilities does Claude Security find?

Claude Security focuses on high-severity vulnerabilities including memory corruption, injection flaws, authentication bypasses, and complex logic errors that pattern-matching tools typically miss. It's particularly effective at finding context-dependent vulnerabilities that require understanding code across multiple files.

### How is this different from traditional security tools?

Traditional tools often use rule-based pattern matching, which catches known vulnerability patterns but can produce high false positive rates and miss complex issues. Claude Security reasons through your code like a security researcher. It can read Git history, trace data flows, and understand business logic to find real vulnerabilities and generate real fixes.

### Does Claude Security work with my existing security tools?

Yes. The Claude Security API lets you pull findings into your ticketing, vulnerability management, and reporting tools. You can also resolve or reopen them from there. Webhooks notify your systems when you receive a new finding.

Claude Security is also available as an MCP connector in Claude and Claude Code, so an engineer can pull up a finding, start the fix, and mark it resolved in the same session.

### Do I need to schedule scans?

No. Choose the branch and scope for each repository, and Claude runs a deep baseline scan. After that it keeps scanning changes regularly based on their risk and complexity, so your findings stay close to the current state of your code.
