# **NET FEB 2022 (C): 2 of 3** 

For a positive integer $n$, let $\Omega(n)$ denote
the number of prime factors of $n$ counted with multiplicity. For
instance, $\Omega(3) = 1$, $\Omega(6) = \Omega(9) = 2$. Let $p > 3$ be a
prime number and let $N = p(p+2)(p+4)$. Which of the following
statements are true?

(a) $\Omega(N) \ge 3$<br>
(b) There exists primes $p > 3$ such that $\Omega(N) = 3$<br>
(c) $p$ can never be the smallest prime divisor of $N$<br>
(d) $p$ can be the smallest prime divisor of $N$<br>

**Solution**

We know that a product of $n$ consecutive integers is divisible by $n$.
So product of $3$ consecutive integers $p(p+1)(p+2)$ is divisible by
$3$. Note that $p+1$ is divisible by $3$ if and only if $p+4 = (p+1)+3$
is divisible by $3$. So the product $N=p(p+2)(p+4)$ is divisible by $3$.
Since $p > 3$, $3$ is the smallest prime dividing $N$ and $p$ cannot be
the smallest prime dividing $N$. So option (c) is **correct** and option
(d) is **false**.<br>

Since $p > 3$, $3 \mid (p+2)(p+4)$. So $3$ divides exactly one of them
(but not both). Suppose, without the loss of generality, $3 \mid (p+2)$,
then $p+2$ is composite and so it has one more prime factor. Also $p+4$
has at least one prime factor. Therefore, $N = p (p+2)(p+4)$ has at
least $4$ prime factors. Hence, $\Omega(N) = 3$ is not possible. So
option (b) is **false** and option (a) is **true**.<br>


