---
layout: page
title: NET-JULY-2025-C-1-3
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a group, $H$ a subgroup of $G$, and
$
T = \{ gH \mid g \in G \},
$
the set of all left cosets of $H$ in $G$. Let $S_T$ be the set of all permutations of $T$ and let
$
\pi : G \to S_T
$
be the map defined by
$
\pi(g)(g_1H) = gg_1H.
$

For a prime number $p$, let $\mathbb{F}_p$ denote the field with $p$ elements. In which of the following cases is $\ker \pi$ trivial?

(a) $G = \mathrm{GL}_2(\mathbb{F}_p)$ and $H$ is a subgroup of order $p$.<br>
(b) $G = \mathrm{SL}_2(\mathbb{F}_p)$ and $H$ is a subgroup of order $p$.<br>
(c) $p \equiv 3 \pmod{4}$, $G = \mathrm{GL}_2(\mathbb{F}_p)/\mathrm{SL}_2(\mathbb{F}_p)$ and $H$ is a subgroup of order $2$.<br>
(d) $p \equiv 1 \pmod{4}$, $G = \mathrm{GL}_2(\mathbb{F}_p)/\mathrm{SL}_2(\mathbb{F}_p)$ and $H$ is a subgroup of order $2$.<br>

**Solution**

$$
\ker \pi = \{ g \in G \mid gxH = xH \text{ for all } x \in G \}.
$$
This is equivalent to
$$
gxH = xH \iff x^{-1}gx \in H \text{ for all } x \in G.
$$
Hence
$$
\ker \pi = \bigcap_{x \in G} xHx^{-1},
$$
the largest normal subgroup of $G$ contained in $H$ (Refer our notes or Herstein, the lemma after Cayley's theorem).\\
Thus, if $H$ is normal, then $xHx^{-1} = H$ for all $x \in G$ and so $\ker \pi = H$; otherwise, $\ker \pi$ is proper normal subgroup of $G$ contained in $H$. Thus, if $o(H)$ is a prime, then $\ker \pi = \{e\}$ (when $H$ is not normal) or $\ker \pi = H$ (when $H$ is normal).\\
Now, $|GL_2(\mathbb F_2)| = o(G) = (p^2-1)(p^2-p) = p(p-1)^2(p+1)$. Since $p \mid o(G)$ but $p^2 \nmid o(G)$, the subgroup $H$ of $G = GL_2(\mathbb F_2)$ with $o(H) = p$ is the $p$-Sylow subgroup of $G$. To determine whether $H$ is normal or not, by Second Sylow theorem, we check whether it is unique $p$-Sylow subgroup. Note that
$$\begin{pmatrix}
1 & 1 \\ 0 & 1 
\end{pmatrix}\begin{pmatrix}
1 & 1 \\ 0 & 1 
\end{pmatrix} = \begin{pmatrix}
1 & 2 \\ 0 & 1 
\end{pmatrix}.$$
Thus, the matrix $\begin{pmatrix}
1 & 1 \\ 0 & 1 
\end{pmatrix}$ has order $p$ and it generates a subgroup of order $p$ (of upper triangular matrices). Similarly, 
$$\begin{pmatrix}
1 & 0 \\ 1 & 1 
\end{pmatrix}\begin{pmatrix}
1 & 0 \\ 1 & 1 
\end{pmatrix} = \begin{pmatrix}
1 & 0 \\ 2 & 1 
\end{pmatrix}.$$
Thus, the matrix $\begin{pmatrix}
1 & 0 \\ 1 & 1 
\end{pmatrix}$ also has order $p$ which generates another $p$-Sylow subgroup (of lower triangular matrices). Obviously there are more than one $p$-Sylow-subgroups $H$ of $G$ which will hence not be normal and so $\ker \pi \neq H$, i.e., $\ker \pi$ is proper normal subgroup of $G$ contained in $H$. Since, $o(\ker \pi) \mid o(H) = p$, and $\ker \pi \neq H$, we have $\ker \pi = \{I\}$, trivial, and so option (a) is correct.\\
Note that $|SL_2(\mathbb F_p)|= p(p^2-1)|$ (first row can be chosen anything except $(0,0)$ and in second row, only one entry we can chose in $p$ ways as the fourth entry will have to be such that $\det = 1$). The same argument as above applies here, and so option (b) is correct.\\
Now, $|G| = |GL_2(\mathbb F_p)/SL_2(\mathbb F_p)| = \frac{p(p-1)^2(p+1)}{p(p-1)(p+1)} = p-1$. Choosing $p = 3 \equiv 3 \pmod 4$, we get $|G| = 2 = |H|$. Thus, $H$ will be normal in $G$ and $\ker \pi=H \neq \{e\}$. Similarly, for $p = 5 \equiv 1 \pmod 4$, we have $|G| = 4$. Then $G \approx \mathbb Z_4$ or $G \approx K_4$. Then every subgroup $H$ of $G$ is normal and so $\ker \pi=H \neq \{e\}$. Hence, options (c) and (d) are incorrect.


