---
layout: page
title: NET 30 NOV 2020 (C)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET 30 NOV 2020 (C): 1 of 3**  -->

For positive integers $m$ and $n$, let $\gcd(m,n)$ denote their greatest common divisor. Let $m > n$ be such
that $\gcd(m,n) =1$. Which of the following statements are true?

(a) $\gcd(m-n,m+n) = 1$<br>
(b) $\gcd(m-n,m+n)$ can have a prime divisor<br>
(c) There exists integers $x,y$ such that $nx-my = 3$<br>
(d) $\gcd(m-n,m+n)$ can be an odd prime<br>

**Solution**

Let $d = \gcd(m-n,m+n)$. Then $d\mid m-n$ and $d \mid m+n$. But then
$d\mid (m-n)+(m+n) = 2m$. Similarly, $d \mid 2n$. Since $d\mid 2m$ and
$d\mid 2n$, we have 

$$d\mid \gcd(2m,2n) = 2 \gcd(m,n) = 2\cdot 1 = 2.$$

Therefore, $d = 1$ or $d=2$. Since $d=2$ is a possibility, option (a)
and option(d) are # **Not true** and option (b) is **true**.<br>

Also since $\gcd(m,n)=1$ (by Bezout's identity), there exists integers
$x'$ and $y'$ such that $mx'+ny' = 1$. Multiplying both sides by $3$, we
get $m(2x') - n(-3y') = 3.$ Taking $x = 3x'$, $y = -3y'$, we have
$mx-ny=3$. So option (c) is also **true**.


