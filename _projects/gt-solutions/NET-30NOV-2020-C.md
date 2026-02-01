---
layout: page
title: NET-30NOV-2020-C
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a cyclic group of order $8$ and $H = S_5$ be the permutation group of $5$ elements. Which of the following statements are necessarily true?

(a) There is no nontrivial group homomorphism from $G$ to $H$<br>
(b) There is no injective group homomorphism from $G$ to $H$<br>
(c) There is no surjective group homomorphism from $G$ to $H$<br>
(d) There are more than $20$ different group homomorphisms from $G$ to $H$<br>

**Solution**

We may consider $G = \mathbb Z_8$. Then we have to determine homomorphisms $f: \mathbb Z_8 \to S_5$. Since $\mathbb Z_8$ is cyclic, it suffices to determine the image of $1$, i.e., $f(1)$. Since $f$ is a homomorphism, $o(f(1)) \mid o(1)=8$. Also $o(f(1)) \mid o(S_5) = 120$. Hence, $o(f(1)) \mid \gcd(8,120)=8$. Thus, $o(f(1))$ has possibilities $1$, $2$, $4$, $8$. Since we are looking for nontrivial homomorphism $f$ and there is no element of order $8$ in $S_5$, we have $o(f(1))$ is either $2$ or $4$. There are $10$ elements of order $2$ and $30$ elements of order $4$ in $S_5$. Hence, there are at $40$ different nontrivial group homomorphism from $G = \mathbb Z_8$ to $H = S_5$.\\
If $f$ is injective, then $\ker f = \{0\}$. By first isomorphism theorem, $G/\ker f$ is isomorphic to a subgroup of order $8$ of $S_5$. This is not possible. Hence, $f$ cannot be injective.\\
Also there cannot be a surjective function from a set of $8$ elements to a set of $120$ elements. Hence, $f$ cannot be surjective.
