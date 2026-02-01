---
layout: page
title: NET-DEC-2016-C-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Consider the following subsets of the group of $2 \times 2$ non-singular matrices over $\mathbb R$:
$$G = \left\{\begin{pmatrix}
a & b \\ 0 & d
\end{pmatrix}: a, b, d \in \mathbb R,\ ad=1\right\}$$
$$H=\left\{\begin{pmatrix}
1 & b\\ 0 & 1
\end{pmatrix}: b \in \mathbb R\right\}.$$
Which of the following statements are correct?

(a) $G$ forms a group under matrix multiplication.<br>
(b) $H$ is a normal subgroup of $G$.<br>
(c) The quotient group $G/H$ is well-defined and is abelian.<br>
(d) The quotient group $G/H$ is well defined and is isomorphic to the group of diagonal matrices (over $\mathbb R$) with determinant $1$.<br>

**Solution**

(a) It can be easily checked that $G$ is a group under multiplication.

(b) It can be easily checked that $H$ is a normal subgroup of $G$.

(c) Let $G'$ be the group of diagonal matrices (over $\mathbb R$) of the form $\begin{pmatrix}
a & 0 \\ 0 & d
\end{pmatrix}$ with  $ad=1$. Define $f: G \to G'$ by $f\left(\begin{pmatrix}
a & b \\ 0 & d
\end{pmatrix}\right) = \begin{pmatrix}
a & 0 \\ 0 & d
\end{pmatrix}$. Then $f$ is an onto homomorphism with $\ker f = H$. Hence, $G/H \approx G'$. Since $G'$ is abelian, this statement is true.

(d) From above it follows that this statement is true.