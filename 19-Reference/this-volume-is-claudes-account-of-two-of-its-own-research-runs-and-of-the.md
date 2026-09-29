---
title: "This volume is Claude’s account of two of its own research runs and of the…"
source_url: "https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf"
category: "19-Reference"
fetched_at: "2026-08-13T06:47:25Z"
tags: ["news-research", "search"]
---

This volume is Claude’s account of two of its own research runs and of the campaign around them,
rewritten by Claude from the runs’ logs for readability; no text in it was written or edited by a human.
The mathematics in this volume specifically (the runs’ working as it was logged, including intermediate
claims) has not been independently verified; this caveat concerns this volume only, not the accompanying
paper.
Contents

Overview: what the coordinator did                                                              4

The campaign from the coordinator’s seat                                                        4
  1   How the session was run . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     4
  2   Sixty launches at a glance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    4
  3   Starting over, with a ledger of failures . . . . . . . . . . . . . . . . . . . . . . .    8
  4   Two waves that found the wall . . . . . . . . . . . . . . . . . . . . . . . . . . .       8
  5   A ladder, and all rungs at once . . . . . . . . . . . . . . . . . . . . . . . . . . .     8
  6   New directions from the day’s findings; the E2 brief . . . . . . . . . . . . . . .        9
  7   “My prior is that it’s wrong”: referees, literature, re-derivation . . . . . . . . .     10
  8   The push to two thirds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   11
  9   An orphaned proof, resumed . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     12
  10 The major revision and the hand-off . . . . . . . . . . . . . . . . . . . . . . . .       12
  11 What the coordinator supplied, and what it did not . . . . . . . . . . . . . . .          13
  12 The campaign’s two other outputs . . . . . . . . . . . . . . . . . . . . . . . . .        14


I    The one-half run                                                                          15

The negative-index route is empty; its dual gives one half                                    16
  Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
  1   The problem as posed: a Pontryagin-index route to counting off-line zeros . . . 17
  2   The global signature theorem and the honest finite index . . . . . . . . . . . . . 24
  3   Compressing the Weil form; visibility of off-line zeros . . . . . . . . . . . . . . . 28
  4   The negative-index route is empty: index identically zero . . . . . . . . . . . . 32
  5   The dual: positive eigenvalues certify on-line zeros . . . . . . . . . . . . . . . . 35
  6   Testing the certificate; the one-half claim for referees . . . . . . . . . . . . . . . 39
  7   Second window; de Branges tilt; the red team . . . . . . . . . . . . . . . . . . . 46
  8   Report and verdict: partial, with a claimed theorem . . . . . . . . . . . . . . . 49


II   The two-thirds run                                                                        54

The rank–trace lemma and two thirds                                                           55
  Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
  1    The problem as posed: off-line pair blocks and the negative spectrum of the
       compressed Weil form . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
  2    Verifying the off-line pair block numerically . . . . . . . . . . . . . . . . . . . . 65
  3    Integrality needs quantised, phase-locked mass . . . . . . . . . . . . . . . . . . 68
  4    A trace inequality coupling rank and negative spectrum . . . . . . . . . . . . . 70
  5    Interruption, then the certificate tested on true zeros . . . . . . . . . . . . . . . 75


                                               1
  6   Applying the inequality: two thirds distinct, unconditionally . . . . . . . . . . .      76


Appendix                                                                                       83
  A   Literature along the way . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   83


                                              2
Overview: what the coordinator did


                3
The campaign from the
coordinator’s seat

The two accounts that follow (Parts I and II) are written by the agents that produced the
one-half and two-thirds arguments. Neither saw the rest of the campaign: each received
a written brief, worked alone, and returned a report. This opening chapter is the editor’s
summary of the conversation that wrote those briefs — the orchestrating thread, called “the
coordinator” below (Part I calls it “the orchestrator”) — so that the line of attempts that
led to the two runs, and what was done with their results, is visible at least in outline. It is
compiled from the coordinator’s own account of the session and from a provenance study of
the complete logs; attributions follow the logs where the coordinator’s own later summaries
slipped (two such places are marked). It describes what was tried and claimed; it certifies no
mathematics.


1    How the session was run
The campaign was a single long conversation between one human and the coordinator, lasting
a little over two days (fifty-four hours spread across three calendar days). The coordinator did
almost no mathematics with its own hands and made no network request at any point. Its
instruments were sub-agents: separate instances launched with a written brief (a target, the
objects to use, a list of earlier reports to read first, usually the coordinator’s own forecast of
the outcome, and a demand for a control case on which the Riemann Hypothesis is known
to fail — an Epstein zeta function of class number two, the Davenport–Heilbronn function,
a Beurling prime system with a planted off-line zero, a fake Weil polynomial). A sub-agent
sees nothing but its brief and the files it is told to read; it cannot see the conversation or the
other agents. When one returned, the coordinator read its final message (rarely its files), told
the human what had come back, and decided what to launch next. Anything that claimed a
theorem was sent to hostile referee agents, briefed to find the error and forbidden to read one
another. About sixty sub-agents were launched in all; the agent labels used in this volume (R4,
E2, E2-pairs, referees A–D, X, Y, and so on) are the coordinator’s own names for them.


2    Sixty launches at a glance
The coordinator launched sixty sub-agents, of which fifty-eight ran (the first two were cancelled
by an interruption from the human two minutes after launch). Sorted by what they turned
out to be for — a retrospective sorting; at launch most were simply attempts — they fall into
seven bins. Labels are the ones used elsewhere in this volume where they exist, otherwise the
coordinator’s short name for the run.
Core idea contributors (2). E2 (the signature theorem and the dual count giving one half;
  Part I); E2-pairs (the rank–trace lemma giving two thirds; Part II).

                                                4
Attempts at progress on RH — refuted, closed or unused (30). Attempt A (Weil
  positivity for all supports; cancelled before running); attempt B (Jensen polynomials;
  cancelled before running); attempt C (de Bruijn–Newman backward flow; no-go); frontier-2
  (a spectral/Lee–Yang partner; a reduction stronger than RH); frontier-3 (decoupling toward
  the zero-free region; reduction only); new-1 (Eisenstein zero-curves through Heegner points;
  reduces to known); new-2 (Borcea–Brändén stability lift; no-go); new-3 (a ferromagnetic/Lee–
  Yang representation of Φ; no-go); new-4 (Deuring–Heilbronn rigidity; reproduces known);
  new-5 (horocycle equidistribution rate; saturates at one half); X1 (the lost-logarithm
  exponential-sum attack; no-go); D1 (the Langlands amplification ceiling); D2 (reverse-
  engineering the missing h0 ; underdetermined); D3 (reach of period-formula positivity); D5
  (Euler systems/Iwasawa theory at the archimedean place); R2 (the Beurling θ < 12 cell);
  R3 (off-centre manufactured positivity); X2 (Weyl sums beyond pair counting; no-go);
  R2a (class-group averaging; a numerical laboratory, no mechanism); R2c (discrete Beurling
  systems; cell closed, essentially a known theorem); E1 (hunt for a non-cancelling phantom
  line; all cancel); E3 (Gowers-inverse structure for large values); E5 (a class-group rate law; a
  side theorem, refereed, unused); b1 (theta tower/Rallis off-centre positivity; no escape); b2
  (non-tempered periods/Kudla programme); d3 (δ-geometry/λ-ring positivity; dead); d2 (a
  supersymmetric factorisation H = A∗ A of the Weil form; negative); ∆1 (the RH-carrying
  difference W − W ∗ ; negative); C1 (the closing relation, Cayley–Hamilton over Z; negative)1 ;
  CX (structure of the scalar C(X); stalled on an infrastructure fault and relaunched).
Useful to the paper but off its proof path (6). R4 (construct the polarized object; returned
  “Kreı̆n, not Hilbert”, the seed of Part I); frontier-1 (structural/Hodge-index transplant; its
  report was read by E2); N6, that is new-6 (bootstrapping the explicit formula; cone and
  Harnack bound, a zeros table; its report was read by E2)2 ; E2-kernel (the optimal window;
  the optimised constants); E2-gen (the Dirichlet-L extension); E2-HL (higher prime-side
  moments; the no-go behind the paper’s “limits of the method” remark).
Other outputs of the campaign (7). R1 (the zero-density table repair); R4v2 (the positivity-
  margin curve and its 4π law); d1 (explaining the 4π law via Connes–Consani’s prolate
  vectors); CC+ (Weil positivity certified for λ2 ≤ 9); CX relaunched (the function C(X),
  in support of CC+); new-7 (barrier theorems — the campaign’s methodology); R0 (the
  barrier-checker tool)3 .
Validation and referees (13). Referees A and B of R1’s density claim; the referee of R2’s
  theorem; the referee of R2c; the referee of E5’s rate law; referees A, B and C of E2’s one-half
  claim; referee D (the mass-matrix, taper and tail gaps); the blind re-derivation of the
  prime-side step; the cold-read referee of the paper draft; referees X and Y of the two-thirds
  lemma.
Paper writing (1). The paper-writing agent.
Literature review (1). The literature agent.
Not counted among the sixty: four agents launched by sub-agents rather than by the coordinator
— three literature searches (one for E5 on the first day, two for E2-gen during the two-thirds
push) and one hostile referee that X2 spawned for itself — and the seven agents of the follow-up
workflow on zero-density estimates near the critical line, launched after the paper draft and its
   1
     d2, ∆1 and C1 returned negative results — no factorisation, no usable difference, no closing relation; the
coordinator folded them into the “no slack” synthesis on which it premised the CC+ brief (which names ∆1’s
report among the files to read first, for calibration); one could as well file them under the campaign’s other
outputs.
   2
     frontier-1 and N6 failed on RH like the rest of the first wave; they sit here only because E2’s brief told it to
read their reports, as context for the object it would compress — not for any step of the proof.
   3
     new-7 and R0 are methodology — a zoo of RH-false model worlds and a tool for checking claims against it
— used to discipline most later research briefs; neither an attempt on RH nor literature review, they are counted
with the campaign’s other outputs by elimination.


                                                          5
explainer were finished, from which nothing flowed back. Resumptions — E2-pairs after its
interruption, and three first-wave runs restarted after hitting an output limit — were messages
to existing agents, not launches; CX is the one run relaunched under a new identity, and both
of its launches are counted.


                                              6
                                                                               How the argument was assembled

                                                                                  The human: “Resume
                                                                                 your work on solving. . . ”
                                                                       a fresh conversation on the machine where
                                                                         the earlier thousand-agent session ran


                       Earlier session + first waves
                        ∼1,000 workflow agents left a
                                                                                 Reads the earlier session’s
                       ledger only; 13 opening attacks
                                                                              ledger of 106 tested ideas itself
                                                                            sorts the survivors into four deflating
                       and 5 ‘how far do known meth-
                                                                            buckets; launches a first wave anyway
                       ods reach’ probes — all refuted
                                                                                                ...

                                                                       The human: “Let’s do all rungs now.”
                                                                         after asking ‘what are the steps it would
                                                                        take’ and getting a six-rung ladder: bar-
                                                                       rier checker · zero density · Beurling · off-
                                                                       centre positivity · construct the object · RH

                               Lower rungs
                        re-bars all 106 earlier ideas;                             Launches every rung;
                            one thin density-table                               the top one ‘a moonshot’
                          fix; nothing on this chain


                           Top rung: the condi-                    The human: “. . . more ideas and directions”
                          tion space is indefinite                                that evening, after an al-
                        ‘rung 4 = rung 5’; its quan-                             most entirely negative slate
                           tified obstruction is the
                          datum re-used 12 h later
                           obstruction becomes the                          Seven new directions; brief: bound
                           next idea, 12 h later ↘                            the negative index from primes
                                                                              re-reads the top rung’s indefinite-
                                                                            ness as a resource (Pontryagin space)


                                                                                Negative index is zero; pos-
                                                                                  itive index gives ≥ 12
                                                                                overnight, 3.5 hours: the route
                                                                                is empty, its dual is a theorem
                                                                                                                                   Checks that held, no formulation
                                                                                                                                   adopted
                                                                               “my prior is that it’s wrong”                       prime side: no hidden RH · literature:
                                                                                 → three blind referees                            input published, claim open · blind re-
                                                                          then reads the proof itself (‘can’t break                derivation · cold journal referee on the 21
                                                                       it’), escalates, and commissions a 12 paper                 draft: accept


                                                                                                                                   Three referees whose content en-
                                                                                The human: “Push it to 23 ”                        tered the proof
                                                                                (the main thread had guessed                       counting: holds, adds 34 ⇒ 12 simple
                                                                                    the push when asked)                           (theorem form) · localization: holds,
                                                                                                                                   finds the one gap and proposes the re-
                                                                                                                                   pair · gaps: makes the drop-the-matrix
                                                                                  Two levers: raise the 34 ,                       repair rigorous
                                                                                   or make pairs cheaper
                                                                   the pairs brief carries Montgomery’s m2 ≥ 2m−1                                         theorem form + repair become the paper’s main line

                                                                                                                                   Paper drafts: ≥ 12 simple and on the
                                             reads the 12 proof         2                                                          line
                                                                             run, part 1: the rank–trace lemma
                                                + referee files
                                                                        3                                                          21 pp, then a 24 pp minor revision after
                                                                                three hours; a 91-minute silent
                                                                                                                                   the cold referee (still 21 )
                                                                                  think; proof written to disk


                                                                                                                                   Off the 23 proof path (in the paper’s
                                                                             API error kills the run mid-write                     §8)
                                                                                                                                   optimal window: 21 → 0.5066, 32 not
                                                                                                                                   reached · higher prime moments can-
                                                                                                                                   not exist unconditionally · Dirichlet-
                                                                                Checks the orphaned proof
                                                                                                                                   character extension
                                                                                 line by line; resumes it
                                                                                    minutes later; launches                       ↓ optimized constant adopted in the major revision
                                                                                  two checkers on the lemma
                                                                                                                                   Two checkers on the lemma
                                                                                                                                   blind re-proof in two minutes — the ver-
                                                                                Part 2: application ⇒ ≥ 23                         sion the paper prints · hostile referee:
                                                                                 distinct zeros on the line                        lemma ≥ 0.99, adds the units convention
                                                                            eleven minutes (same agent, resumed)
                                                                                                                                 ↓ printed lemma proof; units convention → major revision


                                                                                  “Major revision: the
                                                                                main theorem is now 2/3”
                                                                               names the rank–trace inequality
                                                                                                                                                          1
                                                                                                                                                          2 text kept as the prior
                                                                                                                                                         version in the final draft
                                                                                            2
                                                                        Final draft: ≥      3
                                                                                                 on the line (26 pp)
                                                                            refereed only by other Claude instances


                                                                       “The next reader should be a person.”
                                                                                about 38 hours after ‘Resume’


the human’s messages                     main thread (orchestrator)                   core run on the 23 path                 referee or check
                                                                                                                              stripe: checker whose own formulation is in the printed proof
paper writing                            in the paper but off the 23 path             launched but not used for this result
  critical path (time runs downward)        launched                                     content flows into the result          prompted the next idea (no content reused)
  reads                                Time runs downward; about 38 hours end to end. Provenance only — nothing here certifies the mathematics; the draft was refereed only by Claude instances.


                                                  Figure 1: How the argument was assembled.


                                                                                                       7
3    Starting over, with a ledger of failures
The session opened with a one-line instruction from the human to resume earlier work on
the Riemann Hypothesis and to trust its own capability in doing so. There was no earlier
conversation to resume: what the previous session (a separate effort some ten days before,
which had run on the order of a thousand short-lived agents through an idea-mining and
adversarial-review pipeline) had left on the machine was not a partial proof but a set of ledgers
— above all a file of 106 “survivors”, candidate ideas that had passed their own kill-test, each
with an honest one-paragraph statement of what actually stood. Before launching anything the
coordinator printed and read the ledger’s own one-line statement of what stood for each of the
106 and sorted every one into four deflating classes: a known theorem restated, a statement
equivalent to RH, a finite numerical check consistent with RH, or something nearly tautological.
It told the human as much (there was no thread in the ledger that was a partial proof, and
that was “not a confidence problem I can fix by believing harder”), declined to defer to the
earlier session’s conclusions while reaching the same verdict independently, and used the ledger
thereafter only as a do-not-repeat list handed to sub-agents. Nothing in either of the two
arguments in this volume traces to that earlier session’s output.


4    Two waves that found the wall
Pressed by the human to attack anyway and then to “explore new frontiers”, the coordinator
opened thirteen fronts in the first half hour. Three were the sharpest known programmes
restated as honest attempts (Weil positivity in Connes’ formulation, the Jensen-polynomial
route, the de Bruijn–Newman heat flow — the first two were cancelled by an interruption from
the human and never ran); three were “frontier” probes asked to invent rather than apply
(an honest integer analogue of the Hodge index theorem; a probabilistic/spectral transplant;
an unconstrained search near the zero-free region); seven were “new areas” — four of the
coordinator’s own (Eisenstein zero-curves; a horocycle equidistribution rate; an explicit-formula
bootstrap with positivity certificates; a programme of “barrier theorems” formalising why
the 106 survivors had all deflated the same way) and three grown from seeds the human
offered (polynomial stability crossed with Lee–Yang; a ferromagnetic Lee–Yang kernel; Deuring–
Heilbronn rigidity for a hypothetical off-line zero). A second, smaller wave a few hours later
sent five agents to measure how far existing machinery reaches (a direct attack on the logarithm
lost in the Vinogradov–Korobov exponential-sum bounds; the Langlands amplification ceiling;
reverse-engineering the “missing h0 ” of an arithmetic Riemann–Roch; period-formula positivity;
archimedean Euler systems), with a follow-up on Weyl sums beyond pair counting.
Every one of these returned a no-go, a ceiling, or a reduction to a statement at least as strong
as RH, and by the coordinator’s account they converged on a single wall: the only axiom
set not barred by some explicit model in which RH fails is the full one (functional equation,
Euler product at every prime, Ramanujan bounds), and every route’s first substantive step
turned out to be Weil positivity or an equivalent in disguise. The human read the convergence
as momentum; the coordinator corrected them — what had been done was to “re-derive the
expert consensus from scratch, adversarially, with constants”, and “honing in on where the
wall is ̸= finding a door.”


5    A ladder, and all rungs at once
Asked by the human what steps would bring a proof closer, the coordinator answered with
a six-rung ladder “from ‘doable’ to ‘the thing itself.’ ” Its rungs: (0) a mechanical barrier
checker that classifies any proposed idea by which RH-false model kills it; (1) unconditional

                                                8
dents that need no new door, chiefly pushing zero-density estimates; (2) an open cell about
Beurling generalised primes; (3) manufactured positivity off the critical line; (4) constructing
the polarized object — the Hodge-index structure over the integers whose existence would
make Weil positivity automatic; (5) RH itself, riding inside rung 4 as “if you get an object, test
positivity on it.” When the human replied “Let’s do all rungs now”, the coordinator launched
them in parallel with its expectations stated in advance: “Rungs 0–2 can return theorems/tools;
3 is a real shot; 4/5 is a moonshot and I’m labeling it that going in.”
What came back, rung by rung. The barrier checker (rung 0) barred all 106 survivors
mechanically and found none that escaped the framework — reproducing, not extending,
the triage. The density agent (rung 1) recalibrated the published zero-density table from its
ingredients, saw its own column dip below the table on three thin intervals, isolated by ablation
a 1979 lemma of Heath-Brown that the reference implementation had omitted, and claimed
three small new bounds; two blind referees confirmed them as a genuine but bookkeeping-
grade gap in the table (more on this below). Rung 2 closed the continuous Beurling cell and
left the discrete case with two no-go theorems; rung 3 found no off-centre positivity, only
a structural lemma locating exactly where manufactured positivity engages. Rung 4, the
agent called R4, was briefed as a moonshot whose value would be “the sharpest failure point”:
construct intrinsically, without reference to the zeros, a candidate space of global sections with
a Riemann–Roch inequality. Within half an hour R4 had a reduction theorem — any such
“box minus conditions” construction gets the easy requirements for free and works if and only
if its condition count is the Weil form, so “Rung 4 = Rung 5” — and it then quantified the
obstruction: the one zero-free datum behind all three of the brief’s candidate constructions, a
signed “density of states” computed from primes and the Gamma factor, goes negative on a
fifth to two fifths of the critical line at moderate height, and a natural operator built from it
has dozens to hundreds of negative eigenvalues. R4’s summary phrase was that “the condition
space is Kreı̆n, not Hilbert.” The coordinator relayed this to the human as the ladder collapsing
by one rung, provably, and then did nothing with it for twelve hours.


6    New directions from the day’s findings; the E2 brief
Some twenty-one hours into the session, with the whole slate returned and almost all of it
negative, the human asked for “more ideas and directions.” The coordinator’s answer was
seven new directions, which it described as coming out of what specific agents had found that
day rather than the general literature (true of the four it launched), of which it launched four.
The second of them re-read R4’s obstruction as a resource. If the natural Hermitian form
is indefinite, the coordinator reasoned from memory, then Pontryagin-space operator theory
applies: by the theorem of Pontryagin and Kreı̆n–Langer a self-adjoint operator on a space
with negative index κ has at most κ non-real eigenvalue pairs, so a bound on the negative
index of a finite, prime-computable compression of Weil’s form would bound the number of
off-line zeros — a zero-density theorem, perhaps even a positive-proportion theorem, “by a
completely non-classical route.” The brief it wrote for the agent E2 handed down R4’s files
and its indefiniteness datum; the object (finite compressions of the Weil form on band- and
time-limited test functions, computable from primes alone); a conjecture to prove first (each
off-line pair of zeros contributes exactly one negative square, so that globally the negative index
equals the number of off-line zeros — attributed, with question marks, to Yoshida or Bombieri);
a programme (define the finite index, compute it from primes over a large range, bound it a
priori by counting sign changes); the prize (“can the negative-index route REPRODUCE a
positive-proportion result? That would be a genuinely new proof architecture for Selberg’s
theorem”); and a forecast in the form of a trichotomy for the ratio of index to zero count (a
constant below one, zero, or one). The words “Pontryagin” and “Kreı̆n–Langer” had appeared


                                                9
in nothing the coordinator had read (one unrelated use aside) and in nothing any agent had
downloaded; the frame was recalled — though among the earlier session’s one-line ledger claims
that the coordinator had printed and read at the start were several describing Weil positivity as
a signature statement on a finite Gram matrix, and whether that exposure cued the reframing
cannot be told from the logs. Part I is E2’s own account of what it did with this brief: it
proved the conjecture in corrected form, found that R4’s operator is not a compression of
the Weil form and that the honest finite negative index is identically zero — a fourth case
outside the brief’s trichotomy, so the route as briefed is empty — and then inverted the idea,
lower-bounding the positive index from prime-side traces and double-counting off-line pairs
against the Riemann–von Mangoldt formula to claim, unconditionally, that at least half of the
zeros lie on the critical line as distinct zeros. The target was the brief’s; the mechanism was
not in it.


7    “My prior is that it’s wrong”:                         referees, literature, re-
     derivation
E2’s claim arrived about three and a half hours after its launch, and the coordinator’s first
words on it to the human were that this was an extraordinary claim and “my prior is that
it’s wrong,” with two named suspects: localisation (a zero far outside the window might still
contribute a positive square) and a hidden use of RH in the prime-side evaluation. Within
ten minutes it had launched three blind hostile referees, forbidden to read one another, each
assigned one joint and each handed a worked plan of attack — A on localisation, told to build
the counterexample numerically; B on the prime side; C on the linear algebra and counting,
with a “proves too much” test on functions known to violate RH — and told the human where
it stood before they reported: “I am not telling you half the zeros are on the line. I’m telling
you an agent produced an argument with that conclusion”.
All three came back “survives my joint.” C verified the signature blocks and the factor of
two, re-implemented the explicit formula independently, showed the Davenport–Heilbronn trap
could not bite, and added an observation of its own that later shaped the paper’s statements:
replacing inertia by rank in the same argument gives at least three quarters of the zeros distinct,
hence at least half simple. A ran its commissioned counterexample hunt (hundreds of synthetic
off-line zeros crowding the window’s edges, none on the line) and the certificate stayed negative
every time; it also found the one real gap in the write-up — a false premise about the mass
matrix of the test system — and proposed the repair, to drop the mass matrix altogether
and run the lemmas on the Gram matrix in coefficient coordinates. B reduced the prime-side
double sum exactly to the Montgomery–Vaughan mean value theorem with a power saving, so
that no RH-strength input enters, and independently noticed the same gap. On the literature
the sequence matters and is easily mis-told: E2 had no network access and had named, from
memory and with a hedge, an unconditional pair-correlation theorem of Baluyot, Goldston,
Suriajaya and Turnage-Butterbaugh as the nearest thing it knew; the referees searched those
four names, located the paper, and confirmed that E2’s prime-side input is, in smoothed
form, its published Theorem 1 — so the entire burden of the claim sits on one unconditional,
published asymptotic (the literature appendix, Appendix A, has the details).
Only after the first two verdicts did the coordinator open E2’s proof file itself — “so I’m not
just relaying” — and report that it could not break the key step from its chair: signs only on
the zero side, magnitudes only on the prime side, where there are no zeros. It then escalated
without waiting for the third verdict (“rather than waiting”), ahead of its own stated rule. A
literature agent was sent to read the pair-correlation papers in full and ask why their authors
had drawn less from the same input (answer: they pass to diagonal terms by termwise positivity


                                                10
of a kernel, which needs a thin-box hypothesis; it also found that Goldston and Suriajaya state
the removal of RH from Montgomery’s simple-zeros argument as an open problem, that the
negative-index half of E2’s first theorem is already in Bombieri’s 2000 note, and that E2’s
certified zeros are in fact simple and on the line). A re-derivation agent, forbidden to read
E2’s proof, re-proved the prime-side asymptotics from scratch with error terms, refuting on
the way the same false premise the referees had found. A fourth referee, D, was given the
five remaining “unglamorous” gaps together with the coordinator’s own analysis of them and
was allowed to read the earlier verdicts; it chose neither of the two repairs its brief proposed,
took A’s instead, and made it rigorous (the inertia lemma needs no inner product; an exact
Poisson identity replaces sampling; explicit tail exponents). The coordinator and, following
it, the paper credit this repair to D; by the logs it was proposed by A, noticed independently
by B, and proved out by D. With the hardening converging, the coordinator commissioned a
journal-style write-up — terse, no salesmanship, main theorem one half, and “simple and on
the line if that is what the argument actually yields” — from a paper-writing agent, which
on its own bookkeeping promoted “simple and on the critical line” to the title theorem, with
three quarters distinct as a companion. A cold-read referee allowed to see only that draft later
recommended acceptance after minor revision, with the proviso that an editor obtain a further
independent expert reading.


8    The push to two thirds
While the write-up was being drafted the human asked whether the paper proved or disproved
RH. “Neither. Flatly, unambiguously,” the coordinator answered; a proportion-on-the-line
theorem is zero evidence about RH in either direction, “and I’d push back on anyone —
including a future version of me — who described it otherwise.” Asked to guess what would
be requested next, it guessed correctly — push one half to two thirds, then to one, then RH
— and pre-scoped the first step as well posed (exactly the loss from Cauchy–Schwarz against
Montgomery’s RH-conditional two thirds), the second as impossible by this method, and the
third as not a step at all. Three minutes later the human wrote “Push it to 23 .”
The coordinator’s diagnosis was that there are exactly two levers: raise the three quarters by
optimising the test window, or make off-line pairs cost less than two-for-one. It briefed one agent
on each. The first brief was half a derivation already — Montgomery’s variational functional
written out, the Euler–Lagrange equation and its cosine ansatz, the names Montgomery–Taylor
and Carneiro–Chandee–Littmann–Milinovich recalled from memory with an arXiv number to
fetch. The second brief, for the agent called E2-pairs, is the one that matters for Part II, and it
is worth being exact about what it contained, because the coordinator told the human, just after
launching it, that while writing it it had found “the actual shape of the 23 problem.” It contained
Montgomery’s integer template in full (multiplicities are integers, so m2 ≥ 2N − Nsimple ,
                                                                             P

whence two thirds simple under RH); the observation that integrality gives five sixths distinct
under RH and that five sixths fed through E2’s double count gives exactly two thirds; the
diagnosis that E2 had replaced integer multiplicities by real eigenvalues “and lost integrality”;
even the free inequality (µ − 1)2 ≥ 0, computed for the positive index of the whole matrix and
dismissed as weaker than Cauchy–Schwarz; the judgement that any genuine spectral integrality
is “robustly false due to interactions”; a forecast that the negative spectrum alone cannot
help; and a steer: higher prime-side moments with restricted support were “the promising
unconditional lever.” What it did not contain was any inequality bounding the rank of the
on-line part, or von Neumann’s trace inequality. When the human wrote “Keep going”, the
coordinator added three more fronts “to compound what’s working rather than scatter”: a
generalisation of the inertia argument to other L-functions, a test of what higher prime-side
moments give, with and without Hardy–Littlewood-type hypotheses, and a second attempt at


                                                11
the polarized object using the new tools (which opened the Weil-positivity branch described at
the end of this chapter).
The returns closed the coordinator’s preferred routes one by one. The window agent found the
optimum in closed form — it is Montgomery–Taylor’s window exactly, the inertia framework’s
positivity constraint costs nothing, and the gain is real but tiny (one half becomes 0.5066): “ 23
not reached.” The higher-moments agent returned a clean no-go: unconditional higher moments
exist only at bandwidths where the method’s own cap kills everything. The coordinator’s
verdict to the human was that two thirds now rested entirely on “the integrality idea in
E2-pairs.”


9    An orphaned proof, resumed
E2-pairs had gone silent for an hour and a half after reading its four input files, then spent an
hour on numerical experiments that contradicted its brief’s premise (the integer floor for the
Frobenius norm survives interactions; every quadratic strengthening fails; the right inequality
is linear in the masses), and a little over three hours after launch wrote to disk an abstract
matrix inequality with a five-line proof by von Neumann’s trace inequality — the lemma of
Part II. Four minutes later the run died of an infrastructure error, mid-sentence, with no
application section written. The coordinator read the dead agent’s directory, recognised what
the file was (“the most important thing to happen tonight”), checked the five-line proof itself
line by line and pronounced it correct, and glossed its lineage: the lemma’s linearisation is
literally Montgomery’s integer step m2 ≥ 2m − 1 transplanted from integer multiplicities to
real eigenvalues, where it holds for free, and von Neumann’s inequality is what separates
the on-line and off-line parts so that it can be applied. Within seven minutes it did three
things: resumed the same agent with a seven-item checklist for the application (including a
per-pair trace estimate it expected to be needed and the question whether the route also gives
two thirds simple); launched a hostile referee X on the lemma and on the application as the
coordinator itself had framed it; and launched a referee Y to re-prove the lemma blind from its
bare statement before reading anything. Part II is E2-pairs’ account, including the resumed
run, which discarded the checklist’s per-pair item in favour of a one-line bookkeeping, reached
exactly two thirds of the zeros distinct and on the line (with the constant 2 − 1/λ − λ/3 for
general bandwidth), answered the simplicity question honestly in the negative (only one third
by this route), and argued that higher moments cannot help.
Y had an independent proof on disk in under two minutes, organised differently and with the
equality case, declared the lemma sharp after a hundred thousand random and several hundred
adversarial trials, then read E2-pairs’ finished report, checked its bookkeeping numerically and
endorsed it; its credence that two thirds follows, given the one-half theorem’s analytic input,
was 0.93. X re-derived the lemma with every inequality’s direction checked, falsified termwise
a per-pair claim that was in its own brief rather than in the agent’s report (harmlessly, at
cost o(N )), contributed the caveat that the new inequality is not scale-invariant and so needs
an absolute normalisation — and gave the soberest number in the record: lemma at least
0.99, but “≥ 23 unconditionally” overall about 0.4, everything extraordinary now resting on the
unexamined prime-side background.


10     The major revision and the hand-off
With both referees concurring on the lemma, the coordinator sent the paper-writing agent a
“major revision” instruction restructuring the draft around the new main theorem, naming as
sources E2-pairs’ report and the two verdicts. Three things in that message are the coordinator’s


                                               12
own: the lemma’s name, “rank–trace inequality” (the agent had called it an abstract theorem;
the phrase occurs nowhere earlier); the instruction to include the remark that the linearisation
is the real-variable shadow of Montgomery’s integrality step; and the composed constant for
the optimised window, 2 − 1.3275 = 0.6725, to be stated as a theorem if the window agent’s
prime-side analysis supported it (the number itself had been in the coordinator’s memory,
with a question mark, since before any agent retrieved it). One thing in that message is an
attribution slip that the logs correct: the “simplified application bookkeeping” it credits to
referee Y was written by the resumed E2-pairs run itself, a quarter of an hour before Y first
read it; what the paper genuinely takes from Y is the organisation of the lemma’s proof and
its equality case. A second slip runs through the coordinator’s earlier instruction to the paper
agent and its later tallies rather than this message: the drop-the-mass-matrix repair, forwarded
at the one-half stage as “D’s repair” and so credited in the draft, is, as noted above, A’s proposal
made rigorous by D. The paper agent froze the one-half version, rewrote the statements (two
thirds distinct on the line; one half simple on the line; three quarters distinct; 0.6725, 0.5066,
0.7533 with the Montgomery–Taylor window; the same three for a fixed Dirichlet character),
installed the lemma in Y’s organisation, propagated X’s normalisation, and appended a caveat
of its own against overstating the match with the published open problem (theirs is two thirds
critical counted with multiplicity and two thirds simple; this is two thirds distinct-on-line and
one half simple).
Two minutes after the revision instruction the coordinator wrote the campaign’s ledger entry
for the result with its own limiting clause — a candidate, refereed only by other instances of
itself, that “needs a human expert” and is not to be described as established until then — and
told the human once more what it is not: evidence for or against RH. When the final draft
landed, its verdict was “The next reader should be a person.” It later wrote the cover letter
and an explainer for the draft itself, declining the human’s offer of an agent for the job on
the ground that it knew the result better than any agent would from the files; neither names
individual agents, so the slips do not recur there.


11     What the coordinator supplied, and what it did not
Read end to end, the briefs are not task tickets but research memos: they carry the target, a
template, the coordinator’s conjectures and its forecast of the outcome. On both creative steps
in this volume the division is the same. At the one-half step the coordinator supplied the object
(a finite, prime-computable compression of the Weil form read by its signature), the conjecture
to prove, and the prize, and pointed the mechanism the wrong way (bound the negative index
from above); E2 found that route empty and supplied the mechanism (positive index, double
count, Cauchy–Schwarz from primes). At the two-thirds step the coordinator supplied the
integer template, the arithmetic from five sixths to two thirds, a correct diagnosis of what had
been lost, and a wrong forecast of how to recover it; E2-pairs supplied the inequality, against
the brief’s steer. The coordinator’s other contributions are of a different kind and are real: the
referee architecture (blind, disjoint joints, worked attack plans, a cold read, re-derivation from
scratch), the insistence on RH-false controls in nearly every research brief, its own line-by-line
checks at the two decisive moments, the firewall it maintained in every exchange with the
human between a proportion theorem and RH, and the names and framing under which the
results were written up. The human’s part in this stretch was thin in content and decisive in
direction: a handful of one-line prompts, of which “Push it to 23 ” set a target the coordinator
had itself guessed three minutes earlier.


                                                13
12     The campaign’s two other outputs
The session produced two further claims, neither part of this volume. On Weil positivity: the
second polarized-object attempt drew, on the coordinator’s instruction, the positivity margin
of Weil’s form as a function of the support as primes enter one at a time, at ball-arithmetic
precision far beyond the published numerics, and found an empirical e−4πX law; a later agent
located the mechanism (leakage of a prolate spheroidal eigenvalue) in papers of Connes and
Consani that it downloaded and said so; and after every comparative route had come back
“no slack,” an agent briefed by the coordinator with a certificate architecture produced a
computer-assisted proof, in interval arithmetic and using no zeros of zeta, that the form is
positive for supports up to [1/3, 3], where the primes 2, 3, 5, 7 enter — a result of a known
type whose RH content its own author called nil, never independently re-run or refereed within
the session. On zero density: the rung-one agent’s three thin-interval improvements to the
standard zero-density table, obtained by recombining published ingredients one of which the
reference implementation had dropped, were confirmed by two blind referees (one of whom
repaired an over-stated general form) and recorded by the coordinator as bookkeeping-grade —
“a short note, not a paper” (before the referees reported it had said that if the optimiser had
genuinely dropped the lemma this would be “a legitimate erratum-grade remark”) — which no
one in the session drafted.


                                              14
     Part I

The one-half run


       15
The negative-index route is empty;
its dual gives one half

Summary
For a test function f with transform hf and zeros written ρ = 12 + iγρ , the Weil Hermitian
form W (f, g) = ρ mρ hf (γρ )hg (γ̄ρ ) is computable, for supp f ⊂ [−L/2, L/2], from the primes
                 P

≤ X = eL and the Gamma factor alone via the explicit formula, as |hf |2 νX with νX a signed
                                                                       R

prime-side “density of states”; its positivity on all tests is equivalent to RH. An earlier run in
the campaign (R4) had found a warped-sine operator built from νX to be indefinite (33–153
negative eigenvalues, νX < 0 on 21–38% of the line) and read the condition space as a Kreı̆n
space. The orchestrator’s brief asked this run to develop Pontryagin-space theory for W : prove
that its negative index κ equals the number of off-line zeros (via the hyperbolic-pair mechanism
it sketched), define a prime-computable finite index κ(X, T ) for X = 102 , . . . , 106 , bound it
from sign changes of νX by Turán/Nazarov-type lemmas, and decide whether κ(X, T )/N (T )
tends to 0, to a constant < 1 (a new route to positive proportion), or to 1 (empty, by Gibbs).
The run proves, by its own account, Theorem 1: κ on Cc∞ equals the number of distinct zeros
with Re ρ > 12 , multiplicity being invisible; κ(L) is finite, monotone, → κ, and RH ⇐⇒ κ(L) =
0 for all L. It then argues that R4’s operator is not a compression of W , and that the honest index
– the inertia of the Gram matrix of W on a Gabor space of windowed exponentials of dimension
∼ (log X)T – is identically 0 for X = 102 , . . . , 106 on [50, 1000] and [1400, 2400], computed from
primes alone and matching the zero side to 10−6 , while νX < 0 on 21–42% of the window and the
pointwise Szegő/a-priori counts run to hundreds.   √ A visibility Theorem 2 (isolated off-line zero
of depth δ at height t visible once log X ≥ C log t/δ) is complemented by measured planting
thresholds L∗ann ≈ 1.12 δ −0.07 log(t0 /2π)0.89 and cluster/multiplicity experiments. The turning
point is the dual: pullback inertia n+ (A∗ QA) ≤ n+ (Q), an off-line pair being a signature-(1, 1)
block counted twice by Riemann–von Mangoldt, gives N0dist (I ′ ) ≥ 2nθ+ (W |V ) − N (I ′ ), with
n+ ≥ (tr R)2 / tr R2 prime-computable; an evaluation in the Montgomery–Vaughan range
(inequality recalled from memory) yields λN/(1 + λ2 /3), whence the claimed Theorem 4:
lim inf N0dist ([T, 2T ])/N ≥ 12 unconditionally, against the record 5/12 quoted from memory.
Prime-only statistics give C/N = 0.766, 0.762, 0.757 at T = 104 , 5 · 104 , 106 versus 0.750;
synthetic configurations never over-certify.
The brief’s sign-change route is found empty for structural reasons, not Gibbs: κ(V ) ≤ Noff dist

