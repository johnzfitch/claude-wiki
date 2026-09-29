---
title: "Text editor tool - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:22Z"
tags: ["api"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Ftext-editor-tool)

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

# Text editor tool

Copy page



Give Claude the Anthropic-defined text editor tool to view, create, and edit files, and handle its view, str_replace, create, and insert commands.

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

Claude can use an Anthropic-schema text editor tool to view and modify text files, helping you debug, fix, and improve your code or other text documents. This allows Claude to directly interact with your files, providing hands-on assistance rather than just suggesting changes.

For model support, see the [Tool reference](agents-and-tools-tool-use-tool-reference.md).

## When to use the text editor tool

Some examples of when to use the text editor tool are:

- **Code debugging:** Have Claude identify and fix bugs in your code, from syntax errors to logic issues.
- **Code refactoring:** Let Claude improve your code structure, readability, and performance through targeted edits.
- **Documentation generation:** Ask Claude to add docstrings, comments, or README files to your code base.
- **Test creation:** Have Claude create unit tests for your code based on its analysis of the implementation.

## Use the text editor tool

Provide the text editor tool (named `str_replace_based_edit_tool`) to Claude using the Messages API.

You can optionally specify a `max_characters` parameter to control truncation when viewing large files.



`max_characters` is only compatible with `text_editor_20250728` and later versions of the text editor tool.

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
    tools=[
        {
            "type": "text_editor_20250728",
            "name": "str_replace_based_edit_tool",
            "max_characters": 10000,
        }
    ],
    messages=[
        {
            "role": "user",
            "content": "There's a syntax error in my primes.py file. Can you help me fix it?",
        }
    ],
)

print(response)
```

Use the text editor tool in the following way:

1.  1

    ### Provide Claude with the text editor tool and a user prompt

    - Include the text editor tool in your API request
    - Provide a user prompt that may require examining or modifying files, such as "Can you fix the syntax error in my code?"

2.  2

    ### Claude uses the tool to examine files or directories

    - Claude assesses what it needs to look at and uses the `view` command to examine file contents or list directory contents
    - The API response will contain a `tool_use` content block with the `view` command

3.  3

    ### Execute the view command and return results

    - Extract the file or directory path from Claude's tool use request
    - Read the file's contents or list the directory contents
    - If a `max_characters` parameter was specified in the tool configuration, truncate the file contents to that length
    - Return the results to Claude by continuing the conversation with a new `user` message containing a `tool_result` content block

4.  4

    ### Claude uses the tool to modify files

    - After examining the file or directory, Claude may use a command such as `str_replace` to make changes or `insert` to add text at a specific line number.
    - If Claude uses the `str_replace` command, Claude constructs a properly formatted tool use request with the old text and new text to replace it with

5.  5

    ### Execute the edit and return results

    - Extract the file path, old text, and new text from Claude's tool use request
    - Perform the text replacement in the file
    - Return the results to Claude

6.  6

    ### Claude provides its analysis and explanation

    - After examining and possibly editing the files, Claude provides a complete explanation of what it found and what changes it made

### Text editor tool commands

The text editor tool supports several commands for viewing and modifying files:

#### view

The `view` command allows Claude to examine the contents of a file or list the contents of a directory. It can read the entire file or a specific range of lines.

Parameters:

- `command`: Must be "view"
- `path`: The path to the file or directory to view
- `view_range` (optional): An array of two integers specifying the start and end line numbers to view. Line numbers are 1-indexed, and -1 for the end line means read to the end of the file. This parameter only applies when viewing files, not directories.

### Example view commands

Example for viewing a file:

```python
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "str_replace_based_edit_tool",
  "input": {
    "command": "view",
    "path": "primes.py"
  }
}
```



Example for viewing a directory:

```python
{
  "type": "tool_use",
  "id": "toolu_02B19r91rw91mr917835mr9",
  "name": "str_replace_based_edit_tool",
  "input": {
    "command": "view",
    "path": "src/"
  }
}
```



#### str_replace

The `str_replace` command allows Claude to replace a specific string in a file with a new string. This is used for making precise edits.

Parameters:

- `command`: Must be "str_replace"
- `path`: The path to the file to modify
- `old_str`: The text to replace (must match exactly, including whitespace and indentation)
- `new_str`: The new text to insert in place of the old text

### Example str_replace command

```python
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "str_replace_based_edit_tool",
  "input": {
    "command": "str_replace",
    "path": "primes.py",
    "old_str": "for num in range(2, limit + 1)",
    "new_str": "for num in range(2, limit + 1):"
  }
}
```



#### create

The `create` command allows Claude to create a new file with specified content.

Parameters:

- `command`: Must be "create"
- `path`: The path where the new file should be created
- `file_text`: The content to write to the new file

### Example create command

```python
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "str_replace_based_edit_tool",
  "input": {
    "command": "create",
    "path": "test_primes.py",
    "file_text": "import unittest\nimport primes\n\nclass TestPrimes(unittest.TestCase):\n    def test_is_prime(self):\n        self.assertTrue(primes.is_prime(2))\n        self.assertTrue(primes.is_prime(3))\n        self.assertFalse(primes.is_prime(4))\n\nif __name__ == '__main__':\n    unittest.main()"
  }
}
```



#### insert

The `insert` command allows Claude to insert text at a specific location in a file.

Parameters:

- `command`: Must be "insert"
- `path`: The path to the file to modify
- `insert_line`: The line number after which to insert the text (0 for beginning of file)
- `insert_text`: The text to insert

### Example insert command

```python
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "str_replace_based_edit_tool",
  "input": {
    "command": "insert",
    "path": "primes.py",
    "insert_line": 0,
    "insert_text": "\"\"\"Module for working with prime numbers.\n\nThis module provides functions to check if a number is prime\nand to generate a list of prime numbers up to a given limit.\n\"\"\"\n"
  }
}
```



### Example: Fixing a syntax error with the text editor tool

This example demonstrates how Claude uses the text editor tool to fix a syntax error in a Python file.

First, your application provides Claude with the text editor tool and a prompt to fix a syntax error:

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
    tools=[{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}],
    messages=[
        {
            "role": "user",
            "content": "There's a syntax error in my primes.py file. Can you help me fix it?",
        }
    ],
)

print(response)
```

