# Plugin System Capabilities — Reality Check

**Date**: 2026-03-15
**Critical Question**: Can plugins implement dynamic `getSystemPrompt()` and `getPromptForCommand()`, or are they limited to static markdown?

---

## TL;DR: Major Limitation Discovered

**Plugin agents and skills are STATIC markdown files only.**

The dynamic JavaScript functions (`getSystemPrompt({ toolUseContext })` and `getPromptForCommand(args)`) are **ONLY available to built-in agents/skills** compiled into the binary.

Plugins **cannot** provide JavaScript implementations. They can only provide:
- ✅ Static markdown agent definitions (`agents/*.md`)
- ✅ Static markdown skill definitions (`skills/*/SKILL.md`)
- ✅ Static slash commands (`commands/*.md` or inline in manifest)
- ✅ MCP servers (which CAN have dynamic logic via MCP protocol)

---

## What Built-In Agents Can Do vs. Plugin Agents

### Built-In Agents (JavaScript in Binary)

```javascript
// File: built-in agent in binary source code
export default {
  agentType: "claude-code-guide",
  whenToUse: "Use when user asks about Claude Code...",
  tools: ["Read", "WebFetch"],
  source: "built-in",
  model: "haiku",

  // ✅ DYNAMIC systemPrompt with runtime context
  getSystemPrompt({ toolUseContext }) {
    const baseKnowledge = `<static expertise here>`;

    // Can access runtime state
    const commands = toolUseContext.options.commands;
    const agents = toolUseContext.options.agentDefinitions.activeAgents;
    const mcpClients = toolUseContext.options.mcpClients;
    const settings = getCurrentSettings();

    // Build dynamic context
    const sections = [];
    if (commands.length > 0) {
      sections.push(`**Available skills**: ${commands.map(c => c.name).join(', ')}`);
    }

    return `${baseKnowledge}\n\n---\n\n${sections.join('\n\n')}`;
  }
};
```

**Capabilities**:
- ✅ Access runtime state via `toolUseContext`
- ✅ Inject current project files, settings, MCP servers
- ✅ Dynamic logic (conditionals, loops, data processing)
- ✅ Import modules, call functions
- ❌ Requires modifying Claude Code binary

### Plugin Agents (Markdown Files)

```markdown
---
name: burn-architect
description: Burn architecture specialist — tensors, modules, autodiff
tools:
  - Read
  - Write
  - Grep
  - Glob
model: sonnet
memory: project
---

You are the Burn architecture specialist with deep expertise in:

## Core Tensor Operations

- `Tensor::zeros(shape)` — zero-initialized tensor
- `Tensor::ones(shape)` — one-initialized
...

## Module Design Patterns

...
```

**How it's processed**:
1. YAML frontmatter is parsed
2. Markdown body becomes the `systemPrompt` (static string)
3. No dynamic logic possible
4. No access to `toolUseContext`

**Capabilities**:
- ✅ Static systemPrompt from markdown
- ✅ Tool restrictions via `tools` field
- ✅ Memory persistence via `memory` field
- ✅ Model selection via `model` field
- ❌ NO dynamic context injection
- ❌ NO runtime state access
- ❌ NO conditional logic

---

## What Built-In Skills Can Do vs. Plugin Skills

### Built-In Skills (JavaScript in Binary)

```javascript
// File: built-in skill in binary source code
{
  name: "claude-api",
  description: "Build apps with the Claude API...",
  allowedTools: ["Read", "Grep", "Glob", "WebFetch"],
  userInvocable: true,

  // ✅ DYNAMIC prompt generation
  async getPromptForCommand(userArgs) {
    // Detect project language
    const lang = await detectProjectLanguage();

    // Filter docs by language
    const relevantDocs = allDocs.filter(doc =>
      doc.path.startsWith(`${lang}/`) || doc.path.startsWith('shared/')
    );

    // Build dynamic prompt
    const docsContent = relevantDocs.map(doc =>
      `<doc path="${doc.path}">\n${doc.content}\n</doc>`
    ).join('\n\n');

    return [{
      type: "text",
      text: `${quickRef}\n\n${docsContent}\n\n## User Request\n\n${userArgs}`
    }];
  }
}
```

**Capabilities**:
- ✅ Dynamic prompt generation based on user input
- ✅ Async operations (file reading, detection)
- ✅ Conditional logic (language detection, filtering)
- ✅ Can bundle docs as JavaScript strings
- ❌ Requires modifying Claude Code binary

### Plugin Skills (Markdown Files)

```markdown
---
name: burn-docs
description: Load Burn framework API documentation
allowedTools:
  - Read
  - Grep
---

# Burn Framework Reference

## Quick Navigation

**Tensor operations**: Core tensor APIs
**Module patterns**: Design patterns
**Backend selection**: WGPU, CUDA, Metal