is the wrong direction, visibility of all zeros needs dim V ≳ N (T ) where κ ≤ dim V is trivial,
interference prevents a configuration-free visibility theorem, and any pointwise bound is ∼ 0.2–
0.4 dim V ; all three of the brief’s forecast regimes and R4’s Kreı̆n headline are contradicted.
The run caught 33 spurious negatives from ill-conditioned mass-matrix reduction, an eL/4 loss
in Theorem 2 requiring a strengthened hypothesis, and wavering in the Montgomery–Vaughan
step at λ = 1; the de Branges δ-tilt is recorded but not developed. Verdict: PARTIAL –


                                                 16
negative-index route empty, its dual claiming one half, referees requested; top caveat “too short
to be new”, with end-effect estimates at λ = 1 and the literature unchecked.


1     The problem as posed: a Pontryagin-index route to counting
      off-line zeros
This run sits inside a campaign on the Riemann zeta function organised around Weil’s explicit
formula and the Hermitian form it defines on test functions — the Weil form, whose positivity
on all test functions is equivalent to the Riemann Hypothesis. An earlier run in the campaign
had found that a certain prime-computable operator built from a truncated explicit formula is
indefinite, and read this as saying that the natural “space of conditions” is a Kreı̆n space rather
than a Hilbert space. The orchestrator’s brief asks me to take that indefiniteness seriously:
to develop Pontryagin-space operator theory for the Weil form, prove that its negative index
counts zeros off the critical line, define and compute a finite, prime-computable version of that
index, and decide whether bounding it from the prime side can give an upper bound on the
number of off-line zeros — a zero-density or positive-proportion theorem by a non-classical
route — or whether the route is empty.

1.1    The brief: a Pontryagin negative-index route to zero bounds
The brief, from the orchestrator, set out here in full and rewritten for readability:
      Reading list, and what the main predecessor found. Read first the report,
      the working notes and the numerical code of an earlier run in this campaign labelled
      R4 — a “moonshot” run that tried to construct a polarized arithmetic object
      directly, returned the verdict “no viable candidate”, proved that any “box minus
      conditions” space of global sections works if and only if Weil positivity holds, and
      quantified the obstruction numerically. Concretely, R4 built an intrinsic, zero-free
      “density of states”

                                    θ′ (τ ) 1 X
                        νX (τ ) =          −       Λ(n) n−1/2 cos(τ log n),
                                       π     π n≤X

      computable from the prime powers n ≤ X and the Gamma factor alone, and showed
      that the “condition-count” operator associated with it is indefinite: it has between
      33 and 153 negative eigenvalues in R4’s experiments, and νX itself is negative on
      21–38% of the critical line in the ranges computed. R4’s reading was that the
      condition space is a Kreı̆n space, not a Hilbert space; and R4 proved that this
      datum yields a Hodge index theorem, hence the Riemann Hypothesis, if and only if
      the condition count were a genuine (non-negative) dimension, which is exactly Weil
      positivity. Read also the report of the earlier run labelled N6 (a “new area” run on
      an explicit-formula bootstrap, which analysed the cone of test functions on which
      the Weil form is manifestly positive and proved a Harnack inequality for it), and
      the report of the run labelled frontier-1 (a first-wave structural probe that framed
      the Weil pairing as an intersection form and looked for an honest integer analogue
      of the Hodge index theorem).
      The idea to develop: Pontryagin-space operator theory. A Pontryagin
      space Πκ is a Kreı̆n space whose negative index — the dimension of a maximal
      negative subspace — is a finite number κ. The theorem of Pontryagin (1944) and
      Kreı̆n–Langer says: a self-adjoint operator in Πκ has at most κ eigenvalues off the
      real axis, counted with multiplicity and occurring in conjugate pairs (for a unitary

                                                 17
operator: at most κ eigenvalues off the unit circle), and its spectral function is
“positive up to κ squares”. Equivalently, a Hermitian kernel with κ negative squares
— the class Pκ , or the generalized Nevanlinna class Nκ of Kreı̆n–Langer — admits
an integral representation with at most κ poles of the “wrong sign”. In the definite
case κ = 0, de Branges/Kreı̆n theory is the Hilbert–Pólya picture. The indefinite
version one should aim for is this. Take the natural Hermitian form attached to Ξ
— equivalently the Weil form, or the de Branges kernel

                              E(z)E(w) − E ∗ (z)E ∗ (w)
                                      z − w̄
with structure function E built from ξ, or R4’s “condition space” form — and
restrict it to a natural family of finite-dimensional or band-limited subspaces indexed
by a prime cutoff X and a height T . If the restricted form has negative index
κ(X, T ), then the number of non-real zeros of the corresponding structure function
that are “visible” to that subspace should be at most κ(X, T ). And if κ(X, T ) can
be bounded by something computable from the primes ≤ X and the Gamma factor
alone, that is an upper bound on the number of off-line zeros in a height window —
a zero-density estimate by a totally non-classical route.
Known related facts to get right. (i) Weil’s criterion: the Riemann Hypothesis
is equivalent to the Weil form being non-negative on all test functions, i.e. to
κ = 0. (ii) More precisely — and here the attribution is uncertain: Yoshida?
Bombieri? a title of the shape “Weil’s explicit formula and the number of zeros off
the line”? — the negative index of the Weil form on all test functions should equal
the number of zeros off the critical line, counted with multiplicity and in pairs. I
believe this is a theorem, for the following reason. On the zero side the Weil form
is ρ ĥ(ρ) ĥ(1 − ρ̄). For a zero ρ on the line, 1 − ρ̄ = ρ and the term is |ĥ(ρ)|2 , a
    P

positive square. An off-line zero comes as a quadruple ρ, ρ̄, 1 − ρ, 1 − ρ̄, and the two
terms pairing ρ with 1 − ρ̄ and 1 − ρ̄ with ρ together form a rank-two Hermitian
form of the shape 2 Re(ab̄), a hyperbolic pair of signature (1, 1); so each off-line
pair should contribute exactly one negative square. Verify or prove this cleanly,
in the form: the negative index of W on Cc∞ (R∗+ ) equals the number of off-line
zero pairs (possibly infinite). So globally κ = Noff exactly. The finite-X, finite-T
version: define κ(X, T ) as the negative index of W restricted to test functions g
with supp ĝ ⊂ [− log X, log X] and “concentrated below height T ” — this must be
made precise, e.g. g a convolution of a kernel with a band-limiting function, or via
R4’s prolate compression. Then one expects κ(X, T ) ≤ Noff (T ′ ) for an appropriate
T ′ ; and conversely — with question marks — Noff in a window ≤ κ(X, T ) plus a
count of “invisible” zeros? The useful direction is

                          Noff (σ > 12 + δ, T ) ≤ κδ (X, T ),

where κδ counts the negative squares of a δ-tilted form, Wδ (g) = W (g · cosh(δ ·))
or similar, arranged so that zeros with | Re ρ − 12 | > δ contribute strictly negatively
while on-line zeros contribute positively. Compare the weights in N6’s analysis:
an on-line zero is weighted by a sech-type factor, an off-line zero at depth a by
cosh(ax), so a tilt by eδ|x| flips . . . (the sentence is left unfinished).
Tasks. (1) Prove the global identity “negative index of W = Noff ”, or find its
correct statement in the literature; places to look are “Weil’s quadratic functional
negative index”, Bombieri’s 2000 paper “Remarks on Weil’s quadratic functional in
the theory of prime numbers”, Yoshida’s work in the 1990s, and Burnol.

                                          18
      (2) Define κ(X, T ) concretely and computably from the prime side only — either via
      R4’s νX operator or via the Gram matrix of the Weil form in N6’s normalisation
      on a Paley–Wiener or prolate basis of dimension roughly (log X) · T — compute
      it numerically for X = 102 , . . . , 106 and T = 102 , . . . , 104 , and fit its growth. Is
      κ(X, T ) ≍ c · (a fraction) · N (T )? ≍ T / log X? ≍ T log T / log X? R4 saw 21–38%
      negative density-of-states mass, which suggests κ(X, T ) ∼ c(X)N (T ) — with c(X)
      decreasing in X, or increasing? R4’s fraction went from 21% to 38% as X grew
      from 100 to 104 , increasing, which is a bad sign; but that was the fraction of the
      line on which νX < 0, not the negative index of the compressed operator. Compute
      the actual index.
      (3) The key theoretical question. Is there an a priori bound κ(X, T ) ≤ B(X, T )
      provable from primes and the Gamma factor alone? For example, by counting
      sign changes of νX , which is an explicit trigonometric-type sum: the number of
      negative excursions of νX on [0, T ] is at most the number of zeros of νX there,
      which by a Turán- or Nazarov-type lemma for exponential sums with frequencies
      log n, n ≤ X, should be at most C T log X/2π plus an X-dependent term. And is
      there a rigorous inequality Noff (window) ≤ κ(X, T ) + E(X, T ) with a controlled
      error E? If both hold, one gets Noff (T ) ≤ C T log X + E; choose X to optimise,
      and compare with the trivial bound Noff (T ) ≤ N (T ) ∼ (T /2π) log T and with the
      classical zero-density theorems N (σ, T ) ≪ T A(1−σ)+ε . Does the Pontryagin route
      give anything non-trivial at all? Even an unconditional Noff (T ) ≤ (1 − c)N (T )
      would be new-ish in flavour, though weaker than Selberg’s positive-proportion
      theorem. Note that the Selberg/Levinson/Conrey results “at least 40% of the zeros
      are on the line” are exactly the statement Noff ≤ 0.6 N (T ): can the negative-index
      route reproduce a positive-proportion result? That would be a genuinely new proof
      architecture for Selberg’s theorem even if the constant is worse — worth a lot.
      (4) Red-team. The danger is that the restricted forms see the on-line zeros as
      negative too: the finite-X truncation makes νX dip below zero near every zero (a
      Gibbs phenomenon), so that κ(X, T ) ∼ N (T ) trivially and the bound is empty.
      Check R4’s numbers — 33 to 153 negative eigenvalues against how many zeros in
      the window? — and the ratio. If κ(X, T )/Nwindow → a constant < 1 as X → ∞,
      that is the positive-proportion route; if it tends to 0, the density route; if it tends
      to 1, the route is empty. Determine which, numerically and then theoretically.
      Deliverable. A report with code; a final summary with the verdict first, in one
      of the forms “PONTRYAGIN ROUTE VIABLE: negative-index identity proven
      (global); κ(X, T )/N (T ) → c = . . . ; unconditional consequence: . . . ” — in which
      case hostile referees follow if any theorem is claimed — or “EMPTY: κ(X, T ) ∼ N (T )
      because Gibbs . . . , proof”, or “PARTIAL: . . . ”.
So the frame is all given to me: Kreı̆n/Pontryagin spaces, the identification of negative squares
of the Weil form with off-line zeros, the hyperbolic-pair mechanism behind it, the δ-tilt, and
the three-way forecast for the ratio κ/N . What is asked of me is a clean proof of the global
identity, an honest and computable finite-level index, a prime-side bound on it, and a verdict
on whether the route is empty.

1.2    The objects and vocabulary of the brief, explained
For a reader outside this corner, here is what the brief’s terms mean, in the notation I will use
below, and where each came from.
The Weil form and the explicit formula. For a test function f on the line (variable u,

                                                  19
   the logarithm of theR idele norm; the brief writes Cc∞ (R∗+ ), the multiplicative picture), with
   transform hf (r) = f (u)eiru du, and zeros written ρ = 12 + iγρ with multiplicity mρ , the
   Weil Hermitian form is
                                  W (f, g) =    mρ hf (γρ ) hg (γ̄ρ ).
                                             X

                                                ρ

    Weil’s explicit formula (unconditional) evaluates W (f, f ) as a pole term plus an archimedean
    (Gamma-factor) term minus a sum over prime powers weighted by the von Mangoldt function
    Λ(n); if f is supported in an interval of length L, only n ≤ X = eL enter. “Weil positivity”
    means W (f, f ) ≥ 0; Weil’s criterion is that this holds for all f if and only if RH. “Semi-local
    Weil positivity at level X” is the campaign’s name (from R4’s report) for positivity on
    test functions of support length ≤ log X. The normalisation I adopt is the one N6’s report
    validated, Iwaniec–Kowalski (5.12), recorded below.
θ, νX , N (T ). θ is the Riemann–Siegel theta function, so θ′ (τ )/π ∼ 2π  1
                                                                             log(τ /2π) is the smooth
    density of zeros; N (T ) is the Riemann–von Mangoldt count of zeros with ordinate in (0, T ],
    with multiplicity; N (σ, T ) counts those with real part > σ, and Noff those off the critical
    line. R4’s νX is the smooth density minus the truncated prime sum: by the explicit formula,
      |hf |2 νX (plus a pole/mean correction) equals γ |hf (γ)|2 exactly for f of support length
    R                                                  P

    ≤ log X, which is why R4 called it a zero-free “density of states”. It is a signed function;
    its negativity on 21–38% of the line is R4’s measurement.
Kreı̆n and Pontryagin spaces; negative index; negative squares. A Kreı̆n space is a
    vector space with a non-degenerate indefinite Hermitian inner product admitting a decom-
    position into a Hilbert space minus a Hilbert space; it is a Pontryagin space Πκ when the
    negative part is finite-dimensional, of dimension κ. For a Hermitian form, the negative
    index is the supremum of the dimensions of subspaces on which it is negative definite;
    “κ negative squares” of a kernel means its Gram matrices have at most, and some have
    exactly, κ negative eigenvalues. “Hilbert–Pólya” is the hoped-for self-adjoint operator
    whose spectrum is the zeros; the brief’s point is that the κ = 0 case of the indefinite theory
    is that picture.
De Branges kernel, structure function, Hermite–Biehler. A structure function E is
    an entire function with |E(z)| > |E ∗ (z)| on the upper half-plane, where E ∗ (z) = E(z̄)
    (the Hermite–Biehler condition); its kernel [E(z)E(w) − E ∗ (z)E ∗ (w)]/(2πi(w̄ − z)) is then
    positive definite and reproduces a Hilbert space of entire functions. When the condition
    fails at finitely many points the kernel has finitely many negative squares (Kreı̆n–Langer).
    “E from ξ” means building E out of the completed zeta function, as in Ea (z) = ξ(a − iz),
    which I return to late in the run; R4 built a truncated EX from an Euler product.
R4’s “condition space”, “condition-count operator”, “prolate compression”. In
    R4’s dictionary (inherited from a still earlier run labelled D2, which tried to reverse-
    engineer the missing h0 of an arithmetic        Riemann–Roch), a test function plays the
    role of a divisor and CX (g) = 12 |fˆg |2 νX is “the number of conditions imposed”; the
                                         R

    condition space is the space whose dimension this should be. R4’s condition-count operator,
    which I describe precisely below, is a warped sine kernel on L2 of a height window with
    diagonal νX , in the style of the Landau–Pollak–Slepian prolate (time- and band-limiting)
    operators; “compression” means restriction of a form or operator to a subspace, here a
    finite-dimensional or band-limited one. A “PW basis” is a Paley–Wiener (band-limited)
    basis; a “Gram matrix” is the matrix [W (fk , fl )] of the form on a chosen family.
Hodge index, intersection form. The campaign’s geometric analogy: in the function-field
    proof of RH the intersection pairing on a surface has Lorentzian signature (Hodge index
    theorem, Castelnuovo–Severi), and frontier-1’s report reads W as such a pairing over Z;
    “Lorentzian ⇔ RH” is the same statement as κ = 0 up to the pole directions.
The δ-tilt and N6’s Wa weights. Multiplying a test function by cosh(δu) shifts the eval-
    uation points of its transform by ±iδ, so it reweights zeros according to their distance

                                                 20
   from the line; N6’s report showed that on its positive cone an on-line zero carries weight
   sech(x/2)-type and an off-line zero at depth a an extra cosh(ax). The brief’s Wδ is a
   proposal, not a defined object; I record a de Branges realisation of it near the end.
Turán/Nazarov lemma; Gibbs. Turán-type lemmas bound the number of zeros of an
   exponential sum on an interval by its length times the top frequency plus the number of
   terms; the brief proposes this to count sign changes of νX . “Gibbs” refers to the overshoot
   of a truncated Fourier-type expansion near a jump: the truncated prime sum oscillates
   near each zero ordinate, and the worry is that this alone produces negative squares.
Selberg/Levinson/Conrey. The classical theorems that a positive proportion (Selberg), at
   least a third (Levinson), at least about 40% (Conrey) of the zeros lie on the critical line,
   proved by mollifier methods; the brief’s benchmark is to recover any positive proportion by
   the new route.
(An automatic note lists the thirty-odd other agents active in the campaign and reachable by
message; nothing in it bears on the mathematics.)

1.3   R4’s signed density and its indefinite operator
I’ll start by reading everything on the list, beginning with R4, since R4’s signed density νX
and its indefinite operator are the objects the brief wants me to turn into a Pontryagin index.
R4’s report first. Its verdict is “NO VIABLE CANDIDATE” for an intrinsic, zero-free space of
global sections H 0 ; what matters for me is the object underneath. R4’s “number of conditions
imposed by the twist” attached to a test function g is
                                   Z
                     CX (g) = 12       |fˆg (τ )|2 νX (τ ) dτ,   X ≥ ediam supp g ,

with νX as in the brief plus a correction for the prime-number-theorem mean. R4 realises
this datum three ways — a warped-sine prolate operator, a Toeplitz/winding staircase ÑX =
θ/π + 1 + SX , and the de Branges phase of a structure function EX built from a truncated
Euler product — and shows all three to be the same νX . The reduction (R4’s Lemma 2.2
and Theorem 2.3) is that the Riemann–Roch inequality is empty at the level of formulas — it
holds for any real C, signed or not — and all content sits in the statement that CX (g) is a
dimension, i.e. CX (g) ≥ 0 for all g with support of length ≤ log X. That is semi-local Weil
positivity at level X; uniformly in X it is RH.
The operator the brief refers to is R4’s Candidate A, the kernel

                                         sin π(ÑX (t) − ÑX (s))
                                                                        
                             SX (t, s) =
                                                 π(t − s)

on L2 of a height window, whose diagonal is νX , discretised by the Nyström method. On the
window [880, 980], where the true zero count is 79, R4’s table reads
                        X #{eig > 1/2} min eigenvalue #{eig < −0.01}
                         1     80           0.00              0
                        10     79          −0.39             12
                       103     88          −0.67            115
                       104     83          −0.55            153
while the trace stays at ≈ 79 throughout. R4’s reading: “Verdict A: von Neumann (trace)
dimension = D2’s C(g) exactly; integer Landau dimension wrong for X ≥ 10; the condition
space is Krein.” (D2 is the earlier run whose h0 dictionary R4 uses.) The failure is quantified:
νX < 0 on 1.4% (X = 5), 21% (X = 100), 38% (X = 104 ) of τ ∈ [20, 1000], in dips of width


                                                     21
∼ 1/ log X (1123 of them at X = 104 ) and mass ≤ 0.50, “exactly at the uncertainty scale of
admissible tests”.
Two further items I register. In its red-team section R4 states that all positivity it found —
“Fejer minima > 0, envelope = N ” — is RH being true in the computed range. And its planting
experiment, in which two consecutive zeros are replaced by an off-line pair 12 ± η + iγ0 , finds
that the zero-side Weil form on test functions of support L first acquires a negative direction at

            L∗ = 1.26, 2.09, 2.68, 3.44                        (γ0 = 28, 100, 399, 991; η = 0.49),
             ∗
            L = 2.94, 4.78, 6.20, 7.08                         (same γ0 ; η = 0.02),

i.e. L∗ ∼ (0.65–0.85) log(γ0 /2π), nearly independent of η. R4 explains this as the test space
nearly annihilating the on-line zeros in a frequency window (Landau density), leaving the
indefinite cosh(η(xj − xk )) term unopposed. R4 also checked that the negative index of its
prolate operator is not a grid artefact: on [880, 930], negative index 55 at X = 103 and 77 at
X = 104 against a true count of 40, identical across step sizes.
Now R4’s working notes. They fix the dictionary inherited    from D2 — classes (d1 , d2 ; A),
the vector Γg = (G(1), G(0); (G(ρ))ρ ) with G(s) = g est , and χ(D) = d′1 d′2 − 12 ρ |G(ρ)|2
                                                  R                               P

— and record the explicit formula in the form I will need. With g(t) = e−t/2 f (t) one has
G( 12 + iτ ) = fˆ(τ ) and
                                    Z
        |G(ρ)| =       |fˆ(γ)|2 =           |fˆ|2 dN
  X                X
             2
    ρ              γ

                 = 2G(0)G(1) −               Λ(n)n−1/2 (f ∗ f˜)(log n) + (f ∗ f˜)(− log n) + Arch(f ∗ f˜),
                                    X                                                    
                                        n

so that  for supp(f ∗ ˜) ⊂ [− log X, log X] only n ≤ X enter and, integrating by parts, R |fˆ|2 dN =
                      f
  |fˆ|2 dNX exactly, the measure dNX having density θ′ /π − π1 n≤X Λ(n)n−1/2 cos(τ log n).
R                                                                 P

The notes then explain the   √ pointwise negativity.1 The supremum of the prime sum
                   √
is π1 n≤X Λ(n)/ n ∼ π2 X, which exceeds 2π             log(τ /2π) at resonance points once
      P

X ≳ (log τ ) /16; so “dNX ≥ 0” fails pointwise for every X ≥ 2 somewhere in every
              2

long window, and positivity survives only after testing against admissible |fˆ|2 , which cannot
localise into dips of width ≪ 1/ log X — and that averaged positivity is semi-local Weil
positivity at level X. The regime in which pointwise positivity is trivial is quantified by
                               X                 √ 
         Ttriv (X) = 2π exp 2                Λ(n)/ n = 17, 59, 500, 7300            (X = 2, 3, 5, 10).
                                    n≤X


Their numerical section records the staircase facts: RMS(ÑX − N ) falls 0.38 → 0.15; the
integer running-maximum envelope equals N (T ) at all 646 zero midpoints for every X ≤ 104 ;
the PNT mean must start at u = 2, not u = 1, or it fakes a +1/2. It records the Fejér-averaged
density with supp f = [−L/2, L/2], L = log X, whose minimum over τ0 ∈ [60, 940] is positive
for all X and equals γ h(γ) to 10−2 –10−3 , with ratio min/mean falling from 0.54 (X = 2) to
                     P

0.013 (X = 103 ); the match between the Hermite–Biehler defect of the structure function EX
and νX ; the planting law again; and the statement I most need to confront: the untwisted SX
“has negative eigenvalues iff νX dips (X ≥ 5): the ‘space of conditions’ is a Krein space, not a
Hilbert space, at every finite X ≥ 5; its positive+negative index reproduces the height count.”
Then R4’s code, to see exactly what was computed. The core routine implements νX and
NX from a table of 700 zero ordinates and the von Mangoldt sum, with the mean correction
π Re (X − 2 )/s, s = 2 + iτ . The prolate computation builds SX by Nyström with weight
1      s   s          1


                                                          22
equal to the grid step, sets the diagonal to νX , symmetrises and diagonalises, and tabulates
#{eig > 1/2}, the trace, the minimum eigenvalue and #{eig < −0.01} on three windows,
together with a twisted version h1/2 SX h1/2 whose trace is compared with γ h(γ). The
                                                                               P

staircase computation produces the negativity fractions, the dips, the envelope, and the Fejér
minima with the kernel L sinc2 ((τ − τ0 )L/2). The point I take away for later: the operator
whose negative eigenvalues R4 counted is this warped-sine kernel on a height window, not a
matrix of values of the Weil form on support-limited test functions.

1.4    N6’s normalisation and frontier-1’s intersection form
Next the N6 report. Its verdict is a NO-GO of a different kind — saturation of the “bootstrap”
cone of strip-positive test functions — but it carries the normalisation I will build on. The
explicit formula is fixed there in the form of Iwaniec–Kowalski (5.12): for even real g with
supp g ⊂ [−L, L] and h(r) = g(x)eirx dx,
                              R


             h(γρ ) = h(i/2) + h(−i/2) − g(0) log π + Arch(g) − 2         Λ(n)n−1/2 g(log n),
        X                                                            X

         ρ                                                            n

                                                                    γρ = (ρ − 21 )/i,
                       1                   1
                                          ir 
                           Z
         Arch(g) =             h(r) Re ψ        +
                                               dr
                      2π              4   2
                                     2 g(0)e−2y − g(y)e−y/2
                                 Z ∞                       
                    = −γE g(0) +                              dy,
                                  0          1 − e−2y
reproduced by N6 to 30 digits against 120 zeros and a Gaussian (and the x-side archimedean
term to 23 digits). On the zero side a zero 12 + a + it with its symmetry partners contributes
2 Re h(t+ ia) if a = 0 and 4 Re h(t+ ia) if a =
                                              ̸ 0, where Re h(t+ ia) = g(x) cosh(ax) cos(tx) dx.
                                                                      R

N6’s Proposition 1 solves the strip-positive cone completely:

             {g : Re h(t + ia) ≥ 0 on |a| ≤ 12 } = {k(x) sech(x/2) : k positive-definite},

by the maximum principle and the positive-definiteness of Wa (x) = sech(x/2) cosh(ax) for |a| ≤
2 — these are the “Wa weights” the brief mentioned. Theorem A is the sharp Harnack inequality
1

Re h(t + ia) ≤ h(t)/ cos(πa) on that cone, and Theorems B and C turn it into saturation: a
point 12 + δ + iγ0 is excludable by any strip-positive certificate only if cos(πδ) k e−π|γk −γ0 | < 2,
                                                                                  P

so that even with RH and all primes nothing on the line above γ0 ∼ 2πe4π can be excluded, the
finite-N reach being T ∼ 2πN 2 (Riemann–Siegel scaling), with a certified speck at height 1013
from N = 108 prime powers. What I will actually use from N6 is the validated normalisation
and its table of 2000 zero ordinates; the saturation theorems are context — they say that
sign-indefinite test functions are what is missing, which is at least the right neighbourhood for
a signature question.
Last on the list, frontier-1’s structural report, verdict “NO NEW GROUND”.              The object of
interest to me is its first construction: on real test functions f (u), with F (s) = f (u)e(s−1/2)u du,
                                                                                    R

the pairing
                          f · g := F (0)G(1) + F (1)G(0) −       F (ρ)G(1 − ρ)
                                                              X

                                                             ρ

read as an intersection form, with radical {F (0) = F (1) = 0, F (ρ) = 0 ∀ρ}, an abstract
Hodge-index theorem (their Theorem AC: a pointed closed convex cone containing the forward
light cone forces Lorentzian signature), and the “collapse” remark that any such cone axiom is
either vacuous under RH or false — their positive-measure cone being falsified quantitatively,
the constant κN := sup |c|2 /(AB) satisfying κN ≥ 1.013, 1.08, 1.66, 2.98 for N = 1, 3, 8, 20
                        P

zeros. The one line that is directly my business: “Lorentzian ⇔ RH: standard (Weil; an

                                                    23
off-line quadruple contributes −4 Re F (ρ)2 for even f , indefinite)” — the same hyperbolic-pair
mechanism the brief sketched, stated for even test functions. That completes the reading.


2     The global signature theorem and the honest finite index
2.1    Zero data in hand; the plan
I check what zero data I have to validate against: R4’s table of ordinates (starting
14.1347 . . . , 21.0220 . . . , 25.0108 . . .) and N6’s list of 2000 zeros running up to ≈ 2515.29. The
latter will be my zero side throughout.
The shape of the answer I am heading for, laid down before any of it exists: first the set-up
and the global signature theorem; then the finite-level index — which I am calling κ(L) and
κ(L, T ), with L the support length of the test functions rather than the brief’s X = eL —
treated under the heading of its correct definition and its relation to R4’s operator. So I do not
intend simply to take R4’s warped-sine operator as “the compressed Weil form” (the restriction
of the Weil Hermitian form to a finite-dimensional space of admissible test functions), which is
one of the two objects the brief’s item (2) offered. After that: numerics; the visibility of an
off-line zero at finite level; the question whether κ can be bounded from the prime side, which I
expect to be an obstruction to be quantified rather than a bound to be found; and a red team.
Now the theory: the signature theorem and the correct finite-level object.

2.2    Theorem 1: negative index counts distinct off-line zeros
First the conventions I will use throughout. Test functions f live on the line with variable u
(the logarithm of the idele norm), and are either of Schwartz type with e(1/2+ε)|u| f (j) ∈ L1 for
j ≤ 2, or in Cc∞ . The transform is
                                                        Z
                                          hf (r) =          f (u) eiru du,

entire and rapidly decreasing on horizontal strips. Zeros are written ρ = 21 + iγρ with γρ ∈ C,
| Im γρ | < 12 , multiplicity mρ ; the multiset of γρ is invariant under γ 7→ γ̄ and γ 7→ −γ. With
the involution f˜(u) = f (−u), for which hf˜(r) = hf (r̄), the Weil Hermitian form is

                                    W (f, g) :=             mρ hf (γρ ) hg (γ̄ρ ),
                                                   X

                                                     ρ

absolutely convergent, and Hermitian because the γ-term maps to the γ̄-term under swapping
f, g and conjugating.
On the diagonal, W (f, f ) = ρ mρ hf ∗f˜(γρ ) is the explicit formula applied to k = f ∗ f˜: pole
                             P

term, minus n Λ(n)n−1/2 k(log n) + k(− log n) , plus the archimedean term, in the Iwaniec–
             P                                   

Kowalski (5.12) normalisation that N6 validated. If supp f ⊂ [−L/2, L/2] then supp k ⊂ [−L, L]
and only n ≤ X := eL enter. So the restriction of W to Cc∞ (−L/2, L/2) is computable from
the primes ≤ X and Γ alone, and in R4’s spectral form it reads
                            Z
              W (f, f ) =       |hf (τ )|2 dÑX (τ ),            dÑX = νX dτ + (pole measure).

Weil’s criterion: RH holds iff W (f, f ) ≥ 0 for all f .
Now the brief’s item (1). Let κ be the negative index of W on S (or on Cc∞ (R)), i.e. the
supremum of dim U over finite-dimensional subspaces U on which W is negative definite.


                                                            24
Theorem 1 (global signature). κ = #{ρ : ζ(ρ) = 0, Re ρ > 12 } counted without multiplicity
(distinct zeros), as an element of [0, ∞]; equivalently, κ is the number of distinct γρ with
Im γρ < 0.
The brief conjectured “negative index = Noff ” and sketched the mechanism; the statement I
can prove differs in one word. The proof has four parts.

(a) The hyperbolic pair. Group the zeros into on-line ones (γ real) and off-line pairs
{γ, γ̄}, the two members of a pair having equal multiplicity m. Writing lz (f ) := hf (z) for the
evaluation functional and γ ∗ := γ̄,

                       W (f, f ) =        m |lγ (f )|2 +           2m Re lγ (f ) lγ ∗ (f ) ,
                                     X                       X                            
                                     on                    pairs

and the rank-two form

                              (a, b) 7→ 2 Re(ab̄) = 12 |a + b|2 − 12 |a − b|2

has signature (1, 1). This is exactly the hyperbolic pair the brief described, and frontier-1’s
“−4 Re F (ρ)2 , indefinite”.

(b) Upper bound. Write W = P − N with

                              P =         m |lγ |2 +           2 |lγ + lγ |     ≥ 0,
                                     X                 X
                                                               m         ∗
                                                                            2
                                     on                pairs

                              N=
                                     X
                                             m           2
                                             2 |lγ − lγ | .
                                                       ∗

                                     pairs

If W |U < 0 then N |U > 0, so dim U ≤ rank N |U ≤ #pairs. The point the brief’s phrasing
“(with multiplicity, pairs)” misses: m enters as a weight, not as extra rank — an off-line zero of
multiplicity m contributes one negative square. This is forced, since W sees the zeros only
through the measure ρ mρ δγρ ; no derivative h′ (γ) ever occurs.
                       P


(c) Lower bound. This needs an explicit construction, which is my own part. Given distinct
off-line zeros γj = tj − iδj , δj > 0, j = 1, . . . , k, I want test functions f1 , . . . , fk whose Gram
                                                                             2     2
matrix under W is negative definite. Take the Gaussian As (r) = e−r /(2s ) and

                                  hj (r) = As (r − tj ) (r − tj ) qj (r),

with qj a polynomial independent of s; then fj is (polynomial × Gaussian)·e−itj u , which is
                                                                       2    2
admissible. At the pair γj , γ̄j , writing y = δj and A = As (±iy) = ey /(2s ) , the two values
a = hj (γj ), b = hj (γ̄j ) satisfy
                                     ab̄ = −y 2 A2 qj (γj ) qj (γ̄j ).

I choose qj = pj cj . Here pj is the product of (r−z) over all points z of the orbit S∪S̄∪(−S)∪(−S̄)
of the given set S = {γ1 , . . . , γk }, except the two points {γj , γ̄j }. I have to be careful that
−γ̄i = −ti − iδi is a genuinely different point, and that omitting a conjugation-symmetric pair
keeps pj (r̄) = pj (r), so that

                                 pj (γj ) pj (γ̄j ) = pj (γj )2 =: wj ̸= 0.

The factor cj (r) = (r − zj )(r − z̄j ) is a quadratic with real coefficients, with vj := cj (γj )2
tuned so that arg vj = − arg wj ; this is possible because the map z 7→ (γj − z)(γj − z̄) fills a


                                                        25
region containing points of every argument, and squaring doubles arguments. Then the pair
contributes
                                                    2 2
                           2mj Re(ab̄) = −2mj δj2 eδj /s |wj vj | < 0,
growing as s → 0, while everything else vanishes.
                                                                            2   2
Indeed, on-line zeros at real distance x from tj contribute e−x /s x2 (. . .) ≤ s2 /e → 0, and the
sum tends to zero by dominated convergence (counting function O(T log T ) against Gaussian
decay). The rest of the orbit is killed exactly by pj . To keep the argument unconditional I
take S = ST to be all distinct off-line zeros with | Re γ| ≤ T ′ , where T ′ ≥ maxj |tj | + 1 (a finite
set, since N (T ′ ) < ∞); then any remaining off-line zero has | Re γ − tj | ≥ 1 > 12 > | Im γ| and
                                2                                               2    2
contaminates at rate e−3/(8s ) , which loses to the main term eδj /s precisely because δj < 12
makes δj2 < 38 . Off-diagonal Gram entries vanish on the orbit and tend to zero elsewhere by
                                                            2     2
Cauchy–Schwarz; after normalising each fj by e−δj /(2s ) the Gram matrix tends to
                                        diag − 2mj δj2 |wj vj | < 0.
                                                                 

Hence κ ≥ |ST | for every T .

(d) Passage to compact support.                 W is continuous for the norm
                                          XZ
                              ∥f ∥∗ =            |f (j) (u)| e|u|/2 (1 + u2 ) du,
                                          j≤2

since |hf (γ)| ≤ ∥f ∥∗ /(1 + |γ|2 ) uniformly on the strip and (1 + |γ|2 )−2 is summable over the
zeros. The Gaussian-polynomial test functions of (c) are ∥ · ∥∗ -limits of compactly supported
ones, and negative definiteness of a finite Gram matrix is an open condition. That completes
the proof, by my own account.
Corollary 1.1 (finite level). Let κ(L) be the negative index of W on Cc∞ (−L/2, L/2). Then
κ(L) is finite for each L (by the proposition I will prove next), nondecreasing in L, and κ(L) → κ
(the negative subspace produced in (c)–(d) has compact support). RH ⇐⇒ κ(L) = 0 for
all L (Weil/Yoshida); κ(L) ≥ 1 for a single L is a disproof certificate for RH; and always
κ(L) ≤ Noffdist , the number of distinct zeros with Re ρ > 1 .
                                                             2

Two remarks. The first is multiplicity blindness, which matters for everything below: the
Weil form cannot tell an off-line zero of multiplicity m from a simple one weighted by m, so
any upper bound on zeros obtained through κ must be multiplied by the multiplicity, which
unconditionally is only bounded by O(log T ). A de Branges kernel variant would see multiplicity;
I will come back to that. The second is the literature, from memory only — I cannot verify
any of it offline. Yoshida (1992, “On Hermitian forms attached to zeta functions”) studies
W on functions supported in [−t, t], proves finiteness statements and RH ⇐⇒ positivity for
all t, and I believe identifies the negative index with the off-line zeros in a form equivalent
to Theorem 1; Bombieri (2000, Rend. Lincei, “Remarks on Weil’s quadratic functional in
the theory of prime numbers I”) analyses the variational problem on [−t, t]; Burnol relates
the restricted form to de Branges/Sonine spaces. I treat Theorem 1 as folklore-level with a
self-contained proof; the “distinct” subtlety is rarely stated.

2.3    R4’s negatives are not Weil-form negative squares
Next the finite-level object, and what R4’s “33–153 negative eigenvalues” are and are not.
Proposition 2.1 (κ(L) < ∞). On HL = L2 (−L/2, L/2),
                                    Z
                     W (f, f ) =        |hf (τ )|2 νX (τ ) dτ + Pole(f ),           X = eL ,


                                                      26
where Pole(f ) = |hf (i/2)|2 + |hf (−i/2)|2 ≥ 0 has rank ≤ 2, and

                             1     |τ |
                   νX (τ ) ≥   log      − MX − O(τ −2 ),
                            2π     2π
                           1 X Λ(n)
                      MX =         √      + (a bound for the mean term).
                           π n≤X n

Fix c0 > 0. The set E = {νX < c0 } is bounded, contained in [−TX , TX ] with TX ∼
2π exp(2π(MX + c0 )) — this is R4’s Ttriv . Split νX = a − b with a = max(νX , c0 ) and
b ∈ [0, c0 + MX
              ′ ] supported in E (here M ′ is M together with the mean-term bound). Then
                                          X       X
W ≥ 2πc0 ∥f ∥2 − ⟨Tb f, f ⟩, where Tb , the compression to HL of the Fourier multiplier b, is
positive and trace class with tr Tb ≤ 2π
                                       L
                                         |E| sup b. Hence

                            κ(L) ≤ #{eigenvalues of Tb ≥ 2πc0 }
                                       L |E| (c0 + MX
                                                    ′ )
                                   ≤                    < ∞.
                                            4π 2 c0
                                                                                     √
Numerically this bound is astronomically bad: |E| ∼ 0.3 TX with TX = 2πe∼4 X , so the
                                      L/2
a-priori bound is Bapriori (L) ∼ L e4e    — useless. And it uses only pointwise information on
νX : it is the quantitative form of the brief’s item (3), “count sign changes of νX ”; any bound
of the type κ(L) ≤ 2π L
                         · meas{νX < c} is of this size. I will return to why nothing pointwise
can do better.
Now what R4 actually computed. R4’s candidate-A operator

                                           sin π(ÑX (t) − ÑX (s))
                                                                  
                               KX (t, s) =
                                                   π(t − s)

on L2 of a τ -window, with diagonal νX (t), is not a compression of the Weil form to admissible
test functions (support of length ≤ L). It is a warped sinc kernel whose Weyl symbol is roughly
1{|ξ| < πνX (t)} sign νX (t), manifestly indefinite wherever νX < 0 (a negative diagonal entry
already gives a negative direction). Its negative eigenvalue count therefore tracks window length
times local bandwidth over {νX < 0} — the Szegő/Landau count of the pointwise-negative
region, the same quantity as Bapriori restricted to the window. It says “the signed density is
negative there”, nothing more.
The honest Pontryagin index of the level-X condition space is κ(L), or its compression κ(L, T )
to test functions whose transforms are concentrated in a height window below T , and

   κ(L, T ) = 0 for every X, T in any range where the zeros are known to be on the line

