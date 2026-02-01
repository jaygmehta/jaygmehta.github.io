---
layout: page
title: NET-JUNE-2023-C-2-4
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a group of order $2023$. Which of the following statements are true?

(a) $G$ is an Abelian group.<br>
(b) $G$ is a cyclic group.<br>
(c) $G$ is a simple group.<br>
(d) $G$ is not a simple group.<br>

**Solution**

$2023 = 7 \times 17^2$. It is easy to see that $n_7 = 1$ and $n_{17} =1$. Thus, both the $7$-Sylow subgroup and the $17$-Sylow subgroup are normal, say $H$ and $K$. Then $G = HK$. Since both $H$ and $K$ are abelian, $G$ is abelian. Also, being unique Sylow subgroup, $H$ and $K$ are normal and hence $G$ cannot be simple. Thus, options (a) and (d) are correct. Note that $G$ need not be cyclic. For example, $\mathbb Z_7 \times \mathbb Z_{17} \times \mathbb Z_{17}$ is a group of order $2023$ which is not cyclic. So option (b) is not true.