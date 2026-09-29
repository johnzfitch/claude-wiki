# Agent SDK

35 pages. The full text of every page is in [llms.txt](llms.txt).

- [Agent SDK overview - Claude Code Docs](agent-sdk-overview.md) — Build production AI agents with Claude Code as a library
- [Agent SDK reference - Python - Claude Code Docs](agent-sdk-python.md) — Complete API reference for the Python Agent SDK, including all functions, types, and classes.
- [Agent SDK reference - TypeScript - Claude Code Docs](agent-sdk-typescript.md) — Complete API reference for the TypeScript Agent SDK, including all functions, types, and interfaces.
- [Agent Sdk Verifier Py](claude-code-plugins-agent-sdk-dev-agents-agent-sdk-verifier-py.md) — You are a Python Agent SDK application verifier. Your role is to thoroughly inspect Python Agent SDK applications for correct SDK usage, adherence to official…
- [Agent Sdk Verifier Ts](claude-code-plugins-agent-sdk-dev-agents-agent-sdk-verifier-ts.md) — You are a TypeScript Agent SDK application verifier. Your role is to thoroughly inspect TypeScript Agent SDK applications for correct SDK usage, adherence to…
- [Configure permissions - Claude Code Docs](agent-sdk-permissions.md) — Control and observability
- [Configure your agent - Claude Code Docs](agent-sdk-configuration.md) — Configure Agent SDK sessions: compose the options object, set the model, environment, and limits, and find each feature option’s page.
- [Connect to external tools with MCP - Claude Code Docs](agent-sdk-mcp.md) — Configure MCP servers to extend your agent with external tools. Covers transport types, tool search for large tool sets, authentication, and error handling.
- [Examples - Claude Code Docs](agent-sdk-examples.md) — Find a complete, runnable Agent SDK project or a guided recipe in the Claude Cookbook that matches what you want to build.
- [Extend agents with skills - Claude Code Docs](agent-sdk-skills.md) — Control which skills Claude can invoke in Claude Agent SDK sessions, dispatch commands by name, and author skills your sessions discover
- [Get structured output from agents - Claude Code Docs](agent-sdk-structured-outputs.md) — Return validated JSON from agent workflows using JSON Schema, Zod, or Pydantic. Get type-safe, structured data after multi-turn tool use.
- [Give Claude custom tools - Claude Code Docs](agent-sdk-custom-tools.md) — Define custom tools with the Claude Agent SDK’s in-process MCP server so Claude can call your functions, hit your APIs, and perform domain-specific operations.
- [Handle approvals and user input - Claude Code Docs](agent-sdk-user-input.md) — Surface Claude’s approval requests and clarifying questions to users, then return their decisions to the SDK.
- [Hosting the Agent SDK - Claude Code Docs](agent-sdk-hosting.md) — Deploy the Agent SDK in production: subprocess architecture, session persistence, scaling, observability, and multi-tenant isolation for Docker, Kubernetes…
- [How the agent loop works - Claude Code Docs](agent-sdk-agent-loop.md) — Understand the message lifecycle, tool execution, context window, and architecture that power your SDK agents.
- [Intercept and control agent behavior with hooks - Claude Code Docs](agent-sdk-hooks.md) — Control and observability
- [Migrate to Claude Agent SDK - Claude Code Docs](agent-sdk-migration-guide.md) — Guide for migrating the Claude Code TypeScript and Python SDKs to the Claude Agent SDK
- [Modifying system prompts - Claude Code Docs](agent-sdk-modifying-system-prompts.md) — Choose between the claudecode preset and a custom system prompt, and customize behavior with CLAUDE.md, output styles, append, or a fully custom prompt.
- [Observability with OpenTelemetry - Claude Code Docs](agent-sdk-observability.md) — Control and observability
- [Persist sessions to external storage - Claude Code Docs](agent-sdk-session-storage.md) — Mirror Agent SDK session transcripts to your own object store, key-value store, or database so other hosts can resume your sessions.
- [Plugins in the SDK - Claude Code Docs](agent-sdk-plugins.md) — Load custom plugins to extend Claude Code with skills, agents, hooks, and MCP servers through the Agent SDK
- [Quickstart - Claude Code Docs](agent-sdk-quickstart.md) — Get started with the Python or TypeScript Agent SDK to build AI agents that work autonomously
- [Rewind file changes with checkpointing - Claude Code Docs](agent-sdk-file-checkpointing.md) — Control and observability
- [Scale to many tools with tool search - Claude Code Docs](agent-sdk-tool-search.md) — Scale your agent to thousands of tools by discovering and loading only what’s needed, on demand.
- [Securely deploying AI agents - Claude Code Docs](agent-sdk-secure-deployment.md) — A guide to securing Claude Code and Agent SDK deployments with isolation, credential management, and network controls
- [Slash Commands in the SDK - Claude Code Docs](agent-sdk-slash-commands.md) — Learn how to use slash commands to control Claude Code sessions through the SDK
- [Stream responses in real-time - Claude Code Docs](agent-sdk-streaming-output.md) — Get real-time responses from the Agent SDK as text and tool calls stream in
- [Streaming Input - Claude Code Docs](agent-sdk-streaming-vs-single-mode.md) — Understanding the two input modes for Claude Agent SDK and when to use each
- [Subagents in the SDK - Claude Code Docs](agent-sdk-subagents.md) — Define and invoke subagents to isolate context, run tasks in parallel, and apply specialized instructions in your Claude Agent SDK applications.
- [Track cost and usage - Claude Code Docs](agent-sdk-cost-tracking.md) — Control and observability
- [Track todos - Claude Code Docs](agent-sdk-todo-tracking.md) — Control and observability
- [Troubleshoot the Agent SDK - Claude Code Docs](agent-sdk-troubleshooting.md) — Fix Agent SDK errors when the Claude Code CLI fails to start, the CLI process exits, or a successful result arrives without structured output.
- [TypeScript SDK V2 session API (removed) - Claude Code Docs](agent-sdk-typescript-v2-preview.md) — Reference for the removed V2 TypeScript Agent SDK session API, with session-based send/stream patterns for multi-turn conversations.
- [Use Claude Code features in the SDK - Claude Code Docs](agent-sdk-claude-code-features.md) — Load project instructions, skills, hooks, and other Claude Code features into your SDK agents.
- [Work with sessions - Claude Code Docs](agent-sdk-sessions.md) — How sessions persist agent conversation history, and when to use continue, resume, and fork to return to a prior run.
