---
layout: page
title: NET-JUNE-2018-C-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G=S_3$ be the permutation group of $3$ symbols. Then

(a) $G$ is isomorphic to a subgroup of a cyclic group.<br>
(b) there exists a cyclic group $H$ such that $G$ maps homomorphically onto $H$.<br>
(c) $G$ is a product of cyclic groups.<br>
(d) there exists a non-trivial homomorphism from $G$ to the additive group $(\mathbb Q,+)$ of rational numbers.<br>

**Solution**

(a) $S_3$ is not cyclic. So this can never happen.

(b) Let $H=\{\pm 1\}$. Define $\phi: S_n \to H$ by 
$$\phi(\theta) = \left\{ \begin{array}{ll}
1 &\ \text{ if $\theta$ is even}\\
-1 &\ \text{ if $\theta$ is odd}
\end{array}\right.$$
Then $\phi$ is a non-trivial homomorphism.

(c) Direct product of cyclic groups is abelian. So this can never happen.

(d) If $f : S_3 \to \mathbb Q$ is a non-trivial homomorphism. Then $\ker f$ is a normal subgroup of $S_3$ and $S_3/\ker f$ is isomorphic to a subgroup of $\mathbb Q$. Now, $\ker f =\{e\}$ or $H=\{e,\psi,\psi^2\}$. In both these cases we get $S_3/\{e\}$, or a group of order $2$, i.e. $S_3/H$. Since $S_3$ is not abelian and $\mathbb Q$ does not have a subgroup of order $2$, none of these can happen.