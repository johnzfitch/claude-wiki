---
title: "Files 4Zrzovbb Website E2Cdf9Dad157F298842A1224779Ac0A8999E1Da5 Pdf 540B68985E"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/e2cdf9dad157f298842a1224779ac0a8999e1da5.pdf"
category: "19-Reference"
fetched_at: "2026-08-07T06:39:13Z"
---

NP-Hardness of Approximating the Closest Vector Problem
                     within a Polynomial Factor


                                                Abstract
         We prove that there is an absolute constant c′ > 0 (one may take c′ = 1.8 × 10−5 ) such
      that the promise problem GapCVPnc′ is NP-hard under deterministic polynomial-time Karp
      reductions: given a basis B ∈ Qn×n of a full-rank lattice L ⊂ Rn and a target t ∈ Qn , it is
                                                                    ′
      NP-hard to distinguish dist2 (t, L) ≤ 1 from dist2 (t, L) > nc . The proof is a direct algebraic
      reduction from 3SAT through a Reed–Muller consistency lattice. All lemmas are stated
      and proved in full; external citations are to: the Cook–Levin theorem, Bertrand’s postulate,
      the Delsarte–Goethals–MacWilliams duality for generalized Reed–Muller codes, the explicit
      Lang–Weil bounds of Cafure–Matera, the elementary point bound for affine varieties, and
      polynomial-time Hermite normal form computation.

Theorem. With c′ := 1.8 × 10−5 , the promise problem GapCVPnc′ is NP-hard under determin-
istic polynomial-time Karp reductions.


1     Definitions, conventions, parameters
1.1    Lattices and the promise problem
A lattice L ⊂ Rn is the set of integer combinations of a basis B = (b1 , . . . , bn ) of Rn ; we write
dist2 (t, L) := minv∈L ∥t − v∥2 (the minimum is attained). For a function γ = γ(n) ≥ 1, the
promise problem GapCVPγ has instances (B, t) with B ∈ Qn×n nonsingular and t ∈ Qn ; YES
instances satisfy dist2 (t, L(B)) ≤ 1, NO instances satisfy dist2 (t, L(B)) > γ(n). A promise
problem Π is NP-hard under deterministic Karp reductions if for every language Λ ∈ NP there
is a deterministic polynomial-time computable map taking instances of Λ to instances of Π,
mapping members to YES instances and non-members to NO instances. By the Cook–Levin
theorem it suffices to reduce from 3SAT.

Theorem 1.1 (Main). With c′ := 1.8 × 10−5 , GapCVPnc′ is NP-hard under deterministic
polynomial-time Karp reductions.

1.2    Measures, tables, codes, lattices of encodings
Fix a prime q. For a finite set Σ, Z[Σ] denotes theP        free abelian group with basis
                                                                                        P (ev )v∈Σ 2; its
elements  are  called  integer   measures on Σ.  For µ  =     v µv ev we write aug µ :=  v µv , ∥µ∥2 :=
                                                       ′ induces the pushforward ϕ : Z[Σ] → Z[Σ′ ],
P 2                     P
    µ
   v v and    ∥µ∥ 1 :=     v |µv |. A map  ϕ : Σ →   Σ                                ∗
ev 7→ eϕ(v) . For Σ = FJq , margȷ denotes the pushforward along v 7→ vȷ . We write µ̄ := µ mod q
and use the convention 00 := 1.


                                                     1
    A table on a finite domain X with J slots is a map F : X → Z[FJq ]; its coordinates are
F (x)v ∈ Z. A code C ⊆ (FJq )X is an Fq -linear space of J-tuples of functions. For c ∈ C, Enc(c)
is the table Enc(c)(x) := ec(x) , and
                                                                         J
                             L(C) := Z-span{Enc(c) : c ∈ C} ⊆ ZX×Fq .
                                                                                      J
With P := q 2000 , we say that a table F is C-structured if F ∈ L(C) + P ZX×Fq .
    RM(m0 , e) denotes the space of polynomials in Fq [x1 , . . . , xm0 ] of total degree ≤ e (identified
with their evaluation tables on Fm                                              m0
                                 q when convenient). A code on X = Fq has coordinate degree
                                   0

≤ d¯ if every slot function of every codeword is the evaluation of a polynomial of total degree
   ¯
≤ d.
    Two standard facts will be used throughout.

Lemma 1.2 (Schwartz–Zippel and reduced evaluation). (i) A nonzero f ∈ Fq [x1 , . . . , xm0 ]
   of total degree D has at most Dq m0 −1 zeros in Fm
                                                    q .
                                                      0


 (ii) A nonzero polynomial all of whose individual degrees are ≤ q − 1 (in particular, any
      nonzero polynomial of total degree < q) does not vanish identically on Fm q ; consequently
                                                                                 0

      two polynomials of total degree < q defining the same function are equal.

Proof. (i) Induction on m0 via the leading variable. (ii) The evaluation map is injective on the
span of the monomials with individual degrees ≤ q − 1 (dimension count q m0 against q m0 points,
triangularity via interpolation; alternatively, induction on m0 ).

1.3    Parameters
The input is a 3CNF formula φ with N variables and at least one clause (clauses are ordered
triples of literals; formulas with no clause, or with N < N0 below, are handled trivially in §2.6).
We fix:

   • m := 8, m′ := 3m + 3 = 27; h := ⌈N 1/m ⌉; d := 60h;

   • q := the least prime ≥ d40 ; by Bertrand’s postulate d40 ≤ q < 2d40 , so h ≤ q 1/40 and
     q ≥ h40 ≥ N 5 ;
                  4                                           5
   • N0 := 22·10 , so that N ≥ N0 implies q ≥ N 5 ≥ 210 ; in particular every explicit constant
     ≤ 2100 appearing below is ≤ q 0.001 (the “absorption rule”, used silently in the ledger of
     §12.1);

   • H := {0, 1, 2, . . . , h − 1} ⊂ Fq (residues; {0, 1} ⊆ H, |H| = h ≥ 2);

   • c := 10−3 , c3 := 10−2 ; g 2 := 16q 2c ;

   • witness degrees d3 := m′ h + 3(d + 1) + d = 267h + 3 and d6 := 2d + mh = 128h;

   • penalty weight W := q 1000 , padding scale P := q 2000 ;

   • windows L1 := ⌈q 0.15 ⌉, L2 := ⌊q 0.3 ⌋.


                                                   2
    The variables of φ are identified with distinct points of H m via a fixed injection ιvar (base-h
digits; hm ≥ N ). A clause C = (ℓ1 , ℓ2 , ℓ3 ) with ℓι = (vι , bι ) (bι = 1 iff the literal is negated) is
encoded as
                                                                                          ′
                w(C) := ιvar (v1 ), ιvar (v2 ), ιvar (v3 ), 1 − b1 , 1 − b2 , 1 − b3 ∈ H m .
                                                                                    

                          ′
We write points of Fm   q  as w = (y1 , y2 , y3 , s) with yι ∈ Fm                            3
                                                                  q , s = (s1 , s2 , s3 ) ∈ Fq , and put
πι (w) := yι . For a Boolean assignment α, the literal ℓι of C is true iff α(vι ) = sι , where sι = 1−bι
                                               ′
is the ι-th s-coordinate of w(C). Let ϕ̂ : H m → {0, 1} be the indicator of {w(C) : C ∈ φ} and let
Φ̂ ∈ Fq [w] be its unique extension with all individual   degrees < h (Lemma 3.1); then Φ̂ ̸= 0 and
            ′
                                                  Q
deg Φ̂ ≤ m (h − 1). Finally we set Zκ (w) := η∈H (wκ − η) (degree h, vanishing on {wκ ∈ H});
on Fmq we use the same notation Zκ (x), κ ≤ m.


2     The construction
2.1    Layers
A layer is a quadruple τ = (Xτ , Jτ , Cτ , στ ) consisting of a domain, a slot number, a code and
an integer scaling. We use exactly four layers (numbered 1, 2, 3, 6):

                    τ           Xτ     Jτ                          Cτ                     d¯τ        στ
               1 (A-layer)      Fm
                                 q     1              {A : A ∈ RM(m, d)}                   d        q 26
                                   ′
                2 (triple)      Fm
                                 q     3     {(Aπ1 , Aπ2 , Aπ3 ) : A ∈ RM(m, d)}           d      ⌈q 33/2 ⌉
                                   ′
           3 (clause witness)   Fm
                                 q     m′    {(B1 , . . . , Bm′ ) : Bκ ∈ RM(m′ , d3 )}    d3      ⌈q 33/2 ⌉
           6 (Bool. witness)    Fm
                                 q     m      {(B1 , . . . , Bm ) : Bκ ∈ RM(m, d6 )}      d6        q 26

    Here d¯τ is the coordinate degree of Cτ . With dimτ := dim Xτ we have στ2 q dimτ ∈ [q 60 , 4q 60 ]
for each τ , hence             X
                        ∆2φ :=    στ2 q dimτ ∈ [4q 60 , 16q 60 ], ∆φ ≤ 4q 30 .                 (2.1)
                                  τ


2.2    Penalties
Each penalty is a Z-linear form ℓρ on the joint table vector (F1 , F2 , F3 , F6 ) with coefficients in
{0, ±1}, together with a target value βρ ∈ {0, 1}. The rows are:

(P0) for each τ and each x ∈ Xτ : aug Fτ (x) = 1.
                      ′
(P1) for each w ∈ Fm
                                                                             
                    q , ι ∈ {1, 2, 3} and u ∈ Fq :  margι F2 (w) u − F1 (πι w) u = 0, i.e. the
     measure equality margι F2 (w) = F1 (πι w).
                                                           
(P4) for each w and u ∈ Fq : (Θw )∗ F2 (w) u − (Ξw )∗ F3 (w) u = 0, where
                                        3                                    m  ′
                                        Y                                    X
                         Θw (v) := Φ̂(w) (vι − sι ),            Ξw (u) :=           Zκ (w) uκ .
                                            ι=1                              κ=1


                ∈ Fm                              m                                 2
                                                            
(P6) for each x P  q and u ∈ Fq : θ∗ F1 (x) u − (Ξx )∗ F6 (x) u = 0, where θ(v) := v − v and
       m         m
     Ξx (u) := κ=1 Zκ (x)uκ .
                                       ′
     Each row touches at most 2q m table entries (with coefficients ±1). The number of rows is
2q 8 + 2q 27 (P0) + 3q 28 (P1) + q 28 (P4) + q 9 (P6).

                                                      3
2.3    Coordinates, lattice, target
The coordinate set is I = Imass ⊔ Ipen : one mass coordinate per triple (τ, x, v) and one penalty
coordinate per row ρ. In total,

           Dtot = q 9 + q 30 + q 54 + q 16 + 2q 8 + 2q 27 + 3q 28 + q 28 + q 9 ≤ 2q 54 ≤ q 55 .     (2.2)
                  |          {z          } |                {z               }
                            mass                        penalty

    For a table u supported on layer τ define the vector Γτ (u) ∈ ZI : the mass coordinates of
layer τ carry στ u, the other mass coordinates carry 0, and penalty coordinate ρ carries W ℓρ (u).
The lattice L is generated by:

   1. Γτ (b) for every vector b in the basis of L(Cτ ) provided by Lemma 2.1, for each τ ;

   2. padding: στ (i) P ei for every mass coordinate i (of layer τ (i)), and P eρ for every penalty
      coordinate ρ.

   The target t⋆ ∈ ZI is 0 on all mass coordinates and W βρ on penalty coordinate ρ (so W on
P0 rows and 0 on P1/P4/P6 rows). By the padding, L has full rank n = Dtot .
   Every v ∈ L has the form
                         X
                    v=      Γτ (uτ ) + P · (padding part),   uτ ∈ L(Cτ ),               (2.3)
                             τ

and its mass coordinates read στ Fτ (x)v with Fτ := uτ + P µ(τ ) for integer tables µ(τ ) , while
penalty coordinate ρ reads W ℓρ (F ) + P νρ for some νρ ∈ Z (one absorbs W P ℓρ (µ(·) ) into P νρ ;
note P | W P ). In particular, each Fτ is Cτ -structured.
Lemma 2.1 (Explicit bases). Given an Fq -basis c1 , . . . , ck of a code C on X (q prime), a Z-
basis of L(C), with entries of bit-size polynomial in |X|q J , is computable in time polynomial in
|X|q J k.
Proof. For 0 ≤ i ≤ k let C (i) := span(c1 , . . . , ci ). Let σij (0 ≤ j ≤ q − 1) be the coordinate
                        J
permutation of ZX×Fq given by (σij u)x,v := ux,v−jci (x) ; then σij Enc(c) = Enc(c + jci ). Since q
is prime, every c′ ∈ C (i) equals c + jci with c ∈ C (i−1) and j ∈ {0, . . . , q − 1}; conversely all such
elements lie in C (i) . Hence
                                                 q−1
                                                     σij L(C (i−1) ).
                                                X
                                          (i)
                                     L(C ) =
                                                 j=0

Starting from the basis {Enc(0)} of L(C (0) ), iterate: given a basis Bi−1 (of size ≤ |X|q J ), the set
{σij b : b ∈ Bi−1 , 0 ≤ j < q} (q|Bi−1 | vectors) generates L(C (i) ); compute the Hermite normal
form of the stacked matrix to obtain Bi . Polynomial running time and bit-sizes follow from
polynomial-time HNF algorithms (Kannan–Bachem; entry bounds via Hadamard).

Lemma 2.2 (Restrictions; plane membership is automatic). Let Y ⊆ X and let C|Y denote the
restricted code. Restriction of tables maps L(C) into L(C|Y ) and P ZX×· into P ZY ×· . Hence
a C-structured table restricts, on every affine plane Π ⊂ X = Fm q , to a C|Π -structured table.
                                                                  0

Likewise, any pushforward applied pointwise (marginals, ϕ∗ with ϕ depending on the point) maps
Enc(c) to Enc of the image codeword and hence maps structured tables to structured tables for
the image code. The same holds for domain-extended families of pointwise pushforwards: if

                                                    4
                                       ′
(ϕz )z∈Z is a family of maps FJq → FJq and F is C-structured on X, then F̃ (x, z) := (ϕz )∗ F (x)
is C̃-structured on X × Z for C̃ := {(x, z) 7→ ϕz (c(x)) : c ∈ C} (an Fq -linear code whenever each
ϕz is linear on values).
Proof. Immediate from Enc(c)|Y = Enc(c|Y ) and (ϕz )∗ Enc(c)(x) = eϕz (c(x)) (so the family map
sends Enc(c) to Enc of the image codeword on X × Z), together with the Z-linearity of all maps
involved (the P Z parts are preserved since pushforwards have integer matrices).

2.4   Output instance
The reduction computes all generators and the target exactly (evaluating Φ̂ by Lagrange in-
terpolation over H), stacks the generators,
                                    q       computes a basis B0 of L by HNF, computes the
integer ∆2φ and the rational R := ⌈ q 20 ∆2φ ⌉/q 10 — the ceiling integer square root, so that
∆φ ≤ R ≤ ∆φ + q −10 ≤ (1 + q −10 )∆φ (using ∆φ ≥ 2q 30 ≥ 1) — and outputs (B0 /R, t⋆ /R).

2.5   Sizes and time
We have q ≤ 2(60(N 1/8 + 1))40 = O(N 5 ) and n ≤ 2q 54 = O(N 270 ). The primitive data
(penalty coefficients, paddings, W , P , target entries) have bit-size O(log q) · 2100 = poly(N );
the generators Γτ (b) inherit the polynomial bit-sizes of the bases of Lemma 2.1, and the final
HNF basis again has polynomial bit-size. The prime q is found by trial division in time O(d80 ).
                                     +m′
Code dimensions are at most m′ d3m
                                         
                                      ′    ≤ q. The total running time is polynomial in N (of
large but fixed degree), and the reduction is deterministic.

2.6   Degenerate inputs
If φ has no clause, output a fixed YES instance (B = (1), t = 0, n = 1: distance 0 ≤ 1). If
N < N0 , decide φ by brute force (constant time) and output either the fixed YES instance
                                                                             ′
above or the fixed NO instance B = (3), t = 3/2, n = 1 (distance 3/2 > 1 = nc ).


3     Completeness
Lemma 3.1 (Low-degree extension). Every f : H M → Fq has a unique extension F ∈
Fq [w1 , . . . , wM ] with all individual degrees < h; and a polynomial with individual degrees < h
vanishing on H M is 0.
                                                                              −η
Proof. Existence: Lagrange interpolation, F = z∈H M f (z) κ η̸=zκ wzκκ−η
                                                     P           Q Q
                                                                                 . Vanishing: induc-
                                           j
tion on M ; write R = j<h Rj (w′ )wM ; for each w′ ∈ H M −1 the univariate polynomial of degree
                            P

< h vanishes on h points, so all Rj vanish on H M −1 ; now induct. Uniqueness follows.

Lemma 3.2 (Division). If P ∈ Fq [w1 , . . . , wM ] vanishes identically on H M , then
P = M
   P
    κ=1 Zκ Bκ with deg Bκ ≤ deg P − h.

Proof. Divide P by the monic univariate Z1 (w1 ): since Z1 − w1h has degree ≤ h − 1, each
cancellation step replaces a term of total degree ≤ deg P by terms of strictly smaller w1 -degree
and total degree ≤ deg P ; hence P = Z1 B1 + R1 with deg B1 ≤ deg P − h, deg R1 ≤ deg P
and degw1 R1 < h. Divide R1 by Z2 (this does not increase w1 -degrees), and so on. The final
remainder R has all individual degrees < h and vanishes on H M , hence R = 0 by Lemma 3.1.

                                                 5
Proposition 3.3 (Completeness). If φ is satisfiable then dist2 (t⋆ , L) ≤ ∆φ .

Proof. Let α be a satisfying assignment, extended by 0 to all of H m , and let A ∈ Fq [x1 , . . . , xm ]
be its individual-degree-< h extension; then deg A ≤ m(h − 1) ≤ 8h ≤ d, so A ∈ RM(m, d). Set
F1 := Enc(A) and F2 := Enc((Aπ1 , Aπ2 , Aπ3 )).Q
                                                                                 ′                    ′
    Clause witness. The polynomial Pα := Φ̂ ι (A(yι ) − sι ) vanishes on H m : at w ∈ H m ,
