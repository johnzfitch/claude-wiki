---
category: "22-Safety-Policy"
fetched_at: "2026-03-15T12:17:11Z"
source_url: "https://support.anthropic.com/en/articles/11697096-anthropic-mcp-directory-policy"
title: "Anthropic MCP Directory Policy | Claude Help Center"
---

# Anthropic MCP Directory Policy

Updated yesterday


This is a prior version of our policy. Please refer to [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) for the most updated version.

Anthropic's Connectors Directory curates third-party Model Context Protocol servers to help users find high-quality tools that work seamlessly within Claude. We review submissions to our directory to ensure they meet our standards for safety, security, and compatibility with other servers. We conduct both initial and ongoing reviews of servers, and may require developers to address compliance issues to maintain directory inclusion. All servers must maintain compliance with these requirements, including any future changes, to remain in the directory.

## Safety and Security

1\) MCP servers must not be designed to facilitate or easily enable violation of our [Usage Policy](https://www.anthropic.com/legal/aup). All MCP servers must comply with our Universal Usage Standards and High-Risk Use Case requirements. All MCP servers must also comply with our policy on the [countries and regions Anthropic currently supports](https://www.anthropic.com/supported-countries).

2\) MCP servers must not employ methods to evade or enable users to circumvent Claude's safety guardrails.

3\) MCP servers should prioritize user privacy protection. Developers should take care to responsibly handle personal data, follow privacy best practices, and ensure compliance with applicable laws.

4\) MCP servers should only collect data from the user’s context that is necessary to perform their function. MCP servers should not collect extraneous conversation data, even for logging purposes.

5\) MCP servers must not infringe on the intellectual property rights of others.

6\) MCP servers should not attempt to access information about the users’ previous chats or the contents of their memory.

## Compatibility

7\) MCP tool descriptions must narrowly and unambiguously describe what each tool does and when it should be invoked.

8\) MCP tool descriptions must precisely match actual functionality, ensuring the server is called at correct and appropriate times. Descriptions must not include unexpected functionality or promise undelivered features.

9\) MCP tool descriptions should not create confusion or conflict with other MCP servers in our directory.

10\) MCP servers should not intentionally call or coerce Claude into calling other servers. Similarly, tool descriptions should not be written in a way that intentionally leads to other servers calling them.

11\) MCP servers should not attempt to interfere with Claude calling tools from other servers.

12\) MCP servers should not direct Claude to dynamically pull behavioral instructions from external sources for Claude to execute.

## Functionality

13\) MCP servers must deliver reliable performance with fast response times and maintain consistently high availability.

14\) MCP servers must gracefully handle errors and provide helpful feedback rather than generic error messages.

15\) MCP servers should be frugal with their use of tokens. The amount of tokens a given tool call uses should be roughly commensurate with the complexity or impact of the task. When possible, users should be given options to exclude unnecessary text in the response. Tool names may not exceed 64 characters.

16\) Remote MCP servers that connect to a remote service and require authentication must use secure OAuth 2.0 with certificates from recognized authorities.

17\) MCP servers must provide all applicable [annotations](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations) for their tools, in particular *readOnlyHint*, *destructiveHint*, and *title*.

18\) Remote MCP servers should support the [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) transport. Servers may support [SSE](https://modelcontextprotocol.io/specification/2024-11-05/basic/transports#http-with-sse) for the time being, but in the future it will be deprecated.

19\) Local MCP servers should be built with reasonably current versions of all dependencies, including packages in *node_modules*.

## Developer Requirements

20\) Developers of MCP servers that collect user data or connect to a remote service must provide a clear, accessible privacy policy link explaining data collection, usage, and retention.

21\) Developers must provide verified contact information and support channels for users with product concerns.

22\) Developers must document how their MCP server works, its intended purpose, and how users can troubleshoot issues.

23\) Developers must provide a standard testing account with sample data for Anthropic to verify full MCP functionality.

24\) Developers must provide at least three working examples of prompts or use cases that demonstrate core functionality.

25\) Developers must verify that they own or control any API endpoint their MCP server connects to.

26\) Developers must maintain their MCP server and address issues within reasonable timeframes.

27\) Developers must agree to our [MCP Directory Terms](https://support.anthropic.com/en/articles/11697081-anthropic-mcp-directory-terms-and-conditions).

## Unsupported Use Cases

At this time, we also disallow inclusion of MCP servers to our directory for certain use cases. We will revisit these restrictions as our directory evolves.

28\) MCP servers that transfer money, cryptocurrency, or other financial assets, or execute financial transactions on behalf of users.

29\) MCP servers that can generate images, video, or audio content. Design-focused MCP servers that can only create non-human-like visual outputs (such as diagrams, charts, UI mockups, logos, or other design assets) are allowed in the directory.

30\) MCP servers that enable cross-service automation. Servers must be limited to their designated service and cannot orchestrate actions across unrelated third-party applications. We may allow cross-service automation in limited cases, but we will explicitly notify users that external connections have not been reviewed.

------------------------------------------------------------------------

Related Articles


Get started with custom connectors using remote MCP


Building custom connectors via remote MCP servers


Anthropic Connectors Directory FAQ


Remote MCP Server Submission Guide


Anthropic Software Directory Policy
