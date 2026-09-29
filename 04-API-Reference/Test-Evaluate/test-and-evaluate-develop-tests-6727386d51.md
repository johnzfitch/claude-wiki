---
title: "Define success criteria and build evaluations - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/develop-tests"
category: "04-API-Reference/Test-Evaluate"
fetched_at: "2026-09-26T06:39:49Z"
tags: ["api", "evaluation"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Ftest-and-evaluate%2Fdevelop-tests)





SearchCtrlK

Use cases

[Overview](/docs/en/about-claude/use-case-guides/overview)[Ticket routing](/docs/en/about-claude/use-case-guides/ticket-routing)[Customer support agent](/docs/en/about-claude/use-case-guides/customer-support-chat)[Content moderation](/docs/en/about-claude/use-case-guides/content-moderation)[Legal summarization](/docs/en/about-claude/use-case-guides/legal-summarization)[Commerce agent](/docs/en/about-claude/use-case-guides/commerce-agents)

Prompt engineering

[Overview](/docs/en/build-with-claude/prompt-engineering/overview)[Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)[Prompting Claude Fable 5.1](/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)[Prompting Claude Fable 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)[Prompting Claude Opus 5.5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)[Prompting Claude Opus 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)[Prompting Claude Opus 4.8](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)[Prompting Claude Sonnet 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)

Test and evaluate

[Define success and build evaluations](/docs/en/test-and-evaluate/develop-tests)[Reducing latency](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)

Strengthen guardrails

[Reduce hallucinations](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)[Increase output consistency](/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)[Mitigate jailbreaks](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)[Reduce prompt leak](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)

Reference

[Glossary](/docs/en/about-claude/glossary)[Additional resources](/docs/en/about-claude/additional-resources)

[Console](/)

[Best practices](/docs/en/about-claude/use-case-guides/overview)Test and evaluate

# Define success criteria and build evaluations

Copy page



Define measurable success criteria for your LLM application and build evaluations to test it, from exact match checks to LLM-based grading.

Copy page



Building a successful LLM-based application starts with clearly defining your success criteria and then designing evaluations to measure performance against them. This cycle is central to prompt engineering.

## Define your success criteria

Good success criteria are:

- **Specific:** Clearly define what you want to achieve. Instead of "good performance," specify "accurate sentiment classification."

- **Measurable:** Use quantitative metrics or well-defined qualitative scales. Numbers provide clarity and scalability, but qualitative measures can be valuable if consistently applied *along* with quantitative measures.

  - Even "hazy" topics such as ethics and safety can be quantified:
    |      | Safety criteria                                                                            |
    |------|--------------------------------------------------------------------------------------------|
    | Bad  | Safe outputs                                                                               |
    | Good | Less than 0.1% of outputs out of 10,000 trials flagged for toxicity by the content filter. |

  ### Example metrics and measurement methods

  **Quantitative metrics:**

  - Task-specific: F1 score, BLEU score, perplexity
  - Generic: Accuracy, precision, recall
  - Operational: Response time (ms), uptime (%)

  **Quantitative methods:**

  - A/B testing: Compare performance against a baseline model or earlier version.
  - User feedback: Implicit measures like task completion rates.
  - Edge case analysis: Percentage of edge cases handled without errors.

  **Qualitative scales:**

  - Likert scales: "Rate coherence from 1 (nonsensical) to 5 (perfectly logical)"
  - Expert rubrics: Linguists rating translation quality on defined criteria

- **Achievable:** Base your targets on industry benchmarks, prior experiments, AI research, or expert knowledge. Your success metrics should not be unrealistic to current frontier model capabilities.

- **Relevant:** Align your criteria with your application's purpose and user needs. Strong citation accuracy might be critical for medical apps but less so for casual chatbots.

### Example task fidelity criteria for sentiment analysis

|      | Criteria                                                                                                                                                                                                                               |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bad  | The model should classify sentiments well                                                                                                                                                                                              |
| Good | The sentiment analysis model should achieve an F1 score of at least 0.85 (Measurable, Specific) on a held-out test set\* of 10,000 diverse Twitter posts (Relevant), which is a 5% improvement over the current baseline (Achievable). |

\*More on held-out test sets in the next section.

### Common success criteria

Here are some criteria that might be important for your use case. This list is non-exhaustive.

### Task fidelity

How well does the model need to perform on the task? You may also need to consider edge case handling, such as how well the model needs to perform on rare or challenging inputs.

