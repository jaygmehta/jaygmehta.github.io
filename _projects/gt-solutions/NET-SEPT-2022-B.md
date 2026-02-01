---
layout: page
title: NET-SEPT-2022-B
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a simple group of order $168$. How many elements of order $7$ does it have?

(a) $6$<br>
(b) $7$<br>
(c) $48$<br>
(d) $56$<br>

**Solution**

$168= 2^3 \times 3 \times 7$. Therefore the number of subgroups of order $7$ (i.e. $7$-Sylow subgroups) is of the form $n_7=1+7k$. But $1+7k \mid o(G)= 2^3 \times 3 \times 7$. Since $\gcd(1+7k,7)=1$, $1+7k \mid 24$. So, $k=0$ or $k=1$, i.e., $n_7=1$ or $n_7=8$. Since $G$ is simple, $1$ is not possible. So, $n_7=8$. Each of this group of order $7$ has $6$ elements of order $7$ (other than $e$). Therefore there are total $8 \times 6 = 48$ elements of order $7$.
