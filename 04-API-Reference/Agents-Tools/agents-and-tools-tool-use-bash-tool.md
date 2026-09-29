---
title: "Bash tool - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:23Z"
tags: ["api", "security"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Fbash-tool)

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

[Messages](../../01-Getting-Started/intro.md)Tools

# Bash tool

Copy page



Let Claude request shell commands that your application runs in a persistent bash session and returns as tool results.

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

The bash tool is a [client tool](agents-and-tools-tool-use-how-tool-use-works.md): Claude doesn't run commands itself. When you include the tool in a request, Claude replies with a `tool_use` block that names the command to run. Your application runs that command in a bash session it owns and returns the output in a `tool_result` block.

Your application keeps one bash process alive across tool calls, so state persists between commands. The working directory, environment variables, and any files a command creates are still there for the next command.

The current version of the tool is `bash_20250124`. For model support, beta headers, and the earlier version, see [Tool versions](#tool-versions). For all Anthropic-provided tools, see the [Tool reference](agents-and-tools-tool-use-tool-reference.md).

## Use cases

- **Development workflows:** Run build commands, tests, and development tools
- **System automation:** Execute scripts, manage files, automate tasks
- **Data processing:** Process files, run analysis scripts, manage datasets
- **Environment setup:** Install packages, configure environments

## Quick start

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[{"type": "bash_20250124", "name": "bash"}],
    messages=[
        {"role": "user", "content": "List all Python files in the current directory."}
    ],
)

print(response)
```

Claude responds with `stop_reason: "tool_use"` and a `tool_use` block that contains the command for your application to run:

Output



```python
{
  "id": "msg_01XAbCDeFgHiJkLmNoPQrStU",
  "model": "claude-opus-5-5",
  "stop_reason": "tool_use",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I'll list all Python files in the current directory for you."
    },
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "bash",
      "input": {
        "command": "ls *.py"
      }
    }
  ]
}
```

Run `input.command` in your bash session and send the output back as a `tool_result`. See [Implement the bash tool](#implement-the-bash-tool) for the round trip.

## How it works

Each tool call is one round trip between Claude and your application:

1.  Claude returns a `tool_use` block containing the `command` to run.
2.  Your application runs the command in its bash session.
3.  Your application returns the command's output, stdout and stderr together, to Claude in a `tool_result` block.
4.  Claude either requests another command in the same session or responds with text.

Claude can also return several `tool_use` blocks in one response. Run them in order in the same session and return all of the results in one `user` message. See [Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md).

The API is stateless. Nothing about your shell session travels between requests, so your application decides when the session starts, how long it lives, and when to restart it. For the full request and response cycle, see [Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md).

## Parameters

A bash tool definition has two required fields, `type` and `name`, and the `name` must be `bash`. The tool is schema-less: you don't provide an `input_schema`, because the schema is built into Claude's model and can't be modified. The following table lists the input fields Claude sets when it calls the tool.

| Parameter | Required | Description                               |
|-----------|----------|-------------------------------------------|
| `command` | Yes\*    | The bash command to run                   |
| `restart` | No       | Set to `true` to restart the bash session |

\*Required unless using `restart`

To handle `restart: true`, kill the shell process, start a new one, and return a `tool_result` that confirms the restart. A restarted session starts clean: the working directory, environment variables, and any running processes are gone.

### Example usage

Run a command:

```python
{
  "command": "ls -la *.py"
}
```



Restart the session:

```python
{
  "restart": true
}
```



## Tool versions

`bash_20250124` is the current version of the tool, and it requires no beta header. Every model from Claude Sonnet 3.7 ([retired](../../20-Models/about-claude-model-deprecations.md)) onward accepts it, including all current Claude models.

The original `bash_20241022` version works only with the October 2024 Claude Sonnet 3.5 model ([retired](../../20-Models/about-claude-model-deprecations.md)). Requests that use it need the `anthropic-beta: computer-use-2024-10-22` header, and the SDKs expose it only in their beta namespaces. New integrations should use `bash_20250124`.

## Example: Multistep automation

Claude can chain commands across tool calls to complete a multistep task:

``` inline-block
User request:
"Install the requests library and create a simple Python script that
fetches a joke from an API, then run it."

Claude's tool uses:
1. Install package
   {"command": "pip install requests"}

2. Create script
   {"command": "cat > fetch_joke.py << 'EOF'\nimport requests\nresponse = requests.get('https://official-joke-api.appspot.com/random_joke')\njoke = response.json()\nprint(f\"Setup: {joke['setup']}\")\nprint(f\"Punchline: {joke['punchline']}\")\nEOF"}

3. Run script
   {"command": "python fetch_joke.py"}
