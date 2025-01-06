# **NET 26 NOV 2020 (B): 1 of 2** 

Which of the following is true?

(a) Every even integer $n \ge 16$ divides $(n-1)!+3$<br>
(b) Every odd integer $n \ge 16$ divides $(n-1)!$<br>
(c) Every even integer $n \ge 16$ divides $(n-1)!$<br>
(d) For every even integer $n \ge 16$, $n^2$ divides $n!+1$<br>

**Solution**

1.  Suppose $n$ is even and $n \mid (n-1)!+3$. Since $n$ is even,
    $2 \mid n$ and so $2 \mid (n-1)!+3$ which is not possible as
    $(n-1)!+3$ is always odd.<br>

2.  This is not true. Take $n = 17$. Then $17 \nmid 16!$.\
    In general, for any prime $p$, $p \nmid (p-1)!$. By Wilson's
    theorem, $(p-1)! \equiv 1 \pmod p$.<br>

3.  This is **true**. Let $n = 2k$ be even integer $n \ge 16$. Then
    $n-1 = 2k-1$ and 
    $$\begin{align*}
    (n-1)! = (2k-1)! =&\ 1 \times 2 \times 3 \times \cdots \times k \times (k+1) \times \cdots (2k-1)\\
    =&\ 2 \times k \times [ 3 \times \cdots \times (k-1) \times (k+1) \times \cdots \times (2k-1)].\\
    =&\ 2k \times \text{some integer } m.
    \end{align*}$$ 
    Hence, $n \mid (n-1)!$.\
    Note that, if $n$ is composite $n \mid (n-1)!$ and more generally,
    $\gcd(n,(n-1)!) = 1$ or $n$.<br>

4.  This is not true as $17^2 \nmid 17! + 1$. For any prime $p$,
    $p^2 \nmid p!+1$. This is because $p! = p(p-1)!$ and so $p!+1$ is of
    the for $kp+1$ and we know that $\gcd(p^m,pk+1) = 1$.


