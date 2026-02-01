---
layout: page
title: NET-JUNE-2016-B
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G=(\mathbb Z/25\, \mathbb Z)^*$ be the group units (i.e. the elements that have multiplicative inverse) in the ring $(\mathbb Z/25\, \mathbb Z)$. Which of the following is a generator of $G$?

(a) $3$<br>
(b) $4$<br>
(c) $5$<br>
(d) $6$<br>

**Solution**

We know that $(\mathbb Z/25\, \mathbb Z)^* = U(25)$ is a cyclic group as $=25=5^2$ is of the form $p^k$ for odd prime $p$. The order of $U(25)$ is $\phi(25) = (5^2-5) = 20$. In fact,
$$U(25) = \{1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24\}.$$
If $a \in U(25)$, then $o(a) \mid 20$, i.e. $o(a) = 1,2,4,5,10,20$. We show that $o(2) \neq 1,2,4,5,10$. Then $2$ becomes a generator of $U(25)$.\\
$2^2 = 4 \neq 0 \pmod{25}$, $2^4 = 16 \neq 0 \pmod{25}$, $2^{5} = 32 \equiv 7 \neq 0 \pmod{25}$, $2^{10} = 1024 \equiv 24\neq 0 \pmod{25}$.\\
We know that if $g$ is one generator (primitive root mod $n$) of $U(n)$, then other generators are of the form $g^{i}$, where $\gcd(i,\phi(n))=1$.

(a) $3$ is a generator of $(\mathbb Z/25\, \mathbb Z)^*$ as $2^7 = 128 \equiv 3 \pmod{25}$.<br>

(b) $2^2 = 4$ but power is $2$ and $\gcd(2,20) = 2\neq 1$. Hence, $4$ is not a generator.<br>

(c) $5 \times 5 = 25 \equiv 0 \pmod{25}$. Hence, $5$ is not a unit, i.e. $5 \not\in U(25)$.<br>

(d) $2^8 = 256 \equiv 6 \pmod{25}$ but power is $8$ and $\gcd(8,20) = 2\neq 1$. Hence, $2^8 = 6$ is not a generator.