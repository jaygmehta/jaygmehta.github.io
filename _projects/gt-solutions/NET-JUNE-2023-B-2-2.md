---
layout: page
title: NET-JUNE-2023-B-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $p$ be a prime number. Let $G$ be a group such that for each $g \in G$ there exists an $n \in \mathbb N$ such that $g^{p^n} = 1$. Which of the following statements is FALSE?

(a) If $|G| =p^6$, then $G$ has a subgroup of index $p^2$.<br>
(b) If $|G| =p^6$, then $G$ has at least five normal subgroups.<br>
(c) Center of $G$ can be infinite.<br>
(d) There exists $G$ with $|G| = p^6$ such that $G$ has exactly six normal subgroups.<br>

**Solution**

By first Sylow theorem, there is a subgroup of $G$ of order $p^n$ for each $n = 1,2,\ldots, 6$. The index of a subgroup of order $p^4$ is $p^2$ and so this option is true. We are looking for false option.\\
\textbf{Result (Theorem).} A group $G$ of order $p^n$, $p$ primes and $n \in \mathbb N$, always has a normal subgroup of order $p^m$, for all $m \le n$. The proof can be given by induction on $n$ using the fact that $Z \neq \{e\}$, and that there is a one-one correspondence between normal subgroups of $G/Z$ (in general $G/N$ or $\overline{G}$) to the normal subgroups of $G$ containing the kernel $K$ of the canonical homomorphism $G \to G/Z$. Thus, here, $G$ has normal subgroups of order $p^k$ for $k = 0,1,2,\ldots, 6$ and so the second option (b) is true. We are looking for false option.\\
For $G=\mathbb{Z}_p \times \mathbb Z_p \times \cdots$, the center is $G$ itself which is infinite and so the third option (c) is true. We are looking for false option.\\
From argument given in second option (b), it is clear that $G$ need not necessarily have exactly six normal subgroups and so this last option (d) is FALSE and hence it is the only correct option.
