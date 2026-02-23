---
category: "04-API-Reference"
fetched_at: "2026-02-23T00:45:50Z"
source_url: "https://raw.githubusercontent.com/anthropics/anthropic-cookbook/main/claude_agent_sdk/research_agent/architecture_diagram.md"
title: "Architecture_Diagram"
---

\# Research Agent Architecture \`\`\`mermaid graph TD User\[User\] --\> Agent\[Research Agent\] Agent --\> Tools\[Tools\] Tools --\> WebSearch\[WebSearch\] Tools --\> Read\[Read Files/Images\] style Agent fill:#f9f,stroke:#333,stroke-width:3px style Tools fill:#bbf,stroke:#333,stroke-width:2px \`\`\` \# Communication Flow Diagram \`\`\`mermaid sequenceDiagram participant User participant Agent participant Tools User-\>\>Agent: Query loop Until Complete Agent-\>\>Agent: Think Agent-\>\>Tools: Search/Read Tools--\>\>Agent: Results end Agent--\>\>User: Answer \`\`\`
