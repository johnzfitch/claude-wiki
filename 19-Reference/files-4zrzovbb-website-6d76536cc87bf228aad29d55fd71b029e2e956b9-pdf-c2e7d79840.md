---
title: "Files 4Zrzovbb Website 6D76536Cc87Bf228Aad29D55Fd71B029E2E956B9 Pdf C2E7D79840"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/6d76536cc87bf228aad29d55fd71b029e2e956b9.pdf"
category: "19-Reference"
fetched_at: "2026-08-09T06:49:14Z"
---

Lower bounds for the arithmetic formula and circuit complexity
                       of the permanent


                                                Abstract
         We prove two unconditional lower bounds for the arithmetic complexity of the permanent
     over fields of characteristic zero. First, every arithmetic formula computing permn has
     Ω(n4 / log n) leaves, improving the classical Ω(n3 ) bound obtained from the algebraic form
     of Nechiporuk’s method. Second, every arithmetic circuit computing permn has at least
     n2 log2 log2 n/500 internal nodes; in particular the circuit complexity of the permanent is
     super-quadratic. The formula bound combines a Nechiporuk–Kalorkoti transfer lemma with
     a new transcendence-degree estimate for the family of padded permanental minors attached
     to a diagonal arc of Θ(log n) cells, proved through a character-collapse identity in a square-
     zero algebra. The circuit bound applies Baur–Strassen and Strassen’s degree bound to an
     explicit valuated affine section of the graph of the permanental cofactor map, whose initial
     system is a “forced-column rook system”; the number of isolated points in a single fibre is
     driven up by an equivariant orbit construction whose nondegeneracy is certified by an Euler–
     Jacobi universality theorem together with a row-graded degeneration of the bare-window
     Jacobian.


1    Introduction
Let F be a field and let
                                          n
                                        X Y
                           permn =                xiσ(i) ∈ F[x11 , . . . , xnn ]
                                       σ∈Sn i=1

be the permanent of a generic n × n matrix. The permanent is the standard hard polynomial
of algebraic complexity theory: it is complete for Valiant’s class VNP [14], and proving super-
polynomial lower bounds for its arithmetic circuit or formula size is the central open problem of
the area [11, 2]. In the absence of such bounds one asks for the best unconditional bounds that
current techniques can deliver. This paper proves two of them.
    Throughout, an arithmetic formula over F is a rooted binary tree whose leaves are labelled
by variables or constants of F and whose internal nodes are labelled + or ×; its size is its number
of leaves, and L(f ) is the minimum size of a formula computing f . An arithmetic circuit is a
directed acyclic graph whose sources are labelled by variables or constants and whose internal
nodes are labelled + or × with fan-in two and unrestricted fan-out (no division); its size is the
number of internal nodes, and C(f ) is the minimum size of a circuit computing f .
Theorem (Main Theorem A). Over every field of characteristic zero,
                                              4 
                                                n
                            L(permn ) = Ω             ;
                                               log n
in particular L(permn ) = ω(n3 ).

                                                    1
Theorem (Main Theorem B). Over every field of characteristic zero,
                                    n2 log2 log2 n
                   C(permn ) ≥                           for all sufficiently large n;
                                         500
in particular C(permn ) = ω(n2 ).

Prior work. Ryser’s formula [10] exhibits permn as a depth-3 formula of size O(n2 2n ), so
L(permn ) = 2O(n) ; no better upper bound is known. On the lower-bound side, Nechiporuk’s
method [8] for Boolean formulas was transferred to the arithmetic setting by Kalorkoti [6], who
replaced the count of subfunctions by the transcendence degree of the family of coefficients
obtained by expanding the polynomial in a block of variables, and deduced L(permn ) = Ω(n3 ).
Main Theorem A improves this to Ω(n4 / log n); Remark I.6.3 shows that this is, up to constant
factors, the largest bound that the Nechiporuk–Kalorkoti measure can yield for the permanent,
so the bound is optimal for the method. For general circuits the only technique available is
Strassen’s degree bound [12] combined with the derivative trick of Baur and Strassen [1]: a
size-s circuit for f yields a size-5s circuit for the gradient of f , whose graph is an irreducible
variety of degree at most 25s , so that 5 C(f ) ≥ log2 of the number of isolated points of any
affine-linear section of that graph. For polynomials such as power sums this gives Ω(N log d)
bounds in N variables of degree d; for the permanent, however, the method reduces to a hard
counting problem about the permanental cofactor map X 7→ (perm X ij )ij , and we are not aware
                                                                        bb

of any bound better than the trivial Ω(n2 ). Main Theorem B provides a super-quadratic bound.
For restricted models much more is known; for instance Raz [9] proved super-polynomial lower
bounds for multilinear formulas computing the permanent, and Mignon and Ressayre [7] proved
a quadratic lower bound on the determinantal complexity of the permanent in characteristic
zero.

Overview of the proof of Main Theorem A. Part I. The Nechiporuk–Kalorkoti transfer
lemma (Lemma I.2.1) states that if Φ is a formula computing f and Y is a set of variables, then
the transcendence degree of the family of coefficients of f expanded in the Y -monomials is at
most 4sY (Φ) + 2, where sY (Φ) is the number of Y -labelled leaves; summing over a partition
of the variables into blocks bounds L(f ) from below. The new ingredient is the Key Lemma
(Lemma I.4.1): for a block consisting of k = Θ(log n) cells in pairwise distinct rows and columns,
the coefficient family — a family of padded permanental minors indexed by subsets T of the block
— has transcendence degree Ω(n2 ), i.e. as large as the ambient number of variables allows. Since
the blocks can be taken to be Θ(n2 / log n) disjoint “diagonal arcs”, this yields Ω(n4 / log n). The
Key Lemma is proved by a Jacobian certificate: we evaluate the relevant minors of the Jacobian
matrix at an explicit matrix built from a primitive M -th root of unity ω with M = 2a − 1,
factor each Jacobian entry into a product of two independent injection sums (Lemma I.4.2), and
evaluate each injection sum in closed form by a character-collapse identity in the square-zero
algebra C[xi ]/(x2i ) (Lemma I.4.3). The outcome is that the selected rows of the Jacobian become
pairwise distinct characters of Z2M , scaled by positive factorials; distinct characters are linearly
independent, which furnishes a nonvanishing minor. The positivity of the factorial factors is
precisely where the argument is permanental: the analogous determinantal certificate vanishes
identically.

Overview of the proof of Main Theorem B, I. Part II. By Baur–Strassen and the degree
                                                              2
bound it suffices to exhibit an affine-linear subspace W ⊆ A2n meeting the graph Γn of the

                                                     2
                                    2
permanental cofactor map in 2Ω(n log log n) isolated points. We work over the algebraic closure K
of Q(τ ) with its τ -adic valuation and design an explicit valuated “anchor” matrix P ◦ (τ ) together
with a slice of battery variables; the section W freezes all non-battery entries, parametrizes the
battery affinely, and pins a family of cofactors. An exact analysis of the minimal-weight “correc-
tions” of the base matching (Theorem II.4.1 and its stacked form Theorem II.7.1) identifies the
tight classes of the valuation and shows that all initial coefficients are positive sums with a delete-
one generalized Vandermonde structure; consequently, after Hensel lifting (Theorem II.5.1 and
Complement II.5.2), counting isolated points of Γn ∩ W reduces to counting isolated solutions of
a purely combinatorial forced-column rook system Nj,k (u) = εj,k on a staggered β × (q + β − 1)
board.

Overview of the proof of Main Theorem B, II. The forced-column rook system is a
mean-field system: by a Möbius inversion (the Structure Theorem of § II.6.1) each column’s
equations involve only that column’s own cells and 2β −2 global aggregates, and the local system
in one column is a complete intersection of multidegree (1, 2, . . . , β) with no zeros at infinity,
hence of degree exactly β!. If the aggregates are symmetric, the β! roots of a local system
form a single Sβ -orbit; filling
                          Q      s blocks of β! columns with s complete orbits therefore produces
a fibre invariant under i Sym(β!), so that one nondegenerate arranged configuration yields
((β!)!)s of them (Lemma A). The nondegeneracy of an arranged configuration is equivalent to the
nonsingularity of an explicit matrix M (Lemma L); the coupling block of M is a global residue,
and the Euler–Jacobi vanishing theorem makes it graded-triangular with universal diagonal
blocks (Theorem U), so that the set of bad orbit counts is finite. The remaining germ is resolved
by specializing the formal family at orbit count s = 0, which collapses the Schur determinant to a
single homogeneous polynomial Dβ , the bare-window Jacobian; the Core Theorem (Appendix D)
proves Dβ ̸≡ 0 for all β by a row-graded degeneration whose diagonal blocks admit a closed-form
determinant. Finally the window length is aligned to the orbit count, q ′ = s∗ β! + β − 1, so that
the certificate is invoked exactly on the windows it covers, and a scaling argument decouples
B = Θ(n/β) stacked bands (Theorem II.7.2), multiplying the single-band count.

Organization. Part I (§§I.1–I.6) is self-contained and proves Main Theorem A. Part II proves
Main Theorem B: §§II.1–II.2 contain the transfer to isolated-point counting, §§II.3–II.4 the
valuated design and its tight classes, §II.5 the lifting, §II.6 the single-band counting machinery
and the aligned Count Lemma, §II.7 the stacked assembly and the final budget, and §II.8 the
synthesis. Appendix A discusses known obstructions, Appendix B records which statements
were additionally confirmed by computer algebra, Appendix C contains the full proofs of the
auxiliary results of §II.6.4, and Appendix D contains the proof of the Core Theorem.


Part I
Formula size: L(permn) = Ω(n4/ log n)
Theorem. Let F be any field of characteristic zero and let L(permn ) denote the minimum
number of leaves of an arithmetic formula over F (a rooted binary tree whose leaves are labelled


                                                  3
by variables or constants and whose internal nodes are labelled + or ×) computing
                                                                  n
                                                                X Y
                                             permn =                      xiσ(i) .
                                                               σ∈Sn i=1

Then
                                                             n4
                                                                             
                                              L(permn ) = Ω                       .
                                                            log n
In particular L(permn ) = ω(n3 ).

    Together with Ryser’s formula [10], which gives L(permn ) = 2O(n) (see the end of Section I.5),
the theorem locates the growth rate of L(permn ) between n4 / log n and 2O(n) .
    The proof is organized as follows. Section I.1 fixes notation and records the elementary
direction of the Jacobian criterion. Section I.2 proves the Nechiporuk–Kalorkoti transfer lemma.
Section I.3 sets up a partition of the matrix of variables into Θ(n2 / log n) “diagonal arcs” of size
Θ(log n) and identifies the per-arc coefficient family (padded permanental minors). Section I.4
contains the Key Lemma: each arc family has transcendence degree Ω(n2 ). Section I.5 assembles
the theorem, and Section I.6 contains concluding remarks.
    Throughout, [n] = {1, . . . , n}; for a matrix A and index sets R, C, the matrix “A with
rows R and columns C deleted” is the submatrix of A on the remaining rows and columns; the
permanent of the 0 × 0 matrix is 1. We abbreviate transcendence degree by td.


I.1     Preliminaries
Formulas. A formula Φ over F in variables x1 , . . . , xN is a rooted binary tree; each leaf is
labelled by a variable or by a constant of F, and each internal node is labelled + or × and
has exactly two children. We write Φb for the polynomial computed at the root in the obvious
bottom-up fashion, and |Φ| for the number of leaves of Φ. The formula size of f is L(f ) :=
          b = f }.
