---
layout: page
title: NET-SEPT-2022-C-1-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Which of the following are class equation of a finite group?

(a) $1+3+3+3+3+13+13 = 39$ <br>
(b) $1+1+2+2+2+2+2+2=14$ <br>
(c) $1+3+3+7+7=21$ <br>
(d) $1+1+1+2+5+5=21$ <br>

**Solution**

In second option (b), $o(Z) = 2$. Then $o(G/Z) = \frac{14}{2} = 7$. Thus, $G/Z$ is cyclic. Then we know that $G$ is abelian, but in that case class equation would consists of all the terms $1$. So this option is not true\\
In the last option (d), $2\nmid 15$, so it cannot be a class equation.\\
We know that if $o(G) = pq$, where $p$ and $q$ are primes such that $p< q$ and $p \nmid q-1$. Then $G$ is the unique non-abelian group of order $pq$. In this case $o(Z) = 1$ as it cannot be any prime (otherwise $G$ will be abelian). For any element $a \in G$, $a \neq e$, $N(a) \neq G$. Then $N(a)$ will contain only the powers of $a$. Thus, if $o(a) = p$, then $o(N(a))=p$, and if $o(a) = q$, then $o(N(a))=q$. Thus, for $o(a) = q$, $|C(a)| = \frac{o(G)}{o(N(a))} = \frac{pq}{q} = p$. Thus, each conjugate class of element of order $q$ contains $p$ elements. But there are $q-1$ elements of order $q$ (as $1$-Sylow subgroup is unique). Therefore, there are $\frac{q-1}{p}$-conjugacy classes of order $p$. On the other hand, each conjugate class of an element of order $p$ consists of $o(G)/o(N(a))= pq/p = q$ elements. But there are $pq-1 - (q-1) = pq-q$ elements of order $p$. Hence, there are $\frac{(pq-q)}{q} = p-1$-conjugacy classes of order $q$. So the class equation would be\\
$o(G) = \sum |C(a)| = 1 + \underbrace{q+q+\cdots +q}_{p-1 \text{ times }} +  \underbrace{p+p+\cdots +p}_{\frac{q-1}{p} \text{ times }}.$\\
This shows that option (a) and (c) are correct.
