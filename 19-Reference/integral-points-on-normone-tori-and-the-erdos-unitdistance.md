---
title: "Integral points on norm–one tori and the Erdős unit–distance"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/ca35f196125c899a5ad11f011080202a652aef02.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:58Z"
tags: ["news-research"]
---

Integral points on norm–one tori and the Erdős unit–distance
                         exponent


                                         Abstract
       For a ﬁnite planar set P ⊂ R let u(P ) denote the number of unordered pairs of
                                     2

    points of P at Euclidean distance exactly 1, and write u(n) = max{u(P ) : |P | = n}.
    Erdős, in 1946, conjectured the upper bound u(n) ≤ n1+O(1/ log log n) . We refute this
    conjecture: along an inﬁnite sequence of integers n,
                                                   log log log n
                                            1+c0
                                 u(n) ≥ n            log log n

    with c0 > 0 an absolute constant. Our point sets are produced by projecting OK    2
                                                                                        to
    R via a single real embedding of a number ﬁeld K drawn from an inﬁnite unramiﬁed
      2

    tower of mixed signature and bounded root discriminant. The unit–distance pairs
    come from OK –points of the aﬃne conic u2 +v 2 = 1, which form a group of rank r2 (K)
    — a ﬁxed positive fraction of d = [K : Q]. Applying van der Corput’s theorem turns
    this rank into eΩ(d log log d) unit–distance directions, which dominates the remaining
    eO(d) losses.


Contents

1 Introduction                                                                                  2

2 Number–theoretic preliminaries                                                                3
  2.1   Number ﬁelds, places, and the Minkowski embedding . . . . . . . . . . . .               3
  2.2   The norm–one torus and its logarithm lattice . . . . . . . . . . . . . . . .            3
  2.3   From U (1) to integral vectors on a circle      . . . . . . . . . . . . . . . . . . .   4

3 Four lemmas                                                                                   5
  3.1   A packing upper bound . . . . . . . . . . . . . . . . . . . . . . . . . . . .           5
  3.2   A van der Corput lower bound . . . . . . . . . . . . . . . . . . . . . . . .            5
  3.3   Upper bound for R(1)     . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      6
  3.4   Counting bounded–height points of U (1)         . . . . . . . . . . . . . . . . . . .   8

4 The point set and the key inequality                                                          8

5 An inﬁnite family of number ﬁelds                                                             9
  5.1   An inﬁnite totally real 2–class–ﬁeld tower . . . . . . . . . . . . . . . . . .          9

                                              1
     5.2   The quadratic twist . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   10

6 Proof of the main theorem                                                                  11

7 Consistency with known bounds                                                              12

8 Concluding remarks                                                                         12


1.     Introduction

For a ﬁnite set P ⊂ R2 deﬁne the unit–distance count
                        
               u(P ) = # {p, q} ⊂ P : kp − qk = 1 ,  u(n) = max u(P ).
                                                                     |P |=n
                                   √     √
Erdős observed in 1946 that the n × n integer grid, after a suitable rescaling, satisﬁes
u(n) ≥ n1+c/ log log n for some absolute c > 0, and conjectured that this was essentially the
truth:
                                   u(n) ≤ n1+O(1/ log log n) .                            (1)
On the upper–bound side, the best result to date is the Spencer–Szemerédi–Trotter bound
u(n) = O(n4/3 ).

Theorem 1.1. The inequality (1) fails. More precisely, there are absolute constants
c0 > 0 and n0 and an inﬁnite set N ⊂ Z≥n0 for which

                                             log log log n
                                      1+c0
                           u(n) ≥ n            log log n     (n ∈ N ).

In particular, given any C > 0, there are inﬁnitely many n with u(n) > n1+C/ log log n .

   The second statement follows from the ﬁrst since log log log n tends to inﬁnity. Our
construction does not threaten the Spencer–Szemerédi–Trotter ceiling: the exponent we
produce is 1 + o(1).


Idea of the proof. What drives Erdős’s grid is the fact that the Gaussian integers Z[i]
contain many elements of a ﬁxed norm; the supply,      however, is controlled by the divisor
function, and so is at most exp O(log n/ log log n) for any norm value. We exchange Z[i]
for the ring of integers OK of a number ﬁeld K of large degree d with at least one real
embedding and r2  d complex places. In this regime the norm–one torus {u2 + v 2 = 1}
acquires inﬁnitely many OK –rational points, organized into a group of rank r2 . Choosing
a real embedding σ : K ,→ R projects each such point to an honest unit vector in R2 ,
and van der Corput’s theorem furnishes at least T r2 /R(1) points with every archimedean
valuation in [e−T , eT ], where R(1) is the covolume of the relevant logarithm lattice. Picking
K along an inﬁnite class–ﬁeld tower keeps the root discriminant bounded; Louboutin’s
bound on Ress=1 ζK(i) together with Zimmert’s regulator estimate then limit R(1) ≤ eO(d) .
With T  log d this yields eΩ(d log log d) unit directions, dwarﬁng the other losses, which
are only eO(d) .


                                                  2
2.      Number–theoretic preliminaries

2.1.     Number ﬁelds, places, and the Minkowski embedding

