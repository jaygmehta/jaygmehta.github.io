---
layout: page
title: NET-SEPT-2022-C-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Which of the following statements are necessarily true regarding a group of order $2022$?

(a) Let $g$ be an element of odd order in $G$ and $s_g$ the permutation of $G$ given by $s_g(x) = gx$ for $x \in G$. Then $s_g$ is an even permutation.<br>
(b) Let $H = \{g \in  G \mid o(g) \text{ is odd}\}$ is a normal subgroup of $G$.<br>
(c) $G$ has a normal subgroup of index $337$.<br>
(d) $G$ has only two normal subgroups.<br>

**Solution**

Let $g$ be of order $m$, where $m$ is odd. Then the permutation $s_g$ consists of cycles $(x,gx,g^2x,\ldots, g^{m-1}x)$ for some $x \in G$, which is a cycle of length $m$ (odd). Thus, each cycle is an even permutation and consequently $s_g$ is an even permutation, so the first option (a) is correct.\\
The prime factorization of $2022 = 2 \times 3 \times 337$. 
Note that $n_{337} = 1$ (by third Sylow's theorem) and so $G$ has a normal subgroup of order $337$. So $G$ has at least three normal subgroups (including $\{e\}$ and $G$) and so last option (d) is not correct.\\
Here, the elements of odd order are the elements of $3$ or $337$, which exists by Cauchy's theorem and form groups of order $3$ and $337$, say $H$ and $K$, respectively. Since $K$ is normal (being unique Sylow subgroup), $HK$ is also a subgroup of $G$, containing elements of order $3$, $337$ and possibly $3 \times 337$. Thus, $H = \{g \in  G \mid o(g) \text{ is odd}\}$ is a normal subgroup of $G$, in this case, where $o(G) = 2022$ (need not be true in general). So the second option (b) is true.\\
Let $K$ be a normal subgroup of index $337$. Then $o(K) = 6$. Then $HK$ will be a subgroup of $G$ with $G = HK$ as both $H$ and $K$ are normal, where $H$ is a unique $337$-Sylow subgroup. But, then since $G$ will be abelian (as an application of Sylow's theorem). But $S_3 \times \mathbb Z_{337}$ is a non-abelian group of order $2022$. So the third option (c) is not true.


