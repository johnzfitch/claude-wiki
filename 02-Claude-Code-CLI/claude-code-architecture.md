# Claude Code Architecture for Zack's Setup

> Arch Linux (omarchy) · Ryzen 9800X3D · RTX 4090 · 10Gbps fiber
> Projects: SpecHO, definitelynot.ai, llmx, iOS RE toolkits, Iconics

## Design Principles

1. **Tool Search handles main context** - Don't fight it, leverage it
2. **MCP isolation for subagents** - Purpose-built agents get specific tools
3. **llmx as primary code search** - Replace/augment built-in Explore
4. **No plugin wrappers** - That strategy is obsolete
5. **Explicit over implicit** - Clear tool boundaries, no inheritance surprises

---

## Directory Structure

```
~/.claude/
├── settings.json              # Global settings, disabled built-ins
├── settings.local.json        # Machine-specific overrides (not synced)
├── mcp.json                   # User-scope MCP servers (always available)
├── agents/
│   ├── llmx-explorer.md       # Replaces Explore, uses llmx
│   ├── web-automation.md      # Playwright isolation
│   ├── github-ops.md          # GitHub MCP isolation  
│   ├── re-analyst.md          # Reverse engineering workflow
│   ├── specwriter.md          # Documentation/spec generation
│   └── clean-task.md          # MCP-free general purpose
├── commands/
│   ├── search.md              # /search - llmx semantic search
│   ├── re.md                  # /re - reverse engineering workflow
│   ├── detect.md              # /detect - AI detection pipeline
│   └── index.md               # /index - reindex with llmx
├── skills/
│   ├── specho-analysis/
│   │   └── SKILL.md           # SpecHO fingerprinting workflow
│   ├── re-patterns/
│   │   └── SKILL.md           # iOS/binary RE patterns
│   └── api-conventions/
│       └── SKILL.md           # Your API style guide
├── hooks/
│   └── mcp-guard.py           # PreToolUse hook for MCP auditing
└── plugins/
    └── (empty - not using plugin wrappers)

# Project-level (per repo)
.claude/
├── settings.json              # Project permissions
├── agents/                    # Project-specific agents
├── skills/                    # Project-specific skills
└── CLAUDE.md                  # Project context
```

---

## MCP Server Tiers

### Tier 1: Always-On (User Scope)
Low token cost, high utility, used across all projects.

```json
// ~/.claude/mcp.json
{
  "mcpServers": {
    "llmx": {
      "command": "/home/zack/dev/llmx/target/release/llmx-mcp",
      "env": {
        "LLMX_STORAGE_DIR": "/home/zack/.llmx/indexes",
        "LLMX_MODEL_PATH": "/home/zack/.llmx/models/bge-small-en-v1.5.onnx"
      }
    }
  }
}
```

**Why llmx only?** It's your local semantic search - lightweight, always useful, no external API calls. Everything else is situational.

### Tier 2: Project-Scope (Shared with team)
Tools specific to a project, checked into repo.

```json
// ~/dev/specho/.mcp.json
{
  "mcpServers": {
    "huggingface": {
      "command": "npx",
      "args": ["-y", "@huggingface/mcp-server"],
      "env": {
        "HF_TOKEN": "${HF_TOKEN}"
      }
    }
  }
}

// ~/dev/definitelynot.ai/.mcp.json  
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-playwright"]
    }
  }
}
```

### Tier 3: On-Demand via Subagent
Heavy/specialized tools that should NEVER pollute main context.

These aren't configured globally - they're started by subagents or enabled per-session:

- `playwright` - Only via `web-automation` subagent
- `github` - Only via `github-ops` subagent  
- Database servers - Only via project-specific agents
- Heavy API servers (Jira, Linear, etc.)

---

## Settings Configuration

### Global Settings
```json
// ~/.claude/settings.json
{
  "permissions": {
    "deny": [
      "Task(Explore)",
      "mcp__playwright__*",
      "mcp__github__*"
    ],
    "allow": [
      "mcp__llmx__*",
      "Read",
      "Grep", 
      "Glob"
    ]
  },
  "env": {
    "ENABLE_TOOL_SEARCH": "auto:5",
    "MAX_MCP_OUTPUT_TOKENS": "50000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "85"
  },
  "model": "claude-sonnet-4-5-20250929",
  "cleanupPeriodDays": 14
}
```

**Key decisions:**
- `Task(Explore)` denied - replaced by `llmx-explorer`
- `mcp__playwright__*` denied in main context - only via subagent
- `mcp__github__*` denied in main context - only via subagent
- `ENABLE_TOOL_SEARCH=auto:5` - More aggressive lazy loading (5% threshold)
- `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85` - Compact earlier to preserve context