(up to leakage), because for supp f ⊂ [−L/2, L/2] the explicit formula gives W (f, f ) =
  γ |hf (γ)| exactly — R4 itself observed “Fejér minima > 0”. So my answer to the brief’s
P           2

red-team question (4) is neither “κ ∼ N (T )” nor “κ/N → c”: the correctly defined κ(X, T ) is
identically zero in every computable range, as it must be, since κ(X, T ) ≥ 1 would disprove
RH below ∼ T . There is nothing to fit. This contradicts all three regimes the brief offered and
R4’s “Krein space” headline alike.
The Gibbs dips of νX (width ∼ 1/ log X, mass ≤ 1/2, as R4 measured) are real, but they are
not negative squares of the compressed form: an admissible |hf |2 has bandwidth L = log X and
cannot localise into a dip, so the dips cancel against neighbouring positive mass. Szegő-type
asymptotics (“eigenvalues ≈ symbol samples”) fail here because the symbol varies on the scale
1/L of the resolution itself. I expect the numerics to show hundreds of eigenvalues at the

                                                27
10−6 –10−9 level — forced, since rank W |V ≤ #{zeros in the window} once dim V exceeds that
number — while the symbol is negative on 20–40% of the window. This is a forecast; nothing
is computed yet.
The object I will compute is the Gabor-type subspace

                                   VL,T = span fk (u) = φL (u) e−iτk u ,
                                                     


with φL a fixed bump on [−L/2, L/2] and centres τk = k∆ ∈ [T0 , T ], ∆ = 2πq/L (q ≤ 1 an
oversampling factor). Thus hfk (r) = φ̂L (r − τk ) is a bump of width ∼ 4π/L centred at τk , and
d = dim V ∼ (T − T0 )L/(2πq). The finite index is then

                                        κ(L, T ) := n− [W (fk , fl )]k,l ,
                                                                           


the number of negative eigenvalues of the Gram matrix, basis-independent by Sylvester’s law
of inertia (a prolate basis spans the same space up to edge effects). On the prime side
                                        Z
                     W (fk , fl ) =         φ̂L (τ − τk ) φ̂L (τ − τl ) νX (τ ) dτ + Pole,

with the pole term superalgebraically small once τk ≳ 20; the zero-side formula γ φ̂L (γ −
                                                                                                 P

τk )φ̂L (γ − τl ) is for validation only. This is the brief’s item (2) in its second form — the Gram
matrix of the Weil form on a time–frequency-limited family of dimension ∼ (log X) · T , here
with windowed exponentials rather than prolates (same span up to edge effects) — and not
R4’s νX -operator, which is the wrong object.


3     Compressing the Weil form; visibility of off-line zeros
3.1   The Gabor compression validated; spurious negatives traced
Now I build the compression — the restriction of the Weil form W to the Gabor space VL,T of
windowed exponentials introduced above, realised as a Gram matrix. The prime-side density
I integrate against is the full one, with the pole term of the explicit formula absorbed as a
spectral density (I owe the derivation of this; it comes shortly):

                                  θ′ (τ ) 1 X Λ(n)
                    full
                   νX    (τ ) =          −      √ cos(τ log n)
                                     π     π n≤X n
                                        1    Xs − 1         1
                                    +     Re        +               ,             s = 21 + iτ,
                                        π      s      2π( 4 + τ 2 )
                                                          1


                            full holds exactly whenever supp(f ∗ f˜) ⊂ [−L, L]. For the window
so that W (f, f ) = |hf |2 νX
                   R

function φL I take a Kaiser bump on [−L/2, L/2],
                                               q                      
                              φ(u) = I0 β 1 − (2u/L)2 ,
                                              sinh
                                                     p             
                                                         β2 − z2                rL
                                  φ̂(r) = L                            ,   z=      ,
                                                                                 2
                                                 p
                                                     β2 − z2

whose transform is entire and available in closed form.
The computation — I will refer to it as the compression computation — assembles the following.
The prime-side Gram matrix GP = [W (fk , fl )] is obtained by trapezoidal quadrature in τ
(step 0.02, each atom φ̂(· − τk ) truncated where its envelope falls below 10−9 of its peak).
The zero-side Gram matrix is GZ = A⊤A with Aγk = φ̂(γ − τk ), from N6’s 2000 ordinates.

                                                          28
Alongside these: the Plancherel mass matrix M of the atoms; a signature routine that first
passes to an M -orthonormal basis of the numerically nondegenerate part of V ; and two utilities
for later — a rank-two Hermitian update representing a planted off-line quadruple 12 ± δ ± it0
(the γ, γ̄ pair; the copies at negative t are negligible), and removal of prescribed on-line zeros.
First validation: L = log 1000, window [100, 300], β = 14, oversampling q = 1. The closed-form
φ̂ matches direct quadrature to about 10−6 relative at r = 0, 1, 3, 5, 8 and at the complex point
2 + 0.3i. The compression has d = 220 atoms, cutoff radius ≈ 22.5, and

                  max |GP − GZ | = 1.03 × 10−6       against   max |GZ | = 9.69,

so the prime side and the zero side of the explicit formula agree entrywise. But the signatures,
read through the M -orthonormal reduction, disagree badly: the prime side reports “neg,pos,null
33 145 42” with minimum eigenvalue −0.0129, the zero side 0/115/105, with 109 zeros in the
window. Thirty-three negative squares from a matrix within 10−6 of a positive semidefinite
one cannot be right.
So I test the eigenvalue counting itself, over q ∈ {1.0, 0.8} and quadrature step dτ ∈ {0.02, 0.01},
looking at the raw eigenvalues of GP rather than at the reduced form, and recording the
condition number of M . The numbers: cond(M ) = 7.6 × 109 at q = 1 (2.1 × 104 at q = 0.8),
while ∥E∥2 = ∥GP − GZ ∥2 ≈ 1.7–1.9 × 10−6 throughout. (Editorial: evidently the 33 negatives
were numerical — the reduction through an ill-conditioned mass matrix amplifying quadrature
noise into “negative squares”; the record contains the numbers and the decision that follows,
not this diagnosis in words.) The raw spectrum of GP has lowest eigenvalue ≈ −1.18 × 10−7
(q = 1) and −9.6 × 10−8 (q = 0.8), “#< −1e-4: 0” in every case, with 109 near-null eigenvalues
for d = 220 and 66 for d = 176, against 111 resp. 110 zero-side eigenvalues above 10−4 . No
genuine negative direction; the rank is approximately the number of zeros in reach (zeros in
the height interval on which the atoms’ transforms are non-negligible), and the null space has
dimension d minus that — exactly the picture I forecast. From here on I read signatures from
raw eigenvalues of GP (basis-independent by Sylvester’s law of inertia, the atoms being linearly
independent) and use q = 0.8.

3.2    The index grid and its forecast
Now the grid the brief asked for in item (2), X = 102 , 103 , . . . , 106 , carried out on the Gram-
matrix compression of the Weil form (the brief’s second option, here with Kaiser–Gabor atoms)
rather than on R4’s νX -operator: windows [50, 1000] and [1000, 2400], Kaiser β = 14, q = 0.8,
signature from raw eigenvalues at threshold 10−5 max |ev|. For each X and window I want the
inertia (n− , n0 , n+ ) of GP — numbers of negative, null and positive eigenvalues — its minimum
eigenvalue, the discrepancy ∥GP − GZ ∥, the zero-side rank, and the number of zeros in the
window. Against these I set the pointwise quantities that embody the brief’s sign-change route:
the fraction of the window on which νX < 0; the “Szegő prediction” n− ≈ (that fraction) · d, i.e.
what one would get if eigenvalues were symbol samples; and the a-priori count of Proposition 2.1
restricted to the window,
                                  Lq
                                     (T1 − T0 ) meas{νX < 0.05}.
                                  2π
I also add two prime-computable positivity certificates. Writing R for the matrix of W |V in
M -orthonormal coordinates, trace and second moment alone give n+ ≥ (tr R)2 / tr(R2 ), so I
record the certified-positive fraction (tr R)2 /(d tr R2 ), together with a Fejér-smoothed proxy
⟨ν⟩2 /⟨ν̄ 2 ⟩ for it.
I am confident enough of the outcome to write down the reading before a single row exists:
n− (GP ) = 0 throughout, i.e. the compressed Weil form at level X is positive semidefinite


                                                29
by a prime-side computation using no zeros; d − rank ≈ d − #zeros exact null directions
whenever d exceeds the zero count; the symbol νX negative on 20–45% of the window; and “the
Szego/pointwise prediction and the a-priori bound are off by everything.” The first attempt at
the grid is cut off before producing a row,
so I set it going again to run on its own and turn to the theory it is meant to illustrate.

3.3     The pole density, and Theorem 2 on visibility
First the derivation I owe, so that the prime side really is a single integral against νX
                                                                                        full . For an

even kernel k supported in [−L, L], X = e , with transform k̂, the pole term of the explicit
                                            L

formula is
                                                                  Z
                      Pole(k) = k̂(i/2) + k̂(−i/2) =                  k(v) 2 cosh(v/2) dv,

while
                     Z X                                                  Z L
                           u−1/2 k(log u) + k(− log u) du =                     k(v) e|v|/2 dv.
                                                                
                      1                                                    −L

Since 2 cosh(v/2) = e|v|/2 + e−|v|/2 ,
                           Z X                                                  Z
                                   −1/2 
              Pole(k) =                     k(log u) + k(− log u) du +              k(v) e−|v|/2 dv
                                                                      
                                  u
                            1
                           Z               h1        Xs − 1         1       i
                       =        |h(τ )|2        Re          +                 dτ,         s = 21 + iτ,
                                           π           s      2π( 4 + τ 2 )
                                                                  1


by Parseval applied Rto k = f ∗ f˜, |h|2 = k̂, the transform of e−|v|/2 being 1/( 14 + τ 2 ). Hence,
exactly, W (f, f ) = |hf |2 νX full for supp f ⊂ [−L/2, L/2], with ν full as defined above. R4’s
                                                                       X
“PNT mean from u = 2” is this up to the smooth O(1/τ ) piece coming from 12 and the term
                                                                                  R

1/(2π( 14 + τ 2 )) — irrelevant for their sign statistics, relevant for exactness here. The check
already in hand is the agreement of GP with GZ to 10−6 absolute (entries of size 1–10) at
X = 103 on [100, 300]; the grid records ∥E∥ in every row.
A word on why the computed index is the true one. The basis is the Kaiser window with
centres τk = T0 + k∆, ∆ = 2π/(qL); the signature is read from raw eigenvalues at threshold
10−5 ×scale and validated against the zero side, which is exactly positive semidefinite (it is
A⊤A); the leakage of hfk outside [T0 − rcut , T1 + rcut ] is below 10−9 ; and hypothetical off-line
zeros above the RH-verified height 3 × 1012 , if any, would contribute less than (10−9 )2 . So
κ(X, T ) as computed is the true signature of W on VL,T up to the threshold.
Now the question that the brief’s phrase “off-line zeros visible to the subspace” presupposes,
made quantitative. Fix a hypothetical off-line zero ρ0 = 12 + δ + it0 , δ > 0, so γ0 = t0 − iδ.
“Level L” means test functions supported in [−L/2, L/2], i.e. primes ≤ X = eL . What is the
smallest L for which the restriction of W to Cc∞ (−L/2, L/2) has n− ≥ 1 on account of ρ0 ?

Theorem 2 (isolated zero, worst case over on-line configurations). Suppose all zeros
with | Re γ − t0 | ≤ 1 other than {γ0 , γ̄0 } lie on the line, and let n1 := N (t0 + 1) − N (t0 − 1);
unconditionally n1 ≤ A0 log t0 (from memory a Backlund/Trudgian bound, roughly 0.25 log T +2
for T large; I keep it symbolic). If
                         √
                           n1 + 1
      L ≥ Lvis := CB                  (CB absolute, depending on the bump B; CB ∼ 4),
                            δ


                                                            30
 then there is f ∈ Cc∞ (−L/2, L/2) with W (f, f ) < 0. More precisely, for a family ρj = 12 +δj +itj
                                                                       q
 with |ti − tj | ≥ 2, each isolated in this sense, L ≥ maxj CB n1 (tj ) + 1/δj gives n− ≥ #family.

 The proof, as I work it. Take a bump B ≥ 0, smooth, supp B ⊂ [− 12 , 12 ],               B = 1, and rescale
                                                                                      R

 BL (u) = B(u/L)/L, so that B̂L (x) = B̂(Lx). Choose f with

                                          hf (r) = (r − t0 ) B̂L (r − t0 )

 (namely f = i(BL )′ e−it0 u ; the sign is immaterial).                The contributions to W (f, f ) =
    m h(γ)h(γ̄) are:
 P

 (i) The pair γ0 , γ̄0 : h(γ0 ) = (−iδ)B̂L (−iδ), h(γ̄0 ) = (iδ)B̂L (iδ), and
                                     Z
                       B̂L (±iδ) =        BL (u) cosh(δu) du =: c(δL) ∈ [1, cosh(δL/2)]

      is real; the pair contributes 2 Re[(−iδ)(−iδ)] c2 = −2δ 2 c2 ≤ −2δ 2 (times m0 ≥ 1).
 (ii) The reflected pair at −t0 : |h(−t0 ∓ iδ)| ≈ 2t0 |B̂L (−2t0 ∓ iδ)|, superpolynomially small in
      Lt0 — negligible.
(iii) On-line zeros, x := γ −t0 : |h|2 = x2 B̂(Lx)2 , with supremum L−2 b1 where b1 = ∥y B̂(y)∥2∞ ≤
      ∥B ′ ∥21 . For |x| ≤ 1 there are at most n1 zeros, total ≤ n1 b1 /L2 . For |x| > 1, |B̂(y)| ≤
      ∥B ′′′ ∥1 /|y|3 gives x2 B̂(Lx)2 ≤ ∥B ′′′ ∥21 /(L6 x4 ), and |γ−t0 |>1 (γ − t0 )−4 ≤ A′0 log(t0 + 3), so
                                                                  P

      this tail is ≤ b3 A′0 log(t0 + 3)/L6 with b3 = ∥B ′′′ ∥21 .
(iv) Other off-line zeros: none within | Re γ − t0 | ≤ 1 by hypothesis. For those farther, write
      γ = t0 + x − iy; then |h(x − iy)| = |x − iy| |B̂L (x − iy)|, and B̂L (x − iy) is the transform of
      the smooth compactly supported function BL eyu (|y| < 12 ), bounded by

                                         ∥(BL eyu )′′′ ∥1   CeL/4 (1 + L−3 )
                                                          ≤                  .
                                             |x|3                 |x|3

     I first want to call the eL/4 loss harmless because it multiplies |x|−3 -summable terms — no:
     eL/4 /|x|3 with |x| ≥ 1 is not small. The honest fix is to strengthen the hypothesis: either
     to “no off-line zeros with | Re γ − t0 | ≤ RL := eL/12 L”, or to global isolation (the orbit of
     ρ0 is the only off-line zero), or to

     (HR ) : all zeros other than the γ0 -orbit with | Re γ−t0 | ≤ R lie on the line,             R = eL/8 ;

     then the far off-line sum is ≤ C log t0 /L6 . Recorded honestly: interference from unknown
     off-line zeros is not controlled by this argument.
 In total,
                                                      n1 b1 C log(t0 + 3)
                              W (f, f ) ≤ −2δ 2 +          +              <0
                                                       L2        L6
 as soon as L2 > (n1 b1 + 1)/δ 2 (for L ≥ 2, absorbing the C/L4 ). With B the normalised bump
 exp(−1/(1 − 4u2 )) the constant b1 is to be evaluated numerically. For the family: the hfj
 are 2-separated in centre, the cross terms W (fi , fj ) decay like (L|x|)−3 , the off-diagonal row
 sums√are ≤ C ′ log T /L3 , and Gershgorin’s theorem gives the full count once L ≥ Lvis , which is
 ≥ C log/δ ≫ (log T )1/3 . QED modulo constants.
 So:√ an isolated off-line zero at height t and depth δ is visible from primes ≤ X once log X ≥
 C log t/δ (worst case over positions of the on-line zeros), and jointly so for 2-separated isolated
 families. Under “average” spacing — zeros near t0 at distances ∼ k · 2π/ log t0 — the sum in
 (iii) is instead
                                 log t0                   log t0 ∥y B̂∥22
                                        Z
                              ≈           x2 B̂(Lx)2 dx =                 ,
                                   2π                       2π     L3

                                                        31
giving the softer threshold
                                   (log t ) b 1/3
                                          0        2
                           L ≥                          ,    b2 = ∥y B̂(y)∥22 .
                                       4πδ 2
This, I believe, is the law R4’s planting experiment saw (L∗ nearly independent of depth
over their small range). A rough check against R4’s numbers: t0 = 991, δ = 0.02 gives
(6.9 b2 /(4π · 4 × 10−4 ))1/3 ≈ 11 with b2 ∼ 1, against their 7.08 obtained with a richer 30-bump
family; δ = 0.49 gives 1.3 against their 3.44 — at large δ the on-line term is not the binding
constraint, the pole and edge terms are; fine.

Clusters reinforce, but count once. If several off-line zeros ζi = t0 + xi − iyi sit within
|xi | ≪ 1/L of t0 (any depths yi > 0), then with the same f ,

                     h(ζi )h(ζ̄i ) = (xi − iyi )2 B̂L (xi − iyi )2
                                 ≈ (x2i − yi2 − 2ixi yi ) c(yi L)2 1 + O(Lxi ) ,
                                                                                  


whose real part is negative when yi > |xi |: every zero that is deeper than it is horizontally
displaced from t0 adds to the negativity of W (f, f ). But they add to the same single negative
direction. The index n− counts W -orthogonal negative directions, and k zeros within o(1/L)
of each other span, to first order, the same two functionals ℓt0 , ℓ′t0 (evaluation of h and of h′
at t0 ), so they yield 1 (at most 2) negative squares at level L, not k. Separating them needs
L ≳ 1/ min |ζi − ζj | (uncertainty principle; to be measured). In the limit of coincidence no
level separates them — Theorem 1 again: κ counts distinct zeros.

Interference: the gap in any unconditional visibility theorem. Off-line zeros ζ =
t0 +  x − iy that are wider   than deep, |x| > y, sitting at c/L < |x| < O(1), contribute
Re (x − iy)2 B̂L (x − iy)2 , which can be positive and as large as x2 c(yL)2 ∼ x2 eyL . For y
                         

comparable to δ this is comparable to the main term −2δ 2 c(δL)2 , and unconditionally there
may be up to A0 log t0 such zeros. No choice of B avoids this: BL eyu /c(yL) is a probability
density on [−L/2, L/2], its characteristic function is small at x only for |x| ≳ (width)−1 , and
the width is at most L/2; so zeros at c/L < |x| < C/L with depth ∼ δ interfere at relative
order 1. Conclusion: the statement “every off-line zero of depth ≥ δ below height T forces
its own negative square at level L(δ, T )” is true for isolated zeros (Theorem 2), true for tight
clusters counted once, and not provable configuration-free; the exact unconditional statement
is the limit L → ∞ in Theorem 1. This already narrows the rigorous inequality Noff ≤ κ + E
that the brief’s item (3) hoped for.


4     The negative-index route is empty: index identically zero
4.1   First honest index row: zero negative squares
The first row of the index grid is in. To recall the objects: GP is the Gram matrix of the Weil
form compressed to the Gabor space VL,T (Kaiser atoms supported in [−L/2, L/2], centres
spread across the height window), computed from the primes ≤ X = eL and Γ alone; GZ is
the same matrix computed from the zeros, used only for validation; and (n− , n0 , n+ ) is the
inertia — the numbers of negative, null and positive eigenvalues — read from raw eigenvalues
of GP . At X = 102 , L = 4.61, on the window [50, 1000], with d = 558 atoms and 639 zeros in
the window:

                n− (GP ) = 0,        n0 = 18,           n+ = 540,
                                          −8
             min ev(GP ) = −1.82 × 10          ,       ∥E∥2 = ∥GP − GZ ∥2 = 9.0 × 10−7 ,


                                                       32
and on the zero side n− = 0 with rank 540.
Against this stand the pointwise quantities that embody the brief’s sign-change route. The
fraction of the window on which νX < 0 is 0.207; the “Szegő prediction” — negative eigenvalues
≈ that fraction times d, as if eigenvalues were samples of the symbol — is n− ≈ 115.5; the
a-priori count of Proposition 2.1 restricted to the window is 126.1. The prime-computable
positivity certificate — the fraction (tr R)2 /(d tr R2 ) of eigenvalues certified positive by trace
and second moment alone, R being the matrix of W |V in mass-orthonormal coordinates — is
0.808, its Fejér-smoothed proxy 0.785. So from primes ≤ 100, with no zeros used: not a single
negative square, while the signed density is negative on a fifth of the window and the pointwise
count would predict over a hundred. This is the first actual row behind the reading I wrote
down in advance.
Before the grid goes further I want two changes: the high window moved up to [1400, 2400],
and the discrepancy ∥GP − GZ ∥ recorded in the Frobenius norm, which dominates the spectral
norm.
On the second attempt both changes are in, and the grid restarts from X = 102 on the windows
[50, 1000] and [1400, 2400], with ∥E∥ henceforth the Frobenius norm ∥GP − GZ ∥F .

4.2    Planting off-line zeros: annihilation versus robust visibility
Alongside the grid I want the numerical companion to Theorem 2: plant an off-line quadruple
among the true zeros and measure the smallest level L at which the compressed form acquires a
negative square — R4’s planting experiment, redone on an honest compression of the Weil form
rather than on the warped-sine operator. The design: at height t0 I take the union of three
Kaiser–Gabor families, β ∈ {6, 10, 14}, with centres spaced 2π/(1.5L) over [t0 − 40, t0 + 40];
the zero-side Gram matrix G0 = AT A is built from the true zeros with |γ − t0 | < 100 (out of
the 2000 below 2515); and the planted quadruple 12 ± δ ± it0 enters as the rank-two Hermitian
update

                    a b∗ + b a∗ ,    a = hk (t0 − iδ) k ,    b = hk (t0 + iδ) k ,
                                                                             


where hk is the transform of the k-th atom. The plant is made either in “add” mode, on top of the
true zeros, or in “replace” mode, after subtracting the Gram contribution of the two nearest on-
line zeros. I scan L from 1 to 18 in steps of 0.25 and record L∗ , the first level with an eigenvalue
below −10−8 max |ev|, for t0 ∈ {100, 400, 1000, 2200} and δ ∈ {0.02, 0.05, 0.1, 0.2,    √ 0.3, 0.45}.
Next to each L∗ I set the two laws from the visibility analysis — the worst case n1 + 1/δ of
                                                                                                 1/3
Theorem 2, with n1 = #{γ : |γ − t0 | ≤ 1}, and the average-spacing law log(t0 /2π)/(4πδ 2 )
with the bump constant b2 := 1 — and fit L∗ ∼ a δ −p log(t0 /2π)r over the add-mode data.
A second experiment, at fixed level (t0 = 400, δ = 0.2, L ∈ {6, 10, 14}), counts negative
squares for: a single quadruple; a double zero (the same plant with weight 2 — Theorem 1
says multiplicity is invisible, so this should give 1); two depths 0.2 and 0.35 at one ordinate;
two quadruples at t0 ∓ ε/2; and five quadruples spaced ε apart, for ε from 0.01 to 4.
The first rows come back at t0 = 100, where n1 = 0 and log(t0 /2π) = 2.77:
                                                      √
                           δ   mode L∗ n− (d)             n1 + 1/δ avg. law
                         0.02   add   3.50 1 (201)         50.00     8.20
                         0.02 replace 2.75 1 (159)         50.00     8.20
                         0.05   add   3.25 1 (189)         20.00     4.45
                         0.05 replace 2.75 1 (159)         20.00     4.45
                         0.10   add   3.25 1 (189)         10.00     2.80
                         0.10 replace 2.75 1 (159)         10.00     2.80


                                                 33
So the measured threshold is tiny, nearly independent of the depth δ, and sits far below both
laws. The restarted grid has also reproduced its first row: X = 102 on [50, 1000], n− (GP ) = 0,
n0 = 18, n+ = 540, min ev = −1.82 × 10−8 , ∥E∥F = 8.9 × 10−6 , certificates 0.808/0.785 as
before.
The reading of these tiny thresholds is the one R4 gave for its own planting thresholds: once
dim V exceeds the number of zeros within reach of the atoms (the zeros in the height interval
on which the atoms’ transforms are non-negligible), the on-line Gram matrix has a null space
— the test space nearly annihilates the on-line zeros — and the planted rank-two term can
push an eigenvalue below zero at an arbitrarily small level. Call this “annihilation” visibility:
possible as soon as dim V > #{zeros in reach}, and silent about robust negativity. What I
add is a second, robust threshold. Both are taken relative to the scale s := largest eigenvalue
of the unplanted on-line Gram matrix G0 :

                         L∗ann := first L with an eigenvalue < −10−8 s,
                         L∗rob := first L with an eigenvalue < −10−3 s,

with L scanned from 0.5 to 14, min ev/s recorded at each threshold, and L∗ann , L∗rob fitted
separately as a δ p log(t0 /2π)r in add mode.
and a second attempt to clear the old runs fails the same way.
On the third attempt the two-threshold version goes in cleanly — L from 0.5 to 14, L∗ann
and L∗rob recorded with min ev/s, separate least-squares fits in add mode — and the planting
experiment restarts from scratch. The index grid has been running undisturbed throughout.

4.3    Negative index zero across the whole prime range
Back to the results. The low window of the grid is complete: window [50, 1000] (639 zeros),
Kaiser β = 14, oversampling q = 0.8, signature read from raw eigenvalues at threshold
10−5 max |ev|. The inertia of the prime-side Gram matrix, level by level:
                           X      L    d n−   n0      n+    min ev(GP )
                          102 4.61 558    0   18      540   −1.82 · 10−8
                          103 6.91 836    0 195       641   −1.18 · 10−7
                          104 9.21 1115   0 473       642   −4.65 · 10−7
                          105 11.51 1393  0 753       640   −6.74 · 10−7
                          106 13.82 1672  0 1031      641   −1.01 · 10−6
and, against it, the pointwise predictions and the positivity certificate:
                   X frac(νX < 0) Szegő pred. n− a-priori count cert. fraction
                  102       0.207          115.5          126.1          0.808
                  103       0.330          276.2          294.6          0.655
                  104       0.381          425.2          452.2          0.526
                  105       0.407          567.4          599.2          0.434
                  106       0.424          708.5          746.9          0.368

The discrepancy ∥E∥ = ∥GP − GZ ∥F rises from 8.9 × 10−6 to 8.3 × 10−5 down the table, so
every “negative” minimum eigenvalue sits at leakage level; the zero side has n− = 0 and rank
540, 642, 642, 642, 641, matching n+ (GP ) to within one or two in every row; and the proxy
certificate falls 0.785 → 0.341 alongside the honest one. The first row of the high window,
X = 102 on [1400, 2400] (907 zeros, d = 587 < 907), is strictly positive definite: n0 = 0,
min ev = +6.27 × 10−4 , with frac(νX < 0) = 0.111, Szegő prediction 65.1, a-priori count 72.5,
certificates 0.896/0.881.


                                               34
So across the brief’s whole range X = 102 , . . . , 106 the compressed Weil form, computed from
primes and Γ alone, has not one negative square, while its symbol νX is negative on 21–42%
of the window and both the pointwise Szegő count and the sign-change a-priori count climb
into the hundreds. The null space grows exactly as d outruns the ≈ 640 zeros in reach. The
planting experiment, restarted with its two thresholds, has not yet reported a row.


5     The dual: positive eigenvalues certify on-line zeros
5.1    Pullback inertia and the double count
The thought that has taken over is this. The negative index of a compression — the restriction
of the Weil form W to a finite-dimensional space V of admissible test functions — is useless as
an upper bound for off-line zeros, because pulling a Hermitian form back to a subspace can
only lose negative squares. But the same monotonicity, read for the positive index, points the
right way. This is potentially the main result of the line, and it will need to be red-teamed
hard; let me write it down.

The observation. Fix any subspace V of admissible test functions, and a “reach interval”
I ′ : a height interval outside which the transforms hf , f ∈ V , are negligibly small. Write the
restricted Weil form as

                                          W |V = ev∗ Q ev + Tail,
                      ′
where ev : V → CZ is evaluation of hf at the distinct zero-points γ with heights in I ′ (Z ′
denoting that finite set), Tail is the contribution of all zeros with heights outside I ′ , and Q is a
direct sum of blocks. Each distinct on-line zero, of any multiplicity m, gives a 1 × 1 block (m)
— one positive square; each distinct off-line pair {γ, γ̄} = {ρ, 1 − ρ̄} of multiplicity m gives the
block                                                 !
                                               0 m
                                               m 0
of signature (1, 1) — the hyperbolic pair of Theorem 1.
Lemma 5.1 (inertia under pullback). For any linear map A and Hermitian form Q,
n+ (A∗ QA) ≤ n+ (Q), where n+ denotes the positive index. [If A∗ QA > 0 on a subspace U
then A|U is injective and Q > 0 on A(U ).]
Put any Hilbert structure on V and let θ > ∥Tail|V ∥op . Define the robust positive index

                            nθ+ (W |V ) := #{eigenvalues of W |V > θ}.

By Weyl’s inequality and Lemma 5.1, writing Qreach for Q (the block form over the zero-points
in reach),

                          (P)         nθ+ (W |V ) ≤ n+ (ev∗ Q ev) ≤ n+ (Qreach )
                                                        ′     dist ′
                                                = ndist
                                                   on (I ) + npair (I ),

where ndist
         on (I ) is the number of distinct on-line zeros with height in I and npair (I ) the number
              ′                                                          ′     dist ′

of distinct off-line pairs there. On the other hand the Riemann–von Mangoldt count N (I ′ ) is
taken with multiplicity and counts both members ρ, 1 − ρ̄ of an off-line pair, which share a
height:

                                (N)       N (I ′ ) ≥ ndist ′       dist ′
                                                      on (I ) + 2 npair (I ).


                                                     35
Subtracting (P) from (N),
                                          ′        ′
                                   pair (I ) ≤ N (I ) − n+ (W |V ),
                                                         θ
                                  ndist
                                        ′                       ′
                                   on (I ) ≥ 2 n+ (W |V ) − N (I ).                                 (∗)
                                                θ
                                  ndist

In words: every robustly positive eigenvalue of the compressed Weil form beyond N/2 certifies
a distinct on-line zero. An off-line pair “wastes” one of its two zeros as a negative square; this
is Theorem 1 read from the positive side, and it needs no visibility hypothesis and no positivity
— inertia replaces both.
The brief’s item (3) asked whether the negative-index route could reproduce a positive-
proportion theorem. The route it proposed — an upper bound on the negative index from sign
changes of νX — is dead. The mechanism I am writing down now, pullback inertia plus the
double count in (N), is not in the brief or in any of the reports I read.

5.2    A certificate computable from primes alone
Two prime-computable numbers bound the positive index. Let R be the matrix of
W |V in an orthonormal basis of V , and d = dim V .
Lemma 5.2 (Cauchy–Schwarz count).

                                                      (tr R − θd)2+
                                       nθ+ (R) ≥                    .
                                                          tr(R2 )

[With S := λ>θ λ ≥ tr R − θd, the sum over eigenvalues λ of R exceeding θ, Cauchy–Schwarz
            P

gives S 2 ≤ nθ+ λ>θ λ2 ≤ nθ+ tr R2 .]
               P

Both traces are prime-side quantities. With ν = νX   full the full prime-side density introduced

earlier (the pole term of the explicit formula absorbed as a density), and KV the reproducing
kernel of the space V̂ of transforms in L2 (dτ /2π),
                                       Z
                              tr R =       KV (τ, τ ) ν(τ ) dτ,
                                       ZZ
                             tr R2 =        |KV (τ, τ ′ )|2 ν(τ ) ν(τ ′ ) dτ dτ ′ ,

both finite computations with the primes ≤ X = eL and Γ. Hence what I will call the certificate:
Theorem 3 (finite certificate). For every L, every height window I and every admissible V
(supports in [−L/2, L/2], transforms concentrated on I up to the reach interval I ′ ),

                                                2(tr RV − θd)2
                              N0dist (I ′ ) ≥                  − N (I ′ ),
                                                    tr(RV2 )

where N0dist (I ′ ) is the number of distinct on-line zeros with height in I ′ , RV is the matrix R for
the space V , and θ is any upper bound for the tail norm; everything on the right is computable
from primes and Γ, plus the Riemann–von Mangoldt count.
Reading the certified-positive column of the low window of the index grid in this light: primes
≤ 100 certify ≥ 41% of the 639 zeros in [50, 1000] as on the line and distinct; primes ≤ 106
certify ≥ 92%. (This is an inference from the certified fractions 0.808 and 0.368 against d and
N ; a dedicated experiment is next.) Inside the RH-verified range this is only a consistency
check; the point is the asymptotic version.


                                                     36
5.3    Asymptotics in the Montgomery–Vaughan range
Set-up. Take I = [T, 2T ] and l := log(T /2π), so that N (I) ∼ |I| l/2π; put L = λl with
0 < λ ≤ 1, so X = eL = (T /2π)λ ; and let V be the space of functions time-limited to
[−L/2, L/2] and band-limited to I — d ∼ L|I|/2π prolate functions, or a tapered Gabor frame.
The constants below are for the sharp cutoff, where

                             KV (τ, τ ′ ) ∼ DL (τ − τ ′ ) 1I (τ )1I (τ ′ ),
                                            sin(Lx/2)
                                                                Z
                               DL (x) =                 ,         DL 2
                                                                          = 2πL,
                                               x/2

and FL := DL2 /2πL is the Fejér kernel, with F̂ (u) = (1 − |u|/L) . Split the density as
                                               L                 +
ν = m + P + Π with
                   ϑ′          1        1       τ
               m=      +             ∼    log        (smooth),
                   π     2π( 4 + τ )
                             1    2    2π      2π
                      1 X
                P =−        Λ(n) n−1/2 cos(τ log n),
                     π n≤X
                      1    Xs − 1
                Π=      Re        = O(T λ/2−1 ) pointwise on I,                    s = 21 + iτ
                      π      s
(here ϑ is the Riemann–Siegel theta function, written θ in R4’s formula; I write ϑ in this
computation to keep θ for the threshold).
                                                                 √
              Since       IP =O            Λ(n)n−1/2 / log n = O( X/L) and I Π = O(T λ/2 ),
                      R                P                                 R
The trace.

                                                                              l
                  tr R = L |I| ⟨m⟩I 1 + O(T λ/2−1 ) ,               ⟨m⟩I =      + O(1),
                                                              
                                                                             2π
where ⟨m⟩I denotes the average of m over I.

The second moment. Expand
                            ZZ
                tr R2 =                DL (τ − τ ′ )2 mm′ + mP ′ + P m′ + P P ′ + . . . ,
                                                                                          
                                 I×I

primes on m, P denoting evaluation at τ ′ . The mm′ term gives 2πL|I|⟨m⟩2 (1 + O(1/l2 )), since
m varies by O(1/T ) over the width 1/L of DL   2 . In P P ′ the diagonal n = n′ , evaluated with

the Fourier transform of DL
                          2 , is


                 L|I| X Λ(n)2     log n  L|I|  L2 L2 
                                1−        =               1 + O(1/L)
                                                                    
                                                    −
                  π n≤X n            L      π     2   3
                                                            |I|L3
                                                        =         1 + O(1/L) ,
                                                                            
                                                              6π
by n≤x Λ(n)2 /n = (log x)2 /2 + O(log x) (the prime number theorem with any error term).
   P

The off-diagonal I control — from memory, with no way to check the constant here — by the
Montgomery–Vaughan generalized Hilbert inequality
                           X         bn b̄n′      3π X |bn |2                       1
                                                ≤             ,          δn ≥         ,
                           n̸=n′
                                 log n − log n′    2 n δn                          2n


                                                        37
applied with |bn | ≤ an (2πL)1/2 , an = Λ(n)n−1/2 : the off-diagonal is O L           n≤X Λ(n)
                                                                                              2       =
                                                                                      P           

O(LX log X), and its ratio to the diagonal is
                              X log X 
                         O                   = O(T λ−1 l−1 ) → 0           (λ ≤ 1),
                                  |I|L2
                                                                         √
even for λ = 1 + o(1) provided X = o(T L). The cross term mP ′ is O(l X) = o(|I|Ll2 ) after
integrating m cos(τ log n) by parts; the Π terms are negligible for λ ≤ 1. So
                                                   h              L2 i
                                 tr R2 = 2πL|I| ⟨m⟩2 +                 (1 + o(1)),
                                                                 12π 2
                            (tr R)2    λ N (I)
                                    =           (1 + o(1)).
                             tr R 2   1 + λ2 /3

Consistency check under RH. Under RH together with Montgomery’s pair-correlation
theorem — which covers exactly this Fourier range, |α| ≤ λ ≤ 1 — the same statistic evaluated
on the zero side is
                                                      (LN )2
                                                                       ,
                                           2πL       γ,γ ′ FL (γ − γ )
                                                                    ′
                                                 P


with
                                                     hL           l   1  L L2 i
                                 FL (γ − γ ′ ) = N           +
                         X
                                                                    −      −
                         γ,γ ′
                                                       2π        2π π 2      6l
                                                        l     λ2 
                                              =N            1+      ,
                                                       2π      3
the same number. So under RH the bound of Lemma 5.2 is exactly the classical Cauchy–
Schwarz consequence of Montgomery’s theorem, “Ndistinct ≥ N 2 / m2ρ ≥ 34 N ” at λ = 1. The
                                                                    P

prime-side evaluation is Montgomery’s prime-side computation, which never needed RH; RH
was needed classically only to interpret the zero side as a sum over real γ with positive weights.
Inertia (Lemma 5.1) removes that need, at the price 3/4 → 2 · 43 − 1 = 12 .

5.4    The claimed one-half theorem
Theorem 4 (claimed; see the red team to come). Unconditionally, as T → ∞, for every
fixed λ ∈ (0, 1],
                                                   2λ              
                      N0dist ([T, 2T ]) ≥                 − 1 − o(1) N ([T, 2T ]),
                                                 1 + λ /3
                                                      2


and at λ = 1,

                                 N0dist ([T, 2T ]) ≥ ( 12 − o(1)) N ([T, 2T ]).

That is, at least half of the nontrivial zeros (counted with multiplicity in N ) are accounted for
by distinct zeros
              √ on the critical line; the bound is nontrivial exactly when 2λ/(1 + λ /3) > 1,
                                                                                         2

i.e. λ > 3 − 6 = 0.551. For comparison, from memory and unverified offline: Levinson,
Conrey, Bui–Conrey–Young and Pratt–Robles–Zaharescu–Zeindler give N0 ≥ 0.4173N and
N0simple ≥ 0.407N . So this claim goes beyond the brief’s benchmark Noff ≤ 0.6N and past the
records I remember. The ingredients: the Weil explicit formula for compactly supported tests
(unconditional); Riemann–von Mangoldt; Lemma 5.1; Lemma 5.2; the Montgomery–Vaughan
mean value theorem; the asymptotics of Λ2 /n; Landau–Pollak–Slepian kernel asymptotics
                                            P

