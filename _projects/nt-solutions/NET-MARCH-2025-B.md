---
layout: page
title: NET MARCH 2025 (B)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET MARCH 2025 (B):**  -->

Let $p$ be a prime number. An element $a$ of the group $(\mathbb{Z}/p\mathbb{Z})^\times$
is a primitive root $(\mathbb{Z}/p\mathbb{Z})^\times$ if the order of $a$ in $(\mathbb{Z}/p\mathbb{Z})^\times$ is $p-1$.
Let $S_p$ be the number of primitive roots in $(\mathbb{Z}/p\mathbb{Z})^\times$
and let $\varphi$ denote Euler's $\varphi$-function.
Which of the following statements is true?

(a) For each $p<100$,
$$
\sum_{n=1}^{\infty}\left(\frac{S_p}{\varphi(p)}\right)^n
$$
converges.<br>
(b) For each $100 \le p \le 200$,
$$
\sum_{n=1}^{\infty}\left(\frac{S_p}{\varphi(p)}\right)^n
$$
diverges.<br>
(c) For each $p>200$,
$$
\sum_{n=1}^{\infty}\left(\frac{S_p}{\varphi(p)}\right)^n
$$
converges.<br>
(d) The element $4 \bmod 101$ in $(\mathbb{Z}/101\mathbb{Z})^\times$ is a primitive root.<br>

**Solution**

For a prime $p$, we have $\varphi(p)=p-1$ and
$$
S_p=\varphi(p-1).
$$
Hence the series is geometric with ratio
$$
r=\frac{\varphi(p-1)}{p-1}.
$$
For any odd prime $p$, $\varphi(p-1)<p-1$, so $r<1$ and the series converges.
The only exception is $p=2$, where $r=1$.\\
Thus (a) is false since $p=2<100$.
All primes in $[100,200]$ are odd, so (b) is false.\\
For all $p>200$, the series converges, so (c) is true.\\
Finally, since $2$ has order $100$ modulo $101$, the order of $4=2^2$ is
$$
\frac{100}{\gcd(100,2)}=50\neq 100,
$$
so (d) is false.


