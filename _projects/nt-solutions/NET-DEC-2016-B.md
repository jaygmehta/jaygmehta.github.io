---
layout: page
title: NET DEC 2016 (B)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Given a natural number $n >1$ such that
$(n-1)! \equiv -1 \pmod n$, we can conclude that

(a)$n=p^k$ where $p$ is prime, $k>1$.<br>
(b) $n=pq$ where $p$ and $q$ are distinct primes.<br>
(c) $n=pqr$ where $p,q,r$ are distinct primes.<br>
(d) $n=p$ where $p$ is a prime.<br>

**Solution**

Suppose $n=kl$ for some integers $k$ and $l$. Without loss of generality
assume $k<n$ (i.e. $k\neq n$). Now, $(n-1)! \equiv -1 \pmod n$ implies
$n \mid (n-1)! + 1$. Since $k < n$, $k \mid (n-1)!$. Also, $k \mid n$
and $n \mid (n-1)! +1$ and so $k \mid (n-1)! +1$. Hence $k \mid 1$ or
$k=1$. Thus, $n$ must be prime.


