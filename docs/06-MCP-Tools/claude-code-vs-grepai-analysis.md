# Claude Code Built-in Tools vs grepai: Comprehensive Analysis

> Analysis date: 2026-02-05
> Source: cc-reference.txt (vtrivedy.com) and grepai codebase investigation

---

## Executive Summary

This document compares **Claude Code's built-in tools** (the native tooling shipped with Claude Code CLI) against **grepai** (a semantic code search tool that can integrate with Claude Code). While Claude Code provides general-purpose file operations and text-based search, grepai offers specialized semantic search with vector embeddings, enabling natural language queries that understand code meaning rather than just matching text patterns.

---

## Claude Code Built-in Tools Overview

Claude Code ships with 15 built-in tools for file operations, search, and task management:

### Core File Tools
| Tool | Purpose | Key Features |
|------|---------|--------------|
| **Read** | Read files from filesystem | Supports text, images, PDFs, Jupyter notebooks; offset/limit for large files |
| **Edit** | Exact string replacement | Must read file first; `replace_all` for batch renames |
| **Write** | Create/overwrite files | Prefer Edit for existing files |
| **NotebookEdit** | Edit Jupyter cells | Replace, insert, delete modes |

### Search Tools
| Tool | Purpose | Key Features |
|------|---------|--------------|
| **Glob** | Find files by pattern | Fast pattern matching, sorted by modification time |
| **Grep** | Content search (ripgrep) | Regex, file type filters, context lines, multiline support |

### Task & Agent Tools
| Tool | Purpose | Key Features |
|------|---------|--------------|
| **Task** | Launch sub-agents | Autonomous multi-step tasks; general-purpose agent type |
| **TodoWrite** | Task tracking | Status management (pending/in_progress/completed) |
| **ExitPlanMode** | Exit planning mode | Markdown plan output |

### System Tools
| Tool | Purpose | Key Features |
|------|---------|--------------|
| **Bash** | Shell commands | Background execution, timeouts up to 10 min |
| **BashOutput** | Get background output | Filter with regex |
| **KillShell** | Terminate shells | Stop background processes |
| **WebFetch** | Fetch web content | AI-processed content extraction |
| **WebSearch** | Web search | Domain filtering, current information |
| **SlashCommand** | Execute slash commands | Run available commands programmatically |

### Tool Selection Quick Reference

| Task | Use This | NOT This |
|------|----------|----------|
| Find files by name | Glob | Bash(find/ls) |
| Search content | Grep | Bash(grep/rg) |
| Read file | Read | Bash(cat/head/tail) |
| Edit file | Edit | Bash(sed/awk) |
| Create file | Write | Bash(echo >) |
| Multi-step research | Task | Multiple manual searches |

---

## grepai Overview

grepai is a **privacy-first semantic code search CLI** that indexes code using vector embeddings for natural language queries.

### Architecture

```
[Files] → Scanner → Chunker → Embedder → VectorStore
                                              ↓
[Query] → Embedder → VectorStore.Search → Boost/RRF → Results
```

### Core Components

| Component | Location | Purpose |
|-----------|----------|---------|
| Scanner | `indexer/scanner.go` | Walk filesystem, respect gitignore |
| Chunker | `indexer/chunker.go` | Split files into overlapping chunks (512 tokens) |
| Embedder | `embedder/` | Convert text to vectors |
| VectorStore | `store/` | Store and search vectors |
| Searcher | `search/search.go` | Query processing and result ranking |
| Tracer | `trace/` | Call graph analysis |

### CLI Commands

| Command | Purpose |
|---------|---------|
| `grepai init` | Create config file |
| `grepai watch` | Start daemon with real-time indexing |
| `grepai search <query>` | Semantic search |
| `grepai trace callers <symbol>` | Find all callers |
| `grepai trace callees <symbol>` | Find all called functions |
| `grepai trace graph <symbol>` | Complete call graph |
| `grepai status` | Interactive TUI |
| `grepai agent-setup` | Configure AI agent integration |

### Embedding Providers

| Provider | Type | Default Model | Dimensions |
|----------|------|---------------|------------|
| Ollama | Local | nomic-embed-text | 768 |
| OpenAI | Cloud | text-embedding-3-small | 1536 |
| LMStudio | Local | OpenAI-compatible | varies |

### Storage Backends

| Backend | Type | Best For |
|---------|------|----------|
| GOB | File-based | Small-medium projects |
| PostgreSQL + pgvector | Database | Large/multi-project |
| Qdrant | Vector DB | High-performance vector search |

### Search Features

- **Hybrid Search**: Combines vector similarity with text matching via Reciprocal Rank Fusion (RRF)
- **Structural Boosting**: Penalties for test/mock files, bonuses for src/lib directories
- **Compact Mode**: ~80% token savings for AI agents

---

## Feature Comparison

### Search Capabilities

| Feature | Claude Code (Grep) | grepai |
|---------|-------------------|--------|
| **Search Type** | Text/Regex | Semantic (vector) + Hybrid |
| **Query Language** | Regex patterns | Natural language |
| **Understanding** | Exact match | Meaning-based |
| **Example Query** | `"function.*authenticate"` | `"user login flow"` |
| **Index Required** | No | Yes (one-time) |
| **Real-time Updates** | N/A | Filesystem watcher |

### Query Examples

**Finding authentication code:**

| Tool | Query |
|------|-------|
| Claude Code Grep | `pattern: "authenticate\|login\|auth"` |
| grepai | `grepai search "user authentication flow"` |

