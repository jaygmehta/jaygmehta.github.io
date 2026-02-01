---
layout: page
title: NET-JUNE-2016-C-3-3
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a finite abelian group of order $n$. Pick each correct statement from below.

(a) If $d$ divides $n$, there exists a subgroup of $G$ of order $d$.<br>
(b) If $d$ divides $n$, there exists an element of order $d$ in $G$.<br>
(c) If every proper subgroup of $G$ is cyclic, then $G$ is cyclic.<br>
(d) If $H$ is a subgroup of $G$, there exists a subgroup $N$ of $G$ such that $G/N \cong H$.<br>

**Solution**

(a) We know that, the converse of Lagrange's theorem holds for finite abelian groups. So this is true.<br>

(b) In case of $G=K_4 = \{e,a,b,b\}$ or isomorphically $G=\mathbb Z_2 \times \mathbb Z_2$, $4 \mid o(G)=4$ but $G$ does not have an element of order $4$.<br>

(c) In case of $G=K_4 = \{e,a,b,b\}$ all its three proper subgroups $\{e,a\}$, $\{e,b\}$ and $\{e,c\}$ are cyclic groups of order $2$ but Klein-$4$ group is not cyclic.\\
Another example in case of non-abelian groups is Quaternion group $Q_8$ in which every proper subgroup is cyclic.<br>

(d) If $o(G) = n = p_1^{a_1} \cdots p_k^{a_k}$ and $H$ is subgroup of $G$, then $o(H) = p_1^{b_1} \cdots p_k^{b_k}$, where $0 \le b_i \le a_i$, for all $i = 1,2,\ldots,k$. Then by converse Lagrange's theorem (which is true for finite abelian groups), there exists a subgroup $N$ of $G$ of order $p_1^{a_1-b_1} \cdots p_k^{a_k-b_k}$. Since $G$ is abelian, $N$ is normal and clearly, $o(H) = o(G/N)$. It remains to show that they are isomorphic.\\
Define $f: H \to G$ by $f(h) = h$  $(\forall\ h \in H)$ and $g: G \to G/N$ by $g(x) = xN$. Then $f$ and $g$ are homomorphisms. Hence, their composition $g \circ f: H \to G/N$ is a homomorphism. Since $f$ is one-one and $g$ is onto, $g\circ f$ is one-one and onto and hence $G/N \cong H$.