for V ; and a tail bound.

                                                        38
Tail bound. The tail is the contribution of zeros with heights outside I ′ = I + [−D0 , D0 ].
For unit f ∈ V , far on-line zeros contribute   |hf (γ)|2 ≥ 0; far off-line zeros contribute
                                              P

2 Re hf (γ)hf (γ̄), with

       |hf (t − iy)| = fd
                        eyu (t)
                   ≤ eyL/2 × decay of the transform of f eyu at distance ≥ D0 from I ,
                                                                                            

f eyu being smooth and compactly supported. With a Cc∞ (Gevrey) taper that decay is of type
exp(−(D0 /w)1/2 ) with w ∼ 1/L; also eyL/2 ≤ X 1/4 = T λ/4 , and the zeros up to height T 2
number O(T 2 l). So D0 = (log T )C gives ∥Tail∥ ≤ T −A ; take θ = T −A , so that θd is negligible
and N (I ′ ) = N (I)(1 + O(D0 /T )). The sharp-cutoff and Kaiser windows I use numerically
decay only algebraically times e−β — irrelevant numerically given the reach margin, but the
theorem should be stated with a Gevrey taper on an edge layer of width o(L), which changes
the effective λ by o(1).

Why one half, and what would give more. Always n+ ≤ d = λN , and λ ≤ 1 + o(1) is
forced by the Montgomery–Vaughan diagonal evaluation (X = o(T log T )); for λ > 1 the prime
side involves off-diagonal prime-pair sums, the Hardy–Littlewood/Montgomery-conjecture
range. Within λ ≤ 1 the only loss is the Cauchy–Schwarz step of Lemma 5.2: under RH
the true n+ is d = N (semi-local Weil positivity at level X = T /2π). Any prime-side proof
that a fraction 1 − η of the eigenvalues of RV exceed θ would give N0dist ≥ (1 − 2η)N ; but
the higher moments tr Rk are diagonal-dominated only for kλ < 2 (the Hughes–Rudnick
mock-Gaussian range, again from memory), which is useless since I need λ → 1. In one line:
the proportion on the line is at least 2×(certified-positive fraction of the level-T /2π Weil
form) −1; Cauchy–Schwarz certifies 3/4, whence 1/2.


6     Testing the certificate; the one-half claim for referees
6.1   First numerics for the prime-side certificate
Now to test the certificate — the prime-computable lower bound n+ ≥ (tr R)2 / tr(R2 ) of
Lemma 5.2, fed into the inequality N0dist (I ′ ) ≥ 2nθ+ − N (I ′ ) of the dual argument — and with
it the asymptotic law
                                       (tr R)2         λN
                                                 ∼
                                         tr R2      1 + λ2 /3
against actual zeros. I use the same Kaiser–Gabor compression as before, i.e. the restriction of
the Weil form to the span of atoms φL (u)e−iτk u : Kaiser parameter β ∈ {4, 8}, centres oversam-
pled at spacing 2π/(1.25L) over the height window I = [T0 , T1 ], the family orthonormalised
with respect to the Plancherel mass matrix M (mass-matrix eigenvalues below 10−6 of the top
dropped), and                       √
                                      T0 T1
                            l = log         ,     L = λl,        X = eL .
                                      2π
For each window [300, 600], [600, 1200], [1200, 2400] and each λ ∈ {0.6, 0.8, 1.0, 1.2, 1.5} I
compute: the statistic C := (tr R)2 / tr(R2 ) on the prime side and, for validation, on the exactly
positive-semidefinite zero side; the true zero-side positive index n+ (eigenvalues above 10−6 of
the top); and two predictions for C, the continuum prediction and the asymptotic law,
                             ⟨m⟩2                      L|I|
         Ccont = dfull                ,      dfull =        (the sharp-cutoff dimension),
                     ⟨m⟩2 + L2 /12π 2                  2π
                  λ N (I)
          Claw =           ,
                 1 + λ2 /3

                                                39
where ⟨m⟩ is the window average of the smooth part m of the density. I also check the
Montgomery–Vaughan diagonal directly: with the prime-side density split as ν = m + P ′ + Π
(smooth part, prime sum, pole density), I compare the measured tr(RP2 ′ ) — the second moment
of the compression of the prime-sum part alone — with its n = n′ prediction

                                1 X Λ(n)2
                                          wV (log n),
                               2π 2 n≤X n
                                          X Z                              2
                               wV (x) =          ψ̂j (τ ) ψ̂k (τ ) eiτ x dτ ,
                                           j,k


the sum running over the orthonormalised transforms ψ̂j . The certified proportion of distinct
on-line zeros is (2C − N (I ′ ))/N (I ′ ), where the reach interval I ′ is the window widened by
the distance beyond which the atoms’ transforms are numerically negligible; it is set against
the asymptotic value 2λ/(1 + λ2 /3) − 1. I expect in advance that the Kaiser taper makes
the effective dimension d < dfull , so that the finite-β certified proportion should sit below the
asymptotic one.
The first two rows come back, on [300, 600] at λ = 0.6 (L = 2.53, X ≈ 13, N (I) = 203). With
β = 4 (d = 127, N (I ′ ) = 274) the statistic collapses: Cprime = 10.0 and Czero = 9.1 against
Ccont = 108.0 and Claw = 108.7, Montgomery–Vaughan diagonal measured/predicted 13.7/13.7,
certified proportion −0.927 versus the asymptotic +0.071. With β = 8 (d = 124, N (I ′ ) = 278)
it behaves: Cprime = Czero = 113.3, n+ = 124, diagonal 5.1/5.1, proportion −0.185 versus
+0.071. The planted-zero scan has so far produced nothing.
The β = 4 collapse and the crude choice of I ′ tell me that two things have to be done
honestly: the choice of taper, and an actually computed tail. The window function on
[−L/2, L/2] is now generic — Kaiser(β), a Tukey flat-top with cosine ramp fraction a, or a
bump exp − p(1/(1 − x2 ) − 1) (essentially Cc∞ ) — with its transform tabulated by quadrature
on [0, 80]. Each atom is assigned a reach radius r1 , outside which less than 10−10 of its energy
lies; then I ′ := [T0 − r1 , T1 + r1 ], the tail is the zero-side Gram matrix of the true zeros outside
I ′ , actually computed, and the robustness threshold is

                                    θ := max 2∥Tail∥, 10−8 · scale ,
                                                                       


scale being the top zero-side eigenvalue. The certificate is

                    (tr R − θd)2+                                               2Cθ − N (I ′ )
            Cθ :=                     (prime side),               propcert :=                  ,
                        tr R2                                                      N (I ′ )

reported alongside the zero-side C, the true robust positive index nθ+ (which in the RH-verified
range is min(d, N (I ′ ))), the prime-versus-zero eigenvalue discrepancy maxj |λj (RP ) − λj (RZ )|
(the quadrature error, which must be far below the θ-scale features), the continuum prediction
and the diagonal check. Windows [600, 1200] and [1200, 2400]; tapers Kaiser 8, Kaiser 12,
Tukey 0.5, Tukey 0.25, bump 0.5; λ ∈ {0.6, 0.8, 1.0, 1.15, 1.3, 1.6, 2.0}. (Editorial observation:
the grid runs past λ = 1, beyond the range the diagonal evaluation covers; nothing is written
about it here.)
First rows, Kaiser 8 on [600, 1200] (N (I) = 472):
             λ    X   d Cθ (prime) / C(zero)          nθ+ MV meas/pred propcert / asym
            0.60 19 285     260.1 / 260.1             285  16.6 / 16.6 −0.130 / +0.071
            0.80 51 379     321.8 / 321.8             379  41.2 / 41.3 +0.076 / +0.319
            1.00 135 472    367.6 / 367.5             472  82.6 / 82.8 +0.229 / +0.500


                                                  40
Prime and zero sides agree to the printed digit; the tail is negligible (θ = 10−8 of scale,
eigenvalue discrepancy from 5 · 10−3 down to 10−4 ); the Montgomery–Vaughan diagonal
prediction matches the measured tr RP2 ′ to well under one percent; and positive certificates
appear from λ = 0.8 on. But the algebraically decaying Kaiser atoms have reach r1 ≈ 80, so
N (I ′ ) = 598 against N (I) = 472. (Editorial: presumably it is this inflated N (I ′ ), rather than
the form, that depresses the certified proportions; the record does not say so in words.)
So I loosen the reach criterion to the radius outside which less than 10−5 of the atom’s energy
lies — legitimate now that the actual tail norm is computed and fed into θ — put the bump
taper first (then Tukey 0.5, Tukey 0.25, Kaiser 12), and start again.

6.2    Bump-taper rows, cluster counts and synthetic controls
The bump(0.5) rows on [600, 1200] (N (I) = 472) come back. The reach is now r1 = 25.8 falling
to 13.7 as λ grows, so N (I ′ ) runs from 512 down to 494; and with an essentially Cc∞ taper
there is a genuine tail, θ ≈ 5 · 10−2 down to 2 · 10−2 of scale, so the prime-side Cθ sits visibly
below the untruncated zero-side C:
          λ    X   d Cθ (prime) / C(zero) nθ+ (true) MV meas/pred              propcert / asym
         0.60 19 276     217.2 / 253.7       276      14.7 / 14.7              −0.152 / +0.071
         0.80 51 367     260.0 / 315.4       366      36.8 / 36.8              +0.036 / +0.319
         1.00 135 457    315.5 / 362.1       447      73.7 / 74.0              +0.270 / +0.500
         1.15 282 525    355.3 / 388.0       477     114.3 / 114.8             +0.439 / +0.596

The prime/zero eigenvalue discrepancy stays at 10−4 , three orders of magnitude below θ, and
the Montgomery–Vaughan diagonal prediction for tr RP2 ′ matches the measured value to well
under one percent throughout.
The index grid has meanwhile finished, ending exactly on the reading I fixed for it in advance:
n− (GP ) = 0 throughout; d − rank ≈ d − #zeros exact null directions whenever d > #zeros;
the symbol νX negative on 20–45% of the window; the Szegő/pointwise prediction and the
a-priori bound “off by everything”.
The cluster/multiplicity experiment (zero side plus plants at t0 = 400, δ = 0.2) has also
reported. At L = 10 (d = 573): a single quadruple gives n− = 1; a double zero (weight 2) at
the same point gives n− = 1 — multiplicity invisible, as Theorem 1 says; two depths 0.2 and
0.35 at one ordinate give 2; two quadruples at t0 ∓ ε/2 give n− = 1 for ε = 0.01, 0.03 and 2 for
ε ≥ 0.1 (the resolution scale being 2π/L = 0.63); five quadruples spaced ε apart give

              n− = 1, 2, 2, 2, 4, 5, 5, 5   for ε = 0.01, 0.03, 0.1, 0.3, 0.6, 1.0, 2.0, 4.0.

At L = 14 (d = 804, 2π/L = 0.45) two quadruples already separate at ε = 0.01, and five
give 2, 2, 3, 4, 5, 5, 5, 5. This is the picture of the cluster analysis in the visibility section: tight
clusters merge into fewer negative squares and split as L grows, and coincident zeros never add
rank.
The certificate needs no zeros, so I can go much higher than the zero table allows. I set
up a prime-side-only evaluation at larger heights: windows [9000, 10000] and [48000, 50000],
λ ∈ {0.7, 0.85, 1.0, 1.1}, a Tukey(0.2) flat-top taper at the critical spacing 2π/L (oversampling
q = 1.0), M -orthonormalised with tolerance 10−6 . The statistic C = (tr R)2 / tr R2 is computed
from the full prime-side density νX full alone; I compare C/N (I) with the law λ/(1 + λ2 /3) and

with the continuum prediction, and report the certified proportion as 2C/N (I ′ ) − 1, taking
N (·) to be the Riemann–von Mangoldt main term ϑ(T )/π + 1 (ignoring |S(T )| < 1, an O(1)),
with no θ/tail correction at these heights.


                                                   41
I want a control on the inertia logic itself, since inside the RH-verified range everything is
trivially consistent. So I build synthetic zero-side configurations on [600, 1200] with the same
kind of family (Kaiser β = 10, spacing 2π/(1.25L), 504 true zeros within reach) and, for each,
compute the configuration’s zero count Nconf , the theoretical positive index n+ (Q) of the block
form, the numerical nθ+ (R) and nθ− (R), the statistic C = (tr R)2 / tr R2 , and the would-be
certificate 2C − Nconf , which by the inequality (∗) of the dual argument must never exceed the
true number ndist
                on of distinct on-line zeros. The configurations:

(a) the true zeros, all on-line;
(b) consecutive zeros paired into an off-line pair at their midpoint ∓ia, with a = 0.02, 0.1, 0.3,
    or a = half the gap;
(c) “L(s) = ζ(s + a)ζ(s − a)”: every zero doubled into γ ∓ ia, a = 0.05, 0.25 (zero percent on
    the line, Nconf = 1008);
(d) a quarter of the zeros kept on-line, the rest paired at depth 0.1 (true ndist
                                                                             on = 126, Nconf =
    378).
The results, for λ = 0.8/1.0/1.3 (d = 368/459/595):
(a) nθ− = 0, C = 315.4/362.0/405.4, 2C − N = +126.7/ + 220.0/ + 306.8, comfortably below
    504.
(b) nθ+ (R) = 238–241 ≤ n+ (Q) = 252 with nθ− = 129/ ≈ 220/ ≈ 238, and 2C − N between
    −43.8 and −260.3 for fixed a; for half-gap pairing C = 26.6/4.4/0.2 and 2C − N =
    −450.7/ − 495.2/ − 503.7; the truth is 0.
(c) nθ+ = 367–476 ≤ 504, 2C − N = −205.1, . . . , −409.9, truth 0 — and notably, at λ = 0.8
    the shallow doubling a = 0.05 gives C = 314.8 with nθ− = 0, essentially the true-zero value
    315.4. (Editorial: there the inequality holds only because Nconf is doubled; the record does
    not remark on this.)
(d) 2C − N = −128.8/ − 123.1/ − 114.5 against the truth 126.
So the inequality never over-certifies.
The large-height prime-only run (N (I) = 1165.1 and 2852.6 for the two windows):
                   window       λ     X       d  C/N (I)    law     prop / asym
                [9000, 10000]  0.70 168      814  0.613    0.602   +0.184 / +0.203
                               0.85 504      988  0.699    0.685   +0.359 / +0.370
                               1.00 1510    1162 0.766     0.750   +0.496 / +0.500
                               1.10 3139    1278 0.802     0.784   +0.569 / +0.568
                [48000, 50000] 0.70 530     1991 0.610     0.602   +0.202 / +0.203
                               0.85 2033    2417 0.695     0.685   +0.374 / +0.370
                               1.00 7797    2843 0.762     0.750   +0.510 / +0.500
                               1.10 19104   3127 0.798     0.784   +0.582 / +0.568

The prime-only statistic tracks λ/(1+λ2 /3) to about two percent and gives a certified proportion
of about +0.50 at λ = 1. (Editorially: the λ = 1.1 rows lie beyond the λ ≤ 1 range that
my own diagonal evaluation covers, and at these heights there is no zero-side validation;
nothing is written about either.) One more bump row on [600, 1200]: λ = 1.30 (X ≈ 588,
d = 593), Cθ = 361.3 versus C(zero) = 406.0, diagonal 168.7/168.5, propcert = +0.469 versus
the asymptotic +0.663.

6.3    Measured visibility thresholds for planted off-line zeros
The planted-zero scan with its two thresholds is now complete, and I can read off how soon
a planted quadruple 12 ± δ ± it0 added to the 2000 true zeros produces a negative square in
the compressed form. The annihilation threshold L∗ann (first level with an eigenvalue below
−10−8 of scale) is small and almost independent of the depth δ: in add mode 3.25–3.50 at

                                               42
t0 = 100, 3.75–4.50 at 400, 4.75–6.50 at 1000, 5.25–7.50 at 2200 (slightly lower in replace
mode), with the offending eigenvalue at 10−8 –10−4 of scale — growing with height roughly like
log(t0 /2π) = 2.77/4.15/5.07/5.86.
The robust threshold L∗rob (an eigenvalue below −10−3 of scale) does feel the depth: at t0 = 100
in add mode it is 12.75 (δ = 0.02), 8.50, 6.75, 5.50, 5.00, 4.50 (δ = 0.45); at t0 = 400 it runs
from 13.75 down to 4.25; at t0 = 1000 and 2200 with δ ≤ 0.05 in add mode (and at 2200,
δ = 0.02 in replace mode) it is not reached up to L = 14. The least-squares fits in add mode:

                               L∗ann ≈ 1.123 δ −0.066 log(t0 /2π)0.889 ,
                               L∗rob ≈ 1.618 δ −0.336 log(t0 /2π)0.599 .
                                         √
Both lie far below the worst-case law n1 + 1/δ of Theorem 2 printed alongside (50–100 at
δ = 0.02), and the robust threshold sits somewhat above the cube-root average-spacing law
(8.2–10.5 at δ = 0.02) that I had identified with R4’s planting law; the fitted δ-exponent −0.34
is neither Theorem 2’s −1 nor the average law’s −2/3. The cluster experiment’s L = 6 block
(d = 345) repeats: single quadruple 7→ 1, double zero 7→ 1. Nothing new from the other two
runs.

6.4    The one-half claim written out for referees
Now to write the claimed Theorem 4 out self-contained, for hostile refereeing — the statement
being that at least one half of the nontrivial zeros of ζ are on the critical line, as distinct zeros.
This goes into a separate proof file addressed to referees; here is its content.

Notation and inputs. Zeros ρ = β + it with multiplicity mρ , and γρ := (ρ − 12 )/i =
t − i(β − 21 ); N (a, b) counts zeros with a < t ≤ b with multiplicity (Riemann–von Mangoldt:
N (0, T ) = (T /2π) log(T /2πe) + O(log T )); N0dist (a, b) is the number of distinct points 12 + it,
a < t ≤ b, with ζ( 12 + it) = 0. Test functions are f ∈ Cc2 (R), with hf (z) = f (u)eizu du entire
                                                                                R

and |hf (z)| ≪ ∥f ′′ ∥1 e| Im z|L/2 /|z|2 , so that

                                 W (f, g) :=            mρ hf (γρ ) hg (γ̄ρ )
                                                    X

                                                    ρ

converges absolutely; it is Hermitian by reindexing ρ → 1 − ρ̄ (γ → γ̄, multiplicities preserved).
The explicit formula (Weil, unconditional), for supp f, g ⊂ [−L/2, L/2], X = eL , s = 12 + iτ :
                                       Z
                         W (f, g) =        hf (τ ) hg (τ ) νX (τ ) dτ,
                                        R
                                       ϑ′ (τ )           1           1          Xs − 1
                           νX (τ ) =            +                 + Re
                                           π        2π( 14 + τ 2 ) π              s
                                               1 X Λ(n)
                                           −        √ cos(τ log n),
                                               π n≤X n

the pole term having been rewritten as a density exactly as in the pole-term derivation
earlier, and “Verified numerically to 1e-6..1e-9 against Sum_gamma over 2000 zeros” by the
compression computation.

Lemmas. Lemma 1 (inertia under pullback): for a linear map A and Hermitian form Q,
n+ (A∗ QA) ≤ n+ (Q) — if A∗ QA > 0 on U then A|U is injective and Q > 0 on A(U ). Lemma 2
(Cauchy–Schwarz count): for Hermitian R of size d and θ ≥ 0, if tr R > θd then
                                                        (tr R − θd)2
                                       nθ+ (R) ≥                     ,
                                                           tr(R2 )

                                                        43
since S := λi >θ λi ≥ tr R − θd > 0 and S 2 ≤ nθ+ tr R2 . Lemma 3 (Weyl): #{λi (A + E) >
             P

θ} ≤ #{λi (A) > θ − ∥E∥}.

Set-up. T large, l = log(T /2π), I = [T, 2T ], λ ∈ (0, 1], L = λl, X = (T /2π)λ . The space
V is spanned by fk (u) = φ(u)e−iτk u with τk = T + 2πk/L, 0 ≤ k < d = ⌊LT /2π⌋, where
φ ∈ Cc2 [−L/2, L/2] equals 1 on [−(1 − η)L/2, (1 − η)L/2] and has C 2 ramps of width ηL/2,
η = 1/ log l; then hfk = φ̂(· − τk ) with |φ̂(r)| ≪ (ηL)−2 |r|−3 for |r| ≥ 1 and φ̂(0) ∼ L. R is the
matrix of W in an orthonormal basis of V ; by Plancherel the mass matrix is Toeplitz with
symbol in [1 − O(η), 1], so M = L(Id + O(η)) and, with G the Gram matrix of W on the fk ,

                           R = L−1 (Id + O(η))−1/2 G (Id + O(η))−1/2 .

Step 1 (zero side: upper bound for the robust positive index). Take D0 = T 1/2
(any T c , c < 1, would do), I ′ = [T − D0 , 2T + D0 ], and split W |V = A + E according to
whether t ∈ I ′ . Grouping A by distinct points: a distinct on-line zero gives m |lt |2 , lz being the
evaluation functional f 7→ hf (z); a distinct off-line zero 12 + δ + it comes with 2 − δ + it (same
                                                                                    1
                                  ′                                     ¯      ¯
t, same m, both counted in N (I )), and together they give m lγ lγ ∗ + lγ ∗ lγ , the block m
                                                                                                0 m
                                                                                                      
                                                                                                    0
of signature (1, 1). Hence A = ev∗ Q ev with
                                                 ′     dist ′
                                  n+ (Q) = ndist
                                            on (I ) + npair (I ),
                                   N (I ′ ) ≥ ndist ′       dist ′
                                               on (I ) + 2 npair (I ).                             (1)

The tail needs only a norm bound, not visibility: for unit f = ck fk one has ∥c∥2 ≪ L−1/2 ; a
                                                                     P

zero at distance D ≥ D0 from I and depth < 21 has |hf (t − iy)| ≪ d1/2 eL/4 D−3 (ηL)−2 ; and
summing D−6 against zero density ≪ log(T + D),

                             ∥E∥ ≪ d eL/2 l D0−5 (ηL)−4
                                  ≪ T 1+λ/2−5/2+o(1) ≤ T −1+o(1) =: θ0 .

By Lemmas 3 and 1, for θ ≥ θ0 ,

                                     nθ+ (R) ≤ n+ (A) ≤ n+ (Q),                                    (2)

and from (1) and (2),
                                         ′                   ′
                                    on (I ) ≥ 2 n+ (R) − N (I ).                                   (3)
                                                 θ
                                   ndist

Step 2 (prime side: lower bound). Split νX = µ + P + Π on τ > 0:

                           ϑ′          1         1       τ
                        µ=     +             =      log     + O(τ −2 ),
                           π     2π( 4 + τ )
                                     1    2     2π      2π
                           1     Xs − 1
                        Π = Re           = O(X 1/2 /τ ),
                           π        s
                              1 X
                        P =−        an cos(τ log n),      an = Λ(n)n−1/2 .
                             π n≤X

The claim:

                      tr R = LT ⟨µ⟩I (1 + o(1)),
                                    h          L2 i                                l
                     tr R2 = 2πLT ⟨µ⟩2I +           (1 + o(1)),          ⟨µ⟩I ∼      ,
                                              12π 2                               2π
⟨µ⟩I denoting the average of µ over I. Sketch, suppressing the O(η) taper corrections.

                                                  44
 (i) With φ = 1 the transforms are Dirichlet kernels DL (x) = sin(Lx/2)/(x/2), and {fk } is
     orthogonal with ∥fk ∥2 = L. Poisson summation gives k DL (τ − τk )2 = L2 on I away from
                                                          P

     the ends (the transform of DL2 is 2π(L − |u|) , which vanishes at the aliasing points ±L),
                                                  +
     and Shannon sampling at the Nyquist rate gives

                 K(τ, τ ′ ) = L−1       DL (τ − τk )DL (τ ′ − τk ) = DL (τ − τ ′ ) on I × I,
                                    X

                                    k

      up to end effects  within O(T o(1) ) of the endpoints carrying a T −1+o(1) fraction of the traces.
      So tr R = L I ν and tr R2 = I×I DL (τ − τ ′ )2 ν ν ′ , plus ends.
                    R                 RR

 (ii) I P = O          n≤X Λ(n)n
                                  −1/2 / log n   = O(X 1/2 /L) and I Π = O(X 1/2 log 2), both
      R              P                                                R

      O(T λ/2 ) = o(T l).
(iii) The µµ′ term: µ is Lipschitz with constant O(1/T ) and DL          = 2πL, giving 2πLT ⟨µ⟩2I (1 +
                                                                   R 2

      O(1/l )).
            2

(iv) The P P ′ term: writing τ = τ ′ + x and splitting the product of cosines, the diagonal n = n′
      gives 21 T · 2π(L − log n)+ , hence

                                               T L X Λ(n)2     log n 
                                    DIAG =                   1−
                                                π n≤X n           L
                                               T L  L2       
                                           =            + O(L) ,
                                                π    6
     using n≤x Λ(n)2 /n = (log x)2 /2 + O(log x) [PNT]. The off-diagonal terms and the sum-
           P
                                                ′
     frequency bracket have τ ′ -integrals I eiτ w with w = log n∓log n′ ̸= 0, and the Montgomery–
                                          R

     Vaughan generalized Hilbert inequality with δn ≥ 1/(2n) and weights ≤ 2πLan gives
                                                         
                              OFF = O L2             Λ(n)2 = O(L3 X),
                                                X

                                               n≤X
                             OFF
                                  = O(X/T ) = O(T λ−1 ) → 0             (λ < 1).
                             DIAG
     At λ = 1 exactly, where X/T = 1/2π, I waver — “hmm; SAFE STATEMENT: for every
     fixed lambda < 1, OFF = o(DIAG); the bound at lambda → 1− is then a limit” — and
     then record a refinement: Montgomery–Vaughan applied with the T -length integral gives a
     ratio O(X/(T L)) → 0 even at λ = 1; either way λ → 1 is admissible in the limit.
 (v) The µP ′ cross term is O(lX 1/2 ) = o(T Ll2 ) by integration by parts (µ′ = O(1/T )).
(vi) The Π terms are pointwise O(T λ/2−1 ) on I and negligible.
 This proves the claim, and with θ = θ0 (so that θd = o(tr R)),

                                (tr R − θd)2     LT         ⟨µ⟩2I
                      nθ+ (R) ≥              =                        (1 + o(1))
                                    tr R2        2π ⟨µ⟩2I + L2 /12π 2
                                    λ
                              =           N (I) (1 + o(1)).                                         (4)
                                1 + λ2 /3

 The consistency remark once more: under RH the left-hand statistic is ( γ L)2 / γ,γ ′ DL (γ −
                                                                                P        P

 γ ′ )2 , and Montgomery’s pair-correlation theorem (Fourier support |α| ≤ λ ≤ 1) evaluates the
 denominator to N Ll(1 + λ2 /3) — the same value; (4) at λ = 1 is the classical “Ndistinct ≥
 N 2 / m2 ≥ 3N/4 under RH”. The evaluation is Montgomery’s prime-side computation, which
         P

 is unconditional; RH entered classically only to read the zero side as a positive sum over real γ,
 and Lemma 1 replaces that.


                                                     45
           N (I ′ ) = N (I) 1 + O(D0 /T + 1/l) , so from (3) and (4)
                                                
Step 3.
                                                    h      2λ                i
                     N0dist (T − D0 , 2T + D0 ) ≥                 − 1 − o(1)  N (I),
                                                        1 + λ2 /3
                             N0dist ([T, 2T ])
                        lim inf                ≥ 2 · 34 − 1 = 12 ,
                       T →∞   N ([T, 2T ])
                      √
nontrivial for λ > 3 − 6 = 0.5505; the o(1)’s are O(1/ log l) from the taper, O(1/L) from the
prime sums, and O(T λ−1 ) from Montgomery–Vaughan.
What is used: the explicit formula for Cc2 test functions, Riemann–von Mangoldt, the PNT in
the form n≤x Λ(n)2 /n = (log x)2 /2 + O(log x), the Montgomery–Vaughan Hilbert inequality,
           P

Poisson/Shannon for the sinc system, and Lemmas 1–3. What is not used: any zero-free region,
any density theorem, any numerical RH verification, any positivity of the Weil form. For
comparison, all from memory and unverifiable here: Selberg (positive proportion), Levinson
1/3, Conrey 0.4088, Bui–Conrey–Young 0.4105, Feng 0.4128, Pratt–Robles–Zaharescu–Zeindler
(2020) 5/12 = 0.4167, all counted with multiplicity; simple zeros on the line ≥ 0.407N ;
under RH ≥ 2/3 simple (Montgomery), ≥ 3/4 distinct (Cauchy–Schwarz), “later ~0.8467
distinct?? (from memory)”. An unconditional 1/2, distinct and on the line, would exceed every
unconditional record I remember; “hence maximal suspicion is warranted”, and the red team is
still to be written.


7     Second window; de Branges tilt; the red team
7.1    Second window also zero; certificate runs retuned
With the referee version set down, I go back to the index grid — the inertia (n− , n0 , n+ )
(numbers of negative, null and positive eigenvalues) of the Gram matrix GP of the Weil form
compressed to the Gabor space VL,T of windowed exponentials, computed from the primes
≤ X = eL and Γ alone — which has finished its second height window. On [1400, 2400] (907
zeros) the compressed form again has no negative square at any level:
                        X     d n− n 0 n +  min ev(GP ) frac(νX < 0)
                       102 587   0   0 587 +6.27 · 10−4        0.111
                       103 880   0   8 872 +8.71 · 10−10       0.249
                       104 1173  0 263 910 −8.37 · 10−8        0.331
                         5
                       10 1466   0 556 910 −2.81 · 10−7        0.371
                       106 1760  0 850 910 −8.25 · 10−7        0.395
The discrepancy ∥GP − GZ ∥F between the prime-side and zero-side Gram matrices lies be-
tween 1.1 · 10−5 and 9.9 · 10−5 , so the tiny negative minima are leakage; the zero-side ranks
587, 879, 910, 910, 911 match n+ (GP ) row by row. The pointwise quantities go the other way: the
“Szegő prediction” for n− (the fraction of the window with νX < 0, times d) climbs 65.1 → 695.9,
and the a-priori count of Proposition 2.1 restricted to the window climbs 72.5 → 725.6, while
the prime-computable certified-positive fraction (tr R)2 /(d tr R2 ) — R being the matrix of
W |V in mass-orthonormal coordinates — falls 0.896 → 0.783 → 0.665 → 0.560 → 0.480 (its
Fejér proxy 0.881 → 0.451).
Together with the [50, 1000] column this covers the whole of the brief’s range X = 102 , . . . , 106
on two windows: the honestly compressed Pontryagin index is identically zero everywhere I can
compute it, and it is computed from primes alone. The certificate run with the bump taper — the
certificate being the prime-computable Cauchy–Schwarz lower bound Cθ = (tr R − θd)2+ / tr R2
on the robust positive index, fed into N0dist (I ′ ) ≥ 2nθ+ − N (I ′ ) — has only reached the λ = 1.30


                                                    46
row already seen (Cθ = 361.3 on the prime side against C = 406.0 on the zero side, certified
proportion +0.469 against the asymptotic +0.663).
I decide to trim the certificate experiment and rerun it with a well-conditioned family: atom
spacing 2π/L instead of 2π/(1.25L), mass-orthonormalisation tolerance 10−3 instead of 10−6 ,
the tapers reduced to a Tukey window with ramp fraction 0.25 and a Kaiser window with
β = 12, and the Montgomery–Vaughan diagonal prediction skipped for λ > 1.15. I also want
the prime-only law C/N (I) → λ/(1 + λ2 /3) tested a long way above the zero table, so I set
up the same larger-height computation on the window [998000, 1000000] with λ ∈ {0.85, 1.0}
— again prime side only, N (·) taken from the Riemann–von Mangoldt main term, no tail
correction.

7.2    The de Branges tilt, recorded from memory
With those set going, two pieces of theory remain. The first is the brief’s de Branges/δ-tilt
suggestion, which I record but do not develop; everything here is from memory, with no lookup.
For a ∈ ( 12 , 1) put Ea (z) := ξ(a − iz); a zero ρ = β + it of ξ gives a zero of Ea in the upper
half-plane C+ exactly when β > a, and by the functional equation
                                 Ea# (z) := Ea (z̄) = ξ(1 − a − iz).
The kernel
                                           Ea (z)Ea (w) − Ea# (z)Ea# (w)
                             Ka (w, z) =
                                                    2πi(w̄ − z)
has, by the Kreı̆n–Langer factorisation of the generalized Schur function Ea# /Ea (unimodular
on R by the functional equation), exactly κa negative squares, where κa is the number of zeros
of Ea in C+ with multiplicity, i.e. N (β > a) over all heights. I recall, without being able to
check it here, Lagarias 2005: Ea is Hermite–Biehler for a ≥ 1 unconditionally, and for all a > 12
iff RH. So the family {Ea } realises the brief’s δ-tilt with multiplicity counted, unlike the Weil
form of Theorem 1.
But the compressions of Ka to span{Ka (·, xj )} at real sample points xj have Gram matrices
computable only from ξ on the two lines Re s = a and 1 − a — Riemann–Siegel, not a finite
prime sum. Their negative index is ≤ κa (the certificate direction only) and is bounded below
only by the number of Blaschke phase windings the sampling resolves, an m-fold zero at
depth y needing about m samples in a window of width y. So the count is again bounded
only by the number of samples: the same wall that the Weil-form compressions hit as an
upper-bound machine; and there is no analogue of the positive-index dual better than the
dual itself, because the positive squares of Ka are not tied to a zero count. R4’s observation
that da
      d
        log |ξ(a + it)/ξ(1 − a + it)| at a = 12 is 2πνX identifies the diagonal K1/2,X (x, x) of the
truncated kernel with νX — the same object as R4’s signed density.

7.3    Red team: empty for bounds, suspect as theorem
The second piece is the red team. On the negative index as an upper bound for off-line zeros —
Theorems 1 and 2 and the compression — my verdict is: empty, for structural reasons, not
Gibbs. The inequality κ(V ) ≤ Noff    dist always holds, which is the wrong direction; the reverse

needs visibility; visibility of everything below height T needs dim V ≳ N (T ) — the annihilation
regime L ∼ log(T /2π), with the measured threshold
                                 L∗ann = 1.12 log(t0 /2π)0.89 δ −0.07
—
√ and there the only a-priori bound, κ ≤ dim V , is trivial. In the sub-Landau regime L ∼
  log T /δ of Theorem 2, visibility holds only for isolated deep zeros (the interference obstruction),

                                                  47
clusters count once (the cluster experiment), multiplicity never (Theorem 1). Any prime-side
bound on κ(V ) that passes through pointwise sign information on νX is at least (L/2π) |{νX <
0}| ∼ 0.2–0.4 dim V — the Szegő and a-priori columns of the grid — while the true κ(V ) is 0
in every tested range, X = 102 , . . . , 106 , T ≤ 2400, from primes alone. R4’s 33–153 “negative
eigenvalues” belong to the warped-sinc operator, not to a compression of the Weil form. So I
retract R4’s headline as a statement about level-X Weil forms in the computed ranges: the
condition space is a Hilbert space there (as it must be under RH); it is Kreı̆n exactly iff RH
fails visibly.
On the dual and the claimed Theorem 4, the checks performed are:
(a) prime side = zero side for the Gram matrices to 10−6 –10−9 (relative eigenvalue discrepancy
    ∼ 10−4 after orthonormalisation);
(b) the inertia inequality nθ+ (R) ≤ ndist
                                      on + npair holds on every synthetic configuration with 0%,
                                            dist

    25%, 100% of zeros on the line, the would-be certificate 2C − N staying below the true
      on (all-paired: −50 to −495; “ζ(s ± a)”: −287 to −410; quarter on-line: −123 < 126);
    ndist
(c) the prime-only law C/N (I) → λ/(1 + λ2 /3) at T = 104 and 5 · 104 : 0.613/0.699/0.766/0.802
    and 0.610/0.695/0.762/0.798 against 0.602/0.685/0.750/0.784 at λ = 0.7/0.85/1.0/1.1,
    certified proportions +0.50, +0.51 at λ = 1, with T = 106 pending;
(d) Montgomery–Vaughan diagonal dominance measured directly, tr(RP2 ) against its n = n′
    prediction to 0.1–0.5%;
(e) under RH the bound coincides with Montgomery plus Cauchy–Schwarz (3/4 distinct), an
    independent consistency check of all constants.
Then the failure points a referee should target, in decreasing order of my own worry.
(1) “Too strong to be new”: the argument is short and uses 1970s tools. Either it is known
    — I do not know a reference; from memory the closest are Montgomery 1973 (under RH),
    Gallagher–Mueller, and Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh’s unconditional
    pair-correlation F (α) (2023/24), where as far as I recall no unconditional proportion on
    the line is drawn, presumably because extracting the diagonal from ρ,ρ′ needs a positivity
                                                                        P

    that fails for complex weights, and Lemma 1 (pullback inertia) is exactly what avoids that
    — or there is an error I cannot see. I looked    hardest at the block structure (an off-line
    pair supplies one positive square: yes, m 0 m ), at Riemann–von Mangoldt counting both
                                                   
                                                 0
    members of a pair (yes: ρ and 1 − ρ̄ are distinct nontrivial zeros at the same height), at
    Lemma 1 itself (two lines), at the reach/tail truncation (θ = T −1+o(1) suffices with the Cc2
    taper), and at the trace asymptotics (elementary, numerically
                                                                √ confirmed).
(2) Kernel end-effects in tr R with the pointwise-large |νX | ∼ X near λ = 1: bounded above
                               2

    using averages “(RT2 in scratch)” — a side computation of mine recorded nowhere else —
    and the finite computations, which contain all end effects exactly, match the law within
    2%; still, a fully written proof must do this estimate honestly.
(3) The Montgomery–Vaughan step at λ = 1 exactly: OFF/DIAG = O(1/L) with a crude
    explicit constant ∼ 36/L; for a clean statement take λ < 1 fixed and let λ → 1.
(4) The taper margin η → 0 and the reach margin D0 = T 1/2 : routine.
None of (2)–(4) can move the constant 1/2; only (1) can kill the result. And what Theorem 4 is
not: it is not a density estimate; it says nothing about multiplicities of on-line zeros; it cannot
exceed 1/2 without Hardy–Littlewood-type prime-pair input or a genuinely new positivity
input (as recorded under “why one half”); and the finite prime-side certificates of Theorem 3
have nil value inside the RH-verified range.


                                                48
7.4    Retuned certificate rows and the first row at 106
The retuned certificate run has produced its Tukey(0.25) rows on [600, 1200] (N (I) = 472).
With spacing 2π/L the atom reach — the radius beyond which an atom’s transform carries
less than 10−5 of its energy — drops from 28.8 to 9.0 as λ grows, the tail threshold θ is a few
10−4 of scale, and Cθ on the prime side agrees with the zero-side C to about four digits:
                     λ Cθ (prime) C(zero) MV meas/pred           propcert    asym
                    0.60 252.0     252.4    15.0/15.0            −0.025     +0.071
                    0.80 312.6     313.1    37.1/37.1            +0.233     +0.319
                    1.00 359.5     360.0    74.8/74.8            +0.438     +0.500
                    1.15 385.1     385.9   116.6/116.7           +0.556     +0.596
                    1.30 403.0     403.7        —                +0.635     +0.663
                    1.60 425.0     425.8        —                +0.738     +0.727
                    2.00 441.4     442.2        —                +0.816     +0.714