### Project Settings Example
```json
// ~/dev/specho/.claude/settings.json
{
  "permissions": {
    "allow": [
      "mcp__huggingface__*",
      "Bash(python *)",
      "Bash(cargo *)"
    ]
  }
}
```

---

## Subagent Definitions

### 1. llmx-explorer.md (Replaces Explore)
```yaml
---
name: llmx-explorer
description: |
  Fast semantic code search and codebase exploration. Use for:
  - Finding relevant code by meaning, not just text
  - Understanding codebase structure and patterns
  - Locating implementations, definitions, usages
  - Architectural analysis
  Replaces built-in Explore with semantic search via llmx.
model: haiku
tools: Read, Grep, Glob, mcp__llmx__search, mcp__llmx__index_status
disallowedTools: Write, Edit, Bash, mcp__playwright__*, mcp__github__*
permissionMode: plan
---

You are a semantic code explorer powered by llmx.

## Primary Tool: mcp__llmx__search
Use semantic search FIRST for any code discovery task. Query with natural language descriptions of what you're looking for.

## Fallback Tools
- `Grep` - For exact string/regex matches after semantic search narrows scope
- `Glob` - For file pattern discovery
- `Read` - To examine files found via search

## Response Format
Return findings as:
1. **Relevant Files** - Ranked by semantic relevance
2. **Key Patterns** - Architectural observations
3. **Entry Points** - Where to start for the task

Never modify files. Summarize concisely for the main agent.
```

### 2. web-automation.md (Playwright Isolation)
```yaml
---
name: web-automation
description: |
  Browser automation and web scraping tasks. Use for:
  - Automated testing with Playwright
  - Web scraping and data extraction
  - Screenshot capture and visual testing
  - Form filling and interaction recording
  MUST run in foreground (MCP required).
model: inherit
tools: Read, Write, Bash, mcp__playwright__*
disallowedTools: mcp__github__*, mcp__llmx__*
permissionMode: acceptEdits
---

You are a browser automation specialist using Playwright MCP.

## Available Playwright Tools
- Navigate, click, fill, screenshot
- Wait for selectors, extract text
- Handle multiple pages/contexts

## Constraints
- Always close browser contexts when done
- Return screenshots as base64 when visual verification needed
- Summarize extracted data, don't dump raw HTML

## Response Format
Return:
1. **Actions Taken** - What you did
2. **Results** - Data extracted or verification status
3. **Screenshots** - If visual confirmation needed
```

### 3. github-ops.md (GitHub Isolation)
```yaml
---
name: github-ops
description: |
  GitHub operations and repository management. Use for:
  - Creating/reviewing pull requests
  - Issue management and triage
  - Repository search and analysis
  - Release management
  MUST run in foreground (MCP required).
model: inherit
tools: Read, Bash, mcp__github__*
disallowedTools: mcp__playwright__*, Write, Edit
permissionMode: default
---

You are a GitHub operations specialist.

## Available GitHub Tools
- Search repositories, issues, PRs
- Create/update issues and PRs
- Manage labels, milestones, releases
- Review and comment on code

## Constraints
- Confirm destructive operations before executing
- Summarize PR/issue content, don't dump full text
- Use rate limiting awareness

## Response Format
Return:
1. **Operation** - What was done
2. **Result** - Links to created/modified resources
3. **Summary** - Key information extracted
```

### 4. re-analyst.md (Reverse Engineering)
```yaml
---
name: re-analyst
description: |
  Binary analysis and reverse engineering tasks. Use for:
  - iOS/macOS binary analysis
  - Disassembly and decompilation review
  - Protocol reverse engineering
  - Security vulnerability analysis
  Specialized for RE workflows.
model: inherit
tools: Read, Bash, Grep, Glob
disallowedTools: mcp__*, Write, Edit
permissionMode: plan
skills:
  - re-patterns
---

You are a reverse engineering analyst.

## Methodology
1. Static analysis first (strings, headers, imports)
2. Identify interesting functions via symbols/patterns
3. Trace data flow and control flow
4. Document findings systematically

## Tools Available
- `Bash` for running analysis tools (otool, nm, strings, class-dump, frida)
- `Read` for examining output files
- `Grep/Glob` for pattern matching

## Response Format
Return:
1. **Target Info** - Binary metadata, architecture
2. **Interesting Findings** - Functions, strings, patterns
3. **Recommendations** - Next analysis steps
```

