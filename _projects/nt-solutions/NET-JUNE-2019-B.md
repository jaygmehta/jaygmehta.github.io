---
layout: page
title: NET JUNE 2019 (B)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET JUNE 2019 (B):**  -->

For any integer $n \ge 1$, let <br>
$d(n) = $ number of positive divisors of $n$ <br>
$\nu(n) = $ number of distinct prime divisors of $n$<br>
$\omega(n) = $ number of prime divisors of $n$ counted with multiplicity.<br>

[For example, if $p$ is a prime, then $d(p) = 2, \nu(p) = \nu(p^2) = 1, \omega(p^2)=2$].<br>

(a) If $n \ge 1000$ and $\omega(n) \ge 2$, then $d(n) > \log n$<br>
(b) there exists $n$ such that $d(n) > 3 \sqrt{n}$<br>
(c) For every $n$, $2^{\nu(n)} \le d(n) \le 2^{\omega(n)}$<br>
(d) if $\omega(n) = \omega(m)$, then $d(n) = d(m)$<br>

**Solution**

1.  Choose a number $> 1000$ which is a square of a prime, for instance, $n = 1369 = 37^2$. Then $d(n) = 3$ (as $1,37,1369$ are its only divisors). But 
    $\log(1369) > \log(1000) = 3\log (10) = 3$. Thus, $d(n) > \log(n)$ implies $3>3$ which is not possible and hence first option is **incorrect**.

2.  Note that for $d \mid n$, $d \times \frac{n}{d} = n$. Thus, if $d \mid n$ with $d \le \sqrt{n}$, then $\frac{n}{d}$ is a divisor of $n$ which is $\ge \sqrt{n}$. The number of divisors $d$ of $n$ such that $d \le \sqrt{n}$ is at most $\sqrt{n}$ which is in one-one correspondence between $\frac{n}{d}$. So, the total number of divisors of $n$ is $\le 2 \sqrt{n}$, i.e., $d(n) \le 2 \sqrt{n}$. Therefore, this option is also **incorrect**.

3.  Let $n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_s^{\alpha_s}$. 
    Then 
    $d(n) = (\alpha_1 + 1) (\alpha_2 + 1)\cdots (\alpha_s + 1)$. Since $\alpha_i\ge 1$ and $s \ge 1$, we have

    $$2^s \le d(n) \le 2^{\alpha_1 +\cdots + \alpha_s}.$$

    That is, $2^{\nu(n)} \le d(n) \le w^{\omega(n)}$. Hence, this option is **correct**.

4.  Let $n= pq$ and $m =p^2$, where $p$ and $q$ are distinct primes. For example, $n = 15 = 3 \cdot 5$ and $n = 9 = 3^2$. Then $\omega(n) = 2$ and $\omega(m) = 2$ but $d(n) = 4$ while $d(m) = 3$. Therefore, this option is **incorrect**. 