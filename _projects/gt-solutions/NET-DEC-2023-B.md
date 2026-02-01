---
layout: page
title: NET-DEC-2023-B
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be any finite group. Which one of the following is necessarily true?

(a) $G$ is a union of proper subgroups.<br>
(b) $G$ is a union of proper subgroups if $|G|$ has at least two distinct prime divisors.<br>
(c) If $G$ is abelian, then $G$ is a union of proper subgroups.<br>
(d) $G$ is a union of proper subgroups if and only if $G$ is not cyclic.<br>

**Solution**

Consider $G = \mathbb Z_{10}$. Then the only proper subgroups are unique subgroups of order $2$ and $5$, which are $\langle 5 \rangle = \{0,5\}$ and $\langle 2 \rangle = \{0,2,4,6,8\}$. Clearly $3,7,9$ do not belong to any of these proper subgroups as they have order $10 = o(G)$. Thus, options (a), (b), (c) are false. Then the only option (d) is true.\\
Option (d) is also true for the following reason. If $G$ is cyclic, then any element $a \in G$ with $o(a) = o(G)$ will not appear in any proper subgroup of $G$. Conversely, if $a \in G$ does not appear in any proper subgroup of a finite group $G$, then $\langle a \rangle = G$ as it cannot be a proper subgroup. Thus, $G$ is cyclic.


