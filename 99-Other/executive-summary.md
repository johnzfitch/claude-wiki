---
title: "Executive Summary"
category: "99-Other"
---

## Executive Summary

- Total transitions: 30
- Total commits across transitions: 276
- Sum of per-transition file touches: 1632
- Sum of inserted lines: 74558
- Sum of deleted lines: 51305
- Sum of changed lines (insertions + deletions): 125863

Largest transitions by total changed lines:

| Transition | Changed Lines | + | - | Files | Commits |
|---|---:|---:|---:|---:|---:|
| `rust-v0.105.0-alpha.9 -> rust-v0.105.0-alpha.10` | 43694 | 7699 | 35995 | 113 | 17 |
| `rust-v0.105.0-alpha.16 -> rust-v0.105.0-alpha.17` | 10482 | 7513 | 2969 | 135 | 21 |
| `rust-v0.105.0-alpha.11 -> rust-v0.105.0-alpha.12` | 8692 | 7867 | 825 | 75 | 14 |
| `rust-v0.105.0-alpha.6 -> rust-v0.105.0-alpha.7` | 7078 | 5935 | 1143 | 118 | 22 |
| `rust-v0.105.0-alpha.19 -> rust-v0.105.0-alpha.20` | 6315 | 5920 | 395 | 67 | 9 |
| `rust-v0.105.0-alpha.10 -> rust-v0.105.0-alpha.11` | 5116 | 2671 | 2445 | 232 | 11 |
| `rust-v0.105.0-alpha.3 -> rust-v0.105.0-alpha.4` | 4594 | 4396 | 198 | 69 | 13 |
| `rust-v0.105.0-alpha.8 -> rust-v0.105.0-alpha.9` | 4421 | 3355 | 1066 | 100 | 16 |
| `rust-v0.106.0-alpha.3 -> rust-v0.106.0-alpha.4` | 4135 | 3797 | 338 | 68 | 9 |
| `rust-v0.105.0-alpha.26 -> rust-v0.106.0-alpha.1` | 4007 | 3346 | 661 | 43 | 4 |

Highest-impact subsystems in cumulative range:

| Subsystem | Changed Lines | + | - |
|---|---:|---:|---:|
| `codex-rs/app-server-protocol` | 47303 | 13381 | 33922 |
| `codex-rs/core` | 27542 | 21668 | 5874 |
| `codex-rs/tui` | 15330 | 13818 | 1512 |
| `codex-rs/app-server` | 7586 | 6641 | 945 |
| `codex-rs/network-proxy` | 2770 | 2549 | 221 |
| `codex-rs/utils` | 2307 | 2067 | 240 |
| `codex-rs/linux-sandbox` | 1817 | 1636 | 181 |
| `codex-rs/state` | 1783 | 1756 | 27 |
| `codex-rs/exec-server` | 1416 | 0 | 1416 |
| `.codex` | 1124 | 1124 | 0 |
| `codex-rs/exec` | 617 | 492 | 125 |
| `codex-rs/protocol` | 603 | 562 | 41 |
| `codex-rs/Cargo.lock` | 526 | 445 | 81 |
| `codex-rs/login` | 474 | 450 | 24 |
| `codex-rs/codex-api` | 385 | 94 | 291 |

0.106 alpha-only transitions (alpha.1 -> alpha.5):

| Transition | Changed Lines | + | - | Files | Commits |
|---|---:|---:|---:|---:|---:|
| `rust-v0.106.0-alpha.1 -> rust-v0.106.0-alpha.2` | 233 | 200 | 33 | 8 | 3 |
| `rust-v0.106.0-alpha.2 -> rust-v0.106.0-alpha.3` | 190 | 165 | 25 | 3 | 2 |
| `rust-v0.106.0-alpha.3 -> rust-v0.106.0-alpha.4` | 4135 | 3797 | 338 | 68 | 9 |
| `rust-v0.106.0-alpha.4 -> rust-v0.106.0-alpha.5` | 641 | 84 | 557 | 11 | 4 |

How to trace exact changed code lines:

- Use  for hunk coordinate lookup ( and  line ranges).
- Open the matching diff in  for full context and exact added/removed lines.