min{|Φ| : Φ

Transcendence degree. For a family C ⊆ F[Z] of polynomials in a set of variables Z, we write
tdF C for the transcendence degree over F of the subfield F(C) ⊆ F(Z). We use two standard
facts: a field extension generated by N elements has transcendence degree at most N ; and the
following Jacobian criterion.

Lemma I.1.1 (Jacobian certificate, characteristic 0). Let F be a field with       char F = 0 and let
c1 , . . . , cr ∈ F[Z]. If some r × r minor of the Jacobian matrix ∂ci /∂z i∈[r], z∈Z is a nonzero
element of F[Z], then c1 , . . . , cr are algebraically independent over F; that is, tdF {c1 , . . . , cr } = r.

Proof. Suppose not, and let P ∈ F[y1 , . . . , yr ] be a nonzero polynomial of minimal total degree
with P (c1 , . . . , cr ) = 0. Applying ∂/∂z for each z ∈ Z and using the chain rule,
                          r
                          X                                    ∂ci
                                (∂yi P )(c1 , . . . , cr ) ·       =0        for every z ∈ Z.
                                                               ∂z
                          i=1
                                                    
Thus the row vector (∂y1 P )(c), . . . , (∂yr P )(c) , with c = (c1 , . . . , cr ), annihilates the Jacobian
matrix over the field F(Z). This vector is nonzero: since deg P ≥ 1 and char F = 0, some ∂yi P is

                                                                4
a nonzero polynomial, and it has strictly smaller degree than P , so (∂yi P )(c) ̸= 0 by minimality
of deg P . A nonzero vector over F(Z) annihilating the matrix forces every r × r minor to vanish
identically, contradicting the hypothesis.

Remark I.1.2 (Base field). In Section I.4 we exhibit a minor with integer coefficients and prove
that it is nonzero by evaluating it at a point whose coordinates lie in a cyclotomic field Q(ω). If
a polynomial with rational coefficients takes a nonzero value at some point of Q(ω)N , then it is a
nonzero polynomial over Q, hence also nonzero as an element of F[Z] for every field F containing
a copy of Q, in particular for every field of characteristic zero. Consequently all transcendence-
degree lower bounds proved below hold simultaneously over every characteristic-zero field.


I.2     The transfer lemma
Lemma I.2.1 (Nechiporuk–Kalorkoti transfer). Let Φ be a formula computing f , let Y be a set
of variables, and let Z be the set of all other variables occurring in Φ. Expand
                                      X
                                f =       cα (Z) Y α ,    cα ∈ F[Z],
                                         α

the sum being over monomials Y α in the variables of Y (only finitely many cα are nonzero). Let
sY (Φ) denote the number of leaves of Φ labelled by a variable of Y . Then

                                      tdF {cα }α ≤ 4 sY (Φ) + 2.

Proof. Write s = sY (Φ). If s = 0 then f = c0 ∈ F[Z] and the coefficient family is a single
polynomial, of transcendence degree at most 1 ≤ 2. Assume from now on s ≥ 1.
    Let W be the set of Y -labelled leaves, |W | = s, and let P ⊆ Φ be the union of the root-to-leaf
paths ending in the leaves of W ; thus P is a subtree of Φ whose leaf set is exactly W . Call
v ∈ P a branch vertex if both children of v lie in P ; a tree with s leaves has at most s − 1 branch
vertices. Put

                  V ′ = W ∪ {branch vertices of P } ∪ {root},              |V ′ | ≤ 2s.

Contracting P onto V ′ yields a tree T ′ with vertex set V ′ and at most 2s − 1 edges: each edge e
of T ′ joins a vertex v ∈ V ′ to the first vertex v + ∈ V ′ strictly above it in P . Define the gate set
of e to consist of all vertices of P lying strictly between v and v + , together with v + itself in the
single case where v + is the root and the root is not a branch vertex. In this way every vertex of
P that is neither a W -leaf nor a branch vertex belongs to the gate set of exactly one edge.
     Fix an edge e of T ′ and list its gates w1 , . . . , wt in upward order (possibly t = 0). Each wj is
an internal node of Φ lying on P which is not a branch vertex, so exactly one of its two children
lies in P ; the subtree hanging at the other child contains no Y -leaf and therefore computes some
polynomial uj ∈ F[Z]. If wj is a +-node it transforms the value g arriving from its P -child into
g + uj ; if it is a ×-node, into uj g. Composing these maps along the path yields an affine map

                                g 7−→ Ae g + Be ,        Ae , Be ∈ F[Z]

(with Ae = 1, Be = 0 when t = 0).
    Let R ⊆ F[Z] be the F-subalgebra generated by the at most 2(2s − 1) = 4s − 2 elements
{Ae , Be : e ∈ E(T ′ )}. We claim, by induction upward along T ′ , that the polynomial computed
at each non-root vertex of V ′ lies in R[Y ], and that f ∈ R[Y ].

                                                   5
    Base case. At a leaf w ∈ W the computed value is a variable of Y , which lies in R[Y ].
    Induction step at a branch vertex. Let v ∈ V ′ be a branch vertex, with operation ◦ ∈ {+, ×},
and let e1 , e2 be the two T ′ -edges entering v from below, coming from vertices v1 , v2 ∈ V ′ whose
values G1 , G2 lie in R[Y ] by induction. Then the value computed at v equals

                             (Ae1 G1 + Be1 ) ◦ (Ae2 G2 + Be2 ) ∈ R[Y ].

    The root. If the root is a branch vertex, the previous step applied at the root exhibits
f ∈ R[Y ]. If the root is neither a branch vertex nor a leaf, let e0 be the unique top edge of T ′ ,
with lower endpoint v0 and value G ∈ R[Y ]; the gate set of e0 contains the root, so the affine
map Ae0 (·) + Be0 accounts for the root’s own operation together with all gates below it, and
f = Ae0 G + Be0 ∈ R[Y ]. Finally, if the root is itself a W -leaf then Φ is a single leaf and f is a
variable of Y .
    Since Y ∩ Z = ∅, the expansion of an element of F[Z][Y ] in monomials of Y is unique, and
the coefficients of an element of R[Y ] lie in R. Hence every cα lies in R, and
                                                   
              tdF {cα } ≤ tdF F {Ae , Be }e∈E(T ′ ) ≤ 2(2s − 1) = 4s − 2 ≤ 4s + 2.

Corollary I.2.2 (Partition bound). Let Y1 , . . . , Yp be pairwise disjoint sets of variables and let
f be a polynomial. For each i, let τi be the transcendence degree of the family of coefficients
obtained by expanding f in the variables of Yi (the coefficients being polynomials in all remaining
variables). Then for every subset G ⊆ [p],
                                                   X τi − 2
                                         L(f ) ≥              .
                                                         4
                                                   i∈G

Proof. Fix an optimal formula Φ for f , so that L(f ) = |Φ| is its number of leaves. Each leaf
carries at most one variable label, and by disjointness of the Yi that variable belongs to at
P one Yi ; hence the leaf sets counted by sYi (Φ), i ∈ G, are pairwise disjoint and L(f ) ≥
most
   i∈G sYi (Φ). Applying Lemma I.2.1 to the same formula Φ for each i (with Y := Yi and Z :=
all other variables occurring in Φ) gives sYi (Φ) ≥ (τi − 2)/4. Summing over i ∈ G completes the
proof.


I.3    Arc blocks and padded permanental minors
Fix n and a block size k ≤ n. For 0 ≤ r ≤ n − 1 let
                               
                        Dr = (i, 1 + ((i − 1 + r) mod n)) : i ∈ [n]

be the r-th cyclic diagonal of the grid [n]×[n]. The sets D0 , . . . , Dn−1 partition the grid, and each
of them is the support of a permutation matrix. Cut each Dr into ⌊n/k⌋ arcs of k consecutive
cells (namely, for 0 ≤ j ≤ ⌊n/k⌋ − 1, the cells of Dr with row indices jk + 1, . . . , jk + k), and
place the at most k − 1 remaining cells of each diagonal (those with row index exceeding k⌊n/k⌋)
into a residual set. This produces
                                            p0 = n ⌊n/k⌋
pairwise disjoint arc blocks, each consisting of k cells with pairwise distinct rows and pairwise
distinct columns, together with residual cells; all together they partition the n2 variables. Only
the arc blocks will be used, via the subset G in Corollary I.2.2.

                                                   6
Lemma I.3.1 (Symmetry). Let Y = {(a1 , b1 ), . . . , (ak , bk )} be any set of k cells with pairwise
distinct rows and pairwise distinct columns. The transcendence degree of the coefficient family
obtained by expanding permn in the variables of Y equals the corresponding quantity for the
diagonal prefix Y0 = {(1, 1), . . . , (k, k)}.
Proof. Choose π, ρ ∈ Sn with π(aj ) = j and ρ(bj ) = j for j ∈ [k]; this is possible since the aj
are distinct and the bj are distinct. The substitution xab 7→ xπ(a)ρ(b) is a bijective relabelling of
the variables, hence induces an F-algebra automorphism Ψ of F[xab ]; it maps permn to permn ,
because permuting rows and columns leaves the permanent unchanged, and it maps the variables
of Y bijectively onto the variables of Y0 and the remaining variables bijectively
                                                                                Ponto the remaining
variables. Applying Ψ to the expansion permn = α cα Y α gives permn = α Ψ(cα )Y0α , so the
                                                     P
coefficient family for Y0 is the image under Ψ of the coefficient family for Y . Automorphisms
preserve transcendence degree.

The chunk family. Let Y0 = {(1, 1), . . . , (k, k)} (the chunk ) and let Z denote the remaining
n2 − k variables. Since permn is multilinear and the chunk cells lie in Q
                                                                        distinct rows and distinct
columns, the monomials of permn in the chunk variables are exactly i∈T xii for T ⊆ [k], and
                                             X Y 
                                 permn =               xii cT ,
                                              T ⊆[k]   i∈T

where
                                                                                    
   cT := perm X with rows and columns T deleted, and xii 7→ 0 for i ∈ [k] \ T ∈ F[Z].
                                                              Q
Indeed, the permutations contributing to the coefficient of i∈T xii are exactly those using all
chunk cells of T and avoiding all other chunk cells; deleting the rows and columns indexed by T
accounts for the former, and the substitution xii 7→ 0 (i ∈ [k] \ T ) accounts for the latter. We
write
                                  τn (k) := tdF {cT : T ⊆ [k]},
so that, by Lemma I.3.1, every arc block has coefficient family of transcendence degree exactly
τn (k).
     For the Jacobian computation we record the following: for a non-chunk cell (a, b) with
a, b ∈
     / T,
  ∂cT                                                                                          
        = perm X with rows T ∪ {a} and columns T ∪ {b} deleted, and xii 7→ 0 (i ∈ [k] \ T ) ,
 ∂xab
                                                                                           (I.3.1)
since the permanent is multilinear with ∂ perm /∂xab equal to the permanental minor at (a, b),
and the padding substitution commutes with this differentiation (the padded variables are dis-
tinct from xab ). (If a ∈ T or b ∈ T , the variable xab does not occur in cT and the derivative is
0.)


I.4     The Key Lemma
Lemma I.4.1 (Key Lemma). There is an absolute constant n0 such that for all n ≥ n0 and
every integer k with 2 log2 n + 4 ≤ k ≤ n/2,
                                          3                  3 2
                               τn (k) ≥      (n − k + 1)2 ≥     n .
                                          64                256

                                                 7
I.4.1    The evaluation point
Fix n and k as in the statement and put m := n − k (≥ n/2). Let

  a := ⌊log2 (m + 1)⌋     (so 2a ≤ m + 1 < 2a+1 ),          M := 2a − 1   (odd, m+1   a
                                                                                 2 ≤ 2 , M ≤ m),

and let ω ∈ C be a primitive M -th root of unity. For n ≥ n0 (any n0 ≥ 210 works) we have
m ≥ n/2 ≥ 29 and hence a ≥ 9; moreover m + 1 ≤ n, so

                           2(a − 1) ≤ 2 log2 (m + 1) − 2 ≤ 2 log2 n ≤ k.

We may therefore fix two disjoint subsets I1 = {α1 < · · · < αa−1 } and I2 = {β1 < · · · < βa−1 }
of [k]. Define weight functions g, h : I1 ∪ I2 → Z≥1 by

        g(αj ) = 2j−1 , g(βj ) = 2j−1 ,      h(αj ) = 2j−1 , h(βj ) = 2j     (1 ≤ j ≤ a − 1),
                                        P                      P
and for B ⊆ I1 ∪ I2 write σg (B) = i∈B g(i) and σh (B) = i∈B h(i).
   Define a point P # , an n×n matrix with entries in Q(ω), whose rows and columns are indexed
by the chunk indices 1, . . . , k followed by the bottom indices k + u for u ∈ [m]:

   • top-left k × k block: identically 0 (in particular all pad entries xii , i ∈ [k], are 0);

   • top-right cross: P # [ i, k + u ] = ω g(i) u for i ∈ I1 ∪ I2 and u ≤ M ; all other top-right entries
     are 0 (i.e. for u > M , and for i ∈ / I1 ∪ I2 the whole row is set to 0; its value is irrelevant,
     since such rows i lie in TK = [k] \ K and will always be deleted);

   • bottom-left cross: P # [ k + u, i ] = ω h(i) u for i ∈ I1 ∪ I2 and u ≤ M ; all other bottom-left
     entries are 0;

   • bottom-right m × m block: all entries equal to 1.

   We shall use only the following part of the Jacobian matrix of the family {cT }:

   • rows indexed by TK := [k] \ K for K ⊆ I1 ∪ I2 ;

   • columns indexed by the bottom-block cells (k +s, k +t) with s, t ∈ [M ] (these are genuine
     variables of Z, since only the k chunk-diagonal cells are excluded from Z, and M ≤ m).

By (I.3.1), and because all pad entries of P # are already 0, the corresponding Jacobian entry
evaluated at P # equals
                                                                       
                             J TK , (k + s, k + t)          = perm NK,s,t ,                       (I.4.1)
                                                       P#

where NK,s,t is the matrix P # with rows TK ∪ {k + s} and columns TK ∪ {k + t} deleted.

I.4.2    Exact evaluation of the entries
Throughout we set κ := |K| ≤ 2(a − 1), and we freely identify [M ] = {1, . . . , M } with ZM via
u 7→ u mod M (legitimate because every quantity ω γu depends only on u mod M ).


                                                     8
Lemma I.4.2 (Factorization). Let K ⊆ I1 ∪ I2 with κ = |K| ≤ m − 1, and let s, t ∈ [M ]. Then
                                                             !                          !
                                    X         Y                 X        Y
   perm(NK,s,t ) = (m − 1 − κ)!                   ω g(i)π(i)                  ω h(i)ρ(i) ,
                                        π: K,→[M ]\{t} i∈K           ρ: K,→[M ]\{s} i∈K

where both sums range over injections (an empty set of injections, which occurs when κ > M −1,
contributes the value 0; for K = ∅ each sum equals 1).
Proof. The rows of NK,s,t are indexed by K ⊔ {k + u : u ∈ [m] \ {s}} and its columns by
K ⊔ {k + v : v ∈ [m] \ {t}}. Consider a bijection φ from rows to columns whose associated
product of entries is nonzero.
    A top row i ∈ K has nonzero entries only in columns k +v with v ≤ M and v ̸= t (the top-left
block of P # is zero, and the top-right cross entries vanish for v > M ). Hence the restriction of
φ          rows in K determines an injection π : K ,→ [M ] \ {t}, contributing the entry product
Q to theg(i)π(i)
  i∈K  ω          .
    Dually, a top column i ∈ K can only be hit by a bottom row k + u with u ≤ M and u ̸= s
(again the top-left block is zero and the bottom-left cross entries vanish for u > M ). Hence the
restriction of φ−1 to the columns in K determines an injection ρ : K ,→ [M ] \ {s}, contributing
         h(i)ρ(i) .
Q
  i∈K ω
    The bottom columns used by π and the bottom rows used by ρ are independent resources;
after they are fixed, the remaining m − 1 − κ bottom rows must be matched bijectively with the
remaining m − 1 − κ bottom columns, and every such matching lies inside the all-ones block,
contributing a factor 1. There are (m − 1 − κ)! matchings. Conversely, every triple (injection π,
injection ρ, bijective completion) arises from exactly one bijection φ with nonzero entry product.
Summing the products over all φ gives the stated identity.

   The two injection sums are completely decoupled, and each is evaluated in closed form by
the following character computation, which is the heart of the proof.
Lemma I.4.3 (Character collapse). Let M ≥ 2, let ω ∈ C be a primitive M -th  Proot of unity, let
K be a finite set with integer weights (γi )i∈K , and put κ = |K| and σ(B) := i∈B γi . Assume
                      σ(B) ̸≡ 0   (mod M )         for every nonempty B ⊆ K.                   (I.4.2)
Then κ ≤ M − 1, and for every t ∈ ZM ,
                          X         P
                                   ω i∈K γi π(i) = (−1)κ κ! ω t σ(K) .
                          π: K,→ZM \{t}

Proof. First, (I.4.2) forces κ ≤ M − 1: order K as i1 , . . . , iκ and consider the κ + 1 prefix sums
0, γi1 , γi1 +γi2 , . . . ; if κ ≥ M , two of them would be congruent modulo M , and the corresponding
nonempty block B = {ip+1 , . . . , iq } would satisfy σ(B) ≡ 0 (mod M ).
    Work in the C-algebra
                                         S := C[xi : i ∈ K]/(x2i : i ∈ K),
                                      Q
which has C-basis {xB := i∈B xi : P               B ⊆ K}; write [xB ] for the operator extracting the
coefficient of xB . For u ∈ ZM set Lu := i∈K xi ω γi u ∈ S.
(a) Injection sums are coefficients. For any subset E ⊆ ZM ,
                                  Y                X     P
                            [xK ]     (1 + Lu ) =       ω i∈K γi π(i) .
                                  u∈E                  π:K,→E


                                                   9
Indeed, expanding the product, each factor indexed by u contributes either 1 or a single term
xi ω γi u ; the coefficient of xK collects exactly those choices in which each i ∈ K is selected
precisely once, necessarily at pairwise distinct values of u, i.e. the injections π : K ,→ E (with
π(i) the index of the factor contributing xi ).
(b) The full product equals 1. Let P := u∈ZM (1 + Lu ). The assignment xi 7→ ω γi xi extends
                                             Q
to an algebra automorphism of S which maps Lu to Lu+1 ; it therefore permutes the factors of
P cyclically and fixes P . On the other hand it multiplies the coefficient of xB by ω σ(B) . Hence
[xB ]P = ω σ(B) [xB ]P for every B, so [xB ]P = 0 whenever σ(B) ̸≡ 0 (mod M ), which by (I.4.2)
is the case for every nonempty B. Since [x∅ ]P = 1, we conclude P = 1 in S.
(c) Dividing out one factor. The element Lt is nilpotent with Lκ+1      t   = 0 (everyPmonomial of
degree κ + 1 in the xi repeats a variable), so 1 + Lt is invertible with (1 + Lt )−1 = κr=0 (−1)r Ltr .
Therefore
                           Y                                     X κ
                                 (1 + Lu ) = (1 + Lt )−1 P =         (−1)r Ltr .
                          u∈ZM \{t}                                      r=0

Extracting [xK ], only the term r = κ contributes, and by the multinomial expansion (all κ!
orderings of the κ distinct variables)
                                              Y
                               [xK ] Lκt = κ!   ω γi t = κ! ω tσ(K) .
                                                       i∈K

Combining with (a) applied to E = ZM \ {t} yields the claim.

Corollary I.4.4 (Entries are scaled characters). Let K ⊆ I1 ∪ I2 be such that condition (I.4.2)
holds modulo M for both weight systems g|K and h|K . Then for all s, t ∈ [M ],

                                        = γK ω t σg (K)+s σh (K) ,      γK := (m − 1 − κ)! (κ!)2 > 0.
                            
        J TK , (k + s, k + t)
                                 P#

Proof. By Lemma I.4.3 (applied to the weights g|K ) we have κ ≤ M − 1 ≤ m − 1, so the
hypothesis of Lemma I.4.2 is satisfied. Combining (I.4.1), Lemma I.4.2, and Lemma I.4.3 —
once with weights g|K and excluded residue t, once with weights h|K and excluded residue s —
gives

                                                               κ      tσg (K)         κ      sσh (K)
                                                                                                  
          J TK , (k + s, k + t)         #
                                          = (m − 1 − κ)! · (−1)  κ! ω           · (−1)  κ! ω           ,
                                    P

and the two signs (−1)κ multiply to +1.

I.4.3     The arithmetic design
Encode subsets B ⊆ I1 ∪ I2 by the pair of integers
                      X                       X
               xB :=       2j−1 ,    yB :=         2j−1 ,                 xB , yB ∈ [0, 2a−1 ).
                         j: αj ∈B                       j: βj ∈B


The map B 7→ (xB , yB ) is a bijection onto [0, 2a−1 )2 , and by construction

                              σg (B) = xB + yB ,              σh (B) = xB + 2yB .


                                                         10
(F1) The weight system g never vanishes. For nonempty B we have 1 ≤ σg (B) ≤
2(2a−1 − 1) = M − 1, so σg (B) ̸≡ 0 (mod M ). Thus (I.4.2) holds for g on every K ⊆ I1 ∪ I2 .

(F2) Bad sets for h are large and few. Call a nonempty B ⊆ I1 ∪ I2 bad if σh (B) ≡ 0
(mod M ). Since 1 ≤ σh (B) ≤ 3(2a−1 −1) < 2M , badness is equivalent to xB +2yB = M = 2a −1.
Writing w(·) for the binary digit sum and using subadditivity w(p + q) ≤ w(p) + w(q) together
with w(2y) = w(y), a bad B satisfies
                  |B| = w(xB ) + w(yB ) ≥ w(xB + 2yB ) = w(2a − 1) = a.
Moreover the solutions of x + 2y = 2a − 1 with x, y ∈ [0, 2a−1 ) are exactly y ∈ [2a−2 , 2a−1 ) with
x = M − 2y; hence there are exactly 2a−2 bad sets.

(F3) The good family is large.         Let
                          G := {K ⊆ I1 ∪ I2 : no subset B ⊆ K is bad}.
Every K ∈ G satisfies (I.4.2) for g (by (F1)) and for h (by the definition of G). Each bad B is
contained in exactly 2(2a−2)−|B| ≤ 2a−2 subsets of I1 ∪ I2 , so by a union bound over the 2a−2
bad sets,
                             |G| ≥ 22a−2 − 2a−2 · 2a−2 = 34 22a−2 .
                                                                                        
(F4) Distinct character pairs. The map K 7→ σg (K) mod M, σh (K) mod M is injective
on subsets of I1 ∪ I2 . Indeed, u := σg (K) = xK + yK lies in [0, M − 1], so u is determined by its
residue; next, σh (K) − σg (K) = yK lies in [0, 2a−1 ) ⊆ [0, M ), so yK is the unique representative
in [0, M ) of the residue (σh (K) − σg (K)) mod M ; finally xK = u − yK , and (xK , yK ) determines
K.

I.4.4    Proof of the Key Lemma
Proof of Lemma I.4.1. Consider the submatrix of the Jacobian matrix of the family {cT }T ⊆[k] ,
evaluated at P # , with rows indexed by {TK : K ∈ G} and columns indexed by {(k + s, k + t) :
(s, t) ∈ [M ]2 }. By (F1), (F3) and Corollary I.4.4, the row corresponding to K ∈ G is
                        χK (s, t) := ω tAK +sBK ,
                                                                                
          γK · χ K ,                                (AK , BK ) := σg (K), σh (K) mod M,
with γK > 0. As (s, t) ranges over [M ]2 ∼        = ZM × ZM , the function χK is exactly the charac-
ter (s, t) 7→ ω tAK +sBK of the group Z2M , evaluated at all group elements. By (F4) the pairs
(AK , BK ), K ∈ G, are pairwise distinct, so the χK are pairwise distinct characters of Z2M ;
distinct   characters of a finite abelian group are linearly independent over C (orthogonality:
              t)χ′ (s, t) = M 2 δχ,χ′ ). Hence the displayed submatrix has rank |G| over C, and there-