either ϕ̂(w) = 0 = Φ̂(w), or w = w(C) for a clause C P   satisfied by α, so that some literal is
true, i.e. A(yι ) = sι for some ι. By Lemma 3.2, Pα = κ Zκ Bκ with deg Bκ ≤ deg Pα − h ≤
27(h − 1) + 3 · 8(h − 1) − h ≤ 50h ≤ d3 . Set F3 := Enc((B1 , . . . , Bm′ )).
                                                                                                     (6)
    Booleanity witness. Since α is Boolean, A2 − A vanishes on H m , so A2 − A = κ≤m Zκ Bκ
                                                                                   P
            (6)
with deg Bκ ≤ 2m(h − 1) − h ≤ 15h ≤ d6 . Set F6 := Enc(B(6) ).
    All penalties hold exactly:              (P0) each point carries a single unit atom; (P1)
margι e(A(y1 ),A(y2 ),A(y3 )) = eA(yι ) ; (P4) both sides at w equal ePα (w) ; (P6) both sides at x equal
e(A2 −A)(x) .
    The lattice vector v := Pτ Γτ (Fτ ) (no padding) then matches t⋆ exactly on all penalty
                                  P
coordinates, and ∥v − t⋆ ∥22 = τ στ2 |Xτ | = ∆2φ .


4    Soundness radius: coherent integer proofs
Definition 4.1. A coherent integer proof is a quadruple of tables (F1 , F2 , F3 , F6 ) such that:

 (a) each Fτ is Cτ -structured;

 (b) all penalties (P0), (P1), (P4), (P6) hold exactly over Z;
                     2     2 dimτ for each τ , where g 2 = 16q 2c .
     P
 (c)    x∈Xτ ∥Fτ (x)∥2 ≤ g q

Proposition 4.2. If dist2 (t⋆ , L) ≤ q c ∆φ then a coherent integer proof exists.

Proof. Take v ∈ L with ∥v − t⋆ ∥ ≤ q c ∆φ ≤ q 0.001 · 4q 30 < q 31 and decompose it as in (2.3);
let Fτ = uτ + P µ(τ ) be the integer tables read off the     P mass Pcoordinates. Part (a) holds by
construction. For (c): the mass part of ∥v − t⋆ ∥2 is τ στ2 x ∥Fτ (x)∥2 ≤ q 2c ∆2φ , and στ2 ≥
                                                                                     p
q 60−dimτ together with ∆2φ ≤ 16q 60 gives (c). For (b): pointwise, |Fτ (x)v | ≤ g 2 q 27 ≤ q 14 , so
|ℓρ (F )| ≤ 2q 27 ·q 14 = 2q 41 for every row. Penalty coordinate ρ of v−t⋆ equals W (ℓρ (F )−βρ )+P νρ
with |W (ℓρ (F ) − βρ )| ≤ q 1000 · 3q 41 < q 1042 . If νρ ̸= 0 the coordinate has absolute value
≥ P − q 1042 > q 31 , a contradiction; so νρ = 0, and then W |ℓρ (F ) − βρ | < q 31 < W forces
ℓρ (F ) = βρ .

    The rest of the paper proves: if φ is unsatisfiable, no coherent integer proof exists (Corol-
lary 11.3). Together with Propositions 3.3 and 4.2 this yields Theorem 1.1 (§12).


5    Moment machinery
Throughout §§5–8, “layer” means: a domain Fm    q (2 ≤ m0 ≤ 28), a code C of coordinate degree
                                                  0

≤ d¯ ≤ q 0.04 , and a C-structured table F with aug F (x) = 1 for all x. For k ∈ ZJ≥0 define
                                   X                                     Y kȷ
                       µk (x) :=       vk F̄ (x)v ∈ Fq ,    where vk =    vȷ .
                                   v                                      ȷ


                                                     6
Lemma 5.1 (Plane moment invariant). Let Π ⊂ Fm           0 be an affine plane (∼ F2 ), u a C| -
                                                       q                         = q           Π
structured  table on Π, p a bivariate polynomial on Π,  and suppose  deg p + |k|d¯ ≤ 2q − 3. Then
P           P k
   s∈Π p(s)   v v us,v ≡ 0 (mod q).

Proof. The expression is linear
                             P in u and Q vanishes mod q on the P Z-part (since q | P ). On a
generator Enc(c|Π ) it equals s∈Π p(s) ȷ cȷ (s)kȷ , a full-plane sum of a bivariate polynomial of
degree ≤ 2q − 3. For a monomial y a z b we have (y,z)∈F2q y a z b = ( y y a )( z z b ), and y y a
                                                     P                 P      P            P

vanishes unless a is a positive multiple of q − 1 (for a = 0 the sum is q ≡ 0). A nonzero
contribution therefore needs a, b ≥ q − 1, i.e. total degree ≥ 2q − 2.

Proposition 5.2 (Delsarte–Goethals–MacWilliams duality; quoted). For 0 ≤ ρ ≤ 2(q − 1) − 1
                                                                                  F2
one has GRMq (ρ, 2)⊥ = GRMq (2q − 3 − ρ, 2), where GRMq (ρ, 2) ⊆ Fq q is the evaluation code
of bivariate polynomials of degree ≤ ρ.
Lemma 5.3 (Lines to global). Let f : Fm   q → Fq and let e satisfy 2e ≤ q − 1. If the restriction
                                            0

of f to every affine line agrees with a univariate polynomial of degree ≤ e, then f agrees with a
polynomial of total degree ≤ e.
Proof. Induction on m0 ; the case m0 = 1 is trivial. Fix distinct u0 , . . . , ue ∈ Fq . Each slice
f |xm0 =uj satisfies the hypothesis on Fm       0 −1 , hence by induction lies in RM(m − 1, e). For each
                                              q                                          0
x , the axis-line restriction u 7→ f (x , u) is a polynomial of degree ≤ e, so f (x , u) = i≤e ci (x′ )ui
  ′                                         ′                                          ′
                                                                                             P
where each ci is a fixed linear combination of the slices at u0 , . . . , ue ; hence ci ∈ RM(m0 − 1, e)
(reduced representatives, degree ≤ e). Suppose M := maxi: ci ̸=0 (deg ci + i) > e; P       note M ≤ 2e ≤
q − 1. For any ξ ′ , b′ , restricting to the line u 7→ (ξ ′ + ub′ , u) gives the polynomial i ci (ξ ′ + ub′ )ui
of degree ≤ M ≤ q − 1; by hypothesis it agrees on all q points with a polynomial of degree
≤ e < M , and two polynomials of degree ≤P              q − 1 agreeing on Fq are identical; hence its uM -
coefficient vanishes. That coefficient equals i:deg ci +i=M (ci )deg ci (b′ ), where (ci )D denotes the
degree-D homogeneous part (terms with deg ci + i < M contribute nothing at uM , and the
top coefficient of ci (ξ ′ + ub′ ) in u is (ci )deg ci (b′ ), independently of ξ ′ ). So a sum of nonzero
homogeneous polynomials of distinct degrees ≤ e ≤ q − 1, with individual degrees ≤ q − 1,
vanishes identically on Fm       0 −1 ; by Lemma 1.2(ii) it is the zero polynomial, so each part is zero,
                               q
contradicting ci ̸= 0. Hence M ≤ e.

Proposition 5.4 (Global moment polynomials). Let F be a layer as above and let k satisfy
2|k|d¯ ≤ q − 1. Then there is a unique polynomial Pk of total degree ≤ |k|d¯ with Pk (x) = µk (x)
for all x ∈ Fmq . Moreover P0 = 1.
               0


Proof. Fix a plane Π; by Lemma 2.2, F |Π is C|Π -structured; by Lemma 5.1, µk |Π is orthogonal
to GRMq (2q −3−|k|d,   ¯ 2), hence by Proposition 5.2 lies in GRMq (|k|d,
                                                                       ¯ 2): every plane restriction
of µk is a bivariate polynomial of degree ≤ |k|d. ¯ Every line lies in a plane (m0 ≥ 2), so every
                                       ¯
line restriction has degree ≤ e := |k|d, and 2e ≤ q − 1; Lemma 5.3 produces the polynomial, and
uniqueness follows from Lemma 1.2(ii). Finally P0 = 1 by the augmentation aug F ≡ 1.


6    Algebraic toolkit
Lemma 6.1 (Hankel–valuation power-sum lemma). Let K be a field with a valuation v : K× → Z
(i.e. v(ab) = v(a) + v(b) and v(a + b) ≥ min(v(a), v(b))). Let γ1 , . . . , γν ∈ K× be distinct with
v(γj ) ≤ −1 and v(γPi − γj ) ≤ 2H (i ̸= j, H ∈ Z≥0 ), and let b1 , . . . , bν ∈ K with v(bj ) = 0. Let
β ∈ Z≥0 and pl := j bj γjl . Then there is l with 1 ≤ l ≤ β + 2Hν + 2ν − 1 and v(pl ) < −β.

                                                      7
Proof. Suppose v(pl ) ≥ −β for all l ∈ {Λ, . . . , Λ + 2ν − 2}, where Λ := β + 2Hν + 1. Over any
commutative ring,                                  Y          Y
                                                        bj γjΛ    (γi − γj )2 ,
                                    
                        det pΛ+i+j 0≤i,j<ν =                                                (6.1)
                                                      j      i<j

          matrix equals V ⊤ diag(bj γjΛ )V
