---
layout: page
title: NET JUNE 2017 (B)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET JUNE 2017 (B): 2 of 2**  -->

The remainder obtained when $16^{2016}$ is
divided by $9$ equals

(a) $1$.<br>
(b) $2$.<br>
(c) $3$.<br>
(d) $7$.<br>

**Solution**

By Euler's theorem, if $a$ is relatively prime to $n$, then
$a^{\phi(n)}\equiv 1 \pmod n$. Here $a=16$ and $n=9$. Since $(16,9)=1$
and $\phi(9)=6$, we have 

$$\begin{align*}
& {16}^6 &\equiv &\ 1 \pmod 9\\
\Rightarrow & {({16}^6)}^{336} &\equiv &\ 1^{336} \pmod 9\\
\Rightarrow & {16}^{2016} &\equiv &\ 1 \pmod 9.
\end{align*}$$