Let K be a number ﬁeld of degree d = [K : Q] with ring of integers OK . Denote its real
embeddings by σ1 , . . . , σr1 and its pairs of complex embeddings by τ1 , τ̄1 , . . . , τr2 , τ̄r2 , so
that d = r1 + 2r2 . We write w for a generic archimedean place of K, setting nw = 1
if w is real and nw = 2 if w is complex, and |x|w for the corresponding normalized
absolute
Q           value (|x|σk = |σk (x)| and |x|τj = |τj (x)|). The product formula then reads
     |x| nw = | N                   ×
   w     w        K/Q (x)| for x ∈ K .
     The Minkowski embedding
                                                                                                  
         ι : K −→ Rr1 × Cr2 ∼
                            = Rd ,          x 7−→ σ1 (x), . . . , σr1 (x), τ1 (x), . . . , τr2 (x) ,

identiﬁes OK with a full–rank lattice of covolume 2−r2 |∆K |1/2 , where ∆K = disc(K/Q);
see, for example, Neukirch, Algebraic Number Theory, Springer 1999, Prop. I.5.2.
     For R > 0 deﬁne
                            
                  BR :=         x ∈ OK : |x|w ≤ R for every archimedean w .

The deﬁning region of BR under ι is the convex, origin–symmetric body [−R, R]r1 ×{|z| ≤
R}r2 ⊂ Rd , whose volume is
                                         
             vol [−R, R]r1 × {|z| ≤ R}r2 = (2R)r1 (πR2 )r2 = 2r1 π r2 Rd .          (2)


2.2.     The norm–one torus and its logarithm lattice

Henceforth assume r1 ≥ 1, which in particular forces i ∈  / K (any totally real embedding
would send i into R). Set L := K(i), a quadratic extension of degree 2d, with non–trivial
Galois element η 7→ η̄; on the level of generators a + bi = a − bi for a, b ∈ K. Because i
is imaginary, all archimedean places of L are complex, and we label them as follows.

Lemma 2.1. The archimedean places of L split as:

     • For each real embedding σk of K, a single complex place σ̃k of L, represented by
       σk+ : a + bi 7→ σk (a) + iσk (b).
                                                                             (1)   (2)
     • For each complex embedding τj of K, two complex places τ̃j , τ̃j                  of L, represented
       by τj± : a + bi 7→ τj (a) ± iτj (b) respectively.

In total L has r1 + 2r2 = d complex places, so r1 (L) = 0 and r2 (L) = d. Furthermore, for
every η ∈ L,
                             |η̄|σ̃k = |η|σ̃k , |η̄|τ̃ (1) = |η|τ̃ (2) .               (3)
                                                          j          j


Proof. Any embedding ψ : K ,→ C has two extensions ψ ± : L → C speciﬁed by ψ ± (i) =
                                                           −
±i, and complex conjugation on C takes ψ + to ψ . When ψ = σk is real, σk = σk , so
σk± are complex conjugates and deﬁne a single place. When ψ = τj is complex, τj = τ̄j ,
so the two conjugate pairs {τj+ , τ̄j− } and {τj− , τ̄j+ } yield two distinct places. Finally, the
identity ψ + (η̄) = ψ + (a − bi) = ψ(a) − iψ(b) = ψ − (η) gives (3).

                                                   3
                           
Deﬁnition 2.2. Set U (1) := ζ ∈ OL× : NL/K (ζ) = ζ ζ̄ = 1 .
Lemma 2.3. U (1) is a ﬁnitely generated abelian group of rank r2 . Moreover, every
ζ ∈ U (1) satisﬁes |ζ|σ̃k = 1 for all k and |ζ|τ̃ (1) · |ζ|τ̃ (2) = 1 for all j.
                                                       j          j


Proof. By deﬁnition, U (1) is the kernel of N : OL× → OK                ×
                                                                          . Its image contains (OK          × 2
                                                                                                             ) —
                                           ×         ×                                                ×
because N() =  whenever  ∈ OK ⊂ OL — and so has ﬁnite index in OK . Dirichlet’s
                   2

unit theorem gives rank OL× = r2 (L) − 1 = d − 1 and rank OK                  ×
                                                                                 = r1 + r2 − 1; subtracting,
rank U = (d − 1) − (r1 + r2 − 1) = r2 . For the valuation identities, ζ ζ̄ = 1 combined
       (1)

with (3) gives |ζ|2σ̃k = |ζ|σ̃k |ζ̄|σ̃k = |ζ ζ̄|σ̃k = 1 and |ζ|τ̃ (1) |ζ|τ̃ (2) = |ζ|τ̃ (1) |ζ̄|τ̃ (1) = 1.
                                                                      j    j           j     j

Deﬁnition 2.4. Introduce the logarithm map
                                                                              r2
                              L : U (1) −→ Rr2 ,           ζ 7−→ log |ζ|τ̃ (1) j=1 ,
                                                                           j
                                      
and write R(1) := det L(U (1) )           for the covolume of the image lattice inside Rr2 .
Lemma 2.5. L is a homomorphism with ﬁnite kernel (precisely the roots of unity inside
U (1) ), and its image L(U (1) ) is a full–rank lattice in Rr2 .

Proof. That L is a homomorphism is immediate. If L(ζ) = 0 then combining this with
Lemma 2.3 forces |ζ|w = 1 at every archimedean place of L, and Kronecker’s theorem then
identiﬁes ζ as a root of unity. Thus ker L is ﬁnite, and rank L(U (1) ) = rank U (1) = r2 .


2.3.     From U (1) to integral vectors on a circle

For any ζ ∈ L, write ζ = u + iv with u = 12 (ζ + ζ̄) and v = 2i
                                                             1
                                                                (ζ − ζ̄) both in K.
