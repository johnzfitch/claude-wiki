---
title: "Embeddings - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/embeddings"
category: "04-API-Reference/Guides"
fetched_at: "2026-08-02T05:40:56Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

Thinking

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Compaction](/docs/en/build-with-claude/compaction)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics (beta)](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

Images and vision

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

MCP tunnels

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[](/login)




Messages

Embeddings

Messages/Model capabilities

# Embeddings




Text embeddings are numerical representations of text that enable measuring semantic similarity. This guide introduces embeddings, their applications, and how to use embedding models for tasks like search, recommendations, and anomaly detection.







Before implementing embeddings

When selecting an embeddings provider, there are several factors you can consider depending on your needs and preferences:

- Dataset size & domain specificity: size of the model training dataset and its relevance to the domain you want to embed. Larger or more domain-specific data generally produces better in-domain embeddings
- Inference performance: embedding lookup speed and end-to-end latency. This is a particularly important consideration for large scale production deployments
- Customization: options for continued training on private data, or specialization of models for very specific domains. This can improve performance on unique vocabularies




How to get embeddings with Anthropic

Anthropic does not offer its own embedding model. One embeddings provider that has a wide variety of options and capabilities encompassing all of the preceding considerations is Voyage AI.

Voyage AI makes state-of-the-art embedding models and offers customized models for specific industry domains such as finance and healthcare, or bespoke fine-tuned models for individual customers.

The rest of this guide is for Voyage AI, but you should assess a variety of embeddings vendors to find the best fit for your specific use case.




Available models

Voyage recommends using the following text embedding models:

**Voyage 4 (latest generation)**

| Model            | Context length | Embedding dimension            | Description                                                                                                                                                                                  |
|------------------|----------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `voyage-4-large` | 32,000         | 1024 (default), 256, 512, 2048 | The best general-purpose and multilingual retrieval quality. See the [Voyage 4 blog post](https://blog.voyageai.com/2026/01/15/voyage-4/) for details.                                       |
| `voyage-4`       | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for general-purpose and multilingual retrieval quality. Balances quality and efficiency. See the [Voyage 4 blog post](https://blog.voyageai.com/2026/01/15/voyage-4/) for details. |
| `voyage-4-lite`  | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for latency and cost. See the [Voyage 4 blog post](https://blog.voyageai.com/2026/01/15/voyage-4/) for details.                                                                    |
| `voyage-4-nano`  | 32,000         | 1024 (default), 256, 512, 2048 | Open-weight model (Apache 2.0 license) available on Hugging Face. See the [Voyage 4 blog post](https://blog.voyageai.com/2026/01/15/voyage-4/) for details.                                  |

**Previous generation**

| Model              | Context length | Embedding dimension            | Description                                                                                                                                                                                                                                                            |
|--------------------|----------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `voyage-3-large`   | 32,000         | 1024 (default), 256, 512, 2048 | The best general-purpose and multilingual retrieval quality. See the [voyage-3-large blog post](https://blog.voyageai.com/2025/01/07/voyage-3-large/) for details.                                                                                                     |
| `voyage-3.5`       | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for general-purpose and multilingual retrieval quality. See the [voyage-3.5 blog post](https://blog.voyageai.com/2025/05/20/voyage-3-5/) for details.                                                                                                        |
| `voyage-3.5-lite`  | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for latency and cost. See the [voyage-3.5 blog post](https://blog.voyageai.com/2025/05/20/voyage-3-5/) for details.                                                                                                                                          |
| `voyage-code-3`    | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for **code** retrieval. See the [voyage-code-3 blog post](https://blog.voyageai.com/2024/12/04/voyage-code-3/) for details.                                                                                                                                  |
| `voyage-finance-2` | 32,000         | 1024                           | Optimized for **finance** retrieval and RAG. See the [voyage-finance-2 blog post](https://blog.voyageai.com/2024/06/03/domain-specific-embeddings-finance-edition-voyage-finance-2/) for details.                                                                      |
| `voyage-law-2`     | 16,000         | 1024                           | Optimized for **legal** and **long-context** retrieval and RAG. Also improved performance across all domains. See the [voyage-law-2 blog post](https://blog.voyageai.com/2024/04/15/domain-specific-embeddings-and-retrieval-legal-edition-voyage-law-2/) for details. |

Additionally, Voyage recommends the following multimodal embedding models:

| Model                   | Context length | Embedding dimension            | Description                                                                                                                                                                                                                                                                              |
|-------------------------|----------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `voyage-multimodal-3.5` | 32,000         | 1024 (default), 256, 512, 2048 | Rich multimodal embedding model that can vectorize interleaved text, images, and videos. Includes video support as the first production-grade video embedding model. See the [voyage-multimodal-3.5 blog post](https://blog.voyageai.com/2026/01/15/voyage-multimodal-3-5/) for details. |
| `voyage-multimodal-3`   | 32,000         | 1024                           | Rich multimodal embedding model that can vectorize interleaved text and content-rich images, such as screenshots of PDFs, slides, tables, figures, and more. See the [voyage-multimodal-3 blog post](https://blog.voyageai.com/2024/11/12/voyage-multimodal-3/) for details.             |

The following contextualized chunk embedding models produce chunk-level vectors that capture full document context without manual metadata augmentation. Call these models with `contextualized_embed()` instead of `embed()`:

| Model              | Context length | Embedding dimension            | Description                                                                                                                                                                                                 |
|--------------------|----------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `voyage-context-4` | 120,000        | 1024 (default), 256, 512, 2048 | Contextualized chunk embeddings optimized for general-purpose and multilingual retrieval quality. See the [voyage-context-4 blog post](https://blog.voyageai.com/2026/06/29/voyage-context-4/) for details. |
| `voyage-context-3` | 120,000        | 1024 (default), 256, 512, 2048 | Contextualized chunk embeddings optimized for general-purpose and multilingual retrieval quality. See the [voyage-context-3 blog post](https://blog.voyageai.com/2025/07/23/voyage-context-3/) for details. |

Voyage AI also offers rerankers, which take a query and a list of documents and return them ranked by relevance to the query. Call these models with `rerank()`:

| Model             | Context length | Description                                                                                                                                        |
|-------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `rerank-2.5`      | 32,000         | Highest accuracy. Recommended for most applications. See the [rerank-2.5 blog post](https://blog.voyageai.com/2025/08/11/rerank-2-5/) for details. |
| `rerank-2.5-lite` | 32,000         | Optimized for latency and cost. See the [rerank-2.5 blog post](https://blog.voyageai.com/2025/08/11/rerank-2-5/) for details.                      |

Need help deciding which text embedding model to use? Check out the [Voyage AI FAQ](https://docs.voyageai.com/docs/faq#what-embedding-models-are-available-and-which-one-should-i-use&ref=anthropic).




Getting started with Voyage AI

To access Voyage embeddings:

1.  Sign up on Voyage AI's website.
2.  Obtain an API key.
3.  Set the API key as an environment variable for convenience:

```python
export VOYAGE_API_KEY="<your secret key>"
```



You can obtain the embeddings by either using the official [`voyageai` Python package](https://github.com/voyage-ai/voyageai-python) or HTTP requests, as described in the following sections.




Voyage Python library

Install the `voyageai` package using the following command:

```python
pip install -U voyageai
```



Then, you can create a client object and start using it to embed your texts:

```python
import voyageai

vo = voyageai.Client()
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

texts = ["Sample text 1", "Sample text 2"]

result = vo.embed(texts, model="voyage-4", input_type="document")
print(result.embeddings[0])
print(result.embeddings[1])
```



`result.embeddings` is a list of two embedding vectors, each containing 1024 floating-point numbers. After running the preceding code, the two embeddings are printed on the screen:

``` inline-block
[-0.013131560757756233, 0.019828535616397858, ...]   # embedding for "Sample text 1"
[-0.0069352793507277966, 0.020878976210951805, ...]  # embedding for "Sample text 2"
```



When creating the embeddings, you can specify a few other arguments to the `embed()` function.

For more information on the Voyage Python package, see the [Voyage Python package documentation](https://docs.voyageai.com/docs/embeddings#python-api).




Voyage HTTP API

You can also get embeddings by requesting Voyage HTTP API. For example, you can send an HTTP request through the `curl` command in a terminal:

cURL



```python
curl https://api.voyageai.com/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOYAGE_API_KEY" \
  -d '{
    "input": ["Sample text 1", "Sample text 2"],
    "model": "voyage-4"
  }'
```

The response you would get is a JSON object containing the embeddings and the token usage:

```python
{
  "object": "list",
  "data": [
    {
      "embedding": [-0.013131560757756233, 0.019828535616397858 /* ... */],
      "index": 0
    },
    {
      "embedding": [-0.0069352793507277966, 0.020878976210951805 /* ... */],
      "index": 1
    }
  ],
  "model": "voyage-4",
  "usage": {
    "total_tokens": 10
  }
}
```



For more information on the Voyage HTTP API, see the [Voyage HTTP API documentation](https://docs.voyageai.com/reference/embeddings-api).




AWS Marketplace

Voyage embeddings are available on [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=c9032c7b-70dd-459f-834f-c1e23cf3d092). Instructions for accessing Voyage on AWS are available in the [Voyage AWS Marketplace documentation](https://docs.voyageai.com/docs/aws-marketplace-mongodb-voyage?ref=anthropic).




Quickstart example

The following brief example shows how to use embeddings.

Suppose you have a small corpus of six documents to retrieve from

```python
documents = [
    "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
    "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
    "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
    "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
    "Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.",
    "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature.",
]
```



First, use Voyage to convert each document into an embedding vector.

```python
import voyageai

vo = voyageai.Client()

# Embed the documents
doc_embds = vo.embed(documents, model="voyage-4", input_type="document").embeddings
```



The embeddings allow you to do semantic search / retrieval in the vector space. Given an example query,

```python
query = "When is Apple's conference call scheduled?"
```



Next, convert it into an embedding and conduct a nearest neighbor search to find the most relevant document based on the distance in the embedding space.

```python
import numpy as np

# Embed the query
query_embd = vo.embed([query], model="voyage-4", input_type="query").embeddings[0]

# Compute the similarity
# Voyage embeddings are normalized to length 1, therefore dot-product
# and cosine similarity are the same.
similarities = np.dot(doc_embds, query_embd)

retrieved_id = np.argmax(similarities)
print(documents[retrieved_id])
```



Note that `input_type="document"` and `input_type="query"` are used for embedding the document and query, respectively. More specification can be found in [Voyage Python library](#voyage-python-library).

The output is the fifth document, which is indeed the most relevant to the query:

``` block
Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.
```



If you are looking for a detailed set of recipes on how to do RAG with embeddings, including vector databases, check out the [RAG recipe](https://platform.claude.com/cookbook/third-party-pinecone-rag-using-pinecone).





### Why do Voyage embeddings have superior quality?

### What embedding models are available and which should I use?

### Which similarity function should I use?

### What is the relationship between characters, words, and tokens?

### When and how should I use the input_type parameter?

### What quantization options are available?

### How can I truncate Matryoshka embeddings?




Pricing

Visit Voyage's [pricing page](https://docs.voyageai.com/docs/pricing?ref=anthropic) for the most up to date pricing details.
