---
title: "Zygimantas Straznickas and Stephen A. Weis"
source_url: "https://www-cdn.anthropic.com/e8d50c167ad47beeb03d6109a4a484be95cb38ea/aes_attacks.pdf"
category: "19-Reference"
fetched_at: "2026-10-28T06:37:48Z"
last_modified: "Tue, 28 Jul 2026 15:27:23 GMT"
tags: ["news-research"]
---

Zygimantas Straznickas and Stephen A. Weis

                                     Anthropic
                            {zygi,sweis}@anthropic.com


       Abstract. HAWK is a lattice signature scheme that is currently a third-
       round candidate in NIST’s post-quantum signature competition. We give
       an unconditional, deterministic polynomial-time reduction from HAWK-
       n key recovery over Kn = Q(ζ2ℓ ) to poly(n) calls to an exact Shortest
       Vector Problem (SVP) oracle in dimension n/2 + 1, where n = 2ℓ−1 is
       the ring degree. The reduction uses a nontrivial automorphism of the
       key lattice, supplied by the Galois involution τ : ζ 7→ −ζ and recoverable
       as a shortest√vector of a public rank-n lattice isometric, up to scaling,
       to Zn/2+1 ⊕ 2 Zn/2−1 . Ducas’s block reduction [Duc23; BN24] on this
       near-hypercubic class finds the automorphism, and the descent of van
       Gent and Pulles [GP25] recovers the key from it. In the gate-count model
       of [AGPS20], the attack lowers the key-recovery cost of HAWK-512 from
       2150 to 2108 and of HAWK-1024 from 2288 to 2182 . We demonstrate this
       with a practical implementation that recovers a HAWK-256 secret key
       end-to-end in a few hours on a single server. The construction does not
       transfer to Falcon. Conductors m ∈ {pk , 2pk } (p an odd prime), i.e. the
       m > 4 with cyclic (Z/m)× , evade the attack.

       Keywords: HAWK · Lattice Isomorphism Problem · Module-LIP ·
       Cyclotomic fields · Key recovery · SVP


1    Introduction

NIST’s post-quantum signature competition [NIST22] attracted several proposals
based on hard lattice problems outside the LWE/SIS family. Among these, HAWK
[HAWK25], originally proposed in [DPPvW22], bases its security on the module
Lattice Isomorphism Problem (module-LIP) over power-of-two cyclotomic rings,
and has fast, floating-point-free signing and compact keys. It was recently selected
for the third round of evaluation [Ala26], the only lattice-based candidate to
advance. The secret key is a short basis B ∈ SL2 (Rn ) of the standard lattice
Rn2 over Kn = Q(ζ), where ζ := ζ2ℓ is a primitive 2ℓ -th root of unity (ℓ ≥ 3)
and Rn is its ring of integers. The public key is its Gram matrix Q = B ∗ B
(∗ is the conjugate-transpose), Hermitian with respect to complex conjugation.
Key recovery entails finding any B ′ with B ′∗ B ′ = Q and reduces to the search
module-LIP problem (smLIP) for the isometry class of Rn2 .
2        Z. Straznickas and S. Weis

    The best previously known key-recovery attack is direct Block–Korkine–
Zolotarev (BKZ) lattice reduction on the rank-2n key lattice. HAWK’s de-
signers derive blocksizes βkey ∈ {211, 452, 940} for the three parameter sets
[HAWK25, Table 7] to achieve different security bounds based on best-known
attacks. Ducas [Duc23] provides a powerful tool: a block-reduction algorithm
that, given a lattice already known to be isometric to a scaled Zd , returns its
hidden orthogonal basis with calls to an exact-SVP oracle in dimension only
⌊d/2⌋+1. By itself this yields no HAWK attack: applied to the rank-2n key lattice,
it gives oracle dimension n + 1, with no improvement on the blocksizes above.
Nevertheless, NIST’s second-round status report encourages further analysis
of HAWK’s “security assumptions, particularly the smLIP problem within the
specific structure of cyclotomic number fields” and notes that prior module-LIP
techniques “currently appear inapplicable to the complex cyclotomic number
fields utilized by HAWK” [Ala26, §3.4].

    Prior module-LIP cryptanalysis [GS02; MPPW24; EP24; Che25; LJPW24]
works with complex conjugation c, whose fixed field is totally real. We use a
second order-2 Galois involution on the base field, τ : ζ 7→ −ζ, whose fixed field
is the complex cyclotomic subfield Q(ζ 2 ). We show that the associated τ -cocycle
Vτ = B −1 τ (B) is a shortest vector of a publicly computable lattice of rank only n:
2 × 2 matrices over Rn cut out by Q-linear constraints with coefficients depending
only on Q.
                                                                      p
p We prove    this lattice is isometric to the near-hypercubic lattice n/4 Zn/2+1 ⊕
   n/2 Zn/2−1 (Proposition 4.5), so Ducas’s block reduction [Duc23; BN24]1 finds
all its shortest vectors with SVP calls in dimension n/2 + 1 (Theorem 5.1,
Appendix E). Recovering the key from Vτ is then the descent of van Gent and
Pulles [GP25]: their kernel sublattice {x ∈ Rn2 : τ (x) = Vτ−1 x} is isometric to
a scaled Zn (Proposition D.2), and one further run of Ducas’s algorithm on
it returns an equivalent key. Combined, this is our main result (Theorem 6.1):
HAWK key recovery reduces deterministically to poly(n) calls to exact SVP in
dimension n/2 + 1. We implement the attack and recover HAWK-256 secret keys
end-to-end in §6.2. The construction does not transfer to Falcon (Appendix F).
Conductors with cyclic (Z/m)× (for m > 4, those of the form pk or 2pk with p
an odd prime) evade it; we expect many other composite conductors do not (§7).

    In the gate-count model of the specification [HAWK25, §5.3], the reduction
lowers the key-recovery cost of HAWK-512 from 2150 to at most 2108 gates and of
HAWK-1024 from 2288 to at most 2182 (Table 1, §6.1). §2 outlines the attack; §3
fixes notation; §§4–6 contain the construction, the reduction, and the experiments;
§§7–9 cover the scope of the attack, prior work, and open questions.


1
    The term near-hypercubic is Bambury and Nguyen’s [BN24]; the precise class meant
    throughout this paper is fixed in §3.3.
              HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1                3

2     Technical Overview

A HAWK public key is a matrix Q = B ∗ B ∈ GL2 (Rn ), where B ∈ SL2 (Rn ) is
the secret key, Kn = Q(ζ) for a primitive 2ℓ -th root of unity ζ, Rn = Z[ζ], and
n = 2ℓ−1 is the degree of Kn (§3.1). Key recovery asks for any B ′ with B ′∗ B ′ = Q;
such a B ′ signs in place of the secret key [HAWK25, §5.1]. The Galois group of
Kn /Q contains three involutions: complex conjugation c, the map τ : ζ 7→ −ζ,
and σ := cτ (§3.2). The attack computes the matrix Vτ := B −1 τ (B) from Q
alone (without needing B), then computes a B ′ from Vτ . It has three steps.


2.1   The attack in three steps
                                                            (τ )
 1. Step 1 (§4) computes from Q a basis of a lattice ΛB ⊂ M2 (Rn ) of rank n
    that contains Vτ as a shortest vector in polynomial time.
                                                                         (τ )
 2. Step 2 (Theorem 5.1) computes all 2(n/2 + 1) shortest vectors of ΛB . §6.1
    bounds the number of SVP-oracle calls in dimension n/2 + 1 by O(n2 log n).
    In practice, a single progressive sieve sufficed for HAWK-256, §6.2.
 3. Step 3 (Proposition D.2, Appendix D) computes B ′ from the 2(n/2 + 1)
    candidates: exactly two of them, ±Vτ , satisfy Y ≡ I (mod 2), and these are
    followed by at most two further reduction runs, each with SVP-oracle calls
    in dimension at most n/2 + 1.

    Theorem 6.1 combines the three steps into a deterministic reduction: for
every power of two n ≥ 4, HAWK-n key recovery reduces to poly(n) arithmetic
operations and poly(n) calls to an exact-SVP oracle in dimension at most n/2 + 1.
Table 1 (§6.1) lists the costs per parameter set; Appendix F explains why Falcon
is unaffected.


2.2   Derivation overview

Step 1: the cocycle lattice. The attack needs, from the public key alone, a
lattice that contains a vector leading back to the secret key. That vector is the
cocycle Vτ = B −1 τ (B). Although it is built from B, the vector satisfies the cocycle
equation and an intertwining relation between the two public Gram matrices
Q and τ (Q). Both become Q-linear conditions on its entries with coefficients
computable from the public key (Lemma 4.1). The integer solutions of the two
                                 (τ )
conditions form the lattice ΛB , of rank n (Lemma 4.3). A Z-basis of it is
                                                                                   (τ )
computed from Q in polynomial time (§4.1). Vτ is a shortest vector of ΛB .
                              (τ )
Lengths are measured by Q (Y ) := TrF (det Y ), which is the trace from the
degree-n/4 field F fixed by c and τ , §3.2. det Vτ = 1 since det B = 1, and so its
squared length is the minimum TrF (1) = n/4, regardless of the key-generation
distribution (Lemma 4.4). The step uses two properties of HAWK: det B = 1,
and the public key is the Gram matrix of B.
4         Z. Straznickas and S. Weis

    Step 2: the isometry class and its reduction. Finding the shortest vectors
     (τ )
of ΛB requires its isometry class. The change of variables Y 7→ BY τ (B)−1
carries the cocycle lattice of any key isometrically to that of the trivial key B = I
(Lemma 4.2). The map is secret, but only its existence matters, so the class
                  at B = I. There, working in the power basis, (ΛI , Q(τ ) ) ∼
                                                                          (τ )
can
p be read     off p                                                                  =
   n/4 Zn/2+1 ⊕ n/2 Zn/2−1 (Proposition  √    4.5): up to scaling, the cocycle  lattice
is in the near-hypercubic class [Zp ⊕ 2 Zq ] with p = n/2 + 1, q = n/2 − 1.
   Ducas’s block-reduction framework [Duc23; BN24] solves LIP for this class
with SVP-oracle calls in dimension p = n/2+1 (Theorem 5.1, proved in Appendix
                                                  (τ )
E), returning all 2(n/2 + 1) shortest vectors of ΛB .
   Step 3: from a shortest vector to the key. This step is the automorphism
framework of [GP25] (§5, Appendix D). Each shortest vector Y defines an
order-2 automorphism of the public quadratic module, with fixed sublattice
MY := {x ∈ Rn2 : τ (x) = Y −1 x} under the form T (x, y) := TrKn (x∗ Qy). Only
Y = ±Vτ lead back to the key, and they are the two candidates with Y         √≡I
(mod 2) (the parity test, Appendix D). For ±Vτ , (MY , T ) is isometric to n Zn
with the columns of B −1 (up to roots of unity) as its shortest vectors (Proposition
D.2). One run of the algorithm of [Duc23] returns the shortest vectors with SVP-
oracle calls in dimension at most n/2 + 1, and any pair u1 , u2 with u∗1 Qu2 = 0
gives an equivalent key [u1 u2 ]−1 . Theorem 6.1 assembles the three steps; §6.1
counts the oracle calls and gates.


3      Preliminaries

3.1     Fields, dimensions, and the key-recovery problem

Throughout, ℓ ≥ 3 is fixed, ζm denotes a primitive m-th root of unity and ζ := ζ2ℓ ,
and

                               Kn = Q(ζ),          Rn = Z[ζ],
                     n := [Kn : Q] = 2   ℓ−1
                                               ,   Kn+ := Q(ζ + ζ −1 ).

Here Kn and Rn are the cyclotomic field and its ring of integers, in the notation
of the specification [HAWK25]; n is the ring degree (also the specification’s n),
the module lattice Rn2 has Z-rank 2n, Kn+ is the maximal totally real subfield
of Kn , and [Kn+ : Q] = n/2. For a general number field E, OE denotes its ring
of integers, and we abbreviate TrE := TrE/Q and NE := NE/Q for the trace and
norm down to Q. Superscripts on a ring or field carry several meanings, always
distinguishable from context:

    – the unit group (R× ) and the k-fold Cartesian power (Rk for an integer k ≥ 1);
    – the fixed field or ring of an automorphism, or of the subgroup ⟨· · · ⟩ generated
                                    γ
      by several (E γ , E ⟨c,τ ⟩ , OE , Rnγ );
              HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1              5

 – the (−1)-eigenspace of an involution (E γ=−1 , Rnγ=−1 );
 – the maximal totally real subfield (E + ).

    For X ∈ Ma×b (Kn ) (the a × b matrices over Kn ; we abbreviate Ma := Ma×a )
                T
