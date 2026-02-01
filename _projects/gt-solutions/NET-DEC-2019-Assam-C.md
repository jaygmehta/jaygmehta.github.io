---
layout: page
title: NET-DEC-2019-Assam-C
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $\mathbb R^*$ be the multiplicative group of non-zero real numbers. Which of the following statements are true?

(a) If $H \subseteq \mathbb R^*$ is a subgroup such that $x^2 \in H$ for all $x \in \mathbb R^*$, then $H = \mathbb R^*$<br>
(b) If $H \subseteq \mathbb R^*$ is a subgroup such that $x^3 \in H$ for all $x \in \mathbb R^*$, then $H = \mathbb R^*$<br>
(c) There is no subgroup of $\mathbb R^*$ of index $2$<br>
(d) There is no subgroup of $\mathbb R^*$ of index $3$<br>

**Solution**

Since $x \mapsto x^3$ is a one-one correspondence on $\mathbb R^*$, if $x^3 \in H$ for all $x\in \mathbb R^*$, then $H = \mathbb R^*$.\\
Note that $H = \{x^2 \mid x \in \mathbb R^*\} = (0,\infty)$ is a \textbf{proper} subgroup of $\mathbb R^*$ of index $2$.\\
Suppose $H$ is a subgroup of $\mathbb R^*$ of index $3$, then for any $x\in \mathbb R^*$, $xH \in \mathbb R^*/H$ has order $3$. That is, $(xH)^3 = eH = H$ or $x^3 \in H$. If for all $x\in \mathbb R^*$, $x^3 \in H$, then $H = \mathbb R^*$, which is a contradiction to our assumption that index of $H$ is $3$.