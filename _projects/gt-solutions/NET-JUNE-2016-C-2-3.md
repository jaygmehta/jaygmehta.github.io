---
layout: page
title: NET-JUNE-2016-C-2-3
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Consider the symmetric group $S_{20}$ and its subgroup $A_{20}$ consisting of all even permutations. Let $H$ be a $7$-Sylow of $A_{20}$. Pick each correct statement from below:

(a) $|H|=49$.<br>
(b) $H$ must be cyclic.<br>
(c) $H$ is a normal subgroup of $A_{20}$.<br>
(d) Any $7$-Sylow subgroup of $S_{20}$ is a subset of $A_{20}$.<br>

**Solution**

(a) $o(A_{20})=\frac{20!}{2}=3\cdot 4 \cdots 19 \cdot 20$. Thus, $7^2\mid o(A_{20})$ but $7^3 \nmid o(A_{20})$, i.e. order of $7$-Sylow subgroup $H$ is $49$.<br>

(b) If $H$ is cyclic, then $H$ must have an element of order $49$. In $S_{20}$ the longest cycle can be or length $20$ which has order $20$. Also, we know that every permutation can be written as product or disjoint cycles and order or permutation is the LCM of the order (length) of this disjoint cycles. In no case, $49$ can be LCM of cycles of length $\le 20$.<br>

(c) Suppose $H$ is normal and $K$ be another $7$-Sylow subgroup. Since (by second part of Sylow's thoerem) two $p$-Sylow subgroups are conjugate, for some $x \in S_{20}$, $K=xHx^{-1}=H$. Thus, $H$ becomes unique $7$-Sylow subgroup and by above it is not cyclic. Thus, number of elements or order $7$ in $H$ and hence in $S_{20}$ or $A_{20}$ is $48$. But number of elements in $S_{20}$ or order $7$ (i.e. $7$ cycles) is $\displaystyle \frac{{\mbox{ }}^{20}P_{7}}{7}=\frac{1}{7}\cdot \frac{20!}{(20-7)!}=2\cdot 14 \cdot 15 \cdots 20$ which more than $48$ and hence $H$ cannot be unique $7$-Sylow subgroup. Therefore it must not be normal.<br>

(d) This is true because the order of $7$-Sylow subgroup in $A_{20}$ and $S_{20}$ is $49$. Hence it is the same $7$-Sylow subgroup.