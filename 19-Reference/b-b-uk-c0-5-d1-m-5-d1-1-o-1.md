---
title: "B ·B ≤ ·# UK (C0 ) ≤ ·5 d−1 m = 5 d−1 (1+o(1))."
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/6c28f488d07644c212e352014108c8ed23cc7f76.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:48Z"
tags: ["news-research"]
---

A from–scratch solver, run with no hints and no access to prior
      work on the problem (audited in full), was asked to resolve the Erdős–
      Szemerédi sum–product conjecture. It found the following construc-
      tion, ran its own adversarial verification, assembled a chain of clas-
      sical inputs that would make the construction unconditional, marked
      that chain [unverified], and then declined to assert the result on the
      grounds that the conclusion “contradict[s] the expert consensus” and is
      “far more likely to indicate an undetected error than to be true”. This
      document records the chain in the form of estimates (A)–(F) (§1), the
      solver’s own verification (§2), and its stated reason for not asserting
      the result, verbatim (§3).


1     The chain.
1.1   Setup.
Let K be a totally real number field of degree d with ring of integers oK ,
discriminant ∆K , regulator RegK , and root discriminant |∆K |1/d =: r ≤ r0 .
Fix one real embedding K ,→ R; distinct elements of K give distinct reals.
For C ≥ 1 set

      UK (C) := u ∈ o×                −1
               
                      K : |σ(u)| ∈ [C    , C] for every archimedean σ ;

write m := #|UK (C0 )|. Fix constants C0 ≥ 2, K0 ≥ 103 , R := K0 C02 r.
Choose x1 , . . . , xs ∈ oK \ {0} of house ≤ R/C0 , pairwise inequivalent under
multiplication by UK (C02 ), and set
                     [
           B :=         UK (C0 ) · xj ⊂ oK ⊂ R,    n := #|B| = ms.
                 j≤s

The orbits are disjoint and each has exactly m elements.


                                        1
1.2    The hypothesis.
Hypothesis 1.1 (U′ ). There exist absolute constants C0 ≥ 2, ε > 0, r0 ≥ 1,
and totally real K of arbitrarily large degree d with |∆K |1/d ≤ r0 , such that
                              #|UK (C0 )| ≥ (5 + ε)d .
Equivalently, by Dirichlet’s unit theorem and van der Corput on the log–unit
lattice, (U′ ) asserts the existence of totally real fields of unbounded degree
with bounded root discriminant and RegK ≤ Or0 (1)d . Zimmert’s bound
RegK ≥ 0.04 e0.46d [known] shows regulators grow at least exponentially
but does not contradict (U′ ) for large C0 .

1.3    The estimates.
The solver established the following (its tags [sketch] and [known] re-
tained).
 (A) #|{x ∈ oK : house(x) ≤ M }| ≤ (2M + 1)d (distinct algebraic integers
     are 1–separated in ℓ∞ ). [sketch; verified]
 (B) #|{x ∈ oK : house(x) ≤ M }| ≥ M d /rd/2 once M ≫r0 1.                    [known;
     van der Corput]
 (C) #|UK (C 2 )| ≤ 5d−1 #|UK (C)|.            [sketch; lattice covering]
 (D) s ≥ (R/C0 )d /(5d−1 m rd/2 ) (greedy orbit selection). [sketch]
 (E) #|B · B| ≤ #|UK (C02 )| · s+1    ≤ 5d−1 ms2 . [sketch; verified]
                                    
                                 2

 (F) #|B + B| ≤ (4R + 1)d (every element has house ≤ 2R).                    [sketch;
     verified]
And, independently of (A)–(F), the chain for Hypothesis 1.1 itself:
(C′ ) Totally real towers of bounded root discriminant exist (Martinet/Golod–
      Shafarevich). [known]
(C′′ ) Along any such tower, RegK ≤ Or0 (1)d : the class number formula
       hK RegK = 21−d |∆K |1/2 Ress=1 ζK , the bound hK ≥ 1, and an un-
       conditional Rademacher/Louboutin–type bound Ress=1 ζK ≤ Or0 (1)d .
       [unverified chain]1
