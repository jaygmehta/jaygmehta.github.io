---
layout: page
title: NET 30 NOV 2020 (C)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET 30 NOV 2020 (C): 2 of 3**  -->

For a positive integer $n$, let $\varphi(n)$ be
the Euler's $\varphi$-function. Which of the following statements are
true for $n > 3$?

(a) $\varphi(n)$ can never divided $n$<br>
(b) $\varphi(n) \mid n \Rightarrow$ there exists integers $x,y$ such that $nx+6y = 1$<br>
(c) $\varphi(n) \mid n \Rightarrow$ $n$ can have at most two distinct prime divisors<br>
(d) $\varphi(n) \mid \varphi(nk)$ for every positive integer $k$.<br>

**Solution**

1.  This is false since for $n = 8$, $\varphi(n)= \varphi(8) = 4$ and
    $4 \mid n=8$.<br>

2.  We know (by Bezout's identity) that for integers $a$ and $b$
    $\gcd(a,b) = 1$ if and only if there exists integers $x$ and $y$
    such that $ax+by = 1$.\
    By this, here we have $\gcd(n,6) = 1$. This is false, since
    $\varphi(8) = 4 \mid 8$ but $\gcd(8,6) \neq 1$. In other words, if
    $n=8$, then $1= 8x+6y = 2(4x+3y)$ is not possible as $2 \mid$ RHS
    but $2 \nmid$ LHS.<br>

3.  This option is **True**. Note that $\varphi(n)$ is always even. So
    if $\varphi(n)\mid n$, then $n$ cannot be odd. Suppose
    $n = p^\alpha q^\beta 2^\gamma$ be product of $3$ primes. Then
    $\varphi(n) = p^{\alpha-1}q^{\beta-1}2^{\gamma-1}(p-1)(q-1)(2-1)$.
    Then $2^{\gamma+1} \mid \varphi(n)$ but $2^{\gamma+1}\nmid n$. So
    $\varepsilon(n)$ cannot divide $n$. So this is be true.<br>

4.  Let $n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_s^{\alpha_s}$. Then
    $\varphi(n) = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_s^{\alpha_s-1}(p_1-1)(p_2-2)\cdots (p_s-1)$.<br>

    If
    $k = p_1^{\beta_1} p_2^{\beta_2} \cdots p_s^{\beta_s} q_1^{\gamma_1}\cdots q_t^{\gamma_t}$,
    where $\beta_i \ge 0$ and $\gamma_j \ge 0$, then
    $$nk = p_1^{\alpha_1+\beta_1} p_2^{\alpha_2+\beta_2} \cdots p_s^{\alpha_s+\beta_s}q_1^{\gamma_1}\cdots q_t^{\gamma_t}$$
    and so
    $$\varphi(nk) = p_1^{\alpha_1+\beta_1-1} p_2^{\alpha_2+\beta_2-1} \cdots p_s^{\alpha_s+\beta_s-1}q_1^{\gamma_1-1}\cdots q_t^{\gamma_t-1}.$$
    Clearly, $\varphi(n) \mid \varphi(nk).$


