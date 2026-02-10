# 

**URL:** https://platform.claude.com/cookbook/tool-use-tool-search-with-embeddings

## Page Structure

- Tool search with embeddings
- Tool Search with Embeddings: Scaling Claude to Thousands of Tools
  - Prerequisites
  - Setup
  - Define Tool Library
  - Create Tool Embeddings
  - Implement Tool Search
  - Define the tool\_search Tool
  - Mock Tool Execution
  - Implement Conversation Loop
  - Example 1: Weather Query
  - Example 2: Finance Query
  - Conclusion
    - Applying This to Your Projects
    - Next Steps
    - Further Reading

## Sections & Articles

### Article: Tool Search with Embeddings: Scaling Claude to Thousands of Tools

- **Word Count:** 3324
- **Path:** `div#root > div.pt-12.min-h-screen > main.mx-auto.w-full > div.mx-auto.max-w-4xl > article.mb-12`

Tool Search with Embeddings: Scaling Claude to Thousands of Tools Building Claude applications with dozens of specialized tools quickly hits a wall: providing all tool definitions upfront consumes your context window, increases latency and costs, and makes it harder for Claude to find the right tool. Beyond ~100 tools, this approach becomes impractical. Semantic tool search solves this by treating tools as discoverable resources. Instead of front-loading hundreds of definitions, you give Claude a single tool\_search tool that returns relevant capabilities on demand, cutting context usage by 90%+ while enabling applications that scale to thousands of tools. By the end of this cookbook, you'll be able to: Implement client-side tool search to scale Claude applications from dozens to thousands of tools Use semantic embeddings to dynamically discover relevant tools based on task context Apply this pattern to domain-specific tool libraries (APIs, databases, internal systems) This pattern is used in production by teams managing large tool ecosystems where context efficiency is critical. While we'll demonstrate with a small set of tools for clarity, the same approach scales seamlessly to libraries with hundreds or thousands of tools. Prerequisites Before following this guide, ensure you have: Required Knowledge Python fundamentals - comfortable with functions, dictionaries, and basic data structures Basic understanding of Claude tool use - we recommend reading the Tool Use Guide first Required Tools Python 3.11 or higher Anthropic API key ( get one here ) Setup First, install the required dependencies: python Ensure your .env file contains: Load your environment variables and configure the client: python Define Tool Library Before we can implement semantic search, we need tools to search through. We'll create a library of 8 tools across two categories: Weather and Finance. In production applications, you might manage hundreds or thousands of tools across your internal APIs, database operations, or third-party integrations. The semantic search approach scales to these larger libraries without modification - we're using a small set here purely for demonstration clarity. python Create Tool Embeddings Semantic search works by comparing the meaning of text, rather than just searching for keywords. To enable this, we need to convert each tool definition into an embedding vector that captures its semantic meaning. Since our tool definitions are structured JSON objects with names, descriptions, and parameters, we first convert each tool into a human-readable text representation, then generate embedding vectors using SentenceTransformer's all-MiniLM-L6-v2 model. We picked this model because it is: Lightweight and fast (only 384 dimensions vs 768+ for larger models) Runs locally without requiring API calls Sufficient for tool search (you can experiment with larger models for better accuracy) Let's start by creating a function that converts tool definitions into searchable text: python Now let's create embeddings for all our tools: python Implement Tool Search With our tools embedded as vectors, we can now implement semantic search. If two pieces of text have similar meanings, their embedding vectors will be close together in vector space. We measure this "closeness" using cosine similarity . The search process: Embed the query : Convert Claude's natural language search request into the same vector space as our tools Calculate similarity : Compute cosine similarity between the query vector and each tool vector Rank and return : Sort tools by similarity score and return the top N matches With semantic search, Claude can search using natural language like "I need to check the weather" or "calculate investment returns" rather than exact tool names. Let's implement the search function and test it with a sample query: python Define the tool\_search Tool Now we'll implement the meta-tool that allows Claude to discover other tools on demand. When Claude needs a capability it doesn't have, it searches for it using this tool\_search tool, receives the tool definitions in the result, and can use those newly discovered tools immediately. This is the only tool we provide to Claude initially: python Now let's implement the handler that processes tool\_search calls from Claude and returns discovered tools: python Mock Tool Execution For this demonstration, we'll create mock responses for tool executions. In a real application, these would call actual APIs or services: python Implement Conversation Loop Now let's put it all together! We'll create a conversation loop that handles the complete tool search workflow. The conversation flow: Claude starts with only the tool\_search tool available When Claude calls tool\_search , we run semantic search and return matching tool definitions Claude can then use the discovered tools immediately When Claude calls a discovered tool, we execute it (using mock responses for this demo) The loop continues until Claude has a final answer python Example 1: Weather Query Let's test with a simple weather question. Claude should: Call tool\_search to find weather tools Receive weather tool definitions in the result Use one of the discovered tools python Example 2: Finance Query Let's try a financial calculation query that requires discovering and using finance tools: python Conclusion In this cookbook, we implemented a client-side tool search system that enables Claude to work with large tool libraries efficiently. We covered: Semantic tool discovery : Using embeddings to match natural language queries to relevant tools, enabling Claude to find the right capability without seeing all available tools upfront Dynamic tool loading : Returning tool definitions in tool results using Claude's tool search feature, allowing Claude to discover and immediately use new tools mid-conversation Context optimization : Reducing initial context from thousands of tokens (19+ tool definitions) to just the single tool\_search definition, cutting context usage by 90%+ Applying This to Your Projects Consider tool search when: You have &gt;20 specialized tools and context usage becomes a concern Your tool library grows over time and manual curation becomes impractical You need to support domain-specific APIs with hundreds of endpoints (database operations, internal microservices, third-party integrations) Cost and latency optimization are priorities for your application Next Steps To take this implementation further: Persist embeddings : Cache embeddings to disk to avoid recomputing on every session, reducing startup time Improve search quality : Experiment with different embedding models (e.g., larger models like all-mpnet-base-v2 ) or implement hybrid search combining semantic and keyword matching (BM25) Scale to larger libraries : Test with hundreds or thousands of tools to see how the pattern performs at production scale Add tool metadata : Include usage statistics, cost information, or reliability scores in your search ranking Implement caching : Cache frequently used tool definitions to reduce repeated searches Further Reading Claude Tool Use Guide - Comprehensive guide to building with tools SentenceTransformers Documentation - Learn more about embedding models and semantic search Tool Search Tool Documentation - Official documentation on the tool search pattern

