---
layout: page
title: NET-JULY-2025-C-3-3
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G_1$ and $G_2$ be subgroups of a group $G$. Which of the following statements are true?

(a) If $G_1$ is normal in $G$, then $(G_2G_1)/G_1 \cong G_2/(G_2 \cap G_1)$.<br>
(b) If $H_1$ and $H_2$ are normal subgroups of $G_1$ and $G_2$, respectively, then
$$
(G_1 \times G_2)/(H_1 \times H_2) \cong (G_1/H_1) \times (G_2/H_2).
$$<br>
(c) If $G_1$ is normal in $G_2$ and $G_2$ is normal in $G$, then $G_1$ is normal in $G$.<br>
(d) Every subgroup of prime index in $G$ is normal.<br>

**Solution**

The first option (a) is true as it is nothing but the second isomorphism theorem.\\
Define
$$
\psi : G_1 \times G_2 \to (G_1/H_1) \times (G_2/H_2), \qquad \psi(g_1, g_2) = (g_1H_1, g_2H_2).
$$
This is a surjective homomorphism. Its kernel is
$$
\ker \psi = H_1 \times H_2.
$$
By the First Isomorphism Theorem,
$$
(G_1 \times G_2)/(H_1 \times H_2) \cong (G_1/H_1) \times (G_2/H_2).
$$
In general, the **result** is: if $H_i \trianglelefteq G_i$, then
$$G_1 \times G_2 \times \cdots \times G_n / H_1 \times H_2 \times \cdots \times H_n \approx G_1/H_1 \times G_2/H_2 \times \cdots \times G_n/H_n.$$ 
So option (b) is true.\\
Note that normality is not transitive. Let $G = A_4$ and let $G_2 = \{e, (1,2)(3,4), (1,3)(2,4), (1,4)(2,3)\} \approx K_4$ (abelian) is normal in $G = A_4$ since every conjugate of a non-trivial element of $G_1=K_4$ in $A_4$ (or $S_4$) is again of the form $(a,b)(c,d)$ (same cycle-decomposition) which is already included $G_2$. Let $G_1 = \{e, (1,2)(3,4)\}$. Then $G_1$ is normal in $G_2$ as it is of index $2$. But $G_1$ is not normal in $G = A_4$ as 
$$(1,2,3) [(1,2)(3,4)] (1,3,2)= (1,3)(2,4) \not\in G_1.$$
So option (c) is false.\\
Option (d) is also false because the subgroup $H = \{e, \varphi\}$, where $\varphi = (1,2)$ is of index $3$ (prime) in $G = S_3$, but is not normal.
