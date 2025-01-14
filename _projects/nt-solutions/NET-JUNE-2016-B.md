---
layout: page
title: NET JUNE 2016 (B)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET JUNE 2016 (B):**  -->

Which of the following statements is FALSE? There
exists an integer $x$ such that

(a) $x \equiv 23 \pmod {1000}$ and $x \equiv 45 \pmod {6789}$.<br>
(b) $x \equiv 23 \pmod {1000}$ and $x \equiv 54 \pmod {6789}$.<br>
(c) $x \equiv 32 \pmod {1000}$ and $x \equiv 54 \pmod {9876}$.<br>
(d) $x \equiv 32 \pmod {1000}$ and $x \equiv 44 \pmod {9876}$.<br>

**Solution**

We know that, a system of linear congruences has solutions if and only
if for every pair of congruences within the system 

$$\begin{align*}
x &\ \equiv a_i \pmod{m_i}\\
x &\ \equiv a_j \pmod{m_j}\\
a_i &\ \equiv a_j \pmod{\text{gcd}(m_i,m_j)},
\end{align*}$$

i.e. if and only if gcd$(m_i,m_j) \mid (a_i-a_j)$.<br>

Here, for the pair of congruence $x \equiv 32 \pmod {1000}$ and
$x \equiv 54 \pmod {9876}$, GCD$(1000,9876)=4$ and $54-23=31$. Thus,
$4 \nmid 31$ and hence the pair of congruence does not have a solution.<br>

Also notices that $x \equiv 32 \pmod {1000}$ and
$x \equiv 54 \pmod {9876}$ implies,

$$x = 1000 k + 32 \quad \text{ and } \quad x = 9876k + 54.$$ 

In the first congruence $4\mid 1000$ and $4\mid 32$ and therefore $4\mid x$.
But in the second congruence $4\mid 9876$ but $4 \nmid 54$ and thus
$4\nmid$ which is a contradiction. So the pair of congruences does not
have a solution.


