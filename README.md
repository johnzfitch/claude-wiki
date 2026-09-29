# Claude Wiki

An unofficial Markdown mirror of Anthropic's Claude documentation: the Claude API platform docs, Claude Code docs, the Help Center, the Model Context Protocol site, Anthropic's news, research, and customer-story pages, and Anthropic's public GitHub cookbooks and plugin docs. Every page is a plain `.md` file with YAML frontmatter, sorted into numbered topic folders, so the whole corpus can be grepped, diffed, indexed for RAG, or fed straight to a model.

Not affiliated with or endorsed by Anthropic.

---

## Layout

| Folder | What's in it |
|--------|--------------|
| [`01-Getting-Started`](./01-Getting-Started/) | Intros, quickstarts, first-run setup |
| [`02-Claude-Code-CLI`](./02-Claude-Code-CLI/) | Claude Code docs: setup, settings, commands, workflows, cloud providers |
| [`03-IDE-Integrations`](./03-IDE-Integrations/) | Claude Code in VS Code, JetBrains, and Chrome |
| [`04-API-Reference`](./04-API-Reference/) | Claude Platform docs: `Endpoints/` (per-SDK API reference), `Admin/`, `Agents-Tools/`, `Guides/`, `About/`, `Test-Evaluate/`, `Other/` |
| [`05-Agent-SDK`](./05-Agent-SDK/) | Agent SDK guides and Python / TypeScript references |
| [`06-MCP-Tools`](./06-MCP-Tools/) | Model Context Protocol: `Spec/` (current and draft), `Spec-Archive/` (older versions), `SEPs/`, `Registry/`, `Extensions/`, `Tutorials/`, `Community/`, `General/` |
| [`07-Hooks`](./07-Hooks/) | Claude Code hooks and hook-related plugin docs |
| [`08-Plugins-Skills`](./08-Plugins-Skills/) | Plugins, Agent Skills, marketplaces, plugin and skill source docs |
| [`09-Agents-Patterns`](./09-Agents-Patterns/) | Subagents, agent design patterns, agent cookbooks |
| [`10-Prompting-Guides`](./10-Prompting-Guides/) | Prompt engineering |
| [`11-RAG-Search`](./11-RAG-Search/) | Retrieval, embeddings, search cookbooks |
| [`12-Eval-Testing`](./12-Eval-Testing/) | Evals, testing, moderation |
| [`13-Enterprise-Admin`](./13-Enterprise-Admin/) | Team / Enterprise administration, identity, security, network and gateway setup |
| [`14-Connectors`](./14-Connectors/) | Connectors directory and integrations |
| [`15-Claude-AI-Features`](./15-Claude-AI-Features/) | claude.ai product features: Projects, Artifacts, memory, Cowork, etc. |
| [`16-Mobile-Desktop`](./16-Mobile-Desktop/) | Desktop and mobile apps |
| [`17-Billing-Plans`](./17-Billing-Plans/) | Plans, pricing, usage limits, invoices |
| [`18-Industry-UseCases`](./18-Industry-UseCases/) | Customer case studies and industry solution pages |
| [`19-Reference`](./19-Reference/) | Anthropic news, research, engineering posts, and converted PDFs (system cards, reports) |
| [`20-Models`](./20-Models/) | Model overviews, choosing a model, deprecations, release notes |
| [`21-Account-Support`](./21-Account-Support/) | Account, login, and troubleshooting articles |
| [`22-Safety-Policy`](./22-Safety-Policy/) | Usage policy, safety, privacy, trust |

Each top-level folder also has:

- `INDEX.md`: its pages, grouped by subfolder, with titles and a one-line excerpt.
- `llms.txt`: every page in the category concatenated into a single file, with each page's title, upstream URL and path, ready to drop into a model's context. `04-API-Reference` is too large for one file, so its `llms.txt` lists one file per subfolder, and `Endpoints/` is split by SDK language (`Endpoints/llms-python.txt`, `Endpoints/llms-typescript.txt`, ...).

### Top-level files