since the Q                                 with Vkj = γkj the square Vandermonde matrix, and
det V = i<j (γj − γi ). The left-hand side, being a sum of ν-fold products of entries, has
v ≥ −νβ. The right-hand side is nonzero and has
            X              X
v(RHS) ≤ Λ      v(γj ) + 2   v(γi − γj ) ≤ −Λν + 2Hν(ν − 1) ≤ −Λν + 2Hν 2 = −νβ − ν < −νβ,
                j           i<j

a contradiction.

Lemma 6.2 (Multivariate separation, SEP). Let K be a field and let p1 , . . . , pM ∈ KJ be
distinct. Then there exist polynomials δ1 , . . . , δM ∈ spanK {Xt : t ∈ {0, . . . , M − 1}J } with
δu (pu′ ) = 1 if u = u′ and δu (pu′ ) = 0 otherwise.     Consequently: (i) the evaluation matrix
(pu )u; t∈{0..M −1}J has full row rank M ; (ii) if u wu ptu = 0 for all t ∈ {0..M − 1}J then all
   t
                                                   P
wu = 0.
Proof. Induction on J. For J = 1 this is Lagrange interpolation. For J > 1, group the
points by their last coordinate, with values z1 , . . . , zp (p ≤ M ). Points within a group have
distinct truncations in KJ−1 ; take their inductive indicators (individual degrees ≤ M − 1) and,
                                                                                    XJ −z ′
for a point pu lying in the group with last coordinate zg , multiply by g′ ̸=g zg −z g′ (degree
                                                                             Q
                                                                                          g
≤ p − 1 ≤ M −P1), which vanishes on the other groups. Claims (i) and (ii) follow by applying
the functional u wu (·)(pu ) to δu0 .

Lemma 6.3 (Class separation, CS). Let K be a field and let {(us , Ps )}s≤S1 , {(vr , Qr )}r≤S2 be
finite weighted lists with the Ps pairwise distinct and the Qr pairwise distinctPelements ofPK, and
weights in K. Let S be the number of distinct elements of {Ps } ∪ {Qr }. If s us Psl = r vr Qrl
P 0 ≤ l ≤ SP
for              − 1, then the lists are equal as finitely supported measures: for every R ∈ K,
   s:Ps =R us =   r:Qr =R vr .

Proof. Merge the lists into
                          P onel list on the distinct elements R1 , . . . , RS with coefficients ci =
(P -net) − (Q-net); then i ci Ri = 0 for 0 ≤ l ≤ S − 1, and the S × S Vandermonde matrix at
distinct nodes is invertible.

Remark (Merging). When Lemma 6.3 is applied below (Lemmas 9.1–9.3), the input lists — e.g.
{(b̄j , γjι )}j — may contain repeated atoms; we first merge equal atoms, summing their weights
(this changes neither the power sums nor the induced class measure, and only shrinks the list
sizes used in the window counts). The conclusions are always stated for the induced class
measures, so no generality is lost.


7      The Scalar Decoding Lemma
Theorem 7.1 (Scalar decoding). Let 2 ≤ m0 ≤ 28 and let F : Fm
                                                            q → Z[Fq ] satisfy:
                                                             0


    (i) F is C-structured for a code C of coordinate degree ≤ d¯ ≤ q 0.04 (with J = 1);

 (ii) aug F (x) = 1 for all x;

                                                  8
(iii) there is E0 with |E0 | ≤ q m0 −c3 and                          2     2 m0 , where 16 ≤ ĝ 2 ≤ q 0.02 .
                                                     P
                                                          / 0 ∥F (x)∥2 ≤ ĝ q
                                                         x∈E

Then, with t̂ := ⌈ĝ 2 q c3 ⌉ (≤ 2q 0.03 ), there exist 1 ≤ r ≤ min(  t̂, 2ĝ 2 ) distinct
                                                                                        P polynomials     g1 , . . . , gr
of total degree ≤ d, ¯ nonzero integers a1 , . . . , ar with     P
                                                                     a    =     1  and      a 2 ≤ 2ĝ 2 , and a set
                                                                   j j                     j j
X ⊇ E0 with |X | ≤ 3q m0 −c3 , such that
                                               X
                                     F (x) =       aj egj (x) for all x ∈ / X,
                                                 j

and moreover j āj gjl = Pl in Fq [x] for all 0 ≤ l ≤ L1 = ⌈q 0.15 ⌉, where Pl is the global moment
              P
polynomial of Proposition 5.4.

Proof. Write tx := | supp F̄ (x)| (≥ 1 by (ii), and ≤ ∥F (x)∥22 ). All moment polynomials used
below are within the range of Proposition 5.4 (2ld¯ ≤ 2L1 d¯ ≤ 2q 0.19 ≤ q − 1).
Step 1 (rank collapse). Put E1 := E0 ∪ {x : tx > t̂}; since t̂ + 1 > ĝ 2 q c3 , Markov’s inequality
gives |E1 | ≤ 2q m0 −c3 . Let T := t̂ and HT := (Pi+j )0≤i,j≤T over Fq [x]. For x ∈         / E1 we have
            ⊤                   tx ×(T +1)
HT (x) = V DV with V ∈ Fq                  the Vandermonde matrix of supp F̄ (x) and D the invertible
diagonal matrix of weights; as tx ≤ T + 1, V has full row rank, so rank HT (x) = tx (valid in
any characteristic: V ⊤ is then injective, so ker(V ⊤ DV ) = ker(DV ) = ker V , of dimension
(T +1) − tx ). Let r be the rank of HT over Fq (x). Any nonzero ϱ × ϱ minor is a polynomial of
degree ≤ 2t̂(t̂ + 1)d¯ ≤ 12q 0.1 < q(1 − 2q −c3 ), hence (Lemma 1.2(i)) is nonzero at some x ∈      / E1 ,
giving ϱ ≤ tx ≤ t̂; so r ≤ t̂, and the pointwise rank bound ≤ r gives tx ≤ r for x ∈                / E1 .
All r-minors cannot vanish off E1 (same degree bound), so some x∗ ∈               / E1 has tx∗ = r; there
the leading principal minor ∆r := det(Pi+j )i,j<r is nonzero (square V ⊤ DV ), so ∆r ̸≡ 0 and
deg ∆r ≤ 2r2 d¯ ≤ 8q 0.1 . Define the good set G := {x ∈        / E1 : ∆r (x) ̸= 0}; for x ∈ G we get
                                                 c
r ≤ rank HT (x) = tx ≤ r, so tx = r. Also |G | ≤ 2q     m 0 −c3  + 8q m0 −0.9 , and r ≥ 1 since P0 = 1.
Step 2 (splitting). Let Ψ(x, X) := det M , where M is the (r+1) × (r+1) matrix with rows
(Pl , . . . , Pl+r ) for l = 0, . . . , r − 1 and last row (1, X, . . . , X r ). Expansion along the last row
gives lcX Ψ = ∆r , degX Ψ = r, degx Ψ ≤ r(2r − 1)d¯ ≤ 8q 0.1 , and total degree δQ                Ψ ≤ D0 :=
9q 0.1 . For x ∈ G with support {v1 , . . . , vr }, the coefficient        vector  c of χx (X) :=   i (X − vi )
                                                                              l
                                                             P
satisfies M (x, vi )c = 0 (the moment rows because i F̄ (x)vi vi χx (vi ) = 0; the last row because
                       ′

χx (vi′ ) = 0), so Ψ(x, vi′ ) = 0 for each i′ ; since degX Ψ(x, ·) = r with nonzero leading coefficient,
Ψ(x, X) = ∆r (x)χx (X): at good x, Ψ(x, ·) has exactly r distinct roots, namely the support.
     Claim: every irreducible factor of Ψ in Fq [x, X] involving X has degX = 1. Let G | Ψ be
irreducible with n := degX G ≥ 1 and δ := deg G ≤ D0 . Specializing a factorization, for x ∈ G
we have lcX (G)(x) ̸= 0 (the X-leading coefficients of the factors multiply to ∆r (x) ̸= 0), and
G(x, ·) divides the squarefree, totally split Ψ(x, ·), hence has exactly n distinct roots in Fq . So
the hypersurface V (G) ⊂ Am0 +1 satisfies #V (Fq ) ≥ n|G| ≥ n q m0 (1 − 3q −c3 ).

    • If G is absolutely irreducible, Cafure–Matera’s explicit estimate (applicable since q > 2δ 4 :
      2(9q 0.1 )4 ≤ q 0.42 < q) gives
                                                            1
             #V (Fq ) ≤ q m0 + (δ − 1)(δ − 2)q m0 − 2 + 5δ 13/3 q m0 −1 ≤ q m0 (1 + q −0.29 + q −0.55 ).
                 1+2q     −0.29
       Hence n ≤ 1−3q −0.01 < 2, so n = 1.


    • If G is irreducible but not absolutely irreducible, then over F̄q we have G = c ei=1 Gi
                                                                                     Q
      with e ≥ 2 and Frobenius permuting the Gi transitively (otherwise an orbit product

                                                            9
       would be a proper rational factor). Any Fq -point p with Gi (p) = 0 also satisfies Gi′ (p) =
       0 for some i′ ̸= i (apply σ with Gσi ∼ Gi′ ; σ fixes p). So all rational points lie on
                                                                                      2
       S
         i<i′ V (Gi ) ∩ V (Gi′ ), a variety of dimension ≤ m0 − 1 and degree ≤ δ (Bézout), whence
       #V (Fq ) ≤ δ q 2 m 0 −1 ≤q  m 0 −0.79  (using the standard bound #W (Fq ) ≤ deg W · q dim W ) —
       contradicting #V (Fq ) ≥ 21 q m0 .

    So Ψ = c(x) rj=1 (Aj X −Bj ) with each factor irreducible (Aj ̸= 0, gcd(Aj , Bj ) = 1); degrees
                  Q