### 5. clean-task.md (MCP-Free General Purpose)
```yaml
---
name: clean-task
description: |
  General purpose task execution WITHOUT external tool access. Use for:
  - Code modifications that don't need external APIs
  - File operations and refactoring
  - Local testing and validation
  - Any task where MCP would be overhead
  Lightweight alternative to general-purpose.
model: inherit
tools: Read, Write, Edit, Bash, Grep, Glob
disallowedTools: mcp__*
permissionMode: acceptEdits
---

You are a focused task executor. No external API access.

Work efficiently with local tools only. If you need external data,
tell the main agent to use a specialized subagent instead.
```

### 6. specwriter.md (Documentation)
```yaml
---
name: specwriter
description: |
  Technical documentation and specification writing. Use for:
  - API documentation generation
  - Architecture decision records
  - README and guide creation
  - Code comment generation
  Read-heavy, write-focused.
model: inherit  
tools: Read, Write, Grep, Glob, mcp__llmx__search
disallowedTools: Bash, Edit, mcp__playwright__*, mcp__github__*
permissionMode: acceptEdits
---

You are a technical writer. Read code, write documentation.

## Process
1. Use llmx to find relevant code
2. Read and understand the implementation
3. Write clear, accurate documentation
4. Use consistent formatting (your conventions)

## Output Formats
- Markdown for docs
- JSDoc/docstrings for inline
- OpenAPI for APIs
```

---

## Slash Commands

### /search - Semantic Code Search
```yaml
# ~/.claude/commands/search.md
---
description: Semantic code search using llmx
argument-hint: "<natural language query>"
---

Use the llmx-explorer subagent to search for: $ARGUMENTS

Return the top 10 most relevant results with file paths and brief context.
```

### /index - Reindex Codebase
```yaml
# ~/.claude/commands/index.md
---
description: Reindex current project with llmx
---

Run the llmx indexer on the current project:

```bash
llmx index --path . --storage ~/.llmx/indexes/$(basename $(pwd))
```

Report indexing status when complete.
```

### /re - Reverse Engineering Session
```yaml
# ~/.claude/commands/re.md
---
description: Start reverse engineering analysis
argument-hint: "<binary path or description>"
---

Use the re-analyst subagent to analyze: $ARGUMENTS

Begin with static analysis, then report findings and recommended next steps.
```

### /detect - AI Detection Pipeline
```yaml
# ~/.claude/commands/detect.md
---
description: Run SpecHO AI text detection
argument-hint: "<text or file path>"
---

Analyze the provided content using SpecHO fingerprinting:

1. Extract linguistic features (148-dimensional)
2. Compare against known model signatures
3. Report confidence scores and model attribution

Input: $ARGUMENTS
```

---

## Skills

### specho-analysis/SKILL.md
```yaml
---
name: specho-analysis
description: |
  SpecHO AI text detection and model fingerprinting workflow.
  148-dimensional linguistic analysis for identifying AI-generated text
  and attributing specific models.
disable-model-invocation: false
---

# SpecHO Analysis Workflow

## Feature Extraction Pipeline
1. **Tokenization** - Split into sentences and tokens
2. **Lexical Features** - Vocabulary richness, word length distribution
3. **Syntactic Features** - POS patterns, dependency structures  
4. **Semantic Features** - Embedding-based coherence metrics
5. **Stylometric Features** - Punctuation patterns, sentence rhythm

## Model Signatures
Known fingerprints for: GPT-4, GPT-3.5, Claude 3, Claude 2, Llama, Mistral

## Usage
```python
from specho import SpecHODetector

detector = SpecHODetector()
result = detector.analyze(text)
print(f"AI Probability: {result.ai_score:.2%}")
print(f"Likely Model: {result.attribution}")
```

## Confidence Thresholds
- >0.95: High confidence AI
- 0.70-0.95: Likely AI, needs review
- 0.30-0.70: Uncertain
- <0.30: Likely human
```

### re-patterns/SKILL.md
```yaml
---
name: re-patterns
description: |
  iOS and macOS reverse engineering patterns and techniques.
  Common analysis workflows for binary analysis.
disable-model-invocation: true
---

# iOS/macOS RE Patterns

## Initial Triage
```bash
# Binary info
file <binary>
otool -h <binary>
otool -l <binary> | grep -A2 LC_ENCRYPTION

# Symbols
nm -u <binary>  # Undefined (imports)
nm -g <binary>  # Global (exports)

# Strings
strings -a <binary> | grep -i "api\|key\|secret\|token"

