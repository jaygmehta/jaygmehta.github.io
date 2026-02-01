---
layout: page
title: NET-JUNE-2023-C-1-4
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Which of the following statements are correct?

(a) If $G$ is a group of order $244$, then $G$ contains a unique subgroup of order $27$<br>
(b) If $G$ is a group of order $1694$, then $G$ contains a unique subgroup of order $121$<br>
(c) There exists a group of order $154$ which contains a unique subgroup of order $7$<br>
(d) There exists a group of order $121$ which contains two subgroups of order $11$<br>

**Solution**

$244 = 2^2 \times 61$. Since $27 \nmid 244$, by Lagrange's theorem, $G$ cannot have a subgroup of order $27$. So the option (a) is not correct.\\
$1694 = 11 \times 154 = 11^2 \times 7 \times 2$. By Sylow's third theorem, the number of $11$-Sylow subgroups, i.e., subgroups of order $11^2 = 121$ is $n_{11} = 1$. So, the option (b) is correct.\\
$154 = 11 \times 7 \times 2$. 
%By Sylow's third theorem, the number of $7$-Sylow subgroups, i.e., subgroups of order $7$ is $n_7 = 0$ or $1$. But in the equation it says, there exists. So, the option (c) is correct.\\
The cyclic group $\mathbb Z_{154}$ has a unique subgroup of order $7$ which is $\langle 22 \rangle$. So, the option (c) is correct.\\
We know that every group of order $p^2$ is abelian. Thus, every group of order $121 = 11^2$ is abelian. There are only two groups of order $121$, which are $\mathbb Z_{121}$ and $\mathbb Z_{11} \times \mathbb Z_{11}$. Note that $\mathbb Z_{11}\times \mathbb Z_{11}$ has $120$ elements of order $11$ (all elements other than $(0,0)$). Thus, the number of subgroups of order $11$ are $\frac{120}{\phi(11)} = 12$. Here it is asked two subgroups (i.e., at least two not exactly two). So, the option (d) is correct.