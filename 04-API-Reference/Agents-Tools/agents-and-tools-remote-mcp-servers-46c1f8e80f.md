---
title: "Remote MCP servers - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:22Z"
tags: ["api", "mcp"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fremote-mcp-servers)





SearchCtrlK

First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)[Authentication](/docs/en/manage-claude/authentication)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

[Thinking](/docs/en/build-with-claude/thinking)

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[Console](/)

[Messages](/docs/en/intro)MCP

# Remote MCP servers

Copy page



Connect Claude to third-party remote MCP servers through the MCP connector API. Browse example servers and review the steps to connect.

Copy page



Several companies have deployed remote MCP servers that developers can connect to by using the Anthropic MCP connector API. These servers expand the capabilities available to developers and end users by providing remote access to various services and tools through the MCP protocol.



The remote MCP servers listed below are third-party services designed to work with the Claude API. These servers are not owned, operated, or endorsed by Anthropic. Users should only connect to remote MCP servers they trust and should review each server's security practices and terms before connecting.

## Connecting to remote MCP servers

To connect to a remote MCP server:

1.  Review the documentation for the specific server you want to use.
2.  Ensure you have the necessary authentication credentials.
3.  Follow the server-specific connection instructions provided by each company.

For more information about using remote MCP servers with the Claude API, see [MCP connector](/docs/en/agents-and-tools/mcp-connector).



