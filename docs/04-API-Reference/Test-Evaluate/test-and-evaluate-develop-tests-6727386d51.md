---
category: "04-API-Reference"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/develop-tests"
---


Test & evaluate
Create strong empirical evaluations
Copy page

After defining your success criteria, the next step is designing evaluations to measure LLM performance against those criteria. This is a vital part of the prompt engineering cycle.

This guide focuses on how to develop your test cases.

Building evals and test cases
Eval design principles
Be task-specific: Design evals that mirror your real-world task distribution. Don't forget to factor in edge cases!
Example edge cases
Automate when possible: Structure questions to allow for automated grading (e.g., multiple-choice, string match, code-graded, LLM-graded).
Prioritize volume over quality: More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals.
Example evals
Task fidelity (sentiment analysis) - exact match evaluation
Consistency (FAQ bot) - cosine similarity evaluation
Relevance and coherence (summarization) - ROUGE-L evaluation
Tone and style (customer service) - LLM-based Likert scale
Privacy preservation (medical chatbot) - LLM-based binary classification
Context utilization (conversation assistant) - LLM-based ordinal scale
Writing hundreds of test cases can be hard to do by hand! Get Claude to help you generate more from a baseline set of example test cases.
If you don't know what eval methods might be useful to assess for your success criteria, you can also brainstorm with Claude!
Grading evals

When deciding which method to use to grade evals, choose the fastest, most reliable, most scalable method:

Code-based grading: Fastest and most reliable, extremely scalable, but also lacks nuance for more complex judgements that require less rule-based rigidity.

Exact match: output == golden_answer
String match: key_phrase in output

Human grading: Most flexible and high quality, but slow and expensive. Avoid if possible.

LLM-based grading: Fast and flexible, scalable and suitable for complex judgement. Test to ensure reliability first then scale.

Tips for LLM-based grading
Have detailed, clear rubrics: "The answer should always mention 'Acme Inc.' in the first sentence. If it does not, the answer is automatically graded as 'incorrect.'"
A given use case, or even a specific success criteria for that use case, might require several rubrics for holistic evaluation.
Empirical or specific: For example, instruct the LLM to output only 'correct' or 'incorrect', or to judge from a scale of 1-5. Purely qualitative evaluations are hard to assess quickly and at scale.
Encourage reasoning: Ask the LLM to think first before deciding an evaluation score, and then discard the reasoning. This increases evaluation performance, particularly for tasks requiring complex judgement.
Example: LLM-based grading
Next steps
Brainstorm evaluations

Learn how to craft prompts that maximize your eval scores.

Evals cookbook

More code examples of human-, code-, and LLM-graded evals.

Was this page helpful?