# Public Mirror Workflow

This repo now has a post-sync normalization pass driven by [normalize-public-mirror.yml](/home/zack/dev/claude-wiki-public/.github/workflows/normalize-public-mirror.yml).

## Purpose

The private sync can still deliver files that do not belong in the public mirror as-is. The normalization pass keeps the public repo cleaner without deleting content outright.

## What It Does

1. Runs [normalize_public_mirror.py](/home/zack/dev/claude-wiki-public/scripts/normalize_public_mirror.py) after category-folder pushes.
2. Quarantines low-confidence files into `meta/quarantine/` instead of deleting them.
3. Updates public category counts in [README.md](/home/zack/dev/claude-wiki-public/README.md).
4. Writes machine-readable and human-readable cleanup reports into `meta/`.

## Quarantine Rules

- `local_only_rules`: files ending in `.local.md`
- `agent_prompt_files`: files whose front matter contains `allowed-tools:`
- `placeholder_stubs`: placeholder captures such as `"[Content of the ... previous WebFetch result]"`
- `empty_body_stubs`: files that only contain front matter and no body
- `uncurated_99_other`: files in `99-Other/` that have no YAML front matter at all

## Rollout Model

1. Private repo sync publishes category folders into this repo.
2. This workflow runs automatically on that push.
3. It quarantines obvious non-public artifacts.
4. If anything changed, it commits a follow-up normalization commit.

## Follow-Up Work

- Add a second-stage title and slug normalization pass once filename policy is settled.
- Move placeholder detection upstream into the private repo so these files never land here.
- Replace the current quarantine heuristics with stronger source-aware validation once all public docs consistently carry `source_url`.
