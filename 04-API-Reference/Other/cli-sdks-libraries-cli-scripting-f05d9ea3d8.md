---
title: "CLI scripting and automation - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:41:05Z"
tags: ["api", "cli"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


CLI, SDKs, and libraries

[Overview](/docs/en/cli-sdks-libraries/overview)

ant CLI

[Quickstart](/docs/en/cli-sdks-libraries/cli/quickstart)[Authentication options](/docs/en/cli-sdks-libraries/cli/authentication)[Using the CLI](/docs/en/cli-sdks-libraries/cli/using)[Scripting and automation](/docs/en/cli-sdks-libraries/cli/scripting)

Client SDKs

[Middleware](/docs/en/cli-sdks-libraries/middleware)[Python](/docs/en/cli-sdks-libraries/sdks/python)[TypeScript](/docs/en/cli-sdks-libraries/sdks/typescript)[C#](/docs/en/cli-sdks-libraries/sdks/csharp)[Go](/docs/en/cli-sdks-libraries/sdks/go)[Java](/docs/en/cli-sdks-libraries/sdks/java)[PHP](/docs/en/cli-sdks-libraries/sdks/php)[Ruby](/docs/en/cli-sdks-libraries/sdks/ruby)

Libraries and integrations

[Apple Foundation Models](/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)[OpenAI SDK compatibility](/docs/en/cli-sdks-libraries/libraries/openai-sdk)

[](/login)




CLI, SDKs, and libraries

Scripting and automation

CLI, SDKs, and libraries/ant CLI

# CLI scripting and automation




Version-control API resources as YAML, chain ant CLI commands in scripts, operate on resources from Claude Code, and authenticate curl calls with CLI credentials.




This page covers task-oriented workflows built on the `ant` CLI. For the underlying flags and output options, see [Using the CLI](/docs/en/cli-sdks-libraries/cli/using).




Version-controlling API resources

You can use the CLI to version control API resources such as skills, agents, environments, or deployments as YAML files in your repository and keep them in sync with the Claude API.



For more information on these resources, see [Managed Agents](/docs/en/managed-agents/overview).

1.  1

    Define your agent

    Write the agent definition to `summarizer.agent.yaml`:

    summarizer.agent.yaml

    

    ``` shiki
    name: Summarizer
    model: claude-opus-5
    system: |
      You are a helpful assistant that writes concise summaries.
    tools:
      - type: agent_toolset_20260401
    ```

2.  2

    Create the agent

    ``` shiki
    ant beta:agents create < summarizer.agent.yaml
    ```

    

    Output

    

    ``` shiki
    {
      "id": "agent_011CYm1BLqPXpQRk5khsSXrs",
      "version": 1,
      "name": "Summarizer",
      "model": "claude-opus-5"
      /* ... */
    }
    ```

    Note the `id` from the response. You'll pass it to the session create command in a later step.

    

    Check `summarizer.agent.yaml` into your repository and keep it in sync with the API in your CI pipeline. The update command needs the agent ID and current version as flags:

    CLI

    

    ``` shiki
    ant beta:agents update --agent-id agent_011CYm1BLqPXpQRk5khsSXrs --version 1 < summarizer.agent.yaml
    ```

3.  3

    Define the environment

    A session runs in an [environment](/docs/en/api/cli/beta/environments), which defines the sandbox it executes in. Write the environment definition to `summarizer.environment.yaml`:

    summarizer.environment.yaml

    

    ``` shiki
    name: summarizer-env
    config:
      type: cloud
      networking:
        type: unrestricted
    ```

4.  4

    Create the environment

    ``` shiki
    ant beta:environments create < summarizer.environment.yaml
    ```

    

    Output

    

    ``` shiki
    {
      "id": "env_01595EKxaaTTGwwY3kyXdtbs",
      "name": "summarizer-env"
      /* ... */
    }
    ```

    Note the `id` from the response. You'll pass it to the session create command in a later step.

    

    Check `summarizer.environment.yaml` into your repository and keep it in sync with the API in your CI pipeline. The update command needs the environment ID as a flag:

    CLI

    

    ``` shiki
    ant beta:environments update --environment-id env_01595EKxaaTTGwwY3kyXdtbs < summarizer.environment.yaml
    ```

5.  5

    Start a session

    Paste the agent `id` and environment `id` from the previous outputs into the session create command:

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

6.  6

    Send a user message

    Copy the session `id` from the previous output into `--session-id`:

    ``` shiki
    ant beta:sessions:events send \
      --session-id session_01JZCh78XvmxJjiXVy3oSi7K \
      --event '{type: user.message, content: [{type: text, text: "Summarize the benefits of type safety in one sentence."}]}'
    ```

    

7.  7

    Read the conversation

    `--transform` runs against each listed event, so this prints the text of every message in order. `--format auto` overrides the interactive explorer that list commands open by default in a terminal:

    ``` shiki
    ant beta:sessions:events list \
      --session-id session_01JZCh78XvmxJjiXVy3oSi7K \
      --transform 'content.0.text' --format auto --raw-output
    ```

    

    Output

    

    ``` block
    Summarize the benefits of type safety in one sentence.
    Type safety catches errors at compile time rather than runtime, reducing bugs, improving code clarity, enabling better tooling support, and making codebases easier to maintain and refactor with confidence.
    ```

    

    To watch a session as it runs, use `ant beta:sessions:events stream --session-id session_01JZCh78XvmxJjiXVy3oSi7K`. Events are written to stdout as they arrive.




Scripting patterns

The CLI is designed to compose with standard shell tooling.




Chain list output into a second command

`--transform id --raw-output` on a list endpoint emits one bare ID per line, so standard tools such as `head` and `xargs` apply directly. Capture the first result, then pass it to a follow-up command:

```python
FIRST_AGENT=$(ant beta:agents list \
  --transform id --raw-output | head -1)

ant beta:agents:versions list \
  --agent-id "$FIRST_AGENT" \
  --transform "{version,created_at}" --format jsonl
```






Inspect errors

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




Use the CLI from Claude Code

[Claude Code](https://code.claude.com/docs/en/overview) can use the `ant` CLI out of the box. With the CLI installed and authenticated, you can ask Claude Code to operate on your API resources directly. For example:

- "List my recent agent sessions and summarize which ones errored."
- "Upload every PDF in `./reports` to the Files API and print the resulting IDs."
- "Pull the events for session `session_01...` and tell me where the agent got stuck."

Claude Code shells out to `ant`, parses the structured output, and reasons over the results (no custom integration code required).




Authenticate curl requests with CLI credentials

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
    "model": "claude-opus-5",
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "hi"}]
  }'
```



Keep `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` unset when working from a CLI login. Either variable takes precedence over the login for `ant` commands (see [Credential precedence](/docs/en/manage-claude/wif-reference#credential-precedence)) and can silently route them to a different organization or workspace.

Run [`ant auth status`](/docs/en/cli-sdks-libraries/cli/authentication#check-authentication-status) to confirm which organization and workspace you are logged in to; it warns when an environment variable is overriding your login.
