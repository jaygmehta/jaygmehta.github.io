---
layout: page
title: NET DEC 2013 (B)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2013 (B):**  -->

For any integers $a, b$, let $N_{a,b}$ denote the
number of positive integers $x < 1000$ such that $x \equiv a \pmod {27}$
and $x \equiv b \pmod{37}$. Then,

(a) There exists $a,b$ such that $N_{a,b} =0$.<br>
(b) For all $a,b$, $N_{a,b} = 1$.<br>
(c) For all $a,b$, $N_{a,b} > 1$.<br>
(d) There exists $a, b$ such that $N_{a,b} =1$ and there exists $a,b$ such that $N_{a,b}=2$.<br>

**Solution**

**Chinese Remainder Theorem:** Let $m_1,\ldots,m_r$ be pairwise
relatively prime integers, i.e. $(m_i,m_j)=1$ if $i \neq j$. Let
$a_1,\ldots,a_r$ be arbitrary integers. Then the system of congruences

$$\begin{align*}
x &\ \equiv a_1 \pmod{m_1}\\
&\ \ \ \vdots\\
x &\ \equiv a_r \pmod{m_r}
\end{align*}$$

has exactly one solution modulo $M=m_1m_2\cdots m_r$.\
Here $a_1=a$, $a_2=b$, $m_1=27$, $m_2=37$, and $\gcd(m_1,m_2)=1$.
Therefore $M=m_1m_2=999$ and hence (by Chinese Remainder Theorem) the
system of congruence 

$$\begin{align*}
k \equiv &\ a \pmod {27}\\
k \equiv &\  b \pmod{37}
\end{align*}$$

has unique solution modulo $999$, i.e. there exists
unique $x$, $1 \le x \le 999$, which satisfies both the above
congruences simultaneously. Hence, $N_{a,b} = 1$ for all integers $a$
and $b$.

