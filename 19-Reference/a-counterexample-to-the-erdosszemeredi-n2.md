---
title: "A COUNTEREXAMPLE TO THE ERDŐS–SZEMERÉDI n2−ε"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/598c5c858faf42137f623ccf5106493bacc9317d.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:57Z"
tags: ["news-research"]
---

A COUNTEREXAMPLE TO THE ERDŐS–SZEMERÉDI n2−ε
                    SUM–PRODUCT BOUND OVER R

        Abstract. We show that the Erdős–Szemerédi sum–product conjecture over R — asserting
        that for every ε > 0 all sufficiently large finite sets A ⊂ R satisfy max(|A + A|, |A · A|) ≥ |A|2−ε
        — is false for a fixed absolute ε. Concretely, taking ε0 = 10−5 we exhibit an infinite family of
        finite sets A ⊂ R with max(|A + A|, |A · A|) < |A|2−ε0 . The sets are orbits of units acting on a
        fixed box of algebraic integers inside totally real number fields of growing degree and bounded
        root discriminant, drawn from an infinite unramified 2-class-field tower. All inputs are classical
        and unconditional: geometry of numbers, Dirichlet’s unit theorem, the analytic class number
        formula, Louboutin’s residue bound, genus theory, and the Golod–Shafarevich criterion. The
        examples are consistent with the known lower bounds max(|A+A|, |A·A|) ≫ |A|4/3+c ; the degree
        of the number field must grow like log |A|, so the mechanism is invisible in the bounded-degree
        regime.


                                              1. Introduction
   For a finite set A ⊂ R write A + A = {a + b : a, b ∈ A} and A · A = {ab : a, b ∈ A}.
The sum–product phenomenon asserts that at least one of these two sets must be substantially
larger than A itself. Erdős and Szemerédi conjectured that max(|A + A|, |A · A|) ≥ |A|2−o(1) ;
equivalently:
        For every ε > 0 there exists n0 such that every finite A ⊂ R with |A| = n ≥ n0
        satisfies max(|A + A|, |A · A|) ≥ n2−ε .
   We disprove this conjecture: the statement fails already for a single fixed value of ε.
Theorem 1.1 (Main Theorem). There is an absolute constant ε0 > 0 (one may take ε0 = 10−5 )
and an infinite set N ⊂ N such that for every n ∈ N there is a finite set A ⊂ R with |A| = n
and
                              max |A + A|, |A · A| < n2−ε0 .
                                                  

In particular, for ε = ε0 there is no n0 as in the displayed statement.
Strategy. Fix a totally real number field K of degree d with ring of integers OK and real
embeddings σ1 , . . . , σd . We build a set A = σ1 (U · X), where U is a set of units all of whose
conjugates lie in a fixed band [e−Θ , eΘ ], and X is a fixed box of algebraic integers. Three
elementary mechanisms operate.
    (1) Sums are controlled by a box. All elements have conjugates bounded by a fixed H =
        H(Θ), independent of |A|. Distinct algebraic integers are 1-separated in the Minkowski
        sup-norm, so a box of radius M contains at most (2M + 1)d integers. Hence |A + A| ≤
        (4H + 1)d , a bound independent of how many points A packs into its box.
    (2) Products are controlled by the unit group. Since A = U ·X, we have A·A ⊆ (U ·U )·(X ·X),
        and U · U is again a band of units; a covering argument shows passing from U to U · U
        costs at most a factor 5d . Thus |A · A| ≤ 5d |U ||X|2 , while |A|2 = |U |2 |X|2 : the product
        set is smaller than |A|2 by a factor ≍ |U |5−d .
    (3) Unique factorisation fixes the size. Choosing X ⊂ 1 + mOK with m larger than the
        house of any ratio of two units of U forces the representation a = ux to be unique, so
        |A| = |U ||X| exactly.
                                                         1
