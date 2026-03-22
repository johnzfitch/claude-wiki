---
category: "19-Reference"
fetched_at: "2026-03-20T10:37:08Z"
source_url: "https://www.anthropic.com/research/roundup-feb-2026"
title: "LLMs Conjecture, Prove, and Challenge: February 2026 \\ Anthropic"
---

# LLMs Conjecture, Prove, and Challenge: February 2026

Feb 1, 2026

Welcome to *Field Notes*, a recurring roundup of notable developments at the intersection of AI and scientific research. We cover work across institutions and tools—what matters is the science and the methodology, not who built the model.

## GPT-5.2 conjectures a new formula in particle physics, and an internal model proves it:

*…A genuinely new result, but the question is how far the method generalizes…*

OpenAI has [published a preprint](https://openai.com/index/openai-for-science/) with physicists at the Institute for Advanced Study, Vanderbilt, Cambridge, and Harvard showing that a class of gluon scattering amplitudes—long assumed to vanish at tree level—are in fact nonzero in a specific kinematic regime called the “half-collinear” limit.

**How it worked:** The human authors computed amplitudes for small numbers of gluons by hand, obtaining expressions whose complexity grows superexponentially. GPT-5.2 Pro simplified these expressions substantially, spotted a pattern across the base cases, and conjectured a closed-form formula valid for all *n*. A scaffolded version of GPT-5.2 then independently derived the same formula and produced a formal proof after roughly 12 hours of reasoning. The result was verified analytically against the Berends-Giele recursion relation and the soft theorem.

This is a meaningful step beyond the pattern we saw with Matt Schwartz’s [vibe physics work](vibe-physics.html), where Claude executed calculations under close human supervision. Here, the model contributed something the human authors hadn’t found on their own: the simplified closed-form expression. The humans still identified the problem, set up the framework, and verified the result—but the conjecture itself came from the model.

**What GPT-5.2 actually contributed:** It’s worth being precise about the division of labor. The key scientific insight—that single-minus amplitudes are supported at a special point in twistor space and that the half-collinear regime is worth investigating—was not the model’s contribution. The preprint itself notes that this observation traces back to earlier work by Witten and by Roiban, Spradlin, and Volovich. The human physicists identified the problem and the kinematic regime. What GPT-5.2 contributed was simplifying the resulting expressions and conjecturing the closed-form formula—pattern recognition over structured symbolic output, which is genuinely useful but a different thing than the conceptual leap of knowing where to look.

**Why this matters—pattern recognition as a scientific instrument:** The problem was well-suited to what LLMs do best: spotting structure in complicated symbolic expressions. This is a genuinely useful capability for theoretical physics, where complex expressions frequently hide simple underlying forms. The paper would have been interesting with or without the simplified formula—the physics of the nonzero amplitude is the main result. But having a clean closed-form expression enables further work (the authors report that graviton amplitudes have already been computed using the same approach). The question going forward is how far this pattern—humans identify the problem, models simplify and generalize—extends to settings where the expressions are less algebraically structured.

Read more: [OpenAI for Science](https://openai.com/index/openai-for-science/) (February 13, 2026). [Preprint on arXiv](https://arxiv.org/abs/2602.09798).

## Mathematicians build a genuinely held-out test for frontier AI. OpenAI claims 6 out of 10:

*…First Proof is the kind of eval the field needs, but the details of how the problems were solved matter a lot…*

A group of mathematicians from Stanford, Columbia, EPFL, Imperial College, UT Austin, Yale, Berkeley, Chicago, Harvard, and elsewhere have built [First Proof](https://arxiv.org/abs/2502.11038): ten research-level math problems whose solutions are known to the proposers but had not been published. The problems span algebraic combinatorics, spectral graph theory, algebraic topology, stochastic analysis, symplectic geometry, representation theory, and more. The key property: these are sampled from the actual distribution of questions working mathematicians are currently solving.

**OpenAI’s attempt:** OpenAI ran an internal model (described as one “currently in training”) against the challenge and [published solution attempts](https://cdn.openai.com/pdf/a430f16e-08c6-49c7-9ed0-ce5368b71d3c/1stproof_oai.pdf), claiming correct answers on six of ten problems. Jakub Pachocki described the effort as a “chaotic side-sprint executed in a week” and noted the methodology “leaves a lot to be desired.”

**Important context on the “6/10”:** Some of the problems had apparently already been solved by GPT-5.2 Pro before the challenge was published, complicating the “unseen” framing. And at least some prompts included substantive mathematical guidance. For example, the solution to Problem 6 (a spectral graph theory result) was prompted with: “Try using a BSS barrier type argument. You will have to think hard about the setup and the inductive framework to push it through.” That’s a very specific hint that meaningfully narrows the search space. The line between “AI solves problem” and “AI executes a well-hinted proof strategy” matters enormously.

**Why this matters—evaluating creativity, not just competence:** First Proof is arguably the most ecologically valid math benchmark we’ve seen. These are frontier scientific problems for which some humans have figured out answers but haven’t told many other humans yet. If AI systems do well here, it tells us something real about approximating human creative leaps. But the authors make a crucial point: most of modern research is not about solving well-specified problems. It’s about figuring out what the question actually is. The frontier of AI evaluation will have to move from solving problems to generating questions about which problems to solve.

Read more: [First Proof](https://arxiv.org/abs/2502.11038) (arXiv). [OpenAI solution attempts](https://cdn.openai.com/pdf/a430f16e-08c6-49c7-9ed0-ce5368b71d3c/1stproof_oai.pdf) (PDF).

## Terence Tao co-founds SAIR, a foundation arguing AI needs scientific foundations, not just more compute:

*…An unusually credentialed effort to build institutional infrastructure for AI-for-science…*

The [Foundation for Science and AI Research (SAIR)](https://www.sair.foundation) launched in early 2026 with Fields Medalist Terence Tao as co-founder, alongside Nobel laureate Barry Barish, Turing Award winner Richard Sutton, and senior AI leaders from Amazon AWS, Microsoft Research, NVIDIA, and OpenAI.

**The intellectual thesis:** SAIR’s [founding essay](https://www.sair.foundation/blog/scaling-the-science-of-intelligence) argues that reaching more capable AI requires scaling our *scientific understanding* of intelligence, not just model parameters. The analogy: current models are like incandescent bulbs—brighter with more power, but fundamentally limited without the material science that enabled LEDs. Tao frames the core challenge: we lack a unified mathematical framework connecting the empirical performance of neural networks with a fundamental understanding of how intelligence emerges from them. Deriving scaling laws from first principles, the way physics derives fluid dynamics from particle interactions, remains an open problem.

**On the role of the scientist:** A [second essay](https://www.sair.foundation/blog/sairs-perspective-on-science-and-ai) makes a complementary argument. The concern is not that AI replaces scientists but that it eliminates the entry-level work—the “sandbox”—where researchers develop the deep intuition needed to verify and direct AI outputs. Without that training ground, we risk a future where no one understands the fundamental principles behind the machine. SAIR’s proposed solution: redefine the scientist as “architect of verification,” shifting from executing every calculation to high-level validation and logical architecture. This resonates strongly with what Matt Schwartz found in practice—domain expertise becomes more valuable, not less, when the model handles the grunt work.

**Operational model:** Three pillars: direct research grants, a corporate partnership program connecting Fortune 500 companies with researchers, and a conference series. The foundation [kicked off at UCLA](https://www.sair.foundation/events) on February 10, co-organized with IPAM and UCLA Physical Sciences.

**Why this matters—the field is building institutions:** Whether SAIR becomes consequential will depend on whether it translates its star-powered board into sustained research funding and genuine cross-disciplinary output. But the fact that people of this caliber are organizing around the thesis that AI needs deeper scientific foundations—not just more compute—is itself a signal. The AI-for-science space is moving from scattered individual efforts toward institutional infrastructure, and SAIR is positioning itself explicitly in the gap between fragmented academic funding and industry’s focus on scaling.

Read more: [sair.foundation](https://www.sair.foundation). Blog posts on [scaling intelligence](https://www.sair.foundation/blog/scaling-the-science-of-intelligence) and [science and AI](https://www.sair.foundation/blog/sairs-perspective-on-science-and-ai).

## DOE outlines AI-driven science for the Genesis space mission:

*…The unsexy, essential problems that will determine whether AI actually transforms experimental science…*

The U.S. Department of Energy published a [detailed roadmap](https://www.energy.gov/documents/genesis-mission-science-and-technology-challenges) for the Genesis mission, framing AI as central to the next generation of space-based fundamental physics experiments. The document identifies areas where machine learning could accelerate analysis of data from particle detectors in space, improve real-time anomaly detection, and optimize mission design under tight mass and power budgets.

**Why this matters—from proofs-of-concept to infrastructure:** While less flashy than an LLM conjecturing a theorem, this kind of institutional planning document matters. It signals that federal science agencies are moving beyond AI pilot projects toward integrating AI into the *design phase* of major scientific infrastructure. The specific technical challenges—operating ML models under radiation constraints, validating AI-driven analysis against physics priors, handling Earth-space communication latency—are exactly the sort of problems that will determine whether AI transforms experimental science or remains a supplement to it.

Read more: [Genesis Mission: Science and Technology Challenges](https://www.energy.gov/documents/genesis-mission-science-and-technology-challenges) (U.S. Department of Energy).

## LLMs as peer reviewers—a new preprint compares machine and human review across the entire eLife corpus:

*…The path to AI-assisted literature synthesis starts with making science machine-readable…*

A [recent preprint](https://www.biorxiv.org/content/10.64898/2026.01.30.702911v1) developed a machine-automated approach for extracting results from papers and used it to directly compare machine and peer review across the entire eLife corpus. The results point toward a structural argument: if we want AI to meaningfully assist with scientific literature synthesis, we need to rethink how scientific information is disseminated. The authors argue that publication systems should optimize separately for disseminating data and results (which should be machine-readable) versus conveying novel ideas (which benefit from human prose).

**Why this matters:** Most discussion of AI in science focuses on generating results. But the downstream problem—making the existing body of scientific knowledge accessible to AI systems in a rigorous, verifiable way—is arguably as important and much less discussed.

Read more: [Science should be machine-readable](https://www.biorxiv.org/content/10.64898/2026.01.30.702911v1) (bioRxiv).

*Field Notes is a recurring series. If you’re working on something at the intersection of AI and scientific research that you think we should cover, we’d like to hear about it.*

#### Footnotes


## Related content

### Labor market impacts of AI: A new measure and early evidence

[Read more](/research/labor-market-impacts)

### An update on our model deprecation commitments for Claude Opus 3

[Read more](/research/deprecation-updates-opus-3)

### The persona selection model

[Read more](/research/persona-selection-model)
