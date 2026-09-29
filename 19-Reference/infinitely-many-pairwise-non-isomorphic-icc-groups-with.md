---
title: "INFINITELY MANY PAIRWISE NON-ISOMORPHIC ICC GROUPS WITH"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/aa58ac140721d83f9850ce35c507daf387ba6334.pdf"
category: "19-Reference"
fetched_at: "2026-08-07T06:39:13Z"
tags: ["news-research"]
---

INFINITELY MANY PAIRWISE NON-ISOMORPHIC ICC GROUPS WITH
 PROPERTY (T) AND A COMMON GROUP VON NEUMANN ALGEBRA

        Abstract. We construct a countably infinite family {Γi }i∈N of pairwise non-isomorphic
        countable discrete ICC groups, each with Kazhdan’s property (T), such that the group von
        Neumann algebras L(Γi ) are mutually isomorphic (trace-preservingly). The groups are twisted
        extensions
                         Gf = Fq [t]4g ×f d Sp2g (Fq [t]), f ∈ Fq [t], q = 2s , g ≥ 2,
        of the symplectic group H = Sp2g (Fq [t]) by the H-module A = Fq [t]4g , where d is a characteristic-
        two metaplectic 2-cocycle extracted from intertwiners of a Weyl system over the local field
        k∞ = Fq ((t−1 )). Three phenomena drive the proof: (1) after a conjugate doubling which
        cancels all scalar (Weil-index) ambiguities, the cocycle d becomes an exact coboundary with
        coefficients in the unitary group of L∞ (A),
                                                 b and a dual isogeny (“isogeny spreading”) transports
        the one untwisting family to all multiples f d at once — whence L(Gf ) ∼   = L(G0 ) for every f ;
        (2) in characteristic two the Weil index of a metaplectic
                                                        p         unipotent is not a scalar but a lattice
        vector, namely the half-Frobenius derivative du/dt, which makes the map f 7→ f [d] injec-
        tive on cohomology; (3) a Morita/Noether–Skolem rigidity analysis of abstract isomorphisms
        Gf → Gf ′ shows that each isomorphism class meets the family {Gf }f ∈R in at most q(q − 1)2 s
        members. Hence infinitely many of the Gtd are pairwise non-isomorphic while all of them
        have the same II1 factor. In particular, group von Neumann algebras need not remember ICC
        Kazhdan groups, and they can fail to do so with infinite multiplicity.


                                             1. Introduction
   For a countable discrete group G, the group von Neumann algebra L(G) ⊆ B(ℓ2 G) is the
bicommutant of the left regular representation (λh )h∈G ; it carries the faithful normal tracial
state τ (x) = ⟨xδe , δe ⟩, and it is a II1 factor whenever G is infinite with infinite conjugacy
classes (ICC) — Lemma 2.6 below. Connes’ rigidity conjecture predicts that for ICC groups
with Kazhdan’s property (T), the algebra L(G) should completely remember G. The present
paper refutes this prediction in a strong, quantified form:
Main Theorem. There exists a countably infinite family {Γi }i∈N of pairwise non-isomorphic
countable discrete ICC groups, each with Kazhdan’s property (T), such that L(Γi ) ∼  = L(Γj ),
                                                                        s
trace-preservingly, for all i, j. Explicitly, for any prime power q = 2 and any g ≥ 2 one may
take a suitable infinite subfamily of the twisted extensions
                        Gf = Fq [t]4g ×f d Sp2g (Fq [t]),    f = td , d ∈ N,
                                      

where d is the characteristic-two metaplectic 2-cocycle constructed in §5; the common II1 factor
is L(G0 ), the group von Neumann algebra of the split extension G0 = Fq [t]4g ⋊ Sp2g (Fq [t]).
1.1 Strategy. Fix once and for all a prime power q = 2s and an integer g ≥ 2, and write
  R := Fq [t],      k∞ := Fq ((t−1 )),         S := R2g ,        H := Sp2g (R),          A := S ⊕ S = R4g ,
with H acting on S through the standard symplectic representation and on A diagonally.
All groups of the family are extensions of the same pair (H, A): for a normalized 2-cocycle
c ∈ Z 2 (H, A) we write A ×c H for the set A × H with multiplication (a, γ)(b, γ ′ ) = (a + γb +
c(γ, γ ′ ), γγ ′ ). The family is {Gf = A ×f d H}f ∈R , where d = (d, d) and d ∈ Z 2 (H, S) is a
metaplectic cocycle. The proof has three independent parts.
                                                        1
2                     NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

  (I) One algebra for all f (§§3–6). The cocycle d arises as follows. The additive group
       2g                                             g
V∞ = k∞   carries a Weyl system v 7→ uv on H = L2 (k∞   ) with multiplier β, whose restriction
to the discrete cocompact lattice S ⊂ V∞ is an honest unitary representation generating a
maximal abelian subalgebra (“lattice masa”). Each γ ∈ H preserves the relations, and by the
Stone–von Neumann–Mackey uniqueness theorem there are intertwining unitaries Vγ′ , which
can be normalized so as to permute the lattice Weyl operators without phases: Vγ′ un Vγ′∗ = uγn
(n ∈ S). The composition law then reads

                   Vγ′ Vγ′′ = µ(γ, γ ′ ) ud(γ,γ ′ ) Vγγ
                                                      ′
                                                        ′,   µ(γ, γ ′ ) ∈ T, d(γ, γ ′ ) ∈ S,

and d is a normalized 2-cocycle whose class κ = [d] ∈ H 2 (H, S) is independent of all choices.
The scalar µ — the Weil-index part — is uncontrollable, but the conjugate doubling Vγ :=
Vγ′ ⊗ Vγ′ on H ⊗ H cancels it identically, leaving the exact relation Vγ Vγ ′ = Ud(γ,γ ′ ) Vγγ ′ , where
a 7→ Ua is a representation of A generating a masa isomorphic to L∞ (X), X = A.      b Comparing
Vγ with the Koopman unitaries of the dual action H ↷ X produces unitaries wγ ∈ U(L∞ (X))
with the exact identity
                                     wγ · γ wγ ′ = ed(γ,γ ′ ) wγγ ′ ,
i.e. the image of [d] in H 2 H, U (L∞ (X)) vanishes — with no measurable selection anywhere:
                                            

all identities hold on the nose in the unitary group of L∞ (X). Finally, multiplication by f on
A dualizes to a measure-preserving surjection fˆ : X → X commuting with the H-action, and
               (f )
composing, wγ := wγ ◦ fˆ untwists f d — one untwister spreads to the whole ladder {f d}f ∈R
at once. Feeding w(f ) into the canonical copy of L∞ (X) inside M = L(G0 ) yields unitaries
πf (a, γ) ∈ M satisfying the Gf -relations, with full generation and the right trace; a standard
recognition principle then gives trace-preserving isomorphisms L(Gf ) ∼ = M for every f ∈ R.
   (II) Infinitely many groups (§§9–10). Distinguishing the Gf needs the opposite esti-
mate: the classes f κ must not die. Here characteristic two produces a small miracle. Restrict
κ to the Siegel unipotent one-parameter subgroup Nα = {νu }u∈R ∼      = (R, +). An explicit nor-
malized gauge over Nα by multiplication operators exists, and its cocycle is computed by
second-degree characters hu of k∞ : the resulting symmetric R-valued cocycle ρ(u, u′ ) has di-
agonal
                                                  p
                                      ρ(u, u) = du/dt ∈ R
— the half-Frobenius derivative: in characteristic two the square of a metaplectic unipotent is
not a scalar (a Weil index) but a lattice translation, and it is unbounded as u ranges over R.
On the other hand, over a module of exponent two the diagonal p   of any equivariant coboundary
is forced to be of the Frobenius-square form u 7→ r0 u2 . Since f du/dt = r0 u2 for all u forces
r0 = 0 (take u = 1) and then f = 0 (take u = t), we get AnnR (κ) = 0: the ladder f 7→ f κ is
injective. To convert this into non-isomorphism of the groups we analyse an arbitrary abstract
isomorphism Ψ : Gf → Gf ′ . A transvection argument in characteristic two shows that A is
the largest abelian normal subgroup of each Gf (every abelian normal subgroup of Sp2g (R)
is trivial — note that −I = I here, so this is sharper than in characteristic zero), whence
Ψ(A) = A and Ψ induces a compatible pair (α, β) and an Eilenberg–MacLane class equation
α∗ [f d] = β ∗ [f ′ d]. A Morita/Noether–Skolem analysis of α — the F2 -span of the diagonal
H-action on A is all of M2g (R) acting diagonally — factors α = G ◦ θ• ◦ Λ with θ in the finite
group Aut(R), G = diag(g, g) with g normalizing H (hence g ∈ F×    q H: the H-invariant bilinear
forms are R ω and q − 1 is odd), and Λ ∈ GL2 (R) mixing the two legs. Pushing the class
equation through this factorization, using that inner transports act trivially on H 2 and a unit
                     NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                              3

lemma coming from the inverse isomorphism, leaves the master equation
                           f ′ κ = ξ θ(f ) κθ ,   ξ ∈ F×
                                                       q , θ ∈ Aut(R),

with κθ depending only on θ. As f ′ 7→ f ′ κ is injective, at most (q − 1) · | Aut(R)| = q(q − 1)2 s
polynomials f ′ can have Gf ′ ∼= Gf . The infinite set {Gtd }d∈N therefore meets infinitely many
isomorphism classes.
    (III) ICC and property (T) (§§7–8). Each Gf is ICC by direct orbit computations
                                                                                    4g
with symmetric shears. For property (T), G0 = A ⋊ H is a lattice in G = k∞             ⋊ Sp2g (k∞ )
— discreteness and a fundamental-domain computation with the compact exact domain m4g ,
together with the Harder–Behr theorem that H is a lattice in Sp2g (k∞ ). The ambient group G
                                        4g
has (T): relative property (T) for (G, k∞  ) is assembled from 2g embedded copies of SL2 (k∞ ) ⋉
  2
k∞ by a uniformity-plus-circumcenter argument, and Sp2g (k∞ ) has (T) for g ≥ 2. Hence G0
has (T); by Connes–Jones, the II1 factor M = L(G0 ) has property (T), and since each Gf is
ICC with L(Gf ) ∼ = M , the converse direction of Connes–Jones gives property (T) for every Gf .
    Why characteristic 2. Four mechanisms make the construction work precisely in charac-
teristic 2. (i) The symplectic form ω is symmetric and all characters of the exponent-2 lattice
are {±1}-valued, so the conjugate doubling V 7→ V ⊗ V cancels the metaplectic scalar exactly,
with no sign hazards. (ii) The Weil index of a metaplectic unipotentpdegenerates from a root
of unity into a lattice vector — the half-Frobenius identity ρ(u, u) = du/dt of §9 — which is
unbounded over R and makes the ladder f 7→ f κ injective. (iii) Over exponent-2 modules, the
diagonal
      p of a symmetric     coboundary equation collapses to a Frobenius square r0 u2 , transverse
                       ×
to f du/dt. (iv) |Fq | = q − 1 is odd, so the scalar arising in the normalizer computation of
§10 is automatically a square, and no similitude-type outer automorphisms appear.
    Split versus twisted. G0 is the split extension; each Gf with f ̸= 0 is a non-split twist of
the same pair (H, A), and Gf ∼  ̸ G0 (Theorem 10.15). The twist is visible to group cohomology
                                 =
with coefficients in A but becomes invisible after pushing the coefficients into the unitary group
of L∞ (A):
         b that is the precise sense in which these groups are identical to the von Neumann
algebra and different to group theory.
    Throughout, q = 2s and g ≥ 2 are fixed.
1.2 Results from the literature. We use the following named results with precise statements
and without reproof.
     • [SvN] (Stone–von Neumann–Mackey; Mackey, A theorem of Stone and von Neumann,
       Duke Math. J. 16 (1949); see also Kleppner, Math. Ann. 158 (1965), and Baggett–
       Kleppner, J. Funct. Anal. 14 (1973)). Let Y be a second countable locally compact
       abelian group and β a continuous multiplier on Y whose symmetrizer y 7→ β(y, ·)β(·, y)−1
       is a topological isomorphism Y → Yb . Then any two irreducible strongly continuous β-
                                                                                      2g
       representations of Y are unitarily equivalent. (We apply this only to Y = k∞      with the
       explicit multiplier β(v, w) = ψ(⟨v2 , w1 ⟩), which is the Mackey–Heisenberg multiplier of
                                              g
       G×G   b for the self-dual group G = k∞   .)
     • [HB] (Reduction theory over function fields: Harder, Invent. Math. 7 (1969); Behr, In-
       vent. Math. 7 (1969); see also Margulis, Discrete Subgroups of Semisimple Lie Groups,
       I.3.2). Let k = Fq (t), let G be a semisimple k-group, and let ∞ be the place with comple-
       tion k∞ = Fq ((t−1 )) and ring of integers away from ∞ equal to Fq [t]. Then G(Fq [t]) is
       a lattice in G(k∞ ): a discrete subgroup such that the quotient carries a G(k∞ )-invariant
       Borel probability measure. In particular this holds for G = Sp2g .
     • [BHV-HR] (Bekka–de la Harpe–Valette, Kazhdan’s Property (T), Thm. 1.6.1). For
       every local field K and g ≥ 2, Sp2g (K) has property (T). (The treatment there is
4                    NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

       uniform in the local field — it proceeds through relative property (T) for pairs of the
       form (SL2 (K) ⋉ K 2 , K 2 ) and root-subgroup generation — and imposes no restriction
       on the characteristic.)
     • [BHV-SL2] (BHV, §1.4). For every local field K, the pair (SL2 (K) ⋉ K 2 , K 2 ) has
       relative property (T).
     • [BHV-Lat] (BHV, Thm. 1.7.1). A lattice in a locally compact second countable group
       with property (T) has property (T). (Lattice: a discrete subgroup such that the quotient
       carries a finite invariant regular Borel measure; the invariant measure our Lemma 8.6
       produces is Radon, hence regular.)
     • [CJ] (Connes–Jones, Bull. London Math. Soc. 17 (1985)). For a countable ICC group
       G, the II1 factor L(G) has property (T) in the sense of Connes–Jones if and only if
       G has property (T). Property (T) for a II1 factor is defined intrinsically (in terms of
       correspondences, i.e. Hilbert bimodules, of the factor); in particular it is an invariant
       of the factor up to ∗-isomorphism.
   We freely use standard facts from measure theory, abstract harmonic analysis, and von
Neumann algebra theory — existence and uniqueness of Haar measure, Riesz–Markov, Stone–
Weierstrass, density of C(K) in L2 , the bicommutant theorem, Kaplansky density, σ-weak
continuity of normal ∗-homomorphisms on bounded sets, divisibility of T (extension of char-
acters from subgroups) and the fact that T has no small subgroups, regularity of finite Borel
measures on locally compact second countable spaces, compact-metrizability of duals of count-
able discrete abelian groups, Urysohn’s lemma, and the structure theorem for finitely generated
modules over a PID — and cite these as [SF] at the point of use. Noether–Skolem for matrix
rings over a PID, needed in §10, is proved in Appendix A.

                                            2. Preliminaries
2.1 Group cohomology and twisted extensions. Let Q be a group acting on an abelian
group B (written (γ, b) 7→ γb, by automorphisms). A map c : Q × Q → B is a 2-cocycle if
                 γ1 c(γ2 , γ3 ) + c(γ1 , γ2 γ3 ) = c(γ1 γ2 , γ3 ) + c(γ1 , γ2 )   (γi ∈ Q),
and a 2-coboundary if c = ∂n for some n : Q → B, where (∂n)(γ, γ ′ ) := γn(γ ′ ) − n(γγ ′ ) + n(γ).
Coboundaries are cocycles (direct substitution), and H 2 (Q, B) := Z 2 (Q, B)/B 2 (Q, B). A
cocycle is normalized if c(e, γ) = c(γ, e) = 0 for all γ. Setting γ1 = γ2 = e in the cocycle
identity gives c(e, γ3 ) = c(e, e), and γ2 = γ3 = e gives c(γ1 , e) = γ1 c(e, e); hence subtracting ∂n
for the constant map n ≡ c(e, e) normalizes any cocycle without changing its class.
   If a commutative ring R acts on B by endomorphisms commuting with the Q-action, then
(f · c)(γ, γ ′ ) := f c(γ, γ ′ ) makes Z 2 , B 2 , H 2 into R-modules (note f · ∂n = ∂(f ◦ n)). For a
subgroup N ≤ Q, restriction of cochains induces an R-linear map resQ             2            2
                                                                           N : H (Q, B) → H (N, B).
If B = B1 ⊕ B2 as Q- and R-modules, then cochains split componentwise and H (Q, B) =        2

H 2 (Q, B1 ) ⊕ H 2 (Q, B2 ), compatibly with the R-structure and with restriction.
   Given a normalized c ∈ Z 2 (Q, B), the set B × Q with the multiplication
                                (a, γ)(b, γ ′ ) := (a + γb + c(γ, γ ′ ), γγ ′ )
is a group, denoted B ×c Q: associativity is exactly the cocycle identity; (0, e) is the unit by
normalization; and (a, γ)−1 = γ −1 a+γ −1 c(γ, γ −1 ), γ −1 whenever B has exponent 2 (the case
relevant to this paper; in general one inserts minus signs), as one checks by multiplying out.
The subset B × {e} is a subgroup isomorphic to B (by normalization, (a, e)(b, e) = (a + b, e));
the projection p(a, γ) := γ is a surjective homomorphism B ×c Q → Q with kernel B × {e},
                    NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                             5

which is therefore normal; and conjugation on the kernel is the given action:
                                  (b, γ)(a, e)(b, γ)−1 = (γa, e).                            (2.1)
Indeed (b, γ)(a, e) = (b + γa, γ) = (γa, e)(b, γ), using normalization of c twice. We identify B
with B × {e} ⊴ B ×c Q throughout. For c = 0 this is the semidirect product B ⋊ Q.
2.2 Property (T) for locally compact groups. All topological groups in this paper are lo-
cally compact, Hausdorff, second countable (lcsc), hence σ-compact and metrizable. A strongly
continuous unitary representation (π, H) of an lcsc group G has almost invariant vectors (a.i.v.)
if for every compact Q ⊂ G and every ε > 0 there is a unit vector ξ with supg∈Q ∥π(g)ξ −ξ∥ ≤ ε;
such a vector is called (Q, ε)-invariant. For a closed subgroup N ≤ G, the pair (G, N ) has
relative property (T) if every strongly continuous unitary representation of G with a.i.v. has a
nonzero N -invariant vector; G has property (T) if (G, G) does. For countable discrete groups
(“compact”=“finite”) this is the usual definition. Relative property (T) is an invariant of the
pair: if ϕ : G → G′ is a topological group isomorphism with ϕ(N ) = N ′ , then (G, N ) has
relative (T) iff (G′ , N ′ ) does (compose representations with ϕ).
Lemma 2.1 (circumcenter). Let B ̸= ∅ be a bounded subset of a Hilbert space H. There is
a unique c0 ∈ H minimizing r(c) := supb∈B ∥c − b∥, and every unitary u of H with uB = B
satisfies uc0 = c0 .
Proof. Let r := inf c r(c) and pick cn with r(cn ) → r. For any b ∈ B, the parallelogram law
gives
                                                                        2
                   ∥cn − cm ∥2 = 2∥cn − b∥2 + 2∥cm − b∥2 − 4 cn +c
                                                                 2
                                                                   m
                                                                     −b .
Bound the first two terms by 2r(cn )2 + 2r(cm )2 ; taking the supremum over b ∈ B in the
                                                            m 2
subtracted term yields −4 supb ∥ cn +c    − b∥2 = −4 r cn +c    ≤ −4r2 . Hence ∥cn − cm ∥2 ≤
                                        m
                                                             
                                      2                   2
       2           2      2
2r(cn ) + 2r(cm ) − 4r → 0: the sequence is Cauchy, with limit c0 , and r(c0 ) = r since
r(·) is 1-Lipschitz. If c′0 is another minimizer, the same inequality applied to the pair c0 , c′0
gives ∥c0 − c′0 ∥2 ≤ 4r2 − 4r2 = 0. Finally, if uB = B then r(uc0 ) = supb∈B ∥uc0 − b∥ =
supb∈B ∥c0 − u−1 b∥ = r(c0 ) = r, so uc0 = c0 by uniqueness.                                   □
2.3 Topological facts. We record, with proofs or precise references, the point-set facts we
use.
Lemma 2.2. Let S     G be an lcsc group. (i) There are compact sets Q1 ⊆ Q2 ⊆ · · · with
Qn ⊆ int Qn+1 and n Qn = G; consequently every compact subset of G is contained in some
Qn . (ii) If N ⊴ G is closed, the quotient G/N is an lcsc group, the quotient map p : G → G/N
is continuous and open, and every compact subset of G/N is the image under p of a compact
subset of G. (iii) A discrete subgroup Γ ≤ G is closed, and G/Γ is a locally compact Hausdorff
second countable space on which G acts continuously with open orbit maps.
                                           S
Proof. (i) By σ-compactness write G = n Kn with Kn compact. Set Q1 := K1 and inductively
let Qn+1 be a compact set containing the compact Qn ∪ Kn+1 in its interior (cover Qn ∪ Kn+1
by finitely many compact neighborhoods and take their union). If K is compact, the open sets
int Qn cover K, and they increase, so K ⊆ Qn for some n. (ii) Openness of p: for U ⊆ G
open, p−1 (p(U )) = U N is open. G/N is Hausdorff (N closed), locally compact and second
countable (continuous open images preserve both), and a topological group. Compact lifting: let
K̇ ⊂ G/N be compact, and let W be a compact neighborhood of e in G. The open sets       p(gW ◦ ),
g ∈ G, cover G/N ; choose g1 , . . . , gk with K̇ ⊆ i p(gi W ◦ ). Then K :=               −1
                                                   S                          S       
                                                                                i gi W ∩ p (K̇)
is compact (p−1 (K̇) is closed) with p(K) = K̇. (iii) Let Γ be discrete: there is an open U ∋ e
with U ∩ Γ = {e}; choose an open symmetric V ∋ e with V −1 V ⊆ U . For any x ∈ G, the set
6                    NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

xV meets Γ in at most one point: if γ, γ ′ ∈ Γ ∩ xV then γ −1 γ ′ ∈ (xV )−1 (xV ) = V −1 V ⊆ U , so
γ = γ ′ . Now let x ∈ Γ; since xV is a neighborhood of x, there is a (then unique) γ ∈ Γ ∩ xV . If
x ̸= γ, then xV ∖{γ} is a neighborhood of x disjoint from Γ, contradicting x ∈ Γ. So x = γ ∈ Γ:
Γ is closed. The quotient G/Γ is then a locally compact Hausdorff second countable space, the
projection is open (as in (ii)), and compact subsets of G/Γ lift to compact subsets of G (same
proof as in (ii)).                                                                               □

2.4 Dual pairs, masas, and normal maps. For a countable discrete abelian group Y , the
dual Yb = Hom(Y, T) is a compact metrizable abelian group; let µ be its Haar probability
measure and ey ∈ C(Yb ), ey (x) := x(y), so that ey ey′ = ey+y′ , ey = e−y , e0 = 1.