| File | Purpose |
|------|---------|
| [`INDEX.md`](./INDEX.md) | Entry point linking every category index and `llms.txt` |
| [`TAGS.md`](./TAGS.md) | Every page grouped by topic tag |
| [`WHATS-NEW.md`](./WHATS-NEW.md) | Pages added, changed, or removed upstream in the last 7 days |
| [`CHANGELOG.md`](./CHANGELOG.md) | The same for the last 90 days |
| [`wiki/tags.json`](./wiki/tags.json) | `{ tag: [path, ...] }`, the machine-readable form of `TAGS.md` |
| [`wiki/crossrefs.json`](./wiki/crossrefs.json) | `{ path: { outlinks, backlinks, external_links } }`, the internal link graph |
| [`wiki/manifest.json`](./wiki/manifest.json) | `{ source_url: { path, title, category, hash, fetched_at } }` for every page, including alias URLs |
| [`wiki/changelog.json`](./wiki/changelog.json) | The dated change records behind `CHANGELOG.md` |

These files are regenerated on every sync, so they are the place to look for current page counts.

---

## Page format

```markdown
---
title: "Best practices for Claude Code - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/best-practices"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-26T06:38:03Z"
tags: ["claude-code"]
---
...
```

- **`source_url`**: the upstream page. Every page has one.
- **`fetched_at`**: when the copy was captured. Pages matched to their upstream source after capture (mostly cookbook notebooks and plugin files from GitHub) have no `fetched_at`.
- **`last_modified`**: the upstream `Last-Modified` header, when the site sends one. It appears on pages fetched from 2026-09-30 on.
- **One file per upstream page.** When a page was captured more than once, the newest capture is kept. When the same text is served at several URLs (for example `/iam` and `/authentication`), one file is kept and `wiki/manifest.json` lists the other URLs with `alias_of`.
- **Filenames come from the upstream URL path**, so they stay stable when a page's title changes.
- Links between mirrored pages are relative `.md` links; site-relative links to pages that aren't mirrored point at the upstream URL.

---

## Using it

```sh
git clone --depth 1 https://github.com/johnzfitch/claude-wiki.git
cd claude-wiki

# full-text search
grep -rl "prompt caching" --include=*.md .

# everything tagged "hooks"
jq -r '.hooks[]' wiki/tags.json

# which pages link to a given page
jq -r '."05-Agent-SDK/agent-sdk-overview.md".backlinks[]' wiki/crossrefs.json

# where a page came from and when
grep -E '^(source_url|fetched_at):' 02-Claude-Code-CLI/best-practices.md

# the local file for an upstream URL
jq -r '.pages["https://code.claude.com/docs/en/hooks"].path' wiki/manifest.json
```

For quick LLM context on a single topic, use that folder's `llms.txt`. For RAG, chunk on the Markdown headings and keep `title`, `source_url`, and `fetched_at` as metadata so answers can cite the upstream page.

---

## Sources

Pages are pulled from:

- [platform.claude.com](https://platform.claude.com/docs): Claude API / Platform docs
- [code.claude.com](https://code.claude.com/docs): Claude Code and Agent SDK docs
- [support.claude.com](https://support.claude.com): Help Center
- [modelcontextprotocol.io](https://modelcontextprotocol.io): MCP specification and guides
- [anthropic.com](https://www.anthropic.com) and [claude.com](https://www.claude.com): news, research, customer stories, solution pages, PDFs
- GitHub: [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks), [anthropics/claude-code](https://github.com/anthropics/claude-code) plugin docs, and a few other `anthropics` / `modelcontextprotocol` repositories
- [agentskills.io](https://agentskills.io): Agent Skills format docs

A scheduled job checks upstream daily and publishes here, as `Sync docs from upstream` commits, only when something changed. The upstream site is always authoritative; check `fetched_at` to see how current a page is.

---

## License

All documentation content is authored by and belongs to Anthropic and remains under Anthropic's terms. See [`LICENSE`](./LICENSE) and <https://www.anthropic.com/terms>. This mirror exists for offline reading and searchability.