Claude uses the text editor tool first to view the file:

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
      "text": "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
    },
    {
      "type": "tool_use",
      "id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
      "name": "str_replace_based_edit_tool",
      "input": {
        "command": "view",
        "path": "primes.py"
      }
    }
  ]
}
```

Your application should then read the file and return its contents to Claude:

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
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}],
    messages=[
        {
            "role": "user",
            "content": "There's a syntax error in my primes.py file. Can you help me fix it?",
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue.",
                },
                {
                    "type": "tool_use",
                    "id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
                    "name": "str_replace_based_edit_tool",
                    "input": {"command": "view", "path": "primes.py"},
                },
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
                    "content": '1: def is_prime(n):\n2:     """Check if a number is prime."""\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     """Generate a list of prime numbers up to the given limit."""\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     """Main function to demonstrate prime number generation."""\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f"Prime numbers up to {limit}:")\n29:     print(prime_list)\n30:     print(f"Found {len(prime_list)} prime numbers.")\n31: \n32: if __name__ == "__main__":\n33:     main()',
                }
            ],
        },
    ],
)

print(response)
```



**Line numbers**

In the preceding example, the `view` tool result includes file contents with line numbers prepended to each line (for example, "1: def is_prime(n):"). Line numbers are not required, but they are essential for successfully using the `view_range` parameter to examine specific sections of files and the `insert_line` parameter to add content at precise locations.

Claude identifies the syntax error and uses the `str_replace` command to fix it:

Output



```python
{
  "id": "msg_01VwXyZAbCdEfGhIjKlMnO",
  "model": "claude-opus-5-5",
  "stop_reason": "tool_use",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
    },
    {
      "type": "tool_use",
      "id": "toolu_01PqRsTuVwXyZAbCdEfGh",
      "name": "str_replace_based_edit_tool",
      "input": {
        "command": "str_replace",
        "path": "primes.py",
        "old_str": "    for num in range(2, limit + 1)",
        "new_str": "    for num in range(2, limit + 1):"
      }
    }
  ]
}
```

