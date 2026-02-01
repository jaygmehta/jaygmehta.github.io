---
layout: page
title: NET-DEC-2023-C-1-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Which of the following statements are true?

(a) Let $G_1$ and $G_2$ be finite groups such that their orders $|G_1|$ and $|G_2|$ are coprime. Then any homomorphism from $G_1$ to $G_2$ is trivial.<br>
(b) Let $G$ be a finite group. Let $f : G \to G$ be a group homomorphism such that $f$ fixes more than half of the elements of $G$. Then $f(x)=x$ for all $x\in G$.<br>
(c) Let $G$ be a finite group having exactly $3$ subgroups. Then $G$ is of order $p^2$ for some prime $p$.<br>
(d) Any finite abelian group $G$ has at least $d(|G|)$ subgroups in $G$, where $d(m)$ denotes the number of positive divisors of $m$.<br>

**Solution**

We know that if $\phi: G_1 \to G_2$ is a homomorphism, then $o(\phi(g)) \mid o(g)$ for all $g \in G_1$. But by Lagrange's theorem (corollary), $o(g) \mid o(G_1)$ and $o(\phi(g)) \mid o(G_2)$. Thus, $o(\phi(g)) \mid \gcd(o(G_1),o(G_2))=1$. Therefore, $\phi(g) = e_2$, identity, for all $g \in G_1$ and hence $\phi$ is a trivial homomorphism and so option (a) is true.\\
Note that $H=\{x \in G : f(x)=x\}$ is a subgroup of $G$. By Lagrange's theorem, $o(H)\mid o(G)$. Thus, if $o(H) \frac{p(G)}{2}$, then $o(H) = o(G)$ and so option (b) is also true.\\
Consider $a \in G, a \neq e$. If $\langle a \rangle = G$, then $G$ is cyclic. Then by the converse of Langrange's theorem, $o(G)$ must have exactly three divisors and hence $o(G) = p^2$. If $\langle a \rangle \neq G$, then $H = \langle a \rangle$ is a unique proper subgroup of $G$, which by uniqueness, has order $p$. Then $o(G) =pm$ for some integer $m$. Now, let $b \in G$, $b \neq e$, $b \not\in H = \langle a\rangle$. Then $\langle b \rangle = G$. Thus, $G$ is cyclic with $o(G)$ having exactly $3$ divisors and again by the converse of Lagrange's theorem, $o(G) = p^2$. So option (c) is true.\\
By Fundamental Theorem of Finite Abelian Groups, there exists a subgroup of order $m$ for every positive divisor $m$ of $|G|$. Therefore, $G$ has at least $d(|G|)$ subgroups, i.e., at least the number of divisors of $|G|$ and so statement (d) is true.  