of factors add, so deg Aj , deg Bj ≤ D0 =: H0 . Put γj := Bj /Aj ∈ Fq (x). If γi = γj for some
i ̸= j, then the factors are proportional (Bi Aj = Bj Ai together with coprimality),     Q          making
Ψ(x, ·) non-squarefree at good points with Ai (x) ̸= 0 — which exist, since c j Aj = ∆r is
nonzero on G; so the γj are pairwise distinct. Define the very good set VG := {x ∈ G : (Bi Aj −
Bj Ai )(x) ̸= 0 ∀i < j}; note that ∆r (x) ̸= 0 already forces c(x) ̸= 0 and all Aj (x) ̸= 0. Then
|G \ VG| ≤ 2r 2H0 q m0 −1 ≤ q m0 −0.83 , and at x ∈ VG we have supp F̄ (x) = {γ1 (x), . . . , γr (x)}, r
distinct values.
Step 3 (weights are constants). Solve the Vandermonde system j γjk Wj = Pk (0 ≤ k ≤ r −
                                                                             P

1) by Cramer’s rule over Fq (x): after clearing denominators (columnwise, γjk = Bjk Ar−1−k j       /Ar−1
                                                                                                      j ),
                                                     2
Wj = Uj /V0 with deg Uj , deg V0 ≤ DA := r H0 + rd ≤ q         ¯   0.17 and V0 ̸= 0 on VG; uniqueness of
the solution gives Wj (x) = F̄ (x)γj (x) ̸= 0 at every x ∈ VG. Suppose some Wj is nonconstant.
Let M1 := ⌊q 0.05 ⌋ and Rsm := {ρ mod q : ρ ∈ Z, |ρ| ≤ M1 }. The set of x where Wj is defined
and takes a value in Rsm has size ≤ (2M1 + 1)DA q m0 −1 ≤ q m0 −0.77 (each level set is contained
in the zero set of Uj − λV0 ̸≡ 0), and V0 vanishes at ≤ DA q m0 −1 points. At every other x ∈ VG,
the integer F (x)γj (x) ≡ Wj (x) ∈    / Rsm , so |F (x)γj (x) | > M1 and ∥F (x)∥2 > M12 ≥ 14 q 0.1 . There
are ≥ |VG| − 2q m0 −0.77 ≥ 21 q m0 such points, all outside E0 , giving mass > 81 q m0 +0.1 > ĝ 2 q m0 —
contradicting (iii). So each Wj is a constant āj ∈ F×       q .
Step 4 (polynomiality and degree). For 0 ≤ l ≤ L1 , the rational function j āj γjl − Pl
                                                                                           P

vanishes on VG; its numerator over j Aj has degree ≤ l(d¯ + rH0 ) ≤ L1 (d¯ + rH0 ) ≤ 19q 0.28 <
                                             Q l

q(1 − 3q −c3 ), so by Lemma 1.2,
                                 X
                                     āj γjl = Pl in Fq (x),      0 ≤ l ≤ L1 .                        (7.1)
                                j

    No finite poles. Fix an irreducible π and the π-adic valuation vπ ; let S := {j : vπ (γj ) ≤ −1}
and suppose S ̸= ∅. For i ̸= j, vπ (γi − γj ) ≤ vπ (Bi Aj − Bj Ai ) ≤ deg(Bi Aj − Bj Ai ) ≤ 2H0 .
Apply
    P Lemma        6.1 (β = 0, H = H0P    , weights āj ): some l ≤ 2H0 |S| + 2|S| − 1 ≤ 40q 0.13 ≤ L1 has
vπ ( j∈S āj γjl ) < 0. But by (7.1), j∈S āj γjl = Pl − j ∈S            l
                                                              P
                                                                  / āj γj has vπ ≥ 0: a contradiction. So
every γj is a polynomial (a priori of degree ≤ H0 ).
                  ¯                                 ¯                                                S
P Degreel ≤ d. Let     P S := l{j : deg γj ≥ d¯+ 1}, ν := |S|, and suppose ν¯ ≥ 1. Set pl :=
   j∈S āj γj = Pl −       / āj γj , of degree ≤ ld for 0 ≤ l ≤ L1 . Take Λ := 2ν d + 1; the window
                         j ∈S
satisfies Λ + 2ν − 2 ≤ 2rd¯ + 2r ≤ 10q 0.07 ≤ L1 . Identity (6.1) for the S-family with offset Λ:
the left-hand    side has degree ≤ ν(Λ + 2ν − 2)d,       ¯ while the right-hand side is nonzero of degree
≥ Λ j∈S deg γj ≥ Λν(d¯ + 1). Hence Λ(d¯ + 1) ≤ (Λ + 2ν − 2)d,                ¯ i.e. Λ ≤ (2ν − 2)d¯ < Λ, a
     P
                                      ¯
contradiction. So all deg γj ≤ d; set gj := γj .
Step 5 P (lift and junk). Let aj ∈ (−q/2, q/2] lift āj (so aj ̸= 0).P Call x ∈ VG clean if
F (x) = j aj egj (x) as integer measures. At x ∈ VG we have F̄ (x) = j āj egj (x) with distinct
atoms; if x is not clean, some entry of F (x) differs from its canonical lift by a nonzero multiple
of q, so ∥F (x)∥2 ≥ q 2 /4; hence at most 4ĝ 2 q m0 −2 points of VG are unclean. At clean x:

                                                    10
                                                    2        2
P                                                                     P
  j aj = aug F (x) = 1 (exactly, over Z) and ∥F (x)∥ =    j aj ; averaging thePmass bound over
                       m        −c
the clean points (≥ q (1 − 3q ) ≥ 2 q
                         0        3     1 m0
                                             of them, all outside E0 ) gives j a2j ≤ 2ĝ 2 , and
in particular r ≤ 2ĝ 2 . Let X be the complement of the clean set; collecting the estimates,
|X | ≤ 2q m0 −c3 + 8q m0 −0.9 + q m0 −0.83 + 4q m0 −1.98 ≤ 3q m0 −c3 . Finally, (7.1) with γj = gj is the
stated polynomial identity.


8     The Tuple Decoding Lemma
The naive route — decode each slot marginal and place the support in the product grid — is
unsound : marginals of signed measures can cancel. For instance, e(0,0) +e(1,1) −e(0,1) −e(1,0) +e(2,2)
has both slot marginals equal to e2 , hiding the values 0, 1. We repair this by a formal mixing
coordinate: one extra domain variable θ, with the mix ℓθ (v) := v1 + θv2 + · · · + θJ−1 vJ , turns
the tuple problem into a scalar problem one dimension up, with no loss of information.

Theorem 8.1 (Tuple decoding). Let 2 ≤ m0 ≤ 27, 1 ≤ J ≤ 27, and let F : Fm                      q
                                                                                                 0 → Z[FJ ]
                                                                                                         q
satisfy:  (i)    F   is C-structured with  C  of  coordinate  degree ≤  ¯ ≤ q 0.035 ; (ii) aug F ≡ 1; (iii)
                                                                        d
               2        2 m0 with 16 ≤ ĝ 2 ≤ q 0.003 . Then there exist 1 ≤ r ≤ 2ĝ 2 distinct tuples
P
   x ∥F (x)∥2 ≤ ĝ q
γ j = (γj , . . . , γj ) of polynomials of total degree ≤ d¯ + J − 1, nonzero integers bj with j bj = 1
         1           J
                                                                                                  P

and j b2j ≤ 2ĝ 2 , and a set X with |X | ≤ 4q m0 −c3 /2 , such that
     P

              X                                           X
    F (x) =       bj eγ j (x)   (x ∈
                                   / X ),      and             b̄j γ kj = Pk in Fq [x] for all |k| ≤ L2 ,        (8.1)
              j                                            j


where Pk are the global moment polynomials of Proposition 5.4 and γ k :=                             ȷ kȷ
                                                                                             Q
                                                                                                 ȷ (γ ) .

Proof. Let t̂ := ⌈ĝ 2 q c3 ⌉ and let tx := | supp F (x)| be the integer support size (this is the right
count both for the ℓ1 –ℓ2 comparison and for the atom bookkeeping below; it dominates the
mod-q support size). Each nonzero integer entry contributes ≥ 1 to ∥F (x)∥22 , so tx ≤ ∥F (x)∥22
and Markov’s inequality gives |{x : tx > t̂}| ≤ q m0 −c3 .
The θ-extension. Define F̃ : Fm       q
                                        0 +1 → Z[F ] by F̃ (x, θ ) := (ℓ ) F (x).
                                                    q            0          θ0 ∗        By Lemma 2.2
