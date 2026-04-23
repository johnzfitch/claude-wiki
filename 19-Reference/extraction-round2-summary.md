---
title: "Extraction Round 2 Summary"
category: "19-Reference"
---

# Extraction Round 2 Summary

## Binary
- Path: `/home/zack/.local/share/claude/versions/2.1.50`
- Type: ELF64 executable (x86-64)
- Size: 225,124,924 bytes

## Runtime Hardening / Layout
- `RELRO`: None (`evidence/checksec_summary.txt`)
- `NX`: Enabled (`evidence/checksec_summary.txt`)
- `PIE`: Disabled (`evidence/checksec_summary.txt`)
- `Canary symbols`: Present (`evidence/checksec_summary.txt`)

## Embedded Component Inventory
- Embedded shared objects carved from host binary:
  - `evidence/carved_elfs/so_00_0xC8753EA.bin`
  - `evidence/carved_elfs/so_01_0xCD3A7F5.bin`
  - `evidence/carved_elfs/so_02_0xCE8564B.bin`
  - `evidence/carved_elfs/so_03_0xCF33781.bin`
- Manifest with offsets/sizes/types: `evidence/carved_shared_objects_manifest.txt`

## BunFS Runtime Assets (from embedded JS loader)
- Loader map: `evidence/bunfs_loader_map.txt`
- Inventory: `evidence/bunfs_embedded_modules.txt`
- Notable modules:
  - `/$bunfs/root/ripgrep.node`
  - `/$bunfs/root/image-processor.node`
  - `/$bunfs/root/file-index.node`
  - `/$bunfs/root/color-diff.node`
  - `/$bunfs/root/resvg.wasm`
  - `/$bunfs/root/tree-sitter.wasm`
  - `/$bunfs/root/tree-sitter-bash.wasm`

## Embedded Data Blobs
- ZSTD blob at `0x3A65E0` carved/decompressed:
  - Compressed: `evidence/carved_zstd_0x3A65E0.bin`
  - Decompressed: `evidence/carved_zstd_0x3A65E0.dec`
  - Strings extracted: `evidence/carved_zstd_0x3A65E0.strings.txt`
  - Summary: `evidence/carved_zstd_summary.txt`
- Decompressed payload contains ~9,966 package-name strings (dependency/package corpus style), not credential material.

## Certificate / Key Material
- PEM region extraction:
  - Bundle: `evidence/extracted_cert_bundle.pem`
  - Parsed cert sample metadata: `evidence/cert_bundle_summary.txt`
- Certificate count detected: 148
- Private key offset markers found: 0 (`evidence/secret_scan_conclusion.txt`)

## Secret Scanning
- High-confidence token regex scans (JWT/sk-ant/github_pat): all 0 hits
  - `evidence/high_conf_token_scan.txt`
- Key marker offset scan:
  - `evidence/key_material_markers_offsets.txt`
- Trufflehog verified scan:
  - `evidence/trufflehog_verified.json` (0 findings)
- Gitleaks on extracted strings:
  - `evidence/gitleaks_strings.json` (7 generic-api-key heuristic hits, all obvious false positives)
  - Consolidated interpretation: `evidence/secret_scan_conclusion.txt`

## Endpoint/Network Surface
- Focused URL list: `evidence/url_auth_telemetry_focus.txt`
- Classified endpoint list: `evidence/network_endpoints_classified.txt`
- Includes OAuth/token endpoints, metrics/telemetry endpoints, API domains, and MCP proxy references.

## Important Note
- `pyghidra-lite` metadata listing works, but functional queries still fail with `Program not found ... Available: []`. Static extraction was therefore completed via shell tooling and binary carving.
