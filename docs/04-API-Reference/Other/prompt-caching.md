::: {.cell .markdown}
# Prompt caching through the Claude API

Prompt caching allows you to store and reuse context within your prompt.
This makes it more practical to include additional information in your
prompt---such as detailed instructions and example responses---which
help improve every response Claude generates.

In addition, by fully leveraging prompt caching within your prompt, you
can reduce latency by \>2x and costs up to 90%. This can generate
significant savings when building solutions that involve repetitive
tasks around detailed book_content.

In this cookbook, we will demonstrate how to use prompt caching in a
single turn and across a multi-turn conversation.
:::

::: {.cell .markdown vscode="{\"languageId\":\"plaintext\"}"}
## Setup

First, let\'s set up our environment with the necessary imports and
initializations:
:::

:::: {.cell .code execution_count="3"}
``` python
%pip install anthropic bs4 --quiet
```

::: {.output .stream .stdout}
    Note: you may need to restart the kernel to use updated packages.
:::
::::

::: {.cell .code execution_count="16"}
``` python
import time

import anthropic
import requests
from bs4 import BeautifulSoup

client = anthropic.Anthropic()
MODEL_NAME = "claude-sonnet-4-5"
TIMESTAMP = int(time.time())
```
:::

::: {.cell .markdown}
Now let\'s fetch some text content to use in our examples. We\'ll use
the text from Pride and Prejudice by Jane Austen which is around
\~187,000 tokens long.
:::

::: {.cell .code}
``` python
def fetch_article_content(url):
    response = requests.get(url, timeout=30)
    soup = BeautifulSoup(response.content, "html.parser")

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Get text
    text = soup.get_text()

    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = "\n".join(chunk for chunk in chunks if chunk)

    return text


# Fetch the content of the article
book_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
book_content = fetch_article_content(book_url)

print(f"Fetched {len(book_content)} characters from the book.")
print("First 500 characters:")
print(book_content[:500])
```
:::

::: {.cell .markdown}
## Example 1: Single turn

Let\'s demonstrate prompt caching with a large document, comparing the
performance and cost between cached and non-cached API calls.
:::

::: {.cell .markdown}
### Part 1: Non-cached API Call (Baseline)

First, let\'s make a truly non-cached API call **without** the
`cache_control` parameter. This will establish our baseline performance.

We\'ll ask for a short output to keep response generation time low,
since prompt caching only affects input processing time.
:::

:::: {.cell .code execution_count="17"}
``` python
def make_non_cached_api_call():
    """Make an API call WITHOUT cache_control - no caching enabled."""
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": str(TIMESTAMP) + "<book>" + book_content + "</book>",
                    # Note: No cache_control parameter here - this is truly non-cached
                },
                {"type": "text", "text": "What is the title of this book? Only output the title."},
            ],
        }
    ]

    start_time = time.time()
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=300,
        messages=messages,
    )
    end_time = time.time()

    return response, end_time - start_time


non_cached_response, non_cached_time = make_non_cached_api_call()

print(f"Non-cached API call time: {non_cached_time:.2f} seconds")
print(f"Input tokens: {non_cached_response.usage.input_tokens}")
print(f"Output tokens: {non_cached_response.usage.output_tokens}")

print("\nResponse:")
print(non_cached_response.content[0].text)
```

::: {.output .stream .stdout}
    Non-cached API call time: 6.86 seconds
    Input tokens: 187363
    Output tokens: 8

    Response:
    Pride and Prejudice
:::
::::

::: {.cell .markdown}
### Part 2: First Cached API Call (Cache Creation)

Now let\'s enable prompt caching by adding
`cache_control: {"type": "ephemeral"}` to the book content.

**Important:** The first call with `cache_control` will **create** the
cache entry. This initial call will have similar timing to the
non-cached call because it still needs to process all tokens. However,
it will store them in the cache for future use.

Look for the `cache_creation_input_tokens` field in the usage stats to
see how many tokens were cached.
:::