write X ∗ := X where ¯· = c is complex conjugation ζ 7→ ζ −1 ; for x ∈ Kn we
set |x|2 := x c(x), an element of Kn+ . The HAWK parameter sets HAWK-256,
HAWK-512, and HAWK-1024 are ℓ ∈ {9, 10, 11}, i.e. n ∈ {256, 512, 1024}; the
names refer to n, as in the specification.
    A HAWK secret key is B ∈ SL2 (Rn ); the public key is Q = B ∗ B ∈ GL2 (Rn ),
which is Hermitian with det Q = 1. Two keys B, B ′ are equivalent if B ′ = U B for
some U ∈ U2 (Rn ) := {U ∈ GL2 (Rn ) : U ∗ U = I} (equivalently B ′∗ B ′ = Q). The
key-recovery problem HAWK-KR(n) (smLIP for the isometry class of Rn2 )
is: given Q, output any B ′ ∈ GL2 (Rn ) with B ′∗ B ′ = Q. Any such B ′ suffices to
forge signatures [HAWK25, §5.1].


3.2   The three involutions

Gal(Kn /Q) ∼
           = (Z/2ℓ )× ∼= Z/2 × Z/2ℓ−2 is non-cyclic for ℓ ≥ 3. Its 2-torsion
subgroup has order 4, with three nontrivial commuting involutions:

           c : ζ 7→ ζ −1 ,   τ : ζ 7→ −ζ,     σ := cτ = τ c : ζ 7→ −ζ −1 .

Their fixed fields are Knc = Kn+ (totally real), Knτ = Q(ζ 2 ) = Q(ζ2ℓ−1 ) (complex
cyclotomic — the field underlying HAWK-(n/2)), and Knσ (a CM field of degree
n/2, i.e. a totally imaginary quadratic extension of a totally real field). Set
        ⟨c,τ ⟩
F := Kn        = Kn+ ∩ Knτ , totally real of degree n/4.


3.3   Lattice conventions

For a Euclidean lattice Λ, λ1 (Λ) denotes the length of a shortest nonzero vector,
Λ∨ := {w ∈ span(Λ) : ⟨w, Λ⟩ ⊆ Z} the dual lattice, and [Λ] the isometry (LIP)
class; between quadratic lattices, ∼= always means isometry, never mere Z-module
isomorphism. For s > 0, s · Λ denotes Λ with all lengths scaled by s (equivalently,
its Gram matrix scaled by s2 ). We write A ⊕ B for the orthogonal direct sum
of quadratic lattices, and call a lattice hypercubic if it is isometric to a scaling
s · Zm of the integer lattice for some s > 0. Bambury and Nguyen [BN24]
call a lattice near-hypercubic when its first minimum is almost as short as the
integer lattice’s, the operational hypothesis being λ1 (Λ) λ1 (Λ∨ ) < 1 − ε for some
ε = 1/poly(rank Λ) [BN24, Thm 1]. The term names a broad family, and in
this paper it always refers to the
                                 √ specific class arising from HAWK, √   the lattices
isometric to a scaling of Zp ⊕ 2 Zq (for which λ1 (Λ) λ1 (Λ∨ ) = 1/ 2, for any
p, q ≥ 1 and any scaling).
   We equip Rn with the trace form ⟨x, y⟩Kn := TrKn (x c(y)); the power-of-two
trace formula (stated in the proof of Proposition 4.5) makes the power basis
6       Z. Straznickas and S. Weis

(ζ j ) orthogonal for it, with all squared norms equal to n. The block-reduction
notation (primitive sublattices, volumes, projected blocks) used by Algorithm 1,
§9, and Appendices D–E is set up at the start of Appendix E.


4     The τ -Cocycle Lattice

The matrix Vτ := B −1 τ (B) measures the failure of the secret basis to be τ -
equivariant. Since det B = 1, its determinant (det B)−1 τ (det B) equals 1, and
applying τ once more gives the cocycle equation Vτ τ (Vτ ) = I: Vτ is the Galois
1-cocycle of B for the quadratic extension Kn /Knτ . On its own this equation
pins down nothing: every A ∈ GL2 (Kn ) yields a solution A−1 τ (A). Two further
constraints, both publicly checkable, cut Vτ down to a shortest vector of a rank-n
lattice.


4.1   Definition
                                     Y22 −Y12
                                              
For Y ∈ M2 (Kn ) write adj Y = −Y      21 Y11
                                                , so Y · adj Y = (det Y )I. Define the
τ -cocycle lattice of the public key Q, and the quadratic form on it, as

                   n                                                                     o
       (τ )
      ΛB      :=       Y ∈ M2 (Rn ) : τ (Y ) = adj Y and Q Y = σ(Y )T τ (Q)               ,
                                      |      {z     }    |      {z        }
                                              (C1)                          (C2)
                                   (τ )
                                  Q       (Y ) := TrF (det Y ),

                                                         ⟨c,τ ⟩
where Q is the public Gram matrix and F = Kn                      the totally real field of degree
n/4 from §3.2.
   Constraint (C1) linearizes the cocycle equation τ (Y ) = Y −1 by replacing Y −1
with adj Y ; constraint (C2) imposes the relation QY = σ(Y )T τ (Q) between the
public Gram matrices Q and τ (Q) with Y as the unknown.
    Both constraints are Q-linear in the 4n rational coordinates of Y (with τ
and σ acting entrywise): (C1) has constant coefficients and (C2) has coefficients
                                                                      (τ )
determined by Q and τ (Q), both publicly computable. Hence ΛB is the integer
kernel of a public linear system, and a Z-basis is computable in polynomial time
via Hermite normal form.
                                        (τ )               (τ )
    The form Q(τ ) is Q-valued on ΛB : for Y ∈ ΛB , (C1) gives τ (det Y ) =
det(adj Y ) = det Y , and taking det of (C2) with det Q = det τ (Q) = 1 gives
                                              ⟨c,τ ⟩
σ(det Y ) = det Y , so det Y ∈ Knτ ∩Knσ = Kn         = F , hence det Y ∈ OF . (Neither
constraint alone suffices: (C1) places det Y in Knτ , (C2) in Knσ .) Shortness is
measured with respect to Q(τ ) throughout. Explicitly, det Y is quadratic in the
4n rational coordinates of Y , so Q(τ ) is a quadratic form in the usual sense;  the
associated bilinear form is (Y, Y ′ ) 7→ 21 TrF det(Y +Y ′ ) − det Y − det Y ′ , and
                          (τ )
the Gram matrices of ΛB used elsewhere are taken with respect to it.
              HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1              7

4.2   The secret cocycle and the secret-basis isometry

                                                                     (τ )
Lemma 4.1. Let Vτ := B −1 τ (B) ∈ SL2 (Rn ). Then Vτ ∈ ΛB and det Vτ = 1.
    Proof. det Vτ = (det B)−1 · τ (det B) = 1. (C1): τ (Vτ ) = τ (B)−1 B = Vτ−1 =
adj Vτ (since det Vτ = 1). (C2): QVτ = B ∗ B · B −1 τ (B) = c(B)T τ (B), and

                 σ(Vτ )T τ (Q) = [cτ (B −1 ) · c(B)]T · τ (B ∗ B)
                               = c(B)T (cτ )(B)−T · (cτ )(B)T τ (B)
                               = c(B)T τ (B).       □

   The defining constraints involve Q, so the lattice itself depends on the key;
the following (secret) isometry shows that its rank, minimum, and isometry class
do not.
   Lemma 4.2. The map φτ : Y 7→ BY τ (B)−1 is a Z-linear bijection
                               (τ )      (τ )
M2 (Rn ) → M2 (Rn ) carrying ΛB onto ΛI (the lattice of §4.1 for the trivial
key B = I, i.e. Q = I) and preserving det (hence Q(τ ) ).
    Proof. B, τ (B) ∈ SL2 (Rn ), so φτ is an Rn -bimodule automorphism. For
W = φτ (Y ): τ (W ) = τ (B)τ (Y )B −1 , and adj W = adj(τ (B)−1 ) · adj Y · adj B =
τ (B)·adj Y ·B −1 (using adj X = X −1 for X ∈ SL2 and adj(XY Z) = adj Z ·adj Y ·
adj X). These agree iff (C1) holds for Y . Rewriting (C2) as QY τ (Q)−1 = σ(Y )T
and substituting Q = c(B)T B, τ (Q)−1 = τ (B)−1 (cτ )(B)−T gives: (C2) ⇔ W =
σ(W )T , which is (C2) at Q = I. Finally det W = det B·det Y ·τ (det B)−1 = det Y .
□
   The attacker does not know φτ (it depends on B). Its existence shows
       (τ )              (τ )
that (ΛB , Q(τ ) ) and (ΛI , Q(τ ) ) are isometric as quadratic Z-lattices, so rank,
minimum, shortest-vector count, and isometry class can be read off from the
Q = I case.


4.3   Rank and explicit parametrization

At B = I the two constraints decouple entrywise, yielding an explicit parametriza-
tion and the rank. Write Rnσ := Rn ∩ Knσ for the fixed ring of σ and Rnτ =−1 :=
{x ∈ Rn : τ (x) = −x} for the (−1)-eigenspace of τ . We call the intersection of
Rn with an eigenspace of an involution an eigenlattice.
                        (τ )           (τ )  a b               σ        τ =−1
    Lemma 4.3. rankZ ΛB = n, and ΛI =           σ(b) τ (a) : a ∈ Rn , b ∈ Rn     .
                                                              (τ )
    Proof. By Lemma 4.2 it suffices to parametrize Λ I = {W ∈ M2 (Rn ) :
τ (W ) = adj W, W = σ(W )T }. Writing W = ba′ ab′ , constraint (C1) gives
τ (a) = a′ , τ (b) = −b, τ (b′ ) = −b′ entrywise, and constraint (C2) gives a = σ(a),
a′ = σ(a′ ), b′ = σ(b). Thus a ∈ Rnσ is free (n/2 Z-dimensions since [Kn : Knσ ] = 2)
and a′ = τ (a) is determined, consistently since σ(a′ ) = στ (a) = τ σ(a) = a′ .
Similarly b ∈ Rnτ =−1 is free (n/2 Z-dimensions, basis {ζ 2j+1 : 0 ≤ j < n/2}) and
8           Z. Straznickas and S. Weis

b′ = σ(b) is determined, consistently since τ (b′ ) = τ σ(b) = στ (b) = −σ(b) = −b′ .
The total rank is n. □
    This computation is where the hypothesis τ ̸= c is used: for τ = c the
composite σ = cτ is the identity, constraint (C2) degenerates, and the analogous
lattice has rank 3n/2 (§8.3, Appendix C).
                                     
                              a   b                                  (τ )
    We write W (a, b) := σ(b)   τ (a)   for the general element of ΛI , so that
    (τ )
ΛI = {W (a, b) : a ∈ Rnσ , b ∈ Rnτ =−1 }. Its determinant a τ (a) − b σ(b) simplifies:
since σ(a) = a, τ (a) = τ σ(a) = c(a) and a τ (a) = |a|2 ; since τ (b) = −b,
σ(b) = cτ (b) = −c(b) and −b σ(b) = |b|2 . Hence det W (a, b) = |a|2 + |b|2 , with no
cross term between a and b.


4.4        Positive-definiteness and shortest vectors
                                                       (τ )
Lemma 4.4. (i) Q(τ ) is positive-definite on ΛB ; (ii) minY ̸=0 Q(τ ) (Y ) = n/4,
attained exactly at the 2(n/2 + 1) vectors Y with Y τ (Y ) = I (equivalently
det Y = 1).
                                         (τ )
    Proof. By Lemma 4.2 work in ΛI . By §4.3, det W (a, b) = |a|2 + |b|2 , a sum
of two elements of the form x c(x), totally ≥ 0 in F , and = 0 iff W = 0. Therefore
Q(τ ) (W ) = TrF (|a|2 + |b|2 ) > 0 for W ̸= 0.
    By the AM–GM inequality over the [F : Q] = n/4 real embeddings, to-
