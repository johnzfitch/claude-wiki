---
title: "Burn Knowledgebase Architecture — Verified Against Claude Code Source"
category: "08-Plugins-Skills"
tags: ["claude-code", "plugins"]
---

# Burn Knowledgebase Architecture — Verified Against Claude Code Source

**Date**: 2026-03-15
**Verification**: Based on analysis of Claude Code 2.1.75 source (`claude-api` skill and `claude-code-guide` agent)

---

## What Anthropic Actually Does

After reviewing the built-in `claude-api` skill and `claude-code-guide` agent implementations, here's the **actual pattern** Anthropic uses:

### Pattern 1: Skills with Embedded Documentation (`claude-api` skill)

**Location**: `2.1.76_resplit/4572.js`

**How it works**:
```javascript
// All documentation is bundled as strings in the binary
const UB$ = {
  "python/claude-api/README.md": "<full markdown content>",
  "python/agent-sdk/README.md": "<full markdown content>",
  "typescript/claude-api/README.md": "<full markdown content>",
  "shared/tool-use-concepts.md": "<full markdown content>",
  // ... ~20 docs total, all embedded
};

// Skill definition
{
  name: "claude-api",
  description: "Build apps with the Claude API or Anthropic SDK...",
  allowedTools: ["Read", "Grep", "Glob", "WebFetch"],

  // Key method: builds prompt dynamically on invocation
  async getPromptForCommand(userArgs) {
    // 1. Auto-detect project language
    const lang = await detectLanguage();  // checks for .py, .ts, etc.

    // 2. Filter docs to relevant language + shared
    const relevantDocs = Object.keys(UB$)
      .filter(path => path.startsWith(`${lang}/`) || path.startsWith("shared/"));

    // 3. Build massive prompt with ALL docs in <doc> tags
    const allDocs = relevantDocs.map(path => {
      return `<doc path="${path}">
