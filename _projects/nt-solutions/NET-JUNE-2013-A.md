---
layout: page
title: NET JUNE 2013 (A)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET JUNE 2013 (A):**  -->

What is the last digit of $7^{73}$?

(a) $7$.<br>
(b) $9$.<br>
(c) $3$.<br>
(d) $1$.<br>

**Solution**

To obtain the last digit of a number, we need to compute the remainder
obtained by dividing the number by $10$.<br>

By Euler's theorem, if $a$ is relatively prime to $n$, then
$a^{\phi(n)}\equiv 1 \pmod n$. Here $a=7$ and $n=10$. Since $(7,10)=1$
and $\phi(10)=4$, we have
 
$$\begin{align*}
& 7^4 &\equiv &\ 1 \pmod {10}\\
\Rightarrow & {(7^4)}^{18} &\equiv &\ 1^{18} \pmod {10}\\
\Rightarrow & 7 \cdot 7^{72}=7^{73} &\equiv &\ 7\cdot 1 =7 \pmod {10}.
\end{align*}$$