---

## Tensor Operations

### Creating Tensors

```rust
let zeros = Tensor::<Backend, 2>::zeros([3, 4], &device);
```

...
```

**How it's processed**:
1. YAML frontmatter is parsed
2. Markdown body is injected as-is when skill is invoked
3. No dynamic logic
4. No user argument access

**Capabilities**:
- ✅ Static markdown content injected on invocation
- ✅ Tool restrictions via `allowedTools` field
- ❌ NO dynamic prompt generation
- ❌ NO access to user arguments
- ❌ NO conditional content
- ❌ NO file reading or language detection

---

## The Critical Difference

| Feature | Built-In (Binary JS) | Plugin (Markdown) |
|---------|---------------------|-------------------|
| **Agent systemPrompt** | Dynamic `getSystemPrompt({ toolUseContext })` | Static markdown body |
| **Skill prompt** | Dynamic `getPromptForCommand(args)` | Static markdown body |
| **Runtime context** | Full access via `toolUseContext` | None |
| **Conditional logic** | Full JavaScript | None |
| **User arguments** | Direct access in skills | None |
| **Language detection** | Can implement | None |
| **File I/O** | Can read project files | Via allowed tools only |
| **Data processing** | Full capabilities | None |
| **Bundled resources** | JavaScript strings | External files only |

---

## What This Means for Burn Plugin

### What We CAN Do (Pure Plugin)

✅ **Static agent definitions** with embedded expertise:
```markdown
---
name: burn-architect
description: Burn architecture specialist
---
You are a Burn expert. Here's the API:
- Tensor::zeros(shape)
- Tensor::ones(shape)
...
```

✅ **Static skill documentation**:
```markdown
---
name: burn-docs
---
# Burn Framework Docs
[All docs embedded here]
```

✅ **MCP server for dynamic logic**:
```python
# MCP server CAN have dynamic logic
@app.tool()
async def query_burn_docs(query: str) -> str:
    # ✅ Can detect language
    # ✅ Can query database
    # ✅ Can filter results
    # ✅ Can return dynamic content
    ...
```

✅ **Teammate coordination** via task system and message passing

### What We CANNOT Do (Plugin Limitations)

❌ **Dynamic agent systemPrompts** that inject current project state
  - Can't show "Burn detected in Cargo.toml"
  - Can't list existing Burn files in project
  - Can't adapt based on user's dependencies

❌ **Dynamic skill prompts** that filter docs by language/query
  - Can't detect if project is using Burn 0.20 vs 0.21
  - Can't filter docs to only Python or Rust
  - Can't inject only relevant docs based on user query

❌ **Bundled documentation in JavaScript**
  - Must ship docs as separate .md files
  - Can't bundle 20 docs into one JavaScript string
  - Can't programmatically filter at invocation time

❌ **Runtime state awareness**
  - Agents can't see what MCP servers are connected
  - Agents can't see user's settings.json
  - Agents can't see what other skills/agents are available

---

## Workarounds Using MCP

The **only way to get dynamic behavior** in plugins is via MCP servers:

### MCP Server for Dynamic Documentation

```python
# plugins/burn-mcp/server.py
from mcp.server import Server

app = Server("burn-kb")

# ✅ Can implement dynamic logic
@app.tool()
async def get_burn_docs(topic: str, version: str = "0.20") -> str:
    # Detect project Burn version
    if version == "auto":
        version = await detect_burn_version()

    # Filter docs by topic
    relevant_docs = filter_docs_by_topic(topic, version)

    # Return dynamic content
    return format_docs(relevant_docs)
```

Then plugin agents call this tool:
```markdown
---
name: burn-architect
tools:
  - mcp__burn-kb__get_burn_docs
  - Read
  - Write
---

You are a Burn expert.

When answering questions:
1. Call `get_burn_docs` tool with the topic
2. Use the returned documentation
3. Provide code examples
```

**Limitation**: This requires the agent to CALL the tool (extra turn), not inject the knowledge into its systemPrompt.

### MCP Server for Runtime Context

```python
@app.tool()
async def get_project_context() -> str:
    """Get current project's Burn setup"""
    cargo_toml = read_file("Cargo.toml")
    has_burn = "burn =" in cargo_toml

    burn_files = find_files("**/*.rs", contains="burn::")

    return f"""
**Burn Status**: {'Detected' if has_burn else 'Not installed'}
**Burn Files**: {len(burn_files)} found
{chr(10).join(f'- {f}' for f in burn_files[:5])}
"""
```

Then agents call this tool, but it's **not in their systemPrompt** — they have to actively query it.

---

## Revised Architecture for Plugin

### Option 1: Pure Plugin (Static Content)

**Strengths**:
- ✅ Works with current plugin system
- ✅ No binary modifications
- ✅ Can ship today

**Weaknesses**:
- ❌ No dynamic context injection
- ❌ Large static systemPrompts (all knowledge embedded)
- ❌ No project awareness
- ❌ No language/version detection

**Implementation**:
```
burn-plugin/
├── manifest.json
├── agents/
│   ├── burn-architect.md     # All Burn API knowledge embedded
│   ├── burn-trainer.md       # All training knowledge embedded
│   └── ...
├── skills/
│   ├── burn-docs/
│   │   └── SKILL.md          # All docs embedded (50-100KB)
│   └── burn-router/
│       └── SKILL.md          # Routing decision tree
└── mcp-servers/
    └── burn-kb/              # MCP server for dynamic queries
        └── server.py