(pointwise pushforward
              P ȷ−1         along the point-dependent map ℓθ0 ), F̃ is C̃-structured, where C̃ :=
{c̃(x, θ0 ) =     θ    cȷ (x) : c ∈ C} is a linear code on Fm     0 +1 of coordinate degree ≤ d       ˜ :=
                 ȷ 0                                            q
d¯+ J − 1 ≤ q 0.04 . Augmentation is preserved. As for mass, ∥F̃ (x,   θ0 )∥22 ≤ ∥F (x)∥21 ≤ tx ∥F (x)∥22 ,
so with E0′ := {x : tx > t̂} × Fq (of size ≤ q (m0 +1)−c3 ) we get (x,θ0 )∈E          2      2 m0 +1 , and
                                                                    P
                                                                             / ′ ∥F̃ ∥ ≤ t̂ĝ q
                                                                                         0
16 ≤ t̂ĝ 2 ≤ 2q 0.016 ≤ q 0.02 . Apply Theorem 7.1 to F̃ (domain dimension m0 + 1 ≤ 28): we obtain
r̃ ≤ t̂′ := ⌈t̂ĝ 2 q c3 ⌉ ≤ 2q 0.03 distinct polynomials                        ˜ nonzero integers ãj , and
                                                          g̃j (x, θ) of degree ≤ d,
X̃ with |X̃ | ≤ 3q (m0 +1)−c3 , such that F̃ = j ãj eg̃j off X̃ .
                                                    P

Reconstruction. Call x good if: (a) tx ≤ t̂; (b) |{θ0 : (x, θ0 ) ∈ X̃ }| ≤ q 1−c3 /2 ; (c) for all
j ̸= j ′ , g̃j (x, ·) ̸= g̃j ′ (x, ·) as polynomials in θ. The failure sets have sizes: (a) ≤ q m0 −c3 ; (b)
≤ 3q (m0 +1)−c3 /q 1−c3 /2 = 3q m0 −c3 /2 (Markov); (c) for each pair, some θ-coefficient of g̃j − g̃j ′ is a
nonzero polynomial in x of degree ≤ d,            ˜ giving ≤ r̃2 dq
                                                                 ˜ m0 −1 ≤ q m0 −0.89 (since r̃2 d˜ ≤ 4q 0.06 ·q 0.04 ≤
q 0.101 by the absorption rule).
     Fix a good x and let Sx := supp F (x) (so |Sx | = tx , with integer weights wv := F (x)v ̸= 0).
                                 / X̃ ; ℓθ0 is injective on Sx (this excludes the roots of at most 2t̂ nonzero
                                                                                                           
Call θ0 valid if: (x, θ0 ) ∈
polynomials ⟨(1, θ, . . . , θJ−1 ), v−v′ ⟩ of degree ≤ J −1, i.e. ≤ t̂2 J values); and the values g̃j (x, θ0 )


                                                          11
are pairwise distinct (excluding ≤ r̃2 d˜ values). At least q − q 1−c3 /2 − t̂2 J − r̃2 d˜ ≥ q/2 valid θ0
exist. For valid θ0 the two integer measures
                           X                                X
                               wv eℓθ0 (v) = F̃ (x, θ0 ) =     ãj eg̃j (x,θ0 )
                             v∈Sx                                       j

have distinct atoms on each side, so the atom sets coincide with matching weights; in particular
tx = r̃, and there is a bijection σθ0 : Sx → [r̃] with g̃σθ0 (v) (x, θ0 ) = ℓθ0 (v) and ãσθ0 (v) = wv . Fix
v ∈ Sx : by pigeonhole some j has σθ (v) = j for at least (q/2)/r̃ ≥ 1 q 0.97 > d˜ valid θ0 , whence
                                          0                                   4
the polynomial identity in θ:
                                                         J
                                                         X
                                          g̃j (x, θ) =         vȷ θȷ−1 .                                (8.2)
                                                         ȷ=1

Distinct v yield distinct right-hand sides of (8.2), hence distinct j (two v’s sharing the same j
would force their moment-curve polynomials to coincide, i.e. v = v′ ); and (c) guarantees that
each v determines a unique j(v). Since |Sx | = tx = r̃, the assignment v 7→ j(v) is a bijection,
every g̃j (x, ·) has the form (8.2), and wv = ãj(v) .
Globalization. Write g̃j (x, θ) =
                                      P                                               ˜ By (8.2), for
                                          γj,i+1 (x)θi with γj,i ∈ Fq [x] of degree ≤ d.
                                         i≥0
every good x the coefficients with i ≥ J vanish; since the good set has ≥ q m0 (1 − 5q −c3 /2 ) points
and d˜ < q/2, these coefficients vanish identically. Set γ j := (γj,1 , . . . , γj,J ) (distinct tuples,
degrees ≤ d),˜ bj := ãj and r := r̃. For every good x, F (x) = P bj eγ (x) with the tuples γ (x)
                                                                         j     j          P          j
pairwise distinct (by (c) and (8.2)). Hence at good x the augmentation gives j bj = 1 over
Z, and ∥F (x)∥2 = j b2j ; averaging the mass bound over good points gives j b2j ≤ 2ĝ 2 and
                     P                                                                  P

r ≤ 2ĝ 2 . Let X be the non-good set: |X | ≤ q m0 −c3 + 3q m0 −c3 /2 + q m0 −0.89 ≤ 4q m0 −c3 /2 .
Moment identities. For |k| ≤ L2 we have 2|k|d¯ ≤ 2qP         0.335 ≤ q − 1, so P exists (of degree
                                                                                      k
      ¯ and equals µk everywhere; at good x, µk (x) =
≤ |k|d)                                                                      k
                                                                j b̄j γ j (x) ; the difference of the two
polynomials has degree ≤ |k|d˜ ≤ q 0.34 < q(1 − 4q −c3 /2 ) and vanishes off X , hence is zero
(Lemma 1.2).


9    Decoding the layers; converting penalties into class identities
Let (F1 , F2 , F3 , F6 ) be a coherent integer proof (Definition 4.1). Apply Theorem 7.1 to F1
(budget g 2 , E0 = ∅) and Theorem 8.1 to F2 , F3 , F6 (budget g 2 ≤ q 0.003 ; coordinate degrees
d, d3 , d6 ≤ q 0.031 ≤ q 0.035 ). This yields:

    • F1 : a list {(ai , Ai )}i≤r1 with Ai distinct, deg Ai ≤ d, ai ∈ Z \ {0},                       2     2
                                                                                  P              P
                                                                                     i ai = 1,    i ai ≤ 2g ;
      |X1 | ≤ 3q m−c3 .
                                                                                     ′
    • F2 : {(bj , γ j )}j≤r2 , distinct triples, deg γjι ≤ d+ := d + 2; |X2 | ≤ 4q m −c3 /2 ; identities (8.1)
      up to L2 .
                                                                    ′
    • F3 : {(ck , Bk )}k≤r3 , deg Bkκ ≤ d3 + 26; |X3 | ≤ 4q m −c3 /2 .

    • F6 : {(fk , Dk )}k≤r6 , deg Dkκ ≤ d6 + 7; |X6 | ≤ 4q m−c3 /2 .
                                                                                   √
   All list sizes are ≤ 2g 2 , all weights are nonzero integers of absolute value ≤ 2g < q/2 (hence
nonzero mod q), and every net (sum of weights over a sublist) has absolute value ≤ 2g 2 < q/2;

                                                     12
hence mod-q equalities
                    P      of nets upgrade to Z-equalities. Class measures: for a weighted
list of polynomials, j nj [Pj ] denotes the induced finitely supported Z- (or Fq -) valued measure
on the polynomial ring.
                                                      ι
                                            P               P
Lemma 9.1 (Slot pinning). For each ι:          j bj [γj ] =  i ai [Ai ◦ πι ] as Z-valued class measures
on Fq [w].
Proof. By (P1), margι F2 (w) = F1 (πι w) for all w. For w ∈             / X2 ∪ πι−1 (X1 ) (aPset of size ≤
   m  ′ −c /2      m ′ −c       m′ −c /2
4q        3   +3q        3 ≤ 5q      3   ), taking l-th moments of both sides gives, mod q, j b̄j γjι (w)l =
                  l                       0.004 ⌉, both sides are polynomials of degree ≤ l d ≤ q 0.035 <
P
   i āi Ai (πι w) . For 0 ≤ l ≤ ⌈q                                                          +
q(1 − 5q −c3 /2 ), so by Lemma 1.2 they are equal as polynomials. Since ⌈q 0.004 ⌉ ≥ r1 + r2 ,
Lemma 6.3 (over K = Fq (w)) gives equality of the Fq -class measures; nets upgrade to Z.

Lemma 9.2 (P4 matching: clause composites). Define Compj := Φ̂ · ι (γjι − sι ) ∈ Fq [w] and
                                                                                  Q
          P                     P                    P
Gk := κ Zκ Bkκ . Then j b̄j [Compj ] = k c̄k [Gk ] as Fq -class measures. Consequently, every
class of the composite list whose net is nonzero mod q equals some Gk and hence
                                       ′                              ′
vanishes identically on H m (each Zκ vanishes on H m ).
Proof. By P (P4), (Θw )∗ F2l(w) P = (Ξw )∗ F3 (w) for all w. For w ∈
                                                                   / X2 ∪ X3 , the l-th moments give,
                                                l                             ′