2      A COUNTEREXAMPLE TO THE ERDŐS–SZEMERÉDI n2−ε SUM–PRODUCT BOUND OVER R

   To beat the exponent 2 we need |U |p≥ ecd for units of constant height bound Θ, while
all losses (5d , box-count discrepancies, |∆K |) are eO(d) . The decisive input is a regulator
bound RegK ≤ eCd with an absolute constant C; then the rank-(d − 1) unit lattice, of covolume
≍ RegK , has at least Θd−1 /(3d RegK ) ≥ e(log Θ−C−o(1))d points in the cube of side 2Θ. Choosing
log Θ > C +log 5 makes the product-set saving a genuine power of n = |A|. The regulator bound
follows for any field of bounded root discriminant from the analytic class number formula,
Louboutin’s residue bound, and hK ≥ 1; infinitely many totally real fields of bounded root
discriminant with d → ∞ arise from the Golod–Shafarevich infinite class field tower.
   Throughout, A = σ1 (S) for a finite S ⊂ K, and since σ1 is an injective field homomorphism
we have |A| = |S|, |A + A| = |S + S|, |A · A| = |S · S|, with the latter computed inside K. We
therefore do all counting inside K without further comment.

                             2. Number-theoretic preliminaries
2.1. Boxes of algebraic integers. Let K be a totally real number field of degree d ≥ 2 with
real embeddings σ1 , . . . , σd : K → R, ring of integers OK and discriminant ∆K . Let
                             ι : K → Rd ,      ι(x) = (σ1 (x), . . . , σd (x)),
be the Minkowski embedding, and for M > 0 put
                        BM := {x ∈ OK : |σi (x)| ≤ M for i = 1, . . . , d}.
                                                         p
Fact 2.1. ι(OK ) is a full-rank lattice in Rd of covolume |∆K |.
  See e.g. Neukirch, Algebraic Number Theory, Prop. I.5.2; for a totally real field all embeddings
are real, so no factor 2−r2 appears.
Lemma 2.2 (packing bound). For every M ≥ 0, |BM | ≤ (2M + 1)d .
Proof.
Q         If x ̸= y in OK , then x − y is a nonzeroQalgebraic integer, so its norm N (x − y) =
  i σ i (x − y) is a nonzero rational integer; hence i |σi (x − y)| ≥ 1 and maxi |σi (x − y)| ≥ 1.
Thus the points ι(x), x ∈ BM , lie in [−M, M ]d and are pairwise at sup-distance ≥ 1. The open
axis-parallel unit cubes centred at these points are pairwise disjoint and lie in [−M − 12 , M + 12 ]d ,
of volume (2M + 1)d ; each has volume 1, so there are at most (2M + 1)d points.                      □
Theorem 2.3 (van der Corput). Let Λ ⊂ Rn be a full-rank lattice and S ⊂ Rn a bounded
convex body symmetric about the origin. If vol(S) > m · 2n det Λ for a positive integer m, then
S contains at least 2m nonzero points of Λ.
   See van der Corput, Acta Arith. 2 (1936), 145–146, or Cassels, An Introduction to the Geom-
etry of Numbers, Ch. III, Thm. II. For m = 1 this is Minkowski’s first theorem.
Corollary 2.4. In the setting of Theorem 2.3, if vol(S) ≥ 2n+1 det Λ then
                                                     vol(S)
                                       #(S ∩ Λ) ≥            .
                                                    2n det Λ
Proof. Put q := vol(S)/(2n det Λ) ≥ 2 and m := ⌈q⌉ − 1 ≥ 1. Then m < q, so Theorem 2.3 gives
at least 2m nonzero lattice points in S; adding the origin, #(S ∩ Λ) ≥ 2m + 1 ≥ 2(q − 1) + 1 ≥
q.                                                                                            □
                                              p                       p
Lemma 2.5 (box lower bound). If M d ≥ 2 |∆K |, then |BM | ≥ M d / |∆K |.
                                                      p