:::: {.cell .code execution_count="18"}
``` python
def make_cached_api_call_create():
    """First call WITH cache_control - creates the cache entry."""
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": str(TIMESTAMP) + "<book>" + book_content + "</book>",
                    "cache_control": {"type": "ephemeral"},  # This enables caching
                },
                {"type": "text", "text": "What is the title of this book? Only output the title."},
            ],
        }
    ]

    start_time = time.time()
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=300,
        messages=messages,
    )
    end_time = time.time()

    return response, end_time - start_time


cached_create_response, cached_create_time = make_cached_api_call_create()

print(f"First cached API call time: {cached_create_time:.2f} seconds")
print(f"Input tokens: {cached_create_response.usage.input_tokens}")
print(f"Output tokens: {cached_create_response.usage.output_tokens}")
print(
    f"Cache creation tokens: {getattr(cached_create_response.usage, 'cache_creation_input_tokens', 0)}"
)

print("\nResponse:")
print(cached_create_response.content[0].text)

print(
    "\nNote: This first call creates the cache but doesn't benefit from it yet - timing is similar to non-cached call."
)
```

::: {.output .stream .stdout}
    First cached API call time: 5.96 seconds
    Input tokens: 16
    Output tokens: 8
    Cache creation tokens: 187347

    Response:
    Pride and Prejudice

    Note: This first call creates the cache but doesn't benefit from it yet - timing is similar to non-cached call.
:::
::::

::: {.cell .markdown}
### Part 3: Second Cached API Call (Cache Hit)

Now let\'s make another API call with the same `cache_control`
parameter. Since the cache was created in Part 2, this call will **read
from the cache** instead of processing all tokens again.

This is where you see the real performance benefit! Look for the
`cache_read_input_tokens` field in the usage stats.
:::

:::: {.cell .code execution_count="19"}
``` python
def make_cached_api_call_hit():
    """Second call WITH cache_control - reads from existing cache."""
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": str(TIMESTAMP) + "<book>" + book_content + "</book>",
                    "cache_control": {"type": "ephemeral"},  # Same cache_control as before
                },
                {"type": "text", "text": "What is the title of this book? Only output the title."},
            ],
        }
    ]

    start_time = time.time()
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=300,
        messages=messages,
    )
    end_time = time.time()

    return response, end_time - start_time


cached_hit_response, cached_hit_time = make_cached_api_call_hit()

print(f"Second cached API call time: {cached_hit_time:.2f} seconds")
print(f"Input tokens: {cached_hit_response.usage.input_tokens}")
print(f"Output tokens: {cached_hit_response.usage.output_tokens}")
print(f"Cache read tokens: {getattr(cached_hit_response.usage, 'cache_read_input_tokens', 0)}")

print("\nResponse:")
print(cached_hit_response.content[0].text)

print("\n" + "=" * 70)
print("PERFORMANCE COMPARISON")
print("=" * 70)
print(f"Non-cached call:       {non_cached_time:.2f}s")
print(f"First cached call:     {cached_create_time:.2f}s (creates cache)")
print(f"Second cached call:    {cached_hit_time:.2f}s (reads from cache)")
print(f"\nSpeedup from caching:  {non_cached_time / cached_hit_time:.1f}x faster!")
print("=" * 70)
```

::: {.output .stream .stdout}
    Second cached API call time: 3.66 seconds
    Input tokens: 16
    Output tokens: 8
    Cache read tokens: 187347

    Response:
    Pride and Prejudice

    ======================================================================
    PERFORMANCE COMPARISON
    ======================================================================
    Non-cached call:       6.86s
    First cached call:     5.96s (creates cache)
    Second cached call:    3.66s (reads from cache)

    Speedup from caching:  1.9x faster!
    ======================================================================
:::
::::

::: {.cell .markdown}
## Summary of Example 1

This example demonstrated three distinct scenarios:

1.  **Non-cached call** - Without `cache_control`, Claude processes all
    \~187k tokens normally
2.  **First cached call** - With `cache_control`, Claude processes all
    tokens AND stores them in cache (similar timing to non-cached)
3.  **Second cached call** - With `cache_control`, Claude reads from the
    existing cache (2-10x faster!)

The key insight: **Prompt caching requires two calls to show benefits**

- The first call with `cache_control` creates the cache entry
- Subsequent calls with the same `cache_control` read from the cache for
  dramatic speedups

This is especially valuable for:

- Large documents or codebases that remain constant across multiple
  queries
- System prompts with detailed instructions
- Multi-turn conversations (as shown in Example 2 below)
:::