P
   (s,t) χ(s,
fore some |G| × |G| minor of it is nonzero.
     That minor is the evaluation at the point P # of the corresponding |G| × |G| minor of the
Jacobian matrix of the family {cT }, which is a polynomial in the variables Z with integer
coefficients. Being nonzero at a point of Q(ω)|Z| , it is a nonzero polynomial, and hence nonzero
over every characteristic-zero field F (Remark I.1.2). By Lemma I.1.1 the |G| polynomials cTK ,
K ∈ G, are algebraically independent over F. Using (F3) and 2a > m+1        2 we conclude

        τn (k) ≥ |G| ≥ 34 · 22a−2 = 16
                                    3
                                       (2a )2 ≥ 64
                                                3
                                                   (m + 1)2 = 64
                                                              3
                                                                 (n − k + 1)2 ≥ 256
                                                                                 3
                                                                                    n2 ,
the last inequality because n − k + 1 > n − k ≥ n/2 for k ≤ n/2.

                                                 11
I.5    Assembly: proof of the Theorem
Proof of the Theorem. Let n ≥ max(n0 , 212 ) and set k := ⌈2 log2 n⌉ + 4; then 2 log2 n + 4 ≤ k ≤
n/2. Apply Corollary I.2.2 to f = permn with the partition of the n2 variables into the p0 =
n⌊n/k⌋ arc blocks of Section I.3 together with the residual cells (taken, say, as singleton blocks),
and with G the set of arc blocks. Each arc block consists of k cells in pairwise distinct rows
and pairwise distinct columns, so by Lemma I.3.1 and Lemma I.4.1 its associated transcendence
                         3                                                        3            1
degree is τi = τn (k) ≥ 256 n2 . Hence, using ⌊n/k⌋ ≥ n/(2k) for k ≤ n/2 and 256     n2 − 2 ≥ 100 n2
for all large n,
                                 3                 n     1
                                   n2 − 2                   n2
                                          
                                                                  n4
                                                                              4 
                            p0 256             n · 2k · 100                     n
              L(permn ) ≥                   ≥                  =       = Ω             ,
                                   4                  4          800 k         log n

because k = Θ(log n). Since n4 / log n = ω(n3 ), this proves the Theorem.

   For completeness of the picture, Ryser’s formula

                                                  X              n X
                                                                 Y
                                            n              |S|
                             permn = (−1)               (−1)               xij
                                                ∅̸=S⊆[n]         i=1 j∈S


is a depth-3 formula of size O(n2 2n ), so L(permn ) = 2O(n) . Thus
                                 4 
                                    n
                               Ω            ≤ L(permn ) ≤ 2O(n) .
                                   log n

I.6    Remarks
Remark I.6.1 (Where the hypotheses are used). Characteristic zero enters three times: in
Lemma I.1.1 (the minimal-degree differentiation argument), in Remark I.1.2 (so that evalua-
tions in Q(ω) certify nonvanishing over F), and through the positivity of the factorial factors
γK = (m − 1 − κ)! (κ!)2 in Corollary I.4.4: over a field of small positive characteristic these
factorials could vanish and the certificate would be destroyed.
Remark I.6.2 (The argument is genuinely permanental). For the determinant, the analogue of
the factor (m − 1 − κ)! in Lemma I.4.2 is the signed sum over the completions inside the all-ones
block, i.e. up to sign the determinant of an all-ones block, which vanishes as soon as m−1−κ ≥ 2
— and in the range of parameters used above one always has m − 1 − κ ≥ m − 1 − 2(a − 1) ≥ 2.
Every entry of the analogous certificate would therefore vanish at P # , and the certificate would
be destroyed. The positive sum over the (m − 1 − κ)! completions inside the all-ones block —
precisely where the determinant would cancel — is the permanental leverage of the argument.
                                                                 P
Remark I.6.3 (The ceiling of the   P measure).    The  measure     blocks td(coefficient family) used
in Corollary I.2.2 is capped by i min 2|Yi | , n2 , which over all partitions of the n2 cells is
                                                    

O(n4 / log n), attained by blocks of size Θ(log n). The bound proved here therefore matches, up
to constants, the largest bound this measure can yield for the permanent.
Remark I.6.4 (An upper bound on τn (k)). The quantity τn (k) obeys the upper bound

                        τn (k) ≤ n2 − k − (2n − k − 2) = (n − 1)2 + 1.


                                                   12
Indeed the coefficient family {cT } is preserved by the (2n − k − 1)-dimensional torus action
                                                           Q
                      xab 7→ λa µb xab : λi µi = 1 (i ≤ k),   a>k λa µa = 1 ,

which acts on the space of Z-variables over F with generic orbits of dimension 2n − k − 2, forcing
the generic fibers of the coefficient map to have dimension at least 2n − k − 2. In the range
                                       3
k ≤ n/2 used above, the lower bound 64   (n−k +1)2 of Lemma I.4.1 is therefore within a constant
factor of optimal. This upper bound is not needed for the Theorem.


Part II
Circuit size: C(permn) = Ω(n2 log log n)
Overview and roadmap
Problem. Let F be a field of characteristic zero. An arithmetic circuit over F in the variables
x1 , . . . , xm is a directed acyclic graph whose sources are labelled by variables or field constants
and whose internal nodes are labelled + or × (fan-in two, fan-out unrestricted, no division); its
size is the number of internal nodes. For n ≥ 1 let C(permn ) denote the minimum size of an
arithmetic circuit computing
                                                    X Y  n
                                        permn (x) =         xi,σ(i) .
                                                     σ∈Sn i=1

Is C(permn ) = ω(n2 )?
This part gives an unconditional proof of the following explicit form.

Theorem. Over every field of characteristic zero,

                                    n2 log2 log2 n
                   C(permn ) ≥                            for all sufficiently large n;
                                         500
in particular C(permn ) = ω(n2 ).

Roadmap. The proof has the following layers: the transfer to isolated-point counting (§II.1–
§II.2, Baur–Strassen together with the Strassen degree bound); the explicit valuated design and
its exact tight-class analysis (§II.3–§II.4); lifting from initial systems to the permanental sec-
tion (§II.5); the single-band counting machinery (§II.6) — orbit seeds, Euler–Jacobi universality
(Theorem U), and the certificate theorem Cert(β), whose core is the bare-window Jacobian the-
orem Dβ ̸≡ 0, proved by an s = 0 specialization and a row-graded block triangularization with
closed-form level blocks; the equivariant aligned Count Lemma (§II.6.5), which converts one non-
degenerate arranged window into ((β!)!)s isolated points of a single fiber; and the stacked-band
assembly (§II.7): Theorem II.7.1 (stacked tight classes), Proposition B (generic smoothness),
and Theorem II.7.2 (band decoupling by scaling), which multiply the single-band count across
B = ⌊n/(3(β + 2))⌋ bands.


                                                     13
Why the windows are aligned. A natural but flawed route would select, at a fixed band
length q, an orbit count s∗ ∈ [q/(2β!), q/β!] dodging the finite bad set B(β). Since
                            q − β + 1 − s∗ β! ≡ q − β + 1     (mod β!)
can never be driven to 0 by the choice of s∗ alone, this leaves Θ(q) unused full (“reservoir”)
columns inside the window, whereas the certificate Cert(β) is proved exactly for windows con-
sisting of s complete orbit blocks plus bare head/tail — and its mechanisms genuinely fail in the
presence of reservoir columns (incomplete root ensembles break Theorem U’s product formula;
the s = 0 specialization no longer collapses to Dβ ; idle columns v = 0 are rank-1 degenerate in
their own-cell jet, and the coupling matrix C(v) diverges as v → 0). The proof below removes
the mismatch by inverting the quantifiers: the orbit count s∗ ∈ / B(β) is chosen first, and every
                                                 ′    ∗
band is then instantiated at the aligned length q = s β! + β − 1, so that the full columns number
exactly s∗ β! and every instantiated window has zero reservoir columns. Thus Cert(β) is invoked
strictly within its proved scope. The band length is a free design parameter (every statement
in §II.3–§II.5 and §II.7 is parametric in q), so the only costs are a factor ≤ 2 in the per-band
column budget and an additive sweep loss, both absorbed into the final constant. The choice is
possible because B(β) is finite with an explicit cardinality bound — no bound on the location
of its elements is needed, since the candidate interval for s∗ grows linearly with the budget Q
while |B(β)| is independent of Q (§II.6.5).

Conventions. Throughout, K denotes the algebraic closure of F0 (τ ) with F0 = Q, equipped
with the τ -adic valuation v (normalized by v(τ ) = 1), valuation ring R and residue field k0 = Q.
Since any circuit over F is a circuit over an extension of F containing K’s ingredients, and permn
has rational coefficients, it suffices to prove the lower bound for circuits over K (base change
can only decrease circuit size).


II.1     Baur–Strassen
Lemma II.1.1. If f ∈ K[x1 , . . . , xN ] has a circuit of size s, then there is a circuit of size at
most 5s computing f and all N partial derivatives ∂f /∂xi simultaneously.
Proof. We induct on s. For s = 0, f is a variable or a constant. For s ≥ 1 pick a bottom gate
g = u ◦ v (with u, v sources). Replace g by a fresh variable y: the new circuit has size s − 1
and computes a polynomial f ′ with f = f ′ (x, g(x)). By induction there is a circuit D′ of size at
most 5(s − 1) computing f ′ and all its partials. Build D as follows: one gate recomputes g and
feeds every former use of y; then
                                 ∂f    ∂f ′      ∂f ′    ∂g
                                     =         +       ·    ,
                                 ∂xi   ∂xi y=g   ∂y y=g ∂xi
and ∂g/∂xi ̸= 0 for at most the two labels u, v, with ∂g/∂u ∈ {1, v} and ∂g/∂v ∈ {1, u} (treating
u, v as the two formal input wires; if they coincide as variables, only one correction is needed
and the count only improves). The corrections cost at most 4 gates (at most 2 products and at
most 2 sums). The total is at most 5(s − 1) + 5 = 5s.

   Applied to permn : by multilinearity,
                                ∂ permn
                                        = Φij (X) := perm X ij ,
                                                           bb
                                  ∂xij

                                                14
the (i, j) permanental cofactor. Hence a size-s circuit for permn yields a circuit with at most 5s
                                                    2       2
internal nodes computing the cofactor map Φ : An → An .


II.2     Strassen’s degree bound and the master inequality
For an affine variety V (pure-dimensional or not), deg V denotes the sum of the degrees of
its irreducible components. We use three standard facts over an algebraically closed field of
characteristic zero.

(F1) If V is irreducible and h has degree d with V ̸⊆ {h = 0}, then deg(V ∩ {h = 0}) ≤ d deg V
     (the sum being over all components; Bézout in the refined form, e.g. [3, §8.4] or [2, Lemma
     8.28]).

(F2) For an affine-linear map π, deg π(V ) ≤ deg V .

(F3) For any affine-linear subspace W , the number of points isolated in V ∩ W is at most
     deg V (apply (F1) repeatedly to the hyperplanes cutting out W : at each step each com-
     ponent either lies inside the hyperplane or is cut properly, and isolated points of the final
     intersection are components).

Lemma II.2.1. Let a circuit with m product gates compute polynomials f1 , . . . , fk . Then W =
{(x, f (x)) : x ∈ K N } is closed, irreducible, of dimension N , and deg W ≤ 2m .

Proof. Introduce a variable zg per product gate, in topological order. Every wire value is an
affine-linear combination of 1, x, z<g (sum gates preserve this). Let V ⊆ AN +m be cut out by the
m quadratic equations zg − Pg Qg = 0 with Pg , Qg affine-linear in (x, z<g ). The projection to x is
an isomorphism onto AN (the gate semantics determine z), so V is irreducible of dimension N .
Cutting the quadrics in topological order, each intermediate locus is the graph of a polynomial
map AN +m−j → Aj , hence irreducible and not contained in the next quadric; so by (F1) iterated,
deg V ≤ 2m . Each fi is an affine-linear function on V ; now apply (F2) to (x, z) 7→ (x, λ(x, z))
with λ = (f1 , . . . , fk ).
                                                                       2
Corollary II.2.2 (master inequality). Let Γn = {(X, Φ(X))} ⊆ A2n over K. For every affine-
                       2
linear subspace W ⊆ A2n ,
                                      1
                       C(permn ) ≥    5 log2 #{isolated points of Γn ∩ W }.

Proof. Combine Lemma II.1.1, Lemma II.2.1 and (F3).

   Everything below constructs a subspace W with many isolated points.


II.3     The design
Fix a window size β and a block count q; the single-band design below is the building block,
stacked to full density in §II.7 (where the final parameters are fixed). All weights are integers
and all units positive rationals. We index rows and columns by disjoint intervals of [n] in the
following roles (any placement with the stated disjointness works; the sizes add up to at most n
for β = q = n/10):


                                                15
   • battery rows W = {r1 , . . . , rβ };

   • battery columns / zone rows Z = {z1 , . . . , zβ+q }: the column zr+j carries the battery cell
     of block j in row r (see below), and the matrix row with the same index z is a zone row ;

   • pool rows P = {p1 , . . . , pβ+2 };

   • target rows Tρ = {ρ1 , . . . , ρq } and target columns Y = {y1 , . . . , yβ }.

Battery. Block j ∈ [q] consists of the β cells br,j := (rr , zr+j ), r = 1, . . . , β. (Thus block
j’s columns are z1+j , . . . , zβ+j ; two cells share a column iff r + j = r′ + j ′ , and then they lie in
different rows, so the transversal monomials below take at most one cell per row and per column.)
The slice variables ur,j sit at these cells with τ -weights µ ≡ −5: on the slice, xbr,j = τ −5 ur,j .

Anchor P ◦ (τ ).    All other cells are as follows (an absent cell is a structural zero):

   • base: (i, i) for every i ∈ [n], weight 0, unit 1;

   • uplinks: (z, p) for z ∈ Z, p ∈ P : weight 2, unit 1;

   • services: (p, x) for p ∈ P , x ∈ W : weight 3, unit wp , the wp being pairwise distinct positive
     rationals;

   • card-uplinks: (yℓ , p) for ℓ ∈ [β]: weight 2 if p = pℓ (the designated card station q(yℓ ) := pℓ ),
     else weight 9; unit 1;

   • rooted pickups: (z1+j , ρj ) for j ∈ [q]: weight 5, unit 1 (so z1 is never used as a battery
     column or pickup row; this slack is harmless);

   • station-to-target-rows: (p, ρj ): weight 9, unit wp .

The section W . This is the affine subspace to be fed into Corollary II.2.2: freeze x at P ◦ (τ )
off the battery; put xbr,j = τ −5 ur,j (an affine parametrization of the slice); and pin the outputs

                              Φρj , yℓ (X) = γj,ℓ τ 5 ,     j ∈ [q], ℓ ∈ [β],
                                                                                        2
with γj,ℓ ∈ k0 to be chosen (Lemma E). This is an affine-linear subspace of A2n
                                                                             K : it consists of
n2 − βq coordinate pins on X, an affine chart on the battery, and βq coordinate pins on the
Y -coordinates.


II.4     Exact tight-class analysis
For a target t = (ρj , yℓ ) and a transversal battery set A (that is, |A| = k ≤ β, with distinct rows,
distinct columns, and rows and columns distinct from those of t — automatic here), define

  coef(t, A) := perm P ◦ with rows/cols of {t} ∪ A deleted, all remaining battery cells → 0 ,
                                                                                                   

                                               −5|A| uA .
                            P
so that on the slice Φt =     A coef(t, A) τ

Theorem II.4.1 (tight classes). With the design of §II.3:

                                                     16
  1. v(coef(t, A)) − 5k ≥ 5 for every A, with equality if and only if k ≥ 1 and z1+j ∈ cols(A);

  2. in the tight case the initial coefficient (the coefficient of τ 5k+5 in coef(t, A), equivalently of
     τ 5 in coef(t, A) τ −5k ) equals
                                                                          
                              cℓ,k = wpℓ k! (k − 1)! ek−1 {wp }p∈P \{pℓ } > 0,

     independently of which tight A (of size k) is taken;

  3. the β × β matrices C (j) = (cℓ,k )ℓ,k are invertible (and do not depend on j).
Proof. Write the minor as base-diagonal plus corrections. Deleting the rows {ρj } ∪ rows(A)
and the columns {yℓ } ∪ cols(A) leaves a matrix in which every remaining row has its base cell
except the displaced rows S = {yℓ } ∪ cols(A) (their base columns are deleted; recall that deleting
column z displaces row z, and deleting column yℓ displaces row yℓ ), and every remaining column
is covered by its base cell except the unclaimed columns T = {ρj } ∪ rows(A). A permutation
contributing to the minor is the base matching outside a correction: a bijection from S to T
realized by chains of designed non-base cells.
    The designed support allows exactly the following moves: a zone row z may go to a pool
column p (uplink; then row p is displaced onto the services/station cells); a pool row p may go
to a column in W or to a column ρj ; the row yℓ may go to a pool column; and the zone row z1+j
may go directly to column ρj . Rows in W have no non-base cells, and no other row is displaced,
so corrections never pass through them; consequently every correction decomposes into disjoint
chains of length one or two:

yℓ → p → x    (x ∈ rows(A)),       z → p → x,           z → p → ρj ,      yℓ → p → ρj ,      z1+j → ρj .

The weights are: 2 + 3 = 5 for the first two types; 2 + 9 = 11 for the third and fourth; 5 for the
fifth; and yℓ → p costs 2 only for p = pℓ (else 9). The correction must match S = {yℓ } ∪ cols(A)
(of size k + 1) onto T = {ρj } ∪ rows(A). The column ρj can be reached only by the pickup
(cost 5, requiring z1+j ∈ S, i.e. z1+j ∈ cols(A)) or through a station (cost 11). Hence the
minimum total weight is 5(k + 1), achieved precisely when z1+j ∈ cols(A), via: the pickup; the
chain yℓ → pℓ → x for some x ∈ rows(A); and the remaining k − 1 zone rows routed through
pairwise distinct stations ̸= pℓ onto the remaining k − 1 unclaimed W -columns. If z1+j ∈/ cols(A)
(including the case k = 0), the minimum is at least 5k + 11 > 5k + 5 — a margin of at least
6. This proves (1), and shows that the minimum is attained only by the described matchings.
(Optimal corrections contain no cycles: every designed non-base cell has weight ≥ 2 > 0, so a
cyclic exchange strictly increases the weight; hence the optimal correction is a disjoint union of
source-to-sink chains, and the chain taxonomy above is exhaustive for tight chains — the type
yℓ → p → ρj has weight ≥ 11, hence is never tight — because W -rows and all remaining rows
carry no non-base cells.)
     Unit bookkeeping: the pickup and the card-uplink have unit 1; the card station pℓ serves one
of the k unclaimed W -columns (k choices, unit wpℓ ); the remaining k − 1 zone rows are matched
to a (k − 1)-subset Q ⊆ P \ {pℓ } of stations in one of (k − 1)! ways, and those
                                                                              Q stations serve the
remaining k − 1 unclaimed columns in one of (k − 1)! ways, contributing p∈Q wp . Summing
over Q gives

               cℓ,k = wpℓ · k · (k − 1)!2 ek−1 (wP \pℓ ) = wpℓ k! (k − 1)! ek−1 (wP \pℓ ).

All terms are positive, so there is no cancellation. This proves (2).

                                                   17
    For (3): the matrix C (j) has rows wpℓ k!(k − 1)! ek−1          (w \ wpℓ ); dividing
                                                                                       P row ℓ by wpℓ > 0 and
column k by k!(k − 1)! > 0 leaves E := ek−1 (wP \pℓ ) ℓ,k∈[β] . Suppose ℓ λℓ (row ℓ) = 0. Row
ℓ lists the coefficients of T |P |−1 , . . . , T |P |−β of Πℓ (T ) := p̸=pℓ (TQ+ wp ), so Σ := ℓ λℓ Πℓ has
                                                                       Q                         P
degree at most |P | − β − 1 = 1. Each Πℓ is divisible by G(T ) := p∈P \{p1 ,...,pβ } (T + wp ), which
has degree 2; hence G | Σ, and together with deg Σ ≤ 1 this forces Σ = 0, i.e.
                                            X Y
                                                  λℓ     (T + wpℓ′ ) ≡ 0.
                                         ℓ     ℓ′ ̸=ℓ
                                         Q
Evaluating at T = −wpm gives λm              ℓ′ ̸=m (wpℓ′ − wpm ) = 0, so λm    = 0 for all m, and E is
invertible.


II.5      Lifting
                                     P A
Theorem II.5.1. Let Nj,k (u) :=       u , the sum being over the transversal battery sets A with
|A| = k and z1+j ∈ cols(A) (the forced-column rook sums: identifying the cell br,j with the rook
square (row r, column r+j) on the staggered β×(β+q−1) board, Nj,k is the sum over placements
of k non-attacking rooks one of which stands in board-column 1 + j). Suppose u∗ ∈ k0βq satisfies
                                                      P                ∗
                           ∗) = γ
           P
             k cℓ,k Nj,k (u       j,ℓ (∀j, ℓ),   det  ∂   k cℓ,k Nj,k   ∂u (u ) ̸= 0.

Then W (§II.3) contains an isolated point of Γn ∩ W with u ≡ u∗ modulo positive valuation,
and distinct u∗ give distinct points. Consequently, by Corollary II.2.2,

        C(permn ) ≥ 15 log2 #{nondegenerate solutions of the forced-column rook system}.

Proof. On the slice, Gj,ℓ (u) := τ −5 Φ(ρj ,yℓ ) − γj,ℓ 5
                                                          
                                                     Pτ has coefficients in R by Theorem II.4.1(1),
and its reduction modulo the maximal ideal is k cℓ,k Nj,k (u) − γj,ℓ by Theorem II.4.1(2). The
reduced Jacobian at u∗ is invertible by hypothesis, so by Hensel’s lemma (the multivariate version
over the completion of R, after a finite extension if needed — K is algebraically closed, so all
lifts stay in K) there is a unique solution u ≡ u∗ . Its Jacobian determinant has valuation 0, in
particular is nonzero, so the point is a multiplicity-one, isolated solution of the square system
cutting out Γn ∩ W on the slice chart.

Complement II.5.2 (isolated suffices). If u∗ is merely an isolated solution of the reduced system
(possibly degenerate), the conclusion

                            #{isolated points of Γn ∩ W } ≥ #{such u∗ }

still holds.

Proof. Pass to a finite subextension L/Q(τ ) containing all coefficients of G and a lift ũ∗ of
u∗ , with discrete valuation ring R0 and completion R̂0 . Isolatedness of u∗ in the special fiber
means that the βq elements Gj,ℓ cut the regular local ring R̂0 [[u − ũ∗ ]] (of dimension βq + 1)
down to dimension 1, so they form a regular sequence and the quotient is finite flat over R̂0
(Weierstrass preparation); its generic fiber is thus nonempty of dimension 0. Equivalently, the
(uncompleted) localization (R0 [u]/(G))u∗ has dimension 1; by the dimension formula over the
universally catenary DVR R0 (with 0-dimensional special fiber at u∗ ), every minimal prime

                                                        18
through u∗ has generic fiber of transcendence degree 0 over L, i.e. is a closed point of V (G)L
with residue field finite over L. Each such point is an isolated K-solution of G = 0 (since
K ⊃ L), and by construction specializes to u∗ . Distinct u∗ give lifts with distinct reductions,
hence distinct K-points.
    Consequently Lemma E below may count merely isolated solutions.
Remark (extension to the stacked design of §II.7). Theorem II.5.1 and Complement II.5.2 are
statements about a pinned valuated section whose tight-class structure is known: the only inputs
are (1) integrality/valuation bounds for the scaled pin equations and (2) the identification of
the reduced (initial) system with the designed tight-class system, both supplied for the stacked
layout by Theorem II.7.1 in place of Theorem II.4.1 (with the stacked initial system — the
band-coupled forced-column rook system — in place of Nj,k ). The proofs go through verbatim;
we use them in §II.7 with the isolated nondegenerate solutions produced by Theorem II.7.2.


II.6     The Count Lemma
Let S(β, q) denote the number of isolated solutions of the forced-column rook system
                              Nj,k (u) = εj,k    (j ∈ [q], k ∈ [β]),
maximized over the targets ε (by Theorem II.4.1(3), the targets γ = Cε realize any ε; for the
lifting of §II.5 we use nondegenerate solutions).
Lemma E (Count Lemma, aligned form). There is an explicit q0 (β) ≤ β! 22β+5 β 10 such
that for every β ≥ 10 and every integer Q ≥ q0 (β) there exist an integer s∗ ≥ Q/(2β!) and an
aligned band length
                                  q ′ = s∗ β! + β − 1 ≤ Q
with
                log2 S(β, q ′ ) ≥ s∗ log2 (β!)! ≥     1                  1 ′
                                               
                                                      4 Q β log2 β   ≥   4 q β log2 β,
                     ∗
witnessed by ((β!)!)s isolated nondegenerate points in a single fiber of the forced-column rook
map N on the board of length q ′ . (The assembly in §II.7 uses one such q ′ per n; no claim is
made, or needed, for non-aligned lengths.)

II.6.1   The Structure Theorem
Re-index the cells by (row r, column c), setting Ur,c = ur,c−r : the board is the β × (q + β − 1)
diagonal band; transversal sets are partial non-attacking rook placements; and Nj,k sums the
placements of k rooks one of which stands in column j (columns β ≤ m ≤ q are full — they
carry β cells; smaller and larger ones are head and tail columns). For ∅ ̸= T ⊆ {0, . . . , β − 1}
let ∆T = c r∈T Ur,c (the aggregates; the 2β − 2 of them with |T | < β occur).
         P Q

Structure Theorem. With xr := Ur,m denoting the forced column’s cells, Möbius inversion
over the column-coincidence partition lattice gives the exact formula
                       X         X         XY
                                                   (−1)|B|−1 (|B| − 1)! ∆B − xB .
                                                                               
              Nm,k =      xr
                         r    |S|=k−1, S̸∋r π⊢S B∈π

    So each column’s equations involve only its own cells and the aggregates: the system is a
mean-field model with coupling rank at most 2β − 2, and the aggregates are symmetric functions
of the full columns’ cell vectors.

                                                19
II.6.2   The local system has degree exactly β!
As a polynomial in x (with thePaggregates frozen), the level-k equation has top form (−1)k−1 k! ek (x)
(by the exponential formula π⊢S B (−1)|B| (|B| − 1)! = (−1)|S| |S|!). Since e1 = · · · = eβ = 0
                                    Q
forces x = 0, the local system Fk (x; ∆) = εk has no solutions at infinity for any param-
eter values: it is a 0-dimensional complete intersection of multidegree (1, 2, . . . , β), of de-
gree
  Q exactly
         Q β!, with β! distinct simple roots for generic (∆, ε) (the Jacobian’s top form is
± k k! · r<s (xr − xs ) ̸≡ 0). In particular the per-column transfer rate is β!, and Bézout gives
the matching ceiling S(β, q) ≤ (β!)q .

II.6.3   Exact laws and small cases
One has S(β, 1) = (β − 1)! and S(β, 2) = β (boundary; full elimination). For β = 2 and all q
(proved by complete analysis of the branch patterns),
                                                         
                                             q−1      q−1
                                 S(2, q) = 2     −          .
                                                       2

This law is confirmed by exact Gröbner-basis counts at q = 2, . . . , 8: 2, 3, 5, 10, 22, 49, 107.
Further data: S(3, 3) = 15 and S(3, 4) = 107 (ratio 7.1 > 3! — the growth meets and initially
exceeds the per-column rate as the boundary dip fills in), and S(4, 3) = 89 (ratio 22 ≈ 4! at the
boundary).

6.3bis Dominance
The polynomial map N : Cβq → Cβq , u 7→ (Nj,k (u)), is dominant; hence its generic fiber count
equals its degree, and the number of isolated points of any fiber is at most that degree.

Proof sketch (uniform witness). Evaluate DN at the configuration x(c) = tc ζ (c-th column; ζ a
fixed generic vector with distinct nonzero coordinates) and let t → 0. Cross-entries ∂Nj,k /∂Ur,m
(for m ̸= j) carry a column-j cell, hence an extra factor t j relative to the diagonal entries
                      (¬j)
∂Nj,k /∂Ur,j = Bk−1 (¬r), whose leading t-term is the unique (k − 1)-rook assignment to the
largest-scale available columns — a nonzero product of distinct ζ-coordinates. The leading
form of each diagonal β × β block is a positive-diagonal rescaling of the delete-one matrix
(ek−1 (ζ \ ζr ))k,r , invertible by the divisibility argument of Theorem II.4.1(3); a weighted block-
triangular expansion then gives det DN ̸= 0 for small t.

    Combined with Complement II.5.2, the Count Lemma may therefore be proved by exhibiting,
for a single (arbitrary) target ε, many points that are merely isolated in their fiber ; nondegen-
eracy is not required anywhere downstream.

II.6.4   Orbit seeds, Euler–Jacobi universality, and the certificate
(a) Isolated points bound the degree. If some fiber of the polynomial map Φ = (Nj,k )
has M isolated points, then Φ is dominant and its generic fiber has at least M points: isolation
forces dominance via fiber dimension, and the local topological index of a holomorphic isolated
zero is at least 1, so nearby fibers meet each isolating ball (by continuity of the degree on balls
avoiding Φ(∂B)); now intersect with the dense locus of generic targets.


                                                 20
(b) Orbit seeds (no genericity needed). Call the aggregates symmetric if gT = γ|T | ; then
each local system F (·; g) is a symmetric polynomial system. For a ∈ Cβ with distinct coordinates
and η := F (a; g), the solution set of F (·; g) = η is exactly the Sβ -orbit of a: the orbit gives β!
distinct roots, and by §II.6.2 the total count with multiplicity is exactly β! for all parameters —
hence all roots are simple and all local Jacobians invertible, unconditionally.
    Multi-orbit seeds. For s ≥ 1 take base vectors a(1) , . . . , a(s) and let sβ! full columns
                                                                                         P Q carry, one
column per root, the s complete orbits, with head/tail cells 0. The orbit sums σ r∈T aσ(r) =
t!(β − t)!et (a) are symmetric, so the configuration’s aggregates are symmetric and consistency
holds identically. Setting ε := N (u∗ ), eachQ orbit’s columns share the common target (all roots
of one system take its value), so the group i Sβ! permuting each orbit’s columns preserves the
fiber: the fiber contains all ((β!)!)s arrangements, and isolation of one gives isolation of all.

(c) Euler–Jacobi universality. The nondegeneracy of an arranged point reduces (by Schur
complements and the implicit function theorem) to the invertibility of I + Σ with
                                    X
                               Σ=       W (ξm )A(ξm )−1 B(ξm )
                                        full m

(the coupling through the 2β − 2 aggregates) together with a head/tail factor. Summed over a
complete root ensemble, the coupling is a global residue with denominator the system Jacobian;
since the local system is a complete intersection of degrees 1, . . . , β with no zeros at infinity, the
Euler–Jacobi vanishing theorem kills all entries of grading |T | < |T ′ | and makes the diagonal
blocks universal — dependent on β only, Johnson-scheme operators. Hence
                                                 β−1
                                                 Y
                                                       det I + s Σuniv
                                                                       
                                 det(I + Σ) =                     (t)    ,
                                                 t=1

a polynomial in the orbit count s with value 1 at s = 0: the bad set B1 (β) of integers s is finite,
unconditionally, and computable.

(d) The certificate theorem. Nondegeneracy of an arranged point is equivalent (Lemma L,
Appendix C) to the nonsingularity of
                                                    
                                      I + Σ −Wh −Wt
                               M=                      ,
                                       BH   AH    0

and Cert(β) is the statement that the germ det M is not identically zero on the consistency
chart.
Certificate Theorem. Cert(β) holds for every β ≥ 2.
   (d1) Jets of F at x = 0, symmetric g. With
                              X Y
                   Pm (γ) :=         (−1)|B|−1 (|B| − 1)! γ|B|               (P0 = 1),
                                π⊢[m] B∈π

                                                            β−1
                                                                
one has Fk (0; g) = 0; ∂gB Fk (0; g) = 0; ∂xr Fk (0; γ) =   k−1 Pk−1 =: αk−1 ;
                                                                           
                                                                β − 1 − |B|
                                      / B] (−1)|B|−1 (|B| − 1)!
               ∂x2r gB Fk (0; γ) = [r ∈                                      P       ;
                                                                 k − 1 − |B| k−1−|B|

                                                   21
and ∂x2r xr′ Fk (0; γ) = −2[r ̸= r′ ] β−2
                                          
                                      k−2 Pk−2 . (Each monomial of Fk carries a cell prefactor xr ;
differentiate it and count the free partitions.)
    (d2) Schur form. For det(I + Σ) ̸= 0, block elimination of δg gives

                                            S = AH + BH RWh BH RWt , R := (I + Σ)−1 ,
                                                                      
       det M = det(I + Σ) · det S,

a β(β − 1)-square matrix on (head cells, tail cells).
    (d3) The formal one-seed family and the s = 0 specialization. Keep a (with distinct coordi-
nates) and the jet directions (Y, Z) transcendental, and take  P s identical orbit blocks of seed a:
the seed aggregates are γb (s) = s b!(β − b)!eb (a) and Σ = s σ C(σa; γ(s)), so that all entries of
M lie in O := Q(a, Y, Z)[s](s) (rational in s, regular at s = 0). Along the curve (y, z) = (κY, κZ)
the consistency fixed point
                                      X                    
                       ĝ = γ(s) + s       [ξσ (ĝ)] − [σa] + h(κY ) + t(κZ)
                                       σ

(here [v] := ( r∈T vr )T for v ∈ Cβ ) has a unique formal solution ĝ(κ) ∈ O[[κ]]: the local
               Q
root
  Q functions   ξσ are defined over O because det A(σa; γ(s)) is a unit of O (at s = 0 it equals
± k k! i<j (ai − aj ) ̸= 0, by Fk (x; 0) = (−1)k−1 k!ek (x)), and I + Σ is a unit of O (its deter-
         Q
minant is 1 at s = 0).
   At s = 0 the window is bare: ĝ = h(κY ) + t(κZ) exactly, R = I, and
                                                                       
                                                              (c′ )
     det S(κ) s=0 = det DF (κY, κZ),      F : (y, z) 7→ Fk χ ; ĝ(y, z) ′                    ,
                                                                                    c =1,...,β−1, k=1,...,β

          ′
where χ(c ) is the head column c′ padded by zeros,
                                       X Y                  X       Y
                          ĝB (y, z) =         yc,r +                      zc,r ,
                                      c: B⊆[0,c) r∈B      c: B⊆[c,β) r∈B

and the identification is the chain rule (∂ĝB /∂yc,r = (Wh )B,(c,r) , etc.). By quasi-homogeneity
(deg xr = 1, deg gB = |B|, every monomial of Fk having degree k), det DF is homogeneous of
degree dβ = β(β − 1)2 /2 and

                      det S(κ)|s=0 = κdβ Dβ (Y, Z),       Dβ := det DF (Y, Z),

the bare window Jacobian.
    (d4) Core Theorem: Dβ ̸≡ 0 for every β ≥ 2. The proof is the content of Appendix D below.
    (d5) Master reduction. If Dβ ̸≡ 0, then the κdβ -coefficient Ddβ (s) ∈ O has Ddβ (0) = Dβ ̸= 0
in Q(a, Y, Z), hence Ddβ ̸= 0 as a rational function of (s, a, Y, Z); its numerator P ∈ Q[s, a, Y, Z]
is nonzero, so B2 (β) := {s∗ : P (s∗ , ·) ≡ 0} is finite. For any integer s∗ ∈
                                                                             / B(β) := B1 (β) ∪ B2 (β),
generic numeric (a, Y, Z) give det S(κ) ̸≡ 0 on the identical-seed chart at s∗ , i.e. det M ̸= 0 at
chart points arbitrarily close to the seed. Finally, the admissible-seed parameter space (tuples
(a(i) ) with distinct coordinates and small (y, z)) is connected, I + Σ is invertible on all of it
(Theorem U’s diagonal blocks are seed-independent), and the germ is analytic there; by the
identity theorem, nonvanishing propagates from the identical-seed point to a generic admissible
seed. Hence for every integer s ∈     / B(β), arranged multi-orbit windows with s blocks admit
nondegenerate configurations: Cert(β) holds.


                                                  22
(e) Remarks.
Remark (why the s = 0 route). Along the uniform curve (y, z) = κ(Y, Z) at numeric s, the
germ det S(κ) vanishes to order Nβ = (β−1)(3β−4)     (anchors 0; head differences κ1 × β−1
                                                                                           
                                             2                                           2   ; tail
       1                                       2    β−1              1
                                                        
bases κ × (β − 1); tail same-row differences κ × 2 — the tail κ -coefficients depend only on
the row, not on the column); this vanishing order was confirmed by high-precision computation
at β = 3, 4. Moreover, since R commutes with the Sβ -action, the order-Nβ coefficient factors
through only five isotypic column-profiles, so its rank is at most 5(β − 1) < β(β − 1) for β ≥ 6:
the leading uniform-κ coefficient vanishes identically for large β, and a uniform-jet certificate
would need an unbounded cascade. The s = 0 specialization (d3) converts the whole cascade
into the single homogeneous Jacobian Dβ , and the row-graded degeneration (d4) resolves it in
one stroke — level k of the triangularization is precisely “grade k − 1 fed by (k − 1)-fold cell
products”.

II.6.5   The aligned Count Lemma (proof of Lemma E)
Throughout this subsection fix β ≥ 2 and an integer s ≥ 1, and put

                                        qs := s β! + β − 1.

On the staggered β × (qs + β − 1) board the full columns are exactly the qs − β + 1 = s β! columns
β ≤ c ≤ qs (1-indexed as in §II.6.1); the β − 1 head columns and the β − 1 tail columns are
partial. A window of aligned length qs carrying s complete orbit blocks therefore has no unused
full columns: it consists of exactly s complete orbit blocks plus bare head/tail — verbatim the
hypothesis class in which Cert(β) is proved in §II.6.4(d1)–(d5). (At a fixed board length q the
unused-column count r(s) = q − β + 1 − sβ! satisfies r(s) ≡ q − β + 1 (mod β!), so no choice of
s alone can make it vanish in general; aligning the board length to the orbit count, rather than
the other way around, is what eliminates reservoir columns.)

Lemma A (equivariant transport). Let q ′ = qs , let F = {c : β ≤ cQ≤ q ′ } be the set of full
columns, partitioned into blocks O1 , . . . , Os with |Oi | = β!, and let G = si=1 Sym(Oi ), of order
                           ′
|G| = ((β!)!)s , act on Cβq by whole-column content permutation,

                                      (ρ(π)u)r,c := ur,π−1 (c)
                                    S
(π extended by the identity off i Oi ; this is well-formed because blocks consist of full columns
only, all of which carry cells in all β rows). Let Pπ permute the equation blocks by the same π:
(Pπ v)(c,k) := v(π−1 (c),k) . Then:

  1. N ◦ ρ(π) = Pπ ◦ N for every π ∈ G;

  2. if the target ε is block-constant (ε(c,·) = η (i) for all c ∈ Oi and each i), then each ρ(π)
     maps the fiber N −1 (ε) bijectively onto itself;

  3. DN (ρ(π)u) = Pπ DN (u) ρ(π)−1 ; consequently ρ(π) carries isolated (respectively nonde-
     generate) points of the fiber to isolated (respectively nondegenerate) points;

  4. if for each i the β! column vectors {u∗·,c }c∈Oi are pairwise distinct, then the orbit ρ(G) u∗
     consists of exactly ((β!)!)s distinct points.


                                                 23
Proof. (1) By the Structure Theorem (§II.6.1), Nc,k (u) = Fk (u·,c ; ∆(u)) with one polynomial
Fk uniform over all columnsP Qc (partial columns being evaluated with absent cells = 0), and
the aggregates ∆T (u) = c r∈T ur,c are column sums, hence invariant under any permutation               
of full-column contents: ∆(ρ(π)u) = ∆(u). Therefore Nc,k (ρ(π)u) = Fk u·,π−1 (c) ; ∆(u) =
Nπ−1 (c),k (u) for c ∈ F, while the head- and tail-column equations are unchanged (π(c) = c and
∆ is invariant).
    (2) Block-constant targets satisfy Pπ ε = ε, so N (u) = ε implies N (ρ(π)u) = Pπ ε = ε; and
ρ(π) is a linear automorphism.
    (3) Differentiating (1) gives DN (ρ(π)u) ρ(π) = Pπ DN (u); both ρ(π) and Pπ are permutation
matrices, and a linear automorphism carrying a fiber onto a fiber preserves isolation, while (3)
gives | det DN (ρ(π)u)| = | det DN (u)|.
    (4) ρ(π)u∗ = ρ(π ′ )u∗ forces u∗·,π−1 (c) = u∗·,π′−1 (c) for all c; within-block distinctness then gives
π = π′.

Lemma B-card (cardinality of the bad set). For every β ≥ 2 the bad set B(β) = B1 (β) ∪
B2 (β) of §II.6.4 is finite, with the explicit cardinality bound

                                    |B(β)| ≤ D(β) := 22β+3 β 10 .

No bound on the location of its elements is asserted or needed.
Proof. The set B1 . By Theorem U, at an s-block seed the coupling is

                                Σ = s Σuniv + (strictly graded-lower),

and by graded block-triangularity
                                                         β−1
                                                         Y
                                                               det I + s Σuniv
                                                                               
                          det(I + Σ)|κ=0 = ∆0 (s) :=                      (t)    ,
                                                         t=1

a polynomial in s of degree at most G = 2β − 2 (the total size of the graded blocks) with
∆0 (0) = 1; hence ∆0 ̸≡ 0 and |B1 (β)| ≤ G.
    The set B2 . We bound the s-degree of the numerator P of the κdβ -coefficient Ddβ (s) of
det S(κ) in the identical-seed formal family of (d3). Recall from (d3) that every entry of the
family lies in the localization R∆ := Q(a, Y, Z)[s][∆0 (s)−1 ], and:
    (i) The seed local Jacobian determinant det A(a; γ(s)) is a nonzero constant in s: indeed γ(s)
is symmetric for every complex s, so by Lemma O (Appendix C) a is a simple root for every
s ∈ C, and a univariate polynomial with no complex zeros is a nonzero constant. Hence the
Taylor coefficients of the local root functions ξσ around the seed, and the entries of W, B, adj A
there, are polynomials in s, of degree at most β 2 per entry (each entry of A, B has at most β − 1
factors γb (s), each linear in s; each entry of adj A is a (β − 1)-minor).
                                                                             j
                                                                   P
    (ii) The fixed-point recursion for ĝ = γ(s) + δ, δ =            j≥1 δj κ , reads (I + Σ|κ=0 ) δj =
Φj (δ1 , . . . , δj−1 ; s) with Φj polynomial in the lower coefficients and in s; inverting I + Σ|κ=0
multiplies by adj(I + Σ|κ=0 )/∆0 (s), whose numerator entries have s-degree at most (G − 1)(β 2 +
1) + 1 ≤ cβ := 2β (β 2 + 2). By induction on j, δj = Pj (s)/∆0 (s)2j−1 with degs Pj ≤ j cβ β.
    (iii) The entries of the Schur matrix S(κ) are polynomial expressions in the (δj )j≤κ-order ,
the jets of AH , BH , Wh , Wt (polynomial in s of degree at most β 2 ) and one further factor R =
(I + Σ)−1 ; hence the κj -coefficient of every entry of S lies in R∆ with numerator degree at most
(j + 2) cβ β.

                                                    24
   (iv) Since det S is a β(β − 1)-fold sum of products,

              P (s, a, Y, Z)
  Ddβ (s) =                  ,        degs P ≤ β(β − 1) (dβ + 2) cβ β + eG,             e ≤ β(β − 1)(dβ + 2),
                 ∆0 (s)e

and with dβ = β(β − 1)2 /2 ≤ β 3 /2 one checks crudely that

                        degs P ≤ β 2 · β 3 · 2β (β 2 + 2) β + β 2 β 3 · 2β ≤ 22β+2 β 10 .

By (d4)–(d5), P ̸= 0 (its value at s = 0 is Dβ · (unit) ̸= 0), so the set B2 of integers s∗ with
P (s∗ , ·) ≡ 0 has at most degs P elements. Adding |B1 | ≤ G ≤ 2β gives the bound. (Any
explicit bound of the form 2O(β) β O(1) serves equally well: only log2 D(β) = O(β) enters the
assembly.)

Proof of Lemma E. Set q0 (β) := 2β! (D(β) + 3) ≤ β! 22β+5 β 10 ; all that is used downstream is
log2 q0 (β) ≤ log2 β! + 2β + 10 log2 β + 5. Let Q ≥ q0 (β).               
    Selection. The candidate interval IQ := ⌈Q/(2β!)⌉, ⌊(Q − β + 1)/β!⌋ contains at least

                        Q−β+1      Q          Q
                              −1−     −1+1 ≥     − 2 ≥ D(β) + 1
                          β!      2β!        2β!

integers, so it contains an integer s∗ ∈
                                       / B(β). Then q ′ := qs∗ = s∗ β!+β −1 ≤ Q and s∗ ≥ Q/(2β!).
    One nondegenerate arranged window. Since s∗ ∈       / B(β), Cert(β) — §II.6.4(d5), whose scope
is exactly the board of aligned length qs∗ , namely s∗ complete orbit blocks plus bare head/tail
and no other columns — provides a consistency-chart point with (y, z) = κ0 (Y, Z) ̸= 0 at
which det M ̸= 0. (The identical-seed chart point of (d5) already suffices; the identity-theorem
propagation to arbitrary admissible seeds is available but not needed here.) Explicitly, the
                                   ′
arranged configuration u∗ ∈ Cβq is: head/tail cells κ0 Y, κ0 Z; the β! columns of block Oi carry,
one each, the β! roots of the common local system F (·; ĝ) = η (i) , where ĝ = ĝ(κ0 ) is the
consistent aggregate vector of Lemma C and η (i) is the block target. By Lemma L, u∗ is an
isolated nondegenerate point of its fiber N −1 (ε), where ε := N (u∗ ).
    Equivariant multiplication. The target ε is block-constant by construction (every column of
Oi is a root of the single system with the single value η (i) , and the consistency of Lemma C
says precisely that the configuration’s true aggregates are ĝ, so Nc,· (u∗ ) = η (i) for c ∈ Oi ).
The β! roots of one local system are pairwise distinct (all roots are simple: Lemma O at the
seed, preserved on the chart by continuity of the simple roots and of det A), so within-block
                                                         ∗
distinctness holds. Lemma A now produces ((β!)!)s distinct isolated nondegenerate points in
the single fiber N −1 (ε):
                                                              ∗
                                         S(β, q ′ ) ≥ ((β!)!)s .
   Arithmetic. By Stirling, log2 (m!) ≥ m(log2 m − log2 e) with m = β!:

                                                                         Q
                   log2 S(β, q ′ ) ≥ s∗ β! (log2 β! − log2 e) ≥            (log2 β! − log2 e).
                                                                         2
For β ≥ 10 we have log2 β! ≥ β log2 β − β log2 e and 12 β log2 β ≥ (β + 1) log2 e (at β = 10:
16.6 ≥ 15.9, and the left-hand side grows faster), whence 12 (log2 β! − log2 e) ≥ 41 β log2 β and

                                 log2 S(β, q ′ ) ≥   1
                                                     4 Q β log2 β   ≥   1 ′
                                                                        4 q β log2 β.


                                                         25
Remark (why reservoir columns must be avoided). Fixing the board length q first and choosing
s∗ ∈ [q/(2β!), q/β!] \ B(β) would leave q − β + 1 − s∗ β! = Θ(q) unused full columns (“reservoirs”)
that Cert(β) does not cover: incomplete root ensembles break Theorem U’s product formula;
with reservoirs present the s = 0 specialization of (d3) no longer collapses det S to the bare-
window Jacobian Dβ ; and idle reservoir columns (v = 0) are rank-1 degenerate in their own-cell
jet (∂xr Fk (0; g) = αk−1 independently of r), with C(v) = W A−1 B divergent as v → 0, so no
openness argument can start there. The aligned selection above eliminates reservoir columns
identically.


II.7     Assembly: the stacked-band layout
The board of §II.3 is β × (q + β − 1), so a single band has at most nβ cells; density Θ(n2 )
therefore requires stacking bands. The following layout achieves it with all budgets honest.

Layout. Partition the row indices into Rbat (n/3), Rpool (n/3) and Rzone (n/3), and use the
column indices Cbat := Rzone (battery columns = zone-row indices) and Cpool := Rpool (station
columns = pool-row indices; targets live there). There are bands b = 1, . . . , B (the band count B
and the per-band block count q are fixed in the Budget paragraph below; q will be the aligned q ′ ).
Band b has battery rows Wb = {wb,0 , . . . , wb,β−1 } (β private rows of Rbat ), and its battery cells
are staggered : with the q + β − 1 active columns {z0 , . . . , zq+β−2 } ⊂ Cbat , the row wb,r carries the
cells (wb,r , zr+j ), j = 0, . . . , q − 1 — every band uses the same staggered β × (q + β − 1) diagonal-
band board of §II.3–§II.6, translated to the shared columns. (The staggering is essential, not
cosmetic: for the full-rectangle variant the initial system is positive-dimensional already at
(B, β) = (1, 3) and (2, 2), while the staggered board carries the exponential laws S(β, q) of
§II.6.) Band b further has a pool Pb (β + 2 private rows of Rpool ) with services (p, x) gated to
x ∈S Wb (weight 3, unit wp , all units distinct positive rationals); uplinks (z, p) for all z ∈ Rzone ,
p ∈ b′ Pb′ (weight 2, unit 1); base cells (i, i) everywhere (weight 0, unit 1); and battery weights
µ ≡ −5.
     Targets. For each band b, each of the q forced columns z ∈ {z0 , . . . , zq−1 } and each of β
designated stations p ∈ Tb ⊆ Pb , pin the cofactor at the cell (z, p): deleting the zone row z
unclaims column z (self-service forcing: only a battery monomial deleting column z can repair
it, since column z hosts no anchor cells besides its base), and deleting column p displaces the
station row p, which must then serve a Wb -column (band-gating). The number of equations is
B · q · β, equal to the number of variables.

Theorem II.7.1 (stacked tight classes). For the equation pinned at the cell (z, p) with p ∈ Tb ,
and a transversal battery set A, one has v(coef) + µ(A) ≥ θ := −2, with equality if and only if
z ∈ cols(A) and A ∩ (band b) ̸= ∅; the initial coefficients are positive sums with the delete-one
Vandermonde structure through wp and the per-band pools.

Proof (taxonomy, as in Theorem II.4.1). Deleting the row z, the column p, and the rows and
columns of A leaves: displaced rows = (the zone rows indexed by cols(A) \ {z}, since the target’s
row deletion removed the zone row z itself if z ∈ cols(A), else column z is unclaimed with no
nonzero entry, i.e. is a zero column — see below) ∪ (the station row p); unclaimed columns
= rows(A) (battery-row base columns) ∪ (column z, if not deleted by A). Non-base cells exist
only on zone rows (uplinks) and pool rows (services, band-gated), so every correction chain


                                                   26
has length at most 2 and is band-pure; and optimal corrections contain no cycles (all designed
weights are positive).
    Column z hosts no anchor cells except its base (whose row is deleted): if z ∈     / cols(A) the minor
has a zero column and the coefficient vanishes (valuation +∞) — the self-service forcing. The
displaced station p can serve only Wb -columns, which are unclaimed only if Ab ̸= ∅; otherwise
p has no non-base sink and the coefficient vanishes (valuation +∞). When both conditions
hold, the minimum-weight correction matches: the station p to one of the |Ab | unclaimed Wb -
columns, and each remaining displaced zone row through a distinct station of some band’s pool
(minus p for band b) to an unclaimed W -column of that band; the cost is 3 + 5(|A| − 1), so that
v(coef) + µ(A) = 3 + 5(|A| − 1) − 5|A| = −2 = θ, uniformly, with every minimal matching’s unit
product positive. Summing gives the exact coefficient law
                                              h
                              K −1                                             i Y
    c(A; b, p) = wp ·                          · kb (kb − 1)!2 ekb −1 (wPb \p ) ·   (kb′ !)2 ekb′ (wPb′ ),
                         kb − 1, (kb′ )b′ ̸=b                                     ′  b ̸=b
              P
where K =      kb′ and the multinomial counts the allocations of the K − 1 interchangeable
displaced zone rows to the bands’ sink groups — an exponential-generating-function product
across bands. All terms are positive.

Level separation. Fix (b, z). The β equations {(b, z, p)}p∈Tb have coefficients wp kb (kb −
1)!2 ekb −1 (wPb \p ) · (a factor independent of p); the β × β matrix

                                  V (b) := wp ℓ! (ℓ − 1)! eℓ−1 (wPb \p ) p,ℓ
                                                                       


is the delete-one generalized Vandermonde of §II.4, invertible for distinct positive units. So the
system is equivalent to the level-separated system: for each band b, forced column z and level
ℓ ∈ {1, . . . , β},
                                                              Y
      (b)
                            X                   K −1
    Gz,ℓ (x) :=                                                   (kb′ !)2 ekb′ (wPb′ ) xA = εb,z,ℓ ,
                                            ℓ − 1, (kb′ )b′ ̸=b ′
                 A transversal, z∈cols(A), |Ab |=ℓ                  b ̸=b

where Ab′ is A’s part on band b′ ’s staggered board, kb′ = |Ab′ | and K = |A|. Every monomial of
 (b)
Gz,ℓ has xb -degree exactly ℓ and xb′ -degree kb′ ≥ 0; the terms with all kb′ = 0 have coefficient
                                                                               (b)
1 and are exactly the pure single-band forced-column rook sums Nz,ℓ (xb ) of §II.6 on band b’s
staggered board.

Theorem II.7.2 (band decoupling by scaling). Suppose the single-band forced-column rook
system {Nz,ℓ (y) = δz,ℓ } on the staggered β × (q + β − 1) board has, for generic targets δ, at least
S isolated nondegenerate solutions. Then there is a choice of pin initial values for which the
coupled stacked system has at least S B isolated nondegenerate solutions.

Remark (where the hypothesis comes from). It is supplied by §II.6.5 together with the following
standard proposition, applied to the forced-column rook map N = Nq′ on the aligned board:
                                                ∗
the aligned Count Lemma produces S = ((β!)!)s isolated nondegenerate points in one fiber; by
Proposition A the map is dominant of degree ≥ S; Proposition B then gives a dense open set of
targets over which all deg N ≥ S solutions are nondegenerate.


                                                     27
Proposition B (generic smoothness supplier). Let Φ : Cm → Cm be a polynomial map,
some fiber of which contains M isolated points. Then there is a dense Zariski-open U ⊆ Cm ,
defined over any field of definition of Φ, such that for every y ∈ U the fiber Φ−1 (y) consists of
                                                                                                m
exactly deg Φ ≥ M points, at each of which det DΦ ̸= 0. In particular U contains points of Q
when Φ is defined over Q.

Proof. By Proposition A (Appendix C), Φ is dominant and its generic fiber has deg Φ ≥ M
points. Dominance in equal dimensions makes C(t) ,→ C(u) (with ti := Φi ) an algebraic, finitely
generated — hence finite — field extension, separable because the characteristic is zero. By
upper semicontinuity of fiber dimension (Chevalley) there is a dense open V1 of the target over
which all fibers are finite; by generic smoothness in characteristic zero ([5, Cor. III.10.7], applied
to the dominant morphism Φ : Am → Am of smooth varieties) there is a dense open V2 over
which Φ is a smooth morphism; over V1 ∩ V2 , smoothness of relative dimension 0 means exactly
that DΦ is invertible at every preimage. Finally, shrinking to a dense open U ⊆ V1 ∩ V2 over
which Φ restricts to a finite morphism (spread out the integral closure of C[t] in C(u): it is a
finite module over a localization C[t][1/f ]), the restriction is finite and étale onto the irreducible
base U , so every fiber has exactly [C(u) : C(t)] = deg Φ points. All the loci above are cut out
by polynomials with coefficients in the field of definition, and a dense Zariski-open subset of Am
                                            m
defined over Q contains Q-points since Q is Zariski dense.
                                                                                      (b)
Proof of Theorem II.7.2. Choose generic per-band targets δ (b) = (δz,ℓ ) and scaling parameters
                                                                                     (b)
s = (s1 , . . . , sB ), and set the level-separated targets εb,z,ℓ := sbℓ δz,ℓ (equivalently, pin initial
        P (b) (b)                                                                            (b) (b)
values ℓ Vpℓ sℓb δz,ℓ , which are nonzero for all small sb ̸= 0 since the leading term sb Vp1 δz,1 ̸= 0).
Substitute xb = sb yb and divide the (b, z, ℓ) equation by sbℓ : since every monomial carries xb -
degree exactly ℓ and xb′ -degree kb′ , the rescaled system (writing cA for the coefficient of xA in
  (b)
Gz,ℓ ) is
                                                          Y            
                          (b)         (b)                          k b′            (b)
                                                   X
                       G (y; s) = N (yb ) +
                     z,ℓ
                        e
                                     z,ℓ                         s ′ cA y A = δ ,
                                                                            b               z,ℓ
                                                 ∃b′ ̸=b: kb′ ≥1   b′ ̸=b

a polynomial system in (y, s) whose value at s = 0 is the block-diagonal product of the B pure
single-band systems, and whose Jacobian in y at s = 0 is block-diagonal with the single-band
Jacobians as blocks. By hypothesis the block system has at least S B solutions (y1∗ , . . . , yB      ∗)

(one S-set per band), each with invertible block-diagonal Jacobian. By the implicit function
theorem applied at each such solution, for all small s ̸= 0 the rescaled system has an isolated
nondegenerate solution y(s) near (y1∗ , . . . , yB
                                                 ∗ ); distinct limits give distinct solutions. The s = 0

fiber is finite (a zero-dimensional product of single-band fibers), so a single sufficiently small
rational s ̸= 0 lies in all of these neighbourhoods simultaneously. Fixing such sb ̸= 0 and
returning to xb = sb yb (an invertible linear change preserving isolation and nondegeneracy),
the coupled stacked initial system with the stated pins has at least S B isolated nondegenerate
solutions.

Budget (aligned instantiation).            Set
                                 j       log2 n k                               jnk
                    β = β(n) =                     ,        Q = Q(n) =                − β + 1.
                                     3 log2 log2 n                               3


                                                       28
For all large n we have β ≥ 10 and Q ≥ q0 (β): indeed log2 q0 (β) ≤ log2 β! + 2β + 10 log2 β + 5,
and log2 β! ≤ β log2 β ≤ 31 log2 n while β ≤ 12
                                             1
                                                log2 n once log2 log2 n ≥ 4, so that

                       log2 q0 (β) ≤ 31 log2 n + 16 log2 n + O(log log n) ≤ 23 log2 n,

i.e. q0 (β) ≤ n2/3 ≤ Q for all large n. Apply Lemma E (§II.6.5) with this Q: it returns s∗ ∈            / B(β)
with s∗ ≥ Q/(2β!) and the aligned band length q ′ = s∗ β! + β − 1 ≤ Q.
      Instantiate every band at length q ′ : band b carries battery cells (wb,r , zr+j ) only for j =
0, . . . , q ′ − 1, and pins only at the q ′ forced columns z0 , . . . , zq′ −1 . The unused shared columns zc ,
c ≥ q ′ + β − 1, carry no battery cells and no pins; their zone rows retain base cells and uplinks
but are inert: a zone row is displaced in a tight correction only when its column is deleted,
and the deleted columns are always battery columns of active blocks or station columns, never
an unused column. Hence Theorem II.7.1’s taxonomy, coefficient law and level separation hold
verbatim with q ′ in place of q (they are parametric in the block count throughout). Budgets:
battery rows Bβ ≤ n/3; pool rows B(β + 2) ≤ n/3 — take B = ⌊n/(3(β + 2))⌋ bands; shared
battery/zone columns q ′ + β − 1 ≤ ⌊n/3⌋; battery cells Bβq ′ ≤ n2 /9; pins Bβq ′ ≤ n2 outputs.

Capacity and conclusion of the proof. By Lemma E, Proposition A, Proposition B and
                                                                      ∗
Theorem II.7.2 (whose hypothesis is instantiated with S = ((β!)!)s at window length q ′ , the
per-band generic targets being taken in Q from Proposition B’s dense open set and realized as
pins through Theorem II.7.1’s invertible level separation), the coupled stacked initial system has
at least S B isolated nondegenerate solutions; by Theorem II.7.1 together with Theorem II.5.1
(the lifting, applied to the stacked design as described in §II.5) each lifts to a distinct isolated
point of Γn ∩ W :

                 #{isolated points of Γn ∩ W } ≥ S B ,             log2 S ≥     1
                                                                                4 Q β log2 β.

Arithmetic, for all large n: B ≥ n/(3(β + 2)) − 1 ≥ n/(4β) (using β ≥ 10 and n large) and
Q ≥ n/3 − β − 1 ≥ n/3.05, so

                                                            n   n                n2
            log2 #{isolated} ≥ B · 41 Qβ log2 β ≥             ·    · β log2 β =      log2 β.
                                                           4β 12.2              48.8

Moreover log2 β ≥ log2 log2 n − log2 (3 log2 log2 n) − 1 ≥ 21 log2 log2 n once log2 log2 n ≥ 13. By
Corollary II.2.2,

                       1 n2 1                n2 log2 log2 n
       C(permn ) ≥      ·    · log2 log2 n ≥                               for all sufficiently large n,
                       5 48.8 2                   500
and in particular C(permn ) = ω(n2 ). All constants are explicit and effective; for instance every
                             13
step above holds for n ≥ 22 , and smaller n are covered by the trivial bound C(permn ) ≥ 0
after shrinking the constant.


II.8      Synthesis: closing the chain and the final bound
Appendix D supplies exactly the statement used in §II.6.4(d5); we now retrace the chain to the
final bound.


                                                      29
II.8.1    From Theorem D to Cert(β)
In the identical-seed formal family of §II.6.4(d3) (seed a with distinct transcendental coordinates,
jet directions (Y, Z), orbit count s; all entries regular at s = 0 in O = Q(a, Y, Z)[s](s) ), the Schur
determinant satisfies det S(κ)|s=0 = κdβ Dβ (Y, Z). By Theorem D, Dβ ̸= 0 in Q(a, Y, Z); hence
the κdβ -coefficient Ddβ (s) ∈ O has Ddβ (0) ̸= 0, so Ddβ ̸= 0 as a rational function and its
numerator P ∈ Q[s, a, Y, Z] is a nonzero polynomial. The set B2 (β) = {s∗ ∈ Z : P (s∗ , ·) ≡ 0} is
therefore finite (bounded by degs P ), and by Lemma B-card (§II.6.5),

                              |B(β)| = |B1 ∪ B2 | ≤ D(β) = 22β+3 β 10 .

For any integer s∗ ∈ / B(β), generic numeric (a, Y, Z) give det S(κ) ̸≡ 0 on the identical-seed chart
at s∗ , i.e. det M ̸= 0 at chart points arbitrarily close to the seed; by Lemma L (Appendix C)
those chart points are isolated nondegenerate points of their fiber of the forced-column rook
map. Thus Cert(β) holds for every integer s ∈   / B(β).

II.8.2    The aligned Count Lemma
With q0 (β) := 2β!(D(β) + 3) ≤ β! 22β+5 β 10 : for every Q ≥ q0 (β) the interval [⌈Q/(2β!)⌉, ⌊(Q −
β + 1)/β!⌋] contains at least D(β) + 1 integers, hence some s∗ ∈/ B(β); set q ′ = s∗ β! + β − 1 ≤ Q.
                                 ′                     ∗
The window of aligned length q consists of exactly s complete orbit blocks plus bare head/tail
— precisely the scope of Cert(β) — and §II.8.1 provides a nondegenerate arranged point u∗
of its fiber, with block-constant target. The β! roots of each block’s local system are pairwise
distinct (Lemma O plus continuity on the chart), so the equivariant transport (Lemma A) yields
         ∗
((β!)!)s pairwise distinct isolated nondegenerate points in the single fiber:
                                                  ∗
                             S(β, q ′ ) ≥ ((β!)!)s ,     s∗ ≥ Q/(2β!).

By Stirling (log2 m! ≥ m(log2 m − log2 e) with m = β!) and β ≥ 10,

             log2 S(β, q ′ ) ≥ s∗ β! (log2 β! − log2 e) ≥   1
                                                            4 Q β log2 β   ≥   1 ′
                                                                               4 q β log2 β.


II.8.3    Assembly across bands
By Proposition A (Appendix C) the forced-column rook map N = Nq′ on the aligned board
                                                                ∗
is dominant with generic fiber count at least S := ((β!)!)s ; by Proposition B there is a dense
Zariski-open set of targets, containing Q-points, over which all deg N ≥ S preimages are non-
degenerate. Feeding these targets into Theorem II.7.2 (band decoupling by scaling: substitute
xb = sb yb and divide the level-ℓ equation of band b by sℓb ; at s = 0 the system is block-diagonal
with the B single-band systems as blocks and block-diagonal Jacobian, and the implicit function
theorem propagates each of the ≥ S B nondegenerate block solutions to the coupled system at
small s ̸= 0) gives at least S B isolated nondegenerate solutions of the stacked initial system,
where B = ⌊n/(3(β + 2))⌋ is the band count. Theorem II.7.1 (stacked tight classes; taxonomy,
positive coefficient law, invertible level separation — all parametric in the block count, applied
at the aligned length q ′ ) identifies this stacked initial system with the reduction of the pinned
permanental section, and Theorem II.5.1 / Complement II.5.2 (Hensel lifting over the valuation
ring) lifts each solution to a distinct isolated point of Γn ∩ W for the affine-linear subspace W
realizing the design and pins:

                              #{isolated points of Γn ∩ W } ≥ S B .

                                                  30
II.8.4     Parameters and arithmetic
Set                              j       log2 n k                        jnk
                    β = β(n) =                     ,        Q = Q(n) =         − β + 1.
                                     3 log2 log2 n                        3
For all large n: β ≥ 10, and q0 (β) ≤ n2/3 ≤ Q (since log2 q0 (β) ≤ log2 β! + 2β + 10 log2 β + 5 ≤
3 log2 n + 6 log2 n + O(log log n) ≤ 3 log2 n), so §II.8.2 applies with this Q and every band is
1           1                         2

instantiated at the one aligned length q ′ ≤ Q; the row and column budgets close (Bβ ≤ n/3
battery rows, B(β + 2) ≤ n/3 pool rows, q ′ + β − 1 ≤ ⌊n/3⌋ shared columns; unused shared
columns are inert for the tight-class taxonomy, §II.7). Then, for all large n, using B ≥ n/(4β)
and Q ≥ n/3.05:

                                                                 n   n                n2
         log2 #{isolated points} ≥ B · 14 Q β log2 β ≥             ·    · β log2 β =      log2 β,
                                                                4β 12.2              48.8

and log2 β ≥ 21 log2 log2 n once log2 log2 n ≥ 13. By the master inequality (Corollary II.2.2),

                                        1 n2 1                n2 log2 log2 n
                      C(permn ) ≥        ·    · log2 log2 n ≥
                                        5 48.8 2                   500
                                                       13
for all sufficiently large n (explicitly for n ≥ 22 , the smaller n being absorbed by shrinking the
constant), and in particular C(permn ) = ω(n2 ).
Remark (the role of the Core Theorem). The only use of §II.6.4(d4) is through §II.8.1: the
nonvanishing of P — equivalently the finiteness of B2 (β) — requires precisely Dβ ̸= 0 as an
element of Q(a, Y, Z), i.e. Dβ ̸≡ 0 as a polynomial in the jet directions (Y, Z) (it does not involve
a). This is what Theorem D proves, for every β ≥ 2.


Appendix A: relation to known obstructions
  (i) No characters or cancellation. All anchor units are positive and every initial coefficient
      is a positive sum (Theorem II.4.1(2)); support-only decoupling is impossible, but is not
      used: the design needs only one-sided domination margins, which the weights provide.

 (ii) The multiplicativity collapse. Designs whose tight coefficients factor over deleted columns
      collapse onto row sums and have no isolated points; here the rooted pickup makes the tight
      support depend on cols(A) ∋ z1+j — non-multiplicative — and the instances computed in
      Appendix B have finite solution sets.

(iii) Twins. Monomials with equal (rows, cols) have equal coefficients (a structural identity);
      the count object Nj,k aggregates them, and the Count Lemma operates directly at the
      aggregated level.
                                                            2
 (iv) Caps. Product and tiling designs cap at 2O(n ) ; the present design is a single non-product
                                                                   2
      system whose generic-coefficient count provably reaches 2Θ(n log log n) (compare §II.6.2 and
      Lemma E).


                                                       31
Appendix B: computer-algebra corroboration
The following statements were additionally checked by exact computer algebra (rational arith-
metic) in small cases.

   • The tight-class statements of Theorem II.4.1 (valuation inequality and the closed form of
     the initial coefficients) for (β, q) ∈ {(2, 3), (3, 3)} and the corresponding matrix sizes, and
     the invertibility of the delete-one matrix E for β = 2, 3.

   • The stacked tight-class law of Theorem II.7.1 (singleton, own-band pair, cross-band pair
     and third-order coefficients) for two stacked bands with β = 2.

   • The exact counts S(2, q) = 2q−1 − q−1
                                                
                                              2   for q = 2, . . . , 8 (values 2, 3, 5, 10, 22, 49, 107),
     together with S(3, 1) = 2, S(3, 2) = 3, S(3, 3) = 15, S(3, 4) = 107, S(4, 2) = 4 and
     S(4, 3) = 89, computed from Gröbner staircases at random rational targets.

   • The Structure Theorem identity Nm,k = Fk (x(m) ; ∆) on staggered boards, including partial
     (head/tail) columns by zero-padding, for (β, q) = (2, 4), (2, 5), (3, 4), (3, 6), (4, 5), (4, 6); and
     the top form Fk (x; 0) = (−1)k−1 k! ek (x) for β ≤ 5.

   • The graded triangularity and universality of Theorem U, and the resulting bad sets B1 (2) =
     B1 (3) = {1}, B1 (4) = ∅.

   • The jet formulas of §II.6.4(d1) for β ≤ 4.

   • Lemma D1 (multilinearity, row-supportQ decomposition and initial forms) and Lemma D3
     (vanishing pattern of J0 and det J0 = k det L(k) ) for β ≤ 7; the closed form of Theo-
     rem D6 for all 2 ≤ k ≤ β ≤ 8; and Dβ ̸= 0 at random rational points for β ≤ 7, with
     homogeneity degrees d3 = 6, d4 = 18, d5 = 40, d6 = 75.

   • Nondegenerate arranged window configurations at β = 3, 4, 5, and, on aligned boards,
     nondegeneracy of arranged windows exactly off the bad set (for instance det DN ̸= 0 at
     (β, s) = (2, 3), (2, 4), (2, 5), (3, 2), (3, 3) and det DN ≡ 0 along the whole chart at (β, s) =
                                                                      q−1   q−1
                                                                               
     (2, 2), matching B(2) = {1, 2} and the exact law S(2, q) = 2 − 2 ); and the equivariant
     transport of Lemma A at (β, s) = (2, 3), where all ((2!)!)3 = 8 arrangements are pairwise
     distinct, lie in one fiber and are nondegenerate.


Appendix C: full proofs for §II.6.4
Proposition A (isolated points bound the degree). If some fiber Φ−1 (y0 ) of a polynomial
map Φ : CN → CN has M isolated points, then Φ is dominant and its generic fiber has at least
M points.
Proof. If Φ were not dominant, every nonempty fiber of Φ : CN → im Φ would have every
component of dimension at least N − dim im Φ ≥ 1, so no fiber could have an isolated point.
Hence Φ is dominant and there is a dense Zariski-open U in the target with #Φ−1 (y) = deg Φ
for y ∈ U . Let x1 , . . . , xM be isolated in Φ−1 (y0 ); pick disjoint closed balls B̄i ∋ xi with
Φ−1 (y0 ) ∩ B̄i = {xi }; then y0 ∈
                                 / Φ(∂Bi ) (a compact set), so there are Euclidean balls Vi ∋ y0
with Vi ∩ Φ(∂Bi ) = ∅. For y ∈ Vi the topological degree of Φ − y on Bi is constant in y and
equals the local index of Φ at xi , which for a holomorphic map at an isolated zero is at least

                                                   32
1; hence Φ−1 (y) ∩ Bi ̸= ∅. Choosing y ∈ U ∩
                                                  T
                                                       i Vi (possible, since U is Euclidean-dense) gives
deg Φ ≥ M .

Lemma O (orbit seeds). If gT = γ|T | (symmetric aggregates) and a ∈ Cβ has pairwise distinct
coordinates, then with η := F (a; g) the solution set of F (·; g) = η is exactly the Sβ -orbit {σa},
and all β! roots are simple.

Proof. The structure formula (§II.6.1) shows that each Fk (·; g) is a symmetric polynomial when
g is symmetric, so the orbit is contained in the solution set, giving β! distinct solutions. By
the Top-Form Lemma (§II.6.2) the system is a complete intersection of degrees 1, . . . , β with
no zeros at infinity for all parameter values, so the solution count with multiplicity is exactly
β!. Hence every orbit point is a simple root (and there are no others); simplicity of a square
system’s root is invertibility of its Jacobian.

Euler–Jacobi Lemma. Let F1 , . . . , Fβ have degrees 1, . . . , β, leading forms with only the trivial
common zero,and simpleProots; let J be the Jacobian determinant.          For a polynomial H: (a)
             β                                                      β
                                                                      
if deg H ≤ 2 − 1 then ξ H(ξ)/J(ξ) = 0; (b) if deg H = 2 the sum depends only on the
leading forms of H and of the Fk .
                              P
Proof. The functional τ (H) = ξ H/J has the global residue representation
                                                  I               .Y
                                             −β
                              τ (H) = (2πi)                   H dx   Fk
                                                  {|Fk |=δ}          k

(properness coming from the no-zeros-at-infinity hypothesis), which is holomorphic in the coef-
ficients of the Fk along families with fixed leading forms and agrees with the root sum off the
discriminant, hence everywhere. Rescaling x 7→ λx maps the family to itself and multiplies τ
             β
by λdeg H−( 2 ) (1 + o(1)) as λ → ∞; boundedness forces (a), and in case (b) the limit kills all
sub-leading terms, proving the dependence claim. (This is the classical Euler–Jacobi vanishing
theorem in the inhomogeneous complete-intersection form; see [4, 13].)

Theorem U (coupling P        universality). For any parameters with simple local roots, the complete-
ensemble coupling Σ1 = all β! roots W (ξ)A(ξ)−1 B(ξ) is graded-triangular (that is, (Σ1 )T,T ′ = 0
for |T | < |T ′ |) and its graded-diagonal blocks are universal (they depend only on β).
                                P
Proof. Each entry of Σ1 is ξ HT,T ′ (ξ)/ det A(ξ) with H = (W adjA B)T,T ′ of degree at most
 β                ′
   
 2 + |T | − |T | by the weighted-degree bookkeeping (WT,r has degree |T | − 1; Ak,r has degree
k − 1 with top form (−1)k−1 k!ek−1 (xr̂ ); Bk,T ′ has degree k − |T ′ |), while det A has degree exactly
 β
   
 2 with top form a nonzero multiple of the Vandermonde. Apply the Euler–Jacobi Lemma:
entries with |T | < |T ′ | vanish (case (a)); entries with |T | = |T ′ | depend only on the leading
forms (case (b)), which are parameter-free — hence universal Q in β. With s complete ensembles,
Σ = s Σuniv + (strictly graded-lower), so det(I + Σ) = t det(I + s Σuniv        (t) ), a polynomial in s
equal to 1 at s = 0: the set of integers s with I + Σ singular is finite and computable.

Lemma L (reduction to the matrix M). Let u∗ be an arranged window configuration (bulk
columns carrying the roots of their blocks’ local systems, head/tail cells at (y, z)) at which every
bulk column’s local Jacobian Am = Dx F (ξm ; ĝ) is invertible (true at orbit seeds by Lemma O,


                                                      33
and on the chart by continuity). Then u∗ is an isolated, nondegenerate point of its fiber if and
only if the square matrix                                 
                                        I + Σ −Wh −Wt
                                 M=
                                         BH     AH       0
is nonsingular, where Σ = m W (ξm )A−1
                          P
                                       m Bm .

Proof. Near u∗ , each bulk column’s cells are determined by the aggregates: the pin equations of
column m read F (·; ĝ) = εm with Am invertible, so by the implicit function theorem the column
equals the analytic root function ξm (ĝ), with Dĝ ξm = −A−1
                                                           m Bm . Substituting, the fiber near u
                                                                                                ∗

is the zero set of

 (G) the aggregate consistency δĝ = Ξ(δĝ) + h(y + δy) − h(y) + t(z + δz) − t(z), where Ξ is the
     induced change of the bulk columns’ contributions, and

 (H) the head columns’ pin equations F (c) (y (c) + δy (c) ; ĝ + δĝ) = εc,· .

The derivative of a column’s aggregate contribution along δĝ is W (ξm )Dĝ ξm = −C(ξm ), so the
linearization of (G) is (I +Σ)δĝ = Wh δy +Wt δz, while the  linearization of (H) is AH δy +BH δĝ =
0. The unknowns are δĝ (G of them) and δy, δz ( β2 each); the equations are G from (G)
and β(β − 1) from (H) — a square system. A nonsingular linearization makes 0 an isolated
nondegenerate solution of (G) & (H), hence u∗ isolated and nondegenerate in the fiber (the
bulk cells follow analytically); conversely a singular M gives a kernel direction tangent to the
fiber.

Lemma C (the consistency chart). Define K(ĝ; y, z) := ĝ − i,j [ξj (ĝ; η (i) )] − h(y) − t(z),
                                                                       P
where the ξj (ĝ; η) are the local root functions. Then Dĝ K = I + Σ; if I + Σ is invertible at a seed,
then for all small (y, z) (and target shifts) there is a unique nearby consistent ĝ(y, z), analytic
in all parameters, and the consistent configurations form a smooth connected chart through the
seed family.

Proof. Implicit differentiation of F (ξ; ĝ) = η as in Lemma L; the seed family — tuples (a(i) )
with distinct coordinates — is connected, being the complement of a discriminant in a product
of affine spaces.


Appendix D: proof of the Core Theorem (§II.6.4(d4))
D.0 Setting and statement
Rows are indexed by r ∈ {0, 1, . . . , β − 1}. The bare window has β(β − 1) independent cell
variables:

   • head cells yc,r , for 1 ≤ c ≤ β − 1 and 0 ≤ r < c (head column c carries exactly the rows
     [0, c) = {0, . . . , c − 1});

   • tail cells zc,r , for 1 ≤ c ≤ β − 1 and c ≤ r ≤ β − 1 (tail column c carries exactly the rows
     [c, β)).


                                                    34
    (These are the partial columns of the staggered board of §II.6.1 at orbit count s = 0: on the
β × (q + β − 1) diagonal band the c-th head column from the left carries the rows [0, c) and the
c-th tail column from the left carries the rows [c, β); the labels here are intrinsic and no board
is needed.) Row r carries exactly β − 1 cells: the β − 1 − r head cells yc,r (for c > r) and the r
tail cells zc,r (for c ≤ r). Write Rρ for the set of cells in row ρ.
    For ∅ ̸= B ⊆ [0, β) the aggregates of the bare window are
                                         X Y                   X Y
                           ĝB (y, z) =             yc,r +            zc,r ,
                                          c>max B r∈B          c≤min B r∈B

the sum over all window columns containing all rows of B of that column’s cell product over
B (head columns c contribute iff B ⊆ [0, c), i.e. c > max B; tail columns iff B ⊆ [c, β), i.e.
                                                                 ′
c ≤ min B). For each head column c′ ∈ {1, . . . , β − 1} let χ(c ) denote its zero-padded cell vector,
    ′
  (c )                        ′
                            (c )                              ′
                                                            (c )            (c′ )
χr = yc′ ,r for r < c′ and χr = 0 for r ≥ c′ , and set χB := r∈B χr .
                                                                    Q
      With the Structure Theorem polynomials (x a β-vector, g = (gB ))
                    β−1
                    X          X         X Y
      Fk (x; g) =         xr                     (−1)|B|−1 (|B| − 1)! (gB − xB )          (k = 1, . . . , β),
                    r=0    S⊆[0,β)\{r} π⊢S B∈π
                            |S|=k−1
                                                                Q
where π runs over the set partitions of S and xB =                  r∈B xr , the bare-window map           is the
polynomial self-map of affine β(β − 1)-space
                                                                                      ′
                                                                    F(c′ ,k) := Fk χ(c ) ; ĝ(y, z) ,
                                                                                                  
          F : (y, z) 7−→ F(c′ ,k) c′ =1,...,β−1, k=1,...,β ,
and
                                         Dβ := det DF ∈ Z[y, z]
is its Jacobian determinant with respect to all β(β − 1) cells (§II.6.4(d3); F(c′ ,k) is the level-k pin
equation of head column c′ of the bare window). Each ĝB is homogeneous of degree |B| and each
F(c′ ,k) homogeneous of degree k, so Dβ is homogeneous of degree dβ = (β − 1) βk=1 (k − 1) =
                                                                                       P
β(β − 1)2 /2.
     It is convenient to introduce the cumulant transform: for T ⊆ [0, β),
                  ′                                       (c′ )        (c′ )           (c′ )
                             X Y
              K (c ) (T ) :=        (−1)|B|−1 (|B| − 1)! MB ,       MB := ĝB − χB ,
                               π⊢T B∈π

        (c′ )
with K (∅) = 1. Grouping the defining sum of Fk by the prefactor row and the partitioned
set gives the identity
                                   β−1
                                   X ′                 ′
                                             X
                        F(c′ ,k) =     χ(c
                                        r
                                           )
                                                   K (c ) (S).                   (D.0.1)
                                             r=0      S⊆[0,β)\{r}
                                                       |S|=k−1

Theorem D (Core Theorem). For every β ≥ 2, Dβ ̸≡ 0.

D.1 Row grading and the support decomposition
Assign to each cell its row: row(yc,r ) = row(zc,r ) = r. The polynomial ring Q[y, z] carries the
Zβ≥0 -grading in which the multidegree of a monomial records, for each row ρ, its total degree in
the cells of row ρ. For a subset T ⊆ [0, β) let ΠT be the linear projection onto the span of the
multilinear monomials of row support exactly T (one cell from each row of T , no other cells).

                                                     35
Lemma D1 (support decomposition). For every c′ , k:
   1. every monomial of F(c′ ,k) is multilinear in the cells and its row multiset is a set of exactly
      k distinct rows;

   2. for every k-subset T ⊆ [0, β),
                                                                ′        ′
                                                        X
                                                              χ(c ) (c )                   T
                                                                                   
                                      ΠT F(c′ ,k) =            r K       T \ {r}       =: F(c′ ,k) ,

                                                        r∈T

                                   T
                         P
      and F(c′ ,k) =       |T |=k F(c′ ,k) .

Proof. Each ĝB is, by definition, a sum of products of one cell from each row of B and no other
                                                                                    (c′ )
cells: it is multilinear with row support exactly B, and the same holds for χB (a single such
                                                        (c′ )
product, or 0), hence for every monomial of MB . A term of (D.0.1) indexed by (r, S, π) is
  (c′ ) Q                               ′
                   |B|−1 (|B| − 1)! M (c ) ; since {r} and the blocks B ∈ π are pairwise disjoint with
                                   
χr        B∈π (−1)                   B
union the k-set T = {r} ⊔ S, every monomial of this term takes exactly one cell from each row
of T and no others. This proves 1 (for the sum (D.0.1)), and shows that the term (r, S, π) is
fixed by ΠT for T = {r} ⊔ S and annihilated by ΠT ′ for T ′ ̸= T . Applying ΠT to (D.0.1) retains
exactly the terms with r ∈ T and S = T \ {r}; re-assembling the inner partition sums into
      ′
K (c ) (T \ {r}) gives 2; and summing 2 over all k-subsets T recovers (D.0.1), which also proves
the final decomposition.
                 (c′ )
    Note that χr         = 0 for r ≥ c′ , so the r-sum in F(c
                                                           T                                          ′
                                                             ′ ,k) effectively runs over r ∈ T ∩ [0, c ); and
 T                                                                   ′
                                                      (c ) (T \{r}) involves only M with B ⊆ T \{r}).
