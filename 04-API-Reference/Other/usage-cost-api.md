::: {#9610be80 .cell .markdown id="9610be80"}
# Usage & Cost Admin API Cookbook {#usage--cost-admin-api-cookbook}

**A practical guide to programmatically accessing your Claude API usage
and cost data**
:::

::: {#69b800fc .cell .markdown id="69b800fc"}
### What You Can Do

**Usage Tracking:**

- Monitor token consumption (uncached input, output, cache
  creation/reads)
- Track usage across models, workspaces, and API keys
- Analyze cache efficiency and server tool usage

**Cost Analysis:**

- Retrieve detailed cost breakdowns by service type
- Monitor spending trends across workspaces
- Generate reports for finance and chargeback scenarios

**Common Use Cases:**

- **Usage Monitoring**: Track consumption patterns and optimize costs
- **Cost Attribution**: Allocate expenses across teams/projects by
  workspace
- **Cache Analysis**: Measure and improve cache efficiency
- **Financial Reporting**: Generate executive summaries and budget
  reports

### API Overview

Two main endpoints:

1.  **Messages Usage API**: Token-level usage data with flexible
    grouping
2.  **Cost API**: Financial data in USD with service breakdowns

### Prerequisites & Security {#prerequisites--security}

- **Admin API Key**: Get from [Claude
  Console](https://console.anthropic.com/settings/admin-keys) (format:
  `sk-ant-admin...`)
- **Security**: Store keys in environment variables, rotate regularly,
  never commit to version control
:::

::: {#edd50a16 .cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="edd50a16" outputId="68f38db3-48ee-429f-cd6e-2d2ae74e009a"}
``` python
import os
from datetime import datetime, time, timedelta
from typing import Any

import requests


class AnthropicAdminAPI:
    """Secure wrapper for Anthropic Admin API endpoints."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_ADMIN_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Admin API key required. Set ANTHROPIC_ADMIN_API_KEY environment variable."
            )

        if not self.api_key.startswith("sk-ant-admin"):
            raise ValueError("Invalid Admin API key format.")

        self.base_url = "https://api.anthropic.com/v1/organizations"
        self.headers = {
            "anthropic-version": "2023-06-01",
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
        }

    def _make_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Make authenticated request with basic error handling."""
        url = f"{self.base_url}/{endpoint}"

        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                raise ValueError("Invalid API key or insufficient permissions") from e
            elif response.status_code == 429:
                raise requests.exceptions.RequestException(
                    "Rate limit exceeded - try again later"
                ) from e
            else:
                raise requests.exceptions.RequestException(f"API error: {e}") from e


# Test connection
def test_connection():
    try:
        client = AnthropicAdminAPI()

        # Simple test query - snap to start of day to align with bucket boundaries
        params = {
            "starting_at": (
                datetime.combine(datetime.utcnow(), time.min) - timedelta(days=1)
            ).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "ending_at": datetime.combine(datetime.utcnow(), time.min).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
            "bucket_width": "1d",
            "limit": 1,
        }

        client._make_request("usage_report/messages", params)
        print("✅ Connection successful!")
        return client

    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return None


client = test_connection()
```
:::

::: {#781a0721 .cell .markdown id="781a0721"}
## Basic Usage & Cost Tracking {#basic-usage--cost-tracking}

### Understanding Usage Data

The Messages Usage API provides token consumption in **time buckets** -
fixed intervals containing aggregated usage.

**Key Metrics:**

- **uncached_input_tokens**: New input tokens (prompts, system messages)
- **output_tokens**: Claude\'s responses
- **cache_creation**: Tokens cached for reuse
- **cache_read_input_tokens**: Previously cached tokens reused

### Basic Usage Query
:::

:::: {#f9b26143 .cell .code execution_count="12" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="f9b26143" outputId="c60b91c0-084d-4629-eddd-cf0fb941e042"}
``` python
def get_daily_usage(client, days_back=7):
    """Get usage data for the last N days."""
    end_time = datetime.combine(datetime.utcnow(), time.min)
    start_time = end_time - timedelta(days=days_back)

    params = {
        "starting_at": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ending_at": end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "bucket_width": "1d",
        "limit": days_back,
    }

    return client._make_request("usage_report/messages", params)


def analyze_usage_data(response):
    """Process and display usage data."""
    if not response or not response.get("data"):
        print("No usage data found.")
        return

    total_uncached_input = total_output = total_cache_creation = 0
    total_cache_reads = total_web_searches = 0
    daily_data = []

    for bucket in response["data"]:
        date = bucket["starting_at"][:10]

        # Sum all results in bucket
        bucket_uncached = bucket_output = bucket_cache_creation = 0
        bucket_cache_reads = bucket_web_searches = 0

        for result in bucket["results"]:
            bucket_uncached += result.get("uncached_input_tokens", 0)
            bucket_output += result.get("output_tokens", 0)

            cache_creation = result.get("cache_creation", {})
            bucket_cache_creation += cache_creation.get(
                "ephemeral_1h_input_tokens", 0
            ) + cache_creation.get("ephemeral_5m_input_tokens", 0)
            bucket_cache_reads += result.get("cache_read_input_tokens", 0)

            server_tools = result.get("server_tool_use", {})
            bucket_web_searches += server_tools.get("web_search_requests", 0)

        daily_data.append(
            {
                "date": date,
                "uncached_input_tokens": bucket_uncached,
                "output_tokens": bucket_output,
                "cache_creation": bucket_cache_creation,
                "cache_reads": bucket_cache_reads,
                "web_searches": bucket_web_searches,
                "total_tokens": bucket_uncached + bucket_output,
            }
        )

        # Add to totals
        total_uncached_input += bucket_uncached
        total_output += bucket_output
        total_cache_creation += bucket_cache_creation
        total_cache_reads += bucket_cache_reads
        total_web_searches += bucket_web_searches

    # Calculate cache efficiency
    total_input_tokens = total_uncached_input + total_cache_creation + total_cache_reads
    cache_efficiency = (
        (total_cache_reads / total_input_tokens * 100) if total_input_tokens > 0 else 0
    )

    # Display summary
    print("📊 Usage Summary:")
    print(f"Uncached input tokens: {total_uncached_input:,}")
    print(f"Output tokens: {total_output:,}")
    print(f"Cache creation: {total_cache_creation:,}")
    print(f"Cache reads: {total_cache_reads:,}")
    print(f"Cache efficiency: {cache_efficiency:.1f}%")
    print(f"Web searches: {total_web_searches:,}")

    return daily_data


# Example usage
if client:
    usage_response = get_daily_usage(client, days_back=7)
    daily_usage = analyze_usage_data(usage_response)
```

::: {.output .stream .stdout}
    📊 Usage Summary:
    Uncached input tokens: 267,751
    Output tokens: 2,848,746
    Cache creation: 0
    Cache reads: 0
    Cache efficiency: 0.0%
    Web searches: 0
:::
::::

::: {#e3164089 .cell .markdown id="e3164089"}
## Basic Cost Tracking

Note: Priority Tier costs use a different billing model and will never
appear in the cost endpoint. You can track Priority Tier usage in the
usage endpoint, but not costs.
:::

:::: {#SP4zefdtF0ft .cell .code execution_count="13" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="SP4zefdtF0ft" outputId="a1daa8d0-f36f-474b-9967-6fe00a0efe52"}
``` python
def get_daily_costs(client, days_back=7):
    """Get cost data for the last N days."""
    end_time = datetime.combine(datetime.utcnow(), time.min)
    start_time = end_time - timedelta(days=days_back)

    params = {
        "starting_at": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ending_at": end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "bucket_width": "1d",  # Only 1d supported for cost API
        "limit": min(days_back, 31),  # Max 31 days per request
    }

    return client._make_request("cost_report", params)


def analyze_cost_data(response):
    """Process and display cost data."""
    if not response or not response.get("data"):
        print("No cost data found.")
        return

    total_cost_minor_units = 0
    daily_costs = []

    for bucket in response["data"]:
        date = bucket["starting_at"][:10]

        # Sum all costs in this bucket
        bucket_cost = 0
        for result in bucket["results"]:
            # Convert string amounts to float if needed
            amount = result.get("amount", 0)
            if isinstance(amount, str):
                try:
                    amount = float(amount)
                except (ValueError, TypeError):
                    amount = 0
            bucket_cost += amount

        daily_costs.append(
            {
                "date": date,
                "cost_minor_units": bucket_cost,
                "cost_usd": bucket_cost / 100,  # Convert to dollars
            }
        )

        total_cost_minor_units += bucket_cost

    total_cost_usd = total_cost_minor_units / 100

    print("💰 Cost Summary:")
    print(f"Total cost: ${total_cost_usd:.4f}")
    print(f"Average daily cost: ${total_cost_usd / len(daily_costs):.4f}")

    return daily_costs


# Example usage
if client:
    cost_response = get_daily_costs(client, days_back=7)
    daily_costs = analyze_cost_data(cost_response)
```

::: {.output .stream .stdout}
    💰 Cost Summary:
    Total cost: $83.7574
    Average daily cost: $11.9653
:::
::::

::: {#6ce76fc4 .cell .markdown id="6ce76fc4"}
## Grouping, Filtering & Pagination {#grouping-filtering--pagination}

### Time Granularity Options

**Usage API** supports three granularities:

- `1m` (1 minute): High-resolution analysis, max 1440 buckets per
  request
- `1h` (1 hour): Medium-resolution, max 168 buckets per request\
- `1d` (1 day): Daily analysis, max 31 buckets per request

**Cost API** supports:

- `1d` (1 day): Only option available, max 31 buckets per request

### Grouping and Filtering
:::

:::: {#87f1a7ac .cell .code execution_count="14" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="87f1a7ac" outputId="3266318c-8af4-4647-9360-b133ffa82452"}
``` python
def get_usage_by_model(client, days_back=7):
    """Get usage data grouped by model, handling pagination automatically."""
    end_time = datetime.combine(datetime.utcnow(), time.min)
    start_time = end_time - timedelta(days=days_back)

    params = {
        "starting_at": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ending_at": end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "group_by[]": ["model"],
        "bucket_width": "1d",
    }

    # Aggregate across all pages of data
    model_usage = {}
    page_count = 0
    max_pages = 10  # Reasonable limit to avoid infinite loops

    try:
        next_page = None

        while page_count < max_pages:
            current_params = params.copy()
            if next_page:
                current_params["page"] = next_page

            response = client._make_request("usage_report/messages", current_params)
            page_count += 1

            # Process this page's data
            for bucket in response.get("data", []):
                for result in bucket.get("results", []):
                    model = result.get("model", "Unknown")
                    uncached = result.get("uncached_input_tokens", 0)
                    output = result.get("output_tokens", 0)
                    cache_creation = result.get("cache_creation", {})
                    cache_creation_tokens = cache_creation.get(
                        "ephemeral_1h_input_tokens", 0
                    ) + cache_creation.get("ephemeral_5m_input_tokens", 0)
                    cache_reads = result.get("cache_read_input_tokens", 0)
                    tokens = uncached + output + cache_creation_tokens + cache_reads

                    if model not in model_usage:
                        model_usage[model] = 0
                    model_usage[model] += tokens

            # Check if there's more data
            if not response.get("has_more", False):
                break

            next_page = response.get("next_page")
            if not next_page:
                break

    except Exception as e:
        print(f"❌ Error retrieving usage data: {e}")
        return {}

    # Display results
    print("📊 Usage by Model:")
    if not model_usage:
        print(f"  No usage data found in the last {days_back} days")
        print("  💡 Try increasing the time range or check if you have recent API usage")
    else:
        for model, tokens in sorted(model_usage.items(), key=lambda x: x[1], reverse=True):
            print(f"  {model}: {tokens:,} tokens")

    return model_usage


def filter_usage_example(client):
    """Example of filtering usage data."""
    params = {
        "starting_at": (datetime.combine(datetime.utcnow(), time.min) - timedelta(days=7)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "ending_at": datetime.combine(datetime.utcnow(), time.min).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "models[]": ["claude-sonnet-4-5"],  # Filter to specific model
        "service_tiers[]": ["standard"],  # Filter to standard tier
        "bucket_width": "1d",
    }

    response = client._make_request("usage_report/messages", params)
    print(f"Found {len(response.get('data', []))} days of filtered usage data")
    return response


# Example usage
if client:
    model_usage = get_usage_by_model(client, days_back=14)
    filtered_usage = filter_usage_example(client)
```

::: {.output .stream .stdout}
    📊 Usage by Model:
      claude-3-5-haiku-20241022: 995,781 tokens
      claude-sonnet-4-5: 861,880 tokens
      claude-opus-4-1: 394,646 tokens
      claude-sonnet-4-5: 356,766 tokens
      claude-opus-4-20250514: 308,223 tokens
      claude-opus-4-1: 199,201 tokens
    Found 7 days of filtered usage data
:::
::::

::: {#487bc11d .cell .markdown id="487bc11d"}
### Pagination for Large Datasets
:::

:::: {#d7cc5437 .cell .code execution_count="18" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="d7cc5437" outputId="e7875fb4-09ae-44d2-f5fc-12a4cbdcce5a"}
``` python
def fetch_all_usage_data(client, params, max_pages=10):
    """Fetch all paginated usage data."""
    all_data = []
    page_count = 0
    next_page = None

    print("📥 Fetching paginated data...")

    while page_count < max_pages:
        current_params = params.copy()
        if next_page:
            current_params["page"] = next_page

        try:
            response = client._make_request("usage_report/messages", current_params)

            if not response or not response.get("data"):
                break

            page_data = response["data"]
            all_data.extend(page_data)
            page_count += 1

            print(f"  Page {page_count}: {len(page_data)} time buckets")

            if not response.get("has_more", False):
                print(f"✅ Complete: Retrieved all data in {page_count} pages")
                break

            next_page = response.get("next_page")
            if not next_page:
                break

        except Exception as e:
            print(f"❌ Error on page {page_count + 1}: {e}")
            break

    print(f"📊 Total retrieved: {len(all_data)} time buckets")
    return all_data


def large_dataset_example(client, days_back=3):
    """Example of handling a large dataset with pagination."""
    # Use recent time range to ensure we have data
    start_time = datetime.combine(datetime.utcnow(), time.min) - timedelta(days=days_back)
    end_time = datetime.combine(datetime.utcnow(), time.min)

    params = {
        "starting_at": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ending_at": end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "bucket_width": "1h",  # Hourly data for more buckets
        "group_by[]": ["model"],
        "limit": 24,  # One day per page
    }

    all_buckets = fetch_all_usage_data(client, params, max_pages=5)

    # Process the large dataset
    if all_buckets:
        total_tokens = sum(
            sum(
                result.get("uncached_input_tokens", 0) + result.get("output_tokens", 0)
                for result in bucket["results"]
            )
            for bucket in all_buckets
        )
        print(f"📈 Total tokens across all data: {total_tokens:,}")

    return all_buckets


# Example usage - use shorter time range to find recent data
if client:
    large_dataset = large_dataset_example(client, days_back=3)
```

::: {.output .stream .stdout}
    📥 Fetching paginated data...
      Page 1: 24 time buckets
      Page 2: 24 time buckets
      Page 3: 24 time buckets
    ✅ Complete: Retrieved all data in 3 pages
    📊 Total retrieved: 72 time buckets
    📈 Total tokens across all data: 1,336,287
:::
::::

::: {#d55bbb55 .cell .markdown id="d55bbb55"}
## Simple Data Export

### CSV Export for External Analysis
:::

:::: {#f365296a .cell .code execution_count="16" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="f365296a" outputId="87b4a733-6f90-4b8d-a109-7a23281b2a4d"}
``` python
import csv


def export_usage_to_csv(client, output_file="usage_data.csv", days_back=30):
    """Export usage data to CSV for external analysis."""

    end_time = datetime.combine(datetime.utcnow(), time.min)
    start_time = end_time - timedelta(days=days_back)

    params = {
        "starting_at": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ending_at": end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "group_by[]": ["model", "service_tier", "workspace_id"],
        "bucket_width": "1d",
    }

    try:
        # Collect all data across pages
        rows = []
        page_count = 0
        max_pages = 20  # Allow more pages for export
        next_page = None

        while page_count < max_pages:
            current_params = params.copy()
            if next_page:
                current_params["page"] = next_page

            response = client._make_request("usage_report/messages", current_params)
            page_count += 1

            # Process this page's data
            for bucket in response.get("data", []):
                date = bucket["starting_at"][:10]
                for result in bucket["results"]:
                    rows.append(
                        {
                            "date": date,
                            "model": result.get("model", ""),
                            "service_tier": result.get("service_tier", ""),
                            "workspace_id": result.get("workspace_id", ""),
                            "uncached_input_tokens": result.get("uncached_input_tokens", 0),
                            "output_tokens": result.get("output_tokens", 0),
                            "cache_creation_tokens": (
                                result.get("cache_creation", {}).get("ephemeral_1h_input_tokens", 0)
                                + result.get("cache_creation", {}).get(
                                    "ephemeral_5m_input_tokens", 0
                                )
                            ),
                            "cache_read_tokens": result.get("cache_read_input_tokens", 0),
                            "web_search_requests": result.get("server_tool_use", {}).get(
                                "web_search_requests", 0
                            ),
                        }
                    )

            # Check if there's more data
            if not response.get("has_more", False):
                break

            next_page = response.get("next_page")
            if not next_page:
                break

        # Write CSV
        if rows:
            with open(output_file, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)

            print(f"✅ Exported {len(rows)} rows to {output_file}")
        else:
            print(f"No usage data to export for the last {days_back} days")
            print("💡 Try increasing days_back or check if you have recent API usage")

    except Exception as e:
        print(f"❌ Export failed: {e}")


def export_costs_to_csv(client, output_file="cost_data.csv", days_back=30):
    """Export cost data to CSV."""

    end_time = datetime.combine(datetime.utcnow(), time.min)
    start_time = end_time - timedelta(days=days_back)

    params = {
        "starting_at": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ending_at": end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "group_by[]": ["workspace_id", "description"],
    }

    try:
        # Collect all data across pages
        rows = []
        page_count = 0
        max_pages = 20
        next_page = None

        while page_count < max_pages:
            current_params = params.copy()
            if next_page:
                current_params["page"] = next_page

            response = client._make_request("cost_report", current_params)
            page_count += 1

            # Process this page's data
            for bucket in response.get("data", []):
                date = bucket["starting_at"][:10]
                for result in bucket["results"]:
                    # Handle both string and numeric amounts
                    amount = result.get("amount", 0)
                    if isinstance(amount, str):
                        try:
                            amount = float(amount)
                        except (ValueError, TypeError):
                            amount = 0

                    rows.append(
                        {
                            "date": date,
                            "workspace_id": result.get(
                                "workspace_id", ""
                            ),  # null for default workspace
                            "description": result.get("description", ""),
                            "currency": result.get("currency", "USD"),
                            "amount_usd": amount / 100,
                        }
                    )

            # Check if there's more data
            if not response.get("has_more", False):
                break

            next_page = response.get("next_page")
            if not next_page:
                break

        if rows:
            with open(output_file, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)

            print(f"✅ Exported {len(rows)} cost records to {output_file}")
        else:
            print(f"No cost data to export for the last {days_back} days")
            print("💡 Try increasing days_back or check if you have recent API usage")

    except Exception as e:
        print(f"❌ Cost export failed: {e}")


# Example usage
if client:
    export_usage_to_csv(client, "my_usage_data.csv", days_back=14)
    export_costs_to_csv(client, "my_cost_data.csv", days_back=14)
```

::: {.output .stream .stdout}
    ✅ Exported 36 rows to my_usage_data.csv
    ✅ Exported 72 cost records to my_cost_data.csv
:::
::::

::: {#5327a1c5 .cell .markdown id="5327a1c5"}
## Wrapping Up

This cookbook covers the essential patterns for working with the Usage &
Cost Admin API:

- **Basic queries** for usage and cost data
- **Grouping and filtering** for detailed analysis\
- **Pagination** for large datasets
- **Cost description parsing** for categorization
- **Common gotchas** to avoid issues
- **Simple CSV export** for external tools

### Next Steps

- Check the [official API documentation](https://docs.claude.com) for
  the latest field definitions
- Test your integration with small date ranges first
- Consider data retention needs for your use case
- Monitor for new API features that may enhance your analysis

### Important Notes

- Field names and available options may evolve as the API matures
- Always handle unknown values gracefully in production code
- The API is designed for historical analysis, not real-time monitoring
- Priority Tier costs use a different billing model and don\'t appear in
  cost endpoints

Happy analyzing! 📊
:::