Proof. Apply Corollary 2.4 to p Λ = ι(OK ) (covolume |∆K | by Fact 2.1)pand S = [−M,p  M ]d , of
             d     d
volume (2M ) = 2 M ≥ 2d     d+1                                    d   d            d
                                  |∆K |. This gives #(S∩Λ) ≥ (2M ) /(2 |∆K |) = M / |∆K |,
and every lattice point of S is ι(x) for some x ∈ BM .                                        □
       A COUNTEREXAMPLE TO THE ERDŐS–SZEMERÉDI n2−ε SUM–PRODUCT BOUND OVER R                        3

                                                                             ×
2.2. Units: a counting lower bound and a doubling upper bound. Let OK          be the unit
group and
                        ×
                          → Rd ,
                                                                          
                   ℓ : OK        ℓ(u) = log |σ1 (u)|, . . . , log |σd (u)| .
Since |N (u)| = 1, the image lies in the hyperplane H := {v ∈ Rd : v1 + · · · + vd = 0}.
Fact 2.6 (Dirichlet’s unit theorem). For a totally real field of degree d we have ker(ℓ) = {±1}
                    ×
and ΛU := ℓ(OK        ) is a full-rank lattice in the (d − 1)-dimensional space H. For a fundamental
system u1 , . . . , ud−1 (so that ℓ(u1 ), . . . , ℓ(ud−1 ) is a Z-basis of ΛU ), the regulator
                                                                   
                                     RegK := det log |σj (ui )| 1≤i,j≤d−1
is independent of the choice of d − 1 embeddings and of the fundamental system.
  See Neukirch, Algebraic Number Theory, §I.7. For Θ > 0 define the unit box
                           ×
               UΘ := {u ∈ OK : e−Θ ≤ |σi (u)| ≤ eΘ ∀i} = {u : ℓ(u) ∈ [−Θ, Θ]d }.
Note UΘ · UΘ ⊆ U2Θ and u/u′ ∈ U2Θ for u, u′ ∈ UΘ .
Lemma 2.7 (unit count). If Θd ≥ 2(2Θ + 1) d RegK , then
                                                       Θd−1
                                           |UΘ | ≥            .
                                                     3 d RegK
Proof. Let L be the (d − 1) × d matrix with rows ℓ(u1 ), . . . , ℓ(ud−1 ), and let 1 = (1, . . . , 1) ∈
Rd . Set v0 := (2Θ + 1)1 and e          Λ := ΛU + Zv0 . Since v0 ∈
                                                                 / H and ΛU spans H, the vectors
ℓ(u1 ), . . . , ℓ(ud−1 ), v0 are linearly independent and form a Z-basis of Λ,
                                                                            e which is therefore a
full-rank lattice in R with d
                                                                   
                                                L                    L
                                   det Λ = det
                                       e             = (2Θ + 1) det     .
                                                v0                   1
                                                               
                                                                L
                                                                    = dj=1 (−1)d+j Mj , where Mj is
                                                                      P
Expanding the last determinant along its final row, det
                                                                1
the minor of L obtained by deleting column j. The vector c := (−1)d+1 M1 , . . . , (−1)d+d Md
                                                                                                      

satisfies ⟨c, ℓ(ui )⟩ = 0 for each i (it is the expansion of a determinant with a repeated row),
i.e. c ⊥ H; hence c = λ1 for some                                              d+j
                                            λ ∈ R, so all signed minors (−1) Mj equal λ, and
                                             L
|λ| = |Md | = RegK . Therefore det               = d RegK and
                                             1

                                     det Λ
                                         e = (2Θ + 1) d RegK .

                       Λ and S = [−Θ, Θ]d : the hypothesis vol(S) = 2d Θd ≥ 2d+1 (2Θ+1)d RegK