Lemma 2.3 (dual pair). (i) {ey }y∈Y is an orthonormal basis of L2 (Yb , µ). (ii) The commutant
of {Mey : y ∈ Y } in B(L2 (Yb )) is {MF : F ∈ L∞ (Yb )}; in particular L∞ (Yb ) (acting by
multiplication) is a masa, and {Mey }′′ = L∞ (Yb ). (iii) Let y 7→ Sy be a unitary representation
of Y on a Hilbert space K with a unit vector Ω such that ⟨Sy Ω, Ω⟩ = δy,0 and span{Sy Ω} =
K. Then there is a unique unitary W : L2 (Yb ) → K with W ey = Sy Ω for all y; it satisfies
W Mey W ∗ = Sy ; hence S := {Sy }′′ is a masa in B(K) and Jb := Ad W : L∞ (Yb ) → S is a unital
                                                  b )Ω, Ω⟩ = F dµ for all F ∈ L∞ (Yb ).
                                                                 R
normal ∗-isomorphism with J(e  b y ) = Sy and ⟨J(F
                                          R                                   R
Proof. (i) Orthonormality: ⟨ey , ey′ ⟩ = ey−y′ dµ, so it suffices to show ey dµ = 0 for y ̸= 0.
There is x0 ∈ Yb with x0 (y) ̸= 1: the cyclic group ⟨y⟩ admits a character not trivial at y (if y
has infinite order, send y to any z ̸= 1; if order m > 1, send y to a primitive m-th root of unity),
and characters
       R         extendR from subgroups to all of  R Y since TR is divisible. Translation invariance
gives ey (x) dµ(x) = ey (x0 x) dµ(x) = x0 (y) ey dµ, so ey dµ = 0. Completeness: span{ey }
is a unital ∗-subalgebra of C(Yb ) separating points (distinct characters of Y differ at some y),
hence norm-dense by Stone–Weierstrass [SF]; and C(Yb ) is dense in L2 [SF].
   (ii) Let T commute with every Mey and put F0 := T 1 ∈ L2 . For every f ∈ T := span{ey }
we get T f = T Mf 1 = Mf T 1 = f F0 , hence
                      Z                                  Z
                            2     2            2       2
                        |f | |F0 | dµ = ∥T f ∥2 ≤ ∥T ∥     |f |2 dµ     (f ∈ T ).

Fix ε > 0 and let E := {|F0 | ≥ ∥T ∥ + ε}. Choose fn ∈ T with fn → 1E in L2 (µ) (density, by
(i)) and, passing to a subsequence, µ-a.e. By Fatou’s lemma,
                   Z                      Z                         Z
(∥T ∥+ε) µ(E) ≤ 1E |F0 | dµ ≤ lim inf |fn | |F0 | dµ ≤ ∥T ∥ lim inf |fn |2 dµ = ∥T ∥2 µ(E),
         2                  2                  2    2        2
                                       n                               n

forcing µ(E) = 0. Hence F0 ∈ L∞ with ∥F0 ∥∞ ≤ ∥T ∥, and T = MF0 on the L2 -dense
subspace T , so T = MF0 . Conversely every MF (F ∈ L∞ ) commutes with the Mey . This
                                                                        ′
proves the commutant statement. Consequently {Mey }′′ = {Mey }′ = {MF : F ∈ L∞ }′ =
{MF : F ∈ L∞ }, where the last equality holds because {MF } is abelian (so {MF } ⊆ {MF }′ )
while any T ∈ {MF }′ commutes in particular with the Mey and hence lies in {MF } by the
commutant statement. Thus L∞ (Yb ) equals its own commutant: it is maximal abelian, and
{Mey }′′ = L∞ (Yb ).
   (iii) W is well defined and isometric on span{ey } since ⟨Sy Ω, Sy′ Ω⟩ = ⟨Sy−y′ Ω, Ω⟩ = δy,y′ =
⟨ey , ey′ ⟩, and extends to a unitary onto K by (i) and the cyclicity hypothesis; uniqueness is
clear. For y, y ′ : W Mey W ∗ Sy′ Ω = W Mey ey′ = W ey+y′ = Sy+y′ Ω = Sy Sy′ Ω; the vectors
Sy′ Ω are total, so W Mey W ∗ = Sy . Hence Ad W (a normal ∗-isomorphism B(L2 ) → B(K))
                      NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                  7


carries {Mey }′′ = L∞ (Yb ) onto {Sy }′′ R= S, which is therefore a masa; and ⟨J(F
                                                                               b )Ω, Ω⟩ =
         ∗
⟨W MF W W 1, W 1⟩ = ⟨F · 1, 1⟩L2 (µ) = F dµ.                                            □

Lemma 2.4 (uniqueness of normal extensions). Let N be a von Neumann algebra and
ϕ1 , ϕ2 : L∞ (Yb ) → N unital normal ∗-homomorphisms with ϕ1 (ey ) = ϕ2 (ey ) for all y ∈ Y .
Then ϕ1 = ϕ2 .
Proof. They agree on span{ey }, hence on its norm closure C(Yb ) (∗-homomorphisms are norm-
continuous). C(Yb ) is a σ-weakly dense C∗ -subalgebra of L∞ (Yb ) (its weak closure is a von
Neumann algebra containing all Mey , hence equal to L∞ by Lemma 2.3(ii)), so by Kaplansky’s
density theorem [SF] the unit ball of C(Yb ) is σ-strongly dense in that of L∞ (Yb ); normal
∗-homomorphisms are σ-weakly continuous on bounded sets [SF].                               □

Lemma 2.5 (normality criterion). Let ϕ : M → N be a unital ∗-homomorphism between
abelian von Neumann algebras, and let ρ be a faithful normal state on N such that ρ ◦ ϕ is
normal on M . Then ϕ is normal.
Proof. Let (xi ) be a bounded increasing net of self-adjoint elements of M with supremum x.
Then (ϕ(xi )) is increasing with ϕ(xi ) ≤ ϕ(x) (ϕ preserves order), so it has a supremum y ≤ ϕ(x)
in N , and ϕ(xi ) → y σ-strongly. Then ρ(y) = limi ρ(ϕ(xi )) = limi (ρ ◦ ϕ)(xi ) = (ρ ◦ ϕ)(x) =
ρ(ϕ(x)) by normality of ρ and of ρ ◦ ϕ. Since ϕ(x) − y ≥ 0 and ρ(ϕ(x) − y) = 0 with ρ faithful,
y = ϕ(x). A ∗-homomorphism preserving suprema of bounded increasing nets is normal.            □
2.5 Group von Neumann algebras. For a countable discrete group G, let λ, ρ denote the
left and right regular representations on ℓ2 G (λg δh = δgh , ρg δh = δhg−1 ); they commute. Set
L(G) := {λg : g ∈ G}′′ and τ (x) := ⟨xδe , δe ⟩.
Definition (II1 factor). In this paper, a II1 factor is an infinite-dimensional von Neumann
algebra with trivial center which possesses a faithful normal tracial state. (This is equivalent
to the standard classification-theoretic definition; only the stated properties are ever used, and
[CJ] concerns exactly such algebras.)
Lemma 2.6. (i) τ is a faithful normal tracial state on L(G), and δe is cyclic and separating
for L(G). (ii) If G is infinite and ICC, then L(G) is a II1 factor.
Proof. (i) Normality and τ (1) = 1 are clear; δe is cyclic since λg δe = δg . For x ∈ L(G) put
x̂ := xδe ∈ ℓ2 G. Since x commutes with all ρg , we get xδg = xρg−1 δe = ρg−1 x̂, i.e.
                                 (xδg )(h) = x̂(hg −1 )     (g, h ∈ G).                             (2.2)
If τ (x∗ x) = ∥x̂∥2 = 0 then xδg = 0 for all g by (2.2), so x = 0: τ is faithful and δe separating.
Traciality: for x, y ∈ L(G), using (2.2) and x   c∗ (h) = ⟨δe , xδh ⟩ = (xδh )(e) = x̂(h−1 ),
                                                X                 X
                      τ (xy) = ⟨yδe , x∗ δe ⟩ =          c∗ (h) =
                                                   ŷ(h) x             ŷ(h) x̂(h−1 ),
                                                h                    h

which is symmetric under x ↔ y (substitute h 7→              h−1 ;  the sum converges absolutely by
Cauchy–Schwarz). Hence τ (xy) = τ (yx). (ii) Let z ∈ L(G) be central and c := ẑ. By
(2.2), (zλg δe )(k) = (zδg )(k) = c(kg −1 ), while (λg zδe )(k) = ẑ(g −1 k) = c(g −1 k); centrality gives
c(kg −1 ) = c(g −1 k) for all g, k ∈ G. Substituting k = gh yields c(ghg −1 ) = c(h) for all g, h:
c is constant on conjugacy classes. As c ∈ ℓ2 , it vanishes on all infinite classes; since G is
ICC, c = c(e)δe , so zδe = c(e)δe , and z = c(e)1 because δe is separating. Thus L(G) is a
factor with a faithful normal trace; it is infinite-dimensional: the vectors δg = λg δe , g ∈ G, are
8                   NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

orthonormal, and a finite-dimensional algebra has finite-dimensional cyclic modules, whereas
L(G)δe ⊇ span{δg } is infinite-dimensional. By the definition above, L(G) is a II1 factor. □

Lemma 2.7 (recognition principle). Let G0 be a countable discrete group, M := L(G0 )
on ℓ2 (G0 ) with trace τ and trace vector δe . Let Λ be a countable group and π : Λ → U(M )
a homomorphism with τ (π(h)) = δh,e for all h ∈ Λ and π(Λ)′′ = M . Then there is a trace-
preserving ∗-isomorphism L(Λ) → M with λh 7→ π(h) for all h ∈ Λ.
Proof. Define W : ℓ2 (Λ) → ℓ2 (G0 ) on the canonical basis by W δh := π(h)δe ; it is isometric
because ⟨π(h)δe , π(k)δe ⟩ = τ (π(k)∗ π(h)) = τ (π(k −1 h)) = δh,k . Let A0 := span π(Λ), a unital
∗-subalgebra of M (π(h)∗ = π(h−1 )) with A′′0 = M . The closure of ran W is A0 δe , an A0 -
invariant and A∗0 -invariant subspace, so the projection p onto it lies in A′0 . For m ∈ M = A′′0 :
mδe = mpδe = pmδe ∈ A0 δe . Since M δe ⊇ {δg : g ∈ G0 } is total, p = 1 and W is unitary. On
basis vectors, W λh W ∗ π(k)δe = W δhk = π(h)π(k)δe , so W λh W ∗ = π(h) by totality. Hence
Ad W maps L(Λ) = {λh }′′ onto π(Λ)′′ = M , and it preserves the traces because W δe = δe :
τ (W xW ∗ ) = ⟨xW ∗ δe , W ∗ δe ⟩ = ⟨xδe , δe ⟩ for x ∈ L(Λ).                                   □

                    3. The field k∞ , the character ψ, and duality
   Let R := Fq [t] and let k∞ := Fq ((t−1 )) P
                                             be the field of formal Laurent series in t−1 : every
x ∈ k∞ ∖ {0} has a unique expansion x = i≤N xi ti with xi ∈ Fq , xN ̸= 0. Let O := Fq [[t−1 ]]
(those x with xi = 0 for i > 0) and m := t−1 O. With the valuation topology, k∞ is a nondiscrete
locally compact second countable totally disconnected field of characteristic 2 (a local field):
the sets
                       BN := tN O = {x : xi = 0 for i > N }       (N ∈ Z)
are compact open additive subgroups which form a neighborhood basis of 0 as N → −∞ and
exhaust k∞ as N → +∞. Each coefficient functional x 7→ xi ∈ Fq is locally constant (constant
on cosets of Bi−1 ), hence continuous. Haar measure on (k∞ , +) is normalized by Haar(m) = 1,
and on all finite powers k∞m we use the corresponding product measure, so that Haar(mm ) = 1.

   Splitting. As topological groups,
                                          k∞ = R ⊕ m :
every x is uniquely the sum of its polynomial part i≥0 xi ti ∈ R and its tail i≤−1 xi ti ∈ m.
                                                      P                      P

Here R is discrete (R ∩ m = {0} with m open, so 0 is isolated in R) and therefore closed in
k∞ (Lemma 2.2(iii) applied to the subgroup R), while m is compact open. In particular m is a
compact exact fundamental domain for R: each coset x + R meets m in exactly one point.
  The character. Define the nontrivial character ψ0 : Fq → {±1}, ψ0 (a) := (−1)Tr(a) ,
Tr := TrFq /F2 . Since the trace commutes with the Frobenius a 7→ a2 and takes values in F2
(where squaring is the identity), Tr(a2 ) = Tr(a), i.e.
                                  ψ0 (a2 ) = ψ0 (a)    (a ∈ Fq ).                             (3.1)
Moreover the F2 -bilinear form (a, b) 7→ Tr(ab) on Fq is nondegenerate: if b ̸= 0 then a 7→ Tr(ab)
is a nonzero functional (as a runs over Fq , ab runs over Fq , and Tr ̸≡ 0 because the polynomial
Ps−1 2j
   j=0 X   has at most 2s−1 < q roots). Define res(x) := x−1 and
                                  ψ := ψ0 ◦ res : k∞ → {±1},
a continuous additive character (res is additive, continuous), trivial on R and on B−2 = t−2 O.
As k∞ has exponent 2, every character of every subquotient of every k∞     m is {±1}-valued; in

particular ψ −1 = ψ = ψ, and we never need to track inversion of values of ψ.
                     NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                 9

Lemma 3.1 (self-duality). (i) R⊥ := {x ∈ k∞ : ψ(xy) = 1 ∀y ∈ R} = R. (ii) y 7→ ψ(y ·) is
injective as a map from k∞ to characters of k∞ ; moreover for y ∈ R∖{0} the character ψ(y ·)|m
is nontrivial, and for y ∈ m ∖ {0} the character ψ(y ·)|R is nontrivial. (iii) Every continuous
character of k∞ is ψ(y ·) for a unique y ∈ k∞ ; every continuous character of m is ψ(n ·)|m for
a unique n ∈ R; every character of the discrete group R is ψ(m ·)|R for a unique m ∈ m.

Proof. (i) Suppose ψ(xy) = 1 for all y ∈ R. For j ≥ 0 and a ∈ Fq , taking y = atj : 1 =
ψ(atj x) = ψ0 (a x−j−1 ), so by nondegeneracy of the trace form x−j−1 = 0 for all j ≥ 0, i.e.
x ∈ R. Conversely if xP    ∈ R then xR ⊆ R ⊆ ker ψ.
   (ii) Let y ̸= 0, y = i≤N yi ti with yN ̸= 0. Take z := at−N −1 with a ∈ Fq chosen so that
Tr(ayN ) ̸= 0; then res(yz) = ayN and ψ(yz) = ψ0 (ayN ) ̸= 1. If y ∈ R ∖ {0} then N ≥ 0,
so z ∈ m; if y ∈ m ∖ {0} then N ≤ −1, so z ∈ R. Injectivity on k∞ : if ψ(y ·) = ψ(y ′ ·) then
ψ((y − y ′ ) ·) ≡ 1, forcing y = y ′ by the above.
   (iii) Characters of m. Let χ be a continuous character of the compact group m. Since T has
no small subgroups and the subgroups B−k−1 (k ≥ 1) form a neighborhood basis of 0 in m,
χ(B−k−1 ) is a subgroup of T contained in a small neighborhood of 1 for large k, hence trivial:
χ factors through the finite group m/B−k−1 , an Fq -space with basis the classes of t−1 , . . . , t−k ,
of order q k . Let Fk := k−1         i
                           L
                             i=0 Fq t ⊂ R and consider the pairing
                                                                        k−1
                                                                       X                 
               Fk × m/B−k−1 → {±1},           (n, m̄) 7→ ψ(nm) = ψ0            ni m−1−i
                                                                         i=0

(well defined: nB−k−1 ⊆ B−2 for n ∈ Fk ). By (ii) it is nondegenerate in each variable (for
m̄ ̸= 0, some m−1−i ̸= 0 with 0 ≤ i ≤ k − 1, and n = ati detects it; symmetrically for
n ̸= 0 use a suitable m̄). Hence n 7→ ψ(n ·) is an injective map Fk → m/B        \  −k−1 between
finite groups of equal order: for a finite group W of exponent 2 — an F2 -vector space of
some finite dimension δ — every character is {±1}-valued, so W        c = HomF (W, F2 ) is the
                                                                                  2
F2 -linear dual space, of cardinality 2 = |W |; here |Fk | = |m/B−k−1 | = q k , and both are
                                       δ

F2 -vector spaces. An injective map between finite sets of equal cardinality is bijective; so
χ = ψ(n ·)|m for a (by (ii) unique in R) n ∈ Fk . Characters of R. R is discrete, so any
homomorphism χ : R → T is a character, determined by its restrictions to the slices Fq ti
(i ≥ 0). By nondegeneracy of the trace form, for each i there is a unique m−1−i ∈ Fq with
χ(ati ) = ψ0 (am−1−i ) for
                       P all a ∈ Fq−1−i
                                     (the map b 7→ ψ0 ( · b) is a bijection from Fq onto F
                                                                                         cq , both
of order q). Set m := i≥0 m−1−i t                           i                        i
                                         ∈ m; then ψ(mat ) = ψ0 (am−1−i ) = χ(at ) for all i, a,
so χ = ψ(m ·)|R ; uniqueness by (ii). Characters of k∞ . Given a continuous character χ of k∞ ,
choose m0 ∈ m with χ|R = ψ(m0 ·)|R and n0 ∈ R with χ|m = ψ(n0 ·)|m . Then ψ((m0 + n0 ) ·)
agrees with χ on R (as ψ(n0 R) = 1 by (i)) and on m (as m0 m ⊆ B−2 ⊆ ker ψ), hence on
R + m = k∞ ; uniqueness by (ii).                                                                □
                                           2g                                              g
  The symplectic space. Let V∞ := k∞          , elements written v = (v1 , v2 ) with vi ∈ k∞ ,
equipped with
                                                                 g
                                                                 X
                 ω(v, w) := ⟨v1 , w2 ⟩ + ⟨v2 , w1 ⟩,   ⟨x, y⟩ :=   xj yj .
                                                                      j=1

In characteristic 2, ω is alternating (ω(v, v) = 2⟨v1 , v2 ⟩ = 0) and symmetric (ω(v, w) = ω(w, v));
it is nondegenerate. Put
      S := R2g ⊂ V∞ ,       H := Sp2g (R) := {γ ∈ GL2g (R) : ω(γv, γw) = ω(v, w) ∀v, w};
10                     NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

H preserves S. In matrix terms, with J := I0 I0 the Gram matrix of ω: γ ∈ Sp2g iff γ T Jγ = J;
                                                  

in particular γ −1 = J −1 γ T J is again a matrix over the same ring, and Sp2g (R) = Sp2g (k∞ ) ∩
GL2g (R).
Lemma 3.2. (i) S ⊥ := {x ∈ V∞ : ψ(ω(x, n)) = 1 ∀n ∈ S} = S. (ii) Every continuous char-
acter of V∞ equals ψ(ω(x, ·)) for a unique x ∈ V∞ . (iii) The map V∞ → S,       b x 7→ ψ(ω(x, ·))|S ,
is surjective with kernel S.
Proof. For x = (x1 , x2 ) and n = (n1 , n2 ), ψ(ω(x, n)) = gj=1 ψ (x1 )j (n2 )j ψ (x2 )j (n1 )j . (ii)
                                                            Q                                  
                                    2g
A continuous character of V∞ = k∞      restricts to a continuous character of each coordinate copy
of k∞ and is the product of these restrictions; by Lemma 3.1(iii) it is v 7→ ψ ⟨y1 , v1 ⟩ + ⟨y2 , v2 ⟩
                      g
for unique y1 , y2 ∈ k∞ , and this equals ψ(ω(x, ·)) for the unique x := (y2 , y1 ). (iii) A character
          2g
of S = R is likewise a product of characters of the coordinate copies of R, hence by Lemma
3.1(iii) of the form n 7→ ψ(⟨m′ , n1 ⟩ + ⟨m, n2 ⟩) with m, m′ ∈ mg , which is ψ(ω(x, ·))|S for
x = (m, m′ ): the map is surjective. Its kernel is S ⊥ by definition, and coordinatewise application
of Lemma 3.1(i) gives S ⊥ = S, proving (i) and (iii).                                                □

Lemma 3.3 (linear maps and Haar measure). For a ∈ GLn (k∞ ) and Borel E ⊆ k∞                     n ,
                                                                              ×
Haar(aE) = | det a| Haar(E), where |d| := Haar(dO)/ Haar(O) for d ∈ k∞ is a multiplicative
function with |t| = q and |u| = 1 for u ∈ O× . In particular every l ∈ Sp2g (k∞ ) has det l = 1 and
                               2g                                    4g    2g     2g
preserves Haar measure on k∞      , and the diagonal action of l on k∞  = k∞  ⊕ k∞   also preserves
Haar measure.
Proof. For fixed a ∈ GLn (k∞ ), E 7→ Haar(aE) is a nonzero translation-invariant Radon
measure, hence = c(a) Haar for a unique c(a) > 0 [SF], and c is multiplicative. We eval-
uate c on generators of GLn (k∞ ): Elementary matrices 1 + rEij (i ̸= j): by Fubini, in-
tegrating first over the i-th coordinate, the shear xi 7→ xi + rxj is a translation
                                                                                 Q         for each
fixed xj , so c = 1. Diagonal matrices diag(d1 , . . . , dn ): by Fubini, c = i c1 (di ), where
c1 (d) := Haark∞ (dE)/ Haark∞ (E) (independent of E); taking E = O gives c1 (d) = |d|, and
multiplicativity of c1 gives multiplicativity of | · |. For a unit u ∈ O× : multiplication by u is
an automorphism of the compact group O, hence preserves its (restricted) Haar measure, so
|u| = 1. And |t−1 | = Haar(t−1 O)/ Haar(O) = [O : m]−1 = q −1 (the compact group O is the
disjoint union of q translates of m), so |t| = q. Generation: every a ∈ GLn (k∞ ) is a product of
elementary and diagonal matrices, by Gaussian elimination over a field: some entry of the first
column is nonzero, so adding a multiple of one row to another makes the (1, 1) entry nonzero;
further elementary row and column operations clear the rest of the first row and column; induct
on n. (Row operations are left multiplication by elementary matrices, column operations right
multiplication.) Since c and | det(·)| are both multiplicative and agree on elementary (det = 1,
c = 1) and diagonal matrices, c(a) = | det a| for all a. Symplectic determinant: γ T Jγ = J
gives (det γ)2 det J = det J and det J ̸= 0, so (det γ)2 = 1; in characteristic 2, x2 = 1 implies
                                                                                  4g
(x + 1)2 = 0, i.e. x = 1. Hence det l = 1, c(l) = 1; the diagonal action on k∞        is l ⊕ l with
det(l ⊕ l) = 1.                                                                                  □

                    4. The Weyl system over k∞ and the lattice masa
                  g
     On H := L2 (k∞ ) define, for v = (v1 , v2 ) ∈ V∞ ,
            uv := Tv1 Mv2 ,     (Tv1 ξ)(x) := ξ(x + v1 ),      (Mv2 ξ)(x) := ψ(⟨x, v2 ⟩) ξ(x),
so that
                                 (uv ξ)(x) = ψ(⟨x + v1 , v2 ⟩) ξ(x + v1 ).                       (4.1)
                       NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                               11

Lemma 4.1. Set β(v, w) := ψ(⟨v2 , w1 ⟩) and q0 (v) := ⟨v1 , v2 ⟩. For all v, w, x ∈ V∞ : (i)
uv uw = β(v, w) uv+w ; β is a continuous {±1}-valued bicharacter on V∞ × V∞ (in particular
a multiplier: the 2-cocycle identity β(v, w)β(v + w, x) = β(w, x)β(v, w + x) holds, both sides
being ψ(⟨v2 , w1 ⟩ + ⟨v2 , x1 ⟩ + ⟨w2 , x1 ⟩)), and β(v, w)β(w, v) = ψ(ω(v, w)); (ii) uv is unitary with
u∗v = u−1                                     ∗
       v = ψ(q0 (v)) uv ; (iii) ux uv ux = ψ(ω(x, v)) uv ; (iv) β ≡ 1 on S × S; hence n 7→ un
(n ∈ S) is a unitary representation of the group S; (v) v 7→ uv is strongly continuous.
Proof. (i) By (4.1),
                (uv uw ξ)(x) = ψ(⟨x + v1 , v2 ⟩) ψ(⟨x + v1 + w1 , w2 ⟩) ξ(x + v1 + w1 ),
while (uv+w ξ)(x) = ψ(⟨x + v1 + w1 , v2 + w2 ⟩) ξ(x + v1 + w1 ). The ratio of the phases is
                                                                
        ψ ⟨x+v1 , v2 ⟩ + ⟨x+v1 +w1 , w2 ⟩ + ⟨x+v1 +w1 , v2 +w2 ⟩ = ψ(⟨w1 , v2 ⟩) = β(v, w)
(all signs may be taken + in characteristic 2, and ψ = ψ −1 ). The remaining claims in (i) are
immediate from the formula for β and bilinearity of ⟨·, ·⟩; for the symmetrizer, β(v, w)β(w, v) =
ψ(⟨v2 , w1 ⟩ + ⟨w2 , v1 ⟩) = ψ(ω(v, w)). (ii) uv is a product of two unitaries. By (i), uv uv =
β(v, v)u2v = ψ(⟨v2 , v1 ⟩)u0 = ψ(q0 (v)) · 1 (as 2v = 0), so u−1
                                                              v = ψ(q0 (v))uv . (iii) By (i) and (ii):
ux uv u∗x = ψ(q0 (x)) ux uv ux = ψ(q0 (x)) β(x, v) β(x+v, x) u2x+v = ψ ⟨x1 , x2 ⟩+⟨x2 , v1 ⟩+⟨x2 +v2 , x1 ⟩ uv ,
                                                                                                           

and the exponent is ⟨x2 , v1 ⟩ + ⟨v2 , x1 ⟩ = ω(x, v). (iv) For n, m ∈ S, ⟨n2 , m1 ⟩ ∈ R ⊆ ker ψ. (v)
Since the uv are unitaries and (v, ξ) 7→ uv ξ is linear in ξ, it suffices to check ∥uv ξ − ξ∥ → 0
as v → 0, for ξ in the subspace of locally constant compactly supported functions — which is
               g
dense in L2 (k∞  ): simple functions are dense, every Borel set of finite measure is approximated
                                                                                                   g
in measure by finite unions of balls (regularity of Haar measure [SF], and the balls x + BN
generate the topology and form a ring of sets up to finite disjoint unions), and indicators of balls
                                                                                             g
are locally constant with compact support. Such ξ is invariant under translations by B−N         and
                 g                          2g         ′
supported in BN for some N ; for v ∈ B−N ′ with N ≥ N large, Tv1 ξ = ξ and |ψ(⟨x, v2 ⟩)−1| = 0
          g           g
for x ∈ BN  , v2 ∈ B−N  −2 (then ⟨x, v2 ⟩ ∈ B−2 ⊆ ker ψ); so uv ξ = ξ for v small.                 □
   Let ξ0 := 1mg ∈ H, a unit vector (Haar(mg ) = 1).
   We record a consequence of Lemma 3.1(iii) for use in the next proof. The map mg → R   cg , m 7→
ψ(⟨m, ·⟩)|Rg , is a group isomorphism: by the R-clause
                                              b        of Lemma 3.1(iii), applied coordinatewise,
                         g
every character of R equals ψ(⟨m, ·⟩)|R for a unique m ∈ mg . It is continuous: for fixed
                                           g

n ∈ Rg , the value ψ(⟨m, n⟩) depends only on finitely many coefficients of m, each of which varies
continuously (indeed locally constantly) with m; so the map into the dual, with its topology of
pointwise convergence, is continuous. A continuous bijective homomorphism from a compact
group onto a Hausdorff topological group is a homeomorphism (continuous bijections from
compact spaces to Hausdorff spaces are closed maps). Hence it transports the Haar probability
                                                                                              g
of mg to that of R   cg ; and the Haar probability of the compact open subgroup mg ⊂ k∞          is
the restriction of the ambient Haar measure (that restriction is a translation-invariant Borel
probability on mg under our normalization, so it is the Haar probability; uniqueness [SF]).
Consequently, by Lemma 2.3(i) applied to Y = Rg , the characters y 7→ ψ(⟨y, n2 ⟩) of mg ,
indexed by n2 ∈ Rg , form an orthonormal basis of L2 (mg ) (with respect to the restricted Haar
measure).
Lemma 4.2 (lattice masa). (i) ⟨un ξ0 , ξ0 ⟩ = δn,0 for all n ∈ S. (ii) ξ0 is cyclic for A :=
{un : n ∈ S}′′ , i.e. span{un ξ0 : n ∈ S} = H. (iii) Consequently (Lemma 2.3 with Y = S)
there is a unique unitary WS : L2 (S) b → H with WS en = un ξ0 ; it satisfies WS Men W ∗ = un ; the
                                                                                      S
algebra A is a masa in B(H); and       J  := Ad W  : L ∞ (S)
                                                          b → A is a normal isomorphism with
                                     R  S        S
JS (en ) = un and ⟨JS (F )ξ0 , ξ0 ⟩ = F dµSb.
12                   NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

                          g
Proof. Use the splitting k∞  = Rg ⊕ mg (§3). For n = (n1 , n2 ) ∈ S and x = p + y with p ∈ Rg ,
      g
y ∈ m , formula (4.1) gives
                                                                                          
        (un ξ)(p + y) = ψ(⟨p + y + n1 , n2 ⟩) ξ (p + n1 ) + y = ψ(⟨y, n2 ⟩) ξ (p + n1 ) + y ,
since ⟨p + n1 , n2 ⟩ ∈ R ⊆ ker ψ. (i) ξ0 is supported on the coset 0 + mg , and un ξ0 on n1 + mg
(set ξ = ξ0 above:     nonzero only if p + n1 = 0). So ⟨un ξ0 , ξ0 ⟩ = 0 unless n1 = 0, in which
case it equals mg ψ(⟨y, n2 ⟩) dy. The functions y 7→ ψ(⟨y, n2 ⟩) on mg , for n2 ∈ Rg , form
                 R

an orthonormal basis of L2 (mg ) (paragraph preceding this lemma); orthogonality against the
constant function 1 (the member with n2 = 0) shows that for n2 ̸= 0 the integral vanishes,
while for n2 = 0 it is 1. (ii) By the displayed formula, un ξ0 = 1n1 +mg · ψ(⟨· − n1 , n2 ⟩), i.e. the
function supported on n1 + mg whose restriction, translated to mg , is the character ψ(⟨·, n2 ⟩).
For fixed n1 , these characters (n2 ∈ Rg ) have dense span in L2 (mg ) (they are an orthonormal
basis; paragraph preceding     Lemma 4.2). Hence span{un ξ0 } contains L2 (n1 + mg ) for every
n1 ∈ R , and H = n1 ∈Rg L2 (n1 + mg ). (iii) Lemma 2.3.
       g
                      L
                                                                                                    □

Lemma 4.3 (irreducibility). {uv : v ∈ V∞ }′ = C1; consequently {uv : v ∈ V∞ }′′ = B(H).
Proof. Let T commute with all uv . In particular T ∈ A′ = A (Lemma 4.2(iii)), say T = JS (F ),
F ∈ L∞ (S).b Fix v ∈ V∞ and let χv := ψ(ω(v, ·))|S ∈ S. b By Lemma 4.1(iii), Ad uv maps un 7→
                                       ∞
χv (n) un and preserves A. Let τv : L (S)         ∞
                                          b → L (S)  b be the translation (τv F )(x) := F (χ−1 x),
                                                                                            v
                                          −1
an automorphism with τv (en ) = χv (n) en ; it is normal by Lemma 2.5, being a unital ∗-
homomorphism      of an abelian von Neumann algebra which preserves the faithful normal state
  · dµ (translation invariance of Haar). Then JS−1 ◦Ad uv ◦JS and τv−1 are normal automorphisms
R

of L∞ (S)b agreeing on every en (both send en 7→ χv (n)en ), hence equal (Lemma 2.4). Since T
commutes with uv , F is τv−1 -invariant, i.e. invariant under translation by χv ; and by Lemma
3.2(iii) the characters χv , v ∈ V∞ , exhaust S. b Thus F ∈ L∞ (S)   b is invariant under every
                                                 R
translation of the compact group S: with c := F dµ, Fubini gives
                                    b
Z                      Z Z                                     ZZ
                                         −1
                                                                    F (x)−F (s−1 x) dµ(x) dµ(s) = 0,
                                              
   |F (x)−c| dµ(x) =          F (x)−F (s x) dµ(s) dµ(x) ≤

because for each fixed s the inner integral vanishes. Hence F = c a.e. and T = c1. The
consequence is the bicommutant theorem [SF].                                        □

Corollary 4.4 (Stone–von Neumann datum). The multiplier β on the second countable
locally compact abelian group V∞ has symmetrizer v 7→ β(v, ·)β(·, v) = ψ(ω(v, ·)), which is a
topological isomorphism V∞ → Vc ∞ . Hence [SvN] applies: any two irreducible strongly contin-
uous β-representations of V∞ are unitarily equivalent. The Weyl system v 7→ uv is one such
(β-representation by Lemma 4.1(i), strongly continuous by 4.1(v), irreducible by Lemma 4.3).
Proof. The symmetrizer is a group homomorphism into Vc ∞ (bilinearity of ω) and is bijective
by Lemma 3.2(ii). Continuity into the compact-open topology: for a compact C ⊂ V∞ we
             2g                            2g
have C ⊆ BN     for some N , and for v ∈ B−N  −2 we get ω(v, w) ∈ B−2 for all w ∈ C, so
ψ(ω(v, ·)) ≡ 1 on C: the symmetrizer is continuous at 0, hence (being a homomorphism)
everywhere. Openness: we claim that for every M ∈ Z,
         σ B 2g = Ann B 2g
                                  
              −M                 := χ ∈ Vc
                              M −2        ∞ : χ| 2g  ≡1 ,
                                                      BM −2
                                                                σ(v) := ψ(ω(v, ·)).
              2g          2g
“⊆”: for v ∈ B−M and w ∈ BM  −2 , every product of a coordinate of v with a coordinate of w lies
in B−M BM −2 ⊆ B−2 ⊆ ker ψ, so σ(v)(w) = 1. “⊇”: by Lemma 3.2(ii) every element of Vc        ∞ is
some σ(v); if a coordinate v∗ of v does not lie in B−M , its leading term has degree N ′ ≥ −M +1,
                       NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                          13

                                                                          ′
and the vector w with the dual coordinate equal to z := at−N −1 and all other coordinates 0 lies
     2g            ′
in BM   −2 (as −N − 1 ≤ M − 2) and satisfies σ(v)(w) = ψ(v∗ z) = ψ0 (a (v∗ )N ′ ) ̸= 1 for suitable
                        2g
a — so σ(v) ∈   / Ann(BM   −2 ). Finally, since every character of the exponent-2 group V∞ is
{±1}-valued, the compact-open basic neighborhood {χ : |χ(w) − 1| < 1 ∀w ∈ C} of the trivial
                                                   2g                  2g                 2g
character equals Ann(C), and Ann(C) ⊇ Ann(BM          ) whenever C ⊆ BM   ; thus {Ann(BM     )}M ∈Z
is a neighborhood basis of the trivial character. So σ maps a neighborhood basis of 0 onto a
neighborhood basis of 1, hence is open. Being a continuous open bijective homomorphism, σ
is a topological isomorphism.                                                                     □

     5. Second-degree characters, normalized intertwiners, and the class κ

5.1 Second-degree characters. Definition. Let U be an abelian topological group of expo-
nent 2 and b : U × U → {±1} a continuous symmetric bicharacter. A second-degree character
for b is a continuous map h : U → T with
                               h(x + y) = h(x) h(y) b(x, y)           (x, y ∈ U ).
Setting x = y = 0 gives h(0) = 1; setting y = x gives 1 = h(0) = h(x)2 b(x, x), so h(x)2 =
b(x, x)−1 ∈ {±1} and h takes values in µ4 = {±1, ±i}.
Lemma 5.1 (existence and extension). Let U = k∞       m (any m ≥ 1), let b be a continuous

symmetric {±1}-valued bicharacter on U , let B ≤ U be a subgroup, and let hB : B → µ4 be a
second-degree character for b|B×B (if B = 0, take hB = 1). Assume there is a compact open
subgroup C0 ≤ U with b|C0 ×C0 ≡ 1 and B ∩ C0 = 0. Then there exists a second-degree character
h : U → µ4 for b with h|B = hB .
Proof. First define h on the open subgroup U0 := B ⊕ C0 by
                             h(x + c) := hB (x) b(x, c)          (x ∈ B, c ∈ C0 );
this is well defined because the sum is direct. It satisfies the second-degree identity on U0 : for
x, x′ ∈ B, c, c′ ∈ C0 ,
h (x+c)+(x′ +c′ ) = hB (x+x′ ) b(x+x′ , c+c′ ) = hB (x)hB (x′ )b(x, x′ ) b(x, c)b(x, c′ )b(x′ , c)b(x′ , c′ ),
                   

while
 h(x + c) h(x′ + c′ ) b(x + c, x′ + c′ ) = hB (x)b(x, c) hB (x′ )b(x′ , c′ ) b(x, x′ )b(x, c′ )b(c, x′ )b(c, c′ );
the two agree because b is symmetric (b(x′ , c) = b(c, x′ )) and b(c, c′ ) = 1. It is continuous:
near x0 + c0 , every point of U0 is x0 + (c0 + c) with c ∈ C0 small, and h(x0 + c0 + c) =
h(x0 + c0 ) b(x0 , c) → h(x0 + c0 ) as c → 0 (b continuous, b(x0 , 0) = 1).
   The quotient U/U0 is discrete (as U0 is open) and σ-compact (U is), hence countable; since
U has exponent 2, U/U0 is an F2 -vector space, so it has a countable basis; lift basis vectors to
u1 , u2 , · · · ∈ U and set Un := Un−1
                                    S ⊕ {0, un } (the sums are direct by linear independence of
the basis mod U0 ), so that U = n≥0 Un with each Un open. Inductively extend h from Un−1
to Un : choose ϵn ∈ µ4 with ϵ2n = b(un , un )−1 (possible: b(un , un ) ∈ {±1} and every element of
{±1} has a square root in µ4 ), and define
                     h(y + δun ) := h(y) ϵδn b(y, un )δ         (y ∈ Un−1 , δ ∈ {0, 1}).
The second-degree identity on Un : take y + δun , y ′ + δ ′ un with y, y ′ ∈ Un−1 , δ, δ ′ ∈ {0, 1}. If
δ ′ = 0 (or symmetrically δ = 0):
      h (y + δun ) + y ′ = h(y + y ′ )ϵδn b(y + y ′ , un )δ = h(y)h(y ′ )b(y, y ′ )ϵδn b(y, un )δ b(y ′ , un )δ ,
                        
14                      NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

and h(y + δun )h(y ′ )b(y + δun , y ′ ) = h(y)ϵδn b(y, un )δ h(y ′ )b(y, y ′ )b(un , y ′ )δ : equal, by symmetry
of b. If δ = δ ′ = 1: the sum is (y + y ′ ) + 2un = y + y ′ ∈ Un−1 , and

     h(y + y ′ ) vs. h(y + un )h(y ′ + un )b(y + un , y ′ + un )
                                  = h(y)h(y ′ )ϵ2n b(y, un )b(y ′ , un ) · b(y, y ′ )b(y, un )b(un , y ′ )b(un , un ).
Using b(·, ·)2 = 1 and ϵ2n b(un , un ) = 1, the right side reduces to h(y)h(y ′ )b(y, y ′ ) = h(y + y ′ ).
So the identity holds on Un . Continuity on Un holds because Un = Un−1 ⊔ (un + Un−1 ) is a
disjoint union of open sets on each of which h is continuous (on the second piece, h(un + y) =
h(y)ϵn b(y, un ), continuous in y). The union h : U → µ4 is a second-degree character (any pair
x, y lies in some Un ) extending hB .                                                                  □

5.2 Intertwining pairs. For γ ∈ Sp2g (k∞ ) define
                             bγ (v, w) := β(γv, γw) β(v, w)             (v, w ∈ V∞ ),
a continuous {±1}-valued bicharacter. It is symmetric: using Lemma 4.1(i) twice,
                   bγ (v, w) bγ (w, v) = ψ(ω(γv, γw)) ψ(ω(v, w)) = ψ(ω(v, w))2 = 1,
and since all values are ±1 this says bγ (v, w) = bγ (w, v).
Definition. An intertwining pair for γ is a pair (c, V ) where c : V∞ → T is continuous, V is a
unitary of H, and
                             V uv V ∗ = c(v) uγv       (v ∈ V∞ ).                         (5.1)

Lemma 5.2 (existence). For every γ ∈ Sp2g (k∞ ) there exists an intertwining pair for γ.

Proof. Since bγ is continuous with bγ (0, 0) = 1 and {1} is open in {±1}, there is a neighborhood
                                                                                         2g
W of (0, 0) with bγ |W = 1; choosing N with C × C ⊆ W for the subgroup C := B−N             (balls
are subgroups!), we get bγ |C×C ≡ 1. By Lemma 5.1 (with B = 0) there is a second-degree
character c for bγ . Then v 7→ c(v)uγv is a strongly continuous β-representation:

     c(v)uγv · c(w)uγw = c(v)c(w)β(γv, γw)uγ(v+w)
                              = c(v + w) bγ (v, w)−1 β(γv, γw) uγ(v+w) = β(v, w) c(v + w)uγ(v+w) ,
using the second-degree identity and b−1
                                       γ β(γ·, γ·) = β. It is irreducible, because the operators
c(v)uγv generate the same von Neumann algebra as the uw (w ∈ V∞ ), namely B(H) (Lemma
4.3). By Corollary 4.4 ([SvN]) there is a unitary V with V uv V ∗ = c(v)uγv for all v.        □

Lemma 5.3 (classification). Fix γ and an intertwining pair (c, V ) for γ. (i) If V ′ is a
unitary and c′ : V∞ → T is an arbitrary function such that V ′ uv V ′∗ = c′ (v)uγv for all v, then
c′ is automatically continuous, and it is a second-degree character for bγ ; in particular (c′ , V ′ )
is an intertwining pair, and so is (c, V ) itself, i.e. c is a second-degree character for bγ . (ii)
The intertwining pairs for γ are exactly the pairs
                                                   
                           c · ψ(ω(x, γ ·)), z ux V ,     x ∈ V∞ , z ∈ T,
and (x, z) is uniquely determined.
Proof. (i) Multiplying V ′ uv V ′∗ = c′ (v)uγv and V ′ uw V ′∗ = c′ (w)uγw and comparing with
V ′ uv uw V ′∗ = β(v, w)V ′ uv+w V ′∗ gives c′ (v)c′ (w)β(γv, γw) = β(v, w)c′ (v + w), the second-
degree identity. Continuity: fix v0 and choose unit vectors ξ, η with ⟨uγv0 ξ, η⟩ ̸= 0; by strong
                     NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                               15

continuity (Lemma 4.1(v)) the function v 7→ ⟨uγv ξ, η⟩ is continuous, hence nonzero on a neigh-
borhood of v0 , on which
                                                 ⟨V ′ uv V ′∗ ξ, η⟩
                                        c′ (v) =
                                                   ⟨uγv ξ, η⟩
is a quotient of continuous functions. (ii) Let (c′ , V ′ ) be an intertwining pair and Y := V ′ V ∗ .
For w ∈ V∞ write w = γv:
                 Y uw Y ∗ = V ′ V ∗ uγv V V ′∗ = V ′ c(v)−1 uv V ′∗ = c′ (v)c(v)−1 uw .
                                           

The function χ(w) := c′ (γ −1 w) c(γ −1 w)−1 is a quotient of two second-degree characters for the
same bicharacter bγ , hence a continuous character of V∞ ; by Lemma 3.2(ii), χ = ψ(ω(x, ·))
for a unique x ∈ V∞ . By Lemma 4.1(iii), ux uw u∗x = ψ(ω(x, w))uw = χ(w)uw as well, so u∗x Y
commutes with every uw , hence u∗x Y = z1 for some z ∈ T by Lemma 4.3, i.e. V ′ = z ux V ;
then c′ (v) = χ(γv)c(v) = c(v)ψ(ω(x, γv)). Conversely, for any (x, z), (zux V )uv (zux V )∗ =
ux c(v)uγv u∗x = c(v)ψ(ω(x, γv))uγv by Lemma 4.1(iii), so these are intertwining pairs. Unique-
ness: if zux V = z ′ ux′ V then u∗x ux′ ∈ T1, so by Lemma 4.1(i) ux+x′ ∈ T1; but if y ̸= 0 then uy is
not scalar (Lemma 4.1(iii) and Lemma 3.2(ii): Ad uy multiplies uv by the nontrivial character
ψ(ω(y, ·))); hence x = x′ and then z = z ′ .                                                       □
5.3 The normalized gauge. Now restrict to γ ∈ H = Sp2g (R), so that γS = S.
Lemma 5.4 (normalization). Let γ ∈ H. (i) For any intertwining pair (c, V ) for γ, the
restriction c|S is a ({±1}-valued) character of S. (ii) There exists an intertwining pair for γ
with
                                    V un V ∗ = uγn    (n ∈ S),                               (5.2)
                                                                                        ′   ′
equivalently c|S ≡ 1; call such pairs normalized. (iii) Two normalized pairs (c, V ), (c , V ) for
γ differ exactly by V ′ = z un V with z ∈ T, n ∈ S (and then c′ = c · ψ(ω(n, γ·))).
Proof. (i) For n, m ∈ S: bγ (n, m) = β(γn, γm)β(n, m) = 1 by Lemma 4.1(iv) (both arguments
in S × S, as γS = S), so c(n + m) = c(n)c(m); a character of the exponent-2 group S is
{±1}-valued. (ii) Start from any intertwining pair (c, V ) (Lemma 5.2). By (i) and Lemma
3.2(iii) there is y ∈ V∞ with ψ(ω(y, ·))|S = c|S (a character of S). Put x := γy. Then by
Lemma 5.3(ii), (c · ψ(ω(x, γ·)), ux V ) is an intertwining pair, and for n ∈ S:
              c(n) ψ(ω(x, γn)) = c(n) ψ(ω(γy, γn)) = c(n) ψ(ω(y, n)) = c(n)2 = 1.
(iii) By Lemma 5.3(ii), V ′ = zux V with c′ = c ψ(ω(x, γ·)); normalization of both forces
ψ(ω(x, γn)) = 1 for all n ∈ S, i.e. (as γS = S) ψ(ω(x, m)) = 1 for all m ∈ S, i.e. x ∈ S ⊥ = S
(Lemma 3.2(i)). Conversely every such pair is normalized, since for n ∈ S, ψ(ω(x, γn)) = 1. □

Standing choice. Fix once and for all, for each γ ∈ H, a normalized intertwining pair
(cγ , Vγ′ ), with (ce , Ve′ ) = (1, 1). (This is a countable family of choices — H is countable —
and no continuity or measurability in γ is ever required: H is discrete. This is the reason no
measurable-selection issues arise anywhere in this paper.)

5.4 The class κ. Proposition 5.5. (i) There are unique maps µ : H × H → T and d :
H × H → S with
                     Vγ′ Vγ′′ = µ(γ, γ ′ ) ud(γ,γ ′ ) Vγγ
                                                        ′
                                                          ′ (γ, γ ′ ∈ H).   (5.3)
(ii) d is a normalized 2-cocycle: d ∈ Z 2 (H, S), d(e, ·) = d(·, e) = 0. (iii) The class κ := [d] ∈
H 2 (H, S) does not depend on the choice of the normalized family {(cγ , Vγ′ )}γ∈H with Ve′ = 1.
(Requiring Ve′ = 1 costs nothing: any normalized pair for e may be replaced by (1, 1).) (iv) All
of (i)–(iii) hold verbatim for a family of normalized pairs indexed by a subgroup N ≤ H (with
16                           NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

Ve′ = 1), producing a class κN ∈ H 2 (N, S); and κN = resH
                                                         N κ. In particular the restriction of
κ to N may be computed from any normalized family over N , not necessarily the restriction of
the global one.
Proof. (i) Vγ′ Vγ′′ satisfies, for v ∈ V∞ ,
                       (Vγ′ Vγ′′ )uv (Vγ′ Vγ′′ )∗ = Vγ′ cγ ′ (v)uγ ′ v Vγ′∗ = cγ ′ (v) cγ (γ ′ v) uγγ ′ v ,
so cγ ′ · (cγ ◦ γ ′ ), Vγ′ Vγ′′ is an intertwining pair for γγ ′ (the trivializing function is continuous,
                               

being a product of continuous functions; alternatively Lemma 5.3(i)). Its restriction to S is
trivial: for n ∈ S, cγ ′ (n) = 1 and cγ (γ ′ n) = 1 since γ ′ n ∈ S. Comparing with the normal-
ized pair (cγγ ′ , Vγγ′ ) via Lemma 5.4(iii) — both are normalized pairs for γγ ′ — yields unique
                        ′

µ(γ, γ ′ ) ∈ T and d(γ, γ ′ ) ∈ S with (5.3). (Uniqueness also directly: if µud Vγγ                      ′ = µ̃u V ′ then
                                                                                                            ′   d˜ γγ ′
                              ˜
ud+d˜ is scalar, so d = d, then µ = µ̃.)
   (ii) Expand (Vγ′1 Vγ′2 )Vγ′3 = Vγ′1 (Vγ′2 Vγ′3 ) using (5.3), the relation Vγ′1 un Vγ′∗1 = uγ1 n (5.2), and
un um = un+m for n, m ∈ S (Lemma 4.1(i),(iv)):
                              LHS = µ(γ1 , γ2 )µ(γ1 γ2 , γ3 ) ud(γ1 ,γ2 )+d(γ1 γ2 ,γ3 ) Vγ′1 γ2 γ3 ,
     RHS = µ(γ2 , γ3 ) Vγ′1 ud(γ2 ,γ3 ) Vγ′∗1 Vγ′1 Vγ′2 γ3 = µ(γ2 , γ3 )µ(γ1 , γ2 γ3 ) uγ1 d(γ2 ,γ3 )+d(γ1 ,γ2 γ3 ) Vγ′1 γ2 γ3 .
By the uniqueness in (i) (comparing the S-parts),
                                d(γ1 , γ2 ) + d(γ1 γ2 , γ3 ) = γ1 d(γ2 , γ3 ) + d(γ1 , γ2 γ3 ),
the cocycle identity. Normalization: Ve′ = 1 gives Vγ′ Ve′ = Vγ′ = µ(γ, e)ud(γ,e) Vγ′ , so d(γ, e) = 0,
µ(γ, e) = 1; similarly d(e, γ) = 0.
    (iii) By Lemma 5.4(iii), any other normalized family has the form Ṽγ = zγ unγ Vγ′ with zγ ∈ T,
nγ ∈ S, and ze = 1, ne = 0 (since Ṽe = 1 and the pair (z, n) for e is unique). Then, using (5.2)
and β|S×S = 1,
Ṽγ Ṽγ ′ = zγ zγ ′ unγ Vγ′ unγ ′ Vγ′∗ Vγ′ Vγ′′ = zγ zγ ′ µ(γ, γ ′ ) unγ +γnγ ′ +d(γ,γ ′ ) Vγγ
                                                                                             ′                         ′
                                                                                                                        
                                                                                               ′ = zγ zγ ′ zγγ ′ µ(γ, γ ) u ˜
                                                                                                                           d(γ,γ ′ ) Ṽγγ
                                                                                                                                          ′


with d˜ = d + ∂n, (∂n)(γ, γ ′ ) = γnγ ′ − nγγ ′ + nγ (signs irrelevant: exponent 2). So [d]
                                                                                         ˜ = [d].
   (iv) Every step above used only products of group elements within the indexing set, so the
same arguments apply to a family indexed by a subgroup N , yielding dN ∈ Z 2 (N, S) and a
class κN independent of the choice of normalized family over N . Taking as one such family the
restriction {(cγ , Vγ′ )}γ∈N of the global family, whose cocycle is d|N ×N , we get κN = [d|N ×N ] =
resH
   N κ.                                                                                            □
5.5 The groups. Let A := S ⊕ S = R4g with the diagonal H-action γ̂(s, s′ ) := (γs, γs′ ), and
let
                                    d := (d, d) ∈ Z 2 (H, A),
a normalized cocycle (componentwise, by Proposition 5.5(ii)) with class [d] = (κ, κ) under
H 2 (H, A) = H 2 (H, S) ⊕ H 2 (H, S). The polynomial ring R acts on S and on A by scalar
multiplication, commuting with the H-action; thus f d ∈ Z 2 (H, A) is a normalized cocycle for
every f ∈ R, with class (f κ, f κ).
Definition 5.6. For f ∈ R put
                                       Gf := A ×f d H
(§2.1). Each Gf is a countable discrete group containing A = A × {e} as a normal subgroup
with Gf /A ∼
           = H, and conjugation on A is the diagonal action (2.1). For f = 0, G0 = A ⋊ H is
the semidirect product.
                      NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                    17

Remark 5.7 (gauge-independence of the family). The cocycle d, hence d and each Gf ,
depends on the fixed choice of normalized family made above. This dependence is harmless: if
{Ṽγ } is another normalized family (with Ṽe = 1), its cocycle is d˜ = d + ∂n for some n : H → S
                                                                          
with ne = 0 (proof of Proposition 5.5(iii)), so f d̃ = f d + ∂ f (n, n) , and the map (a, γ) 7→
(a + f (nγ , nγ ), γ) is an isomorphism A ×f d H → A ×f d̃ H (direct computation with the twisted
multiplication). All statements proved below about the groups Gf are therefore independent
of the gauge. For definiteness we keep the family fixed once and for all, and d, d, κ, Gf always
refer to it.

       6. Doubling, untwisting, isogeny spreading: L(Gf ) ∼
                                                          = L(G0 ) for all f
6.1 The dual solenoid. Let X := A,       b the dual of the countable discrete group A = R4g : a
compact metrizable abelian group with Haar probability µ. Since A has exponent 2, every
character is {±1}-valued and X has exponent 2. Write ea ∈ C(X), ea (x) = x(a), as in §2.4.
The H-action dualizes: for γ ∈ H define Φγ : X → X by (Φγ x)(a) := x(γ̂ −1 a); each Φγ is a
continuous automorphism of the compact group X, hence preserves µ: the pushforward (Φγ )∗ µ
is a Borel probability measure with ((Φγ )∗ µ)(E + y) = µ(Φ−1           −1          −1
                                                               γ E + Φγ y) = µ(Φγ E) for all
y ∈ X, i.e. translation-invariant, so it equals µ by uniqueness of Haar measure [SF]; γ 7→ Φγ is
an action, and
            ea ◦ Φ−1         γ
                  γ = eγ̂a =: ea ,                      F := F ◦ Φ−1
                                           more generally      γ             ∞
                                                                  γ (F ∈ L (X))        (6.1)
defines an action of H on L∞ (X) by trace-preserving (i.e. γ F dµ = F dµ, by µ-preservation
                                                          R         R
of Φγ ) automorphisms, which are normal by Lemma 2.5 (each γ (·) is a unital ∗-homomorphism
                                      ∞
of              R Neumann algebra L (X) whose composition with the faithful normal state
R the abelian von
   · dµ is again · dµ, hence normal).

6.2 Conjugate doubling. Let H denote the conjugate Hilbert space of H (same additive
group, written ξ;¯ scalar action c · ξ¯ := c̄ξ; inner product ⟨ξ,
                                                               ¯ η̄⟩ := ⟨η, ξ⟩). For T ∈ B(H) let
               ¯
T̄ ∈ B(H), T̄ ξ := T ξ; then T 7→ T̄ is conjugate-linear, multiplicative, ∗-preserving, unital, and
bijective; in particular zT = z̄ T̄ for z ∈ C and T̄ is unitary iff T is.
   On K := H ⊗ H define, for a = (n, n′ ) ∈ A = S ⊕ S,
                                 Ua := un ⊗ ūn′ ,     Ω := ξ0 ⊗ ξ¯0 .

Lemma 6.1. (i) a 7→ Ua is a unitary representation of A with ⟨Ua Ω, Ω⟩ = δa,0 , and Ω is cyclic
for B := {Ua : a ∈ A}′′ . Consequently (Lemma 2.3) there is a unitary W0 : L2 (X) → K with
W0 ea = Ua Ω, the algebra B is a masa in B(K), and Jb := Ad W0 : L∞ (X) → B is a normal
                                                        R
∗-isomorphism with J(eb a ) = Ua and ⟨J(F  b )Ω, Ω⟩ = F dµ.
   (ii) Let ργ be the Koopman unitaries on L2 (X): (ργ h)(x) := h(Φ−1      γ x) (unitary since Φγ
preserves µ; ργγ ′ = ργ ργ ′ ), and put ρ̃γ := W0 ργ W0∗ ∈ U(K). Then ρ̃γ Ua ρ̃−1
                                                                               γ = Uγ̂a , and

                                   Jb ◦ (γ ·) = Ad ρ̃γ ◦ Jb on L∞ (X).                                 (6.2)
Proof. (i) U is a representation: Ua Ub = un um ⊗ ūn′ ūm′ = un+m ⊗ un′ um′ = Ua+b by Lemma
4.1(i),(iv) (no scalars on S) and multiplicativity of the bar map. Orthonormality: ⟨Ua Ω, Ω⟩ =
⟨un ξ0 , ξ0 ⟩⟨ūn′ ξ¯0 , ξ¯0 ⟩ = δn,0 ⟨un′ ξ0 , ξ0 ⟩ = δn,0 δn′ ,0 by Lemma 4.2(i). Cyclicity: Ua Ω = un ξ0 ⊗
un′ ξ0 ; by Lemma 4.2(ii) the vectors un ξ0 are total in H and the un′ ξ0 are total in H (the bar
map is a conjugate-linear isometric bijection, preserving totality), and elementary tensors of
total sets are total in the Hilbert tensor product (a vector orthogonal to all ξ ⊗ η̄ with ξ, η̄
running through total sets is orthogonal to all elementary tensors — inner products against
18                     NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

elementary tensors are separately continuous and linear in each leg — hence zero, as elementary
tensors are total by definition of H ⊗ H). The rest is Lemma 2.3 with Y = A, Yb = X.
   (ii) First, on L2 (X): ργ Mea ρ−1
                                  γ = Mea ◦Φ−1
                                            γ
                                                = Meγ̂a (direct computation: (ργ Mea ρ−1γ h)(x) =
ea (Φγ x)h(x)). Conjugating by W0 and using W0 Mea W0 = Ua (Lemma 2.3(iii)) gives ρ̃γ Ua ρ̃−1
      −1                                                 ∗
                                                                                              γ =
                                                                         ∞
Uγ̂a . Now both sides of (6.2) are normal unital ∗-homomorphisms L (X) → B(K) (composi-
                                          b γ ea ) = J(e
tions of such), and on the generator ea : J(                              b a )ρ̃−1
                                                     b γ̂a ) = Uγ̂a = ρ̃γ J(e    γ . Apply Lemma
2.4.                                                                                            □
     For γ ∈ H set
                                           Vγ := Vγ′ ⊗ Vγ′ ∈ U(K).

Lemma 6.2. For all γ, γ ′ ∈ H and a ∈ A:
               (i) Vγ Ua V∗γ = Uγ̂a ;        (ii) Vγ Vγ ′ = Ud(γ,γ ′ ) Vγγ ′ ;        (iii) Ve = 1.
Proof. (i) By (5.2), Vγ′ un Vγ′∗ = uγn ; applying the bar map (which is multiplicative and ∗-
                                                                      ∗
preserving) to the same scalar-free relation for n′ gives Vγ′ ūn′ Vγ′ = ūγn′ ; tensoring, Vγ U(n,n′ ) V∗γ =
U(γn,γn′ ) = Uγ̂a . (ii) By (5.3) and conjugate-linearity of the bar map,
                                 Vγ′ Vγ′′ = Vγ′ Vγ′′ = µ(γ, γ ′ ) ūd(γ,γ ′ ) Vγγ
                                                                                ′ ,
                                                                                  ′


hence
                   Vγ Vγ ′ = µµ (γ, γ ′ ) ud(γ,γ ′ ) ⊗ ūd(γ,γ ′ ) Vγγ ′ = U(d,d)(γ,γ ′ ) Vγγ ′ ,
                                                                 

since |µ(γ, γ ′ )|2 = 1. (iii) Ve′ = 1.                                                                      □
   The conjugate doubling has annihilated the uncontrollable Weil-index scalar µ: identity (ii)
is exact.

6.3 The untwister. Proposition 6.3. Define ϖγ := Vγ ρ̃−1  γ and wγ := J
                                                                           b−1 (ϖγ ). Then
ϖγ ∈ U(B), so wγ ∈ U(L∞ (X)) (a T-valued L∞ class); we = 1; and for all γ, γ ′ ∈ H:
                               wγ · γ wγ ′ = ed(γ,γ ′ ) wγγ ′      in U (L∞ (X)).                         (6.3)
Proof. For every a ∈ A, by Lemma 6.1(ii) and Lemma 6.2(i),
                   ϖγ Ua ϖγ−1 = Vγ ρ̃−1
                                                   −1                 −1
                                          γ Ua ρ̃γ Vγ = Vγ Uγ̂ −1 a Vγ = Uγ̂γ̂ −1 a = Ua ,
                                       ′
so ϖγ ∈ {Ua : a ∈ A}′ = {Ua }′′ = B ′ = B (B is a masa, and the commutant of a set equals
the commutant of the von Neumann algebra it generates). Clearly ϖe = 1. Now
                                                         −1 −1               −1
                ϖγ · ρ̃γ ϖγ ′ ρ̃−1   = Vγ ρ̃−1
                                   
                                γ           γ ρ̃γ Vγ ′ ρ̃γ ′ ρ̃γ = Vγ Vγ ′ ρ̃γγ ′ = Ud(γ,γ ′ ) ϖγγ ′ ,

using ρ̃γ ρ̃γ ′ = ρ̃γγ ′ and Lemma 6.2(ii). Apply Jb−1 : by (6.2), Jb−1 (ρ̃γ ϖγ ′ ρ̃−1             γ Jb−1 ϖ ′ =
                                                                                                             
                                                                                         γ ) =             γ
γ w ′ , and Jb−1 (U ) = e ; (6.3) follows.                                                                     □
   γ                 d      d


6.4 Isogeny spreading. Lemma 6.4. Let f ∈ R ∖ {0}. Multiplication by f on A is an
injective H-equivariant endomorphism; its dual fˆ : X → X, (fˆx)(a) := x(f a), is a continuous
surjective endomorphism of X with: (i) ea ◦ fˆ = ef a for all a ∈ A; (ii) fˆ ◦ Φγ = Φγ ◦ fˆ for all
γ ∈ H; (iii) fˆ∗ µ = µ. Consequently Ξf : L∞ (X) → L∞ (X), Ξf (F ) := F ◦ fˆ, is a well-defined
unital, integral-preserving, normal ∗-endomorphism with Ξf (ea ) = ef a , Ξf ◦ γ = γ ◦ Ξf , and Ξf
maps U(L∞ ) into U(L∞ ).
                     NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                     19

Proof. Injectivity of a 7→ f a: A is a free R-module and R is a domain. Equivariance: the H-
action is R-linear. fˆ is a continuous homomorphism with (i) by definition. Surjectivity: given
y ∈ X, define a character χ0 on the subgroup f A ≤ A by χ0 (f a) := y(a) — well defined by
injectivity — and extend χ0 to a character x of A (A is an F2 -vector space: choose a complement
of f A and extend by 1; or quote divisibility of T). Then fˆx = y. (iii) fˆ∗ µ is a Borel probability
on X; for y = fˆz ∈ fˆ(X) = X and Borel E: (fˆ∗ µ)(E+y) = µ(fˆ−1 E+z) = µ(fˆ−1 E) = (fˆ∗ µ)(E)
(using fˆ−1 (E + fˆz) = fˆ−1 (E) + z, valid since fˆ is a surjective homomorphism, and translation
invariance of µ). So fˆ∗ µ is translation invariant, hence = µ [SF]. Consequently: Ξf is well
defined on L∞ -classes and integral-preserving because µ(fˆ−1 (null)) = 0 and F ◦ fˆ dµ =
                                                                                       R

  F d(fˆ∗ µ) = F dµ; it is clearly a unital ∗-homomorphism, and it is Rnormal by Lemma 2.5
R              R

(the normality criterion), applied with the faithful normal state ρ = · dµ on L∞ (X): the
composition ρ ◦ Ξf = · dµ is normal. Commutation with the H-action: by (ii), (γ F ) ◦ fˆ =
                         R

F ◦ Φ−1    ˆ        ˆ −1 γ           ˆ                                                         ˆ
      γ ◦ f = F ◦ f ◦ Φγ = (F ◦ f ). Unitaries go to unitaries: |F | = 1 a.e. implies |F ◦ f | = 1
a.e.                                                                                               □
                                              (f )                                         (0)
Proposition 6.5. For f ∈ R define wγ                 := Ξf (wγ ) = wγ ◦ fˆ if f ̸= 0, and wγ := 1. Then
 (f )
we = 1 and, for all γ, γ ′ ∈ H,
                                     (f )                 (f )
                          wγ(f ) · γ wγ ′ = ef d(γ,γ ′ ) wγγ ′    in U (L∞ (X)).                       (6.4)
Proof. For f ̸= 0: apply the normal ∗-homomorphism Ξf to (6.3), using Ξf (ed ) = ef d and
                                 (f )
Ξf (γ wγ ′ ) = γ Ξf (wγ ′ ) = γ wγ ′ (Lemma 6.4). For f = 0: e0 = 1 and the identity is trivial. □
6.5 The canonical copy of L∞ (X) inside L(G0 ) and the isomorphism theorem. Let
M := L(G0 ) act on ℓ2 (G0 ), with trace τ as in §2.5, and write
                         ua := λ(a,e) ,       ℓγ := λ(0,γ)       (a ∈ A, γ ∈ H).
(From here through the end of §8, the symbol ua refers to these group-von-Neumann-algebra
                                                                                                 (f )
unitaries; the Weyl operators uv of §§4–6.4 enter §§6.5–8 only through the functions wγ ∈
L∞ (X). The Weyl operators reappear, with their original meaning, in §9, which is independent
of §§6.5–8.) From the group law of G0 = A ⋊ H: ua ub = ua+b , ℓγ ℓγ ′ = ℓγγ ′ , ℓγ ua ℓ∗γ = uγ̂a ,
λ(a,γ) = ua ℓγ , and τ (ua ℓγ ) = δ(a,γ),(0,e) .
   Under the unitary ℓ2 (G0 ) ∼  = ℓ2 (A)⊗ℓ2 (H), δ(a,γ) 7→ δa ⊗δγ , one computes from (a, e)(b, γ ′ ) =
(a + b, γ ) and (0, γ)(b, γ ) = (γ̂b, γγ ′ ):
         ′                  ′

    ua = Sa ⊗ 1,       ℓγ = Tγ ⊗ λH
                                  γ ,          where Sa δb = δa+b , Tγ δb = δγ̂b , λH
                                                                                    γ δγ ′ = δγγ ′ .   (6.5)

Lemma 6.6. (i) N := {ua : a ∈ A}′′ = {Sa }′′ ⊗ 1 (as sets of operators on ℓ2 (A) ⊗ ℓ2 (H)), and
there is a normal unital ∗-isomorphism
                                                                 Z
                          ∞
                     ȷ : L (X) → N ,   ȷ(ea ) = ua ,      τ ◦ ȷ = · dµ.

(ii) For every γ ∈ H and F ∈ L∞ (X):                   ℓγ ȷ(F ) ℓ∗γ = ȷ(γ F ). (iii) N is abelian, and for
F ∈ U(L∞ (X)), ȷ(F ) ∈ U(N ) ⊆ U(M ).
Proof. (i) Apply Lemma 2.3 to Y = A on ℓ2 (A) with the representation S and the vector δ0 :
⟨Sa δ0 , δ0 ⟩ = δa,0 and {Sa δ0 } = {δ                                                    ∞           ′′
                                        R a } is total; this gives ′′a normal′′ iso j0 : L (X) → {Sa } ,
j0 (ea ) = Sa , with ⟨j0 (F )δ0 , δ0 ⟩ = F dµ. Next, {Sa ⊗ 1} = {Sa } ⊗ 1: the inclusion ⊇ holds
because for x ∈ {Sa }′′ , by Kaplansky [SF] there is a bounded net xi ∈ span{Sa } with xi → x
σ-strongly, and then xi ⊗ 1 → x ⊗ 1 σ-strongly with xi ⊗ 1 ∈ span{ua }; the inclusion ⊆: every
20                      NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

T ∈ {Sa }′ gives T ⊗ 1 ∈ {Sa ⊗ 1}′ , so any y ∈ {Sa ⊗ 1}′′ commutes with {T ⊗ 1} and with
1⊗B(ℓ2 H) (as each Sa ⊗1 does); the commutant of 1⊗B(ℓ2 H) is B(ℓ2 A)⊗1 (matrix-coefficient
computation over an orthonormal basis of ℓ2 H: writing y as an H × H matrix of operators on
ℓ2 A, commutation with all 1⊗eγγ ′ forces y diagonal with constant diagonal), so y = x⊗1 with x
commuting with every T ∈ {Sa }′ , i.e. x ∈ {Sa }′′ . Define      R ȷ(F ) := j0 (F )⊗1; then ȷ(ea ) = ua and
τ (ȷ(F )) = ⟨(j0 (F ) ⊗ 1)δ(0,e) , δ(0,e) ⟩ = ⟨j0 (F )δ0 , δ0 ⟩ = F dµ; ȷ is normal (j0 is, and x 7→ x ⊗ 1
is a normal isomorphism onto its image). (ii) Both sides are normal unital ∗-homomorphisms
L∞ (X) → B(ℓ2 G0 ); on generators, ℓγ ȷ(ea )ℓ∗γ = ℓγ ua ℓ∗γ = uγ̂a = ȷ(eγ̂a ) = ȷ(γ ea ). Apply Lemma
2.4. (iii) Clear.                                                                                         □

Theorem 6.7. For every f ∈ R, the map
                                             πf (a, γ) := ua Wγ(f ) ℓγ ,         Wγ(f ) := ȷ wγ(f ) ,
                                                                                                   
                 πf : Gf → U(M ),
is a group homomorphism with τ (πf (a, γ)) = δ(a,γ),(0,e) and πf (Gf )′′ = M . Consequently
(Lemma 2.7) there is a trace-preserving ∗-isomorphism
                                        ∼
                                        =
                            L(Gf ) −−→ L(G0 ) = M,                 λ(a,γ) 7→ πf (a, γ).
Proof. Homomorphism. Using (6.5)-relations, Lemma 6.6(ii), commutativity of N , and the
ȷ-image of (6.4):
                                          (f )                           (f )                                (f ) 
πf (a, γ) πf (b, γ ′ ) = ua Wγ(f ) ℓγ ub Wγ ′ ℓγ ′ = ua Wγ(f ) uγ̂b ȷ(γ wγ ′ ) ℓγ ℓγ ′ = ua+γ̂b ȷ wγ(f ) ·γ wγ ′ ℓγγ ′
                                     (f )                            (f )
          = ua+γ̂b ȷ ef d(γ,γ ′ ) ȷ wγγ ′ ℓγγ ′ = ua+γ̂b+f d(γ,γ ′ ) Wγγ ′ ℓγγ ′ = πf (a, γ)(b, γ ′ ) ,
                                                                                                    

where (a, γ)(b, γ ′ ) = (a + γ̂b + f d(γ, γ ′ ), γγ ′ ) is the Gf -law and we used ȷ(ec ) = uc . Also
              (f )
πf (0, e) = We = ȷ(1) = 1. Since each πf (a, γ) is unitary, πf is a homomorphism into U(M )
                      (f )
(ua , ℓγ ∈ M and Wγ ∈ N ⊆ M ).
                                 (f )
   Trace. For γ ̸= e: y := ua Wγ ∈ N = {Sb ⊗ 1}′′ . By Kaplansky [SF] there is a bounded net
yi ∈ span{ub : b ∈ A} with yi → y σ-weakly. Then
                        
            τ πf (a, γ) = ⟨y ℓγ δ(0,e) , δ(0,e) ⟩ = ⟨y δ(0,γ) , δ(0,e) ⟩ = lim⟨yi δ(0,γ) , δ(0,e) ⟩ = 0,
                                                                             i
                                                                                                        (f )
because ⟨ub δ(0,γ) , δ(0,e) ⟩ = ⟨δ(b,γ) , δ(0,e) ⟩ = 0 for every b when γ ̸= e. For γ = e: we = 1, so
τ (πf (a, e)) = τ (ua ) = δa,0 .
                                                                                              (f )
   Generation. πf (a, e) = ua , so πf (Gf )′′ ⊇ {ua }′′ = N = ȷ(L∞ (X)); in particular (Wγ )−1 ∈
                               (f )
πf (Gf )′′ , whence ℓγ = (Wγ )−1 πf (0, γ) ∈ πf (Gf )′′ for every γ. But {ua , ℓγ } generate {λ(a,γ) =
ua ℓγ }, hence M . So πf (Gf )′′ = M .
   Lemma 2.7 (applied with G0 , Λ = Gf , π = πf ) finishes the proof.                                □

Remark. One untwisting family (wγ ) serves all f ∈ R simultaneously through Ξf ; every
identity above holds exactly in U(L∞ (X)) and U (M ).

                                             7. All Gf are ICC
   Recall the symmetric shears: for symmetric matrices b, c ∈ Symg (over any commutative
ring of characteristic 2 under consideration),
                                     
               1 b                  1 0
        xb :=          ,    yc :=              (block form, acting on columns (v1 , v2 )T ).
               0 1                  c 1
                     NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                               21

Lemma 7.1. For b, c ∈ Mg : xb ∈ Sp2g iff b is symmetric, and yc ∈ Sp2g iff c is symmetric. In
particular xb , yc ∈ H for b, c ∈ Symg (R).
Proof. ω(xb v, xb w) = ⟨v1 +bv2 , w2 ⟩+⟨v2 , w1 +bw2 ⟩ = ω(v, w)+⟨bv2 , w2 ⟩+⟨v2 , bw2 ⟩ = ω(v, w)+
⟨(b + bT )v2 , w2 ⟩, which vanishes identically iff b + bT = 0, i.e. (characteristic 2) b = bT . The
computation for yc is symmetric.                                                                  □

Proposition 7.2. (i) For every γ ∈ H ∖ {e}, the subgroup (1 + γ̂)A = {a + γ̂a : a ∈ A} of A
is infinite. (ii) Every orbit of the diagonal H-action on A ∖ {0} is infinite.
Proof. (i) 1 + γ̂ is an R-linear endomorphism of A (the R-action commutes with γ̂). If its image
were {0} then γ̂ = idA , so γ would fix S = R2g pointwise, i.e. γ = e — excluded. A nonzero
R-submodule of the torsion-free R-module A contains a nonzero cyclic submodule Rx ∼            = R,
which is infinite. (ii) Let 0 ̸= a = (n, n′ ) ∈ A = S ⊕ S. Since the action is diagonal, it suffices
to treat the case n = (n1 , n2 ) ̸= 0 (if n = 0 then n′ ̸= 0 and the identical argument applies to
the second summand). If n1 ̸= 0, pick α with (n1 )α ̸= 0 and consider γu := yuEαα ∈ H, u ∈ R:
then γu n = (n1 , n2 + u(n1 )α eα ), and these vectors are pairwise distinct as u ranges over the
infinite ring R (their second components differ, since (n1 )α ̸= 0 and R is a domain). Hence the
vectors γ̂u a = (γu n, γu n′ ) are pairwise distinct, and the orbit of a is infinite. If n1 = 0 then
n2 ̸= 0; use xuEαα with (n2 )α ̸= 0 instead, which moves n to (n1 + u(n2 )α eα , n2 ).            □

Proposition 7.3. For every f ∈ R, the group Gf is a countably infinite ICC group. In
particular (Lemma 2.6) M := L(G0 ) is a II1 factor.
Proof. Gf is countable and infinite. Let h ∈ Gf ∖ {(0, e)}. Case h = (a, e), a ̸= 0: by (2.1), the
conjugacy class of h contains {(γ̂a, e) : γ ∈ H}, infinite by Proposition 7.2(ii). Case h = (a, γ),
γ ̸= e: since A has exponent 2 and the cocycle f d is normalized, (b, e)−1 = (b, e) for b ∈ A,
and
     (b, e)(a, γ)(b, e)−1 = (b + a, γ)(b, e) = b + a + γ̂b + f d(γ, e), γ = a + (1 + γ̂)b, γ .
                                                                                           

As b ranges over A, this set is infinite by Proposition 7.2(i).                                     □

                                        8. Property (T)

8.1 Uniformity and assembly. Lemma 8.1 (uniformity). Let G be lcsc, N ⊴ G closed,
and suppose (G, N ) has relative property (T). Then for every ε > 0 there are a compact Q ⊂ G
and δ > 0 with the following property: in every strongly continuous unitary representation (π, H)
of G, every (Q, δ)-invariant unit vector ξ satisfies ∥ξ − P ξ∥ ≤ ε, where P is the orthogonal
projection onto the space HN of N -invariant vectors.
Proof. First, HN is G-invariant: for ξ ∈ HN , g ∈ G, n ∈ N : π(n)π(g)ξ = π(g)π(g −1 ng)ξ =
π(g)ξ since g −1 ng ∈ N . Hence (HN )⊥ is G-invariant and P ∈ π(G)′ .
   Suppose the conclusion fails for some ε0 > 0. Take an exhaustion Q1 ⊆ Q2 ⊆ · · · of G as in
Lemma 2.2(i). For each n there are then a strongly continuous representation (πn , Hn ) and a
(Qn , n1 )-invariant unit vector ξn with ∥ξn −Pn ξn ∥ > ε0 . Put ηn := (1−Pn )ξn , so ∥ηn ∥ > ε0 , and
let ζn := ηn /∥ηn ∥, a unit vector in the subrepresentation πn⊥ of πn on (HnN )⊥ — a representation
with no nonzero N -invariant vectors (an N -invariant vector there lies in HnN ∩ (HnN )⊥ = 0).
Since 1 − Pn ∈ πn (G)′ , for g ∈ Qn :
                                            ∥(1 − Pn )(πn (g)ξn − ξn )∥   1/n
                       ∥πn (g)ζn − ζn ∥ =                               ≤     .
                                                       ∥ηn ∥               ε0
22                    NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

The direct sum π ⊥ :=
                         L ⊥
                            n πn is a strongly continuous unitary representation of G with no
nonzero N -invariant vector (each component would be one). But it has a.i.v.: given a compact
Q and ε > 0, choose n with Q ⊆ Qn (Lemma 2.2(i)) and 1/(nε0 ) ≤ ε; then the vector ζn , viewed
in the direct sum, is (Q, ε)-invariant. This contradicts relative property (T) of (G, N ).  □

Lemma 8.2 (assembly). Let G be lcsc and N ≤ G a closed subgroup such that N =
N1 N2 · · · Nr (every element of N is a product n1 · · · nr with ni ∈ Ni ), where each Ni is a
closed subgroup of G admitting a closed subgroup Σi ≤ G with Ni ⊴ Σi and (Σi , Ni ) having
relative property (T). Then (G, N ) has relative property (T).
                                                                                             1
Proof. Let (π, H) be a strongly continuous representation of G with a.i.v. Set ε := 8r           and, for
each i, apply Lemma 8.1 to the lcsc group Σi (closed subgroups of lcsc groups are lcsc) with
                         Sr Ni , obtaining
its closed normal subgroup                   (Qi , δi ) with Qi ⊂ Σi ⊆ G compact. Choose a unit
vector ξ ∈ H which is       i=1 iQ , min i i -invariant. For each i, the restriction π|Σi is strongly
                                          δ
continuous and ξ is (Qi , δi )-invariant for it, so by the choice of (Qi , δi ) there is an Ni -invariant
vector ηi (namely Pi ξ) with ∥ξ − ηi ∥ ≤ ε. Hence for every ni ∈ Ni :
                ∥π(ni )ξ − ξ∥ ≤ ∥π(ni )(ξ − ηi )∥ + ∥π(ni )ηi − ηi ∥ + ∥ηi − ξ∥ ≤ 2ε.
For n = n1 · · · nr ∈ N , telescoping:
                          Xr                                    r
                                                                X
                                                                  ∥π(ni )ξ − ξ∥ ≤ 2rε = 14 .
                                                             
       ∥π(n)ξ − ξ∥ ≤            π(n1 · · · ni−1 ) π(ni )ξ − ξ =
                         i=1                                     i=1

Let B := π(N )ξ: a nonempty bounded subset of H (contained in the unit sphere) with π(n)B =
B for every n ∈ N . By Lemma 2.1 its circumcenter c0 is fixed by every π(n), n ∈ N , and
∥c0 − ξ∥ ≤ r(ξ) = supb∈B ∥ξ − b∥ ≤ 41 , so c0 ̸= 0: a nonzero N -invariant vector.        □

Lemma 8.3 ((T) from relative (T) and the quotient). Let G be lcsc and N ⊴ G closed.
If (G, N ) has relative property (T) and G/N has property (T), then G has property (T).
Proof. Let (π, H) be a strongly continuous representation of G with a.i.v.; we must produce
a nonzero G-invariant vector. Split H = HN ⊕ (HN )⊥ , a G-invariant decomposition with
P ∈ π(G)′ the projection onto HN (proof of Lemma 8.1). The subrepresentation π ⊥ on (HN )⊥
has no nonzero N -invariant vectors, so by relative property (T) it does not have a.i.v.: there
are a compact Q0 ⊂ G and δ0 ∈ (0, 1] such that no unit vector of (HN )⊥ is (Q0 , δ0 )-invariant
for π ⊥ .
   Claim: the representation π N of G on HN has a.i.v. Let Q′ ⊂ G be compact and ε′ > 0;
we may assume ε′ ≤ 1. Put δ := 14 min(δ0 , ε′ ) and choose a unit vector ξ which is (Q0 ∪ Q′ , δ)-
invariant for π; write ξ = η ⊕ ζ with η = P ξ. If ∥ζ∥ > δ/δ0 , then ζ/∥ζ∥ would be a unit vector
                         ζ     ζ
of (HN )⊥ with ∥π ⊥ (g) ∥ζ∥ − ∥ζ∥ ∥ ≤ ∥π(g)ξ − ξ∥/∥ζ∥ ≤ δ/∥ζ∥ < δ0 for g ∈ Q0 (using P ∈ π(G)′ )
— impossible. So ∥ζ∥ ≤ δ/δ0 ≤ 41 and ∥η∥2 = 1 − ∥ζ∥2 ≥ 15                           1            ′
                                                           16 , in particular ∥η∥ ≥ 2 . For g ∈ Q :
                                             ∥P (π(g)ξ − ξ)∥    δ
                                η
                       π N (g) ∥η∥    η
                                   − ∥η∥ =                   ≤     = 2δ ≤ ε′ .
                                                   ∥η∥         1/2
This proves the claim.
   Since N acts trivially on HN , π N factors through a unitary representation π̇ of G/N , which
is strongly continuous: for fixed ξ ∈ HN the map G → H, g 7→ π N (g)ξ, is continuous and
constant on cosets of N , and the quotient map p is open (Lemma 2.2(ii)), so the factored
map gN 7→ π̇(gN )ξ is continuous (p open and continuous implies that a function on G/N is
continuous iff its pullback is). Moreover π̇ has a.i.v.: every compact Q̇ ⊂ G/N is p(Q) for
                          NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                      23


some compact Q ⊂ G (Lemma 2.2(ii)), and a (Q, ε)-invariant unit vector for π N is (Q̇, ε)-
invariant for π̇. By property (T) of G/N there is a nonzero π̇(G/N )-invariant vector in HN ; it
is π(G)-invariant.                                                                            □

8.2 The ambient group G and its property (T). Let
                                       4g
        L := Sp2g (k∞ ),         V := k∞  = V∞ ⊕ V∞ (diagonal L-action),                   G := V ⋊ L,
with the product topology on V × L and multiplication (v, l)(w, m) = (v + lw, lm). Here L is a
closed subset of the second countable locally compact space M2g (k∞ ) (cut out by the polynomial
equations γ T Jγ = J) and a topological group (multiplication is polynomial; inversion γ −1 =
J −1 γ T J is polynomial), hence lcsc; and G is lcsc (k∞ is second countable, products preserve
this; the action map L × V → V is polynomial, hence continuous).
                                                                        g      g
   Let ε1 , . . . , εg , φ1 , . . . , φg be the standard basis of V∞ = k∞  ⊕ k∞   (εi := (ei , 0), φi := (0, ei )),
so thatLω(εi , φj ) = δij and ω(εi , εj ) = ω(φi , φj ) = 0: a hyperbolic (symplectic) basis, and
V∞ = gi=1 Pi with Pi := k∞ εi ⊕ k∞ φi .
                             (i)
   For each i let SL2 ≤ GL2g (k∞ ) be the copy of SL2 (k∞ ) acting on Pi in the basis (εi , φi )
and trivially on j̸=i Pj . These matrices are symplectic: write V∞ = Pi ⊕ Pi⊥ω with Pi⊥ω =
                        L
                                                          ⊥ω pointwise satisfies ω(T v, T w) = ω(v, w) when-
L
   j̸=i Pj ; a map T preserving Pi and fixing Pi
ever v, w lie in different summands (both sides vanish: ω(Pi , Pi⊥ω ) = 0 and T Pi = Pi ) or
both in Pi⊥ω (where T = id); and on the plane Pi a linear map preserves the nondegenerate
alternating form ω|Pi iff its determinant is 1 (for 2 × 2 matrices, ω(T v, T w) = det T · ω(v, w)).
        (i)
So SL2 ≤ L, and it is closed in L (cut out by the linear conditions fixing the complement and
                                                                                          (j)
preserving Pi , together with det = 1 on the Pi -block). For j ∈ {1, 2} let Pi ≤ V be the copy
of Pi in the j-th summand of V = V∞ ⊕ V∞ , and set
                                              (j)       (i)   (j)
                                            Σi      := SL2 ⋉Pi       ≤ G,
                                (j)         (i)                     (j)       (i)                               (i)
i.e. the closed subgroup Pi ⋊ SL2 = {(v, l) : v ∈ Pi , l ∈ SL2 } (a subgroup because SL2
             (j)
preserves Pi ; closed as a product of closed sets in V × L). The map
                              2      (j)                      (j)    (j)
                                               (x, y), T 7→ xεi + yφi , T (i)
                                                                             
                 SL2 (k∞ ) ⋉ k∞ −→ Σi ,
                    (i)                                       (j)    (j)
(where T (i) ∈ SL2 is T in the basis (εi , φi ), and εi , φi are the copies in leg j) is an isomor-
phism of topological groups carrying k∞  2 onto P (j) : it is a homeomorphism by construction,
                                                     i
                                        (i)               (j)
and a homomorphism because the SL2 -action on Pi is the standard action in the chosen
basis. Thus by [BHV-SL2] and invariance of relative property (T) under isomorphism of pairs
                    (j)   (j)
(§2.2), each pair (Σi , Pi ) has relative property (T).
Proposition 8.4. G has property (T).
                                             (j)
Proof. The 2g closed subgroups Pi ≤ V ≤ G (1 ≤ i ≤ g, j ∈ {1, 2}) satisfy: V is their
setwise product in any fixed order, each element of V being the sum of its components in the
                     L       (j)                                          (j)
decomposition V =      i,j Pi    — a product of r = 2g elements. Each Pi is normal in the
                      (j)             (j)   (j)
closed subgroup Σi , and (Σi , Pi ) has relative property (T) as just shown. By Lemma 8.2,
(G, V ) has relative property (T). The quotient G/V is topologically isomorphic to L (the map
(v, l) 7→ l is a continuous open surjective homomorphism with kernel V ), and L = Sp2g (k∞ ) has
property (T) by [BHV-HR] (g ≥ 2, k∞ a local field). By Lemma 8.3, G has property (T). □
24                  NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

8.3 G0 is a lattice in G. The subgroup A = R4g is discrete in V (coordinatewise: R is
discrete in k∞ , §3), and D0 := m4g is a compact exact fundamental domain for A in V :
every v ∈ V decomposes uniquely as v = δ + w with δ ∈ A, w ∈ D0 (the splitting k∞ =
R ⊕ m, coordinatewise); also Haar(D0 ) = 1. The subgroup H is discrete in L: if γ ∈ H, the
neighborhood {l ∈ L : l − γ ∈ M2g (m)} meets M2g (R) ⊇ H only in γ (two matrices over R
differing by a matrix over m are equal, since R ∩ m = 0). Hence G0 = A ⋊ H is a discrete
subgroup of G: as a subset of V × L it is the product A × H of two discrete subsets, which
is discrete in the product topology — and the topology of G is the product topology. By
Lemma 2.2(iii), G0 is closed in G and the quotient G/G0 is a locally compact Hausdorff second
countable space. By [HB] (applied to G = Sp2g ) there is an L-invariant Borel probability
measure ν on L/H. We record that supp ν = L/H, i.e. every nonempty open subset of L/H
has positive ν-measure. Indeed, fix a countable base {Bi } of the second countable space L/H
and let N be the union of those Bi with ν(Bi ) = 0: then ν(N ) = 0 (countable subadditivity),
N contains every open null set, and supp ν := (L/H) ∖ N is closed and nonempty (ν ̸= 0).
For l ∈ L, left translation by l is a homeomorphism preserving ν, so it maps open null sets to
open null sets; hence it preserves N and supp ν. Thus supp ν is a nonempty closed L-invariant
subset of the transitive L-space L/H, so it is everything.
Lemma 8.5 (two-domain identity). Let h : V → C be Borel, A-periodic (h(v + δ) = h(v)
for δ ∈ A), and either nonnegative or bounded.R Then Rfor any two Borel exact fundamental
domains F, F ′ of A in V of finite Haar measure, F h = F ′ h (both integrals being defined, and
absolutely convergent in the bounded case).

Proof. The sets F ∩ (F ′ + δ), δ ∈ A, are pairwise disjoint Borel sets with union F (existence
and uniqueness of the decomposition v = δ + w′ , w′ ∈ F ′ , for v ∈ F ), and likewise the sets
(F − δ) ∩ F ′ partition F ′ . By translation invariance of Haar measure and A-periodicity of h,
     Z       XZ                         XZ                         XZ               Z
        h=                    h(v) dv =              h(w + δ) dw =              h=       h.
                      ′                               ′                            ′    F′
      F      δ∈A F ∩(F +δ)               δ∈A (F −δ)∩F                 δ∈A (F −δ)∩F

For h ≥ 0 all terms are defined in [0, ∞] and the interchanges are countableP   additivity.
                                                                                  R           For
bounded h, apply the same computation to |h| first to see absolute convergence ( δ F ∩(F ′ +δ) |h| ≤
∥h∥∞ Haar(F ) < ∞), then to h.                                                                  □

Lemma 8.6. G0 is a lattice in G: the quotient G/G0 carries a nonzero finite G-invariant
Radon measure.

Proof. For F ∈ Cc (G/G0 ) define
                                         Z
                                                          
                             φF (l) :=        F (lv, l) G0 dv    (l ∈ L).
                                         D0

The map (l, v) 7→ F ((lv, l)G0 ) is continuous (composition of the continuous maps (l, v) 7→ (lv, l),
the open continuous projection G → G/G0 , and F ), so by compactness of D0 and uniform
continuity on compacta, φF is continuous; and |φF (l)| ≤ ∥F ∥∞ Haar(D0 ) = ∥F ∥∞ . For fixed
l, the function v 7→ F ((lv, l)G0 ) is A-periodic: (l(v + δ), l) = (lv, l)(δ, e) and (δ, e) ∈ G0 .
   Right H-invariance. For λ ∈ H: (lλv, lλ) = (lλv, l)(0, λ) with (0, λ) ∈ G0 , so F ((lλv, lλ)G0 ) =
F ((lλv, l)G0 ); substituting v ′ = λv (Haar-preserving, Lemma 3.3) gives
                                 Z                       Z
                                                               F (lv ′ , l)G0 dv ′ .
                                                                            
                      φF (lλ) =      F (lλv, l)G0 dv =
                                 D0                        λD0
                        NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                         25

Now λD0 is again a Borel exact fundamental domain for A (λ is a bijection of V with λA = A,
so v ∈ λδ + λD0 uniquely, and λA = A reindexes), of measure 1; by Lemma 8.5 (bounded
case) the last integral equals φF (l). Hence φF descends to a continuous function φ̇F on L/H
(L → L/H is open).
   Compact support. supp F is a compact subset of G/G0 , hence (Lemma 2.2(iii)) the image of
a compact K ⊂ G; enlarging K, we may take K = KV ×KL with KV ⊂ V , KL ⊂ L compact. If
φF (l) ̸= 0 then (lv, l)G0 ∈ supp F for some v ∈ D0 , so (lv, l) = (kV , kL )(δ, h) for some kV ∈ KV ,
kL ∈ KL , (δ, h) ∈ G0 ; comparing second coordinates, l = kL h, i.e. lH ∈ {kH : k ∈ KL }, a
compact subset of L/H (continuous image of KL ). RSo φ̇F ∈ Cc (L/H).
   The functional and its measure. Define I(F ) := L/H φ̇F dν — defined since φ̇F ∈ Cc , with
|I(F )| ≤ ∥F ∥∞ since ν is a probability measure. I is linear and positive (F ≥ 0 ⇒ φF ≥ 0).
By the Riesz–Markov theorem [SF] on the locally compact     R         Hausdorff second countable space
G/G0 , there is a Radon measure m with I(F ) = F dm; and m(G/G0 ) = sup{I(F ) : F ∈
Cc , 0 ≤ F ≤ 1} ≤ 1 < ∞.
   G-invariance. Fix g0 = (v0 , l0 ) ∈ G; note (v0 , l0 )−1 = (l0−1 v0 , l0−1 ), since (v0 , l0 )(l0−1 v0 , l0−1 ) =
(v0 + v0 , e) = (0, e) in characteristic 2. Then
                  g0−1 (lv, l) = l0−1 v0 + l0−1 lv, l0−1 l = (l0−1 l)(v + l−1 v0 ), l0−1 l ,
                                                                                         

so, substituting w := v + l−1 v0 (a Haar-preserving translation),
                            Z                     Z
                                 −1
                                                            F ((l0−1 l)w, l0−1 l)G0 dw.
                                                                                  
           φF (g−1 ·) (l) =   F g0 (lv, l)G0 dv =
                 0
                              D0                             D0 +l−1 v0

The integrand is a bounded A-periodic Borel function of w (as before), and D0 + l−1 v0 is a
Borel exact fundamental domain of A (a translate of one); by Lemma 8.5 the integral equals the
one over D0 , which is φF (l0−1 l). Hence φ̇F (g−1 ·) (lH) = φ̇F (l0−1 lH) and, by L-invariance of ν,
                                                       0
I(F (g0−1 ·)) = I(F ). By uniqueness in Riesz–Markov, g0 · m = m: the measure m is G-invariant.
  Nontriviality. Fix any x0 = (v0 , l0 )G0 ∈ G/G0 and choose F ∈ Cc (G/G0 ), F ≥ 0, F (x0 ) = 1
(Urysohn on the locally compact Hausdorff space). Write l0−1 v0 = δ + v ∗ with δ ∈ A, v ∗ ∈ D0 .
Then
             (l0 v ∗ , l0 ) G0 ∋ (l0 v ∗ , l0 )(δ, e) = (l0 v ∗ + l0 δ, l0 ) = (l0 (l0−1 v0 ), l0 ) = (v0 , l0 ),
so (l0 v ∗ , l0 )G0 = x0 and the integrand of φF (l0 ) equals 1 at v = v ∗ ; by continuity, φF (l0 ) > 0.
Hence φ̇F > 0 on a nonempty open subset of L/H, and since supp ν = L/H, I(F ) > 0. So
m ̸= 0, and G0 is a lattice in G.                                                                      □

8.4 Property (T) for every Gf . Theorem 8.7. (i) G0 has property (T). (ii) M = L(G0 ) is
a II1 factor with property (T) in the sense of Connes–Jones. (iii) For every f ∈ R, the group
Gf has property (T). (iv) Every countable discrete group with property (T), in particular every
Gf , is finitely generated.
Proof. (i) G0 is a lattice in G (Lemma 8.6), and G has property (T) (Proposition 8.4); by
[BHV-Lat], G0 has property (T). (ii) G0 is ICC (Proposition 7.3), so M is a II1 factor (Lemma
2.6), and M = L(G0 ) has property (T) by the forward direction of [CJ]. (iii) Fix f . The
group Gf is ICC (Proposition 7.3), so L(Gf ) is a II1 factor, and L(Gf ) ∼
                                                                         = M by Theorem 6.7.
Property (T) in the sense of Connes–Jones is an invariant of the abstract ∗-isomorphism class
of a II1 factor: we recall that a II1 factor N has property (T) if there are a finite set F ⊂ N
and ε > 0 such that every Hilbert N -N -bimodule containing a unit vector ξ with ∥xξ − ξx∥ ≤ ε
for all x ∈ F contains a nonzero central vector (xη = ηx for all x ∈ N ); bimodules transport
along any ∗-isomorphism, so the notion is invariant. Hence L(Gf ) has property (T), and by
26                   NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

the converse direction
                  S      of [CJ], Gf has property (T). (iv) Let G be countable discrete with (T),
and write G =L n Fn with finite sets F1 ⊆ F2 ⊆ · · · , e ∈ F1 ; let Gn := ⟨Fn ⟩. The unitary
                       2
representation      n ℓ (G/Gn ) (quasi-regular representations) has a.i.v.: for finite Q ⊂ G and
any ε, pick n with Q ⊆ Fn ; the vector δeGn ∈ ℓ2 (G/Gn ) is fixed by every g ∈ Q (as gGn = Gn ).
By property (T) there is a nonzero invariant vector, hence some ℓ2 (G/Gn ) contains a nonzero
G-invariant vector ξ. Invariance means ξ is constant on the G-orbits in G/Gn ; the action is
                                                                2
                                                             S ℓ only if [G : Gn ] < ∞. Choosing
transitive, so ξ is a nonzero constant function, which lies in
coset representatives t1 , . . . , tk of Gn in G, we get G = i ti Gn = ⟨Fn ∪ {t1 , . . . , tk }⟩: G is
finitely generated.                                                                                 □

                        9. Faithfulness of the ladder: AnnR (κ) = 0
   Throughout this section fix α ∈ {1, . . . , g} and let E := Eαα ∈ Symg (R) be the corresponding
diagonal matrix unit. For u ∈ R define
                                                                                         
        νu := yuE ∈ H,        νu (v1 , v2 ) = v1 , u(v1 )α eα + v2     v = (v1 , v2 ) ∈ V∞ ;
νu is symplectic by Lemma 7.1 (uE is symmetric). Clearly νu νu′ = νu+u′ , and u 7→ νu is
injective (νu (eα , 0) = (eα , ueα ) determines u). Thus
                              Nα := {νu : u ∈ R} ≤ H,    Nα ∼
                                                            = (R, +),
an infinite elementary abelian 2-group (νu2 = ν2u = ν0 = e).
9.1 An explicit normalized family over Nα . For u ∈ R define bu : k∞ × k∞ → {±1},
bu (y, z) := ψ(uyz): a continuous, symmetric, {±1}-valued bicharacter of k∞ . It is trivial on
R × R (for y, z ∈ R, uyz ∈ R ⊆ ker ψ), so the constant function 1 is a second-degree character
for bu |R×R . For u ̸= 0 set Nu := ⌈(deg u + 2)/2⌉ ≥ 1 and C0 := B−Nu ; then for y, z ∈ C0
we have uyz ∈ tdeg u−2Nu O ⊆ t−2 O ⊆ ker ψ (as deg u − 2Nu ≤ −2), so bu |C0 ×C0 ≡ 1; and
R ∩ C0 = 0 since Nu ≥ 1. By Lemma 5.1 (with U = k∞ , B = R, hB ≡ 1) choose, once and for
all for each u ∈ R ∖ {0}, a second-degree character
               hu : k∞ → µ4 ,        hu (y + z) = hu (y) hu (z) ψ(uyz),       hu |R ≡ 1,
and set h0 := 1 (a second-degree character for b0 ≡ 1, trivial on R). Define
                                    g
           fu (x) := hu (xα ) (x ∈ k∞ ),        Vν′′u := mfu (multiplication by fu on H),
a unitary (fu is continuous with |fu | ≡ 1); note Vν′′0 = 1.
Lemma 9.1. For every u ∈ R, the pair cu , Vν′′u , where cu (v) := hu (s) ψ(us2 ) with s := (v1 )α ,
                                                  

is a normalized intertwining pair for νu (in the sense of §5.2–5.3).
Proof. Let ξ ∈ H and v = (v1 , v2 ), s = (v1 )α . Using (4.1) and m∗fu = mfu :
                mfu uv m∗fu ξ (x) = fu (x) ψ(⟨x + v1 , v2 ⟩) fu (x + v1 ) ξ(x + v1 ).
                             

By the second-degree identity, hu (xα + s) = hu (xα )hu (s)ψ(uxα s), so
                fu (x) fu (x + v1 ) = hu (xα ) hu (xα ) hu (s) ψ(uxα s) = hu (s) ψ(uxα s)
(ψ is {±1}-valued, so ψ(·) = ψ(·)). On the other hand νu v = (v1 , useα + v2 ), so by (4.1)
                                                                  
   (uνu v ξ)(x) = ψ ⟨x + v1 , useα + v2 ⟩ ξ(x + v1 ) = ψ us(xα + s) ψ(⟨x + v1 , v2 ⟩) ξ(x + v1 ).
                                                                            
Comparing the two displays: with χu,v (x) := hu (s) ψ(uxα s) ψ us(xα + s) (a function of x),
we get mfu uv m∗fu = mχu,v uνu v ; and the x-dependent factors cancel,
             χu,v (x) = hu (s) ψ(uxα s) ψ(usxα ) ψ(us2 ) = hu (s) ψ(us2 )              g
                                                                                 (x ∈ k∞ ),
                       NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                    27


using ψ(·) = ψ(·) and ψ(uxα s)ψ(usxα ) = 1. So mfu uv m∗fu is the constant cu (v) = hu (s)ψ(us2 )
times uνu v . The function cu is continuous (hu , ψ and v 7→ (v1 )α are), so (cu , Vν′′u ) is an
intertwining pair for νu . It is normalized: for n ∈ S we have s = (n1 )α ∈ R, so hu (s) = 1 and
us2 ∈ R ⊆ ker ψ, giving cu (n) = 1, i.e. Vν′′u un Vν′′u∗ = uνu n .                             □


Lemma 9.2. For u, u′ ∈ R put gu,u′ := hu hu′ hu+u′ : k∞ → T. Then: (i) gu,u′ is a continuous
character of k∞ , trivial on R; hence there is a unique ρ(u, u′ ) ∈ R with gu,u′ = ψ ρ(u, u′ ) · .
                                                                                                

(ii) ρ is symmetric with ρ(u, 0) = ρ(0, u) = 0, and
            Vν′′u Vν′′u′ = uD(u,u′ ) Vν′′u+u′ , D(u, u′ ) := 0, ρ(u, u′ ) eα ∈ S = Rg ⊕ Rg .
                                                                            


(iii) D is a normalized cocycle in Z 2 (Nα , S) and

                                      resH             2
                                         Nα κ = [D] ∈ H (Nα , S).

Proof. (i) For y, z ∈ k∞ , using the second-degree identity for each of hu , hu′ , hu+u′ and ψ(·) =
ψ(·):

gu,u′ (y+z) = hu (y)hu (z)ψ(uyz)·hu′ (y)hu′ (z)ψ(u′ yz)·hu+u′ (y) hu+u′ (z) ψ (u+u′ )yz = gu,u′ (y) gu,u′ (z);
                                                                                       

so gu,u′ is a continuous character, trivial on R because all three factors are. By Lemma 3.1(iii)
it equals ψ(w ·) for a unique w ∈ k∞ , and triviality on R forces w ∈ R⊥ = R (Lemma 3.1(i)).
   (ii) Symmetry is clear, and gu,0 = hu · 1 · hu = 1 gives ρ(u, 0) = 0. Multiplication operators
compose exactly:
        Vν′′u Vν′′u′ = mfu fu′ , fu (x)fu′ (x) = gu,u′ (xα ) hu+u′ (xα ) = ψ ρ(u, u′ ) xα fu+u′ (x).
                                                                                         

Finally mψ(ρ (·)α ) = Mρeα = u(0,ρeα ) by (4.1) (no translation part; ψ(⟨x, ρeα ⟩) = ψ(ρxα )). Hence
Vν′′u Vν′′u′ = u(0,ρ(u,u′ )eα ) Vν′′u+u′ .
    (iii) The family {(cu , Vν′′u )}u∈R , indexed by Nα ∼= (R, +) via u 7→ νu , is a family of normalized
                                     ′′
intertwining pairs with Vν0 = 1 (Lemma 9.1). By (ii) and the uniqueness clause of Proposition
5.5(i) (applied over the subgroup Nα ), the associated cocycle of this family is exactly D (with
scalar part µ ≡ 1). By Proposition 5.5(iv), D ∈ Z 2 (Nα , S) is a normalized cocycle and
[D] = κNα = resH                                                                        ′ ′′               ′
                       Nα κ. (Concretely, the cocycle identity for D reads νu D(u , u ) + D(u, u +
u′′ ) = D(u + u′ , u′′ ) + D(u, u′ ); since D takes values in {0} ⊕ Reα and νu (0, reα ) = (0, reα )
— the action fixes vectors with vanishing first block — this amounts to the scalar identity
ρ(u′ , u′′ )+ρ(u, u′ +u′′ ) = ρ(u+u′ , u′′ )+ρ(u, u′ ), which also follows directly from gu′ ,u′′ gu,u′ +u′′ =
gu+u′ ,u′′ gu,u′ , an identity immediate from the definition of g.)                                          □

P The i half-Frobenius Weil index. In characteristic 2, squaring is additive. For x =
9.2
  i≤N xi t ∈ k∞ ,
                                     X
                                x2 =     x2i t2i :
                                                    i≤N

the coefficient of tn in x2 is the finite sum i+j=n xi xj , in which the off-diagonal terms cancel in
                                               P

pairs (xi xj + xj xi = 0), leaving x2n/2 for even n and 0 for odd n. Recall also that the Frobenius
a 7→ a2 is an automorphism of Fq (additive in characteristic 2 since (a + b)2 = a2 + b2 ,
multiplicative,
√                injective since a2 = 0 forces a = 0, hence bijective on the finite set Fq ); write
  · for its inverse.
28                   NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

                                   k
                       P
Definition. For u =        k≥0 uk t ∈ R set
                                       r
                                           du    X √
                             D(u) :=          :=     uk t(k−1)/2 ∈ R.
                                           dt
                                                   k odd

                                                                k−1 =             k−1 , with all
                                                      P               P
(In characteristic 2 the formal√derivative is du/dt =   k kuk t         k odd uk t
exponents even, and applying · to its coefficients and halving exponents yields the displayed
polynomial, whose square is du/dt.) Note
                                       D(1) = 0,            D(t) = 1.

Proposition 9.3 (half-Frobenius identity). For every u ∈ R: ρ(u, u) = D(u). Equiv-
              2
alently, Vν′′u = u(0, D(u)eα ) : the square of the metaplectic unipotent Vν′′u is the lattice Weyl
                          p
operator of the vector (0, du/dt eα ). In particular ρ(u, u) does not depend on the choice of
the characters hu .

Proof. Since 2u = 0 we have h2u = h0 = 1, so gu,u = h2u . The second-degree identity at z = y
gives 1 = hu (0) = hu (2y) = hu (y)2 ψ(uy 2 ), i.e.

                                  hu (y)2 = ψ(uy 2 )          (y ∈ k∞ ),
using ψ(·)−1 = ψ(·). Thus gu,u (y) = ψ(uy 2 ), and by the uniqueness in Lemma 9.2(i) it suffices
to prove
                                ψ(uy 2 ) = ψ D(u) y
                                                    
                                                         (y ∈ k∞ ).
                        i                                    2              k
             P                                                      P          P 2 2i 
Write y =       i≤N yi t . By the additivity of squaring, uy =        k uk t     i yi t  , and the
                −1
coefficient of t collects the finitely many pairs with k+2i = −1, i.e. k odd and i = −(k+1)/2:
                                  X                    X √                 2
                            2              2
                     res(uy ) =        uk y−(k+1)/2 =          uk y−(k+1)/2 ,
                                 k odd                        k odd

the last equality again by additivity of squaring, now in Fq . Hence, using first the definition
ψ = ψ0 ◦ res and then thePFrobenius-invariance  (3.1) of the trace character ψ0 — i.e. ψ0 (c2 ) =
                               √
ψ0 (c), applied with c = k odd uk y−(k+1)/2 ∈ Fq —
                                                         X √                
                       2             2          2
                                       
                 ψ(uy ) = ψ0 res(uy ) = ψ0 (c ) = ψ0             uk y−(k+1)/2 .
                                                                  k odd
                                              P √
                                                    uk yi t(k−1)/2+i , and the coefficient of t−1 collects
                                  P
On the other hand, D(u) y =           k odd    i
i = −(k + 1)/2:
                                           X √
                                res D(u)y =     uk y−(k+1)/2 .
                                                    k odd

So ψ(uy 2 ) = ψ(D(u)y) for all y, as required. The final sentence holds because D(u) is defined
without reference to hu .                                                                    □

   (In characteristic 0, the square of a metaplectic lift of a unipotent differs from the lift of its
square by a scalar — a Weil index. Proposition p 9.3 says that in characteristic 2 this pscalar has
become a lattice translation, by the vector (0, du/dt eα ) ∈ S — whose entry D(u) = du/dt ∈
R is unbounded as u ranges over R. This is the engine of the whole separation argument.)
                     NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                29

9.3 Nonvanishing. Theorem 9.4. For every f ∈ R ∖ {0} we have f κ ̸= 0 in H 2 (H, S).
Hence AnnR (κ) = 0 and the map R → H 2 (H, S), f 7→ f κ, is injective.
Proof. Suppose f κ = 0. Restriction resH
                                       Nα is R-linear (§2.1), so by Lemma 9.2(iii),

                         0 = resH                            2
                                Nα (f κ) = f [D] = [f D] in H (Nα , S).

Identify Nα = (R, +) via u 7→ νu . Then there is a map σ = (σ1 , σ2 ) : R → S = Rg ⊕ Rg with
f D(u, v) = νu σ(v)−σ(u+v)+σ(u)            (u, v ∈ R),     where νu (s1 , s2 ) = (s1 , u(s1 )α eα +s2 ).
Write ϕ := (σ1 )α : R → R and s := (σ2 )α : R → R for the α-coordinates. Taking the
α-coordinate of the second block of the displayed equation (the second block of νu σ(v) is
u(σ1 (v))α eα + σ2 (v), and the second block of f D(u, v) is f ρ(u, v)eα ):
                   f ρ(u, v) = u ϕ(v) + s(v) − s(u + v) + s(u)        (u, v ∈ R).                   (⋆)
Symmetry. The left-hand side of (⋆) is symmetric in (u, v) (Lemma 9.2(ii)), and so is the part
s(v) − s(u + v) + s(u); subtracting the instance of (⋆) with u, v interchanged therefore yields
u ϕ(v) = v ϕ(u) for all u, v ∈ R. Setting u = 1: ϕ(v) = r0 v with r0 := ϕ(1) ∈ R. Diagonal.
Taking u = v = 0 in (⋆) gives 0 = s(0). Now take v = u in (⋆): since R has characteristic 2,
s(v) + s(u) = 2s(u) = 0 and s(u + v) = s(2u) = s(0) = 0, so, using Proposition 9.3,
                                f D(u) = r0 u2       for all u ∈ R.
At u = 1: D(1) = 0, so r0 = 0 (R is a domain and 12 = 1). At u = t: D(t) = 1, so f = r0 t2 = 0
— contradicting f ̸= 0.                                                                     □
   (Characteristic 2 enters exactly twice: over an exponent-2 module the diagonal of the cobound-
ary part of a symmetric cocycle equation collapses to the Frobenius-square
                                                                    p        form r0 u2 ; and the
half-Frobenius D exists. The two one-parameter families u 7→ f du/dt and u 7→ r0 u2 are
transverse: they agree for all u only when f = r0 = 0.)

             10. Separation: each isomorphism class is finite in the family
  Throughout this section, f, f ′ ∈ R and Ψ : Gf → Gf ′ denotes a group isomorphism. We
show (Theorem 10.15) that for fixed f there are at most q(q − 1)2 s elements f ′ ∈ R with
Gf ′ ∼
     = Gf .

10.1 Transvections and abelian normal subgroups of symplectic groups in charac-
teristic 2. Let K ⊇ R be an infinite field of characteristic 2 — we fix K := Fq (t) — and extend
ω to K2g by the same formula. For 0 ̸= v ∈ K2g and λ ∈ K, the transvection
                                    Tv,λ (x) := x + λ ω(x, v) v
satisfies:
                                                                        −1
Lemma 10.1. (i) Tv,λ ∈ Sp2g (K); (ii) Tv,λ Tv,λ′ = Tv,λ+λ′ , Tv,0 = 1, Tv,λ = Tv,λ ; (iii)
gTv,λ g −1 = Tgv,λ for g ∈ Sp2g (K); (iv) Tµv,λ = Tv,λµ2 for µ ∈ K× .

Proof. (i) ω(T x, T y) = ω(x, y) + λω(x, v)ω(v, y) + λω(y, v)ω(x, v) + λ2 ω(x, v)ω(y, v)ω(v, v) =
ω(x, y), using ω(v, v) = 0 and symmetry ω(v, y) = ω(y, v) with characteristic 2. (ii) Tv,λ Tv,λ′ x =
x + λ′ ω(x, v)v + λω(x + λ′ ω(x, v)v, v)v = x + (λ + λ′ )ω(x, v)v (again ω(v, v) = 0); and Tv,λ2 =

Tv,2λ = 1. (iii) gTv,λ g −1 x = g g −1 x + λω(g −1 x, v)v = x + λω(x, gv)gv. (iv) Immediate from
                                                         
the formula.                                                                                       □
30                     NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

  Let U + (K) := {xb : b ∈ Symg (K)} and U − (K) := {yc : c ∈ Symg (K)} (Lemma 7.1 over K),
               
and w0 := I0 I0 (symplectic: it swaps the two blocks, and ω is symmetric under this swap).
Lemma 10.2. Let Γ1 := ⟨U + (K) ∪ U − (K)⟩ ≤ Sp2g (K). Then: (i) w0 = xI yI xI ∈ Γ1 ; (ii) for
every v1 ∈ Kg ∖ {0} and z ∈ Kg there is c ∈ Symg (K) with cv1 = z; (iii) Γ1 acts transitively
on K2g ∖ {0}; (iv) Γ1 contains every transvection Tv,λ (v ̸= 0, λ ∈ K).
Proof. (i) Block computation in characteristic 2:
                                                                 
              1 1    1 0        0 1                        0 1   1 1    0 1
    x I yI =                =         ,      (xI yI )xI =             =       = w0 .
              0 1    1 1        1 1                        1 1   0 1    1 0
(ii) Pick j with (v1 )j ̸= 0 and set µ := (v1 )−1     j . The symmetric matrices µEjj and µ(Emj + Ejm )
(m ̸= j) send v1 to ej and to em + µ(v1 )m ej respectively. Hence the image of the linear map
Symg (K) → Kg , c 7→ cv1 , contains ej and em + µ(v1 )m ej for all m ̸= j, hence contains
e1 , . . . , eg : it is all of Kg . (iii) Let (v1 , v2 ) ̸= 0. If v1 ̸= 0: choose c with cv1 = v2 (by (ii));
then yc (v1 , v2 ) = (v1 , cv1 + v2 ) = (v1 , 0). If v1 = 0: w0 (0, v2 ) = (v2 , 0) with v2 ̸= 0. So every
nonzero vector is Γ1 -equivalent to some (v1 , 0), v1 ̸= 0. Next, w0 (v1 , 0) = (0, v1 ), and choosing
b ∈ Symg with bv1 = e1 (by (ii)), xb (0, v1 ) = (bv1 , v1 ) = (e1 , v1 ); choosing c with ce1 = v1 ,
yc (e1 , v1 ) = (e1 , ce1 + v1 ) = (e1 , 0). Hence every nonzero vector is Γ1 -equivalent to (e1 , 0). (iv)
For v = (e1 , 0): ω(x, v) = ⟨x2 , e1 ⟩ = (x2 )1 , so T(e1 ,0),λ (x1 , x2 ) = (x1 + λ(x2 )1 e1 , x2 ) = xλE11 x,
i.e. T(e1 ,0),λ ∈ U + (K) ⊆ Γ1 . For general v ̸= 0, write v = g(e1 , 0) with g ∈ Γ1 (by (iii)); then
Tv,λ = gT(e1 ,0),λ g −1 ∈ Γ1 by Lemma 10.1(iii).                                                             □

Lemma 10.3 (key rigidity lemma). Let K be an infinite field of characteristic 2 and g ≥ 1.
Let N ≤ Sp2g (K) be an abelian subgroup normalized by every transvection. Then N = {1}.

Proof. Suppose 1 ̸= n ∈ N. First note that for any z with ω(z, nz) = 0 and any λ,
                                                          −1
                         mz,λ := [n, Tz,λ ] = n Tz,λ n−1 Tz,λ = Tnz,λ Tz,λ ∈ N,
                                                                             −1
by Lemma 10.1(ii),(iii); membership in N holds because mz,λ = n · Tz,λ n−1 Tz,λ
                                                                                
                                                                                  is a product
of two elements of N (N is normalized by Tz,λ ). The same formula [n, Tz,λ ] = Tnz,λ Tz,λ ∈ N
holds for arbitrary z ̸= 0 (no orthogonality needed for membership).
   Case 1: there is v with µ0 := ω(v, nv) ̸= 0. Put w := nv. Then v, w are linearly
independent (w = µv would force ω(v, w) = µ ω(v, v) = 0), and P := Kv + Kw is a symplectic
plane (ω|P is nondegenerate since ω(v, w) = µ0 ̸= 0). Both Tv,λ and Tw,λ fix P ⊥ω pointwise
(ω(x, v) = ω(x, w) = 0 there) and preserve P ; on P , in the basis (v, w), using ω(w, v) =
ω(v, w) = µ0 (symmetry!):
                                                        
                                1 a                     1 0
                    Tv,λ |P =         ,     Tw,λ |P =        ,   a := λµ0
                                0 1                    a 1
(e.g. Tv,λ v = v, Tv,λ w = w + λω(w, v)v = w + av). Hence
                                                                         
                                                       1 0   1 a     1   a
         mλ := [n, Tv,λ ] = Tw,λ Tv,λ ∈ N,   mλ |P =              =             .
                                                       a 1   0 1     a 1 + a2
For a ̸= b both nonzero, the (1, 2)-entries of ma mb |P and mb ma |P are a+b+ab2 and a+b+a2 b,
which differ because ab2 + a2 b = ab(a + b) ̸= 0. Since K is infinite, choose λ ̸= λ′ nonzero and
put a = λµ0 , b = λ′ µ0 : then mλ , mλ′ ∈ N do not commute (they agree on P ⊥ and differ on P )
— contradicting commutativity of N.
                       NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                    31

   Case 2: ω(v, nv) = 0 for all v. Polarizing (0 = ω(x + y, n(x + y)) = ω(x, ny) + ω(y, nx))
gives
                              ω(x, ny) = ω(y, nx)     (x, y).                         (10.1)
Replacing x by nx in (10.1) and using ω(nx, ny) = ω(x, y) (symplecticity) and symmetry of ω:
   ω(y, n2 x) = ω(nx, ny) = ω(x, y) = ω(y, x) ⇒ ω y, (n2 + 1)x = 0 ∀x, y ⇒ n2 = 1.
                                                               

So n is an involution; (n + 1)2 = n2 + 2n + 1 = 0, hence F := ker(n + 1) ⊇ im(n + 1), and
n ̸= 1 gives rank(n + 1) ≥ 1. (In particular n is not a nontrivial scalar: µ2 = 1 forces µ = 1 in
characteristic 2.)
   Subcase rank(n + 1) = 1. Write (n + 1)x = ℓ(x)u0 with u0 ̸= 0 and ℓ a nonzero linear
functional; nx = x + ℓ(x)u0 . From (n + 1)2 = 0: ℓ(x)ℓ(u0 )u0 = 0 for all x, so ℓ(u0 ) = 0.
Symplecticity of n: for all x, y,
 ω(x, y) = ω(nx, ny) = ω(x, y) + ℓ(y)ω(x, u0 ) + ℓ(x)ω(u0 , y) ⇒ ℓ(y)ω(x, u0 ) = ℓ(x)ω(y, u0 ),
using symmetry. Pick x0 with ℓ(x0 ) ̸= 0. If ω(x0 , u0 ) = 0, then ℓ(x0 )ω(y, u0 ) = 0 for all
y, forcing u0 = 0 (nondegeneracy) — absurd; so ω(x0 , u0 ) ̸= 0 and ℓ = λ0 ω(·, u0 ) with
λ0 := ℓ(x0 )/ω(x0 , u0 ) ̸= 0. Thus n = Tu0 ,λ0 , and then ω(x, nx) = λ0 ω(x, u0 )2 , which is nonzero
for suitable x — contradicting the Case-2 hypothesis.
   Subcase rank(n + 1) ≥ 2. Fix v ∈  / F and put w := nv ̸= v, u := (n + 1)v = v + w ∈ F ∖ {0};
note ω(v, w) = ω(v, nv) = 0, and w ∈   / Kv: if nv = µv then v = n2 v = µ2 v gives µ2 = 1, µ = 1,
w = v — excluded. Also (n + 1)w = (n2 + n)v = (1 + n)v = u.
   Choose z with
                                 ω(z, v) ̸= 0 and (n + 1)z ∈    / Ku.
Existence: since rank(n + 1) ≥ 2, im(n + 1) ̸⊆ Ku, so there is z2 with (n + 1)z2 ∈         / Ku; by
nondegeneracy there is z1 with ω(z1 , v) ̸= 0. If z2 also has ω(z2 , v) ̸= 0, take z = z2 ; if z1 also
has (n + 1)z1 ∈/ Ku, take z = z1 ; otherwise ω(z2 , v) = 0 and (n + 1)z1 ∈ Ku, and z := z1 + z2
has ω(z, v) = ω(z1 , v) ̸= 0 and (n + 1)z = (n + 1)z1 + (n + 1)z2 ∈   / Ku.
   Claim: v, w, z, nz are linearly independent. First, z ∈ / Kv + Kw: on that plane (n + 1) has
image Ku (as (n + 1)v = (n + 1)w = u), while (n + 1)z ∈      / Ku. So v, w, z are independent (v, w
independent as shown). Suppose nz = αv+βw+γz. Applying n (with nv = w, nw = n2 v = v):
z = n2 z = αw + βv + γnz = αw + βv + γ(αv + βw + γz), i.e. (1 + γ 2 )z = (β + γα)v + (α + γβ)w.
Independence of v, w, z forces γ 2 = 1, so γ = 1, and then β = α (coefficients: β + α = 0).
Hence (n + 1)z = nz + z = αv + αw = αu ∈ Ku — contradiction. So no such dependence exists
and v, w, z, nz are independent.
   Now, since ω(x, nx) ≡ 0, both z and v satisfy the orthogonality needed for the commutator
formula with cross terms killed: for any z ′ with ω(z ′ , nz ′ ) = 0,
              mz ′ ,λ = Tnz ′ ,λ Tz ′ ,λ = 1 + λQz ′ ,   Qz ′ x := ω(x, z ′ )z ′ + ω(x, nz ′ ) nz ′ ,
because Tnz ′ ,λ Tz ′ ,λ x = x + λω(x, z ′ )z ′ + λω x + λω(x, z ′ )z ′ , nz ′ nz ′ and the cross term carries
                                                                              

the factor ω(z ′ , nz ′ ) = 0. Apply this with z ′ = v (Q := Qv , Qv x = ω(x, v)v + ω(x, w)w, as
nv = w) and z ′ = z (Qz ): for all λ, λ′ ∈ K,
 1 + λQv , 1 + λ′ Qz ∈ N ⇒ (1 + λQv )(1 + λ′ Qz ) = (1 + λ′ Qz )(1 + λQv ) ⇒ Qv Qz = Qz Qv
(take λ = λ′ = 1 and expand: 1 + P + Q + P Q = 1 + Q + P + QP ). Write a(x) := ω(x, v),
b(x) := ω(x, w), c(x) := ω(x, z), d(x) := ω(x, nz) and p := ω(z, v), p′ := ω(z, w), r := ω(nz, v),
r′ := ω(nz, w). Using symmetry of ω:
Qv Qz x = c(x) pv + p′ w + d(x) rv + r′ w ,       Qz Qv x = a(x) pz + r nz + b(x) p′ z + r′ nz .
                                                                                             
32                   NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

The functionals a, b, c, d are linearly independent (they are ω-pairings against the independent
vectors v, w, z, nz, and ω is nondegenerate), so there is x with (a, b, c, d)(x) = (1, 0, 0, 0). For
this x: Qv Qz x = 0 while Qz Qv x = pz+r nz; independence of z, nz forces p = 0 — contradicting
p = ω(z, v) ̸= 0.                                                                                 □

10.2 Abelian normal subgroups of H and of Gf . Lemma 10.4 (polynomial density).
Let K be a field, R0 ⊆ K an infinite subset, and P ∈ K[X1 , . . . , Xm ] a polynomial vanishing on
R0m . Then P = 0.
Proof. Induction on m. For m = 1: a nonzero one-variable polynomial P has at most deg P
roots (each root c splits off a factor: division with remainder gives P = (X1 − c)Q + P (c) =
(X1 − c)Q with deg Q < deg P ; induct), but P vanishes on the infinite set R0 . For m > 1:
                                     j
                                       ; for each fixed (x1 , . . . , xm−1 ) ∈ R0m−1 the one-variable
           P
write P = j Pj (X1 , . . . , Xm−1 )Xm
            P           j
polynomial j Pj (x)Xm vanishes on R0 , hence all Pj (x) = 0; by induction each Pj = 0.             □
                                           2
   We consider Sp2g (K) ⊆ M2g (K) = A4g (K) with the Zariski topology (closed sets = common
zero sets of polynomials in the matrix entries). For fixed h, the maps x 7→ hx, x 7→ xh,
x 7→ hxh−1 and x 7→ x−1 = J −1 xT J (on Sp2g ) are polynomial with polynomial inverses, hence
Zariski-homeomorphisms of Sp2g (K). (We never need joint continuity of multiplication, which
fails for the Zariski topology; all arguments below use one variable at a time.)
Lemma 10.5. Let N ≤ Sp2g (K) be a subgroup and N := N its Zariski closure. (i) N is
a subgroup. (ii) If N is abelian, so is N. (iii) The set Nor := {x ∈ Sp2g (K) : xNx−1 ⊆
N and x−1 Nx ⊆ N} is a Zariski-closed subgroup, and it contains every h with hN h−1 = N .
Proof. (i) Inversion is a homeomorphism mapping N onto N , so N−1 = N −1 = N. For n ∈ N :
left translation by n is a homeomorphism mapping N into N , so nN = nN ⊆ N. Thus N N ⊆
N; now for y ∈ N: right translation by y maps N into N (just shown), so Ny = N y ⊆ N = N.
Hence NN ⊆ N. (ii) For fixed n ∈ N , the centralizer C(n) = {x : xn = nx} is Zariski closed
(linear equations in x) and contains N , hence contains N: every y ∈ N commutes with every
n ∈ N . So for fixed y ∈ N, C(y) is closed and contains N , hence contains N. (iii) For fixed
m ∈ N, {x : xmx−1 ∈ N} is closed (the map x 7→ xmx−1 = xm J −1 xT J is polynomial;
preimage of the closed set N), and similarly for x−1 mx; Nor is the intersection over m ∈ N of
these closed sets. It is a subgroup: it is symmetric (x ∈ Nor ⇔ x−1 ∈ Nor by construction)
and closed under products (xy m (xy)−1 = x(ymy −1 )x−1 ∈ xNx−1 ⊆ N, and likewise for the
inverse condition). If hN h−1 = N then, conjugation by h being a homeomorphism, hNh−1 =
hN h−1 = N, so h ∈ Nor.                                                                     □

Proposition 10.6. (i) Every abelian normal subgroup of H = Sp2g (R) is trivial. (ii) For every
f ∈ R: the subgroup A ⊴ Gf is abelian and normal, and every abelian normal subgroup of Gf
is contained in A. Consequently every isomorphism Ψ : Gf → Gf ′ satisfies Ψ(A) = A.
Proof. (i) Let N̄ ⊴ H be abelian, and N its Zariski closure inside Sp2g (K), K = Fq (t). By
Lemma 10.5, N is an abelian subgroup and the closed subgroup Nor contains H (normality
of N̄ in H). We claim Nor ⊇ U ± (K): the set U + (K) is Zariski closed in M2g (K) and the
parametrization Symg (K) ∼  = Kg(g+1)/2 → U + (K), b 7→ xb , is linear in the entries with linear
inverse; hence a Zariski-closed subset of Sp2g (K) containing U + (R) = {xb : b ∈ Symg (R)}
contains U + (K), because a polynomial in the entries of b vanishing on Symg (R) — i.e. on
Rg(g+1)/2 — vanishes identically (Lemma 10.4, R infinite). Since U + (R) ⊆ H ⊆ Nor and Nor
is closed, U + (K) ⊆ Nor; likewise U − (K) ⊆ Nor. As Nor is a subgroup, Γ1 = ⟨U ± (K)⟩ ⊆ Nor,
                       NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                     33

so by Lemma 10.2(iv) every transvection normalizes N. By Lemma 10.3, N = {1}, hence
N̄ = {1}.
   (ii) A is abelian normal in Gf (§2.1). Let N ⊴ Gf be abelian, and let p : Gf → H be the
projection. Then p(N ) is an abelian normal subgroup of H (images of normal subgroups under
surjections are normal; of abelian, abelian), hence trivial by (i); so N ⊆ ker p = A. For the
consequence: Ψ(A) is an abelian normal subgroup of Gf ′ , so Ψ(A) ⊆ A; applying the same to
Ψ−1 gives Ψ−1 (A) ⊆ A, i.e. A ⊆ Ψ(A).                                                      □

10.3 The Eilenberg–MacLane class equation. Lemma 10.7 (class equation). Let Q be
a group, let B, B ′ be Q-modules, and let c ∈ Z 2 (Q, B), c′ ∈ Z 2 (Q, B ′ ) be normalized cocycles.
Let Ψ : B ×c Q → B ′ ×c′ Q be an isomorphism with Ψ(B) = B ′ (identifying B ∼           = B × {e}
etc.). Then: (i) Ψ(a, e) = (αa, e) for a group isomorphism α : B → B ′ , and there are a map
t : Q → B ′ and a bijection β : Q → Q with Ψ(0, γ) = (tγ , βγ); β is a group automorphism of
Q and te = 0. (ii) Compatibility: α(γa) = β(γ) α(a) for all γ ∈ Q, a ∈ B — i.e. α : B → Bβ′
is a Q-module isomorphism, where Bβ′ denotes B ′ with the twisted action γ ∗ b := β(γ)b. (iii)
For all γ, γ ′ ∈ Q:
                         α c(γ, γ ′ ) = c′ (βγ, βγ ′ ) + β(γ)tγ ′ − tγγ ′ + tγ .
                                     

Consequently α∗ [c] = β ∗ [c′ ] in H 2 (Q, Bβ′ ), where α∗ [c] := [α ◦ c] and β ∗ [c′ ] := [c′ ◦ (β × β)]. Both
operations are well defined on cohomology: α ◦ c and c′ ◦ (β × β) are cocycles for the twisted
action (see the proof ), and coboundaries map to twisted coboundaries — α ◦ ∂n = ∂β (α ◦ n) by
(ii), and (∂n′ ) ◦ (β × β) = ∂β (n′ ◦ β) by substitution, where ∂β is the coboundary for the action
γ ∗ b = β(γ)b. In particular α∗ : H 2 (Q, B) → H 2 (Q, Bβ′ ) is an isomorphism, with inverse
(α−1 )∗ defined analogously through the compatibility α−1 (β(γ)b) = γ α−1 (b).
Proof. (i) Ψ restricted to the subgroup B is an isomorphism onto B ′ , written α. Let p : B×c Q →
Q and p′ : B ′ ×c′ Q → Q be the projections (homomorphisms, §2.1). The composite p′ ◦ Ψ is a
surjective homomorphism killing B = ker p (as Ψ(B) = B ′ = ker p′ ), so there is a unique map
β : Q → Q with β ◦ p = p′ ◦ Ψ, and β is a surjective homomorphism. It is injective: if β(γ) = e
then Ψ(0, γ) ∈ ker p′ = B ′ , so (0, γ) ∈ Ψ−1 (B ′ ) = B, forcing γ = e. Thus β ∈ Aut(Q), and
Ψ(0, γ) = (tγ , βγ) for some tγ ∈ B ′ . Finally Ψ(0, e) = (0, e) (Ψ maps the unit to the unit) gives
te = 0. (ii) Apply Ψ to the conjugation identity (2.1): Ψ (0, γ)(a, e)(0, γ)−1 = Ψ(γa, e) =
(α(γa), e); on the other hand it equals (tγ , βγ)(αa, e)(tγ , βγ)−1 = (β(γ)α(a), e), again by (2.1)
in the target group. (iii) Apply Ψ to (0, γ)(0, γ ′ ) = (c(γ, γ ′ ), γγ ′ ) = (c(γ, γ ′ ), e)(0, γγ ′ ):
                      (tγ , βγ)(tγ ′ , βγ ′ ) = tγ + β(γ)tγ ′ + c′ (βγ, βγ ′ ), β(γγ ′ )
                                                                                         

must equal Ψ(c(γ, γ ′ ), e) Ψ(0, γγ ′ ) = α(c(γ, γ ′ )) + tγγ ′ , β(γγ ′ ) . Comparing B ′ -components
                                                                            

gives the displayed identity; it says precisely that the twisted-action cocycles α◦c and c′ ◦(β ×β)
differ by the twisted coboundary ∂t (for the action γ ∗ b = β(γ)b, under which both are indeed
cocycles: for α ◦ c use (ii) and the cocycle identity for c; for c′ ◦ (β × β) substitute β’s into the
identity for c′ ).                                                                                       □
  Applying Lemma 10.7 to Ψ : Gf → Gf ′ (legitimate by Proposition 10.6: Ψ(A) = A), with
B = B ′ = A, c = f d, c′ = f ′ d, we obtain α ∈ Aut(A), β ∈ Aut(H) with
                                             α(γ̂a) = βγ
                                                      c α(a),                                           (10.2)
                                   α∗ [f d] = β ∗ [f ′ d] in H 2 (H, Aβ ).                              (10.3)

Corollary 10.8. If f ̸= 0 then Gf ∼
                                  ̸ G0 .
                                   =
34                    NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

Proof. Suppose Ψ : Gf → G0 is an isomorphism. With f ′ = 0, (10.3) gives α∗ [f d] = 0; since
α∗ is an isomorphism H 2 (H, A) → H 2 (H, Aβ ) (inverse (α−1 )∗ , using (10.2)), [f d] = 0, i.e.
(f κ, f κ) = 0, so f κ = 0 and f = 0 by Theorem 9.4.                                          □
     From now on assume f, f ′ ̸= 0.

10.4 Rigidity of α: Morita/Noether–Skolem. Let E ⊆ EndF2 (A) be the F2 -linear span of
{γ̂ : γ ∈ H}. Since {γ̂} is closed under composition and contains 1 = ê, E is a unital ring.
Lemma 10.9. E = {diag(m, m) : m ∈ M2g (R)}, acting diagonally on A = R2g ⊕ R2g ; thus
E∼
 = M2g (R) as rings. Its center is {r · idA : r ∈ R} ∼
                                                     = R.
Proof. “⊆”: each γ̂ = diag(γ, γ) with γ ∈ M2g (R), and the F2 -span of such block-diagonal “dou-
bled” matrices consists of doubled matrices. “⊇”: working inside M2g (R) (one leg; everything
is doubled),
                                                                 
                                            0 b      0 0         bc 0
                        (xb − 1)(yc − 1) =                 =            ,
                                            0 0      c 0         0 0
and (xb − 1)(yc − 1) = xb yc − xb − yc + 1 lies in the span of {γ̂} (each of the four terms is ± an
element of H or 1; signs are irrelevant over F2 ). The products bc of symmetric matrices F2 -span
Mg (R): Eαα · (rEαα ) = rEαα , and for α ̸= β, Eαα · r(Eαβ + Eβα ) = rEαβ ; every matrix is the
sum of such single-entry matrices. So E containsall ( m     0
                                                           0 0 ), m ∈ Mg (R) (doubled). Multiplying
                                                   0 I
on the left and/or right by ŵ0 ∈ E (w0 = I 0 ∈ H) produces all four g × g corner blocks:
w0 ( m 0       0 0      m0          0m          m0          0 0
     0 0 ) = ( m 0 ), ( 0 0 )w0 = ( 0 0 ), w0 ( 0 0 )w0 = ( 0 m ). Sums of corner blocks give every
matrix of M2g (R) (doubled). Center: an element diag(m, m) is central iff m commutes with all
of M2g (R), iff m = r 1 with r ∈ R (commuting with every matrix unit Eij forces m diagonal
with all diagonal entries equal). The map r 7→ r idA = diag(r1, r1) is a ring isomorphism of R
onto the center, injective because A is a faithful R-module.                                      □

   By (10.2), the conjugation map Θ := α(·)α−1 on EndF2 (A) maps γ̂ 7→ βγ;   c being an F2 -
algebra automorphism of EndF2 (A) carrying the generating set {γ̂} bijectively onto itself (via
the bijection β), it restricts to a ring automorphism Θ of E ∼
                                                             = M2g (R). Θ preserves the center,
so it defines θ ∈ Autring (R) by Θ(r id) = θ(r) id, and then
                              α(ra) = θ(r) α(a)      (r ∈ R, a ∈ A).                         (10.4)

Lemma 10.10. Autring (R) is the finite group Θfin of the maps determined by θ|Fq = φ ∈
Gal(Fq /F2 ) and θ(t) = at + b (a ∈ F×
                                     q , b ∈ Fq ); its order is q(q − 1)s.

Proof. A ring automorphism θ preserves the unit group R× = F×            q and 0, hence preserves
Fq = F× q  ∪ {0} setwise, restricting to a field automorphism φ of F q (necessarily fixing the prime
field F2 ). There are exactly s such automorphisms: choosing a primitive element α of Fq over
F2 with minimal polynomial mα of degree s, any automorphism is determined by its value on α,
                                                                                                   j
which must be one of the at most s roots of mα in Fq ; and the iterated Frobenius maps x 7→ x2 ,
                                                          j      j′
0 ≤ j < s, are s pairwise distinct automorphisms: if x2 = x2 for all x, with 0 ≤ j < j ′ < s,
                                                               j ′ −j
then composing with the inverse of the j-th iterate gives x2          = x for all x ∈ Fq — but that
                        j ′ −j    s−1
equation has at most 2         ≤2     < q solutions. So Aut(Fq ) = Gal(Fq /F2 ) has order s. Let
p := θ(t). Then θ(R) = φ(Fq )[p] = Fq [p]. If deg p = 0 then Fq [p] = Fq ̸= R; if deg p ≥ 2 then
every element of Fq [p] ∖ Fq has degree ≥ 2, so t ∈  / Fq [p]. Surjectivity thus forces deg p = 1:
θ(t) = at + b, a ̸= 0. Conversely, each choice of (φ, a, b) defines an automorphism (its inverse
corresponds to (φ−1 , φ−1 (a−1 ), φ−1 (−a−1 b))). The count is s · (q − 1) · q.                  □
                          NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                       35

  For θ ∈ Θfin let θ∗ denote the entrywise application of θ to matrices — a ring automor-
phism of M2g (R) fixing J (entries 0, 1), hence satisfying θ∗ (H) = H — and let θ• denote the
coordinatewise application of θ to S = R2g or A = R4g : an additive bijection with
θ• (r a) = θ(r) θ• (a),       θ• (ma) = θ∗ (m) θ• (a) (m ∈ M2g (R) acting on a leg, or doubled on A).
                                                                                             (10.5)
Proposition 10.11 (canonical form of α). (In this statement and for the rest of §10,
the symbol g in expressions like g ∈ GL2g (R), Ad(g), G = diag(g, g) denotes a matrix ; the
subscript 2g continues to refer to the fixed integer g ≥ 2. No expression below uses the two
meanings in the same formula ambiguously.) There exist g ∈ GL2g (R) and Λ = (λij ) ∈ GL2 (R)
such that, with G := diag(g, g) acting on A and Λ acting “across the legs” by Λ(s1 , s2 ) :=
(λ11 s1 + λ12 s2 , λ21 s1 + λ22 s2 ):
                      α = G ◦ θ• ◦ Λ       and     β(γ) = g θ∗ (γ) g −1 (γ ∈ H).             (10.6)
Moreover g normalizes H in GL2g (R).
Proof. The map (θ     −1 ) ◦Θ is an automorphism of M (R) ∼ E which is R-linear: (θ −1 ) Θ(rm) =
                          ∗                             2g   =                            ∗
  −1                        −1
                    
(θ )∗ θ(r)Θ(m) = r (θ )∗ Θ(m). By Noether–Skolem over the PID R (Theorem A.1, proved
in Appendix A), (θ−1 )∗ ◦Θ = Ad(g1 ) for some g1 ∈ GL2g (R); hence Θ = θ∗ ◦Ad(g1 ) = Ad(g)◦θ∗
with g := θ∗ (g1 ).
   Translate to endomorphisms of A: for m ∈ M2g (R), writing m̂ := diag(m, m), we have
Θ(m̂) = gθ∗\  (m)g −1 = G θ• m̂ θ•−1 G−1 by (10.5). Since also Θ(m̂) = αm̂α−1 , the additive
bijection
                                            α2 := θ•−1 G−1 α
commutes with every m̂ ∈ E.
   Commutants: we claim the additive maps A → A commuting with all of E are exactly the
maps Λ as in the statement with λij ∈ R. Indeed, the two inclusions ι1 , ι2 : S → A and
projections p1 , p2 : A → S are E-equivariant (for the diagonal action), so ϕij := pi ◦ α2 ◦
ιj : S → S is an additive map commuting with the M2g (R)-action on the standard module
S = R2g . For such ϕ := ϕij : E11 ϕ(ε1 ) = ϕ(E11 ε1 ) = ϕ(ε1 ) forces ϕ(ε1 ) ∈ Rε1 , say = λε1 ;
then ϕ(εi ) = ϕ(Ei1 ε1 ) = Ei1 λε1 = λεi , and ϕ(rεi ) = ϕ((rI)εi ) = (rI)λεi = λrεi ; by additivity
ϕ = λ · idS . (Here ε1 , . . . , ε2g is the standard basis of S and Ei1 , rI ∈ M2g (R).) Hence
α2 = Λ with Λ = (λij ) ∈ M2 (R). Since α2 is bijective, so is Λ, and its inverse — being the
same construction applied to α2−1 , which also commutes with E — is again of this form; so
Λ ∈ GL2 (R).
   This proves α = Gθ• Λ. For β: by (10.2), βγ   c = αγ̂α−1 = Θ(γ̂) = gθ∗\  (γ)g −1 , and m 7→ m̂ is
injective, so β(γ) = gθ∗ (γ)g . Finally β(H) = H and θ∗ (H) = H give gHg −1 = H.
                                −1                                                                □

Lemma 10.12 (normalizer). {h ∈ GL2g (R) : hHh−1 = H} = F×
                                                        q · H.

Proof. Step 1: the H-invariant R-bilinear forms on R2g are R
                                                             ω. Let M ∈ M2g (R) be the
                                                    M11 M12
Gram matrix of an invariant form, in blocks M = M    21 M22
                                                            . Invariance under xb means
xT                                                                  T
                                           I b
                                                                        I 0
                                                                             
 b M xb = M for all symmetric b; with xb = 0 I (column action) and xb = b I :
                                                                    
                   T             M11             M11 b + M12
                 xb M xb =                                             .
                             bM11 + M21 bM11 b + bM12 + M21 b + M22
Equality with M for all symmetric b forces M11 b = 0 for all b (take the (1, 2) block), so M11 = 0
(b = I), and then bM12 + M21 b = 0, i.e. (characteristic 2) bM12 = M21 b for all symmetric b.
36                      NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)

