---
layout: page
title: NET FEB 2022 (B)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET FEB 2022 (B):**  -->

Let $S = \{n : 1\le n \le 999;\ 3 \mid n \text{ or } 37 \mid n\}$. How many integers are there in the set $S^c = \{n : 1 \le n \le 999;\ n\not\in S\}$?

(a) $639$<br>
(b) $648$<br>
(c) $666$<br>
(d) $909$<br>

**Solution**

Let $M$ and $N$ be the set of all integers from $1$ to $999$ which are
divisible by $3$ and $37$ respectively. Then $M=\{3, 6,\ldots,999\}$,
$N=\{37, 74,\ldots,999\}$ and $|M| = \frac{999}{3}=333$,
$|N| = \frac{999}{37}=27$.<br>

If an integer is divisible by both $3$ and $37$, then it is divisible by
$3 \times 37 = 111$. Number of such integers between $1$ and $999$ are
$|M\cap N| = \frac{999}{111} = 9.$<br>

Here $S = M \cup N$. So,

$$|S| = |M \cup N| = |M| + |N| - |M \cap N| = 333 + 27 - 9 = 360 - 9 = 351.$$ 

Then
$|S^c| = 999-351 = 648$.


