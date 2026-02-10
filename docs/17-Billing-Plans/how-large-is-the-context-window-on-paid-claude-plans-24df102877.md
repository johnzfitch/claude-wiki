---
category: "17-Billing-Plans"
source_url: "https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans"
---


Claude’s context window size is 200K, meaning it can ingest 200K+ tokens (about 500 pages of text or more) when using a paid Claude plan.

Note: Users on Enterprise plans have access to a 500K context window when chatting with Claude Sonnet 4.5. See What is the Enterprise plan? for more information.

 

Automatic context management

For users on paid plans with code execution enabled, Claude automatically manages your conversation context. When your conversation approaches the context window limit, Claude summarizes earlier messages to make room for new content. This does not count towards your usage limit, and allows conversations to continue indefinitely in most cases.

 

Your full chat history is preserved so Claude can reference it, even after earlier portions have been summarized. You may occasionally notice Claude "organizing its thoughts" during long conversations—this is the automatic context management at work.

Note: Code execution must be enabled for automatic context management to work. In rare edge cases (such as very large first messages or system errors), you may still encounter context window limits.

 

Maximizing your context window

While context is managed automatically for most conversations, you can still optimize how you use your available context space:

Utilize projects effectively: Projects use retrieval-augmented generation (RAG), which allows Claude to work with larger amounts of information by only loading relevant content into the context window.

Keep project instructions concise: Claude performs best when you use project instructions for general context around your project, key guidelines, and Claude's role.

Manage tools and connectors: These features are token-intensive, so being mindful of how many you have active helps maximize your available context.

Related Articles
How large is the Claude API’s context window?
Understanding usage and length limits
Using Claude’s chat search and memory to build on previous context
Extra usage for paid Claude plans
Understanding Claude Error Messages