Taking b = Eii : Eii M12 has nonzero entries only in row i, and M21 Eii only in column i; equality
forces (M12 )ij = 0 = (M21 )ji for j ̸= i and (M12 )ii = (M21 )ii . So M12 = M21 = D diagonal.
Taking b = Eij + Eji (i ̸= j): bD = Djj Eij + Dii Eji and Db = Dii Eij + Djj Eji , soDii = Djj :
D = λI. Invariance under the yc symmetrically forces M22 = 0. Hence M = λ I0 I0 = λJ, the
Gram matrix of λω.
   Step 2. Let h normalize H. For γ ∈ H: hγh−1 ∈ H preserves ω, so γ T (hT Jh)γ = hT Jh:
the form with Gram matrix hT Jh is H-invariant, so hT Jh = cJ with c ∈ R by Step 1.
Taking determinants: c2g det J = (det h)2 det J, and det J ̸= 0, so c2g = (det h)2 ∈ R× = F×       q
(h ∈ GL2g (R)). Since degrees add in the domain R, c2g ∈ F×    q   forces deg c =  0 and  c ̸
                                                                                            = 0, i.e.
c ∈ F×            ×                                                 ×           2
      q . Since |Fq | = q − 1 is odd, squaring is a bijection of Fq , so c = ζ for some ζ ∈ Fq ;
                                                                                                  ×
        −1   T    −1       −2                −1
