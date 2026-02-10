# rnetsharp MCP Server Tools

Complete list of 16 tools exposing rnetsharp's capabilities to Claude Code.

## Core Fetching

### fetch
Raw HTTP request with full response data.
- Returns: status, protocol, timing, headers, HTML content
- Use case: When you need raw HTML or full response headers

### batch_fetch
Parallel fetching of multiple URLs efficiently.
- Returns: Results for all URLs with status and timing
- Use case: Downloading multiple pages at once

## Content Extraction

### scrape_text
Clean text extraction from webpages.
- Removes navigation, scripts, styles
- Optional CSS selector for targeted extraction
- Use case: Getting readable article text

### scrape_article
Intelligent article parsing with metadata.
- Extracts: title, author, date, description, body, word count
- Use case: Blog posts, news articles, documentation

### extract_links
All links from a page with absolute URLs.
- Converts relative to absolute URLs
- Returns link text and href
- Use case: Site crawling, link discovery

### extract_emails
Email address harvesting from page content.
- Finds all unique email addresses
- Use case: Contact discovery, lead generation

### extract_forms
Form extraction with fields and actions.
- Returns: action URL, method, field names/types
- Use case: Understanding form structure for automation

### extract_tables
HTML tables as structured data.
- Returns: headers and rows
- Use case: Data extraction from tables

### extract_media
All media files (images, videos, audio).
- Returns: URLs for all media with metadata
- Use case: Media asset discovery

### extract_resources
CSS and JavaScript file URLs.
- Returns: All stylesheet and script URLs
- Use case: Asset enumeration, dependency mapping

### extract_structured_data
Semantic data extraction.
- Extracts: JSON-LD, Open Graph, Twitter Cards
- Use case: Rich metadata, SEO analysis

## Analysis

### detect_tech_stack
Technology and framework detection.
- Detects: CMS (WordPress, Drupal, Shopify)
- Frameworks: React, Vue, Angular, Next.js
- Analytics: Google Analytics, Facebook Pixel
- Libraries: jQuery, Bootstrap, Tailwind
- Servers: nginx, Apache, Cloudflare
- Use case: Competitive analysis, tech research

### check_performance
Page performance analysis.
- Returns: connect time, TTFB, total time
- Content size, protocol metrics
- Use case: Performance monitoring, optimization

## Advanced Operations

### crawl_site
Recursive site crawling for directory enumeration.
- Follows same-domain links only
- Configurable max depth (1-5)
- Returns: All discovered URLs with structure
- Use case: Site mapping, content discovery

### download_file
File downloads (PDFs, images, archives).
- Saves to disk automatically
- Generates filename from URL if not provided
- Use case: Downloading documents, media files

### post_data
POST requests with JSON or form data.
- Custom headers and content types
- Returns: response body and headers
- Use case: API calls, form submissions

## All Tools Use rnetsharp Features

Every tool automatically gets:
- **Browser fingerprinting** - Chrome 142, Firefox 133, Safari 18
- **HTTP/2 + HTTP/3** - Automatic protocol selection
- **Cookie management** - Persistent across requests
- **Human-like timing** - Built into BrowserIdentity
- **Alt-Svc learning** - Protocol optimization over time

## Usage Patterns

### Single Page Analysis
```python
# Get everything about a page
{
  "scrape_article": url,
  "extract_links": url,
  "extract_media": url,
  "detect_tech_stack": url,
  "check_performance": url
}
```

### Site Mapping
```python
# Discover site structure
{
  "crawl_site": {
    "url": base_url,
    "max_depth": 3
  }
}
```

### Data Extraction
```python
# Extract structured data
{
  "extract_forms": url,      # Form fields
  "extract_tables": url,     # Table data
  "extract_emails": url,     # Contact info
}
```

### Competitive Research
```python
{
  "detect_tech_stack": competitor_url,
  "extract_resources": competitor_url,  # See their libraries
  "check_performance": competitor_url   # Compare speed
}
```

## Configuration

All tools accept optional `browser` parameter:
- `"chrome"` (default) - Chrome 142 fingerprint
- `"firefox"` - Firefox 133 fingerprint
- `"safari"` - Safari 18 fingerprint

The Controller maintains state across requests:
- Cookie jar persisted
- Protocol database learned
- Metrics collected
- Health monitored

## Installation

Run: `./mcp/install.sh`

Then add to `~/.claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "rnetsharp": {
      "command": "/home/zack/dev/rnetsharp/.venv/bin/python",
      "args": ["/home/zack/dev/rnetsharp/mcp/server.py"]
    }
  }
}
```

Restart Claude Code.