Your application should then make the edit and return the result:

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
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}],
    messages=[
        # Previous messages...
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you.",
                },
                {
                    "type": "tool_use",
                    "id": "toolu_01PqRsTuVwXyZAbCdEfGh",
                    "name": "str_replace_based_edit_tool",
                    "input": {
                        "command": "str_replace",
                        "path": "primes.py",
                        "old_str": "    for num in range(2, limit + 1)",
                        "new_str": "    for num in range(2, limit + 1):",
                    },
                },
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": "toolu_01PqRsTuVwXyZAbCdEfGh",
                    "content": "Successfully replaced text at exactly one location.",
                }
            ],
        },
    ],
)

print(response)
```

Finally, Claude provides a complete explanation of the fix:

Output



```python
{
  "id": "msg_01IjKlMnOpQrStUvWxYzAb",
  "model": "claude-opus-5-5",
  "stop_reason": "end_turn",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I've fixed the syntax error in your primes.py file. The issue was in the `get_primes` function at line 19. There was a missing colon (:) at the end of the for loop line.\n\nHere's what I changed:\n\nFrom:\n```python\nfor num in range(2, limit + 1)\n```\n\nTo:\n```python\nfor num in range(2, limit + 1):\n```\n\nIn Python, a colon is required at the end of statements that start a new code block, such as for loops, if statements, function definitions, etc. Without the colon, Python raises a syntax error because it doesn't know where the code block begins.\n\nYour code should now run correctly. The function will properly generate a list of prime numbers up to the specified limit."
    }
  ]
}
```

## Implement the text editor tool

The text editor tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

The tool type is `type: "text_editor_20250728"` for Claude 4 and later models.

1.  1

    ### Initialize your editor implementation

    Create helper functions to handle file operations like reading, writing, and modifying files. Consider implementing backup functionality to recover from mistakes.

2.  2

    ### Handle editor tool calls

    Create a function that processes tool calls from Claude based on the command type:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    def handle_editor_tool(tool_call):
        input_params = tool_call.input
        command = input_params.get("command", "")
        file_path = input_params.get("path", "")

        match command:
            case "view":
                # Read and return file contents
                pass
            case "str_replace":
                # Replace text in file
                pass
            case "create":
                # Create new file
                pass
            case "insert":
                # Insert text at location
                pass
    ```

3.  3

    ### Implement security measures

    Add validation and security checks:

    - Validate file paths to prevent directory traversal
    - Create backups before making changes
    - Handle errors gracefully
    - Implement permissions checks

4.  4

    ### Process Claude's responses

    Extract and handle tool calls from Claude's responses:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    # Process tool use in Claude's response
    for content in response.content:
        if content.type == "tool_use":
            # Execute the tool based on command
            result = handle_editor_tool(content)

            # Return result to Claude
            tool_result = {
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": result,
            }
    ```



When implementing the text editor tool, keep in mind:

1.  **Security:** The tool has access to your local filesystem, so implement proper security measures.
2.  **Backup:** Always create backups before allowing edits to important files.
3.  **Validation:** Validate all inputs to prevent unintended changes.
4.  **Unique matching:** Make sure replacements match exactly one location to avoid unintended edits.

### Handle errors

When using the text editor tool, various errors may occur. Here is guidance on how to handle them:

### File not found

If Claude tries to view or modify a file that doesn't exist, return an appropriate error message in the `tool_result`:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: File not found",
      "is_error": true
    }
  ]
}
```



### Multiple matches for replacement

If Claude's `str_replace` command matches multiple locations in the file, return an appropriate error message:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: Found 3 matches for replacement text. Please provide more context to make a unique match.",
      "is_error": true
    }
  ]
}
```



### No matches for replacement

If Claude's `str_replace` command doesn't match any text in the file, return an appropriate error message:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: No match found for replacement. Please check your text and try again.",
      "is_error": true
    }
  ]
}
```



### Permission errors

