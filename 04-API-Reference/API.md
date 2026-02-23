# claude-wiki API Documentation

## CLI Reference

### discover_claude_sources.py

Discover documentation URLs from sitemaps, crawlers, and seed lists.

```bash
python3 tools/discover_claude_sources.py \
  --out sources/sources.discovered.jsonl \
  --sources-dir sources/
```

**Options:**
- `--out PATH` (required): Output JSONL file path
- `--sources-dir PATH`: Directory containing *.seed.jsonl files

**Output Format:**
```jsonl
{"url": "https://...", "category": "04-API-Reference", "kind": "html", "title_hint": "..."}
```

---

### update_claude_docs.py

Fetch and convert sources to markdown, manage state, rebuild index.

```bash
# Fetch all sources
python3 tools/update_claude_docs.py fetch --concurrency 20 --delay 0.3

# Rebuild index only
python3 tools/update_claude_docs.py index

# Show recent changes
python3 tools/update_claude_docs.py changes

# Check archivable docs
python3 tools/update_claude_docs.py archive-check
python3 tools/update_claude_docs.py archive-check --apply
```

**Commands:**
- `update`: Run full pipeline (discover + fetch + index)
- `fetch`: Fetch and convert sources
- `index`: Rebuild manifest.tsv and index.md
- `changes`: Show stats from last run
- `archive-check`: Check/archive removed docs

**Fetch Options:**
- `--concurrency N`: Parallel requests (default: 20)
- `--delay SECONDS`: Per-domain delay (default: 0.3)

---

### validate_docs.py

Validate documentation format and metadata.

```bash
python3 tools/validate_docs.py --check-yaml --check-markdown --check-urls --sample 10
```

**Options:**
- `--check-yaml`: Validate YAML front matter
- `--check-markdown`: Check markdown format
- `--check-urls`: Verify source URLs accessible
- `--sample N`: Sample size for URL checks

---

### check_links.py

Find broken external links in documentation.

```bash
python3 tools/check_links.py --sample 50
```

**Options:**
- `--sample N`: Check only N random docs

---

### benchmark.py

Benchmark HTTP and Pandoc performance.

```bash
python3 tools/benchmark.py --iterations 10
```

**Options:**
- `--iterations N`: Number of test iterations

---

## Python API Examples

### Using Discovery Functions

```python
from tools.update_claude_docs import classify_link, normalize_link, should_traverse

# Classify a URL
result = classify_link("https://platform.claude.com/docs/api-reference")
# Returns: {"url": "...", "category": "04-API-Reference", "kind": "html"}

# Normalize a relative link
base = "https://support.claude.com/en/"
normalized = normalize_link("../articles/123", base)
# Returns: "https://support.claude.com/articles/123"

# Check if URL should be crawled
should_crawl = should_traverse("https://support.claude.com/en/articles/123")
# Returns: True
```

### Using Hash Functions

```python
from tools.update_claude_docs import sha256_bytes, sha256_bytes_incremental

# Standard hashing
data = b"hello world"
hash_val = sha256_bytes(data)

# Incremental hashing for large files
large_data = b"x" * (200 * 1024)
hash_val, is_incremental = sha256_bytes_incremental(large_data)
# Returns: (hash, True) for files > 100KB
```

### Reading State Files

```python
import json
from pathlib import Path

state_dir = Path("state")

for state_file in state_dir.glob("*.json"):
    state = json.loads(state_file.read_text())

    url = state["url"]
    doc_path = state["doc"]
    content_hash = state["content_hash"]
    fetched_at = state["fetched_at"]

    # Optional fields
    etag = state.get("etag")
    last_modified = state.get("last_modified")
    archived_at = state.get("archived_at")
```

---

## Data Format Reference

### Sources JSONL

File: `sources/sources.discovered.jsonl`

```jsonl
{"url": "https://...", "category": "04-API-Reference", "kind": "html", "title_hint": "Optional Title"}
```

**Fields:**
- `url` (string, required): Source URL
- `category` (string, required): Category (01-24 or 99-Other)
- `kind` (string, required): "html" or "pdf"
- `title_hint` (string, optional): Suggested title

---

### State JSON

File: `state/<sha256>.json`

```json
{
  "url": "https://...",
  "content_hash": "abc123...",
  "incremental_hash": false,
  "doc": "docs/04-API-Reference/doc-abc123.md",
  "title": "Doc Title",
  "fetched_at": "2025-01-15T12:00:00Z",
  "last_modified": "Wed, 15 Jan 2025 12:00:00 GMT",
  "etag": "\"abc123\"",
  "archived_at": "2025-02-01T10:00:00Z",
  "archived_reason": "source_removed"
}
```

**Fields:**
- `url`: Source URL
- `content_hash`: SHA-256 hash of content
- `incremental_hash`: Boolean, true if incremental hash used
- `doc`: Relative path to markdown file
- `title`: Document title
- `fetched_at`: ISO 8601 timestamp
- `last_modified`: HTTP Last-Modified header
- `etag`: HTTP ETag header
- `archived_at`: When doc was archived (optional)
- `archived_reason`: Why doc was archived (optional)

---

### Markdown Front Matter

```yaml
---
source_url: "https://..."
category: "04-API-Reference"
title: "Document Title"
fetched_at: "2025-01-15T12:00:00Z"
last_modified: "Wed, 15 Jan 2025 12:00:00 GMT"
---

Document content here...
```

**Required Fields:**
- `source_url`: Original URL
- `category`: Category (01-24 or 99-Other)

**Optional Fields:**
- `title`: Document title
- `fetched_at`: Fetch timestamp
- `last_modified`: HTTP Last-Modified value

---

## Event Hooks API

*Note: Event hooks are not yet implemented but planned for future releases.*

Proposed hook points:
- `pre-fetch`: Before fetching a URL
- `post-fetch`: After successful fetch
- `pre-convert`: Before Pandoc conversion
- `post-convert`: After Pandoc conversion
- `pre-archive`: Before archiving a doc
- `post-archive`: After archiving a doc

Example:
```bash
# ~/.config/claude-wiki/hooks/post-fetch
#!/bin/bash
# Custom processing after each fetch
url="$1"
status="$2"
echo "Fetched: $url ($status)"
```

---

## Performance Tips

1. **HTTP Conditional Requests**:
   - Re-running fetch uses ETags and Last-Modified headers
   - Expect 70-90% cache hit rate on repeat runs

2. **Parallel Fetching**:
   - Default concurrency: 20
   - Increase for faster fetches: `--concurrency 50`
   - Decrease if hitting rate limits: `--concurrency 5`

3. **Rate Limiting**:
   - Default delay: 0.3s per domain
   - Increase for strict servers: `--delay 1.0`
   - Controlled via `CLAUDE_WIKI_DELAY` env var

4. **Incremental Hashing**:
   - Automatically used for files > 100KB
   - First/last 8KB + filesize as quick hash
   - Full hash computed only on mismatch

---

## Troubleshooting

### Import Errors

```python
# Add tools to path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "tools"))

from update_claude_docs import classify_link
```

### Missing Dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### Rate Limiting (429 errors)

```bash
# Increase delay, reduce concurrency
python3 tools/update_claude_docs.py fetch --concurrency 10 --delay 1.0
```