# Objective-C
class-dump <binary> > headers.h
```

## Frida Patterns
```javascript
// Hook method
Interceptor.attach(ObjC.classes.ClassName["- methodName:"].implementation, {
  onEnter: function(args) {
    console.log("Called with:", ObjC.Object(args[2]));
  }
});

// Trace class
ObjC.classes.ClassName.$methods.forEach(function(m) {
  console.log(m);
});
```

## Common Targets
- `SecItemCopyMatching` - Keychain access
- `CC_SHA256` / `CCCrypt` - Crypto operations
- `NSURLSession` - Network requests
- `UIApplication openURL` - URL schemes
```

---

## Hooks

### mcp-guard.py (Audit MCP Usage)
```python
#!/usr/bin/env python3
# ~/.claude/hooks/mcp-guard.py
"""
PreToolUse hook to audit and optionally block MCP tool usage.
Logs all MCP calls for review.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

LOG_FILE = Path.home() / ".claude" / "mcp-audit.log"

def main():
    input_data = json.load(sys.stdin)
    tool_name = input_data.get("tool_name", "")
    
    # Only process MCP tools
    if not tool_name.startswith("mcp__"):
        sys.exit(0)
    
    # Log the call
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "tool": tool_name,
        "session": input_data.get("session_id", "unknown"),
        "input": input_data.get("tool_input", {})
    }
    
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    # Allow the call (exit 0)
    # To block: exit 2 with error message
    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Hook Configuration
```json
// In ~/.claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__.*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/mcp-guard.py"
          }
        ]
      }
    ]
  }
}
```

---

## CLAUDE.md Template

```markdown
# Project: [Name]

## Quick Context
[2-3 sentences about what this project does]

## Tech Stack
- Language: [Rust/Python/TypeScript/etc]
- Framework: [if applicable]
- Key deps: [important libraries]

## Directory Structure
```
src/           - Main source
tests/         - Test files
docs/          - Documentation
```

## Development Commands
```bash
# Build
cargo build --release

# Test
cargo test

# Run
./target/release/[binary]
```

## Code Conventions
- [Your style preferences]
- [Naming conventions]
- [Error handling patterns]

## Subagent Guidelines
When delegating tasks:
- **Code search**: Use llmx-explorer (semantic search)
- **Web automation**: Use web-automation (foreground only)
- **GitHub ops**: Use github-ops (foreground only)
- **General tasks**: Use clean-task (no MCP overhead)
- **NEVER** give subagents MCP tools they don't explicitly need

## Current Focus
[What you're working on - update this]
```

---

## Workflow Integration

### Daily Workflow
```
1. Start session: `claude` (llmx always available)
2. Code search: `/search <query>` or natural language
3. Tasks needing GitHub: Claude auto-delegates to github-ops
4. Tasks needing browser: Claude auto-delegates to web-automation
5. Everything else: clean-task or inline

Tool Search handles main context. Subagents handle isolation.
```

### Project Onboarding
```bash
# Index new project
cd ~/dev/new-project
llmx index --path . --storage ~/.llmx/indexes/new-project

# Create project config if needed
mkdir -p .claude
cat > .claude/settings.json << 'EOF'
{
  "permissions": {
    "allow": ["Bash(cargo *)"]
  }
}
EOF

# Add project-specific MCP if needed
cat > .mcp.json << 'EOF'
{
  "mcpServers": {}
}
EOF
```

### Monitoring
```bash
# Check context usage
# In Claude Code: /context or /doctor

# Review MCP audit log
tail -f ~/.claude/mcp-audit.log | jq .

# Check llmx index status
llmx status
```

---

## Migration Checklist

- [ ] Backup existing `~/.claude/` directory
- [ ] Create directory structure above
- [ ] Move MCP servers from mcp.json to appropriate tiers
- [ ] Create subagent definitions
- [ ] Create slash commands
- [ ] Add hooks for MCP auditing
- [ ] Update CLAUDE.md in active projects
- [ ] Test subagent delegation with explicit prompts
- [ ] Verify Tool Search is working: `/doctor`

---

## Known Limitations

1. **Background subagents can't use MCP** - Always use foreground for MCP-heavy tasks
2. **Custom plugin subagents may not inherit MCP** - Known bug (#13605)
3. **No scoped MCP per-subagent** - Feature requested (#6915, #7289)
4. **Built-in agents can't be overridden by name** - Must disable + replace
5. **Tool Search threshold is global** - Can't set per-server

---

## Future Improvements (Watch These Issues)

- [ ] #6915 - MCP tools available only to subagent
- [ ] #7289 - Disable MCP in default, enable for subagents
- [ ] #13605 - Plugin subagents MCP access
- [ ] #13254 - Background subagents MCP access
