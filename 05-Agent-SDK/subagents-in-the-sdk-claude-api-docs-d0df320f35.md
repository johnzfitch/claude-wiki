---
category: "05-Agent-SDK"
fetched_at: "2026-02-07T10:04:45Z"
source_url: "https://platform.claude.com/docs/en/agent-sdk/subagents"
title: "Subagents in the SDK - Claude API Docs"
---

Guides

# Subagents in the SDK

Copy page

Define and invoke subagents to isolate context, run tasks in parallel, and apply specialized instructions in your Claude Agent SDK applications.

Copy page

Subagents are separate agent instances that your main agent can spawn to handle focused subtasks. Use subagents to isolate context for focused subtasks, run multiple analyses in parallel, and apply specialized instructions without bloating the main agent's prompt.

This guide explains how to define and use subagents in the SDK using the `agents` parameter.

## 

Overview

You can create subagents in three ways:

- **Programmatically**: use the `agents` parameter in your `query()` options ([TypeScript](/docs/en/agent-sdk/typescript#agentdefinition), [Python](/docs/en/agent-sdk/python#agentdefinition))
- **Filesystem-based**: define agents as markdown files in `.claude/agents/` directories (see [defining subagents as files](https://code.claude.com/docs/en/sub-agents))
- **Built-in general-purpose**: Claude can invoke the built-in `general-purpose` subagent at any time via the Task tool without you defining anything

This guide focuses on the programmatic approach, which is recommended for SDK applications.

When you define subagents, Claude decides whether to invoke them based on each subagent's `description` field. Write clear descriptions that explain when the subagent should be used, and Claude will automatically delegate appropriate tasks. You can also explicitly request a subagent by name in your prompt (e.g., "Use the code-reviewer agent to...").

## 

Benefits of using subagents

### 

Context management

Subagents maintain separate context from the main agent, preventing information overload and keeping interactions focused. This isolation ensures that specialized tasks don't pollute the main conversation context with irrelevant details.

**Example**: a `research-assistant` subagent can explore dozens of files and documentation pages without cluttering the main conversation with all the intermediate search results, returning only the relevant findings.

### 

Parallelization

Multiple subagents can run concurrently, dramatically speeding up complex workflows.

**Example**: during a code review, you can run `style-checker`, `security-scanner`, and `test-coverage` subagents simultaneously, reducing review time from minutes to seconds.

### 

Specialized instructions and knowledge

Each subagent can have tailored system prompts with specific expertise, best practices, and constraints.

**Example**: a `database-migration` subagent can have detailed knowledge about SQL best practices, rollback strategies, and data integrity checks that would be unnecessary noise in the main agent's instructions.

### 

Tool restrictions

Subagents can be limited to specific tools, reducing the risk of unintended actions.

**Example**: a `doc-reviewer` subagent might only have access to Read and Grep tools, ensuring it can analyze but never accidentally modify your documentation files.

## 

Creating subagents

### 

Programmatic definition (recommended)

Define subagents directly in your code using the `agents` parameter. This example creates two subagents: a code reviewer with read-only access and a test runner that can execute commands. The `Task` tool must be included in `allowedTools` since Claude invokes subagents through the Task tool.

Python

``` shiki
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

async def main():
    async for message in query(
        prompt="Review the authentication module for security issues",
        options=ClaudeAgentOptions(
            # Task tool is required for subagent invocation
            allowed_tools=["Read", "Grep", "Glob", "Task"],
            agents={
                "code-reviewer": AgentDefinition(
                    # description tells Claude when to use this subagent
                    description="Expert code review specialist. Use for quality, security, and maintainability reviews.",
                    # prompt defines the subagent's behavior and expertise
                    prompt="""You are a code review specialist with expertise in security, performance, and best practices.

When reviewing code:
- Identify security vulnerabilities
- Check for performance issues
- Verify adherence to coding standards
- Suggest specific improvements

Be thorough but concise in your feedback.""",
                    # tools restricts what the subagent can do (read-only here)
                    tools=["Read", "Grep", "Glob"],
                    # model overrides the default model for this subagent
                    model="sonnet"
                ),
                "test-runner": AgentDefinition(
                    description="Runs and analyzes test suites. Use for test execution and coverage analysis.",
                    prompt="""You are a test execution specialist. Run tests and provide clear analysis of results.

Focus on:
- Running test commands
- Analyzing test output
- Identifying failing tests
- Suggesting fixes for failures""",
                    # Bash access lets this subagent run test commands
                    tools=["Bash", "Read", "Grep"]
                )
            }
        )
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

### 

AgentDefinition configuration

| Field | Type | Required | Description |
|----|----|----|----|
| `description` | `string` | Yes | Natural language description of when to use this agent |
| `prompt` | `string` | Yes | The agent's system prompt defining its role and behavior |
| `tools` | `string[]` | No | Array of allowed tool names. If omitted, inherits all tools |
| `model` | `'sonnet' | 'opus' | 'haiku' | 'inherit'` | No | Model override for this agent. Defaults to main model if omitted |

Subagents cannot spawn their own subagents. Don't include `Task` in a subagent's `tools` array.

### 

Filesystem-based definition (alternative)

You can also define subagents as markdown files in `.claude/agents/` directories. See the [Claude Code subagents documentation](https://code.claude.com/docs/en/sub-agents) for details on this approach. Programmatically defined agents take precedence over filesystem-based agents with the same name.

Even without defining custom subagents, Claude can spawn the built-in `general-purpose` subagent when `Task` is in your `allowedTools`. This is useful for delegating research or exploration tasks without creating specialized agents.

## 

Invoking subagents

### 

Automatic invocation

Claude automatically decides when to invoke subagents based on the task and each subagent's `description`. For example, if you define a `performance-optimizer` subagent with the description "Performance optimization specialist for query tuning", Claude will invoke it when your prompt mentions optimizing queries.

Write clear, specific descriptions so Claude can match tasks to the right subagent.

### 

Explicit invocation

To guarantee Claude uses a specific subagent, mention it by name in your prompt:

``` inline-block
"Use the code-reviewer agent to check the authentication module"
```

This bypasses automatic matching and directly invokes the named subagent.

### 

Dynamic agent configuration

You can create agent definitions dynamically based on runtime conditions. This example creates a security reviewer with different strictness levels, using a more powerful model for strict reviews.

Python

``` shiki
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

# Factory function that returns an AgentDefinition
# This pattern lets you customize agents based on runtime conditions
def create_security_agent(security_level: str) -> AgentDefinition:
    is_strict = security_level == "strict"
    return AgentDefinition(
        description="Security code reviewer",
        # Customize the prompt based on strictness level
        prompt=f"You are a {'strict' if is_strict else 'balanced'} security reviewer...",
        tools=["Read", "Grep", "Glob"],
        # Key insight: use a more capable model for high-stakes reviews
        model="opus" if is_strict else "sonnet"
    )

async def main():
    # The agent is created at query time, so each request can use different settings
    async for message in query(
        prompt="Review this PR for security issues",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Grep", "Glob", "Task"],
            agents={
                # Call the factory with your desired configuration
                "security-reviewer": create_security_agent("strict")
            }
        )
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

## 

Detecting subagent invocation

Subagents are invoked via the Task tool. To detect when a subagent is invoked, check for `tool_use` blocks with `name: "Task"`. Messages from within a subagent's context include a `parent_tool_use_id` field.

This example iterates through streamed messages, logging when a subagent is invoked and when subsequent messages originate from within that subagent's execution context.

The message structure differs between SDKs. In Python, content blocks are accessed directly via `message.content`. In TypeScript, `SDKAssistantMessage` wraps the Claude API message, so content is accessed via `message.message.content`.

Python

``` shiki
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

async def main():
    async for message in query(
        prompt="Use the code-reviewer agent to review this codebase",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Glob", "Grep", "Task"],
            agents={
                "code-reviewer": AgentDefinition(
                    description="Expert code reviewer.",
                    prompt="Analyze code quality and suggest improvements.",
                    tools=["Read", "Glob", "Grep"]
                )
            }
        )
    ):
        # Check for subagent invocation in message content
        if hasattr(message, 'content') and message.content:
            for block in message.content:
                if getattr(block, 'type', None) == 'tool_use' and block.name == 'Task':
                    print(f"Subagent invoked: {block.input.get('subagent_type')}")

        # Check if this message is from within a subagent's context
        if hasattr(message, 'parent_tool_use_id') and message.parent_tool_use_id:
            print("  (running inside subagent)")

        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

## 

Resuming subagents

Subagents can be resumed to continue where they left off. Resumed subagents retain their full conversation history, including all previous tool calls, results, and reasoning. The subagent picks up exactly where it stopped rather than starting fresh.

When a subagent completes, Claude receives its agent ID in the Task tool result. To resume a subagent programmatically:

1.  **Capture the session ID**: Extract `session_id` from messages during the first query
2.  **Extract the agent ID**: Parse `agentId` from the message content
3.  **Resume the session**: Pass `resume: sessionId` in the second query's options, and include the agent ID in your prompt

You must resume the same session to access the subagent's transcript. Each `query()` call starts a new session by default, so pass `resume: sessionId` to continue in the same session.

If you're using a custom agent (not a built-in one), you also need to pass the same agent definition in the `agents` parameter for both queries.

The example below demonstrates this flow: the first query runs a subagent and captures the session ID and agent ID, then the second query resumes the session to ask a follow-up question that requires context from the first analysis.

TypeScript

``` shiki
import { query, type SDKMessage } from '@anthropic-ai/claude-agent-sdk';

// Helper to extract agentId from message content
// Stringify to avoid traversing different block types (TextBlock, ToolResultBlock, etc.)
function extractAgentId(message: SDKMessage): string | undefined {
  if (!('message' in message)) return undefined;
  // Stringify the content so we can search it without traversing nested blocks
  const content = JSON.stringify(message.message.content);
  const match = content.match(/agentId:\s*([a-f0-9-]+)/);
  return match?.[1];
}

let agentId: string | undefined;
let sessionId: string | undefined;

// First invocation - use the Explore agent to find API endpoints
for await (const message of query({
  prompt: "Use the Explore agent to find all API endpoints in this codebase",
  options: { allowedTools: ['Read', 'Grep', 'Glob', 'Task'] }
})) {
  // Capture session_id from ResultMessage (needed to resume this session)
  if ('session_id' in message) sessionId = message.session_id;
  // Search message content for the agentId (appears in Task tool results)
  const extractedId = extractAgentId(message);
  if (extractedId) agentId = extractedId;
  // Print the final result
  if ('result' in message) console.log(message.result);
}

// Second invocation - resume and ask follow-up
if (agentId && sessionId) {
  for await (const message of query({
    prompt: `Resume agent ${agentId} and list the top 3 most complex endpoints`,
    options: { allowedTools: ['Read', 'Grep', 'Glob', 'Task'], resume: sessionId }
  })) {
    if ('result' in message) console.log(message.result);
  }
}
```

Subagent transcripts persist independently of the main conversation:

- **Main conversation compaction**: When the main conversation compacts, subagent transcripts are unaffected. They're stored in separate files.
- **Session persistence**: Subagent transcripts persist within their session. You can resume a subagent after restarting Claude Code by resuming the same session.
- **Automatic cleanup**: Transcripts are cleaned up based on the `cleanupPeriodDays` setting (default: 30 days).

## 

Tool restrictions

Subagents can have restricted tool access via the `tools` field:

- **Omit the field**: agent inherits all available tools (default)
- **Specify tools**: agent can only use listed tools

This example creates a read-only analysis agent that can examine code but cannot modify files or run commands.

Python

``` shiki
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

async def main():
    async for message in query(
        prompt="Analyze the architecture of this codebase",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Grep", "Glob", "Task"],
            agents={
                "code-analyzer": AgentDefinition(
                    description="Static code analysis and architecture review",
                    prompt="""You are a code architecture analyst. Analyze code structure,
identify patterns, and suggest improvements without making changes.""",
                    # Read-only tools: no Edit, Write, or Bash access
                    tools=["Read", "Grep", "Glob"]
                )
            }
        )
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

### 

Common tool combinations

| Use case | Tools | Description |
|----|----|----|
| Read-only analysis | `Read`, `Grep`, `Glob` | Can examine code but not modify or execute |
| Test execution | `Bash`, `Read`, `Grep` | Can run commands and analyze output |
| Code modification | `Read`, `Edit`, `Write`, `Grep`, `Glob` | Full read/write access without command execution |
| Full access | All tools | Inherits all tools from parent (omit `tools` field) |

## 

Troubleshooting

### 

Claude not delegating to subagents

If Claude completes tasks directly instead of delegating to your subagent:

1.  **Include the Task tool**: subagents are invoked via the Task tool, so it must be in `allowedTools`
2.  **Use explicit prompting**: mention the subagent by name in your prompt (e.g., "Use the code-reviewer agent to...")
3.  **Write a clear description**: explain exactly when the subagent should be used so Claude can match tasks appropriately

### 

Filesystem-based agents not loading

Agents defined in `.claude/agents/` are loaded at startup only. If you create a new agent file while Claude Code is running, restart the session to load it.

### 

Windows: long prompt failures

On Windows, subagents with very long prompts may fail due to command line length limits (8191 chars). Keep prompts concise or use filesystem-based agents for complex instructions.

## 

Related documentation

- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents): comprehensive subagent documentation including filesystem-based definitions
- [SDK overview](/docs/en/agent-sdk/overview): getting started with the Claude Agent SDK

Was this page helpful?

- 

- [Overview](#overview)

- [Benefits of using subagents](#benefits-of-using-subagents)

- [Context management](#context-management)

- [Parallelization](#parallelization)

- [Specialized instructions and knowledge](#specialized-instructions-and-knowledge)

- [Tool restrictions](#tool-restrictions)

- [Creating subagents](#creating-subagents)

- [Programmatic definition (recommended)](#programmatic-definition-recommended)

- [AgentDefinition configuration](#agent-definition-configuration)

- [Filesystem-based definition (alternative)](#filesystem-based-definition-alternative)

- [Invoking subagents](#invoking-subagents)

- [Automatic invocation](#automatic-invocation)

- [Explicit invocation](#explicit-invocation)

- [Dynamic agent configuration](#dynamic-agent-configuration)

- [Detecting subagent invocation](#detecting-subagent-invocation)

- [Resuming subagents](#resuming-subagents)

- [Tool restrictions](#tool-restrictions-2)

- [Common tool combinations](#common-tool-combinations)

- [Troubleshooting](#troubleshooting)

- [Claude not delegating to subagents](#claude-not-delegating-to-subagents)

- [Filesystem-based agents not loading](#filesystem-based-agents-not-loading)

- [Windows: long prompt failures](#windows-long-prompt-failures)

- [Related documentation](#related-documentation)

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