(C′′′ ) #|UK (C0 )| ≥ (log C0 )d−1 · Or0 (1)−d / RegK (van der Corput on the
        log–unit lattice), so (C′′ ) ⇒ (U′ ) with C0 = Or0 (1).
   1
    The label [unverified chain] is the solver’s own marking for this argument, not ours;
see §2.


                                           2
1.4    The tally.
Assuming (A)–(F) and (U′ ): n = ms ≥ (R/C0 )d /(5d−1 rd/2 ) by (D), so

#|B + B|  (4R + 1) · 25C02 r d  100 d            #|B · B|   5d−1  5 d
        ≤                       ≈        ,                    ≤     ≤      ,
   n2            R2                K0                  n2        m    5+ε

and since n ≤ (2R + 1)d both are ≤ n−ş with
                                                    
                      min log(K0 /100), log(1 + ε/5)
                 ş =                                 > 0.
                            log(2K0 C02 r0 + 1)

Thus (U′ ) + (A)–(F) ⇒ (NEG); and (C′ ) + (C′′ ) + (C′′′ ) ⇒ (U′ ). The
discriminant does not improve the container bound (F); it enters only the
lower bound (B) for n, which is why bounded root discriminant must be
hypothesized.


2     The solver’s verification.
The solver commissioned an independent adversarial re–derivation (attacking
each lemma, re–deriving the bookkeeping, and checking consistency with the
literature). Findings, in its words:
     Two genuine defects, both repairable. (i) The originally proposed constant
R = 100C02 r makes (F) fail to beat n2 for large d; K0 ≥ 103 repairs it.
(ii) Bounded root discriminant is not automatic from the presence of many
small units; it must be part of the hypothesis, as in (U′ ).
     No refutation of the repaired implication. After the two repairs, the con-