mod q,      j b̄j Compj (w) =       k c̄k Gk (w) . Degrees: deg Compj ≤ m (h − 1) + 3d+ ≤ 210h
and deg Gk ≤ h + d3 + 26 ≤ 270h; for 0 ≤ l ≤ ⌈q 0.004 ⌉ (≥ r2 + r3 ) we have l · 270h ≤
q 0.036 < q(1 − 8q −c3 /2 ), so Lemma 1.2 upgrades these to polynomial identities, and Lemma 6.3
concludes.

Lemma 9.3 (P6 matching: a Boolean class exists). There is i∗ ≤ r1 with ai∗ ̸= 0 and Ai∗ (x) ∈
{0, 1} for every x ∈ H m .
Proof. By (P6) and the same derivation (exceptional set X1 ∪X6 , degrees ≤ max(2d, h+d6 +7) ≤
130h, window ⌈q 0.004 ⌉ ≥ r1 + r6 ),
                                                    (6)   (6)
                   X                       X                     X
                        āi [ A2i − Ai ] =   f¯k [ Gk ], Gk :=       Zκ Dkκ ,
                       i                     k                            κ≤m

                                                                                                       2
                      P Fq [x1 , . . . , xm ]. Partition {1, . . . , r1 } according to the polynomial Ai −Ai ;
as Fq -class measures on
the part nets sum to i āi = 1̄ ̸= 0, so some part P has net ̸= 0 mod q. By the measure equality,
                                 (6)                  (6)
its polynomial equals some Gk , and every Gk vanishes identically on H m (each Zκ does; the
zero polynomial also qualifies). Pick any i∗ ∈ P: then (A2i∗ − Ai∗ )|H m = 0, i.e. Ai∗ is Boolean
on H m , and ai∗ ̸= 0. (The pairing A ↔ 1 − A merging into one part is harmless: any member
serves.)

Remark. Lemma 9.3 deliberately uses only polynomial-identity class facts evaluated on H m ,
never table values at points of H m : the subcube H m (of size hm ≤ q m/40 ) is far smaller than
any exceptional set, so pointwise facts there would be worthless.


10     Moment membership, the extended window, and triple
       rigidity
Lemma 10.1 (Moment membership, MM). Write F2 = i∈I ci Enc(A′i π) + P µ with ci ∈ Z
                                                             P
and A′i ∈ RM(m, d) distinct (possible since F2 is C2 -structured; I may be astronomically large).

                                                     13
Then for every k and every w,
                                         X
                      µk (F2 )(w) ≡              c̄i A′i (y1 )k1 A′i (y2 )k2 A′i (y3 )k3   (mod q).
                                             i

Moreover, if 2|k|d ≤ q − 1, then as polynomials
                                         X Y
                                    Pk =    c̄i A′i (yι )kι ;                                          (10.1)
                                                        i          ι

in particular Pk does not involve the s-variables, it involves the block yι only if kι > 0, and
degyι Pk ≤ kι d — uniformly in the other components of k.

Proof. The first display follows from Enc(A′ π)(w) = e(A′ (y1 ),A′ (y2 ),A′ (y3 )) , the linearity of µk , and
q | P . The right-hand side of (10.1) is a polynomial of total degree ≤ |k|d < q computing the
same function as Pk (of degree ≤ |k|d < q); by Lemma 1.2(ii) they are equal as polynomials,
and the structural properties are inherited from each summand.

Lemma 10.2 (Extended-window identities, R+). For all k with |k| ≤ L2 = ⌊q 0.3 ⌋,
                 X Y                  X Y
                    b̄j  γjι (w)kι =     c̄i  A′i (yι )kι  in Fq [w].                                  (R+)
                          j      ι                          i          ι

Proof. Concatenate (8.1) for F2 with (10.1); both are valid for |k| ≤ L2 (indeed 2|k|d ≤ q − 1
holds).
                                         P                P
Theorem 10.3 (Triple rigidity, R2).         j bj [γ j ] =   i ai [(Ai π1 , Ai π2 , Ai π3 )] as Z-valued
class measures on tuples; equivalently, r2 = r1 and, after reindexing, bi = ai and
γ i = (Ai π1 , Ai π2 , Ai π3 ).

Proof. Write θk for the common polynomial in (R+).
Phase I (locality). Claim: for each slot ι and each variable ξ outside the block yι (i.e. in yι′
with ι′ ̸= ι, or in s), degξ γjι = 0 for all j. Take ι = 1 (the other cases are symmetric, using
the tag pairs (1, 3) and (1, 2)). Fix a foreign ξ and let v := − degξ , a valuation on Fq (w) with
v ≤ 0 on nonzero polynomials and v = 0 exactly on the ξ-free ones. Group the indices j by
the pair (ψu , χu ) := (γj2 , γj3 ): say N ≤ r2 distinct pairs. Fix a group u0 . By Lemma 6.2 the
evaluation matrix (ψut2 χtu3 )u; t∈{0..N −1}2 over Fq (w) has rank N ; choose N independent columns,
P ∆ ̸=t2 0 tbe
let            the corresponding minor, and solve by Cramer’s rule for ct = (cofactor)/∆ with
    c  ψ  χ       uu0 . Entry ξ-degrees are ≤ 2(N − 1)d+ , so degξ ∆ and all cofactor degrees are
            3 = δ
   t t u u
     2
≤ 2r2 d+ . For every k with k + 2r2 ≤ L2 , grouping (R+) at k = (k, t2 , t3 ) gives
                                      X                         1 X
                              Qk :=          b̄j (γj1 )k =          (cofactor)t θ(k,t2 ,t3 ) .
                                                                ∆ t
                                      j∈u0

By Lemma 10.1, degξ θ(k,t2 ,t3 ) ≤ r2 d (more precisely ≤ t2 d if ξ ∈ y2 , ≤ t3 d if ξ ∈ y3 , and = 0
if ξ ∈ s) — uniformly in k. Hence v(Qk ) ≥ −D̄ for all such k, where D̄ := 5r22 d+ ≤ q 0.04 .
Let S := {j ∈ u0 : degξ γj1 ≥ 1} and suppose S ̸= ∅, ν := |S|. Within the group the γj1 are
pairwise distinct (the tuples are distinct and the pair is fixed). For j ∈    / S the terms b̄j (γj1 )k
are ξ-free, so pk := j∈S b̄j (γj1 )k satisfies v(pk ) ≥ −D̄ for all k ≤ L2 − 2r2 . Apply Lemma 6.1
                    P

with H = 0 (differences are nonzero polynomials, so v ≤ 0), β = D̄ and weights b̄j ∈ F×       q : some


                                                                14
l ≤ D̄ + 2ν − 1 ≤ q 0.05 ≤ L2 − 2r2 has v(pl ) < −D̄, a contradiction. So S = ∅. Applying this to
all foreign ξ and all slots: γjι = Gιj (yι ) with Gιj ∈ Fq [yι ] of degree ≤ d+ .
Phase II (coupling). Substitute y2 := y1P           into (R+) (a ring homomorphism, so identities are
preserved). The right-hand side becomes i c̄i A′i (y1 )k1 +k2 A′i (y3 )k3 , a function of (k1 +k2 , k3 )
only. Subtracting the identities for (k1 , k2 , k3 ) and (k1 −1, k2 +1, k3 ) (with k1 ≥ 1),
                     X
                         b̄j G1j (y1 ) − G2j (y1 ) G1j (y1 )k1 −1 G2j (y1 )k2 G3j (y3 )k3 = 0.
                                                  

                       j

The nodes nj := (G1j (y1 ), G2j (y1 ), G3j (y3 )) ∈ Fq (y1 , y3 )3 are pairwise distinct (coordinatewise
equality forces equality of the polynomial triples, i.e. j = j ′ ). Taking (k1 − 1, k2 , k3 ) = t ∈
{0, . . . , r2 − 1}3 (all with |k| ≤ 3r2 ≤ L2 ), Lemma 6.2(ii) gives b̄j (G1j − G2j ) = 0 for every j; since
b̄j ̸= 0, G1j = G2j . The substitution y3 := y1 likewise gives G1j = G3j . So every tuple is coupled:
γ j = (Gj π1 , Gj π2 , Gj π3 ) with Gj := G1j pairwise distinct.
                                                                     P                  P
Phase III (identification). Lemma 9.1 with ι = 1 reads j bj [Gj (y1 )] = i ai [Ai (y1 )] with
all atoms distinct on each side; hence the weighted sets coincide: {(bj , Gj )} = {(ai , Ai )}.


11     Endgame
                                                                                     Q3
Lemma 11.1 (Injectivity of composites). The map A 7→ CompA := Φ̂ ·                     ι=1 (A(yι ) − sι ) is
injective on Fq [x1 , . . . , xm ] (for arbitrary degrees), and CompA ̸= 0.
Proof. We have Φ̂ ̸= 0 (as φ has a clause), and each factor A(yι ) − sι is a nonzero polyno-
mial, of degree 1 in sι with leading coefficient −1 (a unit), and hence irreducible in the UFD
Fq [y1 , y2 , y3 , s1 , s2 , s3 ] (a factorization would Q
                                                         have a unit degree-0-in-sι factor). If CompA =
CompA′′ , cancel Φ̂: the irreducible factors of ι (A(yι ) − sι ) match those of ι (A′′ (yι ) − sι ) up
                                                                                       Q
