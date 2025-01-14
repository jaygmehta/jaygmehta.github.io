---
layout: page
title: NET DEC 2015 (C)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2015 (C):**  -->
Which of the following intervals contains an
integer satisfying the following three congruences:<br>
$x\equiv 2 \pmod 5$, $x \equiv 3 \pmod 7$ and $x \equiv 4 \pmod {11}$.

(a) $[401,600]$.<br>
(b) $[601,800]$.<br>
(c) $[801,1000]$.<br>
(d) $[1001,1200]$.<br>

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
$M_kx \equiv 1 \pmod{m_k}$.<br>

Here (by Chinese Remainder Theorem) $a_1=2$, $a_2=3$, $a_3=4$, $m_1=5$,
$m_2=7$, $m_3=11$ and $m_i$'s are are pairwise co-prime. Therefore
$M=m_1m_2m_3=385$ and so $M_1 = \frac{M}{m_1} = 77$, $M_2=55$, $M_3=35$.<br>

Now, $b_1$ is the solution of the congruence\
$M_1x \equiv 1 \pmod 5 \Rightarrow 77x \equiv 2 x \equiv 1 \pmod 5$.
Therefore $b_1=3$. Similarly, $b_2$ is solution of the congruence
$55x \equiv 6x \equiv 1 \pmod 7$. Hence, $b_2=6=-1$. Similarly, $b_3=6$.
Therefore the solution is

$$x \equiv  1137 \equiv -18 \pmod {385} \quad \text{ or } \quad x = 385k-18 = 385k +367,$$

where $k=0,1,2,\ldots$. Substituting values of $k$, we get that $x$ lies
in the interval $[601,800]$ and $[1001,1200]$.