gether with NF (det W ) ∈ Z≥1 (nonzero algebraic integer), we have Q(τ ) (W ) ≥
(n/4) NF (det W )4/n ≥ n/4. Equality throughout holds iff det W = 1: equality
in the AM–GM forces det W to be constant across the real embeddings of F ,
and a totally positive constant of integer norm 1 is 1. Conversely every Y with
det Y = 1 has Q(τ ) (Y ) = TrF (1) = n/4. Hence the minimum is n/4, attained
exactly at the Y with det Y = 1, equivalently (since Y · adj Y = (det Y )I and
adj Y = τ (Y ) by (C1)) at the Y with Y τ (Y ) = I.
    For the count, a shortest vector is a W (a, b) with |a|2 + |b|2 = 1, both
summands totally non-negative algebraic integers in OF : if both were nonzero,
each would lie in (0, 1) at every real embedding, hence have norm in (0, 1),
which is impossible. So one summand vanishes, and the nonzero one of a, b is
an algebraic integer all of whose archimedean absolute values equal 1, hence a
root of unity by Kronecker’s theorem. Either b = 0 and a is a root of unity of
Knσ , i.e. a = ±1 (since σ(ζ k ) = ζ k forces ζ 2k = (−1)k , i.e. k ∈ {0, n}), giving
the 2 vectors ±I; or a = 0 and b is a root of unity of Kn with τ (b) = −b, i.e.
b ∈ {ζ k : k odd}, giving n vectors. Total 2(n/2 + 1). □


4.5        The isometry class

                                                (τ )
By Lemma 4.2 the isometry class of (ΛB , Q(τ ) ) is that of the trivial-key lattice:
   Proposition 4.5. (ΛI , Q(τ ) ) ∼
                      (τ )           p                   p
                                  =    n/4 Zn/2+1 ⊕        n/2 Zn/2−1 .
               HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1                   9

                        (τ )
    Proof. By §4.3, ΛI = {W (a, b) : a ∈ Rnσ , b ∈ Rnτ =−1 } with det W (a, b) =
|a| + |b|2 , so the two summands are Q(τ ) -orthogonal and Q(τ ) (W (a, b)) =
  2

TrF (|a|2 ) + TrF (|b|2 ) = 14 ⟨a, a⟩Kn + 14 ⟨b, b⟩Kn , where ⟨·, ·⟩Kn is the trace form of
§3.3 and we used |a|2 , |b|2 ∈ F and [Kn : F ] = 4. It remains to compute the restric-
tion of ⟨·, ·⟩Kn to the eigenlattices Rnτ =−1 = ker(τ +1)|Rn and Rnσ = ker(σ −1)|Rn .

     By the power-of-two trace formula (TrKn (ζ m ) equals n if m ≡ 0, −n if m ≡ n,
else 0, mod 2ℓ ), the power basis (ζ j√
                                      )0≤j<n is ⟨·, ·⟩Kn -orthogonal with all squared
norms equal to n: (Rn , ⟨·, ·⟩Kn ) ∼
                                   = n Zn . Every γ ∈ Gal(Kn /Q) is an isometry
of this lattice (TrKn (γ(x)γ(y)) = TrKn (γ(xy)) = TrKn (xy)) and maps each ζ j to
     ′
±ζ j , i.e. acts on the orthogonal basis by a signed permutation. For an involution
the cycles have length 1 or 2, and the ε-eigenlattice (ε = ±1) decomposes
orthogonally over the cycles: a basis vector fixed with sign ε contributes itself
(squared norm n); a basis vector fixed with sign −ε contributes nothing; a 2-cycle
           ′                                                ′
ζ j 7→ sζ j 7→ ζ j contributes the single vector ζ j + εsζ j (squared norm 2n).

    For τ : τ (ζ j ) = (−1)j ζ j — every basis vector is fixed up to sign, there are
L 2-cycles,
no             and       (−1)-eigenlattice is the span of the odd powers: Rnτ =−1 =
                  √ then/2
            j ∼
   j odd Zζ =        nZ .

    For σ: σ(ζ j ) = (−1)j ζ −j = (−1)j+1 ζ n−j for 1 ≤ j ≤ n − 1 (using ζ −j =
−ζ n−j ), and σ(1) = 1. The underlying permutation j 7→ n − j has two fixed
points, j = 0 (sign +1; this is the case σ(1) = 1 treated separately above)
and j = n/2 (sign (−1)n/2+1 = −1 since n/2 is even), and n/2 − 1 two-cycles
{j, n − j}; on the rank-2 sublattice Zζ j ⊕ Zζ n−j the involution acts by ( 0s 0s )
with s = (−1)j+1 , whose integer fixed vectors are exactly Z(ζ j + sζ n−j ). Hence
                                              √          √
                       Z ζ j + (−1)j+1 ζ n−j ∼
               Ln/2−1
Rnσ = Z · 1 ⊕      j=1                        = n Z ⊕ 2n Zn/2−1 .

    Dividing all squared norms by 4 (n/4 and n/2) and combining the two Q(τ ) -
orthogonal summands gives the claim. The n/2 + 1 short basis vectors (squared
norm n/4) are W (1, 0) = I and W (0, ζ j ) for j odd. □
                                       p              √                    (τ )
    Corollary 4.6. After rescaling by 4/n (i.e. 2/ n), the public lattice ΛB
                      ′
is in the LIP class [Λ ] [DvW21] of the near-hypercubic lattice

                       √
          Λ′ := Zp ⊕       2 Zq ,   p := n/2 + 1, q := n/2 − 1, p + q = n.


The Gram representative D = diag(Ip , 2Iq ) is integral; the dual class is [Zp ⊕
√1 Zq ]. (The integers p, q fixed here are used throughout §5 and Appendix E;
  2
they are not to be confused with the odd prime p of §7.)

    Remark 4.7. The proof of Proposition 4.5 uses TrKn (ζ m ) = 0 for all 0 <
|m| < n. For non-power-of-two conductors this fails (e.g., TrQ(ζp )/Q (ζpm ) = −1 for
an odd prime p and all m ̸≡ 0), and the analogous lattice need not be isometric
           ′      ′
to any a Zp ⊕ b Zq , 0 < a < b; see §7.
10       Z. Straznickas and S. Weis

                                                (τ )
5     Recovering the Key from ΛB
                                                                                √
Corollary 4.6 places the rescaled cocycle lattice in the LIP class [Λ′ ] = [Zp ⊕ 2 Zq ],
p = n/2 + 1, q = n/2 − 1. We run Ducas’s two-block reduction [Duc23, Alg. 1]
with cut k := p − 1:


Algorithm 1 Ducas’s two-block reduction [Duc23, Alg. 1] on [Λ′ ], cut k = p − 1.
The reduction operations are defined in §E.4.
Require: integral Gram matrix of a basis B = (b0 , . . . , bp+q−1 ) of Λ ∈ [Λ′ ] (this B is
    unrelated to the secret key of §3.1)
Ensure: U ∈ GLp+q (Z) with U T (input) U = diag(Ip , 2Iq ) up to signed permutation
 1: while vol(B[0:k−1] )2 > 1 do
 2:   dual-SVP reduce B[0:k] ; primal-SVP reduce B[k:p+q−1]
 3: HKZ-reduce B[0:k−1] ; HKZ-reduce B[k:p+q−1] ; size-reduce B


Ducas’s progress lemma [Duc23, Lemma 4] fails on [Λ′ ] (§E.1); Appendix E
adapts the product-progress framework of [BN24, Lemma 1, Thm 1] to [Λ′ ],
supplying the no-abort bound (Lemma E.2; see Remark E.5), and proves:
     Theorem 5.1. On input an integral Gram matrix H of a basis of a lattice      in
[Λ′ ], Algorithm 1 terminates after at most p2 ln p + p ln 2(p − 1) ln maxi ∥bi ∥ + 3p
                                                  √
iterations (any basis of [Λ′ ] has maxi ∥bi ∥ ≥ 2) and outputs U ∈ GLp+q (Z)
with U T HU = diag(Ip , 2Iq ) up to signed permutation, using SVP-oracle calls in
dimension ≤ p = n/2 + 1 only.
     Proof: Appendix E.
                                                                     (τ )
    Algorithm 1 returns all 2(n/2 + 1) shortest vectors of ΛB . For each, x 7→
Y τ (x) is an order-2 automorphism of the public form (Rn2 , T ) outside the trivial
group of [GP25] (Lemma D.1), so the descent of van Gent and Pulles [GP25,
Props. 1–2] applies: a short vector of the kernel sublattice MY recovers an
equivalent key.
   Appendix D sharpens the analysis to an unconditional bound: the parity test
Y ≡ I √ (mod 2) selects the two candidates Y = ±Vτ , for which the kernel is
exactly n Zn (Proposition D.2), so one further run of Ducas’s algorithm [Duc23]
on it returns the key with SVP-oracle calls in dimension at most n/2 + 1.


6     Main Theorem and Security Consequences

Theorem 6.1. For every power of two n ≥ 4 there is a deterministic algorithm
that, given a HAWK-n public key Q = B ∗ B with B ∈ SL2 (Rn ), outputs B ′ ∈
GL2 (Rn ) with B ′∗ B ′ = Q, making poly(n) arithmetic operations and poly(n)
calls to an exact-SVP oracle in dimension at most n/2 + 1.
     Proof.
              HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1                11

                                                        (τ )
 1. Compute a Z-basis and Gram matrix G(τ ) of (ΛB , Q(τ ) ) from Q. By Lemma
    4.2 and Proposition 4.5, n4 G(τ ) is an integral Gram matrix of a lattice in [Λ′ ].
 2. LLL-reduce n4 G(τ ) and apply Algorithm 1 (Theorem 5.1): the p output basis
    vectors of minimal norm, pulled back to M2 (Rn ) and taken with both signs,
                                              (τ )
    are the 2(n/2 + 1) shortest vectors of ΛB . This uses poly(n) × SVP(n/2 + 1).
 3. For each of the two Y with Y ≡ I (mod 2) (exactly ±Vτ , by the parity test of
    Appendix D): compute a Z-basis and T -Gram of MY , T (x, y) := TrKn (x∗ Qy),
    by Hermite normal form on the constraint τ (x) = Y −1 x (with Y −1 = adj Y ∈
    M2 (Rn ) since det Y = 1); LLL-reduce n1 T -Gram and solve Zn -LIP on it via
    [Duc23], using poly(n) × SVP(n/2 + 1) (Appendix D). For each pair        (u1 , u2 )
    from the resulting shortest-vector set with u∗1 Qu2 = 0 (at most n2 pairs up
    to sign), test whether B ′ := [u1 u2 ]−1 satisfies B ′ ∈ GL2 (Rn ) and B ′∗ B ′ = Q;
    output the first such B ′ .

By Proposition D.2, step (3) succeeds for Y = ±Vτ . □


6.1   Cost estimates

Table 1 compares the per-call cost of the SVP oracle at the designers’ blocksize
βkey and at the oracle dimension n/2+1 of Theorem 6.1, under both the Core-SVP
heuristic (20.292β [BDGL16]) and the gate-count model of Albrecht, Gheorghiu,
Postlethwaite, and Schanck [AGPS20]. Asymptotically the improvement is a
factor of two in the oracle dimension: βkey /n → 1 under the model of [HAWK25,
§5.1] while ours is n/2 + 1. With the provable sieve of [ADRS15] as the oracle
this gives time 2(n/2+1)+o(n) unconditionally.


Table 1. Cost of one SVP-oracle call. β is the oracle dimension: βkey [HAWK25, Table 7]
for the spec, n/2 + 1 for the attack. ∗ Core-SVP is our conversion 20.292β (exponent
rounded to the nearest integer); the specification reports blocksizes and AGPS20 gate
counts only. AGPS20 gates are the classical list-decoding gate counts of [AGPS20]
at sieve dimension βeff = β − d4f(β), with dimensions-for-free [Duc18] computed and
rounded as in [HAWK25, §5.3]. † HAWK-256 is a challenge parameter set [HAWK25,
§3.2], for which the specification states no gate count (the entry 274 at βkey is our
computation); §6.2 reports actual recoveries.

                          n           β         Core-SVP∗      AGPS20 gates
                               Spec Attack Spec Attack Spec           Attack
         HAWK-256  256
                     †
                                211       129   262
                                                       2 38
                                                               274
                                                                       252
         HAWK-512  512          452       257   2132   275     2141    286
         HAWK-1024 1024         940       513   2274   2150    2278    2158


    The HAWK specification reports total key-recovery costs of 2150 and 2288 gates
