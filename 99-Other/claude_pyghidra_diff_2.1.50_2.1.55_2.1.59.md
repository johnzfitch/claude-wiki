# Claude Binary Reverse Engineering Diff Report

Scope: `/home/zack/.local/share/claude/versions/2.1.50` -> `/home/zack/.local/share/claude/versions/2.1.55` -> `/home/zack/.local/share/claude/versions/2.1.59`
Method: pyghidra-lite MCP (`import_binary`, `elf_info`, `elf_sections`, `list_imports`, `list_exports`, `list_functions`, `get_function_info`, `search_strings`) with supplemental ELF sanity checks.

## 1) Binary Identity

- `2.1.50`
  - size: `225,124,924`
  - sha256: `74042739197c58a4791c1f67414c0d8956639ec2f2e935280872b83d4317be78`
  - BuildID: `54a45ee1039649fa1c3e55d73be36ae7192f0531`
- `2.1.55`
  - size: `227,281,653` (`+2,156,729` vs `2.1.50`)
  - sha256: `c4ba00f654e539cefde027f5371371f519ec1394925abfcb09661af613aa7489`
  - BuildID: `819d4aec874364f20a70aed51af27f3235fb3250`
- `2.1.59`
  - size: `227,880,817` (`+599,164` vs `2.1.55`)
  - sha256: `7a4a653982b07e0a8157f8d3b2c2f8e442520ab07b2fa2e692ba054dbba210c9`
  - BuildID: `819d4aec874364f20a70aed51af27f3235fb3250` (same as `2.1.55`)

## 2) ELF Structure Diff (pyghidra-lite)

### 2.1.50 -> 2.1.55

Major mapped-section changes observed in `elf_sections`:

- `.text`: `59,888,004` -> `60,879,544` (`+991,540`)
- `.rodata`: `41,703,688` -> `41,729,160` (`+25,472`)
- `.plt`: `6,560` -> `6,576` (`+16`)
- `.dynsym`: `23,544` -> `23,568` (`+24`)
- `.dynstr`: `16,687` -> `16,709` (`+22`)
- `.rela.plt`: `9,816` -> `9,840` (`+24`)
- `.got.plt`: `3,296` -> `3,304` (`+8`)
- `.data`: `123,204` -> `123,124` (`-80`)
- `.data.rel.ro`: `420,768` -> `420,832` (`+64`)

Interpretation: `2.1.55` contains a meaningful code/data rebuild vs `2.1.50`.

### 2.1.55 -> 2.1.59

Core mapped sections are identical in pyghidra-lite output:

- `.text`: unchanged (`60,879,544`)
- `.rodata`: unchanged (`41,729,160`)
- `.plt/.got.plt/.rela.plt/.dynsym/.dynstr`: unchanged

Only trailing/unallocated region changed:

- `unallocated_0`: `123,963,629` -> `124,562,793` (`+599,164`)

Interpretation: code-bearing sections are unchanged from `2.1.55` to `2.1.59`; the delta is in non-mapped payload growth.

## 3) Import Surface Diff

Using pyghidra-lite `list_imports` (validated against ELF UND symbol set):

### 2.1.50 -> 2.1.55

- Added import:
  - `pthread_attr_setstack`
- No removed imports detected in UND set diff.

### 2.1.55 -> 2.1.59

- No import additions/removals detected.

Counts (supplemental UND set check):

- `2.1.50`: 420 unique UND imports
- `2.1.55`: 421
- `2.1.59`: 421

## 4) Exported/API Symbol Surface

pyghidra-lite `list_exports` samples show:

- `2.1.50` export addresses differ materially from later builds (e.g., `entry`, N-API and `uv_*` ranges shifted).
- `2.1.55` and `2.1.59` export name/address pairs are identical in sampled ranges (first 100 exports).

## 5) Function-Level Checks (pyghidra-lite)

Representative symbols:

- `entry`
  - `2.1.50`: `0x02ae8a00`
  - `2.1.55`: `0x02aef200`
  - `2.1.59`: `0x02aef200` (same as `2.1.55`)
- `napi_create_array`
  - `2.1.50`: `0x032c0960`
  - `2.1.55`: `0x032cab50`
  - `2.1.59`: `0x032cab50` (same as `2.1.55`)
- `uv_hrtime`
  - `2.1.50`: `0x0414c820`
  - `2.1.55`: `0x04158120`
  - `2.1.59`: `0x04158120` (same as `2.1.55`)

Interpretation: `2.1.50` -> `2.1.55` moved/reshaped function layout; `2.1.55` and `2.1.59` remain functionally aligned on inspected symbols.

## 6) String/Relocation Notes

- `ZSTD_trace_*` and `__wrap_gettid` string tokens appear across versions in `search_strings`.
- Practical import/API delta still resolves to the single observable import addition (`pthread_attr_setstack`) at `2.1.55`.

## 7) Consolidated Conclusions

1. `2.1.50` to `2.1.55` is a substantive binary rebuild (code + rodata + import surface changed).
2. `2.1.55` to `2.1.59` shows no mapped code-section changes in pyghidra-lite outputs.
3. `2.1.59` differs primarily by a `+599,164` growth in non-mapped/trailing payload, matching total file size delta.
4. BuildID parity (`2.1.55` == `2.1.59`) plus identical key section sizes strongly indicates unchanged executable core between those two versions.

