---
layout: page
title: NET-DEC-2014-B-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

In the group of all invertible $4 \times 4$ matrices with entries in the field of $3$ elements, any $3$-Sylow subgroup has cardinality:

(a) $3$<br>
(b) $81$<br>
(c) $243$<br>
(d) $729$<br>

**Solution**

We know that the number of invertible $n\times n$ matrices with entries in $\mathbb F_q$ (i.e. order of $GL_n(\mathbb F_q)$) is $(q^n-1)(q^n-q)(q^n-q^2) \cdots (q^n-q^{n-1})$.\\
Here $o(GL_4(\mathbb F_3))= (3^4-1)(3^4-3)(3^4-3^2)(3^4-3^3) = 80\cdot 78 \cdot 72 \cdot 54$. Notice that $3^6\mid o(GL_4(\mathbb F_3))$ but $3^7 \nmid o(GL_4(\mathbb F_3))$. Thus, the order of $3$-Sylow subgroup is $3^6=729$.\\
Note that
\begin{align*}
o(GL_n(\mathbb F_q)) =&\ (q^n-1)(q^n-q)(q^n-q^2) \cdots (q^n-q^{n-1})\\
=&\ q\cdot q^2 \cdots q^{n-1} (q^n-1)(q^{n-1}-1)(q^{n-2}-1) \cdots (q-1).
\end{align*}
Therefore, the order of $q$-Sylow subgroup in $GL_n(\mathbb F_q)$ is $q \cdot q^2 \cdots q^{n-1} = q^{n(n-1)/2}.$