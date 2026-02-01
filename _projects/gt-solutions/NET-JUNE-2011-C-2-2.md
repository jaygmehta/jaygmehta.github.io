---
layout: page
title: NET-JUNE-2011-C-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

Let $G=\mathbb Z_{10} \times \mathbb Z_{15}$. Then  

(a) $G$ contains exactly one element of order $2$<br>
(b) $G$ contains exactly $5$ elements of order $3$<br>
(c) $G$ contains exactly $24$ element of order $5$<br>
(d) $G$ contains exactly $24$ elements of order $10$<br>

**Solution**

(a) Let $(a,b) \in G=\mathbb Z_{10} \times \mathbb Z_{15}$ be an element of order $2$. Then $(2a,2b)=(0,0)$ and so $2a=0 \pmod{10}$ and $2b=0\pmod{15}$. This implies $a=0,5$ and $b=0$. So $(a,b) = (0,0)$ or $(5,0)$. But $(0,0)$ is identity of $G$ of order $1$. So $G$ has a unique element $(5,0)$ of order $2$.<br>
(b) Let $(a,b) \in G$ be an element of order $3$. Then $(3a,3b)=(0,0)$ and so $3a=0 \pmod{10}$ and $3b=0\pmod{15}$. This implies $a=0$ and $b=0,5,10$. So $(a,b) = (0,0)$ or $(0,5)$ or $(0,10)$. So $G$ has two elements $(0,5)$ and $(0,10)$ of order $3$. It is *False*.<br>
(c) We can compute the elements as above process too. However, we know that $o(a,b) = {\rm lcm}(o(a),o(b)$. So if $o(a,b) = 5$, then $o(a) = 5$ in $\mathbb Z_{10}$ or $o(b) =5$ in $\mathbb Z_{15}$. The possibilities are $(o(a),o(b)) = (5,1) + (1,5) + (5,5)$. Therefore the number of such elements are $4+4+16=24$ (such possibilities).
(d) $o(a,b) = 10 = {\rm lcm}(o(a),o(b))$. But $o(b)$ cannot be $10$ or $2$ since $o(b) \mid 15$. So the possibilities of $a$ and $b$ are $o(a)=1,2,5,10$ and $o(b) = 1,5$ which give ${\rm lcm} = 10$ are listed below.<br>

-- $a$ has order $10$ and $b$ has order $1$. The possibilities are $a=1,3,5,7$ and $b=0$. So, total $4$ possibilities in this case.<br>
-- $a$ has order $2$ and $b$ has order $5$. The possibilities are $a=5$ and $b= 3,6,9,12$. Total $4$ possibilities in this case.<br>
-- $a$ has order $10$ and $b$ has order $5$. The possibilities are $a=1,3,5,7$, $b=3,6,7,9$. Total $16$ possibilities.<br>

Hence, there are total $4+4+16 = 24$ such elements.