# WASM Export Semantics Summary

## resvg.wasm
- Total exports: 50
- Signature-mapped exports: `resvg.wasm.exports_detailed.json`
- Intent breakdown:
  - support: 45
  - memory-manager: 5

## tree-sitter.wasm
- Total exports: 153
- Signature-mapped exports: `tree-sitter.wasm.exports_detailed.json`
- Intent breakdown:
  - language-metadata: 16
  - lookahead-state: 6
  - parser-control: 10
  - query-engine: 18
  - syntax-tree-control: 33
  - syntax-node-inspection: 39
  - memory-manager: 4
  - support: 27

## tree-sitter-bash.wasm
- Total exports: 3
- Signature-mapped exports: `tree-sitter-bash.wasm.exports_detailed.json`
- Intent breakdown:
  - support: 3

## Interpretation
- `tree-sitter.wasm` is a full parser runtime core with exports for parser lifecycle, language/query introspection, tree/cursor/node traversal, and query matching.
- `tree-sitter-bash.wasm` is a language loader module exposing a single entry `tree_sitter_bash` that returns the parser language handle.
- `resvg.wasm` is a rendering/module runtime with image render entry points and a large Brotli helper surface for embedded image decode.

## Deep Export Behavior (Call/Mem Profile)
- Call/behavior scans were produced as:
  - `resvg.wasm.call_graph.json`
  - `tree-sitter.wasm.call_graph.json`
  - `tree-sitter-bash.wasm.call_graph.json`
- `resvg.wasm`: 50 exported functions, 18 imports. Most interesting exported behavior is allocator/pixmap/render/brotli orchestration (eg `resvg_toString`, `resvg_getBBox`, `BrotliDecoderDecompressPrealloc`). One exported function (`renderedimage_pixels`) reaches JS helper imports for typed-array access/creation, consistent with runtime glue.
- `tree-sitter.wasm`: 153 exported functions, 10 imports. It is a mostly self-contained parser/query/query-capture engine; call patterns are mostly internal (no exported entry calls host-only APIs directly). Import surface includes callback hooks (`env.tree_sitter_*_callback`), WASI file/time ops, and `env.emscripten_resize_heap`.
- `tree-sitter-bash.wasm`: 3 exported functions, 11 imports. Behavior is thin parser-language bootstrap with extensive table/data-relocation logic and no direct imported-call fan-out from exports.
