---
title: "Ticket routing - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/about-claude/use-case-guides/ticket-routing"
category: "04-API-Reference/About"
fetched_at: "2026-08-02T05:37:22Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
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


Use cases

[Overview](/docs/en/about-claude/use-case-guides/overview)[Ticket routing](/docs/en/about-claude/use-case-guides/ticket-routing)[Customer support agent](/docs/en/about-claude/use-case-guides/customer-support-chat)[Content moderation](/docs/en/about-claude/use-case-guides/content-moderation)[Legal summarization](/docs/en/about-claude/use-case-guides/legal-summarization)

Prompt engineering

[Overview](/docs/en/build-with-claude/prompt-engineering/overview)[Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)[Prompting Claude Fable 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)[Prompting Claude Opus 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)[Prompting Claude Opus 4.8](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)[Prompting Claude Sonnet 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)

Test and evaluate

[Define success and build evaluations](/docs/en/test-and-evaluate/develop-tests)[Reducing latency](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)

Strengthen guardrails

[Reduce hallucinations](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)[Increase output consistency](/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)[Mitigate jailbreaks](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)[Reduce prompt leak](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)

Reference

[Glossary](/docs/en/about-claude/glossary)

[](/login)




Best practices

Ticket routing

Best practices/Use cases

# Ticket routing




This guide walks through how to harness Claude's advanced natural language understanding capabilities to classify customer support tickets at scale based on customer intent, urgency, prioritization, customer profile, and more.







Prerequisites

- A Claude API key and the Python SDK installed
- Access to, and familiarity with, your existing support ticketing system
- A sample set of historical support tickets for testing




Define whether to use Claude for ticket routing

Here are some key indicators that you should use an LLM like Claude instead of traditional ML approaches for your classification task:

### You have limited labeled training data available

### Your classification categories are likely to change or evolve over time

### You need to handle complex, unstructured text inputs

### Your classification rules are based on semantic understanding

### You require interpretable reasoning for classification decisions

### You want to handle edge cases and ambiguous tickets more effectively

### You need multilingual support without maintaining separate models

------------------------------------------------------------------------




Build and deploy your LLM support workflow




Understand your current support approach

Before you automate, it's crucial to understand your existing ticketing system. Start by investigating how your support team currently handles ticket routing.

Consider questions like:

- What criteria are used to determine what SLA/service offering is applied?
- Is ticket routing used to determine which tier of support or product specialist a ticket goes to?
- Are there any automated rules or workflows already in place? In what cases do they fail?
- How are edge cases or ambiguous tickets handled?
- How does the team prioritize tickets?

The more you know about how humans handle certain cases, the better you can work with Claude to do the task.




Define user intent categories

A well-defined list of user intent categories is crucial for accurate support ticket classification with Claude. Claude’s ability to route tickets effectively within your system is directly proportional to how well-defined your system’s categories are.

Here are some example user intent categories and subcategories.

### Technical issue

### Account management

### Product information

### User guidance

### Feedback

### Order-related

### Service request

### Security concerns

### Compliance and legal

### Emergency support

### Training and education

### Integration and API

In addition to intent, ticket routing and prioritization may also be influenced by other factors such as urgency, customer type, SLAs, or language. Be sure to consider other routing criteria when building your automated routing system.




Establish success criteria

Work with your support team to [define clear success criteria](/docs/en/test-and-evaluate/develop-tests) with measurable benchmarks, thresholds, and goals.

Here are some standard criteria and benchmarks when using LLMs for support ticket routing:

### Classification consistency

### Adaptation speed

### Multilingual handling

### Edge case handling

### Bias mitigation

### Prompt efficiency

### Explainability score

Here are some common success criteria that may be useful regardless of whether an LLM is used:

### Routing accuracy

### Time-to-assignment

### Rerouting rate

### First-contact resolution rate

### Average handling time

### Customer satisfaction scores

### Escalation rate

### Agent productivity

### Self-service deflection rate

### Cost per ticket




Choose the right Claude model

The choice of model depends on the trade-offs between cost, accuracy, and response time.