then (ζ h) J(ζ h) = ζ cJ = J, i.e. ζ h ∈ H and h ∈ Fq H.        ×

   Step 3. Conversely, scalars are central in GL2g (R) and H normalizes itself, so F×q H normalizes
H.                                                                                                 □

10.5 Transports on H 2 (H, S). Definition. A transport pair is a pair (T, β) where β ∈
Aut(H) and T : S → S is an additive bijection with T (γs) = β(γ)T (s) for all γ ∈ H, s ∈ S. It
induces
              T♯ : H 2 (H, S) → H 2 (H, S),   T♯ [c] := T ◦ c ◦ (β −1 × β −1 ) .
                                                                             

Lemma 10.13. (i) T♯ is well defined and bijective; (T, β)♯ ◦ (T ′ , β ′ )♯ = (T ◦ T ′ , β ◦ β ′ )♯ ;
(id, id)♯ = id, and (T −1 , β −1 ) is a transport pair with (T −1 )♯ = (T♯ )−1 . (ii) If T is θ-semilinear
(T (rs) = θ(r)T (s)) then T♯ (r x) = θ(r) T♯ (x) for x ∈ H 2 (H, S), r ∈ R. In particular, for such
T , AnnR (T♯ κ) = θ(AnnR κ) = 0 by Theorem 9.4. (iii) For ζ ∈ F×         q , (ζ · idS , idH ) is a transport
pair with (ζ·)♯ = ζ· (the R-module action). (iv) (Inner transports are trivial.) For h0 ∈ H, the
pair (h0 ·, Ad h0 ) — s 7→ h0 s, γ 7→ h0 γh−10 — is a transport pair, and (h0 ·)♯ = id on H (H, S).
                                                                                                    2


