---
layout: page
title: NET-DEC-2023-C-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be the group (under matrix multiplication) of $2\times 2$ invertible matrices with entries from $\mathbb{Z}/9\mathbb{Z}$. Let $a$ be the order of $G$.
Which of the following statements are true?

(a) $a$ is divisible by $3^4$.<br>
(b) $a$ is divisible by $2^4$.<br>
(c) $a$ is not divisible by $48$.<br>
(d) $a$ is divisible by $3^6$.<br>

**Solution**

The group $G$ is $\mathrm{GL}(2,\mathbb{Z}/9\mathbb{Z})$.
For a prime $p$ and $k \ge 1$, the order of $\mathrm{GL}(n,\mathbb{Z}/p^k\mathbb{Z})$ is
$
|\mathrm{GL}(n,\mathbb{Z}/p^k\mathbb{Z})|
=
p^{n^2(k-1)}|GL_n(\mathbb Z_p)|.$
Here, $n=2$, $p=3$ and $k=2$, so
$$
a = 3^{4(2-1)}(3^2-1)(3^2-3) = 3^{4}(9-1)(9-3) = 81 \cdot 8 \cdot 6 = 3888.
$$
Factorizing, we get
$
3888 = 2^4 \times 3^5.
$ 
So, only options (a) and (b) are correct.
