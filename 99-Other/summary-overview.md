---
title: "WASM Extraction Summary"
category: "99-Other"
---

# WASM Extraction Summary

| module | embedded marker offset | wasm start | size (bytes) | extracted file | functions |
|---|---:|---:|---:|---|---:|
| resvg.wasm | 221059122 | 221059146 | 2478655 | evidence/wasm_extracted/resvg.wasm | 50 |
| tree-sitter.wasm | 223537753 | 223537783 | 205547 | evidence/wasm_extracted/tree-sitter.wasm | 153 |
| tree-sitter-bash.wasm | 223743282 | 223743317 | 1380769 | evidence/wasm_extracted/tree-sitter-bash.wasm | 3 |

Exports have been enumerated into:
- evidence/wasm_extracted/resvg.wasm.exports.json
- evidence/wasm_extracted/tree-sitter.wasm.exports.json
- evidence/wasm_extracted/tree-sitter-bash.wasm.exports.json

See corresponding `*.summary.json` files for exact offsets and ranges.
