---
layout: page
title: NET-DEC-2012-B
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET DEC 2016 (B): 1 of 2**  -->

The last two digits of $7^{81}$ are 

(a) $07$<br>
(b) $17$<br>
(c) $37$<br>
(d) $47$<br>

**Solution**

To obtain last two digits of a number, we need to compute the remainder obtained by dividing the number by $100$.\\
By Euler's theorem, if $a$ is relatively prime to $n$, then $a^{\phi(n)}\equiv 1 \pmod n$. Here $a=3$ and $n=100$. Since $(7,100)=1$ and $\phi(100)=\phi(4)\phi(25)=2 \times 20 = 40$, we have
$$\begin{aligned}
& 7^{40} &\equiv &\ 1 \pmod {100}\\
\Rightarrow & {(7^40)}^{2} &\equiv &\ 1^{2} \pmod {100}\\
\Rightarrow & 7 \cdot 7^{80} = 7^{81} &\equiv &\ 7 \cdot 1= 7 \pmod {100}.
\end{aligned}$$
Thus, last two digits (i.e. the remainder) is $07$. 