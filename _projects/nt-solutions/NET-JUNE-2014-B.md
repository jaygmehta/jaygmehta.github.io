---
layout: page
title: NET JUNE 2014 (B)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET JUNE 2014 (B):**  -->

If $n$ is a positive integer such that sum of all
positive integers $a$ satisfying $1 \le a \le n$ and $\gcd(a,n)=1$ is
equal to $240 n$, then the number of summands, namely, $\phi(n)$, is

(a) $120$.<br>
(b) $124$.<br>
(c) $240$.<br>
(d) $480$.<br>

**Solution**

We know that, if $k < n$ and $(k,n)=1$ then $(n-k,n)=1$ (an easy
exercise). The number of integers $k<n$ such that $(k,n)=1$ is
$\phi(n)$. Pairing $k$ and $n-k$ will add up to $n$. So adding all these
integers we get $\underbrace{n+n+\cdots+n}_{\phi(n)\ {\rm times}}$, i.e.
$\frac{n\phi(n)}{2}$.<br>

Here, we are given that $\frac{n\phi(n)}{2}=240n$ which implies
$\phi(n)=480$.