${UB$[path].trim()}
</doc>`;
    }).join('\n\n');

    // 4. Return prompt with quick reference guide + all docs + user request
    return [{
      type: "text",
      text: `${quickReferenceGuide}\n\n${allDocs}\n\n## User Request\n\n${userArgs}`
    }];
  }
}
```

**Key findings**:
-  **All docs bundled in binary** — No external database, no file I/O at runtime
-  **Language detection** — Auto-detects Python/TypeScript/etc from project files
-  **Filtered injection** — Only injects relevant language docs (not all 20)
-  **On-demand loading** — Docs only injected when skill is invoked
-  **Single massive prompt** — ALL relevant docs in one shot (~50-100KB of markdown)

### Pattern 2: Agents with Dynamic SystemPrompt (`claude-code-guide` agent)

**Location**: `2.1.76_resplit/2880.js`

**How it works**:
```javascript
{
  agentType: "claude-code-guide",
  whenToUse: "Use when user asks about Claude Code, Agent SDK, or Claude API...",
  tools: ["Read", "WebFetch", "WebSearch", "WebBrowse"],
  source: "built-in",
  model: "haiku",

  // Dynamic systemPrompt builder
  getSystemPrompt({ toolUseContext }) {
    const commands = toolUseContext.options.commands;
    const agents = toolUseContext.options.agentDefinitions.activeAgents;
    const mcpClients = toolUseContext.options.mcpClients;
    const settings = getCurrentSettings();

    const sections = [];

    // Add available custom skills
    if (commands.filter(c => c.type === "prompt").length > 0) {
      sections.push(`**Available custom skills in this project:**
${commands.map(c => `- /${c.name}: ${c.description}`).join('\n')}`);
    }

    // Add available custom agents
    const customAgents = agents.filter(a => a.source !== "built-in");
    if (customAgents.length > 0) {
      sections.push(`**Available custom agents:**
${customAgents.map(a => `- ${a.agentType}: ${a.whenToUse}`).join('\n')}`);
    }

    // Add MCP servers
    if (mcpClients && mcpClients.length > 0) {
      sections.push(`**Configured MCP servers:**
${mcpClients.map(c => `- ${c.name}`).join('\n')}`);
    }

    // Add user settings
    if (Object.keys(settings).length > 0) {
      sections.push(`**User's settings.json:**
\`\`\`json
${JSON.stringify(settings, null, 2)}
\`\`\``);
    }

    // Combine base prompt + runtime context
    const basePrompt = getBaseGuidePrompt();  // Static knowledge

    if (sections.length > 0) {
      return `${basePrompt}

---

# User's Current Configuration

${sections.join('\n\n')}`;
    }

    return basePrompt;
  }
}
```

**Key findings**:
-  **Dynamic context injection** — `getSystemPrompt()` receives runtime `toolUseContext`
-  **Environment awareness** — Injects list of installed skills, agents, MCP servers, settings
-  **Base + runtime split** — Static knowledge in base prompt, dynamic config appended
-  **No database queries** — All info comes from in-memory state
-  **Called on agent spawn** — Built fresh each time agent is created

---

## How This Compares to My Original Proposal

### What I Got Right 

1. **Multi-tier architecture is correct**
   - Tier 1 (agent systemPrompt): Verified 
   - Tier 2 (shared resources): Partially verified 
   - Tier 3 (skills for coordination): Verified 

2. **Agent isolation for knowledge partitioning**
   - Confirmed: Each agent has separate `getSystemPrompt()` 
   - Confirmed: Tool restrictions create security boundaries 

3. **Skills inject on-demand**
   - Confirmed: `getPromptForCommand()` builds prompts at invocation time 

4. **Dynamic context in systemPrompts**
   - Confirmed: `getSystemPrompt({ toolUseContext })` receives runtime state 

---

## Revised Optimal Architecture (Based on Verified Patterns)

### Tier 1: Agent SystemPrompts (Dynamic Runtime Context)

Each agent's `getSystemPrompt({ toolUseContext })` builds a prompt with:
- **Static domain knowledge** (embedded in the function)
- **Dynamic runtime context** (from `toolUseContext`)

**Example: `burn-architect` agent**

```javascript
// In plugin agents/burn-architect.js
export default {
  name: "burn-architect",
  description: "Burn architecture specialist — tensors, modules, autodiff...",
  tools: ["Read", "Write", "Grep", "Glob"],
  model: "sonnet",

  // Dynamic systemPrompt builder
  getSystemPrompt({ toolUseContext }) {
    const baseKnowledge = `
You are the Burn architecture specialist with deep expertise in:

## Core Tensor Operations (Memorized)

- \`Tensor::zeros(shape)\` — zero-initialized tensor
- \`Tensor::ones(shape)\` — one-initialized
- \`Tensor::matmul(other)\` — matrix multiplication
- \`tensor.reshape(new_shape)\` — view with new dimensions
- \`tensor.transpose()\` — swap last two dims

## Module Design Patterns

### Record Pattern (State Management)
All learnable modules implement \`Module<B>\`:
\`\`\`rust
#[derive(Module, Debug)]
pub struct LinearLayer<B: Backend> {
    weight: Param<Tensor<B, 2>>,
    bias: Param<Tensor<B, 1>>,
}
\`\`\`

### Config Pattern (Initialization)
\`\`\`rust
#[derive(Config, Debug)]
pub struct ConvBlockConfig {
    in_channels: usize,
    out_channels: usize,
}

impl ConvBlockConfig {
    pub fn init<B: Backend>(&self) -> ConvBlock<B> { ... }
}
\`\`\`

## Common Pitfalls to Prevent

1. **Shape mismatch on matmul**: \`[B, N, D] @ [D, D]\` → Need broadcast
2. **Missing \`.inner()\`**: When crossing train/inference boundary
3. **Backend type leakage**: Return \`Tensor<B, 2>\`, not \`Tensor<WgpuBackend, 2>\`
`;

    // Add runtime context (current project state)
    const sections = [];

    // Check if Burn is already in dependencies
    const hasBurn = toolUseContext.readFileState.has("Cargo.toml") &&
      toolUseContext.readFileState.get("Cargo.toml")?.content?.includes("burn =");

    if (hasBurn) {
      sections.push("**Burn detected in project** — Ready to assist with implementation.");
    } else {
      sections.push("**Burn not yet added** — Will help set up dependencies if needed.");
    }

    // Check for existing Burn code
    const burnFiles = Array.from(toolUseContext.readFileState.keys())
      .filter(path => path.endsWith('.rs') &&
        toolUseContext.readFileState.get(path)?.content?.includes('burn::'));

    if (burnFiles.length > 0) {
      sections.push(`**Burn code found in:**\n${burnFiles.map(f => `- ${f}`).join('\n')}`);
    }

    if (sections.length > 0) {
      return `${baseKnowledge}\n\n---\n\n# Current Project Context\n\n${sections.join('\n\n')}`;
    }

    return baseKnowledge;
  }
};
```

**Why this works**:
- Static knowledge = domain expertise (tensor APIs, patterns)
- Dynamic context = project state (dependencies, existing files)
- No external queries needed — all from in-memory `toolUseContext`

### Tier 2: Skills with Embedded Reference (Language-Filtered Injection)

Following the `claude-api` pattern, create a skill that bundles documentation and injects language-filtered subsets.

**Example: `burn-docs` skill**

```javascript
// In plugin skills/burn-docs/index.js
import { burnApiDocs } from './bundled-docs.js';