Apply Corollary 2.4 to e
holds by assumption, so
                                                      Θd            Θd−1
                        Λ ∩ [−Θ, Θ]d
                                       
                      # e                   ≥                   ≥          .
                                                (2Θ + 1) d RegK   3 d RegK
Finally, every point λ + kv0 (λ ∈ ΛU , k ∈ Z) of Λ e ∩ [−Θ, Θ]d has coordinate sum kd(2Θ + 1),
                            d
while any point of [−Θ, Θ] has coordinate sum of absolute value at most dΘ < d(2Θ + 1); hence
k = 0 and the point lies in ΛU . Each such v = ℓ(u) gives a unit u ∈ UΘ , and distinct lattice
points give distinct units, whence |UΘ | ≥ Θd−1 /(3d RegK ).                                □
Lemma 2.8 (doubling of the unit count). For every Θ > 0, |U2Θ | ≤ 5d |UΘ |.
4       A COUNTEREXAMPLE TO THE ERDŐS–SZEMERÉDI n2−ε SUM–PRODUCT BOUND OVER R

Proof. Write B := [−Θ, Θ]d , so 2B = [−2Θ, 2Θ]d , and Λ := ΛU . Since u 7→ ℓ(u) is 2-to-1 onto Λ
(Fact 2.6) and, for any T , u ∈ UT iff ℓ(u) ∈ [−T, T ]d , it suffices to show #(Λ∩2B) ≤ 5d #(Λ∩B).
   Choose a maximal {y1 , . . . , ym } ⊆ Λ ∩ 2B with the sets yi + 21 B pairwise disjoint. These lie
in 2B + 21 B = 52 B, so comparing volumes, m vol( 12 B) ≤ vol( 52 B), i.e. m ≤ 5d . By maximality,
every y ∈ Λ ∩ 2B satisfies (y + 21 B) ∩ (yi + 21 B) ̸= ∅ for some i, i.e. y ∈ yi + B. Hence
                               m
                               X
                                     # (Λ − yi ) ∩ B = m #(Λ ∩ B) ≤ 5d #(Λ ∩ B),
                                                    
               #(Λ ∩ 2B) ≤
                               i=1
using Λ − yi = Λ.                                                                                  □
2.3. An upper bound for the regulator.
Theorem 2.9 (analytic class number formula). For a number field K of degree d with r1 real
and r2 complex places, class number hK , regulator RegK , wK roots of unity, and discriminant
∆K ,
                                               2r1 (2π)r2 hK RegK
                            κK := Res ζK (s) =         p          .
                                  s=1               wK |∆K |
Theorem 2.10 (Louboutin). For every number field K ̸= Q of degree d,
                                      e log |∆ | d−1
                                               K
                              κK ≤                     .
                                        2(d − 1)
   See S. Louboutin, Explicit upper bounds for residues of Dedekind zeta functions . . . , Canad.
J. Math. 53 (2001), 1194–1222, Thm. 1; also J. Number Theory 85 (2000), 263–282. Any bound
of shape κK ≤ (C0 log |∆K |/d)d−1 would suffice below.
Lemma 2.11 (regulator bound). Let K be totally real of degree d ≥ 2 with root discriminant
|∆K |1/d ≤ eγ , γ ≥ 4. Then
                                                     γ          γ
                           RegK ≤ eCR d ,      CR := + 1 + log .
                                                     2          4
Proof. For totally real K we have r1 = d, r2 = 0, wK = 2. By Theorem 2.9 and hK ≥ 1,
                                                       p
                                                   2κK |∆K |
                                RegK ≤ hK RegK =              .
                                                       2d
By Theorem 2.10 and log |∆K | ≤ γd,
                          eγd d−1  eγ d−1  d d−1            eγ d−1
                    κK ≤               =                      ≤e           .
                           2(d − 1)          2      d−1             2
Hence
                     2e  eγ d−1 γd/2   4  eγ d γd/2  4
            RegK ≤               e     =          e     = ed(1+log(γ/4)+γ/2) ≤ eCR d ,
                     2d 2                γ 4             γ
