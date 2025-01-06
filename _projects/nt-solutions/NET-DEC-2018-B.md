# **NET DEC 2018 (B):** 

Given integers $a$ and $b$, let $N_{a,b}$ denote
the number of positive integers $k < 100$ such that $k \equiv a \pmod 9$
and $k \equiv b \pmod{11}$. Then which of the following statements is
correct?

(a) $N_{a,b} =1$ for all integers $a$ and $b$.<br>
(b) There exists integers $a$ and $b$ satisfying $N_{a,b} > 1$.<br>
(c) There exists integers $a$ and $b$
satisfying $N_{a,b} =0$.<br>
(d) There exists integers $a$ and $b$ satisfying
$N_{a,b} =$ and there exists integers $c$ and $d$ satisfying
$N_{c,d} > 1$.<br>

**Solution**

**Chinese Remainder Theorem:** Let $m_1,\ldots,m_r$ be pairwise
relatively prime integers, i.e. $(m_i,m_j)=1$ if $i \neq j$. Let
$a_1,\ldots,a_r$ be arbitrary integers. Then the system of congruences
$$\begin{align*}
x &\ \equiv a_1 \pmod{m_1}\\
&\ \ \ \vdots\\
x &\ \equiv a_r \pmod{m_r}
\end{align*}$$
has exactly one solution modulo $M=m_1m_2\cdots m_r$.
The solution is given as follows:
$$x=a_1M_1 b_1 + a_2 M_2 b_2 + \cdots + a_r M_r b_r,$$ 
where
$M_k = \frac{M}{m_k}$ and $b_k$ is the solution of the congruence
$M_kx \equiv 1 \pmod{m_k}$.

Here $a_1=a$, $a_2=b$, $m_1=9$, $m_2=11$, and $\gcd(m_1,m_2)=1$.
Therefore $M=m_1m_2=99$ and hence (by Chinese Remainder Theorem) the
system of congruence 
$$\begin{align*}
k \equiv &\ a \pmod 9\\
k \equiv &\  b \pmod{11}
\end{align*}$$ 
has unique solution modulo $99$, i.e. there exists
unique $k$, $1 \le k \le 99$, which satisfies both the above congruences
simultaneously. Hence, $N_{a,b} = 1$ for all integers $a$ and $b$.

