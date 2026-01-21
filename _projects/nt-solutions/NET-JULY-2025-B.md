---
layout: page
title: NET JULY 2025 (B)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET JULY 2025 (B):**  -->

Which of the following statements is true?

(a) $p\mid 1 + (p-1)!$ for some odd prime $p$.<br>
(b) $p \mid (1234)^{p-1} - 1$ for all primes $p > 700$.<br>
(c) There exists $a \in \mathbb Z$ and a prime $p > 11$ such that $p \nmid a^p - a$.<br>
(d) $p \nmid \frac{(p^2)!}{(p!)^2}$ for some odd prime $p$.<br>

**Solution**

By Wilson's theorem, $(p-1)! \equiv 1 \pmod p$, i.e., $p \mid (p-1)!+1$. So, the option (a) is *false*.

Fermat's little theorem: if $p$ is a prime and $a \in \mathbb Z$ such that $\gcd(a,p) = 1$, then $a^{p-1} \equiv 1 \pmod p$. Here $a = 1234 = 2 \times 617$ and $617$ is prime. Thus, if $p>700$ is a prime, then $\gcd(1234,p) = 1$. Hence, by Fermat's theorem, $(1234)^{p-1} \equiv 1 \pmod p$, i.e., $p \mid (1234)^{p-1} - 1$. So, option (b) is **true**.

Multiplying $p$ to both sides in Fermat's theorem, we get $a^p \equiv a \pmod p$ if $\gcd(a,p) = 1$. If $\gcd(a,p) \neq 1$, then $p \mid a$ and so $a\equiv 0 \pmod p$ and also $a^p \equiv 0 \equiv a \pmod p$. Thus, for any integer $a$ and any prime $p$, we have Fermat's little theorem (version 2): $a^p \equiv a \pmod p$, i.e., $p \mid a^{p} - a$. So, option (c) is *false*.

Note that, for any odd prime $p$, $p^2 \mid (p!)^2$, but $p^3 \nmid (p!)^2$. However, $p^3 \mid (p^2)!$. Hence, $p \mid \frac{(p^2)!}{(p!)^2}$ for all (odd) primes $p$. So, option (d) is *false*.


