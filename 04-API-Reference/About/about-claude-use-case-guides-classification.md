---
title: "Classification - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/about-claude/use-case-guides/classification"
category: "04-API-Reference/About"
fetched_at: "2026-08-09T06:45:55Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

API reference




Console








Search


[](https://platform.claude.com/login)




Browse

Documentation

# Classification




Claude excels at processing, understanding, and recognizing patterns in text, images, and data. These capabilities make Claude especially powerful for classification tasks.




This guide walks through the process of determining the best approach for building a classifier with Claude and the essentials of end-to-end deployment for a Claude classifier, from use case exploration to back-end integration.



Visit the [classification cookbooks](https://platform.claude.com/cookbook/capabilities-classification-guide) to see example classification implementations using Claude.




When to use Claude for classification

When should you consider using an LLM instead of a traditional ML approach for your classification tasks? Here are some key indicators:

1.  **Rule-based classes**: Use Claude when classes are defined by conditions rather than examples, as it can understand underlying rules.
2.  **Evolving classes**: Claude adapts well to new or changing domains with emerging classes and shifting boundaries.
3.  **Unstructured inputs**: Claude can handle large volumes of unstructured text inputs of varying lengths.
4.  **Limited labeled examples**: With few-shot learning capabilities, Claude learns accurately from limited labeled training data.
5.  **Reasoning Requirements**: Claude excels at classification tasks requiring semantic understanding, context, and higher-level reasoning.

------------------------------------------------------------------------




Establish your classification use case

Below is a non-exhaustive list of common classification use cases where Claude excels by industry.

### Tech & IT

### Customer Service

### Healthcare

### Finance

### Legal

------------------------------------------------------------------------




Implement Claude for classification

The three key model decision factors are: intelligence, latency, and price.

For classification, a smaller model like Claude Haiku 4.5 is typically ideal due to its speed and efficiency. Though, for classification tasks where specialized knowledge or complex reasoning is required, Sonnet or Opus may be a better choice. Learn more about how Opus, Sonnet, and Haiku compare in the [models overview](https://platform.claude.com/docs/en/about-claude/models).

Use evaluations to gauge whether a Claude model is performing well enough to launch into production.




1\. Build a strong input prompt

While Claude offers high-level baseline performance out of the box, a strong input prompt helps get the best results.

For a generic classifier that you can adapt to your specific use case, copy the starter prompt below:

### Starter prompt




2\. Develop your test cases

To run your classification evaluation, you will need test cases to run it on. Take a look at the guide to [developing test cases](../Test-Evaluate/test-and-evaluate-develop-tests.md).




3\. Run your eval




Evaluation metrics

Some success metrics to consider evaluating Claude’s performance on a classification task include:

| Criteria              | Description                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Accuracy**          | The model's output exactly matches the golden answer or correctly classifies the input according to the task's requirements. This is typically calculated as (Number of correct predictions) / (Overall number of predictions). |
| **F1 Score**          | The model's output optimally balances precision and recall.                                                                                                                                                                     |
| **Consistency**       | The model's output is consistent with its predictions for similar inputs or follows a logical pattern.                                                                                                                          |
| **Structure**         | The model's output follows the expected format or structure, making it easy to parse and interpret. For example, many classifiers are expected to output JSON format.                                                           |
| **Speed**             | The model provides a response within the acceptable time limit or latency threshold for the task.                                                                                                                               |
| **Bias and Fairness** | If classifying data about people, is it important that the model does not demonstrate any biases based on gender, ethnicity, or other characteristics that would lead to its misclassification.                                 |




Deploy your classifier

To see code examples of how to use Claude for classification, check out the [Classification Guide](https://platform.claude.com/cookbook/capabilities-classification-guide) in the Claude Cookbook.