If there are permission issues with creating, reading, or modifying files, return an appropriate error message:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: Permission denied. Cannot write to file.",
      "is_error": true
    }
  ]
}
```



### Follow implementation best practices

### Provide clear context

When asking Claude to fix or modify code, be specific about what files need to be examined or what issues need to be addressed. Clear context helps Claude identify the right files and make appropriate changes.

**Less helpful prompt:** "Can you fix my code?"

**Better prompt:** "There's a syntax error in my primes.py file that prevents it from running. Can you fix it?"

### Be explicit about file paths

Specify file paths clearly when needed, especially if you're working with multiple files or files in different directories.

**Less helpful prompt:** "Review my helper file"

**Better prompt:** "Can you check my utils/helpers.py file for any performance issues?"

### Create backups before editing

Implement a backup system in your application that creates copies of files before allowing Claude to edit them, especially for important or production code.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
def backup_file(file_path):
    """Create a backup of a file before editing."""
    backup_path = f"{file_path}.backup"
    if os.path.exists(file_path):
        with open(file_path, "r") as src, open(backup_path, "w") as dst:
            dst.write(src.read())
```

### Handle unique text replacement carefully

The `str_replace` command requires an exact match for the text to be replaced. Your application should ensure that there is exactly one match for the old text or provide appropriate error messages.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
def safe_replace(file_path, old_text, new_text):
    """Replace text only if there's exactly one match."""
    with open(file_path, "r") as f:
        content = f.read()

    count = content.count(old_text)
    if count == 0:
        return "Error: No match found"
    elif count > 1:
        return f"Error: Found {count} matches"
    else:
        new_content = content.replace(old_text, new_text)
        with open(file_path, "w") as f:
            f.write(new_content)
        return "Successfully replaced text"
```

### Verify changes

After Claude makes changes to a file, verify the changes by running tests or checking that the code still works as expected.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
def verify_changes(file_path):
    """Run tests or checks after making changes."""
    try:
        # For Python files, check for syntax errors
        if file_path.endswith(".py"):
            import ast

            with open(file_path, "r") as f:
                ast.parse(f.read())
            return "Syntax check passed"
    except Exception as e:
        return f"Verification failed: {str(e)}"
```

------------------------------------------------------------------------

## Pricing and token usage

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you're using.

In addition to the base tokens, the following additional input tokens are needed for the text editor tool:

| Tool                                | Additional input tokens |
|-------------------------------------|-------------------------|
| `text_editor_20250429` (Claude 4.x) | 700 tokens              |

For more detailed information about tool pricing, see [Tool use pricing](agents-and-tools-tool-use-overview.md#pricing).

## Integrate the text editor tool with other tools

You can use the text editor tool alongside other Claude tools. When combining tools, ensure you:

- Match the tool version with the model you're using
- Account for the additional token usage for all tools included in your request

## Change log

| Date             | Version                | Changes                                                                                                                                                                                                                                                                                       |
|------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| July 28, 2025    | `text_editor_20250728` | Release of an updated text editor tool that fixes some issues and adds an optional `max_characters` parameter. It is otherwise identical to `text_editor_20250429`.                                                                                                                           |
| April 29, 2025   | `text_editor_20250429` | Release of the text editor tool for Claude 4. This version removes the `undo_edit` command but maintains all other capabilities. The tool name has been updated to reflect its str_replace-based architecture.                                                                                |
| March 13, 2025   | `text_editor_20250124` | Introduction of standalone text editor tool documentation. This version is optimized for Claude Sonnet 3.7 but has identical capabilities to the previous version.                                                                                                                            |
| October 22, 2024 | `text_editor_20241022` | Initial release of the text editor tool with Claude Sonnet 3.5 (retired; see [Model deprecations](../../20-Models/about-claude-model-deprecations.md)). Provides capabilities for viewing, creating, and editing files through the `view`, `create`, `str_replace`, `insert`, and `undo_edit` commands. |

## Next steps

Here are some ideas for how to use the text editor tool in more convenient and powerful ways:

- **Integrate with your development workflow**: Build the text editor tool into your development tools or IDE
- **Create a code review system**: Have Claude review your code and make improvements
- **Build a debugging assistant**: Create a system where Claude can help you diagnose and fix issues in your code
- **Implement file format conversion**: Let Claude help you convert files from one format to another
- **Automate documentation**: Set up workflows for Claude to automatically document your code

The text editor tool enables Claude to work directly with your code base, supporting workflows from debugging to automated documentation.



[Tool use overview](agents-and-tools-tool-use-overview.md)

Learn how to implement tool workflows for use with Claude.



[Bash tool](agents-and-tools-tool-use-bash-tool.md)

Execute shell commands with Claude.
