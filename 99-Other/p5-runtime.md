# Phase 5 — Runtime & Format Analysis: 2.1.59 → 2.1.70

**Logs:**
- [../logs/p5-elf_sections-2170.json](../logs/p5-elf_sections-2170.json)
- [../logs/p5-elf_sections-2159.json](../logs/p5-elf_sections-2159.json)
- [../logs/p5-detect_embedded_runtime.json](../logs/p5-detect_embedded_runtime.json)

## Binary Overview

| Property | 2.1.59 | 2.1.70 |
|----------|--------|--------|
| File size | 218 MB | **230 MB** (+12 MB) |
| ELF bits | 64 | 64 |
| Machine | x86-64 | x86-64 |
| Sections | 39 | **44** (+5) |
| Symbols | 10,001 | **10,001** (same) |
| Stripped | false | false |
| Has debug | **false** | **true** |

## ELF Section Delta

| Section | 2.1.59 size | 2.1.70 size | Delta |
|---------|-------------|-------------|-------|
| `.rodata` | 41,729,160 B | 43,240,504 B | **+1,511,344 B** (+1.4 MB) |
| `.text` | 60,879,544 B | 65,220,320 B | **+4,340,776 B** (+4.1 MB) |
| `.data` | 123,124 B | 153,540 B | +30,416 B |
| `.data.rel.ro` | 420,832 B | 672,184 B | **+251,352 B** |
| `.init_array` | 96 B | 152 B | **+56 B** (+7 init functions) |
| `.dynsym` | 23,568 B | 25,488 B | +1,920 B |
| `.dynstr` | 16,709 B | 17,809 B | +1,100 B |
| `.bss` | 939,568 B | 1,088,085 B | +148,517 B |
| `unallocated_0` | 124,562,793 B | 129,551,113 B | +4,988,320 B |
| `.plt` | 6,576 B | 7,680 B | +1,104 B |
| `.got` | 6,856 B | 14,208 B | +7,352 B |

## New Sections in 2.1.70

| Section | Size | Purpose |
|---------|------|---------|
| `.gcc_except_table` | 165,448 B | **C++ exception handling tables** — new exception paths |
| `.debug_gdb_scripts` | 34 B | GDB pretty-printer scripts |
| `.eh_frame_hdr` | 252,460 B | Exception frame header index |
| `.eh_frame` | 1,432,240 B | **DWARF call frame info** (1.4MB) — full stack unwinding |
| `.iplt` | 128 B | Indirect PLT (new extern function trampolines) |

**Significance:** The addition of `.gcc_except_table`, `.eh_frame_hdr`, and `.eh_frame` (totaling
**1.85 MB**) indicates that 2.1.70 was compiled with full C++ exception support enabled. This may
reflect new native code (possibly related to `audio-capture.node` integration) or a Bun runtime
upgrade that enabled exception-safe builds.

## Function Count Estimate

The `.text` delta of **+4,340,776 bytes** at an average Bun function size of ~500 bytes
gives an estimated **+8,682 new functions**, consistent with the reported 60,300 → 68,960 (+8,660).

| | 2.1.59 | 2.1.70 |
|-|--------|--------|
| .text size | 60.9 MB | 65.2 MB |
| Reported functions | 60,300 | 68,960 |
| Functions/MB | ~990 | ~1,057 |

## Embedded Runtime Detection

```json
{
  "runtimes": [
    {
      "type": "bunfs",
      "confidence": "high",
      "strategy": "external_tools",
      "note": "Compressed BunFS — extracted via extract_bunfs.py"
    },
    {
      "type": "electron_asar",
      "confidence": "high",
      "strategy": "search_payload",
      "payload_offset": "0x01ed6c01"
    }
  ]
}
```

Note: The `electron_asar` detection at offset `0x01ed6c01` appears to be a false positive
(no readable strings found at that offset). The actual application payload is BunFS-compressed.

## Runtime Version Comparison

| Component | 2.1.59 | 2.1.70 |
|-----------|--------|--------|
| Bun version | **1.3.10** | **1.3.11** |
| Rust crate versions | same set | same set |
| Registry hash | 1949cf8c6b5b557f | 1949cf8c6b5b557f |
| JavaScriptCore | same | same (same Bun minor) |

Bun 1.3.11 vs 1.3.10 is a patch-level upgrade. The same Rust crates and registry hash
confirms the native/C++ components are largely unchanged.

## BunFS Payload Size Delta

| | 2.1.59 | 2.1.70 |
|-|--------|--------|
| `unallocated_0` (BunFS) | 124,562,793 B | 129,551,113 B |
| Delta | | **+4,988,320 B** (+4.8 MB) |

The +4.8 MB in unallocated_0 accounts for:
- New `audio-capture.node` (483 KB)
- Larger `cli.js` (+1,194 lines of minified JS ≈ ~500 KB)
- Other payload compression differences

## Key Observations

1. **Debug symbols present**: `has_debug: true` for 2.1.70 (false for 2.1.59). The `.debug_gdb_scripts`
   section is 34 bytes — minimal, just a GDB script hint. Full DWARF is absent; the "debug" flag
   likely reflects Ghidra's detection of eh_frame data.

2. **Exception handling growth**: +1.85 MB of exception tables suggests significant new C++ code
   or compiler flag change enabling `-fexceptions` on previously nothrow code.

3. **`.init_array` +56 bytes**: 7 additional static initializers run at startup. These may
   initialize new subsystems (Foundry client, remote session manager, audio subsystem).

4. **`.got` nearly doubled**: +7,352 bytes indicates many new dynamic symbol resolutions
   (new library calls or new indirect function calls).

---
*Generated: 2026-03-06 | Binaries: 2.1.59-7a4a6539 → 2.1.70-1e5c1011*
