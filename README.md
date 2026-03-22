# Claude Wiki

Unofficial mirror of Anthropic's Claude documentation — 2,303 Markdown articles across 23 categories, sourced from [docs.anthropic.com](https://docs.anthropic.com), [support.anthropic.com](https://support.anthropic.com), and related Anthropic properties.

Updated weekly. Not affiliated with Anthropic.

---

## For LLMs

Grab [`llms.txt`](./llms.txt) for a structured outline of every document in this repo, or download the full [LLMX search bundle](https://github.com/johnzfitch/claude-wiki/releases/latest) from releases.

```
# Fetch the outline
curl -sL https://raw.githubusercontent.com/johnzfitch/claude-wiki/master/llms.txt

# Download the latest LLMX bundle
gh release download --repo johnzfitch/claude-wiki -p 'claude-wiki-llmx.zip'
```

## For Humans

Every doc is plain Markdown with YAML frontmatter. Browse the folders below or search locally:

<kbd>Ctrl</kbd>+<kbd>F</kbd> in any folder, or clone and grep:

```bash
# Search everything
grep -ri "tool use" */

# Search one category
grep -ri "streaming" 04-API-Reference/

# Find docs by title
find . -name '*.md' | grep -i "prompt"
```

---

## Categories

| Category | Docs | Folder |
|----------|-----:|--------|
| Getting Started | 21 | [`01-Getting-Started`](./01-Getting-Started/) |
| Claude Code CLI | 53 | [`02-Claude-Code-CLI`](./02-Claude-Code-CLI/) |
| IDE Integrations | 5 | [`03-IDE-Integrations`](./03-IDE-Integrations/) |
| API Reference | 329 | [`04-API-Reference`](./04-API-Reference/) |
| Agent SDK | 35 | [`05-Agent-SDK`](./05-Agent-SDK/) |
| MCP Tools | 409 | [`06-MCP-Tools`](./06-MCP-Tools/) |
| Hooks | 15 | [`07-Hooks`](./07-Hooks/) |
| Plugins & Skills | 73 | [`08-Plugins-Skills`](./08-Plugins-Skills/) |
| Agent Patterns | 34 | [`09-Agents-Patterns`](./09-Agents-Patterns/) |
| Prompting Guides | 82 | [`10-Prompting-Guides`](./10-Prompting-Guides/) |
| RAG & Search | 17 | [`11-RAG-Search`](./11-RAG-Search/) |
| Eval & Testing | 6 | [`12-Eval-Testing`](./12-Eval-Testing/) |
| Enterprise Admin | 23 | [`13-Enterprise-Admin`](./13-Enterprise-Admin/) |
| Connectors | 30 | [`14-Connectors`](./14-Connectors/) |
| Claude AI Features | 627 | [`15-Claude-AI-Features`](./15-Claude-AI-Features/) |
| Mobile & Desktop | 21 | [`16-Mobile-Desktop`](./16-Mobile-Desktop/) |
| Billing & Plans | 52 | [`17-Billing-Plans`](./17-Billing-Plans/) |
| Reference | 339 | [`19-Reference`](./19-Reference/) |
| Models | 72 | [`20-Models`](./20-Models/) |
| Account & Support | 27 | [`21-Account-Support`](./21-Account-Support/) |
| Safety & Policy | 32 | [`22-Safety-Policy`](./22-Safety-Policy/) |

<details>
<summary>Largest categories by doc count</summary>

1. **Claude AI Features** (627) — Projects, artifacts, analysis, canvas, conversations
2. **MCP Tools** (409) — Model Context Protocol servers, integrations, tooling
3. **Reference** (339) — API specs, schemas, error codes, SDKs
4. **API Reference** (329) — REST endpoints, parameters, authentication
5. **Prompting Guides** (82) — Prompt engineering, system prompts, best practices

</details>

---

## Upstream Sources

This repo mirrors content from Anthropic's official documentation:

- [docs.anthropic.com](https://docs.anthropic.com) — API docs, guides, SDK references
- [support.anthropic.com](https://support.anthropic.com) — Help center, account, billing
- [docs.claude.ai](https://docs.claude.ai) — Claude Code, MCP, hooks

Content is fetched, converted to Markdown via Pandoc, and organized into numbered categories. See the [private repo](https://github.com/johnzfitch/claude-wiki) tooling for details on the pipeline.

## Releases

Weekly [releases](https://github.com/johnzfitch/claude-wiki/releases) include:

| Asset | Description |
|-------|-------------|
| `llms.txt` | Tiered document outline for LLM context windows |
| `claude-wiki-llmx.zip` | Full LLMX search bundle (offline semantic search) |

## License

This repo contains documentation authored by Anthropic. All content remains under Anthropic's original terms. This mirror is provided for convenience and searchability.