::: {.cell .markdown}
## Example 2: Multi-turn Conversation with Incremental Caching

Now, let\'s look at a multi-turn conversation where we add cache
breakpoints as the conversation progresses.
:::

:::: {.cell .code execution_count="21"}
``` python
class ConversationHistory:
    def __init__(self):
        # Initialize an empty list to store conversation turns
        self.turns = []

    def add_turn_assistant(self, content):
        # Add an assistant's turn to the conversation history
        self.turns.append({"role": "assistant", "content": [{"type": "text", "text": content}]})

    def add_turn_user(self, content):
        # Add a user's turn to the conversation history
        self.turns.append({"role": "user", "content": [{"type": "text", "text": content}]})

    def get_turns(self):
        # Retrieve conversation turns with specific formatting
        result = []
        user_turns_processed = 0
        # Iterate through turns in reverse order
        for turn in reversed(self.turns):
            if turn["role"] == "user" and user_turns_processed < 1:
                # Add the last user turn with ephemeral cache control
                result.append(
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": turn["content"][0]["text"],
                                "cache_control": {"type": "ephemeral"},
                            }
                        ],
                    }
                )
                user_turns_processed += 1
            else:
                # Add other turns as they are
                result.append(turn)
        # Return the turns in the original order
        return list(reversed(result))


# Initialize the conversation history
conversation_history = ConversationHistory()

# System message containing the book content
# Note: 'book_content' should be defined elsewhere in the code
system_message = f"{TIMESTAMP} <file_contents> {book_content} </file_contents>"

# Predefined questions for our simulation
questions = [
    "What is the title of this novel?",
    "Who are Mr. and Mrs. Bennet?",
    "What is Netherfield Park?",
    "What is the main theme of this novel?",
]


def simulate_conversation():
    for i, question in enumerate(questions, 1):
        print(f"\nTurn {i}:")
        print(f"User: {question}")

        # Add user input to conversation history
        conversation_history.add_turn_user(question)

        # Record the start time for performance measurement
        start_time = time.time()

        # Make an API call to the assistant
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=300,
            system=[
                {"type": "text", "text": system_message, "cache_control": {"type": "ephemeral"}},
            ],
            messages=conversation_history.get_turns(),
        )

        # Record the end time
        end_time = time.time()

        # Extract the assistant's reply
        assistant_reply = response.content[0].text
        print(f"Assistant: {assistant_reply}")

        # Print token usage information
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens
        input_tokens_cache_read = getattr(response.usage, "cache_read_input_tokens", "---")
        input_tokens_cache_create = getattr(response.usage, "cache_creation_input_tokens", "---")
        print(f"User input tokens: {input_tokens}")
        print(f"Output tokens: {output_tokens}")
        print(f"Input tokens (cache read): {input_tokens_cache_read}")
        print(f"Input tokens (cache write): {input_tokens_cache_create}")

        # Calculate and print the elapsed time
        elapsed_time = end_time - start_time

        # Calculate the percentage of input prompt cached
        total_input_tokens = input_tokens + (
            int(input_tokens_cache_read) if input_tokens_cache_read != "---" else 0
        )
        percentage_cached = (
            int(input_tokens_cache_read) / total_input_tokens * 100
            if input_tokens_cache_read != "---" and total_input_tokens > 0
            else 0
        )

        print(f"{percentage_cached:.1f}% of input prompt cached ({total_input_tokens} tokens)")
        print(f"Time taken: {elapsed_time:.2f} seconds")

        # Add assistant's reply to conversation history
        conversation_history.add_turn_assistant(assistant_reply)


# Run the simulated conversation
simulate_conversation()
```

