---
title: "CLI scripting and automation - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:29Z"
tags: ["api", "claude-code", "cli"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fcli-sdks-libraries%2Fcli%2Fscripting)





SearchCtrlK

CLI, SDKs, and libraries

[Overview](/docs/en/cli-sdks-libraries/overview)

ant CLI

[Quickstart](/docs/en/cli-sdks-libraries/cli/quickstart)[Authentication options](/docs/en/cli-sdks-libraries/cli/authentication)[Using the CLI](/docs/en/cli-sdks-libraries/cli/using)[Scripting and automation](/docs/en/cli-sdks-libraries/cli/scripting)[Manage resources as code](/docs/en/cli-sdks-libraries/cli/apply)[Connect to a Managed Agents session](/docs/en/cli-sdks-libraries/cli/sessions-connect)

Client SDKs

[Middleware](/docs/en/cli-sdks-libraries/middleware)[Python](/docs/en/cli-sdks-libraries/sdks/python)[TypeScript](/docs/en/cli-sdks-libraries/sdks/typescript)[C#](/docs/en/cli-sdks-libraries/sdks/csharp)[Go](/docs/en/cli-sdks-libraries/sdks/go)[Java](/docs/en/cli-sdks-libraries/sdks/java)[PHP](/docs/en/cli-sdks-libraries/sdks/php)[Ruby](/docs/en/cli-sdks-libraries/sdks/ruby)

Libraries and integrations

[Apple Foundation Models](/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)[OpenAI SDK compatibility](/docs/en/cli-sdks-libraries/libraries/openai-sdk)

[Console](/)

[CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)ant CLI

# CLI scripting and automation

Copy page



Version-control API resources as files with ant apply, chain ant CLI commands in scripts, operate on resources from Claude Code, and authenticate curl calls with CLI credentials.

Copy page



This page covers task-oriented workflows built on the `ant` CLI. For the underlying flags and output options, see [Using the CLI](/docs/en/cli-sdks-libraries/cli/using).

## Version-controlling API resources

To keep agents, environments, and other Claude Managed Agents resources as files in your repository, see [Manage resources as code with ant apply](/docs/en/cli-sdks-libraries/cli/apply).

### Run the applied agent from the shell

Once an agent and environment exist, you can drive a session from the shell:

1.  1

    ### Start a session

    Pass the agent and environment IDs to the session create command. After `ant apply`, read them from `claude-lock.json`: each entry under `resources` has an `id`, and for the project in [Manage resources as code with ant apply](/docs/en/cli-sdks-libraries/cli/apply) the entries are `./agents/summarizer.md` and `./environments/cloud.yaml`.

    ``` shiki
    ant beta:sessions create \
      --agent agent_011CYm1BLqPXpQRk5khsSXrs \
      --environment-id env_01595EKxaaTTGwwY3kyXdtbs \
      --title "Summarization task"
    ```

    

    Output

    

    ``` shiki
    {
      "id": "session_01JZCh78XvmxJjiXVy3oSi7K",
      "status": "running"
      /* ... */
    }
    ```

2.  2

    ### Send a user message

    Copy the session `id` from the previous output into `--session-id`:

    ``` shiki
    ant beta:sessions:events send \
      --session-id session_01JZCh78XvmxJjiXVy3oSi7K \
      --event '{type: user.message, content: [{type: text, text: "Summarize the benefits of type safety in one sentence."}]}'
    ```

    

3.  3

    ### Read the conversation

    Once the agent has replied, list the events. `--transform` runs against each listed event, so this prints the text of every message in order. `--format auto` overrides the interactive explorer that list commands open by default in a terminal:

    ``` shiki
    ant beta:sessions:events list \
      --session-id session_01JZCh78XvmxJjiXVy3oSi7K \
      --transform 'content.0.text' \
      --raw-output \
      --format auto
    ```

    

    Output

    

    ``` block
    Summarize the benefits of type safety in one sentence.
    Type safety catches errors at compile time rather than runtime, reducing bugs, improving code clarity, enabling better tooling support, and making codebases easier to maintain and refactor with confidence.
    ```

    
    To watch a session as it runs, use `ant beta:sessions:events stream --session-id session_01JZCh78XvmxJjiXVy3oSi7K --format jsonl`, which writes each event to stdout as it arrives. Without `--format`, a terminal opens the interactive explorer instead.

## Scripting patterns

The CLI is designed to compose with standard shell tooling.

### Chain list output into a second command

`--transform id --raw-output` on a list endpoint emits one bare ID per line, so standard tools such as `head` and `xargs` apply directly. Capture the first result, then pass it to a follow-up command:

```python
FIRST_AGENT=$(ant beta:agents list --transform id --raw-output | head -1)

ant beta:agents:versions list \
  --agent-id "$FIRST_AGENT" \
  --transform "{version,created_at}" --format jsonl
```



### Inspect errors

The `--transform-error` and `--format-error` flags apply the same filtering to error responses. `--raw-output` does not apply to errors, so use `--format-error yaml` for an unquoted scalar. Extract only the error message:

```python
ant beta:agents retrieve --agent-id bogus \
  --transform-error error.message --format-error yaml 2>&1
```



Output



``` block
GET "https://api.anthropic.com/v1/agents/bogus?beta=true": 404 Not Found
Agent not found.
```

## Use the CLI from Claude Code

[Claude Code](https://code.claude.com/docs/en/overview) can use the `ant` CLI out of the box. With the CLI installed and authenticated, you can ask Claude Code to operate on your API resources directly. For example:

- "List my recent agent sessions and summarize which ones errored."
- "Upload every PDF in `./reports` to the Files API and print the resulting IDs."
- "Pull the events for session `session_01...` and tell me where the agent got stuck."

Claude Code shells out to `ant`, parses the structured output, and reasons over the results (no custom integration code required).

## Authenticate curl requests with CLI credentials

Scripts that call the API with `curl` or another HTTP client can use the credentials stored by [`ant auth login`](/docs/en/cli-sdks-libraries/cli/quickstart#authentication) instead of a static API key. The OAuth access token goes in the `Authorization` header as a bearer token; the `x-api-key` header is only for static API keys.

`ant auth print-credentials --access-token` prints the active profile's access token, refreshing it first if it is expired or near expiry:

cURL



```python
curl https://api.anthropic.com/v1/messages \
  -H "Authorization: Bearer $(ant auth print-credentials --access-token)" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-5-5",
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "hi"}]
  }'
```



Keep `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` unset when working from a CLI login. Either variable takes precedence over the login for `ant` commands (see [Credential precedence](/docs/en/manage-claude/wif-reference#credential-precedence)) and can silently route them to a different organization or workspace.

Run [`ant auth status`](/docs/en/cli-sdks-libraries/cli/authentication#check-authentication-status) to confirm which organization and workspace you are logged in to; it warns when an environment variable is overriding your login.
