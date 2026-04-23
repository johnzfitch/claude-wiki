---
title: "Plugin Marketplace: What It Actually Is"
category: "08-Plugins-Skills"
tags: ["enterprise", "plugins"]
---

# Plugin Marketplace: What It Actually Is

**Date**: 2026-03-13
**Finding**: The plugin marketplace is **NOT CoWork-specific** — it's for **enterprise managed deployments**

---

## What I Found vs. What It Actually Is

### Initial Theory ❌
> "This might already work in Claude CoWork"

### Reality ✅
The plugin system is designed for **enterprise/team managed deployments**, not CoWork specifically.

CoWork in 2.1.70/2.1.74 only added:
- `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` — Shared team memory sync
- `teammate_id` — Team member identification
- `tengu_team_mem_sync_started` — Memory sync telemetry

**CoWork ≠ Plugin Marketplace**. They're separate features.

---

## Seed Directory Architecture (Enterprise Deployment)

### Core Functions

```javascript
// Get seed directory (admin-managed shared plugin location)
function zp() {
  let seedDir = process.env.CLAUDE_CODE_PLUGIN_SEED_DIR;
  return seedDir ? normalizePath(seedDir) : undefined;
}

// Check if path is in seed (read-only)
function qgH(path) {
  let seed = zp();
  if (!seed) return false;
  return path === seed || path.startsWith(seed + PATH_SEP);
}
```

### Usage Pattern

**Corporate IT sets up**:
```bash
# On shared NFS mount or corporate file server
export CLAUDE_CODE_PLUGIN_SEED_DIR=/nfs/corporate/claude-plugins

# Pre-install approved plugins
/nfs/corporate/claude-plugins/
├── cache/
│   ├── corporate-internal/
│   │   ├── security-scanner/
│   │   │   └── 1.0.0/          # Pre-downloaded, cached
│   │   └── compliance-agent/
│   │       └── 2.1.0/
│   └── official/
│       └── database-assistant/
│           └── 1.5.0/
└── known_marketplaces.json     # Pre-configured marketplace sources
```

**Users get**:
- ✅ Instant access to pre-approved plugins (no download)
- ✅ Read-only — can't modify admin-installed plugins
- ✅ Can still install personal plugins to `~/.claude/plugins/`
- ❌ Can't enable/disable seed plugins (policy-locked)

---

## How It Actually Works

### Marketplace Loading Priority

1. **Check seed directory first** (`CLAUDE_CODE_PLUGIN_SEED_DIR`)
   - If marketplace exists in seed → use read-only copy
   - If plugin cached in seed → use cached copy

2. **Check user directory** (`~/.claude/plugin-marketplaces/`)
   - If marketplace not in seed → load from user config
   - Download plugins to user cache

3. **Error handling**:
   ```javascript
   if (qgH(marketplace.installLocation)) {
     throw Error(
       `Marketplace '${name}' is seed-managed (${zp()}). ` +
       `To use a different source, ask your admin to update the seed, ` +
       `or use a different marketplace name.`
     );
   }
   ```

### Auto-Update Behavior

```javascript
async function setMarketplaceAutoUpdate(name, enabled) {
  let marketplaces = await getMarketplaceRegistry();
  let marketplace = marketplaces[name];

  if (qgH(marketplace.installLocation)) {
    throw Error(
      `Marketplace '${name}' is seed-managed (${zp()}) ` +
      `and auto-update is always disabled for seed content. ` +
      `To update: ask your admin to update the seed.`
    );
  }

  // ... normal auto-update logic
}
```

**Seed marketplaces cannot be auto-updated by users** — only admins can update the seed.

---

## Plugin Installation Flow (With Seed)

```
User runs: claude plugin install database-assistant --marketplace official

1. Check if "official" marketplace in seed
   └─ Yes: Use /nfs/corporate/claude-plugins/known_marketplaces.json

2. Load marketplace catalog
   └─ Check seed cache for plugin
      └─ Yes: Use /nfs/corporate/claude-plugins/cache/official/database-assistant/1.5.0/
      └─ No: Download to ~/.claude/plugins/cache/official/database-assistant/1.5.0/

3. Check dependencies (same process for each)

4. Install to:
   - Seed plugins: Use in-place (no copy)
   - Downloaded plugins: ~/.claude/plugins/cache/<marketplace>/<name>/<version>/

5. Enable in settings
   - User settings: ~/.claude/settings.json (if not policy-locked)
   - Policy settings: Read-only from admin
```

---

## CoWork vs. Seed Plugins: Separate Features

| Feature | CoWork | Seed Plugins |
|---------|--------|--------------|
| **Purpose** | Team memory sync | Enterprise plugin distribution |
| **Env Var** | `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` | `CLAUDE_CODE_PLUGIN_SEED_DIR` |
| **What's Shared** | Conversation memory, learnings | Pre-installed plugins, marketplaces |
| **Write Access** | Team members can write memory | Users read-only, admin manages |
| **Version** | New in 2.1.70 | New in 2.1.70 |
| **Telemetry** | `tengu_team_mem_sync_started` | None specific (uses plugin events) |