Proof. (i) Let c ∈ Z 2 (H, S) and cT := T ◦ c ◦ (β −1 × β −1 ). Using T (β −1 (γ)s) = γT (s):
       γ1 cT (γ2 , γ3 ) + cT (γ1 , γ2 γ3 ) = T β −1 (γ1 )c(β −1 γ2 , β −1 γ3 ) + c(β −1 γ1 , β −1 (γ2 γ3 )) ,
                                                                                                           

and similarly for the other side of the cocycle identity; the identity for c at the triple (β −1 γ1 , β −1 γ2 , β −1 γ3 )
transports. Likewise T ◦ ∂n ◦ (β −1 × β −1 ) = ∂(T ◦ n ◦ β −1 ). Compositionand inverses are direct
computations. (ii) T ◦ (rc) ◦ (β −1 × β −1 ) = θ(r) T ◦ c ◦ (β −1 × β −1 ) . For the annihilator:
rT♯ κ = 0 ⇐⇒ T♯ (θ−1 (r)κ) = 0 ⇐⇒ θ−1 (r)κ = 0 ⇐⇒ r = 0. (iii) Clear. (iv) It is a trans-
port pair: h0 (γs) = (h0 γh−1                     2
                            0 )(h0 s). Let c ∈ Z (H, S) be a cocycle; we may assume c normalized