**Code:** [1] [2] [3]

[1] Block 1
```
# Note: we use -q to avoid printing too much to stdout
# Use --only-binary to avoid build issues with pythran
%pip install --only-binary :all: -q anthropic sentence-transformers numpy python-dotenv
```

[2] Block 2
```
huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
To disable this warning, you can either:
	- Avoid using `tokenizers` before the fork if possible
	- Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)

Note: you may need to restart the kernel to use updated packages.
```

[3] Block 3
```
ANTHROPIC_API_KEY=your_key_here
```

## Additional Text Blocks (1)

CookbookCookbook/Tools, RAG & Retrieval/Tool search with embeddingsToolsRAG & RetrievalView on GitHubTool search with embeddingsScale Claude applications to thousands of tools using semantic embeddings for dynamic tool discovery.Henry Keetay@henrykeetayPublished on November 24, 2025Was this page helpful?Tool Search with Embeddings: Scaling Claude to Thousands of Tools Building Claude applications with dozens of specialized tools quickly hits a wall: providing all tool definitions upfront consumes your context window, increases latency and costs, and makes it harder for Claude to find the right tool. Beyond ~100 tools, this approach becomes impractical. Semantic tool search solves this by treating tools as discoverable resources. Instead of front-loading hundreds of definitions, you give Claude a single tool\_search tool that returns relevant capabilities on demand, cutting context usage by 90%+ while enabling applications that scale to thousands of tools. By the end of this cookbook, you'll be able to: Implement client-side tool search to scale Claude applications from dozens to thousands of tools Use semantic embeddings to dynamically discover relevant tools based on task context Apply this pattern to domain-specific tool libraries (APIs, databases, internal systems) This pattern is used in production by teams managing large tool ecosystems where context efficiency is critical. While we'll demonstrate with a small set of tools for clarity, the same approach scales seamlessly to libraries with hundreds or thousands of tools. Prerequisites Before following this guide, ensure you have: Required Knowledge Python fundamentals - comfortable with functions, dictionaries, and basic data structures Basic understanding of Claude tool use - we recommend reading the Tool Use Guide first Required Tools Python 3.11 or higher Anthropic API key (get one here) Setup First, install the required dependencies: python# Note: we use -q to avoid printing too much to stdout # Use --o

## Interactive Elements (39)

