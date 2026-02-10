# MCP Documentation Index

Complete catalog of Model Context Protocol documentation downloaded to this directory.

**Total Files**: 87 official pages + extensions
**Last Updated**: 2026-02-02
**Source**: https://modelcontextprotocol.io/

## Directory Structure

```
mcp-docs/
├── clients.md
├── examples.md
├── extensions.md
├── community/
│   ├── antitrust.md
│   ├── communication.md
│   ├── contributing.md
│   ├── governance.md
│   ├── sep-guidelines.md
│   ├── working-interest-groups.md
│   └── seps/
│       ├── index.md
│       └── [26 SEP files]
├── development/
│   └── roadmap.md
├── docs/
│   ├── sdk.md
│   ├── develop/
│   │   ├── build-client.md
│   │   ├── build-server.md
│   │   ├── connect-local-servers.md
│   │   └── connect-remote-servers.md
│   ├── extensions/
│   │   └── apps.md
│   ├── getting-started/
│   │   └── intro.md
│   ├── learn/
│   │   ├── architecture.md
│   │   ├── client-concepts.md
│   │   └── server-concepts.md
│   ├── tools/
│   │   └── inspector.md
│   └── tutorials/
│       └── security/
│           └── authorization.md
├── experimental/
│   └── ext-skills.md
├── registry/
│   ├── about.md
│   ├── authentication.md
│   ├── faq.md
│   ├── github-actions.md
│   ├── moderation-policy.md
│   ├── package-types.md
│   ├── quickstart.md
│   ├── registry-aggregators.md
│   ├── remote-servers.md
│   ├── terms-of-service.md
│   └── versioning.md
└── specification/
    ├── versioning.md
    └── 2025-11-25/
        ├── index.md
        ├── changelog.md
        ├── schema.md
        ├── architecture/
        │   └── index.md
        ├── basic/
        │   ├── index.md
        │   ├── authorization.md
        │   ├── lifecycle.md
        │   ├── security_best_practices.md
        │   ├── transports.md
        │   └── utilities/
        │       ├── cancellation.md
        │       ├── ping.md
        │       ├── progress.md
        │       └── tasks.md
        ├── client/
        │   ├── elicitation.md
        │   ├── roots.md
        │   └── sampling.md
        └── server/
            ├── index.md
            ├── prompts.md
            ├── resources.md
            ├── tools.md
            └── utilities/
                ├── completion.md
                ├── logging.md
                └── pagination.md
```

## Quick Links by Category

### 🚀 Getting Started
- [Introduction](docs/getting-started/intro.md) - What is MCP?
- [Build a Server](docs/develop/build-server.md) - Server development guide
- [Build a Client](docs/develop/build-client.md) - Client development guide
- [Connect Local Servers](docs/develop/connect-local-servers.md)
- [Connect Remote Servers](docs/develop/connect-remote-servers.md)

### 📖 Core Concepts
- [Architecture](docs/learn/architecture.md) - System overview
- [Server Concepts](docs/learn/server-concepts.md) - Understanding servers
- [Client Concepts](docs/learn/client-concepts.md) - Understanding clients

### 📋 Specification (2025-11-25)
- [Overview](specification/2025-11-25/index.md)
- [Architecture](specification/2025-11-25/architecture/index.md)
- [Base Protocol](specification/2025-11-25/basic/index.md)
- [Authorization](specification/2025-11-25/basic/authorization.md)
- [Lifecycle](specification/2025-11-25/basic/lifecycle.md)
- [Security Best Practices](specification/2025-11-25/basic/security_best_practices.md)
- [Transports](specification/2025-11-25/basic/transports.md)
- [Schema Reference](specification/2025-11-25/schema.md)
- [Changelog](specification/2025-11-25/changelog.md)