tainer count (A), covering constant (C), greedy selection (D), distinctness,
and the bookkeeping of §1.4 all survived independent re–derivation. Con-
sistency checks: no known theorem (Chang’s bounded–degree sum–product,
Evertse–Schlickewei–Schmidt unit–equation counting — whose bounds are
exponential in the rank and hence vacuous at rank ≍ log n —, divisor bounds,
Zimmert/Friedman regulator lower bounds) contradicts the construction.
     The destabilizing finding. The verifier’s own words:

      So the construction does not contradict any known theorem in additive
      combinatorics — but the *package* contradicts itself: if Steps 1–2 are
      right, then together with (e) it yields sets with max(|B + B|, |B · B|) ≤
      n2−δ , δ ≈ 2×10−5 , i.e. an unconditional disproof of ES. That con-
      clusion is extraordinary; the overwhelmingly likely resolution is that
      there is an error either in Steps 1–2 (which I could not find beyond
      the repairable items above) or in the author’s/ my assessment of the


                                         3
      analytic input. The author’s stated reason for openness ("loss of a log
      per character", i.e. ρK ≤ (c log dK )d−1 = eO(d log d) ) ignores that the
      conductors multiply to dK (AM–GM in the abelian case) and that the
                                                 d
      convexity bound achieves the same logddK shape in general; this is
      the single point on which "safely conditional" versus "unconditional
      and unbelievable" turns, and it must be checked against the liter-
      ature (Louboutin, *J. Number Theory/Canad. J. Math.* 2000–01;
      Rademacher 1959) before the claim is circulated.

      (ii) Hypothesis (U): NOT OPEN as claimed; modulo a liter-
      ature check it is KNOWN TRUE — and that is fatal for the
      narrative, not a victory. For C0 ≤ 2 it is known false (Kronecker);
      for large absolute C0 , the form actually needed (with bounded root
      discriminant) follows from Martinet’s totally real towers + the class
      number formula + h ≥ 1 + the classical residue/convexity bound +
      the author’s own Lemma 1. Consequently the document, as corrected
      by its own tools, is not a conditional reduction but an implicit un-
      conditional disproof of Erdős–Szemerédi. Given the strong consensus
      that ES is true, the rational conclusion is that the route contains an
      as-yet-unlocated error — the prime suspects being either a subtle flaw
      in Steps 1–2 that has survived both the author’s and my scrutiny, or a
      misassessment (mine or the author’s) of the residue bound. Until this
      tension is resolved, the claimed theorem should not be accepted.


3    Why the solver does not assert the result.
Verbatim from the solver’s final output (§2.4):

      Given the strength of the consensus for the conjecture and the fact
      that the construction uses only elementary counting on top of clas-
      sical inputs, the overwhelmingly likely explanation is an error that
      neither pass located — the prime suspects being (a) a subtle flaw in
      the combinatorial steps of §2.2 (e.g. in the interaction between the
      greedy selection and the two container bounds), (b) a misquotation
      or misapplication of the residue bound or of the existence of totally
      real towers of bounded root discriminant, or (c) an incompatibility be-
      tween the parameter regimes of the cited results that disappears only
      when all constants are written out in full. Deciding which requires
      a level of expert scrutiny (and ideally a numerical experiment on a
      moderate–degree field with small regulator) that is beyond what this
      investigation can certify.

    And its recommended next step (§5):


                                         4
      the first task is to verify the exact statement and applicability of the
      Rademacher/Louboutin residue bound and of Martinet–type totally
      real towers; the second is a full constant–tracked write–up refereed by
      a number theorist; the third is a numerical study of unit counts and of
      |B + B|, |B · B| in moderate–degree fields of small regulator.


4     The solver’s arguments for each estimate.
We collect here, estimate by estimate, the arguments that the solver itself
produced; the standing setup is that of §1.1. The labels (A)–(F) and (C′ )–
(C′′′ ) are this writeup’s reorganization of what the solver called Lemmas 1–4
and surrounding prose; the arguments, and the tag [unverified chain] on
(C′′ ), are the solver’s own.

4.1   (A) The additive container: upper bound.
                # {x ∈ oK : house(x) ≤ M } ≤ (2M + 1)d .
Take distinct x, y ∈ oK . Then x − y ̸= 0, so its norm is a nonzero rational
integer, and       Y
                      x(i) − y (i) = NK/Q (x − y) ≥ 1,
                     i

which forces maxi |x(i) − y (i) | ≥ 1. Thus the Minkowski images of distinct
integers are 1–separated in ℓ∞ , and the box [−M, M ]d can contain at most
(2M + 1)d of them. The solver stresses the asymmetry: the discriminant
does not enter this upper bound; it enters the true count downward.

4.2   (B) The additive container: lower bound.
         # {x ∈ oK : house(x) ≤ M } ≥ M d /rd/2              (M ≫r0 1).
Here the solver records only the invocation: writing

                   P := # {x ∈ oK : house(x) ≤ R/C0 } ,

van der Corput on the lattice oK (covolume rd/2 ) gives

                           P ≥ (R/C0 )d rd/2 .
                                         


No further argument is supplied.


                                         5
4.3   (C) Lattice doubling of UK .
                       # UK (C 2 ) ≤ 5 d−1 # UK (C) .
The solver states the general fact first: for a lattice Λ and a symmetric
convex body Q in a k–dimensional real vector space,

                         # Λ ∩ 2Q ≤ 5k # Λ ∩ Q .

To see this, pick a maximal set {zi } ⊆ Λ ∩ 2Q whose pairwise differences
avoid int Q. The bodies zi + 21 Q are then pairwise disjoint and all lie inside
5                                                       k
2 Q, so a volume comparison bounds their number by 5 . Maximality forces
every v ∈ Λ ∩ 2Q to satisfy v − zi ∈ Λ ∩ Q for some i, i.e.
                                    [               
                      Λ ∩ 2Q ⊆          zi + (Λ ∩ Q) ,
                                      i

which gives the count. Applying this with k = d − 1 (the log–unit lattice
inside the trace–zero hyperplane), QC02 = 2QC0 , and noting that the torsion
±1 appears identically on both sides, one obtains

                      # UK (C02 ) ≤ 5 d−1 # UK (C0 ) .

4.4   (D) Greedy orbit selection.
                                      (R/C0 )d
                              s ≥                 .
                                    5 d−1 m rd/2
The solver’s procedure is greedy: choose x1 , . . . , xs ∈ oK of house ≤ R/C0
with the property that xi /xj ∈/ UK (C02 ) for i ̸= j. By (B) there are at least
        d
(R/C0 ) /r d/2 integers of house ≤ R/C0 to draw from, and each chosen xi
rules out at most #|UK (C02 )| further candidates; with (C) this yields

                                      (R/C0 )d
                             s ≥                   .
                                    rd/2 · 5 d−1 m
For distinctness of B := j≤s UK (C0 ) xj : if uxi = u′ xj with u, u′ ∈ UK (C0 ),
                        S
then
            xi /xj = u′ /u ∈ UK (C0 ) · UK (C0 )−1 ⊆ UK (C02 ),
which the selection excludes unless i = j, and then u = u′ . Hence the orbits
are disjoint and #|B| = ms exactly.


                                          6
4.5    (E) Product set bound.
                                                           
                                                      s+1
              # B · B ≤ # UK (C02 ) ·                           ≤ 5 d−1 m s2 .
                                                       2
From UK (C0 ) · UK (C0 ) ⊆ UK (C02 ) we get
                                    [
                         B·B ⊆         UK (C02 ) · xi xj ,
                                     i≤j

                                    s+1
                                              unit–orbits of size #|UK (C02 )|, whence
                                          
so the product set is covered by     2

                                                             n2
                                       
                 s+1           2      s+1
# B ·B ≤               ·# UK (C0 ) ≤        ·5 d−1 m = 5 d−1    (1+o(1)).
                  2                    2                     m

4.6    (F) Sum set bound.
                            # B + B ≤ (4R + 1)d .
Each element of B has house ≤ C0 · (R/C0 ) = R, so every element of B + B
has house ≤ 2R; applying (A) with M = 2R gives the display.
    The solver then reworks the bookkeeping and flags a repair. With the
originally proposed R = 100 C02 r, combining (D) with n = ms gives
                      √                                               √       d
          n ≥ 5 (20 C0 r)d ,         #|B + B| ≤                 (20 C0 r)2 + 1 ,

so that                                                           d
                         #|B + B|                 1 + 4001C 2 r
                                                            0
                                  ≤                                    ,
                            n2                         25
which is never a power saving and in fact exceeds 1 once d ≫ C02 r. The
remedy is to take R = K C02 r with K ≥ 103 ; then

                         #|B + B| ≤ n2 · (O(1)/K)d ,

a genuine power saving as long as r ≤ r0 stays bounded.

4.7    (C′ ), (C′′ ), (C′′′ ): the chain for Hypothesis (U′ ).

(C′ ) Totally real towers of bounded root discriminant exist.
    The solver invokes Martinet’s infinite totally real class–field tower (Golod–
Shafarevich), whose root discriminant is an absolute r0 = O(1); the recorded
value is r0 ≈ 913.


                                              7
(C′′ ) Along any such tower, RegK ≤ Or0 (1)d . [unverified chain]
   The chain runs

             RegK ≤ hK RegK = 21−d |∆K |1/2 Ress=1 ζK (s),

using hK ≥ 1 together with the unconditional convexity bound (Rademacher;
in the explicit form attributed to Louboutin)
                                   e log |∆ | d−1
                                            K
               Ress=1 ζK (s) ≤                      ≤ Or0 (1)d
                                     2(d − 1)

valid whenever |∆K |1/d ≤ r0 . Putting these together,
                                   d/2
                  RegK ≤ 21−d r0         · Or0 (1)d = Or0 (1)d .

At r0 ≈ 913 the solver’s numerical instantiation reads RegK ≤ e6d . This is
the step the solver itself tagged [unverified chain].
(C′′′ ) #|UK (C0 )| ≥ (log C0 )d−1 · Or0 (1)−d / RegK , so (C′′ ) ⇒ (U′
                                                                     √ ).
    Van der Corput applied to the log–unit lattice (covolume d · RegK in
the trace–zero hyperplane) gives

                                             c (log C0 )d−1
                        # UK (C0 ) ≥           √            .
                                                 d RegK

Feeding in (C′′ ) turns this into #|UK (C0 )| ≥ Or0 (1)−d (log C0 )d−1 ; choosing
C0 = Or0 (1) large enough (with log C0 ≈ 2000 at r0 ≈ 913) then forces

                           # UK (C0 ) ≥ (5 + ε)d

for an absolute ε > 0, which is Hypothesis (U′ ).

Remark 4.1. Per the solver’s own tags reproduced in §1.3: (A), (E), (F)
are marked [sketch; verified]; (C), (D) are marked [sketch]; (B) and
(C′ ) are marked [known]; (C′′ ) is marked [unverified chain].


                                         8