(adjust by a coboundary; T♯ respects coboundaries).
                                                         Consider the extension Ec := S ×c H and
the inner automorphism Ψ0 := Ad (0, h0 ) of Ec . It preserves S: by (2.1), Ψ0 (a, e) = (h0 a, e).
Lemma 10.7 applies with B = B ′ = S, c = c′ , and yields the data α0 = h0 · (computed above)
and β0 = Ad h0 (the element Ψ0 (0, γ) = (0, h0 )(0, γ)(0, h0 )−1 has H-component h0 γh−1       0 ); thus

         (h0 )∗ [c] = (Ad h0 )∗ [c] in H 2 (H, Sβ0 ),          i.e. [h0 ◦ c] = [c ◦ (Ad h0 × Ad h0 )].
Composing both classes with (β0−1 × β0−1 ) — which maps Z 2 (H, Sβ0 )-cocycles to Z 2 (H, S)-
cocycles and coboundaries to coboundaries (same computation as (i)) — gives [h0 ◦ c ◦ (β0−1 ×
β0−1 )] = [c], i.e. (h0 ·)♯ [c] = [c].                                                      □

10.6 The master equation and the finiteness theorem. Proposition 10.14. Let f, f ′ ∈
R ∖ {0} and let Ψ : Gf → Gf ′ be an isomorphism, with data θ ∈ Θfin , g = ζh0 (ζ ∈ F×q ,
h0 ∈ H; Lemma 10.12), Λ ∈ GL2 (R) as in Proposition 10.11. Set T := g ◦ θ• : S → S, i.e.
                       NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                 37

