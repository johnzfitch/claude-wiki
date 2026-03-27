# Phase 1 — Symbol Diff: 2.1.59 → 2.1.70

**Log:** [../logs/p1-diff_symbols.json](../logs/p1-diff_symbols.json)

## Summary

| Metric | Count |
|--------|-------|
| Symbols added | 1,648,048 |
| Symbols removed | 1,467,337 |
| Symbols in common | 42,772 |
| Net new data symbols | +180,711 |

## Interpretation

All added/removed symbols are Ghidra auto-labeled **data references** (`DAT_*` and `BYTE_ARRAY_*`).
Bun-compiled ELF binaries do not export named function symbols — all application functions are
`FUN_<addr>` in Ghidra's namespace and are not part of the ELF symbol table.

The net +180,711 data symbols reflect:
- New global data structures in the expanded `.data.rel.ro` (+251,352 bytes)
- New pointer tables for the +4.1MB of new `.text` code
- New string table entries for the +1.5MB of new `.rodata` content

## Symbol Table Stats

| | 2.1.59 | 2.1.70 |
|-|--------|--------|
| .dynsym size | 23,568 bytes | 25,488 bytes (+1,920) |
| .symtab size | 24,336 bytes | 26,376 bytes (+2,040) |
| .dynstr size | 16,709 bytes | 17,809 bytes (+1,100) |

The `.dynsym` growth (+1,920 bytes ≈ ~8 new exported symbols at 240 bytes/entry) indicates
a small number of new exported library functions.

## Named Exports (new in 2.1.70)

The larger `.dynsym` suggests ~8 new named exports, likely additional Bun runtime symbols.
Exact names not resolved by diff_symbols (returns only data labels). Use `list_exports` on
a fully-analyzed binary to enumerate them.

## Notes

- Fast-profile binary: function-level analysis not available via this tool path
- Section size deltas (from Phase 5) provide the real function count evidence
- String-based labeling (Phase 2) provides subsystem attribution

---
*Generated: 2026-03-06 | Reference: 2.1.59-7a4a6539 → 2.1.70-1e5c1011*
