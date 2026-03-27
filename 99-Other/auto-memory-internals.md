# Claude Code 2.1.76 — Auto-Memory Internals

How the post-sampling hook system and auto-memory extraction work under the hood.

---

## System Overview

```
Main Query Loop (3896.js)
│
│  user sends message
│  ↓
│  LLM sampling → response messages (e)
│  ↓
│  if (e.length > 0)
│      Zif([...existingMessages, ...newMessages], systemPrompt, userCtx, sysCtx, toolCtx, querySource)
│          │
│          ↓
│      Post-Sampling Hook Registry (Wif[])
│          │
│          └── g9_ (auto-memory extraction)
│                  │
│                  ├── gate checks (feature flag, thresholds)
│                  ├── reads current MEMORY.md
│                  ├── builds extraction prompt
│                  └── forks sub-query (AT) → writes updated MEMORY.md
```

---

## 1. Post-Sampling Hook Framework

**File**: `3887.js`

The hook system is a simple observer pattern — a push-only array of async callbacks.

```javascript
var Wif = [];   // hook registry

// Register a hook
function Tif(callback) {
    Wif.push(callback);
}

// Dispatch to all hooks (called after every LLM turn)
async function Zif(messages, systemPrompt, userContext, systemContext, toolUseContext, querySource) {
    let ctx = {
        messages,        // full conversation history (old + new)
        systemPrompt,    // current system prompt
        userContext,      // user-level context (CLAUDE.md, etc.)
        systemContext,    // system-level context
        toolUseContext,   // tool state (readFileState, etc.)
        querySource       // "repl_main_thread", "session_memory", "agent", etc.
    };
    for (let hook of Wif)
        try {
            await hook(ctx);
        } catch (err) {
            fH(err instanceof Error ? err : Error(`Post-sampling hook failed: ${err}`));
        }
}
```

### Key Properties

- **Sequential execution**: Hooks run one at a time (`for...of` + `await`), not in parallel
- **Error isolation**: Each hook is wrapped in try/catch — one failing hook doesn't block others
- **No return value**: Hooks are fire-and-forget; they can't modify the conversation flow
- **No priority/ordering**: Hooks execute in registration order (FIFO push)
- **Errors go to ring buffer**: Failed hooks report via `fH()` (error reporting system, 100-entry ring buffer)

### Call Site

In `3896.js`, inside the main query generator:

```javascript
// After LLM sampling produces assistant messages (e):
if (e.length > 0)
    Zif([...u, ...e], A, L, D, Y, M);
```

Where `u` = existing conversation messages, `e` = new assistant response messages.
Only fires when the model actually produced output (no-op on empty responses or errors).

---

## 2. Hook Registration

**File**: `4557.js`

Only one hook is currently registered: `g9_` (auto-memory extraction).

```javascript
function nX8() {
    if (L8()) return;     // skip if headless/simple mode (CLAUDE_CODE_SIMPLE)
    if (!$h()) return;    // skip if auto-compact disabled (DISABLE_COMPACT / DISABLE_AUTO_COMPACT)
    Tif(g9_);             // register the auto-memory hook
}
```

`nX8()` is called during session initialization. The hook is only registered when:
1. **Not in simple/headless mode** — `L8()` returns false
2. **Auto-compact enabled** — `$h()` returns true (respects `DISABLE_COMPACT` and `DISABLE_AUTO_COMPACT` env vars plus the `autoCompactEnabled` setting)

---

## 3. Auto-Memory Extraction Hook (g9_)

**File**: `4558.js`

This is the core logic. When the hook fires, it decides whether to extract memories from the conversation and write them to `summary.md`.