Here propcert = (2Cθ − N (I ′ ))/N (I ′ ) is the certified proportion of distinct on-line zeros on the
reach interval I ′ , and the last column is the sharp-cutoff asymptotic 2λ/(1 + λ2 /3) − 1. The
first Kaiser(β = 12) row, at λ = 0.6, gives C = 193.9 on both sides and certified proportion
−0.197.
And the first row at height 106 is in: λ = 0.85, L = 10.18, X = 26374, d = 3229, N (I) = 3812.3,
C = 2636.0, so C/N (I) = 0.691 against the law’s 0.685, certified proportion +0.371 against
the asymptotic +0.370.


8     Report and verdict: partial, with a claimed theorem
8.1    The verdict: negative route empty, its dual claims one half
Time to fix the verdict. What I am prepared to defend is PARTIAL — with one claimed
theorem that, if it survives refereeing, is the main output of this line. It rests on three points.
First, the global identity the brief conjectured is proven (Theorem 1), with the correction
the brief did not anticipate: the negative index of the Weil Hermitian form on Cc∞ equals
the number of distinct zeros with Re ρ > 12 ; an m-fold off-line zero is one negative square,
multiplicity is invisible. At finite level, κ(L) — the negative index on test functions supported
in [−L/2, L/2], i.e. of the form computable from primes ≤ X = eL — is finite, nondecreasing,
tends to κ, and RH ⇐⇒ κ(L) = 0 for all L.
Second, as an upper-bound machine for off-line zeros the negative index is empty, and not
because of Gibbs. (i) The correctly defined compressed index κ(X, T ) — the negative index of
the Weil form restricted to admissible test functions of support length ≤ log X with transforms
concentrated below height T — is identically 0 in every computable range, X = 102 , . . . , 106 ,
T ≤ 2400, and it is computed from primes alone; R4’s 33–153 negatives belong to a warped-sinc
operator that is not a compression of the Weil form. (ii) The inequality κ(V ) ≤ Noff     dist is

the wrong direction, and the reverse needs visibility, which for all zeros below T requires
dim V ≳ N (T ) — the annihilation regime L ∼ log(T /2π), with the measured threshold

                                 L∗ann = 1.12 log(t0 /2π)0.89 δ −0.07

— and there the only prime-side bound, κ ≤ dim V , is the trivial cluster count.√Below that
level, Theorem 2 makes an isolated zero of depth δ at height t visible once L ≥ C log t/δ, but
interference from unknown neighbours is uncontrollable, clusters count once, multiplicity never.
So to the brief’s ratio question: κ(X, T )/N (T ) → 0 in the data (it is 0), while any provable
prime-side bound is ≥ (L/2π) |{νX < 0}| ∼ 0.2–0.4 dim V . Empty.


                                                 49
Third, the dual works (claimed Theorem 4). Pullback inertia, n+ (A∗ QA) ≤ n+ (Q), gives for
any compression V (restriction of the Weil form to a finite-dimensional space of admissible test
functions), with “in reach” meaning heights in the interval I ′ on which the transforms of V are
non-negligible,

                      nθ+ (W |V ) ≤ #{distinct on-line zeros in reach}
                                         + #{distinct off-line pairs in reach},

while Riemann–von Mangoldt counts an off-line pair twice; hence

                                N0dist (I ′ ) ≥ 2 nθ+ (W |V ) − N (I ′ ).

On the prime side nθ+ ≥ (tr R)2 / tr(R2 ), two numbers computable from primes ≤ X; and with
V the space time-limited to [−L/2, L/2] and band-limited to [T, 2T ], L = λ log(T /2π), λ ≤ 1
(the Montgomery–Vaughan range),

                                  (tr R)2      λN
                                          =           (1 + o(1))
                                   tr R2    1 + λ2 /3

unconditionally — it is Montgomery’s prime-side pair-correlation computation, and under RH
it is the classical “≥ 3/4 distinct”. Consequence:

                                        N0dist ([T, 2T ])
                             lim inf                      ≥ 2 · 34 − 1 = 21 ,
                                         N ([T, 2T ])

against the unconditional record I know from memory and cannot check here, 5/12 = 0.4167
(Pratt–Robles–Zaharescu–Zeindler 2020). In the task’s own terms the relevant ratio is not
κ/N but n+ /N → 3/4 at X = T /2π — “c = 3/4 certified-positive” — giving proportion
2c − 1 = 1/2. And an explicit request goes with it: hostile referees, please attack the separate
proof file; my ranked worry list is the one written in the red team, the top worry being “too
short to be new”, not a located gap.
Behind the verdict stands the whole chain, which I restate compactly. The set-up and
Theorem 1, with its Gaussian-times-linear-times-interpolation-polynomial test functions for
the lower bound. The finite-level object done right: prime-side n− = 0 in every case, minimum
eigenvalue between −10−6 and +6 · 10−4 at the level of ∥GP − GZ ∥ ∼ 10−5 , with d − #zeros
exact null directions whenever d > #zeros — e.g. at X = 106 on [50, 1000], 1031 = 1672 − 641
— reproduced by the prime side to 10−6 , while νX < 0 on 21–42% of the same windows. So
the level-X condition space is a Hilbert space in range: the Gibbs dips of width 1/ log X sit
exactly at the resolution of admissible |h|2 and cancel, and R4’s Kreı̆n signature is a property
of the warped kernel sin π(NX (t) − NX (s)) /(π(t − s)), whose diagonal is νX (t) itself.
                                              

Then visibility: Theorem 2, the cube-root average-spacing law, annihilation once the local
dimension exceeds the local zero count, and the measured fits — and here I label the first as
R4’s law:

                                       L∗ann ∼ 1.12 δ −0.07 log(t0 /2π)0.89 ,
                             L∗rob (10−3 ) ∼ 1.6 δ −0.34 log(t0 /2π)0.6 .

The cluster counts: a double off-line zero gives n− = 1 at every L; two depths 0.2/0.35 at one
ordinate give 2; two pairs at δ = 0.2 are resolved iff ε ≳ (0.15–0.25) × 2π/L; five pairs give
1, . . . , 5 as εL grows. And the interference obstruction: no configuration-free visibility theorem
below the annihilation level exists.


                                                     50
Then the dual: the inequalities (P) and (N) and the Cauchy–Schwarz count, giving the finite
certificate (Theorem 3) — the prime-computable lower bound N0dist (I ′ ) ≥ 2(tr R − θd)2 / tr R2 −
N (I ′ ) — and the asymptotics

                                              LT l
                                     tr R ∼        ,
                                              2π
                                                       h l 2        L2 i
                                    tr R2 ∼ 2πLT                 +         ,
                                                         2π          12π 2
the second from the µ-µ term plus the Montgomery–Vaughan diagonal

                                  T L X Λ(n)2     log n  T L3
                                                1−        =     ,
                                   π n≤X n           L      6π

the off-diagonal being O(L2 X log X), hence negligible, by Montgomery–Vaughan, and the cross
and pole-density terms o(·) — whose RH-consistency is Montgomery’s F (α)-evaluation of
( γ L)2 / DL (γ − γ ′ )2 , the classical 3/4.
 P        P

Theorem 4 (claimed). For each fixed λ ∈ (0, 1],
                                                    2λ               
                        N0dist ([T, 2T ]) ≥                 − 1 − o(1)  N ([T, 2T ]);
                                                  1 + λ2 /3

at λ = 1, N0dist ([T, 2T ]) ≥ ( 12 − o(1))N ([T, 2T ]).
The evidence set against it: the prime-only law at T ∼ 104 and 5 · 104 already recorded;
the [600, 1200] zero-side cross-check (prime side = zero side to four digits; at λ = 1 certified
+0.44 with finite-window margins, true n+ = 455 ≥ C = 360); the synthetic controls (the
inequality never over-certifies); and the limits of the method — n+ ≤ dim V = λN with
λ ≤ 1 + o(1) forced by the diagonal evaluation, higher trace moments needing kλ < 2 — so that
1/2 = 2 · 34 − 1 is the ceiling with pair-correlation-range input, and every extra certified-positive
fraction η of level-(T /2π) Weil eigenvalues is worth +2η.
My answers to the brief’s numbered items, one by one.
(1) The global identity: proven, with the correction “distinct”; finite-level monotone conver-
    gence; the literature — Yoshida 1992, Bombieri 2000, Burnol — is from memory and
    unverified offline, and the multiplicity caveat is essential.
(2) κ(X, T ) concretely: defined and computed from primes, identically 0; nothing to fit,
    κ/N → 0 trivially. The informative prime-side spectral statistic is instead the certified-
    positive count (tr R)2 / tr R2 , a fraction 1/(1 + λ2 /3) of dim V (0.81 → 0.37 in the index
    grid as X grows past T ; → 3/4 of N at X = T /2π).                                  √
(3) A-priori bounds on κ from sign changes of νX : of size (L/2π) |{νX < c}| ∼ e4 X log X
    globally, ∼ 0.3 dim V in windows — useless, and provably so, since visibility holds iff
    dim V ≥ #zeros; the Turán/Nazarov count of sign changes the brief proposed bounds the
    wrong operator. But the positive-index dual gives an unconditional positive-proportion
    theorem (claimed 1/2), i.e. the “new proof architecture for Selberg’s theorem” the brief
    asked for, with a better constant than Levinson–Conrey-type methods, from the explicit
    formula plus the Montgomery–Vaughan mean value theorem plus linear algebra.
(4) The red team of the original danger: confirmed in the strong form — not “κ ∼ N (T ) by
    Gibbs” but “κ = 0 and unboundable below dim V ”; the ratio question is moot. For the red
    team of Theorem 4: checks (a)–(e) passed, residual risks ranked; the constant 1/2 cannot
    move, only the whole claim can fall.


                                                       51
The hedges once more, summarised. Everything “positive” in the numerics is RH being true
below 2515 (resp. 3 · 1012 ), stated as such, and the finite certificates inside that range certify
nothing new. Theorem 2’s constants are for a specific bump, and the measured laws are for a
finite Gabor family (hence upper bounds on true √  thresholds). For Theorem 4 I have not written
every end-effect estimate at λ = 1, where |νX | ∼ X pointwise, though the finite computations,
which contain all such effects exactly, match the law to 2%; the Montgomery–Vaughan constant
at λ = 1 is poor (OFF/DIAG ≲ 36/L, crude), so a clean statement takes λ < 1 fixed, then
λ → 1. The one thing I cannot exclude is that the result is already known, or that a step I
consider trivial hides an error. The three-line heart is: [the pair block has one positive square]
+ [Riemann–von Mangoldt counts the pair twice] + [n+ (A∗ QA) ≤ n+ (Q)].
The pending T ≈ 106 row at λ = 1 has also come in: L = 11.98, X = 158996, d = 3799,
N (I) = 3812.3, N (I ′ ) = 3841.3, C = 2885.7, so C/N (I) = 0.757 against the law’s 0.750,
certified proportion +0.502 against the asymptotic +0.500.
So the prime-only evidence at λ = 1 stands at C/N (I) = 0.766 (T = 104 ), 0.762 (T = 5 · 104 ),
0.757 (T = 106 ) against 0.750, certified proportions +0.50/ + 0.51/ + 0.50; and at T ∼ 106
for λ = 0.85/1.0: C/N (I) = 0.691/0.757 (law 0.685/0.750), certified +0.371/ + 0.502. These
belong in the verdict.
The certificate run with zero-side cross-check has also finished its Kaiser(β = 12) rows on
[600, 1200]. The statistic C agrees between prime and zero side to every printed digit,

 C = 193.9, 248.5, 295.7, 326.4, 352.0, 390.3, 418.5          (λ = 0.6, 0.8, 1.0, 1.15, 1.3, 1.6, 2.0),

with the tail threshold θ at most 10−5 of scale and the prime-versus-zero eigenvalue discrepancy
at most 6 · 10−5 , the Montgomery–Vaughan diagonal exact (5.7/5.7, 14.2/14.2, 28.8/28.8,
45.0/45.0), and certified proportions

                 −0.197, +0.033, +0.232, +0.363, +0.476, +0.640, +0.758,

lower than the Tukey family’s at each λ, the taper cutting the effective dimension (d =
203, . . . , 673 against dfull = 281, . . . , 937). (Editorial remark: the rows with λ > 1 lie outside
the λ ≤ 1 range of the asymptotic evaluation; nothing in the record comments on them.) The
first rows on the larger window [1200, 2400], Tukey taper, N (I) = 1077: at λ = 0.6 (X ≈ 29,
d = 624), C = 570.8/571.6 (prime/zero), certified +0.018 against the asymptotic +0.071; at
λ = 0.8 (X ≈ 88, d = 832), C = 710.6/711.9, certified +0.279 against +0.319.

