---
layout: page
title: NET-DEC-2015-C-3-3
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $a_n$ denote the number of those permutations $\sigma$ on $\{1,2,\ldots,n\}$ such that $\sigma$ is a product of exactly two disjoint cycles. Then:

(a) $a_5=50$<br>
(b) $a_4=14$<br>
(c) $a_5=40$<br>
(d) $a_4=11$<br>

**Solution**

Consider such $\sigma \in S_5$, then $\sigma$ can be of the form $4+1$ or $3+2$. \\
The number of permutations in $S_5$ of the form $4+1$ are $\boxed{30}$ because for $(i_1)(i_2,i_3,i_4,i_5)$, there are $5$ possibilities for $i_1$, $4$ for $i_2$, and so on. So total $5 \times 4 \times 3 \times 2 \times 1$ possibilities of such $4+1$ type permutations. But each four-cycle $(i_2,i_3,i_4,i_5)$ can be written in four different ways (starting from $i_2, i_3, i_4$ or $i_5$). Therefore total number such $4+1$ permutations are $\frac{5!}{4} = 30$.\\
Similarly, the number of permutations of the form $3+2$, i.e. $(i_1,i_2,i_3)(i_4,i_5)$ in $S_5$ are $\frac{5!}{3 \times 2} = 5\times 4 = 20$. Hence, total no. of such permutations $\sigma$ are $20+30 = 50$. Therefore, $a_5=50$. Hence, option (a) is \text{correct} and (c) is \textbf{incorrect}.\\
Similarly for $\sigma\in S_4$ the possibilities are $3+1$ and $2+2$. Therefore $a_4 = \frac{4!}{3} + \frac{4!}{2 \times 2 \times 2} = 8 + 3 = \boxed{11}$.
\\
Note that each permutation of the form $(i_1,i_2)(i_3,i_4)$ can be written in $8$ different ways, i.e. interchanging $i_1$ and $i_2$ or interchanging $i_3$ and $i_4$ or writing it as $(i_3,i_4)(i_1,i_2)$. This is the reason why we divided by $8$ in the second term above.