for HAWK-512 and HAWK-1024 [HAWK25, §5.3], computed as n · Cgate (βeff ):
12     Z. Straznickas and S. Weis

Cgate is the AGPS20 gate count of one sieve call [AGPS20], βeff = βkey −d4f(βkey ),
and n is the spec’s lower bound on the number of oracle calls in one BKZ tour.
Under the same model at our dimension n/2 + 1 (so βeff = 224 and 464 after
dimensions-for-free), the per-call costs are 286.0 and 2157.8 ; multiplying by the
call count below gives totals of at most 2108 and 2182 .
    The reduction makes O(n2 log n) oracle calls in at most three reduction runs:
one Algorithm 1 run in step (2) and at most two Zn -LIP runs in step (3), each
preceded by LLL. After LLL every basis vector has squared norm at most 2n ,
since ∥bi ∥2 ≤ 2D−1 λi (Λ)2 for rank√D [LLL82, p. 518] and the successive minima
λi are key-independent (at most 2 and 1 for steps (2) and (3) respectively, by
Propositions 4.5 and D.2). At this input size, the iteration bound of Theorem
5.1 is (n/2+1)2 ln(n/2+1) + O(n log n) for step (2), and that of Remark D.3 is
(n+1)(n/2+1) ln(n/2+1) + O(n log n) per step-(3) run; each iteration makes two
oracle calls, and the terminal HKZ reductions add O(n). The totals come to at
most 221.9 and 224.0 calls for HAWK-512 and HAWK-1024, with the input basis
entering only through a doubly-logarithmic term contributing under 1%.
    Only the SVP-oracle calls are priced, on both sides. The polynomial-time
arithmetic outside the oracle (HNF, LLL, Gram updates, the parity tests of step
(3)) is omitted, as is the non-oracle cost of a BKZ tour in the specification’s
count. Neither side prices memory access, the progressivity factor of roughly 25
[SAB22, §5.2.1], or the overheads of [Duc22]; the latter two are explicitly set
aside in [HAWK25, §5.3].
   A heuristic estimate in the specification’s own methodology goes further:
under the GSA-intersect model of Appendix C, progressive BKZ reaches the
minimum of the rescaled cocycle lattice — a τ -cocycle, by Lemma 4.4 — at
blocksize 205 (HAWK-512) and 432 (HAWK-1024) rather than the proven oracle
dimension n/2 + 1, giving heuristic key-recovery costs of about 280.8 and 2146.5
gates against the specification’s 2150 and 2288 . The provable totals above are thus
conservative by roughly a further 227 and 235 ; Appendix C gives the conversion
and its caveats.


6.2   Implementation and key recovery for HAWK-256

We implemented the attack as a released end-to-end program [code] and recovered
the secret keys of two HAWK-256 public keys generated by the reference key
generator [HAWK25]. The implementation follows steps (1)–(3) of Theorem 6.1,
replacing the provable LIP solvers with heuristic lattice reduction and taking
two shortcuts in step (3); the theorem’s cost bound does not depend on either.
                                                                 (τ )
   Step (1) constructs the 256 × 256 integer Gram matrix of ΛB via an integer
Hermite-normal-form kernel computation followed by LLL reduction of the
resulting basis.
   Step (2) BKZ-reduces this Gram matrix with fpylll to blocksize 44 and runs
a progressive BGJ-type sieve [BGJ15], using the AMX implementation of Zhao,
Ding, and Yang [ZDY25], to a maximum sieving dimension of 118. The sieve
              HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1              13

                                              (τ )
returns two shortest vectors Y, Y ′ of ΛB not related by sign. A sieve database
contains some shortest vectors long before it provably contains all of them;
Remark 6.2 is what makes two enough.
   Remark 6.2 (intertwiner sublattice). Let Y, Y ′ be shortest vectors of
 (τ )
ΛB with Y   ̸= ±Y ′ and neither equal to ±Vτ , and set M := Y · adj(Y ′ ). The
rank-n/2 sublattice

                                       (τ )
                        Λa := {X ∈ ΛB : M X = Xτ (M )}

is cut out by one further public linear system (its coefficients involve only Q, Y ,
Y ′ ), and its two shortest vectors are ±Vτ (proof in Appendix D). The hypothesis
that neither sieve output equals ±Vτ is testable by the parity test of Appendix
D; when it fails the construction is unnecessary.
    The implementation locates ±Vτ directly from Λa : it computes an explicit
Z-basis of this rank-128 lattice and runs LLL followed by progressive BKZ;
blocksize at most 24 sufficed in every run. It then reaches an equivalent key by a
τ -tower descent from ℓ = 9 down to ℓ = 3 (Appendix D, after Lemma D.4) in
place of the single Zn -LIP solve of step (3); each level re-runs steps (1)–(2) at
half the degree, and the resulting rank-128 cocycle lattice at the ℓ = 8 level was
solved at BKZ blocksize at most 16, every lower level by LLL alone. We make
no provable claim for the tower descent; the provable path remains the single
Zn -LIP solve.
    Every attempt succeeded. For one of the two keys, two independent runs each
produced a solution: distinct but unitarily-equivalent secret keys, both passing
the reference implementation’s sign/verify check. A recovery completes within a
few hours on a single 96-core Sapphire Rapids server, dominated by the step-(2)
sieve. The release is a single-command pipeline with per-stage checkpoints that
verifies its output against the HAWK reference implementation as its final step;
Appendix A lists the lemma checks and the (heuristic) end-to-end runs at small
ℓ. For HAWK-512 the proven oracle dimension is 257; we have not attempted it.


7    Scope of the Attack

The attack requires two ingredients: a τ -cocycle lattice (§4), and a half-dimension
reduction for its isometry class (§5, Appendix E). The first is settled by:
   Theorem 7.1. An order-2 Galois element τ ̸= c of Q(ζm ) — and hence the
construction of §4 — exists iff (Z/m)× is non-cyclic, iff m ∈
                                                            / {1, 2, 4, pk , 2pk } for
p an odd prime.
     Proof. §4 requires an order-2 Galois element τ ̸= c; by Lemma B.1 one exists
iff (Z/m)× is non-cyclic. □
    For the second, Theorem 6.1 is proven only for powers of two, but for every
non-cyclic m the cocycle lattice has Vτ as a shortest vector with minimum φ(m)/4
(the proof of Lemma 4.4 uses only τ 2 = 1, τ ̸= c), and we expect heuristic lattice
14      Z. Straznickas and S. Weis

reduction to find it at blocksize somewhat below φ(m)/2 (roughly 0.36–0.42 φ(m)
at the power-of-two parameter sets under the model of Appendix C) whenever
m has a small prime factor: preliminary computations at small parameters for
m = 4p and m = 3 · 2ℓ suggest the cocycle lattice  √ satisfies the hypothesis of
[BN24, Thm 1] with the same constant λ1 λ∨   1 → 1/  2 as the power-of-two case.
   Conductors m ∈ {pk , 2pk } (and the degenerate m ≤ 4) evade the construction.
Over those fields the rank-3φ(m)/2 c-cocycle of §8.3 still applies, with blocksize
roughly 0.72 βkey under the same model (Appendix C).


8     Relation to Prior Work

8.1   Subfield attacks

The NTRU subfield attack of Albrecht, Bai, and Ducas [ABD16] norms the
public key h 7→ NKn /E (h) to a subfield E; the subring variant of Kirchner and
Fouque [KF17] instead restricts the multiplication-by-h matrix to a subring of
the same index. Kirchner and Fouque prove a complexity bound [KF17, Thm 7]
that depends on the secret width only through n log σsk (where σsk is the width
of the NTRU secret), a quantity they observe is invariant under subfield descent
[KF17, §4.2], so descent gains nothing at non-overstretched parameters. By
contrast, the cocycle Vτ of §4 has det Vτ = 1 and Q(τ ) (Vτ ) = n/4 regardless of
the key-generation distribution (Lemma 4.4), so the conservation argument has
no analogue; the construction of §4 involves neither a modulus nor a subfield
descent.


8.2   Gentry–Szydlo and quaternion methods

Gentry and Szydlo [GS02, §8] propose extending their algorithm to recover f
from a basis of (f ) and the relative norm of f over an index-2 subfield only “where
the degree-2 extension is complex conjugation”. Every subsequent module-LIP
reduction we are aware of — to a relative- or reduced-norm principal-ideal problem
[MPPW24; Che25; APvW25], via the symplectic automorphism [LJPW24], or via
the Hermitian square-basis oracle of [EP24] — likewise uses no Galois involution
other than complex conjugation. The construction of this paper instead uses
the involution τ , whose fixed field Knτ = Q(ζ2ℓ−1 ) is complex cyclotomic; the
resulting public lattice has rank n rather than 2n, and the reduction target is
SVP in dimension n/2 + 1 rather than a principal-ideal problem.


8.3   Comparison with the c-cocycle

Chevignard et al. [Che25, §1] construct a rank-2n lattice from the public key
whose shortest vector is the secret (their d is our n); for HAWK it is hypercubic,
and they show a single SVP call in dimension 2n breaks the scheme. Replacing
             HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1               15

τ by c throughout §4 gives a related c-cocycle lattice of rank 3n/2: constraint
(C2) degenerates to “QY symmetric” (since σ = c2 = id), so it is not the lattice
of [Che25], which imposes neither (C1) nor (C2). For τ ̸= c, σ = cτ ̸= id is
itself an order-2 automorphism and (C2) is an independent n/2-dimensional
restriction; this rank saving is the source of the factor-2 blocksize improvement.
The third involution σ gives the same rank n, since the proofs use only τ 2 = 1,
cτ ̸= 1, [Kn : Knτ ] = 2, and the power-of-two trace orthogonality, all of which
hold with τ ↔ σ. Higher-order Galois elements admit no adj-linearized analogue
of (C1), since the linearization of γ(Y ) = Y −1 requires γ 2 = id; we found no
useful replacement.


8.4   The reductions of Ducas and of Bambury–Nguyen

Ducas [Duc23] solves Zd -LIP with polynomially many SVP-oracle calls in di-
mension ⌊d/2⌋ + 1, by a two-block reduction whose progress lemma [Duc23,
Lemma 4] bounds the per-round drop of an integer potential. Bambury and
Nguyen [BN24] extend the early-abort form of the reduction to any sublattice of
ZD with λ1 (Λ)λ1 (Λ∨ ) < 1 − ε, returning one short primal or dual vector at the
same oracle dimension. As noted in §5, we run Ducas’s algorithm on the class
[Λ′ ], where his progress lemma fails and Appendix E supplies the replacement;
Remark E.5 compares the two routes in detail.


8.5   Lattice automorphisms and van Gent–Pulles

Van Gent and Pulles [GP25] show that, given any Z-automorphism of the public
form outside the trivial group generated by the roots of unity and the symplectic
automorphism of [LJPW24], smLIP reduces to BKZ on a kernel sublattice of half
the rank: their Propositions 1–2 construct the kernel and recover the key from a
short vector of it, deterministically and in polynomial time, and their Theorem 1
estimates the BKZ cost heuristically. §5 and Appendix D run their descent on
the automorphisms x 7→ Y τ (x) that the shortest vectors of the cocycle
                                                                    √      lattice
supply (Lemma D.1); Appendix D identifies the kernel exactly as n Zn , which
lets Ducas’s algorithm replace the heuristic BKZ step.


9     Discussion and Open Questions

One attempt to halve the oracle dimension again, to n/4 + 1, by running Algo-
rithm 1 at cut ⌊p/2⌋, is blocked: the loop reaches the non-terminal fixed point
S = Z⌊p/2⌋ ⊂ Zp (where vol(S) = 1 and the product-progress quantity of Lemma
E.2 equals 1), and for n > 8 the residual back-block LIP still requires SVP(n/2−1)
by duality
    √      and Corollary E.4. As a generic [Λ′ ]-LIP problem this would require a
gap- 2 Rankin solver below half-dimension, for which no technique is known.
                                                                            (τ )
   The HAWK instance carries structure a generic member of [Λ′ ] lacks: ΛB is
publicly a rank-4 quadratic OF -lattice (for f ∈ OF , both (C1) and (C2) commute
16        Z. Straznickas and S. Weis

with multiplication by f , and φτ (f Y ) = f φτ (Y )), with OF -valued form det Y .
Since F is totally real its only roots of unity are ±1, which appears to rule out
the known structured-sieve speedups; we leave open whether this rank-4 module
structure admits a solver with SVP-oracle dimension below n/2.


10    Acknowledgements and Disclosures

