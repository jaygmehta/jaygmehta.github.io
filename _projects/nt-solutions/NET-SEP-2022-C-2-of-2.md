# **NET SEP 2022 (C): 2 of 2** 

Consider the function $f(n) = n^5 - 2n^3 + n$,
where $n$ is a positive integer. Which of the following statements are
true?

(a) For every positive integer $k$, there exists a positive integer $n$ such that $f(n)$ is divisible by $2^k$.<br>
(b) $f(n)$ is even for every integer $n \ge 20$.<br>
(c) For every integer $n \ge 20$, either $f(n)$ is odd or $f(n)$
is divisible by $4$.<br>
(d) For every odd integer $n \ge 21$, $f(n)$ is divisible by $64$.

**Solution**

Observe that
$$f(n) = n^5 - 2n^3 + n = n (n^4 - 2n^2 + 1) = n (n^2-1)^2 = n (n-1)^2 (n+1)^2.$$
Note that $n \mid f(n)$. Let $k \in \mathbb N$, taking $n = 2^k$, we
have $2^k \mid f(n) = f(2^k)$. Thus, option (a) is true.<br>

If $n$ is odd, then $(n-1)$, $(n+1)$ are even and hence $f(n)$ is even.
Clearly, if $n$ is even, then $f(n)$ is even. Thus, option (b) is
correct.<br>

Option (c) is false because for $n = 22$, $f(n) = 22 (21)^2 (23)^2$ is
neither odd nor divisible by $4$ (it is only divisible by $2$).
Similarly, $n = 26, 30$, etc. works.<br>

Let $n$ be an odd integer. Then $n = 4k+1$ or $n=4k+3$. If $n = 4k+1$,
then $n-1 = 4k$ and so $(n-1)^2$ is divisible by $16$. Also,
$(n+1)^2 = (4k+2)^2 = 4 \cdot (2k+1)^2$. This shows that $f(n)$ is
divisible by $64$. Similarly, it can be easily seen that $f(n)$ is
divisible by $64$ if $n=4k+3$. Thus, option (d) is correct.


