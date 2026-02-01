---
layout: page
title: NET-DEC-2011-B-1-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

The number of group homomorphisms from the symmetric group $S_3$ to $\mathbb Z/6 \mathbb Z$ is 

(a) $1$<br>
(b) $2$<br>
(c) $3$<br>
(d) $6$<br>

**Solution**

If $f: S_3 \to \mathbb Z_6$ is a group homomorphism, then $\ker f$ is a normal subgroup of $S_3$ and by first isomorphism theorem, $S_3/\ker f$ is isomorphic to a subgroup of $\mathbb Z_6$.\\
Normal subgroups of $S_3$ are $\{e\}$, $S_3$, and $H=\{e,\psi,\psi^2\}$.\\
If $\ker f=\{e\}$, then $S_3/\{e\}$ is non-abelian of order $6$ which is isomorphic to $\mathbb Z_6$. This is not possible.\\
If $\ker f= S_3$, then $f=0$ is a trivial homomorphism.\\
If $\ker f = H$, then $S_3/H$ is a group of order $2$ which is isomorphic to a unique subgroup $\{0,3\}$ of $\mathbb Z_6$. Hence, there is one such homomorphism $f$ in this case. Therefore, the total number of homomorphisms from $S_3$ to $\mathbb Z_6$ are $2$ (one trivial and one non-trivial).