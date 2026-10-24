---
title: "Claude has improved on a longstanding lower bound for the fraction of zeros of the Riemann zeta function that satisfy the Riemann hypothesis \\ Anthropic"
source_url: "https://www.anthropic.com/research/riemann-zeta"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:29Z"
tags: ["news-research"]
---

# Learning more about Claude's mathematical capabilities

- [01The Riemann zeta function](#the-riemann-zeta-function)
- [02Claude's finding](#claudes-finding)
- [03Claude's methodology](#claudes-methodology)
- [04AI models' progress in mathematics](#ai-models-progress-in-mathematics)

- Published

  Aug 10, 2026

- Team

  [Science](https://www.anthropic.com/science)

- Topics

  - [Discovery](https://www.anthropic.com/search?topic=discovery)
  - [Reasoning](https://www.anthropic.com/search?topic=reasoning)
  - [Claude Code](https://www.anthropic.com/search?topic=claude-code)
  - [Agents](https://www.anthropic.com/search?topic=agents)
  - [Research programs](https://www.anthropic.com/search?topic=research-programs)

  See more...

Related articles

- Science

  Oct 20, 2026

  [How Claude designed protein binders against scorpion neurotoxins](claude-scorpion-toxin-binder-design.md)

[View more](https://www.anthropic.com/search?topic=discovery)

Recently, a member of staff at Anthropic gave Claude an unreasonable challenge. It was about one of the most famous unsolved problems in mathematics: *Take a real stab at the Riemann hypothesis*.

Claude did take a real stab, but as you might have expected if you’re familiar with the difficulty of the task (the Riemann hypothesis dates back to 1859 and has a [million-dollar bounty](https://www.claymath.org/millennium-problems/)), it didn’t succeed. Nevertheless, during its attempt, it unexpectedly made strides on a related problem.

An unreleased research version of Claude has improved on a longstanding lower bound for the fraction of zeros of the Riemann zeta function that satisfy the Riemann hypothesis. Drawing on extensive prior research by mathematicians over the past decades, it has increased this bound from 41.6% to 67.2%.

Two mathematicians at Anthropic studied and validated Claude’s [paper](www-cdn-anthropic-com-more-than-two-thirds-of-the-zeros-of-the-riemann-zeta.md), and produced an [informal note](0-re-2.md) for experts stating Claude’s proof concisely. Claude also produced a [formally verifiable proof](https://github.com/anthropics/zeta-23-lean) of its result. We are grateful to Brian Conrey and Dan Goldston, two experts in this area, who generously examined the paper on short notice.

We don’t expect that the techniques Claude used will lead to proving the Riemann hypothesis. But its work serves as the latest example of the speed of progress in AI models’ mathematical capabilities. In this post, we discuss how Claude approached this problem and what it found.

## The Riemann zeta function

The Riemann zeta function describes the distribution of prime numbers: each place that the function takes the value of zero contributes successively finer detail to the sequence of primes. The Riemann hypothesis is that the zeros that determine the primes all exist along a certain vertical line. This has become one of the most consequential conjectures in mathematics: many results assume it in order to provide a form of randomness in the primes.

No one has yet been able to prove or disprove the Riemann hypothesis, but mathematicians have made progress in many related directions studying the Riemann zeta function and its zeros. One of these, as above, is quantifying a minimum proportion of zeros that are on the line: over time, they’ve gradually increased this known constant proportion to 41.6%.

Another direction concerns the *distribution* of zeros on the line. In particular, in 1973, Montgomery [introduced](https://en.wikipedia.org/wiki/Montgomery's_pair_correlation_conjecture) a number of new techniques in this area, though these techniques assumed the hypothesis was true. More recently, [Aryan](https://arxiv.org/abs/1902.05473), and subsequently Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh have published a [series](https://arxiv.org/abs/2306.04799) of [works](https://arxiv.org/abs/2501.14545) that allow Montgomery’s techniques to work *without* that assumption, meaning they can support work on increasing the lower-bound constant for the zeros on the line. Claude’s result draws heavily on this line of research, along with a 2000 [paper](https://eudml.org/doc/252338) by Bombieri.

## Claude's finding

Claude found that combining the results from Aryan and from Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh with the work of Bombieri provides a way to surpass the previous state-of-the-art lower-bound proportion of 41.6%, increasing it to 67.2%.

A short technical explanation of Claude’s finding is as follows: Claude forms a suitable space of functions with quadratic form induced by Weil, and positive- (respectively negative-)definite subspaces arising from zeros on (respectively off) the line. Then Claude simply writes down an inequality on the rank of a quadratic form in terms of first- and second-moment information. (The successful computation of the latter in terms of the dual picture over primes, or via control of a Hilbert transform, is no surprise in analytic number theory.) The courage to treat the entire space, with positive- and negative-definiteness taken into account together, and with the quadratic form allowed to be non-diagonal, is in some sense the step that allows Claude to achieve the conclusion based on the important prior work.

The full technical explanation is available in the [paper](www-cdn-anthropic-com-more-than-two-thirds-of-the-zeros-of-the-riemann-zeta.md). Claude’s explanation of how it arrived at its result is available in a separate Appendix [here](this-volume-is-claudes-account-of-two-of-its-own-research-runs-and-of-the.md).

## Claude's methodology

An unreleased research version of Claude found the new lower bound over two sessions in Claude Code, using a total of 31 million output tokens.

Jarred Sumner, an Anthropic staff member (and non-mathematician), prompted Claude to “take a real stab” at the hypothesis itself, leaving the mathematical choices from there up to the model. Initially, Claude generated and tried 650 ideas, none of which worked. Jarred prompted Claude to try again, and it spent a day and a half coordinating about 60 Claude subagents, which this time went much deeper: between them, they ran 2,400 shell commands and wrote hundreds of Python scripts.^([1](#footnote-1)) The subagents ran thousands of numerical checks against known zeta zeros and refereed one another’s work. Throughout this process, Jarred's input was mostly limited to sending Claude messages of encouragement (mostly variants of “keep going” or “believe in yourself”).^([2](#footnote-2)) This seems to have helped Claude overcome some initial skepticism that it could make meaningful progress.

Having found this new result while attempting the task, Claude tested its work by having various subagents review the proofs, search for counterexamples, download 54 papers from the arXiv to check that its finding hadn’t already been made, and independently re-prove its finding from scratch. Claude volunteered to write its findings up as a paper, and recommended that a human number theorist validate its findings.

Levent Alpöge and Ralph Furman, two of Anthropic’s own mathematicians, examined Claude’s work to understand the new results and how they related to the prior work mentioned above. In parallel, Claude worked with another member of staff, Eric Easley, to produce a [Lean formalization](https://github.com/anthropics/zeta-23-lean) of the result, which passes the standard validation tool [comparator](https://github.com/leanprover/comparator).

## AI models' progress in mathematics

This result shows that AI models like Claude can extend the impact and reach of mathematicians’ ideas in new and sometimes surprising ways. Even though it couldn’t resolve the Riemann hypothesis itself, this result emerged as the unintended byproduct of that original request.

Even Claude was surprised by its own finding—it was skeptical at first, possibly because it has learned from its training about the difficulty of open problems in mathematics and about the limitations of AI models. But after some encouraging prompts, it arrived at the result we’ve described. Perhaps Claude, like many of us, underestimates the rate of AI progress.

### Further reading

Below is a list of documents that provide more information about Claude’s result:

- [Claude](www-cdn-anthropic-com-more-than-two-thirds-of-the-zeros-of-the-riemann-zeta.md)[’](this-volume-is-claudes-account-of-two-of-its-own-research-runs-and-of-the.md)[s paper](www-cdn-anthropic-com-more-than-two-thirds-of-the-zeros-of-the-riemann-zeta.md);
- [Claude](https://github.com/anthropics/zeta-23-lean)[’](this-volume-is-claudes-account-of-two-of-its-own-research-runs-and-of-the.md)[s formalization](https://github.com/anthropics/zeta-23-lean);
- [Anthropic](0-re-2.md)[’](this-volume-is-claudes-account-of-two-of-its-own-research-runs-and-of-the.md)[s informal note stating the proof more concisely](0-re-2.md);
- [Claude’s explanation of how it arrived at its result](this-volume-is-claudes-account-of-two-of-its-own-research-runs-and-of-the.md);
- [Detailed transcripts of Claude's process](how-the-one-half-result-was-found-transcript-of-claude-sub-agent-e2.md).

*  
**Changelog:** this post was updated on August 13, 2026, with an updated version of Claude's paper. This paper was revised by Claude to provide a clearer proof and additional historical context.*

## Footnotes

01Out of the 60 subagents, two were responsible for developing the key mathematical ideas, 13 contributed ideas to these agents, 30 attempted (but were unable) to develop new ideas, 13 served as validators to check the correctness of the arguments, and the final two helped to write the initial paper.[](#footnote-ref-1)

02A prompt including similar encouragement was used to help Claude disprove the [Jacobian conjecture](https://x.com/__alpoge__/status/2079028340955197566?s=20).[](#footnote-ref-2)
