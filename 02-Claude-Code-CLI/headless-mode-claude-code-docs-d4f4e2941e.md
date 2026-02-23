---
category: "02-Claude-Code-CLI"
fetched_at: "2026-02-23T00:45:39Z"
source_url: "https://code.claude.com/docs/en/headless"
title: "Headless mode - Claude Code Docs"
---

[Skip to main content](#content-area)

[Claude Code Docs home page](/docs)

English

Search...

⌘K

Ask AI

- [Claude Developer Platform](https://platform.claude.com/)
- [Claude Code on the Web](https://claude.ai/code)
- [](https://claude.ai/code)
  Claude Code on the Web

Search...

Navigation

Build with Claude Code

Run Claude Code programmatically

[Getting started](/docs/en/overview)

[Build with Claude Code](/docs/en/sub-agents)

[Deployment](/docs/en/third-party-integrations)

[Administration](/docs/en/setup)

[Configuration](/docs/en/settings)

[Reference](/docs/en/cli-reference)

[Resources](/docs/en/legal-and-compliance)

##### Build with Claude Code

- [](/docs/en/sub-agents)
  Create custom subagents
- [](/docs/en/agent-teams)
  Run agent teams
- [](/docs/en/plugins)
  Create plugins
- [](/docs/en/discover-plugins)
  Discover and install prebuilt plugins
- [](/docs/en/skills)
  Extend Claude with skills
- [](/docs/en/output-styles)
  Output styles
- [](/docs/en/hooks-guide)
  Automate with hooks
- [](/docs/en/headless)
  Programmatic usage
- [](/docs/en/mcp)
  Model Context Protocol (MCP)
- [](/docs/en/troubleshooting)
  Troubleshooting

On this page

- [Basic usage](#basic-usage)
- [Examples](#examples)
- [Get structured output](#get-structured-output)
- [Stream responses](#stream-responses)
- [Auto-approve tools](#auto-approve-tools)
- [Create a commit](#create-a-commit)
- [Customize the system prompt](#customize-the-system-prompt)
- [Continue conversations](#continue-conversations)
- [Next steps](#next-steps)

Build with Claude Code

# Run Claude Code programmatically

Copy page

Use the Agent SDK to run Claude Code programmatically from the CLI, Python, or TypeScript.

Copy page

The [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) gives you the same tools, agent loop, and context management that power Claude Code. It’s available as a CLI for scripts and CI/CD, or as [Python](https://platform.claude.com/docs/en/agent-sdk/python) and [TypeScript](https://platform.claude.com/docs/en/agent-sdk/typescript) packages for full programmatic control.

The CLI was previously called “headless mode.” The `-p` flag and all CLI options work the same way.

To run Claude Code programmatically from the CLI, pass `-p` with your prompt and any [CLI options](/docs/en/cli-reference):

Report incorrect code

Copy

Ask AI

``` shiki
claude -p "Find and fix the bug in auth.py" --allowedTools "Read,Edit,Bash"
```

This page covers using the Agent SDK via the CLI (`claude -p`). For the Python and TypeScript SDK packages with structured outputs, tool approval callbacks, and native message objects, see the [full Agent SDK documentation](https://platform.claude.com/docs/en/agent-sdk/overview).

## 

[​](#basic-usage)

Basic usage

Add the `-p` (or `--print`) flag to any `claude` command to run it non-interactively. All [CLI options](/docs/en/cli-reference) work with `-p`, including:

- `--continue` for [continuing conversations](#continue-conversations)
- `--allowedTools` for [auto-approving tools](#auto-approve-tools)
- `--output-format` for [structured output](#get-structured-output)

This example asks Claude a question about your codebase and prints the response:

Report incorrect code

Copy

Ask AI

``` shiki
claude -p "What does the auth module do?"
```

## 

[​](#examples)

Examples

These examples highlight common CLI patterns.

### 

[​](#get-structured-output)

Get structured output

Use `--output-format` to control how responses are returned:

- `text` (default): plain text output
- `json`: structured JSON with result, session ID, and metadata
- `stream-json`: newline-delimited JSON for real-time streaming

This example returns a project summary as JSON with session metadata, with the text result in the `result` field:

Report incorrect code

Copy

Ask AI

``` shiki
claude -p "Summarize this project" --output-format json
```

To get output conforming to a specific schema, use `--output-format json` with `--json-schema` and a [JSON Schema](https://json-schema.org/) definition. The response includes metadata about the request (session ID, usage, etc.) with the structured output in the `structured_output` field. This example extracts function names and returns them as an array of strings:

Report incorrect code

Copy

Ask AI

``` shiki
claude -p "Extract the main function names from auth.py" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}'
```

Use a tool like [jq](https://jqlang.github.io/jq/) to parse the response and extract specific fields:

Report incorrect code

Copy

Ask AI

``` shiki
# Extract the text result
claude -p "Summarize this project" --output-format json | jq -r '.result'

# Extract structured output
claude -p "Extract function names from auth.py" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}' \
  | jq '.structured_output'
```

### 

[​](#stream-responses)

Stream responses

Use `--output-format stream-json` with `--verbose` and `--include-partial-messages` to receive tokens as they’re generated. Each line is a JSON object representing an event:

Report incorrect code

Copy

Ask AI

``` shiki
claude -p "Explain recursion" --output-format stream-json --verbose --include-partial-messages
```

The following example uses [jq](https://jqlang.github.io/jq/) to filter for text deltas and display just the streaming text. The `-r` flag outputs raw strings (no quotes) and `-j` joins without newlines so tokens stream continuously:

Report incorrect code

Copy

Ask AI

``` shiki
claude -p "Write a poem" --output-format stream-json --verbose --include-partial-messages | \
  jq -rj 'select(.type == "stream_event" and .event.delta.type? == "text_delta") | .event.delta.text'
```

For programmatic streaming with callbacks and message objects, see [Stream responses in real-time](https://platform.claude.com/docs/en/agent-sdk/streaming-output) in the Agent SDK documentation.

### 

[​](#auto-approve-tools)

Auto-approve tools

Use `--allowedTools` to let Claude use certain tools without prompting. This example runs a test suite and fixes failures, allowing Claude to execute Bash commands and read/edit files without asking for permission:

Report incorrect code

Copy

Ask AI

``` shiki
claude -p "Run the test suite and fix any failures" \
  --allowedTools "Bash,Read,Edit"
```

### 

[​](#create-a-commit)

Create a commit

This example reviews staged changes and creates a commit with an appropriate message:

Report incorrect code

Copy

Ask AI

``` shiki
claude -p "Look at my staged changes and create an appropriate commit" \
  --allowedTools "Bash(git diff *),Bash(git log *),Bash(git status *),Bash(git commit *)"
```

The `--allowedTools` flag uses [permission rule syntax](/docs/en/settings#permission-rule-syntax). The trailing ` *` enables prefix matching, so `Bash(git diff *)` allows any command starting with `git diff`. The space before `*` is important: without it, `Bash(git diff*)` would also match `git diff-index`.

User-invoked [skills](/docs/en/skills) like `/commit` and [built-in commands](/docs/en/interactive-mode#built-in-commands) are only available in interactive mode. In `-p` mode, describe the task you want to accomplish instead.

### 

[​](#customize-the-system-prompt)

Customize the system prompt

Use `--append-system-prompt` to add instructions while keeping Claude Code’s default behavior. This example pipes a PR diff to Claude and instructs it to review for security vulnerabilities:

Report incorrect code

Copy

Ask AI

``` shiki
gh pr diff "$1" | claude -p \
  --append-system-prompt "You are a security engineer. Review for vulnerabilities." \
  --output-format json
```

See [system prompt flags](/docs/en/cli-reference#system-prompt-flags) for more options including `--system-prompt` to fully replace the default prompt.

### 

[​](#continue-conversations)

Continue conversations

Use `--continue` to continue the most recent conversation, or `--resume` with a session ID to continue a specific conversation. This example runs a review, then sends follow-up prompts:

Report incorrect code

Copy

Ask AI

``` shiki
# First request
claude -p "Review this codebase for performance issues"

# Continue the most recent conversation
claude -p "Now focus on the database queries" --continue
claude -p "Generate a summary of all issues found" --continue
```

If you’re running multiple conversations, capture the session ID to resume a specific one:

Report incorrect code

Copy

Ask AI

``` shiki
session_id=$(claude -p "Start a review" --output-format json | jq -r '.session_id')
claude -p "Continue that review" --resume "$session_id"
```

## 

[​](#next-steps)

Next steps

[](https://platform.claude.com/docs/en/agent-sdk/quickstart)

## Agent SDK quickstart

Build your first agent with Python or TypeScript

[](/docs/en/cli-reference)

## CLI reference

Explore all CLI flags and options

[](/docs/en/github-actions)

## GitHub Actions

Use the Agent SDK in GitHub workflows

[](/docs/en/gitlab-ci-cd)

## GitLab CI/CD

Use the Agent SDK in GitLab pipelines

Was this page helpful?

Yes

No

[Automate with hooks](/docs/en/hooks-guide)[Model Context Protocol (MCP)](/docs/en/mcp)

[Claude Code Docs home page](/docs)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

Company

[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)

Help and security

[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)

Learn

[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)

Terms and policies

[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)

Assistant

Responses are generated using AI and may contain mistakes.