::: {.output .stream .stdout}

    Turn 1:
    User: What is the title of this novel?
    Assistant: The title of this novel is **Pride and Prejudice** by Jane Austen.
    User input tokens: 3
    Output tokens: 22
    Input tokens (cache read): 0
    Input tokens (cache write): 187360
    0.0% of input prompt cached (3 tokens)
    Time taken: 5.79 seconds

    Turn 2:
    User: Who are Mr. and Mrs. Bennet?
    Assistant: Mr. and Mrs. Bennet are the parents of five daughters: Jane, Elizabeth, Mary, Kitty, and Lydia. 

    **Mr. Bennet** is described as an intelligent, sarcastic man with "quick parts, sarcastic humour, reserve, and caprice." He tends to be detached and ironic, often amusing himself at his wife's expense, and prefers to spend time in his library rather than deal with family matters.

    **Mrs. Bennet** is described as "a woman of mean understanding, little information, and uncertain temper." She is nervous, excitable, and foolish, with her main goal in life being to get her daughters married. She lacks the intelligence and social graces of her husband and is often oblivious to her own impropriety.

    Their contrasting personalities create much of the domestic tension and comedy in the novel. Mr. Bennet married Mrs. Bennet when he was "captivated by youth and beauty," but her weak understanding soon ended any real affection he had for her, leaving him to cope with his disappointment through ironic detachment.
    User input tokens: 3
    Output tokens: 247
    Input tokens (cache read): 187360
    Input tokens (cache write): 36
    100.0% of input prompt cached (187363 tokens)
    Time taken: 8.29 seconds

    Turn 3:
    User: What is Netherfield Park?
    Assistant: **Netherfield Park** is a large estate in Hertfordshire that is rented by Mr. Bingley at the beginning of the novel. 

    It is located about three miles from Longbourn, the Bennet family's home, making it conveniently close for social visits. The estate becomes the center of much excitement and speculation when Mr. Bingley, a wealthy young bachelor, takes up residence there.

    Key points about Netherfield:

    - It's described as a good house with pleasant grounds
    - Mr. Bingley rents it (rather than owning it), as he has not yet purchased an estate of his own
    - His sisters, Caroline Bingley and Mrs. Hurst, live with him there, along with Mrs. Hurst's husband
    - Mr. Darcy, Bingley's close friend, is a frequent visitor
    - The famous ball where Elizabeth and Darcy have their first significant interactions takes place at Netherfield
    - Jane Bennet stays there when she falls ill after riding over in the rain, which allows Elizabeth to visit and spend time at the estate

    Netherfield Park is important to the plot as it brings the wealthy Mr. Bingley (and Mr. Darcy) into the neighborhood, setting the main romantic storylines in motion.
    User input tokens: 3
    Output tokens: 293
    Input tokens (cache read): 187396
    Input tokens (cache write): 258
    100.0% of input prompt cached (187399 tokens)
    Time taken: 10.14 seconds

    Turn 4:
    User: What is the main theme of this novel?
    Assistant: The main themes of **Pride and Prejudice** include:

    **1. Pride and Prejudice (as the title suggests)**
    - The novel explores how pride and prejudice create misunderstandings and obstacles to happiness
    - **Darcy's pride** in his social status initially leads him to insult Elizabeth and look down on her family
    - **Elizabeth's prejudice** against Darcy (based on first impressions and Wickham's lies) blinds her to his true character
    - Both must overcome these flaws to find happiness together

    **2. Class and Social Status**
    - The rigid class distinctions of Regency England and their impact on relationships and marriage prospects
    - The tension between wealth, birth, and merit as measures of a person's worth
    - Lady Catherine's objections to Elizabeth based on her "inferior" connections

    **3. Marriage and Economics**
    - The novel examines different motivations for marriage: love (Jane and Bingley), practicality (Charlotte and Mr. Collins), lust and recklessness (Lydia and Wickham), and the ideal combination of respect, affection, and compatibility (Elizabeth and Darcy)
    - The economic pressures on women to marry well, especially with the entailment of the Bennet estate

    **4. Self-Knowledge and Personal Growth**
    - Elizabeth's journey from prejudice to understanding
    User input tokens: 3
    Output tokens: 300
    Input tokens (cache read): 187654
    Input tokens (cache write): 305
    100.0% of input prompt cached (187657 tokens)
    Time taken: 9.53 seconds
:::
::::

::: {.cell .markdown}
As you can see in this example, response times decreased from nearly 24
seconds to just 7-11 seconds after the initial cache setup, while
maintaining the same level of quality across the answers. Most of this
remaining latency is due to the time it takes to generate the response,
which is not affected by prompt caching.

And since nearly 100% of input tokens were cached in subsequent turns as
we kept adjusting the cache breakpoints, we were able to read the next
user message nearly instantly.
:::
