# **NET 26 NOV 2020 (B): 2 of 2** 

Let $\varphi(n)$ be the cardinality of the set
$\{a \mid 1 \le a \le n, \ (a,n) = 1\}$, where $(a,n)$ denotes the gcd
of $a$ and $n$. Which of the following is NOT true?

(a) There exists infinitely many $n$ such that $\varphi(n) > \varphi(n+1)$.<br>
(b) There exists infinitely many $n$ such that $\varphi(n) < \varphi(n+1)$.<br>
(c) There exists $N \in \mathbb N$ such that $N > 2$ and for all $n > N$,
$\varphi(N) < \varphi(n)$.<br>
(d) The set $\left\{\frac{\varphi(n)}{n} : n \in \mathbb N\right\}$ has finitely many limit points.

**Solution**

1.  This is true as for every $n$ prime,
    $\varphi(n) = n-1 > \varphi(n+1)$ as $n+1$ is not prime and there
    are infinitely many primes. So this statement is true and hence it
    is not the correct option.<br>

2.  This statement is also true when $n+1$ is primes. Then
    $\varphi(n+1) = n$ and $n$ is not prime and so
    $\varphi(n) < n = \varphi(n+1)$. So this is also not the correct
    option.<br>

3.  If $N$ is odd, then
    $\varphi(2N) = \varphi(2) \varphi(N) = \varphi(N)$. So for $n = 2N$,
    the statement does not hold. Similarly, show for $N$ even.<br>

4.  Only left option and hence it must be correct.<br>