#### Server Features
- [Server Overview](specification/2025-11-25/server/index.md)
- [Tools](specification/2025-11-25/server/tools.md)
- [Resources](specification/2025-11-25/server/resources.md)
- [Prompts](specification/2025-11-25/server/prompts.md)
- [Logging](specification/2025-11-25/server/utilities/logging.md)
- [Completion](specification/2025-11-25/server/utilities/completion.md)
- [Pagination](specification/2025-11-25/server/utilities/pagination.md)

#### Client Features
- [Elicitation](specification/2025-11-25/client/elicitation.md)
- [Roots](specification/2025-11-25/client/roots.md)
- [Sampling](specification/2025-11-25/client/sampling.md)

#### Utilities
- [Cancellation](specification/2025-11-25/basic/utilities/cancellation.md)
- [Ping](specification/2025-11-25/basic/utilities/ping.md)
- [Progress](specification/2025-11-25/basic/utilities/progress.md)
- [Tasks](specification/2025-11-25/basic/utilities/tasks.md)

### 🔧 Tools & Development
- [SDK Documentation](docs/sdk.md)
- [MCP Inspector](docs/tools/inspector.md)
- [Example Implementations](examples.md)
- [Client Applications](clients.md)

### 🔐 Security
- [Authorization Tutorial](docs/tutorials/security/authorization.md)
- [Security Best Practices](specification/2025-11-25/basic/security_best_practices.md)

### 🎨 Extensions
- [Extensions Overview](extensions.md)
- [MCP Apps](docs/extensions/apps.md) - Interactive UI extension
- [Experimental: Skills](experimental/ext-skills.md) - Skills over MCP IG

### 📦 MCP Registry
- [About](registry/about.md)
- [Quickstart](registry/quickstart.md)
- [Authentication](registry/authentication.md)
- [Package Types](registry/package-types.md)
- [Versioning](registry/versioning.md)
- [GitHub Actions](registry/github-actions.md)
- [FAQ](registry/faq.md)
- [Moderation Policy](registry/moderation-policy.md)
- [Aggregators](registry/registry-aggregators.md)
- [Remote Servers](registry/remote-servers.md)
- [Terms of Service](registry/terms-of-service.md)

### 🏛️ Governance & Community
- [Governance](community/governance.md)
- [Contributing](community/contributing.md)
- [Working & Interest Groups](community/working-interest-groups.md)
- [Communication Guidelines](community/communication.md)
- [Antitrust Policy](community/antitrust.md)
- [SEP Guidelines](community/sep-guidelines.md)
- [Development Roadmap](development/roadmap.md)

### 📜 Specification Enhancement Proposals (SEPs)
All SEPs are in [`community/seps/`](community/seps/)

Key SEPs:
- [SEP Index](community/seps/index.md)
- [SEP-932: Governance](community/seps/932-model-context-protocol-governance.md)
- [SEP-1865: MCP Apps](community/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp.md)
- [SEP-2133: Extensions](community/seps/2133-extensions.md)
- [SEP-1686: Tasks](community/seps/1686-tasks.md)
- [SEP-1730: SDK Tiering](community/seps/1730-sdks-tiering-system.md)

## Download Tools

### Python Script
Run `python3 download-remaining.py` to download any remaining files not yet fetched.

### Requirements
```bash
pip install requests
```

## Official Resources

- **Website**: https://modelcontextprotocol.io/
- **GitHub Org**: https://github.com/modelcontextprotocol/
- **Specification Repo**: https://github.com/modelcontextprotocol/specification
- **Registry**: https://github.com/modelcontextprotocol/registry
- **Inspector**: https://github.com/modelcontextprotocol/inspector

## Extension Repositories

- **ext-apps**: https://github.com/modelcontextprotocol/ext-apps
- **ext-auth**: https://github.com/modelcontextprotocol/ext-auth
- **experimental-ext-skills**: https://github.com/modelcontextprotocol/experimental-ext-skills

## SDK Repositories

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk
- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

---

*Documentation snapshot as of 2026-02-02*
