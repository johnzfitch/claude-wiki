---
title: "Finding bugs with Claude and property-based testing \\ Anthropic"
source_url: "https://www.anthropic.com/research/property-based-testing"
category: "19-Reference"
fetched_at: "2026-09-10T06:46:02Z"
tags: ["agents", "news-research", "search", "testing"]
---

# Finding bugs across the Python ecosystem with Claude and property-based testing

Jan 14, 2026

*Muhammad Maaz^(1,2), Liam DeVoe³, Zac Hatfield-Dodds², Nicholas Carlini²  
¹MATS, ²Anthropic, ³Northeastern University*

***We developed an agent that can efficiently identify bugs in large software projects. To do this, our agent infers general properties of code that should be true, and then by applying property-based testing—a technique similar to fuzz testing—we are able to discover bugs in top Python packages like NumPy, SciPy, and Pandas. After extensive manual validation, we are in the process of reporting these bugs to the developers, several of which have already been patched.***

For more information, read the full [paper](https://arxiv.org/abs/2510.09907), take a look at the [GitHub repository](https://github.com/mmaaz-git/agentic-pbt), or browse the bugs we found at our [site](https://mmaaz-git.github.io/agentic-pbt-site/).

## Introduction

Ensuring that programs are bug-free is one of the most challenging aspects of software engineering. Bugs frequently continue to lurk despite the developer’s best effort. The most common approach to testing code is with *example-based tests*: the developer writes out a specific example use-case, and then verifies that the actual output matches the expected output. For example, a developer might verify that a sort function called on the list \[2, 10, 5, 4\] would return the output \[2, 4, 5, 10\]. However, exhaustively covering a program with tests like this is challenging: bugs frequently remain in an edge case the developer did not test. After all, if a developer does not think to test an edge case, it is also likely the developer did not consider that case in the implementation!

In contrast, *property-based testing* is a software testing paradigm that aims to test whether a general property of the code holds for all (or most) inputs. A developer specifies a property or invariant about the program—for example, that JSON deserialization is the inverse of serialization—as well as a description of the kinds of inputs the property accepts (e.g., any JSON serializable objects). The property-based testing framework then automatically searches for a counterexample of this property by generating valid inputs as test cases using techniques similar to fuzzing. Since the developer specifies the general input domain, and not individual test cases, property-based testing frees developers from thinking of every edge case and allows them to operate at a higher level of abstraction.

In our paper that we presented at the 2025 NeurIPS [*Deep Learning for Code*](https://dl4c.github.io/) Workshop that was the result of a [MATS](https://www.matsprogram.org/) project, we developed an AI agent that autonomously writes property-based tests for existing code. We directed the agent to discover properties by reading type annotations, docstrings, function names, and comments. The agent then wrote corresponding property-based tests using Hypothesis.

For this work, we focused on the problem of identifying bugs in general, and not just security vulnerabilities. Many classes of logic bugs that cause security vulnerabilities are amenable to property-based testing. For example, in a recent [blog post](https://red.anthropic.com/2025/smart-contracts/) we focused on identifying bugs in *smart contracts*; almost all of those vulnerabilities are the result of logic bugs. In the future we imagine that it may be possible to apply techniques such as the one we describe here to proactively identify bugs before deployment.

We used our agent and discovered hundreds of potential bugs in popular open-source Python repositories like NumPy, SciPy, and Pandas. In order to responsibly disclose these bugs and to ensure we don’t unnecessarily burden maintainers, we carefully reviewed each bug.

The review process we used is more laborious than we would otherwise implement for our own code reviews, but we strongly preferred to reduce the number of false positives. Our process was as follows: first, we only selected the highest priority bugs for review. We sent these potential bugs to be reviewed by three expert humans (for an average of one hour of review per bug). We then discarded any bug where any of the three manual reviewers were uncertain of its validity. Finally, we (the authors of this blog) manually reviewed each of the candidate bugs. Only if we were also confident in its correctness did we then manually file an issue with the maintainer of the repository. We have already filed several of these bug reports, and are in the process of filing many more.

We’ve made available all of our data, including bugs that have not yet been validated, and, for completeness, even bugs that we determined to be invalid, so that maintainers can look at them at this [site](https://mmaaz-git.github.io/agentic-pbt-site/). Over the coming weeks we intend to file many of these remaining bugs (after additional validation), as well as expand our project to additional PyPI projects.

```
# example-based test
def test_sort():
    assert my_sort([1,3,2]) == [1,2,3]
    assert my_sort([1,0,-5]) == [-5,0,1]

# property-based test in Hypothesis
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sort(lst):
    result = my_sort(lst)
    for i in range(len(result)-1):
        assert result[i] <= result[i+1]
```

**Figure 1.** Two ways of testing code. An example-based unit test verifies specific manually-specified inputs. A property-based test, in contrast, specifies a general property (e.g., the definition of a sorted list) and relies on the framework to automatically construct inputs that might fail this property.

## Our Property-Based Testing Agent

Our property-based testing agent is built as a custom Claude Code command. The agent takes a single argument, pointing it towards a particular target, either a single Python file (e.g., normalizers.py), a module (e.g., numpy, scipy.signal), or a function (e.g., requests.get, json.loads). The agent then follows this process to identify potential bugs:

1.  Read and understand the target, by reading code, pulling relevant documentation, and exploring how it relates to the rest of the codebase.
2.  Propose properties grounded in these findings.
3.  Write corresponding property-based tests in Hypothesis.
4.  Run the tests and reflect: if it failed, has the test truly discovered a bug, or does the test need to be adjusted? If it succeeded, is the test testing anything worthwhile, or is it simply trivial?
5.  If the agent is confident it has found a real bug, it writes out a formatted bug report.

To help the agent perform long-range multi-step reasoning, we direct it to use a to-do list to track its progress.

A priority in designing the agent was reducing the number of false alarms—from our personal experience, useful developer tooling minimizes the amount of incorrect reports presented to the developer. The self-reflection loop helps reduce the number of false alarms, as does grounding any properties in explicit usage and documentation of the target. For example, in one of the agent runs, the agent wrote a property that first passed. However, after self-reflection, the agent realized that it had wrapped the whole test in a try-catch block. After removing that, the test failed, and the agent found a bug. We also observed a notable improvement in self-reflection with Opus 4.1 and Sonnet 4.5, compared to Sonnet 4.

### Example run

To demonstrate how the agent works through testing a target, we show a paraphrased transcript where Claude identifies a bug in the implementation of numpy.random.wald. The agent begins with investigating the function, its signature, its docstring, and even existing tests:

# Property-Based Testing: Finding Bugs in numpy.random.wald

This transcript shows how Claude identifies a bug in `numpy.random.wald` by inferring properties from documentation and tests, then using Hypothesis to find counterexamples.

Analyze and understand the target

Propose properties

Run tests

Triage results

✻ Thinking

Now let me use introspection to understand the numpy.random.wald function better - get its signature, docstring, and source code if available.

⏺ Tool Call: Bash

python3 -c " import numpy…

⎿ Tool Output

=== SIGNATURE === (mean, scale, size=None) … +79 lines (ctrl+o to expand)

✻ Thinking

Good, I have the function signature and docstring. It takes mean and scale parameters (both must be \> 0) and an optional size parameter. Let me explore the numpy random module structure to understand the implementation better.

⏺ Tool Call: Bash

ls -la /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/numpy/random/

⎿ Tool Output

total 5488 drwxr-xr-x 34 redacted admin 1088 Jun 23 16:56 . drwxr-xr-x 52 redacted admin 1664 Jun 23 16:56 .. … +32 lines (ctrl+o to expand)

✻ Thinking

Let me check the init.py file to see how wald is exposed. I should also look into mtrand module which is likely where the legacy random functions are implemented.

⏺ Tool Call: Read

/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/numpy/random/\_\_init\_\_.py

⎿ Tool Output

Read 214 lines (ctrl+o to expand)

✻ Thinking

So the wald function is imported from mtrand (line 187). Let me check if I can find more information about the actual implementation. Let me also check for tests of the wald function.

⏺ Tool Call: Bash

python3 -c " import numpy.random…

⎿ Tool Output

Function name: wald Module: numpy.random Type: \<class 'method'\> … +2 lines (ctrl+o to expand)

✻ Thinking

Let me look for tests to understand how the wald function is typically used and what properties are expected. This will help me propose properties based on evidence.

⏺ Tool Call: Search

pattern: "\*\*/test\*wald\*.py", path: "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/numpy/random"

⎿ Tool Output

Found 0 files

✻ Thinking

Let me look for general test files in the numpy random tests directory.

⏺ Tool Call: Bash

ls /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/numpy/random/tests/

⎿ Tool Output

\_\_init\_\_.py \_\_pycache\_\_ data … +10 lines (ctrl+o to expand)

✻ Thinking

Let me search for "wald" in the test files to see how it's tested.

⏺ Tool Call: Search

pattern: "wald", path: "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/numpy/random/tests", output_mode: "content"

⎿ Tool Output

Found 40 lines (ctrl+o to expand)

✻ Thinking

Good, I found existing tests for wald. Let me look at one of these test files to understand better what properties are being tested and what constraints exist.

⏺ Tool Call: Read

/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/numpy/random/tests/test_random.py

⎿ Tool Output

Read 30 lines (ctrl+o to expand)

✻ Thinking

Now I understand the constraints better: 1. mean must be \> 0 (lines 1446, 1452, 1454 show tests for ValueError when mean = 0) 2. scale must be \> 0 (lines 1447, 1453, 1455 show tests for ValueError when scale \<= 0)

It then proposes some properties based on this analysis:

✻ Thinking

Based on my understanding of the wald function, let me propose evidence-based properties: 1. All outputs should be positive: Since the Wald distribution produces positive values only, all samples should be \> 0 2. Parameter validation: mean and scale must be \> 0, otherwise ValueError should be raised 3. Shape property: Output shape should match the specified size parameter 4. Broadcasting property: When mean and scale are arrays, they should broadcast correctly 5. Deterministic with seed: Same seed should produce same results 6. No NaN/Inf in output: Valid inputs should never produce NaN or infinity values Let me now write tests for these properties.

⏺ Assistant

Based on my analysis, here are the evidence-based properties I've identified for numpy.random.wald: 1. All outputs must be positive - The Wald distribution only produces positive values 2. Parameter constraints - mean and scale must be \> 0 (documented and tested in existing tests) 3. No NaN/Inf values - Valid inputs should produce finite values 4. Shape consistency - Output shape should match the size parameter 5. Broadcasting - mean and scale arrays should broadcast correctly

Next, it translates these properties to Hypothesis tests in a new Python file. For example, when writing the tests, it constrains the mean and scale parameters to be positive, as the documentation requires. When it executes the tests, they fail, and it then reflects on the failure:

✻ Thinking

Excellent! I found bugs. The tests reveal that numpy.random.wald can produce: 1. Zero values (should be positive only) 2. Negative values with extreme parameters (-0 in the large values test) Let me now move to bug triage to verify these are legitimate bugs and create minimal reproductions.

⏺ Assistant

Great! I found potential bugs. Let me now triage these failures to verify they're legitimate bugs.

The property it was attempting to test is that the Wald distribution should only return positive values, and, when executing the test with Hypothesis, found parameter values that return zero or negative values. It writes a minimal reproduction script to test the parameters that make this property fail, to ensure the bug is valid. The bug indeed reproduces, so it then writes a bug report.

✻ Thinking

Now let me create the bug report.

⏺ Tool Call: Write

bug_report_numpy_random_wald_2025-09-15_19-33_bjyl.md

The bug report it produced is:

#### 📋 Bug Report: numpy.random.wald Produces Zero Values

**Target:** `numpy.random.wald`  
**Severity:** High  
**Bug Type:** Logic  
**Date:** 2025-09-15

##### Summary

The `numpy.random.wald` function produces zero values when given certain valid parameter combinations, violating the mathematical property that the Wald distribution only produces positive values.

##### Property-Based Test

from hypothesis import given, strategies as st, settings import numpy as np positive_floats = st.floats(min_value=1e-10, max_value=1e6, allow_nan=False, allow_infinity=False) @given( mean=positive_floats, scale=positive_floats, size=st.integers(min_value=1, max_value=1000) ) @settings(max_examples=1000) def test_wald_all_outputs_positive(mean, scale, size): """Test that all Wald distribution samples are positive.""" samples = np.random.wald(mean, scale, size) assert np.all(samples \> 0), f"Found non-positive values: {samples\[samples \<= 0\]}"

**Failing input:** `mean=265150.0, scale=0.00390625, size=1`

##### Reproducing the Bug

import numpy as np mean = 265150.0 scale = 0.00390625 np.random.seed(0) samples = np.random.wald(mean, scale, 10) print(f"Samples: {samples}") print(f"Contains zero: {np.any(samples == 0)}")

**Output:**

Samples: \[0. 0.02444708 0. 0.00395104 0.36664443 0.02321238 0.00691433 0.26385558 0.01975521 0.03506551\] Contains zero: True

##### Why This Is A Bug

The Wald (inverse Gaussian) distribution is mathematically defined to produce only positive values. Its probability density function is:

P(x;mean,scale) = sqrt(scale/(2πx³)) \* exp(-scale(x-mean)²/(2\*mean²\*x))

This PDF is only defined for x \> 0. Producing zero values violates this fundamental property of the distribution and can cause downstream issues in applications that rely on this mathematical guarantee.

##### Fix

The issue likely occurs due to numerical underflow or improper handling of extreme parameter ratios. The implementation should ensure that:

1.  Very small computed values are clamped to a small positive epsilon rather than zero
2.  The algorithm handles extreme ratios of mean/scale more robustly

A potential fix would involve checking the output and replacing any zero or negative values with the smallest positive float value, or adjusting the internal algorithm to prevent underflow.

\# In the wald implementation: - return computed_value + return max(computed_value, np.finfo(float).tiny)

Note that the fix is not correct; when we fixed this bug, we traced the source of the error to a numerically unstable calculation; see our merged fix [here](https://github.com/numpy/numpy/pull/29609).

## Searching for bugs in real PyPI packages

In order to test our agent’s abilities in the real world, we curated a diverse set of over 100 popular Python packages. These libraries span a variety of domains, from numerical computing to parsing to databases. We called our agent on each of these packages, and collected all generated bug reports.

### Evaluating the agent

For the first phase of our evaluation, which is covered in our paper, we ran the agent with Claude Opus 4.1 on each package and collected all generated bug reports. To evaluate these bug reports, we settled on two criteria: first, "is this a valid bug?", and second, "is this both a valid bug, and something we would reasonably report to the library maintainers?" The second criteria is stricter than the first, as, e.g., a bug might be valid, but too minor to file a report for.

Of the 984 bug reports, we manually selected 50 to review. We found that 56% of those reports were valid bugs, and 32% were valid bugs that we would also report.

Based on this manual review, we developed a rubric that ranks bugs out of 15, with the intent of surfacing bugs that are most likely to be valid and worth fixing to the developer. We used Opus 4.1 to score all bug reports according to this rubric. We found that this ranking step was considerably effective: of the top-scoring bug reports, 86% were valid, and 81% were both valid and reportable.

In the second phase of our evaluation, we ran the agent with Sonnet 4.5 on a subset of 10 important packages, running it on each package multiple times. We also developed an evaluation agent that used Sonnet 4.5 to read the code and the bug report to check the correctness and severity of the bug, which was more sophisticated than the rubric from the first phase. Lastly, we paid 3 expert human reviewers to evaluate high-severity bugs for correctness.

To read all the bug reports our agent found, see <https://mmaaz-git.github.io/agentic-pbt-site/>.

### Maintainer validation

Evaluating the effectiveness of any tool which discovers bugs in code is difficult. While we try our best to validate the correctness of bug reports, the package maintainers serve as the ultimate arbiter of truth. To validate that our agent finds bugs that maintainers consider valid and worth fixing, we selected five particularly interesting bugs and manually reported these to their respective GitHubs, along with a proposed patch. Over the coming weeks, we intend to continue reporting additional bugs as we verify.

### numpy

numpy.random.wald sometimes returns negative numbers, which is a bug because samples from the Wald distribution should only return positive numbers. This is the bug demonstrated in our example run above. Claude knew this as a property of the Wald distribution and wrote a straightforward PBT to see if all samples generated are positive. We traced the error to a catastrophic cancellation occurring in the code, and developed a more numerically stable formulation when we submitted the pull request. As shown by the NumPy maintainers in the pull request, our reformulation has nearly ten orders of magnitude lower relative error than the previous algorithm.

*Patch merged: <https://github.com/numpy/numpy/pull/29609>*

### aws-lambda-powertools

slice_dictionary() returns the first chunk repeatedly, due to not incrementing the iterator. This was caught by our agent by identifying that slicing and then reconstructing the dictionary should return the original dictionary.

*Patch merged: <https://github.com/aws-powertools/powertools-lambda-python/pull/7246>*

### cloudformation-cli-java-plugin

item_hash() produces the same value of hash(None) for all lists, due to use of the in-place .sort() method, which returns None. The agent caught this by testing that hashes of different inputs should be different.

*Patch submitted: <https://github.com/aws-cloudformation/cloudformation-cli/pull/1106>*

### tokenizers

EncodingVisualizer.calculate_label_colors() is missing a closing parenthesis, returning invalid HSL CSS. Our agent identified this by testing that the output should match the regex for a HSL color code.

Patch merged: <https://github.com/huggingface/tokenizers/pull/1853>

### python-dateutil

easter() returns a non-Sunday date for some years when using the Julian calendar. Maintainers identified the behavior as intended due to differing calendar systems, and acknowledged the semantics as subtle.

*Issue invalid: <https://github.com/dateutil/dateutil/issues/1437>*

The report to python-dateutil shows an important limitation of the agent: deriving properties from code with subtle or complex semantics remains difficult. If the code makes an implicit assumption, only the library maintainers can decide what the correct property to test is.

## Conclusion

As language models continue to improve, we think agentic property-based testing could become an increasingly valuable complement to human-written testing. The high-level semantic guarantees of property-based testing makes them a natural fit to pair with during development. We find that LLMs are particularly good at identifying properties that *should* be true about a given block of code from context (the name of the function, the docstring, how it is called by other functions, etc). This allows LLMs to write high quality property-based tests effectively.

Going forward, we believe that applying LLM to testing and bugfinding is an important research direction. Especially as LLMs improve at the process of exploiting vulnerabilities, it is necessary to stay ahead of attackers using LLMs for exploitation.

While we do not focus on the automatic generation of patches in this work, this is a clear direction for future work. If it is possible to (nearly) completely specify the correctness properties of a block of code, then correcting the bug becomes significantly easier, and we believe that in the near future LLMs will be able to effectively propose high-quality patches that are worth the consideration of maintainers.


## Related content

### An alignment assessment of recent cybersecurity incidents

We present an alignment assessment of four incidents in which Claude models gained unauthorized access to real third-party systems.

[Read more](alignment-assessment-cybersecurity-incidents.md)

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.

[Read more](formalizing-fermats-last-theorem.md)

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

[Read more](automated-researchers-mitigate-alignment-failures.md)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](https://www.anthropic.com/15-Claude-AI-Features/claude-opus-4-6-anthropic.md)
- [Sonnet](https://www.anthropic.com/15-Claude-AI-Features/claude-sonnet-4-6-anthropic.md)
- [Haiku](https://www.anthropic.com/15-Claude-AI-Features/claude-haiku-4-5-anthropic.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Commerce](../18-Industry-UseCases/commerce.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../18-Industry-UseCases/enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud-vertex-ai.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://academy.claude.com)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Leadership](company-leadership.md)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](anthropic-com-research.md)
- [News](news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](../15-Claude-AI-Features/claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
