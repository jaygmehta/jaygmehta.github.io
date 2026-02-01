---
layout: page
title: NET-JUNE-2018-C-1-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a group with $|G|=96$. Suppose $H$ and $K$ are subgroups of $G$ with $|H|=12$ and $|K|=16$. Then

(a) $H \cap K = \{e\}$<br>
(b) $H \cap K \neq \{e\}$<br>
(c) $H \cap K$ is Abelian<br>
(d) $H \cap K$ is not Abelian<br>

**Solution**

$o(H\cap K) \mid \gcd(o(H),o(K)) = 4$. Therefore, $o(H \cap K) = 1,2$ or $4$. Now,
$$o(G) = \frac{o(H) o(K)}{o(H\cap K)} = \frac{12 \times 16}{o(H \cap K)} > o(G)$$
If $o(H \cap K) =1$. Therefore, $o(H\cap K) = 2$ or $4$, and so $H \cap K \neq \{e\}$. Since, every group of order $2$ and $4$ are abelian, options (a) and (d) are incorrect, whereas options (b) and (d) are correct.