Lemma 2.6. The rule ζ 7→ (2u, 2v) deﬁnes a bijection
                         ∼         
                 U (1) −−→ T := (a, b) ∈ OK    2
                                                 : a 2 + b2 = 4 .

Proof. Given ζ ∈ U (1) , the quantity 2u = ζ + ζ̄ is TrL/K (ζ) and lies in OK , while
2vi = ζ − ζ̄ ∈ OL and, since i ∈ OL× , the element 2v lies in OL ∩ K = OK . A direct
calculation gives (2u)2 + (2v)2 = 4(u2 + v 2 ) = 4ζ ζ̄ = 4, so (2u, 2v) ∈ T ; injectivity is
plain.
   For the reverse direction, take any (a, b) ∈ T and put ζ := 21 (a + bi). Then ζ satisﬁes
the integral equation X 2 − aX + 41 (a2 + b2 ) = X 2 − aX + 1 ∈ OK [X], hence ζ ∈ OL .
Furthermore ζ ζ̄ = 41 (a2 + b2 ) = 1, so ζ −1 = ζ̄ ∈ OL and ζ ∈ U (1) . Since (2u, 2v) = (a, b),
the map is surjective.
Lemma 2.7. Let ζ ∈ U (1) satisfy kL(ζ)k∞ ≤ T , and form (a, b) = (2u, 2v) ∈ OK
                                                                             2 as

above. Then
           |a|σk , |b|σk ≤ 2         (1 ≤ k ≤ r1 ),         |a|τj , |b|τj ≤ 2eT        (1 ≤ j ≤ r2 ).

Proof. At a real place we have σk (u)2 + σk (v)2 = σk (u2 + v 2 ) = 1, so |u|σk , |v|σk ≤ 1.
At a complex place, τj± (ζ) = τj (u) ± iτj (v) gives τj (u) = 21 (τj+ (ζ) + τj− (ζ)), hence with
yj = log |ζ|τ̃ (1) ,
              j
                                                   
              |u|τj ≤     1
                          2   |ζ|τ̃ (1) + |ζ|τ̃ (2) = 21 (eyj + e−yj ) = cosh yj ≤ e|yj | ≤ eT ,
                                 j          j

and similarly for v.

                                                       4
3.     Four lemmas

Throughout this section K denotes a number ﬁeld of degree d with r1 ≥ 1 real and r2
complex places, and we write γ := d1 log |∆K | for the logarithmic root discriminant. Every
constant below depends only on γ and on c := r2 /d ∈ (0, 12 ], never on d itself.


3.1.   A packing upper bound

Lemma 3.1. For every real M ≥ 1, |BM | ≤ (2M + 1)d .
                                                          P           P         P
Proof. Endow Rd ∼  = Rr1 × Cr2 with the norm kxk2∗ := k |x|2σk + 2 j |x|2τj = w nw |x|2w .
For any 0 6= x ∈ OK the weighted AM–GM inequality yields
                     P               Y              1/d
             kxk2∗      w nw |x|w
                                2
                   = P            ≥       (|x|2w )nw      = | NK/Q (x)|2/d ≥ 1,
               d          w n w         w
           √                                            P                              √
so kxk∗ ≥ d. If in addition x ∈ BM then kxk2∗ ≤ M 2 w nw = dM √        2 , i.e. kxk ≤ M d.
                                                                                   ∗

                      √ ι(BM ) sit inside the k · k∗ –ball of radius √
Consequently the images                                              M d and are pairwise
separated by at least d in this norm; open k · k∗ –balls
                                                     √ of√radius d/2 around them are
then disjoint and contained in the ball of radius M d + d/2, so
                               √     √ 
                    vol∥·∥∗ M d + 2d       √ √ d
            |BM | ≤              √      = M √d+
                                               d/2
                                                   d/2
                                                       = (2M + 1)d .
                                  d
                         vol∥·∥∗ 2


3.2.   A van der Corput lower bound

The following is the classical reﬁnement of Minkowski’s ﬁrst theorem that we will need.

Theorem 3.2 (van der Corput). Let Λ ⊂ Rn be a lattice and let S ⊂ Rn be a bounded,
convex, origin–symmetric body. If vol(S) > m · 2n det Λ for some positive integer m, then
S contains at least 2m non–zero points of Λ; in particular |S ∩ Λ| ≥ 2m + 1.

Proof. See J. W. S. Cassels, An Introduction to the Geometry of Numbers, Springer 1971,
Ch. III, Theorem II (p. 71); or P. M. Gruber and C. G. Lekkerkerker, Geometry of
Numbers, 2nd ed., North–Holland 1987, §6, Theorem 1. The original reference is J. G. van
der Corput, Acta Arith. 2 (1936), 145–146.

Corollary 3.3. Under the hypotheses of Theorem 3.2, if vol(S) ≥ 2·2n det Λ then |S∩Λ| ≥
vol(S)/(2n det Λ).

Proof. Set m = bvol(S)/(2n det Λ)c − 1 ≥ 1 when vol(S)/(2n det Λ) is an integer, and
m = bvol(S)/(2n det Λ)c otherwise. In both cases m ≥ vol(S)/(2n det Λ) − 1, and so
|S ∩ Λ| ≥ 2m + 1 ≥ 2 vol(S)/(2n det Λ) − 1 ≥ vol(S)/(2n det Λ).

