---
title: "Skills Frontmatter Analysis - Claude Code 2.1.72"
category: "08-Plugins-Skills"
tags: ["claude-code", "plugins", "skills"]
---

# Skills Frontmatter Analysis - Claude Code 2.1.72

Binary: `/home/zack/.local/share/claude/versions/2.1.72` (234MB, 13,675-line JS payload)
Extracted: `2.1.72_bunfs_extracted/src/entrypoints/cli.js`

## Frontmatter Fields (Complete)

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | string | folder name | Display name |
| `description` | string | extracted from body | Shown in skill listing |
| `allowed-tools` | string[] | none | Tool permissions (e.g., `["Read", "Bash(gh:*)"]`) |
| `user-invocable` | boolean | `true` | User can invoke via `/skillname` |
| `disable-model-invocation` | boolean | `false` | Prevents model auto-invoke |
| `when_to_use` | string | none | Trigger phrases for model auto-invocation |
| `argument-hint` | string | none | Placeholder in UI (e.g., `[issue]`) |
| `arguments` | object | none | Named params with `$name` substitution |
| `model` | string | current | Override model (`inherit` = caller's) |
| `version` | string | none | Version tracking |
| `context` | `"fork"` | none | Fork execution (isolated) |
| `agent` | any | none | Agent configuration |
| `hooks` | object | none | Skill-specific hooks |
| `paths` | string | none | Path restrictions (e.g., `src/**`) |

## Invocation Matrix

```
+---------------------+-----------------+-------------------------+
| user-invocable      | disable-model-  | Result                  |
|                     | invocation      |                         |
+---------------------+-----------------+-------------------------+
| true (default)      | false (default) | User: /skill            |
|                     |                 | Model: auto-invokes     |
+---------------------+-----------------+-------------------------+
| true                | true            | User: /skill            |
|                     |                 | Model: CANNOT invoke    |
+---------------------+-----------------+-------------------------+
| false               | false           | User: hidden from /     |
|                     |                 | Model: auto-invokes     |
+---------------------+-----------------+-------------------------+
| false               | true            | Dead code (unreachable) |
+---------------------+-----------------+-------------------------+
```

## Model Invocation Logic

From `IV` memoized function (line ~6090):

```javascript
// Model-invocable skills filter:
filter((A) =>
  A.type === "prompt" &&
  !A.disableModelInvocation &&
  A.source !== "builtin" &&
  (A.hasUserSpecifiedDescription || A.whenToUse)
)
```

Model auto-invokes only when:
1. `disable-model-invocation` is NOT true
2. Source is not `builtin`
3. Has explicit `description` OR `when_to_use`

## Precedence (Loading Order)

```
+------------------------------------------------------------------+
|                  SKILL LOADING ORDER                             |
|            (later entries override earlier by name)              |
+------------------------------------------------------------------+
|  1. bundledSkills      - Shipped in binary                       |
|  2. builtinPluginSkills - Plugin-provided builtins               |
|  3. skillDirCommands   - .claude/skills/ (project + user)        |
|  4. MCP prompt skills  - From MCP servers                        |
|  5. pluginSkills       - Plugin-loaded skills                    |
|  6. RcA() (local)      - Local slash commands (/help, /config)   |
+------------------------------------------------------------------+
```

**Source types**:
- `builtin` - Hardcoded in binary
- `bundled` - Shipped SKILL.md in binary
- `project` - `.claude/skills/<name>/SKILL.md`
- `user` - `~/.claude/skills/<name>/SKILL.md`
- `plugin` - From installed plugin
- `mcp` - From MCP server prompts

**User overrides project**: User skills load after project skills, so same-name user skill wins.

## Related Surfaces

| Surface | Location | Key Frontmatter |
|---------|----------|-----------------|
| **Skills** | `.claude/skills/<name>/SKILL.md` | All fields above |
| **Agents** | `.claude/agents/<name>.md` | `name`, `description`, `tools`, `model`, `memory` |
| **MCP prompts** | Server `prompts/list` | Server-defined |
| **Hooks** | `settings.json` | N/A (JSON config) |

## Builtin Skills (2.1.72)

| Name | userInvocable | disableModelInvocation | Line |
|------|---------------|------------------------|------|
| `keybindings-help` | false | false | 7329 |
| `debug` | true | **true** | 7595 |
| `simplify` | true | false | 7776 |

## Key Functions

| Minified | Purpose | Line |
|----------|---------|------|
| `kP` | Register builtin skill | 6941+ |
| `cpH` | Load skills from directory | ~1472 |
| `rlf` | Construct skill object from frontmatter | ~1470 |
| `vw` | Parse frontmatter from markdown | (yaml parser) |
| `h0` | Get all skills (memoized) | ~6090 |
| `IV` | Get model-invocable skills | ~6090 |

## Example SKILL.md

```yaml
---
name: My Workflow
description: Does X when Y happens
when_to_use: "Use when user wants X. Examples: 'do X', 'run X'"
allowed-tools:
  - Read
  - Bash(git:*)
  - Glob
user-invocable: true
disable-model-invocation: false
argument-hint: "[target file]"
arguments:
  file: "The file to process"
model: sonnet
context: fork
version: "1.0.0"
paths: "src/**"
---

# My Workflow

Step 1: ...
```

## Notes

- `when_to_use` text is critical for model auto-invocation; should start with "Use when..."
- `context: fork` creates isolated execution (no mid-process user input)
- `allowed-tools` supports patterns like `Bash(gh:*)` for scoped permissions
- `paths` restricts skill to specific file paths (glob patterns)
- `model: inherit` uses caller's model instead of overriding
