---
layout: page
title: NET-DEC-2017-C
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G$ be a finite abelian group and $a, b \in G$ with order$(a)=m$, order$(b)=n$. Which of the following are necessarily true?

(a) order$(ab)=mn$<br>
(b) order$(ab)={\rm lcm}(m,n)$<br>
(c) there is an element of $G$ whose order is ${\rm lcm}(m,n)$<br>
(d) order$(ab)=\gcd(a,b)$<br>

**Solution**

We know that there is an element of order ${\rm lcm}(o(a),o(b))$. Hence, option (c) is true.\\
For other options, take $G = \mathbb Z_{12}$, $a = 2$, $b=4$. Then $o(a) = m=6$ and $o(b)=n=3$. But $o(a+b) = o(6) = 2$ which is neither of $mn = 18$, ${\rm lcm}(m,n)=6$, and $\gcd(m,n)=3$.