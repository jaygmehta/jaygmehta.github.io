---
layout: page
title: NET-JUNE-2015-B-2-2
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

How many elements does the set $\{z \in \mathbb C \mid z^{60}= -1, \ z^k \neq -1 \text{ for } 0 < k <60\}$ have?

(a) $24$<br>
(b) $30$<br>
(c) $32$<br>
(d) $45$<br>

**Solution**

Note that
$$\{z \in \mathbb C \mid z^{60}= -1, \ z^k \neq -1 \text{ for } 0 < k <60\} = \{z \in \mathbb C \mid z^{120}= 1, \ z^k \neq 1 \text{ for } 0 < k <120\}.$$
The later is a cyclic group of $120$-th roots of unity whose order is $120$ and the condition $z^{120}= 1, \ z^k \neq 1 \text{ for } 0 < k <120$ implies that $z$ is generator of the group (i.e. $o(z)=120$). \\
We know that number of generators of a cyclic group of order $120$ is 
$$\phi(120) = \phi(2^3 \cdot 3 \cdot 5) = \phi(8) \phi(3) \phi(5) = 4 \times 2 \times 4 = 32.$$