F(c′ ,k) involves only cells in the rows of T (each K                              B

Lemma D1′ (injective-matching form; sign-free). Index the window columns by C =
{H1 , . . . , Hβ−1 , T1 , . . . , Tβ−1 } and set MHc ,r := yc,r [r < c] and MTc ,r := zc,r [r ≥ c] (the inci-
dence weights of the window, with head and tail copies of an index c treated as distinct columns).
Then for every c′ and every T ⊆ [0, β):
    ′
                      X             Y                                                  X             Y
K (c ) (T ) =                           Mf (r),r , and hence        F(c′ ,k) =                          Mf (r),r :
              f : T ,→ C\{Hc′ } r∈T                                                       |T |=k, f : T ,→ C injective r∈T
                  f injective                                                                     Hc′ ∈im f

the (c′ , k)-coordinate of F is the weighted count of k-cell partial matchings of rows to columns
(one cell per row, one per column) forced to use head column c′ , with all coefficients +1; and
  (c′ )
ink is the same sum restricted to row set exactly [0, k).
                              (c′ )             (c′ )    P                   Q
Proof. By definition MB               = ĝB − χB =
                                           c∈C\{Hc′ } r∈B Mc,r (the aggregate is the sum over
                                              ′
                                            (c )
all columns supporting B, and subtracting χB removes exactly the Hc′ -term). Expanding the
product over the blocks of a partition π ⊢ T and interchanging sums,
              ′
                         X       Y                X        Y
          K (c ) (T ) =                Mh(r),r ·                (−1)|B|−1 (|B| − 1)! ,
                             h:T →C\{Hc′ }     r∈T                       π⊢T        B∈π
                                                                    π refines ker h

where ker h is the partition of T into the fibers of h (a partition-plus-column-choices datum
induces the map h constant on blocks, and conversely the partitions compatible with a given h
are exactly the refinements of ker h, the column choice then being determined). The inner sum

                                                                36
                                                            |B|−1 (|B| − 1)! , and by the exponential
                                    Q P            Q                        
factors over the fibers F ∈ ker h as F       πF ⊢F   B (−1)
formula         X tm X Y
                                 (−1)|B|−1 (|B| − 1)! = exp log(1 + t) = 1 + t,
                                                                           
                     m!
                m≥0      π⊢[m] B∈π

each factor equals 1 if |F | ≤ 1 and 0 if |F | ≥ 2. So only injective h survive, each with coefficient
                                                             (c′ )
1. The formula for F(c′ ,k) follows from (D.0.1) (note χr = MHc′ ,r , and an injective f on T
using Hc′ decomposes uniquely as the forced cell (r, Hc′ ) plus an injection of T \ {r} avoiding
                            (c′ )
Hc′ ); the statement for ink is then Lemma D1.2.

    Lemma D1′ is not needed for the main line below — Lemmas D4–D5 are proved directly
from the partition-sum definition — but it renders all signs transparent, identifies F with the
forced-column rook map of §II.6.1 restricted to the bare window, and provides the reader with
an independent combinatorial route to every entry computation below: an entry of L(k) is a
doubly-rooted matching sum, and at the sparse point Ek of §D.3 the surviving matchings can
be listed by hand.
    Fix integer weights 0 < ω0 < ω1 < · · · <
                                            Pωβ−1 (for instance ωr = r +1; any strictly increasing
choice works). For T ⊆ [0, β) put ω(T ) = r∈T ωr and Wk := ω([0, k)) = ω0 + · · · + ωk−1 .
Lemma D2 (weight gap). For every k-subset T ⊆ [0, β), ω(T ) ≥ Wk , with equality if and
only if T = [0, k).
                                                                         P       P
Proof. List T = {t1 < · · · < tk }; then ti ≥ i − 1 for all i, so ω(T ) = i ωti ≥ i ωi−1 = Wk by
monotonicity. If T ̸= [0, k) then ti > i − 1 for some i, and strict monotonicity of ω makes the
inequality strict.

   Define the initial form of the (c′ , k)-equation:
                           (c′ )
                                               X ′
                                      [0,k)              (c′ )
                                                   χ(c )
                                                                           
                         ink := F(c′ ,k) =           r K       [0, k) \ {r} ,
                                                    r<k

                                                                                 (c′ )      (c′ )       ′
a polynomial in the cells of rows 0, . . . , k − 1 only. For k = 1: in1                  = χ0       K (c ) (∅) = yc′ ,0 .

D.2 The graded degeneration is block triangular
Let t be an indeterminate and st the substitution scaling every row-ρ cell by tωρ . Order the
equations (c′ , k) by level k = 1, . . . , β (each level a group of β − 1 equations, c′ = 1, . . . , β − 1)
and the variables by row ρ = 0, . . . , β − 1 (each row a group of β − 1 cells, in any fixed order
inside a group). Define the renormalized Jacobian

                                Jt := diag t−Wk (c′ ,k) · D F ◦ st .
                                                                     


Lemma D3 (triangularization). With this ordering:
   1. the entry of Jt in equation row (c′ , k) and variable column u ∈ Rρ is
                                                                           T
                                                                         ∂F(c
                                               X                             ′ ,k)
                                                              ω(T )−Wk
                             
                          Jt (c′ ,k), u =                 t                          ∈ Q[t, y, z],
                                                                           ∂u
                                            |T |=k, ρ∈T

      all exponents being ≥ 0;

                                                          37
                                                                     (c′ ) 
   2. at t = 0: the block of J0 in level k and row group ρ equals ∂ ink /∂u c′ , u∈Rρ if ρ ≤ k − 1,
      and 0 if ρ ≥ k;

   3. hence J0 is block lower triangular for the pairing (level k) ↔ (row group k −1), with square
      diagonal blocks
                                    (c′ ) 
                                h           i
                       L(k) := ∂ ink ∂u ′                           (k = 1, . . . , β),
                                                  c =1,...,β−1, u∈Rk−1

                                                           Qβ        (k)      (1) = I
        each of size (β − 1) × (β − 1), and det J0 =        k=1 det L , with L       β−1 ;

  4. if det L(k) ̸≡ 0 in Q[y, z] for every k, then Dβ ̸≡ 0.
                                                   T             T
                                        P
Proof. 1. By Lemma D1, F(c′ ,k) =          |T |=k F(c′ ,k) with F(c′ ,k) multilinear of row support T ,
    T
so F(c              ω(T ) F T
      ′ ,k) ◦ st = t       (c′ ,k) . Differentiating with respect to the coordinate u ∈ Rρ kills the
terms with ρ ∈                         T                     ω(T ) ∂F T
                  / T and gives ∂(F(c    ′ ,k) ◦ st )/∂u = t         (c′ ,k) /∂u (both sides are polynomials in
(Y, Z) after the substitution; the scaling factor of the monomials is unchanged by the derivative
in the scaled coordinates precisely because we differentiate the composite with respect to the
unscaled variable — explicitly, if G is row-homogeneous with support T then G ◦ st = tω(T ) G as
polynomial maps, and one differentiates this identity). Multiplying the (c′ , k)-row by t−Wk and
invoking Lemma D2 gives the display with exponents ω(T ) − Wk ≥ 0.
    2. Setting t = 0 retains exactly the terms with ω(T ) = Wk , i.e. T = [0, k) (Lemma D2),
                                                                                [0,k)          (c′ )
which require ρ ∈ [0, k), i.e. ρ ≤ k − 1; the surviving entry is ∂F(c′ ,k) /∂u = ∂ ink /∂u.
    3. By 2, the (k, ρ)-block of J0 vanishes whenever ρ ≥ k. With equation groups ordered
k = 1, . . . , β and variable groups ordered ρ = 0, . . . , β − 1, the k-th equation group faces the k-th
variable group ρ = k − 1 on the diagonal, so J0 is block lower triangular (every block strictly
above the diagonal has ρ > k − 1, hence vanishes) with square diagonal blocks L(k) of size β − 1;
the determinant of such a matrix is the product of the diagonal-block determinants, with no
                       (c′ )
sign. For k = 1, in1 = yc′ ,0 and R0 = {yc,0 : 1 ≤ c ≤ β − 1}, so L(1) is the identity (ordering
R0 by c).
    4. Over the field Q(t) the chain rule gives

                             D(F ◦ st )(Y, Z) = DF (st (Y, Z)) · diag(tωrow(u) )u ,
                                                         


hence                                                              P
                       det D(F ◦ st )(Y, Z) = Dβ st (Y, Z) · t(β−1) ρ ωρ ,
                                                          
                                       P              P
and so, with the integer N := (β − 1) ρ ωρ − (β − 1) k Wk ,

                             det Jt = t N Dβ st (Y, Z)
                                                      
                                                                 in Q(t)[Y, Z].

If Dβ ≡ 0, the right-hand side vanishes
                                    Q identically, so det Jt ≡ 0 and in particular det J0 = 0; but
                                           (k)
by 3 and the hypothesis, det J0 = k det L is a product of nonzero elements of the integral
domain Q[y, z] — a contradiction.

    By Lemma D3.3–4 it remains to prove that det L(k) ̸≡ 0 for 2 ≤ k ≤ β. We now prove it for
all β, with a closed form.


                                                      38
D.3 The evaluation point Ek and the entries of L(k) |Ek
Fix k with 2 ≤ k ≤ β and set ρ := k − 1 ∈ {1, . . . , β − 1}. Let u1 , . . . , uρ , v1 , . . . , vρ−1 be fresh
indeterminates and let Ek be the substitution

       yc,c−1 := uc (1 ≤ c ≤ ρ),             zc,c := vc (1 ≤ c ≤ ρ − 1),            every other cell := 0.

(The active head cell of head column c ≤ ρ is its bottom cell, row c − 1; the active tail cell of
tail column c ≤ ρ − 1 is its top cell, row c. All active cells lie in rows ≤ ρ − 1; head columns
c > ρ and tail columns c ≥ ρ are entirely zero.) Define
                                                                                          ρ−1
                                                                                          Y
                     w0 := u1 ,     wt := ut+1 + vt (1 ≤ t ≤ ρ − 1),              W :=          wt ,
                                                                                          t=0
                                      Q
and for T ⊆ [0, ρ) write WT :=            t∈T wt (so W = W[0,ρ) ).

Lemma D4 (aggregates at Ek ). Under Ek every column has at most one nonzero cell.
Consequently:
                                                           (c′ )
   1. ĝB |Ek = 0 for all B with |B| ≥ 2, and χB |Ek = 0 for all B with |B| ≥ 2 and all c′ ; hence
         (c′ )
      MB |Ek = 0 for |B| ≥ 2;

   2. ĝ{t} |Ek = wt for 0 ≤ t ≤ ρ − 1 and ĝ{t} |Ek = 0 for t ≥ ρ;
        (c′ )                                                       ′
   3. χr |Ek = uc′ δr,c′ −1 for 1 ≤ c′ ≤ ρ, and χ(c ) |Ek = 0 for c′ ≥ k; hence, for every c′ :
        (c′ )                                          (c′ )
      M{t} |Ek = wt for t ≤ ρ − 1 with t ̸= c′ − 1; M{c′ −1} |Ek = wc′ −1 − uc′ when c′ ≤ ρ; and
         (c′ )                                                     (c′ )
      M{t} |Ek = 0 for every t ≥ ρ (in particular M{ρ} |Ek = 0).

Proof. Head column c has (at most) the single active cell yc,c−1 (present iff c ≤ ρ); tail column
c has (at most) the single active cell zc,c (present iff c ≤ ρ − 1). A monomial of ĝB with |B| ≥ 2
                                                                                            (c′ )
is a product of at least 2 distinct cells of one column, hence vanishes at Ek ; likewise χB is a
product of at least 2 distinct cells of head column c′ . For singletons: the active cells in row t
are yt+1,t = ut+1 (present iff t + 1 ≤ ρ) and zt,t = vt (present iff 1 ≤ t ≤ ρ − 1); summing,
ĝ{0} |Ek = u1 = w0 and ĝ{t} |Ek = ut+1 + vt = wt for 1 ≤ t ≤ ρ − 1, while rows t ≥ ρ host no
active cells. Part 3 is immediate from the definition of Ek and part 2.

    We now compute every entry of L(k) |Ek (derivatives first, then evaluation). The rows of L(k)
are indexed by c′ ∈ {1, . . . , β − 1}; the columns by the row-ρ cells

                          Rρ = { yd,ρ : ρ + 1 ≤ d ≤ β − 1 } ∪ { zc,ρ : 1 ≤ c ≤ ρ },
                               |             {z           }   |         {z       }
                                        β−k head cells                     ρ tail cells

ordered head cells first (d increasing), then tail cells (c increasing). Recall that
                                (c′ )                      ′
                                         X
                                                yc′ ,r K (c ) [0, k) \ {r}
                                                                           
                              ink =
                                            r<min(k,c′ )

          (c′ )
(using χr         = yc′ ,r for r < c′ and = 0 otherwise), and record two facts used repeatedly.


                                                            39
                                                                     (c′ )                   (c′ )
    (F-a) Which M ’s depend on a row-ρ cell. MB = ĝB − χB involves only cells in the rows of
B; so a row-ρ cell can occur only if ρ ∈ B. Moreover for B ∋ ρ: ĝB depends on the head cells yd,ρ
(d > max B ≥ ρ, hence every d ≥ ρ + 1 with B ⊆ [0, d)) and on the tail cells zc,ρ (c ≤ min B);
        (c′ )                       (c′ )
while χB contains the factor χρ , which is the variable yc′ ,ρ if c′ > ρ and is identically 0 if
c′ ≤ ρ.
                            ′
    (F-b) Derivative of K (c ) (T ) at Ek . By the product rule,
       ′                                                                     (c′ )
  ∂K (c ) (T )      X X                          ∂MB0                                         Y                                           (c′ )
                  =     (−1)|B0 |−1 (|B0 | − 1)!                                                          (−1)|B|−1 (|B| − 1)! MB                      ,
     ∂u        Ek                                 ∂u                                     Ek                                                       Ek
                     π⊢T B0 ∈π                                                             B∈π\{B0 }

and by Lemma D4.1 the undifferentiated blocks of a surviving partition must all be singletons.
Hence, for a row-ρ cell u and T ∋ ρ,
            ′                                                                               (c′ )
       ∂K (c ) (T )                 X                                     ∂MB0                              Y            (c′ )
                       =                         (−1)|B0 |−1 (|B0 | − 1)!                                            M{t}             .     (D.3.1)
          ∂u        Ek                                                     ∂u                        Ek                          Ek
                                B0 ⊆T, ρ∈B0                                                               t∈T \B0

(Partitions of T whose differentiated block is B0 and whose other blocks are singletons exist and
are unique; B0 must contain ρ by (F-a).)

Lemma D5 (entries of L(k) |Ek ). Let Tc′ := [0, k) \ {c′ − 1} for 1 ≤ c′ ≤ ρ (so ρ ∈ Tc′ and
Tc′ \ {ρ} = [0, ρ) \ {c′ − 1}). Then:

  1. (high rows) for k ≤ c′ ≤ β − 1 and all row-ρ cells:
                                                 (c′ )                                       (c′ )
                                            ∂ ink                                        ∂ ink
                                                              = W δd,c′ ,                                  = 0;
                                             ∂yd,ρ       Ek                               ∂zc,ρ      Ek


  2. (low rows, head cells) for 1 ≤ c′ ≤ ρ and ρ + 1 ≤ d ≤ β − 1:
                                    (c′ )
                                ∂ ink
                                                 = uc′ W[0,ρ)\{c′ −1}                     (independently of d);
                                 ∂yd,ρ      Ek


  3. (low rows, tail cells) for 1 ≤ c′ ≤ ρ and 1 ≤ c ≤ ρ:
                   (c′ )
                ∂ ink                                                                                 
                                = uc′ W[0,ρ)\{c′ −1} − [ c ̸= c′ − 1 ∧ c ≤ ρ − 1 ] vc W[0,ρ)\{c′ −1, c} .
                 ∂zc,ρ     Ek


                                                                                                                                           (c′ )
Proof. (1). Let c′ ≥ k, so all prefactors yc′ ,r (r < k ≤ c′ ) are genuine variables of ink but
vanish at Ek (the active head cells are yc,c−1 with c ≤ ρ < c′ ). Derivative terms in which ∂/∂u
hits a K-factor retain the prefactor yc′ ,r and die at Ek ; so
                                   (c′ )
                                ∂ ink                X                               ′
                                                           [ u = yc′ ,r ] K (c ) [0, k) \ {r}
                                                                                                            
                                                 =                                                                   .
                                  ∂u        Ek                                                                  Ek
                                                     r<k

A row-ρ cell equals yc′ ,r for some r < k iff u = yc′ ,ρ (using ρ = k − 1 < k and c′ > ρ); this
forces d = c′ in the head-cell case and never happens in the tail-cell case. It remains to evaluate

                                                                    40
   ′                                    ′
K (c ) ([0, k) \ {ρ})|Ek = K (c ) ([0, ρ))|Ek : by Lemma D4.1 only the all-singleton partition survives,
                   (c′ )                                 (c′ )                    ′
giving t<ρ M{t} |Ek = t<ρ wt = W , where M{t} |Ek = wt because χ(c ) |Ek = 0 for c′ ≥ k
          Q                 Q

(Lemma D4.3). This proves (1).
    (2) and (3). Let c′ ≤ ρ. Now the prefactors yc′ ,r have r < c′ ≤ ρ, so no prefactor is a row-ρ
cell and the derivative passes to the K-factors:
                  (c′ )                                          ′                                      ′
              ∂ ink                   X                   ∂K (c ) ([0, k) \ {r})            ∂K (c ) (Tc′ )
                                  =           yc′ ,r    ·                           = uc′ ·                   ,
                ∂u        Ek                ′
                                                     Ek             ∂u           Ek             ∂u         Ek
                                      r<c

by Lemma D4.3 (yc′ ,r |Ek = uc′ δr,c′ −1 ). We evaluate the right-hand factor via (D.3.1); note that
                                   (c′ )
the singleton values there are M{t} |Ek = wt for all t ∈ Tc′ \ B0 ⊆ [0, ρ) \ {c′ − 1} (Lemma D4.3;
                                                                              (c′ )
t ̸= c′ − 1 and t ≤ ρ − 1). By (F-a), and since χB0 ≡ 0 for B0 ∋ ρ when c′ ≤ ρ, only ĝB0 is
                                                                     Ek ̸= 0.
differentiated. We list the blocks B0 ∋ ρ, B0 ⊆ Tc′ , with ∂ĝB0 /∂u|Q
    Case u = yd,ρ , d ≥ ρ + 1. Here ∂ĝB0 /∂yd,ρ = [ d > max B0 ] r∈B0 \{ρ} yd,r . Since ρ ∈ B0 ,
max B0 = ρ and the condition reads d > ρ, which holds. At Ek every cell of head column
d ≥ ρ + 1 vanishes, so the product is nonzero only when empty: B0 = {ρ}, with derivative 1
and sign/factorial factor (−1)0 0! = 1. Then (D.3.1) gives
                                               ′
                                        ∂K (c ) (Tc′ )               Y
                                                          =                     wt = W[0,ρ)\{c′ −1} ,
                                          ∂yd,ρ        Ek
                                                                 t∈Tc′ \{ρ}

independently of d; multiplying by uc′ proves (2).                Q
     Case u = zc,ρ , 1 ≤ c ≤ ρ. Here ∂ĝB0 /∂zc,ρ = [ c ≤ min B0 ] r∈B0 \{ρ} zc,r (only tail column c
carries the cell zc,ρ ). At Ek the only (possibly) nonzero cell of tail column c is zc,c = vc , present
iff c ≤ ρ − 1. So the product is nonzero only if B0 \ {ρ} ⊆ {c}:
   • B0 = {ρ}: derivative 1 (the condition c ≤ ρ holds); factor 1; contribution W[0,ρ)\{c′ −1} .
   • B0 = {c, ρ} with c < ρ: this requires B0 ⊆ Tc′ , i.e. c ̸= c′ − 1 (note that c ∈ [1, ρ − 1] ⊆
     [0, k) automatically); the derivative is [ c ≤ c ] zc,c |Ek = vc ; the sign/factorial factor is
     (−1)2−1 1! = −1; the undifferentiated product is W[0,ρ)\{c′ −1,c} ; contribution −vc W[0,ρ)\{c′ −1,c} .
   • |B0 | ≥ 3: the derivative is a product of at least 2 cells of tail column c other than zc,ρ , at
     most one of which is nonzero at Ek ; contribution 0. (Also, for c = ρ the block B0 = {c, ρ}
     degenerates to {ρ}, already counted.)
Summing the contributions and multiplying by uc′ proves (3).

D.4 The closed form and nonvanishing of det L(k)
Theorem D6 (level-block closed form, general β). For every 2 ≤ k ≤ β, with ρ = k − 1,
in the ordering fixed above:

                                            det L(k)         = (−1)(β−k)ρ W β−k det Θ,
                                                       Ek
                                                                             ρ
where Θ = uc′ W[0,ρ)\{c′ −1} − [ c ̸= c′ − 1 ∧ c ≤ ρ − 1 ]vc W[0,ρ)\{c′ −1,c} c′ ,c=1 is the low-row/tail-
            

cell block of Lemma D5.3, and
                       ρ                 ρ−1                                                                 ρ             ρ−1
                      Y                   Y                        Wρ                                       Y               Y          
det Θ = (−1)ρ−1                   uc′              vc Qρ                      Qρ−1       = (−1)ρ−1 w0 W ρ−2           uc′            vc
                                                            c′ =1 wc −1         c=1 wc
                                                                     ′
                          c′ =1              c=1                                                              c′ =1            c=1


                                                                         41
(the last expression for ρ ≥ 2; for ρ = 1, det Θ = u1 ). In particular

det L(k)        ̸= 0    in Q[u, v] :             at u ≡ v ≡ 1 its value is ± 2(ρ−1)(β−k+ρ−2) (ρ ≥ 2), ±1 (ρ = 1),
           Ek

and therefore det L(k) ̸≡ 0 in Q[y, z] for every 2 ≤ k ≤ β.
Proof. By Lemma D5 the matrix L(k) |Ek , with rows grouped as (low: 1 ≤ c′ ≤ ρ; high: k ≤ c′ ≤
β − 1) and columns grouped as (head cells; tail cells), has the block form
                                       !
                              H     Θ                  h               i
               L(k)    =                  ,     H = uc′ W[0,ρ)\{c′ −1} 1≤c′ ≤ρ ,
                    Ek     W Iβ−k 0                                     ρ<d≤β−1

the high-row blocks being W I (on head cells, by Lemma D5.1, with the identity pairing c′ = d)
                    Swapping the two column groups — (β − k)ρ column transpositions —
and 0 (ontail cells).
           Θ H
produces              , block upper triangular with square diagonal blocks, so
           0 WI

                                    det L(k)              = (−1)(β−k)ρ det Θ · W β−k
                                                     Ek

(for k = β the high block is empty and the formula reads det L(β) |Eβ = det Θ).
    To evaluate det Θ, work in the field Q(u, v) (both sides of the final identity are polynomials, so
computing in the fraction field is legitimate). Using W[0,ρ)\{c′ −1} = W/wc′ −1 and W[0,ρ)\{c′ −1,c} =
W/(wc′ −1 wc ),
                                                
                   uc′ W                        1,                  c = c′ − 1 or c = ρ,
                               ′           ′
          Θc′ ,c =        ψc (c ),    ψc (c ) =      v     u
                   wc′ −1                       1 − c = c+1 , c ̸= c′ − 1, c ≤ ρ − 1,
                                                     wc      wc
where wc − vc = uc+1 was used. Extracting the nonzero factor uc′ W/wc′ −1 from each row c′ ,
                                  ρ
                                 Y u ′W    c
                       det Θ =                        det Ψ,          Ψc′ ,c = ψc (c′ ) (1 ≤ c′ , c ≤ ρ).
                                          wc′ −1
                                  c′ =1

In Ψ, column ρ is the all-ones vector 1 (since c = ρ fails the condition c ≤ ρ − 1, so ψρ ≡ 1),
and for c ≤ ρ − 1 column c equals
                        uc+1          uc+1         uc+1      vc
                             1+ 1−            ec+1 =       1+     ec+1 ,
                          wc            wc            wc       wc
ec+1 being the standard basis vector supported on row c′ = c+1 — the unique row with c = c′ −1
(note c + 1 ∈ [2, ρ], a valid row index). Subtracting uwc+1
                                                         c
                                                            × (column ρ) from column c, for each
c = 1, . . . , ρ − 1, leaves the columns
                                             v1      v2              vρ−1
                                                e2 ,    e3 , . . . ,      eρ , 1.
                                             w1      w2              wρ−1
By multilinearity the determinant has a single expansion term (columns 1, . . . , ρ − 1 contribute
their basis vectors, covering rows 2, . . . , ρ; column ρ must contribute the row-1 component of 1):
                                    ρ−1
                                     Y v                                                           ρ−1
                                                                                                          vc
                                                 c
                                                                                                    Y
                                                                                              ρ−1
                         det Ψ =                     det[e2 , e3 , . . . , eρ , e1 ] = (−1)                  ,
                                             wc                                                           wc
                                       c=1                                                          c=1


                                                                 42
                       the ρ-cycle (1 2 · · · ρ). Q(For ρ = 1, Ψ = [1] and det Θ = u1 W/w0 = u1 .)
the sign being that of Q
Combining, and using ρc′ =1 wc′ −1 = W and ρ−1      c=1 wc = W/w0 ,
                            Y             Y               Wρ                         Y      Y
         det Θ = (−1)ρ−1            uc′          vc                   = (−1)ρ−1 w0 W ρ−2    uc′   vc ,
                                                          W · (W/w0 )
                               c′           c                                             ′
                                                                                          c     c

a polynomial (for ρ ≥ 2; the case ρ = 1 was computed directly). At u ≡ v ≡ 1: w0 = 1, wt = 2
(1 ≤ t ≤ ρ − 1), W = 2ρ−1 , giving the stated nonzero values. Since the specialization Ek of
det L(k) ∈ Q[y, z] is a nonzero element of Q[u, v], the polynomial det L(k) is itself nonzero.

D.5 Proof of Theorem D
We have det L(1) = det Iβ−1 = 1, and det L(k) ̸≡ 0 for 2 ≤ k ≤ β by Theorem D6; hence Dβ ̸≡ 0
by Lemma D3.4.
Remark (explicit small cases). One has D2 = y1,0 and
                  2
                     y2,1 z1,1 (y1,0 − y2,0 )2 − (y1,0 − y2,0 )(z1,1 + z1,2 + z2,2 ) + z1,1 z2,2 ,
                                                                                               
         D3 = ± y1,0

with homogeneity degrees d3 = 6, d4 = 18, d5 = 40, d6 = 75.QThe decomposition of Lemma D1,
the vanishing pattern of Lemma D3 together with det J0 = k det L(k) ̸= 0, the closed form of
Theorem D6 and the nonvanishing of Dβ were additionally verified by exact computer algebra
for small β (see Appendix B).


References
 [1] W. Baur and V. Strassen, The complexity of partial derivatives, Theoret. Comput. Sci. 22
     (1983), 317–330.

 [2] P. Bürgisser, M. Clausen and M. A. Shokrollahi, Algebraic Complexity Theory, Grundlehren
     der mathematischen Wissenschaften 315, Springer, 1997.

 [3] W. Fulton, Intersection Theory, 2nd ed., Springer, 1998.

 [4] P. Griffiths and J. Harris, Principles of Algebraic Geometry, Wiley, 1978.

 [5] R. Hartshorne, Algebraic Geometry, Graduate Texts in Mathematics 52, Springer, 1977.

 [6] K. Kalorkoti, A lower bound for the formula size of rational functions, SIAM J. Comput.
     14 (1985), 678–687.

 [7] T. Mignon and N. Ressayre, A quadratic bound for the determinant and permanent problem,
     Int. Math. Res. Not. 2004 (2004), 4241–4253.

 [8] E. I. Nechiporuk, On a Boolean function, Dokl. Akad. Nauk SSSR 169 (1966), 765–766;

 [9] R. Raz, Multi-linear formulas for permanent and determinant are of super-polynomial size,
     J. ACM 56 (2009), no. 2, Art. 8.

[10] H. J. Ryser, Combinatorial Mathematics, Carus Mathematical Monographs 14, Mathemat-
     ical Association of America, 1963.

                                                              43
[11] A. Shpilka and A. Yehudayoff, Arithmetic circuits: a survey of recent results and open
     questions, Found. Trends Theoret. Comput. Sci. 5 (2010), 207–388.

[12] V. Strassen, Die Berechnungskomplexität von elementarsymmetrischen Funktionen und von
     Interpolationskoeffizienten, Numer. Math. 20 (1973), 238–251.

[13] A. K. Tsikh, Multidimensional Residues and Their Applications, Translations of Mathe-
     matical Monographs 103, American Mathematical Society, 1992.

[14] L. G. Valiant, Completeness classes in algebra, in: Proc. 11th Annual ACM Symposium on
     Theory of Computing (STOC), 1979, 249–261.


                                            44