T (s) = g θ• (s) (a θ-semilinear additive bijection; it is a transport pair for β, as checked below)
and λ(i) := λi1 + λi2 ∈ R (i = 1, 2). Then:
                                      θ(λ(i) ) θ(f ) T♯ κ = f ′ κ    (i = 1, 2).                    (10.7)
Moreover λ(1) = λ(2) =: λ, λ ∈ F×
                                q , and

               f ′ κ = ξ θ(f ) κθ ,         where ξ := θ(λ) ζ ∈ F×
                                                                 q and κθ := (θ• , θ∗ )♯ κ.         (10.8)
Proof. Derivation of (10.7). T is a transport pair for β: T (γs) = gθ• (γs) = g θ∗ (γ)θ• (s) =
β(γ) g θ• (s) = β(γ)T (s), using (10.5) and (10.6). Compute α ◦ (f d): since d(γ, γ ′ ) = (d, d) is
diagonal,
                                                                                                                  
Λ f d, f d = λ(1) f d, λ(2) f d ,              α f d(γ, γ ′ ) = θ(λ(1) f ) T (d(γ, γ ′ )), θ(λ(2) f ) T (d(γ, γ ′ )) ,
                              
                                     hence

using Gθ• (λ(i) f d) = θ(λ(i) f ) gθ• (d) (θ• semilinear, g R-linear). The twisted action on Aβ is
diagonal (γ ∗ a = βγa),
                     c     so H 2 (H, Aβ ) = H 2 (H, Sβ ) ⊕ H 2 (H, Sβ ) and (10.3) splits into two
