# Claude Wiki

Comprehensive unofficial mirror of Anthropic's Claude ecosystem documentation — 1,543 Markdown articles across 22 categories, sourced daily from [docs.anthropic.com](https://docs.anthropic.com), [support.anthropic.com](https://support.anthropic.com), and [docs.claude.ai](https://docs.claude.ai).

Covers the full Claude platform: API reference, Claude Code CLI, Model Context Protocol (MCP), Agent SDK, hooks, plugins, prompting guides, enterprise administration, safety & policy, billing, and model specifications. Every article is plain Markdown with YAML frontmatter — ready for grep, RAG pipelines, or direct LLM ingestion via `llms.txt`.

Not affiliated with Anthropic.

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

<!-- CATEGORY_TABLE_START -->
| Category | Docs | Folder |
|----------|-----:|--------|
| Getting Started | 16 | [`01-Getting-Started`](./01-Getting-Started/) |
| Claude Code CLI | 57 | [`02-Claude-Code-CLI`](./02-Claude-Code-CLI/) |
| IDE Integrations | 5 | [`03-IDE-Integrations`](./03-IDE-Integrations/) |
| API Reference | 24 | [`04-API-Reference`](./04-API-Reference/) |
| Agent SDK | 35 | [`05-Agent-SDK`](./05-Agent-SDK/) |
| MCP Tools | 302 | [`06-MCP-Tools`](./06-MCP-Tools/) |
| Hooks | 17 | [`07-Hooks`](./07-Hooks/) |
| Plugins & Skills | 75 | [`08-Plugins-Skills`](./08-Plugins-Skills/) |
| Agent Patterns | 32 | [`09-Agents-Patterns`](./09-Agents-Patterns/) |
| Prompting Guides | 18 | [`10-Prompting-Guides`](./10-Prompting-Guides/) |
| RAG & Search | 17 | [`11-RAG-Search`](./11-RAG-Search/) |
| Eval & Testing | 5 | [`12-Eval-Testing`](./12-Eval-Testing/) |
| Enterprise Admin | 29 | [`13-Enterprise-Admin`](./13-Enterprise-Admin/) |
| Connectors | 30 | [`14-Connectors`](./14-Connectors/) |
| Claude AI Features | 283 | [`15-Claude-AI-Features`](./15-Claude-AI-Features/) |
| Mobile & Desktop | 11 | [`16-Mobile-Desktop`](./16-Mobile-Desktop/) |
| Billing & Plans | 63 | [`17-Billing-Plans`](./17-Billing-Plans/) |
| 18-Skills | 6 | [`18-Skills`](./18-Skills/) |
| Reference | 361 | [`19-Reference`](./19-Reference/) |
| Models | 78 | [`20-Models`](./20-Models/) |
| Account & Support | 35 | [`21-Account-Support`](./21-Account-Support/) |
| Safety & Policy | 44 | [`22-Safety-Policy`](./22-Safety-Policy/) |
<!-- CATEGORY_TABLE_END -->

<details>
<summary>Largest categories by doc count</summary>

<!-- LARGEST_CATEGORIES_START -->
1. **Reference** (361)
2. **MCP Tools** (302)
3. **Claude AI Features** (283)
4. **Models** (78)
5. **Plugins & Skills** (75)
<!-- LARGEST_CATEGORIES_END -->

</details>

---

## Upstream Sources

This repo mirrors content from Anthropic's official documentation:

- [docs.anthropic.com](https://docs.anthropic.com) — API docs, guides, SDK references
- [support.anthropic.com](https://support.anthropic.com) — Help center, account, billing
- [docs.claude.ai](https://docs.claude.ai) — Claude Code, MCP, hooks

Content is fetched, converted to Markdown, and organized into numbered categories by an automated pipeline. A public-repo normalization pass then quarantines low-confidence files such as local-only prompts, placeholder captures, empty stubs, and uncurated `99-Other` artifacts into `meta/quarantine/`.

## Releases

Weekly [releases](https://github.com/johnzfitch/claude-wiki/releases) include:

| Asset | Description |
|-------|-------------|
| `llms.txt` | Tiered document outline for LLM context windows |
| `claude-wiki-llmx.zip` | Full LLMX search bundle (offline semantic search) |

## License

This repo contains documentation authored by Anthropic. All content remains under Anthropic's original terms. This mirror is provided for convenience and searchability.
