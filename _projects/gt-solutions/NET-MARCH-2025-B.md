---
layout: page
title: NET-MARCH-2025-B
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a group of order $n > 3$ and $H$ be a subgroup with
$1 < |H| < n.$ 
Consider the set
$$X = \bigcup_{g \in G} gHg^{-1}.$$
Which of the following statements is true?

(a) If $G$ is abelian, then $|X| = n$.<br>
(b) If $|X|$ divides $n$, then $G$ is abelian.<br>
(c) $|X| < n$.<br>
(d) $|X|$ divides $n$.<br>

**Solution**

Here, $X$ is the union of all the conjugates of the proper subgroup $H$ of $G$.\\
If $G$ is abelian, then $gHg^{-1} = H$ and so $X = H$. Then $|X| = |H| < n$. So option (a) is false.\\ 
In $G = S_3$, let $H = \langle \psi \rangle = \{e, \psi, \psi^2\}$, where $\psi = (1,2,3)$. Then every conjugate of $H$ is of same order as $H$, i.e., $3$. But $H$ is the only subgroup of order $3$ which is normal. Thus, $X = H$ and $|X| = 3\mid 6 = o(G)$, but $G = S_3$ is not abelian. So, option (b) is false.\\
Since $H$ is a proper subgroup and $o(H) = o(gHg^{-1})$, if $|X| = n = G$, then this would imply that $G$ is union of its proper subgroups. We know that $G$ is union of its proper subgroups if and only if it is non-cyclic. For $G = \mathbb Z_n$, cyclic group of order $n$, for every divisor $m$ of $n$, there is a unique subgroup of order $m$. So, $H$ is the only subgroup of order $m$. In fact, $G$ is abelian and so $X = H$. So, $|X| < n = o(G)$. So, option (c) is true.\\
In $G = S_3$, let $H = \langle \varphi\rangle = \{e, \varphi\}$, where $\varphi = (1,2)$. Then every conjugate of $H$ is of same order as $H$, i.e., $2$. Thus, $X = \{e, \varphi, \varphi\psi, \psi\varphi\}$, where $\psi = (1,2,3)$. Here $|X| = 4 \nmid 6 = o(G)$. So option (d) is false.
