---
category: "04-API-Reference"
source_url: "https://platform.claude.com/docs/en/build-with-claude/overview"
---


Build with Claude
Features overview
Copy page
Explore Claude's advanced features and capabilities.
Core capabilities

These features enhance Claude's fundamental abilities for processing, analyzing, and generating content across various formats and use cases.

Feature Description Availability
1M token context window An extended context window that allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases. Claude API (Beta)

Amazon Bedrock (Beta)

Google Cloud's Vertex AI (Beta)

Microsoft Foundry (Beta)
Agent Skills Extend Claude's capabilities with Skills. Use pre-built Skills (PowerPoint, Excel, Word, PDF) or create custom Skills with instructions and scripts. Skills use progressive disclosure to efficiently manage context. Claude API (Beta)

Microsoft Foundry (Beta)
Batch processing Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Batch API calls costs 50% less than standard API calls. Claude API

Amazon Bedrock

Google Cloud's Vertex AI
Citations Ground Claude's responses in source documents. With Citations, Claude can provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs. Claude API

Amazon Bedrock

Google Cloud's Vertex AI

Microsoft Foundry
Context editing Automatically manage conversation context with configurable strategies. Supports clearing tool results when approaching token limits and managing thinking blocks in extended thinking conversations. Claude API (Beta)

Amazon Bedrock (Beta)

Google Cloud's Vertex AI (Beta)

Microsoft Foundry (Beta)
Effort Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency. Claude API (Beta)

Amazon Bedrock (Beta)

Google Cloud's Vertex AI (Beta)

Microsoft Foundry (Beta)
Extended thinking Enhanced reasoning capabilities for complex tasks, providing transparency into Claude's step-by-step thought process before delivering its final answer. Claude API

Amazon Bedrock

Google Cloud's Vertex AI

Microsoft Foundry
Files API Upload and manage files to use with Claude without re-uploading content with each request. Supports PDFs, images, and text files. Claude API (Beta)

Microsoft Foundry (Beta)
PDF support Process and analyze text and visual content from PDF documents. Claude API

Amazon Bedrock

Google Cloud's Vertex AI

Microsoft Foundry
Prompt caching (5m) Provide Claude with more background knowledge and example outputs to reduce costs and latency. Claude API

Amazon Bedrock

Google Cloud's Vertex AI

Microsoft Foundry
Prompt caching (1hr) Extended 1-hour cache duration for less frequently accessed but important context, complementing the standard 5-minute cache. Claude API

Microsoft Foundry
Search results Enable natural citations for RAG applications by providing search results with proper source attribution. Achieve web search-quality citations for custom knowledge bases and tools. Claude API

Amazon Bedrock

Google Cloud's Vertex AI

Microsoft Foundry
Structured outputs Guarantee schema conformance with two approaches: JSON outputs for structured data responses, and strict tool use for validated tool inputs. Available on Sonnet 4.5, Opus 4.5, and Haiku 4.5. Claude API

Amazon Bedrock (Beta)

Microsoft Foundry (Beta)
Token counting Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. Claude API

Amazon Bedrock

Google Cloud's Vertex AI

Microsoft Foundry
Tool use Enable Claude to interact with external tools and APIs to perform a wider variety of tasks. For a list of supported tools, see the Tools table. Claude API

Amazon Bedrock

Google Cloud's Vertex AI

Microsoft Foundry
Tools

These features enable Claude to interact with external systems, execute code, and perform automated tasks through various tool interfaces.

Feature Description Availability
Bash Execute bash commands and scripts to interact with the system shell and perform command-line operations. Claude API

Amazon Bedrock

Google Cloud's Vertex AI

Microsoft Foundry
Code execution Run Python code in a sandboxed environment for advanced data analysis. Claude API (Beta)

Microsoft Foundry (Beta)
Programmatic tool calling Enable Claude to call your tools programmatically from within code execution containers, reducing latency and token consumption for multi-tool workflows. Claude API (Beta)

Microsoft Foundry (Beta)
Computer use Control computer interfaces by taking screenshots and issuing mouse and keyboard commands. Claude API (Beta)

Amazon Bedrock (Beta)

Google Cloud's Vertex AI (Beta)

Microsoft Foundry (Beta)
Fine-grained tool streaming Stream tool use parameters without buffering/JSON validation, reducing latency for receiving large parameters. Claude API

Amazon Bedrock

Google Cloud's Vertex AI

Microsoft Foundry
MCP connector Connect to remote MCP servers directly from the Messages API without a separate MCP client. Claude API (Beta)

Microsoft Foundry (Beta)
Memory Enable Claude to store and retrieve information across conversations. Build knowledge bases over time, maintain project context, and learn from past interactions. Claude API (Beta)

Amazon Bedrock (Beta)

Google Cloud's Vertex AI (Beta)

Microsoft Foundry (Beta)
Text editor Create and edit text files with a built-in text editor interface for file manipulation tasks. Claude API

Amazon Bedrock

Google Cloud's Vertex AI

Microsoft Foundry
Tool search Scale to thousands of tools by dynamically discovering and loading tools on-demand using regex-based search, optimizing context usage and improving tool selection accuracy. Claude API (Beta)

Amazon Bedrock (Beta)

Google Cloud's Vertex AI (Beta)

Microsoft Foundry (Beta)
Web fetch Retrieve full content from specified web pages and PDF documents for in-depth analysis. Claude API (Beta)

Microsoft Foundry (Beta)
Web search Augment Claude's comprehensive knowledge with current, real-world data from across the web. Claude API

Google Cloud's Vertex AI

Microsoft Foundry

Was this page helpful?