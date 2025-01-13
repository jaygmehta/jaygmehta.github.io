---
layout: page
title: NET 30 NOV 2020 (B)
# description: another without an image
# img:
# importance: 3
#category: fun
---
<!-- # **NET 30 NOV 2020 (B):**  -->

The last two digits of $3^{2019}$ are

(a) $27$<br>
(b) $37$<br>
(c) $57$<br>
(d) $67$<br>

**Solution**

To obtain last two digits of a number, we need to compute the remainder
obtained by dividing the number by $100$.<br>

By Euler's theorem, if $a$ is relatively prime to $n$, then
$a^{\phi(n)}\equiv 1 \pmod n$. Here $a=3$ and $n=100$. Since $(3,100)=1$
and $\phi(100)=\phi(4)\phi(25)=2 \times 20 = 40$, we have

$$\begin{align*}
& 3^{40} &\equiv &\ 1 \pmod {100}\\
\Rightarrow & {(3^{40})}^{50} &\equiv &\ 1^{50} \pmod {100}\\
\Rightarrow & 3^{19} \cdot 3^{2000} &\equiv &\ 3^{19} \pmod {100}.
\end{align*}$$

Note that $3^{4} \equiv 81 \equiv -19 \pmod{100}$.
Therefore, $3^{8} \equiv (-19)^2 361 \equiv 61 \pmod{100}$. Then
$3^{16} \equiv (61)^2 \equiv 3721 \equiv 21 \pmod{100}$. Finally,
$$3^{19} \equiv 3^3 \cdot 3^{16} \equiv 27 \cdot 21 = 567 \equiv 67 \pmod{100}.$$
Thus, last two digits (i.e. the remainder) is $67$.