Many customers have found `claude-haiku-4-5-20251001` an ideal model for ticket routing, as it is the fastest and most cost-effective model in the Claude 4 family while still delivering excellent results. If your classification problem requires deep subject matter expertise or a large volume of intent categories, or complex reasoning, you may opt for the [larger Sonnet model](/docs/en/about-claude/models).




Build a strong prompt

Ticket routing is a type of classification task. Claude analyzes the content of a support ticket and classifies it into predefined categories based on the issue type, urgency, required expertise, or other relevant factors.

Write a ticket classification prompt. The initial prompt should contain the contents of the user request and return both the reasoning and the intent.



Try the [metaprompt recipe from the Claude Cookbook](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/metaprompt.ipynb) to have Claude write a first draft for you.

Here's an example ticket routing classification prompt:

```python
def classify_support_request(ticket_contents):
    # Define the prompt for the classification task
    classification_prompt = f"""You will be acting as a customer support ticket classification system. Your task is to analyze customer support requests and output the appropriate classification intent for each request, along with your reasoning.

        Here is the customer support request you need to classify:

        <request>{ticket_contents}</request>

        Please carefully analyze the above request to determine the customer's core intent and needs. Consider what the customer is asking for has concerns about.

        First, write out your reasoning and analysis of how to classify this request inside <reasoning> tags.

        Then, output the appropriate classification label for the request inside a <intent> tag. The valid intents are:
        <intents>
        <intent>Support, Feedback, Complaint</intent>
        <intent>Order Tracking</intent>
        <intent>Refund/Exchange</intent>
        </intents>

        A request may have ONLY ONE applicable intent. Only include the intent that is most applicable to the request.

        As an example, consider the following request:
        <request>Hello! I had high-speed fiber internet installed on Saturday and my installer, Kevin, was absolutely fantastic! Where can I send my positive review? Thanks for your help!</request>

        Here is an example of how your output should be formatted (for the above example request):
        <reasoning>The user seeks information in order to leave positive feedback.</reasoning>
        <intent>Support, Feedback, Complaint</intent>

        Here are a few more examples:
        <examples>
        <example 2>
        Example 2 Input:
        <request>I wanted to write and personally thank you for the compassion you showed towards my family during my father's funeral this past weekend. Your staff was so considerate and helpful throughout this whole process; it really took a load off our shoulders. The visitation brochures were beautiful. We'll never forget the kindness you showed us and we are so appreciative of how smoothly the proceedings went. Thank you, again, Amarantha Hill on behalf of the Hill Family.</request>

        Example 2 Output:
        <reasoning>User leaves a positive review of their experience.</reasoning>
        <intent>Support, Feedback, Complaint</intent>
        </example 2>
        <example 3>

        ...

        </example 8>
        <example 9>
        Example 9 Input:
        <request>Your website keeps sending ad-popups that block the entire screen. It took me twenty minutes just to finally find the phone number to call and complain. How can I possibly access my account information with all of these popups? Can you access my account for me, since your website is broken? I need to know what the address is on file.</request>

        Example 9 Output:
        <reasoning>The user requests help accessing their web account information.</reasoning>
        <intent>Support, Feedback, Complaint</intent>
        </example 9>

        Remember to always include your classification reasoning before your actual intent output. The reasoning should be enclosed in <reasoning> tags and the intent in <intent> tags. Return only the reasoning and the intent.
        """
```



Here are the key components of this prompt:

- The prompt template is a Python f-string, allowing the `ticket_contents` to be inserted into the `<request>` tags.
- The prompt gives Claude a clearly defined role as a classification system that carefully analyzes the ticket content to determine the customer's core intent and needs.
- The prompt instructs Claude on proper output formatting, in this case to provide its reasoning and analysis inside `<reasoning>` tags, followed by the appropriate classification label inside `<intent>` tags.
- The prompt specifies the valid intent categories: "Support, Feedback, Complaint", "Order Tracking", and "Refund/Exchange".
- The prompt includes a few examples (a.k.a. few-shot prompting) to illustrate how the output should be formatted, which improves accuracy and consistency.

