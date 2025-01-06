# **NET DEC 2012 (C):** 

For positive integers $m$, let $\phi(m)$ denote
the number of integer $k$ such that $1 \le k \le n$ and GCD$(k,m)=1$.
Then which of the following statements are necessarily true?

(a) $\phi(n)$ divides $n$ for every positive integer $n$.<br>
(b) $n$ divides $\phi\big(a^n-1\big)$ for all positive integers $a$ and $n$.<br>
(c) $n$ divides $\phi\big(a^n-1\big)$ for all positive integers $a$ and $n$ such that GCD$(a,n)=1$.<br>
(d) $a$ divides $\phi\big(a^n-1\big)$ for all positive integers $a$ and $n$ such that GCD$(a,n)=1$.

**Solution**

1.  Take $n=10$. Then $\phi(n)=4$ and $\phi(n) \nmid n$. Also,
    $\phi(p)=p-1 \nmid p$.<br>

2.  For $a>1$, first we show that order of $a$ modulo $a^n-1$ is $n$,
    i.e. ${\rm ord}_{a^n-1}(a) = n$. Suppose ${\rm ord}_{a^n-1}(a)=d$.
    If $d < n$ then $a^d < a^n$, so $a^d-1 < a^n-1$. In this case,
    $a^d - 1 \not\equiv 0 \pmod {a^n-1}$.<br>

    Now, since $(a,a^n-1)=1$, by Euler's theorem
    $a^{\phi(a^n-1)} \equiv 1 \pmod{a^n-1}$ or
    $a^{\phi(a^n-1)}-1 \equiv 0\pmod{a^n-1}$. Since the order of $a$ is
    $n$, $n\mid \phi\big(a^n-1\big)$.<br>

3.  Same as above. It is true in general and therefore true for all
    $a,n$ with GCD$(a,n)=1$.<br>

4.  Take $a=3$, $n=2$, we have $a^n-1 = 9-1=8$ and therefore
    $\phi(a^n-1)=\phi(8)=4$ and so $a \nmid \phi(a^n-1)$. This case is
    not true.


