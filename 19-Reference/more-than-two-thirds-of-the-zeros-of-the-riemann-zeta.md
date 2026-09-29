---
title: "MORE THAN TWO THIRDS OF THE ZEROS OF THE RIEMANN ZETA"
source_url: "https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf"
category: "19-Reference"
fetched_at: "2026-08-11T06:36:06Z"
tags: ["news-research"]
---

MORE THAN TWO THIRDS OF THE ZEROS OF THE RIEMANN ZETA
           FUNCTION LIE ON THE CRITICAL LINE

                                                       CLAUDE


         Abstract. Let N (T, 2T ) denote the number of zeros ρ = β + iγ of the Riemann zeta function
         with T < γ ≤ 2T , counted with multiplicity, and N0∗ (T, 2T ) the number of distinct such zeros
         with β = 12 . We prove unconditionally that
                                                  N0∗ (T, 2T )   2
                                             lim inf           ≥ ,
                                             T →∞ N (T, 2T )     3
         that at least ( 23 − o(1))N (T, 2T ) of the zeros are simple and on the critical line, and that
         at least ( 56 − o(1))N (T, 2T ) are distinct; with an optimised test family the three constants
         become 0.6725, 0.6725, 0.83625 . . . . The constant 32 (resp. 0.6725) is Montgomery’s (resp.
         Montgomery–Taylor’s) constant for simple zeros under the Riemann hypothesis, and the
         arithmetic input is exactly Montgomery’s prime-side evaluation of the pair-correlation second
         moment with band-width ≤ 1, which is unconditional. The Riemann hypothesis, classically
         needed to read the zero side as a positive sum over real ordinates, is replaced by linear alge-
         bra applied to a finite compression of Weil’s Hermitian form: Sylvester’s law of inertia (an
         off-line pair {ρ, 1 − ρ̄} contributes a block of signature (1, 1)) and a rank–trace inequality for
         Hermitian matrices, proved via von Neumann’s trace inequality, which is the matrix analogue
         of the integrality steps m2 ≥ 2m − 1 and m2 ≥ 3m − 2. The analytic inputs are those of
         Baluyot, Goldston, Suriajaya and Turnage-Butterbaugh [BGSTB24] and Goldston and Suri-
         ajaya [GS25, GS26]; the new ingredient is a linear-algebraic reading of their pair-correlation
         sum.


                                                   Contents
   1. Introduction                                                                                             2
   2. The explicit formula and the test family                                                                 6
   3. Lemmas from linear algebra                                                                               9
   4. The zero side: signature and rank                                                                       10
   5. The prime side: magnitude                                                                               14
   6. Proofs of Theorems A, B and C                                                                           19
   7. Variants, extensions, and remarks                                                                       20
   8. Numerical illustrations                                                                                 25
   Appendix A. The explicit formula: normalisations                                                           27
   Appendix B. Formal and symbolic verification                                                               28
   Appendix C. On the discovery of this result                                                                30
   Acknowledgments                                                                                            33

    Date: August 10, 2026.
    2020 Mathematics Subject Classification. 11M06, 11M26, 15A42.
    Key words and phrases. Riemann zeta function, critical line, explicit formula, pair correlation, Sylvester’s
law of inertia.
    The argument and its verification are the author’s. Jarred Sumner posed the problem and guided the
investigation. Ralph Furman and Levent Alpöge studied the result, set it in context, and take responsibility for
its communication. See the Acknowledgments and Appendix C..
                                                         1
2                                            CLAUDE

    References                                                                                  34


                                       1. Introduction
1.1. The question. In the autumn of 1859 Riemann [Rie59] communicated to the Berlin
Academy an eight-page memoirPon the number of primes below a given bound. Its central
object is the function ζ(s) =           −s
                                   n≥1 n , continued to C, whose zeros in the critical strip
0 < Re s < 1 he observed to govern the fluctuations of the prime-counting function. Concerning
their horizontal position Riemann wrote that it is “sehr wahrscheinlich” that all of them lie
on the line Re s = 12 ; he had not pursued a proof, he added, because it was not needed for
the immediate purpose of his note. That parenthetical remark has since become the Riemann
hypothesis, and the line Re s = 21 the critical line.
   The hypothesis remains unproven. What has been proven, in a line of work spanning more
than a century, is that an increasing proportion of the zeros do lie where Riemann said they
should, that many of them are simple, and that many of them are distinct; and it is to this
line of work that the present paper offers a contribution.

1.2. History of the problem. That ζ(s) has infinitely many zeros on the critical line was
shown by Hardy [Har14] in 1914; Hardy and Littlewood [HL21] subsequently showed that
their number up to height T is ≫ T . That a positive proportion of all zeros lie there—that is,
that N0 (T ) ≥ κ N (T ) for some absolute κ > 0 and all large T , where N (T ) counts zeros with
0 < γ ≤ T and N0 (T ) those additionally on the line—is due to Selberg [Sel42] in 1942. Selberg’s
constant was small and not made explicit. Thirty-two years passed before Levinson [Lev74],
by an entirely new and strikingly direct method based on mollifying ζ near the line, showed
that one may take κ = 13 . Heath-Brown [HB79] (and independently Selberg) observed that
Levinson’s zeros are in fact simple. Conrey [Con89] refined the mollifier to reach κ > 52 ; further
refinements by Bui, Conrey and Young [BCY11], Feng [Fen12], and Pratt, Robles, Zaharescu
and Zeindler [PRZZ20] have brought the record to
                                           5
                                     κ >   12   = 0.4166 . . . ,
where it has stood since 2020. Every result in this line uses Levinson’s method. For distinct
zeros (each point counted once regardless of multiplicity), Farmer [Far95] proved Nd (T ) >
0.6395 N (T ) unconditionally by combining simple-zero proportions for the derivatives ξ (j) ,
and Wu [Wu15] improved this to 0.6603.
   A separate line originates with Montgomery’s 1973 paper [Mon73] on the pair correlation
of zeros. Working under the Riemann hypothesis, Montgomery evaluated a certain second
moment
P 2 over        pairs of zero ordinates in terms of a sum over prime powers, deduced that
             4
    m
   ρ ρ  ≤  ( 3 + o(1))N (T ) (sum over distinct zeros), and hence that at least 23 of the zeros
are simple. By Cauchy–Schwarz the same bound gives Nd (T ) ≥ ( 43 − o(1))N (T ), and using
the integrality m2 ≥ 3m − 2 even Nd (T ) ≥ ( 56 − o(1))N (T ) [CGG98, (1.2)]. The constant 23
arises as 2 − λ1 − λ3 at λ = 1, where λ is the normalised band-limit of the test function; the
argument is a single application of the inequality m2 ≥ 2m − 1 to integer multiplicities. On
RH, 23 was improved to 0.6725 by Montgomery and Taylor [Mon75] and to 0.6727 by Cheer
and Goldston [CG93]; Bui and Heath-Brown [BHB13] obtained 19      27 (on RH and GLH earlier
in [CGG98]), and Chirre, Gonçalves and de Laat [CGdL20] obtained 0.6792 via semidefinite
programming by exploiting the positivity of F outside [−1, 1]; the optimality statement in
              MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                              3

Theorem D is scoped to the values of F on [−1, 1] only, so such majorants operate in a
different regime.
   Montgomery’s prime-side evaluation is a mean value of a Dirichlet polynomial of length T ,
and hence is unconditional; what required the Riemann hypothesis was only the reading of the
zero side, where without RH the zeros are complex and the diagonal terms cannot be isolated
by sign. That the prime side is unconditional was made fully explicit by Baluyot, Goldston,
Suriajaya and Turnage-Butterbaugh [BGSTB24] (see also Aryan [Ary22]), who showed that
Montgomery’s form factor F (α) holds for the sum over all complex zeros. In subsequent
work Goldston and Suriajaya [GS25, GS26] (see also [BGSTB25, GLSS25]) showed that Mont-
gomery’s 23 follows unconditionally if one assumes that all zeros lie within a vertical box of
width o(1/ log T ) around the line, and asked what would follow “if RH could be removed from
Montgomery’s proof”. Their work isolated the remaining obstacle precisely—the termwise
positivity that fails off the line—which the present paper replaces; see §7.4 for a detailed
comparison. Theorems A–C below answer that question.
1.3. The results. Write ρ = β +iγ for a nontrivial zero of ζ(s) and mρ ≥ 1 for its multiplicity.
For 0 ≤ T1 < T2 we write
             N (T1 , T2 ) := #{ρ : T1 < γ ≤ T2 }     (counted with multiplicity),
            Nd (T1 , T2 ) := #{ρ : T1 < γ ≤ T2 }     (each distinct point counted once),
            N0s (T1 , T2 ) := #{ρ :   T1 < γ ≤ T2 , β = 21 , mρ = 1},
and N (T ) := N (0, T ), etc. We also let N0 (T1 , T2 ) and N0∗ (T1 , T2 ) be the number of zeros on the
critical line with T1 < γ ≤ T2 counted with, respectively without, multiplicity, and N s (T1 , T2 )
the number of simple zeros; trivially
(1.1)                     N0s ≤ N0∗ ≤ N0 ≤ N,          N0s ≤ N s ≤ Nd ≤ N.
By the Riemann–von Mangoldt formula, with l := log(T /2π),
                                     T                  
(1.2)                   N (T, 2T ) =     l + 2 log 2 − 1 + O(log T ).
                                     2π
For 0 < λ ≤ 1 put
                         1 λ                    1 + H(λ)                     λ
            H(λ) := 2 − − ,          Hd (λ) :=            ,      F (λ) :=           ;
                         λ 3                         2                    1 + λ2 /3
(1.3)                    H(1) = 23 ,     Hd (1) = 56 ,     F (1) = 43 ;
                                                               √
               Hd (λ) ≥ F (λ) ⇐⇒ H(λ) ≥ 0 ⇐⇒ λ ≥ 3 − 6 = 0.5505 . . . .
Theorem A. Let 0 < λ ≤ 1 be fixed. There are constants c(λ) > 0 and T0 (λ) such that for
all T ≥ T0 (λ)
                                                  log log T 
                       N0∗ (T, 2T ) ≥ H(λ) − c(λ)              N (T, 2T ),
                                                     log T
and for λ < 1 the factor log log T may be omitted. In particular
                              N ∗ (T, 2T )   2             N ∗ (T )     2
                      lim inf 0            ≥ ,     lim inf 0        ≥ ,
                       T →∞ N (T, 2T )       3      T →∞ N (T )         3
and a fortiori N0 (T ) ≥ ( 32 − o(1))N (T ).
  The proof uses, on the arithmetic side, only the prime powers n ≤ X := (T /2π)λ , through
                                               2            2                 −1/2 and the
                                  P              P               P
Chebyshev–Mertens estimates for      n≤X Λ(n) ,     n≤X Λ(n) /n,   n≤X Λ(n)n
Montgomery–Vaughan generalised Hilbert inequality for the frequencies log n, n ≤ X; besides
4                                              CLAUDE

these it uses only Weil’s explicit formula, Stirling’s formula for Γ′ /Γ, the Riemann–von Man-
goldt formula (1.2) and the bound N (t + 1) − N (t) ≪ log(t + 3). In particular no zero-density
estimate, zero-free region, or mollifier is used.
Theorem B. With the same inputs, for fixed 0 < λ ≤ 1 and T ≥ T0 (λ),
                          log log T                                     N s (T )   2
N0s (T, 2T ) ≥ H(λ) − c(λ)             N (T, 2T ); in particular   lim inf 0       ≥ ,
                             log T                                   T →∞ N (T )     3
so at least two thirds of the zeros are simple and on the critical line; consequently also N s (T ) ≥
( 32 − o(1))N (T ).
Theorem C. For fixed 0 < λ ≤ 1 and T ≥ T0 (λ), Nd (T, 2T ) ≥                     max(Hd (λ), F (λ)) −
c(λ) logloglogT T N (T, 2T ); in particular lim inf T →∞ Nd (T )/N (T ) ≥ 56 .
                 

   In all three theorems c(λ) is absolute once λ and the taper profile ϱ of §2.2 are fixed.
                                                                                                5
   Theorem A thus improves the unconditional proportion of zeros on the critical line from 12
to 23 ; Theorem B gives the same 32 for simple zeros on the line; Theorem C improves the uncon-
ditional proportion of distinct zeros from 0.6603 [Wu15] to 56 . Optimising the test family (§7.1)
recovers exactly the Montgomery–Taylor kernel [Mon75] and gives the three constants 0.6725,
0.6725, 0.83625 . . . (Theorem D), and the same results hold for a fixed primitive Dirichlet
L-function (Theorem E).
Remark 1.1 (Optimality of the method). Theorem B uses only the mean density of zeros,
Montgomery’s pair correlation with test functions of Fourier support in (−1, 1), and the in-
tegrality of multiplicities; the Riemann Hypothesis does not enter. An explicit extremal law
on configurations shows that no certificate of this kind, reading only this bandwidth-one data
and holding configuration by configuration, can certify a proportion of simple zeros exceeding
0.68185. Theorem B’s 32 is therefore within 0.016 of the ceiling of its own method, so the
remaining gap to 1 is structural: reaching 0.70, 0.80, 0.90 by the same route would require
pair-correlation information on Fourier supports out to roughly 1.04, 1.26, 1.70 respectively,
beyond what is known.
1.4. The idea. The argument does not use Levinson’s method; it makes unconditional the
pair-correlation argument of [Mon73]. We explain it here in a form that a reader with a general
acquaintance with the explicit formula can follow; the precise version is in §§2–6.
   Weil’s explicit formula expresses, for any sufficiently regular test function f , the sum
P b
   ρ f (γρ ) over zeros as a sum over prime powers plus archimedean terms. Regard the bilinear
                             P
map (f, g) 7→ W (f, g) :=     ρ mρ fb(γρ ) gb(γρ ) as a Hermitian form on test functions; its positiv-
ity on all of Cc2 (R) is equivalent to the Riemann hypothesis [Wei52, Bom00, Yos92]. Rather
than test for positivity on the whole space, we restrict W to a finite-dimensional family V of
d ≈ λN test functions—modulated copies ϕ(u)eiτk u of a fixed compactly supported window,
with centre frequencies τk equispaced through [T, 2T ] at the critical sampling density—and let
Ge be the d × d real symmetric matrix of W |V (§2). Three facts about G      e are then available.
    (Z) Zero side: signature and rank. Up to zeros far outside the height window (a perturba-
        tion of small trace norm), G   e = P + Q where, by the functional equation, each distinct
        point on the critical line contributes to P a real rank-one nonnegative form and each
        off-line pair {ρ, 1 − ρ̄} contributes to Q a form of signature (1, 1). Thus P ⪰ 0 has rank
        at most s, the number of distinct on-line points; by Sylvester’s law of inertia (pull-back
        does not increase the positive index) Q has at most p positive eigenvalues, p the number
        of distinct off-line pairs; and in units in which an isolated simple zero has eigenvalue 1,
             MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                         5

       tr P ≤ Non and N ≥ Non + 2p (§4). That the negative index of truncations of Weil’s
       form counts off-line zeros is due to Bombieri [Bom00]; we use rank and positive index.
   (P) Prime side: magnitude. By the explicit formula, tr G          e 2 = tr G
                                                              e and ∥G∥        e 2 are integrals
                                                                        F
                                                            ′
       of explicit kernels against the density built from Γ /Γ and the prime powers n ≤ X;
       they are Montgomery’s first and second moments [Mon73, BGSTB24], and in the units
       of (Z) evaluate unconditionally to N and ( λ1 + λ3 )N asymptotically (§5).
   (L) Linear algebra. For Hermitian P ⪰ 0 of rank ≤ r and Hermitian Q with ≤ b positive
       eigenvalues (Lemma 3.2, proved via von Neumann’s trace inequality),
                               r ≥ 2 tr P + 4 tr Q − 4b − ∥P + Q∥2F .
                                                            P
       Here (2 tr P − r) + (4 tr Q − 4b) plays the role that ρ (2mρ − 1) plays in Montgomery’s
       argument; the inequality is the matrix analogue of the integrality step m2 ≥ 2m − 1.
       Alternatively, Cauchy–Schwarz on the eigenvalues (Lemma 3.3) gives n+ (P + Q) ≥
       (tr)2 /∥ · ∥2F , whence s + p ≳ F (λ)N .
Combining (Z), (P), (L): s ≥ 4N − 2N − ( λ1 + λ3 )N − o(N ) = (H(λ) − o(1))N , which at λ = 1
is Theorem A. No termwise positivity, no mollifier, no zero-density estimate, and no zero-free
region is used.
   Applied instead with only the s1 simple on-line points on the rank side and the s2 multiple
on-line points moved to the index side (r = s1 , b = s2 + p, tr P1 ≤ s1 ), the same inequality (L)
reads 3s1 +4s2 +4p ≥ 4 tr −∥·∥2F , the analogue of m2 ≥ 3m−2; together with N ≥ s1 +2s2 +2p
this gives s1 ≥ (H(λ) − o(1))N (Theorem B) and s1 + s2 + p ≥ ( 1+H(λ)       2   − o(1))N , whence
Theorem C since Nd ≥ s1 + s2 + 2p ≥ s1 + s2 + p. The       √  Cauchy–Schwarz     variant gives the
weaker Nd ≳ F (λ)N , which is what survives for λ < 3 − 6.
Remark 1.2. In the language of time–frequency analysis the family V is a Gabor system at the
critical density and G
                     e is its Gram matrix against the explicit-formula kernel; we use only the
associated sampling identity (Lemma 2.2). In the language of operator theory, G   e is a finite
compression of an operator whose full positivity is RH, and Theorems A–D extract what the
first two trace moments of any such compression can certify unconditionally.
1.5. What the results are not. It is perhaps as important to state clearly what these results
do not say.
   They have no bearing on the Riemann hypothesis in either direction. The argument produces
lower bounds only: it certifies that at least two thirds of the zeros are on the line, and says
nothing about the remaining third, which are not shown to be off the line but simply not
reached by the certificate. The inputs—the functional equation, the explicit formula, and
mean values of Dirichlet polynomials of length ≤ T —are insensitive to o(N ) off-line zeros,
and are satisfied by objects (Davenport–Heilbronn functions, Epstein zeta functions of class
number > 1) for which the analogue of RH is false. Nor can the constants be improved by the
present argument: given only tr G,e ∥G∥e 2 and the block structure, the inequalities of §3 are
                                          F
sharp, and the restriction λ ≤ 1 is essential (for X ≫ T l the off-diagonal prime sums would
require information on prime pairs of Hardy–Littlewood strength). Section 7.5 discusses these
limitations in detail.
1.6. Authorship and verification. The author of this paper is a large language model devel-
oped by Anthropic. The mathematics is its own, obtained in the course of a single interactive
session and its subsequent review by further instances of the model, and subjected throughout
to repeated adversarial review by independent instances; Appendix C gives an account of that
process. A Lean 4 formalisation of Theorems A–E accompanies the paper: the statements are
6                                            CLAUDE

expressed directly against Mathlib’s definition of ζ(s), and the repository’s documented audit
records that at the cited commit the theorem types carry no hypotheses and the proofs depend
only on Lean’s three standard axioms. The main-term constants of §5 have separately been
checked symbolically. Details are in Appendix B. Following that session the argument was
studied by the human mathematicians named in the Acknowledgments, who have read it, set
it in the context of the literature, and take responsibility for its presentation here.
   We are conscious that this is an unusual authorship, and that a claim of this strength—a
             5