using γ ≥ 4 in the last step.                                                                      □
2.4. An infinite family of totally real fields of bounded root discriminant.
Theorem 2.12 (Golod–Shafarevich criterion). Let F be a number field and p a prime. If
                                        q
                    dp Cl(F ) ≥ 2 + 2 r1 (F ) + r2 (F ) + δp (F ),
where dp is the Fp -rank of the p-torsion, Cl(F ) is the ideal class group, and δp (F ) = 1 if µp ⊂ F
and 0 otherwise, then the Hilbert p-class field tower F = F (0) ⊂ F (1) ⊂ · · · (with F (i+1) the
maximal unramified abelian p-extension of F (i) , unramified at all places) is infinite.
       A COUNTEREXAMPLE TO THE ERDŐS–SZEMERÉDI n2−ε SUM–PRODUCT BOUND OVER R                        5

   See Golod–Shafarevich, Izv. Akad. Nauk SSSR 28 (1964), 261–272, with Shafarevich’s
relation-rank bound; or P. Roquette, On class field towers, in Cassels–Fröhlich (eds.), Alge-
braic Number Theory, Academic Press 1967, Ch. IX; or H. Koch, Galois Theory of p-Extensions,
Springer 2002, Thm. 11.16 and §11.4. The Galois group G of the maximal unramified p-extension
satisfies d(G) = dp (Cl(F )) and r(G) ≤ d(G) + r1 + r2 − 1 + δp , and a finite p-group obeys
r(G) > d(G)2 /4.
                                         √
Lemma 2.13 (genus theory). Let F = Q( D) be real quadratic with discriminant having exactly
t distinct prime divisors. Then the narrow class group Cl+ (F ) has 2-rank t − 1, and Cl(F ) has
2-rank at least t − 2.
   This is Gauss’s genus theory; see e.g. D. A. Cox, Primes of the Form x2 + ny 2 . The second
statement follows because the kernel of Cl+ (F ) ↠ Cl(F ) has order at most 2, and quotienting
by a group of order 2 drops the 2-rank by at most 1.
                                                                                           √
Proposition 2.14 (the tower). Let D := 3·5·7·11·13·17·19·23 = 111 546 435 and F0 := Q( D).
There is an infinite sequence of number fields F0 ⊂ F1 ⊂ F2 ⊂ · · · such that for every j ≥ 1:
    (1) Fj is totally real;
    (2) [Fj : Q] → ∞ as j → ∞; √
    (3) |∆Fj |1/[Fj :Q] = |∆F0 |1/2 = 2 D < 21 124.
Proof. Since D ≡ 3 (mod 4) and D is squarefree, ∆F0 = 4D, whose distinct prime divisors are
2, 3, 5, 7, 11, 13, 17, 19, 23; thus t = 9 and, by Lemma 2.13, d2 (Cl(F0 )) ≥ 7. For F0 real quadratic,
r1 = 2, r2 = 0, δ2 = 1 (as −1 ∈ F0 ), so the Golod–Shafarevich threshold in Theorem 2.12 is
       √                                                                                      (j)
2 + 2 3 < 5.47 < 7. Hence the Hilbert 2-class field tower of F0 is infinite; let Fj := F0 .
   Each F (i+1) /F (i) is unramified at all places, hence so is Fj /F0 . Unramifiedness at the infinite
places means no real place becomes complex, so each Fj is totally real, giving (1). The tower
being infinite means Fj ⊊ Fj+1 for all j, so the degrees strictly increase, giving (2). Since Fj /F0
is unramified at all finite places, the relative different is trivial, and the conductor–discriminant
                                             [F :F ]
(transitivity) formula gives ∆Fj = ±∆F0j 0 ; taking [Fj : Q]-th roots gives (3).                     □
  We record the numerical consequence: every K = Fj from Proposition 2.14 is totally real
