---
layout: page
title: NET-JUNE-2011-C-1-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $H=\{e, (1,2)(3,4)\}$ and \\
$K=\{e, (1,2)(3,4), (1,3)(2,4), (1,4)(2,3)\}$ be subgroups of $S_4$, where $e$ denotes the identity element of $S_4$. Then 

(a) $H$ and $K$ are normal subgroups of $S_4$<br>
(b) $H$ is normal in $K$ and $K$ is normal in $A_4$%<br>
(c) $H$ is normal in $A_4$ but not normal in $S_4$<br>
(d) $K$ is normal in $S_4$, but $H$ is not<br>

**Solution**

(a) Let $(1,2,3) \in A_4 \subset S_4$ and $(1,2)(3,4) \in H$. Then
$$(1,2,3) (1,2)(3,4) (1,2,3)^{-1} = (1,2,3) (1,2)(3,4) (3,2,1) = (1,3)(2,4) \not\in H.$$
This shows that $H$ is not normal in $A_4$ and also $S_4$. This discards option (c) too.<br>
(b) Since $K$ is abelian, every subgroup of $K$ is normal in $K$. Hence, $H$ is normal in $K$.\\
Let $\sigma \in A_4$ (or even in $S_4$) and $\theta \in K$. Then $\sigma^{-1} \theta \sigma$ is a conjugate of $\theta$ and it has same cycle decomposition as that of $\theta$, i.e. $2+2$. Hence, $\sigma^{-1} \theta \sigma \in K$ and therefore $K$ is normal in $A_4$. \\
Another argument, $K$ is the unique $2$-Sylow subgroup of $A_4$ and hence normal in $A_4$.<br>
(c) By option (a), $H$ is not normal in $A_4$.<br>
(d) Clearly, as seen above $H$ is not normal in $S_4$. $K$ is normal in $S_4$ by the same argument in option (b).