---
source_url: "https://red.anthropic.com/2026/firefox/"
category: "22-Safety-Policy"
fetched_at: "2026-04-08"
---

# Partnering with Mozilla to Improve Firefox's Security

In a collaboration with researchers at Mozilla, Claude Opus 4.6 discovered 22 vulnerabilities in Firefox over the course of two weeks.

Published: March 6, 2026

## Key Findings

- **22 CVEs discovered** in Firefox by Claude Opus 4.6
- **14 flagged as high severity** by Mozilla
- Vulnerabilities were fixed in **Firefox version 148** (released February 24, 2026)
- Bug reports included minimal test cases that allowed Mozilla's security team to quickly verify and reproduce each issue

## CVE-2026-2796: JIT Miscompilation Exploit

The most notable finding was CVE-2026-2796, a JIT miscompilation error in Firefox's JavaScript WebAssembly component:

- Assigned a **critical 9.8 CVSS score**
- Claude wrote an exploit achieving arbitrary read/write and code execution in Firefox's JavaScript engine by leveraging type confusion
- **Important limitation**: The exploit only works within a testing environment that intentionally removes some browser security features
- Claude produced a "crude" exploit in only 2 out of several hundred attempts, costing approximately $4,000 in API credits

## Reception

The collaboration was well-received by Mozilla. The Mozilla Blog post "[Hardening Firefox with Anthropic's Red Team](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/)" describes the partnership from Mozilla's perspective.

## See Also

- [Reverse engineering Claude's CVE-2026-2796 exploit](https://red.anthropic.com/2026/exploit/)
- [0-Days: Vulnerability detection at scale](https://red.anthropic.com/2026/zero-days/)