with                                                √
                        |∆K |1/d ≤ eγ ,   γ := log(2 D) < 9.96,
and hence, by Lemma 2.11 (note γ > 4),
                                              γ         γ
                      RegK ≤ eCR d ,    CR = + 1 + log < 6.90.
                                              2         4
                                       3. The construction
  Throughout this section K = Fj is one of the fields of Proposition 2.14, of degree d, and we
use the absolute constants
γ < 9.96,    CR < 6.90,    Θ := e9 ,   m := ⌈e2Θ ⌉ + 2,    s := 3Θ + 30,    S := es ,   R := 1 + mS.
These are fixed (astronomically large but independent of d). Define
X := 1+m BS = {1+my : y ∈ OK , |σi (y)| ≤ S ∀i},            AK := UΘ ·X = {ux : u ∈ UΘ , x ∈ X},
and finally A := σ1 (AK ) ⊂ R.
   Basic size facts: every x ∈ X has |σi (x)| ≤ 1 + mS = R for all i, and every a = ux ∈ AK has
|σi (a)| ≤ eΘ R for all i. Also 0 ∈
                                  / AK , and |A| = |AK |, |A + A| = |AK + AK |, |A · A| = |AK · AK |
since σ1 is an injective field homomorphism.
6        A COUNTEREXAMPLE TO THE ERDŐS–SZEMERÉDI n2−ε SUM–PRODUCT BOUND OVER R

3.1. The size of A.
Lemma 3.1 (unique factorisation). The map UΘ × X → K, (u, x) 7→ ux, is injective. Conse-
quently
                              |A| = |UΘ | · |X| = |UΘ | · |BS |.
                                                                                ×
Proof. Suppose ux = u′ x′ with u, u′ ∈ UΘ , x, x′ ∈ X. Set w := u/u′ = x′ /x ∈ OK . For each i,
                                              |σi (u)|      eΘ
                                 |σi (w)| =              ≤     = e2Θ .
                                              |σi (u′ )|   e−Θ
Since x ≡ 1 ≡ x′ (mod mOK ), in OK /mOK both classes equal that of 1, and from wx = x′
we get w̄ = 1̄, i.e. w ≡ 1 (mod mOK ). If w ̸= 1, then w − 1 = mβ with β ∈ OK \ {0}, so
|N (w − 1)| = md |N (β)| ≥ md . But for each i,
                             |σi (w − 1)| ≤ |σi (w)| + 1 ≤ e2Θ + 1 < m
because m ≥ e2Θ + 2; multiplying over i gives |N (w − 1)| < md , a contradiction. Hence w = 1,
i.e. u = u′ and x = x′ . Finally |X| = |BS | since y 7→ 1 + my is injective, and |A| = |UΘ ||X| by
the injectivity proved.                                                                          □
Lemma 3.2 (lower bound for |A|). Suppose d is large enough that Θd ≥ 2(2Θ + 1)d eCR d and
S d ≥ 2eγd/2 (both hold for all d ≥ 8, since log Θ = 9 > CR + 2 and s > γ). Then
                                                 Θd−1     Sd
                                      |A| ≥             ·      .
                                                3d eCR d eγd/2
Proof. Combine Lemma 3.1 with Lemma 2.7 (using RegK ≤ eCR d from Lemma    p 2.11 and    Propo-
sition 2.14, so its hypothesis is met) and with Lemma 2.5 for M = S (using |∆K | ≤ e γd/2 ). □
3.2. The sumset.
Lemma 3.3. |A + A| ≤ (4eΘ R + 1)d .
Proof. Every a ∈ AK satisfies |σi (a)| ≤ eΘ R, so every element of AK + AK lies in B2eΘ R ;
Lemma 2.2 gives |AK + AK | ≤ (4eΘ R + 1)d .                                             □
3.3. The product set.
Lemma 3.4. |A · A| ≤ 5d |UΘ | · |X|2 .
Proof. Every element of AK · AK has the form (ux)(u′ x′ ) = (uu′ )(xx′ ) with uu′ ∈ U2Θ and
xx′ ∈ X · X, so AK · AK ⊆ U2Θ · (X · X) and |AK · AK | ≤ |U2Θ | |X · X| ≤ |U2Θ | |X|2 . By
Lemma 2.8, |U2Θ | ≤ 5d |UΘ |.                                                             □

                               4. Proof of the Main Theorem
     Recall the absolute constants
    γ < 9.96, CR < 6.90, Θ = e9 , m = ⌈e2Θ ⌉ + 2 ≤ e2Θ + 3, s = 3Θ + 30, S = es , R = 1 + mS,
