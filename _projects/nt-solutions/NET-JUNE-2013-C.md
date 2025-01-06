# **NET JUNE 2013 (C):** 

Consider the congruence
$x^n \equiv 2 \pmod {13}$. This congruence has a solution for $x$ if

(a) $n=5$.<br>
(b) $n=6$.<br>
(c) $n=7$.<br>
(d) $n=8$.<br>


**Solution**

By Euler's theorem, if $a$ is relatively prime to $m$, then
$a^{\phi(n)}\equiv 1 \pmod m$. Here $m=13$, $\phi(13)=12$ and hence if
$13\nmid x$ then the congruence $x^{12} \equiv 1 \pmod {13}$ has a
solution.

1.  The congruence $x^5 \equiv 2 \pmod {13}$ implies
    $x^{15} \equiv 2^3 \pmod{13}$, i.e.
    $x^{12} x^3 \equiv x^3 \equiv 2^3 \pmod{13}$. It has a solution,
    $x=2$.<br>

2.  The congruence $x^6 \equiv 2 \pmod {13}$ implies
    $x^{12} \equiv 2^2 \pmod{13}$, i.e. $1\equiv 4 \pmod{13}$ which is
    not possible. Hence, this congruence does not have a solution.<br>

3.  The congruence $x^7 \equiv 2 \pmod {13}$ implies
    $x^{14} \equiv 2^2 \pmod{13}$, i.e.
    $x^{12} x^2 \equiv x^2 \equiv 2^2 \pmod{13}$. It has a solution,
    $x=2$.<br>

4.  The congruence $x^8 \equiv 2 \pmod {13}$ implies
    $x^{24} \equiv 2^3 \pmod{13}$, i.e. $1\equiv 8 \pmod{13}$ which is
    not possible. Hence, this congruence does not have a solution.<br>