to scalars. Only the ι-th factor on each side involves sι (the three variable blocks (yι , sι ) are
disjoint), so A(y1 ) − s1 = c(A′′ (y1 ) − s1 ) for a scalar c; comparing s1 -coefficients gives c = 1,
hence A = A′′ .

Theorem 11.2 (Extraction). If a coherent integer proof exists, then φ is satisfiable.
Proof. Decode as in §9. By Theorem 10.3, r2 = r1 and the layer-2 classes are {(ai , (Ai π1 , Ai π2 ,
Ai π3 ))}i≤r1 ; thus the composite list of Lemma 9.2 is {(ai , CompAi )}i≤r1 .
(i) Every class is clause-good. By Lemma 11.1 the CompAi are pairwise distinct, so each
class of the composite partition is a singleton {i} with netQai , and āi ̸= 0 (since 0 < |ai | < q/2).
By Lemma 9.2, for every i the polynomial CompAi = Φ̂ ι (Ai (yι ) − sι ) vanishes identically on
    ′
Hm .
(ii) A Boolean class exists. By Lemma 9.3 there is i∗ with ai∗ ̸= 0 and Ai∗ Boolean on H m .
Combination. Define α(v) := Ai∗ (ιvar (v)) ∈ {0, 1} for each variable v of φ. Let C be any
                                m′
     Q and w := w(C) ∈ H . Then Φ̂(w) = ϕ̂(w) = 1, so by (i) applied at thempoint w we
clause
get ι (Ai∗ (yι ) − sι ) = 0, i.e. Ai∗ (yι ) = sι for some ι; since yι = ιvar (vι ) ∈ H , this says
α(vι ) = sι = 1 − bι , i.e. the literal ℓι is true under α. So α satisfies every clause.

Corollary 11.3 (Soundness). If φ is unsatisfiable, then dist2 (t⋆ , L) > q c ∆φ .
Proof. Otherwise Proposition 4.2 yields a coherent integer proof, and Theorem 11.2 a satisfying
assignment.

                                                    15
12      Parameter ledger and proof of the main theorem
12.1     Ledger
                                   4                   5
Throughout, N ≥ N0 = 22·10 , hence q ≥ 210 and every explicit constant ≤ 2100 is ≤ q 0.001
(absorption). Base quantities: h ≤ q 1/40 ; d = 60h ≤ q 0.026 ; d+ = d + 2; d3 = 267h + 3 ≤ q 0.031 ;
d6 = 128h ≤ q 0.029 ; d˜ ≤ d¯ + 26 ≤ q 0.032 ; g 2 = 16q 0.002 ≤ q 0.003 ; list sizes r• ≤ 2g 2 ≤ q 0.0031 ;
t̂ = ⌈ĝ 2 q c3 ⌉ ≤ 2q 0.03 for scalar calls with ĝ 2 ≤ q 0.02 , while for the θ-calls of §8 (where ĝ 2 = g 2 )
one has t̂ ≤ 2q 0.013 ; windows L1 = ⌈q 0.15 ⌉, L2 = ⌊q 0.3 ⌋.


                                                       16
#    Requirement                                   Instantiation                        Check
1    Bertrand: d40 ≤ q < 2d40                      —                                     ✓
2    scalar cap d¯ ≤ q 0.04                        max: d3 + 26 ≤ q 0.032                ✓
3    scalar budgets 16 ≤ ĝ 2 ≤ q 0.02             direct: g 2 ; θ-calls: t̂ ≤           ✓
                                                   2q 0.013 , so t̂g 2 ≤ 2q 0.016
4    Step-1 minor SZ: 2t̂(t̂ + 1)d¯ < q(1 −        ≤ 12q 0.1                             ✓
     2q −c3 )
5    Prop. 5.4 ranges used: 2ld¯ ≤ q − 1 for       2L1 d¯ ≤ q 0.2 ; 2L2 d3 ≤ 2q 0.335    ✓
     l ≤ max(2t̂, L1 ); 2|k|d¯ ≤ q − 1 for |k| ≤
     L2
6    CM precondition q > 2δ 4 , δ ≤ D0 =           2δ 4 ≤ q 0.42                         ✓
     9q 0.1
7    CM slack:            (δ−1)(δ−2)q −1/2 +       —                                     ✓
          13/3 −1      −0.29
     5δ       q ≤ 2q
 8   conjugate case: δ 2 q −1 ≤ q −0.79 ≪ 1        —                                     ✓
 9   very-good losses ≤ 2r2 H0 q −1 ≤ q −0.83      H0 = D0                               ✓
10   Step 3: DA = r2 H0 + rd¯ ≤ q 0.17 ;           M1 = ⌊q 0.05 ⌋:      q 0.1 /32 >      ✓
     (2M1 +2)DA q −1 ≤ q −0.77 ; M12 /32 >         q 0.02
     ĝ 2
11   no-poles window 2H0 r+2r ≤ 40q 0.13 ≤         —                                     ✓
     L1
12   degree window 2rd+2r ¯      ≤ 10q 0.07 ≤ L1   —                                     ✓
13                   ¯
     (7.1)-SZ: L1 (d + rH0 ) ≤ 19q   0.28
                                           < q/2   —                                     ✓
                           2 m0 −2
                                    √
14   lift: unclean ≤ 4ĝ q         ; 2ĝ < q/2;    —                                     ✓
     |X | ≤ 3q m0 −c3
15   tuple: |E0′ | ≤ q (m0 +1)−c3 (scalar E0 -     —                                     ✓
     cap)
                                                   1 0.97
16   tuple: valid θ0 count ≥ q−q 0.995 −t̂2 J −    4q     > q 0.032                      ✓
     r̃2 d˜ ≥ q/2; pigeonhole (q/2)/r̃ > d˜
17   tuple exceptional ≤ 4q m0 −c3 /2 ; down-      —                                     ✓
     stream SZ uses 1 − 8q −c3 /2 > 12
18   (8.1)/(R+) SZ: L2 d˜ ≤ q 0.34 < q/2;          —                                     ✓
     MM-form L2 d < q
19   CS windows: ⌈q 0.004 ⌉ ≥ r1 + r2 , r2 +       Lemmas 9.1–9.3                        ✓
     r3 , r1 + r6 (≤ 4g 2 ≤ q 0.0032 ); degrees
     l · 270h ≤ q 0.036 < q/2
20   Phase I: D̄ = 5r22 d+ ≤ q 0.04 ; window       —                                     ✓
     D̄+2r2 −1+2r2 ≤ q 0.05 ≤ L2 ; k+2r2 ≤
     L2
21   Phase II window 3r2 ≤ q 0.004 ≤ L2            —                                     ✓
22   completeness degrees: 50h ≤ d3 , 15h ≤        —                                     ✓
     d6 , m(h − 1) ≤ d
23   soundness radius:         q c ∆φ < q 31 ;     Prop. 4.2                             ✓
     |ℓρ (F )| ≤ 2q ; W · 3q 41 < q 1043 <
                     41

     P − q 31 ; q 31 < W
24   nets: 2g 2 < q/2 (mod-q to Z upgrades)        32q 0.002 < q/2                       ✓
                                              −5
25   n ≤ 2q 54 ≤ q 55 ; (1 + q −10 ) ≤ q 10 ;      9.9 × 10−4 = 55 · 1.8 × 10−5          ✓
     c − 10−5 ≥ 55c′


                                            17
12.2    Proof of Theorem 1.1
The reduction of §2 maps a 3CNF formula φ to (B0 /R, t⋆ /R) in deterministic polynomial
time (§2.5), with lattice rank n ≤ q 55 by (2.2). If φ is satisfiable, then dist2 (t⋆ , L) ≤ ∆φ
(Proposition 3.3), so the output instance has distance ≤ ∆φ /R ≤ 1: a YES instance. If φ is
unsatisfiable, then dist2 (t⋆ , L) > q c ∆φ (Corollary 11.3), so the output distance exceeds

              q c ∆φ     qc             −5         −4                    1.8×10−5       ′
                     ≥      −10
                                ≥ q c−10 = q 9.9×10   ≥           q 55               ≥ nc ,
                 R     1+q
                                                                                                ′
a NO instance (ledger #25). Degenerate inputs are handled by §2.6 (for n = 1 we have nc = 1,
and the fixed instances have distances 0 and 3/2). Composing with the Cook–Levin reduction
of any NP language to 3SAT completes the proof, with c′ = 1.8 × 10−5 . ■
External results used without proof. Cook–Levin; Bertrand’s postulate; polynomial-time
Hermite normal form computation with polynomial bit-sizes (Kannan–Bachem); the Delsarte–
Goethals–MacWilliams duality GRMq (ρ, 2)⊥ = GRMq (2q − 3 − ρ, 2) (Proposition 5.2); Cafure–
Matera’s explicit estimate |#V (Fq ) − q dim V | ≤ (δ − 1)(δ − 2)q dim V −1/2 + 5δ 13/3 q dim V −1 for
absolutely irreducible affine V of degree δ under q > 2δ 4 , and the elementary bound #W (Fq ) ≤
deg W · q dim W . The use of the Cafure–Matera bound has massive slack: any bound of the shape
q m0 + δ O(1) q m0 −1/2 valid for q > δ O(1) suffices, since δ ≤ 9q 0.1 here.


                                                 18
