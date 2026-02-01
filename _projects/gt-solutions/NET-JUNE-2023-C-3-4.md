---
layout: page
title: NET-JUNE-2023-C-3-4
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G_1$ and $G_2$ be two groups and $\varphi : G_1 \to G_2$ be a surjective group homomorphism. 
Which of the following statements are true?

(a) If $G_1$ is cyclic then $G_2$ is cyclic.<br>
(b) If $G_1$ is Abelian then $G_2$ is Abelian.<br>
(c) If $H$ is a subgroup of $G_1$ then $\varphi(H)$ is a subgroup of $G_2$.<br>
(d) If $N$ is a normal subgroup of $G_1$ then $\varphi(N)$ is a normal subgroup of $G_2$.<br>

**Solution**

If $G_1=\langle g\rangle$, then
$G_2=\varphi(G_1)=\langle \varphi(g)\rangle,$
hence $G_2$ is cyclic.\\
Let $x,y\in G_2$. Since $\varphi$ is surjective, $x=\varphi(a)$ and $y=\varphi(b)$ for some
$a,b\in G_1$. Then 
$xy=\varphi(ab)=\varphi(ba)=yx,$
so $G_2$ is Abelian.\\
Let $x=\varphi(h_1)$ and $y=\varphi(h_2)$ belong to $\varphi(H)$. Then
$xy^{-1}=\varphi(h_1h_2^{-1})\in\varphi(H),$
so $\varphi(H)$ is a subgroup of $G_2$.\\
Let $g_2\in G_2$. Since $\varphi$ is surjective, $g_2=\varphi(g_1)$ for some $g_1\in G_1$.
Then $g_2\varphi(N)g_2^{-1}=\varphi(g_1Ng_1^{-1})=\varphi(N),$
so $\varphi(N)\triangleleft G_2$.\\
Thus, all the four options are correct.