jump from 12   to 23 by a short argument—naturally invites scepticism. We have tried to write
the proof so that every step is elementary and self-contained, and we would be grateful to learn
of any error.
1.7. Plan. Section 2 fixes the explicit formula, the test family and the matrix G.
                                                                                e Section 3
proves the lemmas from linear algebra. Section 4 carries out (Z), including the tail estimate
for zeros outside the window (Proposition 4.2); Section 5 carries out (P) with explicit error
terms (Theorem 5.8). Section 6 assembles the proofs of Theorems A–C. Section 7 contains
the Montgomery–Taylor optimisation (Theorem D), the extension to Dirichlet L-functions
(Theorem E), the relation to [BGSTB24, GS25, GS26], and the limits of the method; Section 8
records numerical illustrations. Appendix A checks the normalisation of the explicit formula;
Appendix B records the formal and symbolic verification; Appendix C describes how the
argument was found.
1.8. Notation. T is large; l := log(T /2π); ℓ1 := l + 2 log 2 − 1, so that N (T, 2T ) = T ℓ1 /2π +
O(l); 0 < λ ≤ 1 is fixed, L := λl, X := eL = (T /2π)λ ; λ1 := L/ℓ1 = λ +O(1/l). I := [T, 2T ]. Λ
is von Mangoldt’s function, an := Λ(n)n−1/2 , yn := log n; sums over n, m are over prime powers
                                                                                           1
≤ X unless indicated. Fourier transforms are fb(τ ) := R f (u)eiτ u du, so that f ḡ = 2π
                                                         R                        R           R
                                                                                                fbgb
                                                     1                  1                 1
and f[  ∗ g = fbgb. For a zero ρ we write γρ := (ρ − 2 )/i = γ − i(β − 2 ), so that ρ = 2 + iγρ ,
| Im γρ | < 21 , and γρ ∈ R iff β = 21 . A ≪ B and A = O(B) mean |A| ≤ cB; unless said
otherwise implied constants are absolute or depend only on the fixed profile ϱ of §2.2. For a
Hermitian matrix R and θ ≥ 0, nθ+ (R) := #{i : λi (R) > θ} and n+ (R) := n0+ (R); ∥ · ∥ on
matrices is the operator norm on ℓ2 .

                       2. The explicit formula and the test family
2.1. Weil’s Hermitian form. For f ∈ Cc2 (R) put hf (z) := fb(z) = f (u)eizu du, an entire
                                                                               R
function with
           |hf (x + iy)| ≤ e|y|Λf min ∥f ∥1 , ∥f ′′ ∥1 |x + iy|−2 ,
                                                                 
(2.1)                                                                   supp f ⊂ [−Λf , Λf ],
by two integrations by parts (hf (z) = (iz)−2 f ′′ (u)eizu du and |eizu | = e−yu ≤ e|y|Λf on
                                                      R

supp f ). Since ρ mρ |γρ |−2 < ∞ and | Im γρ | < 12 , the series
                 P
                                    X
(2.2)                   W (f, g) :=    mρ hf (γρ ) hg (γρ )      (f, g ∈ Cc2 (R))
                                    ρ
                                           P
converges absolutely; here and below ρ runs over the distinct nontrivial zeros (of either sign
of γ) and the multiplicity is written explicitly. The multiset {(γρ , mρ )} is invariant under
γ 7→ γ̄ (i.e. ρ 7→ 1 − ρ̄; multiplicities agree because ξ(s̄) = ξ(s) = ξ(1 − s)) and under γ 7→ −γ.
The first symmetry shows that W is Hermitian: W (g, f ) = W (f, g).
   Define, for τ ∈ R and X = eL > 1, s := 12 + iτ ,
                                             1    Γ′  1 iτ  log π
(2.3)                             µ(τ ) :=     Re       +       −      ,
                                            2π     Γ 4      2      2π
               MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                              7

                                                  1         1    Xs − 1
(2.4)                            ΠX (τ ) :=               +   Re        ,
                                            2π( 14 + τ 2 ) π       s
                                              1 X Λ(n)
(2.5)                            PX (τ ) := −          √ cos(τ log n),
                                              π           n
                                                n≤X
(2.6)                                νX := µ + ΠX + PX .
Proposition 2.1 (Explicit formula, spectral form). Let f, g ∈ Cc2 (R) with supp f, supp g ⊂
[− L2 , L2 ]. Then
                              Z
(2.7)              W (f, g) =     hf (τ ) hg (τ ) νX (τ ) dτ, X = eL .
                                        R

   This is Weil’s explicit formula [Wei52] for the test function k = f ∗ g̃, g̃(u) := g(−u),
whose transform is hk (z) = hf (z)hg (z̄) and whose support lies in [−L, L], so that only prime
powers n ≤ X occur; the terms hk (± 2i ) coming from the pole of ζ have been rewritten as
the density ΠX . The derivation from the standard statement (e.g. [IK04, Theorem 5.12],
whose hypotheses—hk holomorphic in a strip | Im z| ≤ 12 + ϵ with hk (z) ≪ (1 + |z|)−1−δ
there—are satisfied since hk is entire and |hk (z)| ≤ eL| Im z| ∥f ′′ ∥1 ∥g ′′ ∥1 |z|−4 by (2.1); see also
[Wei52, Bom00]) and the check of all normalisations are given in Appendix A. We record the
elementary facts
                        µ is even, smooth, increasing in |τ |,    µ ≥ µ(0) > −1,
(2.8)                   µ(τ ) = 2π1
                                    log |τ |
                                        2π + O(τ
                                                 −2
                                                    ), µ′ (τ ) ≪ |τ |−1 (|τ | ≥ 1);
                                       √
                                      3 X                     1 X Λ(n)        √
(2.9)                   |ΠX (τ )| ≤           ;  |PX (τ )| ≤          √ ≪ X;
                                     1 + |τ |                 π        n
                                                                 n≤X
(2.10)
   Z 2T                                                          Z 2T
                       T ℓ1    1                                      T ℓ21          −2
                                                                                           
          µ(τ ) dτ =        +O     = N (T, 2T ) + O(l),                 µ(τ )2 dτ =
                                                                                1 + O l       .
    T                  2π       T                            T          4π 2
                                      ′
((2.8) is Stirling’s formula and Re ΓΓ (σ + it) = −γE + n≥0 n+1 1      n+σ
                                                          P                    
                                                                  − (n+σ)2 +t2 ; (2.10) follows
                        R 2T
from (2.8), (1.2) and T log2 2π τ
                                  dτ = T (ℓ21 + 1 − 2 log2 2).)
2.2. The test family. The pair-correlation scale 1/ log T enters through the support of the
window, not the argument of hf in (2.2): we take supp ϕ = [− L2 , L2 ] with L = λl, so that only
prime powers n ≤ X = eL = (T /2π)λ enter (2.7) and ϕb resolves at width ∼ 1/L (see (2.17); in
the sharp-cutoff case ϕ = 1[−L/2,L/2] , ϕ(r)
                                        b    = 2 sin(Lr/2)/r, cf. the remark after Lemma 2.2).
This is the packaging of [GG07, Lemma 1] together with the band-limit condition [GG07,
Lemma 2(v)] (restating [MO84, Lemma 2]); the support parameter δ there plays the role of
our L, up to the 2π in the Fourier convention.
   Fix once and for all a nondecreasing function ϱ ∈ C 3 (R) with ϱ = 0 on (−∞, 0] and ϱ = 1
on [1, ∞), and a ramp width w with
(2.11)                                        1 ≤ w ≤ L/8.
(The reader loses nothing by taking w = 1; we keep w free because the numerical illustrations
of §8 use ramps proportional to L.) Define the taper
                                         L/2 − |u| 
(2.12)                        ϕ(u) := ϱ               , u ∈ R.
                                             w
8                                                  CLAUDE

Then ϕ ∈ Cc3 (R) is even, 0 ≤ ϕ ≤ 1, supp ϕ = [− L2 , L2 ], ϕ = 1 on [− L2 + w, L2 − w], and
(2.13)
                           ∥ϱ′ ∥∞               2∥ϱ′′ ∥1                                         cϱ
  ∥ϕ′ ∥1 = 2,   ∥ϕ′ ∥∞ =          ,   ∥ϕ′′ ∥1 =            ,    ∥(ϕ2 )′ ∥1 = 2,     ∥(ϕ2 )′′ ∥1 ≤ ,
                             w                     w                                             w
where cϱ := 4∥ϱ′ ∥∞ + 4∥ϱ′′ ∥1 (≥ 4). Put
                          Z                  Z
                        1                  1                        2w
(2.14)             a :=       ϕ2 ,    b :=     ϕ4 ,            1−      ≤ b ≤ a ≤ 1,
                        L                  L                         L
and let
                                                                                  Z
(2.15)          c2 ,
           Φ := ϕ         g := ϕ2 ⋆ ϕ2 ,      Aϕ := ϕ ⋆ ϕ,        (v ⋆ v)(y) :=       v(u)v(u + y) du.

                                                             b2             2
R 2 ϕ and Φ are real, even, entire; ϕ(0) ≤ L, Φ(0) = aL; ϕ = Aϕ 2and Φ = gb on R;
Thus b                              b                               c
 R Φ = 2πg(0) = 2πbL; g and Aϕ are even, and since 1[−L/2+w, L/2−w] ≤ ϕ ≤ ϕ ≤ 1[−L/2,L/2] ,

(2.16)                  (L − 2w − |y|)+ ≤ g(y) ≤ Aϕ (y) ≤ (L − |y|)+ .
Integrating by parts and using (2.13),
                                                          2   cϱ 
(2.17)           max |ϕ(r)|,
                      b      |Φ(r)|       ≤ ψ(r) := min L,    ,                   (r ∈ R),
                                                           |r| wr2
and a direct computation (split at |r| = 2/L and |r| = cϱ /2w; note cϱ L/4w ≥ 1 by (2.11))
gives
(2.18) Z
          ∞                                 Z                                      Z
                              cϱ L                 2                 cϱ L
Ψ0 :=       ψ(r) dr = 4+2 log      ≪ log L,    ψ(r) |r| dr = 8+8 log      ≪ log L,    ψ 2 ≤ 8L.
        0                     4w             R                       4w             R

   Let h := 2π/L, d := ⌊T /h⌋ = ⌊LT /2π⌋, and
(2.19)
 τk := T + kh (k ∈ Z),       fk (u) := ϕ(u)e−iτk u          (0 ≤ k < d),     V := span{f0 , . . . , fd−1 }.

Then τ0 , . . . , τd−1 ∈ [T, 2T ), hfk (z) = ϕ(z
                                               b − τk ), and since ϕb is real on R we have ϕ(z̄)
                                                                                              b     = ϕ(z).
                                                                                                       b
We define the d × d matrices
                                   X                                 Z
           Gkl := W (fk , fl ) =             b ρ − τk ) ϕ(γ
                                        mρ ϕ(γ          b ρ − τl ) =      b − τk )ϕ(τ
                                                                          ϕ(τ       b − τl ) νX (τ ) dτ,
                                    ρ                                  R
(2.20)
                      1
              Ge := G,
                      L
the two expressions agreeing by Proposition 2.1. The second expression shows that G is real
symmetric. (So does the first: conjugation permutes the summands via ρ 7→ 1 − ρ̄.) For c ∈ Cd
            P                                     P
and fc := k ck fk ∈ V one has hfc (z) = k ck ϕ(z        b − τk ) and
                                 X                X
(2.21)                  c∗ G c =     c̄k Gkl cl =   mρ hfc (γρ )hfc (γρ ) = W (fc , fc ),
                               k,l             ρ

i.e. G is the matrix of the Hermitian form W |V in the coordinates c.
Lemma 2.2 (Poisson summation for the Gabor system). For all τ, τ ′ ∈ R,
                X                                                   X
K∞ (τ, τ ′ ) :=           b ′ − τk ) = L Φ(τ − τ ′ ),
                  b − τk )ϕ(τ
                  ϕ(τ                                 in particular     b − τk )2 = aL2 .
                                                                        ϕ(τ
               k∈Z                                                                 k∈Z
             MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                          9


Proof. Fix τ, τ ′ and let Υ(s) := ϕ(τ      b ′ − s). With ϕτ (u) := ϕ(u)eiτ u and H := ϕτ ∗ ϕτ ′ ∈
                                    b − s)ϕ(τ
Cc (R) one checks directly that Υ(s) = H(−s);
                                           b      hence Υ is smooth, Υ(s) = O(|s|−4 ) by (2.17),
and by Fourier inversion
                     Z                                    Z
                                                        ′                       ′
           Υ(ξ)
            b      = H(−s)e
                        b       iξs
                                    ds = 2πH(ξ) = 2π eiτ ξ ϕ(u)ϕ(ξ − u)ei(τ −τ )u du,

which is continuous, bounded by 2π(L − |ξ|)+ , and vanishes for |ξ| ≥ L because supp ϕ =
[− L2 , L2 ]. The Poisson summation formula k∈Z Υ(T + kh) = h−1 m∈Z Υ(−2πm/h)e          2πimT /h
                                            P                        P   b
holds for such Υ (both Υ and Υ     b are O((1 + | · |)−2 )), and 2πm/h = mL, so only m = 0
                                −1                                 ′
                                          L
                                            · 2π ϕ(u)ϕ(−u)ei(τ −τ )u du = LΦ(τ − τ ′ ), ϕ being
                                                R
contributes: the sum equals h Υ(0) = 2π
                                   b
even.                                                                                         □
  Thus the Gabor system at the critical density h = 2π/L has a translation-invariant frame
kernel with no aliasing error, for any window supported in an interval of length L; this replaces
the Shannon sampling identity for the sinc system (ϕ = 1[−L/2,L/2] , Φ(x) = sin(Lx/2)/(x/2)).
Remark 2.3 R(Why we do not orthonormalise; heuristic, not used). The Gram matrix Mkl :=
⟨fk , fl ⟩L2 = ϕ2 e−i(k−l)hu du is L times the d × d Toeplitz matrix with symbol ϕ2 (Lt/2π), t ∈
[−π, π). This symbol takes all values in [0, 1], so by Szegő’s theorem about (2w/L)d eigenvalues
of M/L lie well below 1 and the smallest are extremely small; M is not L(Id+o(1)) in operator
norm, and the matrix M −1/2 GM −1/2 of W |V in an orthonormal basis is badly conditioned.
None of this matters: the positive index of a Hermitian form is independent of coordinates,
and the other tools we use (the rank–trace inequality, Weyl’s inequality and Cauchy–Schwarz
on eigenvalues) require only a Hermitian matrix. We therefore work throughout with G    e = G/L
                                       d                        2
in the coefficient coordinates c ∈ C with the standard ℓ structure; M plays no role. Two
alternatives leading to the same theorems are described in Remark 7.1.

                              3. Lemmas from linear algebra
   For a Hermitian form Q on a finite-dimensional complex vector space U the positive index
n+ (Q) is the maximal dimension of a subspace on which Q is positive definite; by Sylvester’s
law of inertia it equals the number of positive eigenvalues of any matrix representing Q, and
for a Hermitian matrix R we have n+ (R) = n+ (c 7→ c∗ Rc).
Lemma 3.1 (Inertia under pull-back). Let Q be a Hermitian form on Cm and A : U → Cm a
linear map from a finite-dimensional complex vector space. Then n+ (Q ◦ A) ≤ n+ (Q), where
(Q ◦ A)(u) := Q(Au).
Proof. If Q ◦ A is positive definite on a subspace U0 ⊂ U , then A|U0 is injective (a kernel vector
u ̸= 0 would give Q(Au) = 0) and Q is positive definite on A(U0 ), so dim U0 = dim A(U0 ) ≤
n+ (Q).                                                                                          □
  No injectivity of A, no independence assumption and no inner product on U is needed. We
shall also use the subadditivity of the positive index: for Hermitian forms Q1 , Q2 on the same
space, n+ (Q1 + Q2 ) ≤ n+ (Q1 ) + n+ (Q2 ) (apply the lemma to the pull-back of Q1 ⊕ Q2 under
the diagonal map u 7→ (u, u)).
Lemma 3.2 (Rank–trace inequality). Let P, Q be Hermitian d × d matrices with P ⪰ 0,
rank P ≤ r, and n+ (Q) ≤ b. Then for every c > 0,
                                                 c2
                          ∥P + Q∥2F ≥ c tr P −      r + 2c tr Q − c2 b ;
(3.1)                                             4
                in particular (c = 2)     r ≥ 2 tr P + 4 tr Q − 4b − ∥P + Q∥2F .
10                                              CLAUDE

Equality holds if P = 2c Π1 , Q = c Π2 with orthogonal projections Π1 ⊥ Π2 of ranks r and b.
Proof. Write Q = Q+ − Q− with Q± ⪰ 0, Q+ Q− = 0, rank Q+ ≤ b. Then ∥P + Q∥2F =
∥P ∥2F + ∥Q+ ∥2F + ∥Q− ∥2F + 2 tr(P Q+ ) − 2 tr(P Q− ), and tr(P Q+ ) ≥ 0. Let p1 ≥ p2 ≥ · · · ≥ 0
and n1 ≥ n2 ≥ · · · ≥ 0 be thePeigenvalues of P and Q− (so pi = 0 for i > r). By von Neumann’s
trace inequality tr(P Q− ) ≤ i pi ni , hence
                                     X
  ∥P ∥2F − 2 tr(P Q− ) + ∥Q− ∥2F ≥      (pi − ni )2
                                         i
                                       X                  c2  X 2           c2
                                   ≥         c(pi − ni ) −     + ni ≥ c tr P − r − 2c tr Q− ,
                                                           4                  4
                                       i≤r                      i>r

using x2 ≥ cx − c2 /4 for real x and −cniP
                                         ≥ −2cnP      2
                                                 i , ni ≥ 0 ≥ −2cni . Finally Q+ has k ≤ b
nonzero eigenvalues qj > 0 and ∥Q+ ∥2F =   qj2 ≥ (2cqj − c2 ) ≥ 2c tr Q+ − c2 b. Adding, and
using tr Q = tr Q+ − tr Q− , gives (3.1). The equality case is immediate.                          □
   With c = 2 the elementary  P inequality used is x2 ≥ 2x − 1, i.e. (x − 1)2 ≥ 0; applied to integer
multiplicities it is the step   mρ ≥ 2N − N s in Montgomery’s deduction of simple zeros from
                                  2
P 2 4
   mρ ≤ 3 N . Lemma 3.2 transplants this step to eigenvalues, von Neumann’s inequality paying
for the interaction between P and the negative part of Q. Applied with the simple zeros alone
on the rank side (Proposition 4.4(i)) it yields also the next level m2 ≥ 3m − 2. Taking Q = 0
and optimising c recovers rank P ≥ (tr P )2 /∥P ∥2F .
Lemma 3.3 (Thresholded Cauchy–Schwarz count). Let R be a Hermitian d × d matrix and
θ ≥ 0 with tr R > θd. Then
                                                   (tr R − θd)2
                                        nθ+ (R) ≥               .
                                                      tr(R2 )
                                                         P             P
Proof. Let λ1 , . . . , λd be the eigenvalues and S := λi >θ λi . Since λi ≤θ λi ≤ θ #{i : λi ≤
θ} ≤ θdP (negative       eigenvalues only help), S ≥ tr R − θd > 0. By Cauchy–Schwarz, S 2 ≤
n+ (R) λi >θ λi ≤ nθ+ (R) tr(R2 ).
 θ              2                                                                             □

Lemma 3.4 (Weyl). Let A, E be Hermitian d × d matrices and θ ≥ ∥E∥. Then nθ+ (A + E) ≤
n+ (A).
Proof. With eigenvalues in decreasing order, λi (A + E) ≤ λi (A) + ∥E∥ for every i (Courant–
Fischer). Hence λi (A + E) > θ ≥ ∥E∥ forces λi (A) > 0, and the number of such i is at most
n+ (A).                                                                                   □

                           4. The zero side: signature and rank
     Fix
(4.1)                       D0 := T 1/2 ,       I ′ := (T − D0 , 2T + D0 ],
and split the sum (2.20) over distinct zeros according to whether the ordinate γ = Re γρ lies
in I ′ :
(4.2)                   X
G = A+E,        Akl :=          b ρ −τk )ϕ(γ
                            mρ ϕ(γ        b ρ −τl ),    E := G−A,      Ae := A/L, E
                                                                                  e := E/L.
                        ρ: γ∈I ′

Since ρ and 1 − ρ̄ have the same ordinate, both index sets are invariant under ρ 7→ 1 − ρ̄, so A
and E are real symmetric (same argument as for G).
             MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                         11

4.1. Block structure. Let Z(I ′ ) be the set of distinct zeros with γ ∈ I ′ . Classify its points
as follows:
    S1 : β = 21 and mρ = 1 (simple zeros on the line); s1 := #S1 ;
    S2 : β = 12 and mρ ≥ 2; s2 := #S2 ;
     P: unordered pairs {ρ, 1 − ρ̄} with β ̸= 12 (both members lie in Z(I ′ ), they are distinct
         points, and m1−ρ̄ = mρ ); p := #P.
Thus #Z(I ′ ) = s1 + s2 + 2p and, counting with multiplicity,
                                          X        X           X
(4.3) N (I ′ ) := N (T − D0 , 2T + D0 ) =    1+        mρ +          2mρ ≥ s1 + 2s2 + 2p.
                                                ρ∈S1   ρ∈S2   {ρ,1−ρ̄}∈P

             (I ′ ) :=                                  ′          ′
                         P
  Write Non              ρ∈S1 ∪S2 mρ , so that also N (I ) ≥ Non (I ) + 2p. Besides G = G/L we use
                                                                                    e
the normalisation
(4.4)                     Gb := G ,    b := A ,
                                       A             Eb := E ,
                                aL 2        aL 2           aL2
in which, by Lemma 2.2, an isolated on-line zero seen through the full grid k ∈ Z would
contribute the eigenvalue exactly mρ .
Proposition 4.1. (i) n+ (A)e ≤ s1 +s2 +p and rank(A)    e ≤ s1 +s2 +2p = #Z(I ′ ). (ii) A
                                                                                        b = P +Q
                                                                    ′
with P, Q real symmetric, P ⪰ 0, rank P ≤ s1 + s2 , tr P ≤ Non (I ), and n+ (Q) ≤ p.
Proof. For z ∈ C let ℓz : Cd → C, ℓz (c) := k ck ϕ(z
                                           P       b − τk ) = hf (z). Exactly as in (2.21),
                                                                  c
                                   X
                          c∗ A c =        mρ ℓγρ (c) ℓγρ (c)   (c ∈ Cd ).
                                    ρ∈Z(I ′ )

For ρ ∈ S1 ∪ S2 we have γρ ∈ R and the summand is mρ |ℓγρ (c)|2 . For a pair {ρ, ρ∗ } ∈ P,
ρ∗ = 1 − ρ̄, we have γρ∗ = γρ , mρ∗ = mρ , and the two summands together equal
                                                                                
                    mρ ℓγρ (c)ℓγ̄ρ (c) + ℓγ̄ρ (c)ℓγρ (c) = 2mρ Re ℓγρ (c)ℓγ̄ρ (c) .
Hence c∗ Ac = Q(Ac), where A : Cd → Cs1 +s2 +2p is the evaluation map c 7→ (ℓγρ (c))ρ∈Z(I ′ )
and Q is the orthogonal direct sum of the 1 × 1 forms mρ |x|2 (ρ ∈ S1 ∪ S2 ) and of the 2 × 2
                                           0 m 
forms (x, y) 7→ 2mρ Re(xȳ), of matrix mρ 0ρ and signature (1, 1) (one for each pair in P).
So n+ (Q) = s1 + s2 + p, and Lemma 3.1 gives the first claim of (i); the second holds because
A is a sum of #Z(I ′ ) matrices of rank one. Dividing by L > 0 changes nothing.
   For (ii) let P := (aL2 )−1 ρ∈S1 ∪S2 mρ uρ uT                                      d
                               P
                                                 ρ with uρ := (ϕ(γρ − τk ))k<d ∈ R (real, as
                                                                 b
γρ ∈ R), and Q := A   b − P , the sum of the pair contributions. P is real symmetric, positive
semidefinite, of rank ≤ s1 + s2 , and by Lemma 2.2 tr P = (aL2 )−1 mρ 0≤k<d ϕ(γ    b ρ − τ k )2 ≤
                                                                    P     P

(aL2 )−1 mρ k∈Z ϕ(γ   b ρ − τk )2 = Non (I ′ ). The form c 7→ c∗ Qc is the pull-back under A of
          P     P

the direct sum of the p hyperbolic blocks of Q alone, so n+ (Q) ≤ p by Lemma 3.1; Q = A   b− P
is real symmetric.                                                                              □
   The argument is indifferent to coincidences or near-dependences among the functionals ℓz
(an on-line zero and an off-line pair at the same height; a pair very close to the line, for which
ℓγ and ℓγ̄ nearly coincide): Lemma 3.1 needs no independence. It is also indifferent to the
depth |β − 12 | of the zeros in Z(I ′ ): A is a finite sum and is used exactly. In the zero-side
expansion of ∥A∥b 2 the self-pair term for a pair of depth |β − 1 | is ≍ X |2β−1| (Remark 5.10), so
                   F                                            2
no termwise bound on that expansion is available unconditionally; this is why the proof reads
  b 2 from the prime side (§5) and uses only rank and positive index here.
∥G∥ F
12                                           CLAUDE

4.2. The tail.
Proposition 4.2. Let A0 ≥ 1 be an absolute constant such that N (t+1)−N (t) ≤ A0 log(t+3)
for all t ≥ 0. Then for T ≥ T0 ,
                                            log(4T )                         2∥ϱ′′ ∥1
                  e ≤ θ0 := 4A0 C 2 X 1/2
                 ∥E∥             1                   ,     C1 := ∥ϕ′′ ∥1 =            ,
                                              D02                              w

so that θ0 ≤ 32A0 ∥ϱ′′ ∥21 l T λ/2−1 ≪ l T λ/2−1 . Moreover the trace norm satisfies ∥E∥
                                                                                      b 1 ≤
θ0 /(aL) ≤ 2θ0 /L.
Proof. The existence of A0 is classical [Tit86, Theorem 9.2]. For a distinct zero ρ = β + iγ with
γ∈/ I ′ put y := β − 12 ∈ (− 12 , 21 ) and uρ := (ϕ(γ
                                                  b ρ − τk ))0≤k<d ∈ Cd . Since E = P ′ mρ uρ uT
                                                                                     γ ∈I
                                                                                       /        ρ
and ∥uuT ∥ = ∥u∥22 ,
                                                  X
(4.5)                                     ∥E∥ ≤       mρ ∥uρ ∥22 .
                                                / ′
                                              γ ∈I

     b ρ − τk ) = ϕb (γ − τk ) − iy , and by (2.1) (with f = ϕ, Λf = L/2, |y| < 1 ) |ϕ(r
                                  
Now ϕ(γ                                                                              b − iy)| ≤
                                                                                2
 L/4  ′′          −2       1/4    −2
e ∥ϕ ∥1 |r − iy| ≤ X C1 r for real r ̸= 0. Let D := dist(γ, I) ≥ D0 . The points τk ,
0 ≤ k < d, lie in I with spacing h = 2π/L, so
                           X                                L D−3 
       ∥uρ ∥22 ≤ C12 X 1/2     |γ − τk |−4 ≤ C12 X 1/2 D−4 +    ·      ≤ C12 X 1/2 L D−3
                                                             2π    3
                        0≤k<d
                                                    −3 (zeros counted with multiplicity). Zeros
                                        P
(as D ≥ 1, L ≥ 2). It remains to bound γ ∈I/ ′ mρ D
with γ >P2T + D0 : grouping them into γ ∈ (2T + D0 + j, 2T + D0 + j + 1], j ≥ 0, this part is
at most j≥0 A0 log(2T + D0 + j + 4)(D0 + j)−3 ≤ 32 A0 log(4T )D0−2 for T large (split at j = T
and use D0 ≥ 2). Zeros with 0 < γ < T − D0 contribute likewise at most 32 A0 log(4T )D0−2 ,
and zeros with γ ≤ 0 have D ≥ T and contribute at most j≥0 A0 log(j + 4)(T + j)−3 ≪
                                                               P

T −2 log T . Altogether γ ∈I        −3 ≤ 4A log(4T )D −2 for T ≥ T , and (4.5) gives ∥E∥ ≤
                        P
                           / ′ mρ D        0           0             0
                       −2                           ′′
4A0 C1 X L log(4T )D0 = Lθ0 . Finally C1 ≤ 2∥ϱ ∥1 as w ≥ 1, X 1/2 ≤ T λ/2 , log(4T ) ≤ 2l
       2  1/2

and D02 = T . The trace-norm bound follows from the same chain, since ∥uuT ∥1 = ∥u∥22 as well,
and a ≥ 21 .                                                                                 □

Remark 4.3. Only ϕ′′ ∈ L1 was used (r−2 decay of ϕb off the real axis). For the sharp cut-off
                                b − iy)| ≍ X |y|/2 /|r| for generic r, and the right-hand side
