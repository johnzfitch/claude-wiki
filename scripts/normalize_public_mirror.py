#!/usr/bin/env python3
"""Normalize the public mirror after docs are synced in."""

from __future__ import annotations

import json
import os
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUARANTINE_ROOT = ROOT / "meta" / "quarantine"
REPORT_JSON = ROOT / "meta" / "public-cleanup-report.json"
REPORT_MD = ROOT / "meta" / "public-cleanup-report.md"
README_PATH = ROOT / "README.md"

CATEGORY_LABELS = {
    "01-Getting-Started": "Getting Started",
    "02-Claude-Code-CLI": "Claude Code CLI",
    "03-IDE-Integrations": "IDE Integrations",
    "04-API-Reference": "API Reference",
    "05-Agent-SDK": "Agent SDK",
    "05-Skills": "Skills",
    "06-MCP-Tools": "MCP Tools",
    "07-Hooks": "Hooks",
    "08-Plugins-Skills": "Plugins & Skills",
    "09-Agents-Patterns": "Agent Patterns",
    "10-Prompting-Guides": "Prompting Guides",
    "11-RAG-Search": "RAG & Search",
    "12-Eval-Testing": "Eval & Testing",
    "13-Enterprise-Admin": "Enterprise Admin",
    "14-Connectors": "Connectors",
    "15-Claude-AI-Features": "Claude AI Features",
    "16-Mobile-Desktop": "Mobile & Desktop",
    "17-Billing-Plans": "Billing & Plans",
    "18-Integrations": "Integrations",
    "18-Industry-UseCases": "Industry Use Cases",
    "19-Reference": "Reference",
    "20-Models": "Models",
    "21-Account-Support": "Account & Support",
    "22-Safety-Policy": "Safety & Policy",
    "23-General-FAQ": "General FAQ",
    "99-Other": "Other",
}


def iter_category_dirs() -> list[Path]:
    """Return public category directories."""
    return sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir() and re.match(r"^\d{2}-", path.name)
    )


def read_text(path: Path) -> str:
    """Read a markdown file."""
    return path.read_text(encoding="utf-8")


def has_front_matter(text: str) -> bool:
    """Return whether a markdown file starts with YAML front matter."""
    return text.startswith("---\n")


def extract_front_matter(text: str) -> str:
    """Return the raw YAML front matter block or an empty string."""
    if not has_front_matter(text):
        return ""
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return ""
    return parts[1]


def extract_body(text: str) -> str:
    """Return markdown body after front matter."""
    if not has_front_matter(text):
        return text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return ""
    return parts[2]


def classify_quarantine_reason(path: Path, text: str) -> str | None:
    """Classify files that should not remain in the public docs root."""
    rel_path = path.relative_to(ROOT)
    body = extract_body(text).strip()
    front_matter = extract_front_matter(text)

    if path.name.endswith(".local.md"):
        return "local_only_rules"
    if "allowed-tools:" in front_matter:
        return "agent_prompt_files"
    if "[Content of the" in body or body.startswith("[Content of "):
        return "placeholder_stubs"
    if has_front_matter(text) and not body:
        return "empty_body_stubs"
    if rel_path.parts[0] == "99-Other" and not has_front_matter(text):
        return "uncurated_99_other"
    return None


def quarantine_file(path: Path, reason: str) -> dict[str, str]:
    """Move a file into quarantine while preserving its relative path."""
    rel_path = path.relative_to(ROOT)
    destination = QUARANTINE_ROOT / reason / rel_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    os.replace(path, destination)
    return {
        "reason": reason,
        "from": str(rel_path),
        "to": str(destination.relative_to(ROOT)),
    }


def collect_counts() -> list[tuple[str, int]]:
    """Count docs in each category recursively."""
    counts: list[tuple[str, int]] = []
    for category_dir in iter_category_dirs():
        count = len(list(category_dir.rglob("*.md")))
        if count > 0:
            counts.append((category_dir.name, count))
    return counts


def render_category_table(counts: list[tuple[str, int]]) -> str:
    """Render the README category table."""
    lines = [
        "| Category | Docs | Folder |",
        "|----------|-----:|--------|",
    ]
    for folder, count in counts:
        label = CATEGORY_LABELS.get(folder, folder)
        lines.append(f"| {label} | {count} | [`{folder}`](./{folder}/) |")
    return "\n".join(lines)


def render_largest_categories(counts: list[tuple[str, int]]) -> str:
    """Render the README top-categories list."""
    lines = []
    for idx, (folder, count) in enumerate(sorted(counts, key=lambda item: item[1], reverse=True)[:5], start=1):
        label = CATEGORY_LABELS.get(folder, folder)
        lines.append(f"{idx}. **{label}** ({count})")
    return "\n".join(lines)


def update_readme(counts: list[tuple[str, int]]) -> None:
    """Refresh public-facing counts in the README."""
    readme = README_PATH.read_text(encoding="utf-8")
    total_docs = sum(count for _, count in counts)
    total_categories = len(counts)

    readme = re.sub(
        r"Comprehensive unofficial mirror of Anthropic's Claude ecosystem documentation — .*?, sourced daily",
        f"Comprehensive unofficial mirror of Anthropic's Claude ecosystem documentation — {total_docs:,} Markdown articles across {total_categories} categories, sourced daily",
        readme,
        count=1,
    )

    category_table = render_category_table(counts)
    largest_categories = render_largest_categories(counts)

    readme = re.sub(
        r"<!-- CATEGORY_TABLE_START -->[\s\S]*<!-- CATEGORY_TABLE_END -->",
        f"<!-- CATEGORY_TABLE_START -->\n{category_table}\n<!-- CATEGORY_TABLE_END -->",
        readme,
        count=1,
    )
    readme = re.sub(
        r"<!-- LARGEST_CATEGORIES_START -->[\s\S]*<!-- LARGEST_CATEGORIES_END -->",
        f"<!-- LARGEST_CATEGORIES_START -->\n{largest_categories}\n<!-- LARGEST_CATEGORIES_END -->",
        readme,
        count=1,
    )

    README_PATH.write_text(readme, encoding="utf-8")


def write_report(moves: list[dict[str, str]], counts: list[tuple[str, int]]) -> None:
    """Persist machine-readable and human-readable cleanup reports."""
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "quarantined_files": moves,
        "quarantine_counts": Counter(move["reason"] for move in moves),
        "category_counts": [{"folder": folder, "count": count} for folder, count in counts],
    }
    REPORT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Public Mirror Cleanup Report",
        "",
        f"- Total quarantined files: {len(moves)}",
        "",
        "## Quarantine Summary",
        "",
    ]
    for reason, count in sorted(payload["quarantine_counts"].items()):
        lines.append(f"- `{reason}`: {count}")

    lines.extend(["", "## Quarantined Files", ""])
    for move in moves:
        lines.append(f"- `{move['from']}` -> `{move['to']}`")

    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    moves: list[dict[str, str]] = []
    for category_dir in iter_category_dirs():
        for path in sorted(category_dir.rglob("*.md")):
            text = read_text(path)
            reason = classify_quarantine_reason(path, text)
            if reason:
                moves.append(quarantine_file(path, reason))

    counts = collect_counts()
    update_readme(counts)
    write_report(moves, counts)
    print(f"Quarantined {len(moves)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
