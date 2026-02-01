---
layout: page
title: NET-FEB-2025-B-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

We say that a group $G$ has property (A) if every non-trivial homomorphism from $G$ to any group is injective. Which of the following groups has property (A)?

(a) The cyclic group of order $6$.<br>
(b) The symmetric group $S_5$.<br>
(c) The alternating group $A_5$.<br>
(d) The dihedral group with $10$ elements.<br>

**Solution**

We know that if $N$ is a non-trivial (proper) normal subgroup of $G$, then $G \to G/N$ is a non-trivial homomorphism with kernel $N$. Now, if a homomorphism is injective, then its kernel is trivial. Thus, we can get a non-injective homomorphism from $G$ to $G/N$ if there exists a proper normal subgroup $N$ of $G$, i.e., if $G$ is not simple.\\
Since $G = \mathbb Z_6$, $S_5$, and $D_5$ or $D_{10}$ are not simple, there will be a non-injective homomorphism from $G$ to $G/N$, where $N$ is one of its proper normal subgroups. Since $A_5$ is simple, it has no proper subgroup. Thus, if $f: A_5\to G'$ is a homomorphism, then $\ker f$ is a normal subgroup of $A_5$, which is $\{e\}$ or $A_5$, being a simple group. Thus, only option (c) is correct.


