---
layout: page
title: NET-MARCH-2025-C-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

An abelian group $G$ is said to have property (P) if for every $N$ of $G$, there exists a subgroup $H$ of $G$ such that $G = N + H$ and $N \cap H = \{0\}$. Which of the following statements are true?

(a) If an abelian group $G$ has property $(P)$, every subgroup of $G$ has property $(P)$.<br>
(b) If an abelian group $G$ has property $(P)$, then every element of $G$ has finite order.<br>
(c) The group $\mathbb{Z}$ has property $(P)$.<br>
(d) If an abelian group $G$ has property $(P)$, then no element has order $p^2$, where $p$ is a prime number.<br>

**Solution**

Let $K$ be a subgroup of $G$ and $N$ be a subgroup of $K$. Then $N$ is a subgroup of $G$. Since $G$ has property (P), there is a subgroup $H$ of $G$ such that $G = N + H$ and $N \cap H =\{0\}$. But then $K \cap H$ is a subgroup of $K$ such that 
$$K = K \cap G = K\cap (N+H) = N + (K \cap H)$$
and $N \cap (K \cap H) = \{0\}$. Thus, if $G$ has property (P), then every subgroup has property (P) and so option (a) is true.\\
$\mathbb Z$ does not have property (P) because every subgroup of $\mathbb Z$ is of the form $m \mathbb Z$, $m \in \mathbb N \cup \{0\}$ and $n\mathbb Z + m\mathbb Z = d \mathbb Z$, where $d = \gcd(m,n)$. Thus for $N = 2\mathbb Z$, there is no subgroup $H$ of $\mathbb Z$ such that $H + 2\mathbb Z = 0$ and $H \cap 2\mathbb Z = \{0\}$. So option (c) is false.\\
Suppose $x \in G$ has infinite order. Then $\langle x \rangle \approx \mathbb Z$, being an infinite cyclic group. But then for $N = \langle 2x \rangle \approx 2\mathbb Z$, there is no $H$ such that $N + H = \langle x \rangle$ and $N \cap H = \{0\}$ as argued for $\mathbb Z$. Hence, every element in $G$ must have a finite order and so option (b) is true.\\
If $a\in G$ has order $p^2$, then $a+a+\cdots+a (p {\rm times}) = ap$ has order $p$ and $N = \langle ap\rangle$.