- **[0]** Cookbook (link) `div#root > header.fixed.top-0 > a`
- **[1]** (unlabeled) (button) `button#radix-_r_0_`
- **[2]** Cookbook (link) `div#root > div.pt-12.min-h-screen > main.mx-auto.w-full > div.mx-auto.max-w-4xl > nav.mb-8.text-sm > a.text-accent-secondary-100.hover:text-accent-secondary-000`
- **[3]** View on GitHub (link) `div.pt-12.min-h-screen > main.mx-auto.w-full > div.mx-auto.max-w-4xl > header.mb-12.pb-8 > div.flex.flex-wrap > a.inline-flex.items-center`
- **[4]** Thumbs up (button) `div.mx-auto.max-w-4xl > header.mb-12.pb-8 > div.flex.items-center > div.flex.items-center > div.flex.items-center > button.inline-flex.items-center`
- **[5]** Thumbs down (button) `div.mx-auto.max-w-4xl > header.mb-12.pb-8 > div.flex.items-center > div.flex.items-center > div.flex.items-center > button.inline-flex.items-center`
- **[8]** Tool Use Guide (link) `main.mx-auto.w-full > div.mx-auto.max-w-4xl > article.mb-12 > ul.list-none.mb-4 > li.mb-2.last:mb-0 > a.text-accent-secondary-100.hover:text-accent-secondary-000`
- **[9]** get one here (link) `main.mx-auto.w-full > div.mx-auto.max-w-4xl > article.mb-12 > ul.list-none.mb-4 > li.mb-2.last:mb-0 > a.text-accent-secondary-100.hover:text-accent-secondary-000`
- **[11]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[12]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[13]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[14]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[16]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[17]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[19]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[20]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[21]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[22]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[24]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[25]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[27]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[28]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[29]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[30]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[32]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[33]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[35]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[36]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[38]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[39]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[41]** Copy code (button) `div.mx-auto.max-w-4xl > article.mb-12 > div.my-6 > div.group.relative > div.flex.items-center > button.inline-flex.items-center`
- **[42]** (unlabeled) (generic) `div.my-6 > div.group.relative > div.relative.py-4 > div.code-input-content > figure > pre.m-0.p-0`
- **[47]** Claude Tool Use Guide (link) `main.mx-auto.w-full > div.mx-auto.max-w-4xl > article.mb-12 > ul.list-none.mb-4 > li.mb-2.last:mb-0 > a.text-accent-secondary-100.hover:text-accent-secondary-000`
- **[48]** SentenceTransformers Documentation (link) `main.mx-auto.w-full > div.mx-auto.max-w-4xl > article.mb-12 > ul.list-none.mb-4 > li.mb-2.last:mb-0 > a.text-accent-secondary-100.hover:text-accent-secondary-000`
- **[49]** Tool Search Tool Documentation (link) `main.mx-auto.w-full > div.mx-auto.max-w-4xl > article.mb-12 > ul.list-none.mb-4 > li.mb-2.last:mb-0 > a.text-accent-secondary-100.hover:text-accent-secondary-000`
- **[50]** Thumbs up (button) `main.mx-auto.w-full > div.mx-auto.max-w-4xl > div.mb-8.py-6 > div.flex.items-center > div.flex.items-center > button.inline-flex.items-center`
- **[51]** Thumbs down (button) `main.mx-auto.w-full > div.mx-auto.max-w-4xl > div.mb-8.py-6 > div.flex.items-center > div.flex.items-center > button.inline-flex.items-center`
- **[52]** Back to Cookbook (link) `div#root > div.pt-12.min-h-screen > main.mx-auto.w-full > div.mx-auto.max-w-4xl > div.flex.flex-wrap > a.inline-flex.items-center`
- **[53]** View on GitHub (link) `div#root > div.pt-12.min-h-screen > main.mx-auto.w-full > div.mx-auto.max-w-4xl > div.flex.flex-wrap > a.inline-flex.items-center`

## Accessibility Issues

### ERROR: Button has no accessible label

**Element:** button  
**Count:** 1

**Locations:**
- `button#radix-_r_0_`

## Page Metadata

- **Language:** en
- **Description:** Scale Claude applications to thousands of tools using semantic embeddings for dynamic tool discovery.
- **Viewport:** 1109x1307
- **Scrollable:** Yes

## Statistics

- **Landmarks:** 2
- **Headings:** 16
- **Interactive Elements:** 39
- **Images:** 1
- **Images with alt text:** 1
