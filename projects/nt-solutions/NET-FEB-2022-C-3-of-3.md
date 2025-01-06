# **NET FEB 2022 (C): 3 of 3** 

A positive integer $n$ coprime to $17$ is called a
primitive root modulo $17$ if $n^k - 1$ is not divisible by $17$ for all
$k$ with $1 \le k \le 16$. Let $a,b$ be distinct positive integers
between $1$ and $16$. Which of the following statements are true?

(a) $2$ is a primitive root modulo $17$<br>
(b) If $a$ is a primitive root modulo $7$ then $a^2$ is not necessarily a primitive root modulo $17$<br>
(c) If $a, b$ are primitive roots modulo $17$, then $ab$ is a primitive root modulo $17$<br>
(d) Product of primitive roots modulo $17$ between $1$ to $16$ is
congruent to $1$ modulo $17$<br>

**Solution**

1.  A primitive root modulo $n$ is a generator of $Z_n^*$, i.e., it has
    order $n-1$. So a primitive root modulo $17$ has order $16$. Here
    $2^8 \equiv 1 \pmod{17}$.<br>

2.  If $a$ is a primitive root modulo $17$, then $a^2$ cannot be a
    primitive root as $a^2$ will have order $8$ because
    $(a^2)^8 = 1 \pmod{17}$.<br>

3.  If $g$ is a primitive root mod $17$, then every element of
    $\mathbb Z_{17}^*$ can be written as a power of $g$. If $a$ is
    another primitive root, then $a = g^k$. But order of $a = g^k$ is
    $16$ if and only if $\gcd(k,16) = 1$. So, if we have one primitive
    root $g$, then we have $\phi(p-1) = \phi(16) = 8$ primitive roots
    given by $g^k$ where $\gcd(k,16)=1$.<br>

    Check that $3$ is a primitive root modulo $17$, i.e.,
    $3^{16} \equiv 1 \pmod{17}$ and $3^k \neq 1 \pmod{17}$ for all
    $k < 16$. Then all other primitive roots modulo $17$ are
    $$\begin{align*}
    3^3 \equiv &\  10\\
    3^5 \equiv &\  5\\
    3^7 \equiv &\  11\\
    3^{-7} = 3^9 \equiv &\  14\\
    3^{-5} = 3^{11} \equiv &\  7\\
    3^{-3} = 3^{13} \equiv &\  12\\
    3^{-1} = 3^{15} \equiv &\  6
    \end{align*}$$
    Note that $3$ is a primitive root and $5$ is a
    primitive root but $15$ is not. So this option is **False.**<br>

4.  Taking product of all primitive roots modulo $17$, we get
    $$3 \cdot 10 \cdot 5 \cdot 11 \cdot 14 \cdot 7 \cdot 12 \cdot 6 \equiv 3^1 \cdot 3^3 
    \cdot 3^5 \cdot 3^7 \cdot 3^{-7} \cdot 3^{-5} \cdot 3^{-3} \cdot 3^{-1} \equiv 1 \pmod{17}.$$
    So this option is also **true.**