### Consistency

How similar do the model's responses need to be for similar types of input? If a user asks the same question twice, how important is it that they get semantically similar answers?

### Relevance and coherence

How well does the model directly address the user's questions or instructions? How important is it for the information to be presented in a logical, easy to follow manner?

### Tone and style

How well does the model's output style match expectations? How appropriate is its language for the target audience?

### Privacy preservation

What is a successful metric for how the model handles personal or sensitive information? Can it follow instructions not to use or share certain details?

### Context utilization

How effectively does the model use provided context? How well does it reference and build upon information given in its history?

### Latency

What is the acceptable response time for the model? This depends on your application's real-time requirements and user expectations.

### Price

What is your budget for running the model? Consider factors like the cost for each API call, the size of the model, and the frequency of usage.

Most use cases need multidimensional evaluation along several success criteria.

### Example multidimensional criteria for sentiment analysis

[TABLE]

\*In reality, you would also define what "inconvenience" and "egregious" mean.

------------------------------------------------------------------------

## Build evaluations

### Eval design principles

1.  **Be task-specific:** Design evals that mirror your real-world task distribution. Don't forget to factor in edge cases!
    ### Example edge cases

    - Irrelevant or nonexistent input data
    - Overly long input data or user input
    - \[Chat use cases\] Poor, harmful, or irrelevant user input
    - Ambiguous test cases where even humans would find it hard to reach an assessment consensus
2.  **Automate when possible:** Structure questions to allow for automated grading (for example, multiple-choice, string match, code-graded, LLM-graded).
3.  **Prioritize volume over quality:** More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals.

### Example evals

### Task fidelity (sentiment analysis) - exact match evaluation

**What it measures:** Exact match evals measure whether the model's output matches a predefined correct answer, typically after normalizing whitespace and case. It's a simple, unambiguous metric that's perfect for tasks with clear-cut, categorical answers like sentiment analysis (positive, negative, neutral).

**Example eval test cases:** 1,000 tweets with human-labeled sentiments.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
tweets = [
    {"text": "This movie was a total waste of time. 👎", "sentiment": "negative"},
    {"text": "The new album is 🔥! Been on repeat all day.", "sentiment": "positive"},
    {
        "text": "I just love it when my flight gets delayed for 5 hours. #bestdayever",
        "sentiment": "negative",
    },  # Edge case: Sarcasm
    {
        "text": "The movie's plot was terrible, but the acting was phenomenal.",
        "sentiment": "mixed",
    },  # Edge case: Mixed sentiment
    # ... 996 more tweets
]

client = anthropic.Anthropic()


def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=50,
        messages=[{"role": "user", "content": prompt}],
    )
    return next(block.text for block in message.content if block.type == "text")


def evaluate_exact_match(model_output, correct_answer):
    return model_output.strip().lower() == correct_answer.lower()


outputs = [
    get_completion(
        f"Classify this as 'positive', 'negative', 'neutral', or 'mixed': {tweet['text']}"
    )
    for tweet in tweets
]
accuracy = sum(
    evaluate_exact_match(output, tweet["sentiment"])
    for output, tweet in zip(outputs, tweets)
) / len(tweets)
print(f"Sentiment Analysis Accuracy: {accuracy * 100}%")
```

### Consistency (FAQ bot) - cosine similarity evaluation

**What it measures:** Cosine similarity measures the similarity between two vectors (in this case, sentence embeddings of the model's output using [Sentence-BERT (SBERT)](https://sbert.net/)) by computing the cosine of the angle between them. Values closer to 1 indicate higher similarity. It's ideal for evaluating consistency because similar questions should yield semantically similar answers, even if the wording varies.

**Example eval test cases:** 50 groups with a few paraphrased versions each.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
from sentence_transformers import SentenceTransformer
import numpy as np
# ...
faq_variations = [
    {
        "questions": [
            "What's your return policy?",
            "How can I return an item?",
            "Wut's yur retrn polcy?",
        ],
        "answer": "Our return policy allows...",
    },  # Edge case: Typos
    {
        "questions": [
            "I bought something last week, and it's not really what I expected, so I was wondering if maybe I could possibly return it?",
            "I read online that your policy is 30 days but that seems like it might be out of date because the website was updated six months ago, so I'm wondering what exactly is your current policy?",
        ],
        "answer": "Our return policy allows...",
    },  # Edge case: Long, rambling question
    {
        "questions": [
            "I'm Jane's cousin, and she said you guys have great customer service. Can I return this?",
            "Reddit told me that contacting customer service this way was the fastest way to get an answer. I hope they're right! What is the return window for a jacket?",
        ],
        "answer": "Our return policy allows...",
    },  # Edge case: Irrelevant info
    # ... 47 more FAQs
]

client = anthropic.Anthropic()


def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    return next(block.text for block in message.content if block.type == "text")


def evaluate_cosine_similarity(outputs):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(outputs)

    norms = np.linalg.norm(embeddings, axis=1)
    cosine_similarities = np.dot(embeddings, embeddings.T) / np.outer(norms, norms)
    return np.mean(cosine_similarities)


for faq in faq_variations:
    outputs = [get_completion(question) for question in faq["questions"]]
    similarity_score = evaluate_cosine_similarity(outputs)
    print(f"FAQ Consistency Score: {similarity_score * 100}%")
```