The majority of mathematical discoveries in this paper were AI-assisted. Human
author contribution mainly consisted of directing, organizing and verifying AI
work. The write-up was partially AI-assisted but was reviewed and edited by the
authors.
   We thank Thomas Pornin and the rest of the HAWK team for reviewing the
work, and especially for feedback on proper attribution for some of our attack’s
components — something AI-assisted work makes more difficult.


References

[ABD16]         M. R. Albrecht, S. Bai, and L. Ducas. “A subfield lattice attack on
                overstretched NTRU assumptions: Cryptanalysis of some FHE and
                graded encoding schemes”. In: CRYPTO 2016, Part I. Ed. by M.
                Robshaw and J. Katz. Vol. 9814. LNCS. Springer, 2016, pp. 153–
                178. url: https://doi.org/10.1007/978-3-662-53018-4_6.
[ADRS15]        D. Aggarwal, D. Dadush, O. Regev, and N. Stephens-Davidowitz.
                “Solving the shortest vector problem in 2n time using discrete
                Gaussian sampling”. In: STOC 2015. ACM, 2015, pp. 733–742.
[AGPS20]        M. R. Albrecht, V. Gheorghiu, E. W. Postlethwaite, and J. M.
                Schanck. “Estimating quantum speedups for lattice sieves”. In:
                ASIACRYPT 2020. Vol. 12492. LNCS. Springer, 2020, pp. 583–
                613.
[Ala26]         G. Alagic, M. Bros, P. Ciadoux, Q. Dang, T. H. Dang, J. Kelsey, J.
                Lichtinger, Y.-K. Liu, C. Miller, D. Moody, R. Peralta, R. Perlner,
                A. Robinson, H. Silberg, D. Smith-Tone, and N. Waller. Status
                Report on the Second Round of the Additional Digital Signature
                Schemes for the NIST Post-Quantum Cryptography Standardiza-
                tion Process. NIST Internal Report 8610. NIST, 2026. url: https:
                //doi.org/10.6028/NIST.IR.8610.
[APvW25]        B. Allombert, A. Pellet-Mary, and W. van Woerden. “Cryptanalysis
                of rank-2 module-LIP: A single real embedding is all it takes”. In:
                EUROCRYPT 2025. Vol. 15602. LNCS. Springer, 2025, pp. 184–
                212. url: https://doi.org/10.1007/978-3-031-91124-8_7.
[BDGL16]        A. Becker, L. Ducas, N. Gama, and T. Laarhoven. “New directions
                in nearest neighbor searching with applications to lattice sieving”.
                In: SODA 2016. SIAM, 2016, pp. 10–24.
            HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1        17

[BGJ15]   A. Becker, N. Gama, and A. Joux. Speeding-up lattice sieving with-
          out increasing the memory, using sub-quadratic nearest neighbor
          search. Cryptology ePrint Archive, Report 2015/522. 2015. url:
          https://eprint.iacr.org/2015/522.
[BN24]    H. Bambury and P. Q. Nguyen. “Improved provable reduction of
          NTRU and hypercubic lattices”. In: Post-Quantum Cryptography –
          PQCrypto 2024. Vol. 14772. LNCS. Springer, 2024, pp. 343–370.
[Che25]   C. Chevignard, G. Mureau, T. Espitau, A. Pellet-Mary, H. Pliatsok,
          and A. Wallet. A reduction from Hawk to the principal ideal problem
          in a quaternion algebra. EUROCRYPT 2025. 2025.
[code]    hawk_recover. hawk_recover: attack implementation and lemma-
          verification scripts for §6.2. github.com/anthropics/cryptography-
          research-demo.
[DPPvW22] L. Ducas, E. W. Postlethwaite, L. N. Pulles, and W. van Woerden.
          “HAWK: Module LIP makes lattice signatures fast, compact and
          simple”. In: Advances in Cryptology – ASIACRYPT 2022, Part IV.
          Ed. by S. Agrawal and D. Lin. Vol. 13794. LNCS. Springer, 2022,
          pp. 65–94. url: https://doi.org/10.1007/978-3-031-22972-
          5_3.
[Duc18]   L. Ducas. “Shortest vector from lattice sieving: a few dimensions
          for free”. In: EUROCRYPT 2018. Vol. 10820. LNCS. Springer,
          2018, pp. 125–145.
[Duc22]   L. Ducas. “Estimating the hidden overheads in the BDGL lattice
          sieving algorithm”. In: PQCrypto 2022. Springer, 2022, pp. 480–
          497.
[Duc23]   L. Ducas. “Provable lattice reduction of Zn with blocksize n/2”. In:
          Des. Codes Cryptogr. 92.4 (2024), pp. 909–916.
[DvW21]   L. Ducas and W. van Woerden. On the lattice isomorphism prob-
          lem, quadratic forms, remarkable lattices, and cryptography. EU-
          ROCRYPT 2022. 2022.
[EP24]    T. Espitau and H. Pliatsok. On Hermitian decomposition lattices
          and the module-LIP problem in rank 2. Cryptology ePrint Archive,
          Report 2024/1148. 2024. url: https://eprint.iacr.org/2024/
          1148.
[GP25]    D. M. H. van Gent and L. N. Pulles. “HAWK: Having automor-
          phisms weakens key”. In: IACR Communications in Cryptology 2.2
          (2025). art. 20. url: https://doi.org/10.62056/a3qjp2w9p.
[GS02]    C. Gentry and M. Szydlo. “Cryptanalysis of the revised NTRU
          signature scheme”. In: EUROCRYPT 2002. Ed. by L. R. Knudsen.
          Vol. 2332. LNCS. Springer, 2002, pp. 299–320.
[HAWK25] J. W. Bos, O. Bronchain, L. Ducas, S. Fehr, Y.-H. Huang, T.
          Pornin, E. W. Postlethwaite, T. Prest, L. N. Pulles, and W. van
          Woerden. HAWK. Tech. rep. version 1.1, submission to the NIST
          PQC additional-signatures call. National Institute of Standards
          and Technology, 2025. url: https://hawk-sign.info.
18       Z. Straznickas and S. Weis

[KF17]         P. Kirchner and P.-A. Fouque. “Revisiting lattice attacks on over-
               stretched NTRU parameters”. In: EUROCRYPT 2017, Part I.
               Vol. 10210. LNCS. Springer, 2017, pp. 3–26.
[LJPW24]       H. Luo, K. Jiang, Y. Pan, and A. Wang. “Cryptanalysis of rank-2
               module-LIP with symplectic automorphisms”. In: ASIACRYPT
               2024. Springer, 2024, pp. 359–385.
[LLL82]        A. K. Lenstra, H. W. Lenstra Jr., and L. Lovász. “Factoring poly-
               nomials with rational coefficients”. In: Math. Ann. 261.4 (1982),
               pp. 515–534.
[MPPW24]       G. Mureau, A. Pellet-Mary, H. Pliatsok, and A. Wallet. Crypt-
               analysis of rank-2 module-LIP in totally real number fields. EURO-
               CRYPT 2024. 2024.
[NIST22]       NIST. Call for additional digital signature schemes for the post-
               quantum cryptography standardization process. 2022. url: https:
               //csrc.nist.gov/projects/pqc-dig-sig.
[PFH20]        T. Prest, P.-A. Fouque, J. Hoffstein, P. Kirchner, V. Lyuba-
               shevsky, T. Pornin, T. Ricosset, G. Seiler, W. Whyte, and Z.
               Zhang. FALCON. Tech. rep. Specification v1.2 (2020-10-01). NIST
               Post-Quantum Cryptography Standardization Process, 2020. url:
               https://falcon-sign.info.
[SAB22]        P. Schwabe, R. Avanzi, J. Bos, L. Ducas, E. Kiltz, T. Lepoint, V.
               Lyubashevsky, J. M. Schanck, G. Seiler, and D. Stehlé. CRYSTALS-
               Kyber. Tech. rep. v3.02. NIST PQC submission, 2021.
[ZDY25]        Z. Zhao, J. Ding, and B.-Y. Yang. “Sieving with streaming memory
               access”. In: IACR Trans. Cryptogr. Hardw. Embed. Syst. 2025.2
               (2025). Software: https : / / github . com / zhaoziyu0008 / BGJ -
               Sieve - AMX, pp. 362–384. url: https : / / doi . org / 10 . 46586 /
               tches.v2025.i2.362-384.
              HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1                19

A     Computational Verification

The released code [code] is the heuristic implementation of §6.2, not the provable
reduction of §5: its SVP stage is progressive BKZ plus a sieve. An accompanying
                                                     p key at ℓ ≤ 6:p
script re-derives the §4 statements exactly on a random               Lemmas 4.1–
4.4 and Proposition 4.5, including the isometry class n/4 Zn/2+1 ⊕ n/2 Zn/2−1
and the shortest-vector count 2(n/2 + 1) by exact enumeration. End-to-end, the
same code recovers keys on synthetic instances at ℓ = 5, 6, 7, 8 in 0.7 s, 1.4 s, 19
s, and 8.6 minutes respectively (single core; BKZ alone reaches the minimum
for n ≤ 128), and on HAWK-256 keys at ℓ = 9. Instances at ℓ ≤ 8 are synthetic
(a random SL2 (Rn ) basis from a reimplemented generator); at ℓ = 9 keys are
generated, and every recovered key is checked by a sign/verify round-trip, using
the official HAWK submission package [HAWK25].


B     Involutions of (Z/m)×

The following lemma is the group-theoretic input to Theorem 7.1; we include its
proof for completeness.
    Lemma B.1. For m ≥ 1 the following are equivalent: (i) (Z/m)× contains
an element of order 2 other than −1; (ii) (Z/m)× is non-cyclic; (iii) m ∈  /
{1, 2, 4, pk , 2pk } for p an odd prime.
    Proof. By the Chinese Remainder Theorem, (Z/m)× ∼     (Z/pki )× over the
                                                       Q
                                                    =              i     i
prime-power factors pki i of m. Each factor with pi odd is cyclic (the primitive
root theorem) of order pki i −1 (pi − 1), which is even; (Z/2)× is trivial, (Z/4)× is
cyclic of order 2, and (Z/2k )× ∼ = Z/2 × Z/2k−2 is non-cyclic for k ≥ 3.
                      / {1, 2, 4, pk , 2pk } then either 8 | m, in which case the factor
    (iii) ⇒ (i): if m ∈
     k ×
(Z/2 ) with k ≥ 3 already contains (Z/2)2 in its 2-torsion, or the decomposition
has at least two factors of even order (this happens when two distinct odd primes
divide m, or when one odd prime divides m and 4 | m). When there are at least
two even-order factors, the element that reduces to −1 in one of them and to
+1 in every other factor has order 2 and differs from −1 in a second even-order
factor. Either way the 2-torsion subgroup has order at least 4 and contains an
involution other than −1.
    (i) ⇒ (ii): for m > 2 the class of −1 has order 2, so (i) provides two distinct
elements of order 2; a cyclic group has at most one. (For m ≤ 2 the group is
trivial and (i) is false.)
   (ii) ⇒ (iii): contrapositively, for m ∈ {1, 2, 4, pk , 2pk } the decomposition has
at most one nontrivial factor, which is cyclic. □


C     The 0.72 βkey estimate of §7

Throughout this appendix m is the conductor and d+ := [Kn+ : Q] = φ(m)/2
(d+ = n/2 for the power-of-two parameter sets). The blocksize model is the
20      Z. Straznickas and S. Weis

heuristic GSA-intersect estimate (GSA: Geometric Series Assumption), as used
for [HAWK25, Table 8]: an unusually short vector of length ν in a rank-d lattice
of volume V is found by progressive BKZ at the smallest β with

                                β/d ν ≤ δβ2β−d−1 V 1/d ,
                            p

                                       β 1/(2(β−1))
                                         
                                δβ = 2πe            ,

a condition that depends only on d and the gap ln ν − d1 ln V; the gap-0 instance
is [DPPvW22, eq. (4)].
                                                                               
    For every conductor, the c-cocycle parametrization at B = I is W = ab c(a)b

with a ∈ Rn , b ∈ Rnc=−1 , det W = |a|2 + |b|2 , and Q(c) (W ) = TrKn+ (det W ) =
1            1                    2     2   +              +
2 ⟨a, a⟩Kn + 2 ⟨b, b⟩Kn (using |a| , |b| ∈ Kn and [Kn : Kn ] = 2). As in Lemma
4.4 with Kn+ in place of F , the minimum is TrKn+ (1) = d+ , attained at the secret
cocycle B −1 c(B), so ν = d+ .
                           p

    Power-of-two conductors. The key lattice is a scaled Z2n , gap 0; the model
