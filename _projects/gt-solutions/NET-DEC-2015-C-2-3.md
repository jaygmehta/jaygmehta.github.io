---
layout: page
title: NET-DEC-2015-C-2-3
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a simple group of order $60$. Then

(a) $G$ has six Sylow-$5$ subgroups.<br>
(b) $G$ has four Sylow-$3$ subgroups.<br>
(c) $G$ has cyclic subgroup of order $6$.<br>
(d) $G$ has a unique element of order $2$.<br>

**Solution**

(a) $1+5 \lambda \mid 2^2 \times 3 \times 5$. But $(1+5\lambda,5)=1$ and hence $1+5\lambda \mid 12$ which implies $\lambda =0$ or $1$. Since $G$ is simple, $\lambda=0$ is not possible. Then $\lambda=1$ implies $1+5\lambda =6$. Thus, the number of $5$-Sylow subgroups of $G$ is $6$.<br>

(b) %$1+3\lambda \mid 2^2 \times 5$ implies $\lambda = 0, 1, 3$. But $G$ being simple, $\lambda=0$ is not possible. Hence the number of $3$-Sylow subgroups of $G$ can be $4$ (if $\lambda=1$) or $10$ (if $\lambda=3$).\\
If there are four $3$-Sylow subgroups (i.e. subgroups of order $3$) of $G$ then number of elements of  order $3$ in $G$ will be $8$. However, we know that $A_5$ is a simple group of order $60$ and it has $\displaystyle \frac{^5P_3}{3}=5 \times 4=20$ elements of order $3$ (i.e. $3$-cycles). Hence, this case is not true. (Note that all $3$ cycles are even permutation and hence the number of $3$ cycles in $S_5$ and $A_5$ is same.)<br>

(c) If we take $G=A_5$ then this case is not possible as $A_5$ cannot have an element of order $6$. The reason is in $A_5$ there is no possibility of $6$-cycle. So clearly the element of order $6$ is a product of a $2$-cycle and a $3$-cycle which is an odd permutation and hence it cannot be in $A_5$.<br>

(d) Since $G$ is simple, $G$ has at least two $2$-Sylow subgroups and they have order $4$. So $G$ has at least two elements of order $2$ (in either case $\mathbb Z_4$ or $\mathbb Z_2 \times \mathbb Z_2$).