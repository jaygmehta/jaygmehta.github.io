---
layout: page
title: NET FEB 2022 (C)
# description: another without an image
# img:
# importance: 3
---
# **NET FEB 2022 (C): 1 of 3** 

Let $p$ be a prime and $N_p$ be the number of
pairs of positive integers $(x,y)$ such that such that
$\frac{1}{x} + \frac{1}{y} = \frac{1}{p^4}$. Which among the following
are possible values of $N_p$?

(a) $0$<br>
(b) $4$<br>
(c) $5$<br>
(d) $9$<br>

**Solution**

$$\begin{align*}
\frac{1}{x} + \frac{1}{y} = \frac{1}{p^4} \Rightarrow &\ \frac{x+y}{xy} = \frac{1}{p^4}\\
\Rightarrow &\ p^4(x+y) = xy\\
\Rightarrow &\ xy - x p^4 - yp^4  = 0\\
\Rightarrow &\ x(y - p^4) - yp^4 -p^8  = p^8\\
\Rightarrow &\ x(y - p^4) - p^4(y -p^4)  = p^8\\
\Rightarrow &\ (x-p^4)(y - p^4) = p^8\\
\Rightarrow &\ ab = p^8 & & (\text{where } a =(x-p^4),\ b =(y - p^4))
\end{align*}$$

Then we have the following possibilities as factors of
$p^8$: $a = p^i, b = p^j$, where $0 \le i, j \le 8$ and $i+j = 8$. The
following are the possibilities. 

$$\begin{align*}
a = 0, b = p^8 \Rightarrow &\ (x,y) = (1+p^4, p^4+p^8)\\
a = p, b = p^7 \Rightarrow &\ (x,y) = (p+p^4, p^4+p^7)\\
a = p^2, b = p^6 \Rightarrow &\ (x,y) = (p^2+p^4, p^4+p^6)\\
a = p^3, b = p^5 \Rightarrow &\ (x,y) = (p^3+p^4, p^4+p^5)\\
a = p^4, b = p^4 \Rightarrow &\ (x,y) = (p^4+p^4, p^4+p^4) = (2p^4,2p^4)\\
a = p^5, b = p^3 \Rightarrow &\ (x,y) = (p^5+p^4, p^4+p^3)\\
a = p^6, b = p^2 \Rightarrow &\ (x,y) = (p^6+p^4, p^4+p^2)\\
a = p^7, b = p \Rightarrow &\ (x,y) = (p^7+p^4, p^4+p)\\
a = p^8, b = 1 \Rightarrow &\ (x,y) = (p^8+p^4, p^4+1)
\end{align*}$$

Thus, there are $5$ distinct pairs but since number of
positive integers are asked, I am going with $9$.


