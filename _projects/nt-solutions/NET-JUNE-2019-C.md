---
layout: page
title: NET JUNE 2019 (C)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET JUNE 2019 (C):**  -->

Let $a \in \mathbb Z$ be such that $a=b^2 +c^2$,
where $b,c \in \mathbb Z \smallsetminus \\{0\\}$. Then $a$ cannot be
written as

(a) $pd^2$, where $d \in \mathbb Z$ and $p$ is a prime with
$p \equiv 1 \pmod 4$<br>
(b) $pd^2$, where $d \in \mathbb Z$ and $p$ is a prime
with $p \equiv 3 \pmod 4$<br>
(c) $pqd^2$, where $d \in \mathbb Z$ and $p,q$ are
primes with $p \equiv 1 \pmod 4$, $q \equiv 3 \pmod 4$<br>
(d) $pqd^2$, where
$d \in \mathbb Z$ and $p,q$ are primes with $p, q \equiv 3 \pmod 4$<br>

**Solution**

We know (by **Fermat's theorem on sum of two squares**) that a prime
$p \equiv 1 \pmod 4$ can be written as (and hence divides) sum of two
squares. Also even prime $2 =1^2+1^2$ can be written as a sum of two
squares.<br>

However, a prime $q \equiv 3 \pmod 4$ cannot divide sum of two squares.
The proof is simple and given below:<br>

Let $q = 4k+3$ and $q \mid a^2+b^2$. Then $a^2 \equiv -b^2 \pmod q$. So

$$a^{2(2k+1)} \equiv - b^{2(2k+1)} \pmod q \Rightarrow a^{4k+2} \equiv -b^{4k+2} \pmod q.$$

By (Euler's or) Fermat's little theorem, we have
$a^{4k+2} \equiv b^{4k+2} \equiv 1 \pmod{4k+3}$, where $4k+3=q$, a
prime. Therefore, from above $1 \equiv -1 \pmod q$ which is a
contradiction.