Lemma 3.4. There exists a constant R0 = R0 (γ, c) such that for all R ≥ R0 ,
                                           r 2     Rd
                                |BR | ≥     π
                                                            .
                                            2
                                                   |∆K |1/2


                                            5
Proof. We apply Corollary 3.3 with Λ = ι(OK ) ⊂ Rd and S = ι(BR ). Using (2) and the
identity det Λ = 2−r2 |∆K |1/2 ,

                vol(S)        2r 1 π r 2 R d   2r1 +r2 π r2 Rd  π r2 Rd
                        =                    =                = 2              .
               2d det Λ   2d · 2−r2 |∆K |1/2    2d |∆K |1/2           |∆K |1/2

The requisite hypothesis vol(S) ≥ 2 · 2d det Λ is equivalent to (π/2)r2 Rd ≥ 2|∆K |1/2 , that
                         1/d
is R ≥ 2|∆K |1/2 (2/π)r2      ≤ 21/d eγ/2 (2/π)c =: R0 .


3.3.    Upper bound for R(1)

We recall two classical inputs.

Theorem 3.5 (Louboutin). For any number ﬁeld E of degree n ≥ 2,
                                                          e log |∆ | n−1
                                                                  E
                           κE := Ress=1 ζE (s) ≤                             .
                                                           2(n − 1)

Proof. S. Louboutin, Explicit upper bounds for residues of Dedekind zeta functions and
values of L–functions at s = 1, and explicit lower bounds for relative class numbers of
CM–ﬁelds, Canad. J. Math. 53 (2001), 1194–1222, Theorem 1.

Theorem 3.6 (Zimmert). There exists an absolute constant cZ > 0 for which RE ≥ cZ
holds at every number ﬁeld E 6= Q satisfying r1 (E) + r2 (E) ≥ 2.

Proof. R. Zimmert, Ideale kleiner Norm in Idealklassen und eine Regulatorabschätzung,
Invent. Math. 62 (1981), 367–380, Satz 3, gives RE /wE ≥ 0.02 e0.1 r2 (E) (in fact more);
combined with wE ≥ 2 this yields RE ≥ 2 · 0.02 = 0.04. One may take cZ = 0.04.

Lemma 3.7. With L = K(i) and R(1) as in Deﬁnition 2.4,

                                          w K RL       wK
                                R(1) ≤      r
                                                ·    ≤    RL .
                                          2   2   RK   cZ

In particular there is a constant C1 = C1 (γ) such that R(1) ≤ eC1 d holds for all suﬃciently
large d.

                                                               ×
Proof. Write `∗L : OL× → Rd , η 7→ (2 log |η|w )w , and `∗K : OK  → Rr1 +r2 ,  7→ (nv log ||v )v ,
for
P the standard logarithm embeddings.
                                P           Their images lie in the hyperplanes HL := {x :
    x
   w w  = 0}  and  H K := {y  :    y
                                  v v  = 0}  respectively, and (cf. Neukirch, op. cit., Ch. I,
§7)                           √                                   √
           covolHL `∗L (OL× ) = d RL ,         covolHK `∗K (OK ×
                                                                 ) = r1 + r2 R K .             (4)
                                    P