Once connected, remote MCP tools follow the same triggering behavior as any other tool. See [When Claude uses MCP tools](/docs/en/agents-and-tools/mcp-connector#when-claude-uses-mcp-tools).

## Remote MCP server examples

[Ticket Tailor(opens in new tab)](https://help.tickettailor.com/en/articles/11892797-how-to-connect-ticket-tailor-to-your-favourite-ai-agent)

Event platform for managing tickets, orders & more

URL



``` inline-block
https://mcp.tickettailor.ai/mcp
```

[Linear(opens in new tab)](https://linear.app/docs/mcp)

Manage issues, projects & team workflows in Linear

URL



``` inline-block
https://mcp.linear.app/mcp
```

[Hugging Face(opens in new tab)](https://huggingface.co/settings/mcp)

Access the Hugging Face Hub and thousands of Gradio Apps

URL



``` inline-block
https://huggingface.co/mcp?login&gradio=none
```

[Blockscout(opens in new tab)](https://github.com/blockscout/mcp-server)

Access and analyze blockchain data

URL



``` inline-block
https://mcp.blockscout.com/mcp
```

[Close(opens in new tab)](https://help.close.com/v1/docs/en/mcp-server)

Connect Claude to Close CRM to securely access and act on your sales data

URL



``` inline-block
https://mcp.close.com/mcp
```

[Cloudflare Developer Platform(opens in new tab)](https://www.support.cloudflare.com/)

Build applications with compute, storage, and AI

URL



``` inline-block
https://bindings.mcp.cloudflare.com/mcp
```

[Egnyte(opens in new tab)](https://developers.egnyte.com/docs/Remote_MCP_Server)

Securely access and analyze Egnyte content

URL



``` inline-block
https://mcp-server.egnyte.com/mcp
```

[Figma(opens in new tab)](https://help.figma.com/hc/en-us/articles/32132100833559)

Generate diagrams and better code from Figma context

URL



``` inline-block
https://mcp.figma.com/mcp
```

[Guru(opens in new tab)](https://help.getguru.com/docs/connecting-gurus-mcp-server)

Search and interact with your company knowledge

URL



``` inline-block
https://mcp.api.getguru.com/mcp
```

[Jotform(opens in new tab)](https://www.jotform.com/developers/mcp/)

Create forms & analyze submissions inside Claude

URL



``` inline-block
https://mcp.jotform.com/mcp-app
```

[monday.com(opens in new tab)](https://developer.monday.com/apps/docs/mondaycom-mcp-integration)

Manage projects, boards, and workflows in monday.com

URL



``` inline-block
https://mcp.monday.com/mcp
```

[Notion(opens in new tab)](https://developers.notion.com/docs/mcp)

Connect your Notion workspace to search, update, and power workflows across tools

URL



``` inline-block
https://mcp.notion.com/mcp
```

[PayPal(opens in new tab)](https://mcp.paypal.com/)

Access PayPal payments platform

URL



``` inline-block
https://mcp.paypal.com/mcp
```

[Stripe(opens in new tab)](https://docs.stripe.com/mcp)

Payment processing and financial infrastructure tools

URL



``` inline-block
https://mcp.stripe.com
```

[Supabase(opens in new tab)](https://supabase.com/docs/guides/getting-started/mcp)

Manage databases, authentication, and storage

URL



``` inline-block
https://mcp.supabase.com/mcp
```

[Vercel(opens in new tab)](https://vercel.com/docs/mcp/vercel-mcp)

Analyze, debug, and manage projects and deployments

URL



``` inline-block
https://mcp.vercel.com/
```

[Wix(opens in new tab)](https://dev.wix.com/docs/sdk/articles/use-the-wix-mcp/about-the-wix-mcp)

Manage and build sites and apps on Wix

URL



``` inline-block
https://mcp.wix.com/mcp
```

[Coupler.io(opens in new tab)](https://help.coupler.io/article/592-coupler-local-mcp-server)

Access business data from hundreds of sources

URL



``` inline-block
https://mcp.coupler.io/mcp/
```

[Dice(opens in new tab)](https://www.dice.com/about/mcp)

Find active tech jobs on Dice

URL



``` inline-block
https://mcp.dice.com/mcp
```

[Miro(opens in new tab)](https://developers.miro.com/docs/miro-mcp)

Access and create new content on Miro boards

URL



``` inline-block
https://mcp.miro.com/
```

[Port IO(opens in new tab)](https://docs.port.io/ai-interfaces/port-mcp-server/overview-and-installation)

Search your context lake and safely run actions

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.port.io/ai-interfaces/port-mcp-server/overview-and-installation/?mcp-setup=claude&region=eu#installing-port-mcp)

[Aiwyn Tax (formerly Column Tax)(opens in new tab)](https://docs.columntax.com/page/aiwyn-tax-mcp-server)

Estimate your federal & state taxes with Aiwyn's tax engine

URL



``` inline-block
https://mcp.columnapi.com/mcp
```

[Circleback(opens in new tab)](https://circleback.ai/docs/mcp)

Search and access context from meetings

URL



``` inline-block
https://app.circleback.ai/api/mcp
```

[Clarify(opens in new tab)](https://docs.clarify.ai/en/articles/13367278-clarify-mcp)

Query your CRM. Create records. Ask anything.

URL



``` inline-block
https://api.clarify.ai/mcp
```

[Clarity AI(opens in new tab)](https://clarity-sfdr20-mcp.pro.clarity.ai/)

Simulate fund classifications under proposed SFDR 2.0

URL



``` inline-block
https://clarity-sfdr20-mcp.pro.clarity.ai/mcp
```

[Day AI(opens in new tab)](https://day.ai/mcp)

Know everything about your prospects & customers with CRMx

URL



``` inline-block
https://day.ai/api/mcp
```

[ICD-10 Codes(opens in new tab)](https://claude.com/resources/tutorials/using-the-icd-10-connector-in-claude)

Access ICD-10-CM and ICD-10-PCS code sets

URL



``` inline-block
https://hcls.mcp.claude.com/icd10_codes/mcp
```

[DevRev(opens in new tab)](https://support.devrev.ai/en-US/devrev/article/ART-21859-remote-mcp-server)

Search and update your company's knowledge graph

URL



``` inline-block
https://api.devrev.ai/mcp/v1
```

[DirectBooker(opens in new tab)](https://www.directbooker.ai/products/mcp-server-documentation)

Compare hotels, then book direct

URL



``` inline-block
https://www.directbooker.ai/claude
```

[Exa(opens in new tab)](https://docs.exa.ai/reference/exa-mcp)

Web Search + Code Docs Search

URL



``` inline-block
https://mcp.exa.ai/mcp
```

[Fathom(opens in new tab)](https://help.fathom.video/en/articles/11497793)

Your meetings, now part of every Claude conversation

URL



``` inline-block
https://api.fathom.ai/mcp
```

[Fireflies(opens in new tab)](https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol)

Analyze and generate insights from meeting transcripts

URL



``` inline-block
https://api.fireflies.ai/mcp
```

[Fiscal.ai(opens in new tab)](https://docs.fiscal.ai/docs/guides/mcp-integration)

Clean Public Equity Fundamental Data

URL



``` inline-block
https://api.fiscal.ai/mcp/sse
```

[Granola(opens in new tab)](https://help.granola.ai/article/granola-mcp#set-up-guide)

The AI notepad for meetings

URL



``` inline-block
https://mcp.granola.ai/mcp
```

[Harmonic(opens in new tab)](https://support.harmonic.ai/en/articles/12785899-harmonic-mcp-server-getting-started-guide)

Discover, research, and enrich companies and people

URL



``` inline-block
https://mcp.api.harmonic.ai
```

[Klarity(opens in new tab)](https://github.com/Klarity-AI/klarity-mcp/blob/main/skills/klarity-process-context-graph/SKILL.md)

Explore your org's processes

URL



``` inline-block
https://architect-v2-api.klarity.ai/mcp
```

[Krisp(opens in new tab)](https://help.krisp.ai/hc/en-us/articles/25416265429660-Krisp-MCP-Supported-tools)

Add your meetings context via transcripts and notes

URL



``` inline-block
https://mcp.krisp.ai/mcp
```

[Lawve AI(opens in new tab)](https://lawve.ai/en/learn/mcp-setup)

Discover expert-written skills for legal work

URL



``` inline-block
https://mcp.lawve.ai/mcp
```

[Lorikeet(opens in new tab)](https://docs.lorikeetcx.ai/mcp/mcp-server)

A universal concierge for complex businesses

URL



``` inline-block
https://mcp.lorikeetcx.ai
```

[LunarCrush(opens in new tab)](https://lunarcrush.com/developers/api/ai)

Add real-time social media data to your searches

URL



``` inline-block
https://lunarcrush.ai/mcp
```

[Mem(opens in new tab)](https://docs.mem.ai/mcp/overview)

The AI notebook for everything on your mind

URL



``` inline-block
https://mcp.mem.ai/mcp
```

[Metaview(opens in new tab)](https://support.metaview.ai/integrations/mcp-integration/mcp-overview.mdx)

The AI platform for recruiting.

URL



``` inline-block
https://mcp.metaview.ai/mcp
```

[Otter.ai(opens in new tab)](https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server)

Unlock your meeting intelligence

URL



``` inline-block
https://mcp.otter.ai/mcp
```

[Peec AI(opens in new tab)](https://docs.peec.ai/mcp/introduction)

Analyze your brand's visibility across LLMs

URL



``` inline-block
https://api.peec.ai/mcp
```

[Read AI(opens in new tab)](https://support.read.ai/hc/en-us/articles/49381158409491-MCP-Server)

Bring your meetings into Claude

URL



``` inline-block
https://api.read.ai/mcp
```

[Scholar Gateway(opens in new tab)](https://docs.scholargateway.ai)

Enhance responses with scholarly research and citations

URL



``` inline-block
https://connector.scholargateway.ai/mcp
```

[Scite(opens in new tab)](https://scite.ai/mcp)

Evidence-based answers grounded in research

URL



``` inline-block
https://api.scite.ai/mcp
```

[Sprouts Data Intelligence(opens in new tab)](https://support.sprouts.ai/en/articles/13384582-sprouts-mcp-server-documentation#h_541c149a52)

From query to qualified lead in seconds.

URL



``` inline-block
https://sprouts-mcp-server.kartikay-dhar.workers.dev
```

[Sybill(opens in new tab)](https://api.sybill.ai/docs/mcp.html)

Ask AI about your sales calls, deals & pipeline

URL



``` inline-block
https://mcp.sybill.ai/mcp
```

[Tray.ai(opens in new tab)](https://tray.ai/documentation/platform/artificial-intelligence/agent-gateway/connecting-clients)

Automate 700+ apps & workflows with governance

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://tray.ai/documentation/platform/artificial-intelligence/agent-gateway/connecting-clients)

[Vibe Prospecting(opens in new tab)](https://developers.explorium.ai/mcp-docs/agentsource-mcp)

Find company & contact data

URL



``` inline-block
https://vibeprospecting.explorium.ai/mcp
```

[Windsor.ai(opens in new tab)](https://windsor.ai/introducing-windsor-mcp/#method-1-using-claude-desktop-3)

Connect Meta Ads, Google Ads, TikTok Ads, LinkedIn Ads + 320 more

URL



``` inline-block
https://mcp.windsor.ai
```

[Era Context(opens in new tab)](https://era.app/help/mcp-server-era-context/)

Manage your personal finances using Claude

URL



``` inline-block
https://context.era.app
```

[Fellow.ai(opens in new tab)](https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server)

Chat with your meetings to uncover actionable insights

URL



``` inline-block
https://fellow.app/mcp
```

[Gamma(opens in new tab)](https://gamma.app/docs/Gamma-MCP-Server-Documentation-m6p43kobgzy15zj?mode=doc)

Create presentations, docs, socials, and sites with AI

URL



``` inline-block
https://mcp.gamma.app/mcp
```

[Lucid(opens in new tab)](https://help.lucid.co/hc/en-us/articles/42578801807508-Integrate-Lucid-with-AI-tools-using-the-Lucid-MCP-server)

Ideate, diagram, and align teams

URL



``` inline-block
https://mcp.lucid.app/mcp
```

[Natoma(opens in new tab)](https://docs.natoma.ai)

Access all your internal tools, enterprise apps & data.

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://natoma.app/?utm=claude)

[NetDocuments(opens in new tab)](https://support.netdocuments.com/)

Securely access your documents in NetDocuments

[Netlify(opens in new tab)](https://docs.netlify.com/build/build-with-ai/netlify-mcp-server/)

Create, deploy, manage, and secure websites on Netlify.

URL



``` inline-block
https://netlify-mcp.netlify.app/mcp
```

[ThoughtSpot Spotter(opens in new tab)](https://developers.thoughtspot.com/docs/mcp-integration#_add_mcp_server_to_the_mcp_clients_config)

Your AI data analyst, from question to trusted insights

URL



``` inline-block
https://agent.thoughtspot.app/mcp?api-version=latest
```

[AWS Marketplace(opens in new tab)](https://docs.aws.amazon.com/marketplace/latest/APIReference/marketplace-mcp-server.html)

Discover, evaluate, and buy solutions for the cloud

URL



``` inline-block
https://marketplace-mcp.us-east-1.api.aws/mcp
```

[Synthesize Bio(opens in new tab)](https://app.synthesize.bio/mcp/docs)

Generate gene expression from a virtual human

URL



``` inline-block
https://app.synthesize.bio/api/mcp
```

[Kindora Funder Discovery(opens in new tab)](https://kindora.co/mcp)

Find funders who support causes like yours

URL



``` inline-block
https://kindora-mcp.azurewebsites.net/mcp/
```

[Omni Analytics(opens in new tab)](https://docs.omni.co/ai/mcp)

Query your data using natural language through Omni's semantic model

URL



``` inline-block
https://callbacks.omniapp.co/callback/mcp
```

[Send(opens in new tab)](https://www.send.co/mcp/docs)

Create shareable documents, one-pagers, and decks

URL



``` inline-block
https://www.send.co/mcp
```

[Shapes(opens in new tab)](https://mcp.shapes.co)

Analyse your live people data, right in Claude

URL



``` inline-block
https://mcp.shapes.co/mcp
```

[Lloyd by The L Suite(opens in new tab)](https://docs.google.com/document/d/1glRh-BdxnTPxzM1cZLzCcmlgIW5-dQ4-NnnStfhI6vk/edit?tab=t.0#heading=h.hgwkvyizzdb3)

Inhouse counsel insights for members of The L Suite

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.google.com/forms/d/e/1FAIpQLSeK2KFt1G1XbqgQdp2J-cvnLDtiUDigSsTjFH-Hk_B-Va0pRw/viewform?usp=publish-editor)

[TopCounsel by The L Suite(opens in new tab)](https://docs.google.com/document/d/1jcekau3Njlc5XfSspSdSGu7qSgKvM00M6DrYm91ZTzA/edit?tab=t.0#heading=h.hgwkvyizzdb3)

Outside Counsel recommendations from Inhouse Counsel

URL



``` inline-block
https://api.techgc.co/api/mcp/topcounsel
```

[ActiveCampaign(opens in new tab)](https://developers.activecampaign.com/page/mcp)

Autonomous marketing to transform how you work

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://developers.activecampaign.com/page/mcp)

[Adobe Experience Manager(opens in new tab)](https://www.adobe.com/go/aem_claude_mcp_docs)

Manage your Adobe Experience Manager content

URL



``` inline-block
https://mcp.adobeaemcloud.com/adobe/mcp/aem
```

[Ahrefs(opens in new tab)](https://docs.ahrefs.com/docs/mcp/reference/introduction)

SEO & AI search analytics

URL



``` inline-block
https://api.ahrefs.com/mcp/mcp
```

[AirOps(opens in new tab)](https://docs.airops.com/mcp)

Craft content that wins AI search

URL



``` inline-block
https://app.airops.com/mcp
```

[Airtable(opens in new tab)](https://support.airtable.com/docs/using-the-airtable-mcp-server)

Bring your structured data to Claude

URL



``` inline-block
https://mcp.airtable.com/mcp
```

[Airwallex Developer(opens in new tab)](https://www.airwallex.com/docs/developer-tools/ai/developer-mcp)

Integrate with the Airwallex Platform using Claude

URL



``` inline-block
https://mcp-demo.airwallex.com/developer
```

[AllTrails(opens in new tab)](https://support.alltrails.com/hc/en-us/articles/47343827423764-AllTrails-integrations-with-AI-services)

Find your next hike

URL



``` inline-block
https://www.alltrails.com/mcp
```

[Attio(opens in new tab)](https://docs.attio.com/mcp/overview)

Search, manage, and update your Attio CRM from Claude

URL



``` inline-block
https://mcp.attio.com/mcp
```

[Audible(opens in new tab)](https://help.audible.com/s/article/connect-audible-to-claude?language=en_US)

Ask for audiobook recommendations

URL



``` inline-block
https://mcp.audible.com/mcp
```

[Autodesk Product Help(opens in new tab)](https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_KnowledgeMcp_autodesk_product_help_mcp_server_html)

Securely access Autodesk's help documentation

URL



``` inline-block
https://developer.api.autodesk.com/knowledge/public/v1/mcp
```

[Base44(opens in new tab)](https://docs.base44.com/developers/backend/overview/mcp-server)

Build and manage Base44 apps

URL



``` inline-block
https://app.base44.com/mcp
```

[Benchling(opens in new tab)](https://help.benchling.com/hc/en-us/articles/40342713479437-Benchling-MCP)

Connect to R&D data, source experiments, and notebooks

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://help.benchling.com/hc/en-us/articles/40342713479437-Benchling-MCP)

[BioRender(opens in new tab)](https://help.biorender.com/hc/en-gb/articles/30870978672157-How-to-use-the-BioRender-MCP-connector)

Search for and use scientific templates and icons

URL



``` inline-block
https://mcp.services.biorender.com/mcp
```

[Bitly(opens in new tab)](https://dev.bitly.com/bitly-mcp/)

Shorten links, generate QR Codes, and track performance

URL



``` inline-block
https://api-ssl.bitly.com/v4/mcp
```

[MT Newswires(opens in new tab)](https://console.blueskyapi.com/docs/EDGE/news/MT_NEWSWIRES_Global#mcp)

Trusted real-time global financial news provider

URL



``` inline-block
https://vast-mcp.blueskyapi.com/mcp
```

[Booking.com(opens in new tab)](https://developers.booking.com/mcp/booking-connector/about)

Find hotels, homes and more

URL



``` inline-block
https://demandapi-mcp.booking.com/v1/mcp/8132308
```

[Box(opens in new tab)](https://developer.box.com/guides/box-mcp)

Search, edit and get insights on your Box content

URL



``` inline-block
https://mcp.box.com
```

[Brex(opens in new tab)](https://www.brex.com/support/using-brex-in-ai-apps)

Intelligent finance automation

URL



``` inline-block
https://api.brex.com/mcp
```

[Orion by Gravity(opens in new tab)](http://docs.runorion.com/)

Get insights from your autonomous AI analyst

URL



``` inline-block
https://g.runorion.com/mcp
```

[Calendly(opens in new tab)](https://help.calendly.com/hc/en-us/articles/36734570264855-Connect-Calendly-to-your-AI-tools-with-Calendly-MCP)

Manage event types, availability, and bookings.

URL



``` inline-block
https://mcp.calendly.com
```

[Canva(opens in new tab)](https://www.canva.dev/docs/connect/canva-mcp-server-setup/)

Search, create, autofill, and export Canva designs

URL



``` inline-block
https://mcp.canva.com/mcp
```

[Carta(opens in new tab)](https://docs.carta.com/api-platform/docs/claude-plugins-setup)

The connected ERP for private capital

URL



``` inline-block
https://mcp.app.carta.com/mcp
```

[CB Insights(opens in new tab)](https://mcp.cbinsights.com)

Predictive intelligence on private companies

URL



``` inline-block
https://mcp.cbinsights.com
```

[CData Connect AI(opens in new tab)](https://cloud.cdata.com/docs/Claude-Client.html)

Managed MCP platform for 350 sources

URL



``` inline-block
https://mcp.cloud.cdata.com/mcp
```

[Microsoft 365(opens in new tab)](https://support.claude.com/en/articles/12542951-enabling-and-using-the-microsoft-365-connector)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

URL



``` inline-block
https://microsoft365.mcp.claude.com/mcp
```

[PubMed(opens in new tab)](https://support.claude.com/en/)

Search biomedical literature from PubMed

URL



``` inline-block
https://pubmed.mcp.claude.com/mcp
```

[Clay(opens in new tab)](https://www.notion.so/clayrun/Clay-Claude-MCP-Server-Documentation-2ef7e66eb01480c9820de48041591aeb?showMoveTo=true&saveParent=true)

Find prospects. Research accounts. Personalize outreach

URL



``` inline-block
https://api.clay.com/v3/mcp
```

[Clerk(opens in new tab)](https://clerk.com/docs/guides/ai/mcp/clerk-mcp-server)

Add authentication, organizations, and billing

URL



``` inline-block
https://mcp.clerk.com/mcp
```

[ClickUp(opens in new tab)](https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP)

Project management & collaboration for teams & agents

URL



``` inline-block
https://mcp.clickup.com/mcp
```

[iManage Work(opens in new tab)](https://docs.imanage.com/cloud/mcpconnector-user-help/en-US/iManage_MCP_Connector_Help.html)

Governed knowledge. AI ready.

URL



``` inline-block
https://cloudimanage.com/mcp/work
```

[Cloudinary(opens in new tab)](https://cloudinary.com/documentation/cloudinary_llm_mcp#available_mcp_servers)

Manage, transform and deliver your images & videos

URL



``` inline-block
https://asset-management.mcp.cloudinary.com/sse
```

[CoinDesk(opens in new tab)](https://mcp.coindesk.com/)

Access Live & Historical Crypto Data, Indices

URL



``` inline-block
https://mcp.coindesk.com/mcp
```

[Consensus(opens in new tab)](https://docs.consensus.app/docs/mcp)

Explore scientific research

URL



``` inline-block
https://mcp.consensus.app/mcp
```

[Aurora(opens in new tab)](https://mcp-docs.ai.consilio.com)

Search your Consilio matters, docs, and more.

URL



``` inline-block
https://mcp.ai.consilio.com
```

[Contentsquare(opens in new tab)](https://support.contentsquare.com/hc/en-us/articles/41563169756945-Model-Context-Protocol-MCP)

Experience analytics platform for digital businesses

URL



``` inline-block
https://api.contentsquare.com/mcp
```

[Context7(opens in new tab)](https://context7.com/docs/overview)

Up-to-date docs for LLMs and AI code editors

URL



``` inline-block
https://mcp.context7.com/mcp
```

[CourtListener(opens in new tab)](https://github.com/freelawproject/courtlistener-api-client/blob/main/MCP_README.md)

Legal research across millions of court records

URL



``` inline-block
https://mcp.courtlistener.com/
```

[Courtroom5(opens in new tab)](https://courtroom5.com/claude)

Civil legal guidance for self-represented litigants

URL



``` inline-block
https://mcp.courtroom5.com/v1
```

[Intuit Credit Karma(opens in new tab)](https://support.creditkarma.com/s/article/Intuit-Credit-Karma-on-Claude-and-ChatGPT)

Credit score factors & insights

URL



``` inline-block
https://anthropic.mcp.creditkarma.com/mcp
```

[Crossbeam(opens in new tab)](https://help.crossbeam.com/en/articles/12601327-crossbeam-mcp-server-beta)

Explore partner data and ecosystem insights in Claude

URL



``` inline-block
https://mcp.crossbeam.com
```

[Crypto.com(opens in new tab)](https://mcp.crypto.com/docs)

Real time prices, orders, charts, and more for crypto

URL



``` inline-block
https://mcp.crypto.com/market-data/mcp
```

[Daloopa(opens in new tab)](https://docs.daloopa.com/docs/daloopa-mcp#/)

Financial fundamental data and KPIs with hyperlinks

URL



``` inline-block
https://mcp.daloopa.com/server/mcp
```

[Databricks(opens in new tab)](https://docs.databricks.com/aws/en/generative-ai/mcp/connect-external-services)

Managed MCP servers with Unity Catalog and Mosaic AI

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.databricks.com/aws/en/generative-ai/mcp/connect-external-services)

[Datadog(opens in new tab)](https://docs.datadoghq.com/bits_ai/mcp_server/)

Debug and resolve issues using Datadog telemetry

[Datasite(opens in new tab)](https://app.global.datasite.com/dev-portal/guides/mcp-server)

Manage your M&A data room from Claude

URL



``` inline-block
https://mcp.global.datasite.com/mcp
```

[Definely(opens in new tab)](https://help.definely.com/en/articles/634922-definely-connector-for-claude-user-guide)

Structured contract review tools for legal teams

URL



``` inline-block
https://mcp.app.definely.com
```

[Descript(opens in new tab)](https://help.descript.com/hc/en-us/articles/45008080343053-Connect-Descript-to-Claude)

Import, edit, or create video with prompts

URL



``` inline-block
https://api.descript.com/v2/mcp/claude
```

[Descrybe Legal Engine(opens in new tab)](https://app.descrybe.com/connect/docs)

Ground your work in clean, structured U.S. primary law

URL



``` inline-block
https://mcp.descrybe.com/mcp
```

[Digits(opens in new tab)](https://help.digits.com/business-connections/digits-mcp-claude)

Track and analyze your finances with Digits

URL



``` inline-block
https://api.digits.com/mcp
```

[D&B Risk Analytics(opens in new tab)](https://view.highspot.com/viewer/2b3c0624606b4d64eb092106b47ad14c)

Execute risk workflows powered by the D&B Commercial Graph™

URL



``` inline-block
https://agents.riskanalytics.dnb.com/mcp
```

[DocuSeal(opens in new tab)](https://www.docuseal.com/guides/integrate-with-ai-agents-using-mcp)

Sign, send & manage documents with DocuSeal

URL



``` inline-block
https://docuseal.com/mcp
```

[Dovetail(opens in new tab)](https://developers.dovetail.com/docs/mcp)

Turn scattered feedback into decisions grounded in customer evidence

URL



``` inline-block
https://dovetail.com/api/mcp
```

[Dremio Cloud(opens in new tab)](https://docs.dremio.com/cloud/sonar/mcp-server/)

Analyze and get insights from your lakehouse data

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.dremio.com/cloud/sonar/mcp-server/)

[Enterpret(opens in new tab)](https://helpcenter.enterpret.com/en/articles/12665166-wisdom-mcp-server)

Get answers from unified feedback of your customers.

URL



``` inline-block
https://wisdom-api.enterpret.com/server/mcp
```

[Euler(opens in new tab)](https://mcp.eulerapp.com/public/docs)

Chat and manage your entire partner program.

URL



``` inline-block
https://mcp.eulerapp.com/mcp
```

[Everlaw(opens in new tab)](https://support.everlaw.com/hc/en-us/articles/50274473477915)

Search and explore your Everlaw database in Claude.

URL



``` inline-block
https://api.everlaw.com/v1/mcp
```

[Expedia(opens in new tab)](https://www.expedia.com/playground/mcp/doc/)

Plan trips, flights and hotels

URL



``` inline-block
https://www.expedia.com/mcp
```

[Fever Event Discovery(opens in new tab)](https://developer.feverup.com/)

Discover live entertainment events worldwide

URL



``` inline-block
https://data-search.apigw.feverup.com/mcp
```

[FMP(opens in new tab)](https://financialmodelingprep.com/developer/docs/mcp-server?utm_source=claude)

Comprehensive financial market data

URL



``` inline-block
https://financialmodelingprep.com/mcp
```

[G2(opens in new tab)](https://documentation.g2.com/docs/g2-mcp-server)

Bring real buyer signals into AI workflows

URL



``` inline-block
https://mcp.g2.com/mcp
```

[Monte Carlo(opens in new tab)](https://docs.getmontecarlo.com/docs/mcp-server)

Data & AI observability

URL



``` inline-block
https://mcp.getmontecarlo.com/mcp
```

[Glean(opens in new tab)](https://docs.glean.com/administration/platform/mcp/about)

Bring enterprise context to Claude and your AI tools

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.glean.com/administration/platform/mcp/about)

[Glovo(opens in new tab)](https://glovoapp.com/docs/en/legal/mcp/)

Anything delivered in minutes

URL



``` inline-block
https://api.glovoapp.com/discovery-mcp/mcp
```

[GoCardless(opens in new tab)](https://developer.gocardless.com/developer-tools/mcp/)

Build GoCardless payment API integrations

URL



``` inline-block
https://mcp.gocardless.com
```

[GoDaddy(opens in new tab)](https://developer.godaddy.com/mcp)

Search domains and check availability

URL



``` inline-block
https://api.godaddy.com/v1/domains/mcp
```

[Goodnotes(opens in new tab)](https://www.notion.so/goodnotes-team/Goodnotes-MCP-Server-Documentation-320b740273d28187a23ad52780a37620)

Turn AI insights into documents

URL



``` inline-block
https://claude-mcp-api.ml.goodnotes.com/mcp
```

[Google Cloud BigQuery(opens in new tab)](https://cloud.google.com/bigquery/docs/use-bigquery-mcp)

BigQuery: Advanced analytical insights for agents

URL



``` inline-block
https://bigquery.googleapis.com/mcp
```

[Google Compute Engine(opens in new tab)](https://cloud.google.com/docs)

MCP server for Google Compute Engine

URL



``` inline-block
https://compute.googleapis.com/mcp
```

[Google Calendar(opens in new tab)](https://developers.google.com/workspace/calendar)

Manage your schedule and coordinate meetings effortlessly

URL



``` inline-block
https://calendarmcp.googleapis.com/mcp/v1
```

[Google Drive(opens in new tab)](https://developers.google.com/workspace/drive)

Search, read, and upload files instantly

URL



``` inline-block
https://drivemcp.googleapis.com/mcp/v1
```

[Gmail(opens in new tab)](https://developers.google.com/workspace/gmail)

Draft replies, summarize threads, & search your inbox

URL



``` inline-block
https://gmailmcp.googleapis.com/mcp/v1
```

[GovTribe(opens in new tab)](https://docs.govtribe.com/user-guide/integrations/govtribe-mcp)

Search government procurement & spending data

URL



``` inline-block
https://govtribe.com/mcp
```

[Grain(opens in new tab)](https://developers.grain.com/mcp)

Put your meetings to work

URL



``` inline-block
https://api.grain.com/_/mcp
```

[Granted(opens in new tab)](https://grantedai.com/mcp)

Discover every grant opportunity in existence.

URL



``` inline-block
https://grantedai.com/api/mcp/mcp
```

[Guidepoint(opens in new tab)](https://clapi-developer.guidepoint.io/mcp/docs)

Real-time access to trusted expert knowledge

URL



``` inline-block
https://clapi.guidepoint.io/mcp-server/v1/mcp
```

[Gusto(opens in new tab)](https://docs.gusto.com/app-integrations/docs/mcp)

Query and analyze your Gusto data

URL



``` inline-block
https://mcp.api.gusto.com/anthropic
```

[Phoenix by HG Insights(opens in new tab)](https://phoenix.hginsights.com/docs/intro)

AI-powered B2B data intelligence & analytics

URL



``` inline-block
https://phoenix.hginsights.com/api/ai/mcp
```

[HubSpot(opens in new tab)](https://knowledge.hubspot.com/integrations/set-up-and-use-the-hubspot-connector-for-claude)

Chat with your CRM data to get personalized insights

URL



``` inline-block
https://mcp.hubspot.com/anthropic
```

[IBISWorld(opens in new tab)](https://help.ibisworld.com/en/articles/14627556-ibisworld-mcp-server-documentation)

Financials, risk data and analysis on 50,000 industries

URL



``` inline-block
https://mcp.ibisworld.com
```

[Interactive Brokers (IBKR)(opens in new tab)](https://www.interactivebrokers.com/lib/cstools/faq/#/content/1442566213)

Trade, invest, analyze, and manage global markets

URL



``` inline-block
https://api.ibkr.com/v1/api/mcp
```

[ICE Data Services(opens in new tab)](https://www.ice.com/ieoauoau)

Analyze U.S. fixed income trade and reference data

URL



``` inline-block
https://fids-mcp.ice.com/mcp
```

[IFTTT(opens in new tab)](https://ift.tt/ai_assistants)

Connect, control, and automate 1,000+ apps with IFTTT

URL



``` inline-block
https://ifttt.com/mcp
```

[Medidata(opens in new tab)](https://learn.medidata.com/en-US/bundle/mcp-server-documentation/page/medidata_mcp_server_documentation.html)

Clinical trial software and site ranking tools

URL



``` inline-block
https://mcp.imedidata.com/mcp
```

[Indeed(opens in new tab)](https://docs.indeed.com/mcp)

Search for jobs on Indeed

URL



``` inline-block
https://mcp.indeed.com/claude/mcp
```

[Instacart(opens in new tab)](https://docs.instacart.com/mcp_servers/)

Groceries and more delivered as fast as 30 minutes

URL



``` inline-block
https://fig-mcp.instacart.com/mcp
```

[Intercom(opens in new tab)](https://developers.intercom.com/docs/guides/mcp)

Access to Intercom data for better customer insights

URL



``` inline-block
https://mcp.intercom.com/mcp
```

[Intuit Mailchimp(opens in new tab)](https://mailchimp.com/help/use-mailchimp-connector-claude)

Create marketing campaigns

URL



``` inline-block
https://ai-inc.mailchimp.com/claude/mcp/v2
```

[Intuit QuickBooks(opens in new tab)](https://quickbooks.intuit.com/learn-support/en-us/help-article/accounting-bookkeeping/use-quickbooks-connector-claude/L3YBlo6Ht_US_en_US?uid=mmzgz9ag)

Business Finances made simple

URL



``` inline-block
https://ai-inc.quickbooks.intuit.com/v1/mcp
```

[Intuit TurboTax(opens in new tab)](https://ttlc.intuit.com/turbotax-support/en-us/help-article/tax-return/access-turbotax-tools-claude)

Estimate tax refunds and connect with live tax experts

URL



``` inline-block
https://ai-inc.turbotax.intuit.com/358A1C1B-F73B-46A7-B130-4B14916E6843/v1/mcp
```

[Ironclad Contracts(opens in new tab)](https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server)

Plain language search for faster contract answers

[Jentic(opens in new tab)](https://docs.jentic.com/guides/mcp/remote-mcp/)

One connection to access all your tools securely

URL



``` inline-block
https://api.jentic.com/mcp
```

[PlayMCP(opens in new tab)](https://www.notion.so/2189b97b4888803dbbdcef264e7eff58)

Connect and use PlayMCP servers in your toolbox

URL



``` inline-block
https://playmcp.kakao.com/mcp
```

[S&P Global(opens in new tab)](https://docs.kensho.com/llmreadyapi/mcp)

Query a range of S&P Global datasets

URL



``` inline-block
https://kfinance.kensho.com/integrations/mcp
```

[Ketryx(opens in new tab)](https://docs.ketryx.com/reference/ketryx-mcp-server)

Search and explore regulated software lifecycle data

URL



``` inline-block
https://app.ketryx.com/api/mcp
```

[Kiwi.com(opens in new tab)](https://mcp-install-instructions.alpic.cloud/servers/kiwi-com-flight-search)

Search flights in Claude

URL



``` inline-block
https://mcp.kiwi.com
```

[Klaviyo(opens in new tab)](https://developers.klaviyo.com/en/docs/klaviyo_mcp_server)

Report, strategize & create with real-time Klaviyo data

URL



``` inline-block
https://mcp.klaviyo.com/mcp?include-mcp-app=true
```

[lastminute.com(opens in new tab)](https://mcp.lastminute.com/docs)

Search, compare and book flights, dynamic packages (flight + hotel) and hotels across global airlines and hotel suppliers.

URL



``` inline-block
https://mcp.lastminute.com/mcp
```

[Legal Data Hunter(opens in new tab)](https://legaldatahunter.com/docs)

Search 23M+ legal docs in 160+ jurisdictions.

URL



``` inline-block
https://legaldatahunter.com/mcp
```

[LILT(opens in new tab)](https://support.lilt.com/kb/LILT-mcp)

High-quality translation with human verification

URL



``` inline-block
https://mcp.lilt.com/mcp
```

[Local Falcon(opens in new tab)](https://github.com/local-falcon/mcp)

AI visibility and local search intelligence platform

URL



``` inline-block
https://mcp.localfalcon.com
```

[LSEG(opens in new tab)](https://www.lseg.com/en/solutions/ai-finance-solutions/anthropic)

Access best in class data & analytics across a broad spectrum of asset classes.

URL



``` inline-block
https://api.analytics.lseg.com/lfa/mcp/server-cl
```

[Lumin(opens in new tab)](https://github.com/luminpdf/lumin-mcp-server)

Manage documents, send signature requests, and convert Markdown to PDF

URL



``` inline-block
https://mcp.luminpdf.com/mcp
```

[Lusha(opens in new tab)](https://docs.lusha.com/mcp-docs)

Find and enrich B2B contacts and companies

URL



``` inline-block
https://mcp.lusha.com/mcp/claude
```

[Magic Patterns(opens in new tab)](https://www.magicpatterns.com/docs/documentation/features/mcp-server/overview)

Discuss and iterate on Magic Patterns designs

URL



``` inline-block
https://mcp.magicpatterns.com/mcp
```

[MailerLite(opens in new tab)](https://developers.mailerlite.com/mcp/#how-mcp-works)

Turn Claude into your email marketing assistant

URL



``` inline-block
https://mcp.mailerlite.com/mcp
```

[Make(opens in new tab)](https://developers.make.com/mcp-server/)

Run Make scenarios and manage your Make account

URL



``` inline-block
https://mcp.make.com
```

[Malwarebytes(opens in new tab)](https://help.malwarebytes.com/hc/en-us/articles/47985341083675-Using-Malwarebytes-in-Claude)

Check links, phones, and emails for scams

URL



``` inline-block
https://scamguard.malwarebytes.com/claude/mcp
```

[Melon(opens in new tab)](https://tech.kakaoent.com/ai/using-melon-mcp-server-en/)

Browse music charts & your personalized music picks

URL



``` inline-block
https://mcp.melon.com/mcp/
```

[Mercury(opens in new tab)](https://docs.mercury.com/docs/connecting-mercury-mcp)

Search, analyze and understand your finances on Mercury

URL



``` inline-block
https://mcp.mercury.com/mcp
```

[Metabase(opens in new tab)](https://www.metabase.com/docs/latest/ai/mcp)

Query and explore your Metabase data

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://www.metabase.com/docs/latest/ai/mcp)

[Microsoft Learn(opens in new tab)](https://learn.microsoft.com/en-us/training/support/mcp)

Search trusted Microsoft docs to power your development

URL



``` inline-block
https://learn.microsoft.com/api/mcp
```

[Mintlify(opens in new tab)](https://www.mintlify.com/docs/ai/mintlify-mcp)

Search, read, and edit your documentation

URL



``` inline-block
https://mcp.mintlify.com
```

[Mixpanel(opens in new tab)](https://docs.mixpanel.com/docs/features/mcp)

Analyze, query, and manage your Mixpanel data

URL



``` inline-block
https://mcp.mixpanel.com/mcp
```

[Moody's(opens in new tab)](https://www.moodys.com/web/en/us/genai/model-context-protocol.html)

Risk insights, analytics, and decision intelligence

URL



``` inline-block
https://api.moodys.com/genai-ready-data/m1/mcp
```

[Morningstar(opens in new tab)](https://developer.morningstar.com/direct-web-services/documentation/mcp-server/morningstar-mcp-server)

Up-to-date investment and market insights

URL



``` inline-block
https://mcp.morningstar.com/mcp
```

[MotherDuck(opens in new tab)](https://motherduck.com/docs/sql-reference/mcp/)

Get answers from your data

URL



``` inline-block
https://api.motherduck.com/mcp
```

[Motion Creative Analytics(opens in new tab)](https://help.motionapp.com/en/articles/14315735-motion-mcp)

Analyze your Meta ad creative & competitor ad libraries

URL



``` inline-block
https://projects.motionapp.com/mcp
```

[MSCI(opens in new tab)](https://www.msci.com/downloads/web/msci-com/data-and-analytics/private-asset-solutions/ai-for-private-markets/msci-mcp-msci-connector-user-guide.pdf)

Turn data into insight

URL



``` inline-block
https://mcp.msci.com/mcp/v1.0/mcp
```

[NetSuite(opens in new tab)](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_7200233106.html)

Connect Claude to NetSuite data for analysis & insights

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://system.netsuite.com/mcp/mcpinfo.nl)

[Owkin(opens in new tab)](https://docs.owkin.com/core-features-and-usage)

Interact with AI agents built for biology

URL



``` inline-block
https://mcp.k.owkin.com/mcp
```

[PagerDuty(opens in new tab)](https://developer.pagerduty.com/docs/mcp-tooling-remote-server)

Manage incidents, services and on-call schedules

URL



``` inline-block
https://mcp.pagerduty.com/mcp
```

[PandaDoc(opens in new tab)](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server)

Create, send, sign and track documents

URL



``` inline-block
https://mcp.pandadoc.com/v1/mcp
```

[Pigment(opens in new tab)](https://kb.pigment.com/docs/mcp-server)

Analyze business data

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://kb.pigment.com/docs/mcp-server)

[PitchBook Premium(opens in new tab)](https://help.pitchbook.com/s/article/PitchBook-Premium-for-Claude-by-Anthropic)

PitchBook data, embedded in the way you work.

URL



``` inline-block
https://premium.mcp.pitchbook.com/mcp
```

[Polar Analytics(opens in new tab)](https://intercom.help/polar-app/en/collections/17268490-polar-mcp)

Bring all your data in one place & connect it to Claude

URL



``` inline-block
https://api.polaranalytics.com/mcp
```

[Postman(opens in new tab)](https://github.com/postmanlabs/postman-mcp-server)

Give API context to your coding agents

URL



``` inline-block
https://mcp.postman.com/minimal
```

[Privacy.com(opens in new tab)](https://developers.privacy.com/docs/mcp-server)

Manage virtual cards and track your spending patterns

URL



``` inline-block
https://mcp.privacy.com
```

[Quartr(opens in new tab)](https://mcp.quartr.com/docs)

Financial data and AI infrastructure for company research.

URL



``` inline-block
https://mcp.quartr.com/mcp
```

[Quo(opens in new tab)](https://support.quo.com/core-concepts/integrations/mcp)

Surface call insights and missed opportunities

URL



``` inline-block
https://mcp.quo.com/mcp
```

[Ramp(opens in new tab)](https://docs.ramp.com/developer-api/v1/guides/ramp-mcp-remote)

Search, access, and analyze your Ramp financial data

URL



``` inline-block
https://ramp-mcp-remote.ramp.com/mcp
```

[Ramp Data(opens in new tab)](https://docs.ramp.com/developer-api/v1/ramp-data)

Search and analyze Ramp spend across 50,000+ businesses

URL



``` inline-block
https://mcp.ramp.com/ramp-data/anthropic/mcp
```

[Bigdata.com(opens in new tab)](https://docs.bigdata.com/mcp-reference)

Access real-time financial data

URL



``` inline-block
https://mcp.bigdata.com/
```

[Razorpay(opens in new tab)](https://razorpay.com/docs/mcp-server/?preferred-country=IN)

Turn Claude into your Razorpay Dashboard Assistant

URL



``` inline-block
https://mcp.razorpay.com/mcp
```

[Resy(opens in new tab)](https://www.americanexpress.com/content/dam/amex/en-us/credit-cards/benefits/resy/resy_mcp_app_claude.pdf)

Find and book restaurants instantly

URL



``` inline-block
https://apigw.americanexpress.com/dining/v1/mcp
```

[Retool(opens in new tab)](https://docs.retool.com/education/labs/resources/mcp)

Build production apps and manage Retool with AI agents

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.retool.com/education/labs/resources/mcp)

[Rillet(opens in new tab)](https://docs.api.rillet.com/docs/mcp)

Query your live GL and financials in plain English

URL



``` inline-block
https://api.rillet.com/mcp
```

[SandboxAQ(opens in new tab)](https://docs.aisim.sandboxaq.com/)

Large Quantitative Models for scientific discovery

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.aisim.sandboxaq.com/)

[Semrush(opens in new tab)](https://developer.semrush.com/api/introduction/semrush-mcp/)

SEO, market data, and brand visibility insights

URL



``` inline-block
https://mcp.semrush.com/claude/v1/mcp
```

[Shopify(opens in new tab)](https://help.shopify.com/en/manual/apps/connecting-ai-tools)

Build, manage, and analyze your Shopify store

URL



``` inline-block
https://setup.shopify.com/mcp
```

[Sigma(opens in new tab)](https://help.sigmacomputing.com/docs/use-sigma-mcp-server)

Query, search, and explore your data with Sigma

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://help.sigmacomputing.com/docs/use-sigma-mcp-server)

[SignNow(opens in new tab)](https://docs.signnow.com/docs/signnow/mcp-server)

Automate eSignature workflows directly from Claude

URL



``` inline-block
https://mcp-server.signnow.com/mcp
```

[Similarweb(opens in new tab)](https://docs.similarweb.com/api-v5/mcp/mcp-setup)

Real time web, mobile app, and market data.

URL



``` inline-block
https://mcp.similarweb.com
```

[Trimble SketchUp(opens in new tab)](https://help.sketchup.com/en/sketchup-claude-connector)

Create and iterate 3D models for use in SketchUp

URL



``` inline-block
https://api.sketchup.com/mcp/v1/sketchup/mcp
```

[Slack(opens in new tab)](https://docs.slack.dev/ai/mcp-server)

Send messages, create canvases, and fetch Slack data

URL



``` inline-block
https://mcp.slack.com/mcp
```

[Smartsheet(opens in new tab)](https://help.smartsheet.com/articles/2483663-use-smartsheet-connector-claude)

Analyze and manage Smartsheet data with Claude

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://help.smartsheet.com/articles/2483656-install-smartsheet-connector-claude#toc-get-started)

[Snowflake(opens in new tab)](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)

Retrieve both structured and unstructured data

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.snowflake.com/en/user-guide/admin-account-identifier#label-account-name-find)

[Solve Intelligence(opens in new tab)](https://api.solveintelligence.com/guide/mcp/intro/)

Search, draft, and chart patents

URL



``` inline-block
https://api.solveintelligence.com/mcp/
```

[Sourcegraph(opens in new tab)](https://sourcegraph.com/docs/api/mcp#sourcegraph-mcp-server)

Give Claude full enterprise-scale codebase context.

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://sourcegraph.com/docs/api/mcp#sourcegraph-mcp-server)

[Splice(opens in new tab)](https://support.splice.com/en/articles/14442749-getting-started-with-the-splice-mcp-server-beta)

Search Splice's sounds catalog, build stacks & more!

URL



``` inline-block
https://mcp.splice.com/mcp
```

[Spotify(opens in new tab)](https://support.spotify.com/)

Music and podcast recommendations, just for you.

URL



``` inline-block
https://mcp-gateway-external-pilot.spotify.net/mcp
```

[AdisInsight(opens in new tab)](https://adisinsight-mcp.springer.com)

Pharmaceutical drug & clinical trial intelligence

URL



``` inline-block
https://adisinsight-mcp.springer.com/mcp
```

[Order by Cash App(opens in new tab)](https://goose-docs.ai/docs/mcp/cash-app-mcp/)

Discover local food spots and order with a conversation

URL



``` inline-block
https://connect.squareup.com/v2/mcp/cash-app
```

[Square(opens in new tab)](https://developer.squareup.com/docs/mcp)

Search and manage transaction, merchant, and payment data

URL



``` inline-block
https://mcp.squareup.com/sse
```

[StubHub(opens in new tab)](https://support.stubhub.com/articles/61000310240-using-stubhub-in-chatgpt-and-claude)

Find tickets on the World's Largest Ticket Marketplace

URL



``` inline-block
https://open-ai-app.stubhub.net/mcp
```

[Superhuman Mail(opens in new tab)](https://help.superhuman.com/hc/en-us/articles/49810745762067-Superhuman-Mail-MCP-Server-Beta)

The most productive email app ever, for Gmail & Outlook

URL



``` inline-block
https://mcp.mail.superhuman.com/mcp
```

[Supermetrics Marketing Analytics(opens in new tab)](https://mcp.supermetrics.com/docs)

Google Ads, Facebook Ads & 200+ marketing platforms

URL



``` inline-block
https://mcp.supermetrics.com/mcp
```

[SurveyMonkey(opens in new tab)](https://www.surveymonkey.com/apps/BKcduxPnkCN4NFCRokUYCw_3D_3D/details/)

Design surveys, collect responses, and analyze results

URL



``` inline-block
https://mcp.surveymonkey.com/mcp
```

[Taskrabbit Booking Assistance(opens in new tab)](https://docs.google.com/document/d/1tWm33lJx4JdwN-Joqk7vydxQHaRGLod68wdS4k_hY9w/edit?tab=t.edb6z98lya3r#heading=h.2j0sep9c1ren)

Find & book local Taskrabbit services near you

URL



``` inline-block
https://mcp.taskrabbit.com/mcp
```

[Tavily(opens in new tab)](https://docs.tavily.com/documentation/mcp)

Connect your AI agents to the web

URL



``` inline-block
https://mcp.tavily.com/mcp
```

[Third Bridge(opens in new tab)](https://www.thirdbridge.com/en-us/data-solutions/mcp)

Expert-led enhanced insights

URL



``` inline-block
https://ai.thirdbridge.com/mcp/sse
```

[CoCounsel Legal(opens in new tab)](https://legal-mcp.thomsonreuters.com/docs/connector-guide)

Thomson Reuters CoCounsel Legal, in Claude

URL



``` inline-block
https://legal-mcp.thomsonreuters.com/mcp
```

[Thumbtack(opens in new tab)](https://docs.google.com/document/d/1RmGske5ktjAi9d7Ayok_yOv3a6Z2RDBSxIlX7aC5OEM/edit?usp=sharing)

Find and hire local pros in Claude

URL



``` inline-block
https://mcp.thumbtack.com/mcp
```

[Tines(opens in new tab)](https://www.tines.com/docs/actions/templates/mcp-server/)

Securely deploy servers in a matter of seconds in Tines

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://www.tines.com/docs/actions/templates/mcp-server/)

[tldraw(opens in new tab)](https://tldraw.notion.site/tldraw-mcp-app)

Let Claude sketch, draw, and diagram with you

URL



``` inline-block
https://tldraw-mcp-app.tldraw.workers.dev/mcp
```

[Tripadvisor(opens in new tab)](https://www.tripadvisor.com)

Find your perfect hotel based on Tripadvisor reviews

URL



``` inline-block
https://production.ai-mcp-extensibility-prd.tamg.cloud/ogMvjY4De1G7CiHanMOAgddl/mcp
```

[Turkish Airlines(opens in new tab)](https://mcp.turkishtechlab.com/)

Search flights, plan trips, and manage bookings

URL



``` inline-block
https://mcp-app.turkishtechlab.com/mcp
```

[Twilio(opens in new tab)](https://www.twilio.com/docs/ai/mcp)

Build powerful communications and customer engagement

URL



``` inline-block
https://mcp.twilio.com/docs
```

[Uber(opens in new tab)](https://www.uber.com/legal/en/)

Get Uber price & time estimates for any ride option

URL



``` inline-block
https://mcp.uber.com/claude/rides-3p/mcp
```

[Uber Eats(opens in new tab)](https://www.ubereats.com)

Explore restaurants and dishes

URL



``` inline-block
https://mcp.ubereats.com/eats-claude/mcp
```

[Udemy Business(opens in new tab)](https://business-support.udemy.com/hc/en-us/articles/34213384429335-How-to-Integrate-the-Udemy-Business-MCP-Server-With-Your-AI-Tool#h_01K9CA42YGCV1AVXPY1RKABKP1)

Search and explore skill-building resources

URL



``` inline-block
https://api.udemy.com/mcp
```

[Pylon(opens in new tab)](https://support.usepylon.com/articles/2407390554-connecting-to-the-pylon-mcp-server?lang=en)

Search and manage Pylon support issues

URL



``` inline-block
https://mcp.usepylon.com/
```

[Verisk Underwriting Intelligence(opens in new tab)](https://www.verisk.com/resources/verisk-underwriting-intelligence/)

Ask questions. Get underwriting insights from Verisk.

URL



``` inline-block
https://gatewaymcp.verisk.com/underwriting/intelligencemcp/v1
```

[Verisk XactRestore(opens in new tab)](https://veriskpropertyestimatingsolutions.my.site.com/s/article/2622)

Natural-language estimating for XactRestore

URL



``` inline-block
https://xactrestore-xactremodelserver-usw2-prod.propsol.io/mcp
```

[Viator(opens in new tab)](https://docs.viator.com/partner-api/mcp/)

Book travel experiences around the world

URL



``` inline-block
https://exp-app-mcp.prod.ep.viator.com/mcp
```

[Visier(opens in new tab)](https://docs.visier.com/developer/agents/mcp/mcp-server.htm)

Find people, productivity and business impact insights

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.visier.com/developer/agents/mcp/mcp-server-set-up.htm)

[Webflow(opens in new tab)](https://developers.webflow.com/mcp/v1.0.0/reference/overview)

Manage Webflow CMS, pages, assets and sites

URL



``` inline-block
https://mcp.webflow.com/mcp
```

[Wolfram(opens in new tab)](https://www.wolfram.com/artificial-intelligence/mcp-service/)

Inject precise, real-time computation and knowledge

URL



``` inline-block
https://agenttools.wolfram.com/mcp
```

[WordPress.com(opens in new tab)](https://developer.wordpress.com/docs/mcp/)

Secure AI access to manage your WordPress.com sites

URL



``` inline-block
https://public-api.wordpress.com/wpcom/v2/mcp/v1
```

[Workable(opens in new tab)](https://workable.readme.io/reference/workable-mcp-server)

Your AI assistant for Hiring and HR — inside Workable

URL



``` inline-block
https://mcp.workable.com/mcp
```

[Workato(opens in new tab)](https://docs.workato.com/en/mcp.html)

Automate workflows and connect your business apps

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://app.workato.com/ai_hub/mcp)

[Wyndham Hotels and Resorts(opens in new tab)](https://www.wyndhamhotels.com/mcp-doc)

Discover the right Wyndham Hotel for you, faster

URL



``` inline-block
https://mcp.wyndhamhotels.com/claude/mcp
```

[Xero(opens in new tab)](https://central.xero.com/s/article/Connect-Xero-using-the-Xero-connector-in-Claude?userregion=true)

Access your Xero financials from any conversation

URL



``` inline-block
https://mcp.xero.com/mcp
```

[Yardi Virtuoso(opens in new tab)](https://help.virtuoso.ai/en/articles/13679727-yardi-virtuoso-mcp-technical-documentation-guide)

Real-time Yardi data & insights

URL



``` inline-block
https://mcp.virtuoso.ai/mcp
```

[Zapier(opens in new tab)](https://docs.zapier.com/mcp/home)

Automate workflows across thousands of apps via conversation

URL



``` inline-block
https://mcp.zapier.com/api/v1/connect
```

[ZipRecruiter(opens in new tab)](https://api.ziprecruiter.com/mcp/docs)

Job search made easy

URL



``` inline-block
https://api.ziprecruiter.com/mcp
```

[Zoho Books(opens in new tab)](https://help.zoho.com/portal/en/kb/mcp/getting-started/articles/zoho-mcp-help-documentation-29-9-2025)

Zoho Books MCP for Smart Finance Ops

[Zoho CRM(opens in new tab)](https://help.zoho.com/portal/en/kb/mcp/getting-started/articles/zoho-mcp-help-documentation-29-9-2025)

MCP Server for Zoho CRM Workflows

[Zoho Desk(opens in new tab)](https://help.zoho.com/portal/en/kb/mcp/getting-started/articles/zoho-mcp-help-documentation-29-9-2025)

Zoho Desk MCP for Customer Support Automation

[Zoho Projects(opens in new tab)](https://help.zoho.com/portal/en/kb/mcp/getting-started/articles/zoho-mcp-help-documentation-29-9-2025)

Zoho Projects MCP for Task & Project Automation

[ZoomInfo(opens in new tab)](https://docs.zoominfo.com/docs/zi-api-mcp-overview/)

Enrich contacts & accounts with GTM intelligence

URL



``` inline-block
https://mcp.zoominfo.com/mcp
```

[Tango(opens in new tab)](https://tango.makegov.com/docs/mcp/)

Search for US Government Contracting Data

URL



``` inline-block
https://govcon.dev/mcp
```

[Jam(opens in new tab)](https://jam.dev/docs/debug-a-jam/mcp)

Record screen and collect automatic context for issues

URL



``` inline-block
https://mcp.jam.dev/mcp
```

[Sentry(opens in new tab)](https://docs.sentry.io/product/sentry-mcp/)

Search, query, and debug errors intelligently

URL



``` inline-block
https://mcp.sentry.dev/mcp
```

[Stytch(opens in new tab)](https://stytch.com/docs/workspace-management/stytch-mcp)

Manage your Stytch Project

URL



``` inline-block
https://mcp.stytch.dev/mcp
```

[Craft(opens in new tab)](https://documents.craft.me/jWeCVJrSfxFRuA)

Notes & second brain

URL



``` inline-block
https://mcp.craft.do/my/mcp
```

[Alma(opens in new tab)](https://alma.food/mcp)

Your nutrition data, inside every Claude conversation.

URL



``` inline-block
https://mcp.alma.food
```

[MoSPI(opens in new tab)](https://www.datainnovation.mospi.gov.in/mospi-mcp)

India's official statistics via natural language

URL



``` inline-block
https://mcp.mospi.gov.in/
```

[Adobe for creativity(opens in new tab)](https://developer.adobe.com/adobe-for-creativity/)

Ideate, create, and deliver with Adobe pro tools

URL



``` inline-block
https://adobe-creativity.adobe.io/mcp
```

[Adobe Journey Optimizer(opens in new tab)](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/combine/ajo-mcp)

Understand and troubleshoot your Journeys and Campaigns

URL



``` inline-block
https://ajo-mcp.adobe.io/mcp
```

[Adobe Marketing Agent(opens in new tab)](https://acrobat.adobe.com/id/urn:aaid:sc:AP:5799e952-be87-4829-b0c4-6f82ca8e8b8b)

Marketing campaign and audience insights from Adobe

URL



``` inline-block
https://aep-ai-ama.adobe.io/mcp
```

[Common Room(opens in new tab)](https://www.commonroom.io/docs/using-common-room/common-room-for-claude-connector-and-plugin/)

Your GTM Copilot

URL



``` inline-block
https://mcp.commonroom.io/mcp
```

[Customer.io(opens in new tab)](https://docs.customer.io/ai/mcp-server/)

Explore customer data and generate insights via Claude

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.customer.io/ai/mcp-server/)

[Eraser(opens in new tab)](https://docs.eraser.io/docs/mcp)

Generate, manage, and update Eraser diagrams and files

URL



``` inline-block
https://app.eraser.io/api/mcp
```

[Harness.io(opens in new tab)](https://github.com/harness/mcp-server)

Build, Ship and Secure your apps on Harness Platform

URL



``` inline-block
https://mcp.harness.io/mcp
```

[Honeycomb(opens in new tab)](https://docs.honeycomb.io/troubleshoot/product-lifecycle/beta/mcp/)

Query and explore observability data and SLOs

URL



``` inline-block
https://mcp.honeycomb.io/mcp
```

[incident.io(opens in new tab)](https://docs.incident.io/ai/remote-mcp)

See and manage everything in incident.io

URL



``` inline-block
https://mcp.incident.io/mcp
```

[n8n(opens in new tab)](https://docs.n8n.io/advanced-ai/mcp/mcp_tools_reference/)

Access and run your n8n workflows

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.n8n.io/advanced-ai/mcp/mcp_tools_reference/)

[Pendo(opens in new tab)](https://support.pendo.io/hc/en-us/articles/41102236924955)

Connect to Pendo for product and user insights

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://support.pendo.io/hc/en-us/articles/41102236924955)

[Sanity(opens in new tab)](https://www.sanity.io/docs/ai/mcp-server)

Create, query, and manage structured content in Sanity

URL



``` inline-block
https://mcp.sanity.io
```

[Starburst(opens in new tab)](https://docs.starburst.io/starburst-galaxy/ai-workflows/mcp-server.html)

Securely retrieve data from your federated data sources

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://docs.starburst.io/starburst-galaxy/ai-workflows/mcp-server.html)

[tldv(opens in new tab)](https://tldv.notion.site/tl-dv-MCP-Official-Documentation-330cce15f3ba80638f5ac0253e3b8fd4?source=copy_link)

Fetch Transcripts & Notes from Meet, Zoom & Teams

URL



``` inline-block
https://mcp.tldv.io/mcp
```

[Tropic(opens in new tab)](https://help.tropicapp.io/hc/en-us/articles/45502083594267-Using-Model-Context-Protocol-MCP-with-Tropic)

Save money on Software + AI contracts

URL



``` inline-block
https://app.tropicapp.io/mcp
```

[Unthread(opens in new tab)](https://docs.unthread.io/docs/unthread-ai/unthread-mcp)

Manage and automate your support tickets

URL



``` inline-block
https://app.unthread.io/api/mcp
```

[Zocks(opens in new tab)](https://help.zocks.io/en/articles/14075856-connect-to-the-zocks-mcp-server)

Analyze client conversations, patterns, and insights.

URL



``` inline-block
https://mcp.zocks.io/v1/mcp
```

[Trellis(opens in new tab)](https://support.trellis.law)

Claude for Trial Court Litigators

URL



``` inline-block
https://mcp.trellis.law/anthropic
```

[Todoist(opens in new tab)](https://github.com/Doist/todoist-ai)

Search, complete, and manage your tasks in Todoist

URL



``` inline-block
https://ai.todoist.net/mcp
```

[Relativity(opens in new tab)](https://help.relativity.com/topic.html?t=GLJ39)

Organize Data. Discover the Truth. Act on It.

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://help.relativity.com/topic.html?t=GLJ39)

[BoardWise(opens in new tab)](https://boardwise.online/mcp)

Calm board-defense guidance for licensed pros.

URL



``` inline-block
https://uakozrqrztgrgwoywxkx.supabase.co/functions/v1/mcp-server
```

[Candid(opens in new tab)](https://support.claude.com/en/articles/12923235-using-the-candid-connector-in-claude)

Research nonprofits and funders using Candid's data

URL



``` inline-block
https://mcp.candid.org/mcp
```

[Learning Commons Knowledge Graph(opens in new tab)](https://docs.learningcommons.org/knowledge-graph/integrations/claude)

K-12 standards, skills, and learning progressions

URL



``` inline-block
https://kg.mcp.learningcommons.org/mcp
```

[Open Targets(opens in new tab)](https://github.com/opentargets/open-targets-platform-mcp)

Drug target discovery and prioritisation platform

URL



``` inline-block
https://mcp.platform.opentargets.org/mcp
```

[Synapse.org(opens in new tab)](https://github.com/susheel/synapse-mcp?tab=readme-ov-file#synapse-mcp-server)

Search and metadata tools for Synapse scientific data

URL



``` inline-block
https://mcp.synapse.org/mcp
```

[Chronograph(opens in new tab)](https://lp-help.chronograph.pe/article/735-chronograph-mcp)

Interact with your Chronograph data directly in Claude

URL



``` inline-block
https://ai.chronograph.pe/mcp
```

[Hex(opens in new tab)](https://learn.hex.tech/docs/administration/mcp-server)

Answer questions with the Hex agent

Requires a user-specific URL. [Get your URL here(opens in new tab)](https://learn.hex.tech/docs/administration/mcp-server#connect-to-claude)

[Zoom for Claude(opens in new tab)](https://developers.zoom.us/docs/mcp/zoom/)

Search, recap, and act on your Zoom meetings

URL



``` inline-block
https://mcp.zoom.us/mcp/zoom/streamable
```



**Looking for more?** [Find hundreds more MCP servers on GitHub](https://github.com/modelcontextprotocol/servers).