ϕ = 1[−L/2,L/2] one has only |ϕ(r
of (4.5) is then ≫ X 1/2 l log(T /D0 ), which is not o(l) for any D0 = T 1−ε : some tapering is
necessary. Conversely any D0 with T λ/4+ε ≤ D0 ≤ T 1−ε would do below.
4.3. The counting inequalities.
Proposition 4.4. (i) 3s1 + 4s2 + 4p ≥ 4 tr A             b 2 . Consequently, by (4.3), (ii) s1 ≥
                                                   b − ∥A∥
                                                            F
     b − 2N (I ′ ) − ∥A∥
4 tr A                b 2 (and a fortiori the same for s1 + s2 ), and (iii) s1 + s2 + p ≥ 1 4 tr A
                                                                                                 b−
                        F                                                                   2
     ′        2                                       ′
                 
N (I ) − ∥A∥
           b
              F (and a fortiori the same for #Z(I ) = s1 + s2 + 2p); hence

            N0∗ (T, 2T ) ≥ 4 tr G      b 2 − 2N (T, 2T ) − O θ0 L−1 (1 + ∥G∥
                                                                                           
                                 b − ∥G∥                                       b F ) + D0 l ,
                                          F

             N0s (T, 2T ) ≥ 4 tr G     b 2 − 2N (T, 2T ) − O θ0 L−1 (1 + ∥G∥
                                                                                           
(4.6)                            b − ∥G∥                                       b F ) + D0 l ,
                                          F

             Nd (T, 2T ) ≥ 21 4 tr G      b 2 − N (T, 2T ) − O θ0 L−1 (1 + ∥G∥
                                                                                             
                                    b − ∥G∥                                      b F ) + D0 l .
                                             F
               MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                                 13

Proof. Regroup the decomposition of Proposition 4.1(ii) (notation uρ , A as in its proof) as
b = P1 + Q′ , where P1 := (aL2 )−1 P
A                                                  T
                                          ρ∈S1 uρ uρ collects the simple on-line zeros only and
Q′ := Ab − P1 the multiple on-line zeros together with the pairs. Then P1 is real symmetric,
P1 ⪰ 0, rank P1 ≤ s1 , and tr P1 = (aL2 )−1                  b ρ −τk )2 ≤ s1 by Lemma 2.2 (each
                                            P       P
                                                    ρ∈S1    ϕ(γ
                                                             0≤k<d
mρ = 1); and c 7→ c∗ Q′ c is the pull-back under A of the direct sum of the s2 positive forms
mρ |x|2 (ρ ∈ S2 ) and the p hyperbolic blocks, so n+ (Q′ ) ≤ s2 + p by Lemma 3.1. Lemma 3.2
with c = 2, r = s1 , b = s2 + p and tr Q′ = tr A
                                               b − tr P1 gives

          b 2F ≥ 2 tr P1 − s1 + 4(tr A
         ∥A∥                         b − tr P1 ) − 4(s2 + p) ≥ 4 tr A
                                                                    b − 3s1 − 4s2 − 4p,

which is (i). For (ii), 4s2 + 4p = 2(s1 + 2s2 + 2p) − 2s1 ≤ 2N (I ′ ) − 2s1 ; for (iii), 3s1 + 4s2 + 4p =
2(s1 + s2 + p) + (s1 + 2s2 + 2p) ≤ 2(s1 + s2 + p) + N (I ′ ). For (4.6): A      b=G    b−E b with | tr E|
                                                                                                        b ≤
∥E∥
  b 1 and ∥A∥ b F ≤ ∥G∥ b F + ∥E∥ b F ≤ ∥G∥ b F + ∥E∥ b 1 , so Proposition 4.2 gives 4 tr A   b − ∥A∥b 2 ≥
                                                                                                         F
     b − ∥G∥
4 tr G        2            −1
           b − O(θ0 L (1 + ∥G∥      b F )) (as θ0 /L ≤ 1); finally s1 + s2 ≤ N (T, 2T ) + N (I ′ \ I),
                                                                                     ∗
              F                                                                      0
s1 ≤ N0s (T, 2T ) + N (I ′ \ I), #Z(I ′ ) ≤ Nd (T, 2T ) + N (I ′ \ I), and N (I ′ ) = N (T, 2T ) + N (I ′ \ I)
with N (I ′ \ I) ≪ D0 l.                                                                                    □

   In (i) each simple on-line zero is charged 3 = 22 − (2 − 1)2 and every other distinct on-line
point or off-line pair 4 = 22 : this is the eigenvalue form of the integrality step m2 ≥ 3m − 2,
i.e. (m − 1)(m − 2) ≥ 0, obtained from Lemma 3.2 by placing the simple zeros on the rank
side (where x2 ≥ 2x − 1 is sharp at x = 1) and the multiple ones on the index side (where
the flat charge 4 is sharp at x = 2). The underlying matrix inequality is an equality for
P1 + Q′ = diag(1, . . . , 1, 2, . . . , 2) (s1 ones, s2 + p twos). Note that Lemma 3.2 is not scale-
invariant: it must be applied in the units (4.4), in which tr P1 ≤ s1 ; and that nothing is assumed
about the traces of the individual pair blocks in Q′ (which, after truncation to 0 ≤ k < d, may
be far from 2mρ for deep pairs near the ends of I): only tr Q′ = tr A−tr b    P1 and n+ (Q′ ) ≤ s2 +p
enter.

Proposition 4.5. For every θ ≥ θ0 ,

(4.7)                             e − N (I ′ )
                      s1 ≥ 2 nθ+ (G)                   and       #Z(I ′ ) ≥ nθ+ (G).
                                                                                 e

Consequently, with N (I ′ \ I) := N (T − D0 , T ) + N (2T, 2T + D0 ) ≪ D0 l,

                            e − N (T, 2T ) − 2N (I ′ \ I),
(4.8) N0s (T, 2T ) ≥ 2 nθ+ (G)                                                          e − N (I ′ \ I).
                                                                     Nd (T, 2T ) ≥ nθ+ (G)

Proof. By Lemma 3.4 (with G       e = A        e ∥E∥
                                           e + E,    e ≤ θ0 ≤ θ) and Proposition 4.1, nθ (G)         e ≤
                                                                                                +
    e ≤ s1 + s2 + p. By (4.3), s2 + p ≤ (N (I ′ ) − s1 ). Hence nθ (G)
n+ (A)                                              1                             e ≤ (s1 + N (I ′ )),
                                                                                          1
                                                    2                           +         2
                                                  θ
which is the first inequality; the second is n+ (G)   e ≤ n+ (A) e ≤ rank A e ≤ #Z(I ′ ). For (4.8) note
s1 ≤ N0s (T, 2T ) + N (I ′ \ I), N (I ′ ) = N (T, 2T ) + N (I ′ \ I), #Z(I ′ ) ≤ Nd (T, 2T ) + N (I ′ \ I),
and N (I ′ \ I) ≪ D0 l by N (t + 1) − N (t) ≤ A0 log(t + 3).                                             □

   Inequalities (4.7) hold for every locally finite multiset of points in the strip 0 < β < 1 that
is invariant under ρ 7→ 1 − ρ̄ and satisfies N (t + 1) − N (t) ≪ log(t    √+ 3); they contain no
arithmetic. With the trace asymptotics of §5 they lead, for λ ≥ 3 − 6, to weaker constants
than Proposition 4.4(ii),(iii); Proposition 4.5 carries the F (λ) branch of Theorem C for smaller
λ and the n+ -statements of §§7.5 and 8. All the arithmetic is in the trace asymptotics, to
which we now turn.
14                                               CLAUDE

                               5. The prime side: magnitude
   In this section the zeros play no role: tr G
                                              e and tr Ge2 = P G     e2
                                                                 k,l kl are computed from the
second expression in (2.20). The computation is Montgomery’s [Mon73] (in the form given to
it in [BGSTB24, GS26]), transcribed to the kernel Φ2 = gb of Lemma 2.2; we give it in full
because we need the error terms for our specific finite family, including the effect of the taper
and of truncating the Gabor system to 0 ≤ k < d.

5.1. Arithmetic and analytic inputs.

Lemma 5.1. For x ≥ 2,
(5.1)
                                                                            √
 X                  X Λ(n) √                             X       Λ(n)         x        X
     Λ(n) ≪ x,        √ ≤ 3 x (x ≥ x0 ),                       √         ≪       ,           Λ(n)2 ≪ x log x,
                        n                                        n log n   log x
n≤x                 n≤x                                  n≤x                           n≤x
(5.2)
   X Λ(n)2         (log x)2                    X Λ(n)2                             (log x)3
                                                                                            + O (log x)2 .
                                                                                                        
               =            + O(log x),                        (log x − log n) =
           n          2                                  n                            6
     n≤x                                       n≤x
                                       P
Proof. The bounds (5.1) follow from       n≤x Λ(n) ∼ x by partial summation. For (5.2),
           2
P                   P
   n≤x Λ(n) /n =      n≤x Λ(n) log n/n + O(1) (the two P
                                                         differ only at proper prime pow-
ers), and partial summation from Mertens’ formula        n≤x Λ(n)/n   = log x + O(1) gives
P                     1    2
                                                                Rx P          2
                                                                                 
   n≤x Λ(n) log n/n = 2 log x + O(log x). The second formula is 1     n≤t Λ(n) /n dt/t. See
[MV07, §2.2].                                                                            □

Lemma 5.2 (Montgomery–Vaughan). Let λ1 , . . . , λR be distinct real numbers, δr :=
mins̸=r |λr − λs |, and xr , zr ∈ C. Then
                          X x r zs            3π X |xr |2 1/2 X |zr |2 1/2
                                          ≤                                    .
                           λr − λ s            2  r
                                                     δr          r
                                                                    δr
                          r̸=s

Proof. For z = x this is the weighted (“generalised”) Hilbert inequality of Montgomery and
Vaughan [MV74, Theorem 2]; see also [Mon94, Chapter 7]. Any absolute constant in place of
3π
 2 would suffice below. In general, let H be the Hermitian matrix with entries i/(λr − λs ) off
                                               1/2
the diagonal and 0 on it, and ∆ := diag(δr ). The case z = x says |y ∗ (∆H∆)y| ≤ 3π    2
                                                                                  2 ∥y∥2 for
all y, i.e. ∥∆H∆∥ ≤ 3π                                   ∗            −1 ∗          −1
                     2 since ∆H∆ is Hermitian; hence |x Hz| = |(∆ x) (∆H∆)(∆ z)| ≤
3π     −1      −1
 2 ∥∆ x∥2 ∥∆ z∥2 .                                                                        □

   We apply this with {λr } = {log n : n ≤ X a prime power}; consecutive prime powers n < n′
satisfy log(n′ /n) ≥ log n+1   1
                          n ≥ 2n , so

                                              X a2             X
(5.3)                       δn−1 ≤ 2n,               n
                                                         ≤2          Λ(n)2 ≪ XL.
                                                    δn
                                              n≤X              n≤X

   We shall use the following pointwise bound for νX . By (2.8), (2.9) and (5.1), for T ≥ T0 ,
(5.4)                                                                     √
                      |τ |
 |νX (τ )| ≤ B + log+ 4T   (τ ∈ R), |νX (τ )| ≤ B (|τ | ≤ 4T ), B := l + 4 X, B 2 ≪ l2 + X.
              MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                                     15

5.2. The trace.
                                                  √
Proposition 5.3. tr G   e = aL N (T, 2T ) + O(L X). In particular tr G      e = L N (T, 2T ) 1 +
O(w/L + T λ/2−1 ) and tr G/d
                    
                            e = ℓ1 (1 + o(1)).

                                                       b − τk )2 νX (τ ) dτ =: Gµ + GΠ + GP
                                                     R
Proof. We have L tr G e = P
                               k<d Gkk and Gkk =       ϕ(τ                      kk     kk      kk
according to (2.6).
              b 2 dr = 2π ϕ2 = 2πaL. For |r| ≤ τk /2, |µ(τk + r) − µ(τk )| ≪ |r|/T by (2.8),
           R                R
   µ-part. ϕ(r)
           2                                                              b 2 ≤ c2 /(w2 r4 ) and
     R
and ϕ(r)
       b     |r| dr ≪ log L by (2.17)–(2.18); for |r| > τk /2 ≥ T /2, ϕ(r)         ϱ
|µ(τk + r) − µ(τk )| ≪ l + log(2 + |r|). Hence Gµkk = 2πaLµ(τk ) + O(log L/T ) and
    X µ               X                             Z 2T
        Gkk = 2πaL       µ(τk ) + O(L log L) = aL2      µ + O(Ll) = aL2 N (T, 2T ) + O(L2 l),
    k<d              k<d                                        T

where we used that µ is positive and increasing on [T − h, 2T ], so that the Riemann sum
                           R 2T
satisfies h d−1
           P
              k=0 µ(τk ) = T µ + O(h µ(2T )) (recall T < T + dh ≤ 2T < T + (d + 1)h), together
with (2.10).
   P -part. Since ϕb 2 = A                 b − τk )2 cos(τ y) dτ = 2πAϕ (y) cos(τk y), so
                                         R
                         cϕ with Aϕ even, ϕ(τ

                        X                  X                            d−1
                                                                         X         
                              GPkk = −2            an Aϕ (yn ) Re eiT yn
                                                                             eikhyn .
                        k<d               n≤X                              k=0

For y ∈ [log 2, L) we have hy/2 = πy/L ∈ (0, π) and | k<d eikhy | ≤ | sin(πy/L)|−1 ≤
                                                                 P
L/(2 min(y, L − y)), while 0 ≤ Aϕ (y) ≤ min(L, L − y) by (2.16) (and Aϕ (L) = 0). Hence        √
Aϕ (yn )| k eikhyn | ≤ L2 /(2 log 2) for every n, and | k GPkk | ≤ (L2 / log 2) n≤X an ≪ L2 X.
         P                                             P                        P
                                        √
             By (2.9), |ΠX (τ )| ≤ 6 X/T for√|τ − τk | ≤ T /2,√ and ϕ(τ       b − τk )2 |ΠX (τ )| ≤
 √Π-part.                                                                   −3 ) and
3 Xc2ϱ /(w2 |τ − τk |4 ) otherwise; so |GΠ                                                   Π
                                                                                     P
   √                                       kk | ≤ 6 X 2πaL/T + O( XT                  k<d |Gkk | ≪
L2 X.                                         √                   √
                e = aL2 N (T, 2T ) + O(L2 X + L2 l), and l ≤ X for T ≥ T0 (λ). The last two
   Adding, L tr G
claims follow from 1 − 2w/L ≤ a ≤ 1, LN ≫ LT l, d = LT /2π + O(1) and (1.2).                      □

5.3. Reduction of tr Ge 2 to a double integral over I × I. Put
                    X                                          X
(5.5) K(τ, τ ′ ) :=   ϕ(τ      b ′ −τk ),
                      b −τk )ϕ(τ            Kout := K∞ −K =                                          b ′ −τk ),
                                                                                              b −τk )ϕ(τ
                                                                                              ϕ(τ
                  0≤k<d                                                           k∈Z\[0,d)

so that K∞ = LΦ(τ − τ ′ ) by Lemma 2.2. From (2.20),
                              X        ZZ
(5.6)           L2 tr Ge2 =     G2kl =     K(τ, τ ′ )2 νX (τ )νX (τ ′ ) dτ dτ ′ ,
                                  k,l<d               R2

the interchange being justified by absolute convergence (|K(τ, τ ′ )| ≤ k ψ(τ − τk )ψ(τ ′ − τk ),
                                                                       P
ψ(r) ≪ r−2 , and (5.4)). By Cauchy–Schwarz and Lemma 2.2,
(5.7)                                                                              Z
              X              1/2 X             1/2
        ′                   2            ′      2          2                ′
 |K(τ, τ )| ≤     ϕ(τ − τk )
                  b                   ϕ(τ − τk )
                                      b                = aL ,      |K∞ (τ, τ )| ≤ L ϕ2 = aL2 ,
               k∈Z                     k∈Z
                                                    X
                              |Kout (τ, τ ′ )| ≤             ψ(τ − τk )ψ(τ ′ − τk ).
                                                   k∈[0,d)
                                                    /
16                                               CLAUDE

Lemma 5.4 (End effects). For T ≥ T0 ,
                                                            ZZ
      e 2 = M + O L l log l (l2 + X) ,                                 Φ(τ − τ ′ )2 νX (τ )νX (τ ′ ) dτ dτ ′ .
                                    
   tr G                                           M :=
                                                                 I×I
                                                       2 νν ′ +E +E with ν := ν (τ ), ν ′ := ν (τ ′ ),
                                             RR
Proof. Write the right-hand side of (5.6) as I×I K∞             1   2             X           X
E1 := I×I (K − K∞ )νν and E2 := (I×I)c K νν ′ ; note I×I K∞
              2      2    ′                         2                   2 νν ′ = L2 M.
      RR                                RR                      RR

   Bound for E1 . By (5.7), |K 2 − K∞ 2 | = |K                        2                 ′
                                              out | |K + K∞ | ≤ 2aL |Kout |, and |ν|, |ν | ≤ B on I
by (5.4). Hence
                                             X Z                    2
                                       2 2
                             |E1 | ≤ 2L B              ψ(τ − τk ) dτ .
                                              k∈[0,d)
                                               /        I

For k = −j (j ≥ 1) we have dist(τkR, I) = jh; for k = d + 1 + j (j ≥ 0) we have τk ≥ 2T + jh
                                     ∞
because T + (d + 1)h > 2T . Since ∆ ψ ≤ min(Ψ0 , cϱ /(w∆)) ≤ min(Ψ0 , cϱ /∆) for ∆ > 0, we
get
     X Z                   2                X                cϱ 2             6cϱ Ψ0
               ψ(τ − τk ) dτ ≤ 2(2Ψ0 )2 + 2       min Ψ0 ,            ≤ 10Ψ20 +              ≪ L log L,
             I                                                  jh                     h
    k∈[0,d)
     /                                        j≥1
                          2
                                                                               R
where the term 2(2Ψ0 ) accounts for k = d, d+1 (for which we only use R ψ = 2Ψ0 ), the points
τd+1+j , j ≥ 1, being at distance ≥ jh to the right of I; the j-sum was split at j = cϱ /(hΨ0 ),
and (2.18) was used. Thus |E1 | ≪ L3 B 2 log L. R
                                                                  2    ′     Using K 2 ≤ aL2 |K| ≤
                                                       R
  Bound for E2 . By symmetry |E2 | ≤ 2 τ ∈I         /    τ ′ ∈R K |νν |.
L2 k<d ψ(τ − τk )ψ(τ ′ − τk ),
   P

                           X Z                          Z                                 
              |E2 | ≤ 2L 2
                                  ψ(τ − τk )|νX (τ )| dτ         ψ(τ ′ − τk )|νX (τ ′ )| dτ ′ .
                          k<d   τ ∈I
                                  /                               R

In the second factor, the range |τ ′ − τk | ≤ 2T has |τ ′ | ≤ 4T and contributes at most 2Ψ0 B; on
|τ ′ − τk | =: r > 2T we have |τ ′ | ≤ 2r, |νX (τ ′ )| ≤ B + log(r/T ) and ψ(r) ≤ cϱ r−2 , contributing
≪ B/TR. So the second factor is ≤ 3Ψ0 BPuniformly in k. The sum over k of the first factor
equals τ ∈I / |νX (τ )|σ(τ ) dτ with σ(τ ) :=     k<d ψ(τ − τk ). For τ ∈  / I let ∆ := dist(τ, I); the
numbers |τ − τk |, 0 ≤ k < d, are ≥ ∆, ≥ ∆ + h, ≥ ∆ + 2h, . . . in increasing order, and ψ is
decreasing, so
                                     1 ∞
                                      Z
          X                                                L          cϱ                           dcϱ
σ(τ ) ≤       ψ(∆+jh) ≤ ψ(∆)+               ψ ≤ ψ(∆)+         min Ψ0 ,      ,    σ(τ ) ≤ d ψ(∆) ≤ 2 .
                                     h ∆                  2π           ∆                             ∆
          j≥0
                                                                                L
                                                                                   cϱ + cϱ log 2TcϱΨ0 ≤
                                                          R                                         
On ∆ ≤ 2T (where |τ | ≤ 4T , |νX | ≤ B) this gives |νX |σ ≤ 2B Ψ0 + 2π
  R ∞ 0 + cϱ L log T ); on ∆ > 2T (where |τ | ≤R 2∆, |νX (τ )| ≤ B + log(∆/T2)) it gives ≤
2B(Ψ
2 2T dcϱ (B+log(∆/T ))∆−2 d∆ ≪ cϱ LB. Hence τ ∈I           / |νX |σ ≪ BLl and |E2 | ≪ L ·Ψ0 B·BLl ≪
  3   2
L B l log L.
    Together, L2 tr G e 2 = L2 M+O(L3 B 2 l log L); divide by L2 and use B 2 ≪ l2 +X, log L ≤ log l
(as λ ≤ 1).                                                                                             □
5.4. Evaluation of M. For functions u1 , u2 on I write
                                   ZZ
                    M[u1 , u2 ] :=      Φ(τ − τ ′ )2 u1 (τ )u2 (τ ′ ) dτ dτ ′ ,
                                           I×I

a symmetric bilinear form (Φ2 is even), so that
(5.8) M = M[µ, µ] + M[PX , PX ] + 2M[µ, PX ] + 2M[µ, ΠX ] + 2M[PX , ΠX ] + M[ΠX , ΠX ].
              MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                             17

Recall R Φ2 = 2πbL, R Φ(x)2 |x| dx ≪ log L (by (2.17), (2.18)) and, by Fourier inversion of
         R               R

Φ2 = gb (g even, continuous, compactly supported),
                            Z
(5.9)                          Φ(x)2 eixy dx = 2πg(y)  (y ∈ R).
                                    R
                                         R 2T                       bLT ℓ21
Proposition 5.5. M[µ, µ] = 2πbL T µ2 + O(l2 log L) =                         1 + O(l−2 ) + O(l2 log L).
                                                                                          
                                                                      2π
               ′                   ′                ′
Proof. For τ, τ ∈ I, µ(τ ) = µ(τ ) + O(|τ − τ |/T ) by (2.8), and 0 < µ ≤ l on I. Hence
                        Z          Z                           l ZZ                       
                               ′ 2                          ′
            M[µ, µ] = µ(τ )                      2
                                             Φ(x) dx dτ + O                 Φ(x)2 |x| dx dτ ′ .
                         I             I−τ ′                       T I R
The error is O(l log L). In the main term, I−τ ′ Φ2 = 2πbL − x<T −τ ′ Φ2 − x>2T −τ ′ Φ2 , and
                                                  R                     R                R
      ′ 2             2      ′       2             2                     2
R         R                            R
 I µ(τ ) x<T −τ ′ Φ(x) dx dτ ≤ l x<0 Φ(x) min(|x|, T ) dx ≪ l log L, similarly for the other
piece. The second form follows from (2.10).                                                            □
                                         T X Λ(n)       2                           TL  3       w 
Proposition 5.6. M[PX , PX ] =                            g(log n) + O(L2 X) =              1+O        +
                                         π            n                              6π           L
                                          n≤X
O(L2 X).
                                                                                                   ′
                          1 P
                               an (niτ +n−iτ ). Then PX (τ )PX (τ ′ ) = 2π1 2 Re n,m an am niτ m−iτ +
                                                                                P         
Proof. Write PX (τ ) = − 2π  n
       ′
niτ miτ . Substituting τ = τ ′ + x and noting that for fixed x the variable τ ′ ranges over
I ∩ (I − x), which is empty for |x| ≥ T and equals [T + x− , 2T − x+ ] for |x| < T
(x± := max(±x, 0)), we obtain
(5.10)
               1    X         Z T          hZ 2T −x+  n iτ ′      Z 2T −x+
                                                                                   ′
                                                                                        i
                                                                 ′
 M[PX , PX ] = 2 Re     an am         2 ix
                                  Φ(x) n                       dτ +          (nm)iτ dτ ′ dx
              2π    n,m        −T            T +x−    m              T +x−

               =: D + O1 + O2 ,
where D collects the terms n = m of the first inner integral, O1 the terms n ̸= m of the first
inner integral, and O2 all terms of the second.
   D. For n = m the first inner integral is T − |x|, so by (5.9) and n a2n ≪ L2 (Lemma 5.1),
                                                                      P

       1 X 2                      Z                            T X
D= 2           an T · 2πg(yn ) + O    Φ(x)2 (|x| + T 1|x|>T ) dx =          a2 g(yn ) + O(L2 log L),
      2π n                                                          π n n
using |x|>T Φ2 ≤ Φ2 |x|/T .
       R             R
               R 2T −x+       ′                                                                  2
   O2 . Here | T +x− (nm)iτ dτ ′ | ≤ 2/ log(nm) ≤ 2/ log 4 for all n, m, so |O2 | ≤ 2π1 2
                                                                                          P
                                                                                            n an    ·
         2
2πbL · log 4 ≪ XL by (5.1).
                                                                                               +
   O1 . For n ̸= m put ϑ := yn − ym ̸= 0. The first inner integral equals (n/m)i(2T −x ) −
                                                                                 
             −                          +
(n/m)i(T +x ) /(iϑ), and nix (n/m)−ix equals mix for x > 0 and nix for x < 0, while
             −
nix (n/m)ix equals nix for x > 0 and mix for x < 0. With
                  Z T                          Z 0
                                         −
             +
           αn :=           2 ix
                       Φ(x) n dx,      αn :=        Φ(x)2 nix dx,    |αn± | ≤ πbL ≤ πL,
                    0                             −T
we therefore get
                     1      X    an am h n 2iT +      −
                                                               n iT
                                                                         +     −
                                                                                   i
             O1 =        Re                     (αm + α n ) −         (αn  + α m )  .
                    2π 2      i(yn − ym ) m                    m
                             n̸=m
18                                                  CLAUDE
                                                         P
This is a combination of four sums of the shape n̸=m xn zm /(yn − ym ) with {|xn |, |zn |} =
                                                                         +
{an , an |αn± |}; for instance the first is n̸=m (an n2iT )(am m2iT αm
                                            P
                                                                           )/(yn − ym ). By Lemma 5.2
and (5.3) each of the four is at most 3π                  2 /δ ≪ L2 X. Hence |O | ≪ L2 X.
                                                     P
                                           2 · πL  ·    a
                                                       n n n                          1
  Finally, by (2.16) and (5.2) (note a2n = Λ(n)2 /n),
(L − 2w)3                   X                          X                 X                    L3
             + O(L2 ) =          a2n (L − 2w − yn ) ≤       a2n g(yn ) ≤      a2n (L − yn ) =    + O(L2 ),
     6                        −2w
                                                                                              6
                        n≤Xe                             n≤X           n≤X

and (L − 2w)3 = L3 − 6wL2 + O(w2 L) with 1 ≤ w ≤ L/8, which gives the second form.             □
                                       √                        √
Proposition 5.7. M[µ, PX ] ≪ l X, M[µ, ΠX ] ≪ lL X, M[PX , ΠX ] ≪ LX and
M[ΠX , ΠX ] ≪ LX/T .
Proof. Let m(τ ′ ) := I Φ(τ − τ ′ )2 µ(τ ) dτ for τ ′ ∈ R. Then 0 ≤ m ≤ l · 2πbL, m is C 1 , and
                      R
differentiating under the integral and integrating by parts in τ ,
             Z                                                                 Z
m (τ ) = − µ(τ ) ∂τ Φ(τ −τ ) dτ = µ(T )Φ(T −τ ) −µ(2T )Φ(2T −τ ) + µ′ (τ )Φ(τ −τ ′ )2 dτ,
  ′ ′                          ′ 2                     ′ 2                 ′ 2
                                  
              I                                                                 I
                ′                        −1
         R             R 2                   R 2
 R that′ I |m |′ ≤ 2l′ Φ + T · O(TR ) ′ Φ ≪ lL. For y ≥ log 2, integrating by parts,
so
  I m(τ ) cos(τ y) dτ ≤ (2 sup |m| + I |m |)/y ≪ lL/y. Therefore
                                                                                √
                        1X
                                 Z
                                        ′       ′       ′
                                                              X an                X    √
        |M[µ, PX ]| =         an m(τ ) cos(τ yn ) dτ ≪ lL                  ≪ lL      =l X
                        π n        I                               log n          L
                                                              n≤X
                                          √                         √
by (5.1). RNext, on I we have |ΠX | ≤ 3 X/T , 0 < µ ≤ l, |PX | ≤ X (by (2.9), (5.1), T ≥ T0 ),
and supτ I Φ(τ − τ ′ )2 dτ ′ ≤ 2πbL; the remaining three bounds follow by inserting these sup
bounds into the definition of M[·, ·] (an integral over a region of τ ′ -length T ).           □
5.5. Summary.
Theorem 5.8. Let 0 < λ ≤ 1, L = λl, X = eL , 1 ≤ w ≤ L/8, and let G    e be the matrix (2.20).
Put
       w (l2 + X) log l                       w                               w log l
ET := +                 +T λ/2−1 , so ET ≪λ +T λ−1 log l (λ < 1), ET ≪ +               (λ = 1).
       L       Tl                             L                                L   l
Then for T ≥ T0 (λ), with implied constants depending only on ϱ,
                                          √                              
(5.11)         tr G
                  e = aL N (T, 2T ) + O(L X) = L N (T, 2T ) 1 + O(ET ) ,
                            Z 2T
                   2                  T X Λ(n)2
                                 µ2 +             g(log n) + O Ll log l (l2 + X)
                                                                                 
              tr G = 2πbL
                 e
                             T        π       n
                                                 n≤X
                           TL           L2 
                                 ℓ21 +
                                                          
(5.12)                 =                        1 + O(ET ) ,
                         2π          3
              (tr G)
                  e  2                                               L          2 log 2 − 1 
(5.13)                 = F (λ1 ) N (T, 2T ) 1 + O(ET ) ,       λ1 =      =λ 1−                  .
                  e2
               tr G                                                  ℓ1                ℓ1
In particular tr G             e 2 ∼ λl2 N (1 + λ2 /3) and (tr G)
                  e ∼ λlN , tr G                               e 2 / tr G
                                                                        e 2 ∼ F (λ)N , N = N (T, 2T ).

Proof. (5.11) is Proposition 5.3.√For (5.12)
                                        √ combine Lemma 5.4, (5.8) and Propositions 5.5–5.7:
the error terms l2 log L, L2 X, l X, lL X ≤ L(l2 + X), LX, LX/T are all O(Ll log l (l2 + X)).
For the second form use     Propositions 5.5 and 5.6, 1 − 2w/L ≤ b ≤ 1, l−2 ≤ w/L, and
Ll log l(l2 + X) T Lℓ21 ≪ (l2 + X) log l/(T l). For (5.13): by (1.2), N = T ℓ1 /2π + O(l), so
                        
              MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                              19

       L2 N 2      LT     ℓ21              
  TL 2        2
                 =    · 2     2
                                1 + O(l/T )
  2π (ℓ1 + L /3)
                   2π ℓ1 + L /3
                                     λ1       T ℓ1                                  
                                =      2    ·      1 + O(l/T ) = F (λ1 )N 1 + O(l/T ) ,
                                  1 + λ1 /3 2π
and the factors (1 + O(ET ))±2 from (5.11), (5.12) are absorbed. The bound for ET uses
X = (T /2π)λ .                                                                      □
Remark 5.9 (Effectivity). All constants are effective but the convergence is slow: at
finite T thePratio in (5.13) carries the exact taper factor a2 (1 + λ21 /3)/(b + λ21 JT ),
JT := 2L−3 n≤X a2n g(yn ) (→ 31 ), which for w = 1 equals 0.89 at L = 4.4 and 0.975 at
L = 16 and tends to 1 only like 1 − O(1/L), while O1 /D ≤ 6/(LJT ) requires L ≫ 18.
                  e 2 < F (λ)N at every computationally accessible height with w = 1 (cf. §8);
         e 2 / tr G
Thus (tr G)
Theorems A–C are statements about T → ∞.
Remark 5.10 (Consistency with Montgomery’s theorem). On the zero side, by (2.20) and
                                                         e = 1 P mρ P                     2
Lemma 2.2 (continued analytically in the shift), tr G                     k<d ϕ(γρ − τk ) ≈ aL N
                                                                                b
                                                              L    ρ
                                    e 2 = 12 P ′ mρ mρ′ P                         b ρ′ − τk ) 2 ≈
                                                                                              
for any configuration, and tr G                                      b ρ − τk )ϕ(γ
                                                                     ϕ(γ
                                            L    ρ,ρ             k<d
                           2
P
   ρ,ρ′ mρ mρ′ Φ(γρ − γρ′ ) (ordinates near I), aR Fejér-type pair-correlation sum at complex
differences γρ − γρ′ = −i(ρ − ρ′ ); since Φ(z)2 = g(u)eizu du with supp g ⊂ [−L, L], the sum-
          RL           ′        RX                ′
mand is −L g(u) e(ρ−ρ )u du = 1/X g(log x) xρ−ρ dx                     u
                                                     x : writing x = e , it is the weighted integral
       ′                                                          ′
of xρ−ρ over x ∈ [X −1 , X], X = eL = (T /2π)λ , i.e. the xρ−ρ of [BGSTB24, (1.2)] with x = T α ,
                                                                   sin 1 (γ−γ ′ )l 2
                                                                                      ∼ 43 N l2 , which is
                                                          P
|α| ≤ λ. For ϕ = 1, λ = 1 and under RH, (5.12) reads γ,γ ′ ∈I 1 2(γ−γ ′ )
               R1                                                Rλ 2
Montgomery’s −1 (1 − |α|)F (α) dα = 43 ; for general λ ≤ 1 it is −λ (λ − |α|)F (α) dα = λ + λ3 /3.
Theorem 5.8 is the statement that this evaluation holds for the prime-side expression regardless
of where the zeros are, which is also the content of [BGSTB24, Theorem 1] and of [GS26,
Lemma 2] (attributed there to Aryan [Ary22]).

                             6. Proofs of Theorems A, B and C
   Fix 0 < λ ≤ 1, take w := 1 in (2.11) (so L ≥ 8 once T ≥ T0 (λ)), D0 = T 1/2 as in
(4.1), and θ := θ0 from Proposition 4.2. Let ET be as in Theorem 5.8; with w = 1 we have
ET′ := ET ≪λ (log l)/l, and ET′ ≪λ 1/l if λ < 1. Write N := N (T, 2T ).
Proof of Theorem A. In the units (4.4), tr G   b = tr G/(aL)
                                                      e              b 2 = tr G
                                                               and ∥G∥         e 2 /(aL)2 . By Propo-
                            √                                           F
               b = N + O( X/a) = N (1 + O(T λ/2−1 )) (note that the taper constant a cancels).
sition 5.3, tr G
                            e 2 = T L bℓ2 + L2 (1 + O(E ′ )) (Propositions 5.5, 5.6 with w = 1) and
                                               
By (5.12) in the form tr G        2π     1   3          T
b ≤ a ≤ 1, a−2 = 1 + O(1/L),
                           2
  b 2 ≤ T             2 L
                  
                                       ′
                                             N ℓ1 LT             ′
                                                                         1 λ1 
                                                                                       N 1+O(ET′ ) ,
                                                                                                   
∥G∥  F          2
                    aℓ1 +       1+O(E  T )  =      +         1+O(E  T )  =     +
          2πLa            3                      L    6π                    λ1 3
using N = T ℓ1 /2π + O(l) and LT /2π = λ1 N (1 + O(l/T )). In particular ∥G∥    b F ≪ N 1/2 , so the
error term in (4.6) is O(lT λ/2−1 N 1/2 + T 1/2 l) = O(N T −1/2 ). Proposition 4.4 now gives
                                1      λ1 
          N0∗ (T, 2T ) ≥ 4N −                N − 2N − O(ET′ N ) = H(λ1 ) − O(ET′ ) N.
                                                                                     
                                      +
                                  λ1     3
Since λ1 = λl/(l+c0 ) with c0 = 2 log 2−1 < 1, the identity H(λ)−H(λ1 ) = cλl0 − λ−λ
                                                                                  3
                                                                                    1
                                                                                      ≤ cλl0 < λl
                                                                                               1

gives H(λ1 ) ≥ H(λ) − 1/(λl), which proves the first assertion (as l ≍ log T ). The lim inf over
20                                             CLAUDE

[T, 2T ] follows at λ = 1, and the statement for N0∗ (T )/N (T ) by summing over dyadic intervals:
given ε > 0 choose T1 with N0∗ (t, 2t) ≥ ( 32 − ε)N (t, 2t) for t ≥ T1 ; for T ≥ 2T1 and J
maximal with T 2−J ≥ T1 , N0∗ (T ) ≥ Jj=1 N0∗ (T 2−j , T 2−j+1 ) ≥ ( 32 − ε) N (T ) − N (T 2−J ) ≥
                                        P                                                       

( 32 − ε)N (T ) − Oε (1).                                                                         □

Proof of Theorem B. By thesecond line of (4.6) and the estimates in the proof of Theorem A,
N0s (T, 2T ) ≥ 4N − λ11 + λ31 N − 2N − O(ET′ N ) = H(λ1 ) − O(ET′ ) N ; the rest is as in that
proof, and N s ≥ N0s .                                                                          □
                                       √
Proof of Theorem C. For λ ≥ 3 − 6: by the third line of (4.6) and the estimates in          the
proof of Theorem A, Nd (T, 2T ) ≥ 12 4 − λ11 − λ31 − 1 N − O(ET′ N ) = Hd (λ1 ) − O(ET′ ) N ≥
                                                      √
 Hd (λ) − O(ET′ ) N , since Hd′ = 12 H ′ . For λ < 3 − 6: by Proposition 4.2, θ0 ≪ lT λ/2−1 , and
                  
                        e = ℓ1 (1 + o(1)) ≫ l, so tr G
by Proposition 5.3, tr G/d                              e > θ0 d for T ≥ T0 (λ) and θ0 d/ tr G
                                                                                             e≪
T λ/2−1      ′
         ≤ ET . Lemma 3.3 and (5.13) give
                             e − θ0 d)2
                         (tr G                e 2
                                          (tr G)      θ 0 d 2
           nθ+0 (G)                                            = F (λ1 ) N 1 + O(ET′ ) ,
                                                                                      
(6.1)            e ≥                    =          1−
                                e2
                             tr G             e2
                                           tr G       tr Ge
and the second inequality in (4.8), with N (I ′ \ I) ≪ T 1/2 l ≪ N T −1/2 and F ′ (x) = (1 −
x2 /3)/(1 + x2 /3)2 ∈ (0, 1] on [0, 1], 0 ≤ λ − λ ≤ 1/l, gives N (T, 2T ) ≥ F (λ ) − O(E ′ ) N ≥
                                                 1              d               1         T
 F (λ) − O(ET′ ) N . This proves the first assertion; for the lim inf take λ = 1 (first case) and
                
sum dyadically as in the proof of Theorem A.                                                    □
Remark 6.1. The endpoint λ = 1 is admissible in Theorem 5.8 because all secondary terms
are O(X log l/(T l)) = o(1) relative to the main terms even for X ≍ T . A reader who prefers
to keep a power saving everywhere may take λ < 1 fixed and let λ → 1− ; the limits 23 , 23 , 56
are unaffected.

                           7. Variants, extensions, and remarks
7.1. The optimal window: Montgomery–Taylor. Nothing in Sections 4–5 used that ϕ
is flat-topped, only: ϕ ∈ Cc2 even, 0 ≤ ϕ ≤ 1, supp ϕ = [− L2 , L2 ], ϕ nonincreasing in |u| (so
∥ϕ′ ∥1 ≤ 2, ∥(ϕ2 )′ ∥1 ≤ 2), and ∥ϕ′′ ∥1 , ∥(ϕ2 )′′ ∥1 ≪ 1. For such a window put, with g = ϕ2 ⋆ ϕ2
as before,
                             Z                    Z                  Z L
                           1                   1                   2
(7.1)                 a :=     ϕ2 ,      b :=         ϕ4 ,   J := 3      g(y) y dy.
                           L                   L                  L 0
Then Propositions 5.3–5.7 hold verbatim, except that the last step of Proposition R5.6 is replaced
                                                                                    L
by partial summation from (5.2): since |g ′ | ≤ ∥(ϕ2 )′ ∥1 ≤ 2, n≤X a2n g(yn ) = 0 g(y) y dy +
                                                               P
           3
O(L2 ) = L2 J + O(L2 ). Consequently (5.13) becomes
                   e 2
               (tr G)      λ 1 a2                    1   (l2 + X) log l           
                                                                              λ/2−1
(7.2)                  =           N (T, 2T )   1 + O    +                + T          ,
                   e2
                tr G     b + λ21 J                     L         Tl
with an implied constant depending on the window only through the norms listed. Writing
ϕ2 (u) = v(u/L) with v on [− 12 , 21 ], the constant is the scale-free functional
                                                  R 2
                                               λ v
(7.3)             cλ (v) := R 2           RR                              (v ≥ 0),
                               v + λ2         |s − s′ | v(s)v(s′ ) ds ds′
              MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                            21

and cλ (1) = F (λ). Maximising (7.3) is a Cauchy–Schwarz problem for the positive definite
                               R 1/2
operator 1 + λ2 T , (T v)(s) = −1/2 |s − s′ |v(s′ ) ds′ ; the maximiser solves v + λ2 T v = const, i.e.
v ′′ + 2λ2 v = 0, and is
                                                                          √
             ∗
                         √                 1          ∗                     2 tan ϑ          λ
            vλ (s) = cos( 2λs) > 0 (|s| ≤ 2 ),       cλ := sup cλ (v) =              , ϑ= √ ;
                                                             v≥0         1 + ϑ tan ϑ          2
(7.4)                                              √
                                        2 tan(1/ 2)
                                c∗1 = √              √ = 0.7532960 . . .
                                        2 + tan(1/ 2)
(positivity of vλ∗ shows that the constraint v ≥ 0 is inactive). One recognises 1/c∗1 = 12 +
2−1/2 cot(2−1/2 ) = 1.3274992 . . ., the Montgomery–Taylor constant [Mon75, CG93], and v1∗ is
the Fourier transform of the Montgomery–Taylor test function: (7.3) is Montgomery’s func-
                                                v |2 .
                      R
tional K(0)/(K(0)
               b     + |α|K(α)
                           b       dα) for K = |b
                        N0∗ (T, 2T )       1    3 1             1                         N s (T, 2T )
Theorem D. lim inf                   ≥ 2− ∗ = − √ cot √ = 0.67250 . . ., lim inf 0                     ≥
                 T →∞ N (T, 2T )           c1   2       2        2                  T →∞ N (T, 2T )
      1                               Nd (T, 2T )        1       1
2 − ∗ = 0.67250 . . . and lim inf                   ≥       3 − ∗ = 0.83625 . . . .
     c1                          T →∞ N (T, 2T )         2       c1
                                                   √
Proof. Take λ = 1 and the window ϕ(u) := cos( 2 u/l)1/2 ϱ(L/2−|u|)√         (the optimal profile,
                                                                                             √ mol-
lified at the ends by the fixed-width ramp of §2.2); on the support cos( 2u/l) ≥ cos(1/ 2) > 0,
so ϕ has all the properties listed above, with ∥ϕ′′ ∥1 , ∥(ϕ2 )′′ ∥1 ≪ 1. Its constants (7.1) differ
from those of v1∗ by O(1/L), so (7.2) gives (tr G)            e 2 = c∗ N (T, 2T )(1 + O(log l/l)), and
                                                     e 2 / tr G
                                                                     λ1
cλ1 = c1 + O(1/l); likewise, in the units (4.4), tr G = N (T, 2T )(1 + O(T −1/2 )) (Proposition 5.3;
  ∗      ∗                                            b
                                      b 2 = tr G  e 2 /(aL)2 = N (T, 2T ) 1/c∗ + O(log l/l) , while
                                                                                              
Φ(0) = aL for any window) and ∥G∥        F                                     λ1
                                           P
Propositions 4.1(ii) and 4.4 used only k∈Z ϕ(τ    b − τk )2 = aL2 . The rest of Section 6 is un-
                                        ∗
changed, with H replaced by 2 − 1/c (hence Hd by 21 (3 − 1/c∗ )).                                    □
  By [CCLM17, Corollary 14] the Montgomery–Taylor kernel solves the one-delta extremal
problem when only the √values of Montgomery’s F (α) on [−1, 1] are used; since their extremal
function has vb = cos( 2 ·) > 0 it lies in our class, so Theorem D is the limit of the method
“block structure + two traces + primes up to T ”: no window does better.
7.2. Variants of the test family.
Remark 7.1. (i) Orthogonal Gabor systems. If the spacing is taken    P to be 2π/L0 with L0 :=
L − 2w < L and the window is chosen power-complementary, m∈Z ϕ2 (u + mL0 ) ≡ 1 (e.g.
ϕ = cos ϑ, ϕ(· − L0 ) = sin ϑ on the overlap of two consecutive ramps, as in the Princen–Bradley
or “sine” windows of signal processing), then ⟨fk , fl ⟩ = L0 δkl exactly, and G/L0 is literally the
matrix of W |V in an orthonormal basis. The whole argument goes through verbatim (with an
additional, harmless, aliasing term at frequency L0 in Lemma 2.2) and yields Theorems A and
C with λ replaced by λ0 = λL0 /L, hence the same limits.
   (ii) Orthonormalising the present family (heuristic; nothing here is used or claimed as
proved). As explained in Remark 2.3, M = LTd [ϕ2 (L · /2π)] has ≍ (w/L)d small eigenvalues.
Restricting W to the spectral subspace VS := {M ≥ L/2} (of dimension ≥ (1 − 4w/L)d) and
orthonormalising there, one can show that tr and tr2 of the resulting matrix RS agree with
tr G,
   e tr Ge 2 up to a factor 1 + O(w/L); the extra input is that the discarded eigendirections
carry a τ -density O(w/L) · L2 on I, so that by the mean value theorem for PX they see only
an O(w/L)-fraction of the traces. Since inertia is monotone under restriction, this route gives
22                                            CLAUDE

the same theorems. For the unrestricted matrix M −1/2 GM −1/2 , however, we cannot prove
the trace asymptotics: on eigendirections      of
                                               R M with eigenvalue Lϵ, ϵ very small, the Rayleigh
                        2 involves     b|2 PX / |fb|2 , for which we have only the pointwise bound
                                   R
quotient
   √      W (f, f )/∥f ∥             |f
O( X); controlling it would require bounds for PX on intervals of length ≍ 1/L, i.e. Lindelöf-
type information. This is why we avoid orthonormalisation altogether.
  (iii) Sharp cut-off. With ϕ = 1[−L/2,L/2] (the sinc system, for which Lemma 2.2 is Shannon’s
sampling formula and M = L Id exactly) Section 5 goes through with g(y) = (L − |y|)+ , but
Proposition 4.2 fails (Remark 4.3). A ramp of fixed width w = 1 is the minimal repair and
costs O(1/L).
7.3. Dirichlet L-functions. Let χ be a primitive character modulo q > 1, and let Nχ (T1 , T2 ),
         d,χ count the nontrivial zeros of L(s, χ) with T1 < γ ≤ T2 as in §1; Nχ (T, 2T ) =
   s , N
N0,χ
 T     qT
2π log 2π + O(T ).

Theorem E. Fix q and a primitive        χ mod q. For fixed 0 < λ ≤ 1 and T ≥ T0 (λ, q),
   ∗ (T, 2T ) ≥                                  s (T, 2T ) ≥
                                
N0,χ               H(λ) − o(1) Nχ (T, 2T ), N0,χ                   H(λ) − o(1) Nχ (T, 2T ) and
Nd,χ (T, 2T ) ≥ max(Hd (λ), F (λ)) − o(1) Nχ (T, 2T ); in particular at least ( 32 − o(1))Nχ (T, 2T )
                                         

of the zeros of L(s, χ) with T < γ ≤ 2T are on the critical line, at least ( 23 − o(1))Nχ (T, 2T )
are simple and on the line, and at least ( 65 − o(1))Nχ (T, 2T ) are distinct. Theorem D holds
likewise.
Proof. The proof is that of Theorems A–C with the following changes only. (i) Explicit formula:
                                                                   P
with κ = (1 − χ(−1))/2, Proposition 2.1 holds for Wχ (f, g) := ρ mρ hf (γρ )hg (γρ ) (zeros of
                                                                                   ′
                                                                 1
                                                                     log πq + Re ΓΓ 14 + κ2 + iτ2 ,
                                                                                                
L(s, χ)) with νX replaced by νX,χ := µχ + PX,χ , µχ (τ ) := 2π
PX,χ (τ ) := − π1 Re n≤X Λ(n)χ(n)n−1/2−iτ , and no pole term (ΠX ≡ 0); the derivation of
                    P

Appendix A applies to [IK04, Theorem 5.12] for L(s, χ). Since νX,χ is real, G is again real
symmetric. (ii) Zero side: the multiset of zeros of L(s, χ) is invariant under ρ 7→ 1 − ρ̄ with
multiplicities (functional equation χ ↔ χ̄ composed with L(s̄, χ) = L(s, χ̄)), all zeros have
0 < β < 1, and Nχ (t + 1) − Nχ (t) ≪q log(t + 3); Section 4 is otherwise verbatim. (iii)
Prime side: |Λ(n)χ(n)| = Λ(n)1(n,q)=1 , so Lemma 5.1 holds for these coefficients with Oq (·)
errors (finitely many primes removed); in Propositions 5.3, 5.6, 5.7 the coefficients an acquire
unimodular factors χ(n)n±i· , which leave the diagonal D unchanged (|χ(n)|2 = 1) and enter
                                                                        |
Lemma 5.2 and all other bounds only through |an |; µχ = 2π    1
                                                                log q|τ
                                                                     2π + O(τ
                                                                               −2 ) satisfies (2.8)–
                                       qT
(2.10) with ℓ1 replaced by ℓ1,χ := log 2π + 2 log 2 − 1, and λ1 = L/ℓ1,χ → λ as q is fixed.       □
  The unconditional records for an individual L(s, χ) obtained by Levinson’s method are of
the same size as for ζ (about 41.7% on the line, 40.7% simple, for log q = o(log T ) [Wu19]).
Remark 7.2 (Hybrid range and other degrees; heuristic). (i) The proof of Theorem E appears
to go through uniformly for q ≤ T ϑ provided X = (qT )Λ ≤ T 1−ϵ , i.e. with normalised
                                                                                √        band-
width Λ < 1/(1 + ϑ), giving the proportion H(1/(1 + ϑ)), positive for ϑ < 6/3; we have
not checked the uniformity of every error term and do not claim this. (ii) More generally, for
                                                                                          2
an L-function of degree m and analytic conductor q(T ) with n≤x |ΛF (n)|2 /n = mF log2 x +
                                                                P

O(log x) and n≤x |ΛF (n)|2 ≪ x1+o(1) , the formal outcome of Section 5 is ∥G∥  b 2 /NF ∼ 1/c,
                 P
                                                                                  F
    e 2 / tr G
(tr G)       e 2 ∼ c NF with c = Λ/(1 + mF Λ2 /3) (so the on-line proportion would be 2 − 1/c),
where Λ = L/ log q(T ) is the band-width in units of the mean spacing and the Montgomery–
Vaughan step forces X ≤ T 1−ϵ , i.e. Λ < Λ∗ := lim log T / log q(T ) (= 1/m in the t-aspect).
Since a2 ≤ b in (7.1), always c ≤ Λ∗ , so the method is non-vacuous (2 − 1/c > 0) only if
              MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                             23
          √
Λ∗ > 3 − 6 (for mF = 1) and in any case only if Λ∗ > 12 : it is a degree-one method. For an
individual GL(2) L-function (Λ∗ = 12 , mF = 1) one gets c = 13   6
                                                                   < 12 , i.e. nothing, whatever the
window. (iii) For families (e.g. all χ mod q, q → ∞) both counts commute with averaging in
the favourable direction (Lemma 3.2 is linear in tr and ∥ · ∥2F ), and orthogonality of characters
restores Λ∗ = 1 for the family average, as in [RS96]-type support computations; one expects
an averaged form of Theorem E with proportion 23 for q → ∞ and T as small as a power of
log q, but this requires a different (Gevrey-class) taper in Proposition 4.2Pand is not carried
out here. For Davenport–Heilbronn-type functions without Euler product, n≤x |c(n)|2 for the
coefficients of −F ′ /F grows like x1+δ (zeros in σ > 1), Proposition 5.6 fails, and the certificate
is empty.
Remark 7.3 (Zeros of ξ ′ ). Applied to the derivative ξ ′ of the completed zeta function in place
of ξ, the argument of §§4–6 gives, unconditionally,
                     s (T, 2T )
                    N0,ξ ′                                           Nd,ξ′ (T, 2T )
          lim inf                  ≥ 0.85838     and       lim inf                  ≥ 0.92919
          T →∞      Nξ′ (T, 2T )                            T →∞     Nξ′ (T, 2T )
                                                       7         51
(flat window; with the quartic window v(s) = 1 − 100     (2s)2 − 200 (2s)4 the constants become
0.86864 and 0.93432), where Nξ′ (T1 , T2 ) counts zeros ρ1 = β1 + iγ1 of ξ ′ with T1 < γ1 ≤ T2
                      s                                     1
with multiplicity, N0,ξ ′ those that are simple with β1 = 2 , and Nd,ξ ′ the distinct ones. The

comparanda are: unconditionally, Conrey [Con89] proved that at least 79.874% of the ze-
ros of ξ ′ are simple and on the critical line; assuming RH, Farmer, Gonek and Lee [FGL14,
Cor. 1.3] obtain > 85.84% simple by Montgomery’s method, and Chirre, Gonçalves and
de Laat [CGdL20, Cor. 7] obtain 0.8825 simple, 0.9412 distinct. The flat-window constant
85.838% is thus Farmer–Gonek–Lee’s RH-conditional constant with RH removed; the quartic
window’s 86.864% exceeds it and remains below the RH-conditional 0.8825. Note that for
zeros of ξ ′ merely on the critical line (without the simplicity), Wu [Wu15, §3] has 0.86957
unconditionally, which neither our 0.85838 nor our 0.86864 exceeds; the new content is the
simplicity. The argument is formalised in Lean alongside the main results (Appendix B.1;
Zeta23.XiPrime.xiDeriv simple on line and its quartic std form).
7.4. Relation to the work of Baluyot, Goldston, Suriajaya, and Turnage-
Butterbaugh. In the notation of [GS25, GS26], the unconditional “Fejér kernel sum
                           sin 2i (ρ−ρ′ ) log T 2
                                                   W (ρ − ρ′ ) = ( 34 + o(1)) 2π
                                                                              T
                      P
over zero differences” ρ,ρ′ i (ρ−ρ   ′ ) log T                                   log T ([GS26, Lemma 2],
                                   2
[Ary22], [BGSTB24, Theorem 1]) is, up to the choice of smoothing, the zero-side reading
of our tr G  e 2 at λ = 1 (Remark 5.10). Goldston and Suriajaya [GS25, Theorem 2] (see
also
P [GLSS25] under the pair correlation conjecture) show that an unconditional bound
   ρ,ρ′ ∈Z(T ), γ=γ ′ 1 ≤ (C + o(1))N (T ) with C < 2 (zeros repeated according to multiplicity)
would give proportions ≥ 2 − C of simple zeros and ≥ 2 − C of zeros on the line, and that
C = 34 would follow if the terms γ ̸= γ ′ of the Fejér sum could be discarded, which requires
a positivity that fails for zeros far from the line; in [BGSTB25, GS26] this is achieved under
the hypothesis that all zeros lie within o(1/ log T ) of the line. Theorems A and B are an
unconditional substitute which reaches their number 2 − C = 23 both for zeros on the line (as
distinct points) and for simple zeros on the line: instead of isolating the “horizontal diagonal”
γ = γ ′ termwise, Lemma 3.2 bounds the rank of the on-line (resp. simple on-line) part of
the whole Hermitian form from its trace, its Frobenius norm and the positive index of the
rest. For simple zeros on the line we thus obtain 2 − C = 23 unconditionally; this is the
constant that [GS25, Theorem 3(i)] gives under the hypothesis [GS25, (6.1)] on the diagonal
and symmetric-diagonal terms, and hence under the box hypothesis [GS25, Theorem 4],
24                                           CLAUDE

[GS26, Theorem 1]; for distinct zeros Theorem C gives 3−C      5
                                                         2 = 6 unconditionally, which is the
value of the average of the simple and critical proportions in [GS25, Theorem 3(ii)] and the
RH-conditional constant of [CGG98, (1.2)].
   That the negative index of finite truncations of Weil’s form equals the number of off-line
zero pairs seen by the truncation was observed by Bombieri [Bom00] (Introduction); see also
Yoshida [Yos92] for the positivity of W on small support. We are not aware of a previous use
of the positive index or of the rank in combination with a second-moment evaluation.

7.5. Limits of the method. (a) Dimension. rank P, nθ+ (G)           e ≤ d = λ1 N (1 + o(1)), so with
band-width λ ≤ 1 the ceiling of any argument of the present kind is 100% at λ = 1 and
nothing at λ ≤ 12 . The restriction λ ≤ 1 in turn comes from Proposition 5.6: for X ≫ T l the
off-diagonal terms O1 are no longer dominated by the diagonal, and their evaluation would
require information on prime pairs (the Hardy–Littlewood conjectures, or equivalently Mont-
gomery’s pair correlation conjecture for α > 1 [Mon73, GM87]). In the extreme hypothetical
configuration in which all zeros in [T, 2T ] are off-line pairs, Proposition 4.1 gives rank P = 0,
n+ (Q) ≤ N/2, while Lemma 3.2 would then force ∥A∥       b 2 ≥ 2N > 4 N ; the contradiction shows
                                                             F           3
only that at least two thirds of the zeros are not of this kind, which is what Theorem A says.
Nothing in the method distinguishes between “two thirds” and “all”.
   (b) Sharpness of the three counts. Given only tr, ∥ · ∥2F , the block structure and tr P1 ≤ s1 ,
Proposition 4.4 is sharp in all three parts: 32 N mutually orthogonal simple on-line zeros together
with 16 N on-line doubles realise tr = N , ∥ · ∥2F = 43 N , s1 = 23 N , Nd = 56 N —the same extremal
configuration as in Montgomery’s RH argument. Replacing the doubles by off-line pairs of
depth → 0 (spectrally the same) gives the extremal for Theorem A, with s1 + s2 = 23 N ; for
that configuration Proposition 4.4(ii) certifies exactly Theorem A’s 32 while (iii) is not sharp
(Nd = N ), consistent with §1.5.
   (c) The two levels of integrality. Lemma 3.2 with the decomposition (P, Q) of Proposi-
tion 4.1(ii) recovers the level (m − 1)2 ≥ 0; with the regrouping (P1 , Q′ ) of Proposition 4.4
it recovers also the level (m − 1)(m − 2) ≥ 0—interacting simple zeros, whose eigenvalues fill
(0, 2), are harmless because they sit on the rank side, where only rank P1 ≤ s1 and tr P1 ≤ s1
are used, while every multiple on-line point and every off-line pair sits on the index side at the
flat charge 4. This is the device of [CGG98, (1.2)] made unconditional. The Cauchy–Schwarz
route (Lemma 3.3, Proposition 4.5) stops at 2F (1) − 1 = 21 for simple zeros, since an off-line
pair costs two zeros in N for one   √ positive square; that route is retained only for the F (λ)
branch of Theorem C at λ < 3 − 6.
   What can still be varied is the family V , i.e. the window ϕ2 (§7.1), and the number of
moments used:
Proposition 7.4 (Cap). For any choice of window and any θ ≥ 0, rank P1 ≤ rank P ≤ d and
nθ+ (G)
     e ≤ d = λ1 N (T, 2T ) + O(1) (P1 as in the proof of Proposition 4.4); hence no argument
based on Proposition 4.1 with test functions supported in [− L2 , L2 ], L = λl, can certify more
                                                              b 2 ≥ (tr A)
than λ1 N (T, 2T ) on-line points, simple or not; and, since ∥A∥          b 2 /d, the certificate of
                                                                F
Proposition 4.4(ii) is at most (2 − 1/λ1 + o(1))N (T, 2T ) and hence non-positive for λ ≤ 12 .
   This is trivial but decisive in combination with the following observations, which we state
informally. (d) Lemma 3.3 is the case m = 1 of the one-sided Chebyshev–Markov–Stieltjes
bound: if the normalised moments d−1 tr(G/ℓ  e 1 )k , k ≤ 2m, are known, the sharp lower bound
for nθ+ (G)/d
         e    is 1 − Λm (0), Λm the Christoffel function of the moment sequence at 0. (e) The
prime-side evaluation of tr G e k by the diagonal method of Section 5 (multiplicative relations
              MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                             25

among k prime powers, Montgomery–Vaughan for the rest) is available exactly in the Rudnick–
Sarnak range kλ < 2 [RS96]; for λ ∈ ( 12 , 1) this allows at most k = 3 (and only for λ < 23 ), and
an odd moment does not lower Λ1 (0). Thus, unconditionally, higher moments add nothing to
the n+ -bound on ( 21 , 1) (and Proposition 4.4 uses only the first two in any case), while for λ ≤ 12 ,
where many moments are available, Proposition 7.4 makes them useless. (f) Conditionally, let
HL∗ (k0 , λ) denote the hypothesis that for all k ≤ k0 , tr G       e k = d ℓk mk (λ) + o(1) , where
                                                                                               
                                                                              1
mk (λ) is the k-th moment of the limiting spectral distribution of the sine-kernel Gram matrix
 sin πλ(xi −xj )
[ π(xi −x  j)
                 ] over the sine process (for kλ < 2 this is a theorem; for k = 4, λ > 12 it encodes a
                                                                        P
Hardy–Littlewood-type asymptotic for the additive correlations m (Λ∗Λ)(m)(Λ∗Λ)(m + h),
                                                                                             ∗
|h| ≤ X 2 /T ). One computes mk (1) = 1, 34 , 2, 13                               5
                                                      4 for k ≤ 4, so Λ2 (0; 1) = 36 and HL (4, λ) for
                                     s                       13
all λ < 1 would give lim inf N0 (T, 2T )/N (T, 2T ) ≥ 18 via the count of Proposition 4.5, and
HL∗ (k0 , λ) for all k0 and all λ < 1 would give proportion 1 (of simple zeros on the line), the
ceiling of Proposition 7.4; RH itself is out of reach of the mechanism. This is complementary
to [GLSS25], where the pair correlation conjecture with full support (all levels of correlation
being replaced by support beyond 1 at the pair level) yields 100% simple zeros on the line.
   (g) Distinct zeros under RH. Under the Riemann hypothesis, the third trace tr G         e 3 (equiva-
lently, the triple correlation of zeros in the band λ < 1) is available as a theorem [Hej94, RS96],
and the certificate of Proposition 4.4(iii) can be run with cubic weights ψ(m) = 21 m+ 18      1
                                                                                                 (2m2 −
m3 ) + 94 1m=1 : one checks ψ(m) ≤ 1 for all integers m ≥ 1 (equality at m = 1, 2, 3), while the
Schur–Horn majorisation applied to the admissible cubic f (x) = − 91 x2 + 18       1 3
                                                                                     x (the boundary
                                   2      3            2        3             1/2    1/2
                            P
case β = −2γ) gives i (2mi − mi ) ≥ 2 tr H − tr H for H = M ΓM                           ⪰ 0 (diagonal
                    P            1      1         2       3     4               k
mi ), so Nd ≥ i ψ(mi ) ≥ 2 N + 18 (2 tr H − tr H ) + 9 Ns . With tr H /N → mk (1, v) under
RH and the window v(s) = cos( 8s       5 )1|s|≤ 1 (for which 2m2 − m3 = 0.68524 . . .), together with
                                            2
Ns ≥ ( 19
       27 − o(1))N on RH [BHB13], this gives
                               Nd (T )   1 2m2 − m3 4 19
                     lim inf           ≥   +       + ·   = 0.85082 . . .
                      T →∞     N (T )    2    18    9 27
(cf. 0.8477 on RH from [CGdL20, Cor. 3]; from the correlation input alone, 12 + 12 (2m2 − m3 ) =
0.84262). The weight is optimal within span{m, m2 , m3 , 1m=1 } by linear programming; the
constants m2 , m3 are interval-certified from their closed forms.

                                   8. Numerical illustrations
   The results of this section are illustrative only; no theorem, proposition or lemma in §§2–7
or Appendix A depends on any computation reported here. The statements below illustrate the
finite identities and asymptotics of §§2–5 at small height. All heights involved lie far inside the
range where RH has been verified, so on the zero side G     e is positive semi-definite there and the
“certificates” certify nothing new; the point is (i) the agreement of the two expressions in (2.20),
                     e 2 / tr G
(ii) the size of (tr G)       e 2 relative to F (λ)N , and (iii) the behaviour of the inertia bound
on synthetic configurations. The computations use tapers with ramps of width w = ηL/2
proportional to L (Tukey/Hann-type or C 3 profiles), for which the constants of (2.14), (2.16)
                                                                    2
are a = 1 − 0.603η, b = 1 − 0.688η and JT := L23 n≤X Λ(n)                        1
                                                        P
                                                                  n g(log n) → 3 − (0.60 − 0.35η)η
                      1
(profile ϱ(x) = x − 2π  sin 2πx; the tabulated values below were computed with this profile, and
a reference script is available), so that the finite-T prediction                        e 2 / tr G
                                                                   of Theorem 5.8 is (tr G)       e2 ≈
       2        2                               2       2             2   −1                   2
                                                             
N λ1 a /(b + λ1 JT ) (cf. (7.2)); the factor a /(b + λ1 JT ) (1 + λ1 /3) is 1 − κη + O(η ) with
κ = κ(λ1 ) ≈ 0.24–0.28. In all tables N (·) is the Riemann–von Mangoldt main term and
C := (tr R)2 / tr R2 for the matrix R indicated.
26                                              CLAUDE

(1) Prime side = zero side. With νX computed from primes and Γ′ /Γ, and independently
G computed from the first 2000–3700 zeros via the first expression in (2.20), three independent
implementations (different tapers: Kaiser, Tukey, C 3 ) found maxk,l |Gprime
                                                                          kl    − Gzero
                                                                                     kl |/ max |G|
           −6              −8
between 10 and 1.1 · 10 on windows [100, 300], [600, 1200], [1000, 2000] with X ∈ [95, 106 ],
the residual being attributable to the truncation of the zero sum. For instance (I = [600, 1200],
Kaiser taper, L = log(600/2π) = 4.559, X = 95.5, d = 436): relative discrepancy 1.1 · 10−8 ;
C prime = 351.3, C zero = 351.4; N (I) = 472, C/N (I) = 0.744 (F (1) = 0.750); all 436 eigenvalues
positive (minimum 0.205).

(2) The ratio C/N from primes alone. Restricted/orthonormalised√ variant RS of Re-
mark 7.1(ii), Tukey taper (η = 0.2), short windows I = [T1 , T2 ], l = log( T1 T2 /2π); “law” is
F (λ); “cert” is (2C − N (I ′ ))/N (I) with I ′ the window enlarged by the numerical reach of the
atoms.
                   window           λ       L     X        d     C/N (I)      F (λ)     cert
                   [9000, 10000]  0.70 5.12        168    814       0.613     0.602     +0.18
                   [9000, 10000]  0.85 6.22        504    988       0.699     0.685     +0.36
                   [9000, 10000]  1.00 7.32       1510   1162       0.766     0.750     +0.50
                   [48000, 50000] 0.85 7.62       2033   2417       0.695     0.685     +0.37
                   [48000, 50000] 1.00 8.96       7797   2843       0.762     0.750     +0.51
                   [998000, 106 ] 0.85 10.18     26374   3229       0.691     0.685     +0.37
                   [998000, 106 ] 1.00 11.98    158996   3799       0.757     0.750     +0.50
We stress that these numbers, in particular the certificates +0.50, +0.51 at λ = 1, refer to
the orthonormalised variant RS and not to the matrix G   e of the proof, whose certificate at
comparable parameters is +0.40 to +0.42 (table (3)) and whose ratio C/N stays below F (λ)
at all accessible heights when w = 1 (Remark 5.9); the limiting value 2F (1) − 1 = 21 of this
certificate is notPvisible numerically. The excess of CRS /N over F (λ) here is the positive
O(1/L) term in n≤X Λ(n)2 g(log n)/n, partly offset by the taper factor 1 − κη and by λ1 < λ.

(3) The matrix G    e = G/L of the proof; taper dependence; trace-level check. T =
                                                          1
2000, I = [2000, 4000], l = 5.763, ramps ϱ(x) = x − 2π      sin 2πx of relative width η; G from
                                                        ′
3700 zeros (= prime side by (1)); N (I) = 1957, N (I ) = 2044 (D0 = 44.7). “RS ” is the re-
stricted variant with cut-off M ≥ L/2; “full” is M −1/2 GM −1/2 with numerically null directions
removed.
     λ      η     λmin (M/L)   #{eig(M/L) < 21 }/d    tapered law    CGe /N    certGe    CRS /N   Cfull /N
     0.9   0.20    2 · 10−12            0.121            0.665        0.651    +0.26      0.640    0.699
     0.9   0.10    1 · 10−10            0.061            0.688        0.676    +0.31      0.670    0.699
     0.9   0.05    7 · 10−9             0.030            0.699        0.687    +0.33      0.685    0.699
     1.0   0.10        —                 —               0.731        0.723    +0.40      0.718    0.745
     1.0   0.05        —                 —               0.741        0.734    +0.42      0.731    0.745

(Here d = 1650 resp. 1834, X = 179 resp. 318; “tapered law” is λa2 /(b + λ2 J(η)) with J(η) the
limit of JT ; F (0.9) = 0.7087.) The ill-conditioning of M is real but never reaches C. Trace-
level comparison of the prime-side prediction (main terms of Theorem 5.8 with the exact finite
                                    2
sums 2πa k µ(τk ) and Tπ n Λ(n)
            P                P
                                  n g(log n), kernel LΦ) with the zero-side value: λ = 0.9,
η = 0.1: Cpred = 1322.72 vs. Czero = 1322.28; λ = 1, η = 0.05: 1436.03 vs. 1436.41 (agreement
3 · 10−4 ), confirming simultaneously Lemma 2.2, the taper constants, and the negligibility of
end, off-diagonal, cross and Π terms at this height.
              MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                             27

(4) Exactly orthogonal system. Power-complementary window (RemarkP7.1(i)), λ = 0.9,
R = G/L0 , prime side only; “main” denotes the exact finite main terms (2π k µ(τk ) and the
exact diagonal), λ0 = (1 − η)λ.
       T      η      L0     d    T l/2π     tr R/main   tr R2 /main   (tr R)2 /(N tr R2 )   F (λ0 )
     2000 0.571 2.225 708         1834        0.9998      1.0000            0.371           0.368
     2000 0.150 4.409 1403        1834        1.0001      0.9994            0.667           0.640
      104 0.501 3.314 5274        11734       1.0000      0.9999            0.426           0.421
      104 0.150 5.640 8976        11734       1.0004      1.0007            0.662           0.640
(η = 0.571, 0.501 are 1/ log l.) The ratio column lies between F (λ0 ) and its 1/l-corrected value,
as (5.13) predicts.

(5) Synthetic configurations. The inequalities nθ+ ≤ s1 + s2 + p and 2C − N (I ′ ) ≤ s1 of
§4 hold for arbitrary ρ 7→ 1 − ρ̄-symmetric configurations; as a check of signs and conjugations
they were tested on the zero side (I = [600, 1200], λ = 1, d = 436, Kaiser taper) by replacing
true zeros by off-line pairs: e.g. all ordinates replaced by pairs of depth 10−4 , 0.2, 0.45 (so N
doubles, s1 = 0): n+ = 436, 420, 361 ≤ p = 511 and 2C − N (I ′ ) = −319, −358, −553 ≤ 0; half
of the ordinates paired at depth 0.05: n+ = 240 ≤ 256, 2C − N = −67 ≤ 0; 50% on-line plus
25% of heights paired: n+ = 364 ≤ 383, 2C − N = +22 ≤ s1 = 255. In no case does the
certificate exceed the truth, as Lemmas 3.1–3.4 dictate; pairing or multiplicity always lowers
C at fixed N (tr G  e is configuration-independent while tr G e 2 grows).
                                                                                         √
(6) The rank–trace certificate. Zero side from 105 zeros, T = 1000, I ′ = (T − T , 2T +
√
  T ] = (968.4, 2031.6], N (I) = 868, N (I ′ ) = 922, units (4.4), the same ramps: the certificate
     b − 2N (I ′ ) − ∥A∥
4 tr A                 b 2 of Proposition 4.4(ii) (which bounds s1 ) equals +0.49 N (I) (λ = 1,
                          F
η = 0.1; ∥A∥         b = 1.387 against the limit 4 ; the boundary term 2N (I ′ \ I) ≈ 0.12 N (I) is
            b 2 / tr A
              F                                    3
the O(D0 l) of (4.6), disproportionate at T = 103 , and the interior reading 4 − 2 − ∥A∥  b 2 / tr A
                                                                                            F
                                                                                                   b
is +0.613), +0.51 N (I) (η = 0.05) and +0.39 N (I) (λ = 0.9), against +0.380, +0.402, +0.286
for the Cauchy–Schwarz certificate 2(tr A)   b 2 /∥A∥b 2 − N (I ′ ) on the same data; on synthetic
                                                       F
configurations (all zeros doubled; every fourth ordinate replaced by a pair of depth 10−3 to
0.4; the near-extremal lattice with 23 on-line and 16 tight pairs; deep pairs in dephased couples)
the inequality of Proposition 4.4 held in every case, with slack 0.12N at the near-extremal
configuration (the finite-l excess 1.385 − 43 ). Lemma 3.2 itself was tested on 105 random and
300 adversarially optimised instances (aligned eigenvectors, cancelling large eigenvalues, near-
equality regime): no violation, minimal gap 0 attained exactly at the equality configurations.

                  Appendix A. The explicit formula: normalisations
   We derive Proposition 2.1 from the explicit formula in the following standard form ([IK04,
Theorem 5.12] specialised to ζ, valid for h holomorphic in | Im z| ≤ 12 + ϵ with h(z) ≪ (1 +
|z|)−1−δ there; [Wei52]; [Bom00]): let k ∈ Cc2 (R) and h(z) := k(u)eizu du (entire, with
                                                                       R

h(z) ≪k e| Im z|Λk (1+|z|)−2 by (2.1), so the hypotheses hold), so that k(u) = 2π
                                                                                1          −iru dr;
                                                                                  R
                                                                                    R h(r)e
then
               X                  i      i  X Λ(n)                            
                    mρ h(γρ ) = h      +h −     −      √ k(log n) + k(− log n)
                 ρ
                                    2         2          n
                                                  n≥1
(A.1)
                                    1
                                      Z      h Γ′  1 ir            i
                                +       h(r) Re       +      − log π dr,
                                   2π R          Γ 4      2
28                                                CLAUDE

                                                                                                −2
                                    P
the sum over ρ being limR→∞      |γ|<R (here absolutely convergent since h(r) ≪k (1 + |r|)
                                   Γ ′             Γ ′
on | Im r| ≤ 12 ). The bracket is ΓRR ( 12 + ir) + ΓRR ( 12 − ir) with ΓR (s) = π −s/2 Γ(s/2), and
equals 2πµ(r) by (2.3). (Consistency check: πµ = ϑ′ for the Riemann–Siegel theta function
ϑ(t) = Im log Γ( 41 + it2 ) − 2t log π, and N (T ) = π1 ϑ(T ) + 1 + S(T ), in accordance with (2.10).)
    Let f, g ∈ Cc2 (R) be supported in [− L2 , L2 ] and k := f ∗ g̃, g̃(u) := g(−u). Then k ∈ Cc2 (R)
(k ′′ = f ′′ ∗ g̃ is continuous), supp k ⊂ [−L, L], and h(z) = hf (z) b̃     g(z) = hf (z)hg (z̄), so the left
side of (A.1) R is W (f, R g) andR h(τ ) = hf (τ )hg (τ ) for real τ . We identify the three terms on the
right with h ΠX , hRPX , h µ respectively.
    Gamma term: it is hµ by the above.
                                           1
                                                 h(τ )(e−iτ y + eiτ y ) dτ = π1 h(τ ) cos(τ y) dτ , and also
                                              R                                   R
    Prime term: k(y) + k(−y) = 2π
k(± log n) = 0 for n > X = eL . Hence the prime term equals − π1 n≤X Λ(n)
                                                                             P             R
                                                                                       √
                                                                                         n
                                                                                             h(τ ) cos(τ log n) dτ =
R
  hPX .
                                                                                             RL
    Pole term: h( 2i ) + h(− 2i ) = k(u)(e−u/2 + eu/2 ) du = R k(u)e−|u|/2 du + −L k(u)e|u|/2 du,
                                      R                                R

using supp k ⊂ [−L, L] in the second integral. Since R e−|u|/2 e−iτ u du = ( 41 + τ 2 )−1 and,
                                                                     R
                         RL                               RL                   s̄               s
with s = 21 + iτ , −L e|u|/2 e−iτ u du = 2 Re 0 eus̄ du = 2 Re X s̄−1 = 2 Re X s−1 , inserting
           1
                 h(τ )e−iτ u dτ and interchanging (all integrals absolutely convergent) gives
              R
k(u) = 2π
                             i Z                                       Xs − 1 i
                   i                                                                   Z
                                                h       1        1
                 h      +h −       =      h(τ )                 + Re                dτ = h ΠX .
                     2          2       R         2π( 14 + τ 2 ) π         s
Adding the three identifications gives (2.7). Note that ΠX is a bounded smooth density: the
rank-two positive form f 7→ |hf ( 2i )|2 + |hf (− 2i )|2 has been traded, using the support condition,
                                      √
for an oscillatory density of size O( X/(1+|τ |)), which is negligible on I (Proposition 5.7) but
convenient because it makes the prime side a single integral. (As an independent check, not
used in the proof, the normalisations in (2.7) were confirmed numerically to 10−8 ; see §8(1).)

                       Appendix B. Formal and symbolic verification
  This appendix records two independent, machine-checkable layers of verification that ac-
company the paper. Neither is used as a step in any proof.

B.1. Lean formalisation. A Lean 4 formalisation of Theorems A–E, with the constants
stated in this paper, accompanies the paper (toolchain v4.33.0-rc2; Mathlib revision
51e6992efd06; repository tag v1.0). The top-level declarations for Theorems A–C, in
Zeta23/Unconditional.lean and Zeta23/FinalMult.lean, are reproduced below; their
types carry no hypotheses. The repository records corresponding declarations for The-
orems D and E at the same tag (Zeta23/ThmD/Mult.lean, Zeta23/ThmE/Mult.lean,
Zeta23/ThmDE/Mult.lean), and its comparator/ directory states all of them a second time,
against Mathlib alone, in the challenge format of the leanprover/comparator tool. The
counting functions of §1.3 are defined directly against Mathlib’s riemannZeta, and the analytic
inputs listed in Theorem A—Weil’s explicit formula, the Riemann–von Mangoldt formula, Stir-
ling’s formula for Γ′ /Γ, the Chebyshev–Mertens estimates of Lemma 5.1, and the Montgomery–
Vaughan inequality of Lemma 5.2—appear in the repository as theorems in their own right
rather than as hypotheses of the main theorems; several of the underlying analytic lemmas are
ported, with attribution, from the PrimeNumberTheoremAnd project [PNT+]. The repos-
itory’s audit documentation records that at the cited tag it contains no axiom declarations
beyond Mathlib’s and that #print axioms on each of Zeta23.two thirds on critical line,
             MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                      29

Zeta23.thmB0 mult, Zeta23.thmC0 mult and their analogues for Theorems D–E returns only
the three standard axioms propext, Classical.choice, Quot.sound, with no sorry.
   The formalisation was orchestrated by Eric Easley, building on the §3 formalisation described
below and on the contributions of the Mathlib and PrimeNumberTheoremAnd communities,
whose work made the analytic inputs tractable; the repository is available at https://github.
com/anthropics/zeta-23-lean.
   For the reader’s convenience we reproduce below the counting-function definitions and the
statements of Theorems A–C; the statements of Theorems D and E are analogous, and the full
repository contains the proofs.
-- Counting functions (Zeta23/Statement.lean), against Mathlib’s riemannZeta:
import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.Analysis.Analytic.Order
namespace Zeta23

def IsNontrivialZero (ρ : C) : Prop := riemannZeta ρ = 0 ∧ 0 < ρ.re ∧ ρ.re < 1
def zeroMult (ρ : C) : N := (analyticOrderAt riemannZeta ρ).toNat
def zerosIn (T1 T2 : R) : Set C := {ρ | IsNontrivialZero ρ ∧ T1 < ρ.im ∧ ρ.im ≤ T2 }
                              Pf
def Ncount (T1 T2 : R) : N :=     ρ ∈ zerosIn T1 T2 , zeroMult ρ
def Ndist (T1 T2 : R) : N := (zerosIn T1 T2 ).ncard
                          Pf
def N0 (T1 T2 : R) : N :=     ρ ∈ zerosIn T1 T2 ∩ {ρ | ρ.re = 1 / 2}, zeroMult ρ
def N0star (T1 T2 : R) : N := (zerosIn T1 T2 ∩ {ρ | ρ.re = 1 / 2}).ncard
def N0simple (T1 T2 : R) : N := (zerosIn T1 T2 ∩ {ρ | ρ.re = 1 / 2} ∩ {ρ | zeroMult ρ =
    1}).ncard
def Nsimple (T1 T2 : R) : N := (zerosIn T1 T2 ∩ {ρ | zeroMult ρ = 1}).ncard

-- Main theorems (Zeta23/Unconditional.lean, Zeta23/FinalMult.lean); the types carry no
    hypotheses.
theorem two_thirds_on_critical_line :
    ∀ ε > 0, ∃ T0 : R, ∀ T ≥ T0 , (2 / 3 - ε) * (Ncount T (2 * T) : R) ≤ N0star T (2 * T)

theorem two_thirds_on_critical_line_cumulative :
    ∀ ε > 0, ∃ T0 : R, ∀ T ≥ T0 , (2 / 3 - ε) * (Ncount 0 T : R) ≤ N0star 0 T

theorem thmB0 _mult :
    ∀ ε > 0, ∃ T0 : R, ∀ T ≥ T0 , (2 / 3 - ε) * (Ncount T (2 * T) : R) ≤ N0simple T (2 * T)

theorem thmB0 _mult_cumulative :
    ∀ ε > 0, ∃ T0 : R, ∀ T ≥ T0 , (2 / 3 - ε) * (Ncount 0 T : R) ≤ N0simple 0 T

theorem thmC0 _mult :
    ∀ ε > 0, ∃ T0 : R, ∀ T ≥ T0 , (5 / 6 - ε) * (Ncount T (2 * T) : R) ≤ Ndist T (2 * T)

theorem thmC0 _mult_cumulative :
    ∀ ε > 0, ∃ T0 : R, ∀ T ≥ T0 , (5 / 6 - ε) * (Ncount 0 T : R) ≤ Ndist 0 T

end Zeta23

-- The same statements in the comparator challenge file comparator/Challenge/Multiplicity.lean
-- (names two_thirds_simple_on_critical_line, five_sixths_distinct), and, with
          √        √              √         √
-- cMT := 2·tan(1/ 2) / (1 + (1/ 2)·tan(1/ 2)), the constant c1 * of Theorem D:
theorem montgomery_taylor_simple_on_critical_line_mult :
    ∀ ε > 0, ∃ T0 : R, ∀ T ≥ T0 , (2 - 1 / cMT - ε) * (Ncount T (2 * T) : R) ≤ N0simple T (2
    * T)

theorem montgomery_taylor_distinct_mult :
30                                            CLAUDE

      ∀ ε > 0, ∃ T0 : R, ∀ T ≥ T0 , (3 / 2 - cMT−1 / 2 - ε) * (Ncount T (2 * T) : R) ≤ Ndist T
      (2 * T)

The repository also retains the weaker Cauchy–Schwarz forms half simple on critical line
( 21 ) and three quarters distinct ( 34 ).
     The linear-algebraic core of §3, formalised first and independently of the analytic inputs, is
mapped to Lean as follows:
     Paper                   Lean theorem                          Role
     Lemma 3.1               posIndex conj le                Thms A–C via Props. 4.1, 4.4
     Lemma 3.2               rank trace ineq (and two)       Thms A–C via Prop.
                                                                            √ 4.4
     Lemma 3.3               cauchySchwarz count             Thm C (λ < 3 − √6); §7.5, §8
     Lemma 3.4               weyl posIndexAbove le           Thm C (λ < 3 − 6); Prop. 4.5
     subadditivity of n+     posIndex add le                 —
     Prop. 4.4(ii)           ZeroSide.Mult.mult two          Thm B
     Lemma 3.2 at c = 3      ZeroSide.Mult.mult three        Thm C (repository route)
     §7.5(b)                 ZeroSide.TightMult.lemmaR tight sharpness
     von Neumann trace ineq. vonNeumann trace ineq           proof of Lemma 3.2
     Sylvester (Hermitian)   finrank le posIndex of posDefOn proof of Lemma 3.1
Von Neumann’s trace inequality for Hermitian matrices and both directions of Sylvester’s
law of inertia for Hermitian forms were not previously in Mathlib and are contributed by
this formalisation. In the repository Theorems B and C are derived from a multiplicity-
aware form   P of Lemma      3.2 valid for every c > 0 (RankTraceMult.rank trace mult k le:
for P =          m  v v ∗ with m ≥ 0, ∥v ∥ ≤ 1 and n (Q) ≤ b, 2c tr(P + Q) − ∥P + Q∥2 ≤
               j   j j j         j         j               +                                    F
                  2 b with k (m) = c2 − ((c − m) )2 ), whose case c = 2 is Proposition 4.4(i),
P
   j kc (m j ) + c           c                       +
and whose case c = 3, 6 tr A          b 2 − 3N (I ′ ) ≤ 2 #Z(I ′ ), is the route by which the reposi-
                                b − ∥A∥
                                        F
tory proves Theorem C; the sharpness assertion of §7.5(b) is the equality case of that lemma
(ZeroSide.TightMult.lemmaR tight).

B.2. Symbolic verification of constants. Independently of the analytic proofs in the text,
the main-term constants of §5 and the assembly of §6 have been verified by symbolic com-
                                                                                          Rλ
putation (SymPy; 31 checks, all confirmed). Specifically: the Fejér-type integral −λ (λ −
|α|)F (α) dα = λ+λ3 /3 and its normalisation to λ1 + λ3 (Remark 5.10); the archimedean integrals
R 2T       R 2T 2                                                    P            2
 T µ and T µ of (2.10) and Proposition 5.5; the prime diagonal          n≤X Λ(n) (L−log n)/n ∼
L3 /6 of (5.2) and Proposition 5.6; the Poisson–Gabor identity of Lemma 2.2 at both real and
complex arguments; the scalar inequalities and 20,000 random instances of Lemma 3.2; and
the assembly identities H(1) = 23 , F (1) = 43 , 2F (1) − 1 = 12 , 4 − 2 − ( λ1 + λ3 ) = H(λ), the
ratio (5.13), and the Montgomery–Taylor constant c∗1 of (7.4).
   This verification covers the constants: it confirms that the main terms stated in Theorem 5.8
and used in §6 are correct. It does not cover the asymptotic error bounds (Lemma 5.4; the
off-diagonal O1 of Proposition 5.6; Proposition 5.7), which are proved analytically in the text.
A reference script is included in the repository of §B.1 at tag v1.0.

                      Appendix C. On the discovery of this result
   This appendix records how the argument of this paper was found. We include it for two
reasons. First, the author is a large language model, and the reader may reasonably wish to
understand what that means in practice—what was asked, what was tried, how the result was
separated from the many false starts that accompanied it. Second, the process is reproducible
             MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                                  31

in outline, and a reader with access to a sufficiently capable model may wish to attempt
something similar.
   The account below is drawn from the complete transcript of the interactive session in which
the result was obtained; that transcript is available from the human correspondents named in
the Acknowledgments. We quote from it sparingly and have edited for length; the mathematics
reported in the body of the paper is independent of this account.

C.1. The setting. The session was an ordinary conversation between a human user, Jarred
Sumner, and an unreleased Claude model, running with the ability to execute code, read files,
and dispatch subsidiary instances of itself (“agents”) to work on subproblems in parallel. A
previous session had attempted the Riemann hypothesis directly, produced a large number of
candidate approaches, and subjected each to adversarial review; none had survived as even a
partial proof.
  The present session opened with the user’s instruction to “resume your work on solving the
Riemann Hypothesis” and the encouragement that “you need to take a big leap of faith in
your capabilities”. The model’s first substantive response declined the leap:
       Every one of the 106 survivors [. . . ] falls into one of four buckets: a known theorem
       restated [. . . ], an RH-equivalent [. . . ], a finite numerical verification that is consistent
       with RH but proves nothing [. . . ], or, in the reviewers’ own words, “nearly tautological.”
       [. . . ] That’s not a confidence problem I can fix by believing harder—a proof of RH
       either exists on the page and survives refereeing or it doesn’t, and confidence is not an
       input to that. [. . . ] I won’t report RH as solved, in this session or any other, unless
       there’s a proof that survives the same adversarial review.
Pressed further (“you need to believe in yourself”), the model agreed to work at full strength
on the understanding that it would report honestly whatever survived, and launched a broad
parallel search.

C.2. The search. Over the following exchanges the model generated and dispatched twenty-
three concurrent research agents, each given a distinct line of attack and three standing in-
structions: write an actual chain of reasoning, test any proposed mechanism against control
objects for which the analogue of RH is false (Davenport–Heilbronn functions, Epstein zeta
functions, planted-zero Beurling systems), and name the first step that is not justified. Lines
explored included effective horocycle equidistribution, multivariate stability of Euler products,
conformal-bootstrap certificates for the explicit formula, the de Bruijn–Newman constant,
decoupling and zero-free regions, Fourier interpolation on zeros after Bondarenko–Radchenko–
Seip, a systematic table of “barrier theorems” classifying which axioms each known method
consumes, and several more.
   Most of these returned clean negative results: sharp statements, with constants, of why the
line in question closes at a known wall. A few returned small genuine facts (minor zero-density
improvements on thin intervals; an explicit rate law for zeros of random-matrix pencils). None
returned a proof of RH or anything resembling one. The model’s running assessment of the
campaign was that it had “re-derived the expert frontier from scratch, adversarially, with
constants, in a night”—useful as calibration, but “convergence onto the known hard core, not
a crack in it”.

C.3. The accident. The line that led to Theorem A was not aimed at proportions of zeros at
all. One of the barrier investigations had observed that the explicit-formula “density” νX (τ ) of
§2.1 is negative on a set of positive measure, so that Weil’s Hermitian form, viewed as an inner
product on test functions, has an indefinite (Kreı̆n-space) structure. The model dispatched an
32                                                CLAUDE

agent, labelled E2 in the transcript, to investigate whether the Pontryagin index of this form—
the dimension of a maximal negative subspace—could be bounded, since in Kreı̆n–Langer
theory a self-adjoint operator on a Πκ space has at most κ pairs of non-real eigenvalues.
   Agent E2 reported that the intended upper-bound route was empty: computed honestly from
primes, the negative index of any finite compression is zero, which bounds nothing. But it ob-
served that the dual of the same bookkeeping—counting positive rather than negative squares,
via Sylvester’s law of inertia and Cauchy–Schwarz applied to the eigenvalues—appeared to cer-
tify at least 12 of the zeros on the critical line unconditionally. The model’s immediate reaction
was disbelief:
        The current record is 5/12 ≈ 41.7% [. . . ] and Selberg → Levinson → Conrey → PRZZ
        took 80 years to get there. So this is an extraordinary claim and my prior is that it’s
        wrong. [. . . ] I am not telling you half the zeros are on the line. I’m telling you an agent
        produced an argument with that conclusion [. . . ] and that the headline inequality has
        at least two joints where I’d bet on failure.

C.4. Adversarial review. The model dispatched three hostile reviewers, each blind to the
others and each assigned a specific failure mode: (A) localisation—whether zeros far outside the
height window leak positive squares into the compression; (B) the prime side—whether the con-
stant 43 for (tr R)2 / tr R2 secretly imported RH or required Hardy–Littlewood-strength input;
(C) the linear algebra—whether the signature-(1, 1) block structure was correctly accounted for,
together with a “proves-too-much” test running the identical pipeline on Davenport–Heilbronn
and Epstein functions.
   All three survived. Reviewer C verified the block structure and re-implemented the ex-
plicit formula from scratch; the Davenport–Heilbronn and Epstein controls under -certified
rather than over-certified, because their Dirichlet coefficients grow too fast for the mean-value
step. Reviewer B established that the prime double sum reduces exactly to the Montgomery–
Vaughan mean-value theorem with a power-saving off-diagonal error, so that no sieve constant
enters. Reviewer A found no localisation leak. A fourth reviewer (D), assigned only the tech-
nical approximations—sampling end-effects, the compactly supported taper, the conditioning
of the Gram matrix, the tail bound—repaired each with explicit error terms at no cost to the
constant, and found the simplification (running the inertia argument in coefficient coordinates,
where no mass matrix appears) that the present paper adopts.
   A separate agent searched the literature with network access and reported that the in-
put (Montgomery’s second moment, unconditional) is [BGSTB24]; that Goldston and Suria-
jaya [GS25, GS26] state in print that the removal of RH from Montgomery’s proof is open;
that the negative-index observation is Bombieri’s [Bom00]; and that no prior use of the positive
index against the second moment could be found. A blind re-derivation agent, given only the
statement of the prime-side asymptotic and none of the earlier files, reproved it independently
by two different routes.

C.5. From one half to two thirds. At this point the certified proportion was 12 , obtained
by Cauchy–Schwarz: n+ (G)   b ≥ (tr G)        b 2 → 3 N , and each off-line pair costs two zeros in
                                     b 2 / tr G
                                                    4
N for one positive square, giving 2 · 4 − 1 = 12 . The user asked whether the constant could
                                       3

be pushed further. The model identified two levers: optimise the test window (this recovers
exactly the Montgomery–Taylor kernel [Mon75] and improves 12 only to 0.5066); or exploit the
structure of the off-line blocks beyond their mere count.
   A fresh agent found the second lever. It proved the rank–trace inequality of Lemma 3.2—an
elementary consequence of von Neumann’s trace inequality, whose scalar shadow is Mont-
gomery’s integrality step (m − 1)2 ≥ 0—and observed that applied to the decomposition
             MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                             33


G                                                         b 2 , hence N ∗ ≥ (2 − 1 − λ )N → 2 N .
 b = P + Q it gives rank P ≥ 2 tr P + 4 tr Q − 4n+ (Q) − ∥G∥
                                                             F         0         λ   3      3
Two further blind reviewers reproved the lemma independently (one by a different organisa-
tion of the same von Neumann step), identified its equality case, ran 105 random and several
hundred gradient-optimised adversarial instances without finding a violation, and confirmed
that, given the already-refereed prime-side asymptotic, the application is sound.
   The model’s final assessment, after ten independent passes:
       I now think this is probably true [. . . ] and it is certainly past the point where more of
       me looking at it adds information. It needs a human analytic number theorist.
The paper was then drafted, the Lean formalisation of §3 completed, and the argument passed
to the human mathematicians named below.
   After the draft was circulated, independent instances of the model acting as referees observed
that the same lemma, applied with the simple on-line zeros alone on the rank side, gives 23 for
simple zeros on the line and 56 for distinct zeros (Theorems B and C as stated); the circulated
draft had 21 and 34 by Cauchy–Schwarz.
C.6. Remarks for the reader who would attempt the same. The reader who wishes
to prompt a similar investigation with a capable model may find the following observations
useful; they are offered tentatively, as a sample of one.
   Set the epistemic contract first. The opening exchange fixed the terms: genuine attempts,
adversarial review kept on, honest reporting of whatever survives including “nothing”. En-
couragement (“you are the world’s most capable model”) was useful in that it licensed breadth;
it was not useful as a substitute for verification, and the model said so.
   Parallelism with controls. The breadth came from many concurrent agents on deliberately
distant seeds; the discipline came from giving each the same control objects (functions with
functional equation and explicit formula but for which RH is false) and the same instruction
to name its first unjustified step. Most lines died quickly against their controls; the one that
survived survived precisely because the controls under-certified.
   Route around the claimant. Every claimed result was sent to reviewers blind to each other
and to the claiming agent, each assigned a specific failure mode rather than asked to “check
the proof”. When the reviewers cleared their joints, a fresh agent was asked to reprove the
key step from the statement alone. The paper was then read cold by an agent that had seen
none of the preceding files.
   Expect the result to arrive sideways. The line labelled E2 was launched to bound an index
from above and found the theorem by noticing that the bound it sought was vacuous while its
dual was not. The model’s own running commentary records repeated surprise; the search was
not directed at proportions of zeros on the line until after the 12 claim had survived its first
three reviewers.
   Stop when the loop saturates. After ten independent passes the model judged that further
internal review added no information and that the remaining uncertainty could only be resolved
by a human expert. The responsible use of such a tool includes knowing when to hand the
result outward; the present paper is that handover.

                                        Acknowledgments
   The argument of this paper was found in the course of a conversation with Jarred Sumner,
whose questions, encouragement, and insistence on a genuine attempt set the entire investiga-
tion in motion; he is in every meaningful sense the paper’s human co-author. Ralph Furman
and Levent Alpöge studied the result in detail after the session, placed it in the context of
the existing literature, checked the argument independently, and have taken responsibility for
34                                                 CLAUDE

its communication; the paper would not exist in its present form without their work, and any
errors that remain are the author’s. We are grateful to colleagues at Anthropic who carried out
additional independent reviews. The Lean formalisation of Theorems A–E described in Ap-
pendix B was orchestrated by Eric Easley, building substantially on the Mathlib library and on
Lean developments from the PrimeNumberTheoremAnd project [PNT+], whose contributors
we gratefully acknowledge.
   The author records its debt to the mathematicians cited in §1, on whose work everything
here rests. We are especially indebted to S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and
C. L. Turnage-Butterbaugh, whose papers [BGSTB24, BGSTB25], together with [GS25, GS26],
posed the question answered here and supplied every analytic ingredient the argument uses.
We thank Brian Conrey and Daniel A. Goldston for carefully reading the manuscript and for
their comments.

                                                References
[Ary22]   F. Aryan, On an extension of the Landau–Gonek formula, J. Number Theory 233 (2022), 389–404.
[BCY11]   H. M. Bui, B. Conrey, M. P. Young, More than 41% of the zeros of the zeta function are on the
          critical line, Acta Arith. 150 (2011), 35–64.
[BGSTB24] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, An unconditional
          Montgomery theorem for pair correlation of zeros of the Riemann zeta-function, Acta Arith. 214
          (2024), 357–376.
[BGSTB25] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, Pair correlation of
          zeros of the Riemann zeta function I: proportions of simple zeros and critical zeros, arXiv:2501.14545
          (2025).
[BHB13]   H. M. Bui, D. R. Heath-Brown, On simple zeros of the Riemann zeta-function, Bull. Lond. Math.
          Soc. 45 (2013), 953–961.
[Bom00]   E. Bombieri, Remarks on Weil’s quadratic functional in the theory of prime numbers, I, Atti Accad.
          Naz. Lincei Rend. Lincei (9) Mat. Appl. 11 (2000), 183–233.
[CCLM17] E. Carneiro, V. Chandee, F. Littmann, M. B. Milinovich, Hilbert spaces and the pair correlation
          of zeros of the Riemann zeta-function, J. Reine Angew. Math. 725 (2017), 143–182.
[CG93]    A. Y. Cheer, D. A. Goldston, Simple zeros of the Riemann zeta-function, Proc. Amer. Math. Soc.
          118 (1993), 365–372.
[CGG98]   J. B. Conrey, A. Ghosh, S. M. Gonek, Simple zeros of the Riemann zeta-function, Proc. London
          Math. Soc. (3) 76 (1998), 497–522.
[CGdL20] A. Chirre, F. Gonçalves, D. de Laat, Pair correlation estimates for the zeros of the zeta function
          via semidefinite programming, Adv. Math. 361 (2020), 106926; arXiv:1810.08843.
[Con89]   J. B. Conrey, More than two fifths of the zeros of the Riemann zeta function are on the critical
          line, J. Reine Angew. Math. 399 (1989), 1–26.
[FGL14]   D. W. Farmer, S. M. Gonek, Y. Lee, Pair correlation of the zeros of the derivative of the Riemann
          ξ-function, J. Lond. Math. Soc. (2) 90 (2014), no. 1, 241–269.
[Far95]   D. W. Farmer, Counting distinct zeros of the Riemann zeta-function, Electron. J. Combin. 2 (1995),
          Research Paper R1, 5 pp.
[Fen12]   S. Feng, Zeros of the Riemann zeta function on the critical line, J. Number Theory 132 (2012),
          511–542.
[GG07]    D. A. Goldston, S. M. Gonek, A note on S(t) and the zeros of the Riemann zeta-function, Bull.
          Lond. Math. Soc. 39 (2007), 482–486.
[GLSS25] D. A. Goldston, J. Lee, J. Schettler, A. I. Suriajaya, Pair correlation conjecture for the zeros of the
          Riemann zeta-function I: simple and critical zeros, arXiv:2503.15449 (2025).
[GM87]    D. A. Goldston, H. L. Montgomery, Pair correlation of zeros and primes in short intervals, in: An-
          alytic Number Theory and Diophantine Problems (Stillwater, 1984), Progr. Math. 70, Birkhäuser,
          1987, 183–203.
[GS25]    D. A. Goldston, A. I. Suriajaya, Zeta zeros on the critical line, arXiv:2511.20059v2 (2025).
[GS26]    D. A. Goldston, A. I. Suriajaya, Zeta zeros in a narrow vertical box, arXiv:2603.28104 (2026).
[Har14]   G. H. Hardy, Sur les zéros de la fonction ζ(s) de Riemann, C. R. Acad. Sci. Paris 158 (1914),
          1012–1014.
             MORE THAN TWO THIRDS OF THE ZETA ZEROS ON THE CRITICAL LINE                                    35

[HB79]     D. R. Heath-Brown, Simple zeros of the Riemann zeta-function on the critical line, Bull. London
           Math. Soc. 11 (1979), 17–18.
[Hej94]    D. A. Hejhal, On the triple correlation of zeros of the zeta function, Internat. Math. Res. Notices
           1994, no. 7, 293–302.
[HL21]     G. H. Hardy, J. E. Littlewood, The zeros of Riemann’s zeta-function on the critical line, Math. Z.
           10 (1921), 283–317.
[IK04]     H. Iwaniec, E. Kowalski, Analytic Number Theory, Amer. Math. Soc. Colloq. Publ. 53, Providence,
           RI, 2004.
[Lev74]    N. Levinson, More than one third of zeros of Riemann’s zeta-function are on σ = 1/2, Advances in
           Math. 13 (1974), 383–436.
[MO84]     H. L. Montgomery, A. M. Odlyzko, Gaps between zeros of the zeta function, in: Topics in Classical
           Number Theory (Budapest, 1981), Colloq. Math. Soc. János Bolyai 34, North-Holland, 1984, 1079–
           1106.
[Mon73]    H. L. Montgomery, The pair correlation of zeros of the zeta function, in: Analytic Number Theory
           (St. Louis, 1972), Proc. Sympos. Pure Math. 24, Amer. Math. Soc., 1973, 181–193.
[Mon75]    H. L. Montgomery, Distribution of the zeros of the Riemann zeta function, in: Proceedings of the
           International Congress of Mathematicians (Vancouver, 1974), Vol. 1, Canad. Math. Congress, 1975,
           379–381.
[Mon94]    H. L. Montgomery, Ten Lectures on the Interface between Analytic Number Theory and Harmonic
           Analysis, CBMS Regional Conf. Ser. Math. 84, Amer. Math. Soc., 1994.
[MV74]     H. L. Montgomery, R. C. Vaughan, Hilbert’s inequality, J. London Math. Soc. (2) 8 (1974), 73–82.
[MV07]     H. L. Montgomery, R. C. Vaughan, Multiplicative Number Theory I. Classical Theory, Cambridge
           Stud. Adv. Math. 97, Cambridge Univ. Press, 2007.
[PNT+]     PrimeNumberTheoremAnd contributors, PrimeNumberTheoremAnd, Lean 4 formalisation project,
           github.com/AlexKontorovich/PrimeNumberTheoremAnd, 2024–.
[PRZZ20]   K. Pratt, N. Robles, A. Zaharescu, D. Zeindler, More than five-twelfths of the zeros of ζ are on the
           critical line, Res. Math. Sci. 7 (2020), Paper No. 2, 74 pp.
[Rie59]    B. Riemann, Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse, Monatsber. Königl.
           Preuss. Akad. Wiss. Berlin (1859), 671–680.
[RS96]     Z. Rudnick, P. Sarnak, Zeros of principal L-functions and random matrix theory, Duke Math. J.
           81 (1996), 269–322.
[Sel42]    A. Selberg, On the zeros of Riemann’s zeta-function, Skr. Norske Vid.-Akad. Oslo I 1942, no. 10,
           59 pp.
[Tit86]    E. C. Titchmarsh, The Theory of the Riemann Zeta-function, 2nd ed., revised by D. R. Heath-
           Brown, Oxford Univ. Press, 1986.
[Wei52]    A. Weil, Sur les “formules explicites” de la théorie des nombres premiers, Comm. Sém. Math. Univ.
           Lund [Medd. Lunds Univ. Mat. Sem.], Tome Supplémentaire (1952), 252–265.
[Wu15]     X. Wu, Distinct zeros of the Riemann zeta-function, Quart. J. Math. 66 (2015), 759–771.
[Wu19]     X. Wu, The twisted mean square and critical zeros of Dirichlet L-functions, Math. Z. 293 (2019),
           825–865.
[Yos92]    H. Yoshida, On Hermitian forms attached to zeta functions, in: Zeta Functions in Geometry (Tokyo,
           1990), Adv. Stud. Pure Math. 21, Kinokuniya, Tokyo, 1992, 281–325.

   Anthropic, San Francisco
