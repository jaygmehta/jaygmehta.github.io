---
layout: page
title: NET-MARCH-2025-C-1-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a finite group. For any prime number $p$, let $E(p) = \{g \in G \mid g^p =1\}$. Which of the following statements are true?

(a) If $p$ divides $|G|$, then $E(p)$ is a subgroup of $G$.<br>
(b) For all $p$, $E(p)$ is a subgroup of $G$.<br>
(c) If $E(p)$ is a subgroup of $G$, then $p$ divides $|G|$.<br>
(d) If $G$ is abelian, then $E(p)$ is a subgroup of $G$.<br>

**Solution**

Consider $G = S_3$ and $p = 2$. Then $E(p) = E(2) = \{g \in S_3 \mid g^2 = e\}$. Thus, $E(2) = \{e, \varphi, \varphi \psi, \psi\varepsilon\}$, where $\varphi = (1,2)$ and $\psi = (1,2,3)$. Since $o(E(2))=4 \nmid 6 = o(S_3)$, $E(2)$ is not a subgroup of $G$. This shows that options (a) and (b) are false.\\
Again, for $p = 5$, $E(5) = \{g \in S_3 \mid g^5 = e\} = \{e\}$ is a subgroup of $G$ but $5 \nmid 6 = o(S_3)$. So option (c) is false.\\
If $G$ is abelian, then in fact, for any $s \in \mathbb Z$, the $G(s) = E(s) = \{g \in G \mid g^s = e\}$ is a subgroup of $G$ (refer $G(s)$ in our syllabus or Herstein). So option (d) is correct.


