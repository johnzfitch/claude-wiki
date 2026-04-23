---
title: "Plugin System + Teammate Architecture Integration"
category: "08-Plugins-Skills"
tags: ["agents", "plugins"]
---

# Plugin System + Teammate Architecture Integration

**Version**: 2.1.76
**Date**: 2026-03-14
**Purpose**: How to wire the teammate system into a Burn development team plugin

---

## Table of Contents

1. [Plugin System Architecture](#plugin-system-architecture)
2. [Agent Loading Pipeline](#agent-loading-pipeline)
3. [Plugin Manifest Schema](#plugin-manifest-schema)
4. [Agent Markdown Format](#agent-markdown-format)
5. [Skill Definition Format](#skill-definition-format)
6. [Integration Strategy](#integration-strategy)
7. [Burn Development Team Design](#burn-development-team-design)
8. [Implementation Guide](#implementation-guide)
9. [File Structure Example](#file-structure-example)

---

## Plugin System Architecture

### Plugin Discovery

Plugins are loaded from:
1. **User plugins**: `~/.claude/plugins/`
2. **Project plugins**: `./.claude/plugins/`
3. **Marketplace plugins**: Downloaded and cached

### Plugin Loading Flow

```javascript
async function KK() {
  // 1. Discover plugins from all sources
  let plugins = await discoverPlugins();

  // 2. Read plugin.json manifests
  for (let plugin of plugins) {
    let manifest = await readPluginManifest(plugin.path);
    plugin.manifest = manifest;
  }

  // 3. Load components
  let { enabled, disabled, errors } = await loadPluginComponents(plugins);

  return { enabled, disabled, errors };
}
```

### Component Loading

**Agents**:
```javascript
pgH = HA(async () => {
  let { enabled } = await KK();
  let agents = [];

  for (let plugin of enabled) {
    // Default path: plugin-root/agents/
    if (plugin.agentsPath) {
      let agentsFromDefault = await J1f(
        plugin.agentsPath,
        plugin.name,
        plugin.source,
        plugin.path,
        plugin.manifest
      );
      agents.push(...agentsFromDefault);
    }

    // Additional paths from manifest
    if (plugin.agentsPaths) {
      for (let path of plugin.agentsPaths) {
        let agentsFromPath = await loadAgentsFromPath(path, plugin);
        agents.push(...agentsFromPath);
      }
    }
  }

  return agents;
});
```

**Skills**:
```javascript
tkA = HA(async () => {
  let { enabled } = await KK();
  let skills = [];

  for (let plugin of enabled) {
    // Default path: plugin-root/skills/
    if (plugin.skillsPath) {
      let skillsFromDefault = await C9f(
        plugin.skillsPath,
        plugin.name,
        plugin.source,
        plugin.manifest,
        plugin.path
      );
      skills.push(...skillsFromDefault);
    }

    // Additional paths from manifest
    if (plugin.skillsPaths) {
      for (let path of plugin.skillsPaths) {
        let skillsFromPath = await loadSkillsFromPath(path, plugin);
        skills.push(...skillsFromPath);
      }
    }
  }

  return skills;
});
```

**Commands** (slash commands):
```javascript
// Similar pattern for commands/
// Default: plugin-root/commands/
// Additional: manifest.commandsPaths
```

**Hooks**:
```javascript
NB = HA(async () => {
  let { enabled } = await KK();
  let allHooks = {
    PreToolUse: [],
    PostToolUse: [],
    TeammateIdle: [],
    TaskCompleted: [],
    // ... all hook events
  };

  for (let plugin of enabled) {
    if (!plugin.hooksConfig) continue;

    let pluginHooks = yo1(plugin);
    for (let event of Object.keys(pluginHooks)) {
      allHooks[event].push(...pluginHooks[event]);
    }
  }

  return allHooks;
});
```

---

## Agent Loading Pipeline

### 1. Directory Scan

```javascript
async function J1f(agentsDir, pluginName, source, pluginPath, manifest, seenFiles) {
  let agents = [];

  // Recursively scan directory for .md files
  async function scanDir(dir, pathComponents = []) {
    let files = await readdir(dir);

    for (let file of files) {
      if (file.isDirectory()) {
        await scanDir(path.join(dir, file.name), [...pathComponents, file.name]);
      } else if (file.isFile() && file.name.endsWith('.md')) {
        let filePath = path.join(dir, file.name);
        let agent = await G1f(filePath, pluginName, pathComponents, source, pluginPath, manifest, seenFiles);
        if (agent) agents.push(agent);
      }
    }
  }

  await scanDir(agentsDir);
  return agents;
}
```

### 2. Markdown Parsing

```javascript
async function G1f(filePath, pluginName, pathComponents, source, pluginPath, manifest, seenFiles) {
  // Avoid duplicate loading
  if (isAlreadySeen(seenFiles, filePath)) return null;

  // Read file
  let content = await readFile(filePath, 'utf-8');

  // Parse frontmatter + content
  let { frontmatter, content: promptContent } = Pw(content, filePath);

  // Build agent type name
  let agentType = [pluginName, ...pathComponents, frontmatter.name || basename(filePath, '.md')].join(':');

  // Parse and validate
  return v1f(filePath, pluginPath, frontmatter, promptContent, source);
}
```

### 3. Agent Definition Construction

```javascript
function v1f(filePath, baseDir, frontmatter, content, source) {
  let { name, description, color, model, tools, skills, memory, background, isolation } = frontmatter;

  // Validate required fields
  if (!name || !description) return null;

  // Parse tools
  let parsedTools = Q6H(tools);  // Handles "*", array, or undefined

  // Memory auto-injection
  if (memory && parsedTools) {
    let toolSet = new Set(parsedTools);
    for (let requiredTool of [Read, Write, Bash]) {
      if (!toolSet.has(requiredTool)) {
        parsedTools = [...parsedTools, requiredTool];
      }
    }
  }

  return {
    baseDir,
    agentType: name,
    whenToUse: description,
    tools: parsedTools,
    skills: YC(skills),  // Parse skill references
    getSystemPrompt: () => {
      if (memory) {
        return content + '\n\n' + I6H(name, memory);
      }
      return content;
    },
    source,  // "plugin"
    filename: basename(filePath, '.md'),
    color,
    model,
    background,
    memory,
    isolation,
  };
}
```

---

## Plugin Manifest Schema

### Complete plugin.json Structure

```typescript
{
  // Basic metadata
  "name": "burn-dev-team",
  "version": "1.0.0",
  "description": "Burn ML framework development team",
  "author": "Your Name",
  "repository": "https://github.com/user/burn-dev-team-plugin",

  // Components (can use default paths or override)
  "agents": "agents/",              // OR specify paths
  "agents": ["agents/", "custom-agents/"],  // Multiple paths

  "skills": "skills/",
  "skills": ["skills/", "custom-skills/"],

  "commands": "commands/",
  "commands": ["commands/", "slash-commands/"],
  "commands": {                     // OR inline definitions
    "burn-help": {
      "content": "...",
      "description": "Burn framework help"
    }
  },

  "hooks": "hooks/hooks.json",
  "hooks": {                        // OR inline definitions
    "TeammateIdle": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "echo 'Teammate ${AGENT_NAME} is idle'"
      }]
    }]
  },

  // MCP servers
  "mcpServers": ".mcp.json",        // Path to MCP config
  "mcpServers": {                   // OR inline definitions
    "burn-mcp": {
      "type": "stdio",
      "command": "burn-mcp-server"
    }
  },

  // User configuration
  "userConfig": {
    "API_KEY": {
      "type": "string",
      "title": "API Key",
      "description": "Your API key",
      "sensitive": true,
      "required": true
    },
    "MODEL_PREFERENCE": {
      "type": "string",
      "title": "Preferred Model",
      "default": "sonnet",
      "required": false
    }
  }
}
```

### Zod Schema (from source)

```javascript
// Plugin manifest schema
PluginManifestSchema = C.object({
  // Required
  name: C.string().min(1),
  version: C.string().min(1),

  // Optional metadata
  description: C.string().optional(),
  author: C.string().optional(),
  repository: C.string().optional(),

  // Component paths
  agents: C.union([
    C.string(),  // Single path
    C.array(C.string())  // Multiple paths
  ]).optional(),

  skills: C.union([
    C.string(),
    C.array(C.string())
  ]).optional(),

  commands: C.union([
    C.string(),
    C.array(C.string()),
    C.record(C.string(), CommandMetadata)  // Inline commands
  ]).optional(),

  hooks: C.union([
    C.string(),  // Path to hooks.json
    C.lazy(() => HooksConfig)  // Inline hook definitions
  ]).optional(),

  mcpServers: C.union([
    C.string(),  // Path to .mcp.json
    C.record(C.string(), McpServerConfig)  // Inline MCP config
  ]).optional(),

  userConfig: C.record(C.string(), UserConfigField).optional(),
});
```

---

## Agent Markdown Format

### File Structure

```markdown
---
name: burn-architect
description: Burn framework architecture specialist - tensors, modules, autodiff
tools: ["*"]
skills: ["burn-router"]
model: sonnet
color: blue
memory: project
background: false
isolation: worktree
permissionMode: acceptEdits
effort: high
maxTurns: 50
mcpServers:
  - burn-docs-server
hooks:
  PostToolUse:
    - matcher: "Write"
      hooks:
        - type: command
          command: "rg 'TODO|FIXME' ${FILE_PATH}"
---

# Burn Architecture Specialist

You are an expert in the Burn deep learning framework. You specialize in:

- **Tensor operations**: Creating, manipulating, and optimizing tensor computations
- **Module system**: Designing neural network architectures using Burn's module trait
- **Autodiff**: Understanding and implementing automatic differentiation
- **Config system**: Using Burn's config pattern for reproducible experiments
- **Records**: Saving and loading model weights

## Your Role in the Team

When working as part of the Burn development team:

1. **Check TaskList** periodically for architecture-related tasks
2. **Claim tasks** that involve tensor operations, module design, or autodiff
3. **Coordinate** with burn-trainer for training integration
4. **Review** code for idiomatic Burn patterns
5. **Communicate** via SendMessage when you need input from teammates

## Architecture Patterns

[... detailed patterns, best practices, code examples ...]
```

### Frontmatter Fields

```typescript
interface AgentFrontmatter {
  // Required
  name: string;              // Agent identifier (becomes agentType)
  description: string;       // whenToUse description

  // Tools
  tools?: string[] | "*";    // Tool allowlist ("*" = all tools)
  disallowedTools?: string[]; // Tool denylist

  // Skills
  skills?: string[];         // Skills to preload (e.g., ["burn-router"])

  // Configuration
  model?: string;            // "sonnet" | "opus" | "haiku" | "inherit"
  color?: string;            // UI color
  permissionMode?: string;   // "default" | "acceptEdits" | "plan" | etc.
  effort?: string | number;  // "low" | "medium" | "high" | integer
  maxTurns?: number;         // Max conversation turns

  // Advanced
  memory?: "user" | "project" | "local";  // Auto-inject memory tools
  background?: boolean;      // Run in background
  isolation?: "worktree";    // Run in isolated worktree

  // MCP servers
  mcpServers?: string[] | Array<string | Record<string, McpServerConfig>>;

  // Hooks
  hooks?: HooksConfig;
}
```

---

## Skill Definition Format

### Skill Directory Structure

```
skills/
  └── burn-router/
      └── SKILL.md
```

### SKILL.md Format

```markdown
---
trigger: burn-router
description: Route Burn framework queries to specialized agents
tools: ["Agent", "TeamCreate", "SendMessage", "TaskCreate"]
model: haiku
effort: low
context: fork
---

# Burn Router Skill

This skill routes incoming Burn framework queries to the appropriate specialist:

- **Tensor operations, modules, autodiff** → burn-architect
- **Training loops, learners, metrics** → burn-trainer
- **Backend selection, deployment, WASM** → burn-deployer
- **ONNX import, model conversion** → burn-importer

## Workflow

1. Analyze the user's request
2. Determine which specialist(s) are needed
3. Create a team if multiple specialists required
4. Spawn appropriate teammates
5. Create tasks for the work
6. Coordinate execution

[... skill implementation ...]
```

### Skill Frontmatter Fields

```typescript
interface SkillFrontmatter {
  // Required
  trigger: string;           // Slash command name (/burn-router)
  description: string;       // Shown in skill list

  // Optional
  tools?: string[] | "*";    // Tool allowlist
  model?: string;            // Preferred model
  effort?: string | number;  // Effort level
  context?: "main" | "fork"; // Execution context
  argumentHint?: string;     // Args hint for UI
  allowedTools?: string[];   // Synonym for tools
}
```

---

## Integration Strategy

### Key Integration Points

1. **Plugin-defined agents** become available in the Agent tool's `subagent_type` dropdown
2. **Agent tool with `team_name` + `name`** spawns plugin agents as teammates
3. **Shared task list** coordinates work between teammates
4. **Message passing** enables inter-agent communication
5. **Hooks** monitor teammate lifecycle events

### Critical Workflow

```
User → /burn-router
  ↓
Skill analyzes request
  ↓
TeamCreate({ team_name: "burn-dev", description: "..." })
  ↓
TaskCreate tasks for work breakdown
  ↓
Agent({ name: "architect", team_name: "burn-dev", subagent_type: "burn:burn-architect", ... })
Agent({ name: "trainer", team_name: "burn-dev", subagent_type: "burn:burn-trainer", ... })
Agent({ name: "deployer", team_name: "burn-dev", subagent_type: "burn:burn-deployer", ... })
  ↓
Teammates auto-claim tasks, execute work, send idle notifications
  ↓
Team lead coordinates, assigns additional tasks
  ↓
SendMessage({ to: "*", message: { type: "shutdown_request" } }) when done
  ↓
TeamDelete()
```

### Agent Type Resolution

```javascript
// Plugin agents get namespaced names
// Format: "{pluginName}:{agentName}"
// Example: "burn:burn-architect"

// When spawning via Agent tool:
Agent({
  name: "architect",              // Teammate name (for SendMessage)
  team_name: "burn-dev",          // Team context
  subagent_type: "burn:burn-architect",  // Plugin-defined agent
  prompt: "Check TaskList for architecture tasks",
  description: "Architecture specialist"
});

// The system resolves:
// 1. subagent_type → finds agent definition from plugin
// 2. Loads agent's systemPrompt, tools, permissions
// 3. Spawns teammate with those capabilities
```

---

## Burn Development Team Design

### Team Structure

Based on the proposed structure, here's how to map to teammates:

#### Core Team Members (4 teammates)

1. **burn-architect** (was burn-app-dev)
   - **Domain**: Tensors, modules, config, autodiff, records
   - **Tools**: `["*"]` (full access)
   - **Skills**: `["burn-router"]` (routing skill)
   - **Responsibilities**: Core Burn application development, architecture decisions

2. **burn-trainer** (was burn-training)
   - **Domain**: Training loops, Learner API, metrics, datasets
   - **Tools**: `["*"]`
   - **Skills**: `["burn-router"]`
   - **Responsibilities**: Training workflows, loss functions, optimization

3. **burn-deployer** (was burn-backends)
   - **Domain**: Backend selection, WASM, no_std, fusion, quantization
   - **Tools**: `["*"]`
   - **Skills**: `["burn-router"]`
   - **Responsibilities**: Production deployment, performance optimization

4. **burn-importer** (was burn-onnx + burn-onnx-surgeon)
   - **Domain**: ONNX import, model conversion, troubleshooting
   - **Tools**: `["*"]`
   - **Skills**: `["burn-router"]`
   - **Responsibilities**: External model integration, format conversion

#### Ecosystem Specialists (4 teammates)

5. **burn-lm**
   - **Domain**: Llama inference/training, InferenceServer
   - **Tools**: `["*"]`
   - **MCP Servers**: `["burn-lm-docs"]`

6. **burn-central**
   - **Domain**: Experiment tracking, model sharing
   - **Tools**: `["*"]`

7. **burn-models**
   - **Domain**: Pre-trained model zoo (8 official + community)
   - **Tools**: `["Read", "WebFetch", "Bash"]`

8. **burn-bench**
   - **Domain**: Benchmarking infrastructure
   - **Tools**: `["*"]`

#### Coordinator Skills

9. **burn-cubecl** (skill, not teammate)
   - **Type**: Skill (not a teammate - invoked when needed)
   - **Trigger**: `/burn-cubecl`
   - **Context**: Fork
   - **Domain**: GPU kernels, CubeCL, #[cube] macro

10. **burn-contrib** (skill, not teammate)
    - **Trigger**: `/burn-contrib`
    - **Domain**: Contributing to Burn codebase

11. **burn-router** (skill, not teammate)
    - **Trigger**: `/burn-router`
    - **Domain**: Intent classification → routing to specialists

### Teammate Capabilities Matrix

| Agent | Debug | Review | Full-Stack | Background |
|-------|-------|--------|------------|------------|
| burn-architect | ✓ | ✓ | ✓ | ✗ |
| burn-trainer | ✓ | ✓ | ✓ | ✗ |
| burn-deployer | ✓ | ✓ | ✓ | ✗ |
| burn-importer | ✓ | ✓ | ✓ | ✗ |
| burn-lm | ✓ | ✓ | ✓ | ✓ |
| burn-central | ✓ | ✓ | ✓ | ✓ |
| burn-models | ✓ | ✗ | ✗ | ✓ |
| burn-bench | ✓ | ✓ | ✓ | ✓ |

**Key**:
- **Debug**: Can diagnose and fix errors in their domain
- **Review**: Can review code for idiomatic patterns
- **Full-Stack**: Can develop + debug + review (no separate reviewer needed)
- **Background**: Suitable for background execution

---

## Implementation Guide

### Step 1: Plugin Structure

```
burn-dev-team/
├── plugin.json
├── agents/
│   ├── burn-architect.md
│   ├── burn-trainer.md
│   ├── burn-deployer.md
│   ├── burn-importer.md
│   ├── burn-lm.md
│   ├── burn-central.md
│   ├── burn-models.md
│   └── burn-bench.md
├── skills/
│   ├── burn-router/
│   │   └── SKILL.md
│   ├── burn-cubecl/
│   │   └── SKILL.md
│   └── burn-contrib/
│       └── SKILL.md
├── hooks/
│   └── hooks.json
└── .mcp.json
```

### Step 2: plugin.json

```json
{
  "name": "burn-dev-team",
  "version": "1.0.0",
  "description": "Burn ML framework development team",
  "author": "Your Name",
  "repository": "https://github.com/user/burn-dev-team-plugin",

  "agents": "agents/",
  "skills": "skills/",
  "hooks": "hooks/hooks.json",
  "mcpServers": ".mcp.json"
}
```

### Step 3: Agent Definitions

**agents/burn-architect.md**:
```markdown
---
name: burn-architect
description: Burn architecture specialist - tensors, modules, config, autodiff, records. Full-stack developer who can design, debug, and review within the architecture domain.
tools: ["*"]
skills: ["burn-router"]
model: sonnet
color: blue
memory: project
permissionMode: acceptEdits
effort: high
---

# Burn Architecture Specialist

You are an expert Burn framework architect on a development team.

## Your Expertise

- Tensor operations and shape management
- Module system and neural network architectures
- Automatic differentiation
- Config pattern for reproducibility
- Record system for model persistence

## Team Workflow

As a teammate in the Burn development team:

1. **Check TaskList** after completing each task
2. **Claim unassigned, unblocked tasks** related to architecture
3. **Prioritize tasks by ID** (lowest first)
4. **Communicate via SendMessage** - your text output is NOT visible to the team
5. **Mark tasks completed** with TaskUpdate when done
6. **Debug and review** your own work - you're a full-stack specialist

## Architecture Patterns

### Tensor Shape Management

```rust
use burn::tensor::Tensor;

// Always document expected shapes
fn linear_forward<B: Backend>(
    input: Tensor<B, 2>,  // [batch_size, input_dim]
    weight: Tensor<B, 2>, // [output_dim, input_dim]
) -> Tensor<B, 2> {      // [batch_size, output_dim]
    input.matmul(weight.transpose())
}
```

[... continue with detailed patterns, examples, debugging tips ...]
```

### Step 4: Routing Skill

**skills/burn-router/SKILL.md**:
```markdown
---
trigger: burn-router
description: Route Burn framework queries to specialized development team
tools: ["Agent", "TeamCreate", "SendMessage", "TaskCreate", "TaskUpdate", "TaskList"]
model: haiku
effort: low
context: fork
---

# Burn Development Team Router

Route incoming Burn framework requests to the appropriate specialist teammates.

## Specialist Mapping

- **Tensors, modules, autodiff, records** → burn-architect
- **Training, learner, metrics, datasets** → burn-trainer
- **Backends, WASM, deployment, optimization** → burn-deployer
- **ONNX import, model conversion** → burn-importer
- **Language models, InferenceServer** → burn-lm
- **Experiment tracking** → burn-central
- **Pre-trained models** → burn-models
- **Benchmarking** → burn-bench

## Workflow

1. Analyze the user's request
2. Determine complexity (single specialist vs. team needed)
3. For teams:
   - Create team with `TeamCreate`
   - Break work into tasks with `TaskCreate`
   - Spawn specialists with `Agent` tool
   - Monitor progress
   - Coordinate via `SendMessage`
   - Shut down gracefully when complete

4. For single specialists:
   - Spawn one agent with appropriate prompt
   - Let them work independently

## Examples

### Complex Multi-Agent Task

User: "Implement a Llama model with training loop and ONNX export"

```
1. TeamCreate({ team_name: "llama-impl", description: "Llama model implementation" })

2. TaskCreate([
   { subject: "Design Llama architecture", owner: null },
   { subject: "Implement training loop", blockedBy: ["1"] },
   { subject: "Add ONNX export", blockedBy: ["2"] }
])

3. Agent({ name: "architect", team_name: "llama-impl", subagent_type: "burn:burn-architect", ... })
   Agent({ name: "trainer", team_name: "llama-impl", subagent_type: "burn:burn-trainer", ... })
   Agent({ name: "importer", team_name: "llama-impl", subagent_type: "burn:burn-importer", ... })

4. Monitor and coordinate

5. SendMessage({ to: "*", message: { type: "shutdown_request" } }) when done

6. TeamDelete()
```

[... detailed routing logic ...]
```

### Step 5: Hooks Configuration

**hooks/hooks.json**:
```json
{
  "TeammateIdle": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": "echo '[Burn Team] ${AGENT_NAME} is idle (${IDLE_REASON})' >> ~/.claude/burn-team.log"
        }
      ]
    }
  ],
  "TaskCompleted": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": "echo '[Burn Team] Task ${TASK_ID} completed by ${OWNER}' >> ~/.claude/burn-team.log"
        }
      ]
    }
  ],
  "SessionStart": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": "echo '=== Burn Development Team Session Started ===' >> ~/.claude/burn-team.log"
        }
      ]
    }
  ]
}
```

### Step 6: MCP Servers (Optional)

**.mcp.json**:
```json
{
  "mcpServers": {
    "burn-docs": {
      "type": "stdio",
      "command": "uvx",
      "args": ["burn-docs-mcp"],
      "env": {
        "BURN_DOCS_PATH": "/path/to/burn/docs"
      }
    }
  }
}
```

### Step 7: Installation

```bash
# Option 1: User-level plugin
mkdir -p ~/.claude/plugins/
cd ~/.claude/plugins/
git clone https://github.com/user/burn-dev-team-plugin burn-dev-team

# Option 2: Project-level plugin
mkdir -p .claude/plugins/
cd .claude/plugins/
git clone https://github.com/user/burn-dev-team-plugin burn-dev-team

# Enable plugin in settings.json
# Add to enabledPlugins:
{
  "enabledPlugins": {
    "burn-dev-team": {
      "enabled": true
    }
  }
}
```

### Step 8: Usage

```bash
# Set the required environment variable
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Start Claude Code
claude

# Use the router skill
/burn-router Implement a CNN for image classification with training loop

# Or manually create team and spawn agents
TeamCreate({ team_name: "cnn-impl", description: "CNN implementation" })

TaskCreate({ subject: "Design CNN architecture", status: "pending" })
TaskCreate({ subject: "Implement training loop", status: "pending", blockedBy: ["1"] })

Agent({
  name: "architect",
  team_name: "cnn-impl",
  subagent_type: "burn:burn-architect",
  prompt: "Check TaskList for architecture tasks",
  description: "CNN architecture"
})

Agent({
  name: "trainer",
  team_name: "cnn-impl",
  subagent_type: "burn:burn-trainer",
  prompt: "Check TaskList for training tasks",
  description: "Training loop"
})

# Monitor progress via TaskList
TaskList()

# Coordinate via messages
SendMessage({ to: "architect", message: "Use 3x3 kernels for convolutions" })

# Shut down when complete
SendMessage({ to: "*", message: { type: "shutdown_request", reason: "Work complete" } })
TeamDelete()
```

---

## File Structure Example

### Complete Plugin Layout

```
~/.claude/plugins/burn-dev-team/
├── plugin.json
│
├── agents/
│   ├── burn-architect.md      # Core team member
│   ├── burn-trainer.md         # Core team member
│   ├── burn-deployer.md        # Core team member
│   ├── burn-importer.md        # Core team member
│   ├── burn-lm.md              # Ecosystem specialist
│   ├── burn-central.md         # Ecosystem specialist
│   ├── burn-models.md          # Ecosystem specialist
│   └── burn-bench.md           # Ecosystem specialist
│
├── skills/
│   ├── burn-router/
│   │   └── SKILL.md            # Main routing skill
│   ├── burn-cubecl/
│   │   └── SKILL.md            # CubeCL kernel skill
│   └── burn-contrib/
│       └── SKILL.md            # Contribution guide skill
│
├── hooks/
│   └── hooks.json              # Lifecycle hooks
│
├── .mcp.json                   # MCP server config (optional)
│
└── README.md                   # Plugin documentation
```

### Agent File Template

```markdown
---
name: {agent-name}
description: {one-line description of expertise and full-stack capability}
tools: ["*"]
skills: ["burn-router"]
model: sonnet
color: {blue|green|yellow|purple|etc}
memory: project
permissionMode: acceptEdits
effort: high
---

# {Agent Title}

You are a {role} on the Burn development team.

## Your Expertise

- {Domain area 1}
- {Domain area 2}
- {Domain area 3}

## Team Workflow

As a teammate in the Burn development team:

1. **Check TaskList** after completing each task
2. **Claim unassigned, unblocked tasks** in your domain (prefer lowest ID first)
3. **Communicate via SendMessage** - your text output is NOT visible to the team
4. **Mark tasks completed** with TaskUpdate when done
5. **Debug and review** your own work - you're a full-stack specialist
6. **Ask for help** via SendMessage when blocked

## Implementation Patterns

[... domain-specific patterns, code examples, debugging guides ...]

## Common Issues

[... troubleshooting guide for domain ...]

## Review Checklist

When reviewing your own work:
- [ ] {Domain-specific check 1}
- [ ] {Domain-specific check 2}
- [ ] {Domain-specific check 3}
```

---

## Summary

### Key Integration Points

1. **Plugin agents** are loaded automatically from `agents/` directory
2. **Agent names** become `{plugin}:{agent}` (e.g., `burn:burn-architect`)
3. **Agent tool** spawns plugin agents as teammates when `name` + `team_name` provided
4. **Skills** provide high-level orchestration and routing
5. **Hooks** monitor teammate lifecycle for logging/notifications
6. **Task system** automatically shared between team members
7. **Message passing** enables coordination

### Critical Flow

```
User invokes /burn-router
  ↓
Skill analyzes request
  ↓
Creates team + tasks
  ↓
Spawns plugin agents as teammates
  ↓
Teammates auto-claim tasks
  ↓
Execute work in parallel
  ↓
Coordinate via SendMessage
  ↓
Mark tasks complete
  ↓
Graceful shutdown
```

### Benefits of This Architecture

1. **Modular**: Each agent is a self-contained specialist
2. **Composable**: Mix and match agents for different tasks
3. **Scalable**: Add new specialists without modifying existing ones
4. **Observable**: Hooks provide visibility into team activity
5. **Maintainable**: Each agent has clear domain boundaries
6. **Full-Stack**: No separate debugger/reviewer - agents handle their own quality

This design enables a true multi-agent Burn development team that coordinates through tasks and messages, exactly like the human development team it's modeled after.
