---
layout: page
title: NET-JULY-2025-C-2-3
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

For a group $G$, let $\mathrm{Aut}(G)$ denote the group (under composition)
of all bijective group homomorphisms from $G$ onto itself.
Which of the following statements are true?

(a) If $G_1, G_2$ are two groups such that $\mathrm{Aut}(G_1)$ is isomorphic
to $\mathrm{Aut}(G_2)$, then $G_1$ is isomorphic to $G_2$.<br>
(b) If $|G| = 2$, then $\mathrm{Aut}(G \times G)$ is abelian.<br>
(c) If $G$ is the group of complex numbers under addition, then
$\mathrm{Aut}(G)$ is abelian.<br>
(d) If $G$ is finite, then $\mathrm{Aut}(G)$ is finite.<br>

**Solution**

We know that $|{\rm Aut}(\mathbb Z_n)| = \phi(n)$. Thus, $|{\rm Aut}(\mathbb Z_4)| = = \phi(4) = 2 =\phi(6) = |{\rm Aut}(\mathbb Z_6)|$. Also $|{\rm Aut}(\mathbb Z_4)| =|{\rm Aut}(\mathbb K_4)|$ but the groups are not isomorphic, so the option (a) is false.\\
If $|G| = 2$, then $G \approx \mathbb Z_2$ and so ${\rm Aut}(G \times G) \approx {\rm Aut}(\mathbb Z_2 \times \mathbb Z_2) = {\rm Aut}(K_4)$. We know that ${\rm Aut}(K_4) \approx S_3$ (it can be seen easily, the six maps: (i) $I$, (ii) $a \mapsto b$ and $b\mapsto a$, but $c\mapsto c$, (iii), (iv) similar to (ii); (v) $a\mapsto b, b\mapsto c, c\mapsto a$ (which is $\psi \in S_3$, (vi) its square ($\psi^2 \ni S_3$). Thus, ${\rm Aut}(G \times G) \approx S_3$, which is non-abelian and so option (b) is false.\\
Clearly, $f(z) = \overline{z}$ and $g(z) = iz$ are automorphisms of $(\mathbb C,+)$. Now, $f(g(z)) = f(iz) = \overline{iz}=-i\overline{z}$, whereas $g(f(z))= g(\overline{z}) = i \overline{z}$. Thus, ${\rm Aut}(\mathbb C)$ is non-abelian and so option (c) is false.\\
Thus, only option (d) is true. Indeed, if $G$ is finite, then there are only finitely many bijections from $G$ to itself. Since $\mathrm{Aut}(G)$ is a subgroup of the symmetric group on $G$, it must be finite.


