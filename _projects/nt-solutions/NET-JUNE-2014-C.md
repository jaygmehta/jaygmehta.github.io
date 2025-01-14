---
layout: page
title: NET JUNE 2014 (C)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET JUNE 2014 (C):**  -->

For positive integers $m$ and $n$, let
$F_n = 2^{2^n}+1$ and $G_m= 2^{2^m}-1$. Which of the following are true?

(a) $F_n$ divides $G_m$ whenever $m>n$.<br>
(b) $\gcd(F_n,G_m) = 1$ whenever $m \neq n$.<br>
(c) $\gcd(F_n,F_m) = 1$ whenever $m \neq n$.
(d) $G_m$ divides $F_n$ whenever $m < n$.<br>

**Solution**

Note that the integers $F_n$ are called Fermat's numbers.<br>

1.  For all $m$, note that
    $G_m = 2^{2^m}-1 = (2^{2^{m-1}})^2 - 1= (2^{2^{m-1}} - 1)(2^{2^{m-1}} + 1) = G_{m-1}F_{m-1}$.<br>

    Again $G_{m-1} = G_{m-2} F_{m-2}$ and so
    $G_m = G_{m-2}F_{m-2}F_{m-1}$. Therefore, if $n < m$, then
    recursively we get 

    $$G_m = G_nF_n F_{n+1} \cdots F_{m-2}F_{m-1}.$$
    
    Therefore $F_n \mid G_m$ if $m > n$.<br>

2.  Since $F_n \mid G_m$ if $m > n$, we conclude that
    $\gcd(F_n,G_m) \neq 1$ when $m > n$. Hence, this option is not
    correct.<br>

3.  Note that 

    $$\begin{align*}
    F_{n+1} =&\ 2^{2^{n+1}}+1\\
    =&\ 2^{2^{n+1}}-1 + 2\\
    =&\ \big((2^{2^n})^2 - 1\big) + 2\\
    =&\ (2^{2^n}+1)(2^{2^n}-1) + 2\\
    =&\ F_n \big((2^{2^{n-1}})^2 - 1\big) + 2\\
    %=&\ F_n (2^{2^{n-1}}+1) (2^{2^{n-1}}-1) +2\\
    =&\ F_n F_{n-1} (2^{2^{n-1}}-1) +2\\
    =&\ \quad \vdots\\
    =&\ F_n F_{n-1} \cdots F_1 F_0 + 2.
    \end{align*}$$

    Thus, if $m < n$, then
    $F_n = F_{n-1} F_{n-2} \cdots F_{m+1} F_m F_{m-1} \cdots F_1 F_0+2$.<br>

    Suppose $\gcd(F_n,F_m) = d$. Then $d\mid F_n$ and $d_\mid F_m$. Then
    by above expression, we say that $d \mid 2$. Therefore, $d = 1$ or
    $d=2$. But since $F_n$ and $F_m$ are odd numbers, $d\neq 2$. Hence,
    $d = 1$. This options is **correct**.<br>

4.  # **Not True.** Example, take $m=2$ and $n =3$. Then
    $G_2 = 2^{2^2} - 1 = 2^4-1 = 15$ and
    $F_3 = 2^{2^3} + 1 = 2^8+1 = 256 + 1 = 257$. Neither $3$ nor $5$
    divides $257$ and hence $G_2 = 15 \nmid 257 = F_3$.


