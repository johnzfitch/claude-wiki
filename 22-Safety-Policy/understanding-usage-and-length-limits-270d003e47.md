---
category: "22-Safety-Policy"
source_url: "https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits"
---


When chatting with Claude, you may encounter two different types of limits that work in distinct ways: usage limits and length limits. Understanding the difference between these can help you use Claude more effectively.

 

What are usage limits?

Usage limits control how much you can interact with Claude over a specific time period. Think of this as your "conversation budget" that determines how many messages you can send to Claude, or how long you can work with Claude Code, before needing to wait for your limit to reset.

 

Your usage is affected by several factors, including the length and complexity of your conversations, the features you use, and which Claude model you're chatting with. Different subscription plans (Pro, Max, Team, etc.) have different usage allowances, with paid plans offering higher limits.

 

Note that your usage of all different Claude product surfaces (claude.ai, Claude Code, Claude Desktop) counts towards the same usage limit.

 

How can I get unlimited usage?

There are a couple of different ways to increase your usage depending on your plan:

If you’re using a paid plan, including Pro, Max, Team, or seat-based Enterprise plans, see these articles for details about purchasing extra usage:

Extra usage for paid Claude plans

Extra usage for Team and seat-based Enterprise plans

If your organization has a usage-based Enterprise plan, your usage is based on consumption. See this article for additional information: How am I billed for my Enterprise plan?

For strategies to maximize your message allotment, see Usage limit best practices.

 

What are length limits?

Length limits relate to Claude's context window—the amount of information Claude can work with in a single chat. Think of the context window as Claude's working memory that determines how much content it can process and remember at once.

Claude's context window size is 200K tokens across all models and paid plans, with one exception: Claude Sonnet 4.5 has a 500K context window for users on Enterprise plans. For more information, refer to What is the Enterprise plan?

 

Automatic context management

For users with code execution enabled, Claude now automatically manages long conversations. When your conversation approaches the context window limit, Claude summarizes earlier messages to continue the conversation seamlessly. This means you can have longer, more natural conversations with fewer interruptions.

 

Your full chat history is preserved so Claude can reference it even after summarization. You may occasionally see that Claude is "organizing its thoughts" during long conversations—this indicates automatic context management is working.

Note: Code execution must be enabled for automatic context management. Rare edge cases (such as very large first messages) may still encounter context limits.

 

How can I increase the size of Claude’s context window?

While you can't increase the fixed context window size for your plan, you can use these strategies to maximize available context space and optimize both your context window and usage limits:

Utilize projects effectively: Projects use retrieval-augmented generation (RAG), which allows Claude to work with larger amounts of information more efficiently by only loading relevant content into the context window.

Shorten project instructions: Keep your project instructions concise and focused on essential information. Claude performs best when you use project instructions for general context around your project, key guidelines, and Claude's role. Reserve task-specific instructions for the chat itself.

Remove unused project files: Regularly clean up files you're no longer actively using in your projects.

Toggle extended thinking off: Turn off this feature when you don't need Claude's enhanced reasoning for a particular task.

Temporarily disable non-critical tools and connectors: Disable web search, Research, and MCP connectors from your "Search and tools" settings when they're not needed for specific conversations.

Note: Tools and connectors are token-intensive, so managing them helps both maximize your available context window and optimize your usage limits.

 

Key differences

The main distinction is that usage limits control how much you can use Claude across all your conversations, while length limits control how long any single conversation can become. Usage limits are about quantity over time, while length limits are about the depth and complexity of individual conversations.

 

If you hit your usage limit, you'll need to wait for it to reset, upgrade your plan, or purchase extra usage. If you hit a length limit, you can start a new conversation or use features like projects to work with larger amounts of information more efficiently.

Related Articles
How large is the context window on paid Claude plans?
Usage limit best practices
Release Notes
Extra usage for paid Claude plans
Understanding Claude Error Messages