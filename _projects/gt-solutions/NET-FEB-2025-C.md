---
layout: page
title: NET-FEB-2025-C
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

A group $G$ is said to be divisible if for every $y \in G$ and for every positive integer $n$, there exists $x \in G$ such that $x^n = y$. Which of the following groups are divisible?

(a) $\mathbb Q$ with ordinary addition<br>
(b) $\mathbb C \setminus \{0\}$ with ordinary multiplication<br>
(c) The cyclic group of order $5$<br>
(d) The symmetric group $S_5$<br>

**Solution**

For $(\mathbb Q,+)$, given any $y \in \mathbb Q$ and $n \in \mathbb N$, we want to find $x \in \mathbb Q$ such that $nx = y$. So, clearly $x =\frac{y}{n} \in \mathbb Q$. So option (a) is true.\\
For $(\mathbb C \setminus \{0\},\cdot)$, given any $y \in \mathbb C^*$ and $n \in \mathbb N$, we want to find $x \in \mathbb C^*$ such that $x^n = y$. So, clearly $x =\sqrt[n]{y} \in \mathbb C^*$. So option (b) is true.\\
For $(\mathbb Z_5,+_5)$, taking $y = 1$ (any number other than $0$), $n = 5$, we cannot find $x \in \mathbb Z_5$ such that $5x = x+x+x+x+x = 1$ in $\mathbb Z_5$. So option (c) is false.\\
Let $y = (1,2,3,4)$ (or any four cycle or any the odd permutation) in $S_5$ and $n = 2$. Then we cannot find $x \in S_5$ such that $x^2 = y$ because for any $x \in S_5$, $x^2$ will always be an even permutation, whereas $y$ is an odd permutation. So option (d) is false.