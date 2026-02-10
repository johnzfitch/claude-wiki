---
category: "05-Agent-SDK"
fetched_at: "2026-02-07T10:04:47Z"
source_url: "https://platform.claude.com/docs/en/agent-sdk/plugins"
title: "Plugins in the SDK - Claude API Docs"
---

Guides

# Plugins in the SDK

Copy page

Load custom plugins to extend Claude Code with commands, agents, skills, and hooks through the Agent SDK

Copy page

Plugins allow you to extend Claude Code with custom functionality that can be shared across projects. Through the Agent SDK, you can programmatically load plugins from local directories to add custom slash commands, agents, skills, hooks, and MCP servers to your agent sessions.

## 

What are plugins?

Plugins are packages of Claude Code extensions that can include:

- **Commands**: Custom slash commands
- **Agents**: Specialized subagents for specific tasks
- **Skills**: Model-invoked capabilities that Claude uses autonomously
- **Hooks**: Event handlers that respond to tool use and other events
- **MCP servers**: External tool integrations via Model Context Protocol

For complete information on plugin structure and how to create plugins, see [Plugins](https://code.claude.com/docs/en/plugins).

## 

Loading plugins

Load plugins by providing their local file system paths in your options configuration. The SDK supports loading multiple plugins from different locations.

TypeScript

``` shiki
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Hello",
  options: {
    plugins: [
      { type: "local", path: "./my-plugin" },
      { type: "local", path: "/absolute/path/to/another-plugin" }
    ]
  }
})) {
  // Plugin commands, agents, and other features are now available
}
```

### 

Path specifications

Plugin paths can be:

- **Relative paths**: Resolved relative to your current working directory (e.g., `"./plugins/my-plugin"`)
- **Absolute paths**: Full file system paths (e.g., `"/home/user/plugins/my-plugin"`)

The path should point to the plugin's root directory (the directory containing `.claude-plugin/plugin.json`).

## 

Verifying plugin installation

When plugins load successfully, they appear in the system initialization message. You can verify that your plugins are available:

TypeScript

``` shiki
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Hello",
  options: {
    plugins: [{ type: "local", path: "./my-plugin" }]
  }
})) {
  if (message.type === "system" && message.subtype === "init") {
    // Check loaded plugins
    console.log("Plugins:", message.plugins);
    // Example: [{ name: "my-plugin", path: "./my-plugin" }]

    // Check available commands from plugins
    console.log("Commands:", message.slash_commands);
    // Example: ["/help", "/compact", "my-plugin:custom-command"]
  }
}
```

## 

Using plugin commands

Commands from plugins are automatically namespaced with the plugin name to avoid conflicts. The format is `plugin-name:command-name`.

TypeScript

``` shiki
import { query } from "@anthropic-ai/claude-agent-sdk";

// Load a plugin with a custom /greet command
for await (const message of query({
  prompt: "/my-plugin:greet",  // Use plugin command with namespace
  options: {
    plugins: [{ type: "local", path: "./my-plugin" }]
  }
})) {
  // Claude executes the custom greeting command from the plugin
  if (message.type === "assistant") {
    console.log(message.content);
  }
}
```

If you installed a plugin via the CLI (e.g., `/plugin install my-plugin@marketplace`), you can still use it in the SDK by providing its installation path. Check `~/.claude/plugins/` for CLI-installed plugins.

## 

Complete example

Here's a full example demonstrating plugin loading and usage:

TypeScript

``` shiki
import { query } from "@anthropic-ai/claude-agent-sdk";
import * as path from "path";

async function runWithPlugin() {
  const pluginPath = path.join(__dirname, "plugins", "my-plugin");

  console.log("Loading plugin from:", pluginPath);

  for await (const message of query({
    prompt: "What custom commands do you have available?",
    options: {
      plugins: [
        { type: "local", path: pluginPath }
      ],
      maxTurns: 3
    }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      console.log("Loaded plugins:", message.plugins);
      console.log("Available commands:", message.slash_commands);
    }

    if (message.type === "assistant") {
      console.log("Assistant:", message.content);
    }
  }
}

runWithPlugin().catch(console.error);
```

## 

Plugin structure reference

A plugin directory must contain a `.claude-plugin/plugin.json` manifest file. It can optionally include:

``` inline-block
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required: plugin manifest
├── commands/                 # Custom slash commands
│   └── custom-cmd.md
├── agents/                   # Custom agents
│   └── specialist.md
├── skills/                   # Agent Skills
│   └── my-skill/
│       └── SKILL.md
├── hooks/                    # Event handlers
│   └── hooks.json
└── .mcp.json                # MCP server definitions
```

For detailed information on creating plugins, see:

- [Plugins](https://code.claude.com/docs/en/plugins) - Complete plugin development guide
- [Plugins reference](https://code.claude.com/docs/en/plugins-reference) - Technical specifications and schemas

## 

Common use cases

### 

Development and testing

Load plugins during development without installing them globally:

``` shiki
plugins: [
  { type: "local", path: "./dev-plugins/my-plugin" }
]
```

### 

Project-specific extensions

Include plugins in your project repository for team-wide consistency:

``` shiki
plugins: [
  { type: "local", path: "./project-plugins/team-workflows" }
]
```

### 

Multiple plugin sources

Combine plugins from different locations:

``` shiki
plugins: [
  { type: "local", path: "./local-plugin" },
  { type: "local", path: "~/.claude/custom-plugins/shared-plugin" }
]
```

## 

Troubleshooting

### 

Plugin not loading

If your plugin doesn't appear in the init message:

1.  **Check the path**: Ensure the path points to the plugin root directory (containing `.claude-plugin/`)
2.  **Validate plugin.json**: Ensure your manifest file has valid JSON syntax
3.  **Check file permissions**: Ensure the plugin directory is readable

### 

Commands not available

If plugin commands don't work:

1.  **Use the namespace**: Plugin commands require the `plugin-name:command-name` format
2.  **Check init message**: Verify the command appears in `slash_commands` with the correct namespace
3.  **Validate command files**: Ensure command markdown files are in the `commands/` directory

### 

Path resolution issues

If relative paths don't work:

1.  **Check working directory**: Relative paths are resolved from your current working directory
2.  **Use absolute paths**: For reliability, consider using absolute paths
3.  **Normalize paths**: Use path utilities to construct paths correctly

## 

See also

- [Plugins](https://code.claude.com/docs/en/plugins) - Complete plugin development guide
- [Plugins reference](https://code.claude.com/docs/en/plugins-reference) - Technical specifications
- [Slash Commands](/docs/en/agent-sdk/slash-commands) - Using slash commands in the SDK
- [Subagents](/docs/en/agent-sdk/subagents) - Working with specialized agents
- [Skills](/docs/en/agent-sdk/skills) - Using Agent Skills

Was this page helpful?

- 

- [What are plugins?](#what-are-plugins)

- [Loading plugins](#loading-plugins)

- [Path specifications](#path-specifications)

- [Verifying plugin installation](#verifying-plugin-installation)

- [Using plugin commands](#using-plugin-commands)

- [Complete example](#complete-example)

- [Plugin structure reference](#plugin-structure-reference)

- [Common use cases](#common-use-cases)

- [Development and testing](#development-and-testing)

- [Project-specific extensions](#project-specific-extensions)

- [Multiple plugin sources](#multiple-plugin-sources)

- [Troubleshooting](#troubleshooting)

- [Plugin not loading](#plugin-not-loading)

- [Commands not available](#commands-not-available)

- [Path resolution issues](#path-resolution-issues)

- [See also](#see-also)

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
