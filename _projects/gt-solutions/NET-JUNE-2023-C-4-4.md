---
layout: page
title: NET-JUNE-2023-C-4-4
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $n \ge 1$ be a positive integer and $S_n$ the symmetric group on $n$ symbols.
Let $\Delta = \{(g,g) : g \in S_n\}$.
Which of the following statements are necessarily true?

(a) The map $f : S_n \times S_n \to S_n$ given by $f(a,b) = ab$ is a group homomorphism.<br>
(b) $\Delta$ is a subgroup of $S_n \times S_n$.<br>
(c) $\Delta$ is a normal subgroup of $S_n \times S_n$.<br>
(d) $\Delta$ is a normal subgroup of $S_n \times S_n$ if $n$ is a prime number.<br>

**Solution**

The map $f(a,b)=ab$ is a homomorphism if and only if
$
f((a_1,b_1)(a_2,b_2)) = f(a_1,b_1)f(a_2,b_2).
$
Now,
$
f((a_1a_2,b_1b_2)) = a_1a_2b_1b_2,
$
while
$
f(a_1,b_1)f(a_2,b_2) = a_1b_1a_2b_2.
$
These are equal for all $a_i,b_i$ if and only if $b_1a_2=a_2b_1$, which is false in $S_n$ for $n\ge 3$. As a particular example, one can take $(\varphi, \psi), (\psi,\psi^2) \in S_3$, where $\varphi = (1,2)$ and $\psi = (1,2,3)$. So option (a) is false.\\
$\Delta$ is nonempty since $(e,e)\in\Delta$.
If $(g,g),(h,h)\in\Delta$, then
$
(g,g)(h,h)=(gh,gh)\in\Delta,
$
and
$
(g,g)^{-1}=(g^{-1},g^{-1})\in\Delta.
$
Thus $\Delta$ is a subgroup of $S_n\times S_n$ and so option (b) is true.\\
Consider $\Delta = \{(e,e), (\varphi,\varphi), (\psi,\psi), (\psi^2,\psi^2), (\varphi\psi,\varphi\psi), (\psi\varphi,\psi\varphi)\} < S_3 \times S_3$. Then for $(\varphi, \psi) \in S_3\times S_3$, we have
$$(\varphi,\psi) (\varphi,\varphi)(\varphi,\psi)^{-1}  = (\varphi\varphi\varphi, \psi \varphi \psi^2)= (\varphi, \varphi \psi) \not\in S_3 \times S_3.$$
So $\Delta$ is not normal and so option (c) is not true. Since $n=3$ is a prime number, option (d) is also not true for the same reason.