```javascript
g9_ = Tx(async function({ messages, toolUseContext, querySource }) {
    // ── Gate 1: Only run on main REPL thread ──
    if (querySource !== "repl_main_thread") return;

    // ── Gate 2: Feature flag must be on ──
    if (!b9_()) return;   // _A("tengu_session_memory", false)

    // ── Gate 3: Init config, check thresholds ──
    U9_();                // load config from tengu_sm_config
    if (!B9_(messages)) return;  // token + tool-call threshold check

    // ── Mark extraction in progress ──
    nnf();   // jR$ = Date.now()  (locks out concurrent extractions)

    // ── Read current memory file ──
    let toolCtx = gQH(toolUseContext);  // snapshot tool context
    let { memoryPath, currentMemory } = await p9_(toolCtx);

    // ── Build extraction prompt ──
    let prompt = await Kif(currentMemory, memoryPath);

    // ── Fork sub-query: extract and write memories ──
    await AT({
        promptMessages: [U$({ content: prompt })],
        cacheSafeParams: bu(hook_context),
        canUseTool: d9_(memoryPath),      // ONLY allow Write to the memory file
        querySource: "session_memory",
        forkLabel: "session_memory",
        overrides: { readFileState: toolCtx.readFileState }
    });

    // ── Log telemetry ──
    Q("tengu_session_memory_extraction", {
        input_tokens, output_tokens,
        cache_read_input_tokens, cache_creation_input_tokens,
        config_min_message_tokens_to_init,
        config_min_tokens_between_update,
        config_tool_calls_between_updates
    });

    // ── Update state ──
    tnf(jJ(messages));  // record token count at extraction time
    F9_(messages);      // update UUID bookmark
    inf();              // clear in-progress lock (jR$ = undefined)
});
```

---

## 4. Threshold System (B9_)

**File**: `4557.js` + `3879.js`

The hook doesn't fire every turn. `B9_()` enforces three thresholds:

```javascript
function B9_(messages) {
    let tokenCount = jJ(messages);  // total tokens in conversation

    // First-time init: have we hit minimum tokens?
    if (!snf()) {                             // snf() = Qnf (has init fired?)
        if (!Hif(tokenCount)) return false;   // tokenCount >= minimumMessageTokensToInit?
        enf();                                // mark init complete
    }

    // Recurring: enough tokens since last extraction?
    let tokenThresholdMet = $if(tokenCount);  // tokenCount - cnf >= minimumTokensBetweenUpdate?

    // Recurring: enough tool calls since last extraction?
    let toolCallThresholdMet = m9_(messages, lX8) >= Aif();  // count tool_use blocks since bookmark

    // Has assistant made tool calls in last message?
    let lastMsgHasToolUse = snH(messages);

    // Trigger if: (both thresholds met) OR (token threshold met AND no pending tool use)
    if (tokenThresholdMet && toolCallThresholdMet || tokenThresholdMet && !lastMsgHasToolUse) {
        lX8 = messages[messages.length - 1]?.uuid;  // bookmark current position
        return true;
    }
    return false;
}
```

### Default Thresholds

**File**: `3880.js`

```javascript
CnH = {
    minimumMessageTokensToInit:  10000,  // 10k tokens before first extraction
    minimumTokensBetweenUpdate:  5000,   // 5k tokens between extractions
    toolCallsBetweenUpdates:     3        // 3 tool calls between extractions
};
```

These can be overridden via the `tengu_sm_config` GrowthBook feature flag (object with same keys).

### State Variables

**File**: `3879.js`

```javascript
var cnf = 0;          // token count at last extraction
var Qnf = false;      // has first extraction fired?
var jR$ = undefined;   // timestamp when extraction started (concurrency lock)
var IWH = {...CnH};   // active config (defaults + overrides)
```

### Concurrency Protection

```javascript
function nnf() { jR$ = Date.now(); }   // mark extraction in-progress
function inf() { jR$ = undefined; }     // mark extraction complete

// rnf() — wait for in-progress extraction (with timeouts)
async function rnf() {
    let start = Date.now();
    while (jR$) {
        if (Date.now() - jR$ > 60000) return;   // extraction timeout: 60s
        if (Date.now() - start > 15000) return;  // wait timeout: 15s
        await new Promise(r => setTimeout(r, 1000));  // poll every 1s
    }
}
```