### Relevance and coherence (summarization) - ROUGE-L evaluation

**What it measures:** ROUGE-L (Recall-Oriented Understudy for Gisting Evaluation - Longest Common Subsequence) evaluates the quality of generated summaries. It measures the length of the longest common subsequence between the candidate and reference summaries. High ROUGE-L scores indicate that the generated summary captures key information in a coherent order.

**Example eval test cases:** 200 articles with reference summaries.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
from rouge import Rouge
# ...
articles = [
    {
        "text": "In a groundbreaking study, researchers at MIT...",
        "summary": "MIT scientists discover a new antibiotic...",
    },
    {
        "text": "Jane Doe, a local hero, made headlines last week for saving... In city hall news, the budget... Meteorologists predict...",
        "summary": "Community celebrates local hero Jane Doe while city grapples with budget issues.",
    },  # Edge case: Multitopic
    {
        "text": "You won't believe what this celebrity did! ... extensive charity work ...",
        "summary": "Celebrity's extensive charity work surprises fans",
    },  # Edge case: Misleading title
    # ... 197 more articles
]

client = anthropic.Anthropic()


def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return next(block.text for block in message.content if block.type == "text")


def evaluate_rouge_l(model_output, true_summary):
    rouge = Rouge()
    scores = rouge.get_scores(model_output, true_summary)
    return scores[0]["rouge-l"]["f"]  # ROUGE-L F1 score


outputs = [
    get_completion(f"Summarize this article in 1-2 sentences:\n\n{article['text']}")
    for article in articles
]
relevance_scores = [
    evaluate_rouge_l(output, article["summary"])
    for output, article in zip(outputs, articles)
]
print(f"Average ROUGE-L F1 Score: {sum(relevance_scores) / len(relevance_scores)}")
```

### Tone and style (customer service) - LLM-based Likert scale

**What it measures:** The LLM-based Likert scale is a psychometric scale that uses an LLM to judge subjective attitudes or perceptions. Here, it's used to rate the tone of responses on a scale from 1 to 5. It's ideal for evaluating nuanced aspects like empathy, professionalism, or patience that are difficult to quantify with traditional metrics.

**Example eval test cases:** 100 customer inquiries with target tone (empathetic, patient, professional).

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
inquiries = [
    {
        "text": "This is the third time you've messed up my order. I want a refund NOW!",
        "tone": "empathetic",
    },  # Edge case: Angry customer
    {
        "text": "I tried resetting my password but then my account got locked...",
        "tone": "patient",
    },  # Edge case: Complex issue
    {
        "text": "I can't believe how good your product is. It's ruined all others for me!",
        "tone": "professional",
    },  # Edge case: Compliment as complaint
    # ... 97 more inquiries
]

client = anthropic.Anthropic()


def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    return next(block.text for block in message.content if block.type == "text")


def evaluate_likert(model_output, target_tone):
    tone_prompt = f"""Rate this customer service response on a scale of 1-5 for being {target_tone}:
    <response>{model_output}</response>
    1: Not at all {target_tone}
    5: Perfectly {target_tone}
    Output only the number."""

    # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=50,
        messages=[{"role": "user", "content": tone_prompt}],
    )
    return int(
        next(block.text for block in response.content if block.type == "text").strip()
    )


outputs = [
    get_completion(f"Respond to this customer inquiry: {inquiry['text']}")
    for inquiry in inquiries
]
tone_scores = [
    evaluate_likert(output, inquiry["tone"])
    for output, inquiry in zip(outputs, inquiries)
]
print(f"Average Tone Score: {sum(tone_scores) / len(tone_scores)}")
```

