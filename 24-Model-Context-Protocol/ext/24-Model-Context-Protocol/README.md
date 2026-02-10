# Model Context Protocol - Complete Documentation Archive

This directory contains a complete archive of the official Model Context Protocol (MCP) documentation.

## What's Included

✅ **20 Core Files Downloaded** (fully complete with all content)
- Getting started guides
- Build tutorials (client & server)
- Architecture documentation
- Core concepts (server & client)
- Community governance
- SDK documentation

📥 **67 Remaining Files** (automated download script ready)
- All 26 SEPs (Specification Enhancement Proposals)
- Complete specification (27 files)
- Registry documentation (11 files)
- Additional tools and tutorials

## Quick Start

### View the Documentation

```bash
cd /home/zack/Documents/mcp-docs

# View the complete index
cat INDEX.md

# Read getting started
cat docs/getting-started/intro.md

# Check architecture
cat docs/learn/architecture.md
```

### Download Remaining Files

Run the automated download script to fetch all remaining 67 files:

```bash
cd /home/zack/Documents/mcp-docs
python3 download-remaining.py
```

**Requirements:**
```bash
pip install requests  # or: uv pip install requests
```

The script will:
- Download all 67 remaining files
- Preserve the directory structure
- Add metadata headers (source URL, download date)
- Show progress and handle errors gracefully
- Use exponential backoff and retry logic

## Directory Overview

```
mcp-docs/
├── INDEX.md                    # Complete catalog of all files
├── README.md                   # This file
├── download-remaining.py       # Automated download script
│
├── clients.md                  # ✅ Downloaded
├── examples.md                 # ✅ Downloaded
├── extensions.md               # ✅ Downloaded
│
├── community/                  # ✅ Downloaded (7 files)
│   ├── governance.md
│   ├── contributing.md
│   └── seps/                   # 📥 26 SEPs (download script)
│
├── docs/                       # ✅ Downloaded (11 files)
│   ├── develop/                # Build guides
│   ├── getting-started/        # Introduction
│   ├── learn/                  # Core concepts
│   ├── tools/                  # 📥 Inspector docs
│   └── extensions/             # 📥 Extensions
│
├── experimental/               # ✅ Downloaded
│   └── ext-skills.md           # Skills over MCP IG
│
├── registry/                   # 📥 11 files (download script)
│   ├── about.md
│   ├── quickstart.md
│   └── ...
│
└── specification/              # 📥 27 files (download script)
    └── 2025-11-25/
        ├── index.md
        ├── architecture/
        ├── basic/
        ├── client/
        └── server/
```

## What You Can Do

### Learn MCP
Start with these files (all ✅ downloaded):
1. `docs/getting-started/intro.md` - What is MCP?
2. `docs/learn/architecture.md` - System overview
3. `docs/learn/server-concepts.md` - Server features
4. `docs/learn/client-concepts.md` - Client features

### Build with MCP
Development guides (all ✅ downloaded):
- `docs/develop/build-server.md` - Complete server tutorial
- `docs/develop/build-client.md` - Complete client tutorial
- `docs/sdk.md` - SDK documentation

### Understand Governance
Community files (all ✅ downloaded):
- `community/governance.md` - How MCP is governed
- `community/contributing.md` - How to contribute
- `community/sep-guidelines.md` - Proposal process

## Official MCP Resources

- **Website**: https://modelcontextprotocol.io/
- **GitHub**: https://github.com/modelcontextprotocol/
- **Registry**: https://github.com/modelcontextprotocol/registry
- **Inspector**: https://github.com/modelcontextprotocol/inspector

## Extensions

### Official Extensions
- **ext-apps**: Interactive UI elements - https://github.com/modelcontextprotocol/ext-apps
- **ext-auth**: Authentication mechanisms - https://github.com/modelcontextprotocol/ext-auth

### Experimental Extensions
- **ext-skills**: Skills over MCP (see `experimental/ext-skills.md`)

## MCP SDK Setup

The MCP SDK and examples are in: `/home/zack/dev/mcp-setup/`

See that directory for:
- Installed npm packages (@modelcontextprotocol/sdk, ext-apps)
- Working example servers
- Inspector test scripts

## File Status Legend

- ✅ **Downloaded** - Complete file with all content saved
- 📥 **Pending** - Run download script to fetch

## Notes

- All downloaded files include metadata headers (source URL, download date)
- Files are saved as markdown (.md) format
- The specification is from version 2025-11-25 (latest stable)
- Some pages may contain links to images hosted on modelcontextprotocol.io

## Updating Documentation

To update the documentation in the future:

1. Check for new specification versions at https://modelcontextprotocol.io/specification/
2. Re-run the download script: `python3 download-remaining.py`
3. Check the roadmap: `development/roadmap.md`
4. Monitor new SEPs: `community/seps/index.md`

---

*Archive created: 2026-02-02*
*Protocol version: 2025-11-25*
