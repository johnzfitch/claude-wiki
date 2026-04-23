---
title: "Changed-Surface Decompile Report"
category: "19-Reference"
---

# Changed-Surface Decompile Report
Scope: `/home/zack/.local/share/claude/versions/2.1.50` vs `2.1.55`, then `2.1.55` vs `2.1.59`.

## 1) Method and scope
- Primary analysis: `pyghidra-lite` (`import_binary`, `binary_info`, `elf_sections`, `list_imports`, `list_exports`, `search_symbols`, `search_strings`, `get_xrefs`, `decompile`, `diff_symbols`).
- Local binary inspection: `readelf`, `cmp`, `grep -abo`, `sha256sum` for file-offset and mapped-vs-unmapped validation.
- Mapped code boundary (from `readelf -l` LOAD file ranges):
  - `2.1.50`: mapped bytes end at file offset `0x6185998` (`102,259,096`).
  - `2.1.55`/`2.1.59`: mapped bytes end at `0x627d9a0` (`103,274,912`).
- Focus: executable mapped surface first (`.text/.rodata/imports/exports/functions`), with payload-only indicators called out separately.

## 2) Executable-level diff evidence (.text/.rodata/imports/exports/functions)
### 2.1.50 -> 2.1.55 (mapped executable changed)
- BuildID changed: `54a45ee1039649fa1c3e55d73be36ae7192f0531` -> `819d4aec874364f20a70aed51af27f3235fb3250`.
- Key section deltas (`readelf -SW`/`pyghidra elf_sections`):
  - `.text`: `0x391d184` (`59,888,004`) -> `0x3a0f2b8` (`60,879,544`), file offset `0x27d6a00` -> `0x27dd200`.
  - `.rodata`: `0x27c5908` (`41,703,688`) -> `0x27cbc88` (`41,729,160`).
  - `.dynsym`: `0x5bf8` -> `0x5c10`; `.dynstr`: `0x412f` -> `0x4145`; `.rela.plt`: `0x2658` -> `0x2670`; `.plt`: `0x19a0` -> `0x19b0`; `.got.plt`: `0xce0` -> `0xce8`.
- Import-set diff (pyghidra + local UND set):
  - Added import: `pthread_attr_setstack` (absent in `2.1.50`, present in `2.1.55`).
  - No removed imports observed.
- Function/export anchor shifts:
  - `napi_create_array`: `0x032c0960` -> `0x032cab50`.
  - `uv_hrtime`: `0x0414c820` -> `0x04158120`.
  - `entry` export (pyghidra): `0x02ae8a00` -> `0x02aef200`.

### 2.1.55 -> 2.1.59 (mapped executable stable)
- BuildID unchanged: both `819d4aec874364f20a70aed51af27f3235fb3250`.
- Core mapped section offsets/sizes identical (`.text/.rodata/.dynsym/.dynstr/.rela.plt/.plt/.data.rel.ro/.got.plt`).
- Import/export/function name sets stable in local ELF symbol extraction:
  - imports: `409` vs `409`, added `0`, removed `0`.
  - exports: `556` vs `556`, added `0`, removed `0`.
- Address checks identical for anchors:
  - `napi_create_array`: both `0x032cab50`.
  - `uv_hrtime`: both `0x04158120`.
  - `pthread_attr_setstack`: both present (`UND` symbol + PLT thunk).

## 3) Decompiled changed subsystems
### Auth/OAuth path
- Mapped executable evidence (`2.1.50`):
  - `FUN_03bc8c60 @ 0x03bc8c60` and `FUN_03bc4a20 @ 0x03bc4a20` decompile with auth/TLS strings:
    - `"TODO: support authentication method: {s}"`
    - `"Server does not support SSL"`
    - `"Failed to upgrade to TLS"`
- OAuth-specific finding (`2.1.59`): payload-only.
  - `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` at file offset `110,848,691` (beyond mapped end `103,274,912`).
  - `CLAUDE_CODE_OAUTH_SCOPES` at `110,848,747` (payload).
  - `pyghidra search_strings` on `2.1.55/2.1.59` returns no mapped xrefs for these tokens.

### Plugin/Cache path
- Mapped executable evidence (`2.1.50`):
  - `FUN_0302a260 @ 0x0302a260`: emits `"Expected plugin to be an object"`.
  - `FUN_02cd6730 @ 0x02cd6730`: decompile includes cache lifecycle strings:
    - `"opening cache/package/version dir"`
    - `"copying files from cache to destination"`
- New plugin/cache env indicators are payload-only:
  - `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS`: `2.1.55` offset `108,338,029`, `2.1.59` offset `108,356,994`.
  - `CLAUDE_CODE_PLUGIN_USE_ZIP_CACHE`: `2.1.59` offset `107,983,531`.
  - All above are beyond mapped end and absent from pyghidra mapped string xrefs.

### VCS/Perforce detection
- Mapped executable evidence: no perforce-specific mapped string/xref surfaced in pyghidra for `2.1.50` or `2.1.55`.
- Payload-only finding (`2.1.59`):
  - `P4PORT` at offset `104,390,904`.
  - `perforce` at offset `104,390,918`.
  - Both are beyond mapped end `103,274,912`.

### Voice stream path
- Mapped executable evidence: no mapped `VOICE_STREAM_BASE_URL` string/xref in pyghidra (`2.1.55/2.1.59`).
- Payload-only finding (`2.1.59`):
  - `VOICE_STREAM_BASE_URL` at offset `112,721,274` (> mapped end).

### Worker epoch/lifecycle
- Mapped executable evidence (`2.1.50`):
  - `FUN_042a4ec0 @ 0x042a4ec0` decompile includes `worker_threads` registration path.
  - `FUN_0333b320 @ 0x0333b320` xref’d by `workers_spawned` / `workers_terminated` strings.
- Mapped ABI-level lifecycle change (`2.1.55`):
  - new import `pthread_attr_setstack` indicates thread stack-control surface added at executable/import layer.
- Worker epoch token is payload-only:
  - `CLAUDE_CODE_WORKER_EPOCH` offset `113,617,025` (`2.1.55`) and `113,653,628` (`2.1.59`), both beyond mapped end.

## 4) 2.1.55 vs 2.1.59 verification
- `cmp -n 103274912` (all mapped bytes) returns no differences.
- First whole-file difference appears at offset `103,318,189` (outside mapped region).
- `pyghidra diff_symbols(2.1.55,2.1.59)`: `num_added=0`, `num_removed=0`, `num_common=2224`.
- BuildID, mapped section geometry, import/export symbol sets, and sampled function addresses are all stable.

## 5) Confidence ratings and limitations
- Executable mapped-surface verdict (`2.1.55` vs `2.1.59` unchanged): **High**.
- `2.1.50` -> `2.1.55` mapped executable changed: **High**.
- Subsystem attribution for OAuth/perforce/voice/plugin-zip/worker-epoch as payload-only: **High** for location classification (file offsets beyond LOAD range), **Medium** for behavioral impact (not dynamically executed here).
- Limitation: many deep decompiles in this binary family contain overlapping/bad-instruction warnings; evidence used here is anchored to repeated string/function/import correlations plus mapped-range math.

## 6) Practical significance
- `2.1.50` -> `2.1.55` is a real native executable rebuild (`.text/.rodata/import` moved and grew).
- `2.1.55` -> `2.1.59` is not a mapped native-code change; differences start after mapped LOAD bytes.
- Requested subsystem indicators in `2.1.59` (OAuth refresh/scopes, perforce/P4PORT, voice stream URL, plugin zip cache, worker epoch token) are currently evidenced as payload-only data additions, not decompiled mapped code changes.