```



The session maintains state between commands, so files created in step 2 are available in step 3.

## Implement the bash tool

Claude determines which command to run. Your application owns everything else: the shell process, the timeout, and the safety checks. The following steps show a minimal implementation.

1.  1

    ### Create a persistent bash session

    Start one long-lived bash process and run every command inside it. Because a pipe to a live process never reports end-of-file, the session prints a unique sentinel line after each command to mark where that command's output ends:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    import subprocess
    import uuid


    class BashSession:
        """A bash process that stays alive between commands so state persists."""

        def __init__(self):
            self.process = subprocess.Popen(
                ["/bin/bash"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # interleave errors with output, in order
                start_new_session=True,  # own process group: a timeout can kill every child
                text=True,
            )

        def execute_command(self, command):
            """Run a command in the session and return its output."""
            sentinel = f"__CLAUDE_BASH_DONE_{uuid.uuid4().hex}__"  # unique per call
            self.process.stdin.write(f"{command}\necho {sentinel}\n")
            self.process.stdin.flush()

            output = []
            for line in self.process.stdout:
                if sentinel in line:  # this command's output is complete
                    break
                output.append(line)
            return "".join(output)

        def restart(self):
            self.process.kill()
            self.process.wait()
            self.__init__()


    bash_session = BashSession()
    print(bash_session.execute_command("cd /tmp && pwd"))
    print(bash_session.execute_command("pwd"))  # still /tmp: the session kept its state
    ```

    The session interleaves stderr with stdout, so error messages land where they happened. The example leaves out what a complete implementation also needs: a timeout that kills the shell and every process it started when a command hangs, then restarts the session. The [Use command timeouts](#follow-implementation-best-practices) best practice shows one way to add it.

2.  2

    ### Process Claude's tool calls

    Extract and run commands from Claude's responses:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    tool_results = []
    for content in response.content:
        if content.type == "tool_use" and content.name == "bash":
            if content.input.get("restart"):
                bash_session.restart()
                result = "Bash session restarted"
            else:
                command = content.input.get("command")
                result = bash_session.execute_command(command)

            # One tool_result per tool_use block, all returned in the next user message
            tool_results.append(
                {"type": "tool_result", "tool_use_id": content.id, "content": result}
            )
    ```

3.  3

    ### Return the result to Claude

    Send the `tool_result` back in a `user` message that continues the same conversation. Claude either requests another command in the same session or finishes its answer:

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        tools=[{"type": "bash_20250124", "name": "bash"}],
        messages=[
            {"role": "user", "content": "List all Python files in the current directory."},
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "tool_use",
                        "id": "toolu_01A09q90qw90lq917835lq9",
                        "name": "bash",
                        "input": {"command": "ls *.py"},
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
                        "content": "analysis.py\nprocess_data.py\n",
                    }
                ],
            },
        ],
    )

    print(response.content)
    ```

    Repeat the run-and-return cycle while `stop_reason` is `tool_use`. For the full loop, see [Handling results from client tools](agents-and-tools-tool-use-handle-tool-calls.md#handling-results-from-client-tools).

4.  4

    ### Implement safety measures

    Add validation and restrictions. Use an allowlist rather than a blocklist: a blocklist misses any command it didn't anticipate. The example also rejects shell operators that appear as separate words:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    import shlex

    ALLOWED_COMMANDS = {"ls", "cat", "echo", "pwd", "grep", "find", "wc", "head", "tail"}
    SHELL_OPERATORS = {"&&", "||", "|", ";", "&", ">", "<", ">>"}


    def validate_command(command):
        # Allow only commands from an explicit allowlist
        try:
            tokens = shlex.split(command)
        except ValueError:
            return False, "Could not parse command"

        if not tokens:
            return False, "Empty command"

        executable = tokens[0]
        if executable not in ALLOWED_COMMANDS:
            return False, f"Command '{executable}' is not in the allowlist"

        # Reject shell operators written as separate words
        for token in tokens[1:]:
            if token in SHELL_OPERATORS or token.startswith(("$", "`")):
                return False, f"Shell operator '{token}' is not allowed"

        return True, None
    ```

    This check is a tripwire for obvious mistakes, not an enforcement boundary. It rejects the spaced chaining (`&&`), pipes, and redirection that the other examples on this page use. It does not catch an operator glued to a word, such as `cat data.txt|grep x`, because the tokenizer keeps `data.txt|grep` inside one token. Decide which commands and operators your application allows. The real control is isolation: run the whole session inside a container or a virtual machine (see [Security](#security)).

### Handle errors

When a command fails or the session breaks, tell Claude what happened. Return the message as the `tool_result` content and set `is_error` to `true`, which marks the tool call as failed. See [Handling errors with is_error](agents-and-tools-tool-use-handle-tool-calls.md#handling-errors-with-is-error).

### Command execution timeout

If a command takes too long to execute:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: command did not finish within 30 seconds",
      "is_error": true
    }
  ]
}
```



### Command not found

If a command doesn't exist:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "bash: nonexistentcommand: command not found",
      "is_error": true
    }
  ]
}
```



### Permission denied

If there are permission issues:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "bash: /root/sensitive-file: Permission denied",
      "is_error": true
    }
  ]
}
```



### Follow implementation best practices

### Use command timeouts

A command that never finishes, such as one that waits for input, blocks the session forever because its sentinel line never arrives. Give every command a deadline. When the deadline passes, stop the shell and everything the command started, then restart the session:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import concurrent.futures
import os
import signal