**Finding error handling:**

| Tool | Query |
|------|-------|
| Claude Code Grep | `pattern: "catch\|error\|exception"` |
| grepai | `grepai search "how errors are handled"` |

### File Operations

| Feature | Claude Code | grepai |
|---------|-------------|--------|
| Read files | ✅ Read tool | ❌ (use Claude Code) |
| Edit files | ✅ Edit tool | ❌ (use Claude Code) |
| Write files | ✅ Write tool | ❌ (use Claude Code) |
| Find files | ✅ Glob tool | ✅ (via search results) |

### Code Intelligence

| Feature | Claude Code | grepai |
|---------|-------------|--------|
| Semantic search | ❌ | ✅ |
| Call graph tracing | ❌ | ✅ (12+ languages) |
| Symbol extraction | ❌ | ✅ |
| Find callers | ❌ | ✅ `trace callers` |
| Find callees | ❌ | ✅ `trace callees` |

### AI Integration

| Feature | Claude Code | grepai |
|---------|-------------|--------|
| JSON output | ❌ | ✅ `--json` |
| Compact output | ❌ | ✅ `--compact` |
| MCP Server | N/A | ✅ Native MCP |
| Token efficiency | Standard | 80% savings with compact |

### Privacy & Performance

| Feature | Claude Code | grepai |
|---------|-------------|--------|
| Local-only option | ✅ | ✅ (Ollama/LMStudio) |
| Cloud option | N/A | ✅ (OpenAI) |
| Real-time index | N/A | ✅ (watcher daemon) |
| Multi-project | ❌ | ✅ (workspaces) |

---

## Complementary Use Cases

### When to Use Claude Code Grep

1. **Exact text search**: Finding specific variable names, imports, strings
2. **Regex patterns**: Complex pattern matching like `log.*Error`
3. **Quick lookups**: No index needed, instant results
4. **Counting occurrences**: `output_mode: "count"`

### When to Use grepai

1. **Natural language queries**: "where is user data validated"
2. **Understanding intent**: "error handling middleware"
3. **Code exploration**: "how does authentication work"
4. **Call graph analysis**: Finding all callers before refactoring
5. **Cross-project search**: Searching multiple codebases

### Recommended Workflow

```
1. Use grepai for initial exploration (natural language)
2. Use Claude Code Grep for exact matches (regex)
3. Use grepai trace for understanding function relationships
4. Use Claude Code Read/Edit/Write for file modifications
```

---

## Future-Forward Analysis

### Claude Code Built-in Tools

**Strengths:**
- Native integration, no setup required
- Covers all file operations
- Task agent for complex multi-step work
- Web fetch/search for external information
- Battle-tested, stable

**Limitations:**
- Text-based search only (no semantic understanding)
- No call graph analysis
- No code intelligence beyond text matching
- No incremental indexing

### grepai

**Strengths:**
- Semantic understanding of code
- Natural language queries
- Call graph tracing
- Multiple embedding providers (local/cloud)
- Real-time incremental indexing
- MCP server for native AI integration
- Token-efficient output formats
- Privacy-first (local Ollama/LMStudio)
- Multi-project workspaces

**Limitations:**
- Requires initial indexing
- No file modification capabilities
- Depends on embedding quality
- Additional tool to maintain

### Verdict: Which is More Future-Forward?

**grepai is more future-forward** for code search and understanding because:

1. **AI-Native Design**: Built specifically for AI agent workflows with MCP, JSON output, and token efficiency
2. **Semantic Understanding**: Natural language queries match how developers think about code
3. **Code Intelligence**: Call graph tracing provides structural understanding beyond text
4. **Scalability**: Multiple storage backends support growth from single projects to enterprise
5. **Privacy Options**: Local embedding providers align with enterprise security requirements
6. **Composability**: Designed to complement (not replace) Claude Code's file operations

**However**, Claude Code's built-in tools remain essential for:
- All file modifications (Read/Edit/Write)
- Exact text matching
- No-setup simplicity
- Shell operations

### Recommended Integration

```yaml
# In CLAUDE.md
## Search Strategy
- Use `grepai search` for semantic queries (understanding code intent)
- Use `grepai trace` for call graph analysis
- Use Claude Code Grep for exact text/regex matches
- Always use Claude Code Read/Edit/Write for file operations
```

---

## Appendix: Tool Parameters Reference

### Claude Code Grep Parameters

```json
{
  "pattern": "regex pattern",
  "path": "/optional/path",
  "output_mode": "content|files_with_matches|count",
  "glob": "*.ts",
  "type": "js|py|rust|go",
  "-A": 3,
  "-B": 3,
  "-C": 3,
  "-i": true,
  "-n": true,
  "multiline": true,
  "head_limit": 10
}
```

### grepai Search Flags

```bash
grepai search "query" \
  -n 10           # Limit results
  --json          # JSON output
  --compact       # Omit content
  --toon          # Token-efficient format
  --workspace ws  # Cross-project
```

### grepai Trace Flags

```bash
grepai trace callers "FunctionName" --json
grepai trace callees "FunctionName" --json
grepai trace graph "FunctionName" --depth 3 --json
```

---

## Source Files

- Claude Code reference: `/home/zack/dev/anthropic-docs-wiki/docs/02-Claude-Code-CLI/claude-code-built-in-tools-reference.md`
- grepai codebase: `/home/zack/dev/grepai/`
- Original source: https://www.vtrivedy.com/posts/claudecode-tools-reference