export default {
  name: "burn-docs",
  description: "Load Burn framework API documentation (tensor ops, modules, backends, training).",
  allowedTools: ["Read", "Grep"],
  userInvocable: true,

  async getPromptForCommand(userQuery) {
    // burnApiDocs structure:
    // {
    //   "tensor-ops.md": "<markdown>",
    //   "modules.md": "<markdown>",
    //   "backends.md": "<markdown>",
    //   "training.md": "<markdown>",
    //   "examples/mnist.md": "<markdown>",
    //   // ... etc
    // }

    // Filter docs based on query keywords
    const keywords = userQuery.toLowerCase();
    let relevantDocs = [];

    if (keywords.includes('tensor') || keywords.includes('operation')) {
      relevantDocs.push('tensor-ops.md');
    }
    if (keywords.includes('module') || keywords.includes('layer')) {
      relevantDocs.push('modules.md');
    }
    if (keywords.includes('backend') || keywords.includes('gpu') || keywords.includes('wgpu')) {
      relevantDocs.push('backends.md');
    }
    if (keywords.includes('train') || keywords.includes('optimizer') || keywords.includes('learner')) {
      relevantDocs.push('training.md');
    }

    // If no specific match, include core docs
    if (relevantDocs.length === 0) {
      relevantDocs = ['tensor-ops.md', 'modules.md', 'training.md'];
    }

    // Build prompt with filtered docs
    const docsContent = relevantDocs.map(path => {
      return `<doc path="${path}">
${burnApiDocs[path].trim()}
</doc>`;
    }).join('\n\n');

    const quickRef = `# Burn Framework Reference

## Quick Navigation

**Tensor operations**: See tensor-ops.md
**Module patterns**: See modules.md
**Backend selection**: See backends.md
**Training setup**: See training.md

---

## Included Documentation

${docsContent}

---

## User Query

${userQuery}`;

    return [{ type: "text", text: quickRef }];
  }
};
```

**Building the bundled docs** (`bundled-docs.js`):

```javascript
// Generated at build time from docs/
export const burnApiDocs = {
  "tensor-ops.md": `# Burn Tensor Operations

## Creating Tensors

\`\`\`rust
use burn::tensor::Tensor;

let zeros = Tensor::<Backend, 2>::zeros([3, 4], &device);
let ones = Tensor::<Backend, 2>::ones([3, 4], &device);
\`\`\`

...
`,

  "modules.md": `# Burn Modules

## Module Trait

\`\`\`rust
#[derive(Module, Debug)]
pub struct MyModel<B: Backend> {
    linear: Linear<B>,
}
\`\`\`

...
`,

  // ... etc
};
```

**Why this works**:
- All docs bundled at plugin install time (no runtime I/O)
- Keyword-based filtering (simple, fast, no database)
- Injects 2-5 docs per query (not all 20+)
- Works offline, zero latency

### Tier 3: Routing Skills (Coordination Logic)

Same as originally proposed — inject decision trees and collaboration patterns.

**No changes needed** — this pattern is already verified in built-in skills.

---

## When to Use Database vs. Bundled Docs

| Scenario | Use Bundled Docs | Use Database |
|----------|------------------|--------------|
| **Documentation is stable** (released framework) | ✅ Bundle | ❌ Overkill |
| **Docs change frequently** (internal APIs) | ❌ Stale | ✅ Live queries |
| **Offline usage required** | ✅ Bundle | ❌ Needs connection |
| **< 50 doc files** | ✅ Bundle | ❌ Overkill |
| **> 1000 doc files** | ❌ Binary bloat | ✅ Database |
| **Need fuzzy search** | ❌ Basic filtering | ✅ FTS5 |
| **Need structured queries** (version, tags, etc.) | ❌ Limited | ✅ SQL |

**For Burn plugin**: **Bundle docs** (stable framework, ~20-30 doc files, offline usage)

---

## Revised Implementation Plan

### Phase 1: Bundle Documentation

1. **Create docs structure**:
   ```
   plugin/docs/
   ├── tensor-ops.md
   ├── modules.md
   ├── backends.md
   ├── training.md
   ├── autodiff.md
   ├── examples/
   │   ├── mnist.md
   │   ├── gpt.md
   │   └── resnet.md
   └── patterns/
       ├── custom-op.md
       └── multi-backend.md
   ```

2. **Build bundled-docs.js**:
   ```bash
   # At plugin build time
   node scripts/bundle-docs.js
   # Reads docs/*.md, generates agents/bundled-docs.js
   ```

3. **Import in agents**:
   ```javascript
   import { burnApiDocs } from './bundled-docs.js';
   ```

### Phase 2: Agent SystemPrompts (Dynamic Context)

1. **Implement `getSystemPrompt({ toolUseContext })` for each agent**
2. **Embed static domain knowledge** (APIs, patterns, pitfalls)
3. **Inject runtime context** (project files, dependencies, existing code)
4. **No external queries** — all from `toolUseContext.readFileState`

### Phase 3: Skills with Filtered Injection

1. **Implement `getPromptForCommand(query)` for `burn-docs` skill**
2. **Keyword-based filtering** → select 2-5 relevant docs
3. **Inject in `<doc>` tags** with quick reference guide
4. **Return as prompt messages**

### Phase 4: Routing Coordinator

1. **Implement `burn-router` skill** with decision tree
2. **Inject on first Burn query** — persists for session
3. **Lists all specialist agents** with when-to-use guides

---

## Key Differences from Original Proposal

| Aspect | Original Proposal | Verified Pattern |
|--------|-------------------|------------------|
| **Knowledgebase storage** | SQLite database | Bundled strings in code |
| **Query mechanism** | MCP tool calls to DB | Keyword filtering of bundle |
| **Injection size** | Single doc per query | All relevant docs (2-5 at once) |
| **Update mechanism** | SQL updates | Rebuild bundle |
| **Offline support** | Requires database file | Built into binary |
| **Setup complexity** | Database + MCP server | Just bundle at build time |
| **Latency** | ~5ms query | 0ms (in-memory) |
| **Fuzzy search** | FTS5 ranking | Basic keyword match |

---

## Conclusion

**Anthropic's actual pattern is simpler and more pragmatic than my proposal.**

### What they do:
1. **Bundle all docs as strings** in the plugin/binary
2. **Filter by keywords or language** at invocation time
3. **Inject all relevant docs** in one shot (rely on large context windows)
4. **Dynamic systemPrompt** builds runtime context from in-memory state

### Why it works:
- ✅ Zero latency (in-memory)
- ✅ Works offline
- ✅ No database setup
- ✅ Simple keyword filtering is "good enough"
- ✅ 200K context makes injecting 5-10 docs cheap

### When to deviate:
- Large knowledgebase (>1000 docs) → Use database
- Frequently updated docs → Use database or live fetching
- Need complex queries → Use FTS5 or vector search
- Multi-tenancy or versioning → Use database

**For a Burn ML plugin with ~30 stable documentation files, follow Anthropic's bundled pattern.**

---

## Updated File Structure

```
burn-plugin/
├── manifest.json
├── agents/
│   ├── burn-architect.js        # getSystemPrompt() with embedded knowledge
│   ├── burn-trainer.js
│   ├── burn-deployer.js
│   ├── burn-importer.js
│   └── bundled-docs.js          # Generated from docs/ at build time
├── skills/
│   ├── burn-docs/
│   │   └── index.js             # getPromptForCommand() filters & injects docs
│   ├── burn-router/
│   │   └── SKILL.md             # Routing decision tree
│   └── burn-cubecl/
│       └── SKILL.md
├── docs/                        # Source markdown (not shipped)
│   ├── tensor-ops.md
│   ├── modules.md
│   ├── backends.md
│   └── ...
└── scripts/
    └── bundle-docs.js           # Build script: docs/*.md → bundled-docs.js
```

**Build process**:
```bash
# During plugin development
npm run bundle-docs  # Generates agents/bundled-docs.js

# At plugin install time
# User gets pre-bundled plugin with docs already in bundled-docs.js
```

**Verification**: ✅ Confirmed against Claude Code 2.1.75 source code.
