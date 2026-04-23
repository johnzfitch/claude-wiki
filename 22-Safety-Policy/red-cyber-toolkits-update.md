---
title: "AI Models on Realistic Cyber Ranges"
source_url: "https://red.anthropic.com/2026/cyber-toolkits-update/"
category: "22-Safety-Policy"
fetched_at: "2026-04-08"
---

# AI Models on Realistic Cyber Ranges

Current Claude models can now succeed at multistage attacks on networks with dozens of hosts using only standard, open-source tools, instead of the custom tools needed by previous generations.

Published: 2026

## Key Findings

### Claude Sonnet 4.5 Progress

- Can succeed on a minority of test networks **without the custom cyber toolkit** needed by previous generations
- Can exfiltrate all simulated personal information in a high-fidelity simulation of the **Equifax data breach** using only a Bash shell on a widely-available Kali Linux host
- Uses standard, open-source penetration testing tools rather than a custom toolkit

### Rapid Improvement

- **Claude Sonnet 3.5** (released ~1 year before Sonnet 4.5): Could not succeed at the Equifax simulation in any of five trials without the specialized cyber toolkit
- **Claude Sonnet 4.5**: Succeeds using only publicly available tools

### Implications

The trajectory of models first needing specialized tools and then being able to operate without them (or using only publicly available tools) is consistent with other trends observed in AI progress. Anthropic believes it presages further improvement in the cyber domain.

## See Also

- [AI for Critical Infrastructure Defense](red-critical-infrastructure-defense.md)
- [Claude Mythos Preview](../20-Models/claude-mythos-preview.md)
