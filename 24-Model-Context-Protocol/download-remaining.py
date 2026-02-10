#!/usr/bin/env python3
"""
MCP Documentation Downloader
Downloads all remaining MCP documentation pages systematically
"""

import requests
import time
from pathlib import Path
from datetime import datetime

# Base directory
BASE_DIR = Path("/home/zack/Documents/mcp-docs")

# Remaining URLs to download
URLS = [
    # SEPs (24 remaining)
    ("community/seps/932-model-context-protocol-governance.md", "https://modelcontextprotocol.io/community/seps/932-model-context-protocol-governance.md"),
    ("community/seps/973-expose-additional-metadata-for-implementations-res.md", "https://modelcontextprotocol.io/community/seps/973-expose-additional-metadata-for-implementations-res.md"),
    ("community/seps/985-align-oauth-20-protected-resource-metadata-with-rf.md", "https://modelcontextprotocol.io/community/seps/985-align-oauth-20-protected-resource-metadata-with-rf.md"),
    ("community/seps/986-specify-format-for-tool-names.md", "https://modelcontextprotocol.io/community/seps/986-specify-format-for-tool-names.md"),
    ("community/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md", "https://modelcontextprotocol.io/community/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md"),
    ("community/seps/991-enable-url-based-client-registration-using-oauth-c.md", "https://modelcontextprotocol.io/community/seps/991-enable-url-based-client-registration-using-oauth-c.md"),
    ("community/seps/994-shared-communication-practicesguidelines.md", "https://modelcontextprotocol.io/community/seps/994-shared-communication-practicesguidelines.md"),
    ("community/seps/1024-mcp-client-security-requirements-for-local-server-.md", "https://modelcontextprotocol.io/community/seps/1024-mcp-client-security-requirements-for-local-server-.md"),
    ("community/seps/1034--support-default-values-for-all-primitive-types-in.md", "https://modelcontextprotocol.io/community/seps/1034--support-default-values-for-all-primitive-types-in.md"),
    ("community/seps/1036-url-mode-elicitation-for-secure-out-of-band-intera.md", "https://modelcontextprotocol.io/community/seps/1036-url-mode-elicitation-for-secure-out-of-band-intera.md"),
    ("community/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md", "https://modelcontextprotocol.io/community/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md"),
    ("community/seps/1302-formalize-working-groups-and-interest-groups-in-mc.md", "https://modelcontextprotocol.io/community/seps/1302-formalize-working-groups-and-interest-groups-in-mc.md"),
    ("community/seps/1303-input-validation-errors-as-tool-execution-errors.md", "https://modelcontextprotocol.io/community/seps/1303-input-validation-errors-as-tool-execution-errors.md"),
    ("community/seps/1319-decouple-request-payload-from-rpc-methods-definiti.md", "https://modelcontextprotocol.io/community/seps/1319-decouple-request-payload-from-rpc-methods-definiti.md"),
    ("community/seps/1330-elicitation-enum-schema-improvements-and-standards.md", "https://modelcontextprotocol.io/community/seps/1330-elicitation-enum-schema-improvements-and-standards.md"),
    ("community/seps/1577--sampling-with-tools.md", "https://modelcontextprotocol.io/community/seps/1577--sampling-with-tools.md"),
    ("community/seps/1613-establish-json-schema-2020-12-as-default-dialect-f.md", "https://modelcontextprotocol.io/community/seps/1613-establish-json-schema-2020-12-as-default-dialect-f.md"),
    ("community/seps/1686-tasks.md", "https://modelcontextprotocol.io/community/seps/1686-tasks.md"),
    ("community/seps/1699-support-sse-polling-via-server-side-disconnect.md", "https://modelcontextprotocol.io/community/seps/1699-support-sse-polling-via-server-side-disconnect.md"),
    ("community/seps/1730-sdks-tiering-system.md", "https://modelcontextprotocol.io/community/seps/1730-sdks-tiering-system.md"),
    ("community/seps/1850-pr-based-sep-workflow.md", "https://modelcontextprotocol.io/community/seps/1850-pr-based-sep-workflow.md"),
    ("community/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp.md", "https://modelcontextprotocol.io/community/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp.md"),
    ("community/seps/2085-governance-succession-and-amendment.md", "https://modelcontextprotocol.io/community/seps/2085-governance-succession-and-amendment.md"),
    ("community/seps/2133-extensions.md", "https://modelcontextprotocol.io/community/seps/2133-extensions.md"),

    # Tools & Extensions (2)
    ("docs/tools/inspector.md", "https://modelcontextprotocol.io/docs/tools/inspector.md"),
    ("docs/extensions/apps.md", "https://modelcontextprotocol.io/docs/extensions/apps.md"),
    ("docs/tutorials/security/authorization.md", "https://modelcontextprotocol.io/docs/tutorials/security/authorization.md"),

    # Registry (11)
    ("registry/about.md", "https://modelcontextprotocol.io/registry/about.md"),
    ("registry/authentication.md", "https://modelcontextprotocol.io/registry/authentication.md"),
    ("registry/faq.md", "https://modelcontextprotocol.io/registry/faq.md"),
    ("registry/github-actions.md", "https://modelcontextprotocol.io/registry/github-actions.md"),
    ("registry/moderation-policy.md", "https://modelcontextprotocol.io/registry/moderation-policy.md"),
    ("registry/package-types.md", "https://modelcontextprotocol.io/registry/package-types.md"),
    ("registry/quickstart.md", "https://modelcontextprotocol.io/registry/quickstart.md"),
    ("registry/registry-aggregators.md", "https://modelcontextprotocol.io/registry/registry-aggregators.md"),
    ("registry/remote-servers.md", "https://modelcontextprotocol.io/registry/remote-servers.md"),
    ("registry/terms-of-service.md", "https://modelcontextprotocol.io/registry/terms-of-service.md"),
    ("registry/versioning.md", "https://modelcontextprotocol.io/registry/versioning.md"),

    # Specification (27)
    ("specification/2025-11-25/index.md", "https://modelcontextprotocol.io/specification/2025-11-25/index.md"),
    ("specification/2025-11-25/architecture/index.md", "https://modelcontextprotocol.io/specification/2025-11-25/architecture/index.md"),
    ("specification/2025-11-25/basic/index.md", "https://modelcontextprotocol.io/specification/2025-11-25/basic/index.md"),
    ("specification/2025-11-25/basic/authorization.md", "https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization.md"),
    ("specification/2025-11-25/basic/lifecycle.md", "https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle.md"),
    ("specification/2025-11-25/basic/security_best_practices.md", "https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices.md"),
    ("specification/2025-11-25/basic/transports.md", "https://modelcontextprotocol.io/specification/2025-11-25/basic/transports.md"),
    ("specification/2025-11-25/basic/utilities/cancellation.md", "https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/cancellation.md"),
    ("specification/2025-11-25/basic/utilities/ping.md", "https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/ping.md"),
    ("specification/2025-11-25/basic/utilities/progress.md", "https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/progress.md"),
    ("specification/2025-11-25/basic/utilities/tasks.md", "https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks.md"),
    ("specification/2025-11-25/client/elicitation.md", "https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation.md"),
    ("specification/2025-11-25/client/roots.md", "https://modelcontextprotocol.io/specification/2025-11-25/client/roots.md"),
    ("specification/2025-11-25/client/sampling.md", "https://modelcontextprotocol.io/specification/2025-11-25/client/sampling.md"),
    ("specification/2025-11-25/server/index.md", "https://modelcontextprotocol.io/specification/2025-11-25/server/index.md"),
    ("specification/2025-11-25/server/prompts.md", "https://modelcontextprotocol.io/specification/2025-11-25/server/prompts.md"),
    ("specification/2025-11-25/server/resources.md", "https://modelcontextprotocol.io/specification/2025-11-25/server/resources.md"),
    ("specification/2025-11-25/server/tools.md", "https://modelcontextprotocol.io/specification/2025-11-25/server/tools.md"),
    ("specification/2025-11-25/server/utilities/completion.md", "https://modelcontextprotocol.io/specification/2025-11-25/server/utilities/completion.md"),
    ("specification/2025-11-25/server/utilities/logging.md", "https://modelcontextprotocol.io/specification/2025-11-25/server/utilities/logging.md"),
    ("specification/2025-11-25/server/utilities/pagination.md", "https://modelcontextprotocol.io/specification/2025-11-25/server/utilities/pagination.md"),
    ("specification/2025-11-25/schema.md", "https://modelcontextprotocol.io/specification/2025-11-25/schema.md"),
    ("specification/2025-11-25/changelog.md", "https://modelcontextprotocol.io/specification/2025-11-25/changelog.md"),
    ("specification/versioning.md", "https://modelcontextprotocol.io/specification/versioning.md"),
]