gives βkey = 221/457/933, within ±10 of the simulated values 211/452/940 of
[HAWK25, Table 7] and within ±1 of [HAWK25, Table 8]. For the c-cocycle        √
lattice, the trace-orthogonal power basis (§3.3) gives (Rn , ⟨·, ·⟩Kn ) = n Zn ,
and c acts on that basis as a signed permutation with one fixed point (1),
one
√ antifixed
         √     point (ζ n/2 ), and d+ − 1 sign-2-cycles, giving (Rnc=−1 , ⟨·, ·⟩Kn ) =
  n Z ⊕ 2n Zd+ −1 by the per-cycle accounting of the proof of Proposition 4.5.
Hence ΛI ∼
         (c)
             = d+ Z2d+ +1 ⊕ 2d+ Zd+ −1 , gap ≈ − 16 ln 2.
               p                p

    Power-of-two τ -cocycle. The same √      model applies to the rescaled cocycle
lattice of Corollary 4.6, Λ′ = Zn/2+1 ⊕ 2 Zn/2−1 : rank d = n, ν = 1, V =
2(n/2−1)/2 , so the gap is − n/2−1         1
                               2n ln 2 ≈ − 4 ln 2. The model then gives blocksizes
92/205/432 at HAWK-256/-512/-1024, that is 0.42–0.46 of the same-model βkey
above and somewhat below the oracle dimension n/2 + 1 of Theorem 6.1; the next
paragraph converts these into the gate counts quoted in §6.1. The ±10 calibration
against the simulated blocksizes is for the key lattice only; a simulator run on
the class [Λ′ ], as was done for the key lattice in [HAWK25, Table 7], would be
the proper counterpart.
    Odd-prime-power conductors. The power basis is not orthogonal, so
            P has gap 0. The key-lattice minimum is φ(m): for x ∈ Rn \ {0},
neither lattice
TrKn |x|2 = σ |σ(x)|2 ≥ φ(m) |N (x)|2/φ(m) ≥ φ(m) by AM–GM and |N (x)| ≥
1, with equality iff x is a root of unity. The volumes follow from |disc Kn | and a
closed form for det(Rnc=−1 , ⟨·, ·⟩Kn ), both checked against exact linear algebra at
m ∈ {5, 7, 9, 11, 13, 25, 27}.
   Ratio. Across every conductor we computed, βc-cocycle /βkey ∈ [0.69, 0.73]:
0.71–0.72 at HAWK-512 and HAWK-1024, 0.72–0.73 for odd-prime-power con-
ductors of comparable degree (m = 769, 1153, 37 , 55 , 2309), and 0.69–0.73 at
HAWK-256 depending on whether the denominator is the simulated or same-
model βkey . The ratio 3/4 suggested by the ranks alone is corrected downward
              HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1             21

chiefly by the 21/6 volume excess: the cocycle target is relatively shorter in its
lattice than the unit vectors are in the key lattice.
    Gate-count conversion for §6.1. At the power-of-two τ -cocycle blocksizes
above (205 for HAWK-512, 432 for HAWK-1024), the recipe of [HAWK25, §5.3]
converts as follows: dimensions-for-free d4f(β) = β ln(4/3)/ ln(β/(2πe)), rounded,
with βeff lowered to a multiple of 8, gives 176 and 392; the classical list-decoding
gate counts of [AGPS20] are 271.8 and 2136.5 per call; and multiplying by n
for one tour gives the heuristic totals 280.8 and 2146.5 quoted in §6.1. Isolating
±Vτ from the shortest vectors (Remark 6.2) is cheaper by the same recipe. The
estimate counts only the top-level step-(2) reduction and prices the final descent
by the τ -tower of §6.2; the alternative, a direct reduction on the Zn -LIP kernel of
step (3), would cost more (285.5 and 2153.6 ). Each tower level repeats the top-level
computation at half the degree and is cheaper by the same recipe (the n = 256
level costs about 251 , the n = 512 level about 281 ), so the top level dominates
the tower. The blocksizes are GSA-intersect estimates rather than the simulated
ones behind [HAWK25, Table 7], a difference of about ±10 in β, or ±2.4 bits;
memory, the progressivity factor, and the overheads of [Duc22] remain unpriced
on both sides, as in §6.1.


D    The Descent as a Strengthened Analysis of van
     Gent–Pulles

                                                                        (τ )
Throughout, Y denotes one of the 2(n/2 + 1) shortest vectors of ΛB , so that
Y τ (Y ) = I and det Y = 1 (Lemma 4.4(ii)), hence Y −1 = τ (Y ), and Y ∗ QY =
τ (Q): by (C2), Y ∗ QY = Y ∗ σ(Y )T τ (Q), and Y ∗ σ(Y )T = (σ(Y ) c(Y ))T =
σ(Y τ (Y ))T = I using cτ = σ and (C1).
    Lemma D.1. The map UY : Rn2 → Rn2 , x 7→ Y τ (x), is an order-2 automor-
phism of the quadratic Z-module (Rn2 , T ), T (x, y) = TrKn (x∗ Qy), lying outside
the trivial group Gn of [GP25] (generated by the roots of unity and the symplectic
automorphism, the latter included after [LJPW24]); and ker(UY − 1) = MY ,
ker(UY + 1) = M−Y .
     Proof. Order 2: UY2 (x) = Y τ (Y ) x = x by the cocycle equation. Isom-
etry: T (UY x, UY y) = TrKn (τ (x)∗ Y ∗ QY τ (y)) = TrKn (τ (x)∗ τ (Q) τ (y)) =
TrKn (τ (x∗ Qy)) = T (x, y), using Y ∗ QY = τ (Q), τ (x)∗ = τ (x∗ ) (the involutions
c and τ commute), and the Galois-invariance of the trace. Exclusion: UY is
τ -semilinear (UY (αx) = τ (α) UY (x) for α ∈ Rn ), while every element of Gn is Rn -
linear and τ ̸= id. Kernels: UY x = ±x ⇐⇒ τ (x) = (±Y )−1 x ⇐⇒ x ∈ M±Y ,
using Y −1 = τ (Y ). □
   In the terminology of [GP25], UY lies in the orthogonal group of the public
form outside their trivial group, M±Y = ker(UY ∓ 1) are the kernel sublattices of
[GP25, Prop. 2], and [GP25, Prop. 1] — proved there, deterministic polynomial
time — recovers an equivalent key from any sufficiently short kernel vector.
                                                                          √
[GP25, Lem. 3 and Prop. 2] prove that these kernels are of the form Zs ⊕ 2 Zt
22       Z. Straznickas and S. Weis
                            √
for some s, t ≥ 0 with λ1 ≤ 2 — enough for the heuristic pricing of [GP25,
Thm. 1], but not enough to determine the split (s, t), which differs between
Y = ±Vτ and the√other candidates. The proofs below identify the kernels exactly
— (M±Vτ , T ) ∼
              = n Zn , with the columns of B −1 up to roots of unity as shortest
vectors — and this exactness is what admits the provable solver of [Duc23]
(Remark D.3) and so upgrades the endgame from the heuristic pricing of [GP25,
Thm. 1] to the unconditional accounting of Theorem 6.1.
                                        (τ )
     Proposition D.2. Let Y ∈ ΛB be a shortest vector with φτ (Y ) = ±I. Then:

 1. MY = B −1 OK   2
                     τ (resp. B
                                 −1
                                    (ζOKnτ )2 for −I), a Z-lattice of rank n;
                 √   n
 2. (MY , T ) ∼= nZ ;  n

 3. the shortest vectors of (MY , T ) are {±B −1 ζ 2j ek : 0 ≤ j < n/2, k ∈ {1, 2}}
    (resp. {±B −1 ζ 2j+1 ek } in the −I case), where e1 , e2 is the standard basis of
    Rn2 ; any pair (u1 , u2 ) from this set with u∗1 Qu2 = 0 satisfies [u1 u2 ]−1 ∈
    U2 (Rn ) · B, an equivalent HAWK secret key. (Here [u1 u2 ] is the matrix with
    columns u1 , u2 .)

    Proof. (1) For Y = Vτ : τ (x) = Vτ−1 x = τ (B)−1 Bx ⇔ τ (Bx) = Bx ⇔ Bx ∈
(Kn ) . Intersecting with Rn2 and using BRn2 = Rn2 (B ∈ SL2 (Rn )) and Rn ∩ Knτ =
   τ 2

OKnτ : MY = B −1 OK     2
                           τ . For Y = −Vτ , τ (Bx) = −Bx gives MY = B
                           n
                                                                                     −1
                                                                                        (ζOKnτ )2 .
(2) For x = B y: x Qx = y (B ) QB y = y y, so T (x, x ) = TrKn (y ∗ y ′ ).
                   −1      ∗          ∗     −1 ∗      −1      ∗              ′
                                                                                      ′
On the basis {ζ 2j ek : 0 ≤ j < n/2, k ∈ {1, 2}} of OK          2
                                                                  τ : TrKn (ζ
                                                                  n
                                                                               2j ζ 2j ) = n δ ′ .
                                                                                              j,j
Hence Gram = nIn . (3) The shortest vectors of a lattice in class [Zm ] are
its orthogonal Z-basis up to sign, so here {±B −1 ζ 2j ek }. For any two of these,
                             ′            ′
(B −1 ζ 2j ek )∗ Q(B −1 ζ 2j ek′ ) = ζ 2(j −j) δk,k′ , which vanishes iff k ̸= k ′ . For such a
pair, [u1 u2 ] = B −1 M with M a monomial matrix whose nonzero entries are
2n-th roots of unity, hence M ∈ U2 (Rn ) and [u1 u2 ]−1 ∈ U2 (Rn ) · B. □
     Selecting ±Vτ : the parity test. The other n shortest vectors do not
lead to the key: for Y with φτ (Y ) = W (0, ω), ω = ζ j with j odd (proof of
Lemma 4.4(ii)), the substitution y = Bx of Proposition D.2’s proof turns the
                                             −1                                    ′
defining condition of MY into      √y2 =n−ω τ (y1 ) with y1 ∈ Rn free, and T (x, x ) =
             ′                  ∼
2 TrKn (y1 y1 ), so (MY , T ) = 2n Z , whose shortest vectors carry no orthonormal
pair. The two useful candidates are recognized by reduction modulo 2: since
τ (ζ i ) = (−1)i ζ i ≡ ζ i , the involution τ acts trivially on Rn /2Rn , so τ (B) ≡ B
and ±Vτ = ±B −1 τ (B) ≡ I (mod 2); whereas any other shortest vector Y =
B −1 W (0, ω)τ (B) ≡ B −1 W (0, ω)B ̸≡ I (mod 2), because B is invertible modulo
2 (as det B = 1), so conjugation by it is a bijection of M2 (Rn /2Rn ) fixing I,
and W (0, ω) has zero diagonal. Thus exactly the two candidates ±Vτ satisfy
Y ≡ I (mod 2Rn ), an O(n)-coefficient check. (The reduction does require the
exact shortest vectors: MY ̸= 0 iff det Y = 1, so an approximate-SVP output Y ′
with Q(τ ) (Y ′ ) > n/4 gives MY ′ = {0}.)
   Remark D.3 (improved iteration count for [Duc23]). The two-bound
termination analysis of Theorem 5.1 (in the notation of its proof, §E.4: po-
tential Wt , primal factor α) applies to [Duc23, Alg. 1] on a lattice in [Zd ],
               HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1                 23

d = 2k ′ + 1: after the primal step the front block L(B[0:k′ ] ) is a primitive
                                          1/2
rank-(k ′ +1) sublattice of volume Wt α with α ≤ 1 [Duc23, Lemma 3], its
                           1/2
dual has covolume (Wt α)−1 , and Minkowski’s theorem gives the same re-
                               1−1/(k′ +1)
cursion Wt+1 ≤ (k ′ +1) Wt                 ; the basic per-iteration factor is 1 − 1/d
[Duc23, Lemma 4]. The iteration count of [Duc23, Thm         2] therefore improves
to d 1 + (k ′ +1) ln(k ′ +1) + (k ′ +1) ln 2k ′ ln maxi ∥bi ∥ + 3(k ′ +1) for any input
basis, again doubly logarithmic in the input. Applied through the even-rank
adjustment Λ 7→ Λ ⊕ Z of [Duc23] (the rank-n lattice (MY , n1 T ) becomes the
odd rank n + 1), it gives (n+1)(n/2+1) ln(n/2+1) + O(n log n) iterations per
descent run under the LLL input bound of §6.1.
                                                         (τ )
    Lemma D.4 (the τ -tower step). Let Y ∈ ΛB be a shortest vector with