def execute_with_timeout(session, command, timeout=30):
    """Run a command in the session, replacing the session if the command hangs."""
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        future = pool.submit(session.execute_command, command)
        try:
            return future.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            # The group is the shell and every process the command started
            os.killpg(session.process.pid, signal.SIGKILL)
            session.restart()
            return f"Error: command did not finish within {timeout} seconds"
```

The kill stops the hung command and everything it started. Return the message as an error `tool_result` (see [Handle errors](#handle-errors)), which marks the tool call as failed.

### Maintain session state

Keep the bash session persistent to maintain environment variables and working directory:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
# Commands run in the same session maintain state
commands = [
    "cd /tmp",
    "echo 'Hello' > test.txt",
    "cat test.txt",  # The session is still in /tmp
]
```

### Handle large outputs

Truncate large outputs to prevent token limit issues:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
def truncate_output(output, max_lines=100):
    lines = output.split("\n")
    if len(lines) > max_lines:
        truncated = "\n".join(lines[:max_lines])
        return f"{truncated}\n\n... Output truncated ({len(lines)} total lines) ..."
    return output
```

### Log all commands

Keep an audit trail. Route every command through one wrapper that records the command before it runs and the output after it finishes. A command that hangs or breaks the session still leaves a record:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


def execute_and_log(session, command):
    """Run a command in the session and keep an audit record of it."""
    logging.info("command=%r", command)
    output = session.execute_command(command)
    logging.info("output=%r", output[:200])  # first 200 characters
    return output
```

The records go to `stderr` by default; point them at a file or your logging pipeline to keep them. Include whatever ties the record to the request in your application, such as the end user and the `tool_use_id`.

## Security



Your application runs whatever command Claude requests. Run the session in an isolated environment, such as a container or a virtual machine, as the least-privileged user that can do the work. Treat every command as untrusted input.

Beyond isolation, add these controls:

- Validate commands before running them, with an allowlist rather than a blocklist. See [Implement the bash tool](#implement-the-bash-tool).
- Set resource limits on the shell process (CPU, memory, and disk), for example with `ulimit`.
- Log every command and its output so you can audit what ran.
- Redact credentials and other secrets from output before returning it to Claude.

## Pricing

The bash tool definition adds the following input tokens to your request. This is in addition to the per-model [tool use system prompt](agents-and-tools-tool-use-overview.md#pricing) that applies whenever any tool is present.

| Model                                               | Additional input tokens |
|-----------------------------------------------------|-------------------------|
| Claude Opus 5, Claude Opus 4.8, and Claude Opus 4.7 | 325 tokens              |
| Claude Opus 4.6, Claude Sonnet 4.6, and earlier     | 244 tokens              |

Additional tokens are consumed by:

- Command outputs (stdout/stderr)
- Error messages
- Large file contents

See [tool use pricing](agents-and-tools-tool-use-overview.md#pricing) for complete pricing details.

## Common patterns

### Development workflows

- Running tests: `pytest && coverage report`
- Building projects: `npm install && npm run build`
- Git operations: `git status && git add . && git commit -m "message"`

For guidance on using git as a checkpoint-and-recovery mechanism in long-running agent workflows, see [state management best practices](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#state-management-best-practices).

### File operations

- Processing data: `wc -l *.csv && ls -lh *.csv`
- Searching files: `find . -name "*.py" | xargs grep "pattern"`
- Creating backups: `tar -czf backup.tar.gz ./data`

### System tasks

- Checking resources: `df -h && free -m`
- Process management: `ps aux | grep python`
- Environment setup: `export PATH=$PATH:/new/path && echo $PATH`

## Limitations

- **No interactive commands:** The session can't run `vim`, `less`, password prompts, or any command that waits for input on stdin.
- **No GUI applications:** The session is command-line only.
- **Session scope:** Bash session state is client-side. Your application is responsible for maintaining the shell session between turns.
- **Output limits:** The API doesn't truncate tool results (an oversized request is rejected). Truncate large outputs in your application before returning them to Claude.
- **No streaming:** Output reaches Claude only when your application returns the `tool_result` in the next request.

## Combining with other tools

The bash tool pairs well with the [Text editor tool](agents-and-tools-tool-use-text-editor-tool.md): Claude edits a file with one tool and requests the command that runs it with the other.



If you're also using the [Code execution tool](agents-and-tools-tool-use-code-execution-tool.md), Claude has access to two separate execution environments: your local bash session and Anthropic's sandboxed container. State is not shared between them. See [Using code execution with other execution tools](agents-and-tools-tool-use-code-execution-tool.md#using-code-execution-with-other-execution-tools) for guidance on prompting Claude to distinguish between environments.

## Next steps



[Text editor tool](agents-and-tools-tool-use-text-editor-tool.md)

View and modify text files to debug, fix, and improve code.



[Tool use with Claude](agents-and-tools-tool-use-overview.md)

Connect Claude to external tools and APIs. See where tools execute, when Claude calls them, and which tool fits your task.