leg-equations in H 2 (H, Sβ ):
                          θ(λ f ) T ◦ d = f ′ d ◦ (β × β)
                          (i)                             
                                                                   (i = 1, 2).
Apply the coboundary-preserving bijection x 7→ x ◦ (β −1 × β −1 ) from β-twisted to standard
coefficients (as in Lemma 10.13): the right side becomes f ′ [d] = f ′ κ and the left side becomes
θ(λ(i) f ) [T ◦ d ◦ (β −1 × β −1 )] = θ(λ(i) )θ(f ) T♯ κ. This is (10.7).
   Equal row sums, λ ̸= 0. Subtracting the two instances of (10.7): θ (λ(1) −λ(2) )f T♯ κ = 0; by
                                                                                                   

Lemma 10.13(ii), θ((λ(1) −λ(2) )f ) = 0, and θ injective, R a domain, f ̸= 0 give λ(1) = λ(2) =: λ.
If λ = 0, (10.7) gives f ′ κ = 0, so f ′ = 0 (Theorem 9.4) — excluded. So λ ̸= 0.
   λ is a unit. Apply (T −1 )♯ = (T♯ )−1 (Lemma 10.13(i)) to (10.7): since T −1 = θ•−1 g −1 is
 −1
θ -semilinear,
                    (T −1 )♯ θ(λf ) T♯ κ = λf κ,         (T −1 )♯ (f ′ κ) = θ−1 (f ′ ) (T −1 )♯ κ,
                                        

so
                                             λf κ = θ−1 (f ′ ) (T −1 )♯ κ.                          (10.9)
Now apply the whole analysis to the isomorphism Ψ−1 : Gf ′ → Gf . Its restriction to A is
α−1 = Λ−1 θ•−1 G−1 . We bring it to canonical form: θ•−1 G−1 = G    e θ−1 with G
                                                                       •
                                                                                 e := diag(g̃, g̃),
       −1   −1                      −1 e  e   −1
g̃ := θ∗ (g ) (by (10.5)); and Λ G = GΛ (leg-matrices commute with doubled matrices:
both act by R-linear operations, one across legs with scalar coefficients, the other within legs),
and Λ−1 θ•−1 = θ•−1 θ+ (Λ−1 ) where θ+ (Λ−1 ) applies θ to the entries of Λ−1 (check on (s1 , s2 ),
using θ•−1 (θ(r)s) = rθ•−1 (s)). Hence
                          α−1 = G
                                e ◦ θ•−1 ◦ Λ,
                                           e               e := θ+ (Λ−1 ) ∈ GL2 (R),
                                                           Λ
which is the canonical form of Ψ−1 , with ring automorphism θ−1 (note (θ−1 )• = θ•−1 ) and
transport Te := g̃ ◦ θ•−1 . We claim Te = T −1 : indeed, for s ∈ S, g̃ θ•−1 (s) = θ∗−1 (g −1 ) θ•−1 (s) =
θ•−1 (g −1 s) by (10.5), so Te = θ•−1 ◦ (g −1 ·) = (g ◦ θ• )−1 = T −1 . The automorphism of H induced
by Ψ−1 is β −1 (the two induced automorphisms compose to the identity), and (T −1 , β −1 ) is
a transport pair by Lemma 10.13(i); moreover α−1 (ra) = θ−1 (r)α−1 (a) by (10.4). Hence the
derivation of (10.7), run verbatim for Ψ−1 with the canonical form just exhibited, gives (with
λ̃ := common row sum of Λ,     e equal for the two rows and nonzero by the same Step applied to
   −1
Ψ ):
                                      θ−1 (λ̃) θ−1 (f ′ ) (T −1 )♯ κ = f κ.
38                   NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)


Substituting (10.9) — i.e. θ−1 (f ′ )(T −1 )♯ κ = λf κ — gives θ−1 (λ̃) λ f κ = f κ, so θ−1 (λ̃)λ −
1 f ∈ AnnR (κ) = 0; since f ̸= 0 and R is a domain, θ−1 (λ̃) λ = 1: λ ∈ R× = F×
 
                                                                                    q .
   Factoring the transport. Write g = ζh0 (Lemma 10.12). As transport pairs,
                             (T, β) = (ζ·, id) ◦ (h0 ·, Ad h0 ) ◦ (θ• , θ∗ ) :
the T -components compose to ζ h0 θ• = gθ• = T , and the automorphism components to
Ad(h0 ) ◦ θ∗ = Ad(ζh0 ) ◦ θ∗ = Ad(g) ◦ θ∗ = β (scalars act trivially by conjugation). (Note
(θ• , θ∗ ) is a transport pair by (10.5), and θ∗ ∈ Aut(H).) By Lemma 10.13(i),(iii),(iv):
                                    T♯ κ = ζ · (h0 )♯ (θ• )♯ κ = ζ κθ .
Substituting into (10.7) (with λ(i) = λ): f ′ κ = θ(λ)θ(f ) ζ κθ = ξ θ(f ) κθ .                     □

Theorem 10.15 (separation). Fix f ∈ R ∖ {0}. Then
            #{f ′ ∈ R : Gf ′ ∼
                             = Gf } ≤ (q − 1) · |Θfin | = q(q − 1)2 s < ∞.
Moreover Gf ′ ∼ ̸ G0 for every f ′ ̸= 0.
                 =
Proof. If Gf ′ ∼ = Gf then f ′ ̸= 0: otherwise Gf ∼     = Gf ′ = G0 , contradicting Corollary 10.8
(as f ̸= 0). So by Proposition 10.14 there are ξ ∈ F×                                ′
                                                             q and θ ∈ Θfin with f κ = ξ θ(f ) κθ .
Thus f ′ κ lies in the set {ξ θ(f ) κθ : ξ ∈ F×  q , θ ∈ Θfin }, of cardinality at most (q − 1)|Θfin |
— note κθ depends only on θ, not on Ψ. Since f ′ 7→ f ′ κ is injective (Theorem 9.4), at most
(q − 1)|Θfin | = q(q − 1)2 s values of f ′ are possible. The last sentence is Corollary 10.8.      □

                              11. Proof of the Main Theorem
   Consider the countable family {Gtd }d∈N (td ̸= 0, pairwise distinct). By Theorem 10.15, each
isomorphism class of groups meets {Gf : f ∈ R} — in particular meets {Gtd } — in at most
q(q − 1)2 s members; hence the groups Gtd , d ∈ N, fall into infinitely many isomorphism classes.
Choose d1 < d2 < · · · with Gtd1 , Gtd2 , . . . pairwise non-isomorphic, and set Γi := Gtdi . Then:
      • each Γi is a countable discrete ICC group (Proposition 7.3) with Kazhdan’s property
         (T) (Theorem 8.7), in particular finitely generated;
      • L(Γi ) ∼
               = L(G0 ) = M trace-preservingly for every i (Theorem 6.7), and M is a II1 factor
         (Proposition 7.3) with property (T) (Theorem 8.7);
      • the Γi are pairwise non-isomorphic, by choice.
   This proves the Main Theorem. ■
   The smallest instance is q = 2, g = 2: infinitely many pairwise non-isomorphic twisted
extensionsF2 [t]8 ×td d Sp4 (F2 [t]), all with group von Neumann algebra the II1 factor L F2 [t]8 ⋊
Sp4 (F2 [t]) .

            Appendix A. Noether–Skolem over a principal ideal domain

Theorem A.1. Let R be a commutative principal ideal domain and n ≥ 1. Every R-algebra
automorphism Θ of Mn (R) is inner: there is Y ∈ GLn (R) with Θ = Ad(Y ), i.e. Θ(m) =
Y mY −1 for all m ∈ Mn (R).
Proof. Let Eij be the matrix units and e := E11 . The matrix ε := Θ(e) ∈ Mn (R) is an
idempotent (ε2 = Θ(e2 ) = ε), so the R-module
                                           L := εRn ⊆ Rn
is a direct summand of Rn (with complement (1 − ε)Rn ), hence finitely generated and torsion-
free; over the PID R it is therefore free ([SF], structure theorem), say L ∼
                                                                           = Rk .
                      NON-ISOMORPHIC ICC (T) GROUPS WITH A COMMON L(G)                                 39

    Step 1: k = 1. Let K be the field of fractions of R and ΘK := Θ ⊗R K, a K-algebra
automorphism of Mn (K); then L ⊗R K = εK n (localize the direct sum Rn = L ⊕ (1 − ε)Rn ), so
k = dimK εK n =: rank ε, and it suffices to show rank ΘK (e) = 1. We use the following algebraic
characterization: for idempotents ε1 , . . . , εm ∈ Mn (K) which are pairwise orthogonal (εi εj = 0
for i ̸= j), the images εi K n are linearly
P                                              P independent subspaces and rank(ε1 + · ·P     · + εm ) =
    i rank εi . Indeed, if v i =  ε i w i and      v
                                                 i L i = 0, applying εj  gives v j = 0; and (   i εi )vj =
ε2j wj = vj , so the image of         εi is exactly i εi K n (it is contained in the sum, and contains
                                P

each summand).                                         Pn
    NowPnapply ΘK to the decomposition 1 = i=1 Eii into n pairwise orthogonal idempotents:
1 = i=1 ΘK (Eii ) is again a sum of n pairwise orthogonal idempotents (ring automorphisms
preserve idempotency and orthogonality), each nonzero (automorphisms are injective), hence
each of rank ≥ 1. Since the ranks add up to rank(1) = n, each ΘK (Eii ) has rank exactly 1.
In particular rank ε = rank ΘK (E11 ) = 1, i.e. k = 1 (using the [SF] structure theorem: the
finitely generated torsion-free R-module L is free, of rank dimK (L ⊗R K)). So L = Rx0 for
some x0 ∈ L with AnnR (x0 ) = 0.
    Step 2: construction of the intertwiner. For v = (v1 , . . . , vn )T ∈ Rn let Ξ(v) := ni=1 vi Ei1 ∈
                                                                                           P
Mn (R) (the matrix with first column v and other columns 0); note Ξ(mv) = m Ξ(v) for
m ∈ Mn (R) and Ξ(v)e = Ξ(v). Define
                                 ϕ : Rn → Rn ,
                                                                       
                                                        ϕ(v) := Θ Ξ(v) x0 .
Then ϕ is R-linear (Θ is R-linear and Ξ is), and for every m ∈ Mn (R):
                                       
                   ϕ(mv) = Θ Ξ(mv) x0 = Θ(m) Θ(Ξ(v)) x0 = Θ(m) ϕ(v).                                (A.1)
  Step 3: ϕ is surjective. Let y ∈ Rn . From 1 = i Eii = i Ei1 e E1i we get
                                                 P         P
                                           n
                                           X
                                      y=         Θ(Ei1 ) ε Θ(E1i ) y.
                                           i=1
Each vector ε Θ(E1i )y lies in L = Rx0 , say εΘ(E1i )y = ci x0 with ci ∈ R. Hence, with
c := (c1 , . . . , cn )T ,
                           X                  X       
                        y=   Θ(Ei1 ) ci x0 = Θ   ci Ei1 x0 = Θ(Ξ(c)) x0 = ϕ(c).
                         i                         i
   Step 4: conclusion. ϕ is given by a matrix Y ∈ Mn (R) (R-linearity), and ϕ surjective
means the columns of Y generate Rn ; solving Y zi = ei for each standard basis vector produces
Z ∈ Mn (R) with Y Z = 1, so det Y det Z = 1, det Y ∈ R× , and Y ∈ GLn (R). Equation (A.1)
reads Y m = Θ(m)Y for all m ∈ Mn (R) (both sides are R-linear maps agreeing on every v),
i.e. Θ(m) = Y mY −1 .                                                                       □
  Remark. The paper applies this with R = Fq [t], a Euclidean domain and in particular a
PID.