---

## 5. Memory File Location

**File**: `4468.js`

```javascript
function Um$() {
    return path.join(configDir(), sessionId(), "session-memory") + path.sep;
}

function XWH() {
    return path.join(Um$(), "summary.md");
}
```

Result: `~/.claude/projects/<project-hash>/<session-id>/session-memory/summary.md`

On first extraction, if the file doesn't exist, it's created with the default template via `flag: "wx"` (exclusive create — won't overwrite).

---

## 6. Extraction Prompt

**File**: `3880.js`

The extraction prompt (`fif()`) instructs the forked sub-query to update the memory file. Key rules:

1. **Scope**: Only analyze the user conversation — exclude system prompt, CLAUDE.md, and the note-taking instructions themselves
2. **Tool restriction**: Only use `Edit` tool on the memory file path (enforced by `d9_()`)
3. **Structure preservation**: Never modify section headers or italic description lines
4. **Per-section limit**: ~2,000 tokens per section (`JR$ = 2000`)
5. **Total file limit**: ~12,000 tokens (`Lif = 12000`)
6. **Parallel edits**: Make all Edit tool calls in a single parallel message, then stop
7. **Priority**: Always keep "Current State" up to date

### Customization

Users can override both the template and extraction prompt:

```
~/.claude/session-memory/config/template.md   → custom memory file template
~/.claude/session-memory/config/prompt.md      → custom extraction prompt
```

If these files exist, they're loaded instead of the defaults. If they fail to load (non-ENOENT error), the error is reported via `fH()` and defaults are used as fallback.

### Oversized File Handling

`sS6()` checks section sizes and total file size, appending condensation instructions:

- If any section exceeds 2,000 tokens: instructs the model to condense it
- If total file exceeds 12,000 tokens: **CRITICAL** instruction to aggressively shorten

### Default Template Sections

```markdown
# Session Title
# Current State
# Task specification
# Files and Functions
# Workflow
# Errors & Corrections
# Codebase and System Documentation
# Learnings
# Key results
# Worklog
```

---

## 7. Tool Restriction (d9_)

**File**: `4557.js`

The forked sub-query is sandboxed — it can only use one tool on one file:

```javascript
function d9_(memoryPath) {
    return async (tool, input) => {
        if (tool.name === Cf &&                // Cf = Edit tool name
            typeof input === "object" &&
            input !== null &&
            "file_path" in input) {
            let filePath = input.file_path;
            if (typeof filePath === "string" && filePath === memoryPath)
                return { behavior: "allow", updatedInput: input };
        }
        return {
            behavior: "deny",
            message: `only ${Cf} on ${memoryPath} is allowed`,
            decisionReason: { type: "other", reason: `only ${Cf} on ${memoryPath} is allowed` }
        };
    };
}
```

This ensures the memory extraction sub-query:
- Can ONLY use the Edit tool (not Read, Bash, Write, or any other tool)
- Can ONLY edit the specific memory file path
- Cannot read files, run commands, or modify anything else

---

## 8. Forked Sub-Query (AT)

**File**: `3900.js`

`AT()` creates an isolated LLM sub-query that shares the parent's conversation context but has its own tool permissions and query source:

```javascript
function AT({
    promptMessages,       // the extraction prompt
    cacheSafeParams,      // cache config from parent
    canUseTool,           // d9_(memoryPath) — restricted tool access
    querySource,          // "session_memory"
    forkLabel,            // "session_memory"
    overrides,            // { readFileState } from parent context
    maxOutputTokens,      // optional limit
    maxTurns,             // optional turn limit
    onMessage,            // optional message callback
    skipTranscript,       // don't save to transcript
    skipCacheWrite        // don't cache results
}) { ... }
```

The sub-query runs the same model as the main conversation, but:
- Uses a separate abort controller (doesn't affect main conversation if it fails)
- Has its own tool permission function (`canUseTool`)
- Is labeled `"session_memory"` for telemetry and to prevent recursive extraction
- Shares the parent's read file state so it knows what files have been read

---

## 9. Telemetry

### Event: `tengu_session_memory_extraction`
Fired after each successful extraction:
```javascript
{
    input_tokens: number,
    output_tokens: number,
    cache_read_input_tokens: number,
    cache_creation_input_tokens: number,
    config_min_message_tokens_to_init: number,    // active threshold
    config_min_tokens_between_update: number,     // active threshold
    config_tool_calls_between_updates: number     // active threshold
}
```

### Event: `tengu_session_memory_file_read`
Fired when the current memory file is read before extraction:
```javascript
{ content_length: number }
```

### Feature Flag: `tengu_session_memory`
- Type: boolean
- Default: `false`
- Controls: Whether auto-memory extraction is enabled at all

### Feature Flag: `tengu_sm_config`
- Type: object
- Default: `{}`
- Controls: Override threshold values (`minimumMessageTokensToInit`, `minimumTokensBetweenUpdate`, `toolCallsBetweenUpdates`)

---

## 10. Complete Data Flow

```
User sends message
    ↓
Main LLM sampling
    ↓
Response messages produced
    ↓
Zif() dispatches to all registered hooks
    ↓
g9_ (auto-memory) runs:
    │
    ├─ querySource === "repl_main_thread"?  (NO → skip, prevents recursion)
    ├─ tengu_session_memory flag on?         (NO → skip)
    ├─ Load config from tengu_sm_config
    ├─ B9_() threshold check:
    │   ├─ First time: tokenCount >= 10,000?
    │   ├─ Recurring: tokenCount - lastExtraction >= 5,000?
    │   └─ Recurring: toolCallsSinceLastExtraction >= 3?
    │   (NO → skip)
    │
    ├─ Lock (nnf: jR$ = Date.now())
    ├─ Read summary.md (create from template if missing)
    ├─ Build extraction prompt (fif + oversize warnings)
    │
    ├─ Fork sub-query via AT():
    │   ├─ Same model as main conversation
    │   ├─ Receives full conversation as context
    │   ├─ Tool access: ONLY Edit on summary.md
    │   ├─ querySource: "session_memory" (prevents recursive hook)
    │   └─ LLM extracts memories → Edit calls to update summary.md
    │
    ├─ Log tengu_session_memory_extraction
    ├─ Update token bookmark (cnf = current token count)
    ├─ Update UUID bookmark (lX8 = last message UUID)
    └─ Unlock (inf: jR$ = undefined)
```

---

## 11. Disabling Auto-Memory

Any of these will prevent the hook from running:

| Method | Effect |
|--------|--------|
| `tengu_session_memory = false` | Feature flag (server-side, default) |
| `DISABLE_COMPACT=true` | Prevents hook registration (`$h()` fails) |
| `DISABLE_AUTO_COMPACT=true` | Same effect |
| `CLAUDE_CODE_SIMPLE=true` | Headless mode, skips hook registration |
| Non-REPL querySource | Hook self-filters (only runs on `repl_main_thread`) |

---

## 12. Relationship to User-Facing "Auto Memory"

The auto-memory system visible to users (`/home/zack/.claude/projects/<hash>/memory/MEMORY.md`) is a **different system** from session memory. Session memory (`summary.md`) is:

- Per-session (lives in session directory, not project memory directory)
- Automatically extracted (no user control over content)
- Used for session continuity after compaction
- Gated by `tengu_session_memory` (currently off by default)

The user-facing auto-memory directory at `~/.claude/projects/<hash>/memory/` is managed by the model directly during conversation (via explicit Write/Edit tool calls in the main conversation), not by this post-sampling hook system.
