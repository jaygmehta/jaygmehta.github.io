---
layout: page
title: NET-JUNE-2012-B-2-4
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Consider the group $\mathbb Q/\mathbb Z$, where $\mathbb Q$ and $\mathbb Z$ are the groups of rationals and integers respectively. Let $n$ be a positive integer. Then there is a cyclic subgroup of order $n$? 

(a) not necessarily.<br>
(b) yes, a unique one.<br>
(c) yes, but not necessarily a unique one.<br>
(d) never<br>

**Solution**

For $n \in \mathbb N$, $n \ge 2$, let 
$$H = \left\langle \frac{1}{n} + \mathbb Z \right\rangle = \left\{\mathbb Z,\frac{1}{n} + \mathbb Z, \frac{2}{n}+ \mathbb Z, \ldots, \frac{n-1}{n} + \mathbb Z \right\}.$$
Then $H$ is a cyclic subgroup of $\mathbb Q/\mathbb Z$ and $o(H)= n$. Now, we show that $H$ is unique.\\
Suppose $K = \left\langle \frac{a}{b} + \mathbb Z\right\rangle$ is a cyclic subgroup of $\mathbb Q/\mathbb Z$ of order $n$. We may assume that $\gcd(a,b) = 1$.\\
Since $o(K) = n$, $\frac{na}{b} \in \mathbb Z$. Therefore, $na = kb$ for some $k \in \mathbb Z$ or we can say that
$$\frac{a}{b} = \frac{k}{n}, \quad \text{ where } \gcd(k,n) = 1.$$
Therefore, $K = \left\langle \frac{k}{n} + \mathbb Z\right\rangle$. Now, we show that $H = K$.\\
Clearly, $\frac{k}{n} + \mathbb Z = \underbrace{\left(\frac{1}{n} + \mathbb Z\right) + \cdots + \left(\frac{1}{n}+\mathbb Z\right)}_{k \text{ times}}$. Hence, $\frac{k}{n} + \mathbb Z \in H$. Thus, $K \subset H$.\\
On the other hand, since $\gcd(k,n)=1$, there exists integers $x$ and $y$ such that $kx+ny=1$. Therefore,
\begin{align*}
\frac{1}{n}+ \mathbb Z = \frac{kx+ny}{n} + \mathbb Z = \frac{kx}{n} + y + \mathbb Z = \frac{kx}{n} + \mathbb Z \in \left\langle \frac{k}{n} + \mathbb Z\right\rangle,
\end{align*}
i.e. $H \subset K$. Hence, $H=K$ and so there is a unique cyclic subgroup of $\mathbb Q/\mathbb Z$ of order $n$.