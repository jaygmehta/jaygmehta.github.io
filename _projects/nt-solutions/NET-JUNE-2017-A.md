---
layout: page
title: NET JUNE 2017 (A)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET JUNE 2017 (A):**  -->
What is the remainder when $3^{256}$ is divided
by $5$?

(a) $1$.<br>
(b) $2$.<br>
(c) $3$.<br>
(d) $4$.<br>

**Solution**

By Euler's theorem, if $a$ is relatively prime to $n$, then
$a^{\phi(n)}\equiv 1 \pmod n$. Here $a=3$ and $n=5$. Since $(3,5)=1$ and
$\phi(5)=4$, we have 

$$\begin{align*}
& 3^4 &\equiv &\ 1 \pmod 5\\
\Rightarrow & {(3^4)}^{64} &\equiv &\ 1^{64} \pmod 5\\
\Rightarrow & 3^{256} &\equiv &\ 1 \pmod 5.
\end{align*}$$