and set ε0 := 10−5 .
Proposition 4.1. There is an absolute constant d0 (one may take d0 = 100) such that for every
field K = Fj of degree d ≥ d0 the set A = A(K) ⊂ R of Section 3 satisfies
                 |A · A| ≤ e−d/20 |A|2−ε0        and      |A + A| ≤ e−d/20 |A|2−ε0 .
In particular both are strictly smaller than |A|2−ε0 .
        A COUNTEREXAMPLE TO THE ERDŐS–SZEMERÉDI n2−ε SUM–PRODUCT BOUND OVER R                   7

Proof. Write n := |A| = |UΘ ||X| (Lemma 3.1); all logarithms are natural.
(a) Product set. By Lemma 3.4, |A · A| ≤ 5d |UΘ ||X|2 , and n2−ε0 = |UΘ |2−ε0 |X|2−ε0 , so it
suffices to prove
(1)                                ed/20 5d |X|ε0 ≤ |UΘ |1−ε0 .
We use |X| = |BS | ≤ (2S + 1)d (Lemma 2.2) and |UΘ | ≥ Θd−1 /(3deCR d ) (Lemmas 2.7 and 2.11,
whose hypothesis was checked in Lemma 3.2). Taking logarithms, (1) follows from
           d                                                                        
(2)           + d log 5 + ε0 d log(2S + 1) ≤ (1 − ε0 ) (d − 1) log Θ − CR d − log(3d) .
           20
Now log(2S + 1) ≤ s + log 2 + e−s ≤ s + 0.70, log Θ = 9, and s + 0.70 = 3e9 + 30.70 < 24 341.
The left-hand side of (2) is at most
                              d 0.05 + 1.61 + 10−5 · 24 341 ≤ 1.91 d,
                                                          

while the right-hand side is at least
            (1 − 10−5 )(9d − 6.90d) − (9 + log(3d)) ≥ 2.09 d − 9 − log(3d) ≥ 1.91 d
for all d ≥ 100 (indeed 0.18d ≥ 9 + log(3d) there). This proves (1).
(b) Sumset. By Lemmas 3.3 and 3.2 it suffices to prove
                                             Θd−1      S d 2−ε0
(3)                 ed/20 (4eΘ R + 1)d ≤              ·           .
                                              3deCR d eγd/2
Take logarithms. Since R = 1 + mS ≤ (e2Θ + 3)S + 1 ≤ e2Θ S(1 + 4e−2Θ ),
                 log(4eΘ R + 1) ≤ log 5 + Θ + 2Θ + s + 4e−2Θ ≤ 3Θ + s + 1.62,
so log(LHS) ≤ d(3Θ + s + 1.62) + d/20 ≤ d(3Θ + s + 1.67). For the right-hand side,
                                   h                                       i
              log(RHS) ≥ (2 − ε0 ) d log Θ + s − CR − γ2 − log Θ − log(3d) .
                                                         

Numerically, with Θ = e9 = 8103.08 . . . and s = 3Θ + 30,
                             3Θ + s + 1.67 = 6Θ + 31.67 ≤ 48 650.3,
          log Θ + s − CR − γ2 ≥ 9 + 3Θ + 30 − 6.90 − 4.98 ≥ 3Θ + 27.1 ≥ 24 336.3.