---

## Deployment Scenarios

### 1. Individual Developer (Default)

```bash
# No seed directory
unset CLAUDE_CODE_PLUGIN_SEED_DIR

# Install plugins to ~/.claude/
claude plugin marketplace add official --source github --repo anthropics/plugins
claude plugin install database-assistant
```

**Result**: Everything in `~/.claude/plugin-marketplaces/` and `~/.claude/plugins/cache/`

---

### 2. Corporate Managed Deployment

```bash
# Corporate IT mounts shared plugin directory
export CLAUDE_CODE_PLUGIN_SEED_DIR=/nfs/corp-it/claude-plugins

# Pre-configured marketplaces in seed
ls $CLAUDE_CODE_PLUGIN_SEED_DIR/known_marketplaces.json
# → corporate-internal, approved-oss

# Users get instant access
claude plugin list --marketplace corporate-internal
# → security-scanner, compliance-agent, sql-auditor (all pre-cached)
```

**Result**:
- Seed plugins available immediately (no download)
- Users can't modify/remove seed marketplaces
- Personal plugins still go to `~/.claude/`

---

### 3. CoWork Team (Separate from Plugins)

```bash
# Team memory sync (separate feature)
export CLAUDE_COWORK_MEMORY_PATH_OVERRIDE=/shared/team-memory

# Plugins still work normally
export CLAUDE_CODE_PLUGIN_SEED_DIR=/shared/team-plugins  # Optional
```

**Result**:
- Team shares conversation memory/learnings
- Plugins can be shared OR individual
- Two independent systems

---

## Policy Integration

Seed plugins integrate with policy settings:

```json
{
  "policySettings": {
    "strictKnownMarketplaces": [
      {
        "source": "directory",
        "path": "/nfs/corp-it/claude-plugins/corporate-internal"
      }
    ],
    "enabledPlugins": {
      "security-scanner@corporate-internal": true,   // Force-enabled
      "risky-plugin@community": false                // Force-disabled
    },
    "pluginTrustMessage": "Only corporate-internal plugins are approved for production use."
  }
}
```

**Effect**:
- Users can only use marketplaces from seed
- Certain plugins are mandatory
- Custom trust message shown

---

## Why Seed Exists: The Enterprise Use Case

### Problem
1. **Slow onboarding**: Each developer downloads plugins individually
2. **Version drift**: Developers on different plugin versions
3. **Security**: Can't control what plugins developers install
4. **Bandwidth**: 100 developers × 50MB plugins = 5GB network traffic

### Solution (Seed Directory)
1. **Fast onboarding**: Plugins pre-cached on NFS mount
2. **Version pinning**: Everyone uses admin-approved versions
3. **Security**: Policy locks allowed marketplaces
4. **Bandwidth**: One download to seed, everyone reads locally

---

## Actual Status: Where Is This Live?

### Evidence It's NOT Live Publicly

1. **Feature flag still off**: `tengu_orchid_trellis = false` by default
2. **No public marketplace**: No `anthropics/claude-plugins` repo exists
3. **No signing/sandboxing**: Security not implemented yet
4. **Seed directory optional**: Not mentioned in public docs

### Evidence It MIGHT Be Live Internally

1. **Seed directory infrastructure complete** — Fully implemented
2. **Policy controls production-ready** — Allowlists, blocklists, managed plugins
3. **CoWork + seed together** — Both added in 2.1.70 (team features)
4. **Deployment-focused** — Not consumer-oriented

### Most Likely Scenario

**Anthropic is using this internally for their own teams:**
- Internal marketplace: `@anthropic/internal-plugins`
- Seed directory: `/shared/anthropic-plugins`
- CoWork memory: `/shared/team-memory`
- Policy-locked: Only approved internal plugins

**Not yet ready for public use:**
- No plugin signing → can't trust community plugins
- No sandboxing → malicious plugins = full access
- No moderation → no review process

---

## Conclusion

The plugin marketplace is **not a CoWork feature** — it's an **enterprise managed deployment system** with:

1. ✅ **Seed directory support** for pre-installed shared plugins
2. ✅ **Policy controls** for locked-down corporate environments
3. ✅ **Multi-marketplace federation** for internal + external catalogs
4. ✅ **Complete dependency resolution** with cycle detection
5. ❌ **No public catalog** — infrastructure only
6. ❌ **No security hardening** — signing/sandboxing missing

**CoWork** is a separate feature for **team memory sync**, not plugin distribution.

Both features likely **exist for Anthropic's internal use** and will be publicly launched when security is ready.

---

**Key Env Vars**:
- `CLAUDE_CODE_PLUGIN_SEED_DIR` — Shared read-only plugin cache
- `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` — Shared team memory sync (separate)

**Status**: Infrastructure complete, security hardening in progress, no public launch yet.