Having Claude split its response into separate XML tag sections lets you use regular expressions to extract the reasoning and intent from the output independently. This lets you create targeted next steps in the ticket routing workflow, such as using only the intent to decide which person to route the ticket to.




Deploy your prompt

It’s hard to know how well your prompt works without deploying it in a test production setting and [running evaluations](/docs/en/test-and-evaluate/develop-tests).

Build the deployment structure. Start by defining the method signature for wrapping the call to Claude. Extend the method you began writing earlier, which takes `ticket_contents` as input, so that it now returns a tuple of `reasoning` and `intent` as output. If you have an existing automation using traditional ML, you'll want to follow that method signature instead.

Python



```python
import re

# Create an instance of the Claude API client
client = anthropic.Anthropic()

# Set the default model
DEFAULT_MODEL = "claude-haiku-4-5-20251001"


def classify_support_request(ticket_contents):
    # Define the prompt for the classification task
    classification_prompt = f"""You will be acting as a customer support ticket classification system.
        ...
        ... The reasoning should be enclosed in <reasoning> tags and the intent in <intent> tags. Return only the reasoning and the intent.
        """
    # Send the prompt to the API to classify the support request.
    message = client.messages.create(
        model=DEFAULT_MODEL,
        max_tokens=500,
        temperature=0,
        messages=[{"role": "user", "content": classification_prompt}],
        stream=False,
    )
    reasoning_and_intent = message.content[0].text

    # Use Python's regular expressions library to extract `reasoning`.
    reasoning_match = re.search(
        r"<reasoning>(.*?)</reasoning>", reasoning_and_intent, re.DOTALL
    )
    reasoning = reasoning_match.group(1).strip() if reasoning_match else ""

    # Similarly, also extract the `intent`.
    intent_match = re.search(r"<intent>(.*?)</intent>", reasoning_and_intent, re.DOTALL)
    intent = intent_match.group(1).strip() if intent_match else ""

    return reasoning, intent
```

This code:

- Creates a client instance using your API key.
- Defines a `classify_support_request` function that takes a `ticket_contents` string.
- Sends the `ticket_contents` to Claude for classification using the `classification_prompt`.
- Returns the model's `reasoning` and `intent` extracted from the response.

Because the entire reasoning and intent text must be generated before parsing, the example sets `stream=False` (the default).

------------------------------------------------------------------------




Evaluate your prompt

Prompting often requires testing and optimization for it to be production ready. To determine the readiness of your solution, evaluate performance based on the success criteria and thresholds you established earlier.

To run your evaluation, you need test cases to run it on. The rest of this guide assumes you have already [developed your test cases](/docs/en/test-and-evaluate/develop-tests).




Build an evaluation function

The example evaluation for this guide measures Claude’s performance along three key metrics:

- Accuracy
- Cost per classification

You may need to assess Claude on other axes depending on what factors that are important to you.

To assess this, first modify the script to add a function that compares the predicted intent with the actual intent and calculates the percentage of correct predictions. Then add cost calculation and time measurement functionality.

Python



```python
import re

# Create an instance of the Claude API client
client = anthropic.Anthropic()

# Set the default model
DEFAULT_MODEL = "claude-haiku-4-5-20251001"


def classify_support_request(request, actual_intent):
    # Define the prompt for the classification task
    classification_prompt = f"""You will be acting as a customer support ticket classification system.
        ...
        ...The reasoning should be enclosed in <reasoning> tags and the intent in <intent> tags. Return only the reasoning and the intent.
        """

    message = client.messages.create(
        model=DEFAULT_MODEL,
        max_tokens=500,
        temperature=0,
        messages=[{"role": "user", "content": classification_prompt}],
    )
    usage = message.usage  # Get the usage statistics for the API call for how many input and output tokens were used.
    reasoning_and_intent = message.content[0].text

    # Use Python's regular expressions library to extract `reasoning`.
    reasoning_match = re.search(
        r"<reasoning>(.*?)</reasoning>", reasoning_and_intent, re.DOTALL
    )
    reasoning = reasoning_match.group(1).strip() if reasoning_match else ""

    # Similarly, also extract the `intent`.
    intent_match = re.search(r"<intent>(.*?)</intent>", reasoning_and_intent, re.DOTALL)
    intent = intent_match.group(1).strip() if intent_match else ""

    # Check if the model's prediction is correct.
    correct = actual_intent.strip() == intent.strip()

    # Return the reasoning, intent, correct, and usage.
    return reasoning, intent, correct, usage
```

