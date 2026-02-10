---
category: "04-API-Reference"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/define-success"
---


Test & evaluate
Define your success criteria
Copy page

Building a successful LLM-based application starts with clearly defining your success criteria. How will you know when your application is good enough to publish?

Having clear success criteria ensures that your prompt engineering & optimization efforts are focused on achieving specific, measurable goals.

Building strong criteria

Good success criteria are:

Specific: Clearly define what you want to achieve. Instead of "good performance," specify "accurate sentiment classification."

Measurable: Use quantitative metrics or well-defined qualitative scales. Numbers provide clarity and scalability, but qualitative measures can be valuable if consistently applied along with quantitative measures.

Even "hazy" topics such as ethics and safety can be quantified:
 Safety criteria
Bad Safe outputs
Good Less than 0.1% of outputs out of 10,000 trials flagged for toxicity by our content filter.
Example metrics and measurement methods

Achievable: Base your targets on industry benchmarks, prior experiments, AI research, or expert knowledge. Your success metrics should not be unrealistic to current frontier model capabilities.

Relevant: Align your criteria with your application's purpose and user needs. Strong citation accuracy might be critical for medical apps but less so for casual chatbots.

Example task fidelity criteria for sentiment analysis
Common success criteria to consider

Here are some criteria that might be important for your use case. This list is non-exhaustive.

Task fidelity
Consistency
Relevance and coherence
Tone and style
Privacy preservation
Context utilization
Latency
Price

Most use cases will need multidimensional evaluation along several success criteria.

Example multidimensional criteria for sentiment analysis
Next steps
Brainstorm criteria

Brainstorm success criteria for your use case with Claude on claude.ai.

Tip: Drop this page into the chat as guidance for Claude!

Design evaluations

Learn to build strong test sets to gauge Claude's performance against your criteria.

Was this page helpful?