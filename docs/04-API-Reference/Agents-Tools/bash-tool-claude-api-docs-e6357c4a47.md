---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:22Z"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool"
title: "Bash tool - Claude API Docs"
---

Tools

# Bash tool

Copy page

Copy page

The bash tool enables Claude to execute shell commands in a persistent bash session, allowing system operations, script execution, and command-line automation.

## 

Overview

The bash tool provides Claude with:

- Persistent bash session that maintains state
- Ability to run any shell command
- Access to environment variables and working directory
- Command chaining and scripting capabilities

## 

Model compatibility

| Model | Tool Version |
|----|----|
| Claude 4 models and Sonnet 3.7 ([deprecated](/docs/en/about-claude/model-deprecations)) | `bash_20250124` |

Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.

## 

Use cases

- **Development workflows**: Run build commands, tests, and development tools
- **System automation**: Execute scripts, manage files, automate tasks
- **Data processing**: Process files, run analysis scripts, manage datasets
- **Environment setup**: Install packages, configure environments

## 

Quick start

Python

``` shiki
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=[
        {
            "type": "bash_20250124",
            "name": "bash"
        }
    ],
    messages=[
        {"role": "user", "content": "List all Python files in the current directory."}
    ]
)
```

## 

How it works

The bash tool maintains a persistent session:

1.  Claude determines what command to run
2.  You execute the command in a bash shell
3.  Return the output (stdout and stderr) to Claude
4.  Session state persists between commands (environment variables, working directory)

## 

Parameters

| Parameter | Required | Description                               |
|-----------|----------|-------------------------------------------|
| `command` | Yes\*    | The bash command to run                   |
| `restart` | No       | Set to `true` to restart the bash session |

\*Required unless using `restart`

### Example usage

## 

Example: Multi-step automation

Claude can chain commands to complete complex tasks:

``` shiki
# User request
"Install the requests library and create a simple Python script that fetches a joke from an API, then run it."

# Claude's tool uses:
# 1. Install package
{"command": "pip install requests"}

# 2. Create script
{"command": "cat > fetch_joke.py << 'EOF'\nimport requests\nresponse = requests.get('https://official-joke-api.appspot.com/random_joke')\njoke = response.json()\nprint(f\"Setup: {joke['setup']}\")\nprint(f\"Punchline: {joke['punchline']}\")\nEOF"}

# 3. Run script
{"command": "python fetch_joke.py"}
```

The session maintains state between commands, so files created in step 2 are available in step 3.

------------------------------------------------------------------------

## 

Implement the bash tool

The bash tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

1.  1

    Set up a bash environment

    Create a persistent bash session that Claude can interact with:

    ``` shiki
    import subprocess
    import threading
    import queue

    class BashSession:
        def __init__(self):
            self.process = subprocess.Popen(
                ['/bin/bash'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=0
            )
            self.output_queue = queue.Queue()
            self.error_queue = queue.Queue()
            self._start_readers()
    ```

2.  2

    Handle command execution

    Create a function to execute commands and capture output:

    ``` shiki
    def execute_command(self, command):
        # Send command to bash
        self.process.stdin.write(command + '\n')
        self.process.stdin.flush()
        
        # Capture output with timeout
        output = self._read_output(timeout=10)
        return output
    ```

3.  3

    Process Claude's tool calls

    Extract and execute commands from Claude's responses:

    ``` shiki
    for content in response.content:
        if content.type == "tool_use" and content.name == "bash":
            if content.input.get("restart"):
                bash_session.restart()
                result = "Bash session restarted"
            else:
                command = content.input.get("command")
                result = bash_session.execute_command(command)
            
            # Return result to Claude
            tool_result = {
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": result
            }
    ```

4.  4

    Implement safety measures

    Add validation and restrictions:

    ``` shiki
    def validate_command(command):
        # Block dangerous commands
        dangerous_patterns = ['rm -rf /', 'format', ':(){:|:&};:']
        for pattern in dangerous_patterns:
            if pattern in command:
                return False, f"Command contains dangerous pattern: {pattern}"
        
        # Add more validation as needed
        return True, None
    ```

### 

Handle errors

When implementing the bash tool, handle various error scenarios:

### Command execution timeout

### Command not found

### Permission denied

### 

Follow implementation best practices

### Use command timeouts

### Maintain session state

### Handle large outputs

### Log all commands

### Sanitize outputs

## 

Security

The bash tool provides direct system access. Implement these essential safety measures:

- Running in isolated environments (Docker/VM)
- Implementing command filtering and allowlists
- Setting resource limits (CPU, memory, disk)
- Logging all executed commands

### 

Key recommendations

- Use `ulimit` to set resource constraints
- Filter dangerous commands (`sudo`, `rm -rf`, etc.)
- Run with minimal user permissions
- Monitor and log all command execution

## 

Pricing

The bash tool adds **245 input tokens** to your API calls.

Additional tokens are consumed by:

- Command outputs (stdout/stderr)
- Error messages
- Large file contents

See [tool use pricing](/docs/en/agents-and-tools/tool-use/overview#pricing) for complete pricing details.

## 

Common patterns

### 

Development workflows

- Running tests: `pytest && coverage report`
- Building projects: `npm install && npm run build`
- Git operations: `git status && git add . && git commit -m "message"`

### 

File operations

- Processing data: `wc -l *.csv && ls -lh *.csv`
- Searching files: `find . -name "*.py" | xargs grep "pattern"`
- Creating backups: `tar -czf backup.tar.gz ./data`

### 

System tasks

- Checking resources: `df -h && free -m`
- Process management: `ps aux | grep python`
- Environment setup: `export PATH=$PATH:/new/path && echo $PATH`

## 

Limitations

- **No interactive commands**: Cannot handle `vim`, `less`, or password prompts
- **No GUI applications**: Command-line only
- **Session scope**: Persists within conversation, lost between API calls
- **Output limits**: Large outputs may be truncated
- **No streaming**: Results returned after completion

## 

Combining with other tools

The bash tool is most powerful when combined with the [text editor](/docs/en/agents-and-tools/tool-use/text-editor-tool) and other tools.

## 

Next steps

[](/docs/en/agents-and-tools/tool-use/overview)

Tool use overview

Learn about tool use with Claude

[](/docs/en/agents-and-tools/tool-use/text-editor-tool)

Text editor tool

View and edit text files with Claude

Was this page helpful?

- 

- [Overview](#overview)

- [Model compatibility](#model-compatibility)

- [Use cases](#use-cases)

- [Quick start](#quick-start)

- [How it works](#how-it-works)

- [Parameters](#parameters)

- [Example: Multi-step automation](#example-multi-step-automation)

- [Implement the bash tool](#implement-the-bash-tool)

- [Handle errors](#handle-errors)

- [Follow implementation best practices](#follow-implementation-best-practices)

- [Security](#security)

- [Key recommendations](#key-recommendations)

- [Pricing](#pricing)

- [Common patterns](#common-patterns)

- [Development workflows](#development-workflows)

- [File operations](#file-operations)

- [System tasks](#system-tasks)

- [Limitations](#limitations)

- [Combining with other tools](#combining-with-other-tools)

- [Next steps](#next-steps)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