Here is a breakdown of the edits:

- The `classify_support_request` method now takes the `actual_intent` from the test cases and compares it against Claude’s intent classification to assess whether they match.
- The method extracts usage statistics for the API call to calculate cost based on input and output tokens used.




Run your evaluation

A proper evaluation requires clear thresholds and benchmarks to determine what is a good result. The preceding script returns the runtime values for accuracy, response time, and cost per classification, but you still need clearly established thresholds. For example:

- **Accuracy:** 95% (out of 100 tests)
- **Cost per classification:** 50% reduction on average (across 100 tests) from current routing method

Having these thresholds allows you to quickly and easily tell at scale, and with impartial empiricism, what method is best for you and what changes might need to be made to better fit your requirements.

------------------------------------------------------------------------




Improve performance

In complex scenarios, it may be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](/docs/en/build-with-claude/prompt-engineering/overview) & [guardrail implementation strategies](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations). Here are some common scenarios:




Use a taxonomic hierarchy for cases with 20+ intent categories

As the number of classes grows, the number of examples required also expands, potentially making the prompt unwieldy. As an alternative, you can consider implementing a hierarchical classification system using a mixture of classifiers.

1.  Organize your intents in a taxonomic tree structure.
2.  Create a series of classifiers at every level of the tree, enabling a cascading routing approach.

For example, you might have a top-level classifier that broadly categorizes tickets into "Technical Issues," "Billing Questions," and "General Inquiries." Each of these categories can then have its own sub-classifier to further refine the classification.

- **Pros - greater nuance and accuracy:** You can create different prompts for each parent path, allowing for more targeted and context-specific classification. This can lead to improved accuracy and more nuanced handling of customer requests.

- **Cons - increased latency:** Be advised that multiple classifiers can lead to increased latency, and Anthropic recommends implementing this approach with the fastest model, Haiku.




Use vector databases and similarity search retrieval to handle highly variable tickets

Despite providing examples being the most effective way to improve performance, if support requests are highly variable, it can be hard to include enough examples in a single prompt.

In this scenario, you could employ a vector database to do similarity searches from a dataset of examples and retrieve the most relevant examples for a given query.

This approach, outlined in detail in the [classification recipe](https://platform.claude.com/cookbook/capabilities-classification-guide), has been shown to improve performance from 71% accuracy to 93% accuracy.




Account specifically for expected edge cases

Here are some scenarios where Claude may misclassify tickets (there may be others that are unique to your situation). In these scenarios, consider providing explicit instructions or examples in the prompt of how Claude should handle the edge case:

### Customers make implicit requests

### Claude prioritizes emotion over intent

### Multiple issues cause issue prioritization confusion

------------------------------------------------------------------------




Integrate Claude into your greater support workflow

Proper integration requires that you make some decisions regarding how your Claude-based ticket routing script fits into the architecture of your greater ticket routing system. There are two ways you could do this:

- **Push-based:** The support ticket system you’re using (for example, Zendesk) triggers your code by sending a webhook event to your routing service, which then classifies the intent and routes it.
  - This approach is more web-scalable, but needs you to expose a public endpoint.
- **Pull-based:** Your code pulls for the latest tickets based on a given schedule and routes them at pull time.
  - This approach is easier to implement but might make unnecessary calls to the support ticket system when the pull frequency is too high or might be overly slow when the pull frequency is too low.

For either of these approaches, you need to wrap your script in a service. The choice of approach depends on what APIs your support ticketing system provides.

------------------------------------------------------------------------




Classification cookbook



Visit the classification cookbook for more example code and detailed eval guidance.




Claude Console

Begin building and evaluating your workflow on the Claude Console.
