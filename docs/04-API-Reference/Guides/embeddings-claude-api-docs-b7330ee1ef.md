---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:16Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/embeddings"
title: "Embeddings - Claude API Docs"
---

Capabilities

# Embeddings

Copy page

Text embeddings are numerical representations of text that enable measuring semantic similarity. This guide introduces embeddings, their applications, and how to use embedding models for tasks like search, recommendations, and anomaly detection.

Copy page

## 

Before implementing embeddings

When selecting an embeddings provider, there are several factors you can consider depending on your needs and preferences:

- Dataset size & domain specificity: size of the model training dataset and its relevance to the domain you want to embed. Larger or more domain-specific data generally produces better in-domain embeddings
- Inference performance: embedding lookup speed and end-to-end latency. This is a particularly important consideration for large scale production deployments
- Customization: options for continued training on private data, or specialization of models for very specific domains. This can improve performance on unique vocabularies

## 

How to get embeddings with Anthropic

Anthropic does not offer its own embedding model. One embeddings provider that has a wide variety of options and capabilities encompassing all of the above considerations is Voyage AI.

Voyage AI makes state-of-the-art embedding models and offers customized models for specific industry domains such as finance and healthcare, or bespoke fine-tuned models for individual customers.

The rest of this guide is for Voyage AI, but we encourage you to assess a variety of embeddings vendors to find the best fit for your specific use case.

## 

Available Models

Voyage recommends using the following text embedding models:

| Model | Context Length | Embedding Dimension | Description |
|----|----|----|----|
| `voyage-3-large` | 32,000 | 1024 (default), 256, 512, 2048 | The best general-purpose and multilingual retrieval quality. See [blog post](https://blog.voyageai.com/2025/01/07/voyage-3-large/) for details. |
| `voyage-3.5` | 32,000 | 1024 (default), 256, 512, 2048 | Optimized for general-purpose and multilingual retrieval quality. See [blog post](https://blog.voyageai.com/2025/05/20/voyage-3-5/) for details. |
| `voyage-3.5-lite` | 32,000 | 1024 (default), 256, 512, 2048 | Optimized for latency and cost. See [blog post](https://blog.voyageai.com/2025/05/20/voyage-3-5/) for details. |
| `voyage-code-3` | 32,000 | 1024 (default), 256, 512, 2048 | Optimized for **code** retrieval. See [blog post](https://blog.voyageai.com/2024/12/04/voyage-code-3/) for details. |
| `voyage-finance-2` | 32,000 | 1024 | Optimized for **finance** retrieval and RAG. See [blog post](https://blog.voyageai.com/2024/06/03/domain-specific-embeddings-finance-edition-voyage-finance-2/) for details. |
| `voyage-law-2` | 16,000 | 1024 | Optimized for **legal** and **long-context** retrieval and RAG. Also improved performance across all domains. See [blog post](https://blog.voyageai.com/2024/04/15/domain-specific-embeddings-and-retrieval-legal-edition-voyage-law-2/) for details. |

Additionally, the following multimodal embedding models are recommended:

| Model | Context Length | Embedding Dimension | Description |
|----|----|----|----|
| `voyage-multimodal-3` | 32000 | 1024 | Rich multimodal embedding model that can vectorize interleaved text and content-rich images, such as screenshots of PDFs, slides, tables, figures, and more. See [blog post](https://blog.voyageai.com/2024/11/12/voyage-multimodal-3/) for details. |

Need help deciding which text embedding model to use? Check out the [FAQ](https://docs.voyageai.com/docs/faq#what-embedding-models-are-available-and-which-one-should-i-use&ref=anthropic).

## 

Getting started with Voyage AI

To access Voyage embeddings:

1.  Sign up on Voyage AI's website
2.  Obtain an API key
3.  Set the API key as an environment variable for convenience:

``` shiki
export VOYAGE_API_KEY="<your secret key>"
```

You can obtain the embeddings by either using the official [`voyageai` Python package](https://github.com/voyage-ai/voyageai-python) or HTTP requests, as described below.

### 

Voyage Python library

The `voyageai` package can be installed using the following command:

``` shiki
pip install -U voyageai
```

Then, you can create a client object and start using it to embed your texts:

``` shiki
import voyageai

vo = voyageai.Client()
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

texts = ["Sample text 1", "Sample text 2"]

result = vo.embed(texts, model="voyage-3.5", input_type="document")
print(result.embeddings[0])
print(result.embeddings[1])
```

`result.embeddings` will be a list of two embedding vectors, each containing 1024 floating-point numbers. After running the above code, the two embeddings will be printed on the screen:

``` inline-block
[-0.013131560757756233, 0.019828535616397858, ...]   # embedding for "Sample text 1"
[-0.0069352793507277966, 0.020878976210951805, ...]  # embedding for "Sample text 2"
```

When creating the embeddings, you can specify a few other arguments to the `embed()` function.

For more information on the Voyage python package, see [the Voyage documentation](https://docs.voyageai.com/docs/embeddings#python-api).

### 

Voyage HTTP API

You can also get embeddings by requesting Voyage HTTP API. For example, you can send an HTTP request through the `curl` command in a terminal:

``` shiki
curl https://api.voyageai.com/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOYAGE_API_KEY" \
  -d '{
    "input": ["Sample text 1", "Sample text 2"],
    "model": "voyage-3.5"
  }'
```

The response you would get is a JSON object containing the embeddings and the token usage:

``` shiki
{
  "object": "list",
  "data": [
    {
      "embedding": [-0.013131560757756233, 0.019828535616397858, ...],
      "index": 0
    },
    {
      "embedding": [-0.0069352793507277966, 0.020878976210951805, ...],
      "index": 1
    }
  ],
  "model": "voyage-3.5",
  "usage": {
    "total_tokens": 10
  }
}
```

For more information on the Voyage HTTP API, see [the Voyage documentation](https://docs.voyageai.com/reference/embeddings-api).

### 

AWS Marketplace

Voyage embeddings are available on [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=seller-snt4gb6fd7ljg). Instructions for accessing Voyage on AWS are available [here](https://docs.voyageai.com/docs/aws-marketplace-model-package?ref=anthropic).

## 

Quickstart example

Now that we know how to get embeddings, let's see a brief example.

Suppose we have a small corpus of six documents to retrieve from

``` shiki
documents = [
    "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
    "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
    "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
    "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
    "Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.",
    "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature."
]
```

We will first use Voyage to convert each of them into an embedding vector

``` shiki
import voyageai

vo = voyageai.Client()

# Embed the documents
doc_embds = vo.embed(
    documents, model="voyage-3.5", input_type="document"
).embeddings
```

The embeddings will allow us to do semantic search / retrieval in the vector space. Given an example query,

``` shiki
query = "When is Apple's conference call scheduled?"
```

we convert it into an embedding, and conduct a nearest neighbor search to find the most relevant document based on the distance in the embedding space.

``` shiki
import numpy as np

# Embed the query
query_embd = vo.embed(
    [query], model="voyage-3.5", input_type="query"
).embeddings[0]

# Compute the similarity
# Voyage embeddings are normalized to length 1, therefore dot-product
# and cosine similarity are the same.
similarities = np.dot(doc_embds, query_embd)

retrieved_id = np.argmax(similarities)
print(documents[retrieved_id])
```

Note that we use `input_type="document"` and `input_type="query"` for embedding the document and query, respectively. More specification can be found [here](/docs/en/build-with-claude/embeddings#voyage-python-package).

The output would be the 5th document, which is indeed the most relevant to the query:

``` inline-block
Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.
```

If you are looking for a detailed set of cookbooks on how to do RAG with embeddings, including vector databases, check out our [RAG cookbook](https://platform.claude.com/cookbook/third-party-pinecone-rag-using-pinecone).

## 

FAQ

### Why do Voyage embeddings have superior quality?

### What embedding models are available and which should I use?

### Which similarity function should I use?

### What is the relationship between characters, words, and tokens?

### When and how should I use the input_type parameter?

### What quantization options are available?

### How can I truncate Matryoshka embeddings?

## 

Pricing

Visit Voyage's [pricing page](https://docs.voyageai.com/docs/pricing?ref=anthropic) for the most up to date pricing details.

Was this page helpful?

- 

- [Before implementing embeddings](#before-implementing-embeddings)

- [How to get embeddings with Anthropic](#how-to-get-embeddings-with-anthropic)

- [Available Models](#available-models)

- [Getting started with Voyage AI](#getting-started-with-voyage-ai)

- [Voyage Python library](#voyage-python-library)

- [Voyage HTTP API](#voyage-http-api)

- [AWS Marketplace](#aws-marketplace)

- [Quickstart example](#quickstart-example)

- [FAQ](#faq)

- [Pricing](#pricing)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