(For a rank–(m−1) lattice inside { xi = 0} ⊂ Rm whose rows sum to zero, all (m−1) ×
(m−1) minors share a common absolute value R, and the hyperplane covolume equals
√
  m R; for `∗L that common value is RL by the deﬁnition of the regulator.)
    Set H ′ := {x ∈ Rd : xσ̃k = 0, xτ̃ (1) + xτ̃ (2) = 0 ∀k, j}, an r2 –dimensional subspace
                                          j          j

contained in HL . By Lemma 2.3, `∗L (U (1) ) ⊂ H ′ . Let

                            A := H ′ ∩ `∗L (OL× ),        B := `∗L (OL× ).


                                                 6
Then A ⊂ B is a sublattice of rank r2 , the short exact sequence 0 → A → B → B/A → 0
produces a full–rank lattice B/A inside HL /H ′ , and

                            covolHL (B) = covolH ′ (A) · covolHL /H ′ (B/A).                             (5)

    Index [A : `∗L (U (1) )]. For η ∈ OL× , the condition `∗L (η) ∈ H ′ holds exactly when
| NL/K (η)|v = 1 at every archimedean v of K, equivalently when NL/K (η) ∈ µK (the
roots of unity of K). Hence A = `∗L ({η : N η ∈ µK }), and since U (1) is the full kernel of
N |O × ,
     L                                                   
                  A : `∗L (U (1) ) ≤ {η : N η ∈ µK } : U (1) ≤ |µK | = wK ,
the last step because N embeds the quotient into µK .
      Covolume of B/A. Deﬁne N∗ : Rd → Rr1 +r2 by (N∗ x)σk = xσ̃k and (N∗ x)τj = xτ̃ (1) +
                                                                                                     j
xτ̃ (2) ; a place–by–place check with Lemma 2.1 conﬁrms that N∗ ◦ `∗L = `∗K ◦ NL/K on OL× .
  j
                                                                                  ∼
Its kernel is H ′ , so N∗ induces a linear  √    isomorphism HL /H ′ −→ HK . In the orthonormal
                                                                                       √
                                                     ′ ⊥
basis {eσ̃k } ∪ {fj := (eτ̃ (1) + eτ̃ (2) )/ 2} of (H ) ⊂ R , N∗ eσ̃k = eσk and N∗ fj = 2 eτj , so
                                                            d
                             j       j

N∗ |(H ′ )⊥ is diagonal with determinant 2r2 /2 . Decomposing (H ′ )⊥ = ( (H ′ )⊥ ∩ HL ) ⊕ R1L
and Rr1 +r2 = HK ⊕ R1K (where 1• is the all–ones vector), one veriﬁes N∗T 1K = 1L |(H ′ )⊥ ,
                         
hence N∗ (H ′ )⊥ ∩ HL = HK ; a block–triangular calculation then yields
                                                                                 q
                                                    ′
                          J := det N∗ : HL /H → HK                  = 2   r2 /2       r1 +r2
                                                                                         d .

                                                                                ×
The map N∗ sends B/A isomorphically onto `∗K (N(OL× )), which sits inside `∗K (OK ) at
        ′     ∗     ×   ∗     ×
index Q := [`K (OK ) : `K (N(OL ))] ≥ 1. Therefore
                                                       √                √
                           covolHK `∗K (N(OL× ))     Q ′ r1 + r2 R K   Q′ d R K
     covolHL /H ′ (B/A) =                          =                 =          .
                                     J                      J            2r2 /2

      Assembling. Substituting (4) and the last two paragraphs into (5),
                                                         √
                 ∗
                                                          d RL          2r2 /2 wK RL
       covolH ′ `L (U ) ≤ wK covolH ′ (A) = wK · √
                     (1)
                                                                     =                .
                                                     Q′ d RK /2r2 /2         Q ′ RK

On U (1) one has L = 21 · π ◦ `∗L , with π : H ′ → Rr2 , x 7→ (xτ̃ (1) )j ; in the orthonormal basis
                            √                                            j

e′j := (eτ̃ (1) − eτ̃ (2) )/ 2 of H ′ , πe′j = √12 ej , so | det π| = 2−r2 /2 and
            j        j


                                                                               wK       RL   w K RL
      R(1) = det L(U (1) ) = 2−r2 · 2−r2 /2 · covolH ′ `∗L (U (1) )       ≤            ·    ≤ r2 ·    .
                                                                               2r 2 Q ′ R K   2    RK

This is the ﬁrst claimed inequality; the second follows from Theorem 3.6 (applicable
because r1 + r2 ≥ 2).
    For the asymptotic estimate, the analytic class number formula hL RL = wL |∆L |1/2 κL /(2π)d
(recall every place of L is complex) gives

                                                            wL |∆L |1/2
                                     R L ≤ hL R L =                     κL .                             (6)
                                                              (2π)d


                                                        7
The conductor–discriminant formula yields |∆L | = |∆K |2 NK/Q (dL/K ), and dL/K | (4)OK
(the discriminant of X 2 + 1), so |∆L | ≤ 4d |∆K |2 = 4d e2γd and log |∆L | ≤ (2γ + 2 log 2)d.
Theorem 3.5 applied with n = 2d now gives
                                                    2d−1                    2d
                                    e(2γ+2 log 2)d
                         κL ≤          2(2d−1)               ≤ e(γ + log 2)

for d ≥ 1. Finally wE ≤ 2[E : Q]2 for any number ﬁeld E — since µm ⊂ E forces
ϕ(m) | [E : Q], hence m ≤ 2[E : Q]2 — so wL ≤ 8d2 and wK ≤ 2d2 . Putting all of this
together,
                        2d2 8d2 · 2d eγd · (e(γ + log 2))2d
                 R(1) ≤    ·                                = eC1 d+O(log d)
                        cZ               (2π)d
with C1 := log 2 + γ − log(2π) + 2 + 2 log(γ + log 2), a constant that depends only on
γ.


3.4.   Counting bounded–height points of U (1)

Lemma 3.8. For T > 0 put D(T ) := #{ζ ∈ U (1) : kL(ζ)k∞ ≤ T }. If T ≥ (2R(1) )1/r2 ,
then D(T ) ≥ T r2 /R(1) .
                                                               
Proof. Because ker L is ﬁnite, D(T ) ≥ # L(U (1) ) ∩ [−T, T ]r2 . Applying Corollary 3.3
with Λ = L(U (1) ) ⊂ Rr2 — full–rank by Lemma 2.5, of determinant R(1) — and S =
[−T, T ]r2 , the ratio vol(S)/(2r2 det Λ) = T r2 /R(1) ≥ 2 by hypothesis, and the lemma
follows.


4.     The point set and the key inequality

Fix a real embedding σ = σ1 : K ,→ R, and for M ≥ 4 deﬁne
                           n                                       o
             P = PK,M :=      1
                              2 σ(x), 1
                                      2 σ(y)   : (x, y) ∈ B M × B M   ⊂ R2 .

Injectivity of σ gives |P | = |BM |2 =: n.

Proposition 4.1. With T := log(M/4),

                                    u(P ) ≥      2 D(T ) · |BM/2 | .
                                                 1                2


Proof. Pick ζ ∈ U (1) with kL(ζ)k∞ ≤ T and let (a, b) ∈ OK
                                                         2 be the corresponding pair

from Lemma 2.6. Lemma 2.7 then bounds |a|w , |b|w ≤ max(2, 2eT ) = M/2 at every
archimedean w (since M ≥ 4).
    Given any (x, y) ∈ BM/2 × BM/2 , set p := ( 21 σ(x), 21 σ(y)) and q := ( 12 σ(x + a), 21 σ(y +
b)). Then p ∈ P because BM/2 ⊂ BM , and |x + a|w ≤ |x|w + |a|w ≤ M/2 + M/2 = M at
every w, so (x + a, y + b) ∈ BM × BM and q ∈ P as well. A direct computation gives
                                            
                 kp − qk2 = 41 σ(a)2 + σ(b)2 = 41 σ(a2 + b2 ) = 14 · 4 = 1.

Hence the map

       Φ : {ζ : kL(ζ)k∞ ≤ T } × (BM/2 × BM/2 ) −→ {(p, q) ∈ P × P : kp − qk = 1}

                                                      8
sending (ζ, (x, y)) to the pair (p, q) above is well–deﬁned. It is also injective: from (p, q)
one recovers (x, y) via injectivity of σ, then (a, b) = (x′ −x, y ′ −y) where (x′ , y ′ ) corresponds
to q, and ﬁnally ζ by inverting Lemma 2.6. Hence the number of ordered unit–distance
pairs in P is at least D(T ) · |BM/2 |2 , and u(P ) is half this count.

Proposition 4.2. There is a constant C2 = C2 (γ, c) > 0 such that for every M ≥
max(4, 2R0 ) (with R0 from Lemma 3.4),
                         u(P )                  −C2 d
                               ≥    2 D(T ) · e
                                    1
                                                      ,    T = log(M/4).
                          n

Proof. Combining Proposition 4.1 with Lemmas 3.1 and 3.4 (the latter applied with
R = M/2 ≥ R0 ),

                    u(P )   D(T ) |BM/2 |2   D(T ) (π/2)2r2 (M/2)2d
                          ≥      ·         ≥      ·                  .
                     n       2     |BM |2     2     |∆K | (2M + 1)2d
                                                                                2d
The trivial bound (M/2)/(2M + 1) ≥ 1/6 for M ≥ 1 gives (M/2)/(2M + 1)               ≥ 6−2d ,
and so
           u(P )   D(T ) (π/2)2r2        D(T )                                
                 ≥       ·             =       exp  2r 2 log π
                                                               − γd − d log 36   ;
             n       2     |∆K | · 36d    2                  2


we may take C2 = γ + log 36 − 2c log(π/2).


5.     An inﬁnite family of number ﬁelds

Proposition 5.1. There exist a real number γ⋆ > 0, a rational c⋆ ∈ (0, 12 ), and an inﬁnite
sequence of number ﬁelds (Km )m≥0 with dm := [Km : Q] → ∞, such that for each m:

  (i) r1 (Km ) ≥ 1 and r2 (Km ) = c⋆ dm ;
 (ii) d1m log |∆Km | ≤ γ⋆ .

     The proof spans the rest of the section.


5.1.    An inﬁnite totally real 2–class–ﬁeld tower

Theorem 5.2 (Golod–Shafarevich criterion). Let F be a number ﬁeld and p a prime. If
                                    q
                 dp Cl(F ) > 2 + 2 r1 (F ) + r2 (F ) + δp (F ) ,

where δp (F ) = 1 when µp ⊂ F and 0 otherwise, then the Hilbert p–class–ﬁeld tower
F = F0 ⊂ F1 ⊂ F2 ⊂ · · · is inﬁnite.

Proof. E. S. Golod and I. R. Shafarevich, On the class ﬁeld tower (Russian), Izv. Akad.
Nauk SSSR Ser. Mat. 28 (1964), 261–272, show that a pro–p group G with d(G) generators
and r(G) relations is inﬁnite whenever r(G) < d(G)2 /4. Taking G to be the Galois group
of the maximal unramiﬁed p–extension of F gives d(G) = dp (Cl(F )), and Shafarevich’s
relation–rank bound,
                                            
              r(G) ≤ d(G) + dimFp OF× ⊗ Fp = d(G) + (r1 + r2 − 1) + δp ,

                                                  9
controls r(G) (see P. Roquette, On class ﬁeld towers, in Cassels–Fröhlich, Algebraic Num-
ber Theory, Academic Press 1967, Ch. IX, Theorems 1–3, or H. Koch, Galois Theory of
p–Extensions, Springer 2002, Theorem 11.16). Solving d(G) + (r1 + r2 − 1 + δp ) < d(G)2 /4
recovers the stated criterion.
                                                          √
Lemma 5.3. There exists a real quadratic ﬁeld F0 = Q( D) whose Hilbert 2–class–ﬁeld
tower is inﬁnite.

Proof. Let D > 0 be squarefree with exactly t distinct prime divisors. Gauss’s genus
theory (see e.g. D. A. Cox, Primes of the Form x2 + ny 2 , Wiley 1989, Prop. 3.11) gives
d2 (Cl+ (F0 )) = t − 1 for the narrow class group. The natural surjection Cl+ (F0 ) ↠ Cl(F0 )
has kernel of order at most 2 (generated by the narrow class of a totally positive non–
square unit, when one exists), so d2 (Cl(F0 )) ≥ t−2. In the√real quadratic case r1 = 2, r2 =
0, δ2 = 1, and Theorem 5.2 demands d2 (Cl(F0 )) > 2 + 2 3, equivalently d2 (Cl(F0 )) ≥ 6.
Taking t = 8 — for instance with D = 3 · 5 · 7 · 11 · 13 · 17 · 19 · 23 — yields d2 (Cl(F0 )) ≥ 6,
and the tower is therefore inﬁnite.

    Fix such an F0 and its tower F0 ⊂ F1 ⊂ · · · . Each step is unramiﬁed at every place,
including at inﬁnity, so every Fm remains totally real, and |∆Fm |1/[Fm :Q] = |∆F0 |1/2 for
all m.


5.2.   The quadratic twist
         √                                            √
Put α := D ∈ F0 . Its two real embeddings carry α to ± D, so it has one positive and
one negative real conjugate.

Lemma 5.4. α is not a square in Fm for any m ≥ 0.
                          √
Proof. The extension F0 ( α)/F0 is ramiﬁed at the real place at which α < 0 (where
the place becomes complex), and so cannot be contained in any everywhere–unramiﬁed
                                                                   √
extension of F0 . Since Fm /F0 is everywhere unramiﬁed, we conclude α ∈
                                                                      / Fm .
                                                 √
Deﬁnition 5.5. For each m ≥ 0, set Km := Fm ( α).

Lemma 5.6. For every m ≥ 0:

 (a) [Km : Q] = 2[Fm : Q]; in particular dm = [Km : Q] → ∞.

 (b) Km /K0 is everywhere unramiﬁed; consequently |∆Km |1/dm = |∆K0 |1/d0 =: eγ⋆ .

 (c) r1 (Km ) = 12 dm and r2 (Km ) = 41 dm .

 (d) i ∈
       / Km .

Proof. (a) Lemma 5.4 gives [Km : Fm ] = 2.
                                 √
   (b) The ﬁelds Fm and K0 = F0 ( α) are linearly disjoint over F0 (again by Lemma 5.4),
so Km = Fm · K0 and Gal(Km /K0 ) ∼    = Gal(Fm /F0 ). Unramiﬁedness behaves well un-
der base change: for any place w of K0 lying over a place v of F0 , the completion
(Km )W /(K0 )w is contained in (Fm )W ′ · (K0 )w /(K0 )w for suitable W, W ′ , and the com-
positum of the unramiﬁed extension (Fm )W ′ /(F0 )v with (K0 )w is unramiﬁed over (K0 )w
(unramiﬁedness of local extensions is preserved by base change; see Neukirch, op. cit.,


                                               10
Prop. II.7.2). This applies at all places, inﬁnite included, so Km /K0 is everywhere un-
ramiﬁed and |∆Km | = |∆K0 |[Km :K0 ] .
    (c) Each real place σ̃ of Fm lies above a unique real place σ0 of F0 , with σ̃(α) = σ0 (α).
Over the [Fm : F0 ] places of Fm above the real place of F0 where σ0 (α) > 0, Km has
2[Fm : F0 ] real places; over the [Fm : F0 ] places above the place where σ0 (α) < 0, Km
has [Fm : F0 ] complex places. Summing these contributions with the one–positive–one–
negative sign data gives r1 (Km ) = 2[Fm : F0 ], r2 (Km ) = [Fm : F0 ], and dm = 2[Fm : Q] =
4[Fm : F0 ], proving (c).
                                                √
    (d) Suppose, for contradiction, i = a + b α with a, b ∈ Fm . Squaring gives −1 =
                √
a2 + b2 α + 2ab α, so (by Lemma 5.4) 2ab = 0. If b = 0, then a2 = −1 is impossible in
         √ real Fm . If a = 0, then α = −1/b is totally negative in Fm , contradicting
the totally                                       2

σ0 (α) = D > 0 at one real place of F0 .

Proof of Proposition 5.1. Take c⋆ = 14 and γ⋆ = d10 log |∆K0 |, where K0 = Q(D1/4 ) with
D as in Lemma 5.3. Then Lemma 5.6 veriﬁes (i)–(ii).

Remark 5.7. Concretely, |∆K0 | divides 256 D3 (the discriminant of X 4 − D), so eγ⋆ ≤
4D3/4 . For D = 3 · 5 · 7 · 11 · 13 · 17 · 19 · 23 this is a ﬁnite, if large, number. We make no
attempt to optimise γ⋆ .


6.     Proof of the main theorem

Let (Km ), c⋆ = 41 , γ⋆ be as supplied by Proposition 5.1. Write d = dm , K = Km ,
r2 = c⋆ d, and let C1 = C1 (γ⋆ ), C2 = C2 (γ⋆ , c⋆ ) be the constants appearing in Lemma 3.7
and Proposition 4.2. Fix once and for all A := 2.

Lemma 6.1. There exists d⋆ = d⋆ (γ⋆ ) such that for every m with dm ≥ d⋆ , setting
M := dA and T := log(M/4):

  (i) M ≥ max(4, 2R0 ) and T ≥ (2R(1) )1/r2 ;

 (ii) log D(T ) ≥ c⋆ d log log d − C1 d − d;

(iii) log n ≤ 2Ad log d + 3d, and log n ≥ 2Ad log d − (γ⋆ + 1)d;

 (iv) log(u(P )/n) ≥ c⋆ d log log d − (C1 + C2 + 2)d.

Proof. (i) R0 = R0 (γ⋆ , c⋆ ) is a constant, and M = d2 ≥ max(4, 2R0 ) for d large.
Lemma 3.7 gives (2R(1) )1/r2 ≤ (2eC1 d )1/(c⋆ d) = 21/(c⋆ d) eC1 /c⋆ , which is bounded, while
T = A log d − log 4 → ∞, so (i) holds once d ≥ d⋆ .
     (ii) By Lemma 3.8 and part (i), D(T ) ≥ T r2 /R(1) . Hence

 log D(T ) ≥ r2 log T − log R(1) ≥ c⋆ d log(A log d − log 4) − C1 d ≥ c⋆ d log log d − C1 d − d

for d large, using log(A log d − log 4) ≥ log log d − 1/c⋆ eventually.
    (iii) Lemma 3.1 gives n = |BM |2 ≤ (2M + 1)2d ≤ (3M )2d , so log n ≤ 2d log(3dA ) =
2Ad log d + 2d log 3 ≤ 2Ad log d + 3d. In the opposite direction, Lemma 3.4 (applicable by
(i)) gives n ≥ (π/2)2r2 M 2d /|∆K |, so log n ≥ 2Ad log d + 2r2 log(π/2) − γ⋆ d ≥ 2Ad log d −
(γ⋆ + 1)d.


                                               11
     (iv) From Proposition 4.2 together with (ii), log(u(P )/n) ≥ log D(T ) − C2 d − log 2 ≥
c⋆ d log log d − (C1 + C2 + 2)d.

Proof of Theorem 1.1. Set C3 := C1 + C2 + 2 and c0 := c⋆ /(12A) = 1/96. Take m
large enough that d = dm ≥ d⋆ and c⋆ log log d ≥ 2C3 , and put n = nm = |BdA |2 and
P = PKm ,dA as above. Lemma 6.1(iv) then gives

                                         u(P )
                                   log         ≥       1
                                                       2 c⋆ d log log d.
                                          n
By Lemma 6.1(iii), for large d we have 12 · 2Ad log d ≤ log n ≤ 3Ad log d and 21 log d ≤
log log n ≤ 2 log d. Therefore
                                    1
     log(u(P )/n)                   2 c⋆ d log log d                   c⋆
                  · log log n ≥                        · 21 log d =       log log d = c0 log log d.
         log n                        3Ad log d                       12A

Since log log n ≤ 2 log d, log log d ≥ 12 log log n − log 2 ≥ 12 log log log n for n large (using
log log n ≥ log log log n). More directly, the inequality log d ≥ 21 log log n yields log log d ≥
log log log n − log 2. Combining,
                                                                             c         log log n
                                                                           1+ 20 · log
                 u(n) ≥ u(P ) ≥ n1+c0 (log log d)/ log log n ≥ n                     log log n


for all suﬃciently large m. As m → ∞, nm → ∞ by Lemma 6.1(iii), so the set N := {nm :
m large} is inﬁnite. Replacing c0 by c0 /2 delivers the ﬁrst statement of the theorem.
   For the second statement: given C > 0, choose m large enough that also c0 log log dm >
C. Then with n = nm ,
                             log(u(n)/n)
                                          · log log n > C,
                                 log n
which is to say u(n) > n1+C/ log log n .


7.     Consistency with known bounds

Proposition 7.1. For the point sets P = PKm ,dA m
                                                   constructed above, u(P ) = n1+o(1) as
m → ∞; in particular u(P ) ≤ n4/3 for all m large enough.

Proof. By Lemma 6.1(iii)–(iv), log(u(P )/n) ≤ log D(T ) ≤ r2 log(2T ) + O(d) (trivially
                                                                                
D(T ) ≤ |{ζ}| is ﬁnite and any crude bound suﬃces); even more simply, u(P ) ≤ n2 implies
log(u(P )/n) ≤ log n, while our lower bound log(u(P )/n) ≥ Ω(d log log d) combined with
log n = Θ(d log d) gives log(u(P )/n)/ log n = O(log log d/ log d) = o(1). Thus u(P ) =
n1+o(1)  n4/3 .


8.     Concluding remarks

Remark 8.1. The threshold d⋆ in Lemma 6.1 depends doubly–exponentially on γ⋆ and
hence on the chosen base ﬁeld F0 ; in absolute terms it is astronomically large. No
optimisation of constants has been attempted. Our construction shows that u(n) ≥
n1+Ω(log log log n/ log log n) along a sparse sequence; we leave open whether u(n) = n1+Θ(log log log n/ log log n) ,
or whether a further iterated logarithm can be extracted.

                                                   12
Remark 8.2. The mechanism diﬀers in spirit from Erdős’s. In the Z[i] grid, the unit–
distance directions are the set {α ∈ Z[i] : |α|2 = r} for a highly composite r; this is a
single orbit of divisors of r under the ﬁnite unit group {±1, ±i}, and its size is dictated by
the divisor function. Over K, the unit group of the relevant order acquires positive rank
r2 = c⋆ d, and van der Corput’s theorem translates that rank into a count of bounded–
height directions growing as (log M )c⋆ d rather than exp(O(log M/ log log M )). The cost
is an eO(d) loss in the overlap ratio, which is dominated as soon as log log d exceeds a
constant depending only on γ⋆ .
Remark 8.3 (On the cited inputs). All four external inputs are unconditional and classical:
van der Corput’s theorem (1936), Louboutin’s residue bound (2001), Zimmert’s regula-
tor bound (1981), and the Golod–Shafarevich criterion (1964) applied via Gauss’s genus
theory at the base ﬁeld. Precise page/theorem references have been supplied throughout.
The proof of Lemma 3.7 contains a detailed covolume computation; a reader content with
the cruder estimate R(1) ≤ eOγ (d) may replace that computation by the observation that
each normalisation factor present is bounded by dO(1) · 2O(d) , which is absorbed.


                                             13
