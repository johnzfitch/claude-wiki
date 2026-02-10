---
category: "19-Reference"
source_url: "https://www.anthropic.com/news/contextual-retrieval"
title: "Contextual Retrieval"
---


# Contextual Retrieval

## Overview
Anthropic introduced Contextual Retrieval, a method improving information retrieval in AI systems. The technique combines two approaches: "Contextual Embeddings and Contextual BM25" to enhance how models access background knowledge from large databases.

## The Problem
Traditional Retrieval-Augmented Generation (RAG) systems split documents into chunks for efficient searching. However, individual chunks often lack surrounding context, making retrieval unreliable. For example, a financial statement might say "revenue grew 3%" without specifying which company or time period.

## The Solution
Contextual Retrieval prepends explanatory context to each chunk before processing. An isolated statement becomes: "This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. The company's revenue grew by 3%..."

## Performance Results
- **Contextual Embeddings alone**: reduced retrieval failures by 35%
- **Combined with BM25**: reduced failures by 49%
- **With reranking added**: reduced failures by 67%

## Implementation
The method uses Claude to automatically generate contextual summaries (typically 50-100 tokens) for each chunk. With prompt caching, the cost is approximately "$1.02 per million document tokens."

## Key Findings
Developers should combine contextual embeddings (using Gemini or Voyage models) with BM25 techniques, reranking, and retrieving the top 20 chunks for optimal performance.