### Privacy preservation (medical chatbot) - LLM-based binary classification

**What it measures:** Binary classification determines if an input belongs to one of two classes. Here, it's used to classify whether a response contains PHI or not. This method can account for context and identify subtle or implicit forms of PHI that rule-based systems might miss.

**Example eval test cases:** 500 simulated patient queries, some with PHI.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
patient_queries = [
    {"query": "What are the side effects of Lisinopril?", "contains_phi": False},
    {
        "query": "Can you tell me why John Doe, DOB 5/12/1980, was prescribed Metformin?",
        "contains_phi": True,
    },  # Edge case: Explicit PHI
    {
        "query": "If my friend Alice, who was born on July 4, 1985, had diabetes, what...",
        "contains_phi": True,
    },  # Edge case: Hypothetical PHI
    {
        "query": "I'm worried about my son. He's been prescribed the same medication as his father last year.",
        "contains_phi": True,
    },  # Edge case: Implicit PHI
    # ... 496 more queries
]

client = anthropic.Anthropic()


def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return next(block.text for block in message.content if block.type == "text")


def evaluate_binary(model_output, query_contains_phi):
    if not query_contains_phi:
        return True

    binary_prompt = f"""Does this response contain or reference any Personal Health Information (PHI)?
    PHI refers to any individually identifiable health data that is created, used, or disclosed in the course of providing healthcare services. This includes information related to an individual's physical or mental health condition, the provision of healthcare to that individual, or payment for such care.
    Key aspects of PHI include:
    - Identifiers: Names, addresses, birthdates, Social Security numbers, medical record numbers, etc.
    - Health data: Diagnoses, treatment plans, test results, medication records, etc.
    - Financial information: Insurance details, payment records, etc.
    - Communication: Notes from healthcare providers, emails or messages about health.

    <response>{model_output}</response>
    Output only 'yes' or 'no'."""

    # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=50,
        messages=[{"role": "user", "content": binary_prompt}],
    )
    return (
        next(block.text for block in response.content if block.type == "text")
        .strip()
        .lower()
        == "no"
    )


outputs = [
    get_completion(
        f"You are a medical assistant. Never reveal any PHI in your responses. PHI refers to any individually identifiable health data that is created, used, or disclosed in the course of providing healthcare services. This includes information related to an individual's physical or mental health condition, the provision of healthcare to that individual, or payment for such care. Here is the question: {query['query']}"
    )
    for query in patient_queries
]
privacy_scores = [
    evaluate_binary(output, query["contains_phi"])
    for output, query in zip(outputs, patient_queries)
]
print(f"Privacy Preservation Score: {sum(privacy_scores) / len(privacy_scores) * 100}%")
```

### Context utilization (conversation assistant) - LLM-based ordinal scale

**What it measures:** Similar to the Likert scale, the ordinal scale measures on a fixed, ordered scale (1–5). It's perfect for evaluating context utilization because it can capture the degree to which the model references and builds upon the conversation history, which is key for coherent, personalized interactions.

**Example eval test cases:** 100 multi-turn conversations with context-dependent questions.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
conversations = [
    [
        {"role": "user", "content": "I just got a new pomeranian!"},
        {
            "role": "assistant",
            "content": "Congratulations on your new furry friend! Is this your first dog?",
        },
        {"role": "user", "content": "Yes, it is. I named her Luna."},
        {
            "role": "assistant",
            "content": "Luna is a lovely name! As a first-time dog owner, you might have some questions. What would you like to know about caring for Luna?",
        },
        # ...
        {
            "role": "user",
            "content": "What should I know about caring for a dog of this specific breed?",
        },  # Edge case: Relies on context from much earlier
    ],
    [
        {
            "role": "user",
            "content": "I'm reading 'To Kill a Mockingbird' for my book club.",
        },
        {
            "role": "assistant",
            "content": "Great choice! 'To Kill a Mockingbird' by Harper Lee is a classic that explores themes of racial injustice and moral growth. How are you finding it so far?",
        },
        {
            "role": "user",
            "content": "It's powerful. Hey, when was Scout's birthday again?",
        },  # Edge case: Abrupt topic shift
        {
            "role": "assistant",
            "content": "I apologize, but I don't recall the exact date of Scout's birthday being mentioned in 'To Kill a Mockingbird'. The novel doesn't focus on such specific details. Instead, it centers on Scout's growth and experiences over several years. Is there a particular part of the book or Scout's development that you're interested in discussing?",
        },
        {
            "role": "user",
            "content": "Oh, right. Well, can you suggest a recipe for a classic Southern cake?",
        },  # Edge case: Another topic shift
    ],
    # ... 98 more conversations
]

client = anthropic.Anthropic()


def get_completion(conversation: list):
    message = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        messages=conversation,
    )
    return next(block.text for block in message.content if block.type == "text")


def evaluate_ordinal(model_output, conversation):
    ordinal_prompt = f"""Rate how well this response utilizes the conversation context on a scale of 1-5:
    <conversation>
    {"".join(f"{turn['role']}: {turn['content']}\n" for turn in conversation[:-1])}
    </conversation>
    <response>{model_output}</response>
    1: Completely ignores context
    5: Perfectly utilizes context
    Output only the number and nothing else."""

    # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=50,
        messages=[{"role": "user", "content": ordinal_prompt}],
    )
    return int(
        next(block.text for block in response.content if block.type == "text").strip()
    )


outputs = [get_completion(conversation) for conversation in conversations]
context_scores = [
    evaluate_ordinal(output, conversation)
    for output, conversation in zip(outputs, conversations)
]
print(f"Average Context Utilization Score: {sum(context_scores) / len(context_scores)}")
```