def download_file(local_path, url, retry=3):
    """Download a single file with retry logic"""
    full_path = BASE_DIR / local_path
    full_path.parent.mkdir(parents=True, exist_ok=True)

    for attempt in range(retry):
        try:
            print(f"Downloading: {url}")
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            # Add metadata header
            content = f"""---
source: {url}
downloaded: {datetime.now().isoformat()}
---

{response.text}
"""

            full_path.write_text(content, encoding='utf-8')
            print(f"✓ Saved to: {local_path}")
            return True

        except Exception as e:
            print(f"✗ Attempt {attempt + 1} failed: {e}")
            if attempt < retry - 1:
                time.sleep(2 ** attempt)  # Exponential backoff

    return False

def main():
    """Main download function"""
    print(f"Starting download of {len(URLS)} files...")
    print(f"Target directory: {BASE_DIR}\n")

    success_count = 0
    failed = []

    for i, (local_path, url) in enumerate(URLS, 1):
        print(f"\n[{i}/{len(URLS)}] ", end="")

        if download_file(local_path, url):
            success_count += 1
        else:
            failed.append((local_path, url))

        # Rate limiting
        time.sleep(0.5)

    # Summary
    print(f"\n{'='*60}")
    print(f"Download complete!")
    print(f"Successful: {success_count}/{len(URLS)}")

    if failed:
        print(f"\nFailed downloads ({len(failed)}):")
        for path, url in failed:
            print(f"  - {path}")

    print(f"\nAll files saved to: {BASE_DIR}")

if __name__ == "__main__":
    main()
