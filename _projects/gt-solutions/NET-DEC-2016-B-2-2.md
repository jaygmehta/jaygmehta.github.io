---
layout: page
title: NET-DEC-2016-B-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $S_n$ denote the permutation group on $n$ symbols and $A_n$ be the subgroup of even permutations. Which of the following is true?

(a) There exists a finite group which is not a subgroup of $S_n$ for any $n\ge 1$.<br>
(b) Every finite group is a subgroup of $A_n$ for some $n \ge 1$.<br>
(c) Every finite group is a quotient of $A_n$ for some $n \ge 1$.<br>
(d) No finite abelian group is a quotient of $S_n$ for some $n \ge 3$.<br>

**Solution**

(a) By Cayley's theorem, this is false.

(b) Every group is isomorphic to $S_n$ for some $n$. We show that $S_n$ is isomorphic to a subgroup of $A_{n+2}$. Then by transitivity $G \approx A_{n+2}$. Hence, this is true.\\
Define $f: S_n \to A_{n+2}$ by
$$f(\theta) = \left\{ \begin{array}{ll}
\theta, &\ \text{ if } \theta \text{ is  even}\\
\theta (n+1, n+2), &\ \text{ if } \theta \text{ is  odd}
\end{array}\right.$$
Then it is easy to check that $f$ is an isomorphism of $S_n$ \textbf{into} $A_{n+2}$ (need not be onto).

(c) $\mathbb Z_2$ cannot be quotient of $A_n$ because if $\mathbb Z_2 \approx A_n/H$ for some subgroup $H$ of $A_n$, then $i_{A_n}(H)=2$ and therefore $H$ is normal in $A_n$. We know that $A_n$ is simple for all $n \ge 3$ except for $n=4$. But $A_4$ also does not have a subgroup of order $6$.  Therefore this statement is false.

(d) We know that $A_n$ is a normal subgroup of $S_n$ being of index $2$. Therefore, $S_n/A_n \approx \mathbb Z_2$. Hence, $\mathbb Z_2$ is quotient of $S_n$ for all $n \ge 3$. Therefore this statement is false.