---
layout: page
title: NET 26 NOV 2020 (C)
# description: another without an image
# img:
# importance: 3
---
<!-- # **NET 26 NOV 2020 (C):**  -->

Let $p$ be an odd prime such that $p \equiv 2 \pmod 3$. Let $\mathbb F_p$ be the field with $p$ elements. Consider the subset $E$ of $\mathbb F_p \times \mathbb F_p$ given by $E =\\{(x,y) \in \mathbb F_p \times \mathbb F_p : y^2 = x^3 + 1\\}$. Which of the following are true?<br>

(a) $E$ has at least two elements<br>
(b) $E$ has at most $2p$ elements<br>
(c) $E$ can have $p^2$ elements<br>
(d) $E$ has at least $2p$ elements<br>

**Solution**

For $x = 0$, we have $y^2 = 1$ and so $y = \pm 1 \equiv 1, p-1 \pmod p$. Thus, $(0,1)$ and $(0,p-1)$ belong to $E$. Hence, $E$ has at least two elements. Thus, **first** option is **correct**.<br>

Since $x \in \mathbb F_p$, there are $p$ at most different possible values of $x$ and so $x^3+1$. But $y^2 = x^3+1$. So even if every value of $x^3+1$ gives two different square roots, then there are at most $2p$ different possible values of $y$ and hence of the points $(x,y)$. Thus, the **second** option is also **correct** and so the **third and fourth options are incorrect**.<br>


