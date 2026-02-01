---
layout: page
title: NET-JUNE-2019-C-1-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $\mathbb Z[x]$ be the ring of polynomials over integers. Then the additive group $\mathbb Z[x]$ is

(a) isomorphic to the multiplicative group $\mathbb Q^+$ of positive rational numbers.<br>
(b) isomorphic to the group of rational numbers $\mathbb Q$ under addition.<br>
(c) countable<br>
(d) uncountable<br>

**Solution**

(a) Define $f: (\mathbb Z[x],+) \to (\mathbb Q^+,\cdot)$ by
$$f(\sum_{k=0}^n a_k x^k) = \prod_{k=0}^n p_k^{a_k},$$
where $p_0 =2$, $p_1=3$, $p_2=5$, $p_3 =7$, i.e. $p_n$ is the $n$-th prime. Then check that $f$ is an onto isomorphism. Hence, $(\mathbb Z[x],+) \approx (\mathbb Q^+,\cdot)$.<br>

(b) **Not True**. Show that $(\mathbb Q^+,\cdot)$ and $(\mathbb Q,+)$ are not isomorphic. This, along with above option will conclude that $(\mathbb Z[x],+)$ is not isomorphic to $(\mathbb Q,+)$.<br>

(c) $D_n = \{p(x) \in \mathbb Z[x] \mid \deg(p(x)) = n\}$ be the set of polynomials of degree $n$. Then $D_n$ is countable (as it is in one-one correspondence with $\underbrace{\mathbb Z \times \mathbb Z\times \cdots \times \mathbb Z}_{n \text{ times}}$. Now, $\mathbb Z[x] = \bigcup\limits_{n \ge 0} D_n$. Since countable union of countable sets is countable, $\mathbb Z[x]$ is countable.<br>

(d)) Since $\mathbb Z[x]$ is countable, this option is **incorrect**.
