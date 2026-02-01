---
layout: page
title: NET-FEB-2022-C
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a group of order $24$. Which of the following statements are necessarily true?

(a) $G$ has a normal subgroup of order $3$<br>
(b) $G$ is not a simple group<br>
(c) There exists an injective group homomorphism from $G$ to $S_8$<br>
(d) $G$ has a subgroup of index $4$<br>

**Solution**

We know that a $p$-Sylow subgroup is normal if and only if it unique. $o(S_4)=24$ and $S_4$ has $3$ subgroups of order $3$. So a subgroup of order $3$ need not be normal.\\
$n_2=1+2k \mid o(G) = 24$. But $\gcd(1+2k,2^3)=1$. So $1+2k \mid 3$. So $n_2 = 1$ or $n_2=3$. Thus, $G$ has either a unique or $3$ subgroups of order $8$ (i.e., $2$-Sylow subgroups). If it is unique, then by second Sylow theorem, it is normal and $G$ cannot be simple. If $G$ has three subgroups of order $8$, then these subgroups will contain elements of order $2$, $4$, or $8$. Total (other than identity), there will be $7 \times 3 = 21$ such elements. Then the remaining $3$ elements will form a unique $3$-Sylow subgroup which will be normal. Summarizing, $G$ has either a unique $2$-Sylow subgroup or a unique $3$-Sylow subgroup which will be normal and hence $G$ cannot be simple.\\
Consider $G = \mathbb Z_{24}$. If there is an injective homomorphism, then $\mathbb Z_{24}$ will be isomorphic to a subgroup of $S_8$. However, $S_8$ cannot have any element of order $24$. So this option is not true.\\
We know that the number of $p$-Sylow subgroups of $G$ is $\frac{o(G)}{o(N(P))}$, where $P$ is one $p$-Sylow subgroup and $N(P)$ is its normalizer. If $n_3=1$, then $G$ has a normal subgroup of order $3$, say $H$. By Cauchy's theorem, there is an element of order $2$ which generates a subgroup $K$ of order $2$. Since $H$ is normal, $HK$ is a subgroup of $G$ of order $6$, and hence index $4$. However, if $n_3 = 4 = \frac{o(G)}{o(N(P))}$, then $N(P)$ is a subgroup of $G$ of index $4$, where $P$ is one $3$-Sylow subgroup of $G$.