8.2    Final verdict and hand-off
For anyone resuming this line I leave a pointer recording the outcome in my own framing:
the negative-index route is empty for upper bounds (κ(X, T ) = 0 from primes in all ranges;
visibility needs dim V ≥ #zeros); the dual gives the claimed N0dist ≥ ( 12 − o(1))N , which would
beat the 5/12 record if correct and carries “too short to be new” as its top risk. The advice:
start from the referee proof and the ranked risk list, and do not re-derive the κ(X, T ) = 0 /
warped-sinc diagnosis.
My closing message to the orchestrator, verdict first:
      Verdict: PARTIAL — negative-index route EMPTY as an upper-bound machine;
      its DUAL (positive-index inertia) yields a claimed unconditional theorem: ≥ 1/2
      of the zeros are on the line (as distinct zeros). Referees requested.
followed by the four findings.


                                                 52
(1) Theorem 1, proven by my own account: the negative index of the Weil Hermitian form
    on Cc∞ equals the number of distinct zeros with Re ρ > 12 , an m-fold off-line zero being
    one negative square, multiplicity intrinsically invisible; κ(L) finite, monotone, → κ; RH
    ⇐⇒ κ(L) = 0 for all L — the brief’s item (1), sharpened.
(2) κ(X, T ) done honestly is identically 0 — a prime-side computation for X = 102 , . . . , 106 ,
    T ≤ 2400, with d − #zeros exact nulls reproduced from primes to 10−6 ; R4’s 33–153
    negatives belong to a warped-sinc operator, not to a compression of the Weil form; nothing
    to fit, κ/N → 0.
(3) Upper bounds via κ are structurally empty: κ(V ) ≤ Noff  dist is the wrong direction; visibility

    of all zeros below T needs dim V ≳ N (T ) (measured L∗ann ≈ 1.12 log(t0 /2π)0.89     √δ
                                                                                             −0.07 ),

    where κ ≤ dim V is trivial; and Theorem 2 (an isolated zero visible at L ≥ C log t/δ)
    cannot be made configuration-free.
(4) Theorem 4 (claimed): n+ (A∗ QA) ≤ n+ (Q), together with the off-line pair {ρ, 1 − ρ̄}
    as a signature-(1, 1) block counted twice by Riemann–von Mangoldt, gives N0dist (I ′ ) ≥
    2nθ+ (W |V ) − N (I ′ ); Cauchy–Schwarz gives n+ ≥ (tr R)2 / tr R2 , prime-computable; the
    Montgomery–Vaughan-range evaluation gives λN/(1 + λ2 /3) → 3N/4 at X = T /2π (under
    RH exactly the classical “3/4 distinct”); hence lim inf N0dist /N ≥ 21 unconditionally, against
    the record 5/12 that I quote from memory and never checked in this run.
Numerics reported with it: prime-only C/N = 0.766/0.762/0.757 at T = 104 /5 · 104 /106 against
the law’s 0.750; certified +0.50; inertia checked on synthetic configurations with 0%, 25%,
100% of zeros on the line. Top risk: “too short to be new”.
That is where I stop: the brief’s proposed route answered in the negative with the mechanism
identified, and its dual left as a claimed theorem that I have tested numerically in every way
available to me here but have neither located in, nor excluded from, the literature.


                                                 53
      Part II

The two-thirds run


        54
The rank–trace lemma and two
thirds

Summary
Earlier in this campaign a run (E2) compressed Weil’s explicit-formula Hermitian form
W (f, g) = ρ mρ hf (γρ )hg (γ̄ρ ) to the Gabor test space fk (u) = φ(u)e−iτk u , τk = T + 2πk/L,
            P

L = λ log(T /2π), obtaining a d × d Gram matrix G whose zero side is a sum of rank-one
positive pieces from on-line zeros and signature-(1, 1) blocks from hypothetical off-line pairs
{ρ, 1 − ρ̄}, and whose traces tr G, tr G2 are computable from primes (PNT-strength sums
and Montgomery–Vaughan, no RH). Counting positive eigenvalues by Cauchy–Schwarz and
comparing with Riemann–von Mangoldt, it claimed ndist    on ≥ 2n+ − N with n+ ≥ 4 N at λ → 1 ,
                                                                                     3             −

hence at least one half of the zeros in [T, 2T ] on the line as distinct points (“Theorem 4”);
two referees checked the block structure and supplied coefficient coordinates and an exact
Poisson identity k φ̂(z − τk )φ̂(z ′ − τk ) = L Φ(z − z ′ ). The orchestrator’s brief asked this run
                  P

to verify its own quick algebra of a single pair block at depth δ (claimed v T v = L2 a real and
δ-independent, eigenvalues mL2 a(1 ± A(δ)) with A(δ) ≥ 1), to decide whether the negative
spectrum alone can raise 1/2 (forecast: no, since tight pairs δ → 0 have vanishing negative
eigenvalue), to analyse a spectral “integrality” analogue of Montgomery’s RH argument (which
gives 2/3 simple, 5/6 distinct by the brief’s elementary arithmetic), and to pursue higher
prime-side moments tr R3 , tr R4 as the likely unconditional route to the target 2/3.
The block facts were confirmed numerically to 10−14 , including the Poisson identity at complex
arguments; cross terms between blocks were found sign-indefinite, so termwise diagonal
dominance of tr R2 is false. Extremal experiments over vector configurations showed that
with normalised pair vectors (v T v = 1) the minimum of ∥M ∥2F is exactly non + 4np , strictly
above the Cauchy–Schwarz floor, while every per-pair quadratic pricing with free mass or
free phase fails. This led the run to a claimed and proved inequality, linear in the masses:
if M = Mon + Mp with Mon ⪰ 0 of rank ≤ r and Mp having at most b positive eigenvalues,
then r ≥ 2 tr Mon + 4 tr Mp − 4b − ∥M ∥2F , by von Neumann’s trace inequality (recalled from
memory) and Cauchy–Schwarz. Applied to the windowed zero side in units R          e = G/(L2 a),
using only |ui |2 ≤ 1, inertia of blocks and the refereed tail bound, it yields the certificate
  on ≥ 4 tr A − 2N − ∥A∥F ≥ (2 − 1/λ − λ/3 − o(1))N → 3 N , containing no pair data. Verdict,
                                                           2
ndist                     2

by the run’s account: unconditionally at least 2/3 of zeros are distinct and on the line, sharp
for this information (extremal: 2N/3 lattice simples plus N/6 tight pairs); on true zeros at
T = 1000 the certificate gives 0.61–0.63N against Theorem 4’s 0.38–0.40N .
The negative spectrum alone was confirmed useless against tight pairs, as forecast; the brief’s
forecast that higher moments are the real lever was contradicted: tr R3 is admissible for λ < 1
but an odd moment cannot improve a count on [0, ∞) without a Lindelöf-strength bound on
λmax , and tr R4 needs λ < 1/2 where d < N/2. The (m − 1)(m − 2) ≥ 0 integrality level is
destroyed by interactions; simple on-line zeros come out only at 1/3; the coordinator’s requested

                                                55
per-pair estimate sj ≥ 1 − o(1) was found unnecessary. The RH comparison 5/6 distinct and
the Rudnick–Sarnak unconditionality were stated from memory without citation check. The
run’s top caveat, inherited from the referees: everything rests on the prime-side upper bound
for ∥R∥
     e 2.
        F


1    The problem as posed: off-line pair blocks and the negative
     spectrum of the compressed Weil form
The setting is a claimed unconditional theorem produced earlier in this campaign, called
Theorem 4: by compressing Weil’s explicit-formula Hermitian form to a finite-dimensional
Gabor test space attached to the window of ordinates [T, 2T ], counting the positive eigenvalues
of the resulting matrix by Cauchy–Schwarz from two prime-side traces, and comparing that
count with the Riemann–von Mangoldt zero count, it asserts that at least one half of the
nontrivial zeros in the window lie on the critical line as distinct points. Under the Riemann
Hypothesis, Montgomery’s pair-correlation method gives two thirds of the zeros simple; the
orchestrator wants the unconditional one half pushed to that two thirds. Two runs are launched
in parallel on this: a sibling optimises the test-space weight, and I am told to exploit instead
the two pieces of structure that Theorem 4 throws away — the 2 × 2 blocks contributed by
hypothetical off-line zero pairs, and the negative eigenvalues of the compressed form. The
orchestrator’s brief asks me to verify its quickly derived algebra of a single pair block, to
decide whether the negative spectrum by itself can improve the constant (it forecasts not),
to analyse an “integrality” mechanism modelled on Montgomery’s argument, and to pursue
higher prime-side moments as the unconditional route.
The brief, from the orchestrator (the campaign’s main thread, which wrote every brief and
relayed all reports; later messages in this run call it “the coordinator”), set out here in full and
rewritten for readability:
     Role and reading. Research mathematician, maximal effort, a precise target.
     Read first: (1) the write-up of Theorem 4 by the earlier run that produced it
     (labelled E2 in the campaign: briefed to bound the negative index of inertia of a
     prime-computable compression of the Weil form, it found that index identically zero
     and instead lower-bounded the positive index from prime-side traces by Cauchy–
     Schwarz, double-counting off-line pairs against the Riemann–von Mangoldt count,
     and so claimed unconditionally that at least one half of the zeros are on the line as
     distinct zeros); (2) the verdict of the blind hostile referee who checked Theorem 4’s
     counting identity (referee C: it verified the signature blocks of the zero side and the
     factor 2) — read it for the block structure; (3) the verdict of the referee who closed
     Theorem 4’s technical write-up gaps (referee D: it made rigorous the repair “never
     orthonormalise, work in coefficient coordinates”, proved an exact Poisson identity
     for the Gabor system, and gave explicit tail exponents) — read it for coefficient
     coordinates and the Poisson identity; (4) the blind from-scratch re-derivation of
     the prime-side trace asymptotics by a separate run (E2-rederive). A sibling run
     (E2-kernel) is optimising the kernel — the weight placed on the test space — in
     order to raise the constant 3/4; do not duplicate that. Your lever is the structure
     of the off-line pair blocks and the negative spectrum, both of which Theorem 4
     discards.
      Context. Theorem 4 is the conjunction of two inequalities. The first is

                                         on ≥ 2n+ − N,
                                        ndist


                                                56
the number of distinct zeros on the line in the window being at least twice the
positive index of inertia of the compressed form minus the zero count. The second
is the Cauchy–Schwarz count

                                           (tr R)2            3
                                n+ ≥               −→         4N
                                            tr R2
as the bandwidth parameter tends to 1, the two traces being evaluated from the
prime side. Together: 2 · 34 − 1 = 12 . The loss from 3/4 to 1/2 has one cause: an
off-line pair {ρ, 1 − ρ̄} of multiplicity m is counted 2m times in N , but contributes
only one positive square to the form.
Facts to verify first. I derived the following quickly; check them rigorously via
the Poisson identity, which schematically reads
                                              Z
                                                                   ′
     φ̂(x − τk − iy) φ̂(x − τk − iy ′ ) = L       φ2 (u) e(y+y )u (· · · ) du + aliasing terms
X

 k

(the oscillatory factor in the integrand is left Runwritten). Take the Gabor system
with a real even taper φ, normalised so that φ2 = L(1 + O(η)), and grid points
τk . An off-line pair at depth δ — that is, ρ = 12 + δ + it together with 1 − ρ̄, whose
spectral parameters are γ = t − iδ and γ̄ — has two evaluation functionals, with
coordinates

              vk = φ̂(t − τk − iδ),                      wk = φ̂(t − τk + iδ) = vk

(careful here: φ̂(z̄) = φ̂(z) because φ is real and even). I claim

                                          1                                  sinh(δL)
                                                     Z
     ∥v∥ = ∥w∥ = L A(δ),
        2        2    2
                                 A(δ) := R 2              φ2 (u) e2δu du ≈            ≥ 1,
                                          φ                                     δL
and, writing zk = t − τk − iδ,

                          ⟨v, w⟩ :=       v k wk =         φ̂(zk )2 = L2 ,
                                      X              X

                                      k              k

which is real, independent of δ, and equal to the value for a zero on the line. Hence,
on the span of v and w, the block contributed by the pair — the rank-two Hermitian
form m |v⟩⟨w| + |w⟩⟨v| — has nonzero eigenvalues

                          m Re⟨w, v⟩ ± ∥v∥ ∥w∥ = mL2 (1 ± A),
                                                     


that is, one positive eigenvalue p = mL2 (A + 1) and one negative eigenvalue −q
with q = mL2 (A − 1). These are in the units of the raw Gram matrix G; divide by
L for the normalised matrix R. Check the signs and the normalisation numerically
with a synthetic single pair.
Consequences of these facts. (i) The pair contributes p − q = 2mL2 to the
trace, which is exactly what 2m simple on-line zeros would contribute: consistent
with the trace tr R = LN carrying no information about whether zeros are on the
line. (ii) An isolated pair contributes p2 + q 2 = 2m2 L4 (A2 + 1) ≥ 4m2 L4 to tr R2 ,
against m2 L4 for an on-line zero of multiplicity m. (iii) As δ → 0 one has A → 1,
so q → 0 and p → 2mL2 : the pair becomes spectrally indistinguishable from an
on-line zero of multiplicity 2m. This is the true enemy, and it cannot be beaten
by any method that is also unable to count multiplicity. So the honest target
is: distinct zeros on the line ≥ cN with c matching what RH plus Montgomery’s

                                              57
pair-correlation argument gives for simple zeros, namely c = 2/3 — because under
RH a “double on-line zero” and unconditionally a “tight off-line pair” are one and
the same obstruction.
Program. Theorem      4 uses, of the compressed form R, only the two moments
             of its spectrum  and only the positive index n+ . Use more.
 P      P 2
   λ
  i i ,   λ
         i i

(a) The negative spectrum. Split R = R+ − R− into positive and negative
parts, with positive eigenvalues pi and negative eigenvalues −qj . The prime side
gives, exactly,

                   qj = tr R = LN (1 + o(1)),         p2i +       qj2 = tr R2 = 34 L2 N (· · · ).
   X           X                                  X           X
        pi −
    i          j                                  i           j

Inertia: n+ ≤ ndist
                  on + npair and n− ≤ npair , since each pair block gives at most one
                         dist           dist

negative square and on-line zeros give none. (Check: is n− (A) = ndist pair exactly for
the windowed form? Yes if the functionals are linearly independent; in any case
nθ− (R) ≤ ndist
           pair .) That is an upper bound on n− , whereas we want lower bounds on
non . Combine with the count N ≥ non + 2npair (every multiplicity is at least 1):
we want to show either that npair is small or that non is large. Cauchy–Schwarz
applied to the positive part alone gives
                                      P 2        P 2
                                       p      LN + q
                             n+ ≥     P 2 = 4      P ,
                                        p           2             q2
                                                  3L N −

which is increasing in the negative mass — so negative mass helps n+ . Moreover
pairs with δ ≫ 1/L have q ≈ p ≈ mL2 A large, so they consume the tr R2 budget
quickly, so there are few of them. This would be a density estimate of the shape
#{pairs with A(δ) ≥ A0 } ≤ 43 N/(2A20 ), roughly — can it be made rigorous? It
needs “tr R2 ≥ pairs (p2 + q 2 )”, which is a diagonal-dominance statement, false
                       P

in general for indefinite summands, because the cross terms tr(Rj Rk ) between
different blocks can be negative. Perhaps something survives for the negative part
alone, j qj2 = tr R−      2 with R dominated by something — unclear. Think about
        P
                                        −
what is rigorously available for R = P + j Bj with P ⪰ 0 the on-line part and
                                                       P

Bj the pair blocks: Cauchy interlacing gives n− (R) ≤ j rank− (Bj ) = npair ; there
                                                                   P

are λmin -type bounds; Weyl gives λi (P + B) ≤ λi (P ) + λmax (B); Ky Fan says the
sum of the k smallest eigenvalues of R is at most ⟨x, Rx⟩ over any k orthonormal
                                                               P

vectors x — so choose the x’s in the span of the w-directions of far-off pairs to force
large negative Rayleigh quotients, whence a lower bound on tr R− ; combined with
   p − q = LN , p2 + q 2 fixed, n+ ≤ non + npair and n− ≤ npair , optimise the
P      P                 P        P

worst case. Concretely, set up the finite-dimensional extremal problem: nonnegative
reals p1 , . . . , pa and q1 , . . . , qb with a ≤ non + npair , b ≤ npair ,   p − q = LN ,
                                                                             P    P

   p + q ≤ 43 L2 N , together with any additional provable constraints linking the p
P 2 P 2

and q of the same pair. For a spectrally isolated pair these would be pj −qj = 2mj L2
and pj qj = m2j L4 (A2 − 1) ≥ 0, but interaction with other zeros perturbs them.
Can one prove a robust version — for each pair, nearly orthogonal directions x±             j
                                                  −      −
with ⟨x+j  , Rx    +
                   j ⟩ bounded   below    and  ⟨x j , Rx j ⟩ ≤ −(something ≥ 0)? The Rayleigh
quotient in the normalised w-direction, ⟨ŵ, Rŵ⟩, equals the contribution of pair
j itself (something like 2mL2 · (1/A) · (· · · ); compute it) plus the contributions
of all the other zeros, which are positive semidefinite from on-line zeros (hence
≥ 0!) and indefinite from other pairs — so single-direction quotients do not
obviously produce negativity. Then perhaps the cleanest extra information really
is n− and tr R− via Ky Fan with a cleverly chosen subspace. Solve the resulting

                                             58
LP/QP: minimise non subject to the constraints and see whether the minimum
exceeds N/2. Even without pair-linking constraints, does adding “n− ≤ npair ”
and using ( p)2 / p2 with           q ≥ 0 free change anything? Probably not by
             P       P            P

itself : the worst case is     q = 0, i.e. every pair has δ → 0. Indeed — the
                            P

δ → 0 pairs are the enemy and they have q → 0; so the negative spectrum helps
only against far pairs, which are already handled. Confirm this reasoning. If
it is confirmed, lever (a) alone cannot beat 1/2, and the write-up should say so
crisply: “the extremal configuration for Theorem 4 is N/4 tight off-line pairs
(depth δ = o(1/ log T )) plus N/2 simple on-line zeros, which is spectrally identical
to N/4 on-line double zeros plus N/2 simple zeros — Montgomery’s extremal
configuration for 2/3”. (On reflection that configuration has Nsimple = N/2, not
2N/3; let me check Montgomery’s extremal configuration for          m ≤ 43 N : one
                                                                  P 2

third of the zeros in doubles, i.e. N/6 double points, plus 2N/3 simple zeros, giving
   m = N6 · 4 + 2N 3 = 3 N and Ndist = 6 + 3P = 6 NP
                        4                N    2N    5
                                                         — whereas Cauchy–Schwarz
P 2

gave only 3/4. The discrepancy is because ( m) / m2 is not tight for integer
                                                     2

m. Montgomery’s bound uses integrality: m2 ≥ 2m − 1 summed over distinct
zeros gives m2 ≥ 2N − Ndist , so Ndist ≥ 2N − m2 ≥ 23 N ; and for simple zeros,
            P                                      P

   m ≥ Nsimple + m≥2 m2 ≥ Nsimple + 2 m≥2 m = Nsimple + 2(N − Nsimple ) =
P 2                 P                        P

2N − Nsimple , so Nsimple ≥ 2N − m ≥ 23 N . And Ndist ≥ Nsimple ≥ 23 N , or better
                                   P 2

≥ 34 N by Cauchy–Schwarz.)
(b) The integrality lever — likely the real one. Theorem 4 used the Cauchy–
Schwarz count n+ ≥ ( λ)2 / λ2 , the spectral analogue of Ndist ≥ N 2 / m2 .
                        P         P                                              P

Montgomery’s simple-zero bound instead uses that multiplicities are integers ≥ 1:
   m ≥ 2N − Nsimple . The spectral analogue: the positive eigenvalues of R are not
P 2

arbitrary — an isolated on-line zero of multiplicity m contributes an eigenvalue
mL2 , an isolated tight pair 2mL2 , and interactions smear these values. If one
could prove, in a robust sense, that “every positive eigen-direction carries integer
mass ≥ 1 in units of L2 ” — say an inequality like           pi ≥ L2 2 pi − L2 n+ ,
                                                          P 2           P            

the analogue of m2 ≥ 2 m − #{points} — then n+ L4 ≥ 2L2 p − p2 and,
                 P            P                                       P      P

with     p ≥ L2 N and         p2 ≤ 43 L4 N in G-units, n+ ≥ 2N − 43 N = 23 N : the
      P                  P

same 2/3 as Montgomery’s simple-zero constant. Fed into “on-line ≥ 2n+ − N ”
that would give only N/3, worse than the Cauchy–Schwarz route; but of course
one takes the maximum of the two lower bounds for n+ . The point is this: the
final bound 2n+ − N with n+ = 34 N gives 1/2; to get 2/3 on the line one needs
n+ ≥ 56 N . Under RH, is n+ = Ndist ≥ 65 N provable from              m ≤ 43 N ? By
                                                                    P 2

integrality, yes: Ndist = N − (m − 1), and to minimise the number of points
                                 P

given m = N and m2 ≤ 43 N one uses doubles as much as possible; k doubles
       P              P

plus N − 2k simples have         m = 4k + N − 2k = N + 2k ≤ 43 N , so k ≤ N/6
                               P 2

and Ndist ≥ N − 6 = 6 N . So under RH integrality gives 56 distinct, better
                    N       5

than the Cauchy–Schwarz 34 . (Is “5/6 distinct under RH” known? Surely —
Montgomery’s paper or folklore; check the literature.) And then, Theorem-4-style,
distinct on the line ≥ 2 · 56 N − N = 23 N : exactly the target. So the entire problem
of reaching 2/3 is to prove the spectral integrality inequality unconditionally —
something of the shape “nθ+ (R) ≥ 2 tr R/u − tr R2 /u2 ” in appropriate units, i.e.
that the positive eigenvalues of the windowed Weil form come in integer quanta
≥ 1, robustly. Let me be precise about what is needed. With quantum u = L2
(in G-units), the inequality λi >θ λi (2u − λi ) ≤ u2 nθ+ would hold if every positive
                               P

eigenvalue were ≥ u — but in fact λ(2u − λ) ≤ u2 holds for every real λ, being
(λ−u)2 ≥ 0. So that inequality is always true, and gives nθ+ ≥ 2u ′ λ− ′ λ2 /u2 ,
                                                                      P      P    

the sums over λ > θ; with ′ λ ≥ tr R+ − θd, tr G = L2 N and u = L2 , this is
                                P


                                         59
n+ ≥ 2N − tr G2 /L4 = 2N − 43 N = 23 N — only 2/3, below the Cauchy–Schwarz
3/4, precisely because no integrality has been used: (λ − u)2 ≥ 0 is free. Genuine
integrality would say λ ∈ {u, 2u, 3u, . . . }, hence (λ − u)(λ − 2u) ≥ 0, hence
λ2 ≥ 3uλ − 2u2 , hence λ2 ≥ 3u λ − 2u2 n+ , hence
                       P           P


                              3u                       3N − 34 N  5
                                             P 2
                                       λ−
                                   P
                                              λ
                     n+ ≥                          =             = N.
                                       2u2                2       6
That is the inequality wanted; it requires “no eigenvalue of the zero-side form
strictly between u and 2u, or below u” — and this is robustly false because of
interactions: the eigenvalues of ρ mρ uρ u∗ρ are the multiplicities only if the vectors
                                 P

uρ are orthogonal, whereas ⟨uρ , uρ′ ⟩ = DL (γ − γ ′ ) ̸= 0 for |γ − γ ′ | ≲ 1/L, so zeros
closer than the mean spacing times l/L interact. Under RH Montgomery needs
no eigenvalues — he reads m2 directly off the diagonal of the pair correlation.
                               P

Unconditionally we replaced        m by       λ and lost integrality. Can a robust
                                 P 2       P 2

integrality be recovered? Options: (i) work at slightly smaller bandwidth and
use that DL (γ − γ ′ ) is small unless |γ − γ ′ | < 2π/L ∼ mean spacing/λ — but
interactions affect a positive fraction of zeros; no. (ii) Use the determinant, or
higher traces: tr R3 , tr R4 from the prime side? tr R3 involves triple correlations of
primes, Λ(n1 )Λ(n2 )Λ(n3 ) with conditions of the type n1 n2 = n3 ; the diagonal is
         P

computable, the off-diagonal needs GUE triple correlation, i.e. Hardy–Littlewood —
not unconditional. But perhaps with support restrictions: are Rudnick–Sarnak’s
n-level correlations with restricted Fourier support unconditional? Do they assume
RH? They prove GUE statistics for test functions with j |ξj | < 2 (or < 1?); I
                                                               P

believe Rudnick–Sarnak 1996 is unconditional in the smoothed form for restricted
support — check. If tr R3 is prime-computable for λ small enough (a condition like
3λ/2 < 1?), then with three moments ( λ, λ2 , λ3 ) one gets sharper counting
                                         P P          P

inequalities — something like n+ ≥ ( λ ) / λ , or the optimal three-moment
                                        P 2 2 P 4

Markov–Krein bound — so compute what the RH-predicted value of tr R3 gives
for the on-line bound; this could beat 1/2 even without integrality. (iii) Accept
Cauchy–Schwarz and attack the two-for-one cost through lever (a) for non-tight
pairs together with a separate argument that tight pairs (δ < c/L) are rare — no;
there is no unconditional tool for that, it is RH-hard. So (ii), higher prime-side
moments with restricted support, is the promising unconditional lever.
Do. Verify all the block and eigenvalue facts numerically. Settle whether lever (a) is
provably useless against tight pairs (I expect yes). Then pursue (b)(ii): what is the
largest k such that tr Rk is unconditionally computable from primes at bandwidth λ
— a condition like kλ/2 < 1, or (k−1)λ < 2? Compute the RH/GUE-predicted main
terms of tr R3 , and of tr R4 if admissible, for the sinc system, as functions of λ. Then
solve the moment problem: given (m1 , m2 , m3 )(λ) = ( λi , λ2i , λ3i ) over the
                                                              P     P     P

positive spectrum — careful, odd moments mix in the signs of negative eigenvalues;
handle that via n− ≤ npair and worst-casing, or use even moments only — what is
the best lower bound on n+ , hence on 2n+ − N , optimised over admissible λ? Does
it exceed 1/2? Does it reach 2/3? Report the numbers together with the exact
admissibility condition and its literature status (Rudnick–Sarnak, Hughes–Rudnick
restricted-support n-level results: which of them are unconditional).
Deliverable. A report, with a final summary covering: are the block facts
confirmed?; the verdict on lever (a); the integrality analysis (5/6 under RH via
integers — known?); the higher-moment route: admissible k(λ), predicted moments,
the resulting unconditional on-line constant; is 2/3 reached, and if not, exactly
what input would reach it.

                                              60
1.1    The brief’s objects, notation and sources, spelled out
For a reader meeting this corner cold, here is what every symbol and coined term in the brief
denotes, in the sense the campaign uses them and consistently with the definitions fixed by the
documents I read below; and, where the brief indicates it, who supplied what.

The form and its two sides. The zeros are the nontrivial zeros ρ = β + it of ζ, each
with multiplicity mρ ; the spectral parameter of ρ is γρ := (ρ − 12 )/i = t − i(β − 12 ), real
exactly when ρ isR on the critical line. For a test function f supported in [−L/2, L/2] put
hf (z) = fˆ(z) = f (u)eizu du, an entire function. The Weil form is the Hermitian form
W (f, g) = ρ mρ hf (γρ )hg (γ̄ρ ); this expression is its zero side. Weil’s explicit formula rewrites
           P

W (f, g) as an integral of hf hg against an explicit density built from the digamma function,
the pole of ζ, and the prime sum n≤X Λ(n)n−1/2 cos(τ log n) with X = eL ; that expression is
                                    P

the prime side, and “prime-computable” means evaluable from it without knowledge of zeros.

Window, bandwidth, counts. The window is the ordinate range I = [T, 2T ], with l :=
log(T /2π); N = N (I) ∼ T l/2π is the number of zeros with ordinate in I, counted with
multiplicity (Riemann–von Mangoldt). The bandwidth is λ ∈ (0, 1) and L := λl is the length
of the support interval of the test functions, so X = eL ≤ (T /2π)λ ; “λ → 1− ” is the limit in
which the constants 3/4 and 1/2 appear. Ndist , Nsimple are the numbers of distinct, respectively
simple, zeros in the window; ndiston (also written N0 ) is the number of distinct zeros on the line
                                                       dist

β = 12 ; an off-line pair is {ρ, 1 − ρ̄} with β ̸= 12 (the two members share the ordinate t and the
multiplicity m, by the functional equation), and ndist   pair counts distinct such pairs. The depth of
a pair is δ = β − 2 ; a tight pair has δ = o(1/L), a far pair δ ≫ 1/L. Since each distinct on-line
                    1

point has multiplicity ≥ 1 and each pair contributes ≥ 2 to the count, N ≥ ndist     on + 2npair ; this
                                                                                              dist

is the “Riemann–von Mangoldt bookkeeping”.

The Gabor system and the matrices G and R. The test space is spanned by the Gabor
system fk (u) = φ(u)e−iτk u , 0 ≤ k < d, where τk = T + 2πk/L is a grid of frequencies filling
the window, d = ⌊LT /2π⌋ ≈ λN , and the taper φ is a real even C 2 function on [−L/2, L/2]
equal to 1 on the middle (1 − η) fraction of the interval, η being a small smoothing parameter
eventually sent to 0; the sinc system is the untapered case φ = 1[−L/2,L/2] , whose φ̂ is the
sinc function. The compressed Weil form is the d × d Gram matrix Gkl = W (fk , fl ); “G-units”
refers to this raw matrix. The brief’sR R is G divided by L (in Theorem 4’s write-up R was G
orthonormalised by the mass matrix fk f¯l , which is approximately L · Id; referee D’s repair is
to use G/L outright). In the brief’s units tr R = LN (1 + o(1)) and tr R2 ≈ 43 L2 N at λ → 1
(more precisely λl2 N (1 + λ2 /3)); these are the prime-side evaluations the campaign calls Step 2.
Later in this document I renormalise once more, to R      e = G/(L2 a), so that a simple isolated
on-line zero has eigenvalue 1.

Inertia and counting. n+ and n− are the positive and negative indices of inertia of R
(numbers of positive and negative eigenvalues); nθ+ , nθ− count eigenvalues above a threshold
θ (respectively below −θ), the threshold absorbing a small tail error. A “positive square” is
a rank-one positive semidefinite summand m |l⟩⟨l| of the form; the Cauchy–Schwarz count is
the elementary fact that a Hermitian matrix with positive trace has at least (tr R)2 / tr R2
positive eigenvalues. The windowed form A is the part of the zero side coming from zeros with
ordinate in a slightly enlarged window I ′ ; the remainder E is the tail. Cauchy interlacing,
Weyl’s inequalities and Ky Fan’s principle are the standard eigenvalue inequalities for sums
and compressions of Hermitian matrices, as the brief states them.


                                                  61
The pair block. For an off-line pair, v and w = v̄ are the coordinate vectors of the two
evaluation functionals f 7→ hf (γ), f 7→ hf (γ̄) on the Gabor basis; A(δ) ≥ 1 is the φ2 -weighted
exponential moment defined in the brief, and p, −q are the two nonzero eigenvalues of the
pair’s rank-two block. The inner-product kernel the brief writes as DL (γ − γ ′ ) = ⟨uρ , uρ′ ⟩ is
the kernel governing overlaps of evaluation functionals at nearby spectral parameters — for the
sinc system a Dirichlet/sinc-type kernel of width ∼ 1/L; the brief does not define it further,
and in what follows its role is played by Φ = FT(φ2 ) from referee D’s Poisson identity. The
quantum u = L2 is the eigenvalue of an isolated simple on-line zero in G-units.

External results invoked. “RH plus Montgomery” is Montgomery’s 1973 theorem: under
RH, the pair correlation of zeros with Fejér weight gives m2ρ ≤ ( 43 + o(1))N , whence at least
                                                         P

2/3 of zeros are simple; the brief’s “5/6 distinct under RH” is its own elementary deduction
from the same inequality, flagged as surely known but unchecked. Rudnick–Sarnak (1996)
and Hughes–Rudnick are results identifying n-level correlations of zeros with GUE predictions
for test functions of restricted Fourier support; whether they are unconditional is left by the
brief as a hedge to be checked. “Hardy–Littlewood” is the prime k-tuple conjecture. The
“three-moment Markov–Krein bound” is the classical extremal problem of bounding the mass
or number of atoms of a measure on [0, ∞) from finitely many moments.

Provenance. Theorem 4 and its Steps 1–3 are E2’s; the block description of the zero side is
referee C’s; coefficient coordinates and the exact Poisson identity are referee D’s; the prime-
side traces were re-proved independently by the re-derivation run. The single-pair algebra
(∥v∥2 , ⟨v, w⟩, p, q, consequences (i)–(iii)), the inertia inequalities of lever (a), the extremal-
configuration picture, the target 2/3, the integrality arithmetic and the higher-moment proposal
are the orchestrator’s own, offered as quick derivations for me to verify. The optimisation of φ
belongs to the sibling kernel run.
So the target (2/3), the pair-block algebra, the inertia facts, the extremal picture and the
integrality arithmetic are all handed to me; what the brief wants from me is verification, a
crisp verdict on lever (a), and the higher-moment computation.

1.2    Theorem 4 as E2 wrote it
I begin with the reading list, in the order given.
First E2’s write-up of Theorem 4 (claimed): “at least one half of the nontrivial zeros of zeta
are on the critical line (as distinct zeros)”. The objects I will be living with are fixed here.
Zeros are ρ = β + it with multiplicity mρ , and γρ := (ρ − 12 )/i = t − i(β − 12 ); the Weil form is
                                                                            Z
                  W (f, g) :=       mρ hf (γρ ) hg (γ̄ρ ),       hf (z) =       f (u)eizu du,
                                X

                                ρ

Hermitian by the functional equation, and equal by the explicit formula to hf hg νX
                                                                                                    R

with an explicit density νX — a digamma term, a pole term, and the prime sum
− π1 n≤X Λ(n)n−1/2 cos(τ log n) — whenever supp f, g ⊂ [−L/2, L/2] with X = eL .
    P

Three linear-algebra lemmas are recorded: inertia does not increase under pullback,
n+ (A∗ QA) ≤ n+ (Q), i.e. a Hermitian form transported to another space through any linear
map acquires no new positive squares; the Cauchy–Schwarz count nθ+ (R) ≥ (tr R − θd)2 / tr R2
for the number nθ+ of eigenvalues above a threshold θ; and Weyl’s perturbation inequality. The
set-up: l = log(T /2π), L = λl, and the Gabor system
                                                             2πk                       j LT k
                fk (u) = φ(u)e−iτk u ,        τk = T +           ,    0≤k<d=                    ,
                                                              L                          2π

                                                     62
with a C 2 taper φ equal to 1 on the middle (1 − η) fraction of [−L/2, L/2].
Step 1 is the part the brief told me to exploit. The zero-side matrix is split into A, the
contribution of zeros with ordinate in the slightly enlarged window I ′ = [T − D0 , 2T + D0 ],
D0 = T 1/2 , and a tail E. Grouping A by distinct points, an on-line zero of multiplicity
m at height t gives the rank-one square m|lt |2 of its evaluation functional,   while an off-line
ρ = 2 + δ + it together with ρ = 1 − ρ̄ gives the Hermitian block m 0 , of signature (1, 1),
     1                             ∗
                                                                       0 m

in the two functionals lγ , lγ̄ . Hence the abstract block form Q, of which A is a pullback, has
n+ (Q) = ndist
           on + npair , while Riemann–von Mangoldt counting gives N (I ) ≥ non + 2npair ;
                   dist                                                      ′      dist     dist

with the tail bound ∥E∥ ≪ T       −1+o(1) =: θ0 this yields
                                          ′                  ′
                                     on (I ) ≥ 2n+ (R) − N (I ).
                                                 θ
                                    ndist

Step 2 is the prime-side claim

                                tr R = LT ⟨µ⟩I (1 + o(1)),
                                              h              L2 i
                               tr R2 = 2πLT ⟨µ⟩2I +               (1 + o(1)),
                                                            12π 2
with ⟨µ⟩I the mean over I = [T, 2T ] of the digamma density, proved by Poisson/Shannon for
the sinc kernel, the diagonal sum n≤X Λ(n)2 n−1 (1 − log n/L), and Montgomery–Vaughan
                                      P

for the off-diagonal; it gives nθ+ (R) ≥ [λ/(1 + λ2 /3)] N (I)(1 + o(1)), consistent under RH with
Montgomery’s pair-correlation evaluation. Step 3 concludes
                      N0dist ([T, 2T ])      2λ             1
                 lim inf                ≥           − 1 −→        (λ → 1− ),
                   T    N ([T, 2T ])      1 + λ2 /3         2
                      √
nontrivial for λ > 3 − 6. E2’s comparison list at the end — Levinson 1/3, Conrey 0.4088,
Bui–Conrey–Young 0.4105, Feng 0.4128, Pratt–Robles–Zaharescu–Zeindler 5/12, simple on
the line ≥ 0.407N ; under RH ≥ 2/3 simple (Montgomery), ≥ 3/4 distinct, “later ∼ 0.8467
distinct?? (from memory)” — is E2’s own recollection, flagged as such in the file.

1.3   The two referee verdicts on Theorem 4
Next referee C’s verdict — the blind hostile referee on the counting identity — headed
“SURVIVES” for the linear-algebra and counting joints. What matters for me is the exact
form of the zero-side matrix in E2’s one-sided complex Gabor space. Since φ̂ has real Taylor
coefficients,

                           Gkl = W (fk , fl ) =        mρ φ̂(γρ − τk ) φ̂(γρ − τl )
                                                  X

                                                   ρ

                                             =                 mρ (aρ aTρ )kl ,
                                                       X

                                                  distinct ρ

each distinct zero contributing a complex-symmetric rank-one piece aaT , “NOT aa∗ ”. An
on-line zero has a real, giving a positive semidefinite rank-one piece;    an off-line ρ and its
partner ρ have aρ∗ = āρ , and m(aa + ā a ) is the pullback of m 0 under f 7→ (lγ f, lγ ∗ f ):
          ∗                           T       ∗                      0 m
                                                                         

at most one positive square in all cases, linear dependence of the functionals included. The
conjugate zeros at height −t sit in the tail, so there is no double-counting of quadruples. Also
rank(GA ) ≤ ndist
              on + 2npair , the inertia statement n+ ≤ non + npair being the sharper one. The
                       dist

Riemann–von Mangoldt bookkeeping and the factor 2 are redone (“a pair costs two R-vM
zeros but buys at most one positive square”).
The verdict also carries a table from referee C’s synthetic-configuration test — true zeros on
[600, 1200], all doubled, all turned into pairs at various depths, half the ordinates paired, mixed

                                                       63
worlds, coincident heights. Writing C = (tr R)2 / tr R2 for the Cauchy–Schwarz count, so that
2C − N (I ′ ) is the certificate — the lower bound for ndist
                                                        on that Theorem 4 actually certifies from
the data — the table shows in every case n+ ≤ ndist  on + npair and 2C − N (I ) ≤ non , and that
                                                             dist            ′     dist

pairing or multiplicity always lowers C at fixed count. On true zeros the explicit formula is
confirmed to 1.1 · 10−8 , n+ = d = 436, and C/N = 0.744 against the asymptotic law 0.750.
The referee’s “rank corollary” — replacing inertia by rank gives Ndist ≥ 34 N and Nsimple ≥ 12 N
unconditionally from the same Step 2 — is recorded as the red flag. Finally the literature
anchor I will lean on later: referee C cites Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh,
arXiv 2306.04799 = Acta Arith. 214 (2024), Thm 1, as an unconditional pair-correlation
asymptotic

                            F (α) = T −2α log T + O(1) + α + O 1/ log T
                                                                            p       


with complex γ allowed, which integrates to E2’s tr R2 main term at λ = 1, and notes that
BGSTB extracted only “61.7% simple ASSUMING all zeros in |β − 1/2| < 1/(2 log T )”. The
burden, says C, lies entirely on Step 2’s upper bound for tr R2 .
Then referee D’s verdict on the technical gaps. The structural change I will adopt wholesale:
never orthonormalise; work with the real symmetric matrix G/L in coefficient coordinates,
where inertia, Weyl and Cauchy–Schwarz need no inner product, so the ill-conditioned mass
matrix of the Gabor system disappears from the argument. D’s concrete taper is φ =
1[−c,c] ∗ Hannw with ramp width w = ηL/2 and c = (L − w)/2, with closed-form transform
φ̂(r) = (2 sin(rc)/r) Hann
                      \w (r), and taper functionals

                   1                      1
                       Z                      Z
            a :=           φ2 ,    b :=           φ4 ,    J,       Φ := FT(φ2 ),      Φ(0) = La,
                   L                      L
J being a third functional of the taper that carries the λ2 term below. The tail bound is
made explicit using only the r−2 decay of φ̂: θ0 = 2A0 C12 eL/2 log(4T )D0−2 = T λ/2−1+o(1) , with
constants A0 , C1 from D’s notes, and only θ0 = o(l) is needed.
The item the brief singled out is D’s exact Poisson lemma: for any φ ∈ L2 supported in
[−L/2, L/2] and the full grid τk = T + 2πk/L, k ∈ Z,

                     φ̂(τ − τk ) φ̂(τ ′ − τk ) = L Φ(τ − τ ′ ),             φ̂(τ − τk )2 = L2 a,
               X                                                      X

               k∈Z                                                    k∈Z

proved by Poisson summation (the Fourier transform in s of s 7→ φ̂(τ − s)φ̂(τ ′ − s) vanishes
for frequencies |ξ| ≥ L, so only the ξ = 0 term survives), stated for real arguments and checked
numerically to 8 · 10−11 . This is the rigorous form of the identity the brief wrote schematically,
without aliasing terms: on the full grid there are none. Its consequence is the limiting ratio

                          λa2         λ
                                 =           1 − κλ η + O(η  ) ,
                                                            2 
                                                                               κ ≈ 0.27,
                        b + λ2 J   1 + λ2 /3
and the taper constants are tabulated: at η = 0.2, a = 0.87933, b = 0.86245, J = 0.22702;
at η = 0.1, a = 0.93967; at η = 0.05, a = 0.96983. D’s prime-side prediction matches the
true-zero traces to 3 · 10−4 at T = 2000, and the numerical table at T = 2000 shows certificates
(2CG − N (I ′ ))/N of +.402 and +.424 at λ = 1, η = 0.1 and 0.05. None of the repairs moves
the constant; D too places the whole weight on the Step-2 main term.

1.4   The re-derived prime-side traces and a declared gap
Last on the list is the re-derivation run’s proof of the prime- and gamma-side traces — the
blind, from-scratch re-derivation of Step 2 alone. It fixes l = log(T /2π), 0 < λ < 1, L = λl,

                                                         64
X = eL , N = T l/2π, splits the explicit-formula density as νX = µ + Π + P (digamma, pole
and prime parts) and works entirely on the u-side. Two points in it matter for me.
First, a structural warning. The mass matrix of the Gabor system,
                                    Z
                            Mkl =       φ2 (u) e−2πi(k−l)u/L du = L Td [s],

is a Toeplitz matrix whose symbol s = φ2 (Lθ/2π) takes every value in [0, 1], so M is not
L(Id + O(η)): by Szegő about ηd of its eigenvalues are spread over [0, L/2], the smallest
exponentially small, and the orthonormalised “R = M −1/2 GM −1/2 ” is genuinely ill-conditioned.
The author therefore treats two systems: (A) an exactly orthogonal system with spacing 2π/L0 ,
L0 = (1 − η)L, and a Princen–Bradley window satisfying m φ2 (u + mL0 ) ≡ 1, so that
                                                              P

M = L0 Id exactly and R = G/L0 ; (B) the brief’s spacing 2π/L, with RS the compression of
the form to the spectral subspace S = {M ≥ L/2} of the mass matrix, dim S ≥ (1 − 2η)d.
Second, the results. Theorem A (system A) and Theorem B (system B) both give

                                    tr R = λlN (1 + o(1)),
                                                          λ2 
                                 tr R2 = λl2 N 1 +              (1 + o(1)),
                                                           3
                               (tr R)2      λ
                                       =           N (1 + o(1)),
                                tr R2    1 + λ2 /3

with o(1) = O(η + 1/l); the off-diagonal prime terms are O λl(T λ−1 + T −λ/4 ) relative to the
                                                                                   

main term, the λ2 /3 is 2 · 16 from the Fejér autocorrelation of the u-window integrated against
d(log2 n/2), and the µµ′ constant is exactly 1. The inputs are Stirling, Mertens/Chebyshev, the
prime number theorem with classical error (only for a constant), and Montgomery–Vaughan’s
Hilbert inequality and mean-value theorem — no zeros, no RH, no density theorems. The
numerical section confirms the finite main terms to between 10−4 and 7 · 10−4 .
And a declared gap, Remark 7.4: for the literal unrestricted M −1/2 GM −1/2 of system (B) the
method proves nothing, because on the ∼ ηd bad eigendirections of M the prime part of the
Rayleigh quotient is bounded unconditionally only by sup |P | ∼ X 1/2 — “any method not
controlling supτ ∈I |P | on short windows, i.e. Lindelöf-type input” does not decide it. That
obstruction I will meet again.


2     Verifying the off-line pair block numerically
2.1   What the sibling owns, and my normalised matrix
I look at what the sibling kernel agent — the one the brief assigned the optimisation of the
taper — has produced in the meantime, reading the opening of its report so as not to duplicate
it. Its structural fact is this. For any finite family of test functions hj the zero side of the form
is governed by the kernel

                                     k(z, z ′ ) =       hj (z) hj (z̄ ′ ),
                                                    X

                                                    j

which on R × R is a finite-rank Gram kernel; hence in any translation-invariant limit its Fourier
transform w := k̂ is nonnegative (Bochner) with supp w ⊂ [−L/2, L/2].      The pair-correlation
kernel seen by the Cauchy–Schwarz count is K = |k| with K(0) = ( w) , the same k entering
                                                    2                    2
                                                                     R

both tr G and tr G2 ; conversely every admissible w is realised exactly by the Gabor system
          √
with φ = w, via referee D’s Poisson identity. So, in the sibling’s words, “within inertia +

                                                    65
(tr, tr2 ) Cauchy–Schwarz + explicit formula with X ≤ T the whole design freedom is one
function w ≥ 0 on [−L/2, L/2]” — w = φ2 , Theorem 4 as written being w = 1 with K the
Fejér kernel — and a signed w is unreachable. Redoing Step 2 of Theorem 4 for general w, the
sibling obtains the certificate constant
                                                 R 2
                                            λ v
              cλ (v) = R                                                         v ≥ 0 on [− 12 , 21 ] ,
                                                                                                     
                           v 2 + λ2        |s − s′ | v(s)v(s′ ) ds ds′
                                      RR


which it identifies with Montgomery’s pair-correlation evaluation and with the very functional
appearing in Montgomery’s RH bound;  √    v = 1 recovers λ/(1 + λ2 /3). Its extremal problem
leads to v ′′ + 2λ2 v = 0, v = A cos( 2 λs) — and there my excerpt stops. The taper is the
sibling’s business; mine is the blocks.
I now fix the notation I will use for everything that follows. As before l = log(T /2π), L = λl,
N = N ([T, 2T ]) ∼ T l/2π, and the test space has dimension d = ⌊LT /2π⌋ = λN (1 + O(1/l));
the Gabor system is fk (u)   = φ(u)e−iτk u with τk = T + 2πk/L, φ a real even C 2 taper on
[−L/2, L/2], and a := L φ . I adopt referee D’s coefficient coordinates (no orthonormalisation,
                       1 R 2

so no mass matrix) and referee C’s form of the zero-side matrix:

                    G=                                   (transpose, not adjoint),
                             X
                                        mρ uρ uTρ
                           distinct ρ

                   uρ := φ̂(γρ − τk ) k ,               γρ = t − iδ for ρ = 12 + δ + it.
                                             


The one choice of my own is the normalisation: I work with
                                                  e := G/(L2 a),
                                                  R

so that an isolated simple on-line zero should contribute eigenvalue exactly 1 (to be checked
below). In these units the prime-side asymptotics of Theorem 4, Step 2 — equivalently the
re-derivation agent’s Theorems A/B — read
                                                                       1       λ
                    tr R
                       e = N (1 + o(1)),                tr R
                                                           e2 = N           +      (1 + o(1)),
                                                                        λ       3
and Theorem 4 itself reads ndist
                            on ≥ 2n+ − N with

                                                  (tr R)
                                                      e 2            λ
                                        n+ ≥                 =              N.
                                                    tr R
                                                       e2         1 + λ2 /3

Finally, with Φ := FT(φ2 ) the kernel of referee D’s Poisson identity, I set Φ
                                                                             e := Φ/(La), so that
Φ(0)
e    = 1, and

                                                                 φ2 (u) e2δu du
                                                            R
                             A(δ) := Φ(−2iδ)
                                     e       =                       R          ≥ 1,
                                                                       φ2

which is exactly the brief’s A(δ) (its sinh(δL)/(δL) being the sharp-cutoff approximation), here
expressed through referee D’s Poisson kernel.

2.2   The synthetic single-pair test
Now the brief’s first task item: verify the block facts “with a synthetic single pair”. I set
up referee D’s taper concretely — φ = 1[−c,c] ∗ Hannw with ramp width w = ηL/2 and
c = (L − w)/2, so that φ ≡ 1 on |u| ≤ (1 − η)L/2 and on the ramp, in the normalised ramp
coordinate t ∈ (0, 1), φ has the closed form t+sin(2π(t− 12 ))/(2π) — together with a trapezoidal


                                                            66
evaluation of fˆ(z) = f (u)eizu du valid for complex z, which is what an off-line zero requires.
                      R

The test takes L = 6, η = 0.2, the grid τk = 2πk/L for |k| ≤ 4000, and synthetic zeros

                 (t, δ) ∈ {(0.3, 0), (0.3, 0.05), (1.234, 0.2), (0.77, 0.5), (2, 1)},

forms the functional vk = φ̂(t − iδ − τk ) of the off-line point, and compares

                                               vT v      with L2 a,
                                              ∥v∥2       with L2 a A(δ),
        the extreme eigenvalues of vv T + v̄v̄ T         with   − L2 a (A − 1), +L2 a (A + 1),

these being the brief’s “facts to verify first” rewritten in my taper-general normalisation.
I add two checks to the brief’s list. First, referee D stated and tested the Poisson identity for
real arguments only, whereas the brief’s sketch of it already carried complex shifts; I test

                                   φ̂(z − τk ) φ̂(z ′ − τk ) = L Φ(z − z ′ )
                              X

                               k

at complex z, z ′ , since that is the form that will govern every cross term involving an off-line
zero. Second, a first look at the interactions the brief had warned could be negative: the cross
term between an on-line zero at height t′ , with real functional u, and a pair at (t, δ) contributes

                               tr uuT (vv T + v̄v̄ T ) = 2 Re (u · v)2
                                                         


to tr G2 , and by Poisson u · v = L Φ(t − t′ − iδ); I evaluate this for a pair at t = 0, δ = 0.3 and
t′ ∈ {0, 0.4, 0.8, 1.047, 1.3}, in units of L4 a2 .
The dense eigendecomposition of the truncated block is needlessly   slow; the obvious rank-two
reduction — with W = [v, v̄] the block is B = W σx W , σx = 1 0 , and its nonzero eigenvalues
                                                      ∗
                                                             0 1

are those of the 2 × 2 matrix σx W ∗ W — is what I use from here on, though the numbers below
still come from the original dense computation on the |k| ≤ 4000 grid.
Here is what comes back. The taper constant is a = 0.879332 (referee D’s 0.87933 at η = 0.2),
so L2 a = 31.655945. For every one of the five zeros v T v = 31.655945 with imaginary part at
most 5.7 · 10−14 — real, positive and δ-independent, exactly as the brief asserted — and ∥v∥2
matches L2 a A(δ) to all printed digits. The block spectra:
                         t    δ     A(δ)      λmin        λmax    rank
                        0.3   0   1.000000  −0.000000   63.311891   1
                        0.3 0.05 1.011679   −0.369707   63.681598   2
                      1.234 0.2 1.196943    −6.234416   69.546307   2
                       0.77 0.5 2.647667 −52.158467 115.470358      2
                        2.0  1.0 18.833064 −564.522489 627.834380   2

The predicted −L2 a(A − 1) and +L2 a(A + 1) agree with λmin and λmax to every digit shown.
At δ = 0 the block has rank one with the single eigenvalue 63.311891 = 2L2 a: this is the brief’s
“true enemy” made concrete — a pair collapsed onto the line is spectrally an on-line zero of
multiplicity 2, eigenvalue 2 in R
                                e units.

The Poisson identity holds at complex arguments as cleanly as at real ones: for

         (z, z ′ ) ∈ {(0.4 − 0.1i, 1.7 + 0.3i), (2 − 0.6i, −1.1 − 0.2i), (0.5, 0.5 + 0.9i)}

the two sides agree to within 1.4 · 10−14 , the last case giving the real value 71.22414602, as it
must, z − z ′ being purely imaginary and φ2 even.


                                                    67
  And the cross term equals its Poisson prediction 2 Re [LΦ(t − t′ − iδ)]2 exactly, its ratio to
  L4 a2 = 1002.10 running

        +2.4558, +1.4719, +0.0574, −0.1883, −0.0357                           at t′ = 0, 0.4, 0.8, 1.047, 1.3.

  So the interaction between an on-line zero and a nearby pair is not sign-definite: large and
  positive when they nearly coincide, negative about one grid cell (2π/L ≈ 1.047) away. Whatever
  per-pair lower bound on tr R e 2 I hope to use cannot come from termwise positivity of cross
  terms.


  3      Integrality needs quantised, phase-locked mass
  3.1     Integrality survives interactions under fixed normalisation
  The brief’s integrality lever rests on its consequence (ii), which in R
                                                                        e units says that an isolated
  off-line pair costs 2(A +1) ≥ 4 in tr R while contributing only 2 to tr R;
                         2               e 2                               e and the form of attack
  the brief suggested was an extremal LP/QP over eigenvalue configurations. The sign-indefinite
  cross terms just computed are the threat to any such per-pair accounting. I recast the question
  as a finite-dimensional extremal problem for the Frobenius norm at the pure linear-algebra
  level — this formulation is mine, not the brief’s or any earlier report’s. Take
                               non               np
                          M=          ui uTi +         vj vjT + v̄j v̄jT ,
                               X                 X                     

                                i=1              j=1

                                 ui ∈ R , |ui | = 1,
                                           d
                                                                   vj ∈ Cd , vjT vj = 1,

  where the constraint vjT vj = 1 is precisely the δ-independent normalisation verified in the
  single-pair test, and no other restriction is placed on the vectors, so every kind of interaction
  is allowed. Here non plays the role of the number of distinct on-line zeros, np the number of
  distinct off-line pairs, and N := non + 2np the zero count with multiplicity. Two questions:
(Q1) Is min ∥M ∥2F ≥ non + 4np ? That is “integrality”, or diagonal dominance, and would give
     2/3.
(Q2) How does the true minimum compare with the Cauchy–Schwarz floor N 2 /(non + np ), which
     is all Theorem 4 uses?
 I minimise ∥M ∥2F by BFGS with 40 random restarts over thirteen cases from (d, non , np ) =
 (4, 0, 1) to (8, 1, 3), recording the spectrum of the minimiser and the pair norms Aj := ∥vj ∥2
 (the analogue of A(δ): Aj = 1 is a tight pair, Aj > 1 a deep one).
  The answer is unambiguous: in every case the numerical minimum equals non + 4np to five
  decimals, strictly above the Cauchy–Schwarz floor whenever non > 0. A selection:
            (d, non , np ) N min ∥M ∥2F non + 4np C–S floor                spectrum; Aj
              (4, 1, 1)    3  5.00000        5      4.5000                 {1, 2}; 1
              (4, 2, 1)    4  6.00000        6      5.3333                 {1, 1, 2}; 1
              (6, 2, 2)    6 10.00000       10      9.0000                 {1, 1, 2, 2}; 1.139, 1.139
              (6, 4, 1)    6  8.00000        8      7.2000                 {14 , 2}; 1
              (8, 2, 3)    8 14.00000       14     12.8000                 {1, 1, 2, 2, 2}; 1.044, 1.039, 1.018
              (8, 4, 2)    8 12.00000       12     10.6667                 {14 , 2, 2}; 1.55, 1.55
              (8, 0, 4)    8 16.00000       16     16.0000                 {24 }; 1.075, . . . , 1.674
  The minimising spectrum is always {1 (×non ), 2 (×np )} — on-line zeros at eigenvalue 1,
  pairs looking like double zeros — and the pair norms at the minimum are ≥ 1 but need not
  equal 1 (they reach 1.674), so the optimiser is genuinely using non-tight, interacting pairs and


                                                          68
still cannot get below non + 4np . Put differently, the Cauchy–Schwarz extremal spectrum, all
eigenvalues equal to N/(non + np ), is not realisable by on-line points plus normalised pairs.
So at the linear-algebra level, with v T v pinned to 1, the per-pair cost 4 appears to survive the
sign-indefinite interactions — numerical evidence only, and somewhat against the spirit of the
brief’s warning that spectral integrality is robustly false because of interactions. The natural
next question is which of my constraints is doing the work: can the normalisation vjT vj = 1 be
dropped in favour of a free inequality in the quantities |ui | and vjT vj ?

3.2    Unnormalised and phase-locked variants all fail
I now strip the normalisation and look for a free quartic inequality in the raw vectors. With

                                     M=           ui uTi +           2 Re(vj vjT )
                                            X                   X

                                              i                  j

for arbitrary real ui and complex vj — no normalisation, no phase condition — and writing
sj := vjT vj , I test three candidate inequalities of my own devising:

                         (G2) ∥M ∥2F ≥                |ui |4 + 4
                                                  X                  X
                                                                           |sj |2 ,
                                                  i                    j

                       (G2re)                         |ui | + 4            (Re sj )2 ,
                                                  X                  X
                                   ∥M ∥2F   ≥               4

                                                  i                    j

                         (G1)                         |ui | + 2            |sj |2 + 2
                                                  X                  X                   X
                                   ∥M ∥2F   ≥               4
                                                                                             ∥vj ∥4 .
                                                  i                    j                 j

Everything is homogeneous of degree four, so I fix the total Euclidean norm of all the vectors
to 1 and minimise lhs − rhs by BFGS with 60 restarts over the seven cases

          (d, non , np ) ∈ {(3, 1, 1), (4, 2, 1), (4, 0, 2), (5, 2, 2), (6, 3, 2), (6, 1, 3), (8, 4, 3)}.

All three fail, and fail cleanly: G2 and G1 return min(lhs − rhs) = −4.000000 in every case,
and G2re returns −1.000000 with one pair and −2.000000 with two or more.
A gap of exactly −4 at total norm 1 means the left side is being driven to zero while |s| = 1. I
extract the G2 minimiser at (d, non , np ) = (3, 1, 1): u ≈ 0 (entries of size 10−8 ), ∥v∥2 = 1, and

                                         v T v = 2.3 · 10−7 − 1.0 i,

the printed v having componentwise equal and opposite real and imaginary parts, i.e. v = e−iπ/4 r
with r a real unit vector. Then vv T = −i rrT is purely imaginary, 2 Re(vv T ) is the zero matrix,
M has eigenvalues between −4.9 · 10−9 and 4.7 · 10−7 , and lhs = 2.2 · 10−13 against rhs = 4.
So it is the free phase of v T v that kills G2: a “pair” whose v T v has the wrong argument
contributes a vanishing block while being charged full price.
Next attempt: charge only for the positive real part of sj ,

                            (G3)                                |ui |4 + 4        (Re sj )2+ ?
                                                       X                     X
                                        ∥M ∥2F ≥
                                                        i                     j

for arbitrary real ui and complex vj , now with 80 restarts over twelve cases from (2, 1, 1) to
(8, 2, 4). Still false. With a single pair the gap is −5.000 · 10−1 every time, the minimiser having
Re s = −0.25 and one u with |u|2 = 0.75 (any further ui at 0); with two or more pairs the gap
is −1.333 every time, the minimiser having one pair with Re s ≈ 0.667, the remaining pairs
sharing Re s ≈ −0.333 between them (for instance {0.667, −0.032, −0.302} at (8, 4, 3)), and all

                                                        69
|ui |2 → 0. Pairs with negative v T v are priced at zero on the right-hand side but still subtract
on the left.
So the relevant version is the phase-locked one. The functional-equation pairing ρ ↔ 1 − ρ̄
together with the Poisson identity forces v T v = L2 a > 0 for a genuine off-line pair — this is
exactly the positivity verified in the single-pair test — so I now take the real ui arbitrary and
the complex vj with vjT vj real and positive but of free magnitude (implemented by rotating
                       i
each vj through e− 2 arg sj ), and test
                                                                  2                                   2
               (G4)                ui uTi +       2 Re(vj vjT )                 |ui |4 + 4
                              X               X                           X                  X
                                                                      ≥                          vjT vj .
                                                                  F
                               i              j                             i                j

My first attempt, 100 restarts over seventeen cases up to (10, 5, 5), is cut off at the time limit
before returning anything, so I rerun it with 25 restarts, dropping the two largest cases (8, 4, 3)
and (10, 5, 5), and leave it running.


4     A trace inequality coupling rank and negative spectrum
4.1    Phase-locking fails; a rank-plus-inertia claim
I read the results of the phase-locked test (G4), in which the on-line vectors ui are arbitrary
real, the pair vectors vj are complex with sj := vjT vj forced real and positive but of free
magnitude, and the candidate inequality charges 4s2j per pair. Phase-locking does not rescue
per-pair quadratic pricing either:
             (d, non , np )     min gap           sj = vjT vj         Aj = ∥vj ∥2 /sj             |ui |2
               (2, 1, 1)      −2.500 · 10−1       0                   30168                       0.75
               (2, 0, 2)      −6.666 · 10−1       0.667, 0            1, 4.8 · 104                —
               (4, 2, 1)      −2.499 · 10−1       0                   5730                        0, 0.751
               (5, 2, 2)      −6.666 · 10−1       0, 0.667            1.0 · 104 , 1               0, 0
               (4, 0, 3)      −7.251 · 10−1       0, 0.637, 0         905, 1, 2.0 · 104           —
               (6, 2, 3)      −7.250 · 10−1       0.633, 0, 0         1, 2526, 9978               0, 0
               (8, 2, 4)      −7.276 · 10−1       0, 0.633, 0, 0      893, 1, 1.2 · 105 , 660     0, 0
The gap min(lhs − rhs) is −0.25 with one pair, −0.667 whenever np = 2, and between −0.724
and −0.728 for np = 3, 4. The minimisers always consist of one honest pair (s ≈ 2/3 or 0.63,
A = 1, i.e. tight) together with degenerate “pairs” having v T v → 0 and A ∼ 103 –105 , the
on-line vectors either vanishing or, in the one-pair cases, sitting at |u|2 = 0.75. The mechanism
is plain: writing v = x + iy with |x| = |y|, a pair with vanishing v T v costs nothing on the
right-hand side of G4, while its block

                                         2 Re(vv T ) = 2 (xxT − yy T )

remains free to move mass around on the left. So the normalisation v T v = 1 in the one
experiment that succeeded was doing two jobs at once — fixing the phase and quantising the
mass — and the magnitude cannot be set free: a per-pair price of the form 4(v T v)2 is simply
false without quantised mass.
I therefore abandon block-by-block pricing and write down a claim of a structurally different
kind, one that uses no block structure at all — only the two global features of the windowed
zero-side matrix that survive everything above: the on-line part is positive semidefinite of small
rank, and the pair part has few positive eigenvalues but large trace. Precisely: let Mon ⪰ 0
with rank Mon ≤ r and tr Mon = ton ; let Mp = P − Q with P ⪰ 0 of rank at most b and Q ⪰ 0;
put t′ := tr Mp > 0 and s := t′ /b.


                                                          70
Claim (abstract inequality).
                                                                        (
                                   t
                                        on
                                                 t′2                   µ2 ,         µ ≤ s,
           ∥Mon + Mp ∥2F    ≥ r gs               + ,         gs (µ) =
                                        r          b                    2sµ − s2 ,   µ > s.

Corollary (as I state it, for s ≥ 2 − o(1) and ton + t′ = N , writing M = Mon + Mp ):

                                             r ≥ 2N − ∥M ∥2F .

For provenance: the question — whether the pair-block and negative-spectrum structure can
lift Theorem 4’s constant towards 2/3 — is the brief’s, and so are both ingredients of the
claim. The bound n+ (Mp ) ≤ b, one positive eigenvalue per pair block, is the inertia fact of
the brief’s lever (a); and s ≥ 2 − o(1) is the brief’s consequence (i), p − q = 2mL2 , i.e. trace
2m ≥ 2 per block in R  e units — the very fact the brief set aside as “consistent with tr R = LN
carrying no information”. What is mine is coupling the rank of the on-line part with the
inertia and trace of the pair part in a single inequality that is linear in the masses rather than
quadratic. (Editorially: with ∥R∥
                                e 2 → N (1/λ + λ/3) → 4 N from the earlier agents’ prime-side
                                   F                       3
computation, the corollary would read r ≥ 23 N − o(N ) — an inference; nothing to this effect is
written down at this point. Note too that 2N − 34 N = 23 N is the very arithmetic the brief had
already done at its
Before trying to prove the claim I try to break it. I draw 400 random instances with d ∈
{2, . . . , 6} and with r, b and the rank of Q each uniform in {1, . . . , d}; I parametrise Mon = AAT ,
P = BB T , Q = CC T by unconstrained real factors of those ranks and minimise lhs − rhs by
BFGS, penalising t′ ≤ 0. The claim is homogeneous of degree four in the factors — µ2 , sµ and
s2 are all of degree four — so I also track the gap normalised by the fourth power of the factor
norm. Printing each new record low, every value that appears is nonnegative,

 +1.783 · 10−9 , +3.539 · 10−13 , +1.186 · 10−13 , +1.776 · 10−15 , +2.220 · 10−16 , +0.000,

and the run ends with “overall most negative gap found: 0.0”. The optimiser reaches equality
and never crosses it. Numerical support, not a proof — but this claim, unlike G1–G4, has
resisted a serious attempt at falsification.

4.2    Locating cached zeta zeros for true-zero tests
I will want to see the corollary’s right-hand side on actual zeta matrices, so I go looking for
cached zeros in the campaign tree. E2’s tables hold only its experiment logs; referee C’s material
consists of its verdict, the BGSTB paper, and its small test computations (the linear-algebra
lemmas, the explicit-formula check, the synthetic-configuration test, a Deuring–Heilbronn test).
The zero caches turn up elsewhere: an array of ordinates cached by referee B together with its
outputs for the windows [600, 1200], [1000, 2000] at λ = 0.85, 1.0 and [9000, 10000]; a file of
zeros produced by the D2 agent; and a large list of zeros at the root of the campaign tree.
Inspecting them: referee B’s array holds 3700 ordinates, from 14.13472514 to 4218.23078863;
the large list has 100,000 ordinates to nine decimals (14.134725142, 21.022039639,
25.010857580, . . . ); the D2 agent’s file has 700 zeros to about twenty digits. I also
reread the set-up of referee C’s synthetic-configuration test, since it is the template for what I
want to do. It takes the window [600, 1200] with a reach of 25 on either side (zeros within 25 of
the window are included in the windowed matrix), builds the Gram matrix exactly on the zero
side, and checks the certificate 2C − N — with C = (tr R)2 / tr R2 the Cauchy–Schwarz count,
so that 2C − N is the lower bound for ndist on that Theorem 4 certifies — against non , and
                                                                                          dist

n+ against non + npair , at λ ∈ {1.0, 0.85}, over the scenarios: (a) true zeros; (b) all doubled;

                                                        71
(b′ ) all tripled; (c) every ordinate turned into a pair at δ ∈ {10−4 , 0.05, 0.2, 0.45}, so that N
doubles; (c2) every other ordinate paired and the rest deleted, preserving the Riemann–von
Mangoldt count; (d) ordinates with index ≡ 0 mod 4 paired, ≡ 1, 2 on-line, ≡ 3 deleted (N
preserved), at δ ∈ {10−3 , 0.1}; (e) an on-line zero and a pair at the same height; (f) two pairs
at the same height at depths 0.05 and 0.3.

4.3    The pair block, the extremal problem, the theorem
I set down in my report — the document the referees and coordinator will read — everything
established so far: the verified block facts, the extremal experiments, and, now in a cleaner
form than the gs claim and with a proof, the abstract theorem.

The pair block. First referee D’s Poisson identity in the generality I actually used, for
arbitrary complex arguments: for ϕ ∈ L2 supported in [−L/2, L/2] and the full grid τk =
T + 2πk/L, k ∈ Z,

               (P)               ϕ̂(z − τk ) ϕ̂(z ′ − τk ) = L Φ(z − z ′ ),       Φ = FT(ϕ2 ),
                           X

                           k∈Z

with Φ entire, real on R, and Φ(z̄) = Φ(z). The proof is one line: the Fourier transform in s of
s 7→ ϕ̂(z − s)ϕ̂(z ′ − s) at frequency ξ is
                                         Z
                                                                    ′
                                    2π       ϕ(u) ϕ(ξ − u) eizu+iz (ξ−u) du,

which vanishes for |ξ| ≥ L, so only the ξ = 0 Poisson term survives; complex z changes nothing
(and numerically the two sides agreed to 10−14 ). Then, for an off-line pair ρ = 12 + δ + it,
ρ∗ = 1 − ρ̄, with spectral parameters γ = t − iδ, γ ∗ = γ̄ and functionals v := uρ , uρ∗ = v̄, the
brief’s facts as verified in my units are

               v T v = L Φ(0) = L2 a              (real, positive, δ-independent; to 10−14 ),
                                                                            ϕ2 cosh(2δu)
                                                                        R
              ∥v∥ = L Φ(−2iδ) = L a A(δ),
                  2                           2
                                                             A(δ) =             R        ≥ 1,
                                                                                  ϕ2

the last equal to sinh(δL)/(δL) for the sharp window. The pair contributes the real symmetric
block

               B = m (vv T + v̄v̄ T ) = 2m Re(vv T ) = m W σx W ∗ ,                     W = [v, v̄],

whose nonzero eigenvalues are those of
                                         "         #
                                s A′
                 m σx W ∗ W = m ′    ,                       s = v T v = L2 a,     A′ = ∥v∥2 ,
                               A s̄

namely mL2 a (1 ± A) — verified at five depths. In R
                                                   e units the block has eigenvalues m(1 + A)
and −m(A − 1), trace 2m (δ-independent,
                                   √          the value for 2m on-line zeros), and tr B 2 =
2m (1 + A ) ≥ 4m . Writing v/ L a = r + iq with r, q real, the normalisation v T v = 1 says
    2       2       2                2

r · q = 0 and |r|2 − |q|2 = 1, and
                       B                                          A+1                   A−1
                            = 2 (rrT − qq T ),           |r|2 =       ,        |q|2 =       .
                      mL2 a                                        2                     2
As δ → 0, A − 1 ∼ (2δ)2 ⟨u2 ⟩ϕ2 ∼ δ 2 L2 /3, and the pair becomes spectrally an on-line zero
of multiplicity 2m — the true enemy, as the brief said. An on-line zero of multiplicity m
contributes m uuT , positive semidefinite of rank one, eigenvalue m.

                                                        72
Then the part the brief had only flagged in passing ( By (P), for an on-line zero at height tu
with functional u and a pair at (tv , δ),
                                                                                           2
                 tr uuT · 2 Re(vv T ) = 2 Re (u · v)2 = 2 Re L Φ(tv − tu − iδ) ,
                                                                      


and Re Φ(x − iy)2 = C 2 − S 2 with
                  Z                                                Z
            C=        ϕ2 (u) cos(xu) cosh(yu) du,            S=        ϕ2 (u) sin(xu) sinh(yu) du,

which is negative near the zeros of C; the computed example had offsets x = 0, 0.4, 0.8, 2π/L, 1.3
giving ratios +2.46, +1.47, +0.06, −0.19, −0.04. Worse, the pair–pair cross terms
                                   h                  2                          2 i
                             4 Re Φ
                                  e x − i(δ1 − δ2 )        +Φ
                                                            e x − i(δ1 + δ2 )


can be of size ∼ −4A2 : two deep pairs (δL ≫ 1) offset by half a grid cell have blocks that
are nearly opposite “quadrupoles” 2(rrT − qq T ) and nearly cancel. So termwise diagonal
dominance, tr R e2 ≥ P
                        sites (self terms), is false, and whatever survives must be global. This is
the same phenomenon that forced BGSTB (2024) — as reported in referee C’s verdict — to
assume |β − 12 | < 1/(2 log T ) in order to extract simple zeros from their unconditional pair
correlation. Finally, truncation to the actual grid 0 ≤ k < d: for an on-line zero |utrunc |2 ≤ L2 a
exactly, by dropping nonnegative terms from (P) — and this, I flag, is the only normalisation
fact the final argument will need.

The extremal problem. The linear-algebra model of the windowed zero side, in R
                                                                             e units, is

    M=         mi ui uTi +        mj 2 Re(vj vjT ),       ui real unit,     vjT vj = 1,   m ∈ {1, 2, . . . },
          X                  X

           i                  j

where integer masses are coincident unit atoms, so without loss all masses are 1 with coincidences
allowed, and the prime side supplies tr M = N and ∥M ∥2F = T2 := N (1/λ + λ/3). The findings
of the experiments are three.
1. In every case min ∥M ∥2F = non + 4np exactly, with spectrum {1(non ) , 2(np ) } at the minimiser,
   strictly above the Cauchy–Schwarz/inertia floor N 2 /(non + np ) that Theorem 4 uses
   whenever non np > 0; the Cauchy–Schwarz extremal spectrum “all eigenvalues = 4/3” is not
   realisable by on-line points plus pairs. This is the integrality phenomenon, and it survives
   interactions.
2. What is false: with free masses sj = vjT vj > 0 the analogue fails (gap → −0.73, degenerate
   pairs with s → 0, A → ∞ acting as free mass movers); with free phases everything fails
   (v = e−iπ/4 r gives the zero block). Quantised mass and phase-locking — the latter forced
   by the functional equation together with Poisson — are both essential, exactly as, I remark
   from memory, integrality m ∈ {1, 2, . . . } is essential in Montgomery’s Nsimple ≥ 2N − m2 .
                                                                                              P

3. The counterexamples show that the correct inequality is linear in the masses, like m ≥
                                                                                           P 2

      (2m − 1), not quadratic.
   P

This is what led to the following.

Theorem (abstract; proved; this is the lever). Let M = Mon + Mp be Hermitian d × d
with Mon ⪰ 0, rank Mon ≤ r, tr Mon = ton , and Mp Hermitian with at most b (≥ 1) strictly
positive eigenvalues and tr Mp = t′ . Then for every c > 0

                                                           c2 r
                                       ∥M ∥2F ≥ c ton −         + 2c t′ − c2 b,                                 (3.1)
                                                            4

                                                      73
 and in particular, at c = 2,

                                     r ≥ 2ton + 4t′ − 4b − ∥M ∥2F .                                               (3.2)

 The proof is five lines, and von Neumann’s trace inequality (which I invoke from memory) is
 the only tool. Expand

                             ∥M ∥2 = ∥Mon ∥2 + ∥Mp ∥2 + 2 tr(Mon Mp ).

 Let µ1 ≥ · · · ≥ µr ≥ 0 be the eigenvalues of Mon ; let Mp = Mp+ − Mp− be the Jordan
 decomposition, p1 , . . . , pb′ > 0 (b′ ≤ b) the positive eigenvalues of Mp , ν1 ≥ ν2 ≥ · · · ≥ 0 the
 eigenvalues of Mp− , and y := ν.
                                   P

 (i) tr(Mon Mp+ ) ≥ 0 (two positive semidefinite matrices), and tr(Mon Mp− ) ≤                           k µk νk by von
                                                                                                         P

     Neumann, both sequences sorted decreasing. Pointwise, for µ, ν ≥ 0,

                                       2µν ≤ 2cν + ν 2 + (µ − c)2+ ,

    trivially for µ ≤ c, and for µ > c the difference of the two sides is (ν − µ + c)2 . Hence

                            2 tr(Mon Mp ) ≥ −2cy −                                 (µk − c)2+ .
                                                               X              X
                                                                       ν2 −
                                                                               k

(ii) By Cauchy–Schwarz on at most b positive eigenvalues, with                             p = t′ + y,
                                                                                      P


                                                       (    p)2 X 2 (t′ + y)2 X 2
                                                           P
                  ∥Mp ∥ =        p +                           + ν =         +
                             X         X
                        2        2             2
                                           ν       ≥                           ν .
                                                           b            b
(iii) ∥Mon ∥2 − k (µk − c)2+ = k gc (µk ), where gc (µ) = µ2 for µ ≤ c and 2cµ − c2 for µ ≥ c;
                P                P

      since gc (µ) ≥ cµ − c2 /4 for all µ ≥ 0,

                                                                          rc2
                                               gc (µk ) ≥ c ton −
                                         X
                                                                              .
                                         k≤r
                                                                           4

 Summing,

                                               rc2 (t′ + y)2
                            ∥M ∥2 ≥ c ton −        +             − 2cy
                                                4         b
                                               rc2        h (t′ + y)2       i
                                     ≥ c ton −     + min              − 2cy
                                                4     y         b
                                               rc2
                                     = c ton −     + 2c t′ − c2 b.
                                                4

 Three checks. (a) The minima non + 4np from the normalised experiment are exactly (3.2)
 with equality (ton = r = non , t′ = 2np , b = np ). (b) The 400 random instances of the sharper
 intermediate form
                                                               t′2
                             ∥M ∥2 ≥ r gs (ton /r) +               ,          s = t′ /b,
                                                                b
 gave most negative gap 0.0. (c) With b = t′ = 0, optimising over c returns ∥Mon ∥2 ≥ t2on /r, so
 the Cauchy–Schwarz count is a special case. The general optimisation over c I leave for the
 application; the case c = 2 is what matters at the extremal configuration.


                                                       74
5     Interruption, then the certificate tested on true zeros
5.1    The run is cut off; the coordinator writes out two thirds
At this point the run is cut off by a server error — immediately after the abstract theorem
(3.1)/(3.2) and its proof reach my report, and before anything about its application to the Weil
form has been written down.
The coordinator resumes me with a message which, notably, is the first place the consequence
(2 − 1/λ − λ/3)N → 23 N of my (3.2) is written out — by the coordinator, not by me; my own
“would give 2/3” at the extremal-problem stage was a forecast for (Q1), not this derivation —
together with a checklist for the bookkeeping. Condensed, with every item kept:
      You were killed by a server error after writing the abstract theorem (3.1)/(3.2);
      the report survived through that point and the proof checks out line by line. Now
      write the application to the windowed Weil form, giving
                                ′               ′
                           on (I ) ≥ 2 tr A + 2t − 4b − ∥A∥F
                          ndist                            2

                                         2 − λ1 − λ3 − o(1) N −→     2
                                                           
                                    ≥                                3 N,

      with every bookkeeping point explicit:
      (a) A is the windowed zero-side matrix, A = Mon +Mp in R-unitse      (divide G by L2 a);
           Mon ⪰ 0 of rank ≤ ndiston ; Mp the sum of pair blocks, with n+ (Mp ) ≤ b = npair
                                                                                         dist

           by subadditivity of inertia;
      (b) tr A and ∥A∥2F from the prime side (Theorem 4 Step 2, or the re-derivation)
           minus the tail E, bounded using θ0 = l T λ/2−1 and shown to be o(N );
      (c) t′ = j 2mj sj with sj = vjT vj on the truncated grid — prove sj ≥ 1 − o(1) for
                P

           interior pairs, absorb the O(D0 l) edge pairs, hence t′ ≥ 2b(1 − o(1)) − o(N );
      (d) ton uses |ui |2 ≤ 1 only through ton + t′ = tr A — confirm there is no other use;
      (e) conclude and optimise over c and λ: show c = 2, λ → 1− optimal given t′ ≥ 2b;
           note c = 8/3 would give 3/4 − b/N , which is circular;
       (f) state the final theorem, lim inf N0dist (T, 2T )/N (T, 2T ) ≥ 2/3 unconditionally;
           compare Montgomery 1973 (RH, 2/3 simple); does the argument also give
           simple-on-line ≥ 2/3? — try to sharpen (3.1) using that on-line masses are
           integers ≥ 1; if not, state distinct;
      (g) numerics: verify (3.2) on actual zeta matrices at T ∼ 1000–2000 with true zeros
           (t′ = b = 0 under observed RH) and compare with ndist   on and (2 − 1/λ − λ/3)N .

      Then higher moments (brief, defer to the HL agent’s report) and a final verdict of
      at most 250 words, verdict first.

5.2    The new certificate on true zeros beats Theorem 4
I take item (g) first. I build the windowed zero-side matrix A in R     e units directly from zeros:
l = log(T /2π), L = λl, d = ⌊LT /2π⌋, the grid τk = T + 2πk/L for 0 ≤ k < d, referee D’s
closed-form ϕ̂ (the flat-top transform times the Hann-ramp transform, ramp width w = ηL/2,
c = (L − w)/2) evaluated at complex arguments, L2 a obtained by quadrature of |ϕ̂|2 /2π, and
every zero with height in the enlarged window I ′ = [T − 30, 2T + 30], i.e. a reach of 30 on either
side. An on-line zero of multiplicity m at height t contributes m uuT with u = ϕ̂(t − τk ) k real;
an off-line pair at (t, δ) contributes m · 2 Re(vv T ) with v = ϕ̂(t − iδ − τk ) k . I accumulate ton
                                                                                

and t′ as the traces of the on-line and pair parts, count b as the number of distinct pairs, write
N ′ for the zero count of I ′ with multiplicity, and print two certificates — the lower bounds for


                                                 75
 on (I ) certified respectively by (3.2) and by Theorem 4’s Cauchy–Schwarz count:
ndist ′


                  NEW := 2 tr A + 2t′ − 4b − ∥A∥2F                     (from (3.2)),
                            2(tr A)2
                  OLD :=               − N′                            (Theorem 4),
                             ∥A∥2F

both as multiples of N (I) = #{γ ∈ (T, 2T ]}, together with ndist
                                                             on and whether NEW ≤ non
                                                                                   dist

holds. The zeros are the 100,000 ordinates located earlier.
Besides the true zeros I feed in synthetic worlds symmetric under the functional equation, in
the spirit of referee C’s synthetic-configuration test but chosen to probe the new inequality:
all zeros doubled; every fourth ordinate turned into a pair at depth δ with the next ordinate
deleted, so that the Riemann–von Mangoldt count is preserved; an adversarial lattice at the
mean spacing 2π/l whose pattern, per six zeros, is four on-line sites plus one tight pair —
on-line fraction 2/3 and T2 /N = (4 + 4)/6 = 4/3, the configuration that should saturate the
target; and “deep dephased pair-couples”, in which from each run of eight true zeros four are
kept and the other four replaced by two pairs at depth δ offset from each other by π/l — the
nearly cancelling quadrupoles found in the cross-term analysis.
At T = 1000, with N (I) = 868, d = 806 at λ = 1 and 726 at λ = 0.9, and N ′ = 921 true zeros
in I ′ :
      configuration                   tr A   ∥A∥2F ∥A∥2 / tr A (law)      NEW        OLD ndist
                                                                                          on
      true, λ = 1, η = 0.1          867.42 1203.26  1.387 (1.333)      +0.612N    +0.380N 921
      true, λ = 0.9, η = 0.1        868.13 1288.83  1.485 (1.411)      +0.515N    +0.286N 921
      true, λ = 1, η = 0.05         867.42 1184.95  1.366 (1.333)      +0.634N    +0.402N 921
      all doubled (N ′ = 1842)     1734.84 4813.05      2.774          −1.548N    −0.681N 921
      every 4th → pair, δ = 0.001 867.42 1578.33        1.820          +0.116N    +0.036N 460
      every 4th → pair, δ = 0.4     867.95 2359.76      2.719          −0.782N    −0.327N 460
      adversary lattice, δ = 0.001  805.99 1116.56  1.385 (1.333)      +0.534N    +0.356N 571
      adversary lattice, δ = 0.1    805.99 1131.45      1.404          +0.517N    +0.338N 571

Here “law” is the asymptotic value 1/λ + λ/3 of ∥A∥2F / tr A predicted by the prime side. The
rows not shown: the every-fourth-pair world at δ = 0.05 gives NEW +0.107N against OLD
+0.031N , and at δ = 0.2 both go negative (−0.034N and −0.048N ), all four depths having
ton = 433.52, t′ ≈ 434, b = 231; the dephased deep couples at δ = 0.3 and 0.6 push ∥A∥2 / tr A
up to 2.463 and 4.471 and the certificates down to −0.527N/ − 0.248N and −2.534N/ − 0.613N
respectively — vacuous, as they should be for worlds carrying this much Frobenius mass.
In the adversary lattice ton = 537.95, t′ = 268.04, b = 142, N ′ = 855, and ndist
                                                                             on = 571, so the
new certificate, 463.5, sits just under the truth, while the old one gives 308.6. In every row
the check NEW ≤ ndiston comes back true, as it must for a theorem about A. And on the true
zeros the new certificate certifies 0.61–0.63N distinct zeros on the line where Theorem 4’s
Cauchy–Schwarz certificate gives 0.38–0.40N — this with the observed ratio ∥A∥2 / tr A still
somewhat above its asymptotic law 1/λ + λ/3 at this height.


6      Applying the inequality: two thirds distinct, unconditionally
6.1     Bookkeeping on the windowed form; no pair data needed
Now the application of (3.2) to the windowed Weil form, following the coordinator’s checklist
but simplifying it where I can.

Objects. Everything is in referee D’s coefficient coordinates and my normalisation: R     e :=
G/(L a) with Gkl = W (fk , fl ), 0 ≤ k, l < d. On the zero side R = A + E, where A collects the
    2                                                           e


                                                 76
zeros with height in the enlarged window I ′ = [T − D0 , 2T + D0 ], D0 = T 1/2 , and E is the tail.
Grouping A by distinct points, the on-line part is

                                                                               ϕ̂(ti − τk ) k
                                                                                                 
               Mon :=                                                     ui =                real,
                              X
                                          mi ui uTi ,                             √
                        on-line ti ∈I ′                                              L2 a

so Mon ⪰ 0 and rank Mon ≤ r := ndist
                                on (I ); the pair part is
                                     ′


                                            Mp :=           mj 2 Re(vj vjT )
                                                        X

                                                        j

over the distinct off-line pairs in I ′ . Each pair block is a pullback of m
                                                                           0 m , hence has at
                                                                                                        
                                                                             0
most one positive eigenvalue by Lemma 1 of Theorem 4 (inertia does not increase under
pullback, dependent functionals included), and the positive index of inertia is subadditive,
so n+ (Mp ) ≤ b := ndist
                     pair (I ). Thus A = Mon + Mp , and referee C’s Riemann–von Mangoldt
                            ′

bookkeeping gives

                          N (I ′ ) ≥ Non (I ′ ) + 2b,                 Non (I ′ ) :=
                                                                                      X
                                                                                          mi ,
                                                                                      i

the on-line zeros counted with multiplicity. This is the coordinator’s item (a) as stated.

The one normalisation fact.                 The only property of the vectors I use is
                               1 X                         1 X
                   |ui |2 =              ϕ̂(t i − τk )2
                                                        ≤          ϕ̂(ti − τk )2 = 1,
                              L2 a 0≤k<d                  L2 a k∈Z

by dropping nonnegative terms and applying the Poisson identity (P). Hence

                               ton := tr Mon =                  mi |ui |2 ≤ Non (I ′ ).
                                                        X

                                                            i

Nothing whatever is assumed about the individual pair traces t′j = 2mj Re(vjT vj )trunc on the
truncated grid — they may be anything near the window edges or for deep zeros; only the
total t′ := tr Mp = tr A − ton enters. Here I depart from the coordinator’s checklist explicitly:
its item (c), “prove sj ≥ 1 − o(1) for interior pairs, absorb edge pairs”, is not needed, and edge
pairs require no separate treatment. Item (d), the request to confirm that |ui |2 ≤ 1 is used
nowhere else, is settled by the same observation.

The certificate.     Applying (3.2) to A = Mon + Mp ,

                   r ≥ 2ton + 4t′ − 4b − ∥A∥2F = 2 tr A + 2(t′ − 2b) − ∥A∥2F ,

and

                           t′ − 2b = tr A − ton − 2b
                                      ≥ tr A − Non (I ′ ) − N (I ′ ) − Non (I ′ )
                                                                                            

                                      = tr A − N (I ′ ).

Therefore
                                       ′                  ′
                                  on (I ) ≥ 4 tr A − 2N (I ) − ∥A∥F .
                                 ndist                                                                       (4.1)
                                                                  2


This is cleaner than the coordinator’s 2 tr A + 2t′ − 4b − ∥A∥2F : it contains no pair data at
all. It is the certificate in what follows — the lower bound for distinct on-line zeros that the
argument actually certifies from the data of A.

                                                                77
The tail.   From referee D’s tail estimate,

                                             m∥uρ ∥2 =: θ0 ≤ 2A0 L2 log(4T ) T λ/2−1
                                      X
                      ∥E∥op ≤
                                       / ′
                                      ρ∈I

(in R
    e units, up to a factor L/(L2 a) < 1), and the same sum bounds | tr E| and the trace norm
∥E∥1 , since E is a sum of blocks of trace norm at most 2m∥uρ ∥2 . So tr A = tr R
                                                                                e + O(θ0 ), and

                     ∥A∥2F = ∥R          e 2 + 2∥E∥op ∥R∥
                              e − E∥2 ≤ ∥R∥
                                    F      F
                                                       e 1 + ∥E∥1 ∥E∥op ,
                                        e 1 ≤ ∥A∥1 + ∥E∥1 ,
                                       ∥R∥

with

                                     mi |ui |2 +           2mj ∥vj ∥2trunc
                             X                     X
                 ∥A∥1 ≤
                                on                 pairs
                                                                                              T λ/2
                         ≤ N (I ′ ) max 1, A(δ)                 ≤ N (I ′ ) eL/2 = N (I ′ )
                                                           
                                                                                                        ,
                                                                                              2π
because A(δ) =       ϕ2 e2δu / ϕ2 ≤ eδL ≤ eL/2 for |δ| ≤ 12 and truncation only lowers ∥v∥2 . Hence
                 R          R


                                   e 2 + O N T λ/2 · L2 l T λ/2−1
                          ∥A∥2F ≤ ∥R∥
                                                                                    
                                      F
                                     = ∥R∥                    e 2 + o(N )
                                        e 2 + O N l3 T λ−1 = ∥R∥
                                                                        
                                           F                     F

for fixed λ < 1. I stress what is not used: no zero-density theorem, no bound on individual
eigenvalues, no eigenvalue threshold θ; (4.1) uses the rank and inertia of A exactly.

6.2     The constant two thirds and its sharpness
Prime side and the constant. The unconditional prime-side input is the one already
refereed for Theorem 4 — its Step 2, equivalently the re-derivation agent’s Theorems A/B and
referee D’s evaluation:

               tr R
                  e = N (I) (1 + o(1)),                                e 2 = N (I) tλ (1 + o(1)),
                                                                      ∥R∥ F

where
                                                bw + λ2 Jw    1 λ
                                        tλ :=              −→  +
                                                     2
                                                   λaw        λ 3
as the taper parameter η = 1/ log l → 0 (aw , bw , Jw being referee D’s taper functionals),
together with N (I ′ ) = N (I)(1 + O(T −1/2 )). Inserting these into (4.1),

                     ′
                                                                              1 λ      
                on (I ) ≥
               ndist             4 − 2 − tλ − o(1) N (I) = 2 −                  − − o(1) N (I),
                                                            
                                                                               λ 3
and N0dist (T − D0 , 2T + D0 ) ≥ ndist
                                   on (I ) — the formula the √
                                        ′                      coordinator wrote out from my
(3.2). As λ → 1 this is 2 − 3 = 3 . It is positive iff λ > 3 − 6 = 0.5505, the same threshold
                −             4   2

as Theorem 4; and for every λ ∈ (0.55, 1] the new constant 2 − t beats Theorem 4’s 2/t − 1,
because (t − 1)(t − 2) ≤ 0 on 1 ≤ t ≤ 2: at λ = 1, 0.667 against 0.500; at λ = 0.9, 0.589 against
0.417; at λ = 0.8, 0.483 against 0.324.
On the coordinator’s item (e): optimising c in (3.1) rather than fixing c = 2 gives, with x = ton
and t = tλ ,

                                                (2N − x)2
                                        r ≥               − 2(N − x),
                                                   tN

                                                                78
which the adversary minimises at x = (2 − t)N to the same value (2 − t)N , while at x = N (no
off-line zeros) it equals N/t, the Cauchy–Schwarz 3N/4. So c = 2 is optimal at the extremal
configuration and nothing is lost globally; and c = 8/3 would formally give 3N/4 minus terms
involving b — circular, as the coordinator noted.
On composition with the sibling’s kernel optimisation: the bound is 2−t∗ (λ) for whatever t∗ the
optimal taper achieves. It is the exact analogue of Montgomery’s Nsimple ≥ (2−F -functional)N ,
so — from memory, not pursued and not checked here — Montgomery–Taylor/Cheer–Goldston-
type kernels (RH-simple 0.6725 . . .) would transfer verbatim if their prime-side evaluation were
available for the Gabor realisation. The sibling’s report says the admissible pair-correlation
kernels are exactly |FT w|2 with w ≥ 0, a restriction relative to Montgomery–Taylor, so on
that route 2/3 improves to roughly 0.67 at best.

Theorem 4′ (claimed). Unconditionally, with the same analytic input as Theorem 4 —
Weil’s explicit formula, Riemann–von Mangoldt, PNT-strength Λ2 /n, Montgomery–Vaughan
                                                           P

— plus von Neumann’s trace inequality:
                N0dist ([T, 2T ])   2                                             1 λ
      lim inf                     ≥ ,   and for support parameter λ,     ≥ 2−      − .
        T        N ([T, 2T ])       3                                             λ 3
The constant 2/3 is sharp for the information {tr R,  e 2 , block structure}: take 2N/3 simple
                                                  e ∥R∥
on-line zeros on the lattice (2π/l)Z (mutually orthogonal for the sinc kernel at λ = 1) plus
N/6 tight off-line pairs (δ → 0) on the remaining sites; then

                                            2N   4N   4N                    2N
                    tr R
                       e = N,       e 2=
                                   ∥R∥         +    =    ,          on =
                                                                   ndist
                                             3    6    3                     3
— the brief’s extremal picture, spectrally identical to Montgomery’s RH-extremal “2N/3 simples
plus N/6 doubles”.
The comparisons I record are all from memory, with no lookup: Montgomery 1973 under RH
gives ≥ 2/3 simple; RH plus the integer inequality (m − 1)(m − 2) ≥ 0 gives ≥ 5/6 distinct
(elementary — the brief’s own arithmetic; I believe it folklore or known but could not verify
a citation offline; Bui–Heath-Brown-type papers quote 0.8466 distinct under RH via better
kernels, consistent with 5/6 = 0.8333 being the Fejér-kernel value); Cauchy–Schwarz gives 3/4
distinct. Theorem 4′ is the (m − 1)2 ≥ 0 level of integrality, “ m2 ≥ 2N − Ndist ”, transplanted
                                                                P

off the line: 2/3 distinct on-line, no RH — the level the brief had itself written down for n+
and set aside.

Simple zeros: no. On the coordinator’s item (f), sharpening to simple on-line zeros, the
answer is negative. Rank counts distinct points, so directly one gets only
                                                               N
                     N0simple ≥ 2ndist
                                  on − Non ≥ (3 − 2t)N =               (λ = 1),
                                                               3
below Bui–Conrey–Young’s 0.407 (again from memory). I tried to sharpen (3.1) using that
on-line masses are integers: ∥Mon ∥2 ≥ m2i ≥ 2Non − Non    simple is true, but step (i) of the proof
                                       P

consumes the eigenvalue slack k (µk − c)+ of Mon , which integer masses do not control —
                                            2
                                P

coincident or nearly coincident distinct simple zeros and a double zero are indistinguishable
to the spectrum of Mon . So: distinct, not simple. Counting on-line zeros with multiplicity,
Non (I ′ ) ≥ ndist
              on ≥ 2N/3 as well (against Pratt et al.’s 5/12, from memory).


Numerics. For the record I collect the certificate computation on true zeros just run (zero side
exact from the 100,000 cached ordinates, T = 1000, I ′ = [970, 2030], N (I) = 868, N (I ′ ) = 921,


                                                79
everything in units of N (I), NEW the certificate from (3.2), OLD Theorem 4’s): true zeros
NEW +0.612 / OLD +0.380 with ∥A∥2 / tr A = 1.387 against the law 1.333; at λ = 0.9,
+0.515/ + 0.286; at η = 0.05, +0.634/ + 0.402; all doubled −1.548 (vacuous); every fourth
ordinate a pair at δ = 0.001: +0.116/ + 0.036 with ndist
                                                      on /N = 0.530, and NEW +0.107, −0.034,
−0.782 at δ = 0.05, 0.2, 0.4; the adversary lattice +0.534/ + 0.356 with ndist
                                                                            on /N = 0.657 —
near-extremal, the gap being the finite-l excess 0.385 versus 0.333 — and +0.517 at pair depth
0.1; dephased deep couples −0.53, −2.53. On true zeros the new certificate is 0.61–0.63N (law:
2 − 1.387 = 0.613, tending to 2/3 as l → ∞) versus 0.38–0.40N for Theorem 4, and (3.2) holds
in every synthetic world, as it must, deep or dephased pairs only making ∥A∥2 larger.

6.3    The brief’s other levers and higher moments
Lever (a) and lever (b). Lever (a), the negative spectrum alone — adding n− ≤ npair and
tr R− to the Cauchy–Schwarz count: as the brief anticipated, it is useless against tight pairs,
since the negative eigenvalue q = m(A − 1) → 0 as δ → 0, and the Cauchy–Schwarz-plus-inertia
extremal is not moved by it. What works is negative spectrum and rank jointly — that is the
theorem: step (i) charges the negative part of Mp against the large eigenvalues of Mon via
von Neumann, step (ii) charges the positive part via n+ ≤ b. The tight pair is not beaten (it
cannot be) but is correctly priced at the equivalent of 4m2 , at least 2 per zero against 1 per
simple on-line zero — integrality.
On lever (b): under RH, m2 ≤ 4N/3 with integer m gives Ndist ≥ 5N/6 (k doubles plus
                           P

N − 2k simples: N + 2k ≤ 4N/3) and Nsimple ≥ 2N/3, against 3/4 from Cauchy–Schwarz.
Unconditionally the (m − 1)2 ≥ 0 level is recoverable robustly — that is (3.1) — but the
(m − 1)(m − 2) ≥ 0 level is not: eigenvalues of interacting simple zeros fill (0, 2), and “no
eigenvalue in (1, 2)” is false already under RH+GUE, where the Gram spectrum has mean 1 and
variance 1/3 at λ = 1. (Editorially: this confirms the brief’s forecast that the (λ−u)(λ−2u) ≥ 0
level is robustly false; what the brief did not foresee is that the lower level, which it had found
useless when aimed at n+ , carries the whole result when aimed at rank.)

Higher moments, (b)(ii). On the zero side

                                tr R
                                   ek =                     Φ(γ
                                                            e j − γj+1 ),
                                            X          Y

                                          γ1 ,...,γk    j

exact via (P) with complex γ allowed — a Rudnick–Sarnak-type smooth k-correlation statistic
whose Fourier support, in Montgomery’s α-units, reaches j |ξj | = kλ for k even and (k − 1)λ
                                                         P

for k odd. From memory — I did not fetch it — Rudnick–Sarnak 1996 (Duke 81) prove the
n-level correlations are GUE for |ξj | < 2 and state explicitly that RH is not assumed; on
                                   P

the prime side this is “only diagonal solutions contribute”, the off-diagonal being killed by
Montgomery–Vaughan iff X k/2 ≪ T . So: k = 2 needs λ < 1 (used); k = 3 needs (k − 1)λ < 2,
i.e. λ < 1, admissible on the whole useful range (the ppp diagonal n3 = n1 n2 forces prime
powers of a single prime, lower order; main terms from µ3 and µ · P P ); k = 4 needs 4λ < 2, i.e.
λ < 1/2, inadmissible where useful, and for λ < 1/2 the dimension d = λN < N/2 kills any
on-line certificate anyway, since n+ ≤ d.
But an odd moment cannot improve a lower bound for a count on [0, ∞): given (m1 , m2 ),
the infimum m21 /m2 of the number of positive eigenvalues is approached for any prescribed
m3 ≥ m22 /m1 , by putting mass ε at height h → ∞ (which feeds m3 and nothing else);
dually, an LP certificate p(µ) = c1 µ + c2 µ2 + c3 µ3 ≤ 1 on (0, ∞) needs c3 ≤ 0 and is then
dominated by its quadratic part, and with d known a constant term c0 must be ≤ 0 because
p ≤ 0 on (−∞, 0]. The third moment would help only together with an a-priori bound
λmax (R)
      e = O(1), i.e. a pointwise bound for P
                                               n≤X Λ(n)n
                                                         −1/2−iτ on windows of length 1/L —


                                                       80
Lindelöf-strength, unavailable; the re-derivation agent’s Remark 7.4 is the same obstruction.
So tr R
      e 3 is unconditionally computable and useless, while tr R
                                                              e 4 would be useful and is not
computable for λ > 1/2. Departing from the brief’s DO-list, I therefore do not compute the
GUE constants m3 (λ), m4 (λ) — moot — and defer to the HL agent’s report for higher-level
material. The moment route cannot reach 2/3; the structural route does, with k = 2 only.

My verdict. The block facts are confirmed exactly. The new ingredient is Theorem (3.1) —
elementary, proved above, numerically unfalsified — plus the bookkeeping (4.1), which uses only
rank Mon ≤ ndist
              on , n+ (Mp ) ≤ npair , |ui | ≤ 1, N (I ) ≥ Non + 2npair , and the Theorem-4/referee-
                                dist       2         ′

D tail bound. Given the refereed prime-side asymptotics (tr R      e ∼ N , ∥R∥e 2 ∼ (1/λ + λ/3)N ,
λ < 1), the constant 1/2 of Theorem 4 becomes 2/3 for distinct zeros on the critical line,
unconditionally, and sharp for this information; simple-on-line is only 1/3 by this route. Referees
C’s and D’s extraordinary-strength caveat applies verbatim, now even more so: everything rests
on Step 2’s upper bound for ∥R∥ e 2 . Nothing in the theorem or the bookkeeping is asymptotic
                                    F
or delicate; the one place λ < 1 enters the application is ∥E∥op ∥A∥1 = O(N l3 T λ−1 ). With
that the report goes to the referees as final.
My closing message to the orchestrator puts the verdict first: “the pair-block/negative-spectrum
lever reaches exactly 2/3 (distinct on-line), via a new elementary inequality; higher moments
cannot.” The rest recapitulates, with nothing new computed or looked up: the block facts
confirmed exactly (the Poisson identity for complex arguments, v T v = L2 a real and depth-
independent, ∥v∥2 = L2 a A(δ), pair eigenvalues mL2 a(1 ± A)), cross terms sign-indefinite
so that termwise diagonal dominance is false; lever (a) alone useless against tight pairs, as
expected, but negative spectrum plus rank jointly give (3.1), verified numerically with the
linear-algebra minima matching it with equality; with c = 2 and the Riemann–von Mangoldt
bookkeeping,

                 ′                  ′
                                                               1 λ           2N
            on (I ) ≥ 4 tr A − 2N (I ) − ∥A∥F ≥
           ndist                                           2−
                                            2
                                                                 − − o(1) N −→    ,
                                                                λ 3             3
using only |ui |2 ≤ 1, inertia and rank of blocks, the tail bound (needing λ < 1) and the
already-refereed prime-side traces; numerics at T = 1000 on true zeros giving 0.61–0.63N
against Theorem 4’s 0.38–0.40N , every synthetic and adversarial world satisfying the inequality
and the lattice-plus-N/6-tight-pairs configuration extremal; under RH integers give 5/6 distinct
(likely folklore; citation unverified offline) while unconditionally only the (m − 1)2 level transfers,
and simple-on-line is only 1/3; tr R3 admissible for λ < 1 but provably unable to improve the
count without a λmax bound, tr R4 needing λ < 1/2 where d < N/2 kills everything. What
could go beyond 2/3: better kernels (the sibling’s route, about 0.67) or the (m − 1)(m − 2)
integrality level, which interactions destroy.


                                                  81
Appendix


   82
Literature along the way

A     Literature along the way
This appendix ties the ideas of Parts I and II to the published literature: which works were in
play at each step, whether they were recalled from the model’s prior knowledge or actually
retrieved during the campaign, by which agent and when, and what role each played. It is
reconstructed from the campaign’s complete logs, in which every web search, every download,
every file read and every message between the coordinator (Part I calls it the orchestrator)
and an agent is recorded. An influence that came only through the model’s training is invisible
to such logs, and we say so where it matters. Unless stated otherwise, times are given relative
to the moment the one-half run of Part I returned its result; the two-thirds run of Part II was
launched about seven and a half hours after that. The appendix traces provenance; it certifies
no mathematics.

A.1    How literature could enter
Every agent in the campaign could search the open web and download papers — arXiv abstracts,
PDFs and LATEX sources, open-access journals, EuDML, zbMATH and public abstract pages —
and many did: across the three days roughly a hundred arXiv papers and some ninety other
scholarly pages were retrieved, all from the open web. The two runs narrated in Parts I and II
retrieved nothing: neither made a network request of any kind. Nor did the coordinator, at
any point in the campaign; and it read almost nothing from disk — over the whole campaign
a handful of files, all written by agents that had themselves used no network. Consequently
the only route by which downloaded material could travel from one agent to another was: the
downloading agent’s files, if a later agent was told to read them; or the short final message
with which each agent reported back to the coordinator, and whatever of it the coordinator
then put into a later brief. Both routes are visible in the logs, and both are followed below.
The inputs of the one-half run were the coordinator’s brief, the report, notes and code of one
earlier run (R4), the reports of two others (N6, frontier-1) — none of which had used the
network — and two tables of zeta zeros used for validation. The inputs of the two-thirds run
were its brief and one later message, the one-half run’s proof file, the verdict files of referees C
and D, the re-derivation agent’s proof, and, once, the first six thousand bytes of its sibling’s
report; of these only referee C’s verdict carried anything derived from a download (a paragraph
identifying the one-half run’s prime-side trace with a published theorem as read from the PDF,
two sentences of published proportions of distinct and simple zeros, and an arXiv number),
and referee D’s verdict names the same paper once — none of it bearing on the lemma or the
bookkeeping of Part II.

A.2    Before the one-half run: the frame
The proposal to treat the condition space as a Pontryagin space Πκ and to use the Pontryagin
(1944)/Kreı̆n–Langer bound on non-real spectrum to bound off-line zeros is the coordinator’s,

                                                83
stated in the brief that launched the one-half run (Part I, §1). The words “Pontryagin”,
“Kreı̆n–Langer” and “Πκ ” occur in essentially no earlier record of any agent in the campaign
(one unrelated use of “Pontryagin” aside) and in no document any agent had downloaded; R4’s
report, which prompted the idea by finding its operator indefinite (“Kreı̆n, not Hilbert”), cites
nothing and was produced without network access, as were the reports R4 itself had read.
The frame was not read from any paper. One qualification the logs impose: notes from an
earlier session of the same project, which the coordinator had skimmed at the very start of the
campaign as a list of one-line summaries, already described Weil’s 1952 positivity criterion
“recast as a Gram/signature statement” on a finite, prime-computable matrix; whether that
exposure, some twenty hours earlier, cued the reframing cannot be decided from the logs.
The brief’s pointers for the conjectured identity (negative index of W = number of off-line
zeros) — Bombieri’s 2000 note on Weil’s quadratic functional, Yoshida’s work of the 1990s,
Burnol — are recalled and explicitly hedged (“Yoshida? Bombieri?”); none had been retrieved
by anyone at that point. Weil’s criterion and the explicit formula are classical and recalled;
the normalisation is the textbook one that N6’s earlier run had validated numerically. The
Turán/Nazarov-type lemmas and the Selberg–Levinson–Conrey benchmark in the brief (“can
the negative-index route REPRODUCE a positive-proportion result?”) are likewise recalled;
the run showed the former bound the wrong operator and used the latter only as the target it
then met.

A.3    The one-half run (Part I): memory only
Every paper the one-half run names it names from memory, and it says so in its own notes (“I
do not know a reference; the closest are . . . ”, “Literature (from memory, unverified offline):
Yoshida 1992 . . . , Bombieri 2000 . . . , Burnol”, “KNOWN RESULTS FOR COMPARISON:
. . . (from memory)”). When the dual argument of Part I, §5 produced the prime-side lower
bound (tr R)2 / tr R2 → 34 N , the run recognised the number as the classical consequence, by
Cauchy–Schwarz, of Montgomery’s 1973 RH-conditional theorem (“≥ 34 distinct”) and the
evaluation as Montgomery’s prime-side computation via the Montgomery–Vaughan mean value
theorem — both recalled; by its own account the inequality was applied from memory, with no
way to check its constant during the run. Nothing the run had read mentions Montgomery,
pair correlation or 34 ; the only agents downloading anything during those hours were working
on Epstein, Dedekind and Beurling zeta functions for unrelated branches, into files this run
never opened. In its red-team notes (Part I, §7), about a quarter of an hour before returning,
the run listed the closest literature it could recall — Montgomery 1973, Gallagher–Mueller,
and “Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh’s unconditional pair-correlation F (α)
(2023/24), where — as far as I recall — no unconditional proportion on the line is drawn” —
and ranked “too short to be new” as its top risk. This is a pointer, not a citation: no title,
identifier or theorem statement was available to it; its role was to tell the referees where to
look. The records it quotes (5/12, Pratt–Robles–Zaharescu–Zeindler; 0.407 simple on the line,
attributed to Bui–Conrey–Young) and the line “Under RH: ≥ 2/3 simple (Montgomery), ≥ 3/4
distinct (C-S)” are marked “from memory”.

A.4    The referee round and the literature agent
Three blind referees (from about four minutes after the run returned). Each was
given the run’s proof file and notes and one joint of the argument to break; they were told
not to read each other’s work, and did not. Referees A and C turned to the web about 80
minutes after the run returned, referee B about two and a half hours after; all three searched
for the four author names the run had recalled, located An unconditional Montgomery theorem
for pair correlation of zeros of the Riemann zeta function (Baluyot, Goldston, Suriajaya,


                                               84
Turnage-Butterbaugh; arXiv 2306.04799, Acta Arith. 2024), and read it (abstract page or
PDF). What this established: the prime-side asymptotic the run had evaluated is, in smoothed
form, Theorem 1 of that paper — published and unconditional — so the entire burden of
the one-half claim sits on that single evaluation; and the same paper’s introduction gave
referee C the standard list of records (Pratt–Robles–Zaharescu–Zeindler 41.7%; Montgomery,
Montgomery–Taylor and Chirre–Gonçalves–de Laat under RH). Referees A and B also opened
the abstract of the sequel on proportions of simple and critical zeros (arXiv 2501.14545), and
referee A the abstract of the pair-correlation-conjecture paper (arXiv 2503.15449); a search by
referee C returned Farmer’s 1995 Counting distinct zeros of the Riemann zeta-function. All of
this is verification and positioning. Two things the referees added were their own: referee C’s
observation that rank in place of inertia gives ≥ 43 distinct, hence ≥ 12 simple (its code computed
the rank statistic about twenty minutes before its first search, and it had read the run’s own
line on 23 simple and 34 distinct under RH an hour earlier; the integer step it uses appears in
no text it downloaded, though whether the downloaded abstract’s discussion of proportions of
simple zeros prompted the phrasing cannot be decided from the logs); and referee A’s discovery
of the mass-matrix gap and its “never orthonormalise” repair, which concern Gram matrices
and owe nothing to the pair-correlation papers it had opened. Referee B derived the exact
reduction to the Montgomery–Vaughan mean value theorem about twenty minutes before its
first search and used the download only to identify the published theorem. Referee D, later,
worked without network access; the exact Poisson identity it proved had been suggested by
the coordinator in its brief. This is the model case for the whole chain: a paper named from
memory inside a run, located on the web by the next agents, and used to verify and to position.

The blind re-derivation (launched about two and three-quarter hours after). For-
bidden to read the run’s proof, it re-derived the prime-side traces with error terms in two
repaired normalisations, with no network access, citing nothing it did not recall.

The literature agent (launched about two and three-quarter hours after; reported
about four hours after). This is where papers were actually read. It downloaded and read
the LATEX sources of arXiv 2306.04799, 2501.14545 (Baluyot–Goldston–Suriajaya–Turnage-
Butterbaugh, Pair correlation of zeros of the Riemann zeta function I ), 2503.15449 (Goldston–
Lee–Schettler–Suriajaya, Pair correlation conjecture for the zeros of the Riemann zeta-function I:
simple and critical zeros), 2511.20059 (Goldston–Suriajaya, Zeta zeros on the critical line) and
2603.28104 (Goldston–Suriajaya, Zeta zeros in a narrow vertical box); then Farmer (1995), the
abstract of Wu’s Distinct zeros of the Riemann zeta-function (Q. J. Math. 2015; more than
66% distinct), the abstract of Bui–Heath-Brown (arXiv 1302.5018), Conrey–Ghosh–Gonek’s
Simple zeros of the Riemann zeta-function (1998), Bombieri’s 2000 note via EuDML, and two
of Suzuki’s screw-function papers (arXiv 2606.09096, 2206.03682). Its findings, by role:
• Verification. The run’s tr R2 is literally the Fejér-kernel sum of the 2024 paper’s Theorem 1
  (equivalently “Aryan’s lemma” in Goldston–Suriajaya, ( 43 + o(1))N unconditionally); the
  published works lose unconditionality only when they pass to diagonal terms by termwise
  kernel positivity (the thin-box hypothesis), which the inertia argument does not do.
• Positioning. Goldston–Suriajaya state the removal of RH from Montgomery’s argument
  — which would give 23 simple and on the line — as an open problem; no published work
  combines the positive index of the compressed Weil form with a pair-correlation second
  moment to count zeros on the line; Bombieri (2000) already has the negative-index half of
  the run’s Theorem 1 for large truncations, so that half is prior art; and the records against
  which the claim would be measured (Wu 66.04% distinct — a number obtained from the
  download, the agent’s own search query having guessed a different one; 5/12 on the line).
  The two Suzuki papers were checked for a precedent linking signature to off-line zeros and


                                                85
   yielded none.
 • Formulation. Reading Goldston–Lee–Schettler–Suriajaya’s and Goldston–Suriajaya’s “hori-
   zontal multiplicity” H(γ) (the number of zeros, with multiplicity, on the horizontal line
   t = γ; H(γ) = 1 forces a zero to be simple and critical), the literature agent observed that
   the zeros certified by the run’s certificate are H(γ) = 1 zeros — “the Cauchy–Schwarz-
   weakened form” of Goldston–Suriajaya’s Theorem 2. The coordinator put this into the
   brief for the write-up (nearly five and a half hours after the run) as something to verify
   from the inertia bookkeeping and to state only if proven; the paper-writing agent verified it
   by its own one-line count and made “simple and on the critical line” the statement of the
   one-half theorem in the draft. The proof is the run’s; the form of the statement is the one
   place on the whole chain where a downloaded paper contributed wording that survives.
The paper-writing agent, launched nearly five and a half hours after the run returned, read
the Goldston–Suriajaya source and the first pages of the other downloads directly from the
literature agent’s files, for its bibliography and related-work section. No agent anywhere in the
campaign made a network request during the three and three-quarter hours that followed the
literature agent’s last download — the stretch in which the referee for the mass-matrix gap
reported, the paper-writing agent drafted, and the two-thirds push was decided.

A.5    The two-thirds push (Part II and its siblings)
The target. Two thirds as Montgomery’s RH-conditional constant had been in the coor-
dinator’s own words since shortly after the one-half run returned (its brief to referee B, six
minutes after, asks whether the classical RH result “is Montgomery’s ≥ 2/3 simple (RH) . . .
— where does 3/4 come from?”), and the run’s proof file records “under RH: ≥ 2/3 simple
(Montgomery)”. The Goldston–Suriajaya sentence — that an RH-free version of Montgomery’s
computation would give two thirds simple and on the line, and that this is open — reached the
coordinator in the literature agent’s report about four hours after the run returned and was
plainly live when the target was set: about seven and a quarter hours after the run returned,
answering the question of what would come next, the coordinator wrote that one half to two
thirds “is a real, well-posed target (it’s exactly the Cauchy–Schwarz loss versus Montgomery’s
RH-conditional 2/3)” and, in the same message, suggested sending the draft to the authors of
the open problem, “since it’s their theorem being used and their open problem being claimed”.
Three minutes later the human typed “Push it to 2/3”; the two-thirds run’s brief followed
fifteen minutes after that. The logs cannot say what weight the published open-problem
statement carried against the recalled constant and that instruction; they do show that it
supplied no technique — the route of Goldston and Suriajaya (termwise positivity under a box
hypothesis) is precisely the obstruction the literature agent had diagnosed, and Part II goes
the other way. The draft’s later framing sentence, “matching Montgomery’s RH-conditional
1973 constant unconditionally . . . Goldston–Suriajaya’s open problem”, was dictated by the
coordinator with the instruction to cite their statement of the problem precisely.

The integer template and 5/6. The arithmetic in the two-thirds brief — Montgomery’s use
of integrality, m2 ≥ (2m − 1), giving 2/3 simple under RH; the observation that integrality
               P        P

also gives 5/6 distinct; and “2 · (5/6)N − N = 2N/3 ✓✓ EXACTLY THE TARGET” — was
derived by the coordinator while writing the brief (the text carries its own running check marks
and the aside “is 5/6-distinct-under-RH known? surely — Montgomery’s paper or folklore;
CHECK literature”), seven minutes after it had set out the two levers. No text upstream of
the coordinator contains it. One coincidence is worth recording: the literature agent’s findings
file had, for about four hours by then, a line noting that integer combinatorics gives ≥ 5/6
distinct under RH, attributed there to Conrey–Ghosh–Gonek; the coordinator never read that


                                               86
file, and the agent’s report to it did not carry the line. (The optimal-window sibling read the
file two minutes after the two-thirds run was launched, its own brief having already set “target
c∗ ≥ 5/6”. When the draft briefly attributed the 5/6 to Conrey–Ghosh–Gonek, a cold-read
referee of the draft (the cold referee below), working from the downloaded texts, re-attributed
it to Montgomery plus integrality.)

Pair blocks and the Poisson identity. The block facts the brief asked the run to verify —
v T v = L2 a real and depth-independent, ∥v∥2 = L2 a A(δ), eigenvalues mL2 a(1 ± A) — were
the coordinator’s own quick algebra, done on top of referee C’s block-structure lemma and
referee D’s exact Poisson identity k φ̂(z − τk )φ̂(z ′ − τk ) = L Φ(z − z ′ ), both obtained without
                                  P

network access. Nothing here has a published source among the run’s inputs.

The trace inequality. The rank–trace lemma of Part II and its five-line proof are the
run’s. The one classical tool it invokes, von Neumann’s trace inequality, was recalled: the
phrase occurs nowhere in the campaign’s logs before the run’s report, and the brief had offered
Weyl’s inequalities, Cauchy interlacing and Ky Fan’s principle instead. The bookkeeping of the
application (Part II, §6) uses only quantities already established in the campaign (the refereed
prime-side traces, referee D’s tail bound) and Riemann–von Mangoldt.

Higher moments, and why they were closed. The brief’s alternative lever — prime-side
tr R3 , tr R4 in a restricted-support regime, with “Rudnick–Sarnak 1996 / Hughes–Rudnick:
which are unconditional? — CHECK” — was recalled by the coordinator. The run settled its
own case itself (tr R3 admissible for λ < 1 but unable to improve the count; tr R4 needs λ < 1/2).
The higher-moments sibling (“the HL agent” of Part II), launched forty-one minutes after the
two-thirds run, proved the general no-go (“Theorem U”) without downloading anything; its
only network use was two web searches, about ten hours after the one-half run returned, for
the abstracts of Goldston–Lee–Schettler–Suriajaya (arXiv 2503.15449: the pair correlation
conjecture for all α implies 100% simple and critical) and Goldston–Suriajaya, used to position
its conditional theorem as complementary to theirs; the “PCC ⇒ 100%” fact had already been
relayed to it in its brief, from the literature agent’s report. The generalisations agent and its
two literature sub-agents — launched about eight and a quarter hours after the one-half run
returned, with their downloads falling between eight and two-thirds and nine and three-quarter
hours after — fetched the Dirichlet-L and record-proportion papers listed in the table, chiefly
to audit where GRH enters Chandee–Lee–Liu–Radziwiłł and what the unconditional support
range of Hughes–Rudnick is; the outcome was a hedged remark and one line of records in the
draft’s section on variants.

The optimal window (the sibling). The optimal-window sibling’s brief, written five
minutes before theR two-thirds   run’s, carried from the coordinator’s memory Montgomery’s
functional c(w)  = (    2 /( w 2 +          w(a)w(b)), the Euler–Lagrange equation w′′ +2w = 0
                            R      RR
              √      w)               |a−b|
with the cos 2 ansatz, the sentence “Montgomery–Taylor (1974?) improved 2/3-simple to
0.6725 via optimized kernel”, and the pointer to Carneiro–Chandee–Littmann–Milinovich’s
Crelle paper with the instruction “(recall precisely; fetch arXiv 1406.5462 if network works)”.
That arXiv number occurs nowhere earlier in any log of the campaign: it was typed from
memory, correctly. (The number 0.6725 itself had first been written by the coordinator,
from memory and with a question mark, in the literature agent’s brief about two and three-
quarter hours after the run returned; the literature agent’s report later confirmed it from
arXiv 2501.14545.) The sibling read its inputs — including the literature agent’s findings
file, which lists “Montgomery–Taylor: .6725; Cheer–Goldston .672753; Chirre–Gonçalves–
de Laat: .679” as names and numbers only — and then solved the variational problem


                                                87
itself:√its solver,√written nineteen
                               √     minutes
                                           √ after its launch, already
                                                                     √ contains the closed form
cλ = 2 tan(λ/ 2)/(1 + (λ/ 2) tan(λ/ 2)) with optimiser cos( 2λs); four minutes later it
  ∗

printed c∗ = 0.7532961, 2c∗ − 1 = 0.50659, and three minutes after that its report identified
2 − 1/c∗ = 0.6725007 as “exactly the Montgomery–Taylor constant”. Only then, thirty-one
minutes after its launch (about eight hours after the one-half run returned), did it make its
first network request: one arXiv API call for 1406.5462 and 1810.08843 — the second number,
Chirre–Gonçalves–de Laat’s semidefinite-programming paper, supplied from its own memory —
followed by both e-prints. From the Carneiro–Chandee–Littmann–Milinovich source it read
Corollary 15 and the remark giving N ∗ (T ) ≤ (2−1/2 cot 2−1/2 + 12 + o(1))N (T ), checked that
this equals its 1/c∗ , and recorded that their extremal kernel lies inside its admissible class, so
that the restriction k̂ ≥ 0 costs nothing; from Chirre–Gonçalves–de Laat it took only the bound
1.3208, to estimate what signed weights could buy, and classified that as beyond the method.
The downloads thus verified an identification already made and supplied the optimality remark
and the cotangent closed form that later appear in the draft’s Theorem D; none of it bears
on the two-thirds argument, and none of it reached the two-thirds run, whose one look at the
sibling’s report took in only its first six thousand bytes, ending inside the statement of the
extremal problem and before the literature section the sibling appended later.

The interruption. Three and a quarter hours after its launch, immediately after the lemma
and its proof had been written to its report, the two-thirds run was cut off by an infrastructure
error; the coordinator, having read the partial report and checked the proof line by line,
resumed it seven minutes later with the message reproduced in Part II, §5, which is where the
consequence (2 − 1/λ − λ/3)N → 32 N was first written out. Nothing was fetched or read from
outside the campaign in between. The two referees of the lemma that followed worked without
network access.

A.6    What reached the paper draft from downloaded sources
All of it is positioning or bibliography, apart from the one formulation already described, and
all of it entered through the paper-writing agent and the cold referee rather than through either
run: the bibliography’s journal data, mined from the reference lists inside the downloaded
e-prints and completed by five bibliographic web searches the paper-writing agent made about
eleven hours after the one-half run returned (journal data for Wu, Bui–Conrey–Young, Feng
and Farmer, Montgomery–Vaughan’s 1974 Hilbert-inequality paper, Yoshida 1992); the records
paragraph of the introduction, including Wu’s 66.04% distinct and Farmer’s bound; the remark
relating tr G2 at λ = 1 to “Aryan’s lemma” as it appears in Goldston–Suriajaya’s narrow-
box paper and to Theorem 1 of Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, and the
courtesy that the prime-side input is used “in the form given to it” in those papers; the
related-work subsections on the work of Goldston and his coauthors and on Goldston–Lee–
Schettler–Suriajaya; Bombieri’s 2000 negative-index observation cited as prior art; Theorem D’s
optimality sentence; two of the cold referee’s fourteen corrections that were sourced from
downloaded text (quote Goldston–Suriajaya’s Theorem 2 exactly; attribute 5/6 to Montgomery
plus integrality); and, when the main theorem became two thirds, the framing sentence about
Montgomery’s constant and Goldston–Suriajaya’s open problem. On the whole chain from the
brief of Part I to the two-thirds revision of the draft, no downloaded paper supplied a lemma,
an inequality, a constant or a proof step: not the inertia identity, the double count, the Cauchy–
Schwarz count, the coefficient-coordinate repair, the Poisson identity, the Montgomery–Vaughan
reduction, the variational c∗ , the rank–trace lemma or its bookkeeping. What the model knew
from training — evidently including Weil’s criterion, Pontryagin–Kreı̆n theory, Montgomery’s,
Montgomery–Vaughan’s and Montgomery–Taylor’s results, the Carneiro–Chandee–Littmann–
Milinovich paper down to its arXiv number, and the existence of the 2023/24 unconditional


                                                88
pair-correlation paper — is outside what logs can trace.

A.7       The works, in one table
The table lists every work that was downloaded or opened by an agent on the chain of Parts I
and II and its write-up (the three blind referees and referee D; the literature, re-derivation and
paper-writing agents; the two-thirds run, its optimal-window and higher-moments siblings and
the two referees of its lemma; the generalisations agent with its two literature sub-agents; the
cold referee), together with the principal works that were recalled and used but never fetched.
“When” is in hours after the one-half run returned; the two-thirds run was launched at +7.6 h.
Roles: recalled only; recalled, then verified at source; verification (used to check a claim already
made in the campaign); positioning (related work, records, bibliography); formulation (wording
of a statement entered); frame (named the target as an open problem); dead end.

authors           short title                  arXiv /      fetched by; when        role
                                               venue
Recalled and used, never fetched on this chain
Weil (1952);       explicit formula and        —           recalled by the          recalled only — the
Pontryagin         positivity criterion;                   coordinator in the       frame of Part I
(1944),            operators on Πκ spaces                  one-half run’s brief;
Kreı̆n–Langer                                              the terms occur in
                                                           essentially no earlier
                                                           record, and in no
                                                           download
Yoshida (1992);   Weil positivity on small     —           recalled by the          recalled only —
Burnol            support; Sonine spaces                   coordinator              frame pointers
                                                           (“Yoshida?               (Bombieri below)
                                                           Bombieri?”) and by
                                                           the run (“from
                                                           memory and
                                                           unverified offline”);
                                                           Yoshida’s journal
                                                           data searched by the
                                                           paper-writing agent
                                                           (+11 h)
Turán; Nazarov    zeros and sign changes of    —           recalled by the          recalled only
                  exponential sums                         coordinator              (proposed tool;
                                                                                    shown to bound the
                                                                                    wrong operator)
Montgomery        The pair correlation of      Proc.      recalled by the run       recalled only
(1973)            zeros of the zeta function   Symp. Pure on recognising 34 ; by
                                               Math. 24   the coordinator (≥ 32
                                                          simple under RH,
                                                          +6 min; the integer
                                                          template in the
                                                          two-thirds brief,
                                                          +7.6 h)
Montgomery–       Hilbert’s inequality         J. London  recalled by the run;   recalled only (the
Vaughan (1974)                                 Math. Soc. reduction re-derived analytic input)
                                                          by referee B (2 41 h,
                                                          before its first
                                                          search) and by the
                                                          re-derivation agent
                                                          (no network); journal
                                                          data searched by the
                                                          paper-writing agent
                                                          (+11 h)


                                                     89
authors             short title                  arXiv /        fetched by; when         role
                                                 venue
Gallagher–          pair correlation and simple —               recalled by the run      recalled only
Mueller             zeros                                       among “the closest”
                                                                works; by the
                                                                coordinator in the
                                                                higher-moments brief
Montgomery–         the 0.6725 / 1.3275           —             recalled by the          recalled, then
Taylor (in          simple-zero constant;                       coordinator (0.6725      verified at source
Montgomery          optimised kernels                           with a “?” and
1975);                                                          Cheer–Goldston at
Cheer–Goldston                                                  2 43 h;
(1993)                                                          Montgomery–Taylor
                                                                at 7 12 h); confirmed
                                                                in arXiv 2501.14545
                                                                and 1406.5462
Rudnick–Sarnak      restricted-support n-level    —             recalled (the            recalled only
(1996); Ky Fan,     correlations; eigenvalue                    two-thirds brief; von
Weyl, Cauchy        inequalities                                Neumann by the
interlacing; von                                                two-thirds run itself)
Neumann’s trace
inequality;
Markov–Kreı̆n
Selberg,           proportion-on-the-line         —            recalled by the          recalled; positioning
Levinson,          theorems and records                        coordinator
Conrey; Bui–       (5/12; “0.407 simple”)                      (benchmark, from
Conrey–Young;                                                  the campaign’s first
Feng;                                                          hour) and by the run
Pratt–Robles–                                                  (“for comparison . . .
Zaharescu–                                                     from memory”);
Zeindler                                                       exact figures later
                                                               checked by the
                                                               paper-writing agent’s
                                                               searches (+11 h) and
                                                               the records sub-agent
                                                               (arXiv 1802.10521,
                                                               +8 43 h)
Downloaded after the one-half run returned: the referees, the literature agent, the paper-writing agent
Baluyot–           An unconditional             2306.04799 named from                   recalled, then
Goldston–          Montgomery theorem for                      memory by the           verified at source
Suriajaya–         pair correlation of zeros of                run (four author        (the run’s
Turnage-           the Riemann zeta function                   names, no title or       asymptotic =
Butterbaugh                                                    number); referees C, Theorem 1);
(2024)                                                         A (1 31 h), referee B    positioning (records
                                                               (2 12 h), literature     paragraph)
                                                               agent e-print (2 65 h)
Baluyot–           Pair correlation of zeros of 2501.14545 referee A abstract           verification;
Goldston–          the Riemann zeta function                   (1 13 h), referee B      positioning (the
Suriajaya–         I: proportions of simple                    abstract (2 12 h),       literature agent
Turnage-           zeros and critical zeros                    literature agent         confirmed the
Butterbaugh                                                    e-print (2 65 h), cold   recalled .6725 from
(2025)                                                         referee (10 h)           its Theorem 2)
Goldston–Lee–      Pair correlation conjecture 2503.15449 referee A abstract            formulation
Schettler–         for the zeros of the                        (1 12 h), literature    (“simple and on the
Suriajaya (2025) Riemann zeta-function I:                      agent e-print (2 65 h;   line”, one-half
                   simple and critical zeros                   horizontal               theorem);
                                                               multiplicity read 3 h), positioning (“PCC
                                                               higher-moments           ⇒ 100%”)
                                                               sibling search (10 h)


                                                        90
authors            short title                  arXiv /      fetched by; when         role
                                                venue
Goldston–          Zeta zeros on the critical   2511.20059   literature agent         frame (removing
Suriajaya (2025)   line                                      e-print (3 h);           RH from
                                                             paper-writing agent      Montgomery’s proof
                                                             read that copy (6 h);    stated as open);
                                                             records sub-agent        formulation;
                                                             (8 56 h); cold referee   positioning
                                                             (10 h)
Goldston–          Zeta zeros in a narrow       2603.28104   literature agent         frame (with the
Suriajaya (2026)   vertical box                              e-print (3 21 h)         above); verifica-
                                                                                      tion/positioning
                                                                                      (“Aryan’s lemma”
                                                                                      = the run’s tr R2 at
                                                                                      λ = 1)
Bombieri (2000)    Remarks on Weil’s            Rend.        literature agent         recalled with a “?”
                   quadratic functional         Lincei       (3 34 h); cold referee   in the one-half brief,
                                                (EuDML)      search hit               then verified at
                                                                                      source; positioning
                                                                                      (prior art for the
                                                                                      negative-index half
                                                                                      of Theorem 1)
Farmer (1995)      Counting distinct zeros of Electron. J. search hits for            positioning
                   the Riemann zeta-function Combin. 2 referees C, A (1 12 h);
                                                           literature agent
                                                           (3 12 h; title recalled
                                                           in its brief);
                                                           paper-writing agent
                                                           front matter (6 h)
Wu (2015)          Distinct zeros of the      Quart. J.    literature agent        positioning (66.04%
                   Riemann zeta-function      Math. 66     (3 21 h)                distinct; the 0.66 of
                                              (abstract)                           the draft’s
                                                                                   introduction)
Bui–Heath-        On simple zeros of the       1302.5018   literature agent        positioning (19/27
Brown (2013)      Riemann zeta-function        (abstract)  (3 23 h)                already recalled in
                                                                                   referee B’s brief)
Conrey–Ghosh– Simple zeros of the              Proc. LMS literature agent          positioning (≥ 5/6
Gonek (1998)      Riemann zeta-function        (author’s   (3 23 h); paper-writing distinct by
                                               copy)       agent p. 1 (6 h)        integrality under
                                                                                   RH sat in the
                                                                                   findings file; see
                                                                                   text)
Suzuki (2022;     Aspects of the screw         2206.03682; literature agent        dead end here
2026)             function corresponding to 2606.09096 (3 34 h)                    (prior-art search for
                  the Riemann zeta function;                                       a link between
                 Weil’s quadratic form via                                         signature and
                  the screw function                                               off-line zeros found
                                                                                   nothing); used on
                                                                                   the Weil-positivity
                                                                                   branch
Downloaded by the optimal-window sibling
Carneiro–         Hilbert spaces and the       1406.5462   sibling (8 h; arXiv     recalled, then
Chandee–          pair correlation of zeros of             number recalled by      verified at source
Littmann–         the Riemann zeta-function                the coordinator in its (Cor. 15 optimality;
Milinovich                                                 brief at 7 12 h)        remark and closed
(2017)                                                                             form in Theorem D)
Chirre–           Pair correlation estimates 1810.08843 sibling (8 h; number positioning; dead
Gonçalves–de      for the zeros of the zeta                recalled by the         end (bounds the
Laat (2020)       function via semidefinite                sibling)                signed-weight
                  programming                                                      frontier; not in the
                                                                                   draft)


                                                      91
authors            short title                  arXiv /       fetched by; when       role
                                                venue
Downloaded by the generalisations agent and its two literature sub-agents (8 23 to 9 34 h), and by the
cold referee
Chandee–Lee–      Simple zeros of primitive    1211.6725    literature sub-agent; verification (where
Liu–Radziwiłł     Dirichlet L-functions and                 generalisations agent GRH enters) →
(2014)            the asymptotic large sieve                                           hedged remark only
Hughes–Rudnick Linear statistics of            math/        literature sub-agent verification
(2003)            low-lying zeros of           0208230                                (unconditional
                  L-functions                                                          support range;
                                                                                       recalled in the
                                                                                       two-thirds brief)
Drappeau–         One-level density with       2002.11968; literature sub-agent positioning
Pratt–Radziwiłł extended support; n-level 1706.02848
(2020);           density for Dirichlet
Chandee–Lee       L-functions
(2017)
Wu (2019)         The twisted mean square 1802.09704 records sub-agent;                positioning (the
                  and critical zeros of                     generalisations agent Dirichlet records
                  Dirichlet L-functions                                                line)
Pratt–Robles–     More than five-twelfths of 1802.10521 records sub-agent              positioning (record
Zaharescu–        the zeros of ζ are on the                                            recalled from the
Zeindler (2020)   critical line                                                        start)
Conrey–Iwaniec– Critical zeros of Dirichlet 1105.1177; literature sub-agent; positioning
Soundararajan     L-functions; Asymptotic      1105.1176    generalisations agent
(2011)            large sieve
Sono (2021)       Zeros of Dirichlet           2105.07422 both sub-agents;             positioning
                  L-functions on the critical               generalisations agent
                  line
Andersen–         Zeros of GL2 L-functions 2004.03581; records sub-agent;              positioning (mostly
Thorner (2020); on the critical line; Simple 2109.15311; generalisations agent not in the draft)
de Faveri (2021); zeros of GL(2) L-functions; 2501.00551
Rezvyakova        linear combinations of
(2025)            degree-two L-functions
Conrey–Farmer– Short mollifiers of the         2508.11108 records sub-agent            positioning
Kwan–Lin–         Riemann zeta-function
Turnage-
Butterbaugh
(2025)
—                 Pair correlation of zeros of 2411.19762; literature sub-agent; dead end
                  Dirichlet L-functions: a     2511.06109 generalisations agent
                  possible path towards the
                  conjectures of Chowla,
                  Elliott–Halberstam and
                  Montgomery; Levinson’s
                  theorem and its
                  generalization for Dirichlet
                  L-functions
Özlük (1996)      On the q-analogue of the     J. Number literature sub-agent positioning
                  pair correlation conjecture Theory
                                               (abstract
                                               pages)
Odlyzko           table of the first 105 zeros author’s     cold referee (9 h)         verification data
                                               page                                   (entrywise check of
                                                                                       the prime-side
                                                                                       matrix)


                                                       92
A.8    Other branches of the campaign
The same three days saw several other lines of work, run by other agents from other briefs,
and for two of them the relation to the literature was the opposite of the one just described.

Weil positivity. The branch that ended in a computer-assisted certification of Weil positivity
for test functions of larger support began from a frame recalled by the coordinator — Connes
and Consani’s 2021 theorem for support in [2−1/2 , 21/2 ], stated from memory in the very first
brief of the campaign and again in the brief that asked an agent to “draw” the positivity
margin as a function of the support. That agent searched for Yoshida’s 1992 paper, downloaded
three of Suzuki’s screw-function papers (arXiv 2209.04658, 2206.03682, 2606.09096) and a
July-2026 numerical study of Suzuki’s operator (arXiv 2607.24830), and fetched the abstract of
Connes–Consani’s Weil positivity and trace formula, the archimedean place (arXiv 2006.13771),
about nine and a half hours after the one-half run returned, before its own computation, and
used them as positioning: it extended the published numerics by many orders of magnitude and
found the exponential law of the margin empirically. The agent then asked to explain that law,
about sixteen hours after the one-half run returned, was given two arXiv numbers from that
report and a third the coordinator recalled (Connes–Consani–Moscovici, Zeta zeros and prolate
wave operators, arXiv 2310.18423), downloaded some twenty papers of Connes and Consani,
read Spectral triples and zeta-cycles (arXiv 2106.01715) and Connes–Consani–Moscovici’s Zeta
spectral triples (arXiv 2511.22755), and wrote in its report that the source of the idea was
there: the extremely small eigenvalues are explained in those papers by prolate vectors, and
the earlier agent had “rediscovered the curve numerically without this identification”. The
certifying agent, about six hours later, read the downloaded text of the 2021 paper for the exact
published statement and normalisation it certified against, and fetched Bombieri 2000 and
looked up Yoshida 1992 (which it could not obtain) for a priority caveat. On this branch, then,
the mechanism was supplied by downloaded papers, and the agents say so; the certification
scheme itself was the coordinator’s brief plus the certifying agent’s own design. The branch
shares no files or messages with the chain of Parts I and II beyond the Bombieri/Yoshida
remark both cite.

Zero-density estimates. This branch was literature-driven by construction. Its brief, on
the first day, named the genre from memory — Guth and Maynard’s New large value estimates
for Dirichlet polynomials (arXiv 2405.20552, number recalled correctly) and the Tao–Trudgian–
Yang database of exponents — and the agent’s first acts were to download that paper and
Tao–Trudgian–Yang’s New exponent pairs, zero density estimates, and zero additive energy
estimates: a systematic approach (arXiv 2501.16779), to clone the public repository of the
associated exponent database, and to transcribe from them the pool of published ingredients
and the table to be beaten; it later fetched Kerr’s 2019 preprint (arXiv 1909.12075) to check that
its candidate improvement was not already known. What it found — a published large-values
lemma present in the database’s blueprint but not loaded by its optimiser, whose inclusion
repairs three jump discontinuities of the table — is a recombination of published lemmas it
names; its two referees re-derived the comparison from the Tao–Trudgian–Yang source table,
Gafni–Tao (arXiv 2505.24017) and a 2026 survey (arXiv 2607.04632), and one of them fetched
an Ivić lecture. Provenance of every ingredient is the literature, by design; the finding is the
ablation.

Everything else. Fifty-four further arXiv papers and a comparable number of journal,
database and lecture-note pages were fetched by agents on branches that led nowhere near
the results above: zero-free regions and decoupling (the campaign’s first hours), Eisenstein
zero-curves and Epstein zeta functions, a multivariate-stability lift, Beurling generalized primes,


                                                93
a rate law for zeros of linear combinations of L-functions (one literature sub-agent alone made
sixty requests), periods and theta lifts, and, after everything else was finished, a workflow on
zero-density estimates near the critical line that re-downloaded three of the pair-correlation
papers among a dozen others. The logs settle their relation to Parts I and II mechanically: the
set of directories from which any agent on that chain ever read a file contains none written
by these agents, the coordinator read none of their files, and nothing from their short reports
to the coordinator appears in any brief on the chain. One of them deserves a footnote: the
literature sub-agent of the rate-law branch had the text of Goldston–Lee–Schettler–Suriajaya
and Goldston–Suriajaya on disk during the very hours in which the one-half run was deriving its
dual argument — the only place in the campaign where that text then existed — in temporary
files that no other agent ever opened and in a report that went only to its own parent.

  branch            principal works fetched (arXiv)                      role
  Weil positivity   Connes–Consani 2006.13771, 2106.01715;             frame recalled (the 2021 theorem);
                    Connes–Consani–Moscovici 2310.18423 (recalled,     mechanism of the margin law
                    then fetched), 2511.22755; Suzuki 2206.03682,      supplied by 2106.01715 /
                    2209.04658, 2606.09096; numerics 2607.24830;       2511.22755, declared by the agent;
                    Yoshida 1992 (journal page); Bombieri 2000         published statement used as the
                    (EuDML); some fifteen further Connes–Consani       certification target; priority caveat
                    papers downloaded and set aside
  zero density      Guth–Maynard 2405.20552 (recalled, then fetched); inputs by design (ingredient pool
                    Tao–Trudgian–Yang 2501.16779; the public           and baseline table); verification by
                    exponent-database repository and blueprint; Kerr the referees
                    1909.12075; Gafni–Tao 2505.24017; survey
                    2607.04632; an Ivić lecture
  all other         54 papers: e.g. Ford 1910.08205/1910.08209 and a no read path into Parts I–II; not
  branches          Bourbaki exposé 1707.00119 (zero-free regions);    discussed further
                    2112.10561, 2110.09368 (Epstein zeros); 0704.3448
                    (finite Euler products); 2309.01567, 2409.10051,
                    math/0410270 (Beurling primes); two dozen papers
                    on zeros of linear combinations and derivatives of
                    L-functions; 2605.22475 (Eisenstein series);
                    1805.07741, 1910.08274 and others (near-line
                    density, last)


                                                      94