φτ (Y ) = ±I (so Y τ (Y ) = I, det Y = 1, and Y ≡ I (mod 2)), and write
K ′ := Knτ , O′ := OK ′ , so that Rn = O′ ⊕ ζO′ . Then (i) MY is the O′ -module
generated by the columns of (I + Y )/2 and (I − Y )/(2ζ) (both in M2 (Rn )), and
(ii) the alternating O′ -bilinear form µ(x, y) := 12 TrKn /K ′ det[x y] on MY is
unimodular: µ(f1 , f2 ) ∈ O′× for every O′ -basis (f1 , f2 ). Consequently any pair
(x, y) ∈ M2Y with µ(x, y) = 1 is a free O′ -basis of MY .
     Proof. (i) The matrices (I + Y )/2 and (I − Y )/(2ζ) are integral because
                                                                  I+Y −1
Y ≡ I (mod 2) and ζ is a unit. For a ∈ O′2 : τ I+Y                       a = Y −1 I+Y
                                                              
                                                         2 a =       2              2 a,
and likewise for (I − Y )/(2ζ) using τ (ζ) = −ζ, so both columns lie in MY .
Conversely, for x ∈ MY write x = a + ζb with a, b ∈ O′2 ; averaging x = a + ζb
                                                                                      ′2
with x = Y τ (x) = Y a − ζY b gives x = I+Y                  I−Y   2           2
                                                    2 a + 2ζ (ζ b) with ζ b ∈ O .
(ii) By Proposition D.2(1), MY = B −1 Ω O′2 with Ω = 1 (resp. Ω = ζ for
−I). For x = B −1 Ωu, y = B −1 Ωw with u, w ∈ O′2 , since det B = 1 we get
det[x y] = Ω 2 det[u w] ∈ K ′ , hence µ(x, y) = Ω 2 det[u w] (det[x y] is already τ -
fixed). For an O′ -basis (f1 , f2 ) = (B −1 Ωu1 , B −1 Ωu2 ) we have [u1 u2 ] ∈ GL2 (O′ ),
so µ(f1 , f2 ) = Ω 2 det[u1 u2 ] ∈ O′× . Finally, µ(x, y) = det(C) µ(f1 , f2 ) where
C ∈ M2 (O′ ) expresses (x, y) in the basis; if µ(x, y) = 1 then det C ∈ O′× and
(x, y) is a basis. □
   For the other shortest vectors (the case φτ (Y ) = W (0, ω), ω = ζ j , above)
the same computation gives µ with values in 2ζ 1−j O′ , never a unit — a second
reason that only ±Vτ descend.
    The τ -tower descent (§6.2). The implementation replaces the single
Zn -LIP solve of step (3) by a descent through the tower of τ -fixed subfields
Q(ζ) ⊃ Q(ζ 2 ) ⊃ Q(ζ 4 ) ⊃ · · · , i.e. from the conductor exponent ℓ down to 3. Each
level computes an OKnτ -basis of MVτ = B −1 OK      2
                                                      τ : by (i), the module is generated
                                                      n
by the columns of (I + Vτ )/2 and (I − Vτ )/(2ζ), and by (ii), a free basis is any
pair (x, y) with µ(x, y) = 1, obtained by a Bézout step in O′ (no class-group
computation). The level then Gauss-reduces this basis under the Q-Hermitian
form and recurses on the resulting HAWK public key over Knτ , re-running steps
(1)–(2) there to obtain the next level’s Vτ .
                                                                            (τ )
   Proof of Remark 6.2. Recall M := Y adj(Y ′ ) and Λa := {X ∈ ΛB : M X =
                                            (τ )
Xτ (M )} for shortest vectors Y ̸= ±Y ′ of ΛB , neither equal to ±Vτ . Transporting
24      Z. Straznickas and S. Weis

by the isometry φτ of Lemma 4.2, the condition M X = Xτ (M ) becomes N W =
W τ (N ) with N = φτ (Y ) · adj(φτ (Y ′ )); since φτ (Y ), φτ (Y ′ ) are shortest vectors
other than ±I, they have the form W (0, b) with b = ζ k , k odd (§4.3; proof
of Lemma 4.4(ii)), so N is diagonal. For W = W (a, b) the diagonal entries of
N W − W τ (N ) vanish identically and the off-diagonal entries vanish only for
                                                                                      (τ )
b = 0 (using Y ̸= ±Y ′ ), so φτ (Λa ) = {W (a, 0) : a ∈ Rnσ }, the summand of ΛI
containing ±I, whose two shortest vectors are ±I by Proposition 4.5. □


E    Correctness of Block Reduction on [Λ′ ]

                                                                √
This appendix proves that LIP for the class [Λ′ ] = [Zp ⊕ 2 Zq ] is solvable
with polynomially many calls to exact SVP in dimension p (Theorem 5.1). The
algorithm is Ducas’s two-block reduction [Duc23, Alg. 1], run unchanged on [Λ′ ] —
the same primal/dual loop at the same oracle dimension, with only the cut fixed
at k := p − 1 for this even-rank class and a final size-reduction made explicit;
what is new is the analysis, since Ducas’s integrality and progress lemmas are
proved only for Zd (Lemmas E.1–E.2 replace them, and this appendix re-derives
termination and correctness). The missing ingredient is the no-abort product-
progress bound for [Λ′ ]. In outline: the algorithm maintains a basis of the lattice
and alternates two SVP-oracle steps on projected blocks of dimension at most p:
a primal step that makes the Gram–Schmidt length ∥b⋆p−1 ∥ as short as possible
and a dual step that makes it as long as possible. The squared volume of the first
p − 1 basis vectors is a positive integer (Lemma E.1) that each primal-plus-dual
round multiplies by a factor at most 1 − 1/p (Lemma E.2), so after O(n2 log n)
rounds (for polynomially-bounded input) it reaches 1, at which point the front
block spans a copy of Zp−1 and the hidden orthogonal basis can be read off
(Theorem 5.1).
    Notation. A sublattice S of a lattice Λ is primitive if S = span(S) ∩ Λ;
vol(S) is its covolume (root-determinant of its Gram), πU (for a subspace U ) is
orthogonal projection onto U , πS⊥ is orthogonal projection onto span(S)⊥ , and
for S primitive in Λ one has S ∨ = πspan(S) (Λ∨ ). For a basis B = (b0 , . . . , bd−1 )
(unrelated to the secret key of §3.1) of a lattice L(B), b⋆i denotes the i-th
Gram–Schmidt vector (the star is unrelated to the adjoint ∗ ) and B[i:j] :=
  ⊥                                ⊥
(π{b 0 ,...,bi−1 }
                   (bi ), . . . , π{b 0 ,...,bi−1 }
                                                    (bj )) the projected block.
   Write {ej }p−1
               j=0 for√the standard basis of √  the Zp summand (norm 1) and
 √      q−1
{ 2fm }m=0 for the 2 Z summand (norm 2), and Rp , Rq ⊂ Rp+q for the
                           q

spans of the two families; the algorithm is given only the Gram matrix of an
arbitrary basis, so this orthogonal basis exists but is hidden, and finding it is
the task. Set k := p − 1 for the cut between the two blocks: the cut must satisfy
k < p for the front block to be able to terminate as an orthonormal subset of the
Zp summand (and for Lemma E.2’s Case 1 to find a unit vector outside it), and
k = p − 1, the largest such cut, keeps both blocks’ SVP dimensions at most p.
              HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1                25

E.1    Block reduction for Zd and its obstruction

Ducas [Duc23, Thms 1, 2] solves Zd -LIP with poly(d) SVP calls in dimension
⌊d/2⌋ + 1, via a 2-block slide reduction with invariant vol(B[0:k−1] )2 ∈ Z>0 . Its
                                                  d
progress lemma is [Duc23, Lemma
                        ⊥   d
                                    p 4]: if S ⊂ Z is primitive of rank k with
vol(S) > 1, then λ1 (πS (Z )) ≤ 1 − 1/d. This is the per-round drop of the
integer potential described above, for the hypercubic class.
                                                √                       2
    This lemma is false for Λ′ : take S = Zk−1 ⊕ 2 Z ⊂ Λ′ (rank
                                                             p k, vol = 2 > 1).
               ′                                ⊥   ′
Then ek−1 ∈ Λ , ek−1 ⊥ S, ∥ek−1 ∥ = 1, so λ1 (πS (Λ )) = 1 > 1 − 1/(p + q), so
the lemma fails.
    Nor can the input itself be transformed into a hypercubic class: the determinant
class in Q× /(Q× )2 of a rational quadratic form of even rank is unchanged by
rescaling, dualizing, and passing to a commensurable lattice, and for Λ′ that class
is 2q ≡ 2 (q odd) while for every rationally scaled hypercubic lattice it is 1. The
fix is to bound the product of the primal and dual steps’ contributions. The
dual lattice Λ′∨ = Zp ⊕ √12 Zq has its short vectors in the q-block — where Λ′
has its long vectors — so when the primal step stalls, the dual step compensates.


E.2    The integrality lemma

Lemma E.1 (Analogue of [Duc23, Lemma 2]). For any sublattice S ⊂ Λ′
of rank r ≥ 1: vol(S)2 ∈ Z>0 . If vol(S)2 = 1 then S ⊂ Zp and S ∼
                                                                = Zr .
    Proof. A Z-basis of S has the form M = ( C        A ) with A ∈ Zp×r , C ∈ Zq×r ,

and Gram GS = M T DM = AT A + 2C T C ∈ Zr×r , so vol(S)2 = det GS ∈ Z>0 .
Suppose det GS = 1. Reducing mod 2: det(AT A) ≡ 1 (mod 2), so det(AT A)
is odd, hence A has full rank r and AT A is positive-definite. The Minkowski
determinant inequality det(P +P ′ ) ≥ det P for P positive-definite and P ′ positive-
semidefinite (equivalently det(I + P −1/2 P ′ P −1/2 ) ≥ 1, since all eigenvalues of the
identity plus a positive-semidefinite matrix are ≥ 1) gives det(AT A) ≤ det GS = 1.
As det(AT A) ∈ Z>0 , it equals 1. Then det(I + 2(AT A)−1/2 C T C(AT A)−1/2 ) = 1
with positive-semidefinite inner factor forces C T C = 0, i.e. C = 0. So S ⊂ Zp
with vol(S) = 1; [Duc23, Lemma 2] applied inside Zp gives S ∼        = Zr . □


E.3    The Product Progress Lemma

One primal step and the subsequent dual step of [Duc23, Alg. 1] jointly multiply
vol(B[0:k−1] ) by the product bounded in the following lemma.
     Lemma E.2. Let S ⊂ Λ′ be primitive of rank k = p − 1 with vol(S) > 1.
Let v be a shortest nonzero vector of πS⊥ (Λ′ ), let ṽ ∈ Λ′ be any lift of v, and set
S ′ := S + Zṽ (primitive of rank p). Then
                                                    p
                        λ1 πS⊥ (Λ′ ) · λ1 (S ′∨ ) ≤
                                    
                                                      1 − 1/p.
26      Z. Straznickas and S. Weis

    Proof. S ′ is primitive: v is shortest in πS⊥ (Λ′ ), hence primitive there. The map
πS : Λ′ → πS⊥ (Λ′ ) is a surjective lattice homomorphism with kernel span(S)∩Λ′ =
  ⊥

S (by primitivity of S), so S ′ = (πS⊥ )−1 (Zv) and Λ′ /S ′ ∼   = πS⊥ (Λ′ )/Zv is torsion-
                 ′∨                ′∨
free. Hence S = πspan(S ′ ) (Λ ).
    Case 1: span(S) ̸⊂ Rp . Since dim span(S) = k < p, some ej ∈               / span(S);
then 0 ̸= πS⊥ (ej ) ∈ πS⊥ (Λ′ ) with ∥πS⊥ (ej )∥ ≤ 1, so λ1 (πS⊥ (Λ′ )) ≤ 1. As
span(S ′ ) ⊃ span(S) has a vector with nonzero Rq -component, some fm satisfies
πspan(S ′ ) (fm ) ̸= 0. Since √12 fm ∈ Λ′∨ , we get 0 ̸= √12 πspan(S ′ ) (fm ) ∈ S ′∨ with
                                      p