```

### Option 2: MCP-Heavy (Dynamic via Tools)

**Strengths**:
- ✅ Full dynamic behavior via MCP tools
- ✅ Project awareness
- ✅ Version detection
- ✅ Can query database

**Weaknesses**:
- ❌ Agents must CALL tools (not in systemPrompt)
- ❌ Extra turns for context gathering
- ❌ More complex setup

**Implementation**:
```
burn-plugin/
├── manifest.json
├── agents/
│   ├── burn-architect.md     # Minimal — delegates to MCP tools
│   └── ...
├── mcp-servers/
│   └── burn-kb/
│       ├── server.py         # All dynamic logic here
│       ├── tools/
│       │   ├── query_docs.py # Doc filtering & injection
│       │   ├── detect_version.py
│       │   └── get_project_context.py
│       └── knowledgebase/
│           └── burn-kb.db    # SQLite database
```

Agents then use:
```markdown
---
name: burn-architect
tools:
  - mcp__burn-kb__query_docs
  - mcp__burn-kb__get_project_context
---

You are a Burn expert.

**Before answering any question**:
1. Call `get_project_context` to see current project setup
2. Call `query_docs` with the user's question topic
3. Use the returned context and docs to answer
```

### Option 3: Hybrid (Best of Both)

**Strengths**:
- ✅ Hot-path knowledge embedded (instant access)
- ✅ Cold-path knowledge via MCP tools (scales)
- ✅ Balanced approach

**Implementation**:
- Embed 20% most-used APIs in agent systemPrompts
- Provide MCP tools for remaining 80% of docs
- Agents use tools when needed, fallback to embedded knowledge

---

## Recommendation

Given plugin limitations, **use Option 3 (Hybrid)**:

### Tier 1: Agent SystemPrompts (Static Embedded Knowledge)
- Embed the **20% hot-path knowledge** that covers 80% of queries
- Example: Core tensor operations, common module patterns
- Size: ~5-10KB per agent (acceptable for static markdown)

### Tier 2: MCP Tools (Dynamic Queryable Knowledge)
- Provide tools for **80% cold-path knowledge** (rarely used APIs)
- Example: Advanced autodiff, custom backends, obscure operations
- Implementation: SQLite database + MCP server

### Tier 3: Skills (Routing & Coordination)
- Static routing decision trees
- Team collaboration patterns
- Inject once per session

**Why this works**:
- Hot-path knowledge is instant (no tool calls)
- Cold-path knowledge is available via tools (scales to millions of docs)
- Doesn't hit plugin limitations (everything is either static markdown or MCP tools)

---

## What Would Require Binary Modifications

If Anthropic wanted to enable true dynamic plugins (like built-in agents):

1. **Plugin JavaScript execution**
   - Allow plugins to provide `.js` files for agents/skills
   - Execute in sandboxed environment
   - Provide `toolUseContext` to plugin code

2. **Plugin API extensions**
   - Expose `getProjectFiles()`, `getSettings()`, `getMcpServers()`
   - Allow plugins to read runtime state
   - Provide lifecycle hooks (onProjectOpen, onFileChange, etc.)

3. **Plugin bundling system**
   - Allow plugins to bundle resources as JavaScript
   - Tree-shakeable imports
   - Build-time optimization

**Current status**: None of this exists. Plugins are static markdown + MCP servers only.

---

## Conclusion

**Critical finding**: Plugins **cannot** implement the dynamic patterns we saw in built-in agents.

**What we can do**:
1. Static agent systemPrompts with embedded knowledge (limited by markdown size)
2. Static skill markdown injected on invocation
3. MCP tools for dynamic queries (requires extra tool calls)
4. Teammate system for coordination (works perfectly)

**What we cannot do**:
1. Dynamic systemPrompts with runtime context injection
2. Dynamic skill prompts with language detection
3. Bundled docs in JavaScript with filtering
4. Project-aware agents without tool calls

**Best path forward**: Hybrid approach with hot-path embedded + cold-path via MCP tools.
