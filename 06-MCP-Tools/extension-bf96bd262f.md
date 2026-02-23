---
category: "06-MCP-Tools"
fetched_at: "2026-02-23T00:45:48Z"
source_url: "https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/extension.md"
title: "Extension"
---

\# Everything Server - Extension Points \*\*\[Architecture\](architecture.md) \| \[Project Structure\](structure.md) \| \[Startup Process\](startup.md) \| \[Server Features\](features.md) \| Extension Points \| \[How It Works\](how-it-works.md)\*\* \## Adding Tools - Create a new file under \`tools/\` with your \`registerXTool(server)\` function that registers the tool via \`server.registerTool(...)\`. - Export and call it from \`tools/index.ts\` inside \`registerTools(server)\`. \## Adding Prompts - Create a new file under \`prompts/\` with your \`registerXPrompt(server)\` function that registers the prompt via \`server.registerPrompt(...)\`. - Export and call it from \`prompts/index.ts\` inside \`registerPrompts(server)\`. \## Adding Resources - Create a new file under \`resources/\` with your \`registerXResources(server)\` function using \`server.registerResource(...)\` (optionally with \`ResourceTemplate\`). - Export and call it from \`resources/index.ts\` inside \`registerResources(server)\`.
