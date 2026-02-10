---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:28Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/sql-sorcerer"
title: "SQL sorcerer - Claude API Docs"
---

Prompt Library

# SQL sorcerer

Copy page

Transform everyday language into SQL queries.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example output

``` shiki
SELECT c.first_name, c.last_name, SUM(o.total_amount) AS total_spent
FROM Customers c
INNER JOIN Orders o ON c.customer_id = o.customer_id
LEFT JOIN Reviews r ON c.customer_id = r.customer_id
WHERE r.review_id IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name;
```

## 

API Request

------------------------------------------------------------------------

Python

Python

TypeScript

TypeScript

AWS Bedrock Python

AWS Bedrock Python

AWS Bedrock TypeScript

AWS Bedrock TypeScript

Vertex AI Python

Vertex AI Python

Vertex AI TypeScript

Vertex AI TypeScript

``` shiki
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-opus-4-6",
  max_tokens=1000,
  temperature=0,
  system="Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists: \n \nCustomers: \n- customer_id (INT, PRIMARY KEY) \n- first_name (VARCHAR) \n- last_name (VARCHAR) \n- email (VARCHAR) \n- phone (VARCHAR) \n- address (VARCHAR) \n- city (VARCHAR) \n- state (VARCHAR) \n- zip_code (VARCHAR) \n \nProducts: \n- product_id (INT, PRIMARY KEY) \n- product_name (VARCHAR) \n- description (TEXT) \n- category (VARCHAR) \n- price (DECIMAL) \n- stock_quantity (INT) \n \nOrders: \n- order_id (INT, PRIMARY KEY) \n- customer_id (INT, FOREIGN KEY REFERENCES Customers) \n- order_date (DATE) \n- total_amount (DECIMAL) \n- status (VARCHAR) \n \nOrder_Items: \n- order_item_id (INT, PRIMARY KEY) \n- order_id (INT, FOREIGN KEY REFERENCES Orders) \n- product_id (INT, FOREIGN KEY REFERENCES Products) \n- quantity (INT) \n- price (DECIMAL) \n \nReviews: \n- review_id (INT, PRIMARY KEY) \n- product_id (INT, FOREIGN KEY REFERENCES Products) \n- customer_id (INT, FOREIGN KEY REFERENCES Customers) \n- rating (INT) \n- comment (TEXT) \n- review_date (DATE) \n \nEmployees: \n- employee_id (INT, PRIMARY KEY) \n- first_name (VARCHAR) \n- last_name (VARCHAR) \n- email (VARCHAR) \n- phone (VARCHAR) \n- hire_date (DATE) \n- job_title (VARCHAR) \n- department (VARCHAR) \n- salary (DECIMAL) \n \nProvide the SQL query that would retrieve the data based on the natural language request.",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders."
        }
      ]
    }
  ]
)
print(message.content)
```

``` inline-block
 
```

Was this page helpful?

- 

- [Example output](#example-output)

- [API Request](#api-request)

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