norm ≤ √12 . Product ≤ 1 · √12 ≤ 1 − 1/p for all p ≥ 2.
                              p               ′     p       p                            p
    Case 2: span(S) ⊂ R . Then S ⊂ Λ ∩ R = Z , and S is primitive in Z .
[Duc23,
p          Lemma 4] (applied inside Zp at rank k < p, vol > 1) gives λ1 (πS⊥ (Zp )) ≤
   1 − 1/p, and πS⊥ (Zp ) ⊂ πS⊥ (Λ′ ) transfers the bound. For the dual factor: the
p + q vectors {ej } ∪ { √12 fm } ⊂ Λ′∨ span Rp+q and each has norm ≤ 1, so at least
                                                       ′
one projects nonzero onto    pthe p-dimensional span(S ); that projection witnesses
λ1 (S ′∨ ) ≤ 1. Product ≤ 1 − 1/p · 1. □
                                                                                  √
    Remark E.3. In Case 1 the hypothesis vol(S) > 1 is not used; the 2-
structure supplies the progress. In Case 2 it is used where [Duc23, Lemma 4]
needs it. The counterexample from §E.1 falls under Case 1, where the dual step
supplies the factor √12 .


E.4    Termination and correctness of Algorithm 1

In Algorithm 1, primal-SVP reduction of a projected block inserts a short-
est vector of that block at its first position, so that the primal step sets
              ⊥
∥b⋆k ∥ = λ1 (π{b 0 ,...,bk−1 }
                               (Λ)). Dual-SVP reduction of B[0:k] applies a unimodu-
lar transform to the first k + 1 basis vectors making ∥b⋆k ∥ as large as possi-
ble, namely 1/λ1 (L(B[0:k] )∨ ) [Duc23]. Size reduction translates each basis vec-
tor by integer multiples of the preceding ones so that every Gram–Schmidt
coefficient µij := ⟨bi , b⋆j ⟩/∥b⋆j ∥2 satisfies |µij | ≤ 12 . HKZ (Hermite–Korkine–
Zolotarev) reduction of a block size-reduces it and SVP-reduces it and, re-
cursively, each of its projected sub-blocks. All SVP calls are in dimension
≤ max(k + 1, p + q − k) = max(p, q + 1) = p = n/2 + 1. The algorithm reads and
updates only the Gram matrix of B; “outputting a basis” means outputting the
unimodular transform from the input basis to it.
     Proof of Theorem 5.1. Termination. By Lemma E.1, Wt := vol(B[0:k−1] )2 ∈
Z>0 throughout. Let St := L(B[0:k−1] ) after iteration t’s dual step; St is primitive
in Λ′ (as the lattice generated by the first k vectors of a Z-basis). We account for
the drop in the potential Wt across the primal step of iteration t and the dual step
of iteration t+1. The primal step sets ∥b⋆k ∥ = λ1 (πS⊥t (Λ′ )) =: α and L(B[0:k] ) =: St′
                    1/2
with vol(St′ ) = Wt α. The next dual step sets ∥b⋆k ∥ = 1/λ1 (St′∨ ) =: 1/γ, so
   1/2                  1/2                                          p
Wt+1 = vol(St′ ) · γ = Wt · αγ. If Wt > 1, Lemma E.2 gives αγ ≤ 1 − 1/p,
so Wt+1 ≤ (1 − 1/p)Wt . From W0 ≤ (maxi ∥bi ∥)2k : at most 2pk ln maxi ∥bi ∥
iterations.
               HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1                 27

    The dependence on the input basis can be reduced to a doubly logarithmic
one. The argument has two phases: first, a recursion proved next brings ln Wt to
at most 1 + p ln p; then the factor 1 − 1/p of Lemma E.2 brings the potential to
                                                           1−1/p
1. In every iteration we additionally have Wt+1 ≤ p Wt           . The primal step’s
contribution satisfies α ≤ 1: since dim span(St ) = k < p, some ej lies outside
span(St ) and projects to a nonzero vector of πS⊥t (Λ′ ) of norm at most 1. For the
                                                                          1/2
dual step, St′∨ is a lattice of rank p and covolume 1/vol(St′ ) = (Wt α)−1 . The
closed cube of side 2 covol(St′∨ )1/p has volume 2p covol(St′∨ ), so by Minkowski’s
convex-body theorem it contains a nonzero point of St′∨ , of Euclidean norm
          √                                                        1/2
at most p covol(St′∨ )1/p . This gives γ 2 = λ1 (St′∨ )2 ≤ p (Wt α)−2/p . Hence
                                     1−1/p        1−1/p
Wt+1 = Wt (αγ)2 ≤ p α2(1−1/p) Wt           ≤ p Wt       . Writing vt := ln Wt , this
reads vt+1 ≤ ln p+(1−1/p) vt . Hence vt ≤ (1−1/p)t v0 +p ln p, and vt ≤ 1+p ln p
within ⌈p ln v0 ⌉ iterations. The factor 1 − 1/p of Lemma E.2 then brings the
integer potential to 1 within p (1 + p ln p) further iterations. With v0 = ln W0 ≤
2k ln maxi ∥bi ∥ this gives the bound stated in the theorem (the +3p there absorbs
the ceiling and the unpaired first dual step).

    Correctness. At termination vol(B[0:k−1] )2 = 1, so by Lemma E.1 the front
block S := L(B[0:k−1] ) is a rank-k sublattice of Zp with an orthonormal basis;
since the only vectors of Zp of norm 1 are the ±ej , S is the span of k of the p unit
vectors. The final step HKZ-reduces the blocks B[0:k−1] (rank k) and B[k:p+q−1]
(rank q + 1) and size-reduces the full basis, using SVP calls in dimension at most
max(k, q + 1) = n/2 < p.

     For the front block: in an HKZ-reduced basis of S every Gram–Schmidt vector
is a unit vector ±ej of Zp (inductively: the first basis vector is a norm-1 vector of
S ⊆ Zp , hence some ±ej ; projecting S orthogonally to it leaves the span of the
remaining unit vectors, whose norm-1 vectors are again ±ej ); the size-reduction
coefficients µij = ⟨bi , b⋆j ⟩/∥b⋆j ∥2 = ⟨bi , ±ej ⟩ are integers, hence are reduced to 0;
the front block becomes an orthonormal set of k unit vectors.
                                                  √             √
     For the back block: πS⊥ (Λ′ ) = Zp−k ⊕ 2 Zq = Z ⊕ 2 Zq . Its shortest vector
is the
    √ remaining unit vector, unique up to sign (everything outside Ze has norm
≥ 2), √  so the first HKZ vector of the back block is ±e; the projection orthogonal
to it is 2 Zq , whose HKZ basis       √ is its orthogonal basis by the same argument as
for the front block (scaled by 2). Size reduction again clears the cross terms:
against a unit vector b⋆j = ±e the coefficient is an integer, and against a vector
         √                                 √
b⋆j = ± 2f the coefficient is ⟨bi , 2f ⟩/2 ∈ (2Z)/2 = Z. The output basis is
                                                              √         √
therefore the hidden orthogonal basis (e0 , . . . , ep−1 , 2f0 , . . . , 2fq−1 ) of Λ′ up
to signed permutation. (These terminal HKZ reductions use SVP dimension n/2
rather than the ⌊n/4⌋ + 1 that a recursive half-dimension LIP solve would give;
the main loop already requires dimension p = n/2 + 1, so the theorem’s bound is
unaffected, and plain HKZ is also how [Duc23, Alg. 1] finishes for Zd .) □
                                  √
     Corollary E.4. [Zp ⊕ s Zq ]-LIP ≤det poly(p) × SVP(p) (deterministic
reduction) for any integer s ≥ 2 and p > q ≥ 0. (Replace “mod 2” by “mod s” in
28      Z. Straznickas and S. Weis

                                              √   p
Lemma E.1; Lemma E.2 Case 1 gives product ≤ 1/ s ≤ 1 − 1/p for p ≥ 2;
Case 2 is unchanged.)
     Remark E.5 (relation to [BN24]). Bambury–Nguyen [BN24, Thm 1]
                                           ′
prove that for any rank-d lattice Λ ⊆ Zd with λ1 (Λ)λ1 (Λ∨ ) < 1 − ε, a nonzero
vector of norm ≤ λ1 (Λ) in Λ or one of norm ≤ λ1 (Λ∨ ) in Λ∨ can be found with
polynomially many SVP calls in dimension ⌊d/2⌋ + 1, terminating as soon as
one is found; their Theorem 4 p returns a full orthogonal basis of Λ ∼   = Zd with a
                                                           ′
γ-approximate oracle for any γ < 2 − 2/d. √   The class [Λ ] satisfies the hypothesis
of their Theorem 1 with λ1 (Λ′ )λ1 (Λ′∨ ) = 1/ 2, and Theorem 5.1 can be read as
a near-hypercubic instance of their framework that returns all shortest vectors.
The analysis here builds on theirs: [BN24, Lemma 1] expresses the per-round
volume drop as the product of the primal and dual steps’ contributions, and
their Theorem 1 bounds that product by λ1 (Λ)λ1 (Λ∨ ) while neither half-block
contains a shortest vector. Lemma E.2 bounds the same product under vol(S) > 1
alone, using the structure of [Λ′ ], so that the loop runs until the front-block
volume reaches 1, where all shortest vectors can be read off (the direct analogue
of [Duc23, Lemma 4] fails for Λ′ , §E.1). An alternative route iterates [BN24, Thm
1], removing each found primal or√dual shortest vector and recursing; the residual
                              ′          ′
lattices remain of the form Zp ⊕ 2 Zq until q ′ = 0, where the hypercubic solver
of [Duc23] applies. We organize the argument as a single termination bound.


F    Falcon and NTRU-Type Schemes Are Not Affected
Falcon [PFH20] uses the same field Kn = Q(ζ2ℓ ), so τ exists. However, the
τ -cocycle construction does not transfer, for two independent structural reasons.
Throughout this section we use Falcon’s standard notation: q denotes the NTRU
modulus (not the integer q = n/2 − 1 of Corollary 4.6), f, g, F, G denote the four
ring elements of Falcon’s secret basis (unrelated to the field F of §§3–4), and σsk
is the Gaussian width of the NTRU secret.
   (i) No public Hermitian Gram. Falcon publishes h = gf −1 mod q ∈ Rn /q
[PFH20, eq. (3.17)], not the Gram of the secret basis B. Two secret keys with
the same h have different Grams (they differ by left-multiplication by an element
of GL2 (Rn ) that need not be unitary), so constraint (C2) of §4.1 — which has
coefficients depending on the Gram matrix — is not a function of the public key.
Without (C2), the lattice of matrices satisfying (C1) alone has rank 2n, not n,
and offers no advantage.
   (ii) det B = q ̸= 1. Lemma 4.2’s integral isometry requires B ∈ SL2 (Rn ),
and Lemma
           4.4’s minimum n/4 requires det Vτ = 1. Falcon’s secret basis is
       g −f
B= G     −F   [PFH20, eq. (2.2)], and the NTRU equation f G − gF = q [PFH20,
                         / Rn× ; the resulting cocycle qB −1 τ (B) has determinant q 2
eq. (3.15)] is det B = q ∈
       (τ )        2
and Q -value q · n/4, above the Gaussian heuristic (the expected first minimum
of a random lattice of the same volume) of any publicly derived q-ary lattice (one
containing q M2 (Rn )) — a worse target than (f, g) ∈ Λh := {(u, v) ∈ Rn2 : uh ≡
v mod q} directly.
              HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1              29

    More generally, consider any polynomial in the entries of B and their Galois
conjugates whose norm is independent of σsk . Each monomial mixes short factors
(f, g, of size ∼ σsk ) with long ones (the completion F, G, of size ∼ q/σsk ); for the
product to be σsk -independent the two must balance, and any non-constant
balanced monomial has norm ≥ Θ(q). Reason (i) and this scale-imbalance
argument apply to any NTRU-type scheme, not only to Falcon. The distribution-
independent minimum of Lemma 4.4 is possible for HAWK because all four
entries of B have the same scale. To the best of our effort, none of the related
side-constructions — descent via NKn /Knτ or NKn /F , or the LIP reduction of
Corollary E.4 applied to q-ary lattices — helps against Falcon: each either reduces
to the standard subfield attacks [ABD16; KF17] or has no Falcon instance.
