---
layout: page
title: NET-DEC-2014-C-1-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a group of order $45$. Then 

(a) $G$ has an element of order $9$.<br>
(b) $G$ has a subgroup of order $9$.<br>
(c) $G$ has a normal subgroup of order $9$.<br>
(d) $G$ has a normal subgroup of order $5$.<br>

**Solution**

(a) The group $\mathbb Z_5 \times \mathbb Z_3 \times \mathbb Z_3$ does not have any element of order $9$. So this is not true.<br>
(b) By Sylow's theorem if $p^\alpha \mid o(G)$, then $G$ has a subgroup of order $p^\alpha$ for a prime $p$ and any positive integer $\alpha$. Here $3^2 \mid o(G)=45$. Therefore, $G$ has a subgroup of order $9$.<br>
(c) $1+3\lambda \mid 45$ by third part of Sylow's theorem. However $(1+3\lambda,3^3)=1$ and hence $1 + 3\lambda \mid 5$ which implies $\lambda=0$. Thus, $G$ has a unique $3$-Sylow subgroup of order $9$ which is normal.<br>
(d) $1+5\lambda \mid 9$ implies $\lambda=0$ and hence the $5$-Sylow subgroup of $G$ is unique and therefore normal.