Hence
      log(RHS) ≥ (2 − 10−5 ) · 24 336.3 d − 2(9 + log(3d)) ≥ 48 672.3 d − 2(9 + log(3d)),
and since 48 672.3 d − 2(9 + log(3d)) ≥ 48 650.3 d for all d ≥ 2 (indeed 22d ≥ 18 + 2 log(3d)),
inequality (3) holds.                                                                        □
Proof of Theorem 1.1. Take the infinite sequence of totally real fields Fj from Proposition 2.14
and discard the finitely many of degree < d0 . For each remaining K of degree d, Section 3
produces a finite set A(K) ⊂ R with, by Proposition 4.1,
  max |A(K) + A(K)|, |A(K) · A(K)| ≤ e−d/20 |A(K)|2−ε0 < |A(K)|2−ε0 ,              ε0 = 10−5 .
                                      

By Lemma 3.2, |A(K)| ≥ S d e−γd/2 Θd−1 /(3deCR d ) → ∞ as d → ∞ (the exponential rate
log Θ + s − CR − γ/2 > 0 is positive), so N := {|A(Fj )| : [Fj : Q] ≥ d0 } is an infinite subset of
N; for every n ∈ N we have a set of size exactly n with max(|A + A|, |A · A|) < n2−ε0 .
   Thus the conjecture fails for ε = ε0 : no matter how large n0 is, there are n ∈ N with n ≥ n0
and sets A of size n for which max(|A + A|, |A · A|) ≥ n2−ε0 does not hold.                      □
8      A COUNTEREXAMPLE TO THE ERDŐS–SZEMERÉDI n2−ε SUM–PRODUCT BOUND OVER R

                                          5. Remarks
Remark 5.1 (Consistency with known lower bounds). The best unconditional sum–product
lower bounds over R have the form max(|A+A|, |A·A|) ≫ |A|4/3+c (Elekes; Solymosi; Konyagin–
Shkredov; Rudnev–Stevens). Our sets satisfy these comfortably: we prove only the upper bound
|A|2−ε0 with ε0 = 10−5 , far above 4/3. Likewise, Elekes–Ruzsa-type results (“very small sumset
forces nearly maximal product set”) are not contradicted, as here both doubling constants are
of size |A|1−O(ε0 ) , outside their regime.
Remark 5.2 (Where the approximate subring lives). The construction exploits that R con-
tains number fields of arbitrarily large degree d whose rings of integers look, inside a bounded
Minkowski box, like d-dimensional arithmetic progressions, and whose unit groups have rank
d − 1 with covolume only eO(d) (bounded root discriminant). The degree is tied to the set size
by d ≍ log n (here n ≈ e(3Θ+O(1))d ); for any fixed degree the same computation saves only a
constant factor, which is why the mechanism is invisible in the classical bounded-degree regime.
Remark 5.3 (Effectivity).
               √                 Everything is explicit: γ < 9.96 comes from the specific real qua-
dratic field Q( 3 · 5 · · · 23), and Θ = e9 , m = ⌈e2Θ ⌉ + 2, S = e3Θ+30 , ε0 = 10−5 , d0 = 100.
                                                        6
The first admissible n ∈ N is of size roughly e2.4·10 — astronomically large but finite, and the
statement disproved is asymptotic. No attempt has been made to optimise; towers with smaller
root discriminant (e.g. Martinet’s) and tighter counting would improve ε0 by several orders of
magnitude.
Remark 5.4 (On the inputs). The construction uses only elementary geometry of numbers
(Minkowski/van der Corput counting and a covering argument), Dirichlet’s unit theorem, the
analytic class number formula, Louboutin’s explicit residue bound for Ress=1 ζK , Gauss’s genus
theory, and the Golod–Shafarevich criterion for infinite class field towers — all classical and
unconditional.
