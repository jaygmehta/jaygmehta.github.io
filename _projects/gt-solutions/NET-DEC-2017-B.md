---
layout: page
title: NET-DEC-2017-B
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

The group $S_3$ of permutations of $\{1,2,3\}$ acts on the three dimensional vectors space over the finite field $\mathbb F_3$ of three elements, by permuting vectors in basis $\{e_1,e_2,e_3\}$ by $\sigma(e_i) = e_{\sigma(i)}$, for all $\sigma \in S_3$. The cardinality of the vectors fixed under the above action is

(a) $0$<br>
(b) $3$<br>
(c) $9$<br>
(d) $27$<br>

**Solution**

Here $V = \mathbb F_3 \times \mathbb F_3 \times \mathbb F_3$. Cardinality of $V$ is $27$. Every $v \in V$ can be written as
$$v = a e_1 + be_2 + c e_3 = (a,b,c).$$
We have to determine the cardinality of the set $W=\{v=(a,b,c) \in \mathbb F_3^3 \mid \sigma(v)=v,\ \forall\ \sigma \in S_3\}$. \\
We know that $S_3=\{e,\phi,\psi,\psi^2,\psi\phi,\phi\psi\}$. Then we have  the following:

-- $e(v) = v \Rightarrow (a,b,c)=(a,b,c)$ and hence it does not give anything.

-- $\phi(v) = v \Rightarrow \phi(a e_1 + b e_2 + c_3) = a e_2 + be_1 + ce_3 = (b,a,c) = (a,b,c)$. Therefore, we have $a=b$.

-- $\phi\psi(v) = v \Rightarrow \phi(a e_1 + b e_2 + c_3) = a e_3 + be_2 + ce_1 = (c,b,a) = (a,b,c)$. Therefore, we have $a=c$.

-- Checking all the possibilities this way, we get $a=b=c$.

Hence, we have $a=b=c$ and so $v = (a,a,a) \in W$, where $a \in \mathbb F_3$. Thus, there are only $3$ such vectors $(0,0,0)$, $(1,1,1)$, and $(2,2,2)$. Therefore $|W| = 3$.