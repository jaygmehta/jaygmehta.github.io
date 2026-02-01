---
layout: page
title: NET-JUNE-2012-B-1-4
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

The no. of nontrivial ring homomorphisms from $\mathbb Z_{12}$ to $\mathbb Z_{28}$ is  

(a) $1$<br>
(b) $3$<br>
(c) $4$<br>
(d) $7$<br>

**Solution**

A ring homomorphism is also a group homomorphism. First we determine all the possible group homomorphisms from $\mathbb Z_{12}$ to $\mathbb Z_{28}$.\\
**Result.** If $\phi: G \to G'$ is a (group) homomorphism, then $o(\phi(g)) \mid o(g)$ for all $g \in G$.\\
Note that it is sufficient to determine $\phi(1)$ as $1$ generates the group $\mathbb Z_{12}$. By the above result, $o(\phi(1)) \mid o(1)=12$. Since $o(\phi(1)) \mid o(\mathbb Z_{28})=28$, we have
$$o(\phi(1)) \mid \gcd(12,28) = 4.$$
Hence, $o(\phi(1))=1$ or $2$ or $4$. Then $\phi(1)=0$ or $14$ or $7,21$.\\
Then the group homomorphism $\phi: \mathbb Z_{12} \to \mathbb Z_{28}$ is given by $\phi(x) = kx$ ($x \in \mathbb Z_{12})$, where $k$ is any of the above possible values.\\
Since $\phi$ is also a ring homomorphism, for every $x, y \in \mathbb Z_{12}$, we must have
\begin{align*}
\Rightarrow &\ \phi(xy) = \phi(x) \phi(y)\\
\Rightarrow &\ kxy = kx ky = k^2 xy.
\end{align*}
Thus $\phi(x) = k x$ can be ring homomorphism only for those values of $k$ for which $k^2 \equiv k \pmod {28}$. Hence, the possible values of $k$ are $0, 21$. Thus, there are total {two} ring homomorphisms from $\mathbb Z_{12}$ to $\mathbb Z_{28}$. Since here it is asked non-trivial homomorphism, there is unique ring homomorphism $\phi(x) = 21x$. So the answer is **one**.