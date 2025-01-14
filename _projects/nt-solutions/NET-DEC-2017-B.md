---
layout: page
title: NET DEC 2017 (B)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2017 (B):**  -->

Let
$f: \mathbb Z \to (\mathbb Z/4\mathbb Z) \times (\mathbb Z/6\mathbb Z)$
be the function $f(n) = (n \mod 4, n\mod 6)$. Then

(a) $(0 \mod 4, 3 \mod 6)$ is in the image of $f$<br>
(b) $(a \mod 4, b \mod 6)$ is
in the image of $f$ for all even integers $a$ and $b$<br>
(c) image of $f$ has
exactly $6$ elements<br>
(d) kernel of $f= 24\mathbb Z$<br>

**Solution**

1.  $f(n) = (0 \mod 4, 3 \mod 6) \Rightarrow n \equiv 0 \pmod 4$ and
    $n \equiv 3 \pmod 6$. Therefore, $n = 6k+3=3(2k+1)$, i.e. $n$ is
    odd. On the other hand, $n = 4k$ which means $n$ is odd. This is a
    contradiction.<br>

2.  By a general version of Chinese Remainder Theorem,
    $x \equiv a \pmod m$ and $x \equiv b \pmod n$ has a solution if
    $\gcd(m,n) \mid a-b$. Here $\gcd(4,6)=2$ and since $a,b$ are even
    $2 \mid a-b$. Hence, the statement is true.<br>

3.  The elements
    $(1,1), (2,2), (3,3), (0,4), (1,5), (2,0), (3,1), (0,2)$ are in
    image which are more than $6$ elements. Hence, the statement is not
    true.<br>

4.  $n \in \ker f \Rightarrow 4 \mid n,\ 6 \mid n$. Therefore,
    ${\rm lcm}(4,6)=12\mid n$. Thus, $\ker f = 12\mathbb Z$.


