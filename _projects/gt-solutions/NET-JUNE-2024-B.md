---
layout: page
title: NET-JUNE-2024-B
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

The number of group homomorphisms from $\mathbb{Z}/150\mathbb{Z}$ to
$\mathbb{Z}/90\mathbb{Z}$ is

(a) $30$<br>
(b) $60$<br>
(c) $45$<br>
(d) $10$<br>

**Solution**

We know that if $\phi: \mathbb Z_m \to \mathbb Z_n$ is a homomorphism, then $o(\phi(g)) \mid o(g)$ for all $g \in \mathbb Z_m$. But by Lagrange's theorem (corollary), $o(g) \mid o(\mathbb Z_m)=m$ and $o(\phi(g)) \mid o(\mathbb Z_n) = n$. Thus, $o(\phi(g)) \mid \gcd(m,n)$. Also, a homomorphism is completely determined by value of $\phi(1)$ as the domain $\mathbb Z_m$ is cyclic. So, here $p(\phi(1)) \mid \gcd(150,90)= 30$. So $o(\phi(1)) = 1$ or $2$ or $3$ or $5$ or $6$ or $10$ or $15$ or $30$. If $o(\phi(1)) =1$, then $\phi(1) = 1$ and $\phi(x) = x$ for all $x$. If $o(\phi(1)) = 2$, then $\phi(1) = 45 \in\mathbb Z_{90}$ and $\phi(x) = 45x$. If $o(\phi(1)) = 3$, then $\phi(1) = 30$ or $60 \in\mathbb Z_{90}$ and $\phi(x) = 30x$, or $\phi(x) = 60x$. This way not only we can count but also determine each homomorphism. \\
In general, $|{\rm Hom}(\mathbb Z_m, \mathbb Z_n)| = \gcd(m,n)$ **(Prove this!)**. So, here there will be $\gcd(150,90) = 30$ such homomorphisms.
