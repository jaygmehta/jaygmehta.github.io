---
layout: page
title: NET-JUNE-2017-C-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

For an integer $n \ge 2$, let $S_n$ be the permutation group on $n$ letters and $A_n$ the alternating group. Let $\mathbb C^*$ be the group of nonzero complex numbers under multiplication. Which of the following are correct statements?

(a) For every integer $n \ge 2$, there is a non trivial homomorphism $\chi : S_n \to \mathbb C^*$.<br>
(b) For every integer $n \ge 2$, there is a unique non trivial homomorphism $\chi : S_n \to \mathbb C^*$.<br>
(c) For every integer $n \ge 3$, there is a non trivial homomorphism $\chi : A_n \to \mathbb C^*$.<br>
(d) For every integer $n \ge 5$, there is no non trivial homomorphism $\chi : A_n \to \mathbb C^*$.<br>

**Solution**

Idea: If there is a homomorphism $f: S_n \to \mathbb C^*$, then by first isomorphism theorem, $S_n/\ker f$ is isomorphic to a subgroup of $\mathbb C^*$ (which is always abelian).

(a) Define $\chi: S_n \to \mathbb C^*$ by 
$$\chi(\theta) = \left\{ \begin{array}{ll}
1 &\ \text{ if $\theta$ is even}\\
-1 &\ \text{ if $\theta$ is odd}
\end{array}\right.$$
Then $\chi$ is a non-trivial homomorphism with $\ker \chi = A_n$.

(b) It suffices to determine the value homomorphism from $S_n$ on its transposition $\tau$. Since a transposition $\tau$ has order $2$, we have
$$(f(\tau))^2 = f(\tau^2) = f(e) = 1.$$
If $f(\tau)=1$, then $f(\theta) = 1$ for all $\theta \in S_n$ and we get trivial homomorphism. So $f(\tau)=-1$. Then $f(\theta)=1$ if $\theta$ is even otherwise it is $-1$, which is the same map as above.

(c) $A_n$ is simple for $n=3$ and $n \ge 5$ (except $n=4$). Kernel of homomorphism is normal subgroup of $A_n$ which does not exits. So there is no non-trivial homomorphism. Hence, this is false.

(d) Since above is false. This statement is true.