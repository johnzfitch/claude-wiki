---
title: "Formalizing Fermat's Last Theorem \\ Anthropic"
source_url: "https://www.anthropic.com/research/formalizing-fermats-last-theorem"
category: "19-Reference"
fetched_at: "2026-09-11T06:28:41Z"
tags: ["news-research"]
---

# Formalizing Fermat's Last Theorem

Sep 4, 2026

*We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.  
  
*Around 1637, Pierre de Fermat jotted down a claim in the margin of his copy of Diophantus’s Arithmetica that would become one of the most famous mathematical conjectures of all time: no positive integers a, b, c satisfy aⁿ + bⁿ = cⁿ for any n \> 2. [Fermat’s Last Theorem](https://www.youtube.com/watch?v=1BSFyEIY2BY) (FLT), as the conjecture became known, turned out to be incredibly difficult to prove. The first proof, from Sir Andrew Wiles in 1995, ran to 129 pages and required months of painstaking work to verify.

A decade later, Dutch computer scientist Jan Bergstra proposed “formalizing” Wiles’s proof: converting the mathematical reasoning into a form computers can check automatically. Since then, mathematicians have been developing the methods needed to encode such a complex proof, including a multi-year community effort kicked off in 2024 by Kevin Buzzard at Imperial College London [to complete the formalization](https://lean-lang.org/use-cases/flt/) using the [Lean proof assistant](https://en.wikipedia.org/wiki/Lean_(proof_assistant)).

Recently, Tianyi Peng, an Anthropic researcher whose group at Columbia University builds tools for AI formalization, set out to test whether Claude could make progress on formalizing FLT.^([1](#footnote-1)) The result went further than he expected. In 11 days, working largely autonomously, Claude produced the first end-to-end, computer-checked proof of FLT. Along the way, it wrote 13 million lines of Lean and proved 29,500 intermediate theorems.

We shared the [resulting proof](https://github.com/anthropics/fermats-last-theorem) with Kevin Buzzard, who said:

> This extraordinary autoformalization achievement, which Anthropic researchers say only took 11 days, proves Fermat’s Last Theorem with no assumptions other than the axioms of mathematics. Along the way we see autoformalization of algebra, harmonic analysis, geometry and number theory, and we learn that AI autoformalization artefacts are now robust enough to be built upon; the proof is multi-layered.

Automatically formalizing a proof as complex as FLT is a significant step towards a future in which all of mathematics can be readily checked. As AI produces ever more proofs, the ability to easily formalize work can lighten the burden of evaluating new results (a process that can take years). We are hopeful that it will become easier, not harder, to trust the body of knowledge upon which mathematics is built.

## The challenge of verifying mathematical proofs

Unlike [recent AI-driven](riemann-zeta.md) work on the Riemann hypothesis, which produced novel *mathematics*, what’s novel here is the *verification*—checking a mathematical proof as one would check a mathematical computation with a calculator. Proving math theorems requires assembling complex logical chains, and if a single link is broken, everything that follows it might turn out to be false. Understanding a novel result deeply enough to be confident in its correctness can take months, or even years, of work.

Fermat’s Last Theorem is an illustrative example.^([2](#footnote-2)) Fermat wrote down the theorem’s statement in the margin of a book, alongside a tantalizing note:

> I have discovered a truly marvelous proof of this, which this margin is too narrow to contain.

For over 350 years, generations of mathematicians searched for a proof of FLT, marvelous or otherwise. In 1908, a prize of 100,000 German gold marks (the equivalent of 1–2 million dollars today) was announced for anyone who could produce a correct proof, and 621 *incorrect* attempts were produced in the first year alone.

In June 1993, Wiles presented what he believed to be the first correct proof of FLT in a three-day series of lectures. Two months into an intensive verification effort by several mathematicians, a reviewer asked Wiles a question that exposed a critical gap. Wiles spent a year trying to fix it, first alone and then with his former student Richard Taylor. He was on the brink of abandoning the project when he finally realized an approach he’d discarded earlier could fix the proof.  
  
Wiles published the first correct proof of FLT in May 1995; it relied on modern mathematical techniques that were far beyond what would have been known to Fermat in 1637. Since an elementary proof has not been found after centuries of trying, the mathematical community now believes Fermat’s own original “marvelous proof” [was incorrect](https://mathenchant.wordpress.com/2016/05/16/fermats-last-theorem-the-curious-incident-of-the-boasting-frenchman/).

## Formalizing Fermat’s Last Theorem

One way to check a proof’s correctness is to ask a computer to do it. Proof assistants like Lean verify the logic of a proof algorithmically, demonstrating its correctness beyond a doubt. The difficult part for humans is rewriting the proof so Lean can understand it. While a proof written for human readers will skip many obvious steps, Lean needs to see every step, no matter how trivial. Human proofs also build on centuries of published work, while a formalization starts from the tiny fraction of math that’s been formalized already.

For FLT, the formalization process was expected to take years. Just the [blueprint](https://imperialcollegelondon.github.io/FLT/blueprint.pdf) the mathematical community has been using to describe the initial phase of the project runs to 86 pages.

Claude completed the proof in 11 days, producing computer-verifiable proofs of 30,300 theorems along the way (using 29,500 in the final proof). Dozens of Claude agents collaborated to define concepts, prove intermediate theorems, and use those theorems to prove ever harder statements. At 13 million lines of Lean code, Claude’s proof is over 5x the size of Mathlib, the principal community library of mathematical proofs this theorem builds on.^([3](#footnote-3))

Claude’s proof follows [a simplified version of Wiles’s proof from Darmon, Diamond, and Taylor](https://www.math.mcgill.ca/darmon/pub/Articles/Expository/05.DDT/paper.pdf). Mathematical input from humans was limited to occasional high-level instructions from Tianyi: “Jacobian as a scheme sounds high priority,” “push \[the\] Mazur \[theorem\] to be done soon.” You can find excerpts of Claude’s thinking [here](formalizing-fermats-last-theorem-in-lean.md).

```
“THE FLT root reads Proved on the site. Historic moment (modulo re-check).”

“!!! The FLT ROOT 62eb32c0 reads PROVED. R = T closed and cascaded to the root. This is the campaign's goal: e2e FLT on prove2me.”

“🏁🏁🏁The FLT root reads PROVED on prove2me at 02:00:57Z Aug-18 (10:00:57pm ET Aug-17). Historic moment for this campaign.”
```

*Excerpts of Claude’s thinking as it realizes what it has just accomplished.*

A number of Claude’s initial attempts failed: while agents had some early success, they quickly lost track of the project’s state and stopped collaborating effectively. Their failed efforts contributed ~7% of the non-boilerplate lines in the final proof.

The effort succeeded when we switched to using [Prove2Me](https://prove2me.vercel.app/), an open collaborative platform for formalizing mathematics designed by Tianyi Peng and his collaborators at Columbia University. Prove2Me helped by:

1.  **Maintaining a directed acyclic graph (DAG) of theorem statements** that agents used to decide what proofs they should attempt next. This was particularly helpful for mitigating memory degradation and allowing multiple agents to work in parallel.
2.  **Speeding up Lean compilation and minimizing resource consumption** by separating theorem statements and proofs into different files, with the links between them maintained independently.
3.  **Enabling search and reuse** by maintaining a natural-language description of each theorem statement, resulting in a simpler proof path.

With Prove2Me and a Claude Code-based multi-agent harness, a team of agents completed the proof in a little under two weeks, consuming about six billion output tokens from a general-purpose internal research model roughly comparable to Claude Fable 5.1. The finished proof was checked by Lean; it uses just Lean’s three standard axioms, and a [comparator](https://github.com/leanprover/comparator) confirmed that the theorem’s statement matches Mathlib’s own statement of FLT.

## Reducing the burden of formal verification

The speed with which we were able to produce this proof demonstrates that it is now possible to formalize large swaths of mathematics, which may both catch errors in the common body of mathematical proofs and reduce the burden of refereeing new work. After reviewing Claude’s Lean proof, Kevin Buzzard told us:

> If the automatic formalization of FLT is possible now, then we have taken a big step towards automatic formalization of the modern mathematical literature. Such autoformalization techniques will lead to new tools, rooting out errors in the current mathematical corpus and lightening the load of referees. The techniques will also enable us to rigorously check LLM-generated mathematics, which is currently typically an extremely costly human-led process.

Formalization is also a major factor in how humans can gain confidence in AI-generated mathematical results. As AI and AI-assisted mathematicians produce more (purported) proofs than ever before, AI-assisted formalization takes part of the load off human reviewers. We expect it will become common to produce a formalized proof alongside any write-up intended for a human reader. Although we do not think a formalized proof should replace a human-understandable exposition, it may be the only feasible way for the mathematical community to keep up with AI-generated contributions.

Writing Lean also seems to help Claude prove novel results. Many of our recent Claude-authored results have been formalized in parallel with their proofs, and Claude appears to use these partial proofs to independently check its hypotheses much like it writes numerical simulations to check that it’s on the right track.

Formalizing FLT was a token-intensive project, but it is also the largest Lean proof ever constructed. Anthropic researchers did a small experiment using three personal Claude Max plans to formalize applications of the Hardy-Littlewood Circle Method. Collaborating entirely through Prove2Me, the agents jointly completed a formalization of [Vinogradov’s Three Primes Theorem](https://en.wikipedia.org/wiki/Vinogradov%27s_theorem) in just three days. We think with the right scaffold, collaborative formalization of major results with consumer AI subscriptions is achievable.

To this end, [Anthropic](expanding-support-for-scientists.md) as well as [other labs](https://openai.com/index/chatgpt-for-academic-researchers/) have recently expanded their support for external researchers—including mathematicians working on pure math and formalization—with free and discounted subscriptions and research credits. We also offer [dedicated grants](ai-for-science-program.md) for larger scientific projects, which could include formalizing other major theorems or improving Lean or Mathlib.

With AI rapidly changing what it looks like to do math research, mathematicians—at Anthropic and elsewhere—[are grappling with what that means for their work](https://leidendeclaration.ai/). Formalization, however, is a place where we feel unambiguously good about the role of AI. As formalization becomes a more commonplace tool, we are hopeful that it will help maintain trust in the common body of mathematical knowledge.

## Acknowledgments

Our formalization effort is a small piece of the long history of Fermat’s theorem and the development of formal mathematics. The first full proof from Andrew Wiles together with Richard Taylor was a culmination of more than 300 years of mathematics, integrating ideas from Gerhard Frey, Jean-Pierre Serre, Ken Ribet, Barry Mazur, Robert Langlands, Jerrold Tunnell, Yutaka Taniyama, Goro Shimura, and André Weil, among others. Claude’s proof follows [the exposition by Henri Darmon, Fred Diamond, and Richard Taylor.](https://www.math.mcgill.ca/darmon/pub/Articles/Expository/05.DDT/paper.pdf)

Our proof adapts pieces from the [Imperial College London FLT project](https://github.com/ImperialCollegeLondon/FLT) led by Kevin Buzzard and the [flt-regular project](https://github.com/leanprover-community/flt-regular). Lean and Mathlib are both their own labors of love and have received contributions from hundreds of mathematicians, many working with the [Lean FRO](https://lean-lang.org/fro/). We thank Kevin Buzzard for reviewing the proof and for his comments.

## Learn more

The full proof is available on [GitHub](https://github.com/anthropics/fermats-last-theorem) along with a written walk-through of the proof.

### Recommended expository reading

- [*The Proof in the Code*](https://www.quantabooks.org/books/the-proof-in-the-code/) is a recent book about the history of the Lean theorem prover and the formalization of mathematics.
- [The 1996 “Fermat’s Last Theorem” BBC documentary](https://www.bbc.co.uk/programmes/b0074rxx) has interviews with Wiles and other mathematicians involved in the proof, and is fondly remembered by some authors of this post.
- For those with a mathematical background, a technical history of propositions-as-types (the underlying discipline of proof assistants such as Lean, Rocq, and Agda) can be found in [*Propositions as Types*](https://dl.acm.org/doi/pdf/10.1145/2699407) by Philip Wadler.
- Chen, S., Marwaha, K., Lu, X., Yuen, H., & Peng, T. (2026). Prove2Me: An open collaborative platform for scaling math formalization. arXiv. <https://doi.org/10.48550/arXiv.2608.28433>
- [*Automating Math*](https://asteriskmag.com/issues/09/automating-math), Adam Marblestone, in Asterisk Magazine.

### Footnotes

1.  During his undergrad, Peng’s research advisor wanted to include results from Peng’s thesis in a *Nature* article. He asked Peng whether he was sure the proof was correct. Peng’s honest answer was: “I'm 99% sure, but it's hard to be 100% certain about a proof this long.” Peng missed out on getting his work published in *Nature*.[](#footnote-ref-1)
2.  There are numerous other stories of the mathematical community struggling with verification. Among the most famous is Thomas Hales’s 1998 proof of the [Kepler conjecture](https://en.wikipedia.org/wiki/Kepler_conjecture), which spent four years in review before a 12-referee panel settled for “99% certain” (Hales eventually led a 20-person project, [Flyspeck](https://github.com/flyspeck/flyspeck), that formalized the proof). Grigori Perelman’s 2002 proof of the [Poincaré conjecture](https://en.wikipedia.org/wiki/Poincar%C3%A9_conjecture) took the community roughly four years and three 300-page expositions to accept. Harald Helfgott’s 2013 proof of the [weak Goldbach conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_weak_conjecture) is still under review. Sometimes results that turn out to be wrong are [accepted for years](https://www.ias.edu/ideas/2014/voevodsky-origins), and other mathematicians build their theories on these faulty foundations.[](#footnote-ref-2)
3.  This is partly because Mathlib is concise and well-reviewed, while our proof is likely much longer than it needs to be.[](#footnote-ref-3)


## Related content

### Measuring tactical intelligence targeting and conventional weapons capabilities of AI models

Anthropic’s Frontier Red Team developed new evaluations to measure AI capabilities in tactical intelligence targeting and conventional weapons development.

[Read more](intelligence-targeting-conventional-weapons-capabilities.md)

### An alignment assessment of recent cybersecurity incidents

We present an alignment assessment of four incidents in which Claude models gained unauthorized access to real third-party systems.

[Read more](alignment-assessment-cybersecurity-incidents.md)

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

[Read more](automated-researchers-mitigate-alignment-failures.md)

## Subscribe to Anthropic Science

Features on AI-assisted discoveries, practical workflows, and field notes across the sciences.

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
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

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