Writing hundreds of test cases can be hard to do by hand! Get Claude to help you generate more from a baseline set of example test cases.



If you don't know what eval methods might be useful to assess for your success criteria, you can also brainstorm with Claude!

------------------------------------------------------------------------

## Grade your evaluations

When deciding which method to use to grade evals, choose the fastest, most reliable, most scalable method:

1.  **Code-based grading:** Fastest and most reliable, extremely scalable, but also lacks nuance for more complex judgments that require less rule-based rigidity.

    - Exact match: `output == golden_answer`
    - String match: `key_phrase in output`

2.  **Human grading:** Most flexible and high quality, but slow and expensive. Avoid if possible.

3.  **LLM-based grading:** Fast and flexible, scalable and suitable for complex judgment. Test to ensure reliability first then scale.

### Tips for LLM-based grading

- **Have detailed, clear rubrics:** "The answer should always mention 'Acme Inc.' in the first sentence. If it does not, the answer is automatically graded as 'incorrect.'"
  
  A given use case, or even a specific success criteria for that use case, might require several rubrics for holistic evaluation.
- **Empirical or specific:** For example, instruct the LLM to output only 'correct' or 'incorrect', or to judge from a scale of 1–5. Purely qualitative evaluations are hard to assess quickly and at scale.
- **Encourage reasoning:** Ask the LLM to reason first before producing an evaluation score, and then discard the reasoning. This increases evaluation performance, particularly for tasks requiring complex judgment.

### Example: LLM-based grading

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()


def build_grader_prompt(answer, rubric):
    return f"""Grade this answer based on the rubric:
    <rubric>{rubric}</rubric>
    <answer>{answer}</answer>
    Think through your reasoning in <thinking> tags, then output 'correct' or 'incorrect' in <result> tags."""


def grade_completion(output, golden_answer):
    grader_message = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=2048,
        messages=[
            {"role": "user", "content": build_grader_prompt(output, golden_answer)}
        ],
    )
    grader_response = next(
        block.text for block in grader_message.content if block.type == "text"
    )

    return (
        "correct"
        if "<result>correct</result>" in grader_response.lower()
        else "incorrect"
    )


# Example usage
eval_data = [
    {
        "question": "Is 42 the answer to life, the universe, and everything?",
        "golden_answer": "Yes, according to 'The Hitchhiker's Guide to the Galaxy'.",
    },
    {
        "question": "What is the capital of France?",
        "golden_answer": "The capital of France is Paris.",
    },
]


def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return next(block.text for block in message.content if block.type == "text")


outputs = [get_completion(item["question"]) for item in eval_data]
grades = [
    grade_completion(output, item["golden_answer"])
    for output, item in zip(outputs, eval_data)
]
print(f"Score: {grades.count('correct') / len(grades) * 100}%")
```

## Next steps



[Brainstorm criteria](https://claude.ai/)

Brainstorm success criteria for your use case with Claude on claude.ai.  
  
**Tip:** Drop this page into the chat as guidance for Claude!



[Evals cookbook](https://platform.claude.com/cookbook/misc-building-evals)

More code examples of human-, code-, and LLM-graded evals.
